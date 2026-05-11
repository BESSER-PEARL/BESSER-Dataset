import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    type::qualifier::list::linha,
    ansic::TypeQualifierListLinhaAtion,
    declaration::list::linha,
    ansic::DeclarationListLinhaAction,
    struct::declarator::list::linha,
    ansic::StructDeclaratorListLinhaAction,
    struct::declaration::list::linha,
    ansic::StructDeclarationListLinhaAction,
    struct::or::union::specifier::complement,
    ansic::StructOrUnionSpecifierComplementAction,
    enumerator::list::linha,
    ansic::EnumeratorListLinhaAction,
    ansic::init::declarator,
    ansic::expression::linha,
    postfix::expression,
    ansic::conditional::expression::linha,
    ansic::logical::or::expression::linha,
    ansic::logical::or::expression,
    ansic::logical::and::expression::linha,
    ansic::logical::and::expression,
    ansic::inclusive::or::expression::linha,
    ansic::inclusive::or::expression,
    ansic::exclusive::or::expression::linha,
    ansic::exclusive::or::expression,
    ansic::and::expression::linha,
    ansic::and::expression,
    ansic::jump::statement,
    ansic::iteration::statement,
    ansic::block::item::list::linha,
    ansic::block::item,
    ansic::block::item::list,
    ansic::additive::expression::complement,
    ansic::additive::expression::linha,
    ansic::selection::statement,
    ansic::expression::statement,
    ansic::labeled::statement,
    ansic::statement,
    ansic::equality::expression::complement,
    ansic::equality::expression::linha,
    ansic::equality::expression,
    ansic::relational::expression::complement,
    ansic::relational::expression::linha,
    ansic::relational::expression,
    ansic::shift::expression::complement,
    ansic::shift::expression::linha,
    ansic::shift::expression,
    ansic::designator::list::linha,
    ansic::designator,
    ansic::designator::list,
    ansic::additive::expression,
    ansic::multiplicative::expression::complement,
    ansic::multiplicative::expression::linha,
    ansic::multiplicative::expression,
    ansic::cast::expression,
    ansic::unary::expression,
    ansic::argument::expression::list::linha,
    ansic::argument::expression::list,
    ansic::postfix::expression::complement,
    ansic::conditional::expression,
    ansic::primary::expression,
    ansic::identifier::list::linha,
    ansic::initializer::list::complement,
    ansic::initializer::list::linha,
    ansic::init::declarator::list::linha,
    ansic::designation,
    ansic::postfix::expression::linha,
    ansic::postfix::expression,
    ansic::generic::assoc::list::linha,
    ansic::generic::association,
    ansic::generic::assoc::list,
    ansic::generic::selection,
    ansic::expression,
    ansic::constant,
    ansic::parameter::type::list,
    ansic::assignment::expression,
    ansic::direct::abstract::declarator::complement,
    ansic::initializer::list,
    ansic::initializer,
    ansic::direct::abstract::declarator::linha,
    ansic::direct::abstract::declarator,
    ansic::abstract::declarator,
    ansic::parameter::list::linha,
    ansic::parameter::declaration,
    ansic::parameter::lista,
    ansic::identifier::list,
    ansic::direct::declarator::complemento,
    ansic::direct::declarator::linha,
    ansic::type::qualifier::list::linha,
    direct::abstract::declarator::complement,
    ansic::type::qualifier::list,
    ansic::direct::declarator,
    ansic::pointer,
    ansic::declaration::list::linha,
    ansic::compound::statement,
    ansic::declaration::list,
    ansic::init::declarator::list,
    ansic::struct::declaration::list,
    ansic::declarator,
    ansic::struct::declarator::list::linha,
    ansic::struct::declarator,
    ansic::static::assert::declaration,
    ansic::struct::declarator::list,
    ansic::specifier::qualifier::list,
    ansic::struct::declaration::list::linha,
    ansic::struct::declaration,
    translation::unit::linha,
    ansic::TranlationUnitLinhaAction,
    init::declarator::list::linha,
    ansic::InitDecclaratorListLinhaAction,
    unary::expression,
    ansic::PlusPlus,
    argument::expression::list::linha,
    ansic::ArgumentExpressionListLinhaAction,
    postfix::expression::complement,
    ansic::PostFixEmpryParams,
    designator::list::linha,
    ansic::DesignatorListLinhaAction,
    initializer::list::linha,
    ansic::InitializerListLinhaAction,
    postfix::expression::linha,
    ansic::PostfixExpressionLinhaAction,
    generic::assoc::list::linha,
    ansic::GenericAssocListLinhaAction,
    ansic::string::ufcg,
    identifier::list::linha,
    ansic::IdentifierListLinhaAction,
    direct::abstract::declarator::linha,
    ansic::DirectAbstractDeclarratorLinhaAction,
    ansic::struct::or::union::specifier::complement,
    ansic::declaration,
    ansic::function::definition,
    ansic::translation::unit::linha,
    ansic::enumeration::constant,
    ansic::enumerator::list::linha,
    ansic::enumerator,
    ansic::enumerator::list,
    ansic::enum::specifier,
    ansic::struct::or::union::specifier,
    ansic::atomic::type::specifier,
    ansic::constant::expression,
    ansic::type::name,
    ansic::alignment::specifier,
    ansic::type::qualifier,
    ansic::type::specifier,
    ansic::declaration::specifiers,
    ansic::external::declaration,
    ansic::translation::unit,
    ansic::DomainModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_type::qualifier::list::linha_is_not_abstract():
    assert not inspect.isabstract(type::qualifier::list::linha)


def test_type::qualifier::list::linha_constructor_exists():
    assert callable(type::qualifier::list::linha.__init__)


def test_type::qualifier::list::linha_constructor_args():
    sig = inspect.signature(type::qualifier::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::typequalifierlistlinhaation_is_not_abstract():
    assert not inspect.isabstract(ansic::TypeQualifierListLinhaAtion)


def test_ansic::typequalifierlistlinhaation_constructor_exists():
    assert callable(ansic::TypeQualifierListLinhaAtion.__init__)


def test_ansic::typequalifierlistlinhaation_constructor_args():
    sig = inspect.signature(ansic::TypeQualifierListLinhaAtion.__init__)
    params = list(sig.parameters.keys())



def test_declaration::list::linha_is_not_abstract():
    assert not inspect.isabstract(declaration::list::linha)


def test_declaration::list::linha_constructor_exists():
    assert callable(declaration::list::linha.__init__)


def test_declaration::list::linha_constructor_args():
    sig = inspect.signature(declaration::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::declarationlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic::DeclarationListLinhaAction)


def test_ansic::declarationlistlinhaaction_constructor_exists():
    assert callable(ansic::DeclarationListLinhaAction.__init__)


def test_ansic::declarationlistlinhaaction_constructor_args():
    sig = inspect.signature(ansic::DeclarationListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_struct::declarator::list::linha_is_not_abstract():
    assert not inspect.isabstract(struct::declarator::list::linha)


def test_struct::declarator::list::linha_constructor_exists():
    assert callable(struct::declarator::list::linha.__init__)


def test_struct::declarator::list::linha_constructor_args():
    sig = inspect.signature(struct::declarator::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::structdeclaratorlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic::StructDeclaratorListLinhaAction)


def test_ansic::structdeclaratorlistlinhaaction_constructor_exists():
    assert callable(ansic::StructDeclaratorListLinhaAction.__init__)


def test_ansic::structdeclaratorlistlinhaaction_constructor_args():
    sig = inspect.signature(ansic::StructDeclaratorListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_struct::declaration::list::linha_is_not_abstract():
    assert not inspect.isabstract(struct::declaration::list::linha)


def test_struct::declaration::list::linha_constructor_exists():
    assert callable(struct::declaration::list::linha.__init__)


def test_struct::declaration::list::linha_constructor_args():
    sig = inspect.signature(struct::declaration::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::structdeclarationlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic::StructDeclarationListLinhaAction)


def test_ansic::structdeclarationlistlinhaaction_constructor_exists():
    assert callable(ansic::StructDeclarationListLinhaAction.__init__)


def test_ansic::structdeclarationlistlinhaaction_constructor_args():
    sig = inspect.signature(ansic::StructDeclarationListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_struct::or::union::specifier::complement_is_not_abstract():
    assert not inspect.isabstract(struct::or::union::specifier::complement)


def test_struct::or::union::specifier::complement_constructor_exists():
    assert callable(struct::or::union::specifier::complement.__init__)


def test_struct::or::union::specifier::complement_constructor_args():
    sig = inspect.signature(struct::or::union::specifier::complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic::structorunionspecifiercomplementaction_is_not_abstract():
    assert not inspect.isabstract(ansic::StructOrUnionSpecifierComplementAction)


def test_ansic::structorunionspecifiercomplementaction_constructor_exists():
    assert callable(ansic::StructOrUnionSpecifierComplementAction.__init__)


def test_ansic::structorunionspecifiercomplementaction_constructor_args():
    sig = inspect.signature(ansic::StructOrUnionSpecifierComplementAction.__init__)
    params = list(sig.parameters.keys())



def test_enumerator::list::linha_is_not_abstract():
    assert not inspect.isabstract(enumerator::list::linha)


def test_enumerator::list::linha_constructor_exists():
    assert callable(enumerator::list::linha.__init__)


def test_enumerator::list::linha_constructor_args():
    sig = inspect.signature(enumerator::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::enumeratorlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic::EnumeratorListLinhaAction)


def test_ansic::enumeratorlistlinhaaction_constructor_exists():
    assert callable(ansic::EnumeratorListLinhaAction.__init__)


def test_ansic::enumeratorlistlinhaaction_constructor_args():
    sig = inspect.signature(ansic::EnumeratorListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_ansic::init::declarator_is_not_abstract():
    assert not inspect.isabstract(ansic::init::declarator)


def test_ansic::init::declarator_constructor_exists():
    assert callable(ansic::init::declarator.__init__)


def test_ansic::init::declarator_constructor_args():
    sig = inspect.signature(ansic::init::declarator.__init__)
    params = list(sig.parameters.keys())



def test_ansic::expression::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::expression::linha)


def test_ansic::expression::linha_constructor_exists():
    assert callable(ansic::expression::linha.__init__)


def test_ansic::expression::linha_constructor_args():
    sig = inspect.signature(ansic::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_postfix::expression_is_not_abstract():
    assert not inspect.isabstract(postfix::expression)


def test_postfix::expression_constructor_exists():
    assert callable(postfix::expression.__init__)


def test_postfix::expression_constructor_args():
    sig = inspect.signature(postfix::expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic::conditional::expression::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::conditional::expression::linha)


def test_ansic::conditional::expression::linha_constructor_exists():
    assert callable(ansic::conditional::expression::linha.__init__)


def test_ansic::conditional::expression::linha_constructor_args():
    sig = inspect.signature(ansic::conditional::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::logical::or::expression::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::logical::or::expression::linha)


def test_ansic::logical::or::expression::linha_constructor_exists():
    assert callable(ansic::logical::or::expression::linha.__init__)


def test_ansic::logical::or::expression::linha_constructor_args():
    sig = inspect.signature(ansic::logical::or::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::logical::or::expression_is_not_abstract():
    assert not inspect.isabstract(ansic::logical::or::expression)


def test_ansic::logical::or::expression_constructor_exists():
    assert callable(ansic::logical::or::expression.__init__)


def test_ansic::logical::or::expression_constructor_args():
    sig = inspect.signature(ansic::logical::or::expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic::logical::and::expression::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::logical::and::expression::linha)


def test_ansic::logical::and::expression::linha_constructor_exists():
    assert callable(ansic::logical::and::expression::linha.__init__)


def test_ansic::logical::and::expression::linha_constructor_args():
    sig = inspect.signature(ansic::logical::and::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::logical::and::expression_is_not_abstract():
    assert not inspect.isabstract(ansic::logical::and::expression)


def test_ansic::logical::and::expression_constructor_exists():
    assert callable(ansic::logical::and::expression.__init__)


def test_ansic::logical::and::expression_constructor_args():
    sig = inspect.signature(ansic::logical::and::expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic::inclusive::or::expression::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::inclusive::or::expression::linha)


def test_ansic::inclusive::or::expression::linha_constructor_exists():
    assert callable(ansic::inclusive::or::expression::linha.__init__)


def test_ansic::inclusive::or::expression::linha_constructor_args():
    sig = inspect.signature(ansic::inclusive::or::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::inclusive::or::expression_is_not_abstract():
    assert not inspect.isabstract(ansic::inclusive::or::expression)


def test_ansic::inclusive::or::expression_constructor_exists():
    assert callable(ansic::inclusive::or::expression.__init__)


def test_ansic::inclusive::or::expression_constructor_args():
    sig = inspect.signature(ansic::inclusive::or::expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic::exclusive::or::expression::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::exclusive::or::expression::linha)


def test_ansic::exclusive::or::expression::linha_constructor_exists():
    assert callable(ansic::exclusive::or::expression::linha.__init__)


def test_ansic::exclusive::or::expression::linha_constructor_args():
    sig = inspect.signature(ansic::exclusive::or::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::exclusive::or::expression_is_not_abstract():
    assert not inspect.isabstract(ansic::exclusive::or::expression)


def test_ansic::exclusive::or::expression_constructor_exists():
    assert callable(ansic::exclusive::or::expression.__init__)


def test_ansic::exclusive::or::expression_constructor_args():
    sig = inspect.signature(ansic::exclusive::or::expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic::and::expression::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::and::expression::linha)


def test_ansic::and::expression::linha_constructor_exists():
    assert callable(ansic::and::expression::linha.__init__)


def test_ansic::and::expression::linha_constructor_args():
    sig = inspect.signature(ansic::and::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::and::expression_is_not_abstract():
    assert not inspect.isabstract(ansic::and::expression)


def test_ansic::and::expression_constructor_exists():
    assert callable(ansic::and::expression.__init__)


def test_ansic::and::expression_constructor_args():
    sig = inspect.signature(ansic::and::expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic::jump::statement_is_not_abstract():
    assert not inspect.isabstract(ansic::jump::statement)


def test_ansic::jump::statement_constructor_exists():
    assert callable(ansic::jump::statement.__init__)


def test_ansic::jump::statement_constructor_args():
    sig = inspect.signature(ansic::jump::statement.__init__)
    params = list(sig.parameters.keys())
    assert "return_vazio" in params, "Missing parameter 'return_vazio'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "break_" in params, "Missing parameter 'break_'"
    assert "return_" in params, "Missing parameter 'return_'"

def test_ansic::jump::statement_has_return_vazio():
    assert hasattr(ansic::jump::statement, "return_vazio")
    descriptor = None
    for klass in ansic::jump::statement.__mro__:
        if "return_vazio" in klass.__dict__:
            descriptor = klass.__dict__["return_vazio"]
            break
    assert isinstance(descriptor, property)

def test_ansic::jump::statement_has_identifier():
    assert hasattr(ansic::jump::statement, "identifier")
    descriptor = None
    for klass in ansic::jump::statement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_ansic::jump::statement_has_break_():
    assert hasattr(ansic::jump::statement, "break_")
    descriptor = None
    for klass in ansic::jump::statement.__mro__:
        if "break_" in klass.__dict__:
            descriptor = klass.__dict__["break_"]
            break
    assert isinstance(descriptor, property)

def test_ansic::jump::statement_has_return_():
    assert hasattr(ansic::jump::statement, "return_")
    descriptor = None
    for klass in ansic::jump::statement.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
            break
    assert isinstance(descriptor, property)



def test_ansic::iteration::statement_is_not_abstract():
    assert not inspect.isabstract(ansic::iteration::statement)


def test_ansic::iteration::statement_constructor_exists():
    assert callable(ansic::iteration::statement.__init__)


def test_ansic::iteration::statement_constructor_args():
    sig = inspect.signature(ansic::iteration::statement.__init__)
    params = list(sig.parameters.keys())



def test_ansic::block::item::list::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::block::item::list::linha)


def test_ansic::block::item::list::linha_constructor_exists():
    assert callable(ansic::block::item::list::linha.__init__)


def test_ansic::block::item::list::linha_constructor_args():
    sig = inspect.signature(ansic::block::item::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::block::item_is_not_abstract():
    assert not inspect.isabstract(ansic::block::item)


def test_ansic::block::item_constructor_exists():
    assert callable(ansic::block::item.__init__)


def test_ansic::block::item_constructor_args():
    sig = inspect.signature(ansic::block::item.__init__)
    params = list(sig.parameters.keys())



def test_ansic::block::item::list_is_not_abstract():
    assert not inspect.isabstract(ansic::block::item::list)


def test_ansic::block::item::list_constructor_exists():
    assert callable(ansic::block::item::list.__init__)


def test_ansic::block::item::list_constructor_args():
    sig = inspect.signature(ansic::block::item::list.__init__)
    params = list(sig.parameters.keys())



def test_ansic::additive::expression::complement_is_not_abstract():
    assert not inspect.isabstract(ansic::additive::expression::complement)


def test_ansic::additive::expression::complement_constructor_exists():
    assert callable(ansic::additive::expression::complement.__init__)


def test_ansic::additive::expression::complement_constructor_args():
    sig = inspect.signature(ansic::additive::expression::complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic::additive::expression::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::additive::expression::linha)


def test_ansic::additive::expression::linha_constructor_exists():
    assert callable(ansic::additive::expression::linha.__init__)


def test_ansic::additive::expression::linha_constructor_args():
    sig = inspect.signature(ansic::additive::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::selection::statement_is_not_abstract():
    assert not inspect.isabstract(ansic::selection::statement)


def test_ansic::selection::statement_constructor_exists():
    assert callable(ansic::selection::statement.__init__)


def test_ansic::selection::statement_constructor_args():
    sig = inspect.signature(ansic::selection::statement.__init__)
    params = list(sig.parameters.keys())



def test_ansic::expression::statement_is_not_abstract():
    assert not inspect.isabstract(ansic::expression::statement)


def test_ansic::expression::statement_constructor_exists():
    assert callable(ansic::expression::statement.__init__)


def test_ansic::expression::statement_constructor_args():
    sig = inspect.signature(ansic::expression::statement.__init__)
    params = list(sig.parameters.keys())



def test_ansic::labeled::statement_is_not_abstract():
    assert not inspect.isabstract(ansic::labeled::statement)


def test_ansic::labeled::statement_constructor_exists():
    assert callable(ansic::labeled::statement.__init__)


def test_ansic::labeled::statement_constructor_args():
    sig = inspect.signature(ansic::labeled::statement.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic::labeled::statement_has_identifier():
    assert hasattr(ansic::labeled::statement, "identifier")
    descriptor = None
    for klass in ansic::labeled::statement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic::statement_is_not_abstract():
    assert not inspect.isabstract(ansic::statement)


def test_ansic::statement_constructor_exists():
    assert callable(ansic::statement.__init__)


def test_ansic::statement_constructor_args():
    sig = inspect.signature(ansic::statement.__init__)
    params = list(sig.parameters.keys())



def test_ansic::equality::expression::complement_is_not_abstract():
    assert not inspect.isabstract(ansic::equality::expression::complement)


def test_ansic::equality::expression::complement_constructor_exists():
    assert callable(ansic::equality::expression::complement.__init__)


def test_ansic::equality::expression::complement_constructor_args():
    sig = inspect.signature(ansic::equality::expression::complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic::equality::expression::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::equality::expression::linha)


def test_ansic::equality::expression::linha_constructor_exists():
    assert callable(ansic::equality::expression::linha.__init__)


def test_ansic::equality::expression::linha_constructor_args():
    sig = inspect.signature(ansic::equality::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::equality::expression_is_not_abstract():
    assert not inspect.isabstract(ansic::equality::expression)


def test_ansic::equality::expression_constructor_exists():
    assert callable(ansic::equality::expression.__init__)


def test_ansic::equality::expression_constructor_args():
    sig = inspect.signature(ansic::equality::expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic::relational::expression::complement_is_not_abstract():
    assert not inspect.isabstract(ansic::relational::expression::complement)


def test_ansic::relational::expression::complement_constructor_exists():
    assert callable(ansic::relational::expression::complement.__init__)


def test_ansic::relational::expression::complement_constructor_args():
    sig = inspect.signature(ansic::relational::expression::complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic::relational::expression::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::relational::expression::linha)


def test_ansic::relational::expression::linha_constructor_exists():
    assert callable(ansic::relational::expression::linha.__init__)


def test_ansic::relational::expression::linha_constructor_args():
    sig = inspect.signature(ansic::relational::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::relational::expression_is_not_abstract():
    assert not inspect.isabstract(ansic::relational::expression)


def test_ansic::relational::expression_constructor_exists():
    assert callable(ansic::relational::expression.__init__)


def test_ansic::relational::expression_constructor_args():
    sig = inspect.signature(ansic::relational::expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic::shift::expression::complement_is_not_abstract():
    assert not inspect.isabstract(ansic::shift::expression::complement)


def test_ansic::shift::expression::complement_constructor_exists():
    assert callable(ansic::shift::expression::complement.__init__)


def test_ansic::shift::expression::complement_constructor_args():
    sig = inspect.signature(ansic::shift::expression::complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic::shift::expression::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::shift::expression::linha)


def test_ansic::shift::expression::linha_constructor_exists():
    assert callable(ansic::shift::expression::linha.__init__)


def test_ansic::shift::expression::linha_constructor_args():
    sig = inspect.signature(ansic::shift::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::shift::expression_is_not_abstract():
    assert not inspect.isabstract(ansic::shift::expression)


def test_ansic::shift::expression_constructor_exists():
    assert callable(ansic::shift::expression.__init__)


def test_ansic::shift::expression_constructor_args():
    sig = inspect.signature(ansic::shift::expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic::designator::list::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::designator::list::linha)


def test_ansic::designator::list::linha_constructor_exists():
    assert callable(ansic::designator::list::linha.__init__)


def test_ansic::designator::list::linha_constructor_args():
    sig = inspect.signature(ansic::designator::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::designator_is_not_abstract():
    assert not inspect.isabstract(ansic::designator)


def test_ansic::designator_constructor_exists():
    assert callable(ansic::designator.__init__)


def test_ansic::designator_constructor_args():
    sig = inspect.signature(ansic::designator.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic::designator_has_identifier():
    assert hasattr(ansic::designator, "identifier")
    descriptor = None
    for klass in ansic::designator.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic::designator::list_is_not_abstract():
    assert not inspect.isabstract(ansic::designator::list)


def test_ansic::designator::list_constructor_exists():
    assert callable(ansic::designator::list.__init__)


def test_ansic::designator::list_constructor_args():
    sig = inspect.signature(ansic::designator::list.__init__)
    params = list(sig.parameters.keys())



def test_ansic::additive::expression_is_not_abstract():
    assert not inspect.isabstract(ansic::additive::expression)


def test_ansic::additive::expression_constructor_exists():
    assert callable(ansic::additive::expression.__init__)


def test_ansic::additive::expression_constructor_args():
    sig = inspect.signature(ansic::additive::expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic::multiplicative::expression::complement_is_not_abstract():
    assert not inspect.isabstract(ansic::multiplicative::expression::complement)


def test_ansic::multiplicative::expression::complement_constructor_exists():
    assert callable(ansic::multiplicative::expression::complement.__init__)


def test_ansic::multiplicative::expression::complement_constructor_args():
    sig = inspect.signature(ansic::multiplicative::expression::complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic::multiplicative::expression::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::multiplicative::expression::linha)


def test_ansic::multiplicative::expression::linha_constructor_exists():
    assert callable(ansic::multiplicative::expression::linha.__init__)


def test_ansic::multiplicative::expression::linha_constructor_args():
    sig = inspect.signature(ansic::multiplicative::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::multiplicative::expression_is_not_abstract():
    assert not inspect.isabstract(ansic::multiplicative::expression)


def test_ansic::multiplicative::expression_constructor_exists():
    assert callable(ansic::multiplicative::expression.__init__)


def test_ansic::multiplicative::expression_constructor_args():
    sig = inspect.signature(ansic::multiplicative::expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic::cast::expression_is_not_abstract():
    assert not inspect.isabstract(ansic::cast::expression)


def test_ansic::cast::expression_constructor_exists():
    assert callable(ansic::cast::expression.__init__)


def test_ansic::cast::expression_constructor_args():
    sig = inspect.signature(ansic::cast::expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic::unary::expression_is_not_abstract():
    assert not inspect.isabstract(ansic::unary::expression)


def test_ansic::unary::expression_constructor_exists():
    assert callable(ansic::unary::expression.__init__)


def test_ansic::unary::expression_constructor_args():
    sig = inspect.signature(ansic::unary::expression.__init__)
    params = list(sig.parameters.keys())
    assert "unary_operator" in params, "Missing parameter 'unary_operator'"

def test_ansic::unary::expression_has_unary_operator():
    assert hasattr(ansic::unary::expression, "unary_operator")
    descriptor = None
    for klass in ansic::unary::expression.__mro__:
        if "unary_operator" in klass.__dict__:
            descriptor = klass.__dict__["unary_operator"]
            break
    assert isinstance(descriptor, property)



def test_ansic::argument::expression::list::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::argument::expression::list::linha)


def test_ansic::argument::expression::list::linha_constructor_exists():
    assert callable(ansic::argument::expression::list::linha.__init__)


def test_ansic::argument::expression::list::linha_constructor_args():
    sig = inspect.signature(ansic::argument::expression::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::argument::expression::list_is_not_abstract():
    assert not inspect.isabstract(ansic::argument::expression::list)


def test_ansic::argument::expression::list_constructor_exists():
    assert callable(ansic::argument::expression::list.__init__)


def test_ansic::argument::expression::list_constructor_args():
    sig = inspect.signature(ansic::argument::expression::list.__init__)
    params = list(sig.parameters.keys())



def test_ansic::postfix::expression::complement_is_not_abstract():
    assert not inspect.isabstract(ansic::postfix::expression::complement)


def test_ansic::postfix::expression::complement_constructor_exists():
    assert callable(ansic::postfix::expression::complement.__init__)


def test_ansic::postfix::expression::complement_constructor_args():
    sig = inspect.signature(ansic::postfix::expression::complement.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic::postfix::expression::complement_has_identifier():
    assert hasattr(ansic::postfix::expression::complement, "identifier")
    descriptor = None
    for klass in ansic::postfix::expression::complement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic::conditional::expression_is_not_abstract():
    assert not inspect.isabstract(ansic::conditional::expression)


def test_ansic::conditional::expression_constructor_exists():
    assert callable(ansic::conditional::expression.__init__)


def test_ansic::conditional::expression_constructor_args():
    sig = inspect.signature(ansic::conditional::expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic::primary::expression_is_not_abstract():
    assert not inspect.isabstract(ansic::primary::expression)


def test_ansic::primary::expression_constructor_exists():
    assert callable(ansic::primary::expression.__init__)


def test_ansic::primary::expression_constructor_args():
    sig = inspect.signature(ansic::primary::expression.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic::primary::expression_has_identifier():
    assert hasattr(ansic::primary::expression, "identifier")
    descriptor = None
    for klass in ansic::primary::expression.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic::identifier::list::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::identifier::list::linha)


def test_ansic::identifier::list::linha_constructor_exists():
    assert callable(ansic::identifier::list::linha.__init__)


def test_ansic::identifier::list::linha_constructor_args():
    sig = inspect.signature(ansic::identifier::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::initializer::list::complement_is_not_abstract():
    assert not inspect.isabstract(ansic::initializer::list::complement)


def test_ansic::initializer::list::complement_constructor_exists():
    assert callable(ansic::initializer::list::complement.__init__)


def test_ansic::initializer::list::complement_constructor_args():
    sig = inspect.signature(ansic::initializer::list::complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic::initializer::list::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::initializer::list::linha)


def test_ansic::initializer::list::linha_constructor_exists():
    assert callable(ansic::initializer::list::linha.__init__)


def test_ansic::initializer::list::linha_constructor_args():
    sig = inspect.signature(ansic::initializer::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::init::declarator::list::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::init::declarator::list::linha)


def test_ansic::init::declarator::list::linha_constructor_exists():
    assert callable(ansic::init::declarator::list::linha.__init__)


def test_ansic::init::declarator::list::linha_constructor_args():
    sig = inspect.signature(ansic::init::declarator::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::designation_is_not_abstract():
    assert not inspect.isabstract(ansic::designation)


def test_ansic::designation_constructor_exists():
    assert callable(ansic::designation.__init__)


def test_ansic::designation_constructor_args():
    sig = inspect.signature(ansic::designation.__init__)
    params = list(sig.parameters.keys())



def test_ansic::postfix::expression::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::postfix::expression::linha)


def test_ansic::postfix::expression::linha_constructor_exists():
    assert callable(ansic::postfix::expression::linha.__init__)


def test_ansic::postfix::expression::linha_constructor_args():
    sig = inspect.signature(ansic::postfix::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::postfix::expression_is_not_abstract():
    assert not inspect.isabstract(ansic::postfix::expression)


def test_ansic::postfix::expression_constructor_exists():
    assert callable(ansic::postfix::expression.__init__)


def test_ansic::postfix::expression_constructor_args():
    sig = inspect.signature(ansic::postfix::expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic::generic::assoc::list::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::generic::assoc::list::linha)


def test_ansic::generic::assoc::list::linha_constructor_exists():
    assert callable(ansic::generic::assoc::list::linha.__init__)


def test_ansic::generic::assoc::list::linha_constructor_args():
    sig = inspect.signature(ansic::generic::assoc::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::generic::association_is_not_abstract():
    assert not inspect.isabstract(ansic::generic::association)


def test_ansic::generic::association_constructor_exists():
    assert callable(ansic::generic::association.__init__)


def test_ansic::generic::association_constructor_args():
    sig = inspect.signature(ansic::generic::association.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_ansic::generic::association_has_default():
    assert hasattr(ansic::generic::association, "default")
    descriptor = None
    for klass in ansic::generic::association.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_ansic::generic::assoc::list_is_not_abstract():
    assert not inspect.isabstract(ansic::generic::assoc::list)


def test_ansic::generic::assoc::list_constructor_exists():
    assert callable(ansic::generic::assoc::list.__init__)


def test_ansic::generic::assoc::list_constructor_args():
    sig = inspect.signature(ansic::generic::assoc::list.__init__)
    params = list(sig.parameters.keys())



def test_ansic::generic::selection_is_not_abstract():
    assert not inspect.isabstract(ansic::generic::selection)


def test_ansic::generic::selection_constructor_exists():
    assert callable(ansic::generic::selection.__init__)


def test_ansic::generic::selection_constructor_args():
    sig = inspect.signature(ansic::generic::selection.__init__)
    params = list(sig.parameters.keys())
    assert "_generic" in params, "Missing parameter '_generic'"

def test_ansic::generic::selection_has__generic():
    assert hasattr(ansic::generic::selection, "_generic")
    descriptor = None
    for klass in ansic::generic::selection.__mro__:
        if "_generic" in klass.__dict__:
            descriptor = klass.__dict__["_generic"]
            break
    assert isinstance(descriptor, property)



def test_ansic::expression_is_not_abstract():
    assert not inspect.isabstract(ansic::expression)


def test_ansic::expression_constructor_exists():
    assert callable(ansic::expression.__init__)


def test_ansic::expression_constructor_args():
    sig = inspect.signature(ansic::expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic::constant_is_not_abstract():
    assert not inspect.isabstract(ansic::constant)


def test_ansic::constant_constructor_exists():
    assert callable(ansic::constant.__init__)


def test_ansic::constant_constructor_args():
    sig = inspect.signature(ansic::constant.__init__)
    params = list(sig.parameters.keys())
    assert "char" in params, "Missing parameter 'char'"
    assert "enumz" in params, "Missing parameter 'enumz'"
    assert "f_constant" in params, "Missing parameter 'f_constant'"
    assert "i_constant" in params, "Missing parameter 'i_constant'"

def test_ansic::constant_has_char():
    assert hasattr(ansic::constant, "char")
    descriptor = None
    for klass in ansic::constant.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_ansic::constant_has_enumz():
    assert hasattr(ansic::constant, "enumz")
    descriptor = None
    for klass in ansic::constant.__mro__:
        if "enumz" in klass.__dict__:
            descriptor = klass.__dict__["enumz"]
            break
    assert isinstance(descriptor, property)

def test_ansic::constant_has_f_constant():
    assert hasattr(ansic::constant, "f_constant")
    descriptor = None
    for klass in ansic::constant.__mro__:
        if "f_constant" in klass.__dict__:
            descriptor = klass.__dict__["f_constant"]
            break
    assert isinstance(descriptor, property)

def test_ansic::constant_has_i_constant():
    assert hasattr(ansic::constant, "i_constant")
    descriptor = None
    for klass in ansic::constant.__mro__:
        if "i_constant" in klass.__dict__:
            descriptor = klass.__dict__["i_constant"]
            break
    assert isinstance(descriptor, property)



def test_ansic::parameter::type::list_is_not_abstract():
    assert not inspect.isabstract(ansic::parameter::type::list)


def test_ansic::parameter::type::list_constructor_exists():
    assert callable(ansic::parameter::type::list.__init__)


def test_ansic::parameter::type::list_constructor_args():
    sig = inspect.signature(ansic::parameter::type::list.__init__)
    params = list(sig.parameters.keys())



def test_ansic::assignment::expression_is_not_abstract():
    assert not inspect.isabstract(ansic::assignment::expression)


def test_ansic::assignment::expression_constructor_exists():
    assert callable(ansic::assignment::expression.__init__)


def test_ansic::assignment::expression_constructor_args():
    sig = inspect.signature(ansic::assignment::expression.__init__)
    params = list(sig.parameters.keys())
    assert "assignment_operator" in params, "Missing parameter 'assignment_operator'"

def test_ansic::assignment::expression_has_assignment_operator():
    assert hasattr(ansic::assignment::expression, "assignment_operator")
    descriptor = None
    for klass in ansic::assignment::expression.__mro__:
        if "assignment_operator" in klass.__dict__:
            descriptor = klass.__dict__["assignment_operator"]
            break
    assert isinstance(descriptor, property)



def test_ansic::direct::abstract::declarator::complement_is_not_abstract():
    assert not inspect.isabstract(ansic::direct::abstract::declarator::complement)


def test_ansic::direct::abstract::declarator::complement_constructor_exists():
    assert callable(ansic::direct::abstract::declarator::complement.__init__)


def test_ansic::direct::abstract::declarator::complement_constructor_args():
    sig = inspect.signature(ansic::direct::abstract::declarator::complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic::initializer::list_is_not_abstract():
    assert not inspect.isabstract(ansic::initializer::list)


def test_ansic::initializer::list_constructor_exists():
    assert callable(ansic::initializer::list.__init__)


def test_ansic::initializer::list_constructor_args():
    sig = inspect.signature(ansic::initializer::list.__init__)
    params = list(sig.parameters.keys())



def test_ansic::initializer_is_not_abstract():
    assert not inspect.isabstract(ansic::initializer)


def test_ansic::initializer_constructor_exists():
    assert callable(ansic::initializer.__init__)


def test_ansic::initializer_constructor_args():
    sig = inspect.signature(ansic::initializer.__init__)
    params = list(sig.parameters.keys())



def test_ansic::direct::abstract::declarator::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::direct::abstract::declarator::linha)


def test_ansic::direct::abstract::declarator::linha_constructor_exists():
    assert callable(ansic::direct::abstract::declarator::linha.__init__)


def test_ansic::direct::abstract::declarator::linha_constructor_args():
    sig = inspect.signature(ansic::direct::abstract::declarator::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::direct::abstract::declarator_is_not_abstract():
    assert not inspect.isabstract(ansic::direct::abstract::declarator)


def test_ansic::direct::abstract::declarator_constructor_exists():
    assert callable(ansic::direct::abstract::declarator.__init__)


def test_ansic::direct::abstract::declarator_constructor_args():
    sig = inspect.signature(ansic::direct::abstract::declarator.__init__)
    params = list(sig.parameters.keys())



def test_ansic::abstract::declarator_is_not_abstract():
    assert not inspect.isabstract(ansic::abstract::declarator)


def test_ansic::abstract::declarator_constructor_exists():
    assert callable(ansic::abstract::declarator.__init__)


def test_ansic::abstract::declarator_constructor_args():
    sig = inspect.signature(ansic::abstract::declarator.__init__)
    params = list(sig.parameters.keys())



def test_ansic::parameter::list::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::parameter::list::linha)


def test_ansic::parameter::list::linha_constructor_exists():
    assert callable(ansic::parameter::list::linha.__init__)


def test_ansic::parameter::list::linha_constructor_args():
    sig = inspect.signature(ansic::parameter::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::parameter::declaration_is_not_abstract():
    assert not inspect.isabstract(ansic::parameter::declaration)


def test_ansic::parameter::declaration_constructor_exists():
    assert callable(ansic::parameter::declaration.__init__)


def test_ansic::parameter::declaration_constructor_args():
    sig = inspect.signature(ansic::parameter::declaration.__init__)
    params = list(sig.parameters.keys())



def test_ansic::parameter::lista_is_not_abstract():
    assert not inspect.isabstract(ansic::parameter::lista)


def test_ansic::parameter::lista_constructor_exists():
    assert callable(ansic::parameter::lista.__init__)


def test_ansic::parameter::lista_constructor_args():
    sig = inspect.signature(ansic::parameter::lista.__init__)
    params = list(sig.parameters.keys())



def test_ansic::identifier::list_is_not_abstract():
    assert not inspect.isabstract(ansic::identifier::list)


def test_ansic::identifier::list_constructor_exists():
    assert callable(ansic::identifier::list.__init__)


def test_ansic::identifier::list_constructor_args():
    sig = inspect.signature(ansic::identifier::list.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic::identifier::list_has_identifier():
    assert hasattr(ansic::identifier::list, "identifier")
    descriptor = None
    for klass in ansic::identifier::list.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic::direct::declarator::complemento_is_not_abstract():
    assert not inspect.isabstract(ansic::direct::declarator::complemento)


def test_ansic::direct::declarator::complemento_constructor_exists():
    assert callable(ansic::direct::declarator::complemento.__init__)


def test_ansic::direct::declarator::complemento_constructor_args():
    sig = inspect.signature(ansic::direct::declarator::complemento.__init__)
    params = list(sig.parameters.keys())



def test_ansic::direct::declarator::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::direct::declarator::linha)


def test_ansic::direct::declarator::linha_constructor_exists():
    assert callable(ansic::direct::declarator::linha.__init__)


def test_ansic::direct::declarator::linha_constructor_args():
    sig = inspect.signature(ansic::direct::declarator::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::type::qualifier::list::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::type::qualifier::list::linha)


def test_ansic::type::qualifier::list::linha_constructor_exists():
    assert callable(ansic::type::qualifier::list::linha.__init__)


def test_ansic::type::qualifier::list::linha_constructor_args():
    sig = inspect.signature(ansic::type::qualifier::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_direct::abstract::declarator::complement_is_not_abstract():
    assert not inspect.isabstract(direct::abstract::declarator::complement)


def test_direct::abstract::declarator::complement_constructor_exists():
    assert callable(direct::abstract::declarator::complement.__init__)


def test_direct::abstract::declarator::complement_constructor_args():
    sig = inspect.signature(direct::abstract::declarator::complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic::type::qualifier::list_is_not_abstract():
    assert not inspect.isabstract(ansic::type::qualifier::list)


def test_ansic::type::qualifier::list_constructor_exists():
    assert callable(ansic::type::qualifier::list.__init__)


def test_ansic::type::qualifier::list_constructor_args():
    sig = inspect.signature(ansic::type::qualifier::list.__init__)
    params = list(sig.parameters.keys())



def test_ansic::direct::declarator_is_not_abstract():
    assert not inspect.isabstract(ansic::direct::declarator)


def test_ansic::direct::declarator_constructor_exists():
    assert callable(ansic::direct::declarator.__init__)


def test_ansic::direct::declarator_constructor_args():
    sig = inspect.signature(ansic::direct::declarator.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic::direct::declarator_has_identifier():
    assert hasattr(ansic::direct::declarator, "identifier")
    descriptor = None
    for klass in ansic::direct::declarator.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic::pointer_is_not_abstract():
    assert not inspect.isabstract(ansic::pointer)


def test_ansic::pointer_constructor_exists():
    assert callable(ansic::pointer.__init__)


def test_ansic::pointer_constructor_args():
    sig = inspect.signature(ansic::pointer.__init__)
    params = list(sig.parameters.keys())



def test_ansic::declaration::list::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::declaration::list::linha)


def test_ansic::declaration::list::linha_constructor_exists():
    assert callable(ansic::declaration::list::linha.__init__)


def test_ansic::declaration::list::linha_constructor_args():
    sig = inspect.signature(ansic::declaration::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::compound::statement_is_not_abstract():
    assert not inspect.isabstract(ansic::compound::statement)


def test_ansic::compound::statement_constructor_exists():
    assert callable(ansic::compound::statement.__init__)


def test_ansic::compound::statement_constructor_args():
    sig = inspect.signature(ansic::compound::statement.__init__)
    params = list(sig.parameters.keys())



def test_ansic::declaration::list_is_not_abstract():
    assert not inspect.isabstract(ansic::declaration::list)


def test_ansic::declaration::list_constructor_exists():
    assert callable(ansic::declaration::list.__init__)


def test_ansic::declaration::list_constructor_args():
    sig = inspect.signature(ansic::declaration::list.__init__)
    params = list(sig.parameters.keys())



def test_ansic::init::declarator::list_is_not_abstract():
    assert not inspect.isabstract(ansic::init::declarator::list)


def test_ansic::init::declarator::list_constructor_exists():
    assert callable(ansic::init::declarator::list.__init__)


def test_ansic::init::declarator::list_constructor_args():
    sig = inspect.signature(ansic::init::declarator::list.__init__)
    params = list(sig.parameters.keys())



def test_ansic::struct::declaration::list_is_not_abstract():
    assert not inspect.isabstract(ansic::struct::declaration::list)


def test_ansic::struct::declaration::list_constructor_exists():
    assert callable(ansic::struct::declaration::list.__init__)


def test_ansic::struct::declaration::list_constructor_args():
    sig = inspect.signature(ansic::struct::declaration::list.__init__)
    params = list(sig.parameters.keys())



def test_ansic::declarator_is_not_abstract():
    assert not inspect.isabstract(ansic::declarator)


def test_ansic::declarator_constructor_exists():
    assert callable(ansic::declarator.__init__)


def test_ansic::declarator_constructor_args():
    sig = inspect.signature(ansic::declarator.__init__)
    params = list(sig.parameters.keys())



def test_ansic::struct::declarator::list::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::struct::declarator::list::linha)


def test_ansic::struct::declarator::list::linha_constructor_exists():
    assert callable(ansic::struct::declarator::list::linha.__init__)


def test_ansic::struct::declarator::list::linha_constructor_args():
    sig = inspect.signature(ansic::struct::declarator::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::struct::declarator_is_not_abstract():
    assert not inspect.isabstract(ansic::struct::declarator)


def test_ansic::struct::declarator_constructor_exists():
    assert callable(ansic::struct::declarator.__init__)


def test_ansic::struct::declarator_constructor_args():
    sig = inspect.signature(ansic::struct::declarator.__init__)
    params = list(sig.parameters.keys())



def test_ansic::static::assert::declaration_is_not_abstract():
    assert not inspect.isabstract(ansic::static::assert::declaration)


def test_ansic::static::assert::declaration_constructor_exists():
    assert callable(ansic::static::assert::declaration.__init__)


def test_ansic::static::assert::declaration_constructor_args():
    sig = inspect.signature(ansic::static::assert::declaration.__init__)
    params = list(sig.parameters.keys())



def test_ansic::struct::declarator::list_is_not_abstract():
    assert not inspect.isabstract(ansic::struct::declarator::list)


def test_ansic::struct::declarator::list_constructor_exists():
    assert callable(ansic::struct::declarator::list.__init__)


def test_ansic::struct::declarator::list_constructor_args():
    sig = inspect.signature(ansic::struct::declarator::list.__init__)
    params = list(sig.parameters.keys())



def test_ansic::specifier::qualifier::list_is_not_abstract():
    assert not inspect.isabstract(ansic::specifier::qualifier::list)


def test_ansic::specifier::qualifier::list_constructor_exists():
    assert callable(ansic::specifier::qualifier::list.__init__)


def test_ansic::specifier::qualifier::list_constructor_args():
    sig = inspect.signature(ansic::specifier::qualifier::list.__init__)
    params = list(sig.parameters.keys())



def test_ansic::struct::declaration::list::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::struct::declaration::list::linha)


def test_ansic::struct::declaration::list::linha_constructor_exists():
    assert callable(ansic::struct::declaration::list::linha.__init__)


def test_ansic::struct::declaration::list::linha_constructor_args():
    sig = inspect.signature(ansic::struct::declaration::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::struct::declaration_is_not_abstract():
    assert not inspect.isabstract(ansic::struct::declaration)


def test_ansic::struct::declaration_constructor_exists():
    assert callable(ansic::struct::declaration.__init__)


def test_ansic::struct::declaration_constructor_args():
    sig = inspect.signature(ansic::struct::declaration.__init__)
    params = list(sig.parameters.keys())



def test_translation::unit::linha_is_not_abstract():
    assert not inspect.isabstract(translation::unit::linha)


def test_translation::unit::linha_constructor_exists():
    assert callable(translation::unit::linha.__init__)


def test_translation::unit::linha_constructor_args():
    sig = inspect.signature(translation::unit::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::tranlationunitlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic::TranlationUnitLinhaAction)


def test_ansic::tranlationunitlinhaaction_constructor_exists():
    assert callable(ansic::TranlationUnitLinhaAction.__init__)


def test_ansic::tranlationunitlinhaaction_constructor_args():
    sig = inspect.signature(ansic::TranlationUnitLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_init::declarator::list::linha_is_not_abstract():
    assert not inspect.isabstract(init::declarator::list::linha)


def test_init::declarator::list::linha_constructor_exists():
    assert callable(init::declarator::list::linha.__init__)


def test_init::declarator::list::linha_constructor_args():
    sig = inspect.signature(init::declarator::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::initdecclaratorlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic::InitDecclaratorListLinhaAction)


def test_ansic::initdecclaratorlistlinhaaction_constructor_exists():
    assert callable(ansic::InitDecclaratorListLinhaAction.__init__)


def test_ansic::initdecclaratorlistlinhaaction_constructor_args():
    sig = inspect.signature(ansic::InitDecclaratorListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_unary::expression_is_not_abstract():
    assert not inspect.isabstract(unary::expression)


def test_unary::expression_constructor_exists():
    assert callable(unary::expression.__init__)


def test_unary::expression_constructor_args():
    sig = inspect.signature(unary::expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic::plusplus_is_not_abstract():
    assert not inspect.isabstract(ansic::PlusPlus)


def test_ansic::plusplus_constructor_exists():
    assert callable(ansic::PlusPlus.__init__)


def test_ansic::plusplus_constructor_args():
    sig = inspect.signature(ansic::PlusPlus.__init__)
    params = list(sig.parameters.keys())
    assert "plus" in params, "Missing parameter 'plus'"

def test_ansic::plusplus_has_plus():
    assert hasattr(ansic::PlusPlus, "plus")
    descriptor = None
    for klass in ansic::PlusPlus.__mro__:
        if "plus" in klass.__dict__:
            descriptor = klass.__dict__["plus"]
            break
    assert isinstance(descriptor, property)



def test_argument::expression::list::linha_is_not_abstract():
    assert not inspect.isabstract(argument::expression::list::linha)


def test_argument::expression::list::linha_constructor_exists():
    assert callable(argument::expression::list::linha.__init__)


def test_argument::expression::list::linha_constructor_args():
    sig = inspect.signature(argument::expression::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::argumentexpressionlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic::ArgumentExpressionListLinhaAction)


def test_ansic::argumentexpressionlistlinhaaction_constructor_exists():
    assert callable(ansic::ArgumentExpressionListLinhaAction.__init__)


def test_ansic::argumentexpressionlistlinhaaction_constructor_args():
    sig = inspect.signature(ansic::ArgumentExpressionListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_postfix::expression::complement_is_not_abstract():
    assert not inspect.isabstract(postfix::expression::complement)


def test_postfix::expression::complement_constructor_exists():
    assert callable(postfix::expression::complement.__init__)


def test_postfix::expression::complement_constructor_args():
    sig = inspect.signature(postfix::expression::complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic::postfixempryparams_is_not_abstract():
    assert not inspect.isabstract(ansic::PostFixEmpryParams)


def test_ansic::postfixempryparams_constructor_exists():
    assert callable(ansic::PostFixEmpryParams.__init__)


def test_ansic::postfixempryparams_constructor_args():
    sig = inspect.signature(ansic::PostFixEmpryParams.__init__)
    params = list(sig.parameters.keys())



def test_designator::list::linha_is_not_abstract():
    assert not inspect.isabstract(designator::list::linha)


def test_designator::list::linha_constructor_exists():
    assert callable(designator::list::linha.__init__)


def test_designator::list::linha_constructor_args():
    sig = inspect.signature(designator::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::designatorlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic::DesignatorListLinhaAction)


def test_ansic::designatorlistlinhaaction_constructor_exists():
    assert callable(ansic::DesignatorListLinhaAction.__init__)


def test_ansic::designatorlistlinhaaction_constructor_args():
    sig = inspect.signature(ansic::DesignatorListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_initializer::list::linha_is_not_abstract():
    assert not inspect.isabstract(initializer::list::linha)


def test_initializer::list::linha_constructor_exists():
    assert callable(initializer::list::linha.__init__)


def test_initializer::list::linha_constructor_args():
    sig = inspect.signature(initializer::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::initializerlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic::InitializerListLinhaAction)


def test_ansic::initializerlistlinhaaction_constructor_exists():
    assert callable(ansic::InitializerListLinhaAction.__init__)


def test_ansic::initializerlistlinhaaction_constructor_args():
    sig = inspect.signature(ansic::InitializerListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_postfix::expression::linha_is_not_abstract():
    assert not inspect.isabstract(postfix::expression::linha)


def test_postfix::expression::linha_constructor_exists():
    assert callable(postfix::expression::linha.__init__)


def test_postfix::expression::linha_constructor_args():
    sig = inspect.signature(postfix::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::postfixexpressionlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic::PostfixExpressionLinhaAction)


def test_ansic::postfixexpressionlinhaaction_constructor_exists():
    assert callable(ansic::PostfixExpressionLinhaAction.__init__)


def test_ansic::postfixexpressionlinhaaction_constructor_args():
    sig = inspect.signature(ansic::PostfixExpressionLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_generic::assoc::list::linha_is_not_abstract():
    assert not inspect.isabstract(generic::assoc::list::linha)


def test_generic::assoc::list::linha_constructor_exists():
    assert callable(generic::assoc::list::linha.__init__)


def test_generic::assoc::list::linha_constructor_args():
    sig = inspect.signature(generic::assoc::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::genericassoclistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic::GenericAssocListLinhaAction)


def test_ansic::genericassoclistlinhaaction_constructor_exists():
    assert callable(ansic::GenericAssocListLinhaAction.__init__)


def test_ansic::genericassoclistlinhaaction_constructor_args():
    sig = inspect.signature(ansic::GenericAssocListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_ansic::string::ufcg_is_not_abstract():
    assert not inspect.isabstract(ansic::string::ufcg)


def test_ansic::string::ufcg_constructor_exists():
    assert callable(ansic::string::ufcg.__init__)


def test_ansic::string::ufcg_constructor_args():
    sig = inspect.signature(ansic::string::ufcg.__init__)
    params = list(sig.parameters.keys())
    assert "__func__" in params, "Missing parameter '__func__'"
    assert "string_literal" in params, "Missing parameter 'string_literal'"

def test_ansic::string::ufcg_has___func__():
    assert hasattr(ansic::string::ufcg, "__func__")
    descriptor = None
    for klass in ansic::string::ufcg.__mro__:
        if "__func__" in klass.__dict__:
            descriptor = klass.__dict__["__func__"]
            break
    assert isinstance(descriptor, property)

def test_ansic::string::ufcg_has_string_literal():
    assert hasattr(ansic::string::ufcg, "string_literal")
    descriptor = None
    for klass in ansic::string::ufcg.__mro__:
        if "string_literal" in klass.__dict__:
            descriptor = klass.__dict__["string_literal"]
            break
    assert isinstance(descriptor, property)



def test_identifier::list::linha_is_not_abstract():
    assert not inspect.isabstract(identifier::list::linha)


def test_identifier::list::linha_constructor_exists():
    assert callable(identifier::list::linha.__init__)


def test_identifier::list::linha_constructor_args():
    sig = inspect.signature(identifier::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::identifierlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic::IdentifierListLinhaAction)


def test_ansic::identifierlistlinhaaction_constructor_exists():
    assert callable(ansic::IdentifierListLinhaAction.__init__)


def test_ansic::identifierlistlinhaaction_constructor_args():
    sig = inspect.signature(ansic::IdentifierListLinhaAction.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic::identifierlistlinhaaction_has_identifier():
    assert hasattr(ansic::IdentifierListLinhaAction, "identifier")
    descriptor = None
    for klass in ansic::IdentifierListLinhaAction.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_direct::abstract::declarator::linha_is_not_abstract():
    assert not inspect.isabstract(direct::abstract::declarator::linha)


def test_direct::abstract::declarator::linha_constructor_exists():
    assert callable(direct::abstract::declarator::linha.__init__)


def test_direct::abstract::declarator::linha_constructor_args():
    sig = inspect.signature(direct::abstract::declarator::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::directabstractdeclarratorlinhaaction_is_not_abstract():
    assert not inspect.isabstract(ansic::DirectAbstractDeclarratorLinhaAction)


def test_ansic::directabstractdeclarratorlinhaaction_constructor_exists():
    assert callable(ansic::DirectAbstractDeclarratorLinhaAction.__init__)


def test_ansic::directabstractdeclarratorlinhaaction_constructor_args():
    sig = inspect.signature(ansic::DirectAbstractDeclarratorLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_ansic::struct::or::union::specifier::complement_is_not_abstract():
    assert not inspect.isabstract(ansic::struct::or::union::specifier::complement)


def test_ansic::struct::or::union::specifier::complement_constructor_exists():
    assert callable(ansic::struct::or::union::specifier::complement.__init__)


def test_ansic::struct::or::union::specifier::complement_constructor_args():
    sig = inspect.signature(ansic::struct::or::union::specifier::complement.__init__)
    params = list(sig.parameters.keys())



def test_ansic::declaration_is_not_abstract():
    assert not inspect.isabstract(ansic::declaration)


def test_ansic::declaration_constructor_exists():
    assert callable(ansic::declaration.__init__)


def test_ansic::declaration_constructor_args():
    sig = inspect.signature(ansic::declaration.__init__)
    params = list(sig.parameters.keys())



def test_ansic::function::definition_is_not_abstract():
    assert not inspect.isabstract(ansic::function::definition)


def test_ansic::function::definition_constructor_exists():
    assert callable(ansic::function::definition.__init__)


def test_ansic::function::definition_constructor_args():
    sig = inspect.signature(ansic::function::definition.__init__)
    params = list(sig.parameters.keys())



def test_ansic::translation::unit::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::translation::unit::linha)


def test_ansic::translation::unit::linha_constructor_exists():
    assert callable(ansic::translation::unit::linha.__init__)


def test_ansic::translation::unit::linha_constructor_args():
    sig = inspect.signature(ansic::translation::unit::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::enumeration::constant_is_not_abstract():
    assert not inspect.isabstract(ansic::enumeration::constant)


def test_ansic::enumeration::constant_constructor_exists():
    assert callable(ansic::enumeration::constant.__init__)


def test_ansic::enumeration::constant_constructor_args():
    sig = inspect.signature(ansic::enumeration::constant.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic::enumeration::constant_has_identifier():
    assert hasattr(ansic::enumeration::constant, "identifier")
    descriptor = None
    for klass in ansic::enumeration::constant.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic::enumerator::list::linha_is_not_abstract():
    assert not inspect.isabstract(ansic::enumerator::list::linha)


def test_ansic::enumerator::list::linha_constructor_exists():
    assert callable(ansic::enumerator::list::linha.__init__)


def test_ansic::enumerator::list::linha_constructor_args():
    sig = inspect.signature(ansic::enumerator::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_ansic::enumerator_is_not_abstract():
    assert not inspect.isabstract(ansic::enumerator)


def test_ansic::enumerator_constructor_exists():
    assert callable(ansic::enumerator.__init__)


def test_ansic::enumerator_constructor_args():
    sig = inspect.signature(ansic::enumerator.__init__)
    params = list(sig.parameters.keys())



def test_ansic::enumerator::list_is_not_abstract():
    assert not inspect.isabstract(ansic::enumerator::list)


def test_ansic::enumerator::list_constructor_exists():
    assert callable(ansic::enumerator::list.__init__)


def test_ansic::enumerator::list_constructor_args():
    sig = inspect.signature(ansic::enumerator::list.__init__)
    params = list(sig.parameters.keys())



def test_ansic::enum::specifier_is_not_abstract():
    assert not inspect.isabstract(ansic::enum::specifier)


def test_ansic::enum::specifier_constructor_exists():
    assert callable(ansic::enum::specifier.__init__)


def test_ansic::enum::specifier_constructor_args():
    sig = inspect.signature(ansic::enum::specifier.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_ansic::enum::specifier_has_identifier():
    assert hasattr(ansic::enum::specifier, "identifier")
    descriptor = None
    for klass in ansic::enum::specifier.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic::struct::or::union::specifier_is_not_abstract():
    assert not inspect.isabstract(ansic::struct::or::union::specifier)


def test_ansic::struct::or::union::specifier_constructor_exists():
    assert callable(ansic::struct::or::union::specifier.__init__)


def test_ansic::struct::or::union::specifier_constructor_args():
    sig = inspect.signature(ansic::struct::or::union::specifier.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "struct_or_union" in params, "Missing parameter 'struct_or_union'"

def test_ansic::struct::or::union::specifier_has_identifier():
    assert hasattr(ansic::struct::or::union::specifier, "identifier")
    descriptor = None
    for klass in ansic::struct::or::union::specifier.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_ansic::struct::or::union::specifier_has_struct_or_union():
    assert hasattr(ansic::struct::or::union::specifier, "struct_or_union")
    descriptor = None
    for klass in ansic::struct::or::union::specifier.__mro__:
        if "struct_or_union" in klass.__dict__:
            descriptor = klass.__dict__["struct_or_union"]
            break
    assert isinstance(descriptor, property)



def test_ansic::atomic::type::specifier_is_not_abstract():
    assert not inspect.isabstract(ansic::atomic::type::specifier)


def test_ansic::atomic::type::specifier_constructor_exists():
    assert callable(ansic::atomic::type::specifier.__init__)


def test_ansic::atomic::type::specifier_constructor_args():
    sig = inspect.signature(ansic::atomic::type::specifier.__init__)
    params = list(sig.parameters.keys())



def test_ansic::constant::expression_is_not_abstract():
    assert not inspect.isabstract(ansic::constant::expression)


def test_ansic::constant::expression_constructor_exists():
    assert callable(ansic::constant::expression.__init__)


def test_ansic::constant::expression_constructor_args():
    sig = inspect.signature(ansic::constant::expression.__init__)
    params = list(sig.parameters.keys())



def test_ansic::type::name_is_not_abstract():
    assert not inspect.isabstract(ansic::type::name)


def test_ansic::type::name_constructor_exists():
    assert callable(ansic::type::name.__init__)


def test_ansic::type::name_constructor_args():
    sig = inspect.signature(ansic::type::name.__init__)
    params = list(sig.parameters.keys())



def test_ansic::alignment::specifier_is_not_abstract():
    assert not inspect.isabstract(ansic::alignment::specifier)


def test_ansic::alignment::specifier_constructor_exists():
    assert callable(ansic::alignment::specifier.__init__)


def test_ansic::alignment::specifier_constructor_args():
    sig = inspect.signature(ansic::alignment::specifier.__init__)
    params = list(sig.parameters.keys())



def test_ansic::type::qualifier_is_not_abstract():
    assert not inspect.isabstract(ansic::type::qualifier)


def test_ansic::type::qualifier_constructor_exists():
    assert callable(ansic::type::qualifier.__init__)


def test_ansic::type::qualifier_constructor_args():
    sig = inspect.signature(ansic::type::qualifier.__init__)
    params = list(sig.parameters.keys())
    assert "namez" in params, "Missing parameter 'namez'"

def test_ansic::type::qualifier_has_namez():
    assert hasattr(ansic::type::qualifier, "namez")
    descriptor = None
    for klass in ansic::type::qualifier.__mro__:
        if "namez" in klass.__dict__:
            descriptor = klass.__dict__["namez"]
            break
    assert isinstance(descriptor, property)



def test_ansic::type::specifier_is_not_abstract():
    assert not inspect.isabstract(ansic::type::specifier)


def test_ansic::type::specifier_constructor_exists():
    assert callable(ansic::type::specifier.__init__)


def test_ansic::type::specifier_constructor_args():
    sig = inspect.signature(ansic::type::specifier.__init__)
    params = list(sig.parameters.keys())
    assert "type_name_str" in params, "Missing parameter 'type_name_str'"

def test_ansic::type::specifier_has_type_name_str():
    assert hasattr(ansic::type::specifier, "type_name_str")
    descriptor = None
    for klass in ansic::type::specifier.__mro__:
        if "type_name_str" in klass.__dict__:
            descriptor = klass.__dict__["type_name_str"]
            break
    assert isinstance(descriptor, property)



def test_ansic::declaration::specifiers_is_not_abstract():
    assert not inspect.isabstract(ansic::declaration::specifiers)


def test_ansic::declaration::specifiers_constructor_exists():
    assert callable(ansic::declaration::specifiers.__init__)


def test_ansic::declaration::specifiers_constructor_args():
    sig = inspect.signature(ansic::declaration::specifiers.__init__)
    params = list(sig.parameters.keys())
    assert "storage_class_specifier" in params, "Missing parameter 'storage_class_specifier'"
    assert "function_specifier" in params, "Missing parameter 'function_specifier'"

def test_ansic::declaration::specifiers_has_storage_class_specifier():
    assert hasattr(ansic::declaration::specifiers, "storage_class_specifier")
    descriptor = None
    for klass in ansic::declaration::specifiers.__mro__:
        if "storage_class_specifier" in klass.__dict__:
            descriptor = klass.__dict__["storage_class_specifier"]
            break
    assert isinstance(descriptor, property)

def test_ansic::declaration::specifiers_has_function_specifier():
    assert hasattr(ansic::declaration::specifiers, "function_specifier")
    descriptor = None
    for klass in ansic::declaration::specifiers.__mro__:
        if "function_specifier" in klass.__dict__:
            descriptor = klass.__dict__["function_specifier"]
            break
    assert isinstance(descriptor, property)



def test_ansic::external::declaration_is_not_abstract():
    assert not inspect.isabstract(ansic::external::declaration)


def test_ansic::external::declaration_constructor_exists():
    assert callable(ansic::external::declaration.__init__)


def test_ansic::external::declaration_constructor_args():
    sig = inspect.signature(ansic::external::declaration.__init__)
    params = list(sig.parameters.keys())



def test_ansic::translation::unit_is_not_abstract():
    assert not inspect.isabstract(ansic::translation::unit)


def test_ansic::translation::unit_constructor_exists():
    assert callable(ansic::translation::unit.__init__)


def test_ansic::translation::unit_constructor_args():
    sig = inspect.signature(ansic::translation::unit.__init__)
    params = list(sig.parameters.keys())



def test_ansic::domainmodel_is_not_abstract():
    assert not inspect.isabstract(ansic::DomainModel)


def test_ansic::domainmodel_constructor_exists():
    assert callable(ansic::DomainModel.__init__)


def test_ansic::domainmodel_constructor_args():
    sig = inspect.signature(ansic::DomainModel.__init__)
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
type::qualifier::list::linha_strategy = st.builds(
    type::qualifier::list::linha,
)
ansic::TypeQualifierListLinhaAtion_strategy = st.builds(
    ansic::TypeQualifierListLinhaAtion,
)
declaration::list::linha_strategy = st.builds(
    declaration::list::linha,
)
ansic::DeclarationListLinhaAction_strategy = st.builds(
    ansic::DeclarationListLinhaAction,
)
struct::declarator::list::linha_strategy = st.builds(
    struct::declarator::list::linha,
)
ansic::StructDeclaratorListLinhaAction_strategy = st.builds(
    ansic::StructDeclaratorListLinhaAction,
)
struct::declaration::list::linha_strategy = st.builds(
    struct::declaration::list::linha,
)
ansic::StructDeclarationListLinhaAction_strategy = st.builds(
    ansic::StructDeclarationListLinhaAction,
)
struct::or::union::specifier::complement_strategy = st.builds(
    struct::or::union::specifier::complement,
)
ansic::StructOrUnionSpecifierComplementAction_strategy = st.builds(
    ansic::StructOrUnionSpecifierComplementAction,
)
enumerator::list::linha_strategy = st.builds(
    enumerator::list::linha,
)
ansic::EnumeratorListLinhaAction_strategy = st.builds(
    ansic::EnumeratorListLinhaAction,
)
ansic::init::declarator_strategy = st.builds(
    ansic::init::declarator,
)
ansic::expression::linha_strategy = st.builds(
    ansic::expression::linha,
)
postfix::expression_strategy = st.builds(
    postfix::expression,
)
ansic::conditional::expression::linha_strategy = st.builds(
    ansic::conditional::expression::linha,
)
ansic::logical::or::expression::linha_strategy = st.builds(
    ansic::logical::or::expression::linha,
)
ansic::logical::or::expression_strategy = st.builds(
    ansic::logical::or::expression,
)
ansic::logical::and::expression::linha_strategy = st.builds(
    ansic::logical::and::expression::linha,
)
ansic::logical::and::expression_strategy = st.builds(
    ansic::logical::and::expression,
)
ansic::inclusive::or::expression::linha_strategy = st.builds(
    ansic::inclusive::or::expression::linha,
)
ansic::inclusive::or::expression_strategy = st.builds(
    ansic::inclusive::or::expression,
)
ansic::exclusive::or::expression::linha_strategy = st.builds(
    ansic::exclusive::or::expression::linha,
)
ansic::exclusive::or::expression_strategy = st.builds(
    ansic::exclusive::or::expression,
)
ansic::and::expression::linha_strategy = st.builds(
    ansic::and::expression::linha,
)
ansic::and::expression_strategy = st.builds(
    ansic::and::expression,
)
ansic::jump::statement_strategy = st.builds(
    ansic::jump::statement,
    return_vazio=
        safe_text,
    identifier=
        safe_text,
    break_=
        safe_text,
    return_=
        safe_text
)
ansic::iteration::statement_strategy = st.builds(
    ansic::iteration::statement,
)
ansic::block::item::list::linha_strategy = st.builds(
    ansic::block::item::list::linha,
)
ansic::block::item_strategy = st.builds(
    ansic::block::item,
)
ansic::block::item::list_strategy = st.builds(
    ansic::block::item::list,
)
ansic::additive::expression::complement_strategy = st.builds(
    ansic::additive::expression::complement,
)
ansic::additive::expression::linha_strategy = st.builds(
    ansic::additive::expression::linha,
)
ansic::selection::statement_strategy = st.builds(
    ansic::selection::statement,
)
ansic::expression::statement_strategy = st.builds(
    ansic::expression::statement,
)
ansic::labeled::statement_strategy = st.builds(
    ansic::labeled::statement,
    identifier=
        safe_text
)
ansic::statement_strategy = st.builds(
    ansic::statement,
)
ansic::equality::expression::complement_strategy = st.builds(
    ansic::equality::expression::complement,
)
ansic::equality::expression::linha_strategy = st.builds(
    ansic::equality::expression::linha,
)
ansic::equality::expression_strategy = st.builds(
    ansic::equality::expression,
)
ansic::relational::expression::complement_strategy = st.builds(
    ansic::relational::expression::complement,
)
ansic::relational::expression::linha_strategy = st.builds(
    ansic::relational::expression::linha,
)
ansic::relational::expression_strategy = st.builds(
    ansic::relational::expression,
)
ansic::shift::expression::complement_strategy = st.builds(
    ansic::shift::expression::complement,
)
ansic::shift::expression::linha_strategy = st.builds(
    ansic::shift::expression::linha,
)
ansic::shift::expression_strategy = st.builds(
    ansic::shift::expression,
)
ansic::designator::list::linha_strategy = st.builds(
    ansic::designator::list::linha,
)
ansic::designator_strategy = st.builds(
    ansic::designator,
    identifier=
        safe_text
)
ansic::designator::list_strategy = st.builds(
    ansic::designator::list,
)
ansic::additive::expression_strategy = st.builds(
    ansic::additive::expression,
)
ansic::multiplicative::expression::complement_strategy = st.builds(
    ansic::multiplicative::expression::complement,
)
ansic::multiplicative::expression::linha_strategy = st.builds(
    ansic::multiplicative::expression::linha,
)
ansic::multiplicative::expression_strategy = st.builds(
    ansic::multiplicative::expression,
)
ansic::cast::expression_strategy = st.builds(
    ansic::cast::expression,
)
ansic::unary::expression_strategy = st.builds(
    ansic::unary::expression,
    unary_operator=
        safe_text
)
ansic::argument::expression::list::linha_strategy = st.builds(
    ansic::argument::expression::list::linha,
)
ansic::argument::expression::list_strategy = st.builds(
    ansic::argument::expression::list,
)
ansic::postfix::expression::complement_strategy = st.builds(
    ansic::postfix::expression::complement,
    identifier=
        safe_text
)
ansic::conditional::expression_strategy = st.builds(
    ansic::conditional::expression,
)
ansic::primary::expression_strategy = st.builds(
    ansic::primary::expression,
    identifier=
        safe_text
)
ansic::identifier::list::linha_strategy = st.builds(
    ansic::identifier::list::linha,
)
ansic::initializer::list::complement_strategy = st.builds(
    ansic::initializer::list::complement,
)
ansic::initializer::list::linha_strategy = st.builds(
    ansic::initializer::list::linha,
)
ansic::init::declarator::list::linha_strategy = st.builds(
    ansic::init::declarator::list::linha,
)
ansic::designation_strategy = st.builds(
    ansic::designation,
)
ansic::postfix::expression::linha_strategy = st.builds(
    ansic::postfix::expression::linha,
)
ansic::postfix::expression_strategy = st.builds(
    ansic::postfix::expression,
)
ansic::generic::assoc::list::linha_strategy = st.builds(
    ansic::generic::assoc::list::linha,
)
ansic::generic::association_strategy = st.builds(
    ansic::generic::association,
    default=
        safe_text
)
ansic::generic::assoc::list_strategy = st.builds(
    ansic::generic::assoc::list,
)
ansic::generic::selection_strategy = st.builds(
    ansic::generic::selection,
    _generic=
        safe_text
)
ansic::expression_strategy = st.builds(
    ansic::expression,
)
ansic::constant_strategy = st.builds(
    ansic::constant,
    char=
        safe_text,
    enumz=
        safe_text,
    f_constant=
        safe_text,
    i_constant=
        st.integers()
)
ansic::parameter::type::list_strategy = st.builds(
    ansic::parameter::type::list,
)
ansic::assignment::expression_strategy = st.builds(
    ansic::assignment::expression,
    assignment_operator=
        safe_text
)
ansic::direct::abstract::declarator::complement_strategy = st.builds(
    ansic::direct::abstract::declarator::complement,
)
ansic::initializer::list_strategy = st.builds(
    ansic::initializer::list,
)
ansic::initializer_strategy = st.builds(
    ansic::initializer,
)
ansic::direct::abstract::declarator::linha_strategy = st.builds(
    ansic::direct::abstract::declarator::linha,
)
ansic::direct::abstract::declarator_strategy = st.builds(
    ansic::direct::abstract::declarator,
)
ansic::abstract::declarator_strategy = st.builds(
    ansic::abstract::declarator,
)
ansic::parameter::list::linha_strategy = st.builds(
    ansic::parameter::list::linha,
)
ansic::parameter::declaration_strategy = st.builds(
    ansic::parameter::declaration,
)
ansic::parameter::lista_strategy = st.builds(
    ansic::parameter::lista,
)
ansic::identifier::list_strategy = st.builds(
    ansic::identifier::list,
    identifier=
        safe_text
)
ansic::direct::declarator::complemento_strategy = st.builds(
    ansic::direct::declarator::complemento,
)
ansic::direct::declarator::linha_strategy = st.builds(
    ansic::direct::declarator::linha,
)
ansic::type::qualifier::list::linha_strategy = st.builds(
    ansic::type::qualifier::list::linha,
)
direct::abstract::declarator::complement_strategy = st.builds(
    direct::abstract::declarator::complement,
)
ansic::type::qualifier::list_strategy = st.builds(
    ansic::type::qualifier::list,
)
ansic::direct::declarator_strategy = st.builds(
    ansic::direct::declarator,
    identifier=
        safe_text
)
ansic::pointer_strategy = st.builds(
    ansic::pointer,
)
ansic::declaration::list::linha_strategy = st.builds(
    ansic::declaration::list::linha,
)
ansic::compound::statement_strategy = st.builds(
    ansic::compound::statement,
)
ansic::declaration::list_strategy = st.builds(
    ansic::declaration::list,
)
ansic::init::declarator::list_strategy = st.builds(
    ansic::init::declarator::list,
)
ansic::struct::declaration::list_strategy = st.builds(
    ansic::struct::declaration::list,
)
ansic::declarator_strategy = st.builds(
    ansic::declarator,
)
ansic::struct::declarator::list::linha_strategy = st.builds(
    ansic::struct::declarator::list::linha,
)
ansic::struct::declarator_strategy = st.builds(
    ansic::struct::declarator,
)
ansic::static::assert::declaration_strategy = st.builds(
    ansic::static::assert::declaration,
)
ansic::struct::declarator::list_strategy = st.builds(
    ansic::struct::declarator::list,
)
ansic::specifier::qualifier::list_strategy = st.builds(
    ansic::specifier::qualifier::list,
)
ansic::struct::declaration::list::linha_strategy = st.builds(
    ansic::struct::declaration::list::linha,
)
ansic::struct::declaration_strategy = st.builds(
    ansic::struct::declaration,
)
translation::unit::linha_strategy = st.builds(
    translation::unit::linha,
)
ansic::TranlationUnitLinhaAction_strategy = st.builds(
    ansic::TranlationUnitLinhaAction,
)
init::declarator::list::linha_strategy = st.builds(
    init::declarator::list::linha,
)
ansic::InitDecclaratorListLinhaAction_strategy = st.builds(
    ansic::InitDecclaratorListLinhaAction,
)
unary::expression_strategy = st.builds(
    unary::expression,
)
ansic::PlusPlus_strategy = st.builds(
    ansic::PlusPlus,
    plus=
        safe_text
)
argument::expression::list::linha_strategy = st.builds(
    argument::expression::list::linha,
)
ansic::ArgumentExpressionListLinhaAction_strategy = st.builds(
    ansic::ArgumentExpressionListLinhaAction,
)
postfix::expression::complement_strategy = st.builds(
    postfix::expression::complement,
)
ansic::PostFixEmpryParams_strategy = st.builds(
    ansic::PostFixEmpryParams,
)
designator::list::linha_strategy = st.builds(
    designator::list::linha,
)
ansic::DesignatorListLinhaAction_strategy = st.builds(
    ansic::DesignatorListLinhaAction,
)
initializer::list::linha_strategy = st.builds(
    initializer::list::linha,
)
ansic::InitializerListLinhaAction_strategy = st.builds(
    ansic::InitializerListLinhaAction,
)
postfix::expression::linha_strategy = st.builds(
    postfix::expression::linha,
)
ansic::PostfixExpressionLinhaAction_strategy = st.builds(
    ansic::PostfixExpressionLinhaAction,
)
generic::assoc::list::linha_strategy = st.builds(
    generic::assoc::list::linha,
)
ansic::GenericAssocListLinhaAction_strategy = st.builds(
    ansic::GenericAssocListLinhaAction,
)
ansic::string::ufcg_strategy = st.builds(
    ansic::string::ufcg,
    __func__=
        safe_text,
    string_literal=
        safe_text
)
identifier::list::linha_strategy = st.builds(
    identifier::list::linha,
)
ansic::IdentifierListLinhaAction_strategy = st.builds(
    ansic::IdentifierListLinhaAction,
    identifier=
        safe_text
)
direct::abstract::declarator::linha_strategy = st.builds(
    direct::abstract::declarator::linha,
)
ansic::DirectAbstractDeclarratorLinhaAction_strategy = st.builds(
    ansic::DirectAbstractDeclarratorLinhaAction,
)
ansic::struct::or::union::specifier::complement_strategy = st.builds(
    ansic::struct::or::union::specifier::complement,
)
ansic::declaration_strategy = st.builds(
    ansic::declaration,
)
ansic::function::definition_strategy = st.builds(
    ansic::function::definition,
)
ansic::translation::unit::linha_strategy = st.builds(
    ansic::translation::unit::linha,
)
ansic::enumeration::constant_strategy = st.builds(
    ansic::enumeration::constant,
    identifier=
        safe_text
)
ansic::enumerator::list::linha_strategy = st.builds(
    ansic::enumerator::list::linha,
)
ansic::enumerator_strategy = st.builds(
    ansic::enumerator,
)
ansic::enumerator::list_strategy = st.builds(
    ansic::enumerator::list,
)
ansic::enum::specifier_strategy = st.builds(
    ansic::enum::specifier,
    identifier=
        safe_text
)
ansic::struct::or::union::specifier_strategy = st.builds(
    ansic::struct::or::union::specifier,
    identifier=
        safe_text,
    struct_or_union=
        safe_text
)
ansic::atomic::type::specifier_strategy = st.builds(
    ansic::atomic::type::specifier,
)
ansic::constant::expression_strategy = st.builds(
    ansic::constant::expression,
)
ansic::type::name_strategy = st.builds(
    ansic::type::name,
)
ansic::alignment::specifier_strategy = st.builds(
    ansic::alignment::specifier,
)
ansic::type::qualifier_strategy = st.builds(
    ansic::type::qualifier,
    namez=
        safe_text
)
ansic::type::specifier_strategy = st.builds(
    ansic::type::specifier,
    type_name_str=
        safe_text
)
ansic::declaration::specifiers_strategy = st.builds(
    ansic::declaration::specifiers,
    storage_class_specifier=
        safe_text,
    function_specifier=
        safe_text
)
ansic::external::declaration_strategy = st.builds(
    ansic::external::declaration,
)
ansic::translation::unit_strategy = st.builds(
    ansic::translation::unit,
)
ansic::DomainModel_strategy = st.builds(
    ansic::DomainModel,
)

@given(instance=type::qualifier::list::linha_strategy)
@settings(max_examples=50)
def test_type::qualifier::list::linha_instantiation(instance):
    assert isinstance(instance, type::qualifier::list::linha)

@given(instance=ansic::TypeQualifierListLinhaAtion_strategy)
@settings(max_examples=50)
def test_ansic::typequalifierlistlinhaation_instantiation(instance):
    assert isinstance(instance, ansic::TypeQualifierListLinhaAtion)

@given(instance=declaration::list::linha_strategy)
@settings(max_examples=50)
def test_declaration::list::linha_instantiation(instance):
    assert isinstance(instance, declaration::list::linha)

@given(instance=ansic::DeclarationListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic::declarationlistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic::DeclarationListLinhaAction)

@given(instance=struct::declarator::list::linha_strategy)
@settings(max_examples=50)
def test_struct::declarator::list::linha_instantiation(instance):
    assert isinstance(instance, struct::declarator::list::linha)

@given(instance=ansic::StructDeclaratorListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic::structdeclaratorlistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic::StructDeclaratorListLinhaAction)

@given(instance=struct::declaration::list::linha_strategy)
@settings(max_examples=50)
def test_struct::declaration::list::linha_instantiation(instance):
    assert isinstance(instance, struct::declaration::list::linha)

@given(instance=ansic::StructDeclarationListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic::structdeclarationlistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic::StructDeclarationListLinhaAction)

@given(instance=struct::or::union::specifier::complement_strategy)
@settings(max_examples=50)
def test_struct::or::union::specifier::complement_instantiation(instance):
    assert isinstance(instance, struct::or::union::specifier::complement)

@given(instance=ansic::StructOrUnionSpecifierComplementAction_strategy)
@settings(max_examples=50)
def test_ansic::structorunionspecifiercomplementaction_instantiation(instance):
    assert isinstance(instance, ansic::StructOrUnionSpecifierComplementAction)

@given(instance=enumerator::list::linha_strategy)
@settings(max_examples=50)
def test_enumerator::list::linha_instantiation(instance):
    assert isinstance(instance, enumerator::list::linha)

@given(instance=ansic::EnumeratorListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic::enumeratorlistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic::EnumeratorListLinhaAction)

@given(instance=ansic::init::declarator_strategy)
@settings(max_examples=50)
def test_ansic::init::declarator_instantiation(instance):
    assert isinstance(instance, ansic::init::declarator)

@given(instance=ansic::expression::linha_strategy)
@settings(max_examples=50)
def test_ansic::expression::linha_instantiation(instance):
    assert isinstance(instance, ansic::expression::linha)

@given(instance=postfix::expression_strategy)
@settings(max_examples=50)
def test_postfix::expression_instantiation(instance):
    assert isinstance(instance, postfix::expression)

@given(instance=ansic::conditional::expression::linha_strategy)
@settings(max_examples=50)
def test_ansic::conditional::expression::linha_instantiation(instance):
    assert isinstance(instance, ansic::conditional::expression::linha)

@given(instance=ansic::logical::or::expression::linha_strategy)
@settings(max_examples=50)
def test_ansic::logical::or::expression::linha_instantiation(instance):
    assert isinstance(instance, ansic::logical::or::expression::linha)

@given(instance=ansic::logical::or::expression_strategy)
@settings(max_examples=50)
def test_ansic::logical::or::expression_instantiation(instance):
    assert isinstance(instance, ansic::logical::or::expression)

@given(instance=ansic::logical::and::expression::linha_strategy)
@settings(max_examples=50)
def test_ansic::logical::and::expression::linha_instantiation(instance):
    assert isinstance(instance, ansic::logical::and::expression::linha)

@given(instance=ansic::logical::and::expression_strategy)
@settings(max_examples=50)
def test_ansic::logical::and::expression_instantiation(instance):
    assert isinstance(instance, ansic::logical::and::expression)

@given(instance=ansic::inclusive::or::expression::linha_strategy)
@settings(max_examples=50)
def test_ansic::inclusive::or::expression::linha_instantiation(instance):
    assert isinstance(instance, ansic::inclusive::or::expression::linha)

@given(instance=ansic::inclusive::or::expression_strategy)
@settings(max_examples=50)
def test_ansic::inclusive::or::expression_instantiation(instance):
    assert isinstance(instance, ansic::inclusive::or::expression)

@given(instance=ansic::exclusive::or::expression::linha_strategy)
@settings(max_examples=50)
def test_ansic::exclusive::or::expression::linha_instantiation(instance):
    assert isinstance(instance, ansic::exclusive::or::expression::linha)

@given(instance=ansic::exclusive::or::expression_strategy)
@settings(max_examples=50)
def test_ansic::exclusive::or::expression_instantiation(instance):
    assert isinstance(instance, ansic::exclusive::or::expression)

@given(instance=ansic::and::expression::linha_strategy)
@settings(max_examples=50)
def test_ansic::and::expression::linha_instantiation(instance):
    assert isinstance(instance, ansic::and::expression::linha)

@given(instance=ansic::and::expression_strategy)
@settings(max_examples=50)
def test_ansic::and::expression_instantiation(instance):
    assert isinstance(instance, ansic::and::expression)

@given(instance=ansic::jump::statement_strategy)
@settings(max_examples=50)
def test_ansic::jump::statement_instantiation(instance):
    assert isinstance(instance, ansic::jump::statement)

@given(instance=ansic::jump::statement_strategy)
def test_ansic::jump::statement_return_vazio_type(instance):
    assert isinstance(instance.return_vazio, str)


@given(instance=ansic::jump::statement_strategy)
def test_ansic::jump::statement_return_vazio_setter(instance):
    original = instance.return_vazio
    instance.return_vazio = original
    assert instance.return_vazio == original

@given(instance=ansic::jump::statement_strategy)
def test_ansic::jump::statement_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=ansic::jump::statement_strategy)
def test_ansic::jump::statement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic::jump::statement_strategy)
def test_ansic::jump::statement_break__type(instance):
    assert isinstance(instance.break_, str)


@given(instance=ansic::jump::statement_strategy)
def test_ansic::jump::statement_break__setter(instance):
    original = instance.break_
    instance.break_ = original
    assert instance.break_ == original

@given(instance=ansic::jump::statement_strategy)
def test_ansic::jump::statement_return__type(instance):
    assert isinstance(instance.return_, str)


@given(instance=ansic::jump::statement_strategy)
def test_ansic::jump::statement_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original

@given(instance=ansic::iteration::statement_strategy)
@settings(max_examples=50)
def test_ansic::iteration::statement_instantiation(instance):
    assert isinstance(instance, ansic::iteration::statement)

@given(instance=ansic::block::item::list::linha_strategy)
@settings(max_examples=50)
def test_ansic::block::item::list::linha_instantiation(instance):
    assert isinstance(instance, ansic::block::item::list::linha)

@given(instance=ansic::block::item_strategy)
@settings(max_examples=50)
def test_ansic::block::item_instantiation(instance):
    assert isinstance(instance, ansic::block::item)

@given(instance=ansic::block::item::list_strategy)
@settings(max_examples=50)
def test_ansic::block::item::list_instantiation(instance):
    assert isinstance(instance, ansic::block::item::list)

@given(instance=ansic::additive::expression::complement_strategy)
@settings(max_examples=50)
def test_ansic::additive::expression::complement_instantiation(instance):
    assert isinstance(instance, ansic::additive::expression::complement)

@given(instance=ansic::additive::expression::linha_strategy)
@settings(max_examples=50)
def test_ansic::additive::expression::linha_instantiation(instance):
    assert isinstance(instance, ansic::additive::expression::linha)

@given(instance=ansic::selection::statement_strategy)
@settings(max_examples=50)
def test_ansic::selection::statement_instantiation(instance):
    assert isinstance(instance, ansic::selection::statement)

@given(instance=ansic::expression::statement_strategy)
@settings(max_examples=50)
def test_ansic::expression::statement_instantiation(instance):
    assert isinstance(instance, ansic::expression::statement)

@given(instance=ansic::labeled::statement_strategy)
@settings(max_examples=50)
def test_ansic::labeled::statement_instantiation(instance):
    assert isinstance(instance, ansic::labeled::statement)

@given(instance=ansic::labeled::statement_strategy)
def test_ansic::labeled::statement_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=ansic::labeled::statement_strategy)
def test_ansic::labeled::statement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic::statement_strategy)
@settings(max_examples=50)
def test_ansic::statement_instantiation(instance):
    assert isinstance(instance, ansic::statement)

@given(instance=ansic::equality::expression::complement_strategy)
@settings(max_examples=50)
def test_ansic::equality::expression::complement_instantiation(instance):
    assert isinstance(instance, ansic::equality::expression::complement)

@given(instance=ansic::equality::expression::linha_strategy)
@settings(max_examples=50)
def test_ansic::equality::expression::linha_instantiation(instance):
    assert isinstance(instance, ansic::equality::expression::linha)

@given(instance=ansic::equality::expression_strategy)
@settings(max_examples=50)
def test_ansic::equality::expression_instantiation(instance):
    assert isinstance(instance, ansic::equality::expression)

@given(instance=ansic::relational::expression::complement_strategy)
@settings(max_examples=50)
def test_ansic::relational::expression::complement_instantiation(instance):
    assert isinstance(instance, ansic::relational::expression::complement)

@given(instance=ansic::relational::expression::linha_strategy)
@settings(max_examples=50)
def test_ansic::relational::expression::linha_instantiation(instance):
    assert isinstance(instance, ansic::relational::expression::linha)

@given(instance=ansic::relational::expression_strategy)
@settings(max_examples=50)
def test_ansic::relational::expression_instantiation(instance):
    assert isinstance(instance, ansic::relational::expression)

@given(instance=ansic::shift::expression::complement_strategy)
@settings(max_examples=50)
def test_ansic::shift::expression::complement_instantiation(instance):
    assert isinstance(instance, ansic::shift::expression::complement)

@given(instance=ansic::shift::expression::linha_strategy)
@settings(max_examples=50)
def test_ansic::shift::expression::linha_instantiation(instance):
    assert isinstance(instance, ansic::shift::expression::linha)

@given(instance=ansic::shift::expression_strategy)
@settings(max_examples=50)
def test_ansic::shift::expression_instantiation(instance):
    assert isinstance(instance, ansic::shift::expression)

@given(instance=ansic::designator::list::linha_strategy)
@settings(max_examples=50)
def test_ansic::designator::list::linha_instantiation(instance):
    assert isinstance(instance, ansic::designator::list::linha)

@given(instance=ansic::designator_strategy)
@settings(max_examples=50)
def test_ansic::designator_instantiation(instance):
    assert isinstance(instance, ansic::designator)

@given(instance=ansic::designator_strategy)
def test_ansic::designator_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=ansic::designator_strategy)
def test_ansic::designator_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic::designator::list_strategy)
@settings(max_examples=50)
def test_ansic::designator::list_instantiation(instance):
    assert isinstance(instance, ansic::designator::list)

@given(instance=ansic::additive::expression_strategy)
@settings(max_examples=50)
def test_ansic::additive::expression_instantiation(instance):
    assert isinstance(instance, ansic::additive::expression)

@given(instance=ansic::multiplicative::expression::complement_strategy)
@settings(max_examples=50)
def test_ansic::multiplicative::expression::complement_instantiation(instance):
    assert isinstance(instance, ansic::multiplicative::expression::complement)

@given(instance=ansic::multiplicative::expression::linha_strategy)
@settings(max_examples=50)
def test_ansic::multiplicative::expression::linha_instantiation(instance):
    assert isinstance(instance, ansic::multiplicative::expression::linha)

@given(instance=ansic::multiplicative::expression_strategy)
@settings(max_examples=50)
def test_ansic::multiplicative::expression_instantiation(instance):
    assert isinstance(instance, ansic::multiplicative::expression)

@given(instance=ansic::cast::expression_strategy)
@settings(max_examples=50)
def test_ansic::cast::expression_instantiation(instance):
    assert isinstance(instance, ansic::cast::expression)

@given(instance=ansic::unary::expression_strategy)
@settings(max_examples=50)
def test_ansic::unary::expression_instantiation(instance):
    assert isinstance(instance, ansic::unary::expression)

@given(instance=ansic::unary::expression_strategy)
def test_ansic::unary::expression_unary_operator_type(instance):
    assert isinstance(instance.unary_operator, str)


@given(instance=ansic::unary::expression_strategy)
def test_ansic::unary::expression_unary_operator_setter(instance):
    original = instance.unary_operator
    instance.unary_operator = original
    assert instance.unary_operator == original

@given(instance=ansic::argument::expression::list::linha_strategy)
@settings(max_examples=50)
def test_ansic::argument::expression::list::linha_instantiation(instance):
    assert isinstance(instance, ansic::argument::expression::list::linha)

@given(instance=ansic::argument::expression::list_strategy)
@settings(max_examples=50)
def test_ansic::argument::expression::list_instantiation(instance):
    assert isinstance(instance, ansic::argument::expression::list)

@given(instance=ansic::postfix::expression::complement_strategy)
@settings(max_examples=50)
def test_ansic::postfix::expression::complement_instantiation(instance):
    assert isinstance(instance, ansic::postfix::expression::complement)

@given(instance=ansic::postfix::expression::complement_strategy)
def test_ansic::postfix::expression::complement_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=ansic::postfix::expression::complement_strategy)
def test_ansic::postfix::expression::complement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic::conditional::expression_strategy)
@settings(max_examples=50)
def test_ansic::conditional::expression_instantiation(instance):
    assert isinstance(instance, ansic::conditional::expression)

@given(instance=ansic::primary::expression_strategy)
@settings(max_examples=50)
def test_ansic::primary::expression_instantiation(instance):
    assert isinstance(instance, ansic::primary::expression)

@given(instance=ansic::primary::expression_strategy)
def test_ansic::primary::expression_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=ansic::primary::expression_strategy)
def test_ansic::primary::expression_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic::identifier::list::linha_strategy)
@settings(max_examples=50)
def test_ansic::identifier::list::linha_instantiation(instance):
    assert isinstance(instance, ansic::identifier::list::linha)

@given(instance=ansic::initializer::list::complement_strategy)
@settings(max_examples=50)
def test_ansic::initializer::list::complement_instantiation(instance):
    assert isinstance(instance, ansic::initializer::list::complement)

@given(instance=ansic::initializer::list::linha_strategy)
@settings(max_examples=50)
def test_ansic::initializer::list::linha_instantiation(instance):
    assert isinstance(instance, ansic::initializer::list::linha)

@given(instance=ansic::init::declarator::list::linha_strategy)
@settings(max_examples=50)
def test_ansic::init::declarator::list::linha_instantiation(instance):
    assert isinstance(instance, ansic::init::declarator::list::linha)

@given(instance=ansic::designation_strategy)
@settings(max_examples=50)
def test_ansic::designation_instantiation(instance):
    assert isinstance(instance, ansic::designation)

@given(instance=ansic::postfix::expression::linha_strategy)
@settings(max_examples=50)
def test_ansic::postfix::expression::linha_instantiation(instance):
    assert isinstance(instance, ansic::postfix::expression::linha)

@given(instance=ansic::postfix::expression_strategy)
@settings(max_examples=50)
def test_ansic::postfix::expression_instantiation(instance):
    assert isinstance(instance, ansic::postfix::expression)

@given(instance=ansic::generic::assoc::list::linha_strategy)
@settings(max_examples=50)
def test_ansic::generic::assoc::list::linha_instantiation(instance):
    assert isinstance(instance, ansic::generic::assoc::list::linha)

@given(instance=ansic::generic::association_strategy)
@settings(max_examples=50)
def test_ansic::generic::association_instantiation(instance):
    assert isinstance(instance, ansic::generic::association)

@given(instance=ansic::generic::association_strategy)
def test_ansic::generic::association_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=ansic::generic::association_strategy)
def test_ansic::generic::association_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=ansic::generic::assoc::list_strategy)
@settings(max_examples=50)
def test_ansic::generic::assoc::list_instantiation(instance):
    assert isinstance(instance, ansic::generic::assoc::list)

@given(instance=ansic::generic::selection_strategy)
@settings(max_examples=50)
def test_ansic::generic::selection_instantiation(instance):
    assert isinstance(instance, ansic::generic::selection)

@given(instance=ansic::generic::selection_strategy)
def test_ansic::generic::selection__generic_type(instance):
    assert isinstance(instance._generic, str)


@given(instance=ansic::generic::selection_strategy)
def test_ansic::generic::selection__generic_setter(instance):
    original = instance._generic
    instance._generic = original
    assert instance._generic == original

@given(instance=ansic::expression_strategy)
@settings(max_examples=50)
def test_ansic::expression_instantiation(instance):
    assert isinstance(instance, ansic::expression)

@given(instance=ansic::constant_strategy)
@settings(max_examples=50)
def test_ansic::constant_instantiation(instance):
    assert isinstance(instance, ansic::constant)

@given(instance=ansic::constant_strategy)
def test_ansic::constant_char_type(instance):
    assert isinstance(instance.char, str)


@given(instance=ansic::constant_strategy)
def test_ansic::constant_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original

@given(instance=ansic::constant_strategy)
def test_ansic::constant_enumz_type(instance):
    assert isinstance(instance.enumz, str)


@given(instance=ansic::constant_strategy)
def test_ansic::constant_enumz_setter(instance):
    original = instance.enumz
    instance.enumz = original
    assert instance.enumz == original

@given(instance=ansic::constant_strategy)
def test_ansic::constant_f_constant_type(instance):
    assert isinstance(instance.f_constant, str)


@given(instance=ansic::constant_strategy)
def test_ansic::constant_f_constant_setter(instance):
    original = instance.f_constant
    instance.f_constant = original
    assert instance.f_constant == original

@given(instance=ansic::constant_strategy)
def test_ansic::constant_i_constant_type(instance):
    assert isinstance(instance.i_constant, int)


@given(instance=ansic::constant_strategy)
def test_ansic::constant_i_constant_setter(instance):
    original = instance.i_constant
    instance.i_constant = original
    assert instance.i_constant == original

@given(instance=ansic::parameter::type::list_strategy)
@settings(max_examples=50)
def test_ansic::parameter::type::list_instantiation(instance):
    assert isinstance(instance, ansic::parameter::type::list)

@given(instance=ansic::assignment::expression_strategy)
@settings(max_examples=50)
def test_ansic::assignment::expression_instantiation(instance):
    assert isinstance(instance, ansic::assignment::expression)

@given(instance=ansic::assignment::expression_strategy)
def test_ansic::assignment::expression_assignment_operator_type(instance):
    assert isinstance(instance.assignment_operator, str)


@given(instance=ansic::assignment::expression_strategy)
def test_ansic::assignment::expression_assignment_operator_setter(instance):
    original = instance.assignment_operator
    instance.assignment_operator = original
    assert instance.assignment_operator == original

@given(instance=ansic::direct::abstract::declarator::complement_strategy)
@settings(max_examples=50)
def test_ansic::direct::abstract::declarator::complement_instantiation(instance):
    assert isinstance(instance, ansic::direct::abstract::declarator::complement)

@given(instance=ansic::initializer::list_strategy)
@settings(max_examples=50)
def test_ansic::initializer::list_instantiation(instance):
    assert isinstance(instance, ansic::initializer::list)

@given(instance=ansic::initializer_strategy)
@settings(max_examples=50)
def test_ansic::initializer_instantiation(instance):
    assert isinstance(instance, ansic::initializer)

@given(instance=ansic::direct::abstract::declarator::linha_strategy)
@settings(max_examples=50)
def test_ansic::direct::abstract::declarator::linha_instantiation(instance):
    assert isinstance(instance, ansic::direct::abstract::declarator::linha)

@given(instance=ansic::direct::abstract::declarator_strategy)
@settings(max_examples=50)
def test_ansic::direct::abstract::declarator_instantiation(instance):
    assert isinstance(instance, ansic::direct::abstract::declarator)

@given(instance=ansic::abstract::declarator_strategy)
@settings(max_examples=50)
def test_ansic::abstract::declarator_instantiation(instance):
    assert isinstance(instance, ansic::abstract::declarator)

@given(instance=ansic::parameter::list::linha_strategy)
@settings(max_examples=50)
def test_ansic::parameter::list::linha_instantiation(instance):
    assert isinstance(instance, ansic::parameter::list::linha)

@given(instance=ansic::parameter::declaration_strategy)
@settings(max_examples=50)
def test_ansic::parameter::declaration_instantiation(instance):
    assert isinstance(instance, ansic::parameter::declaration)

@given(instance=ansic::parameter::lista_strategy)
@settings(max_examples=50)
def test_ansic::parameter::lista_instantiation(instance):
    assert isinstance(instance, ansic::parameter::lista)

@given(instance=ansic::identifier::list_strategy)
@settings(max_examples=50)
def test_ansic::identifier::list_instantiation(instance):
    assert isinstance(instance, ansic::identifier::list)

@given(instance=ansic::identifier::list_strategy)
def test_ansic::identifier::list_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=ansic::identifier::list_strategy)
def test_ansic::identifier::list_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic::direct::declarator::complemento_strategy)
@settings(max_examples=50)
def test_ansic::direct::declarator::complemento_instantiation(instance):
    assert isinstance(instance, ansic::direct::declarator::complemento)

@given(instance=ansic::direct::declarator::linha_strategy)
@settings(max_examples=50)
def test_ansic::direct::declarator::linha_instantiation(instance):
    assert isinstance(instance, ansic::direct::declarator::linha)

@given(instance=ansic::type::qualifier::list::linha_strategy)
@settings(max_examples=50)
def test_ansic::type::qualifier::list::linha_instantiation(instance):
    assert isinstance(instance, ansic::type::qualifier::list::linha)

@given(instance=direct::abstract::declarator::complement_strategy)
@settings(max_examples=50)
def test_direct::abstract::declarator::complement_instantiation(instance):
    assert isinstance(instance, direct::abstract::declarator::complement)

@given(instance=ansic::type::qualifier::list_strategy)
@settings(max_examples=50)
def test_ansic::type::qualifier::list_instantiation(instance):
    assert isinstance(instance, ansic::type::qualifier::list)

@given(instance=ansic::direct::declarator_strategy)
@settings(max_examples=50)
def test_ansic::direct::declarator_instantiation(instance):
    assert isinstance(instance, ansic::direct::declarator)

@given(instance=ansic::direct::declarator_strategy)
def test_ansic::direct::declarator_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=ansic::direct::declarator_strategy)
def test_ansic::direct::declarator_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic::pointer_strategy)
@settings(max_examples=50)
def test_ansic::pointer_instantiation(instance):
    assert isinstance(instance, ansic::pointer)

@given(instance=ansic::declaration::list::linha_strategy)
@settings(max_examples=50)
def test_ansic::declaration::list::linha_instantiation(instance):
    assert isinstance(instance, ansic::declaration::list::linha)

@given(instance=ansic::compound::statement_strategy)
@settings(max_examples=50)
def test_ansic::compound::statement_instantiation(instance):
    assert isinstance(instance, ansic::compound::statement)

@given(instance=ansic::declaration::list_strategy)
@settings(max_examples=50)
def test_ansic::declaration::list_instantiation(instance):
    assert isinstance(instance, ansic::declaration::list)

@given(instance=ansic::init::declarator::list_strategy)
@settings(max_examples=50)
def test_ansic::init::declarator::list_instantiation(instance):
    assert isinstance(instance, ansic::init::declarator::list)

@given(instance=ansic::struct::declaration::list_strategy)
@settings(max_examples=50)
def test_ansic::struct::declaration::list_instantiation(instance):
    assert isinstance(instance, ansic::struct::declaration::list)

@given(instance=ansic::declarator_strategy)
@settings(max_examples=50)
def test_ansic::declarator_instantiation(instance):
    assert isinstance(instance, ansic::declarator)

@given(instance=ansic::struct::declarator::list::linha_strategy)
@settings(max_examples=50)
def test_ansic::struct::declarator::list::linha_instantiation(instance):
    assert isinstance(instance, ansic::struct::declarator::list::linha)

@given(instance=ansic::struct::declarator_strategy)
@settings(max_examples=50)
def test_ansic::struct::declarator_instantiation(instance):
    assert isinstance(instance, ansic::struct::declarator)

@given(instance=ansic::static::assert::declaration_strategy)
@settings(max_examples=50)
def test_ansic::static::assert::declaration_instantiation(instance):
    assert isinstance(instance, ansic::static::assert::declaration)

@given(instance=ansic::struct::declarator::list_strategy)
@settings(max_examples=50)
def test_ansic::struct::declarator::list_instantiation(instance):
    assert isinstance(instance, ansic::struct::declarator::list)

@given(instance=ansic::specifier::qualifier::list_strategy)
@settings(max_examples=50)
def test_ansic::specifier::qualifier::list_instantiation(instance):
    assert isinstance(instance, ansic::specifier::qualifier::list)

@given(instance=ansic::struct::declaration::list::linha_strategy)
@settings(max_examples=50)
def test_ansic::struct::declaration::list::linha_instantiation(instance):
    assert isinstance(instance, ansic::struct::declaration::list::linha)

@given(instance=ansic::struct::declaration_strategy)
@settings(max_examples=50)
def test_ansic::struct::declaration_instantiation(instance):
    assert isinstance(instance, ansic::struct::declaration)

@given(instance=translation::unit::linha_strategy)
@settings(max_examples=50)
def test_translation::unit::linha_instantiation(instance):
    assert isinstance(instance, translation::unit::linha)

@given(instance=ansic::TranlationUnitLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic::tranlationunitlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic::TranlationUnitLinhaAction)

@given(instance=init::declarator::list::linha_strategy)
@settings(max_examples=50)
def test_init::declarator::list::linha_instantiation(instance):
    assert isinstance(instance, init::declarator::list::linha)

@given(instance=ansic::InitDecclaratorListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic::initdecclaratorlistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic::InitDecclaratorListLinhaAction)

@given(instance=unary::expression_strategy)
@settings(max_examples=50)
def test_unary::expression_instantiation(instance):
    assert isinstance(instance, unary::expression)

@given(instance=ansic::PlusPlus_strategy)
@settings(max_examples=50)
def test_ansic::plusplus_instantiation(instance):
    assert isinstance(instance, ansic::PlusPlus)

@given(instance=ansic::PlusPlus_strategy)
def test_ansic::plusplus_plus_type(instance):
    assert isinstance(instance.plus, str)


@given(instance=ansic::PlusPlus_strategy)
def test_ansic::plusplus_plus_setter(instance):
    original = instance.plus
    instance.plus = original
    assert instance.plus == original

@given(instance=argument::expression::list::linha_strategy)
@settings(max_examples=50)
def test_argument::expression::list::linha_instantiation(instance):
    assert isinstance(instance, argument::expression::list::linha)

@given(instance=ansic::ArgumentExpressionListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic::argumentexpressionlistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic::ArgumentExpressionListLinhaAction)

@given(instance=postfix::expression::complement_strategy)
@settings(max_examples=50)
def test_postfix::expression::complement_instantiation(instance):
    assert isinstance(instance, postfix::expression::complement)

@given(instance=ansic::PostFixEmpryParams_strategy)
@settings(max_examples=50)
def test_ansic::postfixempryparams_instantiation(instance):
    assert isinstance(instance, ansic::PostFixEmpryParams)

@given(instance=designator::list::linha_strategy)
@settings(max_examples=50)
def test_designator::list::linha_instantiation(instance):
    assert isinstance(instance, designator::list::linha)

@given(instance=ansic::DesignatorListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic::designatorlistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic::DesignatorListLinhaAction)

@given(instance=initializer::list::linha_strategy)
@settings(max_examples=50)
def test_initializer::list::linha_instantiation(instance):
    assert isinstance(instance, initializer::list::linha)

@given(instance=ansic::InitializerListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic::initializerlistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic::InitializerListLinhaAction)

@given(instance=postfix::expression::linha_strategy)
@settings(max_examples=50)
def test_postfix::expression::linha_instantiation(instance):
    assert isinstance(instance, postfix::expression::linha)

@given(instance=ansic::PostfixExpressionLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic::postfixexpressionlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic::PostfixExpressionLinhaAction)

@given(instance=generic::assoc::list::linha_strategy)
@settings(max_examples=50)
def test_generic::assoc::list::linha_instantiation(instance):
    assert isinstance(instance, generic::assoc::list::linha)

@given(instance=ansic::GenericAssocListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic::genericassoclistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic::GenericAssocListLinhaAction)

@given(instance=ansic::string::ufcg_strategy)
@settings(max_examples=50)
def test_ansic::string::ufcg_instantiation(instance):
    assert isinstance(instance, ansic::string::ufcg)

@given(instance=ansic::string::ufcg_strategy)
def test_ansic::string::ufcg___func___type(instance):
    assert isinstance(instance.__func__, str)


@given(instance=ansic::string::ufcg_strategy)
def test_ansic::string::ufcg___func___setter(instance):
    original = instance.__func__
    instance.__func__ = original
    assert instance.__func__ == original

@given(instance=ansic::string::ufcg_strategy)
def test_ansic::string::ufcg_string_literal_type(instance):
    assert isinstance(instance.string_literal, str)


@given(instance=ansic::string::ufcg_strategy)
def test_ansic::string::ufcg_string_literal_setter(instance):
    original = instance.string_literal
    instance.string_literal = original
    assert instance.string_literal == original

@given(instance=identifier::list::linha_strategy)
@settings(max_examples=50)
def test_identifier::list::linha_instantiation(instance):
    assert isinstance(instance, identifier::list::linha)

@given(instance=ansic::IdentifierListLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic::identifierlistlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic::IdentifierListLinhaAction)

@given(instance=ansic::IdentifierListLinhaAction_strategy)
def test_ansic::identifierlistlinhaaction_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=ansic::IdentifierListLinhaAction_strategy)
def test_ansic::identifierlistlinhaaction_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=direct::abstract::declarator::linha_strategy)
@settings(max_examples=50)
def test_direct::abstract::declarator::linha_instantiation(instance):
    assert isinstance(instance, direct::abstract::declarator::linha)

@given(instance=ansic::DirectAbstractDeclarratorLinhaAction_strategy)
@settings(max_examples=50)
def test_ansic::directabstractdeclarratorlinhaaction_instantiation(instance):
    assert isinstance(instance, ansic::DirectAbstractDeclarratorLinhaAction)

@given(instance=ansic::struct::or::union::specifier::complement_strategy)
@settings(max_examples=50)
def test_ansic::struct::or::union::specifier::complement_instantiation(instance):
    assert isinstance(instance, ansic::struct::or::union::specifier::complement)

@given(instance=ansic::declaration_strategy)
@settings(max_examples=50)
def test_ansic::declaration_instantiation(instance):
    assert isinstance(instance, ansic::declaration)

@given(instance=ansic::function::definition_strategy)
@settings(max_examples=50)
def test_ansic::function::definition_instantiation(instance):
    assert isinstance(instance, ansic::function::definition)

@given(instance=ansic::translation::unit::linha_strategy)
@settings(max_examples=50)
def test_ansic::translation::unit::linha_instantiation(instance):
    assert isinstance(instance, ansic::translation::unit::linha)

@given(instance=ansic::enumeration::constant_strategy)
@settings(max_examples=50)
def test_ansic::enumeration::constant_instantiation(instance):
    assert isinstance(instance, ansic::enumeration::constant)

@given(instance=ansic::enumeration::constant_strategy)
def test_ansic::enumeration::constant_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=ansic::enumeration::constant_strategy)
def test_ansic::enumeration::constant_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic::enumerator::list::linha_strategy)
@settings(max_examples=50)
def test_ansic::enumerator::list::linha_instantiation(instance):
    assert isinstance(instance, ansic::enumerator::list::linha)

@given(instance=ansic::enumerator_strategy)
@settings(max_examples=50)
def test_ansic::enumerator_instantiation(instance):
    assert isinstance(instance, ansic::enumerator)

@given(instance=ansic::enumerator::list_strategy)
@settings(max_examples=50)
def test_ansic::enumerator::list_instantiation(instance):
    assert isinstance(instance, ansic::enumerator::list)

@given(instance=ansic::enum::specifier_strategy)
@settings(max_examples=50)
def test_ansic::enum::specifier_instantiation(instance):
    assert isinstance(instance, ansic::enum::specifier)

@given(instance=ansic::enum::specifier_strategy)
def test_ansic::enum::specifier_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=ansic::enum::specifier_strategy)
def test_ansic::enum::specifier_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic::struct::or::union::specifier_strategy)
@settings(max_examples=50)
def test_ansic::struct::or::union::specifier_instantiation(instance):
    assert isinstance(instance, ansic::struct::or::union::specifier)

@given(instance=ansic::struct::or::union::specifier_strategy)
def test_ansic::struct::or::union::specifier_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=ansic::struct::or::union::specifier_strategy)
def test_ansic::struct::or::union::specifier_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=ansic::struct::or::union::specifier_strategy)
def test_ansic::struct::or::union::specifier_struct_or_union_type(instance):
    assert isinstance(instance.struct_or_union, str)


@given(instance=ansic::struct::or::union::specifier_strategy)
def test_ansic::struct::or::union::specifier_struct_or_union_setter(instance):
    original = instance.struct_or_union
    instance.struct_or_union = original
    assert instance.struct_or_union == original

@given(instance=ansic::atomic::type::specifier_strategy)
@settings(max_examples=50)
def test_ansic::atomic::type::specifier_instantiation(instance):
    assert isinstance(instance, ansic::atomic::type::specifier)

@given(instance=ansic::constant::expression_strategy)
@settings(max_examples=50)
def test_ansic::constant::expression_instantiation(instance):
    assert isinstance(instance, ansic::constant::expression)

@given(instance=ansic::type::name_strategy)
@settings(max_examples=50)
def test_ansic::type::name_instantiation(instance):
    assert isinstance(instance, ansic::type::name)

@given(instance=ansic::alignment::specifier_strategy)
@settings(max_examples=50)
def test_ansic::alignment::specifier_instantiation(instance):
    assert isinstance(instance, ansic::alignment::specifier)

@given(instance=ansic::type::qualifier_strategy)
@settings(max_examples=50)
def test_ansic::type::qualifier_instantiation(instance):
    assert isinstance(instance, ansic::type::qualifier)

@given(instance=ansic::type::qualifier_strategy)
def test_ansic::type::qualifier_namez_type(instance):
    assert isinstance(instance.namez, str)


@given(instance=ansic::type::qualifier_strategy)
def test_ansic::type::qualifier_namez_setter(instance):
    original = instance.namez
    instance.namez = original
    assert instance.namez == original

@given(instance=ansic::type::specifier_strategy)
@settings(max_examples=50)
def test_ansic::type::specifier_instantiation(instance):
    assert isinstance(instance, ansic::type::specifier)

@given(instance=ansic::type::specifier_strategy)
def test_ansic::type::specifier_type_name_str_type(instance):
    assert isinstance(instance.type_name_str, str)


@given(instance=ansic::type::specifier_strategy)
def test_ansic::type::specifier_type_name_str_setter(instance):
    original = instance.type_name_str
    instance.type_name_str = original
    assert instance.type_name_str == original

@given(instance=ansic::declaration::specifiers_strategy)
@settings(max_examples=50)
def test_ansic::declaration::specifiers_instantiation(instance):
    assert isinstance(instance, ansic::declaration::specifiers)

@given(instance=ansic::declaration::specifiers_strategy)
def test_ansic::declaration::specifiers_storage_class_specifier_type(instance):
    assert isinstance(instance.storage_class_specifier, str)


@given(instance=ansic::declaration::specifiers_strategy)
def test_ansic::declaration::specifiers_storage_class_specifier_setter(instance):
    original = instance.storage_class_specifier
    instance.storage_class_specifier = original
    assert instance.storage_class_specifier == original

@given(instance=ansic::declaration::specifiers_strategy)
def test_ansic::declaration::specifiers_function_specifier_type(instance):
    assert isinstance(instance.function_specifier, str)


@given(instance=ansic::declaration::specifiers_strategy)
def test_ansic::declaration::specifiers_function_specifier_setter(instance):
    original = instance.function_specifier
    instance.function_specifier = original
    assert instance.function_specifier == original

@given(instance=ansic::external::declaration_strategy)
@settings(max_examples=50)
def test_ansic::external::declaration_instantiation(instance):
    assert isinstance(instance, ansic::external::declaration)

@given(instance=ansic::translation::unit_strategy)
@settings(max_examples=50)
def test_ansic::translation::unit_instantiation(instance):
    assert isinstance(instance, ansic::translation::unit)

@given(instance=ansic::DomainModel_strategy)
@settings(max_examples=50)
def test_ansic::domainmodel_instantiation(instance):
    assert isinstance(instance, ansic::DomainModel)

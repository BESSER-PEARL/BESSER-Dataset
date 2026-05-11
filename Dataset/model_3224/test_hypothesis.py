import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    argument::expression::list::linha,
    myDsl::ArgumentExpressionListLinhaAction,
    postfix::expression::complement,
    myDsl::PostFixEmpryParams,
    designator::list::linha,
    myDsl::DesignatorListLinhaAction,
    initializer::list::linha,
    myDsl::InitializerListLinhaAction,
    init::declarator::list::linha,
    myDsl::InitDecclaratorListLinhaAction,
    unary::expression,
    myDsl::PlusPlus,
    direct::abstract::declarator::linha,
    myDsl::DirectAbstractDeclarratorLinhaAction,
    type::qualifier::list::linha,
    myDsl::TypeQualifierListLinhaAtion,
    declaration::list::linha,
    myDsl::DeclarationListLinhaAction,
    struct::declarator::list::linha,
    myDsl::StructDeclaratorListLinhaAction,
    postfix::expression::linha,
    myDsl::PostfixExpressionLinhaAction,
    generic::assoc::list::linha,
    myDsl::GenericAssocListLinhaAction,
    translation::unit::linha,
    myDsl::TranlationUnitLinhaAction,
    identifier::list::linha,
    myDsl::IdentifierListLinhaAction,
    myDsl::init::declarator,
    myDsl::expression::linha,
    struct::declaration::list::linha,
    myDsl::StructDeclarationListLinhaAction,
    struct::or::union::specifier::complement,
    myDsl::StructOrUnionSpecifierComplementAction,
    enumerator::list::linha,
    myDsl::EnumeratorListLinhaAction,
    myDsl::string::dsl,
    myDsl::conditional::expression::linha,
    myDsl::logical::or::expression::linha,
    myDsl::logical::or::expression,
    myDsl::logical::and::expression::linha,
    myDsl::logical::and::expression,
    postfix::expression,
    myDsl::block::item::list::linha,
    myDsl::block::item,
    myDsl::block::item::list,
    myDsl::inclusive::or::expression::linha,
    myDsl::inclusive::or::expression,
    myDsl::exclusive::or::expression::linha,
    myDsl::exclusive::or::expression,
    myDsl::and::expression::linha,
    myDsl::and::expression,
    myDsl::jump::statement,
    myDsl::iteration::statement,
    myDsl::selection::statement,
    myDsl::expression::statement,
    myDsl::labeled::statement,
    myDsl::statement,
    myDsl::shift::expression::complement,
    myDsl::shift::expression::linha,
    myDsl::shift::expression,
    myDsl::additive::expression::complement,
    myDsl::additive::expression::linha,
    myDsl::equality::expression::complement,
    myDsl::equality::expression::linha,
    myDsl::equality::expression,
    myDsl::relational::expression::complement,
    myDsl::relational::expression::linha,
    myDsl::relational::expression,
    myDsl::additive::expression,
    myDsl::multiplicative::expression::complement,
    myDsl::multiplicative::expression::linha,
    myDsl::multiplicative::expression,
    myDsl::cast::expression,
    myDsl::unary::expression,
    myDsl::argument::expression::list::linha,
    myDsl::argument::expression::list,
    myDsl::postfix::expression::complement,
    myDsl::conditional::expression,
    myDsl::designator::list::linha,
    myDsl::designator,
    myDsl::designator::list,
    myDsl::initializer::list::complement,
    myDsl::initializer::list::linha,
    myDsl::init::declarator::list::linha,
    myDsl::designation,
    myDsl::postfix::expression::linha,
    myDsl::postfix::expression,
    myDsl::generic::assoc::list::linha,
    myDsl::generic::association,
    myDsl::generic::assoc::list,
    myDsl::generic::selection,
    myDsl::expression,
    myDsl::constant,
    myDsl::primary::expression,
    myDsl::identifier::list::linha,
    myDsl::direct::abstract::declarator::complement,
    myDsl::initializer::list,
    myDsl::initializer,
    myDsl::direct::abstract::declarator::linha,
    myDsl::direct::abstract::declarator,
    myDsl::abstract::declarator,
    myDsl::parameter::list::linha,
    myDsl::parameter::declaration,
    myDsl::identifier::list,
    myDsl::parameter::type::list,
    myDsl::assignment::expression,
    myDsl::direct::declarator::complemento,
    myDsl::direct::declarator::linha,
    myDsl::type::qualifier::list::linha,
    direct::abstract::declarator::complement,
    myDsl::type::qualifier::list,
    myDsl::direct::declarator,
    myDsl::pointer,
    myDsl::declaration::list::linha,
    myDsl::compound::statement,
    myDsl::declaration::list,
    myDsl::parameter::lista,
    myDsl::init::declarator::list,
    myDsl::declarator,
    myDsl::struct::declarator::list::linha,
    myDsl::struct::declarator,
    myDsl::static::assert::declaration,
    myDsl::struct::declarator::list,
    myDsl::specifier::qualifier::list,
    myDsl::struct::declaration::list::linha,
    myDsl::struct::declaration,
    myDsl::struct::or::union::specifier::complement,
    myDsl::struct::declaration::list,
    myDsl::enumeration::constant,
    myDsl::enumerator::list::linha,
    myDsl::enumerator,
    myDsl::enumerator::list,
    myDsl::enum::specifier,
    myDsl::struct::or::union::specifier,
    myDsl::atomic::type::specifier,
    myDsl::constant::expression,
    myDsl::type::name,
    myDsl::alignment::specifier,
    myDsl::type::qualifier,
    myDsl::type::specifier,
    myDsl::declaration::specifiers,
    myDsl::declaration,
    myDsl::function::definition,
    myDsl::translation::unit::linha,
    myDsl::external::declaration,
    myDsl::translation::unit,
    myDsl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_argument::expression::list::linha_is_not_abstract():
    assert not inspect.isabstract(argument::expression::list::linha)


def test_argument::expression::list::linha_constructor_exists():
    assert callable(argument::expression::list::linha.__init__)


def test_argument::expression::list::linha_constructor_args():
    sig = inspect.signature(argument::expression::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::argumentexpressionlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl::ArgumentExpressionListLinhaAction)


def test_mydsl::argumentexpressionlistlinhaaction_constructor_exists():
    assert callable(myDsl::ArgumentExpressionListLinhaAction.__init__)


def test_mydsl::argumentexpressionlistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl::ArgumentExpressionListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_postfix::expression::complement_is_not_abstract():
    assert not inspect.isabstract(postfix::expression::complement)


def test_postfix::expression::complement_constructor_exists():
    assert callable(postfix::expression::complement.__init__)


def test_postfix::expression::complement_constructor_args():
    sig = inspect.signature(postfix::expression::complement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::postfixempryparams_is_not_abstract():
    assert not inspect.isabstract(myDsl::PostFixEmpryParams)


def test_mydsl::postfixempryparams_constructor_exists():
    assert callable(myDsl::PostFixEmpryParams.__init__)


def test_mydsl::postfixempryparams_constructor_args():
    sig = inspect.signature(myDsl::PostFixEmpryParams.__init__)
    params = list(sig.parameters.keys())



def test_designator::list::linha_is_not_abstract():
    assert not inspect.isabstract(designator::list::linha)


def test_designator::list::linha_constructor_exists():
    assert callable(designator::list::linha.__init__)


def test_designator::list::linha_constructor_args():
    sig = inspect.signature(designator::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::designatorlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl::DesignatorListLinhaAction)


def test_mydsl::designatorlistlinhaaction_constructor_exists():
    assert callable(myDsl::DesignatorListLinhaAction.__init__)


def test_mydsl::designatorlistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl::DesignatorListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_initializer::list::linha_is_not_abstract():
    assert not inspect.isabstract(initializer::list::linha)


def test_initializer::list::linha_constructor_exists():
    assert callable(initializer::list::linha.__init__)


def test_initializer::list::linha_constructor_args():
    sig = inspect.signature(initializer::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::initializerlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl::InitializerListLinhaAction)


def test_mydsl::initializerlistlinhaaction_constructor_exists():
    assert callable(myDsl::InitializerListLinhaAction.__init__)


def test_mydsl::initializerlistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl::InitializerListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_init::declarator::list::linha_is_not_abstract():
    assert not inspect.isabstract(init::declarator::list::linha)


def test_init::declarator::list::linha_constructor_exists():
    assert callable(init::declarator::list::linha.__init__)


def test_init::declarator::list::linha_constructor_args():
    sig = inspect.signature(init::declarator::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::initdecclaratorlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl::InitDecclaratorListLinhaAction)


def test_mydsl::initdecclaratorlistlinhaaction_constructor_exists():
    assert callable(myDsl::InitDecclaratorListLinhaAction.__init__)


def test_mydsl::initdecclaratorlistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl::InitDecclaratorListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_unary::expression_is_not_abstract():
    assert not inspect.isabstract(unary::expression)


def test_unary::expression_constructor_exists():
    assert callable(unary::expression.__init__)


def test_unary::expression_constructor_args():
    sig = inspect.signature(unary::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::plusplus_is_not_abstract():
    assert not inspect.isabstract(myDsl::PlusPlus)


def test_mydsl::plusplus_constructor_exists():
    assert callable(myDsl::PlusPlus.__init__)


def test_mydsl::plusplus_constructor_args():
    sig = inspect.signature(myDsl::PlusPlus.__init__)
    params = list(sig.parameters.keys())
    assert "plus" in params, "Missing parameter 'plus'"

def test_mydsl::plusplus_has_plus():
    assert hasattr(myDsl::PlusPlus, "plus")
    descriptor = None
    for klass in myDsl::PlusPlus.__mro__:
        if "plus" in klass.__dict__:
            descriptor = klass.__dict__["plus"]
            break
    assert isinstance(descriptor, property)



def test_direct::abstract::declarator::linha_is_not_abstract():
    assert not inspect.isabstract(direct::abstract::declarator::linha)


def test_direct::abstract::declarator::linha_constructor_exists():
    assert callable(direct::abstract::declarator::linha.__init__)


def test_direct::abstract::declarator::linha_constructor_args():
    sig = inspect.signature(direct::abstract::declarator::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::directabstractdeclarratorlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl::DirectAbstractDeclarratorLinhaAction)


def test_mydsl::directabstractdeclarratorlinhaaction_constructor_exists():
    assert callable(myDsl::DirectAbstractDeclarratorLinhaAction.__init__)


def test_mydsl::directabstractdeclarratorlinhaaction_constructor_args():
    sig = inspect.signature(myDsl::DirectAbstractDeclarratorLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_type::qualifier::list::linha_is_not_abstract():
    assert not inspect.isabstract(type::qualifier::list::linha)


def test_type::qualifier::list::linha_constructor_exists():
    assert callable(type::qualifier::list::linha.__init__)


def test_type::qualifier::list::linha_constructor_args():
    sig = inspect.signature(type::qualifier::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::typequalifierlistlinhaation_is_not_abstract():
    assert not inspect.isabstract(myDsl::TypeQualifierListLinhaAtion)


def test_mydsl::typequalifierlistlinhaation_constructor_exists():
    assert callable(myDsl::TypeQualifierListLinhaAtion.__init__)


def test_mydsl::typequalifierlistlinhaation_constructor_args():
    sig = inspect.signature(myDsl::TypeQualifierListLinhaAtion.__init__)
    params = list(sig.parameters.keys())



def test_declaration::list::linha_is_not_abstract():
    assert not inspect.isabstract(declaration::list::linha)


def test_declaration::list::linha_constructor_exists():
    assert callable(declaration::list::linha.__init__)


def test_declaration::list::linha_constructor_args():
    sig = inspect.signature(declaration::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::declarationlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl::DeclarationListLinhaAction)


def test_mydsl::declarationlistlinhaaction_constructor_exists():
    assert callable(myDsl::DeclarationListLinhaAction.__init__)


def test_mydsl::declarationlistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl::DeclarationListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_struct::declarator::list::linha_is_not_abstract():
    assert not inspect.isabstract(struct::declarator::list::linha)


def test_struct::declarator::list::linha_constructor_exists():
    assert callable(struct::declarator::list::linha.__init__)


def test_struct::declarator::list::linha_constructor_args():
    sig = inspect.signature(struct::declarator::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::structdeclaratorlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl::StructDeclaratorListLinhaAction)


def test_mydsl::structdeclaratorlistlinhaaction_constructor_exists():
    assert callable(myDsl::StructDeclaratorListLinhaAction.__init__)


def test_mydsl::structdeclaratorlistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl::StructDeclaratorListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_postfix::expression::linha_is_not_abstract():
    assert not inspect.isabstract(postfix::expression::linha)


def test_postfix::expression::linha_constructor_exists():
    assert callable(postfix::expression::linha.__init__)


def test_postfix::expression::linha_constructor_args():
    sig = inspect.signature(postfix::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::postfixexpressionlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl::PostfixExpressionLinhaAction)


def test_mydsl::postfixexpressionlinhaaction_constructor_exists():
    assert callable(myDsl::PostfixExpressionLinhaAction.__init__)


def test_mydsl::postfixexpressionlinhaaction_constructor_args():
    sig = inspect.signature(myDsl::PostfixExpressionLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_generic::assoc::list::linha_is_not_abstract():
    assert not inspect.isabstract(generic::assoc::list::linha)


def test_generic::assoc::list::linha_constructor_exists():
    assert callable(generic::assoc::list::linha.__init__)


def test_generic::assoc::list::linha_constructor_args():
    sig = inspect.signature(generic::assoc::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::genericassoclistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl::GenericAssocListLinhaAction)


def test_mydsl::genericassoclistlinhaaction_constructor_exists():
    assert callable(myDsl::GenericAssocListLinhaAction.__init__)


def test_mydsl::genericassoclistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl::GenericAssocListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_translation::unit::linha_is_not_abstract():
    assert not inspect.isabstract(translation::unit::linha)


def test_translation::unit::linha_constructor_exists():
    assert callable(translation::unit::linha.__init__)


def test_translation::unit::linha_constructor_args():
    sig = inspect.signature(translation::unit::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::tranlationunitlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl::TranlationUnitLinhaAction)


def test_mydsl::tranlationunitlinhaaction_constructor_exists():
    assert callable(myDsl::TranlationUnitLinhaAction.__init__)


def test_mydsl::tranlationunitlinhaaction_constructor_args():
    sig = inspect.signature(myDsl::TranlationUnitLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_identifier::list::linha_is_not_abstract():
    assert not inspect.isabstract(identifier::list::linha)


def test_identifier::list::linha_constructor_exists():
    assert callable(identifier::list::linha.__init__)


def test_identifier::list::linha_constructor_args():
    sig = inspect.signature(identifier::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::identifierlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl::IdentifierListLinhaAction)


def test_mydsl::identifierlistlinhaaction_constructor_exists():
    assert callable(myDsl::IdentifierListLinhaAction.__init__)


def test_mydsl::identifierlistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl::IdentifierListLinhaAction.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl::identifierlistlinhaaction_has_identifier():
    assert hasattr(myDsl::IdentifierListLinhaAction, "identifier")
    descriptor = None
    for klass in myDsl::IdentifierListLinhaAction.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::init::declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl::init::declarator)


def test_mydsl::init::declarator_constructor_exists():
    assert callable(myDsl::init::declarator.__init__)


def test_mydsl::init::declarator_constructor_args():
    sig = inspect.signature(myDsl::init::declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::expression::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::expression::linha)


def test_mydsl::expression::linha_constructor_exists():
    assert callable(myDsl::expression::linha.__init__)


def test_mydsl::expression::linha_constructor_args():
    sig = inspect.signature(myDsl::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_struct::declaration::list::linha_is_not_abstract():
    assert not inspect.isabstract(struct::declaration::list::linha)


def test_struct::declaration::list::linha_constructor_exists():
    assert callable(struct::declaration::list::linha.__init__)


def test_struct::declaration::list::linha_constructor_args():
    sig = inspect.signature(struct::declaration::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::structdeclarationlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl::StructDeclarationListLinhaAction)


def test_mydsl::structdeclarationlistlinhaaction_constructor_exists():
    assert callable(myDsl::StructDeclarationListLinhaAction.__init__)


def test_mydsl::structdeclarationlistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl::StructDeclarationListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_struct::or::union::specifier::complement_is_not_abstract():
    assert not inspect.isabstract(struct::or::union::specifier::complement)


def test_struct::or::union::specifier::complement_constructor_exists():
    assert callable(struct::or::union::specifier::complement.__init__)


def test_struct::or::union::specifier::complement_constructor_args():
    sig = inspect.signature(struct::or::union::specifier::complement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::structorunionspecifiercomplementaction_is_not_abstract():
    assert not inspect.isabstract(myDsl::StructOrUnionSpecifierComplementAction)


def test_mydsl::structorunionspecifiercomplementaction_constructor_exists():
    assert callable(myDsl::StructOrUnionSpecifierComplementAction.__init__)


def test_mydsl::structorunionspecifiercomplementaction_constructor_args():
    sig = inspect.signature(myDsl::StructOrUnionSpecifierComplementAction.__init__)
    params = list(sig.parameters.keys())



def test_enumerator::list::linha_is_not_abstract():
    assert not inspect.isabstract(enumerator::list::linha)


def test_enumerator::list::linha_constructor_exists():
    assert callable(enumerator::list::linha.__init__)


def test_enumerator::list::linha_constructor_args():
    sig = inspect.signature(enumerator::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::enumeratorlistlinhaaction_is_not_abstract():
    assert not inspect.isabstract(myDsl::EnumeratorListLinhaAction)


def test_mydsl::enumeratorlistlinhaaction_constructor_exists():
    assert callable(myDsl::EnumeratorListLinhaAction.__init__)


def test_mydsl::enumeratorlistlinhaaction_constructor_args():
    sig = inspect.signature(myDsl::EnumeratorListLinhaAction.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::string::dsl_is_not_abstract():
    assert not inspect.isabstract(myDsl::string::dsl)


def test_mydsl::string::dsl_constructor_exists():
    assert callable(myDsl::string::dsl.__init__)


def test_mydsl::string::dsl_constructor_args():
    sig = inspect.signature(myDsl::string::dsl.__init__)
    params = list(sig.parameters.keys())
    assert "string_literal" in params, "Missing parameter 'string_literal'"
    assert "__func__" in params, "Missing parameter '__func__'"

def test_mydsl::string::dsl_has_string_literal():
    assert hasattr(myDsl::string::dsl, "string_literal")
    descriptor = None
    for klass in myDsl::string::dsl.__mro__:
        if "string_literal" in klass.__dict__:
            descriptor = klass.__dict__["string_literal"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::string::dsl_has___func__():
    assert hasattr(myDsl::string::dsl, "__func__")
    descriptor = None
    for klass in myDsl::string::dsl.__mro__:
        if "__func__" in klass.__dict__:
            descriptor = klass.__dict__["__func__"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::conditional::expression::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::conditional::expression::linha)


def test_mydsl::conditional::expression::linha_constructor_exists():
    assert callable(myDsl::conditional::expression::linha.__init__)


def test_mydsl::conditional::expression::linha_constructor_args():
    sig = inspect.signature(myDsl::conditional::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::logical::or::expression::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::logical::or::expression::linha)


def test_mydsl::logical::or::expression::linha_constructor_exists():
    assert callable(myDsl::logical::or::expression::linha.__init__)


def test_mydsl::logical::or::expression::linha_constructor_args():
    sig = inspect.signature(myDsl::logical::or::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::logical::or::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::logical::or::expression)


def test_mydsl::logical::or::expression_constructor_exists():
    assert callable(myDsl::logical::or::expression.__init__)


def test_mydsl::logical::or::expression_constructor_args():
    sig = inspect.signature(myDsl::logical::or::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::logical::and::expression::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::logical::and::expression::linha)


def test_mydsl::logical::and::expression::linha_constructor_exists():
    assert callable(myDsl::logical::and::expression::linha.__init__)


def test_mydsl::logical::and::expression::linha_constructor_args():
    sig = inspect.signature(myDsl::logical::and::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::logical::and::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::logical::and::expression)


def test_mydsl::logical::and::expression_constructor_exists():
    assert callable(myDsl::logical::and::expression.__init__)


def test_mydsl::logical::and::expression_constructor_args():
    sig = inspect.signature(myDsl::logical::and::expression.__init__)
    params = list(sig.parameters.keys())



def test_postfix::expression_is_not_abstract():
    assert not inspect.isabstract(postfix::expression)


def test_postfix::expression_constructor_exists():
    assert callable(postfix::expression.__init__)


def test_postfix::expression_constructor_args():
    sig = inspect.signature(postfix::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::block::item::list::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::block::item::list::linha)


def test_mydsl::block::item::list::linha_constructor_exists():
    assert callable(myDsl::block::item::list::linha.__init__)


def test_mydsl::block::item::list::linha_constructor_args():
    sig = inspect.signature(myDsl::block::item::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::block::item_is_not_abstract():
    assert not inspect.isabstract(myDsl::block::item)


def test_mydsl::block::item_constructor_exists():
    assert callable(myDsl::block::item.__init__)


def test_mydsl::block::item_constructor_args():
    sig = inspect.signature(myDsl::block::item.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::block::item::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::block::item::list)


def test_mydsl::block::item::list_constructor_exists():
    assert callable(myDsl::block::item::list.__init__)


def test_mydsl::block::item::list_constructor_args():
    sig = inspect.signature(myDsl::block::item::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::inclusive::or::expression::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::inclusive::or::expression::linha)


def test_mydsl::inclusive::or::expression::linha_constructor_exists():
    assert callable(myDsl::inclusive::or::expression::linha.__init__)


def test_mydsl::inclusive::or::expression::linha_constructor_args():
    sig = inspect.signature(myDsl::inclusive::or::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::inclusive::or::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::inclusive::or::expression)


def test_mydsl::inclusive::or::expression_constructor_exists():
    assert callable(myDsl::inclusive::or::expression.__init__)


def test_mydsl::inclusive::or::expression_constructor_args():
    sig = inspect.signature(myDsl::inclusive::or::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::exclusive::or::expression::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::exclusive::or::expression::linha)


def test_mydsl::exclusive::or::expression::linha_constructor_exists():
    assert callable(myDsl::exclusive::or::expression::linha.__init__)


def test_mydsl::exclusive::or::expression::linha_constructor_args():
    sig = inspect.signature(myDsl::exclusive::or::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::exclusive::or::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::exclusive::or::expression)


def test_mydsl::exclusive::or::expression_constructor_exists():
    assert callable(myDsl::exclusive::or::expression.__init__)


def test_mydsl::exclusive::or::expression_constructor_args():
    sig = inspect.signature(myDsl::exclusive::or::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::and::expression::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::and::expression::linha)


def test_mydsl::and::expression::linha_constructor_exists():
    assert callable(myDsl::and::expression::linha.__init__)


def test_mydsl::and::expression::linha_constructor_args():
    sig = inspect.signature(myDsl::and::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::and::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::and::expression)


def test_mydsl::and::expression_constructor_exists():
    assert callable(myDsl::and::expression.__init__)


def test_mydsl::and::expression_constructor_args():
    sig = inspect.signature(myDsl::and::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::jump::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::jump::statement)


def test_mydsl::jump::statement_constructor_exists():
    assert callable(myDsl::jump::statement.__init__)


def test_mydsl::jump::statement_constructor_args():
    sig = inspect.signature(myDsl::jump::statement.__init__)
    params = list(sig.parameters.keys())
    assert "return_" in params, "Missing parameter 'return_'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "break_" in params, "Missing parameter 'break_'"
    assert "return_vazio" in params, "Missing parameter 'return_vazio'"

def test_mydsl::jump::statement_has_return_():
    assert hasattr(myDsl::jump::statement, "return_")
    descriptor = None
    for klass in myDsl::jump::statement.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::jump::statement_has_identifier():
    assert hasattr(myDsl::jump::statement, "identifier")
    descriptor = None
    for klass in myDsl::jump::statement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::jump::statement_has_break_():
    assert hasattr(myDsl::jump::statement, "break_")
    descriptor = None
    for klass in myDsl::jump::statement.__mro__:
        if "break_" in klass.__dict__:
            descriptor = klass.__dict__["break_"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::jump::statement_has_return_vazio():
    assert hasattr(myDsl::jump::statement, "return_vazio")
    descriptor = None
    for klass in myDsl::jump::statement.__mro__:
        if "return_vazio" in klass.__dict__:
            descriptor = klass.__dict__["return_vazio"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::iteration::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::iteration::statement)


def test_mydsl::iteration::statement_constructor_exists():
    assert callable(myDsl::iteration::statement.__init__)


def test_mydsl::iteration::statement_constructor_args():
    sig = inspect.signature(myDsl::iteration::statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::selection::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::selection::statement)


def test_mydsl::selection::statement_constructor_exists():
    assert callable(myDsl::selection::statement.__init__)


def test_mydsl::selection::statement_constructor_args():
    sig = inspect.signature(myDsl::selection::statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::expression::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::expression::statement)


def test_mydsl::expression::statement_constructor_exists():
    assert callable(myDsl::expression::statement.__init__)


def test_mydsl::expression::statement_constructor_args():
    sig = inspect.signature(myDsl::expression::statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::labeled::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::labeled::statement)


def test_mydsl::labeled::statement_constructor_exists():
    assert callable(myDsl::labeled::statement.__init__)


def test_mydsl::labeled::statement_constructor_args():
    sig = inspect.signature(myDsl::labeled::statement.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl::labeled::statement_has_identifier():
    assert hasattr(myDsl::labeled::statement, "identifier")
    descriptor = None
    for klass in myDsl::labeled::statement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::statement)


def test_mydsl::statement_constructor_exists():
    assert callable(myDsl::statement.__init__)


def test_mydsl::statement_constructor_args():
    sig = inspect.signature(myDsl::statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::shift::expression::complement_is_not_abstract():
    assert not inspect.isabstract(myDsl::shift::expression::complement)


def test_mydsl::shift::expression::complement_constructor_exists():
    assert callable(myDsl::shift::expression::complement.__init__)


def test_mydsl::shift::expression::complement_constructor_args():
    sig = inspect.signature(myDsl::shift::expression::complement.__init__)
    params = list(sig.parameters.keys())
    assert "sright" in params, "Missing parameter 'sright'"
    assert "sleft" in params, "Missing parameter 'sleft'"

def test_mydsl::shift::expression::complement_has_sright():
    assert hasattr(myDsl::shift::expression::complement, "sright")
    descriptor = None
    for klass in myDsl::shift::expression::complement.__mro__:
        if "sright" in klass.__dict__:
            descriptor = klass.__dict__["sright"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::shift::expression::complement_has_sleft():
    assert hasattr(myDsl::shift::expression::complement, "sleft")
    descriptor = None
    for klass in myDsl::shift::expression::complement.__mro__:
        if "sleft" in klass.__dict__:
            descriptor = klass.__dict__["sleft"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::shift::expression::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::shift::expression::linha)


def test_mydsl::shift::expression::linha_constructor_exists():
    assert callable(myDsl::shift::expression::linha.__init__)


def test_mydsl::shift::expression::linha_constructor_args():
    sig = inspect.signature(myDsl::shift::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::shift::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::shift::expression)


def test_mydsl::shift::expression_constructor_exists():
    assert callable(myDsl::shift::expression.__init__)


def test_mydsl::shift::expression_constructor_args():
    sig = inspect.signature(myDsl::shift::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::additive::expression::complement_is_not_abstract():
    assert not inspect.isabstract(myDsl::additive::expression::complement)


def test_mydsl::additive::expression::complement_constructor_exists():
    assert callable(myDsl::additive::expression::complement.__init__)


def test_mydsl::additive::expression::complement_constructor_args():
    sig = inspect.signature(myDsl::additive::expression::complement.__init__)
    params = list(sig.parameters.keys())
    assert "menos" in params, "Missing parameter 'menos'"
    assert "mais" in params, "Missing parameter 'mais'"

def test_mydsl::additive::expression::complement_has_menos():
    assert hasattr(myDsl::additive::expression::complement, "menos")
    descriptor = None
    for klass in myDsl::additive::expression::complement.__mro__:
        if "menos" in klass.__dict__:
            descriptor = klass.__dict__["menos"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::additive::expression::complement_has_mais():
    assert hasattr(myDsl::additive::expression::complement, "mais")
    descriptor = None
    for klass in myDsl::additive::expression::complement.__mro__:
        if "mais" in klass.__dict__:
            descriptor = klass.__dict__["mais"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::additive::expression::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::additive::expression::linha)


def test_mydsl::additive::expression::linha_constructor_exists():
    assert callable(myDsl::additive::expression::linha.__init__)


def test_mydsl::additive::expression::linha_constructor_args():
    sig = inspect.signature(myDsl::additive::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::equality::expression::complement_is_not_abstract():
    assert not inspect.isabstract(myDsl::equality::expression::complement)


def test_mydsl::equality::expression::complement_constructor_exists():
    assert callable(myDsl::equality::expression::complement.__init__)


def test_mydsl::equality::expression::complement_constructor_args():
    sig = inspect.signature(myDsl::equality::expression::complement.__init__)
    params = list(sig.parameters.keys())
    assert "igual" in params, "Missing parameter 'igual'"
    assert "maior" in params, "Missing parameter 'maior'"
    assert "maior_igual" in params, "Missing parameter 'maior_igual'"
    assert "menor" in params, "Missing parameter 'menor'"
    assert "menor_igual" in params, "Missing parameter 'menor_igual'"
    assert "n_igual" in params, "Missing parameter 'n_igual'"

def test_mydsl::equality::expression::complement_has_igual():
    assert hasattr(myDsl::equality::expression::complement, "igual")
    descriptor = None
    for klass in myDsl::equality::expression::complement.__mro__:
        if "igual" in klass.__dict__:
            descriptor = klass.__dict__["igual"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::equality::expression::complement_has_maior():
    assert hasattr(myDsl::equality::expression::complement, "maior")
    descriptor = None
    for klass in myDsl::equality::expression::complement.__mro__:
        if "maior" in klass.__dict__:
            descriptor = klass.__dict__["maior"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::equality::expression::complement_has_maior_igual():
    assert hasattr(myDsl::equality::expression::complement, "maior_igual")
    descriptor = None
    for klass in myDsl::equality::expression::complement.__mro__:
        if "maior_igual" in klass.__dict__:
            descriptor = klass.__dict__["maior_igual"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::equality::expression::complement_has_menor():
    assert hasattr(myDsl::equality::expression::complement, "menor")
    descriptor = None
    for klass in myDsl::equality::expression::complement.__mro__:
        if "menor" in klass.__dict__:
            descriptor = klass.__dict__["menor"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::equality::expression::complement_has_menor_igual():
    assert hasattr(myDsl::equality::expression::complement, "menor_igual")
    descriptor = None
    for klass in myDsl::equality::expression::complement.__mro__:
        if "menor_igual" in klass.__dict__:
            descriptor = klass.__dict__["menor_igual"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::equality::expression::complement_has_n_igual():
    assert hasattr(myDsl::equality::expression::complement, "n_igual")
    descriptor = None
    for klass in myDsl::equality::expression::complement.__mro__:
        if "n_igual" in klass.__dict__:
            descriptor = klass.__dict__["n_igual"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::equality::expression::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::equality::expression::linha)


def test_mydsl::equality::expression::linha_constructor_exists():
    assert callable(myDsl::equality::expression::linha.__init__)


def test_mydsl::equality::expression::linha_constructor_args():
    sig = inspect.signature(myDsl::equality::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::equality::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::equality::expression)


def test_mydsl::equality::expression_constructor_exists():
    assert callable(myDsl::equality::expression.__init__)


def test_mydsl::equality::expression_constructor_args():
    sig = inspect.signature(myDsl::equality::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::relational::expression::complement_is_not_abstract():
    assert not inspect.isabstract(myDsl::relational::expression::complement)


def test_mydsl::relational::expression::complement_constructor_exists():
    assert callable(myDsl::relational::expression::complement.__init__)


def test_mydsl::relational::expression::complement_constructor_args():
    sig = inspect.signature(myDsl::relational::expression::complement.__init__)
    params = list(sig.parameters.keys())
    assert "maior_igual" in params, "Missing parameter 'maior_igual'"
    assert "menor_igual" in params, "Missing parameter 'menor_igual'"
    assert "maior" in params, "Missing parameter 'maior'"
    assert "menor" in params, "Missing parameter 'menor'"

def test_mydsl::relational::expression::complement_has_maior_igual():
    assert hasattr(myDsl::relational::expression::complement, "maior_igual")
    descriptor = None
    for klass in myDsl::relational::expression::complement.__mro__:
        if "maior_igual" in klass.__dict__:
            descriptor = klass.__dict__["maior_igual"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::relational::expression::complement_has_menor_igual():
    assert hasattr(myDsl::relational::expression::complement, "menor_igual")
    descriptor = None
    for klass in myDsl::relational::expression::complement.__mro__:
        if "menor_igual" in klass.__dict__:
            descriptor = klass.__dict__["menor_igual"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::relational::expression::complement_has_maior():
    assert hasattr(myDsl::relational::expression::complement, "maior")
    descriptor = None
    for klass in myDsl::relational::expression::complement.__mro__:
        if "maior" in klass.__dict__:
            descriptor = klass.__dict__["maior"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::relational::expression::complement_has_menor():
    assert hasattr(myDsl::relational::expression::complement, "menor")
    descriptor = None
    for klass in myDsl::relational::expression::complement.__mro__:
        if "menor" in klass.__dict__:
            descriptor = klass.__dict__["menor"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::relational::expression::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::relational::expression::linha)


def test_mydsl::relational::expression::linha_constructor_exists():
    assert callable(myDsl::relational::expression::linha.__init__)


def test_mydsl::relational::expression::linha_constructor_args():
    sig = inspect.signature(myDsl::relational::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::relational::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::relational::expression)


def test_mydsl::relational::expression_constructor_exists():
    assert callable(myDsl::relational::expression.__init__)


def test_mydsl::relational::expression_constructor_args():
    sig = inspect.signature(myDsl::relational::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::additive::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::additive::expression)


def test_mydsl::additive::expression_constructor_exists():
    assert callable(myDsl::additive::expression.__init__)


def test_mydsl::additive::expression_constructor_args():
    sig = inspect.signature(myDsl::additive::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::multiplicative::expression::complement_is_not_abstract():
    assert not inspect.isabstract(myDsl::multiplicative::expression::complement)


def test_mydsl::multiplicative::expression::complement_constructor_exists():
    assert callable(myDsl::multiplicative::expression::complement.__init__)


def test_mydsl::multiplicative::expression::complement_constructor_args():
    sig = inspect.signature(myDsl::multiplicative::expression::complement.__init__)
    params = list(sig.parameters.keys())
    assert "multiplica" in params, "Missing parameter 'multiplica'"
    assert "divide" in params, "Missing parameter 'divide'"
    assert "modulo" in params, "Missing parameter 'modulo'"

def test_mydsl::multiplicative::expression::complement_has_multiplica():
    assert hasattr(myDsl::multiplicative::expression::complement, "multiplica")
    descriptor = None
    for klass in myDsl::multiplicative::expression::complement.__mro__:
        if "multiplica" in klass.__dict__:
            descriptor = klass.__dict__["multiplica"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::multiplicative::expression::complement_has_divide():
    assert hasattr(myDsl::multiplicative::expression::complement, "divide")
    descriptor = None
    for klass in myDsl::multiplicative::expression::complement.__mro__:
        if "divide" in klass.__dict__:
            descriptor = klass.__dict__["divide"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::multiplicative::expression::complement_has_modulo():
    assert hasattr(myDsl::multiplicative::expression::complement, "modulo")
    descriptor = None
    for klass in myDsl::multiplicative::expression::complement.__mro__:
        if "modulo" in klass.__dict__:
            descriptor = klass.__dict__["modulo"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::multiplicative::expression::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::multiplicative::expression::linha)


def test_mydsl::multiplicative::expression::linha_constructor_exists():
    assert callable(myDsl::multiplicative::expression::linha.__init__)


def test_mydsl::multiplicative::expression::linha_constructor_args():
    sig = inspect.signature(myDsl::multiplicative::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::multiplicative::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::multiplicative::expression)


def test_mydsl::multiplicative::expression_constructor_exists():
    assert callable(myDsl::multiplicative::expression.__init__)


def test_mydsl::multiplicative::expression_constructor_args():
    sig = inspect.signature(myDsl::multiplicative::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::cast::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::cast::expression)


def test_mydsl::cast::expression_constructor_exists():
    assert callable(myDsl::cast::expression.__init__)


def test_mydsl::cast::expression_constructor_args():
    sig = inspect.signature(myDsl::cast::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::unary::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::unary::expression)


def test_mydsl::unary::expression_constructor_exists():
    assert callable(myDsl::unary::expression.__init__)


def test_mydsl::unary::expression_constructor_args():
    sig = inspect.signature(myDsl::unary::expression.__init__)
    params = list(sig.parameters.keys())
    assert "unary_operator" in params, "Missing parameter 'unary_operator'"

def test_mydsl::unary::expression_has_unary_operator():
    assert hasattr(myDsl::unary::expression, "unary_operator")
    descriptor = None
    for klass in myDsl::unary::expression.__mro__:
        if "unary_operator" in klass.__dict__:
            descriptor = klass.__dict__["unary_operator"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::argument::expression::list::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::argument::expression::list::linha)


def test_mydsl::argument::expression::list::linha_constructor_exists():
    assert callable(myDsl::argument::expression::list::linha.__init__)


def test_mydsl::argument::expression::list::linha_constructor_args():
    sig = inspect.signature(myDsl::argument::expression::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::argument::expression::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::argument::expression::list)


def test_mydsl::argument::expression::list_constructor_exists():
    assert callable(myDsl::argument::expression::list.__init__)


def test_mydsl::argument::expression::list_constructor_args():
    sig = inspect.signature(myDsl::argument::expression::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::postfix::expression::complement_is_not_abstract():
    assert not inspect.isabstract(myDsl::postfix::expression::complement)


def test_mydsl::postfix::expression::complement_constructor_exists():
    assert callable(myDsl::postfix::expression::complement.__init__)


def test_mydsl::postfix::expression::complement_constructor_args():
    sig = inspect.signature(myDsl::postfix::expression::complement.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl::postfix::expression::complement_has_identifier():
    assert hasattr(myDsl::postfix::expression::complement, "identifier")
    descriptor = None
    for klass in myDsl::postfix::expression::complement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::conditional::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::conditional::expression)


def test_mydsl::conditional::expression_constructor_exists():
    assert callable(myDsl::conditional::expression.__init__)


def test_mydsl::conditional::expression_constructor_args():
    sig = inspect.signature(myDsl::conditional::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::designator::list::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::designator::list::linha)


def test_mydsl::designator::list::linha_constructor_exists():
    assert callable(myDsl::designator::list::linha.__init__)


def test_mydsl::designator::list::linha_constructor_args():
    sig = inspect.signature(myDsl::designator::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::designator_is_not_abstract():
    assert not inspect.isabstract(myDsl::designator)


def test_mydsl::designator_constructor_exists():
    assert callable(myDsl::designator.__init__)


def test_mydsl::designator_constructor_args():
    sig = inspect.signature(myDsl::designator.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl::designator_has_identifier():
    assert hasattr(myDsl::designator, "identifier")
    descriptor = None
    for klass in myDsl::designator.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::designator::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::designator::list)


def test_mydsl::designator::list_constructor_exists():
    assert callable(myDsl::designator::list.__init__)


def test_mydsl::designator::list_constructor_args():
    sig = inspect.signature(myDsl::designator::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::initializer::list::complement_is_not_abstract():
    assert not inspect.isabstract(myDsl::initializer::list::complement)


def test_mydsl::initializer::list::complement_constructor_exists():
    assert callable(myDsl::initializer::list::complement.__init__)


def test_mydsl::initializer::list::complement_constructor_args():
    sig = inspect.signature(myDsl::initializer::list::complement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::initializer::list::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::initializer::list::linha)


def test_mydsl::initializer::list::linha_constructor_exists():
    assert callable(myDsl::initializer::list::linha.__init__)


def test_mydsl::initializer::list::linha_constructor_args():
    sig = inspect.signature(myDsl::initializer::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::init::declarator::list::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::init::declarator::list::linha)


def test_mydsl::init::declarator::list::linha_constructor_exists():
    assert callable(myDsl::init::declarator::list::linha.__init__)


def test_mydsl::init::declarator::list::linha_constructor_args():
    sig = inspect.signature(myDsl::init::declarator::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::designation_is_not_abstract():
    assert not inspect.isabstract(myDsl::designation)


def test_mydsl::designation_constructor_exists():
    assert callable(myDsl::designation.__init__)


def test_mydsl::designation_constructor_args():
    sig = inspect.signature(myDsl::designation.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::postfix::expression::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::postfix::expression::linha)


def test_mydsl::postfix::expression::linha_constructor_exists():
    assert callable(myDsl::postfix::expression::linha.__init__)


def test_mydsl::postfix::expression::linha_constructor_args():
    sig = inspect.signature(myDsl::postfix::expression::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::postfix::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::postfix::expression)


def test_mydsl::postfix::expression_constructor_exists():
    assert callable(myDsl::postfix::expression.__init__)


def test_mydsl::postfix::expression_constructor_args():
    sig = inspect.signature(myDsl::postfix::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::generic::assoc::list::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::generic::assoc::list::linha)


def test_mydsl::generic::assoc::list::linha_constructor_exists():
    assert callable(myDsl::generic::assoc::list::linha.__init__)


def test_mydsl::generic::assoc::list::linha_constructor_args():
    sig = inspect.signature(myDsl::generic::assoc::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::generic::association_is_not_abstract():
    assert not inspect.isabstract(myDsl::generic::association)


def test_mydsl::generic::association_constructor_exists():
    assert callable(myDsl::generic::association.__init__)


def test_mydsl::generic::association_constructor_args():
    sig = inspect.signature(myDsl::generic::association.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_mydsl::generic::association_has_default():
    assert hasattr(myDsl::generic::association, "default")
    descriptor = None
    for klass in myDsl::generic::association.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::generic::assoc::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::generic::assoc::list)


def test_mydsl::generic::assoc::list_constructor_exists():
    assert callable(myDsl::generic::assoc::list.__init__)


def test_mydsl::generic::assoc::list_constructor_args():
    sig = inspect.signature(myDsl::generic::assoc::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::generic::selection_is_not_abstract():
    assert not inspect.isabstract(myDsl::generic::selection)


def test_mydsl::generic::selection_constructor_exists():
    assert callable(myDsl::generic::selection.__init__)


def test_mydsl::generic::selection_constructor_args():
    sig = inspect.signature(myDsl::generic::selection.__init__)
    params = list(sig.parameters.keys())
    assert "_generic" in params, "Missing parameter '_generic'"

def test_mydsl::generic::selection_has__generic():
    assert hasattr(myDsl::generic::selection, "_generic")
    descriptor = None
    for klass in myDsl::generic::selection.__mro__:
        if "_generic" in klass.__dict__:
            descriptor = klass.__dict__["_generic"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::expression)


def test_mydsl::expression_constructor_exists():
    assert callable(myDsl::expression.__init__)


def test_mydsl::expression_constructor_args():
    sig = inspect.signature(myDsl::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::constant_is_not_abstract():
    assert not inspect.isabstract(myDsl::constant)


def test_mydsl::constant_constructor_exists():
    assert callable(myDsl::constant.__init__)


def test_mydsl::constant_constructor_args():
    sig = inspect.signature(myDsl::constant.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"
    assert "char" in params, "Missing parameter 'char'"
    assert "f_constant" in params, "Missing parameter 'f_constant'"
    assert "i_constant" in params, "Missing parameter 'i_constant'"
    assert "enumz" in params, "Missing parameter 'enumz'"

def test_mydsl::constant_has_string():
    assert hasattr(myDsl::constant, "string")
    descriptor = None
    for klass in myDsl::constant.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::constant_has_char():
    assert hasattr(myDsl::constant, "char")
    descriptor = None
    for klass in myDsl::constant.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::constant_has_f_constant():
    assert hasattr(myDsl::constant, "f_constant")
    descriptor = None
    for klass in myDsl::constant.__mro__:
        if "f_constant" in klass.__dict__:
            descriptor = klass.__dict__["f_constant"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::constant_has_i_constant():
    assert hasattr(myDsl::constant, "i_constant")
    descriptor = None
    for klass in myDsl::constant.__mro__:
        if "i_constant" in klass.__dict__:
            descriptor = klass.__dict__["i_constant"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::constant_has_enumz():
    assert hasattr(myDsl::constant, "enumz")
    descriptor = None
    for klass in myDsl::constant.__mro__:
        if "enumz" in klass.__dict__:
            descriptor = klass.__dict__["enumz"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::primary::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::primary::expression)


def test_mydsl::primary::expression_constructor_exists():
    assert callable(myDsl::primary::expression.__init__)


def test_mydsl::primary::expression_constructor_args():
    sig = inspect.signature(myDsl::primary::expression.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl::primary::expression_has_identifier():
    assert hasattr(myDsl::primary::expression, "identifier")
    descriptor = None
    for klass in myDsl::primary::expression.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::identifier::list::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::identifier::list::linha)


def test_mydsl::identifier::list::linha_constructor_exists():
    assert callable(myDsl::identifier::list::linha.__init__)


def test_mydsl::identifier::list::linha_constructor_args():
    sig = inspect.signature(myDsl::identifier::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::direct::abstract::declarator::complement_is_not_abstract():
    assert not inspect.isabstract(myDsl::direct::abstract::declarator::complement)


def test_mydsl::direct::abstract::declarator::complement_constructor_exists():
    assert callable(myDsl::direct::abstract::declarator::complement.__init__)


def test_mydsl::direct::abstract::declarator::complement_constructor_args():
    sig = inspect.signature(myDsl::direct::abstract::declarator::complement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::initializer::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::initializer::list)


def test_mydsl::initializer::list_constructor_exists():
    assert callable(myDsl::initializer::list.__init__)


def test_mydsl::initializer::list_constructor_args():
    sig = inspect.signature(myDsl::initializer::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::initializer_is_not_abstract():
    assert not inspect.isabstract(myDsl::initializer)


def test_mydsl::initializer_constructor_exists():
    assert callable(myDsl::initializer.__init__)


def test_mydsl::initializer_constructor_args():
    sig = inspect.signature(myDsl::initializer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::direct::abstract::declarator::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::direct::abstract::declarator::linha)


def test_mydsl::direct::abstract::declarator::linha_constructor_exists():
    assert callable(myDsl::direct::abstract::declarator::linha.__init__)


def test_mydsl::direct::abstract::declarator::linha_constructor_args():
    sig = inspect.signature(myDsl::direct::abstract::declarator::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::direct::abstract::declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl::direct::abstract::declarator)


def test_mydsl::direct::abstract::declarator_constructor_exists():
    assert callable(myDsl::direct::abstract::declarator.__init__)


def test_mydsl::direct::abstract::declarator_constructor_args():
    sig = inspect.signature(myDsl::direct::abstract::declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::abstract::declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl::abstract::declarator)


def test_mydsl::abstract::declarator_constructor_exists():
    assert callable(myDsl::abstract::declarator.__init__)


def test_mydsl::abstract::declarator_constructor_args():
    sig = inspect.signature(myDsl::abstract::declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::parameter::list::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::parameter::list::linha)


def test_mydsl::parameter::list::linha_constructor_exists():
    assert callable(myDsl::parameter::list::linha.__init__)


def test_mydsl::parameter::list::linha_constructor_args():
    sig = inspect.signature(myDsl::parameter::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::parameter::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::parameter::declaration)


def test_mydsl::parameter::declaration_constructor_exists():
    assert callable(myDsl::parameter::declaration.__init__)


def test_mydsl::parameter::declaration_constructor_args():
    sig = inspect.signature(myDsl::parameter::declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::identifier::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::identifier::list)


def test_mydsl::identifier::list_constructor_exists():
    assert callable(myDsl::identifier::list.__init__)


def test_mydsl::identifier::list_constructor_args():
    sig = inspect.signature(myDsl::identifier::list.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl::identifier::list_has_identifier():
    assert hasattr(myDsl::identifier::list, "identifier")
    descriptor = None
    for klass in myDsl::identifier::list.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::parameter::type::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::parameter::type::list)


def test_mydsl::parameter::type::list_constructor_exists():
    assert callable(myDsl::parameter::type::list.__init__)


def test_mydsl::parameter::type::list_constructor_args():
    sig = inspect.signature(myDsl::parameter::type::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::assignment::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::assignment::expression)


def test_mydsl::assignment::expression_constructor_exists():
    assert callable(myDsl::assignment::expression.__init__)


def test_mydsl::assignment::expression_constructor_args():
    sig = inspect.signature(myDsl::assignment::expression.__init__)
    params = list(sig.parameters.keys())
    assert "assignment_operator" in params, "Missing parameter 'assignment_operator'"

def test_mydsl::assignment::expression_has_assignment_operator():
    assert hasattr(myDsl::assignment::expression, "assignment_operator")
    descriptor = None
    for klass in myDsl::assignment::expression.__mro__:
        if "assignment_operator" in klass.__dict__:
            descriptor = klass.__dict__["assignment_operator"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::direct::declarator::complemento_is_not_abstract():
    assert not inspect.isabstract(myDsl::direct::declarator::complemento)


def test_mydsl::direct::declarator::complemento_constructor_exists():
    assert callable(myDsl::direct::declarator::complemento.__init__)


def test_mydsl::direct::declarator::complemento_constructor_args():
    sig = inspect.signature(myDsl::direct::declarator::complemento.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::direct::declarator::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::direct::declarator::linha)


def test_mydsl::direct::declarator::linha_constructor_exists():
    assert callable(myDsl::direct::declarator::linha.__init__)


def test_mydsl::direct::declarator::linha_constructor_args():
    sig = inspect.signature(myDsl::direct::declarator::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::type::qualifier::list::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::type::qualifier::list::linha)


def test_mydsl::type::qualifier::list::linha_constructor_exists():
    assert callable(myDsl::type::qualifier::list::linha.__init__)


def test_mydsl::type::qualifier::list::linha_constructor_args():
    sig = inspect.signature(myDsl::type::qualifier::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_direct::abstract::declarator::complement_is_not_abstract():
    assert not inspect.isabstract(direct::abstract::declarator::complement)


def test_direct::abstract::declarator::complement_constructor_exists():
    assert callable(direct::abstract::declarator::complement.__init__)


def test_direct::abstract::declarator::complement_constructor_args():
    sig = inspect.signature(direct::abstract::declarator::complement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::type::qualifier::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::type::qualifier::list)


def test_mydsl::type::qualifier::list_constructor_exists():
    assert callable(myDsl::type::qualifier::list.__init__)


def test_mydsl::type::qualifier::list_constructor_args():
    sig = inspect.signature(myDsl::type::qualifier::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::direct::declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl::direct::declarator)


def test_mydsl::direct::declarator_constructor_exists():
    assert callable(myDsl::direct::declarator.__init__)


def test_mydsl::direct::declarator_constructor_args():
    sig = inspect.signature(myDsl::direct::declarator.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl::direct::declarator_has_identifier():
    assert hasattr(myDsl::direct::declarator, "identifier")
    descriptor = None
    for klass in myDsl::direct::declarator.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::pointer_is_not_abstract():
    assert not inspect.isabstract(myDsl::pointer)


def test_mydsl::pointer_constructor_exists():
    assert callable(myDsl::pointer.__init__)


def test_mydsl::pointer_constructor_args():
    sig = inspect.signature(myDsl::pointer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::declaration::list::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::declaration::list::linha)


def test_mydsl::declaration::list::linha_constructor_exists():
    assert callable(myDsl::declaration::list::linha.__init__)


def test_mydsl::declaration::list::linha_constructor_args():
    sig = inspect.signature(myDsl::declaration::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::compound::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::compound::statement)


def test_mydsl::compound::statement_constructor_exists():
    assert callable(myDsl::compound::statement.__init__)


def test_mydsl::compound::statement_constructor_args():
    sig = inspect.signature(myDsl::compound::statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::declaration::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::declaration::list)


def test_mydsl::declaration::list_constructor_exists():
    assert callable(myDsl::declaration::list.__init__)


def test_mydsl::declaration::list_constructor_args():
    sig = inspect.signature(myDsl::declaration::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::parameter::lista_is_not_abstract():
    assert not inspect.isabstract(myDsl::parameter::lista)


def test_mydsl::parameter::lista_constructor_exists():
    assert callable(myDsl::parameter::lista.__init__)


def test_mydsl::parameter::lista_constructor_args():
    sig = inspect.signature(myDsl::parameter::lista.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::init::declarator::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::init::declarator::list)


def test_mydsl::init::declarator::list_constructor_exists():
    assert callable(myDsl::init::declarator::list.__init__)


def test_mydsl::init::declarator::list_constructor_args():
    sig = inspect.signature(myDsl::init::declarator::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl::declarator)


def test_mydsl::declarator_constructor_exists():
    assert callable(myDsl::declarator.__init__)


def test_mydsl::declarator_constructor_args():
    sig = inspect.signature(myDsl::declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::struct::declarator::list::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::declarator::list::linha)


def test_mydsl::struct::declarator::list::linha_constructor_exists():
    assert callable(myDsl::struct::declarator::list::linha.__init__)


def test_mydsl::struct::declarator::list::linha_constructor_args():
    sig = inspect.signature(myDsl::struct::declarator::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::struct::declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::declarator)


def test_mydsl::struct::declarator_constructor_exists():
    assert callable(myDsl::struct::declarator.__init__)


def test_mydsl::struct::declarator_constructor_args():
    sig = inspect.signature(myDsl::struct::declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::static::assert::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::static::assert::declaration)


def test_mydsl::static::assert::declaration_constructor_exists():
    assert callable(myDsl::static::assert::declaration.__init__)


def test_mydsl::static::assert::declaration_constructor_args():
    sig = inspect.signature(myDsl::static::assert::declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::struct::declarator::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::declarator::list)


def test_mydsl::struct::declarator::list_constructor_exists():
    assert callable(myDsl::struct::declarator::list.__init__)


def test_mydsl::struct::declarator::list_constructor_args():
    sig = inspect.signature(myDsl::struct::declarator::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::specifier::qualifier::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::specifier::qualifier::list)


def test_mydsl::specifier::qualifier::list_constructor_exists():
    assert callable(myDsl::specifier::qualifier::list.__init__)


def test_mydsl::specifier::qualifier::list_constructor_args():
    sig = inspect.signature(myDsl::specifier::qualifier::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::struct::declaration::list::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::declaration::list::linha)


def test_mydsl::struct::declaration::list::linha_constructor_exists():
    assert callable(myDsl::struct::declaration::list::linha.__init__)


def test_mydsl::struct::declaration::list::linha_constructor_args():
    sig = inspect.signature(myDsl::struct::declaration::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::struct::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::declaration)


def test_mydsl::struct::declaration_constructor_exists():
    assert callable(myDsl::struct::declaration.__init__)


def test_mydsl::struct::declaration_constructor_args():
    sig = inspect.signature(myDsl::struct::declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::struct::or::union::specifier::complement_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::or::union::specifier::complement)


def test_mydsl::struct::or::union::specifier::complement_constructor_exists():
    assert callable(myDsl::struct::or::union::specifier::complement.__init__)


def test_mydsl::struct::or::union::specifier::complement_constructor_args():
    sig = inspect.signature(myDsl::struct::or::union::specifier::complement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::struct::declaration::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::declaration::list)


def test_mydsl::struct::declaration::list_constructor_exists():
    assert callable(myDsl::struct::declaration::list.__init__)


def test_mydsl::struct::declaration::list_constructor_args():
    sig = inspect.signature(myDsl::struct::declaration::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::enumeration::constant_is_not_abstract():
    assert not inspect.isabstract(myDsl::enumeration::constant)


def test_mydsl::enumeration::constant_constructor_exists():
    assert callable(myDsl::enumeration::constant.__init__)


def test_mydsl::enumeration::constant_constructor_args():
    sig = inspect.signature(myDsl::enumeration::constant.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl::enumeration::constant_has_identifier():
    assert hasattr(myDsl::enumeration::constant, "identifier")
    descriptor = None
    for klass in myDsl::enumeration::constant.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::enumerator::list::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::enumerator::list::linha)


def test_mydsl::enumerator::list::linha_constructor_exists():
    assert callable(myDsl::enumerator::list::linha.__init__)


def test_mydsl::enumerator::list::linha_constructor_args():
    sig = inspect.signature(myDsl::enumerator::list::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::enumerator_is_not_abstract():
    assert not inspect.isabstract(myDsl::enumerator)


def test_mydsl::enumerator_constructor_exists():
    assert callable(myDsl::enumerator.__init__)


def test_mydsl::enumerator_constructor_args():
    sig = inspect.signature(myDsl::enumerator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::enumerator::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::enumerator::list)


def test_mydsl::enumerator::list_constructor_exists():
    assert callable(myDsl::enumerator::list.__init__)


def test_mydsl::enumerator::list_constructor_args():
    sig = inspect.signature(myDsl::enumerator::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::enum::specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl::enum::specifier)


def test_mydsl::enum::specifier_constructor_exists():
    assert callable(myDsl::enum::specifier.__init__)


def test_mydsl::enum::specifier_constructor_args():
    sig = inspect.signature(myDsl::enum::specifier.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl::enum::specifier_has_identifier():
    assert hasattr(myDsl::enum::specifier, "identifier")
    descriptor = None
    for klass in myDsl::enum::specifier.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::struct::or::union::specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::or::union::specifier)


def test_mydsl::struct::or::union::specifier_constructor_exists():
    assert callable(myDsl::struct::or::union::specifier.__init__)


def test_mydsl::struct::or::union::specifier_constructor_args():
    sig = inspect.signature(myDsl::struct::or::union::specifier.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "struct_or_union" in params, "Missing parameter 'struct_or_union'"

def test_mydsl::struct::or::union::specifier_has_identifier():
    assert hasattr(myDsl::struct::or::union::specifier, "identifier")
    descriptor = None
    for klass in myDsl::struct::or::union::specifier.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::struct::or::union::specifier_has_struct_or_union():
    assert hasattr(myDsl::struct::or::union::specifier, "struct_or_union")
    descriptor = None
    for klass in myDsl::struct::or::union::specifier.__mro__:
        if "struct_or_union" in klass.__dict__:
            descriptor = klass.__dict__["struct_or_union"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::atomic::type::specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl::atomic::type::specifier)


def test_mydsl::atomic::type::specifier_constructor_exists():
    assert callable(myDsl::atomic::type::specifier.__init__)


def test_mydsl::atomic::type::specifier_constructor_args():
    sig = inspect.signature(myDsl::atomic::type::specifier.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::constant::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::constant::expression)


def test_mydsl::constant::expression_constructor_exists():
    assert callable(myDsl::constant::expression.__init__)


def test_mydsl::constant::expression_constructor_args():
    sig = inspect.signature(myDsl::constant::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::type::name_is_not_abstract():
    assert not inspect.isabstract(myDsl::type::name)


def test_mydsl::type::name_constructor_exists():
    assert callable(myDsl::type::name.__init__)


def test_mydsl::type::name_constructor_args():
    sig = inspect.signature(myDsl::type::name.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::alignment::specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl::alignment::specifier)


def test_mydsl::alignment::specifier_constructor_exists():
    assert callable(myDsl::alignment::specifier.__init__)


def test_mydsl::alignment::specifier_constructor_args():
    sig = inspect.signature(myDsl::alignment::specifier.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::type::qualifier_is_not_abstract():
    assert not inspect.isabstract(myDsl::type::qualifier)


def test_mydsl::type::qualifier_constructor_exists():
    assert callable(myDsl::type::qualifier.__init__)


def test_mydsl::type::qualifier_constructor_args():
    sig = inspect.signature(myDsl::type::qualifier.__init__)
    params = list(sig.parameters.keys())
    assert "namez" in params, "Missing parameter 'namez'"

def test_mydsl::type::qualifier_has_namez():
    assert hasattr(myDsl::type::qualifier, "namez")
    descriptor = None
    for klass in myDsl::type::qualifier.__mro__:
        if "namez" in klass.__dict__:
            descriptor = klass.__dict__["namez"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::type::specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl::type::specifier)


def test_mydsl::type::specifier_constructor_exists():
    assert callable(myDsl::type::specifier.__init__)


def test_mydsl::type::specifier_constructor_args():
    sig = inspect.signature(myDsl::type::specifier.__init__)
    params = list(sig.parameters.keys())
    assert "type_name_str" in params, "Missing parameter 'type_name_str'"

def test_mydsl::type::specifier_has_type_name_str():
    assert hasattr(myDsl::type::specifier, "type_name_str")
    descriptor = None
    for klass in myDsl::type::specifier.__mro__:
        if "type_name_str" in klass.__dict__:
            descriptor = klass.__dict__["type_name_str"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::declaration::specifiers_is_not_abstract():
    assert not inspect.isabstract(myDsl::declaration::specifiers)


def test_mydsl::declaration::specifiers_constructor_exists():
    assert callable(myDsl::declaration::specifiers.__init__)


def test_mydsl::declaration::specifiers_constructor_args():
    sig = inspect.signature(myDsl::declaration::specifiers.__init__)
    params = list(sig.parameters.keys())
    assert "storage_class_specifier" in params, "Missing parameter 'storage_class_specifier'"
    assert "function_specifier" in params, "Missing parameter 'function_specifier'"

def test_mydsl::declaration::specifiers_has_storage_class_specifier():
    assert hasattr(myDsl::declaration::specifiers, "storage_class_specifier")
    descriptor = None
    for klass in myDsl::declaration::specifiers.__mro__:
        if "storage_class_specifier" in klass.__dict__:
            descriptor = klass.__dict__["storage_class_specifier"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::declaration::specifiers_has_function_specifier():
    assert hasattr(myDsl::declaration::specifiers, "function_specifier")
    descriptor = None
    for klass in myDsl::declaration::specifiers.__mro__:
        if "function_specifier" in klass.__dict__:
            descriptor = klass.__dict__["function_specifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::declaration)


def test_mydsl::declaration_constructor_exists():
    assert callable(myDsl::declaration.__init__)


def test_mydsl::declaration_constructor_args():
    sig = inspect.signature(myDsl::declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::function::definition_is_not_abstract():
    assert not inspect.isabstract(myDsl::function::definition)


def test_mydsl::function::definition_constructor_exists():
    assert callable(myDsl::function::definition.__init__)


def test_mydsl::function::definition_constructor_args():
    sig = inspect.signature(myDsl::function::definition.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::translation::unit::linha_is_not_abstract():
    assert not inspect.isabstract(myDsl::translation::unit::linha)


def test_mydsl::translation::unit::linha_constructor_exists():
    assert callable(myDsl::translation::unit::linha.__init__)


def test_mydsl::translation::unit::linha_constructor_args():
    sig = inspect.signature(myDsl::translation::unit::linha.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::external::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::external::declaration)


def test_mydsl::external::declaration_constructor_exists():
    assert callable(myDsl::external::declaration.__init__)


def test_mydsl::external::declaration_constructor_args():
    sig = inspect.signature(myDsl::external::declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::translation::unit_is_not_abstract():
    assert not inspect.isabstract(myDsl::translation::unit)


def test_mydsl::translation::unit_constructor_exists():
    assert callable(myDsl::translation::unit.__init__)


def test_mydsl::translation::unit_constructor_args():
    sig = inspect.signature(myDsl::translation::unit.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::model_is_not_abstract():
    assert not inspect.isabstract(myDsl::Model)


def test_mydsl::model_constructor_exists():
    assert callable(myDsl::Model.__init__)


def test_mydsl::model_constructor_args():
    sig = inspect.signature(myDsl::Model.__init__)
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
argument::expression::list::linha_strategy = st.builds(
    argument::expression::list::linha,
)
myDsl::ArgumentExpressionListLinhaAction_strategy = st.builds(
    myDsl::ArgumentExpressionListLinhaAction,
)
postfix::expression::complement_strategy = st.builds(
    postfix::expression::complement,
)
myDsl::PostFixEmpryParams_strategy = st.builds(
    myDsl::PostFixEmpryParams,
)
designator::list::linha_strategy = st.builds(
    designator::list::linha,
)
myDsl::DesignatorListLinhaAction_strategy = st.builds(
    myDsl::DesignatorListLinhaAction,
)
initializer::list::linha_strategy = st.builds(
    initializer::list::linha,
)
myDsl::InitializerListLinhaAction_strategy = st.builds(
    myDsl::InitializerListLinhaAction,
)
init::declarator::list::linha_strategy = st.builds(
    init::declarator::list::linha,
)
myDsl::InitDecclaratorListLinhaAction_strategy = st.builds(
    myDsl::InitDecclaratorListLinhaAction,
)
unary::expression_strategy = st.builds(
    unary::expression,
)
myDsl::PlusPlus_strategy = st.builds(
    myDsl::PlusPlus,
    plus=
        safe_text
)
direct::abstract::declarator::linha_strategy = st.builds(
    direct::abstract::declarator::linha,
)
myDsl::DirectAbstractDeclarratorLinhaAction_strategy = st.builds(
    myDsl::DirectAbstractDeclarratorLinhaAction,
)
type::qualifier::list::linha_strategy = st.builds(
    type::qualifier::list::linha,
)
myDsl::TypeQualifierListLinhaAtion_strategy = st.builds(
    myDsl::TypeQualifierListLinhaAtion,
)
declaration::list::linha_strategy = st.builds(
    declaration::list::linha,
)
myDsl::DeclarationListLinhaAction_strategy = st.builds(
    myDsl::DeclarationListLinhaAction,
)
struct::declarator::list::linha_strategy = st.builds(
    struct::declarator::list::linha,
)
myDsl::StructDeclaratorListLinhaAction_strategy = st.builds(
    myDsl::StructDeclaratorListLinhaAction,
)
postfix::expression::linha_strategy = st.builds(
    postfix::expression::linha,
)
myDsl::PostfixExpressionLinhaAction_strategy = st.builds(
    myDsl::PostfixExpressionLinhaAction,
)
generic::assoc::list::linha_strategy = st.builds(
    generic::assoc::list::linha,
)
myDsl::GenericAssocListLinhaAction_strategy = st.builds(
    myDsl::GenericAssocListLinhaAction,
)
translation::unit::linha_strategy = st.builds(
    translation::unit::linha,
)
myDsl::TranlationUnitLinhaAction_strategy = st.builds(
    myDsl::TranlationUnitLinhaAction,
)
identifier::list::linha_strategy = st.builds(
    identifier::list::linha,
)
myDsl::IdentifierListLinhaAction_strategy = st.builds(
    myDsl::IdentifierListLinhaAction,
    identifier=
        safe_text
)
myDsl::init::declarator_strategy = st.builds(
    myDsl::init::declarator,
)
myDsl::expression::linha_strategy = st.builds(
    myDsl::expression::linha,
)
struct::declaration::list::linha_strategy = st.builds(
    struct::declaration::list::linha,
)
myDsl::StructDeclarationListLinhaAction_strategy = st.builds(
    myDsl::StructDeclarationListLinhaAction,
)
struct::or::union::specifier::complement_strategy = st.builds(
    struct::or::union::specifier::complement,
)
myDsl::StructOrUnionSpecifierComplementAction_strategy = st.builds(
    myDsl::StructOrUnionSpecifierComplementAction,
)
enumerator::list::linha_strategy = st.builds(
    enumerator::list::linha,
)
myDsl::EnumeratorListLinhaAction_strategy = st.builds(
    myDsl::EnumeratorListLinhaAction,
)
myDsl::string::dsl_strategy = st.builds(
    myDsl::string::dsl,
    string_literal=
        safe_text,
    __func__=
        safe_text
)
myDsl::conditional::expression::linha_strategy = st.builds(
    myDsl::conditional::expression::linha,
)
myDsl::logical::or::expression::linha_strategy = st.builds(
    myDsl::logical::or::expression::linha,
)
myDsl::logical::or::expression_strategy = st.builds(
    myDsl::logical::or::expression,
)
myDsl::logical::and::expression::linha_strategy = st.builds(
    myDsl::logical::and::expression::linha,
)
myDsl::logical::and::expression_strategy = st.builds(
    myDsl::logical::and::expression,
)
postfix::expression_strategy = st.builds(
    postfix::expression,
)
myDsl::block::item::list::linha_strategy = st.builds(
    myDsl::block::item::list::linha,
)
myDsl::block::item_strategy = st.builds(
    myDsl::block::item,
)
myDsl::block::item::list_strategy = st.builds(
    myDsl::block::item::list,
)
myDsl::inclusive::or::expression::linha_strategy = st.builds(
    myDsl::inclusive::or::expression::linha,
)
myDsl::inclusive::or::expression_strategy = st.builds(
    myDsl::inclusive::or::expression,
)
myDsl::exclusive::or::expression::linha_strategy = st.builds(
    myDsl::exclusive::or::expression::linha,
)
myDsl::exclusive::or::expression_strategy = st.builds(
    myDsl::exclusive::or::expression,
)
myDsl::and::expression::linha_strategy = st.builds(
    myDsl::and::expression::linha,
)
myDsl::and::expression_strategy = st.builds(
    myDsl::and::expression,
)
myDsl::jump::statement_strategy = st.builds(
    myDsl::jump::statement,
    return_=
        safe_text,
    identifier=
        safe_text,
    break_=
        safe_text,
    return_vazio=
        safe_text
)
myDsl::iteration::statement_strategy = st.builds(
    myDsl::iteration::statement,
)
myDsl::selection::statement_strategy = st.builds(
    myDsl::selection::statement,
)
myDsl::expression::statement_strategy = st.builds(
    myDsl::expression::statement,
)
myDsl::labeled::statement_strategy = st.builds(
    myDsl::labeled::statement,
    identifier=
        safe_text
)
myDsl::statement_strategy = st.builds(
    myDsl::statement,
)
myDsl::shift::expression::complement_strategy = st.builds(
    myDsl::shift::expression::complement,
    sright=
        safe_text,
    sleft=
        safe_text
)
myDsl::shift::expression::linha_strategy = st.builds(
    myDsl::shift::expression::linha,
)
myDsl::shift::expression_strategy = st.builds(
    myDsl::shift::expression,
)
myDsl::additive::expression::complement_strategy = st.builds(
    myDsl::additive::expression::complement,
    menos=
        safe_text,
    mais=
        safe_text
)
myDsl::additive::expression::linha_strategy = st.builds(
    myDsl::additive::expression::linha,
)
myDsl::equality::expression::complement_strategy = st.builds(
    myDsl::equality::expression::complement,
    igual=
        safe_text,
    maior=
        safe_text,
    maior_igual=
        safe_text,
    menor=
        safe_text,
    menor_igual=
        safe_text,
    n_igual=
        safe_text
)
myDsl::equality::expression::linha_strategy = st.builds(
    myDsl::equality::expression::linha,
)
myDsl::equality::expression_strategy = st.builds(
    myDsl::equality::expression,
)
myDsl::relational::expression::complement_strategy = st.builds(
    myDsl::relational::expression::complement,
    maior_igual=
        safe_text,
    menor_igual=
        safe_text,
    maior=
        safe_text,
    menor=
        safe_text
)
myDsl::relational::expression::linha_strategy = st.builds(
    myDsl::relational::expression::linha,
)
myDsl::relational::expression_strategy = st.builds(
    myDsl::relational::expression,
)
myDsl::additive::expression_strategy = st.builds(
    myDsl::additive::expression,
)
myDsl::multiplicative::expression::complement_strategy = st.builds(
    myDsl::multiplicative::expression::complement,
    multiplica=
        safe_text,
    divide=
        safe_text,
    modulo=
        safe_text
)
myDsl::multiplicative::expression::linha_strategy = st.builds(
    myDsl::multiplicative::expression::linha,
)
myDsl::multiplicative::expression_strategy = st.builds(
    myDsl::multiplicative::expression,
)
myDsl::cast::expression_strategy = st.builds(
    myDsl::cast::expression,
)
myDsl::unary::expression_strategy = st.builds(
    myDsl::unary::expression,
    unary_operator=
        safe_text
)
myDsl::argument::expression::list::linha_strategy = st.builds(
    myDsl::argument::expression::list::linha,
)
myDsl::argument::expression::list_strategy = st.builds(
    myDsl::argument::expression::list,
)
myDsl::postfix::expression::complement_strategy = st.builds(
    myDsl::postfix::expression::complement,
    identifier=
        safe_text
)
myDsl::conditional::expression_strategy = st.builds(
    myDsl::conditional::expression,
)
myDsl::designator::list::linha_strategy = st.builds(
    myDsl::designator::list::linha,
)
myDsl::designator_strategy = st.builds(
    myDsl::designator,
    identifier=
        safe_text
)
myDsl::designator::list_strategy = st.builds(
    myDsl::designator::list,
)
myDsl::initializer::list::complement_strategy = st.builds(
    myDsl::initializer::list::complement,
)
myDsl::initializer::list::linha_strategy = st.builds(
    myDsl::initializer::list::linha,
)
myDsl::init::declarator::list::linha_strategy = st.builds(
    myDsl::init::declarator::list::linha,
)
myDsl::designation_strategy = st.builds(
    myDsl::designation,
)
myDsl::postfix::expression::linha_strategy = st.builds(
    myDsl::postfix::expression::linha,
)
myDsl::postfix::expression_strategy = st.builds(
    myDsl::postfix::expression,
)
myDsl::generic::assoc::list::linha_strategy = st.builds(
    myDsl::generic::assoc::list::linha,
)
myDsl::generic::association_strategy = st.builds(
    myDsl::generic::association,
    default=
        safe_text
)
myDsl::generic::assoc::list_strategy = st.builds(
    myDsl::generic::assoc::list,
)
myDsl::generic::selection_strategy = st.builds(
    myDsl::generic::selection,
    _generic=
        safe_text
)
myDsl::expression_strategy = st.builds(
    myDsl::expression,
)
myDsl::constant_strategy = st.builds(
    myDsl::constant,
    string=
        safe_text,
    char=
        safe_text,
    f_constant=
        safe_text,
    i_constant=
        st.integers(),
    enumz=
        safe_text
)
myDsl::primary::expression_strategy = st.builds(
    myDsl::primary::expression,
    identifier=
        safe_text
)
myDsl::identifier::list::linha_strategy = st.builds(
    myDsl::identifier::list::linha,
)
myDsl::direct::abstract::declarator::complement_strategy = st.builds(
    myDsl::direct::abstract::declarator::complement,
)
myDsl::initializer::list_strategy = st.builds(
    myDsl::initializer::list,
)
myDsl::initializer_strategy = st.builds(
    myDsl::initializer,
)
myDsl::direct::abstract::declarator::linha_strategy = st.builds(
    myDsl::direct::abstract::declarator::linha,
)
myDsl::direct::abstract::declarator_strategy = st.builds(
    myDsl::direct::abstract::declarator,
)
myDsl::abstract::declarator_strategy = st.builds(
    myDsl::abstract::declarator,
)
myDsl::parameter::list::linha_strategy = st.builds(
    myDsl::parameter::list::linha,
)
myDsl::parameter::declaration_strategy = st.builds(
    myDsl::parameter::declaration,
)
myDsl::identifier::list_strategy = st.builds(
    myDsl::identifier::list,
    identifier=
        safe_text
)
myDsl::parameter::type::list_strategy = st.builds(
    myDsl::parameter::type::list,
)
myDsl::assignment::expression_strategy = st.builds(
    myDsl::assignment::expression,
    assignment_operator=
        safe_text
)
myDsl::direct::declarator::complemento_strategy = st.builds(
    myDsl::direct::declarator::complemento,
)
myDsl::direct::declarator::linha_strategy = st.builds(
    myDsl::direct::declarator::linha,
)
myDsl::type::qualifier::list::linha_strategy = st.builds(
    myDsl::type::qualifier::list::linha,
)
direct::abstract::declarator::complement_strategy = st.builds(
    direct::abstract::declarator::complement,
)
myDsl::type::qualifier::list_strategy = st.builds(
    myDsl::type::qualifier::list,
)
myDsl::direct::declarator_strategy = st.builds(
    myDsl::direct::declarator,
    identifier=
        safe_text
)
myDsl::pointer_strategy = st.builds(
    myDsl::pointer,
)
myDsl::declaration::list::linha_strategy = st.builds(
    myDsl::declaration::list::linha,
)
myDsl::compound::statement_strategy = st.builds(
    myDsl::compound::statement,
)
myDsl::declaration::list_strategy = st.builds(
    myDsl::declaration::list,
)
myDsl::parameter::lista_strategy = st.builds(
    myDsl::parameter::lista,
)
myDsl::init::declarator::list_strategy = st.builds(
    myDsl::init::declarator::list,
)
myDsl::declarator_strategy = st.builds(
    myDsl::declarator,
)
myDsl::struct::declarator::list::linha_strategy = st.builds(
    myDsl::struct::declarator::list::linha,
)
myDsl::struct::declarator_strategy = st.builds(
    myDsl::struct::declarator,
)
myDsl::static::assert::declaration_strategy = st.builds(
    myDsl::static::assert::declaration,
)
myDsl::struct::declarator::list_strategy = st.builds(
    myDsl::struct::declarator::list,
)
myDsl::specifier::qualifier::list_strategy = st.builds(
    myDsl::specifier::qualifier::list,
)
myDsl::struct::declaration::list::linha_strategy = st.builds(
    myDsl::struct::declaration::list::linha,
)
myDsl::struct::declaration_strategy = st.builds(
    myDsl::struct::declaration,
)
myDsl::struct::or::union::specifier::complement_strategy = st.builds(
    myDsl::struct::or::union::specifier::complement,
)
myDsl::struct::declaration::list_strategy = st.builds(
    myDsl::struct::declaration::list,
)
myDsl::enumeration::constant_strategy = st.builds(
    myDsl::enumeration::constant,
    identifier=
        safe_text
)
myDsl::enumerator::list::linha_strategy = st.builds(
    myDsl::enumerator::list::linha,
)
myDsl::enumerator_strategy = st.builds(
    myDsl::enumerator,
)
myDsl::enumerator::list_strategy = st.builds(
    myDsl::enumerator::list,
)
myDsl::enum::specifier_strategy = st.builds(
    myDsl::enum::specifier,
    identifier=
        safe_text
)
myDsl::struct::or::union::specifier_strategy = st.builds(
    myDsl::struct::or::union::specifier,
    identifier=
        safe_text,
    struct_or_union=
        safe_text
)
myDsl::atomic::type::specifier_strategy = st.builds(
    myDsl::atomic::type::specifier,
)
myDsl::constant::expression_strategy = st.builds(
    myDsl::constant::expression,
)
myDsl::type::name_strategy = st.builds(
    myDsl::type::name,
)
myDsl::alignment::specifier_strategy = st.builds(
    myDsl::alignment::specifier,
)
myDsl::type::qualifier_strategy = st.builds(
    myDsl::type::qualifier,
    namez=
        safe_text
)
myDsl::type::specifier_strategy = st.builds(
    myDsl::type::specifier,
    type_name_str=
        safe_text
)
myDsl::declaration::specifiers_strategy = st.builds(
    myDsl::declaration::specifiers,
    storage_class_specifier=
        safe_text,
    function_specifier=
        safe_text
)
myDsl::declaration_strategy = st.builds(
    myDsl::declaration,
)
myDsl::function::definition_strategy = st.builds(
    myDsl::function::definition,
)
myDsl::translation::unit::linha_strategy = st.builds(
    myDsl::translation::unit::linha,
)
myDsl::external::declaration_strategy = st.builds(
    myDsl::external::declaration,
)
myDsl::translation::unit_strategy = st.builds(
    myDsl::translation::unit,
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
)

@given(instance=argument::expression::list::linha_strategy)
@settings(max_examples=50)
def test_argument::expression::list::linha_instantiation(instance):
    assert isinstance(instance, argument::expression::list::linha)

@given(instance=myDsl::ArgumentExpressionListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl::argumentexpressionlistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl::ArgumentExpressionListLinhaAction)

@given(instance=postfix::expression::complement_strategy)
@settings(max_examples=50)
def test_postfix::expression::complement_instantiation(instance):
    assert isinstance(instance, postfix::expression::complement)

@given(instance=myDsl::PostFixEmpryParams_strategy)
@settings(max_examples=50)
def test_mydsl::postfixempryparams_instantiation(instance):
    assert isinstance(instance, myDsl::PostFixEmpryParams)

@given(instance=designator::list::linha_strategy)
@settings(max_examples=50)
def test_designator::list::linha_instantiation(instance):
    assert isinstance(instance, designator::list::linha)

@given(instance=myDsl::DesignatorListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl::designatorlistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl::DesignatorListLinhaAction)

@given(instance=initializer::list::linha_strategy)
@settings(max_examples=50)
def test_initializer::list::linha_instantiation(instance):
    assert isinstance(instance, initializer::list::linha)

@given(instance=myDsl::InitializerListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl::initializerlistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl::InitializerListLinhaAction)

@given(instance=init::declarator::list::linha_strategy)
@settings(max_examples=50)
def test_init::declarator::list::linha_instantiation(instance):
    assert isinstance(instance, init::declarator::list::linha)

@given(instance=myDsl::InitDecclaratorListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl::initdecclaratorlistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl::InitDecclaratorListLinhaAction)

@given(instance=unary::expression_strategy)
@settings(max_examples=50)
def test_unary::expression_instantiation(instance):
    assert isinstance(instance, unary::expression)

@given(instance=myDsl::PlusPlus_strategy)
@settings(max_examples=50)
def test_mydsl::plusplus_instantiation(instance):
    assert isinstance(instance, myDsl::PlusPlus)

@given(instance=myDsl::PlusPlus_strategy)
def test_mydsl::plusplus_plus_type(instance):
    assert isinstance(instance.plus, str)


@given(instance=myDsl::PlusPlus_strategy)
def test_mydsl::plusplus_plus_setter(instance):
    original = instance.plus
    instance.plus = original
    assert instance.plus == original

@given(instance=direct::abstract::declarator::linha_strategy)
@settings(max_examples=50)
def test_direct::abstract::declarator::linha_instantiation(instance):
    assert isinstance(instance, direct::abstract::declarator::linha)

@given(instance=myDsl::DirectAbstractDeclarratorLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl::directabstractdeclarratorlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl::DirectAbstractDeclarratorLinhaAction)

@given(instance=type::qualifier::list::linha_strategy)
@settings(max_examples=50)
def test_type::qualifier::list::linha_instantiation(instance):
    assert isinstance(instance, type::qualifier::list::linha)

@given(instance=myDsl::TypeQualifierListLinhaAtion_strategy)
@settings(max_examples=50)
def test_mydsl::typequalifierlistlinhaation_instantiation(instance):
    assert isinstance(instance, myDsl::TypeQualifierListLinhaAtion)

@given(instance=declaration::list::linha_strategy)
@settings(max_examples=50)
def test_declaration::list::linha_instantiation(instance):
    assert isinstance(instance, declaration::list::linha)

@given(instance=myDsl::DeclarationListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl::declarationlistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl::DeclarationListLinhaAction)

@given(instance=struct::declarator::list::linha_strategy)
@settings(max_examples=50)
def test_struct::declarator::list::linha_instantiation(instance):
    assert isinstance(instance, struct::declarator::list::linha)

@given(instance=myDsl::StructDeclaratorListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl::structdeclaratorlistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl::StructDeclaratorListLinhaAction)

@given(instance=postfix::expression::linha_strategy)
@settings(max_examples=50)
def test_postfix::expression::linha_instantiation(instance):
    assert isinstance(instance, postfix::expression::linha)

@given(instance=myDsl::PostfixExpressionLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl::postfixexpressionlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl::PostfixExpressionLinhaAction)

@given(instance=generic::assoc::list::linha_strategy)
@settings(max_examples=50)
def test_generic::assoc::list::linha_instantiation(instance):
    assert isinstance(instance, generic::assoc::list::linha)

@given(instance=myDsl::GenericAssocListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl::genericassoclistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl::GenericAssocListLinhaAction)

@given(instance=translation::unit::linha_strategy)
@settings(max_examples=50)
def test_translation::unit::linha_instantiation(instance):
    assert isinstance(instance, translation::unit::linha)

@given(instance=myDsl::TranlationUnitLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl::tranlationunitlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl::TranlationUnitLinhaAction)

@given(instance=identifier::list::linha_strategy)
@settings(max_examples=50)
def test_identifier::list::linha_instantiation(instance):
    assert isinstance(instance, identifier::list::linha)

@given(instance=myDsl::IdentifierListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl::identifierlistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl::IdentifierListLinhaAction)

@given(instance=myDsl::IdentifierListLinhaAction_strategy)
def test_mydsl::identifierlistlinhaaction_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=myDsl::IdentifierListLinhaAction_strategy)
def test_mydsl::identifierlistlinhaaction_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl::init::declarator_strategy)
@settings(max_examples=50)
def test_mydsl::init::declarator_instantiation(instance):
    assert isinstance(instance, myDsl::init::declarator)

@given(instance=myDsl::expression::linha_strategy)
@settings(max_examples=50)
def test_mydsl::expression::linha_instantiation(instance):
    assert isinstance(instance, myDsl::expression::linha)

@given(instance=struct::declaration::list::linha_strategy)
@settings(max_examples=50)
def test_struct::declaration::list::linha_instantiation(instance):
    assert isinstance(instance, struct::declaration::list::linha)

@given(instance=myDsl::StructDeclarationListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl::structdeclarationlistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl::StructDeclarationListLinhaAction)

@given(instance=struct::or::union::specifier::complement_strategy)
@settings(max_examples=50)
def test_struct::or::union::specifier::complement_instantiation(instance):
    assert isinstance(instance, struct::or::union::specifier::complement)

@given(instance=myDsl::StructOrUnionSpecifierComplementAction_strategy)
@settings(max_examples=50)
def test_mydsl::structorunionspecifiercomplementaction_instantiation(instance):
    assert isinstance(instance, myDsl::StructOrUnionSpecifierComplementAction)

@given(instance=enumerator::list::linha_strategy)
@settings(max_examples=50)
def test_enumerator::list::linha_instantiation(instance):
    assert isinstance(instance, enumerator::list::linha)

@given(instance=myDsl::EnumeratorListLinhaAction_strategy)
@settings(max_examples=50)
def test_mydsl::enumeratorlistlinhaaction_instantiation(instance):
    assert isinstance(instance, myDsl::EnumeratorListLinhaAction)

@given(instance=myDsl::string::dsl_strategy)
@settings(max_examples=50)
def test_mydsl::string::dsl_instantiation(instance):
    assert isinstance(instance, myDsl::string::dsl)

@given(instance=myDsl::string::dsl_strategy)
def test_mydsl::string::dsl_string_literal_type(instance):
    assert isinstance(instance.string_literal, str)


@given(instance=myDsl::string::dsl_strategy)
def test_mydsl::string::dsl_string_literal_setter(instance):
    original = instance.string_literal
    instance.string_literal = original
    assert instance.string_literal == original

@given(instance=myDsl::string::dsl_strategy)
def test_mydsl::string::dsl___func___type(instance):
    assert isinstance(instance.__func__, str)


@given(instance=myDsl::string::dsl_strategy)
def test_mydsl::string::dsl___func___setter(instance):
    original = instance.__func__
    instance.__func__ = original
    assert instance.__func__ == original

@given(instance=myDsl::conditional::expression::linha_strategy)
@settings(max_examples=50)
def test_mydsl::conditional::expression::linha_instantiation(instance):
    assert isinstance(instance, myDsl::conditional::expression::linha)

@given(instance=myDsl::logical::or::expression::linha_strategy)
@settings(max_examples=50)
def test_mydsl::logical::or::expression::linha_instantiation(instance):
    assert isinstance(instance, myDsl::logical::or::expression::linha)

@given(instance=myDsl::logical::or::expression_strategy)
@settings(max_examples=50)
def test_mydsl::logical::or::expression_instantiation(instance):
    assert isinstance(instance, myDsl::logical::or::expression)

@given(instance=myDsl::logical::and::expression::linha_strategy)
@settings(max_examples=50)
def test_mydsl::logical::and::expression::linha_instantiation(instance):
    assert isinstance(instance, myDsl::logical::and::expression::linha)

@given(instance=myDsl::logical::and::expression_strategy)
@settings(max_examples=50)
def test_mydsl::logical::and::expression_instantiation(instance):
    assert isinstance(instance, myDsl::logical::and::expression)

@given(instance=postfix::expression_strategy)
@settings(max_examples=50)
def test_postfix::expression_instantiation(instance):
    assert isinstance(instance, postfix::expression)

@given(instance=myDsl::block::item::list::linha_strategy)
@settings(max_examples=50)
def test_mydsl::block::item::list::linha_instantiation(instance):
    assert isinstance(instance, myDsl::block::item::list::linha)

@given(instance=myDsl::block::item_strategy)
@settings(max_examples=50)
def test_mydsl::block::item_instantiation(instance):
    assert isinstance(instance, myDsl::block::item)

@given(instance=myDsl::block::item::list_strategy)
@settings(max_examples=50)
def test_mydsl::block::item::list_instantiation(instance):
    assert isinstance(instance, myDsl::block::item::list)

@given(instance=myDsl::inclusive::or::expression::linha_strategy)
@settings(max_examples=50)
def test_mydsl::inclusive::or::expression::linha_instantiation(instance):
    assert isinstance(instance, myDsl::inclusive::or::expression::linha)

@given(instance=myDsl::inclusive::or::expression_strategy)
@settings(max_examples=50)
def test_mydsl::inclusive::or::expression_instantiation(instance):
    assert isinstance(instance, myDsl::inclusive::or::expression)

@given(instance=myDsl::exclusive::or::expression::linha_strategy)
@settings(max_examples=50)
def test_mydsl::exclusive::or::expression::linha_instantiation(instance):
    assert isinstance(instance, myDsl::exclusive::or::expression::linha)

@given(instance=myDsl::exclusive::or::expression_strategy)
@settings(max_examples=50)
def test_mydsl::exclusive::or::expression_instantiation(instance):
    assert isinstance(instance, myDsl::exclusive::or::expression)

@given(instance=myDsl::and::expression::linha_strategy)
@settings(max_examples=50)
def test_mydsl::and::expression::linha_instantiation(instance):
    assert isinstance(instance, myDsl::and::expression::linha)

@given(instance=myDsl::and::expression_strategy)
@settings(max_examples=50)
def test_mydsl::and::expression_instantiation(instance):
    assert isinstance(instance, myDsl::and::expression)

@given(instance=myDsl::jump::statement_strategy)
@settings(max_examples=50)
def test_mydsl::jump::statement_instantiation(instance):
    assert isinstance(instance, myDsl::jump::statement)

@given(instance=myDsl::jump::statement_strategy)
def test_mydsl::jump::statement_return__type(instance):
    assert isinstance(instance.return_, str)


@given(instance=myDsl::jump::statement_strategy)
def test_mydsl::jump::statement_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original

@given(instance=myDsl::jump::statement_strategy)
def test_mydsl::jump::statement_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=myDsl::jump::statement_strategy)
def test_mydsl::jump::statement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl::jump::statement_strategy)
def test_mydsl::jump::statement_break__type(instance):
    assert isinstance(instance.break_, str)


@given(instance=myDsl::jump::statement_strategy)
def test_mydsl::jump::statement_break__setter(instance):
    original = instance.break_
    instance.break_ = original
    assert instance.break_ == original

@given(instance=myDsl::jump::statement_strategy)
def test_mydsl::jump::statement_return_vazio_type(instance):
    assert isinstance(instance.return_vazio, str)


@given(instance=myDsl::jump::statement_strategy)
def test_mydsl::jump::statement_return_vazio_setter(instance):
    original = instance.return_vazio
    instance.return_vazio = original
    assert instance.return_vazio == original

@given(instance=myDsl::iteration::statement_strategy)
@settings(max_examples=50)
def test_mydsl::iteration::statement_instantiation(instance):
    assert isinstance(instance, myDsl::iteration::statement)

@given(instance=myDsl::selection::statement_strategy)
@settings(max_examples=50)
def test_mydsl::selection::statement_instantiation(instance):
    assert isinstance(instance, myDsl::selection::statement)

@given(instance=myDsl::expression::statement_strategy)
@settings(max_examples=50)
def test_mydsl::expression::statement_instantiation(instance):
    assert isinstance(instance, myDsl::expression::statement)

@given(instance=myDsl::labeled::statement_strategy)
@settings(max_examples=50)
def test_mydsl::labeled::statement_instantiation(instance):
    assert isinstance(instance, myDsl::labeled::statement)

@given(instance=myDsl::labeled::statement_strategy)
def test_mydsl::labeled::statement_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=myDsl::labeled::statement_strategy)
def test_mydsl::labeled::statement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl::statement_strategy)
@settings(max_examples=50)
def test_mydsl::statement_instantiation(instance):
    assert isinstance(instance, myDsl::statement)

@given(instance=myDsl::shift::expression::complement_strategy)
@settings(max_examples=50)
def test_mydsl::shift::expression::complement_instantiation(instance):
    assert isinstance(instance, myDsl::shift::expression::complement)

@given(instance=myDsl::shift::expression::complement_strategy)
def test_mydsl::shift::expression::complement_sright_type(instance):
    assert isinstance(instance.sright, str)


@given(instance=myDsl::shift::expression::complement_strategy)
def test_mydsl::shift::expression::complement_sright_setter(instance):
    original = instance.sright
    instance.sright = original
    assert instance.sright == original

@given(instance=myDsl::shift::expression::complement_strategy)
def test_mydsl::shift::expression::complement_sleft_type(instance):
    assert isinstance(instance.sleft, str)


@given(instance=myDsl::shift::expression::complement_strategy)
def test_mydsl::shift::expression::complement_sleft_setter(instance):
    original = instance.sleft
    instance.sleft = original
    assert instance.sleft == original

@given(instance=myDsl::shift::expression::linha_strategy)
@settings(max_examples=50)
def test_mydsl::shift::expression::linha_instantiation(instance):
    assert isinstance(instance, myDsl::shift::expression::linha)

@given(instance=myDsl::shift::expression_strategy)
@settings(max_examples=50)
def test_mydsl::shift::expression_instantiation(instance):
    assert isinstance(instance, myDsl::shift::expression)

@given(instance=myDsl::additive::expression::complement_strategy)
@settings(max_examples=50)
def test_mydsl::additive::expression::complement_instantiation(instance):
    assert isinstance(instance, myDsl::additive::expression::complement)

@given(instance=myDsl::additive::expression::complement_strategy)
def test_mydsl::additive::expression::complement_menos_type(instance):
    assert isinstance(instance.menos, str)


@given(instance=myDsl::additive::expression::complement_strategy)
def test_mydsl::additive::expression::complement_menos_setter(instance):
    original = instance.menos
    instance.menos = original
    assert instance.menos == original

@given(instance=myDsl::additive::expression::complement_strategy)
def test_mydsl::additive::expression::complement_mais_type(instance):
    assert isinstance(instance.mais, str)


@given(instance=myDsl::additive::expression::complement_strategy)
def test_mydsl::additive::expression::complement_mais_setter(instance):
    original = instance.mais
    instance.mais = original
    assert instance.mais == original

@given(instance=myDsl::additive::expression::linha_strategy)
@settings(max_examples=50)
def test_mydsl::additive::expression::linha_instantiation(instance):
    assert isinstance(instance, myDsl::additive::expression::linha)

@given(instance=myDsl::equality::expression::complement_strategy)
@settings(max_examples=50)
def test_mydsl::equality::expression::complement_instantiation(instance):
    assert isinstance(instance, myDsl::equality::expression::complement)

@given(instance=myDsl::equality::expression::complement_strategy)
def test_mydsl::equality::expression::complement_igual_type(instance):
    assert isinstance(instance.igual, str)


@given(instance=myDsl::equality::expression::complement_strategy)
def test_mydsl::equality::expression::complement_igual_setter(instance):
    original = instance.igual
    instance.igual = original
    assert instance.igual == original

@given(instance=myDsl::equality::expression::complement_strategy)
def test_mydsl::equality::expression::complement_maior_type(instance):
    assert isinstance(instance.maior, str)


@given(instance=myDsl::equality::expression::complement_strategy)
def test_mydsl::equality::expression::complement_maior_setter(instance):
    original = instance.maior
    instance.maior = original
    assert instance.maior == original

@given(instance=myDsl::equality::expression::complement_strategy)
def test_mydsl::equality::expression::complement_maior_igual_type(instance):
    assert isinstance(instance.maior_igual, str)


@given(instance=myDsl::equality::expression::complement_strategy)
def test_mydsl::equality::expression::complement_maior_igual_setter(instance):
    original = instance.maior_igual
    instance.maior_igual = original
    assert instance.maior_igual == original

@given(instance=myDsl::equality::expression::complement_strategy)
def test_mydsl::equality::expression::complement_menor_type(instance):
    assert isinstance(instance.menor, str)


@given(instance=myDsl::equality::expression::complement_strategy)
def test_mydsl::equality::expression::complement_menor_setter(instance):
    original = instance.menor
    instance.menor = original
    assert instance.menor == original

@given(instance=myDsl::equality::expression::complement_strategy)
def test_mydsl::equality::expression::complement_menor_igual_type(instance):
    assert isinstance(instance.menor_igual, str)


@given(instance=myDsl::equality::expression::complement_strategy)
def test_mydsl::equality::expression::complement_menor_igual_setter(instance):
    original = instance.menor_igual
    instance.menor_igual = original
    assert instance.menor_igual == original

@given(instance=myDsl::equality::expression::complement_strategy)
def test_mydsl::equality::expression::complement_n_igual_type(instance):
    assert isinstance(instance.n_igual, str)


@given(instance=myDsl::equality::expression::complement_strategy)
def test_mydsl::equality::expression::complement_n_igual_setter(instance):
    original = instance.n_igual
    instance.n_igual = original
    assert instance.n_igual == original

@given(instance=myDsl::equality::expression::linha_strategy)
@settings(max_examples=50)
def test_mydsl::equality::expression::linha_instantiation(instance):
    assert isinstance(instance, myDsl::equality::expression::linha)

@given(instance=myDsl::equality::expression_strategy)
@settings(max_examples=50)
def test_mydsl::equality::expression_instantiation(instance):
    assert isinstance(instance, myDsl::equality::expression)

@given(instance=myDsl::relational::expression::complement_strategy)
@settings(max_examples=50)
def test_mydsl::relational::expression::complement_instantiation(instance):
    assert isinstance(instance, myDsl::relational::expression::complement)

@given(instance=myDsl::relational::expression::complement_strategy)
def test_mydsl::relational::expression::complement_maior_igual_type(instance):
    assert isinstance(instance.maior_igual, str)


@given(instance=myDsl::relational::expression::complement_strategy)
def test_mydsl::relational::expression::complement_maior_igual_setter(instance):
    original = instance.maior_igual
    instance.maior_igual = original
    assert instance.maior_igual == original

@given(instance=myDsl::relational::expression::complement_strategy)
def test_mydsl::relational::expression::complement_menor_igual_type(instance):
    assert isinstance(instance.menor_igual, str)


@given(instance=myDsl::relational::expression::complement_strategy)
def test_mydsl::relational::expression::complement_menor_igual_setter(instance):
    original = instance.menor_igual
    instance.menor_igual = original
    assert instance.menor_igual == original

@given(instance=myDsl::relational::expression::complement_strategy)
def test_mydsl::relational::expression::complement_maior_type(instance):
    assert isinstance(instance.maior, str)


@given(instance=myDsl::relational::expression::complement_strategy)
def test_mydsl::relational::expression::complement_maior_setter(instance):
    original = instance.maior
    instance.maior = original
    assert instance.maior == original

@given(instance=myDsl::relational::expression::complement_strategy)
def test_mydsl::relational::expression::complement_menor_type(instance):
    assert isinstance(instance.menor, str)


@given(instance=myDsl::relational::expression::complement_strategy)
def test_mydsl::relational::expression::complement_menor_setter(instance):
    original = instance.menor
    instance.menor = original
    assert instance.menor == original

@given(instance=myDsl::relational::expression::linha_strategy)
@settings(max_examples=50)
def test_mydsl::relational::expression::linha_instantiation(instance):
    assert isinstance(instance, myDsl::relational::expression::linha)

@given(instance=myDsl::relational::expression_strategy)
@settings(max_examples=50)
def test_mydsl::relational::expression_instantiation(instance):
    assert isinstance(instance, myDsl::relational::expression)

@given(instance=myDsl::additive::expression_strategy)
@settings(max_examples=50)
def test_mydsl::additive::expression_instantiation(instance):
    assert isinstance(instance, myDsl::additive::expression)

@given(instance=myDsl::multiplicative::expression::complement_strategy)
@settings(max_examples=50)
def test_mydsl::multiplicative::expression::complement_instantiation(instance):
    assert isinstance(instance, myDsl::multiplicative::expression::complement)

@given(instance=myDsl::multiplicative::expression::complement_strategy)
def test_mydsl::multiplicative::expression::complement_multiplica_type(instance):
    assert isinstance(instance.multiplica, str)


@given(instance=myDsl::multiplicative::expression::complement_strategy)
def test_mydsl::multiplicative::expression::complement_multiplica_setter(instance):
    original = instance.multiplica
    instance.multiplica = original
    assert instance.multiplica == original

@given(instance=myDsl::multiplicative::expression::complement_strategy)
def test_mydsl::multiplicative::expression::complement_divide_type(instance):
    assert isinstance(instance.divide, str)


@given(instance=myDsl::multiplicative::expression::complement_strategy)
def test_mydsl::multiplicative::expression::complement_divide_setter(instance):
    original = instance.divide
    instance.divide = original
    assert instance.divide == original

@given(instance=myDsl::multiplicative::expression::complement_strategy)
def test_mydsl::multiplicative::expression::complement_modulo_type(instance):
    assert isinstance(instance.modulo, str)


@given(instance=myDsl::multiplicative::expression::complement_strategy)
def test_mydsl::multiplicative::expression::complement_modulo_setter(instance):
    original = instance.modulo
    instance.modulo = original
    assert instance.modulo == original

@given(instance=myDsl::multiplicative::expression::linha_strategy)
@settings(max_examples=50)
def test_mydsl::multiplicative::expression::linha_instantiation(instance):
    assert isinstance(instance, myDsl::multiplicative::expression::linha)

@given(instance=myDsl::multiplicative::expression_strategy)
@settings(max_examples=50)
def test_mydsl::multiplicative::expression_instantiation(instance):
    assert isinstance(instance, myDsl::multiplicative::expression)

@given(instance=myDsl::cast::expression_strategy)
@settings(max_examples=50)
def test_mydsl::cast::expression_instantiation(instance):
    assert isinstance(instance, myDsl::cast::expression)

@given(instance=myDsl::unary::expression_strategy)
@settings(max_examples=50)
def test_mydsl::unary::expression_instantiation(instance):
    assert isinstance(instance, myDsl::unary::expression)

@given(instance=myDsl::unary::expression_strategy)
def test_mydsl::unary::expression_unary_operator_type(instance):
    assert isinstance(instance.unary_operator, str)


@given(instance=myDsl::unary::expression_strategy)
def test_mydsl::unary::expression_unary_operator_setter(instance):
    original = instance.unary_operator
    instance.unary_operator = original
    assert instance.unary_operator == original

@given(instance=myDsl::argument::expression::list::linha_strategy)
@settings(max_examples=50)
def test_mydsl::argument::expression::list::linha_instantiation(instance):
    assert isinstance(instance, myDsl::argument::expression::list::linha)

@given(instance=myDsl::argument::expression::list_strategy)
@settings(max_examples=50)
def test_mydsl::argument::expression::list_instantiation(instance):
    assert isinstance(instance, myDsl::argument::expression::list)

@given(instance=myDsl::postfix::expression::complement_strategy)
@settings(max_examples=50)
def test_mydsl::postfix::expression::complement_instantiation(instance):
    assert isinstance(instance, myDsl::postfix::expression::complement)

@given(instance=myDsl::postfix::expression::complement_strategy)
def test_mydsl::postfix::expression::complement_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=myDsl::postfix::expression::complement_strategy)
def test_mydsl::postfix::expression::complement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl::conditional::expression_strategy)
@settings(max_examples=50)
def test_mydsl::conditional::expression_instantiation(instance):
    assert isinstance(instance, myDsl::conditional::expression)

@given(instance=myDsl::designator::list::linha_strategy)
@settings(max_examples=50)
def test_mydsl::designator::list::linha_instantiation(instance):
    assert isinstance(instance, myDsl::designator::list::linha)

@given(instance=myDsl::designator_strategy)
@settings(max_examples=50)
def test_mydsl::designator_instantiation(instance):
    assert isinstance(instance, myDsl::designator)

@given(instance=myDsl::designator_strategy)
def test_mydsl::designator_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=myDsl::designator_strategy)
def test_mydsl::designator_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl::designator::list_strategy)
@settings(max_examples=50)
def test_mydsl::designator::list_instantiation(instance):
    assert isinstance(instance, myDsl::designator::list)

@given(instance=myDsl::initializer::list::complement_strategy)
@settings(max_examples=50)
def test_mydsl::initializer::list::complement_instantiation(instance):
    assert isinstance(instance, myDsl::initializer::list::complement)

@given(instance=myDsl::initializer::list::linha_strategy)
@settings(max_examples=50)
def test_mydsl::initializer::list::linha_instantiation(instance):
    assert isinstance(instance, myDsl::initializer::list::linha)

@given(instance=myDsl::init::declarator::list::linha_strategy)
@settings(max_examples=50)
def test_mydsl::init::declarator::list::linha_instantiation(instance):
    assert isinstance(instance, myDsl::init::declarator::list::linha)

@given(instance=myDsl::designation_strategy)
@settings(max_examples=50)
def test_mydsl::designation_instantiation(instance):
    assert isinstance(instance, myDsl::designation)

@given(instance=myDsl::postfix::expression::linha_strategy)
@settings(max_examples=50)
def test_mydsl::postfix::expression::linha_instantiation(instance):
    assert isinstance(instance, myDsl::postfix::expression::linha)

@given(instance=myDsl::postfix::expression_strategy)
@settings(max_examples=50)
def test_mydsl::postfix::expression_instantiation(instance):
    assert isinstance(instance, myDsl::postfix::expression)

@given(instance=myDsl::generic::assoc::list::linha_strategy)
@settings(max_examples=50)
def test_mydsl::generic::assoc::list::linha_instantiation(instance):
    assert isinstance(instance, myDsl::generic::assoc::list::linha)

@given(instance=myDsl::generic::association_strategy)
@settings(max_examples=50)
def test_mydsl::generic::association_instantiation(instance):
    assert isinstance(instance, myDsl::generic::association)

@given(instance=myDsl::generic::association_strategy)
def test_mydsl::generic::association_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=myDsl::generic::association_strategy)
def test_mydsl::generic::association_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=myDsl::generic::assoc::list_strategy)
@settings(max_examples=50)
def test_mydsl::generic::assoc::list_instantiation(instance):
    assert isinstance(instance, myDsl::generic::assoc::list)

@given(instance=myDsl::generic::selection_strategy)
@settings(max_examples=50)
def test_mydsl::generic::selection_instantiation(instance):
    assert isinstance(instance, myDsl::generic::selection)

@given(instance=myDsl::generic::selection_strategy)
def test_mydsl::generic::selection__generic_type(instance):
    assert isinstance(instance._generic, str)


@given(instance=myDsl::generic::selection_strategy)
def test_mydsl::generic::selection__generic_setter(instance):
    original = instance._generic
    instance._generic = original
    assert instance._generic == original

@given(instance=myDsl::expression_strategy)
@settings(max_examples=50)
def test_mydsl::expression_instantiation(instance):
    assert isinstance(instance, myDsl::expression)

@given(instance=myDsl::constant_strategy)
@settings(max_examples=50)
def test_mydsl::constant_instantiation(instance):
    assert isinstance(instance, myDsl::constant)

@given(instance=myDsl::constant_strategy)
def test_mydsl::constant_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=myDsl::constant_strategy)
def test_mydsl::constant_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=myDsl::constant_strategy)
def test_mydsl::constant_char_type(instance):
    assert isinstance(instance.char, str)


@given(instance=myDsl::constant_strategy)
def test_mydsl::constant_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original

@given(instance=myDsl::constant_strategy)
def test_mydsl::constant_f_constant_type(instance):
    assert isinstance(instance.f_constant, str)


@given(instance=myDsl::constant_strategy)
def test_mydsl::constant_f_constant_setter(instance):
    original = instance.f_constant
    instance.f_constant = original
    assert instance.f_constant == original

@given(instance=myDsl::constant_strategy)
def test_mydsl::constant_i_constant_type(instance):
    assert isinstance(instance.i_constant, int)


@given(instance=myDsl::constant_strategy)
def test_mydsl::constant_i_constant_setter(instance):
    original = instance.i_constant
    instance.i_constant = original
    assert instance.i_constant == original

@given(instance=myDsl::constant_strategy)
def test_mydsl::constant_enumz_type(instance):
    assert isinstance(instance.enumz, str)


@given(instance=myDsl::constant_strategy)
def test_mydsl::constant_enumz_setter(instance):
    original = instance.enumz
    instance.enumz = original
    assert instance.enumz == original

@given(instance=myDsl::primary::expression_strategy)
@settings(max_examples=50)
def test_mydsl::primary::expression_instantiation(instance):
    assert isinstance(instance, myDsl::primary::expression)

@given(instance=myDsl::primary::expression_strategy)
def test_mydsl::primary::expression_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=myDsl::primary::expression_strategy)
def test_mydsl::primary::expression_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl::identifier::list::linha_strategy)
@settings(max_examples=50)
def test_mydsl::identifier::list::linha_instantiation(instance):
    assert isinstance(instance, myDsl::identifier::list::linha)

@given(instance=myDsl::direct::abstract::declarator::complement_strategy)
@settings(max_examples=50)
def test_mydsl::direct::abstract::declarator::complement_instantiation(instance):
    assert isinstance(instance, myDsl::direct::abstract::declarator::complement)

@given(instance=myDsl::initializer::list_strategy)
@settings(max_examples=50)
def test_mydsl::initializer::list_instantiation(instance):
    assert isinstance(instance, myDsl::initializer::list)

@given(instance=myDsl::initializer_strategy)
@settings(max_examples=50)
def test_mydsl::initializer_instantiation(instance):
    assert isinstance(instance, myDsl::initializer)

@given(instance=myDsl::direct::abstract::declarator::linha_strategy)
@settings(max_examples=50)
def test_mydsl::direct::abstract::declarator::linha_instantiation(instance):
    assert isinstance(instance, myDsl::direct::abstract::declarator::linha)

@given(instance=myDsl::direct::abstract::declarator_strategy)
@settings(max_examples=50)
def test_mydsl::direct::abstract::declarator_instantiation(instance):
    assert isinstance(instance, myDsl::direct::abstract::declarator)

@given(instance=myDsl::abstract::declarator_strategy)
@settings(max_examples=50)
def test_mydsl::abstract::declarator_instantiation(instance):
    assert isinstance(instance, myDsl::abstract::declarator)

@given(instance=myDsl::parameter::list::linha_strategy)
@settings(max_examples=50)
def test_mydsl::parameter::list::linha_instantiation(instance):
    assert isinstance(instance, myDsl::parameter::list::linha)

@given(instance=myDsl::parameter::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::parameter::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::parameter::declaration)

@given(instance=myDsl::identifier::list_strategy)
@settings(max_examples=50)
def test_mydsl::identifier::list_instantiation(instance):
    assert isinstance(instance, myDsl::identifier::list)

@given(instance=myDsl::identifier::list_strategy)
def test_mydsl::identifier::list_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=myDsl::identifier::list_strategy)
def test_mydsl::identifier::list_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl::parameter::type::list_strategy)
@settings(max_examples=50)
def test_mydsl::parameter::type::list_instantiation(instance):
    assert isinstance(instance, myDsl::parameter::type::list)

@given(instance=myDsl::assignment::expression_strategy)
@settings(max_examples=50)
def test_mydsl::assignment::expression_instantiation(instance):
    assert isinstance(instance, myDsl::assignment::expression)

@given(instance=myDsl::assignment::expression_strategy)
def test_mydsl::assignment::expression_assignment_operator_type(instance):
    assert isinstance(instance.assignment_operator, str)


@given(instance=myDsl::assignment::expression_strategy)
def test_mydsl::assignment::expression_assignment_operator_setter(instance):
    original = instance.assignment_operator
    instance.assignment_operator = original
    assert instance.assignment_operator == original

@given(instance=myDsl::direct::declarator::complemento_strategy)
@settings(max_examples=50)
def test_mydsl::direct::declarator::complemento_instantiation(instance):
    assert isinstance(instance, myDsl::direct::declarator::complemento)

@given(instance=myDsl::direct::declarator::linha_strategy)
@settings(max_examples=50)
def test_mydsl::direct::declarator::linha_instantiation(instance):
    assert isinstance(instance, myDsl::direct::declarator::linha)

@given(instance=myDsl::type::qualifier::list::linha_strategy)
@settings(max_examples=50)
def test_mydsl::type::qualifier::list::linha_instantiation(instance):
    assert isinstance(instance, myDsl::type::qualifier::list::linha)

@given(instance=direct::abstract::declarator::complement_strategy)
@settings(max_examples=50)
def test_direct::abstract::declarator::complement_instantiation(instance):
    assert isinstance(instance, direct::abstract::declarator::complement)

@given(instance=myDsl::type::qualifier::list_strategy)
@settings(max_examples=50)
def test_mydsl::type::qualifier::list_instantiation(instance):
    assert isinstance(instance, myDsl::type::qualifier::list)

@given(instance=myDsl::direct::declarator_strategy)
@settings(max_examples=50)
def test_mydsl::direct::declarator_instantiation(instance):
    assert isinstance(instance, myDsl::direct::declarator)

@given(instance=myDsl::direct::declarator_strategy)
def test_mydsl::direct::declarator_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=myDsl::direct::declarator_strategy)
def test_mydsl::direct::declarator_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl::pointer_strategy)
@settings(max_examples=50)
def test_mydsl::pointer_instantiation(instance):
    assert isinstance(instance, myDsl::pointer)

@given(instance=myDsl::declaration::list::linha_strategy)
@settings(max_examples=50)
def test_mydsl::declaration::list::linha_instantiation(instance):
    assert isinstance(instance, myDsl::declaration::list::linha)

@given(instance=myDsl::compound::statement_strategy)
@settings(max_examples=50)
def test_mydsl::compound::statement_instantiation(instance):
    assert isinstance(instance, myDsl::compound::statement)

@given(instance=myDsl::declaration::list_strategy)
@settings(max_examples=50)
def test_mydsl::declaration::list_instantiation(instance):
    assert isinstance(instance, myDsl::declaration::list)

@given(instance=myDsl::parameter::lista_strategy)
@settings(max_examples=50)
def test_mydsl::parameter::lista_instantiation(instance):
    assert isinstance(instance, myDsl::parameter::lista)

@given(instance=myDsl::init::declarator::list_strategy)
@settings(max_examples=50)
def test_mydsl::init::declarator::list_instantiation(instance):
    assert isinstance(instance, myDsl::init::declarator::list)

@given(instance=myDsl::declarator_strategy)
@settings(max_examples=50)
def test_mydsl::declarator_instantiation(instance):
    assert isinstance(instance, myDsl::declarator)

@given(instance=myDsl::struct::declarator::list::linha_strategy)
@settings(max_examples=50)
def test_mydsl::struct::declarator::list::linha_instantiation(instance):
    assert isinstance(instance, myDsl::struct::declarator::list::linha)

@given(instance=myDsl::struct::declarator_strategy)
@settings(max_examples=50)
def test_mydsl::struct::declarator_instantiation(instance):
    assert isinstance(instance, myDsl::struct::declarator)

@given(instance=myDsl::static::assert::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::static::assert::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::static::assert::declaration)

@given(instance=myDsl::struct::declarator::list_strategy)
@settings(max_examples=50)
def test_mydsl::struct::declarator::list_instantiation(instance):
    assert isinstance(instance, myDsl::struct::declarator::list)

@given(instance=myDsl::specifier::qualifier::list_strategy)
@settings(max_examples=50)
def test_mydsl::specifier::qualifier::list_instantiation(instance):
    assert isinstance(instance, myDsl::specifier::qualifier::list)

@given(instance=myDsl::struct::declaration::list::linha_strategy)
@settings(max_examples=50)
def test_mydsl::struct::declaration::list::linha_instantiation(instance):
    assert isinstance(instance, myDsl::struct::declaration::list::linha)

@given(instance=myDsl::struct::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::struct::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::struct::declaration)

@given(instance=myDsl::struct::or::union::specifier::complement_strategy)
@settings(max_examples=50)
def test_mydsl::struct::or::union::specifier::complement_instantiation(instance):
    assert isinstance(instance, myDsl::struct::or::union::specifier::complement)

@given(instance=myDsl::struct::declaration::list_strategy)
@settings(max_examples=50)
def test_mydsl::struct::declaration::list_instantiation(instance):
    assert isinstance(instance, myDsl::struct::declaration::list)

@given(instance=myDsl::enumeration::constant_strategy)
@settings(max_examples=50)
def test_mydsl::enumeration::constant_instantiation(instance):
    assert isinstance(instance, myDsl::enumeration::constant)

@given(instance=myDsl::enumeration::constant_strategy)
def test_mydsl::enumeration::constant_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=myDsl::enumeration::constant_strategy)
def test_mydsl::enumeration::constant_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl::enumerator::list::linha_strategy)
@settings(max_examples=50)
def test_mydsl::enumerator::list::linha_instantiation(instance):
    assert isinstance(instance, myDsl::enumerator::list::linha)

@given(instance=myDsl::enumerator_strategy)
@settings(max_examples=50)
def test_mydsl::enumerator_instantiation(instance):
    assert isinstance(instance, myDsl::enumerator)

@given(instance=myDsl::enumerator::list_strategy)
@settings(max_examples=50)
def test_mydsl::enumerator::list_instantiation(instance):
    assert isinstance(instance, myDsl::enumerator::list)

@given(instance=myDsl::enum::specifier_strategy)
@settings(max_examples=50)
def test_mydsl::enum::specifier_instantiation(instance):
    assert isinstance(instance, myDsl::enum::specifier)

@given(instance=myDsl::enum::specifier_strategy)
def test_mydsl::enum::specifier_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=myDsl::enum::specifier_strategy)
def test_mydsl::enum::specifier_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl::struct::or::union::specifier_strategy)
@settings(max_examples=50)
def test_mydsl::struct::or::union::specifier_instantiation(instance):
    assert isinstance(instance, myDsl::struct::or::union::specifier)

@given(instance=myDsl::struct::or::union::specifier_strategy)
def test_mydsl::struct::or::union::specifier_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=myDsl::struct::or::union::specifier_strategy)
def test_mydsl::struct::or::union::specifier_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl::struct::or::union::specifier_strategy)
def test_mydsl::struct::or::union::specifier_struct_or_union_type(instance):
    assert isinstance(instance.struct_or_union, str)


@given(instance=myDsl::struct::or::union::specifier_strategy)
def test_mydsl::struct::or::union::specifier_struct_or_union_setter(instance):
    original = instance.struct_or_union
    instance.struct_or_union = original
    assert instance.struct_or_union == original

@given(instance=myDsl::atomic::type::specifier_strategy)
@settings(max_examples=50)
def test_mydsl::atomic::type::specifier_instantiation(instance):
    assert isinstance(instance, myDsl::atomic::type::specifier)

@given(instance=myDsl::constant::expression_strategy)
@settings(max_examples=50)
def test_mydsl::constant::expression_instantiation(instance):
    assert isinstance(instance, myDsl::constant::expression)

@given(instance=myDsl::type::name_strategy)
@settings(max_examples=50)
def test_mydsl::type::name_instantiation(instance):
    assert isinstance(instance, myDsl::type::name)

@given(instance=myDsl::alignment::specifier_strategy)
@settings(max_examples=50)
def test_mydsl::alignment::specifier_instantiation(instance):
    assert isinstance(instance, myDsl::alignment::specifier)

@given(instance=myDsl::type::qualifier_strategy)
@settings(max_examples=50)
def test_mydsl::type::qualifier_instantiation(instance):
    assert isinstance(instance, myDsl::type::qualifier)

@given(instance=myDsl::type::qualifier_strategy)
def test_mydsl::type::qualifier_namez_type(instance):
    assert isinstance(instance.namez, str)


@given(instance=myDsl::type::qualifier_strategy)
def test_mydsl::type::qualifier_namez_setter(instance):
    original = instance.namez
    instance.namez = original
    assert instance.namez == original

@given(instance=myDsl::type::specifier_strategy)
@settings(max_examples=50)
def test_mydsl::type::specifier_instantiation(instance):
    assert isinstance(instance, myDsl::type::specifier)

@given(instance=myDsl::type::specifier_strategy)
def test_mydsl::type::specifier_type_name_str_type(instance):
    assert isinstance(instance.type_name_str, str)


@given(instance=myDsl::type::specifier_strategy)
def test_mydsl::type::specifier_type_name_str_setter(instance):
    original = instance.type_name_str
    instance.type_name_str = original
    assert instance.type_name_str == original

@given(instance=myDsl::declaration::specifiers_strategy)
@settings(max_examples=50)
def test_mydsl::declaration::specifiers_instantiation(instance):
    assert isinstance(instance, myDsl::declaration::specifiers)

@given(instance=myDsl::declaration::specifiers_strategy)
def test_mydsl::declaration::specifiers_storage_class_specifier_type(instance):
    assert isinstance(instance.storage_class_specifier, str)


@given(instance=myDsl::declaration::specifiers_strategy)
def test_mydsl::declaration::specifiers_storage_class_specifier_setter(instance):
    original = instance.storage_class_specifier
    instance.storage_class_specifier = original
    assert instance.storage_class_specifier == original

@given(instance=myDsl::declaration::specifiers_strategy)
def test_mydsl::declaration::specifiers_function_specifier_type(instance):
    assert isinstance(instance.function_specifier, str)


@given(instance=myDsl::declaration::specifiers_strategy)
def test_mydsl::declaration::specifiers_function_specifier_setter(instance):
    original = instance.function_specifier
    instance.function_specifier = original
    assert instance.function_specifier == original

@given(instance=myDsl::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::declaration)

@given(instance=myDsl::function::definition_strategy)
@settings(max_examples=50)
def test_mydsl::function::definition_instantiation(instance):
    assert isinstance(instance, myDsl::function::definition)

@given(instance=myDsl::translation::unit::linha_strategy)
@settings(max_examples=50)
def test_mydsl::translation::unit::linha_instantiation(instance):
    assert isinstance(instance, myDsl::translation::unit::linha)

@given(instance=myDsl::external::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::external::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::external::declaration)

@given(instance=myDsl::translation::unit_strategy)
@settings(max_examples=50)
def test_mydsl::translation::unit_instantiation(instance):
    assert isinstance(instance, myDsl::translation::unit)

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)

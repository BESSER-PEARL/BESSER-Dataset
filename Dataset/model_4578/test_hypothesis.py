import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    postfix::expressionR,
    struct::or::union::specifier,
    labeled::statement,
    identifier::listR,
    identifier::list,
    direct::declarator,
    declaration::specifiers,
    myDsl::argument::expression::list,
    myDsl::EObject,
    abstract::declarator,
    myDsl::argument::expression::listR,
    type::specifier,
    myDsl::atomic::type::specifier,
    myDsl::struct::or::union::specifier,
    declaration,
    myDsl::struct::declaration,
    myDsl::struct::declaration::list,
    myDsl::struct::declarator::listR,
    myDsl::struct::declarator,
    myDsl::struct::declarator::list,
    myDsl::struct::declaration::listR,
    myDsl::type::specifier,
    struct::declaration,
    myDsl::static::assert::declaration,
    type::name,
    myDsl::specifier::qualifier::list,
    myDsl::designator::listR,
    myDsl::designator,
    designation,
    atomic::type::specifier,
    static::assert::declaration,
    designator,
    myDsl::designation,
    myDsl::postfix::expressionR,
    myDsl::primary::expression,
    unary::expression,
    myDsl::postfix::expression,
    cast::expression,
    myDsl::designator::list,
    myDsl::initializer::listR,
    myDsl::cast::expression,
    myDsl::multiplicative::expressionR,
    myDsl::additive::expressionR,
    myDsl::multiplicative::expression,
    myDsl::type::name,
    myDsl::unary::expression,
    initializer,
    myDsl::initializer::list,
    myDsl::relational::expressionR,
    myDsl::shift::expression,
    myDsl::equality::expressionR,
    myDsl::relational::expression,
    shift::expression,
    myDsl::additive::expression,
    myDsl::shift::expressionR,
    myDsl::inclusive::or::expressionR,
    myDsl::exclusive::or::expression,
    myDsl::logical::and::expressionR,
    myDsl::equality::expression,
    myDsl::and::expressionR,
    myDsl::exclusive::or::expressionR,
    myDsl::and::expression,
    constant::expression,
    assignment::expression,
    myDsl::conditional::expression,
    myDsl::expressionR,
    primary::expression,
    myDsl::StringC,
    expression::statement,
    jump::statement,
    myDsl::IDENTIFIER,
    myDsl::inclusive::or::expression,
    myDsl::logical::or::expressionR,
    myDsl::logical::and::expression,
    conditional::expression,
    myDsl::logical::or::expression,
    myDsl::initializer,
    myDsl::init::declarator::listR,
    myDsl::init::declarator,
    myDsl::init::declarator::list,
    parameter::declaration,
    block::item,
    myDsl::statement,
    myDsl::block::item::listR,
    myDsl::block::item,
    compound::statement,
    myDsl::block::item::list,
    statement,
    myDsl::selection::statement,
    myDsl::jump::statement,
    myDsl::expression::statement,
    myDsl::expression,
    myDsl::iteration::statement,
    myDsl::labeled::statement,
    myDsl::parameter::listR,
    myDsl::parameter::declaration,
    parameter::type::list,
    myDsl::parameter::list,
    myDsl::identifier::listR,
    myDsl::declaration::listR,
    myDsl::abstract::declarator,
    myDsl::type::qualifier::listR,
    pointer,
    myDsl::type::qualifier::list,
    myDsl::pointer,
    struct::declarator,
    myDsl::constant::expression,
    init::declarator,
    myDsl::compound::statement,
    myDsl::identifier::list,
    myDsl::parameter::type::list,
    myDsl::assignment::expression,
    myDsl::direct::declaratorR,
    declarator,
    myDsl::direct::declarator,
    myDsl::external::declaration,
    myDsl::translation::unit,
    myDsl::Model,
    myDsl::declaration::list,
    myDsl::declarator,
    external::declaration,
    myDsl::declaration,
    myDsl::function::definition,
    myDsl::declaration::specifiers,
    myDsl::translation::unitR,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_postfix::expressionr_is_not_abstract():
    assert not inspect.isabstract(postfix::expressionR)


def test_postfix::expressionr_constructor_exists():
    assert callable(postfix::expressionR.__init__)


def test_postfix::expressionr_constructor_args():
    sig = inspect.signature(postfix::expressionR.__init__)
    params = list(sig.parameters.keys())



def test_struct::or::union::specifier_is_not_abstract():
    assert not inspect.isabstract(struct::or::union::specifier)


def test_struct::or::union::specifier_constructor_exists():
    assert callable(struct::or::union::specifier.__init__)


def test_struct::or::union::specifier_constructor_args():
    sig = inspect.signature(struct::or::union::specifier.__init__)
    params = list(sig.parameters.keys())



def test_labeled::statement_is_not_abstract():
    assert not inspect.isabstract(labeled::statement)


def test_labeled::statement_constructor_exists():
    assert callable(labeled::statement.__init__)


def test_labeled::statement_constructor_args():
    sig = inspect.signature(labeled::statement.__init__)
    params = list(sig.parameters.keys())



def test_identifier::listr_is_not_abstract():
    assert not inspect.isabstract(identifier::listR)


def test_identifier::listr_constructor_exists():
    assert callable(identifier::listR.__init__)


def test_identifier::listr_constructor_args():
    sig = inspect.signature(identifier::listR.__init__)
    params = list(sig.parameters.keys())



def test_identifier::list_is_not_abstract():
    assert not inspect.isabstract(identifier::list)


def test_identifier::list_constructor_exists():
    assert callable(identifier::list.__init__)


def test_identifier::list_constructor_args():
    sig = inspect.signature(identifier::list.__init__)
    params = list(sig.parameters.keys())



def test_direct::declarator_is_not_abstract():
    assert not inspect.isabstract(direct::declarator)


def test_direct::declarator_constructor_exists():
    assert callable(direct::declarator.__init__)


def test_direct::declarator_constructor_args():
    sig = inspect.signature(direct::declarator.__init__)
    params = list(sig.parameters.keys())



def test_declaration::specifiers_is_not_abstract():
    assert not inspect.isabstract(declaration::specifiers)


def test_declaration::specifiers_constructor_exists():
    assert callable(declaration::specifiers.__init__)


def test_declaration::specifiers_constructor_args():
    sig = inspect.signature(declaration::specifiers.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::argument::expression::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::argument::expression::list)


def test_mydsl::argument::expression::list_constructor_exists():
    assert callable(myDsl::argument::expression::list.__init__)


def test_mydsl::argument::expression::list_constructor_args():
    sig = inspect.signature(myDsl::argument::expression::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::eobject_is_not_abstract():
    assert not inspect.isabstract(myDsl::EObject)


def test_mydsl::eobject_constructor_exists():
    assert callable(myDsl::EObject.__init__)


def test_mydsl::eobject_constructor_args():
    sig = inspect.signature(myDsl::EObject.__init__)
    params = list(sig.parameters.keys())



def test_abstract::declarator_is_not_abstract():
    assert not inspect.isabstract(abstract::declarator)


def test_abstract::declarator_constructor_exists():
    assert callable(abstract::declarator.__init__)


def test_abstract::declarator_constructor_args():
    sig = inspect.signature(abstract::declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::argument::expression::listr_is_not_abstract():
    assert not inspect.isabstract(myDsl::argument::expression::listR)


def test_mydsl::argument::expression::listr_constructor_exists():
    assert callable(myDsl::argument::expression::listR.__init__)


def test_mydsl::argument::expression::listr_constructor_args():
    sig = inspect.signature(myDsl::argument::expression::listR.__init__)
    params = list(sig.parameters.keys())



def test_type::specifier_is_not_abstract():
    assert not inspect.isabstract(type::specifier)


def test_type::specifier_constructor_exists():
    assert callable(type::specifier.__init__)


def test_type::specifier_constructor_args():
    sig = inspect.signature(type::specifier.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::atomic::type::specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl::atomic::type::specifier)


def test_mydsl::atomic::type::specifier_constructor_exists():
    assert callable(myDsl::atomic::type::specifier.__init__)


def test_mydsl::atomic::type::specifier_constructor_args():
    sig = inspect.signature(myDsl::atomic::type::specifier.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::struct::or::union::specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::or::union::specifier)


def test_mydsl::struct::or::union::specifier_constructor_exists():
    assert callable(myDsl::struct::or::union::specifier.__init__)


def test_mydsl::struct::or::union::specifier_constructor_args():
    sig = inspect.signature(myDsl::struct::or::union::specifier.__init__)
    params = list(sig.parameters.keys())
    assert "Struct_or_union" in params, "Missing parameter 'Struct_or_union'"

def test_mydsl::struct::or::union::specifier_has_Struct_or_union():
    assert hasattr(myDsl::struct::or::union::specifier, "Struct_or_union")
    descriptor = None
    for klass in myDsl::struct::or::union::specifier.__mro__:
        if "Struct_or_union" in klass.__dict__:
            descriptor = klass.__dict__["Struct_or_union"]
            break
    assert isinstance(descriptor, property)



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(declaration)


def test_declaration_constructor_exists():
    assert callable(declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::struct::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::declaration)


def test_mydsl::struct::declaration_constructor_exists():
    assert callable(myDsl::struct::declaration.__init__)


def test_mydsl::struct::declaration_constructor_args():
    sig = inspect.signature(myDsl::struct::declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::struct::declaration::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::declaration::list)


def test_mydsl::struct::declaration::list_constructor_exists():
    assert callable(myDsl::struct::declaration::list.__init__)


def test_mydsl::struct::declaration::list_constructor_args():
    sig = inspect.signature(myDsl::struct::declaration::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::struct::declarator::listr_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::declarator::listR)


def test_mydsl::struct::declarator::listr_constructor_exists():
    assert callable(myDsl::struct::declarator::listR.__init__)


def test_mydsl::struct::declarator::listr_constructor_args():
    sig = inspect.signature(myDsl::struct::declarator::listR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::struct::declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::declarator)


def test_mydsl::struct::declarator_constructor_exists():
    assert callable(myDsl::struct::declarator.__init__)


def test_mydsl::struct::declarator_constructor_args():
    sig = inspect.signature(myDsl::struct::declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::struct::declarator::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::declarator::list)


def test_mydsl::struct::declarator::list_constructor_exists():
    assert callable(myDsl::struct::declarator::list.__init__)


def test_mydsl::struct::declarator::list_constructor_args():
    sig = inspect.signature(myDsl::struct::declarator::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::struct::declaration::listr_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::declaration::listR)


def test_mydsl::struct::declaration::listr_constructor_exists():
    assert callable(myDsl::struct::declaration::listR.__init__)


def test_mydsl::struct::declaration::listr_constructor_args():
    sig = inspect.signature(myDsl::struct::declaration::listR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::type::specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl::type::specifier)


def test_mydsl::type::specifier_constructor_exists():
    assert callable(myDsl::type::specifier.__init__)


def test_mydsl::type::specifier_constructor_args():
    sig = inspect.signature(myDsl::type::specifier.__init__)
    params = list(sig.parameters.keys())



def test_struct::declaration_is_not_abstract():
    assert not inspect.isabstract(struct::declaration)


def test_struct::declaration_constructor_exists():
    assert callable(struct::declaration.__init__)


def test_struct::declaration_constructor_args():
    sig = inspect.signature(struct::declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::static::assert::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::static::assert::declaration)


def test_mydsl::static::assert::declaration_constructor_exists():
    assert callable(myDsl::static::assert::declaration.__init__)


def test_mydsl::static::assert::declaration_constructor_args():
    sig = inspect.signature(myDsl::static::assert::declaration.__init__)
    params = list(sig.parameters.keys())



def test_type::name_is_not_abstract():
    assert not inspect.isabstract(type::name)


def test_type::name_constructor_exists():
    assert callable(type::name.__init__)


def test_type::name_constructor_args():
    sig = inspect.signature(type::name.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::specifier::qualifier::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::specifier::qualifier::list)


def test_mydsl::specifier::qualifier::list_constructor_exists():
    assert callable(myDsl::specifier::qualifier::list.__init__)


def test_mydsl::specifier::qualifier::list_constructor_args():
    sig = inspect.signature(myDsl::specifier::qualifier::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::designator::listr_is_not_abstract():
    assert not inspect.isabstract(myDsl::designator::listR)


def test_mydsl::designator::listr_constructor_exists():
    assert callable(myDsl::designator::listR.__init__)


def test_mydsl::designator::listr_constructor_args():
    sig = inspect.signature(myDsl::designator::listR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::designator_is_not_abstract():
    assert not inspect.isabstract(myDsl::designator)


def test_mydsl::designator_constructor_exists():
    assert callable(myDsl::designator.__init__)


def test_mydsl::designator_constructor_args():
    sig = inspect.signature(myDsl::designator.__init__)
    params = list(sig.parameters.keys())



def test_designation_is_not_abstract():
    assert not inspect.isabstract(designation)


def test_designation_constructor_exists():
    assert callable(designation.__init__)


def test_designation_constructor_args():
    sig = inspect.signature(designation.__init__)
    params = list(sig.parameters.keys())



def test_atomic::type::specifier_is_not_abstract():
    assert not inspect.isabstract(atomic::type::specifier)


def test_atomic::type::specifier_constructor_exists():
    assert callable(atomic::type::specifier.__init__)


def test_atomic::type::specifier_constructor_args():
    sig = inspect.signature(atomic::type::specifier.__init__)
    params = list(sig.parameters.keys())



def test_static::assert::declaration_is_not_abstract():
    assert not inspect.isabstract(static::assert::declaration)


def test_static::assert::declaration_constructor_exists():
    assert callable(static::assert::declaration.__init__)


def test_static::assert::declaration_constructor_args():
    sig = inspect.signature(static::assert::declaration.__init__)
    params = list(sig.parameters.keys())



def test_designator_is_not_abstract():
    assert not inspect.isabstract(designator)


def test_designator_constructor_exists():
    assert callable(designator.__init__)


def test_designator_constructor_args():
    sig = inspect.signature(designator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::designation_is_not_abstract():
    assert not inspect.isabstract(myDsl::designation)


def test_mydsl::designation_constructor_exists():
    assert callable(myDsl::designation.__init__)


def test_mydsl::designation_constructor_args():
    sig = inspect.signature(myDsl::designation.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::postfix::expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl::postfix::expressionR)


def test_mydsl::postfix::expressionr_constructor_exists():
    assert callable(myDsl::postfix::expressionR.__init__)


def test_mydsl::postfix::expressionr_constructor_args():
    sig = inspect.signature(myDsl::postfix::expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::primary::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::primary::expression)


def test_mydsl::primary::expression_constructor_exists():
    assert callable(myDsl::primary::expression.__init__)


def test_mydsl::primary::expression_constructor_args():
    sig = inspect.signature(myDsl::primary::expression.__init__)
    params = list(sig.parameters.keys())



def test_unary::expression_is_not_abstract():
    assert not inspect.isabstract(unary::expression)


def test_unary::expression_constructor_exists():
    assert callable(unary::expression.__init__)


def test_unary::expression_constructor_args():
    sig = inspect.signature(unary::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::postfix::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::postfix::expression)


def test_mydsl::postfix::expression_constructor_exists():
    assert callable(myDsl::postfix::expression.__init__)


def test_mydsl::postfix::expression_constructor_args():
    sig = inspect.signature(myDsl::postfix::expression.__init__)
    params = list(sig.parameters.keys())



def test_cast::expression_is_not_abstract():
    assert not inspect.isabstract(cast::expression)


def test_cast::expression_constructor_exists():
    assert callable(cast::expression.__init__)


def test_cast::expression_constructor_args():
    sig = inspect.signature(cast::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::designator::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::designator::list)


def test_mydsl::designator::list_constructor_exists():
    assert callable(myDsl::designator::list.__init__)


def test_mydsl::designator::list_constructor_args():
    sig = inspect.signature(myDsl::designator::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::initializer::listr_is_not_abstract():
    assert not inspect.isabstract(myDsl::initializer::listR)


def test_mydsl::initializer::listr_constructor_exists():
    assert callable(myDsl::initializer::listR.__init__)


def test_mydsl::initializer::listr_constructor_args():
    sig = inspect.signature(myDsl::initializer::listR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::cast::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::cast::expression)


def test_mydsl::cast::expression_constructor_exists():
    assert callable(myDsl::cast::expression.__init__)


def test_mydsl::cast::expression_constructor_args():
    sig = inspect.signature(myDsl::cast::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::multiplicative::expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl::multiplicative::expressionR)


def test_mydsl::multiplicative::expressionr_constructor_exists():
    assert callable(myDsl::multiplicative::expressionR.__init__)


def test_mydsl::multiplicative::expressionr_constructor_args():
    sig = inspect.signature(myDsl::multiplicative::expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::additive::expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl::additive::expressionR)


def test_mydsl::additive::expressionr_constructor_exists():
    assert callable(myDsl::additive::expressionR.__init__)


def test_mydsl::additive::expressionr_constructor_args():
    sig = inspect.signature(myDsl::additive::expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::multiplicative::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::multiplicative::expression)


def test_mydsl::multiplicative::expression_constructor_exists():
    assert callable(myDsl::multiplicative::expression.__init__)


def test_mydsl::multiplicative::expression_constructor_args():
    sig = inspect.signature(myDsl::multiplicative::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::type::name_is_not_abstract():
    assert not inspect.isabstract(myDsl::type::name)


def test_mydsl::type::name_constructor_exists():
    assert callable(myDsl::type::name.__init__)


def test_mydsl::type::name_constructor_args():
    sig = inspect.signature(myDsl::type::name.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::unary::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::unary::expression)


def test_mydsl::unary::expression_constructor_exists():
    assert callable(myDsl::unary::expression.__init__)


def test_mydsl::unary::expression_constructor_args():
    sig = inspect.signature(myDsl::unary::expression.__init__)
    params = list(sig.parameters.keys())
    assert "Unary_operator" in params, "Missing parameter 'Unary_operator'"

def test_mydsl::unary::expression_has_Unary_operator():
    assert hasattr(myDsl::unary::expression, "Unary_operator")
    descriptor = None
    for klass in myDsl::unary::expression.__mro__:
        if "Unary_operator" in klass.__dict__:
            descriptor = klass.__dict__["Unary_operator"]
            break
    assert isinstance(descriptor, property)



def test_initializer_is_not_abstract():
    assert not inspect.isabstract(initializer)


def test_initializer_constructor_exists():
    assert callable(initializer.__init__)


def test_initializer_constructor_args():
    sig = inspect.signature(initializer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::initializer::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::initializer::list)


def test_mydsl::initializer::list_constructor_exists():
    assert callable(myDsl::initializer::list.__init__)


def test_mydsl::initializer::list_constructor_args():
    sig = inspect.signature(myDsl::initializer::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::relational::expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl::relational::expressionR)


def test_mydsl::relational::expressionr_constructor_exists():
    assert callable(myDsl::relational::expressionR.__init__)


def test_mydsl::relational::expressionr_constructor_args():
    sig = inspect.signature(myDsl::relational::expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::shift::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::shift::expression)


def test_mydsl::shift::expression_constructor_exists():
    assert callable(myDsl::shift::expression.__init__)


def test_mydsl::shift::expression_constructor_args():
    sig = inspect.signature(myDsl::shift::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::equality::expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl::equality::expressionR)


def test_mydsl::equality::expressionr_constructor_exists():
    assert callable(myDsl::equality::expressionR.__init__)


def test_mydsl::equality::expressionr_constructor_args():
    sig = inspect.signature(myDsl::equality::expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::relational::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::relational::expression)


def test_mydsl::relational::expression_constructor_exists():
    assert callable(myDsl::relational::expression.__init__)


def test_mydsl::relational::expression_constructor_args():
    sig = inspect.signature(myDsl::relational::expression.__init__)
    params = list(sig.parameters.keys())



def test_shift::expression_is_not_abstract():
    assert not inspect.isabstract(shift::expression)


def test_shift::expression_constructor_exists():
    assert callable(shift::expression.__init__)


def test_shift::expression_constructor_args():
    sig = inspect.signature(shift::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::additive::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::additive::expression)


def test_mydsl::additive::expression_constructor_exists():
    assert callable(myDsl::additive::expression.__init__)


def test_mydsl::additive::expression_constructor_args():
    sig = inspect.signature(myDsl::additive::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::shift::expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl::shift::expressionR)


def test_mydsl::shift::expressionr_constructor_exists():
    assert callable(myDsl::shift::expressionR.__init__)


def test_mydsl::shift::expressionr_constructor_args():
    sig = inspect.signature(myDsl::shift::expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::inclusive::or::expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl::inclusive::or::expressionR)


def test_mydsl::inclusive::or::expressionr_constructor_exists():
    assert callable(myDsl::inclusive::or::expressionR.__init__)


def test_mydsl::inclusive::or::expressionr_constructor_args():
    sig = inspect.signature(myDsl::inclusive::or::expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::exclusive::or::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::exclusive::or::expression)


def test_mydsl::exclusive::or::expression_constructor_exists():
    assert callable(myDsl::exclusive::or::expression.__init__)


def test_mydsl::exclusive::or::expression_constructor_args():
    sig = inspect.signature(myDsl::exclusive::or::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::logical::and::expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl::logical::and::expressionR)


def test_mydsl::logical::and::expressionr_constructor_exists():
    assert callable(myDsl::logical::and::expressionR.__init__)


def test_mydsl::logical::and::expressionr_constructor_args():
    sig = inspect.signature(myDsl::logical::and::expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::equality::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::equality::expression)


def test_mydsl::equality::expression_constructor_exists():
    assert callable(myDsl::equality::expression.__init__)


def test_mydsl::equality::expression_constructor_args():
    sig = inspect.signature(myDsl::equality::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::and::expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl::and::expressionR)


def test_mydsl::and::expressionr_constructor_exists():
    assert callable(myDsl::and::expressionR.__init__)


def test_mydsl::and::expressionr_constructor_args():
    sig = inspect.signature(myDsl::and::expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::exclusive::or::expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl::exclusive::or::expressionR)


def test_mydsl::exclusive::or::expressionr_constructor_exists():
    assert callable(myDsl::exclusive::or::expressionR.__init__)


def test_mydsl::exclusive::or::expressionr_constructor_args():
    sig = inspect.signature(myDsl::exclusive::or::expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::and::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::and::expression)


def test_mydsl::and::expression_constructor_exists():
    assert callable(myDsl::and::expression.__init__)


def test_mydsl::and::expression_constructor_args():
    sig = inspect.signature(myDsl::and::expression.__init__)
    params = list(sig.parameters.keys())



def test_constant::expression_is_not_abstract():
    assert not inspect.isabstract(constant::expression)


def test_constant::expression_constructor_exists():
    assert callable(constant::expression.__init__)


def test_constant::expression_constructor_args():
    sig = inspect.signature(constant::expression.__init__)
    params = list(sig.parameters.keys())



def test_assignment::expression_is_not_abstract():
    assert not inspect.isabstract(assignment::expression)


def test_assignment::expression_constructor_exists():
    assert callable(assignment::expression.__init__)


def test_assignment::expression_constructor_args():
    sig = inspect.signature(assignment::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::conditional::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::conditional::expression)


def test_mydsl::conditional::expression_constructor_exists():
    assert callable(myDsl::conditional::expression.__init__)


def test_mydsl::conditional::expression_constructor_args():
    sig = inspect.signature(myDsl::conditional::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl::expressionR)


def test_mydsl::expressionr_constructor_exists():
    assert callable(myDsl::expressionR.__init__)


def test_mydsl::expressionr_constructor_args():
    sig = inspect.signature(myDsl::expressionR.__init__)
    params = list(sig.parameters.keys())



def test_primary::expression_is_not_abstract():
    assert not inspect.isabstract(primary::expression)


def test_primary::expression_constructor_exists():
    assert callable(primary::expression.__init__)


def test_primary::expression_constructor_args():
    sig = inspect.signature(primary::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::stringc_is_not_abstract():
    assert not inspect.isabstract(myDsl::StringC)


def test_mydsl::stringc_constructor_exists():
    assert callable(myDsl::StringC.__init__)


def test_mydsl::stringc_constructor_args():
    sig = inspect.signature(myDsl::StringC.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"

def test_mydsl::stringc_has_string():
    assert hasattr(myDsl::StringC, "string")
    descriptor = None
    for klass in myDsl::StringC.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_expression::statement_is_not_abstract():
    assert not inspect.isabstract(expression::statement)


def test_expression::statement_constructor_exists():
    assert callable(expression::statement.__init__)


def test_expression::statement_constructor_args():
    sig = inspect.signature(expression::statement.__init__)
    params = list(sig.parameters.keys())



def test_jump::statement_is_not_abstract():
    assert not inspect.isabstract(jump::statement)


def test_jump::statement_constructor_exists():
    assert callable(jump::statement.__init__)


def test_jump::statement_constructor_args():
    sig = inspect.signature(jump::statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::identifier_is_not_abstract():
    assert not inspect.isabstract(myDsl::IDENTIFIER)


def test_mydsl::identifier_constructor_exists():
    assert callable(myDsl::IDENTIFIER.__init__)


def test_mydsl::identifier_constructor_args():
    sig = inspect.signature(myDsl::IDENTIFIER.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::identifier_has_name():
    assert hasattr(myDsl::IDENTIFIER, "name")
    descriptor = None
    for klass in myDsl::IDENTIFIER.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::inclusive::or::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::inclusive::or::expression)


def test_mydsl::inclusive::or::expression_constructor_exists():
    assert callable(myDsl::inclusive::or::expression.__init__)


def test_mydsl::inclusive::or::expression_constructor_args():
    sig = inspect.signature(myDsl::inclusive::or::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::logical::or::expressionr_is_not_abstract():
    assert not inspect.isabstract(myDsl::logical::or::expressionR)


def test_mydsl::logical::or::expressionr_constructor_exists():
    assert callable(myDsl::logical::or::expressionR.__init__)


def test_mydsl::logical::or::expressionr_constructor_args():
    sig = inspect.signature(myDsl::logical::or::expressionR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::logical::and::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::logical::and::expression)


def test_mydsl::logical::and::expression_constructor_exists():
    assert callable(myDsl::logical::and::expression.__init__)


def test_mydsl::logical::and::expression_constructor_args():
    sig = inspect.signature(myDsl::logical::and::expression.__init__)
    params = list(sig.parameters.keys())



def test_conditional::expression_is_not_abstract():
    assert not inspect.isabstract(conditional::expression)


def test_conditional::expression_constructor_exists():
    assert callable(conditional::expression.__init__)


def test_conditional::expression_constructor_args():
    sig = inspect.signature(conditional::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::logical::or::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::logical::or::expression)


def test_mydsl::logical::or::expression_constructor_exists():
    assert callable(myDsl::logical::or::expression.__init__)


def test_mydsl::logical::or::expression_constructor_args():
    sig = inspect.signature(myDsl::logical::or::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::initializer_is_not_abstract():
    assert not inspect.isabstract(myDsl::initializer)


def test_mydsl::initializer_constructor_exists():
    assert callable(myDsl::initializer.__init__)


def test_mydsl::initializer_constructor_args():
    sig = inspect.signature(myDsl::initializer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::init::declarator::listr_is_not_abstract():
    assert not inspect.isabstract(myDsl::init::declarator::listR)


def test_mydsl::init::declarator::listr_constructor_exists():
    assert callable(myDsl::init::declarator::listR.__init__)


def test_mydsl::init::declarator::listr_constructor_args():
    sig = inspect.signature(myDsl::init::declarator::listR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::init::declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl::init::declarator)


def test_mydsl::init::declarator_constructor_exists():
    assert callable(myDsl::init::declarator.__init__)


def test_mydsl::init::declarator_constructor_args():
    sig = inspect.signature(myDsl::init::declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::init::declarator::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::init::declarator::list)


def test_mydsl::init::declarator::list_constructor_exists():
    assert callable(myDsl::init::declarator::list.__init__)


def test_mydsl::init::declarator::list_constructor_args():
    sig = inspect.signature(myDsl::init::declarator::list.__init__)
    params = list(sig.parameters.keys())



def test_parameter::declaration_is_not_abstract():
    assert not inspect.isabstract(parameter::declaration)


def test_parameter::declaration_constructor_exists():
    assert callable(parameter::declaration.__init__)


def test_parameter::declaration_constructor_args():
    sig = inspect.signature(parameter::declaration.__init__)
    params = list(sig.parameters.keys())



def test_block::item_is_not_abstract():
    assert not inspect.isabstract(block::item)


def test_block::item_constructor_exists():
    assert callable(block::item.__init__)


def test_block::item_constructor_args():
    sig = inspect.signature(block::item.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::statement)


def test_mydsl::statement_constructor_exists():
    assert callable(myDsl::statement.__init__)


def test_mydsl::statement_constructor_args():
    sig = inspect.signature(myDsl::statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::block::item::listr_is_not_abstract():
    assert not inspect.isabstract(myDsl::block::item::listR)


def test_mydsl::block::item::listr_constructor_exists():
    assert callable(myDsl::block::item::listR.__init__)


def test_mydsl::block::item::listr_constructor_args():
    sig = inspect.signature(myDsl::block::item::listR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::block::item_is_not_abstract():
    assert not inspect.isabstract(myDsl::block::item)


def test_mydsl::block::item_constructor_exists():
    assert callable(myDsl::block::item.__init__)


def test_mydsl::block::item_constructor_args():
    sig = inspect.signature(myDsl::block::item.__init__)
    params = list(sig.parameters.keys())



def test_compound::statement_is_not_abstract():
    assert not inspect.isabstract(compound::statement)


def test_compound::statement_constructor_exists():
    assert callable(compound::statement.__init__)


def test_compound::statement_constructor_args():
    sig = inspect.signature(compound::statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::block::item::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::block::item::list)


def test_mydsl::block::item::list_constructor_exists():
    assert callable(myDsl::block::item::list.__init__)


def test_mydsl::block::item::list_constructor_args():
    sig = inspect.signature(myDsl::block::item::list.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(statement)


def test_statement_constructor_exists():
    assert callable(statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::selection::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::selection::statement)


def test_mydsl::selection::statement_constructor_exists():
    assert callable(myDsl::selection::statement.__init__)


def test_mydsl::selection::statement_constructor_args():
    sig = inspect.signature(myDsl::selection::statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::jump::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::jump::statement)


def test_mydsl::jump::statement_constructor_exists():
    assert callable(myDsl::jump::statement.__init__)


def test_mydsl::jump::statement_constructor_args():
    sig = inspect.signature(myDsl::jump::statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::expression::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::expression::statement)


def test_mydsl::expression::statement_constructor_exists():
    assert callable(myDsl::expression::statement.__init__)


def test_mydsl::expression::statement_constructor_args():
    sig = inspect.signature(myDsl::expression::statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::expression)


def test_mydsl::expression_constructor_exists():
    assert callable(myDsl::expression.__init__)


def test_mydsl::expression_constructor_args():
    sig = inspect.signature(myDsl::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::iteration::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::iteration::statement)


def test_mydsl::iteration::statement_constructor_exists():
    assert callable(myDsl::iteration::statement.__init__)


def test_mydsl::iteration::statement_constructor_args():
    sig = inspect.signature(myDsl::iteration::statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::labeled::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::labeled::statement)


def test_mydsl::labeled::statement_constructor_exists():
    assert callable(myDsl::labeled::statement.__init__)


def test_mydsl::labeled::statement_constructor_args():
    sig = inspect.signature(myDsl::labeled::statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::parameter::listr_is_not_abstract():
    assert not inspect.isabstract(myDsl::parameter::listR)


def test_mydsl::parameter::listr_constructor_exists():
    assert callable(myDsl::parameter::listR.__init__)


def test_mydsl::parameter::listr_constructor_args():
    sig = inspect.signature(myDsl::parameter::listR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::parameter::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::parameter::declaration)


def test_mydsl::parameter::declaration_constructor_exists():
    assert callable(myDsl::parameter::declaration.__init__)


def test_mydsl::parameter::declaration_constructor_args():
    sig = inspect.signature(myDsl::parameter::declaration.__init__)
    params = list(sig.parameters.keys())



def test_parameter::type::list_is_not_abstract():
    assert not inspect.isabstract(parameter::type::list)


def test_parameter::type::list_constructor_exists():
    assert callable(parameter::type::list.__init__)


def test_parameter::type::list_constructor_args():
    sig = inspect.signature(parameter::type::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::parameter::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::parameter::list)


def test_mydsl::parameter::list_constructor_exists():
    assert callable(myDsl::parameter::list.__init__)


def test_mydsl::parameter::list_constructor_args():
    sig = inspect.signature(myDsl::parameter::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::identifier::listr_is_not_abstract():
    assert not inspect.isabstract(myDsl::identifier::listR)


def test_mydsl::identifier::listr_constructor_exists():
    assert callable(myDsl::identifier::listR.__init__)


def test_mydsl::identifier::listr_constructor_args():
    sig = inspect.signature(myDsl::identifier::listR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::declaration::listr_is_not_abstract():
    assert not inspect.isabstract(myDsl::declaration::listR)


def test_mydsl::declaration::listr_constructor_exists():
    assert callable(myDsl::declaration::listR.__init__)


def test_mydsl::declaration::listr_constructor_args():
    sig = inspect.signature(myDsl::declaration::listR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::abstract::declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl::abstract::declarator)


def test_mydsl::abstract::declarator_constructor_exists():
    assert callable(myDsl::abstract::declarator.__init__)


def test_mydsl::abstract::declarator_constructor_args():
    sig = inspect.signature(myDsl::abstract::declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::type::qualifier::listr_is_not_abstract():
    assert not inspect.isabstract(myDsl::type::qualifier::listR)


def test_mydsl::type::qualifier::listr_constructor_exists():
    assert callable(myDsl::type::qualifier::listR.__init__)


def test_mydsl::type::qualifier::listr_constructor_args():
    sig = inspect.signature(myDsl::type::qualifier::listR.__init__)
    params = list(sig.parameters.keys())
    assert "Type_qualifier" in params, "Missing parameter 'Type_qualifier'"

def test_mydsl::type::qualifier::listr_has_Type_qualifier():
    assert hasattr(myDsl::type::qualifier::listR, "Type_qualifier")
    descriptor = None
    for klass in myDsl::type::qualifier::listR.__mro__:
        if "Type_qualifier" in klass.__dict__:
            descriptor = klass.__dict__["Type_qualifier"]
            break
    assert isinstance(descriptor, property)



def test_pointer_is_not_abstract():
    assert not inspect.isabstract(pointer)


def test_pointer_constructor_exists():
    assert callable(pointer.__init__)


def test_pointer_constructor_args():
    sig = inspect.signature(pointer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::type::qualifier::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::type::qualifier::list)


def test_mydsl::type::qualifier::list_constructor_exists():
    assert callable(myDsl::type::qualifier::list.__init__)


def test_mydsl::type::qualifier::list_constructor_args():
    sig = inspect.signature(myDsl::type::qualifier::list.__init__)
    params = list(sig.parameters.keys())
    assert "Type_qualifier" in params, "Missing parameter 'Type_qualifier'"

def test_mydsl::type::qualifier::list_has_Type_qualifier():
    assert hasattr(myDsl::type::qualifier::list, "Type_qualifier")
    descriptor = None
    for klass in myDsl::type::qualifier::list.__mro__:
        if "Type_qualifier" in klass.__dict__:
            descriptor = klass.__dict__["Type_qualifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::pointer_is_not_abstract():
    assert not inspect.isabstract(myDsl::pointer)


def test_mydsl::pointer_constructor_exists():
    assert callable(myDsl::pointer.__init__)


def test_mydsl::pointer_constructor_args():
    sig = inspect.signature(myDsl::pointer.__init__)
    params = list(sig.parameters.keys())



def test_struct::declarator_is_not_abstract():
    assert not inspect.isabstract(struct::declarator)


def test_struct::declarator_constructor_exists():
    assert callable(struct::declarator.__init__)


def test_struct::declarator_constructor_args():
    sig = inspect.signature(struct::declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::constant::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::constant::expression)


def test_mydsl::constant::expression_constructor_exists():
    assert callable(myDsl::constant::expression.__init__)


def test_mydsl::constant::expression_constructor_args():
    sig = inspect.signature(myDsl::constant::expression.__init__)
    params = list(sig.parameters.keys())



def test_init::declarator_is_not_abstract():
    assert not inspect.isabstract(init::declarator)


def test_init::declarator_constructor_exists():
    assert callable(init::declarator.__init__)


def test_init::declarator_constructor_args():
    sig = inspect.signature(init::declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::compound::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::compound::statement)


def test_mydsl::compound::statement_constructor_exists():
    assert callable(myDsl::compound::statement.__init__)


def test_mydsl::compound::statement_constructor_args():
    sig = inspect.signature(myDsl::compound::statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::identifier::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::identifier::list)


def test_mydsl::identifier::list_constructor_exists():
    assert callable(myDsl::identifier::list.__init__)


def test_mydsl::identifier::list_constructor_args():
    sig = inspect.signature(myDsl::identifier::list.__init__)
    params = list(sig.parameters.keys())



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
    assert "Assignment_operator" in params, "Missing parameter 'Assignment_operator'"

def test_mydsl::assignment::expression_has_Assignment_operator():
    assert hasattr(myDsl::assignment::expression, "Assignment_operator")
    descriptor = None
    for klass in myDsl::assignment::expression.__mro__:
        if "Assignment_operator" in klass.__dict__:
            descriptor = klass.__dict__["Assignment_operator"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::direct::declaratorr_is_not_abstract():
    assert not inspect.isabstract(myDsl::direct::declaratorR)


def test_mydsl::direct::declaratorr_constructor_exists():
    assert callable(myDsl::direct::declaratorR.__init__)


def test_mydsl::direct::declaratorr_constructor_args():
    sig = inspect.signature(myDsl::direct::declaratorR.__init__)
    params = list(sig.parameters.keys())



def test_declarator_is_not_abstract():
    assert not inspect.isabstract(declarator)


def test_declarator_constructor_exists():
    assert callable(declarator.__init__)


def test_declarator_constructor_args():
    sig = inspect.signature(declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::direct::declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl::direct::declarator)


def test_mydsl::direct::declarator_constructor_exists():
    assert callable(myDsl::direct::declarator.__init__)


def test_mydsl::direct::declarator_constructor_args():
    sig = inspect.signature(myDsl::direct::declarator.__init__)
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



def test_mydsl::declaration::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::declaration::list)


def test_mydsl::declaration::list_constructor_exists():
    assert callable(myDsl::declaration::list.__init__)


def test_mydsl::declaration::list_constructor_args():
    sig = inspect.signature(myDsl::declaration::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl::declarator)


def test_mydsl::declarator_constructor_exists():
    assert callable(myDsl::declarator.__init__)


def test_mydsl::declarator_constructor_args():
    sig = inspect.signature(myDsl::declarator.__init__)
    params = list(sig.parameters.keys())



def test_external::declaration_is_not_abstract():
    assert not inspect.isabstract(external::declaration)


def test_external::declaration_constructor_exists():
    assert callable(external::declaration.__init__)


def test_external::declaration_constructor_args():
    sig = inspect.signature(external::declaration.__init__)
    params = list(sig.parameters.keys())



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



def test_mydsl::declaration::specifiers_is_not_abstract():
    assert not inspect.isabstract(myDsl::declaration::specifiers)


def test_mydsl::declaration::specifiers_constructor_exists():
    assert callable(myDsl::declaration::specifiers.__init__)


def test_mydsl::declaration::specifiers_constructor_args():
    sig = inspect.signature(myDsl::declaration::specifiers.__init__)
    params = list(sig.parameters.keys())
    assert "Type_qualifier" in params, "Missing parameter 'Type_qualifier'"
    assert "Storage_class_specifier" in params, "Missing parameter 'Storage_class_specifier'"

def test_mydsl::declaration::specifiers_has_Type_qualifier():
    assert hasattr(myDsl::declaration::specifiers, "Type_qualifier")
    descriptor = None
    for klass in myDsl::declaration::specifiers.__mro__:
        if "Type_qualifier" in klass.__dict__:
            descriptor = klass.__dict__["Type_qualifier"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::declaration::specifiers_has_Storage_class_specifier():
    assert hasattr(myDsl::declaration::specifiers, "Storage_class_specifier")
    descriptor = None
    for klass in myDsl::declaration::specifiers.__mro__:
        if "Storage_class_specifier" in klass.__dict__:
            descriptor = klass.__dict__["Storage_class_specifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::translation::unitr_is_not_abstract():
    assert not inspect.isabstract(myDsl::translation::unitR)


def test_mydsl::translation::unitr_constructor_exists():
    assert callable(myDsl::translation::unitR.__init__)


def test_mydsl::translation::unitr_constructor_args():
    sig = inspect.signature(myDsl::translation::unitR.__init__)
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
postfix::expressionR_strategy = st.builds(
    postfix::expressionR,
)
struct::or::union::specifier_strategy = st.builds(
    struct::or::union::specifier,
)
labeled::statement_strategy = st.builds(
    labeled::statement,
)
identifier::listR_strategy = st.builds(
    identifier::listR,
)
identifier::list_strategy = st.builds(
    identifier::list,
)
direct::declarator_strategy = st.builds(
    direct::declarator,
)
declaration::specifiers_strategy = st.builds(
    declaration::specifiers,
)
myDsl::argument::expression::list_strategy = st.builds(
    myDsl::argument::expression::list,
)
myDsl::EObject_strategy = st.builds(
    myDsl::EObject,
)
abstract::declarator_strategy = st.builds(
    abstract::declarator,
)
myDsl::argument::expression::listR_strategy = st.builds(
    myDsl::argument::expression::listR,
)
type::specifier_strategy = st.builds(
    type::specifier,
)
myDsl::atomic::type::specifier_strategy = st.builds(
    myDsl::atomic::type::specifier,
)
myDsl::struct::or::union::specifier_strategy = st.builds(
    myDsl::struct::or::union::specifier,
    Struct_or_union=
        safe_text
)
declaration_strategy = st.builds(
    declaration,
)
myDsl::struct::declaration_strategy = st.builds(
    myDsl::struct::declaration,
)
myDsl::struct::declaration::list_strategy = st.builds(
    myDsl::struct::declaration::list,
)
myDsl::struct::declarator::listR_strategy = st.builds(
    myDsl::struct::declarator::listR,
)
myDsl::struct::declarator_strategy = st.builds(
    myDsl::struct::declarator,
)
myDsl::struct::declarator::list_strategy = st.builds(
    myDsl::struct::declarator::list,
)
myDsl::struct::declaration::listR_strategy = st.builds(
    myDsl::struct::declaration::listR,
)
myDsl::type::specifier_strategy = st.builds(
    myDsl::type::specifier,
)
struct::declaration_strategy = st.builds(
    struct::declaration,
)
myDsl::static::assert::declaration_strategy = st.builds(
    myDsl::static::assert::declaration,
)
type::name_strategy = st.builds(
    type::name,
)
myDsl::specifier::qualifier::list_strategy = st.builds(
    myDsl::specifier::qualifier::list,
)
myDsl::designator::listR_strategy = st.builds(
    myDsl::designator::listR,
)
myDsl::designator_strategy = st.builds(
    myDsl::designator,
)
designation_strategy = st.builds(
    designation,
)
atomic::type::specifier_strategy = st.builds(
    atomic::type::specifier,
)
static::assert::declaration_strategy = st.builds(
    static::assert::declaration,
)
designator_strategy = st.builds(
    designator,
)
myDsl::designation_strategy = st.builds(
    myDsl::designation,
)
myDsl::postfix::expressionR_strategy = st.builds(
    myDsl::postfix::expressionR,
)
myDsl::primary::expression_strategy = st.builds(
    myDsl::primary::expression,
)
unary::expression_strategy = st.builds(
    unary::expression,
)
myDsl::postfix::expression_strategy = st.builds(
    myDsl::postfix::expression,
)
cast::expression_strategy = st.builds(
    cast::expression,
)
myDsl::designator::list_strategy = st.builds(
    myDsl::designator::list,
)
myDsl::initializer::listR_strategy = st.builds(
    myDsl::initializer::listR,
)
myDsl::cast::expression_strategy = st.builds(
    myDsl::cast::expression,
)
myDsl::multiplicative::expressionR_strategy = st.builds(
    myDsl::multiplicative::expressionR,
)
myDsl::additive::expressionR_strategy = st.builds(
    myDsl::additive::expressionR,
)
myDsl::multiplicative::expression_strategy = st.builds(
    myDsl::multiplicative::expression,
)
myDsl::type::name_strategy = st.builds(
    myDsl::type::name,
)
myDsl::unary::expression_strategy = st.builds(
    myDsl::unary::expression,
    Unary_operator=
        safe_text
)
initializer_strategy = st.builds(
    initializer,
)
myDsl::initializer::list_strategy = st.builds(
    myDsl::initializer::list,
)
myDsl::relational::expressionR_strategy = st.builds(
    myDsl::relational::expressionR,
)
myDsl::shift::expression_strategy = st.builds(
    myDsl::shift::expression,
)
myDsl::equality::expressionR_strategy = st.builds(
    myDsl::equality::expressionR,
)
myDsl::relational::expression_strategy = st.builds(
    myDsl::relational::expression,
)
shift::expression_strategy = st.builds(
    shift::expression,
)
myDsl::additive::expression_strategy = st.builds(
    myDsl::additive::expression,
)
myDsl::shift::expressionR_strategy = st.builds(
    myDsl::shift::expressionR,
)
myDsl::inclusive::or::expressionR_strategy = st.builds(
    myDsl::inclusive::or::expressionR,
)
myDsl::exclusive::or::expression_strategy = st.builds(
    myDsl::exclusive::or::expression,
)
myDsl::logical::and::expressionR_strategy = st.builds(
    myDsl::logical::and::expressionR,
)
myDsl::equality::expression_strategy = st.builds(
    myDsl::equality::expression,
)
myDsl::and::expressionR_strategy = st.builds(
    myDsl::and::expressionR,
)
myDsl::exclusive::or::expressionR_strategy = st.builds(
    myDsl::exclusive::or::expressionR,
)
myDsl::and::expression_strategy = st.builds(
    myDsl::and::expression,
)
constant::expression_strategy = st.builds(
    constant::expression,
)
assignment::expression_strategy = st.builds(
    assignment::expression,
)
myDsl::conditional::expression_strategy = st.builds(
    myDsl::conditional::expression,
)
myDsl::expressionR_strategy = st.builds(
    myDsl::expressionR,
)
primary::expression_strategy = st.builds(
    primary::expression,
)
myDsl::StringC_strategy = st.builds(
    myDsl::StringC,
    string=
        safe_text
)
expression::statement_strategy = st.builds(
    expression::statement,
)
jump::statement_strategy = st.builds(
    jump::statement,
)
myDsl::IDENTIFIER_strategy = st.builds(
    myDsl::IDENTIFIER,
    name=
        safe_text
)
myDsl::inclusive::or::expression_strategy = st.builds(
    myDsl::inclusive::or::expression,
)
myDsl::logical::or::expressionR_strategy = st.builds(
    myDsl::logical::or::expressionR,
)
myDsl::logical::and::expression_strategy = st.builds(
    myDsl::logical::and::expression,
)
conditional::expression_strategy = st.builds(
    conditional::expression,
)
myDsl::logical::or::expression_strategy = st.builds(
    myDsl::logical::or::expression,
)
myDsl::initializer_strategy = st.builds(
    myDsl::initializer,
)
myDsl::init::declarator::listR_strategy = st.builds(
    myDsl::init::declarator::listR,
)
myDsl::init::declarator_strategy = st.builds(
    myDsl::init::declarator,
)
myDsl::init::declarator::list_strategy = st.builds(
    myDsl::init::declarator::list,
)
parameter::declaration_strategy = st.builds(
    parameter::declaration,
)
block::item_strategy = st.builds(
    block::item,
)
myDsl::statement_strategy = st.builds(
    myDsl::statement,
)
myDsl::block::item::listR_strategy = st.builds(
    myDsl::block::item::listR,
)
myDsl::block::item_strategy = st.builds(
    myDsl::block::item,
)
compound::statement_strategy = st.builds(
    compound::statement,
)
myDsl::block::item::list_strategy = st.builds(
    myDsl::block::item::list,
)
statement_strategy = st.builds(
    statement,
)
myDsl::selection::statement_strategy = st.builds(
    myDsl::selection::statement,
)
myDsl::jump::statement_strategy = st.builds(
    myDsl::jump::statement,
)
myDsl::expression::statement_strategy = st.builds(
    myDsl::expression::statement,
)
myDsl::expression_strategy = st.builds(
    myDsl::expression,
)
myDsl::iteration::statement_strategy = st.builds(
    myDsl::iteration::statement,
)
myDsl::labeled::statement_strategy = st.builds(
    myDsl::labeled::statement,
)
myDsl::parameter::listR_strategy = st.builds(
    myDsl::parameter::listR,
)
myDsl::parameter::declaration_strategy = st.builds(
    myDsl::parameter::declaration,
)
parameter::type::list_strategy = st.builds(
    parameter::type::list,
)
myDsl::parameter::list_strategy = st.builds(
    myDsl::parameter::list,
)
myDsl::identifier::listR_strategy = st.builds(
    myDsl::identifier::listR,
)
myDsl::declaration::listR_strategy = st.builds(
    myDsl::declaration::listR,
)
myDsl::abstract::declarator_strategy = st.builds(
    myDsl::abstract::declarator,
)
myDsl::type::qualifier::listR_strategy = st.builds(
    myDsl::type::qualifier::listR,
    Type_qualifier=
        safe_text
)
pointer_strategy = st.builds(
    pointer,
)
myDsl::type::qualifier::list_strategy = st.builds(
    myDsl::type::qualifier::list,
    Type_qualifier=
        safe_text
)
myDsl::pointer_strategy = st.builds(
    myDsl::pointer,
)
struct::declarator_strategy = st.builds(
    struct::declarator,
)
myDsl::constant::expression_strategy = st.builds(
    myDsl::constant::expression,
)
init::declarator_strategy = st.builds(
    init::declarator,
)
myDsl::compound::statement_strategy = st.builds(
    myDsl::compound::statement,
)
myDsl::identifier::list_strategy = st.builds(
    myDsl::identifier::list,
)
myDsl::parameter::type::list_strategy = st.builds(
    myDsl::parameter::type::list,
)
myDsl::assignment::expression_strategy = st.builds(
    myDsl::assignment::expression,
    Assignment_operator=
        safe_text
)
myDsl::direct::declaratorR_strategy = st.builds(
    myDsl::direct::declaratorR,
)
declarator_strategy = st.builds(
    declarator,
)
myDsl::direct::declarator_strategy = st.builds(
    myDsl::direct::declarator,
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
myDsl::declaration::list_strategy = st.builds(
    myDsl::declaration::list,
)
myDsl::declarator_strategy = st.builds(
    myDsl::declarator,
)
external::declaration_strategy = st.builds(
    external::declaration,
)
myDsl::declaration_strategy = st.builds(
    myDsl::declaration,
)
myDsl::function::definition_strategy = st.builds(
    myDsl::function::definition,
)
myDsl::declaration::specifiers_strategy = st.builds(
    myDsl::declaration::specifiers,
    Type_qualifier=
        safe_text,
    Storage_class_specifier=
        safe_text
)
myDsl::translation::unitR_strategy = st.builds(
    myDsl::translation::unitR,
)

@given(instance=postfix::expressionR_strategy)
@settings(max_examples=50)
def test_postfix::expressionr_instantiation(instance):
    assert isinstance(instance, postfix::expressionR)

@given(instance=struct::or::union::specifier_strategy)
@settings(max_examples=50)
def test_struct::or::union::specifier_instantiation(instance):
    assert isinstance(instance, struct::or::union::specifier)

@given(instance=labeled::statement_strategy)
@settings(max_examples=50)
def test_labeled::statement_instantiation(instance):
    assert isinstance(instance, labeled::statement)

@given(instance=identifier::listR_strategy)
@settings(max_examples=50)
def test_identifier::listr_instantiation(instance):
    assert isinstance(instance, identifier::listR)

@given(instance=identifier::list_strategy)
@settings(max_examples=50)
def test_identifier::list_instantiation(instance):
    assert isinstance(instance, identifier::list)

@given(instance=direct::declarator_strategy)
@settings(max_examples=50)
def test_direct::declarator_instantiation(instance):
    assert isinstance(instance, direct::declarator)

@given(instance=declaration::specifiers_strategy)
@settings(max_examples=50)
def test_declaration::specifiers_instantiation(instance):
    assert isinstance(instance, declaration::specifiers)

@given(instance=myDsl::argument::expression::list_strategy)
@settings(max_examples=50)
def test_mydsl::argument::expression::list_instantiation(instance):
    assert isinstance(instance, myDsl::argument::expression::list)

@given(instance=myDsl::EObject_strategy)
@settings(max_examples=50)
def test_mydsl::eobject_instantiation(instance):
    assert isinstance(instance, myDsl::EObject)

@given(instance=abstract::declarator_strategy)
@settings(max_examples=50)
def test_abstract::declarator_instantiation(instance):
    assert isinstance(instance, abstract::declarator)

@given(instance=myDsl::argument::expression::listR_strategy)
@settings(max_examples=50)
def test_mydsl::argument::expression::listr_instantiation(instance):
    assert isinstance(instance, myDsl::argument::expression::listR)

@given(instance=type::specifier_strategy)
@settings(max_examples=50)
def test_type::specifier_instantiation(instance):
    assert isinstance(instance, type::specifier)

@given(instance=myDsl::atomic::type::specifier_strategy)
@settings(max_examples=50)
def test_mydsl::atomic::type::specifier_instantiation(instance):
    assert isinstance(instance, myDsl::atomic::type::specifier)

@given(instance=myDsl::struct::or::union::specifier_strategy)
@settings(max_examples=50)
def test_mydsl::struct::or::union::specifier_instantiation(instance):
    assert isinstance(instance, myDsl::struct::or::union::specifier)

@given(instance=myDsl::struct::or::union::specifier_strategy)
def test_mydsl::struct::or::union::specifier_Struct_or_union_type(instance):
    assert isinstance(instance.Struct_or_union, str)


@given(instance=myDsl::struct::or::union::specifier_strategy)
def test_mydsl::struct::or::union::specifier_Struct_or_union_setter(instance):
    original = instance.Struct_or_union
    instance.Struct_or_union = original
    assert instance.Struct_or_union == original

@given(instance=declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, declaration)

@given(instance=myDsl::struct::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::struct::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::struct::declaration)

@given(instance=myDsl::struct::declaration::list_strategy)
@settings(max_examples=50)
def test_mydsl::struct::declaration::list_instantiation(instance):
    assert isinstance(instance, myDsl::struct::declaration::list)

@given(instance=myDsl::struct::declarator::listR_strategy)
@settings(max_examples=50)
def test_mydsl::struct::declarator::listr_instantiation(instance):
    assert isinstance(instance, myDsl::struct::declarator::listR)

@given(instance=myDsl::struct::declarator_strategy)
@settings(max_examples=50)
def test_mydsl::struct::declarator_instantiation(instance):
    assert isinstance(instance, myDsl::struct::declarator)

@given(instance=myDsl::struct::declarator::list_strategy)
@settings(max_examples=50)
def test_mydsl::struct::declarator::list_instantiation(instance):
    assert isinstance(instance, myDsl::struct::declarator::list)

@given(instance=myDsl::struct::declaration::listR_strategy)
@settings(max_examples=50)
def test_mydsl::struct::declaration::listr_instantiation(instance):
    assert isinstance(instance, myDsl::struct::declaration::listR)

@given(instance=myDsl::type::specifier_strategy)
@settings(max_examples=50)
def test_mydsl::type::specifier_instantiation(instance):
    assert isinstance(instance, myDsl::type::specifier)

@given(instance=struct::declaration_strategy)
@settings(max_examples=50)
def test_struct::declaration_instantiation(instance):
    assert isinstance(instance, struct::declaration)

@given(instance=myDsl::static::assert::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::static::assert::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::static::assert::declaration)

@given(instance=type::name_strategy)
@settings(max_examples=50)
def test_type::name_instantiation(instance):
    assert isinstance(instance, type::name)

@given(instance=myDsl::specifier::qualifier::list_strategy)
@settings(max_examples=50)
def test_mydsl::specifier::qualifier::list_instantiation(instance):
    assert isinstance(instance, myDsl::specifier::qualifier::list)

@given(instance=myDsl::designator::listR_strategy)
@settings(max_examples=50)
def test_mydsl::designator::listr_instantiation(instance):
    assert isinstance(instance, myDsl::designator::listR)

@given(instance=myDsl::designator_strategy)
@settings(max_examples=50)
def test_mydsl::designator_instantiation(instance):
    assert isinstance(instance, myDsl::designator)

@given(instance=designation_strategy)
@settings(max_examples=50)
def test_designation_instantiation(instance):
    assert isinstance(instance, designation)

@given(instance=atomic::type::specifier_strategy)
@settings(max_examples=50)
def test_atomic::type::specifier_instantiation(instance):
    assert isinstance(instance, atomic::type::specifier)

@given(instance=static::assert::declaration_strategy)
@settings(max_examples=50)
def test_static::assert::declaration_instantiation(instance):
    assert isinstance(instance, static::assert::declaration)

@given(instance=designator_strategy)
@settings(max_examples=50)
def test_designator_instantiation(instance):
    assert isinstance(instance, designator)

@given(instance=myDsl::designation_strategy)
@settings(max_examples=50)
def test_mydsl::designation_instantiation(instance):
    assert isinstance(instance, myDsl::designation)

@given(instance=myDsl::postfix::expressionR_strategy)
@settings(max_examples=50)
def test_mydsl::postfix::expressionr_instantiation(instance):
    assert isinstance(instance, myDsl::postfix::expressionR)

@given(instance=myDsl::primary::expression_strategy)
@settings(max_examples=50)
def test_mydsl::primary::expression_instantiation(instance):
    assert isinstance(instance, myDsl::primary::expression)

@given(instance=unary::expression_strategy)
@settings(max_examples=50)
def test_unary::expression_instantiation(instance):
    assert isinstance(instance, unary::expression)

@given(instance=myDsl::postfix::expression_strategy)
@settings(max_examples=50)
def test_mydsl::postfix::expression_instantiation(instance):
    assert isinstance(instance, myDsl::postfix::expression)

@given(instance=cast::expression_strategy)
@settings(max_examples=50)
def test_cast::expression_instantiation(instance):
    assert isinstance(instance, cast::expression)

@given(instance=myDsl::designator::list_strategy)
@settings(max_examples=50)
def test_mydsl::designator::list_instantiation(instance):
    assert isinstance(instance, myDsl::designator::list)

@given(instance=myDsl::initializer::listR_strategy)
@settings(max_examples=50)
def test_mydsl::initializer::listr_instantiation(instance):
    assert isinstance(instance, myDsl::initializer::listR)

@given(instance=myDsl::cast::expression_strategy)
@settings(max_examples=50)
def test_mydsl::cast::expression_instantiation(instance):
    assert isinstance(instance, myDsl::cast::expression)

@given(instance=myDsl::multiplicative::expressionR_strategy)
@settings(max_examples=50)
def test_mydsl::multiplicative::expressionr_instantiation(instance):
    assert isinstance(instance, myDsl::multiplicative::expressionR)

@given(instance=myDsl::additive::expressionR_strategy)
@settings(max_examples=50)
def test_mydsl::additive::expressionr_instantiation(instance):
    assert isinstance(instance, myDsl::additive::expressionR)

@given(instance=myDsl::multiplicative::expression_strategy)
@settings(max_examples=50)
def test_mydsl::multiplicative::expression_instantiation(instance):
    assert isinstance(instance, myDsl::multiplicative::expression)

@given(instance=myDsl::type::name_strategy)
@settings(max_examples=50)
def test_mydsl::type::name_instantiation(instance):
    assert isinstance(instance, myDsl::type::name)

@given(instance=myDsl::unary::expression_strategy)
@settings(max_examples=50)
def test_mydsl::unary::expression_instantiation(instance):
    assert isinstance(instance, myDsl::unary::expression)

@given(instance=myDsl::unary::expression_strategy)
def test_mydsl::unary::expression_Unary_operator_type(instance):
    assert isinstance(instance.Unary_operator, str)


@given(instance=myDsl::unary::expression_strategy)
def test_mydsl::unary::expression_Unary_operator_setter(instance):
    original = instance.Unary_operator
    instance.Unary_operator = original
    assert instance.Unary_operator == original

@given(instance=initializer_strategy)
@settings(max_examples=50)
def test_initializer_instantiation(instance):
    assert isinstance(instance, initializer)

@given(instance=myDsl::initializer::list_strategy)
@settings(max_examples=50)
def test_mydsl::initializer::list_instantiation(instance):
    assert isinstance(instance, myDsl::initializer::list)

@given(instance=myDsl::relational::expressionR_strategy)
@settings(max_examples=50)
def test_mydsl::relational::expressionr_instantiation(instance):
    assert isinstance(instance, myDsl::relational::expressionR)

@given(instance=myDsl::shift::expression_strategy)
@settings(max_examples=50)
def test_mydsl::shift::expression_instantiation(instance):
    assert isinstance(instance, myDsl::shift::expression)

@given(instance=myDsl::equality::expressionR_strategy)
@settings(max_examples=50)
def test_mydsl::equality::expressionr_instantiation(instance):
    assert isinstance(instance, myDsl::equality::expressionR)

@given(instance=myDsl::relational::expression_strategy)
@settings(max_examples=50)
def test_mydsl::relational::expression_instantiation(instance):
    assert isinstance(instance, myDsl::relational::expression)

@given(instance=shift::expression_strategy)
@settings(max_examples=50)
def test_shift::expression_instantiation(instance):
    assert isinstance(instance, shift::expression)

@given(instance=myDsl::additive::expression_strategy)
@settings(max_examples=50)
def test_mydsl::additive::expression_instantiation(instance):
    assert isinstance(instance, myDsl::additive::expression)

@given(instance=myDsl::shift::expressionR_strategy)
@settings(max_examples=50)
def test_mydsl::shift::expressionr_instantiation(instance):
    assert isinstance(instance, myDsl::shift::expressionR)

@given(instance=myDsl::inclusive::or::expressionR_strategy)
@settings(max_examples=50)
def test_mydsl::inclusive::or::expressionr_instantiation(instance):
    assert isinstance(instance, myDsl::inclusive::or::expressionR)

@given(instance=myDsl::exclusive::or::expression_strategy)
@settings(max_examples=50)
def test_mydsl::exclusive::or::expression_instantiation(instance):
    assert isinstance(instance, myDsl::exclusive::or::expression)

@given(instance=myDsl::logical::and::expressionR_strategy)
@settings(max_examples=50)
def test_mydsl::logical::and::expressionr_instantiation(instance):
    assert isinstance(instance, myDsl::logical::and::expressionR)

@given(instance=myDsl::equality::expression_strategy)
@settings(max_examples=50)
def test_mydsl::equality::expression_instantiation(instance):
    assert isinstance(instance, myDsl::equality::expression)

@given(instance=myDsl::and::expressionR_strategy)
@settings(max_examples=50)
def test_mydsl::and::expressionr_instantiation(instance):
    assert isinstance(instance, myDsl::and::expressionR)

@given(instance=myDsl::exclusive::or::expressionR_strategy)
@settings(max_examples=50)
def test_mydsl::exclusive::or::expressionr_instantiation(instance):
    assert isinstance(instance, myDsl::exclusive::or::expressionR)

@given(instance=myDsl::and::expression_strategy)
@settings(max_examples=50)
def test_mydsl::and::expression_instantiation(instance):
    assert isinstance(instance, myDsl::and::expression)

@given(instance=constant::expression_strategy)
@settings(max_examples=50)
def test_constant::expression_instantiation(instance):
    assert isinstance(instance, constant::expression)

@given(instance=assignment::expression_strategy)
@settings(max_examples=50)
def test_assignment::expression_instantiation(instance):
    assert isinstance(instance, assignment::expression)

@given(instance=myDsl::conditional::expression_strategy)
@settings(max_examples=50)
def test_mydsl::conditional::expression_instantiation(instance):
    assert isinstance(instance, myDsl::conditional::expression)

@given(instance=myDsl::expressionR_strategy)
@settings(max_examples=50)
def test_mydsl::expressionr_instantiation(instance):
    assert isinstance(instance, myDsl::expressionR)

@given(instance=primary::expression_strategy)
@settings(max_examples=50)
def test_primary::expression_instantiation(instance):
    assert isinstance(instance, primary::expression)

@given(instance=myDsl::StringC_strategy)
@settings(max_examples=50)
def test_mydsl::stringc_instantiation(instance):
    assert isinstance(instance, myDsl::StringC)

@given(instance=myDsl::StringC_strategy)
def test_mydsl::stringc_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=myDsl::StringC_strategy)
def test_mydsl::stringc_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=expression::statement_strategy)
@settings(max_examples=50)
def test_expression::statement_instantiation(instance):
    assert isinstance(instance, expression::statement)

@given(instance=jump::statement_strategy)
@settings(max_examples=50)
def test_jump::statement_instantiation(instance):
    assert isinstance(instance, jump::statement)

@given(instance=myDsl::IDENTIFIER_strategy)
@settings(max_examples=50)
def test_mydsl::identifier_instantiation(instance):
    assert isinstance(instance, myDsl::IDENTIFIER)

@given(instance=myDsl::IDENTIFIER_strategy)
def test_mydsl::identifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::IDENTIFIER_strategy)
def test_mydsl::identifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::inclusive::or::expression_strategy)
@settings(max_examples=50)
def test_mydsl::inclusive::or::expression_instantiation(instance):
    assert isinstance(instance, myDsl::inclusive::or::expression)

@given(instance=myDsl::logical::or::expressionR_strategy)
@settings(max_examples=50)
def test_mydsl::logical::or::expressionr_instantiation(instance):
    assert isinstance(instance, myDsl::logical::or::expressionR)

@given(instance=myDsl::logical::and::expression_strategy)
@settings(max_examples=50)
def test_mydsl::logical::and::expression_instantiation(instance):
    assert isinstance(instance, myDsl::logical::and::expression)

@given(instance=conditional::expression_strategy)
@settings(max_examples=50)
def test_conditional::expression_instantiation(instance):
    assert isinstance(instance, conditional::expression)

@given(instance=myDsl::logical::or::expression_strategy)
@settings(max_examples=50)
def test_mydsl::logical::or::expression_instantiation(instance):
    assert isinstance(instance, myDsl::logical::or::expression)

@given(instance=myDsl::initializer_strategy)
@settings(max_examples=50)
def test_mydsl::initializer_instantiation(instance):
    assert isinstance(instance, myDsl::initializer)

@given(instance=myDsl::init::declarator::listR_strategy)
@settings(max_examples=50)
def test_mydsl::init::declarator::listr_instantiation(instance):
    assert isinstance(instance, myDsl::init::declarator::listR)

@given(instance=myDsl::init::declarator_strategy)
@settings(max_examples=50)
def test_mydsl::init::declarator_instantiation(instance):
    assert isinstance(instance, myDsl::init::declarator)

@given(instance=myDsl::init::declarator::list_strategy)
@settings(max_examples=50)
def test_mydsl::init::declarator::list_instantiation(instance):
    assert isinstance(instance, myDsl::init::declarator::list)

@given(instance=parameter::declaration_strategy)
@settings(max_examples=50)
def test_parameter::declaration_instantiation(instance):
    assert isinstance(instance, parameter::declaration)

@given(instance=block::item_strategy)
@settings(max_examples=50)
def test_block::item_instantiation(instance):
    assert isinstance(instance, block::item)

@given(instance=myDsl::statement_strategy)
@settings(max_examples=50)
def test_mydsl::statement_instantiation(instance):
    assert isinstance(instance, myDsl::statement)

@given(instance=myDsl::block::item::listR_strategy)
@settings(max_examples=50)
def test_mydsl::block::item::listr_instantiation(instance):
    assert isinstance(instance, myDsl::block::item::listR)

@given(instance=myDsl::block::item_strategy)
@settings(max_examples=50)
def test_mydsl::block::item_instantiation(instance):
    assert isinstance(instance, myDsl::block::item)

@given(instance=compound::statement_strategy)
@settings(max_examples=50)
def test_compound::statement_instantiation(instance):
    assert isinstance(instance, compound::statement)

@given(instance=myDsl::block::item::list_strategy)
@settings(max_examples=50)
def test_mydsl::block::item::list_instantiation(instance):
    assert isinstance(instance, myDsl::block::item::list)

@given(instance=statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, statement)

@given(instance=myDsl::selection::statement_strategy)
@settings(max_examples=50)
def test_mydsl::selection::statement_instantiation(instance):
    assert isinstance(instance, myDsl::selection::statement)

@given(instance=myDsl::jump::statement_strategy)
@settings(max_examples=50)
def test_mydsl::jump::statement_instantiation(instance):
    assert isinstance(instance, myDsl::jump::statement)

@given(instance=myDsl::expression::statement_strategy)
@settings(max_examples=50)
def test_mydsl::expression::statement_instantiation(instance):
    assert isinstance(instance, myDsl::expression::statement)

@given(instance=myDsl::expression_strategy)
@settings(max_examples=50)
def test_mydsl::expression_instantiation(instance):
    assert isinstance(instance, myDsl::expression)

@given(instance=myDsl::iteration::statement_strategy)
@settings(max_examples=50)
def test_mydsl::iteration::statement_instantiation(instance):
    assert isinstance(instance, myDsl::iteration::statement)

@given(instance=myDsl::labeled::statement_strategy)
@settings(max_examples=50)
def test_mydsl::labeled::statement_instantiation(instance):
    assert isinstance(instance, myDsl::labeled::statement)

@given(instance=myDsl::parameter::listR_strategy)
@settings(max_examples=50)
def test_mydsl::parameter::listr_instantiation(instance):
    assert isinstance(instance, myDsl::parameter::listR)

@given(instance=myDsl::parameter::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::parameter::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::parameter::declaration)

@given(instance=parameter::type::list_strategy)
@settings(max_examples=50)
def test_parameter::type::list_instantiation(instance):
    assert isinstance(instance, parameter::type::list)

@given(instance=myDsl::parameter::list_strategy)
@settings(max_examples=50)
def test_mydsl::parameter::list_instantiation(instance):
    assert isinstance(instance, myDsl::parameter::list)

@given(instance=myDsl::identifier::listR_strategy)
@settings(max_examples=50)
def test_mydsl::identifier::listr_instantiation(instance):
    assert isinstance(instance, myDsl::identifier::listR)

@given(instance=myDsl::declaration::listR_strategy)
@settings(max_examples=50)
def test_mydsl::declaration::listr_instantiation(instance):
    assert isinstance(instance, myDsl::declaration::listR)

@given(instance=myDsl::abstract::declarator_strategy)
@settings(max_examples=50)
def test_mydsl::abstract::declarator_instantiation(instance):
    assert isinstance(instance, myDsl::abstract::declarator)

@given(instance=myDsl::type::qualifier::listR_strategy)
@settings(max_examples=50)
def test_mydsl::type::qualifier::listr_instantiation(instance):
    assert isinstance(instance, myDsl::type::qualifier::listR)

@given(instance=myDsl::type::qualifier::listR_strategy)
def test_mydsl::type::qualifier::listr_Type_qualifier_type(instance):
    assert isinstance(instance.Type_qualifier, str)


@given(instance=myDsl::type::qualifier::listR_strategy)
def test_mydsl::type::qualifier::listr_Type_qualifier_setter(instance):
    original = instance.Type_qualifier
    instance.Type_qualifier = original
    assert instance.Type_qualifier == original

@given(instance=pointer_strategy)
@settings(max_examples=50)
def test_pointer_instantiation(instance):
    assert isinstance(instance, pointer)

@given(instance=myDsl::type::qualifier::list_strategy)
@settings(max_examples=50)
def test_mydsl::type::qualifier::list_instantiation(instance):
    assert isinstance(instance, myDsl::type::qualifier::list)

@given(instance=myDsl::type::qualifier::list_strategy)
def test_mydsl::type::qualifier::list_Type_qualifier_type(instance):
    assert isinstance(instance.Type_qualifier, str)


@given(instance=myDsl::type::qualifier::list_strategy)
def test_mydsl::type::qualifier::list_Type_qualifier_setter(instance):
    original = instance.Type_qualifier
    instance.Type_qualifier = original
    assert instance.Type_qualifier == original

@given(instance=myDsl::pointer_strategy)
@settings(max_examples=50)
def test_mydsl::pointer_instantiation(instance):
    assert isinstance(instance, myDsl::pointer)

@given(instance=struct::declarator_strategy)
@settings(max_examples=50)
def test_struct::declarator_instantiation(instance):
    assert isinstance(instance, struct::declarator)

@given(instance=myDsl::constant::expression_strategy)
@settings(max_examples=50)
def test_mydsl::constant::expression_instantiation(instance):
    assert isinstance(instance, myDsl::constant::expression)

@given(instance=init::declarator_strategy)
@settings(max_examples=50)
def test_init::declarator_instantiation(instance):
    assert isinstance(instance, init::declarator)

@given(instance=myDsl::compound::statement_strategy)
@settings(max_examples=50)
def test_mydsl::compound::statement_instantiation(instance):
    assert isinstance(instance, myDsl::compound::statement)

@given(instance=myDsl::identifier::list_strategy)
@settings(max_examples=50)
def test_mydsl::identifier::list_instantiation(instance):
    assert isinstance(instance, myDsl::identifier::list)

@given(instance=myDsl::parameter::type::list_strategy)
@settings(max_examples=50)
def test_mydsl::parameter::type::list_instantiation(instance):
    assert isinstance(instance, myDsl::parameter::type::list)

@given(instance=myDsl::assignment::expression_strategy)
@settings(max_examples=50)
def test_mydsl::assignment::expression_instantiation(instance):
    assert isinstance(instance, myDsl::assignment::expression)

@given(instance=myDsl::assignment::expression_strategy)
def test_mydsl::assignment::expression_Assignment_operator_type(instance):
    assert isinstance(instance.Assignment_operator, str)


@given(instance=myDsl::assignment::expression_strategy)
def test_mydsl::assignment::expression_Assignment_operator_setter(instance):
    original = instance.Assignment_operator
    instance.Assignment_operator = original
    assert instance.Assignment_operator == original

@given(instance=myDsl::direct::declaratorR_strategy)
@settings(max_examples=50)
def test_mydsl::direct::declaratorr_instantiation(instance):
    assert isinstance(instance, myDsl::direct::declaratorR)

@given(instance=declarator_strategy)
@settings(max_examples=50)
def test_declarator_instantiation(instance):
    assert isinstance(instance, declarator)

@given(instance=myDsl::direct::declarator_strategy)
@settings(max_examples=50)
def test_mydsl::direct::declarator_instantiation(instance):
    assert isinstance(instance, myDsl::direct::declarator)

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

@given(instance=myDsl::declaration::list_strategy)
@settings(max_examples=50)
def test_mydsl::declaration::list_instantiation(instance):
    assert isinstance(instance, myDsl::declaration::list)

@given(instance=myDsl::declarator_strategy)
@settings(max_examples=50)
def test_mydsl::declarator_instantiation(instance):
    assert isinstance(instance, myDsl::declarator)

@given(instance=external::declaration_strategy)
@settings(max_examples=50)
def test_external::declaration_instantiation(instance):
    assert isinstance(instance, external::declaration)

@given(instance=myDsl::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::declaration)

@given(instance=myDsl::function::definition_strategy)
@settings(max_examples=50)
def test_mydsl::function::definition_instantiation(instance):
    assert isinstance(instance, myDsl::function::definition)

@given(instance=myDsl::declaration::specifiers_strategy)
@settings(max_examples=50)
def test_mydsl::declaration::specifiers_instantiation(instance):
    assert isinstance(instance, myDsl::declaration::specifiers)

@given(instance=myDsl::declaration::specifiers_strategy)
def test_mydsl::declaration::specifiers_Type_qualifier_type(instance):
    assert isinstance(instance.Type_qualifier, str)


@given(instance=myDsl::declaration::specifiers_strategy)
def test_mydsl::declaration::specifiers_Type_qualifier_setter(instance):
    original = instance.Type_qualifier
    instance.Type_qualifier = original
    assert instance.Type_qualifier == original

@given(instance=myDsl::declaration::specifiers_strategy)
def test_mydsl::declaration::specifiers_Storage_class_specifier_type(instance):
    assert isinstance(instance.Storage_class_specifier, str)


@given(instance=myDsl::declaration::specifiers_strategy)
def test_mydsl::declaration::specifiers_Storage_class_specifier_setter(instance):
    original = instance.Storage_class_specifier
    instance.Storage_class_specifier = original
    assert instance.Storage_class_specifier == original

@given(instance=myDsl::translation::unitR_strategy)
@settings(max_examples=50)
def test_mydsl::translation::unitr_instantiation(instance):
    assert isinstance(instance, myDsl::translation::unitR)

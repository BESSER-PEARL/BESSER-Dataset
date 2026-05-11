import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    type::specifier,
    myDsl::complexType,
    myDsl::voidType,
    myDsl::unsignedType,
    myDsl::doubleType,
    myDsl::longType,
    myDsl::shortType,
    myDsl::signedType,
    myDsl::charType,
    myDsl::imaginaryType,
    myDsl::declaration::list2,
    myDsl::external::declaration,
    myDsl::EObject,
    myDsl::declaration::list,
    myDsl::function::definition,
    myDsl::jump::statement,
    myDsl::iteration::statement,
    myDsl::selection::statement,
    myDsl::expression::statement,
    myDsl::compound::statement,
    myDsl::labeled::statement,
    myDsl::statement,
    myDsl::block::item,
    myDsl::initializer::list2,
    myDsl::designation,
    myDsl::initializer,
    myDsl::direct::abstract::declarator2,
    myDsl::direct::abstract::declarator,
    myDsl::designator::list2,
    myDsl::designator,
    myDsl::designator::list,
    myDsl::parameter::list2,
    myDsl::parameter::declaration,
    myDsl::parameter::list,
    myDsl::type::qualifier::list2,
    myDsl::identifier::list2,
    myDsl::abstract::declarator,
    myDsl::direct::declarator,
    myDsl::pointer,
    myDsl::identifier::list,
    myDsl::parameter::type::list,
    myDsl::type::qualifier::list,
    myDsl::direct::declarator2,
    myDsl::struct::declarator::list2,
    myDsl::struct::declarator,
    myDsl::struct::declarator::list,
    myDsl::specifier::qualifier::list,
    myDsl::enumerator::list2,
    myDsl::enumerator,
    myDsl::enumerator::list,
    myDsl::atomic::type::specifier,
    myDsl::declarator,
    myDsl::init::declarator::list2,
    myDsl::init::declarator,
    myDsl::alignment::specifier,
    myDsl::struct::declaration::list2,
    myDsl::struct::declaration,
    struct::or::union::specifier,
    myDsl::struct::declaration::list,
    myDsl::struct::or::union,
    myDsl::enum::specifier,
    myDsl::struct::or::union::specifier,
    myDsl::declaration::specifiers,
    myDsl::declaration,
    myDsl::constant::expression,
    myDsl::expression2,
    myDsl::assignment::operator,
    myDsl::function::specifier,
    myDsl::type::qualifier,
    myDsl::type::specifier,
    myDsl::storage::class::specifier,
    myDsl::static::assert::declaration,
    myDsl::init::declarator::list,
    simple::expression,
    myDsl::floatType,
    myDsl::INC::OR,
    myDsl::intType,
    myDsl::variableRef,
    myDsl::LOG::AND,
    myDsl::EQL,
    myDsl::stringType,
    myDsl::EXC::OR,
    myDsl::ADD,
    myDsl::booleanType,
    myDsl::MINUS,
    myDsl::LOG::OR,
    myDsl::MUL,
    myDsl::AND,
    myDsl::SHF,
    myDsl::REL,
    myDsl::unary::expression,
    postfix::expression2,
    myDsl::argument::expression::list,
    myDsl::initializer::list,
    myDsl::postfix::expression2,
    myDsl::postfix::expression,
    myDsl::generic::association,
    myDsl::generic::assoc::list,
    myDsl::assignment::expression,
    myDsl::expression,
    myDsl::conditional::expression,
    myDsl::constant,
    myDsl::type::name,
    myDsl::simple::expression,
    myDsl::translation::unit,
    myDsl::Model,
    myDsl::generic::selection,
    myDsl::string::nova,
    myDsl::enumeration::constant,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_type::specifier_is_not_abstract():
    assert not inspect.isabstract(type::specifier)


def test_type::specifier_constructor_exists():
    assert callable(type::specifier.__init__)


def test_type::specifier_constructor_args():
    sig = inspect.signature(type::specifier.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::complextype_is_not_abstract():
    assert not inspect.isabstract(myDsl::complexType)


def test_mydsl::complextype_constructor_exists():
    assert callable(myDsl::complexType.__init__)


def test_mydsl::complextype_constructor_args():
    sig = inspect.signature(myDsl::complexType.__init__)
    params = list(sig.parameters.keys())
    assert "complex_type" in params, "Missing parameter 'complex_type'"

def test_mydsl::complextype_has_complex_type():
    assert hasattr(myDsl::complexType, "complex_type")
    descriptor = None
    for klass in myDsl::complexType.__mro__:
        if "complex_type" in klass.__dict__:
            descriptor = klass.__dict__["complex_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::voidtype_is_not_abstract():
    assert not inspect.isabstract(myDsl::voidType)


def test_mydsl::voidtype_constructor_exists():
    assert callable(myDsl::voidType.__init__)


def test_mydsl::voidtype_constructor_args():
    sig = inspect.signature(myDsl::voidType.__init__)
    params = list(sig.parameters.keys())
    assert "void_type" in params, "Missing parameter 'void_type'"

def test_mydsl::voidtype_has_void_type():
    assert hasattr(myDsl::voidType, "void_type")
    descriptor = None
    for klass in myDsl::voidType.__mro__:
        if "void_type" in klass.__dict__:
            descriptor = klass.__dict__["void_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::unsignedtype_is_not_abstract():
    assert not inspect.isabstract(myDsl::unsignedType)


def test_mydsl::unsignedtype_constructor_exists():
    assert callable(myDsl::unsignedType.__init__)


def test_mydsl::unsignedtype_constructor_args():
    sig = inspect.signature(myDsl::unsignedType.__init__)
    params = list(sig.parameters.keys())
    assert "unsigned_type" in params, "Missing parameter 'unsigned_type'"

def test_mydsl::unsignedtype_has_unsigned_type():
    assert hasattr(myDsl::unsignedType, "unsigned_type")
    descriptor = None
    for klass in myDsl::unsignedType.__mro__:
        if "unsigned_type" in klass.__dict__:
            descriptor = klass.__dict__["unsigned_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::doubletype_is_not_abstract():
    assert not inspect.isabstract(myDsl::doubleType)


def test_mydsl::doubletype_constructor_exists():
    assert callable(myDsl::doubleType.__init__)


def test_mydsl::doubletype_constructor_args():
    sig = inspect.signature(myDsl::doubleType.__init__)
    params = list(sig.parameters.keys())
    assert "double_type" in params, "Missing parameter 'double_type'"

def test_mydsl::doubletype_has_double_type():
    assert hasattr(myDsl::doubleType, "double_type")
    descriptor = None
    for klass in myDsl::doubleType.__mro__:
        if "double_type" in klass.__dict__:
            descriptor = klass.__dict__["double_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::longtype_is_not_abstract():
    assert not inspect.isabstract(myDsl::longType)


def test_mydsl::longtype_constructor_exists():
    assert callable(myDsl::longType.__init__)


def test_mydsl::longtype_constructor_args():
    sig = inspect.signature(myDsl::longType.__init__)
    params = list(sig.parameters.keys())
    assert "long_type" in params, "Missing parameter 'long_type'"

def test_mydsl::longtype_has_long_type():
    assert hasattr(myDsl::longType, "long_type")
    descriptor = None
    for klass in myDsl::longType.__mro__:
        if "long_type" in klass.__dict__:
            descriptor = klass.__dict__["long_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::shorttype_is_not_abstract():
    assert not inspect.isabstract(myDsl::shortType)


def test_mydsl::shorttype_constructor_exists():
    assert callable(myDsl::shortType.__init__)


def test_mydsl::shorttype_constructor_args():
    sig = inspect.signature(myDsl::shortType.__init__)
    params = list(sig.parameters.keys())
    assert "short_type" in params, "Missing parameter 'short_type'"

def test_mydsl::shorttype_has_short_type():
    assert hasattr(myDsl::shortType, "short_type")
    descriptor = None
    for klass in myDsl::shortType.__mro__:
        if "short_type" in klass.__dict__:
            descriptor = klass.__dict__["short_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::signedtype_is_not_abstract():
    assert not inspect.isabstract(myDsl::signedType)


def test_mydsl::signedtype_constructor_exists():
    assert callable(myDsl::signedType.__init__)


def test_mydsl::signedtype_constructor_args():
    sig = inspect.signature(myDsl::signedType.__init__)
    params = list(sig.parameters.keys())
    assert "signed_type" in params, "Missing parameter 'signed_type'"

def test_mydsl::signedtype_has_signed_type():
    assert hasattr(myDsl::signedType, "signed_type")
    descriptor = None
    for klass in myDsl::signedType.__mro__:
        if "signed_type" in klass.__dict__:
            descriptor = klass.__dict__["signed_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::chartype_is_not_abstract():
    assert not inspect.isabstract(myDsl::charType)


def test_mydsl::chartype_constructor_exists():
    assert callable(myDsl::charType.__init__)


def test_mydsl::chartype_constructor_args():
    sig = inspect.signature(myDsl::charType.__init__)
    params = list(sig.parameters.keys())
    assert "char_type" in params, "Missing parameter 'char_type'"

def test_mydsl::chartype_has_char_type():
    assert hasattr(myDsl::charType, "char_type")
    descriptor = None
    for klass in myDsl::charType.__mro__:
        if "char_type" in klass.__dict__:
            descriptor = klass.__dict__["char_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::imaginarytype_is_not_abstract():
    assert not inspect.isabstract(myDsl::imaginaryType)


def test_mydsl::imaginarytype_constructor_exists():
    assert callable(myDsl::imaginaryType.__init__)


def test_mydsl::imaginarytype_constructor_args():
    sig = inspect.signature(myDsl::imaginaryType.__init__)
    params = list(sig.parameters.keys())
    assert "imaginary_type" in params, "Missing parameter 'imaginary_type'"

def test_mydsl::imaginarytype_has_imaginary_type():
    assert hasattr(myDsl::imaginaryType, "imaginary_type")
    descriptor = None
    for klass in myDsl::imaginaryType.__mro__:
        if "imaginary_type" in klass.__dict__:
            descriptor = klass.__dict__["imaginary_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::declaration::list2_is_not_abstract():
    assert not inspect.isabstract(myDsl::declaration::list2)


def test_mydsl::declaration::list2_constructor_exists():
    assert callable(myDsl::declaration::list2.__init__)


def test_mydsl::declaration::list2_constructor_args():
    sig = inspect.signature(myDsl::declaration::list2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::external::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::external::declaration)


def test_mydsl::external::declaration_constructor_exists():
    assert callable(myDsl::external::declaration.__init__)


def test_mydsl::external::declaration_constructor_args():
    sig = inspect.signature(myDsl::external::declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::eobject_is_not_abstract():
    assert not inspect.isabstract(myDsl::EObject)


def test_mydsl::eobject_constructor_exists():
    assert callable(myDsl::EObject.__init__)


def test_mydsl::eobject_constructor_args():
    sig = inspect.signature(myDsl::EObject.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::declaration::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::declaration::list)


def test_mydsl::declaration::list_constructor_exists():
    assert callable(myDsl::declaration::list.__init__)


def test_mydsl::declaration::list_constructor_args():
    sig = inspect.signature(myDsl::declaration::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::function::definition_is_not_abstract():
    assert not inspect.isabstract(myDsl::function::definition)


def test_mydsl::function::definition_constructor_exists():
    assert callable(myDsl::function::definition.__init__)


def test_mydsl::function::definition_constructor_args():
    sig = inspect.signature(myDsl::function::definition.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::jump::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::jump::statement)


def test_mydsl::jump::statement_constructor_exists():
    assert callable(myDsl::jump::statement.__init__)


def test_mydsl::jump::statement_constructor_args():
    sig = inspect.signature(myDsl::jump::statement.__init__)
    params = list(sig.parameters.keys())
    assert "goto" in params, "Missing parameter 'goto'"
    assert "return_" in params, "Missing parameter 'return_'"
    assert "break_" in params, "Missing parameter 'break_'"
    assert "continue_" in params, "Missing parameter 'continue_'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl::jump::statement_has_goto():
    assert hasattr(myDsl::jump::statement, "goto")
    descriptor = None
    for klass in myDsl::jump::statement.__mro__:
        if "goto" in klass.__dict__:
            descriptor = klass.__dict__["goto"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::jump::statement_has_return_():
    assert hasattr(myDsl::jump::statement, "return_")
    descriptor = None
    for klass in myDsl::jump::statement.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
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

def test_mydsl::jump::statement_has_continue_():
    assert hasattr(myDsl::jump::statement, "continue_")
    descriptor = None
    for klass in myDsl::jump::statement.__mro__:
        if "continue_" in klass.__dict__:
            descriptor = klass.__dict__["continue_"]
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



def test_mydsl::iteration::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::iteration::statement)


def test_mydsl::iteration::statement_constructor_exists():
    assert callable(myDsl::iteration::statement.__init__)


def test_mydsl::iteration::statement_constructor_args():
    sig = inspect.signature(myDsl::iteration::statement.__init__)
    params = list(sig.parameters.keys())
    assert "for_" in params, "Missing parameter 'for_'"
    assert "do" in params, "Missing parameter 'do'"
    assert "while_" in params, "Missing parameter 'while_'"

def test_mydsl::iteration::statement_has_for_():
    assert hasattr(myDsl::iteration::statement, "for_")
    descriptor = None
    for klass in myDsl::iteration::statement.__mro__:
        if "for_" in klass.__dict__:
            descriptor = klass.__dict__["for_"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::iteration::statement_has_do():
    assert hasattr(myDsl::iteration::statement, "do")
    descriptor = None
    for klass in myDsl::iteration::statement.__mro__:
        if "do" in klass.__dict__:
            descriptor = klass.__dict__["do"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::iteration::statement_has_while_():
    assert hasattr(myDsl::iteration::statement, "while_")
    descriptor = None
    for klass in myDsl::iteration::statement.__mro__:
        if "while_" in klass.__dict__:
            descriptor = klass.__dict__["while_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::selection::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::selection::statement)


def test_mydsl::selection::statement_constructor_exists():
    assert callable(myDsl::selection::statement.__init__)


def test_mydsl::selection::statement_constructor_args():
    sig = inspect.signature(myDsl::selection::statement.__init__)
    params = list(sig.parameters.keys())
    assert "switch" in params, "Missing parameter 'switch'"
    assert "if_" in params, "Missing parameter 'if_'"
    assert "else_" in params, "Missing parameter 'else_'"

def test_mydsl::selection::statement_has_switch():
    assert hasattr(myDsl::selection::statement, "switch")
    descriptor = None
    for klass in myDsl::selection::statement.__mro__:
        if "switch" in klass.__dict__:
            descriptor = klass.__dict__["switch"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::selection::statement_has_if_():
    assert hasattr(myDsl::selection::statement, "if_")
    descriptor = None
    for klass in myDsl::selection::statement.__mro__:
        if "if_" in klass.__dict__:
            descriptor = klass.__dict__["if_"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::selection::statement_has_else_():
    assert hasattr(myDsl::selection::statement, "else_")
    descriptor = None
    for klass in myDsl::selection::statement.__mro__:
        if "else_" in klass.__dict__:
            descriptor = klass.__dict__["else_"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::expression::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::expression::statement)


def test_mydsl::expression::statement_constructor_exists():
    assert callable(myDsl::expression::statement.__init__)


def test_mydsl::expression::statement_constructor_args():
    sig = inspect.signature(myDsl::expression::statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::compound::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::compound::statement)


def test_mydsl::compound::statement_constructor_exists():
    assert callable(myDsl::compound::statement.__init__)


def test_mydsl::compound::statement_constructor_args():
    sig = inspect.signature(myDsl::compound::statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::labeled::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::labeled::statement)


def test_mydsl::labeled::statement_constructor_exists():
    assert callable(myDsl::labeled::statement.__init__)


def test_mydsl::labeled::statement_constructor_args():
    sig = inspect.signature(myDsl::labeled::statement.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "default" in params, "Missing parameter 'default'"
    assert "case" in params, "Missing parameter 'case'"

def test_mydsl::labeled::statement_has_identifier():
    assert hasattr(myDsl::labeled::statement, "identifier")
    descriptor = None
    for klass in myDsl::labeled::statement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::labeled::statement_has_default():
    assert hasattr(myDsl::labeled::statement, "default")
    descriptor = None
    for klass in myDsl::labeled::statement.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::labeled::statement_has_case():
    assert hasattr(myDsl::labeled::statement, "case")
    descriptor = None
    for klass in myDsl::labeled::statement.__mro__:
        if "case" in klass.__dict__:
            descriptor = klass.__dict__["case"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::statement_is_not_abstract():
    assert not inspect.isabstract(myDsl::statement)


def test_mydsl::statement_constructor_exists():
    assert callable(myDsl::statement.__init__)


def test_mydsl::statement_constructor_args():
    sig = inspect.signature(myDsl::statement.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::block::item_is_not_abstract():
    assert not inspect.isabstract(myDsl::block::item)


def test_mydsl::block::item_constructor_exists():
    assert callable(myDsl::block::item.__init__)


def test_mydsl::block::item_constructor_args():
    sig = inspect.signature(myDsl::block::item.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::initializer::list2_is_not_abstract():
    assert not inspect.isabstract(myDsl::initializer::list2)


def test_mydsl::initializer::list2_constructor_exists():
    assert callable(myDsl::initializer::list2.__init__)


def test_mydsl::initializer::list2_constructor_args():
    sig = inspect.signature(myDsl::initializer::list2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::designation_is_not_abstract():
    assert not inspect.isabstract(myDsl::designation)


def test_mydsl::designation_constructor_exists():
    assert callable(myDsl::designation.__init__)


def test_mydsl::designation_constructor_args():
    sig = inspect.signature(myDsl::designation.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::initializer_is_not_abstract():
    assert not inspect.isabstract(myDsl::initializer)


def test_mydsl::initializer_constructor_exists():
    assert callable(myDsl::initializer.__init__)


def test_mydsl::initializer_constructor_args():
    sig = inspect.signature(myDsl::initializer.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::direct::abstract::declarator2_is_not_abstract():
    assert not inspect.isabstract(myDsl::direct::abstract::declarator2)


def test_mydsl::direct::abstract::declarator2_constructor_exists():
    assert callable(myDsl::direct::abstract::declarator2.__init__)


def test_mydsl::direct::abstract::declarator2_constructor_args():
    sig = inspect.signature(myDsl::direct::abstract::declarator2.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_mydsl::direct::abstract::declarator2_has_static():
    assert hasattr(myDsl::direct::abstract::declarator2, "static")
    descriptor = None
    for klass in myDsl::direct::abstract::declarator2.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::direct::abstract::declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl::direct::abstract::declarator)


def test_mydsl::direct::abstract::declarator_constructor_exists():
    assert callable(myDsl::direct::abstract::declarator.__init__)


def test_mydsl::direct::abstract::declarator_constructor_args():
    sig = inspect.signature(myDsl::direct::abstract::declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::designator::list2_is_not_abstract():
    assert not inspect.isabstract(myDsl::designator::list2)


def test_mydsl::designator::list2_constructor_exists():
    assert callable(myDsl::designator::list2.__init__)


def test_mydsl::designator::list2_constructor_args():
    sig = inspect.signature(myDsl::designator::list2.__init__)
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



def test_mydsl::parameter::list2_is_not_abstract():
    assert not inspect.isabstract(myDsl::parameter::list2)


def test_mydsl::parameter::list2_constructor_exists():
    assert callable(myDsl::parameter::list2.__init__)


def test_mydsl::parameter::list2_constructor_args():
    sig = inspect.signature(myDsl::parameter::list2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::parameter::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::parameter::declaration)


def test_mydsl::parameter::declaration_constructor_exists():
    assert callable(myDsl::parameter::declaration.__init__)


def test_mydsl::parameter::declaration_constructor_args():
    sig = inspect.signature(myDsl::parameter::declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::parameter::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::parameter::list)


def test_mydsl::parameter::list_constructor_exists():
    assert callable(myDsl::parameter::list.__init__)


def test_mydsl::parameter::list_constructor_args():
    sig = inspect.signature(myDsl::parameter::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::type::qualifier::list2_is_not_abstract():
    assert not inspect.isabstract(myDsl::type::qualifier::list2)


def test_mydsl::type::qualifier::list2_constructor_exists():
    assert callable(myDsl::type::qualifier::list2.__init__)


def test_mydsl::type::qualifier::list2_constructor_args():
    sig = inspect.signature(myDsl::type::qualifier::list2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::identifier::list2_is_not_abstract():
    assert not inspect.isabstract(myDsl::identifier::list2)


def test_mydsl::identifier::list2_constructor_exists():
    assert callable(myDsl::identifier::list2.__init__)


def test_mydsl::identifier::list2_constructor_args():
    sig = inspect.signature(myDsl::identifier::list2.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_mydsl::identifier::list2_has_identifier():
    assert hasattr(myDsl::identifier::list2, "identifier")
    descriptor = None
    for klass in myDsl::identifier::list2.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::abstract::declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl::abstract::declarator)


def test_mydsl::abstract::declarator_constructor_exists():
    assert callable(myDsl::abstract::declarator.__init__)


def test_mydsl::abstract::declarator_constructor_args():
    sig = inspect.signature(myDsl::abstract::declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::direct::declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl::direct::declarator)


def test_mydsl::direct::declarator_constructor_exists():
    assert callable(myDsl::direct::declarator.__init__)


def test_mydsl::direct::declarator_constructor_args():
    sig = inspect.signature(myDsl::direct::declarator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::direct::declarator_has_name():
    assert hasattr(myDsl::direct::declarator, "name")
    descriptor = None
    for klass in myDsl::direct::declarator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::pointer_is_not_abstract():
    assert not inspect.isabstract(myDsl::pointer)


def test_mydsl::pointer_constructor_exists():
    assert callable(myDsl::pointer.__init__)


def test_mydsl::pointer_constructor_args():
    sig = inspect.signature(myDsl::pointer.__init__)
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
    assert "ellipsis" in params, "Missing parameter 'ellipsis'"

def test_mydsl::parameter::type::list_has_ellipsis():
    assert hasattr(myDsl::parameter::type::list, "ellipsis")
    descriptor = None
    for klass in myDsl::parameter::type::list.__mro__:
        if "ellipsis" in klass.__dict__:
            descriptor = klass.__dict__["ellipsis"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::type::qualifier::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::type::qualifier::list)


def test_mydsl::type::qualifier::list_constructor_exists():
    assert callable(myDsl::type::qualifier::list.__init__)


def test_mydsl::type::qualifier::list_constructor_args():
    sig = inspect.signature(myDsl::type::qualifier::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::direct::declarator2_is_not_abstract():
    assert not inspect.isabstract(myDsl::direct::declarator2)


def test_mydsl::direct::declarator2_constructor_exists():
    assert callable(myDsl::direct::declarator2.__init__)


def test_mydsl::direct::declarator2_constructor_args():
    sig = inspect.signature(myDsl::direct::declarator2.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_mydsl::direct::declarator2_has_static():
    assert hasattr(myDsl::direct::declarator2, "static")
    descriptor = None
    for klass in myDsl::direct::declarator2.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::struct::declarator::list2_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::declarator::list2)


def test_mydsl::struct::declarator::list2_constructor_exists():
    assert callable(myDsl::struct::declarator::list2.__init__)


def test_mydsl::struct::declarator::list2_constructor_args():
    sig = inspect.signature(myDsl::struct::declarator::list2.__init__)
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



def test_mydsl::specifier::qualifier::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::specifier::qualifier::list)


def test_mydsl::specifier::qualifier::list_constructor_exists():
    assert callable(myDsl::specifier::qualifier::list.__init__)


def test_mydsl::specifier::qualifier::list_constructor_args():
    sig = inspect.signature(myDsl::specifier::qualifier::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::enumerator::list2_is_not_abstract():
    assert not inspect.isabstract(myDsl::enumerator::list2)


def test_mydsl::enumerator::list2_constructor_exists():
    assert callable(myDsl::enumerator::list2.__init__)


def test_mydsl::enumerator::list2_constructor_args():
    sig = inspect.signature(myDsl::enumerator::list2.__init__)
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



def test_mydsl::atomic::type::specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl::atomic::type::specifier)


def test_mydsl::atomic::type::specifier_constructor_exists():
    assert callable(myDsl::atomic::type::specifier.__init__)


def test_mydsl::atomic::type::specifier_constructor_args():
    sig = inspect.signature(myDsl::atomic::type::specifier.__init__)
    params = list(sig.parameters.keys())
    assert "atomic" in params, "Missing parameter 'atomic'"

def test_mydsl::atomic::type::specifier_has_atomic():
    assert hasattr(myDsl::atomic::type::specifier, "atomic")
    descriptor = None
    for klass in myDsl::atomic::type::specifier.__mro__:
        if "atomic" in klass.__dict__:
            descriptor = klass.__dict__["atomic"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl::declarator)


def test_mydsl::declarator_constructor_exists():
    assert callable(myDsl::declarator.__init__)


def test_mydsl::declarator_constructor_args():
    sig = inspect.signature(myDsl::declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::init::declarator::list2_is_not_abstract():
    assert not inspect.isabstract(myDsl::init::declarator::list2)


def test_mydsl::init::declarator::list2_constructor_exists():
    assert callable(myDsl::init::declarator::list2.__init__)


def test_mydsl::init::declarator::list2_constructor_args():
    sig = inspect.signature(myDsl::init::declarator::list2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::init::declarator_is_not_abstract():
    assert not inspect.isabstract(myDsl::init::declarator)


def test_mydsl::init::declarator_constructor_exists():
    assert callable(myDsl::init::declarator.__init__)


def test_mydsl::init::declarator_constructor_args():
    sig = inspect.signature(myDsl::init::declarator.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::alignment::specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl::alignment::specifier)


def test_mydsl::alignment::specifier_constructor_exists():
    assert callable(myDsl::alignment::specifier.__init__)


def test_mydsl::alignment::specifier_constructor_args():
    sig = inspect.signature(myDsl::alignment::specifier.__init__)
    params = list(sig.parameters.keys())
    assert "alignas" in params, "Missing parameter 'alignas'"

def test_mydsl::alignment::specifier_has_alignas():
    assert hasattr(myDsl::alignment::specifier, "alignas")
    descriptor = None
    for klass in myDsl::alignment::specifier.__mro__:
        if "alignas" in klass.__dict__:
            descriptor = klass.__dict__["alignas"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::struct::declaration::list2_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::declaration::list2)


def test_mydsl::struct::declaration::list2_constructor_exists():
    assert callable(myDsl::struct::declaration::list2.__init__)


def test_mydsl::struct::declaration::list2_constructor_args():
    sig = inspect.signature(myDsl::struct::declaration::list2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::struct::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::declaration)


def test_mydsl::struct::declaration_constructor_exists():
    assert callable(myDsl::struct::declaration.__init__)


def test_mydsl::struct::declaration_constructor_args():
    sig = inspect.signature(myDsl::struct::declaration.__init__)
    params = list(sig.parameters.keys())



def test_struct::or::union::specifier_is_not_abstract():
    assert not inspect.isabstract(struct::or::union::specifier)


def test_struct::or::union::specifier_constructor_exists():
    assert callable(struct::or::union::specifier.__init__)


def test_struct::or::union::specifier_constructor_args():
    sig = inspect.signature(struct::or::union::specifier.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::struct::declaration::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::declaration::list)


def test_mydsl::struct::declaration::list_constructor_exists():
    assert callable(myDsl::struct::declaration::list.__init__)


def test_mydsl::struct::declaration::list_constructor_args():
    sig = inspect.signature(myDsl::struct::declaration::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::struct::or::union_is_not_abstract():
    assert not inspect.isabstract(myDsl::struct::or::union)


def test_mydsl::struct::or::union_constructor_exists():
    assert callable(myDsl::struct::or::union.__init__)


def test_mydsl::struct::or::union_constructor_args():
    sig = inspect.signature(myDsl::struct::or::union.__init__)
    params = list(sig.parameters.keys())
    assert "union" in params, "Missing parameter 'union'"
    assert "struct" in params, "Missing parameter 'struct'"

def test_mydsl::struct::or::union_has_union():
    assert hasattr(myDsl::struct::or::union, "union")
    descriptor = None
    for klass in myDsl::struct::or::union.__mro__:
        if "union" in klass.__dict__:
            descriptor = klass.__dict__["union"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::struct::or::union_has_struct():
    assert hasattr(myDsl::struct::or::union, "struct")
    descriptor = None
    for klass in myDsl::struct::or::union.__mro__:
        if "struct" in klass.__dict__:
            descriptor = klass.__dict__["struct"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::enum::specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl::enum::specifier)


def test_mydsl::enum::specifier_constructor_exists():
    assert callable(myDsl::enum::specifier.__init__)


def test_mydsl::enum::specifier_constructor_args():
    sig = inspect.signature(myDsl::enum::specifier.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "enumt" in params, "Missing parameter 'enumt'"

def test_mydsl::enum::specifier_has_identifier():
    assert hasattr(myDsl::enum::specifier, "identifier")
    descriptor = None
    for klass in myDsl::enum::specifier.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::enum::specifier_has_enumt():
    assert hasattr(myDsl::enum::specifier, "enumt")
    descriptor = None
    for klass in myDsl::enum::specifier.__mro__:
        if "enumt" in klass.__dict__:
            descriptor = klass.__dict__["enumt"]
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

def test_mydsl::struct::or::union::specifier_has_identifier():
    assert hasattr(myDsl::struct::or::union::specifier, "identifier")
    descriptor = None
    for klass in myDsl::struct::or::union::specifier.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::declaration::specifiers_is_not_abstract():
    assert not inspect.isabstract(myDsl::declaration::specifiers)


def test_mydsl::declaration::specifiers_constructor_exists():
    assert callable(myDsl::declaration::specifiers.__init__)


def test_mydsl::declaration::specifiers_constructor_args():
    sig = inspect.signature(myDsl::declaration::specifiers.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::declaration)


def test_mydsl::declaration_constructor_exists():
    assert callable(myDsl::declaration.__init__)


def test_mydsl::declaration_constructor_args():
    sig = inspect.signature(myDsl::declaration.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::constant::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::constant::expression)


def test_mydsl::constant::expression_constructor_exists():
    assert callable(myDsl::constant::expression.__init__)


def test_mydsl::constant::expression_constructor_args():
    sig = inspect.signature(myDsl::constant::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::expression2_is_not_abstract():
    assert not inspect.isabstract(myDsl::expression2)


def test_mydsl::expression2_constructor_exists():
    assert callable(myDsl::expression2.__init__)


def test_mydsl::expression2_constructor_args():
    sig = inspect.signature(myDsl::expression2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::assignment::operator_is_not_abstract():
    assert not inspect.isabstract(myDsl::assignment::operator)


def test_mydsl::assignment::operator_constructor_exists():
    assert callable(myDsl::assignment::operator.__init__)


def test_mydsl::assignment::operator_constructor_args():
    sig = inspect.signature(myDsl::assignment::operator.__init__)
    params = list(sig.parameters.keys())
    assert "left_assign" in params, "Missing parameter 'left_assign'"
    assert "or_assign" in params, "Missing parameter 'or_assign'"
    assert "xor_assign" in params, "Missing parameter 'xor_assign'"
    assert "and_assign" in params, "Missing parameter 'and_assign'"
    assert "div_assign" in params, "Missing parameter 'div_assign'"
    assert "right_assign" in params, "Missing parameter 'right_assign'"
    assert "sub_assign" in params, "Missing parameter 'sub_assign'"
    assert "add_assign" in params, "Missing parameter 'add_assign'"
    assert "mul_assign" in params, "Missing parameter 'mul_assign'"
    assert "mod_assign" in params, "Missing parameter 'mod_assign'"

def test_mydsl::assignment::operator_has_left_assign():
    assert hasattr(myDsl::assignment::operator, "left_assign")
    descriptor = None
    for klass in myDsl::assignment::operator.__mro__:
        if "left_assign" in klass.__dict__:
            descriptor = klass.__dict__["left_assign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::assignment::operator_has_or_assign():
    assert hasattr(myDsl::assignment::operator, "or_assign")
    descriptor = None
    for klass in myDsl::assignment::operator.__mro__:
        if "or_assign" in klass.__dict__:
            descriptor = klass.__dict__["or_assign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::assignment::operator_has_xor_assign():
    assert hasattr(myDsl::assignment::operator, "xor_assign")
    descriptor = None
    for klass in myDsl::assignment::operator.__mro__:
        if "xor_assign" in klass.__dict__:
            descriptor = klass.__dict__["xor_assign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::assignment::operator_has_and_assign():
    assert hasattr(myDsl::assignment::operator, "and_assign")
    descriptor = None
    for klass in myDsl::assignment::operator.__mro__:
        if "and_assign" in klass.__dict__:
            descriptor = klass.__dict__["and_assign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::assignment::operator_has_div_assign():
    assert hasattr(myDsl::assignment::operator, "div_assign")
    descriptor = None
    for klass in myDsl::assignment::operator.__mro__:
        if "div_assign" in klass.__dict__:
            descriptor = klass.__dict__["div_assign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::assignment::operator_has_right_assign():
    assert hasattr(myDsl::assignment::operator, "right_assign")
    descriptor = None
    for klass in myDsl::assignment::operator.__mro__:
        if "right_assign" in klass.__dict__:
            descriptor = klass.__dict__["right_assign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::assignment::operator_has_sub_assign():
    assert hasattr(myDsl::assignment::operator, "sub_assign")
    descriptor = None
    for klass in myDsl::assignment::operator.__mro__:
        if "sub_assign" in klass.__dict__:
            descriptor = klass.__dict__["sub_assign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::assignment::operator_has_add_assign():
    assert hasattr(myDsl::assignment::operator, "add_assign")
    descriptor = None
    for klass in myDsl::assignment::operator.__mro__:
        if "add_assign" in klass.__dict__:
            descriptor = klass.__dict__["add_assign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::assignment::operator_has_mul_assign():
    assert hasattr(myDsl::assignment::operator, "mul_assign")
    descriptor = None
    for klass in myDsl::assignment::operator.__mro__:
        if "mul_assign" in klass.__dict__:
            descriptor = klass.__dict__["mul_assign"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::assignment::operator_has_mod_assign():
    assert hasattr(myDsl::assignment::operator, "mod_assign")
    descriptor = None
    for klass in myDsl::assignment::operator.__mro__:
        if "mod_assign" in klass.__dict__:
            descriptor = klass.__dict__["mod_assign"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::function::specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl::function::specifier)


def test_mydsl::function::specifier_constructor_exists():
    assert callable(myDsl::function::specifier.__init__)


def test_mydsl::function::specifier_constructor_args():
    sig = inspect.signature(myDsl::function::specifier.__init__)
    params = list(sig.parameters.keys())
    assert "inline" in params, "Missing parameter 'inline'"
    assert "noreturn" in params, "Missing parameter 'noreturn'"

def test_mydsl::function::specifier_has_inline():
    assert hasattr(myDsl::function::specifier, "inline")
    descriptor = None
    for klass in myDsl::function::specifier.__mro__:
        if "inline" in klass.__dict__:
            descriptor = klass.__dict__["inline"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::function::specifier_has_noreturn():
    assert hasattr(myDsl::function::specifier, "noreturn")
    descriptor = None
    for klass in myDsl::function::specifier.__mro__:
        if "noreturn" in klass.__dict__:
            descriptor = klass.__dict__["noreturn"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::type::qualifier_is_not_abstract():
    assert not inspect.isabstract(myDsl::type::qualifier)


def test_mydsl::type::qualifier_constructor_exists():
    assert callable(myDsl::type::qualifier.__init__)


def test_mydsl::type::qualifier_constructor_args():
    sig = inspect.signature(myDsl::type::qualifier.__init__)
    params = list(sig.parameters.keys())
    assert "restrict" in params, "Missing parameter 'restrict'"
    assert "atomic" in params, "Missing parameter 'atomic'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "const" in params, "Missing parameter 'const'"

def test_mydsl::type::qualifier_has_restrict():
    assert hasattr(myDsl::type::qualifier, "restrict")
    descriptor = None
    for klass in myDsl::type::qualifier.__mro__:
        if "restrict" in klass.__dict__:
            descriptor = klass.__dict__["restrict"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::type::qualifier_has_atomic():
    assert hasattr(myDsl::type::qualifier, "atomic")
    descriptor = None
    for klass in myDsl::type::qualifier.__mro__:
        if "atomic" in klass.__dict__:
            descriptor = klass.__dict__["atomic"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::type::qualifier_has_volatile():
    assert hasattr(myDsl::type::qualifier, "volatile")
    descriptor = None
    for klass in myDsl::type::qualifier.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::type::qualifier_has_const():
    assert hasattr(myDsl::type::qualifier, "const")
    descriptor = None
    for klass in myDsl::type::qualifier.__mro__:
        if "const" in klass.__dict__:
            descriptor = klass.__dict__["const"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::type::specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl::type::specifier)


def test_mydsl::type::specifier_constructor_exists():
    assert callable(myDsl::type::specifier.__init__)


def test_mydsl::type::specifier_constructor_args():
    sig = inspect.signature(myDsl::type::specifier.__init__)
    params = list(sig.parameters.keys())
    assert "typedef_name" in params, "Missing parameter 'typedef_name'"

def test_mydsl::type::specifier_has_typedef_name():
    assert hasattr(myDsl::type::specifier, "typedef_name")
    descriptor = None
    for klass in myDsl::type::specifier.__mro__:
        if "typedef_name" in klass.__dict__:
            descriptor = klass.__dict__["typedef_name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::storage::class::specifier_is_not_abstract():
    assert not inspect.isabstract(myDsl::storage::class::specifier)


def test_mydsl::storage::class::specifier_constructor_exists():
    assert callable(myDsl::storage::class::specifier.__init__)


def test_mydsl::storage::class::specifier_constructor_args():
    sig = inspect.signature(myDsl::storage::class::specifier.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "register" in params, "Missing parameter 'register'"
    assert "auto" in params, "Missing parameter 'auto'"
    assert "typedef" in params, "Missing parameter 'typedef'"
    assert "thread_local" in params, "Missing parameter 'thread_local'"
    assert "extern" in params, "Missing parameter 'extern'"

def test_mydsl::storage::class::specifier_has_static():
    assert hasattr(myDsl::storage::class::specifier, "static")
    descriptor = None
    for klass in myDsl::storage::class::specifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::storage::class::specifier_has_register():
    assert hasattr(myDsl::storage::class::specifier, "register")
    descriptor = None
    for klass in myDsl::storage::class::specifier.__mro__:
        if "register" in klass.__dict__:
            descriptor = klass.__dict__["register"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::storage::class::specifier_has_auto():
    assert hasattr(myDsl::storage::class::specifier, "auto")
    descriptor = None
    for klass in myDsl::storage::class::specifier.__mro__:
        if "auto" in klass.__dict__:
            descriptor = klass.__dict__["auto"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::storage::class::specifier_has_typedef():
    assert hasattr(myDsl::storage::class::specifier, "typedef")
    descriptor = None
    for klass in myDsl::storage::class::specifier.__mro__:
        if "typedef" in klass.__dict__:
            descriptor = klass.__dict__["typedef"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::storage::class::specifier_has_thread_local():
    assert hasattr(myDsl::storage::class::specifier, "thread_local")
    descriptor = None
    for klass in myDsl::storage::class::specifier.__mro__:
        if "thread_local" in klass.__dict__:
            descriptor = klass.__dict__["thread_local"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::storage::class::specifier_has_extern():
    assert hasattr(myDsl::storage::class::specifier, "extern")
    descriptor = None
    for klass in myDsl::storage::class::specifier.__mro__:
        if "extern" in klass.__dict__:
            descriptor = klass.__dict__["extern"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::static::assert::declaration_is_not_abstract():
    assert not inspect.isabstract(myDsl::static::assert::declaration)


def test_mydsl::static::assert::declaration_constructor_exists():
    assert callable(myDsl::static::assert::declaration.__init__)


def test_mydsl::static::assert::declaration_constructor_args():
    sig = inspect.signature(myDsl::static::assert::declaration.__init__)
    params = list(sig.parameters.keys())
    assert "string_literal" in params, "Missing parameter 'string_literal'"
    assert "static_assert" in params, "Missing parameter 'static_assert'"

def test_mydsl::static::assert::declaration_has_string_literal():
    assert hasattr(myDsl::static::assert::declaration, "string_literal")
    descriptor = None
    for klass in myDsl::static::assert::declaration.__mro__:
        if "string_literal" in klass.__dict__:
            descriptor = klass.__dict__["string_literal"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::static::assert::declaration_has_static_assert():
    assert hasattr(myDsl::static::assert::declaration, "static_assert")
    descriptor = None
    for klass in myDsl::static::assert::declaration.__mro__:
        if "static_assert" in klass.__dict__:
            descriptor = klass.__dict__["static_assert"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::init::declarator::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::init::declarator::list)


def test_mydsl::init::declarator::list_constructor_exists():
    assert callable(myDsl::init::declarator::list.__init__)


def test_mydsl::init::declarator::list_constructor_args():
    sig = inspect.signature(myDsl::init::declarator::list.__init__)
    params = list(sig.parameters.keys())



def test_simple::expression_is_not_abstract():
    assert not inspect.isabstract(simple::expression)


def test_simple::expression_constructor_exists():
    assert callable(simple::expression.__init__)


def test_simple::expression_constructor_args():
    sig = inspect.signature(simple::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::floattype_is_not_abstract():
    assert not inspect.isabstract(myDsl::floatType)


def test_mydsl::floattype_constructor_exists():
    assert callable(myDsl::floatType.__init__)


def test_mydsl::floattype_constructor_args():
    sig = inspect.signature(myDsl::floatType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "float_type" in params, "Missing parameter 'float_type'"

def test_mydsl::floattype_has_value():
    assert hasattr(myDsl::floatType, "value")
    descriptor = None
    for klass in myDsl::floatType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::floattype_has_float_type():
    assert hasattr(myDsl::floatType, "float_type")
    descriptor = None
    for klass in myDsl::floatType.__mro__:
        if "float_type" in klass.__dict__:
            descriptor = klass.__dict__["float_type"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::inc::or_is_not_abstract():
    assert not inspect.isabstract(myDsl::INC::OR)


def test_mydsl::inc::or_constructor_exists():
    assert callable(myDsl::INC::OR.__init__)


def test_mydsl::inc::or_constructor_args():
    sig = inspect.signature(myDsl::INC::OR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::inttype_is_not_abstract():
    assert not inspect.isabstract(myDsl::intType)


def test_mydsl::inttype_constructor_exists():
    assert callable(myDsl::intType.__init__)


def test_mydsl::inttype_constructor_args():
    sig = inspect.signature(myDsl::intType.__init__)
    params = list(sig.parameters.keys())
    assert "int_type" in params, "Missing parameter 'int_type'"
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl::inttype_has_int_type():
    assert hasattr(myDsl::intType, "int_type")
    descriptor = None
    for klass in myDsl::intType.__mro__:
        if "int_type" in klass.__dict__:
            descriptor = klass.__dict__["int_type"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::inttype_has_value():
    assert hasattr(myDsl::intType, "value")
    descriptor = None
    for klass in myDsl::intType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::variableref_is_not_abstract():
    assert not inspect.isabstract(myDsl::variableRef)


def test_mydsl::variableref_constructor_exists():
    assert callable(myDsl::variableRef.__init__)


def test_mydsl::variableref_constructor_args():
    sig = inspect.signature(myDsl::variableRef.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_mydsl::variableref_has_variable():
    assert hasattr(myDsl::variableRef, "variable")
    descriptor = None
    for klass in myDsl::variableRef.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::log::and_is_not_abstract():
    assert not inspect.isabstract(myDsl::LOG::AND)


def test_mydsl::log::and_constructor_exists():
    assert callable(myDsl::LOG::AND.__init__)


def test_mydsl::log::and_constructor_args():
    sig = inspect.signature(myDsl::LOG::AND.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::eql_is_not_abstract():
    assert not inspect.isabstract(myDsl::EQL)


def test_mydsl::eql_constructor_exists():
    assert callable(myDsl::EQL.__init__)


def test_mydsl::eql_constructor_args():
    sig = inspect.signature(myDsl::EQL.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mydsl::eql_has_op():
    assert hasattr(myDsl::EQL, "op")
    descriptor = None
    for klass in myDsl::EQL.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::stringtype_is_not_abstract():
    assert not inspect.isabstract(myDsl::stringType)


def test_mydsl::stringtype_constructor_exists():
    assert callable(myDsl::stringType.__init__)


def test_mydsl::stringtype_constructor_args():
    sig = inspect.signature(myDsl::stringType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::exc::or_is_not_abstract():
    assert not inspect.isabstract(myDsl::EXC::OR)


def test_mydsl::exc::or_constructor_exists():
    assert callable(myDsl::EXC::OR.__init__)


def test_mydsl::exc::or_constructor_args():
    sig = inspect.signature(myDsl::EXC::OR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::add_is_not_abstract():
    assert not inspect.isabstract(myDsl::ADD)


def test_mydsl::add_constructor_exists():
    assert callable(myDsl::ADD.__init__)


def test_mydsl::add_constructor_args():
    sig = inspect.signature(myDsl::ADD.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::booleantype_is_not_abstract():
    assert not inspect.isabstract(myDsl::booleanType)


def test_mydsl::booleantype_constructor_exists():
    assert callable(myDsl::booleanType.__init__)


def test_mydsl::booleantype_constructor_args():
    sig = inspect.signature(myDsl::booleanType.__init__)
    params = list(sig.parameters.keys())
    assert "bool_type" in params, "Missing parameter 'bool_type'"
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl::booleantype_has_bool_type():
    assert hasattr(myDsl::booleanType, "bool_type")
    descriptor = None
    for klass in myDsl::booleanType.__mro__:
        if "bool_type" in klass.__dict__:
            descriptor = klass.__dict__["bool_type"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::booleantype_has_value():
    assert hasattr(myDsl::booleanType, "value")
    descriptor = None
    for klass in myDsl::booleanType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::minus_is_not_abstract():
    assert not inspect.isabstract(myDsl::MINUS)


def test_mydsl::minus_constructor_exists():
    assert callable(myDsl::MINUS.__init__)


def test_mydsl::minus_constructor_args():
    sig = inspect.signature(myDsl::MINUS.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::log::or_is_not_abstract():
    assert not inspect.isabstract(myDsl::LOG::OR)


def test_mydsl::log::or_constructor_exists():
    assert callable(myDsl::LOG::OR.__init__)


def test_mydsl::log::or_constructor_args():
    sig = inspect.signature(myDsl::LOG::OR.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::mul_is_not_abstract():
    assert not inspect.isabstract(myDsl::MUL)


def test_mydsl::mul_constructor_exists():
    assert callable(myDsl::MUL.__init__)


def test_mydsl::mul_constructor_args():
    sig = inspect.signature(myDsl::MUL.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mydsl::mul_has_op():
    assert hasattr(myDsl::MUL, "op")
    descriptor = None
    for klass in myDsl::MUL.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::and_is_not_abstract():
    assert not inspect.isabstract(myDsl::AND)


def test_mydsl::and_constructor_exists():
    assert callable(myDsl::AND.__init__)


def test_mydsl::and_constructor_args():
    sig = inspect.signature(myDsl::AND.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::shf_is_not_abstract():
    assert not inspect.isabstract(myDsl::SHF)


def test_mydsl::shf_constructor_exists():
    assert callable(myDsl::SHF.__init__)


def test_mydsl::shf_constructor_args():
    sig = inspect.signature(myDsl::SHF.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mydsl::shf_has_op():
    assert hasattr(myDsl::SHF, "op")
    descriptor = None
    for klass in myDsl::SHF.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::rel_is_not_abstract():
    assert not inspect.isabstract(myDsl::REL)


def test_mydsl::rel_constructor_exists():
    assert callable(myDsl::REL.__init__)


def test_mydsl::rel_constructor_args():
    sig = inspect.signature(myDsl::REL.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mydsl::rel_has_op():
    assert hasattr(myDsl::REL, "op")
    descriptor = None
    for klass in myDsl::REL.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::unary::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::unary::expression)


def test_mydsl::unary::expression_constructor_exists():
    assert callable(myDsl::unary::expression.__init__)


def test_mydsl::unary::expression_constructor_args():
    sig = inspect.signature(myDsl::unary::expression.__init__)
    params = list(sig.parameters.keys())
    assert "alignof" in params, "Missing parameter 'alignof'"
    assert "inc_op" in params, "Missing parameter 'inc_op'"
    assert "dec_op" in params, "Missing parameter 'dec_op'"
    assert "sizeof" in params, "Missing parameter 'sizeof'"
    assert "unary_operator" in params, "Missing parameter 'unary_operator'"

def test_mydsl::unary::expression_has_alignof():
    assert hasattr(myDsl::unary::expression, "alignof")
    descriptor = None
    for klass in myDsl::unary::expression.__mro__:
        if "alignof" in klass.__dict__:
            descriptor = klass.__dict__["alignof"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::unary::expression_has_inc_op():
    assert hasattr(myDsl::unary::expression, "inc_op")
    descriptor = None
    for klass in myDsl::unary::expression.__mro__:
        if "inc_op" in klass.__dict__:
            descriptor = klass.__dict__["inc_op"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::unary::expression_has_dec_op():
    assert hasattr(myDsl::unary::expression, "dec_op")
    descriptor = None
    for klass in myDsl::unary::expression.__mro__:
        if "dec_op" in klass.__dict__:
            descriptor = klass.__dict__["dec_op"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::unary::expression_has_sizeof():
    assert hasattr(myDsl::unary::expression, "sizeof")
    descriptor = None
    for klass in myDsl::unary::expression.__mro__:
        if "sizeof" in klass.__dict__:
            descriptor = klass.__dict__["sizeof"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::unary::expression_has_unary_operator():
    assert hasattr(myDsl::unary::expression, "unary_operator")
    descriptor = None
    for klass in myDsl::unary::expression.__mro__:
        if "unary_operator" in klass.__dict__:
            descriptor = klass.__dict__["unary_operator"]
            break
    assert isinstance(descriptor, property)



def test_postfix::expression2_is_not_abstract():
    assert not inspect.isabstract(postfix::expression2)


def test_postfix::expression2_constructor_exists():
    assert callable(postfix::expression2.__init__)


def test_postfix::expression2_constructor_args():
    sig = inspect.signature(postfix::expression2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::argument::expression::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::argument::expression::list)


def test_mydsl::argument::expression::list_constructor_exists():
    assert callable(myDsl::argument::expression::list.__init__)


def test_mydsl::argument::expression::list_constructor_args():
    sig = inspect.signature(myDsl::argument::expression::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::initializer::list_is_not_abstract():
    assert not inspect.isabstract(myDsl::initializer::list)


def test_mydsl::initializer::list_constructor_exists():
    assert callable(myDsl::initializer::list.__init__)


def test_mydsl::initializer::list_constructor_args():
    sig = inspect.signature(myDsl::initializer::list.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::postfix::expression2_is_not_abstract():
    assert not inspect.isabstract(myDsl::postfix::expression2)


def test_mydsl::postfix::expression2_constructor_exists():
    assert callable(myDsl::postfix::expression2.__init__)


def test_mydsl::postfix::expression2_constructor_args():
    sig = inspect.signature(myDsl::postfix::expression2.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::postfix::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::postfix::expression)


def test_mydsl::postfix::expression_constructor_exists():
    assert callable(myDsl::postfix::expression.__init__)


def test_mydsl::postfix::expression_constructor_args():
    sig = inspect.signature(myDsl::postfix::expression.__init__)
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



def test_mydsl::assignment::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::assignment::expression)


def test_mydsl::assignment::expression_constructor_exists():
    assert callable(myDsl::assignment::expression.__init__)


def test_mydsl::assignment::expression_constructor_args():
    sig = inspect.signature(myDsl::assignment::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::expression)


def test_mydsl::expression_constructor_exists():
    assert callable(myDsl::expression.__init__)


def test_mydsl::expression_constructor_args():
    sig = inspect.signature(myDsl::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::conditional::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::conditional::expression)


def test_mydsl::conditional::expression_constructor_exists():
    assert callable(myDsl::conditional::expression.__init__)


def test_mydsl::conditional::expression_constructor_args():
    sig = inspect.signature(myDsl::conditional::expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::constant_is_not_abstract():
    assert not inspect.isabstract(myDsl::constant)


def test_mydsl::constant_constructor_exists():
    assert callable(myDsl::constant.__init__)


def test_mydsl::constant_constructor_args():
    sig = inspect.signature(myDsl::constant.__init__)
    params = list(sig.parameters.keys())
    assert "enumt" in params, "Missing parameter 'enumt'"
    assert "i_constant" in params, "Missing parameter 'i_constant'"
    assert "f_constant" in params, "Missing parameter 'f_constant'"

def test_mydsl::constant_has_enumt():
    assert hasattr(myDsl::constant, "enumt")
    descriptor = None
    for klass in myDsl::constant.__mro__:
        if "enumt" in klass.__dict__:
            descriptor = klass.__dict__["enumt"]
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

def test_mydsl::constant_has_f_constant():
    assert hasattr(myDsl::constant, "f_constant")
    descriptor = None
    for klass in myDsl::constant.__mro__:
        if "f_constant" in klass.__dict__:
            descriptor = klass.__dict__["f_constant"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::type::name_is_not_abstract():
    assert not inspect.isabstract(myDsl::type::name)


def test_mydsl::type::name_constructor_exists():
    assert callable(myDsl::type::name.__init__)


def test_mydsl::type::name_constructor_args():
    sig = inspect.signature(myDsl::type::name.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::simple::expression_is_not_abstract():
    assert not inspect.isabstract(myDsl::simple::expression)


def test_mydsl::simple::expression_constructor_exists():
    assert callable(myDsl::simple::expression.__init__)


def test_mydsl::simple::expression_constructor_args():
    sig = inspect.signature(myDsl::simple::expression.__init__)
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



def test_mydsl::generic::selection_is_not_abstract():
    assert not inspect.isabstract(myDsl::generic::selection)


def test_mydsl::generic::selection_constructor_exists():
    assert callable(myDsl::generic::selection.__init__)


def test_mydsl::generic::selection_constructor_args():
    sig = inspect.signature(myDsl::generic::selection.__init__)
    params = list(sig.parameters.keys())
    assert "generic" in params, "Missing parameter 'generic'"

def test_mydsl::generic::selection_has_generic():
    assert hasattr(myDsl::generic::selection, "generic")
    descriptor = None
    for klass in myDsl::generic::selection.__mro__:
        if "generic" in klass.__dict__:
            descriptor = klass.__dict__["generic"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::string::nova_is_not_abstract():
    assert not inspect.isabstract(myDsl::string::nova)


def test_mydsl::string::nova_constructor_exists():
    assert callable(myDsl::string::nova.__init__)


def test_mydsl::string::nova_constructor_args():
    sig = inspect.signature(myDsl::string::nova.__init__)
    params = list(sig.parameters.keys())
    assert "func_name" in params, "Missing parameter 'func_name'"
    assert "string_literal" in params, "Missing parameter 'string_literal'"

def test_mydsl::string::nova_has_func_name():
    assert hasattr(myDsl::string::nova, "func_name")
    descriptor = None
    for klass in myDsl::string::nova.__mro__:
        if "func_name" in klass.__dict__:
            descriptor = klass.__dict__["func_name"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::string::nova_has_string_literal():
    assert hasattr(myDsl::string::nova, "string_literal")
    descriptor = None
    for klass in myDsl::string::nova.__mro__:
        if "string_literal" in klass.__dict__:
            descriptor = klass.__dict__["string_literal"]
            break
    assert isinstance(descriptor, property)



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
type::specifier_strategy = st.builds(
    type::specifier,
)
myDsl::complexType_strategy = st.builds(
    myDsl::complexType,
    complex_type=
        safe_text
)
myDsl::voidType_strategy = st.builds(
    myDsl::voidType,
    void_type=
        safe_text
)
myDsl::unsignedType_strategy = st.builds(
    myDsl::unsignedType,
    unsigned_type=
        safe_text
)
myDsl::doubleType_strategy = st.builds(
    myDsl::doubleType,
    double_type=
        safe_text
)
myDsl::longType_strategy = st.builds(
    myDsl::longType,
    long_type=
        safe_text
)
myDsl::shortType_strategy = st.builds(
    myDsl::shortType,
    short_type=
        safe_text
)
myDsl::signedType_strategy = st.builds(
    myDsl::signedType,
    signed_type=
        safe_text
)
myDsl::charType_strategy = st.builds(
    myDsl::charType,
    char_type=
        safe_text
)
myDsl::imaginaryType_strategy = st.builds(
    myDsl::imaginaryType,
    imaginary_type=
        safe_text
)
myDsl::declaration::list2_strategy = st.builds(
    myDsl::declaration::list2,
)
myDsl::external::declaration_strategy = st.builds(
    myDsl::external::declaration,
)
myDsl::EObject_strategy = st.builds(
    myDsl::EObject,
)
myDsl::declaration::list_strategy = st.builds(
    myDsl::declaration::list,
)
myDsl::function::definition_strategy = st.builds(
    myDsl::function::definition,
)
myDsl::jump::statement_strategy = st.builds(
    myDsl::jump::statement,
    goto=
        safe_text,
    return_=
        safe_text,
    break_=
        safe_text,
    continue_=
        safe_text,
    identifier=
        safe_text
)
myDsl::iteration::statement_strategy = st.builds(
    myDsl::iteration::statement,
    for_=
        safe_text,
    do=
        safe_text,
    while_=
        safe_text
)
myDsl::selection::statement_strategy = st.builds(
    myDsl::selection::statement,
    switch=
        safe_text,
    if_=
        safe_text,
    else_=
        safe_text
)
myDsl::expression::statement_strategy = st.builds(
    myDsl::expression::statement,
)
myDsl::compound::statement_strategy = st.builds(
    myDsl::compound::statement,
)
myDsl::labeled::statement_strategy = st.builds(
    myDsl::labeled::statement,
    identifier=
        safe_text,
    default=
        safe_text,
    case=
        safe_text
)
myDsl::statement_strategy = st.builds(
    myDsl::statement,
)
myDsl::block::item_strategy = st.builds(
    myDsl::block::item,
)
myDsl::initializer::list2_strategy = st.builds(
    myDsl::initializer::list2,
)
myDsl::designation_strategy = st.builds(
    myDsl::designation,
)
myDsl::initializer_strategy = st.builds(
    myDsl::initializer,
)
myDsl::direct::abstract::declarator2_strategy = st.builds(
    myDsl::direct::abstract::declarator2,
    static=
        safe_text
)
myDsl::direct::abstract::declarator_strategy = st.builds(
    myDsl::direct::abstract::declarator,
)
myDsl::designator::list2_strategy = st.builds(
    myDsl::designator::list2,
)
myDsl::designator_strategy = st.builds(
    myDsl::designator,
    identifier=
        safe_text
)
myDsl::designator::list_strategy = st.builds(
    myDsl::designator::list,
)
myDsl::parameter::list2_strategy = st.builds(
    myDsl::parameter::list2,
)
myDsl::parameter::declaration_strategy = st.builds(
    myDsl::parameter::declaration,
)
myDsl::parameter::list_strategy = st.builds(
    myDsl::parameter::list,
)
myDsl::type::qualifier::list2_strategy = st.builds(
    myDsl::type::qualifier::list2,
)
myDsl::identifier::list2_strategy = st.builds(
    myDsl::identifier::list2,
    identifier=
        safe_text
)
myDsl::abstract::declarator_strategy = st.builds(
    myDsl::abstract::declarator,
)
myDsl::direct::declarator_strategy = st.builds(
    myDsl::direct::declarator,
    name=
        safe_text
)
myDsl::pointer_strategy = st.builds(
    myDsl::pointer,
)
myDsl::identifier::list_strategy = st.builds(
    myDsl::identifier::list,
    identifier=
        safe_text
)
myDsl::parameter::type::list_strategy = st.builds(
    myDsl::parameter::type::list,
    ellipsis=
        safe_text
)
myDsl::type::qualifier::list_strategy = st.builds(
    myDsl::type::qualifier::list,
)
myDsl::direct::declarator2_strategy = st.builds(
    myDsl::direct::declarator2,
    static=
        safe_text
)
myDsl::struct::declarator::list2_strategy = st.builds(
    myDsl::struct::declarator::list2,
)
myDsl::struct::declarator_strategy = st.builds(
    myDsl::struct::declarator,
)
myDsl::struct::declarator::list_strategy = st.builds(
    myDsl::struct::declarator::list,
)
myDsl::specifier::qualifier::list_strategy = st.builds(
    myDsl::specifier::qualifier::list,
)
myDsl::enumerator::list2_strategy = st.builds(
    myDsl::enumerator::list2,
)
myDsl::enumerator_strategy = st.builds(
    myDsl::enumerator,
)
myDsl::enumerator::list_strategy = st.builds(
    myDsl::enumerator::list,
)
myDsl::atomic::type::specifier_strategy = st.builds(
    myDsl::atomic::type::specifier,
    atomic=
        safe_text
)
myDsl::declarator_strategy = st.builds(
    myDsl::declarator,
)
myDsl::init::declarator::list2_strategy = st.builds(
    myDsl::init::declarator::list2,
)
myDsl::init::declarator_strategy = st.builds(
    myDsl::init::declarator,
)
myDsl::alignment::specifier_strategy = st.builds(
    myDsl::alignment::specifier,
    alignas=
        safe_text
)
myDsl::struct::declaration::list2_strategy = st.builds(
    myDsl::struct::declaration::list2,
)
myDsl::struct::declaration_strategy = st.builds(
    myDsl::struct::declaration,
)
struct::or::union::specifier_strategy = st.builds(
    struct::or::union::specifier,
)
myDsl::struct::declaration::list_strategy = st.builds(
    myDsl::struct::declaration::list,
)
myDsl::struct::or::union_strategy = st.builds(
    myDsl::struct::or::union,
    union=
        safe_text,
    struct=
        safe_text
)
myDsl::enum::specifier_strategy = st.builds(
    myDsl::enum::specifier,
    identifier=
        safe_text,
    enumt=
        safe_text
)
myDsl::struct::or::union::specifier_strategy = st.builds(
    myDsl::struct::or::union::specifier,
    identifier=
        safe_text
)
myDsl::declaration::specifiers_strategy = st.builds(
    myDsl::declaration::specifiers,
)
myDsl::declaration_strategy = st.builds(
    myDsl::declaration,
)
myDsl::constant::expression_strategy = st.builds(
    myDsl::constant::expression,
)
myDsl::expression2_strategy = st.builds(
    myDsl::expression2,
)
myDsl::assignment::operator_strategy = st.builds(
    myDsl::assignment::operator,
    left_assign=
        safe_text,
    or_assign=
        safe_text,
    xor_assign=
        safe_text,
    and_assign=
        safe_text,
    div_assign=
        safe_text,
    right_assign=
        safe_text,
    sub_assign=
        safe_text,
    add_assign=
        safe_text,
    mul_assign=
        safe_text,
    mod_assign=
        safe_text
)
myDsl::function::specifier_strategy = st.builds(
    myDsl::function::specifier,
    inline=
        safe_text,
    noreturn=
        safe_text
)
myDsl::type::qualifier_strategy = st.builds(
    myDsl::type::qualifier,
    restrict=
        safe_text,
    atomic=
        safe_text,
    volatile=
        safe_text,
    const=
        safe_text
)
myDsl::type::specifier_strategy = st.builds(
    myDsl::type::specifier,
    typedef_name=
        safe_text
)
myDsl::storage::class::specifier_strategy = st.builds(
    myDsl::storage::class::specifier,
    static=
        safe_text,
    register=
        safe_text,
    auto=
        safe_text,
    typedef=
        safe_text,
    thread_local=
        safe_text,
    extern=
        safe_text
)
myDsl::static::assert::declaration_strategy = st.builds(
    myDsl::static::assert::declaration,
    string_literal=
        safe_text,
    static_assert=
        safe_text
)
myDsl::init::declarator::list_strategy = st.builds(
    myDsl::init::declarator::list,
)
simple::expression_strategy = st.builds(
    simple::expression,
)
myDsl::floatType_strategy = st.builds(
    myDsl::floatType,
    value=
        safe_text,
    float_type=
        safe_text
)
myDsl::INC::OR_strategy = st.builds(
    myDsl::INC::OR,
)
myDsl::intType_strategy = st.builds(
    myDsl::intType,
    int_type=
        safe_text,
    value=
        safe_text
)
myDsl::variableRef_strategy = st.builds(
    myDsl::variableRef,
    variable=
        safe_text
)
myDsl::LOG::AND_strategy = st.builds(
    myDsl::LOG::AND,
)
myDsl::EQL_strategy = st.builds(
    myDsl::EQL,
    op=
        safe_text
)
myDsl::stringType_strategy = st.builds(
    myDsl::stringType,
)
myDsl::EXC::OR_strategy = st.builds(
    myDsl::EXC::OR,
)
myDsl::ADD_strategy = st.builds(
    myDsl::ADD,
)
myDsl::booleanType_strategy = st.builds(
    myDsl::booleanType,
    bool_type=
        safe_text,
    value=
        safe_text
)
myDsl::MINUS_strategy = st.builds(
    myDsl::MINUS,
)
myDsl::LOG::OR_strategy = st.builds(
    myDsl::LOG::OR,
)
myDsl::MUL_strategy = st.builds(
    myDsl::MUL,
    op=
        safe_text
)
myDsl::AND_strategy = st.builds(
    myDsl::AND,
)
myDsl::SHF_strategy = st.builds(
    myDsl::SHF,
    op=
        safe_text
)
myDsl::REL_strategy = st.builds(
    myDsl::REL,
    op=
        safe_text
)
myDsl::unary::expression_strategy = st.builds(
    myDsl::unary::expression,
    alignof=
        safe_text,
    inc_op=
        safe_text,
    dec_op=
        safe_text,
    sizeof=
        safe_text,
    unary_operator=
        safe_text
)
postfix::expression2_strategy = st.builds(
    postfix::expression2,
)
myDsl::argument::expression::list_strategy = st.builds(
    myDsl::argument::expression::list,
)
myDsl::initializer::list_strategy = st.builds(
    myDsl::initializer::list,
)
myDsl::postfix::expression2_strategy = st.builds(
    myDsl::postfix::expression2,
)
myDsl::postfix::expression_strategy = st.builds(
    myDsl::postfix::expression,
)
myDsl::generic::association_strategy = st.builds(
    myDsl::generic::association,
    default=
        safe_text
)
myDsl::generic::assoc::list_strategy = st.builds(
    myDsl::generic::assoc::list,
)
myDsl::assignment::expression_strategy = st.builds(
    myDsl::assignment::expression,
)
myDsl::expression_strategy = st.builds(
    myDsl::expression,
)
myDsl::conditional::expression_strategy = st.builds(
    myDsl::conditional::expression,
)
myDsl::constant_strategy = st.builds(
    myDsl::constant,
    enumt=
        safe_text,
    i_constant=
        safe_text,
    f_constant=
        safe_text
)
myDsl::type::name_strategy = st.builds(
    myDsl::type::name,
)
myDsl::simple::expression_strategy = st.builds(
    myDsl::simple::expression,
)
myDsl::translation::unit_strategy = st.builds(
    myDsl::translation::unit,
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
)
myDsl::generic::selection_strategy = st.builds(
    myDsl::generic::selection,
    generic=
        safe_text
)
myDsl::string::nova_strategy = st.builds(
    myDsl::string::nova,
    func_name=
        safe_text,
    string_literal=
        safe_text
)
myDsl::enumeration::constant_strategy = st.builds(
    myDsl::enumeration::constant,
    identifier=
        safe_text
)

@given(instance=type::specifier_strategy)
@settings(max_examples=50)
def test_type::specifier_instantiation(instance):
    assert isinstance(instance, type::specifier)

@given(instance=myDsl::complexType_strategy)
@settings(max_examples=50)
def test_mydsl::complextype_instantiation(instance):
    assert isinstance(instance, myDsl::complexType)

@given(instance=myDsl::complexType_strategy)
def test_mydsl::complextype_complex_type_type(instance):
    assert isinstance(instance.complex_type, str)


@given(instance=myDsl::complexType_strategy)
def test_mydsl::complextype_complex_type_setter(instance):
    original = instance.complex_type
    instance.complex_type = original
    assert instance.complex_type == original

@given(instance=myDsl::voidType_strategy)
@settings(max_examples=50)
def test_mydsl::voidtype_instantiation(instance):
    assert isinstance(instance, myDsl::voidType)

@given(instance=myDsl::voidType_strategy)
def test_mydsl::voidtype_void_type_type(instance):
    assert isinstance(instance.void_type, str)


@given(instance=myDsl::voidType_strategy)
def test_mydsl::voidtype_void_type_setter(instance):
    original = instance.void_type
    instance.void_type = original
    assert instance.void_type == original

@given(instance=myDsl::unsignedType_strategy)
@settings(max_examples=50)
def test_mydsl::unsignedtype_instantiation(instance):
    assert isinstance(instance, myDsl::unsignedType)

@given(instance=myDsl::unsignedType_strategy)
def test_mydsl::unsignedtype_unsigned_type_type(instance):
    assert isinstance(instance.unsigned_type, str)


@given(instance=myDsl::unsignedType_strategy)
def test_mydsl::unsignedtype_unsigned_type_setter(instance):
    original = instance.unsigned_type
    instance.unsigned_type = original
    assert instance.unsigned_type == original

@given(instance=myDsl::doubleType_strategy)
@settings(max_examples=50)
def test_mydsl::doubletype_instantiation(instance):
    assert isinstance(instance, myDsl::doubleType)

@given(instance=myDsl::doubleType_strategy)
def test_mydsl::doubletype_double_type_type(instance):
    assert isinstance(instance.double_type, str)


@given(instance=myDsl::doubleType_strategy)
def test_mydsl::doubletype_double_type_setter(instance):
    original = instance.double_type
    instance.double_type = original
    assert instance.double_type == original

@given(instance=myDsl::longType_strategy)
@settings(max_examples=50)
def test_mydsl::longtype_instantiation(instance):
    assert isinstance(instance, myDsl::longType)

@given(instance=myDsl::longType_strategy)
def test_mydsl::longtype_long_type_type(instance):
    assert isinstance(instance.long_type, str)


@given(instance=myDsl::longType_strategy)
def test_mydsl::longtype_long_type_setter(instance):
    original = instance.long_type
    instance.long_type = original
    assert instance.long_type == original

@given(instance=myDsl::shortType_strategy)
@settings(max_examples=50)
def test_mydsl::shorttype_instantiation(instance):
    assert isinstance(instance, myDsl::shortType)

@given(instance=myDsl::shortType_strategy)
def test_mydsl::shorttype_short_type_type(instance):
    assert isinstance(instance.short_type, str)


@given(instance=myDsl::shortType_strategy)
def test_mydsl::shorttype_short_type_setter(instance):
    original = instance.short_type
    instance.short_type = original
    assert instance.short_type == original

@given(instance=myDsl::signedType_strategy)
@settings(max_examples=50)
def test_mydsl::signedtype_instantiation(instance):
    assert isinstance(instance, myDsl::signedType)

@given(instance=myDsl::signedType_strategy)
def test_mydsl::signedtype_signed_type_type(instance):
    assert isinstance(instance.signed_type, str)


@given(instance=myDsl::signedType_strategy)
def test_mydsl::signedtype_signed_type_setter(instance):
    original = instance.signed_type
    instance.signed_type = original
    assert instance.signed_type == original

@given(instance=myDsl::charType_strategy)
@settings(max_examples=50)
def test_mydsl::chartype_instantiation(instance):
    assert isinstance(instance, myDsl::charType)

@given(instance=myDsl::charType_strategy)
def test_mydsl::chartype_char_type_type(instance):
    assert isinstance(instance.char_type, str)


@given(instance=myDsl::charType_strategy)
def test_mydsl::chartype_char_type_setter(instance):
    original = instance.char_type
    instance.char_type = original
    assert instance.char_type == original

@given(instance=myDsl::imaginaryType_strategy)
@settings(max_examples=50)
def test_mydsl::imaginarytype_instantiation(instance):
    assert isinstance(instance, myDsl::imaginaryType)

@given(instance=myDsl::imaginaryType_strategy)
def test_mydsl::imaginarytype_imaginary_type_type(instance):
    assert isinstance(instance.imaginary_type, str)


@given(instance=myDsl::imaginaryType_strategy)
def test_mydsl::imaginarytype_imaginary_type_setter(instance):
    original = instance.imaginary_type
    instance.imaginary_type = original
    assert instance.imaginary_type == original

@given(instance=myDsl::declaration::list2_strategy)
@settings(max_examples=50)
def test_mydsl::declaration::list2_instantiation(instance):
    assert isinstance(instance, myDsl::declaration::list2)

@given(instance=myDsl::external::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::external::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::external::declaration)

@given(instance=myDsl::EObject_strategy)
@settings(max_examples=50)
def test_mydsl::eobject_instantiation(instance):
    assert isinstance(instance, myDsl::EObject)

@given(instance=myDsl::declaration::list_strategy)
@settings(max_examples=50)
def test_mydsl::declaration::list_instantiation(instance):
    assert isinstance(instance, myDsl::declaration::list)

@given(instance=myDsl::function::definition_strategy)
@settings(max_examples=50)
def test_mydsl::function::definition_instantiation(instance):
    assert isinstance(instance, myDsl::function::definition)

@given(instance=myDsl::jump::statement_strategy)
@settings(max_examples=50)
def test_mydsl::jump::statement_instantiation(instance):
    assert isinstance(instance, myDsl::jump::statement)

@given(instance=myDsl::jump::statement_strategy)
def test_mydsl::jump::statement_goto_type(instance):
    assert isinstance(instance.goto, str)


@given(instance=myDsl::jump::statement_strategy)
def test_mydsl::jump::statement_goto_setter(instance):
    original = instance.goto
    instance.goto = original
    assert instance.goto == original

@given(instance=myDsl::jump::statement_strategy)
def test_mydsl::jump::statement_return__type(instance):
    assert isinstance(instance.return_, str)


@given(instance=myDsl::jump::statement_strategy)
def test_mydsl::jump::statement_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original

@given(instance=myDsl::jump::statement_strategy)
def test_mydsl::jump::statement_break__type(instance):
    assert isinstance(instance.break_, str)


@given(instance=myDsl::jump::statement_strategy)
def test_mydsl::jump::statement_break__setter(instance):
    original = instance.break_
    instance.break_ = original
    assert instance.break_ == original

@given(instance=myDsl::jump::statement_strategy)
def test_mydsl::jump::statement_continue__type(instance):
    assert isinstance(instance.continue_, str)


@given(instance=myDsl::jump::statement_strategy)
def test_mydsl::jump::statement_continue__setter(instance):
    original = instance.continue_
    instance.continue_ = original
    assert instance.continue_ == original

@given(instance=myDsl::jump::statement_strategy)
def test_mydsl::jump::statement_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=myDsl::jump::statement_strategy)
def test_mydsl::jump::statement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl::iteration::statement_strategy)
@settings(max_examples=50)
def test_mydsl::iteration::statement_instantiation(instance):
    assert isinstance(instance, myDsl::iteration::statement)

@given(instance=myDsl::iteration::statement_strategy)
def test_mydsl::iteration::statement_for__type(instance):
    assert isinstance(instance.for_, str)


@given(instance=myDsl::iteration::statement_strategy)
def test_mydsl::iteration::statement_for__setter(instance):
    original = instance.for_
    instance.for_ = original
    assert instance.for_ == original

@given(instance=myDsl::iteration::statement_strategy)
def test_mydsl::iteration::statement_do_type(instance):
    assert isinstance(instance.do, str)


@given(instance=myDsl::iteration::statement_strategy)
def test_mydsl::iteration::statement_do_setter(instance):
    original = instance.do
    instance.do = original
    assert instance.do == original

@given(instance=myDsl::iteration::statement_strategy)
def test_mydsl::iteration::statement_while__type(instance):
    assert isinstance(instance.while_, str)


@given(instance=myDsl::iteration::statement_strategy)
def test_mydsl::iteration::statement_while__setter(instance):
    original = instance.while_
    instance.while_ = original
    assert instance.while_ == original

@given(instance=myDsl::selection::statement_strategy)
@settings(max_examples=50)
def test_mydsl::selection::statement_instantiation(instance):
    assert isinstance(instance, myDsl::selection::statement)

@given(instance=myDsl::selection::statement_strategy)
def test_mydsl::selection::statement_switch_type(instance):
    assert isinstance(instance.switch, str)


@given(instance=myDsl::selection::statement_strategy)
def test_mydsl::selection::statement_switch_setter(instance):
    original = instance.switch
    instance.switch = original
    assert instance.switch == original

@given(instance=myDsl::selection::statement_strategy)
def test_mydsl::selection::statement_if__type(instance):
    assert isinstance(instance.if_, str)


@given(instance=myDsl::selection::statement_strategy)
def test_mydsl::selection::statement_if__setter(instance):
    original = instance.if_
    instance.if_ = original
    assert instance.if_ == original

@given(instance=myDsl::selection::statement_strategy)
def test_mydsl::selection::statement_else__type(instance):
    assert isinstance(instance.else_, str)


@given(instance=myDsl::selection::statement_strategy)
def test_mydsl::selection::statement_else__setter(instance):
    original = instance.else_
    instance.else_ = original
    assert instance.else_ == original

@given(instance=myDsl::expression::statement_strategy)
@settings(max_examples=50)
def test_mydsl::expression::statement_instantiation(instance):
    assert isinstance(instance, myDsl::expression::statement)

@given(instance=myDsl::compound::statement_strategy)
@settings(max_examples=50)
def test_mydsl::compound::statement_instantiation(instance):
    assert isinstance(instance, myDsl::compound::statement)

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

@given(instance=myDsl::labeled::statement_strategy)
def test_mydsl::labeled::statement_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=myDsl::labeled::statement_strategy)
def test_mydsl::labeled::statement_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=myDsl::labeled::statement_strategy)
def test_mydsl::labeled::statement_case_type(instance):
    assert isinstance(instance.case, str)


@given(instance=myDsl::labeled::statement_strategy)
def test_mydsl::labeled::statement_case_setter(instance):
    original = instance.case
    instance.case = original
    assert instance.case == original

@given(instance=myDsl::statement_strategy)
@settings(max_examples=50)
def test_mydsl::statement_instantiation(instance):
    assert isinstance(instance, myDsl::statement)

@given(instance=myDsl::block::item_strategy)
@settings(max_examples=50)
def test_mydsl::block::item_instantiation(instance):
    assert isinstance(instance, myDsl::block::item)

@given(instance=myDsl::initializer::list2_strategy)
@settings(max_examples=50)
def test_mydsl::initializer::list2_instantiation(instance):
    assert isinstance(instance, myDsl::initializer::list2)

@given(instance=myDsl::designation_strategy)
@settings(max_examples=50)
def test_mydsl::designation_instantiation(instance):
    assert isinstance(instance, myDsl::designation)

@given(instance=myDsl::initializer_strategy)
@settings(max_examples=50)
def test_mydsl::initializer_instantiation(instance):
    assert isinstance(instance, myDsl::initializer)

@given(instance=myDsl::direct::abstract::declarator2_strategy)
@settings(max_examples=50)
def test_mydsl::direct::abstract::declarator2_instantiation(instance):
    assert isinstance(instance, myDsl::direct::abstract::declarator2)

@given(instance=myDsl::direct::abstract::declarator2_strategy)
def test_mydsl::direct::abstract::declarator2_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=myDsl::direct::abstract::declarator2_strategy)
def test_mydsl::direct::abstract::declarator2_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=myDsl::direct::abstract::declarator_strategy)
@settings(max_examples=50)
def test_mydsl::direct::abstract::declarator_instantiation(instance):
    assert isinstance(instance, myDsl::direct::abstract::declarator)

@given(instance=myDsl::designator::list2_strategy)
@settings(max_examples=50)
def test_mydsl::designator::list2_instantiation(instance):
    assert isinstance(instance, myDsl::designator::list2)

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

@given(instance=myDsl::parameter::list2_strategy)
@settings(max_examples=50)
def test_mydsl::parameter::list2_instantiation(instance):
    assert isinstance(instance, myDsl::parameter::list2)

@given(instance=myDsl::parameter::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::parameter::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::parameter::declaration)

@given(instance=myDsl::parameter::list_strategy)
@settings(max_examples=50)
def test_mydsl::parameter::list_instantiation(instance):
    assert isinstance(instance, myDsl::parameter::list)

@given(instance=myDsl::type::qualifier::list2_strategy)
@settings(max_examples=50)
def test_mydsl::type::qualifier::list2_instantiation(instance):
    assert isinstance(instance, myDsl::type::qualifier::list2)

@given(instance=myDsl::identifier::list2_strategy)
@settings(max_examples=50)
def test_mydsl::identifier::list2_instantiation(instance):
    assert isinstance(instance, myDsl::identifier::list2)

@given(instance=myDsl::identifier::list2_strategy)
def test_mydsl::identifier::list2_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=myDsl::identifier::list2_strategy)
def test_mydsl::identifier::list2_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=myDsl::abstract::declarator_strategy)
@settings(max_examples=50)
def test_mydsl::abstract::declarator_instantiation(instance):
    assert isinstance(instance, myDsl::abstract::declarator)

@given(instance=myDsl::direct::declarator_strategy)
@settings(max_examples=50)
def test_mydsl::direct::declarator_instantiation(instance):
    assert isinstance(instance, myDsl::direct::declarator)

@given(instance=myDsl::direct::declarator_strategy)
def test_mydsl::direct::declarator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::direct::declarator_strategy)
def test_mydsl::direct::declarator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::pointer_strategy)
@settings(max_examples=50)
def test_mydsl::pointer_instantiation(instance):
    assert isinstance(instance, myDsl::pointer)

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

@given(instance=myDsl::parameter::type::list_strategy)
def test_mydsl::parameter::type::list_ellipsis_type(instance):
    assert isinstance(instance.ellipsis, str)


@given(instance=myDsl::parameter::type::list_strategy)
def test_mydsl::parameter::type::list_ellipsis_setter(instance):
    original = instance.ellipsis
    instance.ellipsis = original
    assert instance.ellipsis == original

@given(instance=myDsl::type::qualifier::list_strategy)
@settings(max_examples=50)
def test_mydsl::type::qualifier::list_instantiation(instance):
    assert isinstance(instance, myDsl::type::qualifier::list)

@given(instance=myDsl::direct::declarator2_strategy)
@settings(max_examples=50)
def test_mydsl::direct::declarator2_instantiation(instance):
    assert isinstance(instance, myDsl::direct::declarator2)

@given(instance=myDsl::direct::declarator2_strategy)
def test_mydsl::direct::declarator2_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=myDsl::direct::declarator2_strategy)
def test_mydsl::direct::declarator2_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=myDsl::struct::declarator::list2_strategy)
@settings(max_examples=50)
def test_mydsl::struct::declarator::list2_instantiation(instance):
    assert isinstance(instance, myDsl::struct::declarator::list2)

@given(instance=myDsl::struct::declarator_strategy)
@settings(max_examples=50)
def test_mydsl::struct::declarator_instantiation(instance):
    assert isinstance(instance, myDsl::struct::declarator)

@given(instance=myDsl::struct::declarator::list_strategy)
@settings(max_examples=50)
def test_mydsl::struct::declarator::list_instantiation(instance):
    assert isinstance(instance, myDsl::struct::declarator::list)

@given(instance=myDsl::specifier::qualifier::list_strategy)
@settings(max_examples=50)
def test_mydsl::specifier::qualifier::list_instantiation(instance):
    assert isinstance(instance, myDsl::specifier::qualifier::list)

@given(instance=myDsl::enumerator::list2_strategy)
@settings(max_examples=50)
def test_mydsl::enumerator::list2_instantiation(instance):
    assert isinstance(instance, myDsl::enumerator::list2)

@given(instance=myDsl::enumerator_strategy)
@settings(max_examples=50)
def test_mydsl::enumerator_instantiation(instance):
    assert isinstance(instance, myDsl::enumerator)

@given(instance=myDsl::enumerator::list_strategy)
@settings(max_examples=50)
def test_mydsl::enumerator::list_instantiation(instance):
    assert isinstance(instance, myDsl::enumerator::list)

@given(instance=myDsl::atomic::type::specifier_strategy)
@settings(max_examples=50)
def test_mydsl::atomic::type::specifier_instantiation(instance):
    assert isinstance(instance, myDsl::atomic::type::specifier)

@given(instance=myDsl::atomic::type::specifier_strategy)
def test_mydsl::atomic::type::specifier_atomic_type(instance):
    assert isinstance(instance.atomic, str)


@given(instance=myDsl::atomic::type::specifier_strategy)
def test_mydsl::atomic::type::specifier_atomic_setter(instance):
    original = instance.atomic
    instance.atomic = original
    assert instance.atomic == original

@given(instance=myDsl::declarator_strategy)
@settings(max_examples=50)
def test_mydsl::declarator_instantiation(instance):
    assert isinstance(instance, myDsl::declarator)

@given(instance=myDsl::init::declarator::list2_strategy)
@settings(max_examples=50)
def test_mydsl::init::declarator::list2_instantiation(instance):
    assert isinstance(instance, myDsl::init::declarator::list2)

@given(instance=myDsl::init::declarator_strategy)
@settings(max_examples=50)
def test_mydsl::init::declarator_instantiation(instance):
    assert isinstance(instance, myDsl::init::declarator)

@given(instance=myDsl::alignment::specifier_strategy)
@settings(max_examples=50)
def test_mydsl::alignment::specifier_instantiation(instance):
    assert isinstance(instance, myDsl::alignment::specifier)

@given(instance=myDsl::alignment::specifier_strategy)
def test_mydsl::alignment::specifier_alignas_type(instance):
    assert isinstance(instance.alignas, str)


@given(instance=myDsl::alignment::specifier_strategy)
def test_mydsl::alignment::specifier_alignas_setter(instance):
    original = instance.alignas
    instance.alignas = original
    assert instance.alignas == original

@given(instance=myDsl::struct::declaration::list2_strategy)
@settings(max_examples=50)
def test_mydsl::struct::declaration::list2_instantiation(instance):
    assert isinstance(instance, myDsl::struct::declaration::list2)

@given(instance=myDsl::struct::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::struct::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::struct::declaration)

@given(instance=struct::or::union::specifier_strategy)
@settings(max_examples=50)
def test_struct::or::union::specifier_instantiation(instance):
    assert isinstance(instance, struct::or::union::specifier)

@given(instance=myDsl::struct::declaration::list_strategy)
@settings(max_examples=50)
def test_mydsl::struct::declaration::list_instantiation(instance):
    assert isinstance(instance, myDsl::struct::declaration::list)

@given(instance=myDsl::struct::or::union_strategy)
@settings(max_examples=50)
def test_mydsl::struct::or::union_instantiation(instance):
    assert isinstance(instance, myDsl::struct::or::union)

@given(instance=myDsl::struct::or::union_strategy)
def test_mydsl::struct::or::union_union_type(instance):
    assert isinstance(instance.union, str)


@given(instance=myDsl::struct::or::union_strategy)
def test_mydsl::struct::or::union_union_setter(instance):
    original = instance.union
    instance.union = original
    assert instance.union == original

@given(instance=myDsl::struct::or::union_strategy)
def test_mydsl::struct::or::union_struct_type(instance):
    assert isinstance(instance.struct, str)


@given(instance=myDsl::struct::or::union_strategy)
def test_mydsl::struct::or::union_struct_setter(instance):
    original = instance.struct
    instance.struct = original
    assert instance.struct == original

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

@given(instance=myDsl::enum::specifier_strategy)
def test_mydsl::enum::specifier_enumt_type(instance):
    assert isinstance(instance.enumt, str)


@given(instance=myDsl::enum::specifier_strategy)
def test_mydsl::enum::specifier_enumt_setter(instance):
    original = instance.enumt
    instance.enumt = original
    assert instance.enumt == original

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

@given(instance=myDsl::declaration::specifiers_strategy)
@settings(max_examples=50)
def test_mydsl::declaration::specifiers_instantiation(instance):
    assert isinstance(instance, myDsl::declaration::specifiers)

@given(instance=myDsl::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::declaration)

@given(instance=myDsl::constant::expression_strategy)
@settings(max_examples=50)
def test_mydsl::constant::expression_instantiation(instance):
    assert isinstance(instance, myDsl::constant::expression)

@given(instance=myDsl::expression2_strategy)
@settings(max_examples=50)
def test_mydsl::expression2_instantiation(instance):
    assert isinstance(instance, myDsl::expression2)

@given(instance=myDsl::assignment::operator_strategy)
@settings(max_examples=50)
def test_mydsl::assignment::operator_instantiation(instance):
    assert isinstance(instance, myDsl::assignment::operator)

@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_left_assign_type(instance):
    assert isinstance(instance.left_assign, str)


@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_left_assign_setter(instance):
    original = instance.left_assign
    instance.left_assign = original
    assert instance.left_assign == original

@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_or_assign_type(instance):
    assert isinstance(instance.or_assign, str)


@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_or_assign_setter(instance):
    original = instance.or_assign
    instance.or_assign = original
    assert instance.or_assign == original

@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_xor_assign_type(instance):
    assert isinstance(instance.xor_assign, str)


@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_xor_assign_setter(instance):
    original = instance.xor_assign
    instance.xor_assign = original
    assert instance.xor_assign == original

@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_and_assign_type(instance):
    assert isinstance(instance.and_assign, str)


@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_and_assign_setter(instance):
    original = instance.and_assign
    instance.and_assign = original
    assert instance.and_assign == original

@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_div_assign_type(instance):
    assert isinstance(instance.div_assign, str)


@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_div_assign_setter(instance):
    original = instance.div_assign
    instance.div_assign = original
    assert instance.div_assign == original

@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_right_assign_type(instance):
    assert isinstance(instance.right_assign, str)


@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_right_assign_setter(instance):
    original = instance.right_assign
    instance.right_assign = original
    assert instance.right_assign == original

@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_sub_assign_type(instance):
    assert isinstance(instance.sub_assign, str)


@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_sub_assign_setter(instance):
    original = instance.sub_assign
    instance.sub_assign = original
    assert instance.sub_assign == original

@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_add_assign_type(instance):
    assert isinstance(instance.add_assign, str)


@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_add_assign_setter(instance):
    original = instance.add_assign
    instance.add_assign = original
    assert instance.add_assign == original

@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_mul_assign_type(instance):
    assert isinstance(instance.mul_assign, str)


@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_mul_assign_setter(instance):
    original = instance.mul_assign
    instance.mul_assign = original
    assert instance.mul_assign == original

@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_mod_assign_type(instance):
    assert isinstance(instance.mod_assign, str)


@given(instance=myDsl::assignment::operator_strategy)
def test_mydsl::assignment::operator_mod_assign_setter(instance):
    original = instance.mod_assign
    instance.mod_assign = original
    assert instance.mod_assign == original

@given(instance=myDsl::function::specifier_strategy)
@settings(max_examples=50)
def test_mydsl::function::specifier_instantiation(instance):
    assert isinstance(instance, myDsl::function::specifier)

@given(instance=myDsl::function::specifier_strategy)
def test_mydsl::function::specifier_inline_type(instance):
    assert isinstance(instance.inline, str)


@given(instance=myDsl::function::specifier_strategy)
def test_mydsl::function::specifier_inline_setter(instance):
    original = instance.inline
    instance.inline = original
    assert instance.inline == original

@given(instance=myDsl::function::specifier_strategy)
def test_mydsl::function::specifier_noreturn_type(instance):
    assert isinstance(instance.noreturn, str)


@given(instance=myDsl::function::specifier_strategy)
def test_mydsl::function::specifier_noreturn_setter(instance):
    original = instance.noreturn
    instance.noreturn = original
    assert instance.noreturn == original

@given(instance=myDsl::type::qualifier_strategy)
@settings(max_examples=50)
def test_mydsl::type::qualifier_instantiation(instance):
    assert isinstance(instance, myDsl::type::qualifier)

@given(instance=myDsl::type::qualifier_strategy)
def test_mydsl::type::qualifier_restrict_type(instance):
    assert isinstance(instance.restrict, str)


@given(instance=myDsl::type::qualifier_strategy)
def test_mydsl::type::qualifier_restrict_setter(instance):
    original = instance.restrict
    instance.restrict = original
    assert instance.restrict == original

@given(instance=myDsl::type::qualifier_strategy)
def test_mydsl::type::qualifier_atomic_type(instance):
    assert isinstance(instance.atomic, str)


@given(instance=myDsl::type::qualifier_strategy)
def test_mydsl::type::qualifier_atomic_setter(instance):
    original = instance.atomic
    instance.atomic = original
    assert instance.atomic == original

@given(instance=myDsl::type::qualifier_strategy)
def test_mydsl::type::qualifier_volatile_type(instance):
    assert isinstance(instance.volatile, str)


@given(instance=myDsl::type::qualifier_strategy)
def test_mydsl::type::qualifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original

@given(instance=myDsl::type::qualifier_strategy)
def test_mydsl::type::qualifier_const_type(instance):
    assert isinstance(instance.const, str)


@given(instance=myDsl::type::qualifier_strategy)
def test_mydsl::type::qualifier_const_setter(instance):
    original = instance.const
    instance.const = original
    assert instance.const == original

@given(instance=myDsl::type::specifier_strategy)
@settings(max_examples=50)
def test_mydsl::type::specifier_instantiation(instance):
    assert isinstance(instance, myDsl::type::specifier)

@given(instance=myDsl::type::specifier_strategy)
def test_mydsl::type::specifier_typedef_name_type(instance):
    assert isinstance(instance.typedef_name, str)


@given(instance=myDsl::type::specifier_strategy)
def test_mydsl::type::specifier_typedef_name_setter(instance):
    original = instance.typedef_name
    instance.typedef_name = original
    assert instance.typedef_name == original

@given(instance=myDsl::storage::class::specifier_strategy)
@settings(max_examples=50)
def test_mydsl::storage::class::specifier_instantiation(instance):
    assert isinstance(instance, myDsl::storage::class::specifier)

@given(instance=myDsl::storage::class::specifier_strategy)
def test_mydsl::storage::class::specifier_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=myDsl::storage::class::specifier_strategy)
def test_mydsl::storage::class::specifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=myDsl::storage::class::specifier_strategy)
def test_mydsl::storage::class::specifier_register_type(instance):
    assert isinstance(instance.register, str)


@given(instance=myDsl::storage::class::specifier_strategy)
def test_mydsl::storage::class::specifier_register_setter(instance):
    original = instance.register
    instance.register = original
    assert instance.register == original

@given(instance=myDsl::storage::class::specifier_strategy)
def test_mydsl::storage::class::specifier_auto_type(instance):
    assert isinstance(instance.auto, str)


@given(instance=myDsl::storage::class::specifier_strategy)
def test_mydsl::storage::class::specifier_auto_setter(instance):
    original = instance.auto
    instance.auto = original
    assert instance.auto == original

@given(instance=myDsl::storage::class::specifier_strategy)
def test_mydsl::storage::class::specifier_typedef_type(instance):
    assert isinstance(instance.typedef, str)


@given(instance=myDsl::storage::class::specifier_strategy)
def test_mydsl::storage::class::specifier_typedef_setter(instance):
    original = instance.typedef
    instance.typedef = original
    assert instance.typedef == original

@given(instance=myDsl::storage::class::specifier_strategy)
def test_mydsl::storage::class::specifier_thread_local_type(instance):
    assert isinstance(instance.thread_local, str)


@given(instance=myDsl::storage::class::specifier_strategy)
def test_mydsl::storage::class::specifier_thread_local_setter(instance):
    original = instance.thread_local
    instance.thread_local = original
    assert instance.thread_local == original

@given(instance=myDsl::storage::class::specifier_strategy)
def test_mydsl::storage::class::specifier_extern_type(instance):
    assert isinstance(instance.extern, str)


@given(instance=myDsl::storage::class::specifier_strategy)
def test_mydsl::storage::class::specifier_extern_setter(instance):
    original = instance.extern
    instance.extern = original
    assert instance.extern == original

@given(instance=myDsl::static::assert::declaration_strategy)
@settings(max_examples=50)
def test_mydsl::static::assert::declaration_instantiation(instance):
    assert isinstance(instance, myDsl::static::assert::declaration)

@given(instance=myDsl::static::assert::declaration_strategy)
def test_mydsl::static::assert::declaration_string_literal_type(instance):
    assert isinstance(instance.string_literal, str)


@given(instance=myDsl::static::assert::declaration_strategy)
def test_mydsl::static::assert::declaration_string_literal_setter(instance):
    original = instance.string_literal
    instance.string_literal = original
    assert instance.string_literal == original

@given(instance=myDsl::static::assert::declaration_strategy)
def test_mydsl::static::assert::declaration_static_assert_type(instance):
    assert isinstance(instance.static_assert, str)


@given(instance=myDsl::static::assert::declaration_strategy)
def test_mydsl::static::assert::declaration_static_assert_setter(instance):
    original = instance.static_assert
    instance.static_assert = original
    assert instance.static_assert == original

@given(instance=myDsl::init::declarator::list_strategy)
@settings(max_examples=50)
def test_mydsl::init::declarator::list_instantiation(instance):
    assert isinstance(instance, myDsl::init::declarator::list)

@given(instance=simple::expression_strategy)
@settings(max_examples=50)
def test_simple::expression_instantiation(instance):
    assert isinstance(instance, simple::expression)

@given(instance=myDsl::floatType_strategy)
@settings(max_examples=50)
def test_mydsl::floattype_instantiation(instance):
    assert isinstance(instance, myDsl::floatType)

@given(instance=myDsl::floatType_strategy)
def test_mydsl::floattype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=myDsl::floatType_strategy)
def test_mydsl::floattype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl::floatType_strategy)
def test_mydsl::floattype_float_type_type(instance):
    assert isinstance(instance.float_type, str)


@given(instance=myDsl::floatType_strategy)
def test_mydsl::floattype_float_type_setter(instance):
    original = instance.float_type
    instance.float_type = original
    assert instance.float_type == original

@given(instance=myDsl::INC::OR_strategy)
@settings(max_examples=50)
def test_mydsl::inc::or_instantiation(instance):
    assert isinstance(instance, myDsl::INC::OR)

@given(instance=myDsl::intType_strategy)
@settings(max_examples=50)
def test_mydsl::inttype_instantiation(instance):
    assert isinstance(instance, myDsl::intType)

@given(instance=myDsl::intType_strategy)
def test_mydsl::inttype_int_type_type(instance):
    assert isinstance(instance.int_type, str)


@given(instance=myDsl::intType_strategy)
def test_mydsl::inttype_int_type_setter(instance):
    original = instance.int_type
    instance.int_type = original
    assert instance.int_type == original

@given(instance=myDsl::intType_strategy)
def test_mydsl::inttype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=myDsl::intType_strategy)
def test_mydsl::inttype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl::variableRef_strategy)
@settings(max_examples=50)
def test_mydsl::variableref_instantiation(instance):
    assert isinstance(instance, myDsl::variableRef)

@given(instance=myDsl::variableRef_strategy)
def test_mydsl::variableref_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=myDsl::variableRef_strategy)
def test_mydsl::variableref_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=myDsl::LOG::AND_strategy)
@settings(max_examples=50)
def test_mydsl::log::and_instantiation(instance):
    assert isinstance(instance, myDsl::LOG::AND)

@given(instance=myDsl::EQL_strategy)
@settings(max_examples=50)
def test_mydsl::eql_instantiation(instance):
    assert isinstance(instance, myDsl::EQL)

@given(instance=myDsl::EQL_strategy)
def test_mydsl::eql_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=myDsl::EQL_strategy)
def test_mydsl::eql_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=myDsl::stringType_strategy)
@settings(max_examples=50)
def test_mydsl::stringtype_instantiation(instance):
    assert isinstance(instance, myDsl::stringType)

@given(instance=myDsl::EXC::OR_strategy)
@settings(max_examples=50)
def test_mydsl::exc::or_instantiation(instance):
    assert isinstance(instance, myDsl::EXC::OR)

@given(instance=myDsl::ADD_strategy)
@settings(max_examples=50)
def test_mydsl::add_instantiation(instance):
    assert isinstance(instance, myDsl::ADD)

@given(instance=myDsl::booleanType_strategy)
@settings(max_examples=50)
def test_mydsl::booleantype_instantiation(instance):
    assert isinstance(instance, myDsl::booleanType)

@given(instance=myDsl::booleanType_strategy)
def test_mydsl::booleantype_bool_type_type(instance):
    assert isinstance(instance.bool_type, str)


@given(instance=myDsl::booleanType_strategy)
def test_mydsl::booleantype_bool_type_setter(instance):
    original = instance.bool_type
    instance.bool_type = original
    assert instance.bool_type == original

@given(instance=myDsl::booleanType_strategy)
def test_mydsl::booleantype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=myDsl::booleanType_strategy)
def test_mydsl::booleantype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl::MINUS_strategy)
@settings(max_examples=50)
def test_mydsl::minus_instantiation(instance):
    assert isinstance(instance, myDsl::MINUS)

@given(instance=myDsl::LOG::OR_strategy)
@settings(max_examples=50)
def test_mydsl::log::or_instantiation(instance):
    assert isinstance(instance, myDsl::LOG::OR)

@given(instance=myDsl::MUL_strategy)
@settings(max_examples=50)
def test_mydsl::mul_instantiation(instance):
    assert isinstance(instance, myDsl::MUL)

@given(instance=myDsl::MUL_strategy)
def test_mydsl::mul_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=myDsl::MUL_strategy)
def test_mydsl::mul_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=myDsl::AND_strategy)
@settings(max_examples=50)
def test_mydsl::and_instantiation(instance):
    assert isinstance(instance, myDsl::AND)

@given(instance=myDsl::SHF_strategy)
@settings(max_examples=50)
def test_mydsl::shf_instantiation(instance):
    assert isinstance(instance, myDsl::SHF)

@given(instance=myDsl::SHF_strategy)
def test_mydsl::shf_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=myDsl::SHF_strategy)
def test_mydsl::shf_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=myDsl::REL_strategy)
@settings(max_examples=50)
def test_mydsl::rel_instantiation(instance):
    assert isinstance(instance, myDsl::REL)

@given(instance=myDsl::REL_strategy)
def test_mydsl::rel_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=myDsl::REL_strategy)
def test_mydsl::rel_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=myDsl::unary::expression_strategy)
@settings(max_examples=50)
def test_mydsl::unary::expression_instantiation(instance):
    assert isinstance(instance, myDsl::unary::expression)

@given(instance=myDsl::unary::expression_strategy)
def test_mydsl::unary::expression_alignof_type(instance):
    assert isinstance(instance.alignof, str)


@given(instance=myDsl::unary::expression_strategy)
def test_mydsl::unary::expression_alignof_setter(instance):
    original = instance.alignof
    instance.alignof = original
    assert instance.alignof == original

@given(instance=myDsl::unary::expression_strategy)
def test_mydsl::unary::expression_inc_op_type(instance):
    assert isinstance(instance.inc_op, str)


@given(instance=myDsl::unary::expression_strategy)
def test_mydsl::unary::expression_inc_op_setter(instance):
    original = instance.inc_op
    instance.inc_op = original
    assert instance.inc_op == original

@given(instance=myDsl::unary::expression_strategy)
def test_mydsl::unary::expression_dec_op_type(instance):
    assert isinstance(instance.dec_op, str)


@given(instance=myDsl::unary::expression_strategy)
def test_mydsl::unary::expression_dec_op_setter(instance):
    original = instance.dec_op
    instance.dec_op = original
    assert instance.dec_op == original

@given(instance=myDsl::unary::expression_strategy)
def test_mydsl::unary::expression_sizeof_type(instance):
    assert isinstance(instance.sizeof, str)


@given(instance=myDsl::unary::expression_strategy)
def test_mydsl::unary::expression_sizeof_setter(instance):
    original = instance.sizeof
    instance.sizeof = original
    assert instance.sizeof == original

@given(instance=myDsl::unary::expression_strategy)
def test_mydsl::unary::expression_unary_operator_type(instance):
    assert isinstance(instance.unary_operator, str)


@given(instance=myDsl::unary::expression_strategy)
def test_mydsl::unary::expression_unary_operator_setter(instance):
    original = instance.unary_operator
    instance.unary_operator = original
    assert instance.unary_operator == original

@given(instance=postfix::expression2_strategy)
@settings(max_examples=50)
def test_postfix::expression2_instantiation(instance):
    assert isinstance(instance, postfix::expression2)

@given(instance=myDsl::argument::expression::list_strategy)
@settings(max_examples=50)
def test_mydsl::argument::expression::list_instantiation(instance):
    assert isinstance(instance, myDsl::argument::expression::list)

@given(instance=myDsl::initializer::list_strategy)
@settings(max_examples=50)
def test_mydsl::initializer::list_instantiation(instance):
    assert isinstance(instance, myDsl::initializer::list)

@given(instance=myDsl::postfix::expression2_strategy)
@settings(max_examples=50)
def test_mydsl::postfix::expression2_instantiation(instance):
    assert isinstance(instance, myDsl::postfix::expression2)

@given(instance=myDsl::postfix::expression_strategy)
@settings(max_examples=50)
def test_mydsl::postfix::expression_instantiation(instance):
    assert isinstance(instance, myDsl::postfix::expression)

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

@given(instance=myDsl::assignment::expression_strategy)
@settings(max_examples=50)
def test_mydsl::assignment::expression_instantiation(instance):
    assert isinstance(instance, myDsl::assignment::expression)

@given(instance=myDsl::expression_strategy)
@settings(max_examples=50)
def test_mydsl::expression_instantiation(instance):
    assert isinstance(instance, myDsl::expression)

@given(instance=myDsl::conditional::expression_strategy)
@settings(max_examples=50)
def test_mydsl::conditional::expression_instantiation(instance):
    assert isinstance(instance, myDsl::conditional::expression)

@given(instance=myDsl::constant_strategy)
@settings(max_examples=50)
def test_mydsl::constant_instantiation(instance):
    assert isinstance(instance, myDsl::constant)

@given(instance=myDsl::constant_strategy)
def test_mydsl::constant_enumt_type(instance):
    assert isinstance(instance.enumt, str)


@given(instance=myDsl::constant_strategy)
def test_mydsl::constant_enumt_setter(instance):
    original = instance.enumt
    instance.enumt = original
    assert instance.enumt == original

@given(instance=myDsl::constant_strategy)
def test_mydsl::constant_i_constant_type(instance):
    assert isinstance(instance.i_constant, str)


@given(instance=myDsl::constant_strategy)
def test_mydsl::constant_i_constant_setter(instance):
    original = instance.i_constant
    instance.i_constant = original
    assert instance.i_constant == original

@given(instance=myDsl::constant_strategy)
def test_mydsl::constant_f_constant_type(instance):
    assert isinstance(instance.f_constant, str)


@given(instance=myDsl::constant_strategy)
def test_mydsl::constant_f_constant_setter(instance):
    original = instance.f_constant
    instance.f_constant = original
    assert instance.f_constant == original

@given(instance=myDsl::type::name_strategy)
@settings(max_examples=50)
def test_mydsl::type::name_instantiation(instance):
    assert isinstance(instance, myDsl::type::name)

@given(instance=myDsl::simple::expression_strategy)
@settings(max_examples=50)
def test_mydsl::simple::expression_instantiation(instance):
    assert isinstance(instance, myDsl::simple::expression)

@given(instance=myDsl::translation::unit_strategy)
@settings(max_examples=50)
def test_mydsl::translation::unit_instantiation(instance):
    assert isinstance(instance, myDsl::translation::unit)

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)

@given(instance=myDsl::generic::selection_strategy)
@settings(max_examples=50)
def test_mydsl::generic::selection_instantiation(instance):
    assert isinstance(instance, myDsl::generic::selection)

@given(instance=myDsl::generic::selection_strategy)
def test_mydsl::generic::selection_generic_type(instance):
    assert isinstance(instance.generic, str)


@given(instance=myDsl::generic::selection_strategy)
def test_mydsl::generic::selection_generic_setter(instance):
    original = instance.generic
    instance.generic = original
    assert instance.generic == original

@given(instance=myDsl::string::nova_strategy)
@settings(max_examples=50)
def test_mydsl::string::nova_instantiation(instance):
    assert isinstance(instance, myDsl::string::nova)

@given(instance=myDsl::string::nova_strategy)
def test_mydsl::string::nova_func_name_type(instance):
    assert isinstance(instance.func_name, str)


@given(instance=myDsl::string::nova_strategy)
def test_mydsl::string::nova_func_name_setter(instance):
    original = instance.func_name
    instance.func_name = original
    assert instance.func_name == original

@given(instance=myDsl::string::nova_strategy)
def test_mydsl::string::nova_string_literal_type(instance):
    assert isinstance(instance.string_literal, str)


@given(instance=myDsl::string::nova_strategy)
def test_mydsl::string::nova_string_literal_setter(instance):
    original = instance.string_literal
    instance.string_literal = original
    assert instance.string_literal == original

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

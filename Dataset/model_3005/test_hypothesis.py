import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    miniJava::Null,
    miniJava::SymbolRef,
    miniJava::IntConstant,
    miniJava::Division,
    miniJava::ArrayAccess,
    miniJava::This,
    miniJava::Equality,
    miniJava::BoolConstant,
    miniJava::FieldAccess,
    miniJava::StringConstant,
    miniJava::Super,
    miniJava::ArrayLength,
    miniJava::Inequality,
    miniJava::Multiplication,
    miniJava::MethodCall,
    miniJava::And,
    miniJava::Neg,
    miniJava::Minus,
    miniJava::NewObject,
    miniJava::Not,
    miniJava::NewArray,
    miniJava::Or,
    miniJava::Plus,
    miniJava::Inferior,
    miniJava::Superior,
    miniJava::InferiorOrEqual,
    miniJava::SuperiorOrEqual,
    miniJava::TypeRef,
    miniJava::Assignee,
    Assignee,
    miniJava::NamedElement,
    SingleTypeRef,
    miniJava::StringTypeRef,
    miniJava::IntegerTypeRef,
    miniJava::VoidTypeRef,
    miniJava::BooleanTypeRef,
    miniJava::ClassRef,
    TypeRef,
    miniJava::ArrayTypeRef,
    miniJava::SingleTypeRef,
    TypeDeclaration,
    miniJava::Class,
    miniJava::Interface,
    NamedElement,
    miniJava::TypedDeclaration,
    miniJava::TypeDeclaration,
    miniJava::Import,
    miniJava::Statement,
    Statement,
    miniJava::PrintStatement,
    miniJava::ForStatement,
    miniJava::IfStatement,
    miniJava::Return,
    miniJava::WhileStatement,
    miniJava::Assignment,
    miniJava::Expression,
    Symbol,
    miniJava::VariableDeclaration,
    miniJava::Block,
    miniJava::Parameter,
    Member,
    miniJava::Field,
    miniJava::Method,
    TypedDeclaration,
    miniJava::Member,
    miniJava::Symbol,
    miniJava::Program,
    AccessLevel,
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



def test_minijava::null_is_not_abstract():
    assert not inspect.isabstract(miniJava::Null)


def test_minijava::null_constructor_exists():
    assert callable(miniJava::Null.__init__)


def test_minijava::null_constructor_args():
    sig = inspect.signature(miniJava::Null.__init__)
    params = list(sig.parameters.keys())



def test_minijava::symbolref_is_not_abstract():
    assert not inspect.isabstract(miniJava::SymbolRef)


def test_minijava::symbolref_constructor_exists():
    assert callable(miniJava::SymbolRef.__init__)


def test_minijava::symbolref_constructor_args():
    sig = inspect.signature(miniJava::SymbolRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava::intconstant_is_not_abstract():
    assert not inspect.isabstract(miniJava::IntConstant)


def test_minijava::intconstant_constructor_exists():
    assert callable(miniJava::IntConstant.__init__)


def test_minijava::intconstant_constructor_args():
    sig = inspect.signature(miniJava::IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minijava::intconstant_has_value():
    assert hasattr(miniJava::IntConstant, "value")
    descriptor = None
    for klass in miniJava::IntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minijava::division_is_not_abstract():
    assert not inspect.isabstract(miniJava::Division)


def test_minijava::division_constructor_exists():
    assert callable(miniJava::Division.__init__)


def test_minijava::division_constructor_args():
    sig = inspect.signature(miniJava::Division.__init__)
    params = list(sig.parameters.keys())



def test_minijava::arrayaccess_is_not_abstract():
    assert not inspect.isabstract(miniJava::ArrayAccess)


def test_minijava::arrayaccess_constructor_exists():
    assert callable(miniJava::ArrayAccess.__init__)


def test_minijava::arrayaccess_constructor_args():
    sig = inspect.signature(miniJava::ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_minijava::this_is_not_abstract():
    assert not inspect.isabstract(miniJava::This)


def test_minijava::this_constructor_exists():
    assert callable(miniJava::This.__init__)


def test_minijava::this_constructor_args():
    sig = inspect.signature(miniJava::This.__init__)
    params = list(sig.parameters.keys())



def test_minijava::equality_is_not_abstract():
    assert not inspect.isabstract(miniJava::Equality)


def test_minijava::equality_constructor_exists():
    assert callable(miniJava::Equality.__init__)


def test_minijava::equality_constructor_args():
    sig = inspect.signature(miniJava::Equality.__init__)
    params = list(sig.parameters.keys())



def test_minijava::boolconstant_is_not_abstract():
    assert not inspect.isabstract(miniJava::BoolConstant)


def test_minijava::boolconstant_constructor_exists():
    assert callable(miniJava::BoolConstant.__init__)


def test_minijava::boolconstant_constructor_args():
    sig = inspect.signature(miniJava::BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minijava::boolconstant_has_value():
    assert hasattr(miniJava::BoolConstant, "value")
    descriptor = None
    for klass in miniJava::BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minijava::fieldaccess_is_not_abstract():
    assert not inspect.isabstract(miniJava::FieldAccess)


def test_minijava::fieldaccess_constructor_exists():
    assert callable(miniJava::FieldAccess.__init__)


def test_minijava::fieldaccess_constructor_args():
    sig = inspect.signature(miniJava::FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_minijava::stringconstant_is_not_abstract():
    assert not inspect.isabstract(miniJava::StringConstant)


def test_minijava::stringconstant_constructor_exists():
    assert callable(miniJava::StringConstant.__init__)


def test_minijava::stringconstant_constructor_args():
    sig = inspect.signature(miniJava::StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minijava::stringconstant_has_value():
    assert hasattr(miniJava::StringConstant, "value")
    descriptor = None
    for klass in miniJava::StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minijava::super_is_not_abstract():
    assert not inspect.isabstract(miniJava::Super)


def test_minijava::super_constructor_exists():
    assert callable(miniJava::Super.__init__)


def test_minijava::super_constructor_args():
    sig = inspect.signature(miniJava::Super.__init__)
    params = list(sig.parameters.keys())



def test_minijava::arraylength_is_not_abstract():
    assert not inspect.isabstract(miniJava::ArrayLength)


def test_minijava::arraylength_constructor_exists():
    assert callable(miniJava::ArrayLength.__init__)


def test_minijava::arraylength_constructor_args():
    sig = inspect.signature(miniJava::ArrayLength.__init__)
    params = list(sig.parameters.keys())



def test_minijava::inequality_is_not_abstract():
    assert not inspect.isabstract(miniJava::Inequality)


def test_minijava::inequality_constructor_exists():
    assert callable(miniJava::Inequality.__init__)


def test_minijava::inequality_constructor_args():
    sig = inspect.signature(miniJava::Inequality.__init__)
    params = list(sig.parameters.keys())



def test_minijava::multiplication_is_not_abstract():
    assert not inspect.isabstract(miniJava::Multiplication)


def test_minijava::multiplication_constructor_exists():
    assert callable(miniJava::Multiplication.__init__)


def test_minijava::multiplication_constructor_args():
    sig = inspect.signature(miniJava::Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_minijava::methodcall_is_not_abstract():
    assert not inspect.isabstract(miniJava::MethodCall)


def test_minijava::methodcall_constructor_exists():
    assert callable(miniJava::MethodCall.__init__)


def test_minijava::methodcall_constructor_args():
    sig = inspect.signature(miniJava::MethodCall.__init__)
    params = list(sig.parameters.keys())



def test_minijava::and_is_not_abstract():
    assert not inspect.isabstract(miniJava::And)


def test_minijava::and_constructor_exists():
    assert callable(miniJava::And.__init__)


def test_minijava::and_constructor_args():
    sig = inspect.signature(miniJava::And.__init__)
    params = list(sig.parameters.keys())



def test_minijava::neg_is_not_abstract():
    assert not inspect.isabstract(miniJava::Neg)


def test_minijava::neg_constructor_exists():
    assert callable(miniJava::Neg.__init__)


def test_minijava::neg_constructor_args():
    sig = inspect.signature(miniJava::Neg.__init__)
    params = list(sig.parameters.keys())



def test_minijava::minus_is_not_abstract():
    assert not inspect.isabstract(miniJava::Minus)


def test_minijava::minus_constructor_exists():
    assert callable(miniJava::Minus.__init__)


def test_minijava::minus_constructor_args():
    sig = inspect.signature(miniJava::Minus.__init__)
    params = list(sig.parameters.keys())



def test_minijava::newobject_is_not_abstract():
    assert not inspect.isabstract(miniJava::NewObject)


def test_minijava::newobject_constructor_exists():
    assert callable(miniJava::NewObject.__init__)


def test_minijava::newobject_constructor_args():
    sig = inspect.signature(miniJava::NewObject.__init__)
    params = list(sig.parameters.keys())



def test_minijava::not_is_not_abstract():
    assert not inspect.isabstract(miniJava::Not)


def test_minijava::not_constructor_exists():
    assert callable(miniJava::Not.__init__)


def test_minijava::not_constructor_args():
    sig = inspect.signature(miniJava::Not.__init__)
    params = list(sig.parameters.keys())



def test_minijava::newarray_is_not_abstract():
    assert not inspect.isabstract(miniJava::NewArray)


def test_minijava::newarray_constructor_exists():
    assert callable(miniJava::NewArray.__init__)


def test_minijava::newarray_constructor_args():
    sig = inspect.signature(miniJava::NewArray.__init__)
    params = list(sig.parameters.keys())



def test_minijava::or_is_not_abstract():
    assert not inspect.isabstract(miniJava::Or)


def test_minijava::or_constructor_exists():
    assert callable(miniJava::Or.__init__)


def test_minijava::or_constructor_args():
    sig = inspect.signature(miniJava::Or.__init__)
    params = list(sig.parameters.keys())



def test_minijava::plus_is_not_abstract():
    assert not inspect.isabstract(miniJava::Plus)


def test_minijava::plus_constructor_exists():
    assert callable(miniJava::Plus.__init__)


def test_minijava::plus_constructor_args():
    sig = inspect.signature(miniJava::Plus.__init__)
    params = list(sig.parameters.keys())



def test_minijava::inferior_is_not_abstract():
    assert not inspect.isabstract(miniJava::Inferior)


def test_minijava::inferior_constructor_exists():
    assert callable(miniJava::Inferior.__init__)


def test_minijava::inferior_constructor_args():
    sig = inspect.signature(miniJava::Inferior.__init__)
    params = list(sig.parameters.keys())



def test_minijava::superior_is_not_abstract():
    assert not inspect.isabstract(miniJava::Superior)


def test_minijava::superior_constructor_exists():
    assert callable(miniJava::Superior.__init__)


def test_minijava::superior_constructor_args():
    sig = inspect.signature(miniJava::Superior.__init__)
    params = list(sig.parameters.keys())



def test_minijava::inferiororequal_is_not_abstract():
    assert not inspect.isabstract(miniJava::InferiorOrEqual)


def test_minijava::inferiororequal_constructor_exists():
    assert callable(miniJava::InferiorOrEqual.__init__)


def test_minijava::inferiororequal_constructor_args():
    sig = inspect.signature(miniJava::InferiorOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_minijava::superiororequal_is_not_abstract():
    assert not inspect.isabstract(miniJava::SuperiorOrEqual)


def test_minijava::superiororequal_constructor_exists():
    assert callable(miniJava::SuperiorOrEqual.__init__)


def test_minijava::superiororequal_constructor_args():
    sig = inspect.signature(miniJava::SuperiorOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_minijava::typeref_is_not_abstract():
    assert not inspect.isabstract(miniJava::TypeRef)


def test_minijava::typeref_constructor_exists():
    assert callable(miniJava::TypeRef.__init__)


def test_minijava::typeref_constructor_args():
    sig = inspect.signature(miniJava::TypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava::assignee_is_not_abstract():
    assert not inspect.isabstract(miniJava::Assignee)


def test_minijava::assignee_constructor_exists():
    assert callable(miniJava::Assignee.__init__)


def test_minijava::assignee_constructor_args():
    sig = inspect.signature(miniJava::Assignee.__init__)
    params = list(sig.parameters.keys())



def test_assignee_is_not_abstract():
    assert not inspect.isabstract(Assignee)


def test_assignee_constructor_exists():
    assert callable(Assignee.__init__)


def test_assignee_constructor_args():
    sig = inspect.signature(Assignee.__init__)
    params = list(sig.parameters.keys())



def test_minijava::namedelement_is_not_abstract():
    assert not inspect.isabstract(miniJava::NamedElement)


def test_minijava::namedelement_constructor_exists():
    assert callable(miniJava::NamedElement.__init__)


def test_minijava::namedelement_constructor_args():
    sig = inspect.signature(miniJava::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minijava::namedelement_has_name():
    assert hasattr(miniJava::NamedElement, "name")
    descriptor = None
    for klass in miniJava::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_singletyperef_is_not_abstract():
    assert not inspect.isabstract(SingleTypeRef)


def test_singletyperef_constructor_exists():
    assert callable(SingleTypeRef.__init__)


def test_singletyperef_constructor_args():
    sig = inspect.signature(SingleTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava::stringtyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava::StringTypeRef)


def test_minijava::stringtyperef_constructor_exists():
    assert callable(miniJava::StringTypeRef.__init__)


def test_minijava::stringtyperef_constructor_args():
    sig = inspect.signature(miniJava::StringTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava::integertyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava::IntegerTypeRef)


def test_minijava::integertyperef_constructor_exists():
    assert callable(miniJava::IntegerTypeRef.__init__)


def test_minijava::integertyperef_constructor_args():
    sig = inspect.signature(miniJava::IntegerTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava::voidtyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava::VoidTypeRef)


def test_minijava::voidtyperef_constructor_exists():
    assert callable(miniJava::VoidTypeRef.__init__)


def test_minijava::voidtyperef_constructor_args():
    sig = inspect.signature(miniJava::VoidTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava::booleantyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava::BooleanTypeRef)


def test_minijava::booleantyperef_constructor_exists():
    assert callable(miniJava::BooleanTypeRef.__init__)


def test_minijava::booleantyperef_constructor_args():
    sig = inspect.signature(miniJava::BooleanTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava::classref_is_not_abstract():
    assert not inspect.isabstract(miniJava::ClassRef)


def test_minijava::classref_constructor_exists():
    assert callable(miniJava::ClassRef.__init__)


def test_minijava::classref_constructor_args():
    sig = inspect.signature(miniJava::ClassRef.__init__)
    params = list(sig.parameters.keys())



def test_typeref_is_not_abstract():
    assert not inspect.isabstract(TypeRef)


def test_typeref_constructor_exists():
    assert callable(TypeRef.__init__)


def test_typeref_constructor_args():
    sig = inspect.signature(TypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava::arraytyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava::ArrayTypeRef)


def test_minijava::arraytyperef_constructor_exists():
    assert callable(miniJava::ArrayTypeRef.__init__)


def test_minijava::arraytyperef_constructor_args():
    sig = inspect.signature(miniJava::ArrayTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava::singletyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava::SingleTypeRef)


def test_minijava::singletyperef_constructor_exists():
    assert callable(miniJava::SingleTypeRef.__init__)


def test_minijava::singletyperef_constructor_args():
    sig = inspect.signature(miniJava::SingleTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_minijava::class_is_not_abstract():
    assert not inspect.isabstract(miniJava::Class)


def test_minijava::class_constructor_exists():
    assert callable(miniJava::Class.__init__)


def test_minijava::class_constructor_args():
    sig = inspect.signature(miniJava::Class.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_minijava::class_has_abstract():
    assert hasattr(miniJava::Class, "abstract")
    descriptor = None
    for klass in miniJava::Class.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_minijava::interface_is_not_abstract():
    assert not inspect.isabstract(miniJava::Interface)


def test_minijava::interface_constructor_exists():
    assert callable(miniJava::Interface.__init__)


def test_minijava::interface_constructor_args():
    sig = inspect.signature(miniJava::Interface.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_minijava::typeddeclaration_is_not_abstract():
    assert not inspect.isabstract(miniJava::TypedDeclaration)


def test_minijava::typeddeclaration_constructor_exists():
    assert callable(miniJava::TypedDeclaration.__init__)


def test_minijava::typeddeclaration_constructor_args():
    sig = inspect.signature(miniJava::TypedDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_minijava::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(miniJava::TypeDeclaration)


def test_minijava::typedeclaration_constructor_exists():
    assert callable(miniJava::TypeDeclaration.__init__)


def test_minijava::typedeclaration_constructor_args():
    sig = inspect.signature(miniJava::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "accessLevel" in params, "Missing parameter 'accessLevel'"

def test_minijava::typedeclaration_has_accessLevel():
    assert hasattr(miniJava::TypeDeclaration, "accessLevel")
    descriptor = None
    for klass in miniJava::TypeDeclaration.__mro__:
        if "accessLevel" in klass.__dict__:
            descriptor = klass.__dict__["accessLevel"]
            break
    assert isinstance(descriptor, property)



def test_minijava::import_is_not_abstract():
    assert not inspect.isabstract(miniJava::Import)


def test_minijava::import_constructor_exists():
    assert callable(miniJava::Import.__init__)


def test_minijava::import_constructor_args():
    sig = inspect.signature(miniJava::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_minijava::import_has_importedNamespace():
    assert hasattr(miniJava::Import, "importedNamespace")
    descriptor = None
    for klass in miniJava::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_minijava::statement_is_not_abstract():
    assert not inspect.isabstract(miniJava::Statement)


def test_minijava::statement_constructor_exists():
    assert callable(miniJava::Statement.__init__)


def test_minijava::statement_constructor_args():
    sig = inspect.signature(miniJava::Statement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_minijava::printstatement_is_not_abstract():
    assert not inspect.isabstract(miniJava::PrintStatement)


def test_minijava::printstatement_constructor_exists():
    assert callable(miniJava::PrintStatement.__init__)


def test_minijava::printstatement_constructor_args():
    sig = inspect.signature(miniJava::PrintStatement.__init__)
    params = list(sig.parameters.keys())



def test_minijava::forstatement_is_not_abstract():
    assert not inspect.isabstract(miniJava::ForStatement)


def test_minijava::forstatement_constructor_exists():
    assert callable(miniJava::ForStatement.__init__)


def test_minijava::forstatement_constructor_args():
    sig = inspect.signature(miniJava::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_minijava::ifstatement_is_not_abstract():
    assert not inspect.isabstract(miniJava::IfStatement)


def test_minijava::ifstatement_constructor_exists():
    assert callable(miniJava::IfStatement.__init__)


def test_minijava::ifstatement_constructor_args():
    sig = inspect.signature(miniJava::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_minijava::return_is_not_abstract():
    assert not inspect.isabstract(miniJava::Return)


def test_minijava::return_constructor_exists():
    assert callable(miniJava::Return.__init__)


def test_minijava::return_constructor_args():
    sig = inspect.signature(miniJava::Return.__init__)
    params = list(sig.parameters.keys())



def test_minijava::whilestatement_is_not_abstract():
    assert not inspect.isabstract(miniJava::WhileStatement)


def test_minijava::whilestatement_constructor_exists():
    assert callable(miniJava::WhileStatement.__init__)


def test_minijava::whilestatement_constructor_args():
    sig = inspect.signature(miniJava::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_minijava::assignment_is_not_abstract():
    assert not inspect.isabstract(miniJava::Assignment)


def test_minijava::assignment_constructor_exists():
    assert callable(miniJava::Assignment.__init__)


def test_minijava::assignment_constructor_args():
    sig = inspect.signature(miniJava::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_minijava::expression_is_not_abstract():
    assert not inspect.isabstract(miniJava::Expression)


def test_minijava::expression_constructor_exists():
    assert callable(miniJava::Expression.__init__)


def test_minijava::expression_constructor_args():
    sig = inspect.signature(miniJava::Expression.__init__)
    params = list(sig.parameters.keys())



def test_symbol_is_not_abstract():
    assert not inspect.isabstract(Symbol)


def test_symbol_constructor_exists():
    assert callable(Symbol.__init__)


def test_symbol_constructor_args():
    sig = inspect.signature(Symbol.__init__)
    params = list(sig.parameters.keys())



def test_minijava::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(miniJava::VariableDeclaration)


def test_minijava::variabledeclaration_constructor_exists():
    assert callable(miniJava::VariableDeclaration.__init__)


def test_minijava::variabledeclaration_constructor_args():
    sig = inspect.signature(miniJava::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_minijava::block_is_not_abstract():
    assert not inspect.isabstract(miniJava::Block)


def test_minijava::block_constructor_exists():
    assert callable(miniJava::Block.__init__)


def test_minijava::block_constructor_args():
    sig = inspect.signature(miniJava::Block.__init__)
    params = list(sig.parameters.keys())



def test_minijava::parameter_is_not_abstract():
    assert not inspect.isabstract(miniJava::Parameter)


def test_minijava::parameter_constructor_exists():
    assert callable(miniJava::Parameter.__init__)


def test_minijava::parameter_constructor_args():
    sig = inspect.signature(miniJava::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_minijava::field_is_not_abstract():
    assert not inspect.isabstract(miniJava::Field)


def test_minijava::field_constructor_exists():
    assert callable(miniJava::Field.__init__)


def test_minijava::field_constructor_args():
    sig = inspect.signature(miniJava::Field.__init__)
    params = list(sig.parameters.keys())



def test_minijava::method_is_not_abstract():
    assert not inspect.isabstract(miniJava::Method)


def test_minijava::method_constructor_exists():
    assert callable(miniJava::Method.__init__)


def test_minijava::method_constructor_args():
    sig = inspect.signature(miniJava::Method.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "static" in params, "Missing parameter 'static'"

def test_minijava::method_has_abstract():
    assert hasattr(miniJava::Method, "abstract")
    descriptor = None
    for klass in miniJava::Method.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_minijava::method_has_static():
    assert hasattr(miniJava::Method, "static")
    descriptor = None
    for klass in miniJava::Method.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_typeddeclaration_is_not_abstract():
    assert not inspect.isabstract(TypedDeclaration)


def test_typeddeclaration_constructor_exists():
    assert callable(TypedDeclaration.__init__)


def test_typeddeclaration_constructor_args():
    sig = inspect.signature(TypedDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_minijava::member_is_not_abstract():
    assert not inspect.isabstract(miniJava::Member)


def test_minijava::member_constructor_exists():
    assert callable(miniJava::Member.__init__)


def test_minijava::member_constructor_args():
    sig = inspect.signature(miniJava::Member.__init__)
    params = list(sig.parameters.keys())
    assert "access" in params, "Missing parameter 'access'"

def test_minijava::member_has_access():
    assert hasattr(miniJava::Member, "access")
    descriptor = None
    for klass in miniJava::Member.__mro__:
        if "access" in klass.__dict__:
            descriptor = klass.__dict__["access"]
            break
    assert isinstance(descriptor, property)



def test_minijava::symbol_is_not_abstract():
    assert not inspect.isabstract(miniJava::Symbol)


def test_minijava::symbol_constructor_exists():
    assert callable(miniJava::Symbol.__init__)


def test_minijava::symbol_constructor_args():
    sig = inspect.signature(miniJava::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_minijava::program_is_not_abstract():
    assert not inspect.isabstract(miniJava::Program)


def test_minijava::program_constructor_exists():
    assert callable(miniJava::Program.__init__)


def test_minijava::program_constructor_args():
    sig = inspect.signature(miniJava::Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minijava::program_has_name():
    assert hasattr(miniJava::Program, "name")
    descriptor = None
    for klass in miniJava::Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_accesslevel_exists():
    # Check that the Enumeration exists
    assert AccessLevel is not None

def test_accesslevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessLevel]
    expected_literals = [
        "PUBLIC",
        "PRIVATE",
        "PROTECTED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessLevel"


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
miniJava::Null_strategy = st.builds(
    miniJava::Null,
)
miniJava::SymbolRef_strategy = st.builds(
    miniJava::SymbolRef,
)
miniJava::IntConstant_strategy = st.builds(
    miniJava::IntConstant,
    value=
        st.integers()
)
miniJava::Division_strategy = st.builds(
    miniJava::Division,
)
miniJava::ArrayAccess_strategy = st.builds(
    miniJava::ArrayAccess,
)
miniJava::This_strategy = st.builds(
    miniJava::This,
)
miniJava::Equality_strategy = st.builds(
    miniJava::Equality,
)
miniJava::BoolConstant_strategy = st.builds(
    miniJava::BoolConstant,
    value=
        safe_text
)
miniJava::FieldAccess_strategy = st.builds(
    miniJava::FieldAccess,
)
miniJava::StringConstant_strategy = st.builds(
    miniJava::StringConstant,
    value=
        safe_text
)
miniJava::Super_strategy = st.builds(
    miniJava::Super,
)
miniJava::ArrayLength_strategy = st.builds(
    miniJava::ArrayLength,
)
miniJava::Inequality_strategy = st.builds(
    miniJava::Inequality,
)
miniJava::Multiplication_strategy = st.builds(
    miniJava::Multiplication,
)
miniJava::MethodCall_strategy = st.builds(
    miniJava::MethodCall,
)
miniJava::And_strategy = st.builds(
    miniJava::And,
)
miniJava::Neg_strategy = st.builds(
    miniJava::Neg,
)
miniJava::Minus_strategy = st.builds(
    miniJava::Minus,
)
miniJava::NewObject_strategy = st.builds(
    miniJava::NewObject,
)
miniJava::Not_strategy = st.builds(
    miniJava::Not,
)
miniJava::NewArray_strategy = st.builds(
    miniJava::NewArray,
)
miniJava::Or_strategy = st.builds(
    miniJava::Or,
)
miniJava::Plus_strategy = st.builds(
    miniJava::Plus,
)
miniJava::Inferior_strategy = st.builds(
    miniJava::Inferior,
)
miniJava::Superior_strategy = st.builds(
    miniJava::Superior,
)
miniJava::InferiorOrEqual_strategy = st.builds(
    miniJava::InferiorOrEqual,
)
miniJava::SuperiorOrEqual_strategy = st.builds(
    miniJava::SuperiorOrEqual,
)
miniJava::TypeRef_strategy = st.builds(
    miniJava::TypeRef,
)
miniJava::Assignee_strategy = st.builds(
    miniJava::Assignee,
)
Assignee_strategy = st.builds(
    Assignee,
)
miniJava::NamedElement_strategy = st.builds(
    miniJava::NamedElement,
    name=
        safe_text
)
SingleTypeRef_strategy = st.builds(
    SingleTypeRef,
)
miniJava::StringTypeRef_strategy = st.builds(
    miniJava::StringTypeRef,
)
miniJava::IntegerTypeRef_strategy = st.builds(
    miniJava::IntegerTypeRef,
)
miniJava::VoidTypeRef_strategy = st.builds(
    miniJava::VoidTypeRef,
)
miniJava::BooleanTypeRef_strategy = st.builds(
    miniJava::BooleanTypeRef,
)
miniJava::ClassRef_strategy = st.builds(
    miniJava::ClassRef,
)
TypeRef_strategy = st.builds(
    TypeRef,
)
miniJava::ArrayTypeRef_strategy = st.builds(
    miniJava::ArrayTypeRef,
)
miniJava::SingleTypeRef_strategy = st.builds(
    miniJava::SingleTypeRef,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
miniJava::Class_strategy = st.builds(
    miniJava::Class,
    abstract=
        st.booleans()
)
miniJava::Interface_strategy = st.builds(
    miniJava::Interface,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
miniJava::TypedDeclaration_strategy = st.builds(
    miniJava::TypedDeclaration,
)
miniJava::TypeDeclaration_strategy = st.builds(
    miniJava::TypeDeclaration,
    accessLevel=
        safe_text
)
miniJava::Import_strategy = st.builds(
    miniJava::Import,
    importedNamespace=
        safe_text
)
miniJava::Statement_strategy = st.builds(
    miniJava::Statement,
)
Statement_strategy = st.builds(
    Statement,
)
miniJava::PrintStatement_strategy = st.builds(
    miniJava::PrintStatement,
)
miniJava::ForStatement_strategy = st.builds(
    miniJava::ForStatement,
)
miniJava::IfStatement_strategy = st.builds(
    miniJava::IfStatement,
)
miniJava::Return_strategy = st.builds(
    miniJava::Return,
)
miniJava::WhileStatement_strategy = st.builds(
    miniJava::WhileStatement,
)
miniJava::Assignment_strategy = st.builds(
    miniJava::Assignment,
)
miniJava::Expression_strategy = st.builds(
    miniJava::Expression,
)
Symbol_strategy = st.builds(
    Symbol,
)
miniJava::VariableDeclaration_strategy = st.builds(
    miniJava::VariableDeclaration,
)
miniJava::Block_strategy = st.builds(
    miniJava::Block,
)
miniJava::Parameter_strategy = st.builds(
    miniJava::Parameter,
)
Member_strategy = st.builds(
    Member,
)
miniJava::Field_strategy = st.builds(
    miniJava::Field,
)
miniJava::Method_strategy = st.builds(
    miniJava::Method,
    abstract=
        st.booleans(),
    static=
        st.booleans()
)
TypedDeclaration_strategy = st.builds(
    TypedDeclaration,
)
miniJava::Member_strategy = st.builds(
    miniJava::Member,
    access=
        safe_text
)
miniJava::Symbol_strategy = st.builds(
    miniJava::Symbol,
)
miniJava::Program_strategy = st.builds(
    miniJava::Program,
    name=
        safe_text
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=miniJava::Null_strategy)
@settings(max_examples=50)
def test_minijava::null_instantiation(instance):
    assert isinstance(instance, miniJava::Null)

@given(instance=miniJava::SymbolRef_strategy)
@settings(max_examples=50)
def test_minijava::symbolref_instantiation(instance):
    assert isinstance(instance, miniJava::SymbolRef)

@given(instance=miniJava::IntConstant_strategy)
@settings(max_examples=50)
def test_minijava::intconstant_instantiation(instance):
    assert isinstance(instance, miniJava::IntConstant)

@given(instance=miniJava::IntConstant_strategy)
def test_minijava::intconstant_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=miniJava::IntConstant_strategy)
def test_minijava::intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=miniJava::Division_strategy)
@settings(max_examples=50)
def test_minijava::division_instantiation(instance):
    assert isinstance(instance, miniJava::Division)

@given(instance=miniJava::ArrayAccess_strategy)
@settings(max_examples=50)
def test_minijava::arrayaccess_instantiation(instance):
    assert isinstance(instance, miniJava::ArrayAccess)

@given(instance=miniJava::This_strategy)
@settings(max_examples=50)
def test_minijava::this_instantiation(instance):
    assert isinstance(instance, miniJava::This)

@given(instance=miniJava::Equality_strategy)
@settings(max_examples=50)
def test_minijava::equality_instantiation(instance):
    assert isinstance(instance, miniJava::Equality)

@given(instance=miniJava::BoolConstant_strategy)
@settings(max_examples=50)
def test_minijava::boolconstant_instantiation(instance):
    assert isinstance(instance, miniJava::BoolConstant)

@given(instance=miniJava::BoolConstant_strategy)
def test_minijava::boolconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=miniJava::BoolConstant_strategy)
def test_minijava::boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=miniJava::FieldAccess_strategy)
@settings(max_examples=50)
def test_minijava::fieldaccess_instantiation(instance):
    assert isinstance(instance, miniJava::FieldAccess)

@given(instance=miniJava::StringConstant_strategy)
@settings(max_examples=50)
def test_minijava::stringconstant_instantiation(instance):
    assert isinstance(instance, miniJava::StringConstant)

@given(instance=miniJava::StringConstant_strategy)
def test_minijava::stringconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=miniJava::StringConstant_strategy)
def test_minijava::stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=miniJava::Super_strategy)
@settings(max_examples=50)
def test_minijava::super_instantiation(instance):
    assert isinstance(instance, miniJava::Super)

@given(instance=miniJava::ArrayLength_strategy)
@settings(max_examples=50)
def test_minijava::arraylength_instantiation(instance):
    assert isinstance(instance, miniJava::ArrayLength)

@given(instance=miniJava::Inequality_strategy)
@settings(max_examples=50)
def test_minijava::inequality_instantiation(instance):
    assert isinstance(instance, miniJava::Inequality)

@given(instance=miniJava::Multiplication_strategy)
@settings(max_examples=50)
def test_minijava::multiplication_instantiation(instance):
    assert isinstance(instance, miniJava::Multiplication)

@given(instance=miniJava::MethodCall_strategy)
@settings(max_examples=50)
def test_minijava::methodcall_instantiation(instance):
    assert isinstance(instance, miniJava::MethodCall)

@given(instance=miniJava::And_strategy)
@settings(max_examples=50)
def test_minijava::and_instantiation(instance):
    assert isinstance(instance, miniJava::And)

@given(instance=miniJava::Neg_strategy)
@settings(max_examples=50)
def test_minijava::neg_instantiation(instance):
    assert isinstance(instance, miniJava::Neg)

@given(instance=miniJava::Minus_strategy)
@settings(max_examples=50)
def test_minijava::minus_instantiation(instance):
    assert isinstance(instance, miniJava::Minus)

@given(instance=miniJava::NewObject_strategy)
@settings(max_examples=50)
def test_minijava::newobject_instantiation(instance):
    assert isinstance(instance, miniJava::NewObject)

@given(instance=miniJava::Not_strategy)
@settings(max_examples=50)
def test_minijava::not_instantiation(instance):
    assert isinstance(instance, miniJava::Not)

@given(instance=miniJava::NewArray_strategy)
@settings(max_examples=50)
def test_minijava::newarray_instantiation(instance):
    assert isinstance(instance, miniJava::NewArray)

@given(instance=miniJava::Or_strategy)
@settings(max_examples=50)
def test_minijava::or_instantiation(instance):
    assert isinstance(instance, miniJava::Or)

@given(instance=miniJava::Plus_strategy)
@settings(max_examples=50)
def test_minijava::plus_instantiation(instance):
    assert isinstance(instance, miniJava::Plus)

@given(instance=miniJava::Inferior_strategy)
@settings(max_examples=50)
def test_minijava::inferior_instantiation(instance):
    assert isinstance(instance, miniJava::Inferior)

@given(instance=miniJava::Superior_strategy)
@settings(max_examples=50)
def test_minijava::superior_instantiation(instance):
    assert isinstance(instance, miniJava::Superior)

@given(instance=miniJava::InferiorOrEqual_strategy)
@settings(max_examples=50)
def test_minijava::inferiororequal_instantiation(instance):
    assert isinstance(instance, miniJava::InferiorOrEqual)

@given(instance=miniJava::SuperiorOrEqual_strategy)
@settings(max_examples=50)
def test_minijava::superiororequal_instantiation(instance):
    assert isinstance(instance, miniJava::SuperiorOrEqual)

@given(instance=miniJava::TypeRef_strategy)
@settings(max_examples=50)
def test_minijava::typeref_instantiation(instance):
    assert isinstance(instance, miniJava::TypeRef)

@given(instance=miniJava::Assignee_strategy)
@settings(max_examples=50)
def test_minijava::assignee_instantiation(instance):
    assert isinstance(instance, miniJava::Assignee)

@given(instance=Assignee_strategy)
@settings(max_examples=50)
def test_assignee_instantiation(instance):
    assert isinstance(instance, Assignee)

@given(instance=miniJava::NamedElement_strategy)
@settings(max_examples=50)
def test_minijava::namedelement_instantiation(instance):
    assert isinstance(instance, miniJava::NamedElement)

@given(instance=miniJava::NamedElement_strategy)
def test_minijava::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=miniJava::NamedElement_strategy)
def test_minijava::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SingleTypeRef_strategy)
@settings(max_examples=50)
def test_singletyperef_instantiation(instance):
    assert isinstance(instance, SingleTypeRef)

@given(instance=miniJava::StringTypeRef_strategy)
@settings(max_examples=50)
def test_minijava::stringtyperef_instantiation(instance):
    assert isinstance(instance, miniJava::StringTypeRef)

@given(instance=miniJava::IntegerTypeRef_strategy)
@settings(max_examples=50)
def test_minijava::integertyperef_instantiation(instance):
    assert isinstance(instance, miniJava::IntegerTypeRef)

@given(instance=miniJava::VoidTypeRef_strategy)
@settings(max_examples=50)
def test_minijava::voidtyperef_instantiation(instance):
    assert isinstance(instance, miniJava::VoidTypeRef)

@given(instance=miniJava::BooleanTypeRef_strategy)
@settings(max_examples=50)
def test_minijava::booleantyperef_instantiation(instance):
    assert isinstance(instance, miniJava::BooleanTypeRef)

@given(instance=miniJava::ClassRef_strategy)
@settings(max_examples=50)
def test_minijava::classref_instantiation(instance):
    assert isinstance(instance, miniJava::ClassRef)

@given(instance=TypeRef_strategy)
@settings(max_examples=50)
def test_typeref_instantiation(instance):
    assert isinstance(instance, TypeRef)

@given(instance=miniJava::ArrayTypeRef_strategy)
@settings(max_examples=50)
def test_minijava::arraytyperef_instantiation(instance):
    assert isinstance(instance, miniJava::ArrayTypeRef)

@given(instance=miniJava::SingleTypeRef_strategy)
@settings(max_examples=50)
def test_minijava::singletyperef_instantiation(instance):
    assert isinstance(instance, miniJava::SingleTypeRef)

@given(instance=TypeDeclaration_strategy)
@settings(max_examples=50)
def test_typedeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)

@given(instance=miniJava::Class_strategy)
@settings(max_examples=50)
def test_minijava::class_instantiation(instance):
    assert isinstance(instance, miniJava::Class)

@given(instance=miniJava::Class_strategy)
def test_minijava::class_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=miniJava::Class_strategy)
def test_minijava::class_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=miniJava::Interface_strategy)
@settings(max_examples=50)
def test_minijava::interface_instantiation(instance):
    assert isinstance(instance, miniJava::Interface)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=miniJava::TypedDeclaration_strategy)
@settings(max_examples=50)
def test_minijava::typeddeclaration_instantiation(instance):
    assert isinstance(instance, miniJava::TypedDeclaration)

@given(instance=miniJava::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_minijava::typedeclaration_instantiation(instance):
    assert isinstance(instance, miniJava::TypeDeclaration)

@given(instance=miniJava::TypeDeclaration_strategy)
def test_minijava::typedeclaration_accessLevel_type(instance):
    assert isinstance(instance.accessLevel, str)


@given(instance=miniJava::TypeDeclaration_strategy)
def test_minijava::typedeclaration_accessLevel_setter(instance):
    original = instance.accessLevel
    instance.accessLevel = original
    assert instance.accessLevel == original

@given(instance=miniJava::Import_strategy)
@settings(max_examples=50)
def test_minijava::import_instantiation(instance):
    assert isinstance(instance, miniJava::Import)

@given(instance=miniJava::Import_strategy)
def test_minijava::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=miniJava::Import_strategy)
def test_minijava::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=miniJava::Statement_strategy)
@settings(max_examples=50)
def test_minijava::statement_instantiation(instance):
    assert isinstance(instance, miniJava::Statement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=miniJava::PrintStatement_strategy)
@settings(max_examples=50)
def test_minijava::printstatement_instantiation(instance):
    assert isinstance(instance, miniJava::PrintStatement)

@given(instance=miniJava::ForStatement_strategy)
@settings(max_examples=50)
def test_minijava::forstatement_instantiation(instance):
    assert isinstance(instance, miniJava::ForStatement)

@given(instance=miniJava::IfStatement_strategy)
@settings(max_examples=50)
def test_minijava::ifstatement_instantiation(instance):
    assert isinstance(instance, miniJava::IfStatement)

@given(instance=miniJava::Return_strategy)
@settings(max_examples=50)
def test_minijava::return_instantiation(instance):
    assert isinstance(instance, miniJava::Return)

@given(instance=miniJava::WhileStatement_strategy)
@settings(max_examples=50)
def test_minijava::whilestatement_instantiation(instance):
    assert isinstance(instance, miniJava::WhileStatement)

@given(instance=miniJava::Assignment_strategy)
@settings(max_examples=50)
def test_minijava::assignment_instantiation(instance):
    assert isinstance(instance, miniJava::Assignment)

@given(instance=miniJava::Expression_strategy)
@settings(max_examples=50)
def test_minijava::expression_instantiation(instance):
    assert isinstance(instance, miniJava::Expression)

@given(instance=Symbol_strategy)
@settings(max_examples=50)
def test_symbol_instantiation(instance):
    assert isinstance(instance, Symbol)

@given(instance=miniJava::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_minijava::variabledeclaration_instantiation(instance):
    assert isinstance(instance, miniJava::VariableDeclaration)

@given(instance=miniJava::Block_strategy)
@settings(max_examples=50)
def test_minijava::block_instantiation(instance):
    assert isinstance(instance, miniJava::Block)

@given(instance=miniJava::Parameter_strategy)
@settings(max_examples=50)
def test_minijava::parameter_instantiation(instance):
    assert isinstance(instance, miniJava::Parameter)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=miniJava::Field_strategy)
@settings(max_examples=50)
def test_minijava::field_instantiation(instance):
    assert isinstance(instance, miniJava::Field)

@given(instance=miniJava::Method_strategy)
@settings(max_examples=50)
def test_minijava::method_instantiation(instance):
    assert isinstance(instance, miniJava::Method)

@given(instance=miniJava::Method_strategy)
def test_minijava::method_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=miniJava::Method_strategy)
def test_minijava::method_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=miniJava::Method_strategy)
def test_minijava::method_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=miniJava::Method_strategy)
def test_minijava::method_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=TypedDeclaration_strategy)
@settings(max_examples=50)
def test_typeddeclaration_instantiation(instance):
    assert isinstance(instance, TypedDeclaration)

@given(instance=miniJava::Member_strategy)
@settings(max_examples=50)
def test_minijava::member_instantiation(instance):
    assert isinstance(instance, miniJava::Member)

@given(instance=miniJava::Member_strategy)
def test_minijava::member_access_type(instance):
    assert isinstance(instance.access, str)


@given(instance=miniJava::Member_strategy)
def test_minijava::member_access_setter(instance):
    original = instance.access
    instance.access = original
    assert instance.access == original

@given(instance=miniJava::Symbol_strategy)
@settings(max_examples=50)
def test_minijava::symbol_instantiation(instance):
    assert isinstance(instance, miniJava::Symbol)

@given(instance=miniJava::Program_strategy)
@settings(max_examples=50)
def test_minijava::program_instantiation(instance):
    assert isinstance(instance, miniJava::Program)

@given(instance=miniJava::Program_strategy)
def test_minijava::program_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=miniJava::Program_strategy)
def test_minijava::program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

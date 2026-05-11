import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    miniJava::TypeRef,
    miniJava::Statement,
    Statement,
    miniJava::Assignment,
    miniJava::ForStatement,
    miniJava::WhileStatement,
    miniJava::Return,
    miniJava::PrintStatement,
    miniJava::IfStatement,
    Symbol,
    miniJava::ClazzToMethodMap,
    miniJava::Block,
    Member,
    miniJava::Field,
    miniJava::Method,
    TypedDeclaration,
    TypeDeclaration,
    miniJava::Clazz,
    miniJava::Member,
    miniJava::Interface,
    NamedElement,
    miniJava::State,
    miniJava::TypeDeclaration,
    miniJava::Import,
    miniJava::Program,
    miniJava::Parameter,
    Call,
    miniJava::MethodCall2,
    miniJava::NewCall,
    miniJava::Call,
    miniJava::ArrayInstance,
    miniJava::ObjectInstance,
    miniJava::Frame,
    miniJava::OutputStream,
    miniJava::FieldBinding,
    Value,
    miniJava::NullValue,
    miniJava::ArrayRefValue,
    miniJava::ObjectRefValue,
    miniJava::StringValue,
    miniJava::IntegerValue,
    miniJava::Value,
    miniJava::SymbolToSymbolBindingMap,
    miniJava::SymbolBinding,
    miniJava::Context,
    miniJava::BooleanValue,
    Expression,
    miniJava::Equality,
    miniJava::Plus,
    miniJava::Inequality,
    miniJava::Not,
    miniJava::Modulo,
    miniJava::SuperiorOrEqual,
    miniJava::This,
    miniJava::ArrayLength,
    miniJava::FieldAccess,
    miniJava::IntConstant,
    miniJava::Multiplication,
    miniJava::BoolConstant,
    miniJava::Inferior,
    miniJava::Null,
    miniJava::SymbolRef,
    miniJava::InferiorOrEqual,
    miniJava::Division,
    miniJava::Super,
    miniJava::StringConstant,
    miniJava::ArrayAccess,
    miniJava::MethodCall,
    miniJava::Superior,
    miniJava::Neg,
    miniJava::And,
    miniJava::Minus,
    miniJava::NewArray,
    miniJava::NewObject,
    miniJava::Or,
    miniJava::Assignee,
    Assignee,
    miniJava::Expression,
    miniJava::VariableDeclaration,
    miniJava::Symbol,
    miniJava::TypedDeclaration,
    miniJava::NamedElement,
    SingleTypeRef,
    miniJava::IntegerTypeRef,
    miniJava::BooleanTypeRef,
    miniJava::VoidTypeRef,
    miniJava::StringTypeRef,
    miniJava::ClassRef,
    TypeRef,
    miniJava::ArrayTypeRef,
    miniJava::SingleTypeRef,
    AccessLevel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_minijava::typeref_is_not_abstract():
    assert not inspect.isabstract(miniJava::TypeRef)


def test_minijava::typeref_constructor_exists():
    assert callable(miniJava::TypeRef.__init__)


def test_minijava::typeref_constructor_args():
    sig = inspect.signature(miniJava::TypeRef.__init__)
    params = list(sig.parameters.keys())



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



def test_minijava::assignment_is_not_abstract():
    assert not inspect.isabstract(miniJava::Assignment)


def test_minijava::assignment_constructor_exists():
    assert callable(miniJava::Assignment.__init__)


def test_minijava::assignment_constructor_args():
    sig = inspect.signature(miniJava::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_minijava::forstatement_is_not_abstract():
    assert not inspect.isabstract(miniJava::ForStatement)


def test_minijava::forstatement_constructor_exists():
    assert callable(miniJava::ForStatement.__init__)


def test_minijava::forstatement_constructor_args():
    sig = inspect.signature(miniJava::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_minijava::whilestatement_is_not_abstract():
    assert not inspect.isabstract(miniJava::WhileStatement)


def test_minijava::whilestatement_constructor_exists():
    assert callable(miniJava::WhileStatement.__init__)


def test_minijava::whilestatement_constructor_args():
    sig = inspect.signature(miniJava::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_minijava::return_is_not_abstract():
    assert not inspect.isabstract(miniJava::Return)


def test_minijava::return_constructor_exists():
    assert callable(miniJava::Return.__init__)


def test_minijava::return_constructor_args():
    sig = inspect.signature(miniJava::Return.__init__)
    params = list(sig.parameters.keys())



def test_minijava::printstatement_is_not_abstract():
    assert not inspect.isabstract(miniJava::PrintStatement)


def test_minijava::printstatement_constructor_exists():
    assert callable(miniJava::PrintStatement.__init__)


def test_minijava::printstatement_constructor_args():
    sig = inspect.signature(miniJava::PrintStatement.__init__)
    params = list(sig.parameters.keys())



def test_minijava::ifstatement_is_not_abstract():
    assert not inspect.isabstract(miniJava::IfStatement)


def test_minijava::ifstatement_constructor_exists():
    assert callable(miniJava::IfStatement.__init__)


def test_minijava::ifstatement_constructor_args():
    sig = inspect.signature(miniJava::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_symbol_is_not_abstract():
    assert not inspect.isabstract(Symbol)


def test_symbol_constructor_exists():
    assert callable(Symbol.__init__)


def test_symbol_constructor_args():
    sig = inspect.signature(Symbol.__init__)
    params = list(sig.parameters.keys())



def test_minijava::clazztomethodmap_is_not_abstract():
    assert not inspect.isabstract(miniJava::ClazzToMethodMap)


def test_minijava::clazztomethodmap_constructor_exists():
    assert callable(miniJava::ClazzToMethodMap.__init__)


def test_minijava::clazztomethodmap_constructor_args():
    sig = inspect.signature(miniJava::ClazzToMethodMap.__init__)
    params = list(sig.parameters.keys())



def test_minijava::block_is_not_abstract():
    assert not inspect.isabstract(miniJava::Block)


def test_minijava::block_constructor_exists():
    assert callable(miniJava::Block.__init__)


def test_minijava::block_constructor_args():
    sig = inspect.signature(miniJava::Block.__init__)
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
    assert "isstatic" in params, "Missing parameter 'isstatic'"
    assert "isabstract" in params, "Missing parameter 'isabstract'"

def test_minijava::method_has_isstatic():
    assert hasattr(miniJava::Method, "isstatic")
    descriptor = None
    for klass in miniJava::Method.__mro__:
        if "isstatic" in klass.__dict__:
            descriptor = klass.__dict__["isstatic"]
            break
    assert isinstance(descriptor, property)

def test_minijava::method_has_isabstract():
    assert hasattr(miniJava::Method, "isabstract")
    descriptor = None
    for klass in miniJava::Method.__mro__:
        if "isabstract" in klass.__dict__:
            descriptor = klass.__dict__["isabstract"]
            break
    assert isinstance(descriptor, property)



def test_typeddeclaration_is_not_abstract():
    assert not inspect.isabstract(TypedDeclaration)


def test_typeddeclaration_constructor_exists():
    assert callable(TypedDeclaration.__init__)


def test_typeddeclaration_constructor_args():
    sig = inspect.signature(TypedDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_minijava::clazz_is_not_abstract():
    assert not inspect.isabstract(miniJava::Clazz)


def test_minijava::clazz_constructor_exists():
    assert callable(miniJava::Clazz.__init__)


def test_minijava::clazz_constructor_args():
    sig = inspect.signature(miniJava::Clazz.__init__)
    params = list(sig.parameters.keys())
    assert "isabstract" in params, "Missing parameter 'isabstract'"

def test_minijava::clazz_has_isabstract():
    assert hasattr(miniJava::Clazz, "isabstract")
    descriptor = None
    for klass in miniJava::Clazz.__mro__:
        if "isabstract" in klass.__dict__:
            descriptor = klass.__dict__["isabstract"]
            break
    assert isinstance(descriptor, property)



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



def test_minijava::state_is_not_abstract():
    assert not inspect.isabstract(miniJava::State)


def test_minijava::state_constructor_exists():
    assert callable(miniJava::State.__init__)


def test_minijava::state_constructor_args():
    sig = inspect.signature(miniJava::State.__init__)
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



def test_minijava::parameter_is_not_abstract():
    assert not inspect.isabstract(miniJava::Parameter)


def test_minijava::parameter_constructor_exists():
    assert callable(miniJava::Parameter.__init__)


def test_minijava::parameter_constructor_args():
    sig = inspect.signature(miniJava::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_call_is_not_abstract():
    assert not inspect.isabstract(Call)


def test_call_constructor_exists():
    assert callable(Call.__init__)


def test_call_constructor_args():
    sig = inspect.signature(Call.__init__)
    params = list(sig.parameters.keys())



def test_minijava::methodcall2_is_not_abstract():
    assert not inspect.isabstract(miniJava::MethodCall2)


def test_minijava::methodcall2_constructor_exists():
    assert callable(miniJava::MethodCall2.__init__)


def test_minijava::methodcall2_constructor_args():
    sig = inspect.signature(miniJava::MethodCall2.__init__)
    params = list(sig.parameters.keys())



def test_minijava::newcall_is_not_abstract():
    assert not inspect.isabstract(miniJava::NewCall)


def test_minijava::newcall_constructor_exists():
    assert callable(miniJava::NewCall.__init__)


def test_minijava::newcall_constructor_args():
    sig = inspect.signature(miniJava::NewCall.__init__)
    params = list(sig.parameters.keys())



def test_minijava::call_is_not_abstract():
    assert not inspect.isabstract(miniJava::Call)


def test_minijava::call_constructor_exists():
    assert callable(miniJava::Call.__init__)


def test_minijava::call_constructor_args():
    sig = inspect.signature(miniJava::Call.__init__)
    params = list(sig.parameters.keys())



def test_minijava::arrayinstance_is_not_abstract():
    assert not inspect.isabstract(miniJava::ArrayInstance)


def test_minijava::arrayinstance_constructor_exists():
    assert callable(miniJava::ArrayInstance.__init__)


def test_minijava::arrayinstance_constructor_args():
    sig = inspect.signature(miniJava::ArrayInstance.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_minijava::arrayinstance_has_size():
    assert hasattr(miniJava::ArrayInstance, "size")
    descriptor = None
    for klass in miniJava::ArrayInstance.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_minijava::objectinstance_is_not_abstract():
    assert not inspect.isabstract(miniJava::ObjectInstance)


def test_minijava::objectinstance_constructor_exists():
    assert callable(miniJava::ObjectInstance.__init__)


def test_minijava::objectinstance_constructor_args():
    sig = inspect.signature(miniJava::ObjectInstance.__init__)
    params = list(sig.parameters.keys())



def test_minijava::frame_is_not_abstract():
    assert not inspect.isabstract(miniJava::Frame)


def test_minijava::frame_constructor_exists():
    assert callable(miniJava::Frame.__init__)


def test_minijava::frame_constructor_args():
    sig = inspect.signature(miniJava::Frame.__init__)
    params = list(sig.parameters.keys())



def test_minijava::outputstream_is_not_abstract():
    assert not inspect.isabstract(miniJava::OutputStream)


def test_minijava::outputstream_constructor_exists():
    assert callable(miniJava::OutputStream.__init__)


def test_minijava::outputstream_constructor_args():
    sig = inspect.signature(miniJava::OutputStream.__init__)
    params = list(sig.parameters.keys())
    assert "stream" in params, "Missing parameter 'stream'"

def test_minijava::outputstream_has_stream():
    assert hasattr(miniJava::OutputStream, "stream")
    descriptor = None
    for klass in miniJava::OutputStream.__mro__:
        if "stream" in klass.__dict__:
            descriptor = klass.__dict__["stream"]
            break
    assert isinstance(descriptor, property)



def test_minijava::fieldbinding_is_not_abstract():
    assert not inspect.isabstract(miniJava::FieldBinding)


def test_minijava::fieldbinding_constructor_exists():
    assert callable(miniJava::FieldBinding.__init__)


def test_minijava::fieldbinding_constructor_args():
    sig = inspect.signature(miniJava::FieldBinding.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_minijava::nullvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava::NullValue)


def test_minijava::nullvalue_constructor_exists():
    assert callable(miniJava::NullValue.__init__)


def test_minijava::nullvalue_constructor_args():
    sig = inspect.signature(miniJava::NullValue.__init__)
    params = list(sig.parameters.keys())



def test_minijava::arrayrefvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava::ArrayRefValue)


def test_minijava::arrayrefvalue_constructor_exists():
    assert callable(miniJava::ArrayRefValue.__init__)


def test_minijava::arrayrefvalue_constructor_args():
    sig = inspect.signature(miniJava::ArrayRefValue.__init__)
    params = list(sig.parameters.keys())



def test_minijava::objectrefvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava::ObjectRefValue)


def test_minijava::objectrefvalue_constructor_exists():
    assert callable(miniJava::ObjectRefValue.__init__)


def test_minijava::objectrefvalue_constructor_args():
    sig = inspect.signature(miniJava::ObjectRefValue.__init__)
    params = list(sig.parameters.keys())



def test_minijava::stringvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava::StringValue)


def test_minijava::stringvalue_constructor_exists():
    assert callable(miniJava::StringValue.__init__)


def test_minijava::stringvalue_constructor_args():
    sig = inspect.signature(miniJava::StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minijava::stringvalue_has_value():
    assert hasattr(miniJava::StringValue, "value")
    descriptor = None
    for klass in miniJava::StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minijava::integervalue_is_not_abstract():
    assert not inspect.isabstract(miniJava::IntegerValue)


def test_minijava::integervalue_constructor_exists():
    assert callable(miniJava::IntegerValue.__init__)


def test_minijava::integervalue_constructor_args():
    sig = inspect.signature(miniJava::IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minijava::integervalue_has_value():
    assert hasattr(miniJava::IntegerValue, "value")
    descriptor = None
    for klass in miniJava::IntegerValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minijava::value_is_not_abstract():
    assert not inspect.isabstract(miniJava::Value)


def test_minijava::value_constructor_exists():
    assert callable(miniJava::Value.__init__)


def test_minijava::value_constructor_args():
    sig = inspect.signature(miniJava::Value.__init__)
    params = list(sig.parameters.keys())



def test_minijava::symboltosymbolbindingmap_is_not_abstract():
    assert not inspect.isabstract(miniJava::SymbolToSymbolBindingMap)


def test_minijava::symboltosymbolbindingmap_constructor_exists():
    assert callable(miniJava::SymbolToSymbolBindingMap.__init__)


def test_minijava::symboltosymbolbindingmap_constructor_args():
    sig = inspect.signature(miniJava::SymbolToSymbolBindingMap.__init__)
    params = list(sig.parameters.keys())



def test_minijava::symbolbinding_is_not_abstract():
    assert not inspect.isabstract(miniJava::SymbolBinding)


def test_minijava::symbolbinding_constructor_exists():
    assert callable(miniJava::SymbolBinding.__init__)


def test_minijava::symbolbinding_constructor_args():
    sig = inspect.signature(miniJava::SymbolBinding.__init__)
    params = list(sig.parameters.keys())



def test_minijava::context_is_not_abstract():
    assert not inspect.isabstract(miniJava::Context)


def test_minijava::context_constructor_exists():
    assert callable(miniJava::Context.__init__)


def test_minijava::context_constructor_args():
    sig = inspect.signature(miniJava::Context.__init__)
    params = list(sig.parameters.keys())



def test_minijava::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(miniJava::BooleanValue)


def test_minijava::booleanvalue_constructor_exists():
    assert callable(miniJava::BooleanValue.__init__)


def test_minijava::booleanvalue_constructor_args():
    sig = inspect.signature(miniJava::BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minijava::booleanvalue_has_value():
    assert hasattr(miniJava::BooleanValue, "value")
    descriptor = None
    for klass in miniJava::BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_minijava::equality_is_not_abstract():
    assert not inspect.isabstract(miniJava::Equality)


def test_minijava::equality_constructor_exists():
    assert callable(miniJava::Equality.__init__)


def test_minijava::equality_constructor_args():
    sig = inspect.signature(miniJava::Equality.__init__)
    params = list(sig.parameters.keys())



def test_minijava::plus_is_not_abstract():
    assert not inspect.isabstract(miniJava::Plus)


def test_minijava::plus_constructor_exists():
    assert callable(miniJava::Plus.__init__)


def test_minijava::plus_constructor_args():
    sig = inspect.signature(miniJava::Plus.__init__)
    params = list(sig.parameters.keys())



def test_minijava::inequality_is_not_abstract():
    assert not inspect.isabstract(miniJava::Inequality)


def test_minijava::inequality_constructor_exists():
    assert callable(miniJava::Inequality.__init__)


def test_minijava::inequality_constructor_args():
    sig = inspect.signature(miniJava::Inequality.__init__)
    params = list(sig.parameters.keys())



def test_minijava::not_is_not_abstract():
    assert not inspect.isabstract(miniJava::Not)


def test_minijava::not_constructor_exists():
    assert callable(miniJava::Not.__init__)


def test_minijava::not_constructor_args():
    sig = inspect.signature(miniJava::Not.__init__)
    params = list(sig.parameters.keys())



def test_minijava::modulo_is_not_abstract():
    assert not inspect.isabstract(miniJava::Modulo)


def test_minijava::modulo_constructor_exists():
    assert callable(miniJava::Modulo.__init__)


def test_minijava::modulo_constructor_args():
    sig = inspect.signature(miniJava::Modulo.__init__)
    params = list(sig.parameters.keys())



def test_minijava::superiororequal_is_not_abstract():
    assert not inspect.isabstract(miniJava::SuperiorOrEqual)


def test_minijava::superiororequal_constructor_exists():
    assert callable(miniJava::SuperiorOrEqual.__init__)


def test_minijava::superiororequal_constructor_args():
    sig = inspect.signature(miniJava::SuperiorOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_minijava::this_is_not_abstract():
    assert not inspect.isabstract(miniJava::This)


def test_minijava::this_constructor_exists():
    assert callable(miniJava::This.__init__)


def test_minijava::this_constructor_args():
    sig = inspect.signature(miniJava::This.__init__)
    params = list(sig.parameters.keys())



def test_minijava::arraylength_is_not_abstract():
    assert not inspect.isabstract(miniJava::ArrayLength)


def test_minijava::arraylength_constructor_exists():
    assert callable(miniJava::ArrayLength.__init__)


def test_minijava::arraylength_constructor_args():
    sig = inspect.signature(miniJava::ArrayLength.__init__)
    params = list(sig.parameters.keys())



def test_minijava::fieldaccess_is_not_abstract():
    assert not inspect.isabstract(miniJava::FieldAccess)


def test_minijava::fieldaccess_constructor_exists():
    assert callable(miniJava::FieldAccess.__init__)


def test_minijava::fieldaccess_constructor_args():
    sig = inspect.signature(miniJava::FieldAccess.__init__)
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



def test_minijava::multiplication_is_not_abstract():
    assert not inspect.isabstract(miniJava::Multiplication)


def test_minijava::multiplication_constructor_exists():
    assert callable(miniJava::Multiplication.__init__)


def test_minijava::multiplication_constructor_args():
    sig = inspect.signature(miniJava::Multiplication.__init__)
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



def test_minijava::inferior_is_not_abstract():
    assert not inspect.isabstract(miniJava::Inferior)


def test_minijava::inferior_constructor_exists():
    assert callable(miniJava::Inferior.__init__)


def test_minijava::inferior_constructor_args():
    sig = inspect.signature(miniJava::Inferior.__init__)
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



def test_minijava::inferiororequal_is_not_abstract():
    assert not inspect.isabstract(miniJava::InferiorOrEqual)


def test_minijava::inferiororequal_constructor_exists():
    assert callable(miniJava::InferiorOrEqual.__init__)


def test_minijava::inferiororequal_constructor_args():
    sig = inspect.signature(miniJava::InferiorOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_minijava::division_is_not_abstract():
    assert not inspect.isabstract(miniJava::Division)


def test_minijava::division_constructor_exists():
    assert callable(miniJava::Division.__init__)


def test_minijava::division_constructor_args():
    sig = inspect.signature(miniJava::Division.__init__)
    params = list(sig.parameters.keys())



def test_minijava::super_is_not_abstract():
    assert not inspect.isabstract(miniJava::Super)


def test_minijava::super_constructor_exists():
    assert callable(miniJava::Super.__init__)


def test_minijava::super_constructor_args():
    sig = inspect.signature(miniJava::Super.__init__)
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



def test_minijava::arrayaccess_is_not_abstract():
    assert not inspect.isabstract(miniJava::ArrayAccess)


def test_minijava::arrayaccess_constructor_exists():
    assert callable(miniJava::ArrayAccess.__init__)


def test_minijava::arrayaccess_constructor_args():
    sig = inspect.signature(miniJava::ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_minijava::methodcall_is_not_abstract():
    assert not inspect.isabstract(miniJava::MethodCall)


def test_minijava::methodcall_constructor_exists():
    assert callable(miniJava::MethodCall.__init__)


def test_minijava::methodcall_constructor_args():
    sig = inspect.signature(miniJava::MethodCall.__init__)
    params = list(sig.parameters.keys())



def test_minijava::superior_is_not_abstract():
    assert not inspect.isabstract(miniJava::Superior)


def test_minijava::superior_constructor_exists():
    assert callable(miniJava::Superior.__init__)


def test_minijava::superior_constructor_args():
    sig = inspect.signature(miniJava::Superior.__init__)
    params = list(sig.parameters.keys())



def test_minijava::neg_is_not_abstract():
    assert not inspect.isabstract(miniJava::Neg)


def test_minijava::neg_constructor_exists():
    assert callable(miniJava::Neg.__init__)


def test_minijava::neg_constructor_args():
    sig = inspect.signature(miniJava::Neg.__init__)
    params = list(sig.parameters.keys())



def test_minijava::and_is_not_abstract():
    assert not inspect.isabstract(miniJava::And)


def test_minijava::and_constructor_exists():
    assert callable(miniJava::And.__init__)


def test_minijava::and_constructor_args():
    sig = inspect.signature(miniJava::And.__init__)
    params = list(sig.parameters.keys())



def test_minijava::minus_is_not_abstract():
    assert not inspect.isabstract(miniJava::Minus)


def test_minijava::minus_constructor_exists():
    assert callable(miniJava::Minus.__init__)


def test_minijava::minus_constructor_args():
    sig = inspect.signature(miniJava::Minus.__init__)
    params = list(sig.parameters.keys())



def test_minijava::newarray_is_not_abstract():
    assert not inspect.isabstract(miniJava::NewArray)


def test_minijava::newarray_constructor_exists():
    assert callable(miniJava::NewArray.__init__)


def test_minijava::newarray_constructor_args():
    sig = inspect.signature(miniJava::NewArray.__init__)
    params = list(sig.parameters.keys())



def test_minijava::newobject_is_not_abstract():
    assert not inspect.isabstract(miniJava::NewObject)


def test_minijava::newobject_constructor_exists():
    assert callable(miniJava::NewObject.__init__)


def test_minijava::newobject_constructor_args():
    sig = inspect.signature(miniJava::NewObject.__init__)
    params = list(sig.parameters.keys())



def test_minijava::or_is_not_abstract():
    assert not inspect.isabstract(miniJava::Or)


def test_minijava::or_constructor_exists():
    assert callable(miniJava::Or.__init__)


def test_minijava::or_constructor_args():
    sig = inspect.signature(miniJava::Or.__init__)
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



def test_minijava::expression_is_not_abstract():
    assert not inspect.isabstract(miniJava::Expression)


def test_minijava::expression_constructor_exists():
    assert callable(miniJava::Expression.__init__)


def test_minijava::expression_constructor_args():
    sig = inspect.signature(miniJava::Expression.__init__)
    params = list(sig.parameters.keys())



def test_minijava::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(miniJava::VariableDeclaration)


def test_minijava::variabledeclaration_constructor_exists():
    assert callable(miniJava::VariableDeclaration.__init__)


def test_minijava::variabledeclaration_constructor_args():
    sig = inspect.signature(miniJava::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_minijava::symbol_is_not_abstract():
    assert not inspect.isabstract(miniJava::Symbol)


def test_minijava::symbol_constructor_exists():
    assert callable(miniJava::Symbol.__init__)


def test_minijava::symbol_constructor_args():
    sig = inspect.signature(miniJava::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_minijava::typeddeclaration_is_not_abstract():
    assert not inspect.isabstract(miniJava::TypedDeclaration)


def test_minijava::typeddeclaration_constructor_exists():
    assert callable(miniJava::TypedDeclaration.__init__)


def test_minijava::typeddeclaration_constructor_args():
    sig = inspect.signature(miniJava::TypedDeclaration.__init__)
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



def test_minijava::integertyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava::IntegerTypeRef)


def test_minijava::integertyperef_constructor_exists():
    assert callable(miniJava::IntegerTypeRef.__init__)


def test_minijava::integertyperef_constructor_args():
    sig = inspect.signature(miniJava::IntegerTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava::booleantyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava::BooleanTypeRef)


def test_minijava::booleantyperef_constructor_exists():
    assert callable(miniJava::BooleanTypeRef.__init__)


def test_minijava::booleantyperef_constructor_args():
    sig = inspect.signature(miniJava::BooleanTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava::voidtyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava::VoidTypeRef)


def test_minijava::voidtyperef_constructor_exists():
    assert callable(miniJava::VoidTypeRef.__init__)


def test_minijava::voidtyperef_constructor_args():
    sig = inspect.signature(miniJava::VoidTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_minijava::stringtyperef_is_not_abstract():
    assert not inspect.isabstract(miniJava::StringTypeRef)


def test_minijava::stringtyperef_constructor_exists():
    assert callable(miniJava::StringTypeRef.__init__)


def test_minijava::stringtyperef_constructor_args():
    sig = inspect.signature(miniJava::StringTypeRef.__init__)
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

def test_accesslevel_exists():
    # Check that the Enumeration exists
    assert AccessLevel is not None

def test_accesslevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessLevel]
    expected_literals = [
        "PRIVATE",
        "PROTECTED",
        "PUBLIC",
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
miniJava::TypeRef_strategy = st.builds(
    miniJava::TypeRef,
)
miniJava::Statement_strategy = st.builds(
    miniJava::Statement,
)
Statement_strategy = st.builds(
    Statement,
)
miniJava::Assignment_strategy = st.builds(
    miniJava::Assignment,
)
miniJava::ForStatement_strategy = st.builds(
    miniJava::ForStatement,
)
miniJava::WhileStatement_strategy = st.builds(
    miniJava::WhileStatement,
)
miniJava::Return_strategy = st.builds(
    miniJava::Return,
)
miniJava::PrintStatement_strategy = st.builds(
    miniJava::PrintStatement,
)
miniJava::IfStatement_strategy = st.builds(
    miniJava::IfStatement,
)
Symbol_strategy = st.builds(
    Symbol,
)
miniJava::ClazzToMethodMap_strategy = st.builds(
    miniJava::ClazzToMethodMap,
)
miniJava::Block_strategy = st.builds(
    miniJava::Block,
)
Member_strategy = st.builds(
    Member,
)
miniJava::Field_strategy = st.builds(
    miniJava::Field,
)
miniJava::Method_strategy = st.builds(
    miniJava::Method,
    isstatic=
        st.booleans(),
    isabstract=
        st.booleans()
)
TypedDeclaration_strategy = st.builds(
    TypedDeclaration,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
miniJava::Clazz_strategy = st.builds(
    miniJava::Clazz,
    isabstract=
        st.booleans()
)
miniJava::Member_strategy = st.builds(
    miniJava::Member,
    access=
        safe_text
)
miniJava::Interface_strategy = st.builds(
    miniJava::Interface,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
miniJava::State_strategy = st.builds(
    miniJava::State,
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
miniJava::Program_strategy = st.builds(
    miniJava::Program,
    name=
        safe_text
)
miniJava::Parameter_strategy = st.builds(
    miniJava::Parameter,
)
Call_strategy = st.builds(
    Call,
)
miniJava::MethodCall2_strategy = st.builds(
    miniJava::MethodCall2,
)
miniJava::NewCall_strategy = st.builds(
    miniJava::NewCall,
)
miniJava::Call_strategy = st.builds(
    miniJava::Call,
)
miniJava::ArrayInstance_strategy = st.builds(
    miniJava::ArrayInstance,
    size=
        st.integers()
)
miniJava::ObjectInstance_strategy = st.builds(
    miniJava::ObjectInstance,
)
miniJava::Frame_strategy = st.builds(
    miniJava::Frame,
)
miniJava::OutputStream_strategy = st.builds(
    miniJava::OutputStream,
    stream=
        safe_text
)
miniJava::FieldBinding_strategy = st.builds(
    miniJava::FieldBinding,
)
Value_strategy = st.builds(
    Value,
)
miniJava::NullValue_strategy = st.builds(
    miniJava::NullValue,
)
miniJava::ArrayRefValue_strategy = st.builds(
    miniJava::ArrayRefValue,
)
miniJava::ObjectRefValue_strategy = st.builds(
    miniJava::ObjectRefValue,
)
miniJava::StringValue_strategy = st.builds(
    miniJava::StringValue,
    value=
        safe_text
)
miniJava::IntegerValue_strategy = st.builds(
    miniJava::IntegerValue,
    value=
        st.integers()
)
miniJava::Value_strategy = st.builds(
    miniJava::Value,
)
miniJava::SymbolToSymbolBindingMap_strategy = st.builds(
    miniJava::SymbolToSymbolBindingMap,
)
miniJava::SymbolBinding_strategy = st.builds(
    miniJava::SymbolBinding,
)
miniJava::Context_strategy = st.builds(
    miniJava::Context,
)
miniJava::BooleanValue_strategy = st.builds(
    miniJava::BooleanValue,
    value=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
miniJava::Equality_strategy = st.builds(
    miniJava::Equality,
)
miniJava::Plus_strategy = st.builds(
    miniJava::Plus,
)
miniJava::Inequality_strategy = st.builds(
    miniJava::Inequality,
)
miniJava::Not_strategy = st.builds(
    miniJava::Not,
)
miniJava::Modulo_strategy = st.builds(
    miniJava::Modulo,
)
miniJava::SuperiorOrEqual_strategy = st.builds(
    miniJava::SuperiorOrEqual,
)
miniJava::This_strategy = st.builds(
    miniJava::This,
)
miniJava::ArrayLength_strategy = st.builds(
    miniJava::ArrayLength,
)
miniJava::FieldAccess_strategy = st.builds(
    miniJava::FieldAccess,
)
miniJava::IntConstant_strategy = st.builds(
    miniJava::IntConstant,
    value=
        st.integers()
)
miniJava::Multiplication_strategy = st.builds(
    miniJava::Multiplication,
)
miniJava::BoolConstant_strategy = st.builds(
    miniJava::BoolConstant,
    value=
        safe_text
)
miniJava::Inferior_strategy = st.builds(
    miniJava::Inferior,
)
miniJava::Null_strategy = st.builds(
    miniJava::Null,
)
miniJava::SymbolRef_strategy = st.builds(
    miniJava::SymbolRef,
)
miniJava::InferiorOrEqual_strategy = st.builds(
    miniJava::InferiorOrEqual,
)
miniJava::Division_strategy = st.builds(
    miniJava::Division,
)
miniJava::Super_strategy = st.builds(
    miniJava::Super,
)
miniJava::StringConstant_strategy = st.builds(
    miniJava::StringConstant,
    value=
        safe_text
)
miniJava::ArrayAccess_strategy = st.builds(
    miniJava::ArrayAccess,
)
miniJava::MethodCall_strategy = st.builds(
    miniJava::MethodCall,
)
miniJava::Superior_strategy = st.builds(
    miniJava::Superior,
)
miniJava::Neg_strategy = st.builds(
    miniJava::Neg,
)
miniJava::And_strategy = st.builds(
    miniJava::And,
)
miniJava::Minus_strategy = st.builds(
    miniJava::Minus,
)
miniJava::NewArray_strategy = st.builds(
    miniJava::NewArray,
)
miniJava::NewObject_strategy = st.builds(
    miniJava::NewObject,
)
miniJava::Or_strategy = st.builds(
    miniJava::Or,
)
miniJava::Assignee_strategy = st.builds(
    miniJava::Assignee,
)
Assignee_strategy = st.builds(
    Assignee,
)
miniJava::Expression_strategy = st.builds(
    miniJava::Expression,
)
miniJava::VariableDeclaration_strategy = st.builds(
    miniJava::VariableDeclaration,
)
miniJava::Symbol_strategy = st.builds(
    miniJava::Symbol,
)
miniJava::TypedDeclaration_strategy = st.builds(
    miniJava::TypedDeclaration,
)
miniJava::NamedElement_strategy = st.builds(
    miniJava::NamedElement,
    name=
        safe_text
)
SingleTypeRef_strategy = st.builds(
    SingleTypeRef,
)
miniJava::IntegerTypeRef_strategy = st.builds(
    miniJava::IntegerTypeRef,
)
miniJava::BooleanTypeRef_strategy = st.builds(
    miniJava::BooleanTypeRef,
)
miniJava::VoidTypeRef_strategy = st.builds(
    miniJava::VoidTypeRef,
)
miniJava::StringTypeRef_strategy = st.builds(
    miniJava::StringTypeRef,
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

@given(instance=miniJava::TypeRef_strategy)
@settings(max_examples=50)
def test_minijava::typeref_instantiation(instance):
    assert isinstance(instance, miniJava::TypeRef)

@given(instance=miniJava::Statement_strategy)
@settings(max_examples=50)
def test_minijava::statement_instantiation(instance):
    assert isinstance(instance, miniJava::Statement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=miniJava::Assignment_strategy)
@settings(max_examples=50)
def test_minijava::assignment_instantiation(instance):
    assert isinstance(instance, miniJava::Assignment)

@given(instance=miniJava::ForStatement_strategy)
@settings(max_examples=50)
def test_minijava::forstatement_instantiation(instance):
    assert isinstance(instance, miniJava::ForStatement)

@given(instance=miniJava::WhileStatement_strategy)
@settings(max_examples=50)
def test_minijava::whilestatement_instantiation(instance):
    assert isinstance(instance, miniJava::WhileStatement)

@given(instance=miniJava::Return_strategy)
@settings(max_examples=50)
def test_minijava::return_instantiation(instance):
    assert isinstance(instance, miniJava::Return)

@given(instance=miniJava::PrintStatement_strategy)
@settings(max_examples=50)
def test_minijava::printstatement_instantiation(instance):
    assert isinstance(instance, miniJava::PrintStatement)

@given(instance=miniJava::IfStatement_strategy)
@settings(max_examples=50)
def test_minijava::ifstatement_instantiation(instance):
    assert isinstance(instance, miniJava::IfStatement)

@given(instance=Symbol_strategy)
@settings(max_examples=50)
def test_symbol_instantiation(instance):
    assert isinstance(instance, Symbol)

@given(instance=miniJava::ClazzToMethodMap_strategy)
@settings(max_examples=50)
def test_minijava::clazztomethodmap_instantiation(instance):
    assert isinstance(instance, miniJava::ClazzToMethodMap)

@given(instance=miniJava::Block_strategy)
@settings(max_examples=50)
def test_minijava::block_instantiation(instance):
    assert isinstance(instance, miniJava::Block)

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
def test_minijava::method_isstatic_type(instance):
    assert isinstance(instance.isstatic, bool)


@given(instance=miniJava::Method_strategy)
def test_minijava::method_isstatic_setter(instance):
    original = instance.isstatic
    instance.isstatic = original
    assert instance.isstatic == original

@given(instance=miniJava::Method_strategy)
def test_minijava::method_isabstract_type(instance):
    assert isinstance(instance.isabstract, bool)


@given(instance=miniJava::Method_strategy)
def test_minijava::method_isabstract_setter(instance):
    original = instance.isabstract
    instance.isabstract = original
    assert instance.isabstract == original

@given(instance=TypedDeclaration_strategy)
@settings(max_examples=50)
def test_typeddeclaration_instantiation(instance):
    assert isinstance(instance, TypedDeclaration)

@given(instance=TypeDeclaration_strategy)
@settings(max_examples=50)
def test_typedeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)

@given(instance=miniJava::Clazz_strategy)
@settings(max_examples=50)
def test_minijava::clazz_instantiation(instance):
    assert isinstance(instance, miniJava::Clazz)

@given(instance=miniJava::Clazz_strategy)
def test_minijava::clazz_isabstract_type(instance):
    assert isinstance(instance.isabstract, bool)


@given(instance=miniJava::Clazz_strategy)
def test_minijava::clazz_isabstract_setter(instance):
    original = instance.isabstract
    instance.isabstract = original
    assert instance.isabstract == original

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

@given(instance=miniJava::Interface_strategy)
@settings(max_examples=50)
def test_minijava::interface_instantiation(instance):
    assert isinstance(instance, miniJava::Interface)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=miniJava::State_strategy)
@settings(max_examples=50)
def test_minijava::state_instantiation(instance):
    assert isinstance(instance, miniJava::State)

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

@given(instance=miniJava::Parameter_strategy)
@settings(max_examples=50)
def test_minijava::parameter_instantiation(instance):
    assert isinstance(instance, miniJava::Parameter)

@given(instance=Call_strategy)
@settings(max_examples=50)
def test_call_instantiation(instance):
    assert isinstance(instance, Call)

@given(instance=miniJava::MethodCall2_strategy)
@settings(max_examples=50)
def test_minijava::methodcall2_instantiation(instance):
    assert isinstance(instance, miniJava::MethodCall2)

@given(instance=miniJava::NewCall_strategy)
@settings(max_examples=50)
def test_minijava::newcall_instantiation(instance):
    assert isinstance(instance, miniJava::NewCall)

@given(instance=miniJava::Call_strategy)
@settings(max_examples=50)
def test_minijava::call_instantiation(instance):
    assert isinstance(instance, miniJava::Call)

@given(instance=miniJava::ArrayInstance_strategy)
@settings(max_examples=50)
def test_minijava::arrayinstance_instantiation(instance):
    assert isinstance(instance, miniJava::ArrayInstance)

@given(instance=miniJava::ArrayInstance_strategy)
def test_minijava::arrayinstance_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=miniJava::ArrayInstance_strategy)
def test_minijava::arrayinstance_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=miniJava::ObjectInstance_strategy)
@settings(max_examples=50)
def test_minijava::objectinstance_instantiation(instance):
    assert isinstance(instance, miniJava::ObjectInstance)

@given(instance=miniJava::Frame_strategy)
@settings(max_examples=50)
def test_minijava::frame_instantiation(instance):
    assert isinstance(instance, miniJava::Frame)

@given(instance=miniJava::OutputStream_strategy)
@settings(max_examples=50)
def test_minijava::outputstream_instantiation(instance):
    assert isinstance(instance, miniJava::OutputStream)

@given(instance=miniJava::OutputStream_strategy)
def test_minijava::outputstream_stream_type(instance):
    assert isinstance(instance.stream, str)


@given(instance=miniJava::OutputStream_strategy)
def test_minijava::outputstream_stream_setter(instance):
    original = instance.stream
    instance.stream = original
    assert instance.stream == original

@given(instance=miniJava::FieldBinding_strategy)
@settings(max_examples=50)
def test_minijava::fieldbinding_instantiation(instance):
    assert isinstance(instance, miniJava::FieldBinding)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=miniJava::NullValue_strategy)
@settings(max_examples=50)
def test_minijava::nullvalue_instantiation(instance):
    assert isinstance(instance, miniJava::NullValue)

@given(instance=miniJava::ArrayRefValue_strategy)
@settings(max_examples=50)
def test_minijava::arrayrefvalue_instantiation(instance):
    assert isinstance(instance, miniJava::ArrayRefValue)

@given(instance=miniJava::ObjectRefValue_strategy)
@settings(max_examples=50)
def test_minijava::objectrefvalue_instantiation(instance):
    assert isinstance(instance, miniJava::ObjectRefValue)

@given(instance=miniJava::StringValue_strategy)
@settings(max_examples=50)
def test_minijava::stringvalue_instantiation(instance):
    assert isinstance(instance, miniJava::StringValue)

@given(instance=miniJava::StringValue_strategy)
def test_minijava::stringvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=miniJava::StringValue_strategy)
def test_minijava::stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=miniJava::IntegerValue_strategy)
@settings(max_examples=50)
def test_minijava::integervalue_instantiation(instance):
    assert isinstance(instance, miniJava::IntegerValue)

@given(instance=miniJava::IntegerValue_strategy)
def test_minijava::integervalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=miniJava::IntegerValue_strategy)
def test_minijava::integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=miniJava::Value_strategy)
@settings(max_examples=50)
def test_minijava::value_instantiation(instance):
    assert isinstance(instance, miniJava::Value)

@given(instance=miniJava::SymbolToSymbolBindingMap_strategy)
@settings(max_examples=50)
def test_minijava::symboltosymbolbindingmap_instantiation(instance):
    assert isinstance(instance, miniJava::SymbolToSymbolBindingMap)

@given(instance=miniJava::SymbolBinding_strategy)
@settings(max_examples=50)
def test_minijava::symbolbinding_instantiation(instance):
    assert isinstance(instance, miniJava::SymbolBinding)

@given(instance=miniJava::Context_strategy)
@settings(max_examples=50)
def test_minijava::context_instantiation(instance):
    assert isinstance(instance, miniJava::Context)

@given(instance=miniJava::BooleanValue_strategy)
@settings(max_examples=50)
def test_minijava::booleanvalue_instantiation(instance):
    assert isinstance(instance, miniJava::BooleanValue)

@given(instance=miniJava::BooleanValue_strategy)
def test_minijava::booleanvalue_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=miniJava::BooleanValue_strategy)
def test_minijava::booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=miniJava::Equality_strategy)
@settings(max_examples=50)
def test_minijava::equality_instantiation(instance):
    assert isinstance(instance, miniJava::Equality)

@given(instance=miniJava::Plus_strategy)
@settings(max_examples=50)
def test_minijava::plus_instantiation(instance):
    assert isinstance(instance, miniJava::Plus)

@given(instance=miniJava::Inequality_strategy)
@settings(max_examples=50)
def test_minijava::inequality_instantiation(instance):
    assert isinstance(instance, miniJava::Inequality)

@given(instance=miniJava::Not_strategy)
@settings(max_examples=50)
def test_minijava::not_instantiation(instance):
    assert isinstance(instance, miniJava::Not)

@given(instance=miniJava::Modulo_strategy)
@settings(max_examples=50)
def test_minijava::modulo_instantiation(instance):
    assert isinstance(instance, miniJava::Modulo)

@given(instance=miniJava::SuperiorOrEqual_strategy)
@settings(max_examples=50)
def test_minijava::superiororequal_instantiation(instance):
    assert isinstance(instance, miniJava::SuperiorOrEqual)

@given(instance=miniJava::This_strategy)
@settings(max_examples=50)
def test_minijava::this_instantiation(instance):
    assert isinstance(instance, miniJava::This)

@given(instance=miniJava::ArrayLength_strategy)
@settings(max_examples=50)
def test_minijava::arraylength_instantiation(instance):
    assert isinstance(instance, miniJava::ArrayLength)

@given(instance=miniJava::FieldAccess_strategy)
@settings(max_examples=50)
def test_minijava::fieldaccess_instantiation(instance):
    assert isinstance(instance, miniJava::FieldAccess)

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

@given(instance=miniJava::Multiplication_strategy)
@settings(max_examples=50)
def test_minijava::multiplication_instantiation(instance):
    assert isinstance(instance, miniJava::Multiplication)

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

@given(instance=miniJava::Inferior_strategy)
@settings(max_examples=50)
def test_minijava::inferior_instantiation(instance):
    assert isinstance(instance, miniJava::Inferior)

@given(instance=miniJava::Null_strategy)
@settings(max_examples=50)
def test_minijava::null_instantiation(instance):
    assert isinstance(instance, miniJava::Null)

@given(instance=miniJava::SymbolRef_strategy)
@settings(max_examples=50)
def test_minijava::symbolref_instantiation(instance):
    assert isinstance(instance, miniJava::SymbolRef)

@given(instance=miniJava::InferiorOrEqual_strategy)
@settings(max_examples=50)
def test_minijava::inferiororequal_instantiation(instance):
    assert isinstance(instance, miniJava::InferiorOrEqual)

@given(instance=miniJava::Division_strategy)
@settings(max_examples=50)
def test_minijava::division_instantiation(instance):
    assert isinstance(instance, miniJava::Division)

@given(instance=miniJava::Super_strategy)
@settings(max_examples=50)
def test_minijava::super_instantiation(instance):
    assert isinstance(instance, miniJava::Super)

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

@given(instance=miniJava::ArrayAccess_strategy)
@settings(max_examples=50)
def test_minijava::arrayaccess_instantiation(instance):
    assert isinstance(instance, miniJava::ArrayAccess)

@given(instance=miniJava::MethodCall_strategy)
@settings(max_examples=50)
def test_minijava::methodcall_instantiation(instance):
    assert isinstance(instance, miniJava::MethodCall)

@given(instance=miniJava::Superior_strategy)
@settings(max_examples=50)
def test_minijava::superior_instantiation(instance):
    assert isinstance(instance, miniJava::Superior)

@given(instance=miniJava::Neg_strategy)
@settings(max_examples=50)
def test_minijava::neg_instantiation(instance):
    assert isinstance(instance, miniJava::Neg)

@given(instance=miniJava::And_strategy)
@settings(max_examples=50)
def test_minijava::and_instantiation(instance):
    assert isinstance(instance, miniJava::And)

@given(instance=miniJava::Minus_strategy)
@settings(max_examples=50)
def test_minijava::minus_instantiation(instance):
    assert isinstance(instance, miniJava::Minus)

@given(instance=miniJava::NewArray_strategy)
@settings(max_examples=50)
def test_minijava::newarray_instantiation(instance):
    assert isinstance(instance, miniJava::NewArray)

@given(instance=miniJava::NewObject_strategy)
@settings(max_examples=50)
def test_minijava::newobject_instantiation(instance):
    assert isinstance(instance, miniJava::NewObject)

@given(instance=miniJava::Or_strategy)
@settings(max_examples=50)
def test_minijava::or_instantiation(instance):
    assert isinstance(instance, miniJava::Or)

@given(instance=miniJava::Assignee_strategy)
@settings(max_examples=50)
def test_minijava::assignee_instantiation(instance):
    assert isinstance(instance, miniJava::Assignee)

@given(instance=Assignee_strategy)
@settings(max_examples=50)
def test_assignee_instantiation(instance):
    assert isinstance(instance, Assignee)

@given(instance=miniJava::Expression_strategy)
@settings(max_examples=50)
def test_minijava::expression_instantiation(instance):
    assert isinstance(instance, miniJava::Expression)

@given(instance=miniJava::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_minijava::variabledeclaration_instantiation(instance):
    assert isinstance(instance, miniJava::VariableDeclaration)

@given(instance=miniJava::Symbol_strategy)
@settings(max_examples=50)
def test_minijava::symbol_instantiation(instance):
    assert isinstance(instance, miniJava::Symbol)

@given(instance=miniJava::TypedDeclaration_strategy)
@settings(max_examples=50)
def test_minijava::typeddeclaration_instantiation(instance):
    assert isinstance(instance, miniJava::TypedDeclaration)

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

@given(instance=miniJava::IntegerTypeRef_strategy)
@settings(max_examples=50)
def test_minijava::integertyperef_instantiation(instance):
    assert isinstance(instance, miniJava::IntegerTypeRef)

@given(instance=miniJava::BooleanTypeRef_strategy)
@settings(max_examples=50)
def test_minijava::booleantyperef_instantiation(instance):
    assert isinstance(instance, miniJava::BooleanTypeRef)

@given(instance=miniJava::VoidTypeRef_strategy)
@settings(max_examples=50)
def test_minijava::voidtyperef_instantiation(instance):
    assert isinstance(instance, miniJava::VoidTypeRef)

@given(instance=miniJava::StringTypeRef_strategy)
@settings(max_examples=50)
def test_minijava::stringtyperef_instantiation(instance):
    assert isinstance(instance, miniJava::StringTypeRef)

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

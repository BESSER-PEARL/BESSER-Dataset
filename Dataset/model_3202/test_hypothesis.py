import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    langc::LinkableArtifact,
    langc::System,
    SwitchClause,
    langc::LabeledClause,
    CodeBlock,
    langc::CodeBlob,
    langc::ConditionalStatement,
    langc::SwitchClause,
    FileName,
    langc::SystemFileName,
    langc::BindableValue,
    Sizeof,
    langc::SizeofExpr,
    langc::SizeofType,
    langc::Dependency,
    Directive,
    langc::WhileStatement,
    langc::SubSystem,
    ElementAccess,
    langc::MemberAccess,
    Name,
    langc::FolderName,
    FileDependency,
    langc::UserInclude,
    langc::SystemInclude,
    Dependency,
    langc::DependencyBlob,
    langc::FileDependency,
    ExpressionStatement,
    langc::ReturnStatement,
    Statement,
    langc::SwitchStatement,
    langc::BreakStatement,
    langc::VariableDeclarationStatement,
    langc::CodeBlock,
    langc::ExpressionStatement,
    langc::Statement,
    Literal,
    langc::FloatingLiteral,
    langc::CharacterLiteral,
    langc::IntegralLiteral,
    Expression,
    langc::LogicalComparison,
    langc::CastExpr,
    langc::ElementAccess,
    langc::Sizeof,
    langc::Literal,
    langc::ExpressionBlob,
    langc::FunctionAddress,
    langc::IndexExpr,
    langc::BinaryOperation,
    langc::StringLiteral,
    langc::DereferenceExpr,
    langc::BlockInitializer,
    langc::AddressOfExpr,
    langc::FunctionCall,
    langc::Expression,
    langc::Element,
    langc::NamedReference,
    NamedElement,
    langc::Enum,
    langc::VariableDeclaration,
    langc::Typedef,
    langc::Structure,
    langc::Function,
    Structure,
    langc::Union,
    langc::Struct,
    langc::Directive,
    langc::DependencyList,
    langc::FileName,
    Element,
    langc::BuiltInType,
    langc::UserElement,
    langc::ElementList,
    langc::Name,
    BindableValue,
    langc::ElementReference,
    langc::Enumerator,
    langc::Macro,
    UserElement,
    langc::FunctionPointer,
    langc::FunctionImplementation,
    langc::NamedElement,
    Pointer,
    CVQualifier,
    LinkageSpec,
    BooleanOperator,
    Operator,
    ElementKind,
    PrimitiveType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_langc::linkableartifact_is_not_abstract():
    assert not inspect.isabstract(langc::LinkableArtifact)


def test_langc::linkableartifact_constructor_exists():
    assert callable(langc::LinkableArtifact.__init__)


def test_langc::linkableartifact_constructor_args():
    sig = inspect.signature(langc::LinkableArtifact.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_langc::linkableartifact_has_name():
    assert hasattr(langc::LinkableArtifact, "name")
    descriptor = None
    for klass in langc::LinkableArtifact.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_langc::system_is_not_abstract():
    assert not inspect.isabstract(langc::System)


def test_langc::system_constructor_exists():
    assert callable(langc::System.__init__)


def test_langc::system_constructor_args():
    sig = inspect.signature(langc::System.__init__)
    params = list(sig.parameters.keys())



def test_switchclause_is_not_abstract():
    assert not inspect.isabstract(SwitchClause)


def test_switchclause_constructor_exists():
    assert callable(SwitchClause.__init__)


def test_switchclause_constructor_args():
    sig = inspect.signature(SwitchClause.__init__)
    params = list(sig.parameters.keys())



def test_langc::labeledclause_is_not_abstract():
    assert not inspect.isabstract(langc::LabeledClause)


def test_langc::labeledclause_constructor_exists():
    assert callable(langc::LabeledClause.__init__)


def test_langc::labeledclause_constructor_args():
    sig = inspect.signature(langc::LabeledClause.__init__)
    params = list(sig.parameters.keys())



def test_codeblock_is_not_abstract():
    assert not inspect.isabstract(CodeBlock)


def test_codeblock_constructor_exists():
    assert callable(CodeBlock.__init__)


def test_codeblock_constructor_args():
    sig = inspect.signature(CodeBlock.__init__)
    params = list(sig.parameters.keys())



def test_langc::codeblob_is_not_abstract():
    assert not inspect.isabstract(langc::CodeBlob)


def test_langc::codeblob_constructor_exists():
    assert callable(langc::CodeBlob.__init__)


def test_langc::codeblob_constructor_args():
    sig = inspect.signature(langc::CodeBlob.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "markerComment" in params, "Missing parameter 'markerComment'"

def test_langc::codeblob_has_text():
    assert hasattr(langc::CodeBlob, "text")
    descriptor = None
    for klass in langc::CodeBlob.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_langc::codeblob_has_markerComment():
    assert hasattr(langc::CodeBlob, "markerComment")
    descriptor = None
    for klass in langc::CodeBlob.__mro__:
        if "markerComment" in klass.__dict__:
            descriptor = klass.__dict__["markerComment"]
            break
    assert isinstance(descriptor, property)



def test_langc::conditionalstatement_is_not_abstract():
    assert not inspect.isabstract(langc::ConditionalStatement)


def test_langc::conditionalstatement_constructor_exists():
    assert callable(langc::ConditionalStatement.__init__)


def test_langc::conditionalstatement_constructor_args():
    sig = inspect.signature(langc::ConditionalStatement.__init__)
    params = list(sig.parameters.keys())



def test_langc::switchclause_is_not_abstract():
    assert not inspect.isabstract(langc::SwitchClause)


def test_langc::switchclause_constructor_exists():
    assert callable(langc::SwitchClause.__init__)


def test_langc::switchclause_constructor_args():
    sig = inspect.signature(langc::SwitchClause.__init__)
    params = list(sig.parameters.keys())
    assert "fallthrough" in params, "Missing parameter 'fallthrough'"

def test_langc::switchclause_has_fallthrough():
    assert hasattr(langc::SwitchClause, "fallthrough")
    descriptor = None
    for klass in langc::SwitchClause.__mro__:
        if "fallthrough" in klass.__dict__:
            descriptor = klass.__dict__["fallthrough"]
            break
    assert isinstance(descriptor, property)



def test_filename_is_not_abstract():
    assert not inspect.isabstract(FileName)


def test_filename_constructor_exists():
    assert callable(FileName.__init__)


def test_filename_constructor_args():
    sig = inspect.signature(FileName.__init__)
    params = list(sig.parameters.keys())



def test_langc::systemfilename_is_not_abstract():
    assert not inspect.isabstract(langc::SystemFileName)


def test_langc::systemfilename_constructor_exists():
    assert callable(langc::SystemFileName.__init__)


def test_langc::systemfilename_constructor_args():
    sig = inspect.signature(langc::SystemFileName.__init__)
    params = list(sig.parameters.keys())



def test_langc::bindablevalue_is_not_abstract():
    assert not inspect.isabstract(langc::BindableValue)


def test_langc::bindablevalue_constructor_exists():
    assert callable(langc::BindableValue.__init__)


def test_langc::bindablevalue_constructor_args():
    sig = inspect.signature(langc::BindableValue.__init__)
    params = list(sig.parameters.keys())



def test_sizeof_is_not_abstract():
    assert not inspect.isabstract(Sizeof)


def test_sizeof_constructor_exists():
    assert callable(Sizeof.__init__)


def test_sizeof_constructor_args():
    sig = inspect.signature(Sizeof.__init__)
    params = list(sig.parameters.keys())



def test_langc::sizeofexpr_is_not_abstract():
    assert not inspect.isabstract(langc::SizeofExpr)


def test_langc::sizeofexpr_constructor_exists():
    assert callable(langc::SizeofExpr.__init__)


def test_langc::sizeofexpr_constructor_args():
    sig = inspect.signature(langc::SizeofExpr.__init__)
    params = list(sig.parameters.keys())



def test_langc::sizeoftype_is_not_abstract():
    assert not inspect.isabstract(langc::SizeofType)


def test_langc::sizeoftype_constructor_exists():
    assert callable(langc::SizeofType.__init__)


def test_langc::sizeoftype_constructor_args():
    sig = inspect.signature(langc::SizeofType.__init__)
    params = list(sig.parameters.keys())



def test_langc::dependency_is_not_abstract():
    assert not inspect.isabstract(langc::Dependency)


def test_langc::dependency_constructor_exists():
    assert callable(langc::Dependency.__init__)


def test_langc::dependency_constructor_args():
    sig = inspect.signature(langc::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_directive_is_not_abstract():
    assert not inspect.isabstract(Directive)


def test_directive_constructor_exists():
    assert callable(Directive.__init__)


def test_directive_constructor_args():
    sig = inspect.signature(Directive.__init__)
    params = list(sig.parameters.keys())



def test_langc::whilestatement_is_not_abstract():
    assert not inspect.isabstract(langc::WhileStatement)


def test_langc::whilestatement_constructor_exists():
    assert callable(langc::WhileStatement.__init__)


def test_langc::whilestatement_constructor_args():
    sig = inspect.signature(langc::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_langc::subsystem_is_not_abstract():
    assert not inspect.isabstract(langc::SubSystem)


def test_langc::subsystem_constructor_exists():
    assert callable(langc::SubSystem.__init__)


def test_langc::subsystem_constructor_args():
    sig = inspect.signature(langc::SubSystem.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_langc::subsystem_has_name():
    assert hasattr(langc::SubSystem, "name")
    descriptor = None
    for klass in langc::SubSystem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_elementaccess_is_not_abstract():
    assert not inspect.isabstract(ElementAccess)


def test_elementaccess_constructor_exists():
    assert callable(ElementAccess.__init__)


def test_elementaccess_constructor_args():
    sig = inspect.signature(ElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_langc::memberaccess_is_not_abstract():
    assert not inspect.isabstract(langc::MemberAccess)


def test_langc::memberaccess_constructor_exists():
    assert callable(langc::MemberAccess.__init__)


def test_langc::memberaccess_constructor_args():
    sig = inspect.signature(langc::MemberAccess.__init__)
    params = list(sig.parameters.keys())



def test_name_is_not_abstract():
    assert not inspect.isabstract(Name)


def test_name_constructor_exists():
    assert callable(Name.__init__)


def test_name_constructor_args():
    sig = inspect.signature(Name.__init__)
    params = list(sig.parameters.keys())



def test_langc::foldername_is_not_abstract():
    assert not inspect.isabstract(langc::FolderName)


def test_langc::foldername_constructor_exists():
    assert callable(langc::FolderName.__init__)


def test_langc::foldername_constructor_args():
    sig = inspect.signature(langc::FolderName.__init__)
    params = list(sig.parameters.keys())
    assert "api" in params, "Missing parameter 'api'"

def test_langc::foldername_has_api():
    assert hasattr(langc::FolderName, "api")
    descriptor = None
    for klass in langc::FolderName.__mro__:
        if "api" in klass.__dict__:
            descriptor = klass.__dict__["api"]
            break
    assert isinstance(descriptor, property)



def test_filedependency_is_not_abstract():
    assert not inspect.isabstract(FileDependency)


def test_filedependency_constructor_exists():
    assert callable(FileDependency.__init__)


def test_filedependency_constructor_args():
    sig = inspect.signature(FileDependency.__init__)
    params = list(sig.parameters.keys())



def test_langc::userinclude_is_not_abstract():
    assert not inspect.isabstract(langc::UserInclude)


def test_langc::userinclude_constructor_exists():
    assert callable(langc::UserInclude.__init__)


def test_langc::userinclude_constructor_args():
    sig = inspect.signature(langc::UserInclude.__init__)
    params = list(sig.parameters.keys())



def test_langc::systeminclude_is_not_abstract():
    assert not inspect.isabstract(langc::SystemInclude)


def test_langc::systeminclude_constructor_exists():
    assert callable(langc::SystemInclude.__init__)


def test_langc::systeminclude_constructor_args():
    sig = inspect.signature(langc::SystemInclude.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_langc::dependencyblob_is_not_abstract():
    assert not inspect.isabstract(langc::DependencyBlob)


def test_langc::dependencyblob_constructor_exists():
    assert callable(langc::DependencyBlob.__init__)


def test_langc::dependencyblob_constructor_args():
    sig = inspect.signature(langc::DependencyBlob.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "markerComment" in params, "Missing parameter 'markerComment'"

def test_langc::dependencyblob_has_text():
    assert hasattr(langc::DependencyBlob, "text")
    descriptor = None
    for klass in langc::DependencyBlob.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_langc::dependencyblob_has_markerComment():
    assert hasattr(langc::DependencyBlob, "markerComment")
    descriptor = None
    for klass in langc::DependencyBlob.__mro__:
        if "markerComment" in klass.__dict__:
            descriptor = klass.__dict__["markerComment"]
            break
    assert isinstance(descriptor, property)



def test_langc::filedependency_is_not_abstract():
    assert not inspect.isabstract(langc::FileDependency)


def test_langc::filedependency_constructor_exists():
    assert callable(langc::FileDependency.__init__)


def test_langc::filedependency_constructor_args():
    sig = inspect.signature(langc::FileDependency.__init__)
    params = list(sig.parameters.keys())



def test_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(ExpressionStatement)


def test_expressionstatement_constructor_exists():
    assert callable(ExpressionStatement.__init__)


def test_expressionstatement_constructor_args():
    sig = inspect.signature(ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_langc::returnstatement_is_not_abstract():
    assert not inspect.isabstract(langc::ReturnStatement)


def test_langc::returnstatement_constructor_exists():
    assert callable(langc::ReturnStatement.__init__)


def test_langc::returnstatement_constructor_args():
    sig = inspect.signature(langc::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_langc::switchstatement_is_not_abstract():
    assert not inspect.isabstract(langc::SwitchStatement)


def test_langc::switchstatement_constructor_exists():
    assert callable(langc::SwitchStatement.__init__)


def test_langc::switchstatement_constructor_args():
    sig = inspect.signature(langc::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_langc::breakstatement_is_not_abstract():
    assert not inspect.isabstract(langc::BreakStatement)


def test_langc::breakstatement_constructor_exists():
    assert callable(langc::BreakStatement.__init__)


def test_langc::breakstatement_constructor_args():
    sig = inspect.signature(langc::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_langc::variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(langc::VariableDeclarationStatement)


def test_langc::variabledeclarationstatement_constructor_exists():
    assert callable(langc::VariableDeclarationStatement.__init__)


def test_langc::variabledeclarationstatement_constructor_args():
    sig = inspect.signature(langc::VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_langc::codeblock_is_not_abstract():
    assert not inspect.isabstract(langc::CodeBlock)


def test_langc::codeblock_constructor_exists():
    assert callable(langc::CodeBlock.__init__)


def test_langc::codeblock_constructor_args():
    sig = inspect.signature(langc::CodeBlock.__init__)
    params = list(sig.parameters.keys())
    assert "forceBraces" in params, "Missing parameter 'forceBraces'"

def test_langc::codeblock_has_forceBraces():
    assert hasattr(langc::CodeBlock, "forceBraces")
    descriptor = None
    for klass in langc::CodeBlock.__mro__:
        if "forceBraces" in klass.__dict__:
            descriptor = klass.__dict__["forceBraces"]
            break
    assert isinstance(descriptor, property)



def test_langc::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(langc::ExpressionStatement)


def test_langc::expressionstatement_constructor_exists():
    assert callable(langc::ExpressionStatement.__init__)


def test_langc::expressionstatement_constructor_args():
    sig = inspect.signature(langc::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_langc::statement_is_not_abstract():
    assert not inspect.isabstract(langc::Statement)


def test_langc::statement_constructor_exists():
    assert callable(langc::Statement.__init__)


def test_langc::statement_constructor_args():
    sig = inspect.signature(langc::Statement.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_langc::floatingliteral_is_not_abstract():
    assert not inspect.isabstract(langc::FloatingLiteral)


def test_langc::floatingliteral_constructor_exists():
    assert callable(langc::FloatingLiteral.__init__)


def test_langc::floatingliteral_constructor_args():
    sig = inspect.signature(langc::FloatingLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_langc::floatingliteral_has_value():
    assert hasattr(langc::FloatingLiteral, "value")
    descriptor = None
    for klass in langc::FloatingLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_langc::characterliteral_is_not_abstract():
    assert not inspect.isabstract(langc::CharacterLiteral)


def test_langc::characterliteral_constructor_exists():
    assert callable(langc::CharacterLiteral.__init__)


def test_langc::characterliteral_constructor_args():
    sig = inspect.signature(langc::CharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_langc::characterliteral_has_value():
    assert hasattr(langc::CharacterLiteral, "value")
    descriptor = None
    for klass in langc::CharacterLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_langc::integralliteral_is_not_abstract():
    assert not inspect.isabstract(langc::IntegralLiteral)


def test_langc::integralliteral_constructor_exists():
    assert callable(langc::IntegralLiteral.__init__)


def test_langc::integralliteral_constructor_args():
    sig = inspect.signature(langc::IntegralLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "bytes" in params, "Missing parameter 'bytes'"
    assert "signed" in params, "Missing parameter 'signed'"
    assert "value" in params, "Missing parameter 'value'"

def test_langc::integralliteral_has_bytes():
    assert hasattr(langc::IntegralLiteral, "bytes")
    descriptor = None
    for klass in langc::IntegralLiteral.__mro__:
        if "bytes" in klass.__dict__:
            descriptor = klass.__dict__["bytes"]
            break
    assert isinstance(descriptor, property)

def test_langc::integralliteral_has_signed():
    assert hasattr(langc::IntegralLiteral, "signed")
    descriptor = None
    for klass in langc::IntegralLiteral.__mro__:
        if "signed" in klass.__dict__:
            descriptor = klass.__dict__["signed"]
            break
    assert isinstance(descriptor, property)

def test_langc::integralliteral_has_value():
    assert hasattr(langc::IntegralLiteral, "value")
    descriptor = None
    for klass in langc::IntegralLiteral.__mro__:
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



def test_langc::logicalcomparison_is_not_abstract():
    assert not inspect.isabstract(langc::LogicalComparison)


def test_langc::logicalcomparison_constructor_exists():
    assert callable(langc::LogicalComparison.__init__)


def test_langc::logicalcomparison_constructor_args():
    sig = inspect.signature(langc::LogicalComparison.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_langc::logicalcomparison_has_operator():
    assert hasattr(langc::LogicalComparison, "operator")
    descriptor = None
    for klass in langc::LogicalComparison.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_langc::castexpr_is_not_abstract():
    assert not inspect.isabstract(langc::CastExpr)


def test_langc::castexpr_constructor_exists():
    assert callable(langc::CastExpr.__init__)


def test_langc::castexpr_constructor_args():
    sig = inspect.signature(langc::CastExpr.__init__)
    params = list(sig.parameters.keys())



def test_langc::elementaccess_is_not_abstract():
    assert not inspect.isabstract(langc::ElementAccess)


def test_langc::elementaccess_constructor_exists():
    assert callable(langc::ElementAccess.__init__)


def test_langc::elementaccess_constructor_args():
    sig = inspect.signature(langc::ElementAccess.__init__)
    params = list(sig.parameters.keys())



def test_langc::sizeof_is_not_abstract():
    assert not inspect.isabstract(langc::Sizeof)


def test_langc::sizeof_constructor_exists():
    assert callable(langc::Sizeof.__init__)


def test_langc::sizeof_constructor_args():
    sig = inspect.signature(langc::Sizeof.__init__)
    params = list(sig.parameters.keys())



def test_langc::literal_is_not_abstract():
    assert not inspect.isabstract(langc::Literal)


def test_langc::literal_constructor_exists():
    assert callable(langc::Literal.__init__)


def test_langc::literal_constructor_args():
    sig = inspect.signature(langc::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"

def test_langc::literal_has_primitiveType():
    assert hasattr(langc::Literal, "primitiveType")
    descriptor = None
    for klass in langc::Literal.__mro__:
        if "primitiveType" in klass.__dict__:
            descriptor = klass.__dict__["primitiveType"]
            break
    assert isinstance(descriptor, property)



def test_langc::expressionblob_is_not_abstract():
    assert not inspect.isabstract(langc::ExpressionBlob)


def test_langc::expressionblob_constructor_exists():
    assert callable(langc::ExpressionBlob.__init__)


def test_langc::expressionblob_constructor_args():
    sig = inspect.signature(langc::ExpressionBlob.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_langc::expressionblob_has_text():
    assert hasattr(langc::ExpressionBlob, "text")
    descriptor = None
    for klass in langc::ExpressionBlob.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_langc::functionaddress_is_not_abstract():
    assert not inspect.isabstract(langc::FunctionAddress)


def test_langc::functionaddress_constructor_exists():
    assert callable(langc::FunctionAddress.__init__)


def test_langc::functionaddress_constructor_args():
    sig = inspect.signature(langc::FunctionAddress.__init__)
    params = list(sig.parameters.keys())



def test_langc::indexexpr_is_not_abstract():
    assert not inspect.isabstract(langc::IndexExpr)


def test_langc::indexexpr_constructor_exists():
    assert callable(langc::IndexExpr.__init__)


def test_langc::indexexpr_constructor_args():
    sig = inspect.signature(langc::IndexExpr.__init__)
    params = list(sig.parameters.keys())



def test_langc::binaryoperation_is_not_abstract():
    assert not inspect.isabstract(langc::BinaryOperation)


def test_langc::binaryoperation_constructor_exists():
    assert callable(langc::BinaryOperation.__init__)


def test_langc::binaryoperation_constructor_args():
    sig = inspect.signature(langc::BinaryOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_langc::binaryoperation_has_operator():
    assert hasattr(langc::BinaryOperation, "operator")
    descriptor = None
    for klass in langc::BinaryOperation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_langc::stringliteral_is_not_abstract():
    assert not inspect.isabstract(langc::StringLiteral)


def test_langc::stringliteral_constructor_exists():
    assert callable(langc::StringLiteral.__init__)


def test_langc::stringliteral_constructor_args():
    sig = inspect.signature(langc::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_langc::stringliteral_has_value():
    assert hasattr(langc::StringLiteral, "value")
    descriptor = None
    for klass in langc::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_langc::dereferenceexpr_is_not_abstract():
    assert not inspect.isabstract(langc::DereferenceExpr)


def test_langc::dereferenceexpr_constructor_exists():
    assert callable(langc::DereferenceExpr.__init__)


def test_langc::dereferenceexpr_constructor_args():
    sig = inspect.signature(langc::DereferenceExpr.__init__)
    params = list(sig.parameters.keys())



def test_langc::blockinitializer_is_not_abstract():
    assert not inspect.isabstract(langc::BlockInitializer)


def test_langc::blockinitializer_constructor_exists():
    assert callable(langc::BlockInitializer.__init__)


def test_langc::blockinitializer_constructor_args():
    sig = inspect.signature(langc::BlockInitializer.__init__)
    params = list(sig.parameters.keys())



def test_langc::addressofexpr_is_not_abstract():
    assert not inspect.isabstract(langc::AddressOfExpr)


def test_langc::addressofexpr_constructor_exists():
    assert callable(langc::AddressOfExpr.__init__)


def test_langc::addressofexpr_constructor_args():
    sig = inspect.signature(langc::AddressOfExpr.__init__)
    params = list(sig.parameters.keys())



def test_langc::functioncall_is_not_abstract():
    assert not inspect.isabstract(langc::FunctionCall)


def test_langc::functioncall_constructor_exists():
    assert callable(langc::FunctionCall.__init__)


def test_langc::functioncall_constructor_args():
    sig = inspect.signature(langc::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_langc::expression_is_not_abstract():
    assert not inspect.isabstract(langc::Expression)


def test_langc::expression_constructor_exists():
    assert callable(langc::Expression.__init__)


def test_langc::expression_constructor_args():
    sig = inspect.signature(langc::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "precendence" in params, "Missing parameter 'precendence'"

def test_langc::expression_has_precendence():
    assert hasattr(langc::Expression, "precendence")
    descriptor = None
    for klass in langc::Expression.__mro__:
        if "precendence" in klass.__dict__:
            descriptor = klass.__dict__["precendence"]
            break
    assert isinstance(descriptor, property)



def test_langc::element_is_not_abstract():
    assert not inspect.isabstract(langc::Element)


def test_langc::element_constructor_exists():
    assert callable(langc::Element.__init__)


def test_langc::element_constructor_args():
    sig = inspect.signature(langc::Element.__init__)
    params = list(sig.parameters.keys())



def test_langc::namedreference_is_not_abstract():
    assert not inspect.isabstract(langc::NamedReference)


def test_langc::namedreference_constructor_exists():
    assert callable(langc::NamedReference.__init__)


def test_langc::namedreference_constructor_args():
    sig = inspect.signature(langc::NamedReference.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_langc::enum_is_not_abstract():
    assert not inspect.isabstract(langc::Enum)


def test_langc::enum_constructor_exists():
    assert callable(langc::Enum.__init__)


def test_langc::enum_constructor_args():
    sig = inspect.signature(langc::Enum.__init__)
    params = list(sig.parameters.keys())



def test_langc::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(langc::VariableDeclaration)


def test_langc::variabledeclaration_constructor_exists():
    assert callable(langc::VariableDeclaration.__init__)


def test_langc::variabledeclaration_constructor_args():
    sig = inspect.signature(langc::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "linkage" in params, "Missing parameter 'linkage'"

def test_langc::variabledeclaration_has_linkage():
    assert hasattr(langc::VariableDeclaration, "linkage")
    descriptor = None
    for klass in langc::VariableDeclaration.__mro__:
        if "linkage" in klass.__dict__:
            descriptor = klass.__dict__["linkage"]
            break
    assert isinstance(descriptor, property)



def test_langc::typedef_is_not_abstract():
    assert not inspect.isabstract(langc::Typedef)


def test_langc::typedef_constructor_exists():
    assert callable(langc::Typedef.__init__)


def test_langc::typedef_constructor_args():
    sig = inspect.signature(langc::Typedef.__init__)
    params = list(sig.parameters.keys())



def test_langc::structure_is_not_abstract():
    assert not inspect.isabstract(langc::Structure)


def test_langc::structure_constructor_exists():
    assert callable(langc::Structure.__init__)


def test_langc::structure_constructor_args():
    sig = inspect.signature(langc::Structure.__init__)
    params = list(sig.parameters.keys())



def test_langc::function_is_not_abstract():
    assert not inspect.isabstract(langc::Function)


def test_langc::function_constructor_exists():
    assert callable(langc::Function.__init__)


def test_langc::function_constructor_args():
    sig = inspect.signature(langc::Function.__init__)
    params = list(sig.parameters.keys())
    assert "linkage" in params, "Missing parameter 'linkage'"

def test_langc::function_has_linkage():
    assert hasattr(langc::Function, "linkage")
    descriptor = None
    for klass in langc::Function.__mro__:
        if "linkage" in klass.__dict__:
            descriptor = klass.__dict__["linkage"]
            break
    assert isinstance(descriptor, property)



def test_structure_is_not_abstract():
    assert not inspect.isabstract(Structure)


def test_structure_constructor_exists():
    assert callable(Structure.__init__)


def test_structure_constructor_args():
    sig = inspect.signature(Structure.__init__)
    params = list(sig.parameters.keys())



def test_langc::union_is_not_abstract():
    assert not inspect.isabstract(langc::Union)


def test_langc::union_constructor_exists():
    assert callable(langc::Union.__init__)


def test_langc::union_constructor_args():
    sig = inspect.signature(langc::Union.__init__)
    params = list(sig.parameters.keys())



def test_langc::struct_is_not_abstract():
    assert not inspect.isabstract(langc::Struct)


def test_langc::struct_constructor_exists():
    assert callable(langc::Struct.__init__)


def test_langc::struct_constructor_args():
    sig = inspect.signature(langc::Struct.__init__)
    params = list(sig.parameters.keys())



def test_langc::directive_is_not_abstract():
    assert not inspect.isabstract(langc::Directive)


def test_langc::directive_constructor_exists():
    assert callable(langc::Directive.__init__)


def test_langc::directive_constructor_args():
    sig = inspect.signature(langc::Directive.__init__)
    params = list(sig.parameters.keys())



def test_langc::dependencylist_is_not_abstract():
    assert not inspect.isabstract(langc::DependencyList)


def test_langc::dependencylist_constructor_exists():
    assert callable(langc::DependencyList.__init__)


def test_langc::dependencylist_constructor_args():
    sig = inspect.signature(langc::DependencyList.__init__)
    params = list(sig.parameters.keys())



def test_langc::filename_is_not_abstract():
    assert not inspect.isabstract(langc::FileName)


def test_langc::filename_constructor_exists():
    assert callable(langc::FileName.__init__)


def test_langc::filename_constructor_args():
    sig = inspect.signature(langc::FileName.__init__)
    params = list(sig.parameters.keys())
    assert "hasObjectCode" in params, "Missing parameter 'hasObjectCode'"

def test_langc::filename_has_hasObjectCode():
    assert hasattr(langc::FileName, "hasObjectCode")
    descriptor = None
    for klass in langc::FileName.__mro__:
        if "hasObjectCode" in klass.__dict__:
            descriptor = klass.__dict__["hasObjectCode"]
            break
    assert isinstance(descriptor, property)



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_langc::builtintype_is_not_abstract():
    assert not inspect.isabstract(langc::BuiltInType)


def test_langc::builtintype_constructor_exists():
    assert callable(langc::BuiltInType.__init__)


def test_langc::builtintype_constructor_args():
    sig = inspect.signature(langc::BuiltInType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_langc::builtintype_has_type():
    assert hasattr(langc::BuiltInType, "type")
    descriptor = None
    for klass in langc::BuiltInType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_langc::userelement_is_not_abstract():
    assert not inspect.isabstract(langc::UserElement)


def test_langc::userelement_constructor_exists():
    assert callable(langc::UserElement.__init__)


def test_langc::userelement_constructor_args():
    sig = inspect.signature(langc::UserElement.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_langc::userelement_has_kind():
    assert hasattr(langc::UserElement, "kind")
    descriptor = None
    for klass in langc::UserElement.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_langc::elementlist_is_not_abstract():
    assert not inspect.isabstract(langc::ElementList)


def test_langc::elementlist_constructor_exists():
    assert callable(langc::ElementList.__init__)


def test_langc::elementlist_constructor_args():
    sig = inspect.signature(langc::ElementList.__init__)
    params = list(sig.parameters.keys())



def test_langc::name_is_not_abstract():
    assert not inspect.isabstract(langc::Name)


def test_langc::name_constructor_exists():
    assert callable(langc::Name.__init__)


def test_langc::name_constructor_args():
    sig = inspect.signature(langc::Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_langc::name_has_name():
    assert hasattr(langc::Name, "name")
    descriptor = None
    for klass in langc::Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bindablevalue_is_not_abstract():
    assert not inspect.isabstract(BindableValue)


def test_bindablevalue_constructor_exists():
    assert callable(BindableValue.__init__)


def test_bindablevalue_constructor_args():
    sig = inspect.signature(BindableValue.__init__)
    params = list(sig.parameters.keys())



def test_langc::elementreference_is_not_abstract():
    assert not inspect.isabstract(langc::ElementReference)


def test_langc::elementreference_constructor_exists():
    assert callable(langc::ElementReference.__init__)


def test_langc::elementreference_constructor_args():
    sig = inspect.signature(langc::ElementReference.__init__)
    params = list(sig.parameters.keys())
    assert "cvQualifier" in params, "Missing parameter 'cvQualifier'"
    assert "pointerSpec" in params, "Missing parameter 'pointerSpec'"

def test_langc::elementreference_has_cvQualifier():
    assert hasattr(langc::ElementReference, "cvQualifier")
    descriptor = None
    for klass in langc::ElementReference.__mro__:
        if "cvQualifier" in klass.__dict__:
            descriptor = klass.__dict__["cvQualifier"]
            break
    assert isinstance(descriptor, property)

def test_langc::elementreference_has_pointerSpec():
    assert hasattr(langc::ElementReference, "pointerSpec")
    descriptor = None
    for klass in langc::ElementReference.__mro__:
        if "pointerSpec" in klass.__dict__:
            descriptor = klass.__dict__["pointerSpec"]
            break
    assert isinstance(descriptor, property)



def test_langc::enumerator_is_not_abstract():
    assert not inspect.isabstract(langc::Enumerator)


def test_langc::enumerator_constructor_exists():
    assert callable(langc::Enumerator.__init__)


def test_langc::enumerator_constructor_args():
    sig = inspect.signature(langc::Enumerator.__init__)
    params = list(sig.parameters.keys())



def test_langc::macro_is_not_abstract():
    assert not inspect.isabstract(langc::Macro)


def test_langc::macro_constructor_exists():
    assert callable(langc::Macro.__init__)


def test_langc::macro_constructor_args():
    sig = inspect.signature(langc::Macro.__init__)
    params = list(sig.parameters.keys())



def test_userelement_is_not_abstract():
    assert not inspect.isabstract(UserElement)


def test_userelement_constructor_exists():
    assert callable(UserElement.__init__)


def test_userelement_constructor_args():
    sig = inspect.signature(UserElement.__init__)
    params = list(sig.parameters.keys())



def test_langc::functionpointer_is_not_abstract():
    assert not inspect.isabstract(langc::FunctionPointer)


def test_langc::functionpointer_constructor_exists():
    assert callable(langc::FunctionPointer.__init__)


def test_langc::functionpointer_constructor_args():
    sig = inspect.signature(langc::FunctionPointer.__init__)
    params = list(sig.parameters.keys())



def test_langc::functionimplementation_is_not_abstract():
    assert not inspect.isabstract(langc::FunctionImplementation)


def test_langc::functionimplementation_constructor_exists():
    assert callable(langc::FunctionImplementation.__init__)


def test_langc::functionimplementation_constructor_args():
    sig = inspect.signature(langc::FunctionImplementation.__init__)
    params = list(sig.parameters.keys())



def test_langc::namedelement_is_not_abstract():
    assert not inspect.isabstract(langc::NamedElement)


def test_langc::namedelement_constructor_exists():
    assert callable(langc::NamedElement.__init__)


def test_langc::namedelement_constructor_args():
    sig = inspect.signature(langc::NamedElement.__init__)
    params = list(sig.parameters.keys())

def test_pointer_exists():
    # Check that the Enumeration exists
    assert Pointer is not None

def test_pointer_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Pointer]
    expected_literals = [
        "const_volatile_pointer",
        "invalid",
        "pointer",
        "volatile_pointer",
        "const_pointer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Pointer"

def test_cvqualifier_exists():
    # Check that the Enumeration exists
    assert CVQualifier is not None

def test_cvqualifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CVQualifier]
    expected_literals = [
        "volatile",
        "unqualified",
        "const",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CVQualifier"

def test_linkagespec_exists():
    # Check that the Enumeration exists
    assert LinkageSpec is not None

def test_linkagespec_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LinkageSpec]
    expected_literals = [
        "unspecified",
        "extern",
        "static",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LinkageSpec"

def test_booleanoperator_exists():
    # Check that the Enumeration exists
    assert BooleanOperator is not None

def test_booleanoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanOperator]
    expected_literals = [
        "or_",
        "and_",
        "less_than",
        "equivalent",
        "greater_than",
        "less_than_equal",
        "not_equivalent",
        "greater_than_equal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanOperator"

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "bitwise_and",
        "assign",
        "add",
        "subtract",
        "bitwise_or",
        "assign_add",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"

def test_elementkind_exists():
    # Check that the Enumeration exists
    assert ElementKind is not None

def test_elementkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ElementKind]
    expected_literals = [
        "headerOnly",
        "implOnly",
        "default",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ElementKind"

def test_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "int8",
        "char",
        "long",
        "int32",
        "void",
        "uint32",
        "uint16",
        "uint8",
        "int16",
        "float",
        "double",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveType"


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
langc::LinkableArtifact_strategy = st.builds(
    langc::LinkableArtifact,
    name=
        safe_text
)
langc::System_strategy = st.builds(
    langc::System,
)
SwitchClause_strategy = st.builds(
    SwitchClause,
)
langc::LabeledClause_strategy = st.builds(
    langc::LabeledClause,
)
CodeBlock_strategy = st.builds(
    CodeBlock,
)
langc::CodeBlob_strategy = st.builds(
    langc::CodeBlob,
    text=
        safe_text,
    markerComment=
        safe_text
)
langc::ConditionalStatement_strategy = st.builds(
    langc::ConditionalStatement,
)
langc::SwitchClause_strategy = st.builds(
    langc::SwitchClause,
    fallthrough=
        st.booleans()
)
FileName_strategy = st.builds(
    FileName,
)
langc::SystemFileName_strategy = st.builds(
    langc::SystemFileName,
)
langc::BindableValue_strategy = st.builds(
    langc::BindableValue,
)
Sizeof_strategy = st.builds(
    Sizeof,
)
langc::SizeofExpr_strategy = st.builds(
    langc::SizeofExpr,
)
langc::SizeofType_strategy = st.builds(
    langc::SizeofType,
)
langc::Dependency_strategy = st.builds(
    langc::Dependency,
)
Directive_strategy = st.builds(
    Directive,
)
langc::WhileStatement_strategy = st.builds(
    langc::WhileStatement,
)
langc::SubSystem_strategy = st.builds(
    langc::SubSystem,
    name=
        safe_text
)
ElementAccess_strategy = st.builds(
    ElementAccess,
)
langc::MemberAccess_strategy = st.builds(
    langc::MemberAccess,
)
Name_strategy = st.builds(
    Name,
)
langc::FolderName_strategy = st.builds(
    langc::FolderName,
    api=
        st.booleans()
)
FileDependency_strategy = st.builds(
    FileDependency,
)
langc::UserInclude_strategy = st.builds(
    langc::UserInclude,
)
langc::SystemInclude_strategy = st.builds(
    langc::SystemInclude,
)
Dependency_strategy = st.builds(
    Dependency,
)
langc::DependencyBlob_strategy = st.builds(
    langc::DependencyBlob,
    text=
        safe_text,
    markerComment=
        safe_text
)
langc::FileDependency_strategy = st.builds(
    langc::FileDependency,
)
ExpressionStatement_strategy = st.builds(
    ExpressionStatement,
)
langc::ReturnStatement_strategy = st.builds(
    langc::ReturnStatement,
)
Statement_strategy = st.builds(
    Statement,
)
langc::SwitchStatement_strategy = st.builds(
    langc::SwitchStatement,
)
langc::BreakStatement_strategy = st.builds(
    langc::BreakStatement,
)
langc::VariableDeclarationStatement_strategy = st.builds(
    langc::VariableDeclarationStatement,
)
langc::CodeBlock_strategy = st.builds(
    langc::CodeBlock,
    forceBraces=
        st.booleans()
)
langc::ExpressionStatement_strategy = st.builds(
    langc::ExpressionStatement,
)
langc::Statement_strategy = st.builds(
    langc::Statement,
)
Literal_strategy = st.builds(
    Literal,
)
langc::FloatingLiteral_strategy = st.builds(
    langc::FloatingLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
langc::CharacterLiteral_strategy = st.builds(
    langc::CharacterLiteral,
    value=
        safe_text
)
langc::IntegralLiteral_strategy = st.builds(
    langc::IntegralLiteral,
    bytes=
        safe_text,
    signed=
        st.booleans(),
    value=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
langc::LogicalComparison_strategy = st.builds(
    langc::LogicalComparison,
    operator=
        safe_text
)
langc::CastExpr_strategy = st.builds(
    langc::CastExpr,
)
langc::ElementAccess_strategy = st.builds(
    langc::ElementAccess,
)
langc::Sizeof_strategy = st.builds(
    langc::Sizeof,
)
langc::Literal_strategy = st.builds(
    langc::Literal,
    primitiveType=
        safe_text
)
langc::ExpressionBlob_strategy = st.builds(
    langc::ExpressionBlob,
    text=
        safe_text
)
langc::FunctionAddress_strategy = st.builds(
    langc::FunctionAddress,
)
langc::IndexExpr_strategy = st.builds(
    langc::IndexExpr,
)
langc::BinaryOperation_strategy = st.builds(
    langc::BinaryOperation,
    operator=
        safe_text
)
langc::StringLiteral_strategy = st.builds(
    langc::StringLiteral,
    value=
        safe_text
)
langc::DereferenceExpr_strategy = st.builds(
    langc::DereferenceExpr,
)
langc::BlockInitializer_strategy = st.builds(
    langc::BlockInitializer,
)
langc::AddressOfExpr_strategy = st.builds(
    langc::AddressOfExpr,
)
langc::FunctionCall_strategy = st.builds(
    langc::FunctionCall,
)
langc::Expression_strategy = st.builds(
    langc::Expression,
    precendence=
        st.integers()
)
langc::Element_strategy = st.builds(
    langc::Element,
)
langc::NamedReference_strategy = st.builds(
    langc::NamedReference,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
langc::Enum_strategy = st.builds(
    langc::Enum,
)
langc::VariableDeclaration_strategy = st.builds(
    langc::VariableDeclaration,
    linkage=
        safe_text
)
langc::Typedef_strategy = st.builds(
    langc::Typedef,
)
langc::Structure_strategy = st.builds(
    langc::Structure,
)
langc::Function_strategy = st.builds(
    langc::Function,
    linkage=
        safe_text
)
Structure_strategy = st.builds(
    Structure,
)
langc::Union_strategy = st.builds(
    langc::Union,
)
langc::Struct_strategy = st.builds(
    langc::Struct,
)
langc::Directive_strategy = st.builds(
    langc::Directive,
)
langc::DependencyList_strategy = st.builds(
    langc::DependencyList,
)
langc::FileName_strategy = st.builds(
    langc::FileName,
    hasObjectCode=
        st.booleans()
)
Element_strategy = st.builds(
    Element,
)
langc::BuiltInType_strategy = st.builds(
    langc::BuiltInType,
    type=
        safe_text
)
langc::UserElement_strategy = st.builds(
    langc::UserElement,
    kind=
        safe_text
)
langc::ElementList_strategy = st.builds(
    langc::ElementList,
)
langc::Name_strategy = st.builds(
    langc::Name,
    name=
        safe_text
)
BindableValue_strategy = st.builds(
    BindableValue,
)
langc::ElementReference_strategy = st.builds(
    langc::ElementReference,
    cvQualifier=
        safe_text,
    pointerSpec=
        safe_text
)
langc::Enumerator_strategy = st.builds(
    langc::Enumerator,
)
langc::Macro_strategy = st.builds(
    langc::Macro,
)
UserElement_strategy = st.builds(
    UserElement,
)
langc::FunctionPointer_strategy = st.builds(
    langc::FunctionPointer,
)
langc::FunctionImplementation_strategy = st.builds(
    langc::FunctionImplementation,
)
langc::NamedElement_strategy = st.builds(
    langc::NamedElement,
)

@given(instance=langc::LinkableArtifact_strategy)
@settings(max_examples=50)
def test_langc::linkableartifact_instantiation(instance):
    assert isinstance(instance, langc::LinkableArtifact)

@given(instance=langc::LinkableArtifact_strategy)
def test_langc::linkableartifact_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=langc::LinkableArtifact_strategy)
def test_langc::linkableartifact_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=langc::System_strategy)
@settings(max_examples=50)
def test_langc::system_instantiation(instance):
    assert isinstance(instance, langc::System)

@given(instance=SwitchClause_strategy)
@settings(max_examples=50)
def test_switchclause_instantiation(instance):
    assert isinstance(instance, SwitchClause)

@given(instance=langc::LabeledClause_strategy)
@settings(max_examples=50)
def test_langc::labeledclause_instantiation(instance):
    assert isinstance(instance, langc::LabeledClause)

@given(instance=CodeBlock_strategy)
@settings(max_examples=50)
def test_codeblock_instantiation(instance):
    assert isinstance(instance, CodeBlock)

@given(instance=langc::CodeBlob_strategy)
@settings(max_examples=50)
def test_langc::codeblob_instantiation(instance):
    assert isinstance(instance, langc::CodeBlob)

@given(instance=langc::CodeBlob_strategy)
def test_langc::codeblob_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=langc::CodeBlob_strategy)
def test_langc::codeblob_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=langc::CodeBlob_strategy)
def test_langc::codeblob_markerComment_type(instance):
    assert isinstance(instance.markerComment, str)


@given(instance=langc::CodeBlob_strategy)
def test_langc::codeblob_markerComment_setter(instance):
    original = instance.markerComment
    instance.markerComment = original
    assert instance.markerComment == original

@given(instance=langc::ConditionalStatement_strategy)
@settings(max_examples=50)
def test_langc::conditionalstatement_instantiation(instance):
    assert isinstance(instance, langc::ConditionalStatement)

@given(instance=langc::SwitchClause_strategy)
@settings(max_examples=50)
def test_langc::switchclause_instantiation(instance):
    assert isinstance(instance, langc::SwitchClause)

@given(instance=langc::SwitchClause_strategy)
def test_langc::switchclause_fallthrough_type(instance):
    assert isinstance(instance.fallthrough, bool)


@given(instance=langc::SwitchClause_strategy)
def test_langc::switchclause_fallthrough_setter(instance):
    original = instance.fallthrough
    instance.fallthrough = original
    assert instance.fallthrough == original

@given(instance=FileName_strategy)
@settings(max_examples=50)
def test_filename_instantiation(instance):
    assert isinstance(instance, FileName)

@given(instance=langc::SystemFileName_strategy)
@settings(max_examples=50)
def test_langc::systemfilename_instantiation(instance):
    assert isinstance(instance, langc::SystemFileName)

@given(instance=langc::BindableValue_strategy)
@settings(max_examples=50)
def test_langc::bindablevalue_instantiation(instance):
    assert isinstance(instance, langc::BindableValue)

@given(instance=Sizeof_strategy)
@settings(max_examples=50)
def test_sizeof_instantiation(instance):
    assert isinstance(instance, Sizeof)

@given(instance=langc::SizeofExpr_strategy)
@settings(max_examples=50)
def test_langc::sizeofexpr_instantiation(instance):
    assert isinstance(instance, langc::SizeofExpr)

@given(instance=langc::SizeofType_strategy)
@settings(max_examples=50)
def test_langc::sizeoftype_instantiation(instance):
    assert isinstance(instance, langc::SizeofType)

@given(instance=langc::Dependency_strategy)
@settings(max_examples=50)
def test_langc::dependency_instantiation(instance):
    assert isinstance(instance, langc::Dependency)

@given(instance=Directive_strategy)
@settings(max_examples=50)
def test_directive_instantiation(instance):
    assert isinstance(instance, Directive)

@given(instance=langc::WhileStatement_strategy)
@settings(max_examples=50)
def test_langc::whilestatement_instantiation(instance):
    assert isinstance(instance, langc::WhileStatement)

@given(instance=langc::SubSystem_strategy)
@settings(max_examples=50)
def test_langc::subsystem_instantiation(instance):
    assert isinstance(instance, langc::SubSystem)

@given(instance=langc::SubSystem_strategy)
def test_langc::subsystem_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=langc::SubSystem_strategy)
def test_langc::subsystem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ElementAccess_strategy)
@settings(max_examples=50)
def test_elementaccess_instantiation(instance):
    assert isinstance(instance, ElementAccess)

@given(instance=langc::MemberAccess_strategy)
@settings(max_examples=50)
def test_langc::memberaccess_instantiation(instance):
    assert isinstance(instance, langc::MemberAccess)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=langc::FolderName_strategy)
@settings(max_examples=50)
def test_langc::foldername_instantiation(instance):
    assert isinstance(instance, langc::FolderName)

@given(instance=langc::FolderName_strategy)
def test_langc::foldername_api_type(instance):
    assert isinstance(instance.api, bool)


@given(instance=langc::FolderName_strategy)
def test_langc::foldername_api_setter(instance):
    original = instance.api
    instance.api = original
    assert instance.api == original

@given(instance=FileDependency_strategy)
@settings(max_examples=50)
def test_filedependency_instantiation(instance):
    assert isinstance(instance, FileDependency)

@given(instance=langc::UserInclude_strategy)
@settings(max_examples=50)
def test_langc::userinclude_instantiation(instance):
    assert isinstance(instance, langc::UserInclude)

@given(instance=langc::SystemInclude_strategy)
@settings(max_examples=50)
def test_langc::systeminclude_instantiation(instance):
    assert isinstance(instance, langc::SystemInclude)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=langc::DependencyBlob_strategy)
@settings(max_examples=50)
def test_langc::dependencyblob_instantiation(instance):
    assert isinstance(instance, langc::DependencyBlob)

@given(instance=langc::DependencyBlob_strategy)
def test_langc::dependencyblob_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=langc::DependencyBlob_strategy)
def test_langc::dependencyblob_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=langc::DependencyBlob_strategy)
def test_langc::dependencyblob_markerComment_type(instance):
    assert isinstance(instance.markerComment, str)


@given(instance=langc::DependencyBlob_strategy)
def test_langc::dependencyblob_markerComment_setter(instance):
    original = instance.markerComment
    instance.markerComment = original
    assert instance.markerComment == original

@given(instance=langc::FileDependency_strategy)
@settings(max_examples=50)
def test_langc::filedependency_instantiation(instance):
    assert isinstance(instance, langc::FileDependency)

@given(instance=ExpressionStatement_strategy)
@settings(max_examples=50)
def test_expressionstatement_instantiation(instance):
    assert isinstance(instance, ExpressionStatement)

@given(instance=langc::ReturnStatement_strategy)
@settings(max_examples=50)
def test_langc::returnstatement_instantiation(instance):
    assert isinstance(instance, langc::ReturnStatement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=langc::SwitchStatement_strategy)
@settings(max_examples=50)
def test_langc::switchstatement_instantiation(instance):
    assert isinstance(instance, langc::SwitchStatement)

@given(instance=langc::BreakStatement_strategy)
@settings(max_examples=50)
def test_langc::breakstatement_instantiation(instance):
    assert isinstance(instance, langc::BreakStatement)

@given(instance=langc::VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_langc::variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, langc::VariableDeclarationStatement)

@given(instance=langc::CodeBlock_strategy)
@settings(max_examples=50)
def test_langc::codeblock_instantiation(instance):
    assert isinstance(instance, langc::CodeBlock)

@given(instance=langc::CodeBlock_strategy)
def test_langc::codeblock_forceBraces_type(instance):
    assert isinstance(instance.forceBraces, bool)


@given(instance=langc::CodeBlock_strategy)
def test_langc::codeblock_forceBraces_setter(instance):
    original = instance.forceBraces
    instance.forceBraces = original
    assert instance.forceBraces == original

@given(instance=langc::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_langc::expressionstatement_instantiation(instance):
    assert isinstance(instance, langc::ExpressionStatement)

@given(instance=langc::Statement_strategy)
@settings(max_examples=50)
def test_langc::statement_instantiation(instance):
    assert isinstance(instance, langc::Statement)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=langc::FloatingLiteral_strategy)
@settings(max_examples=50)
def test_langc::floatingliteral_instantiation(instance):
    assert isinstance(instance, langc::FloatingLiteral)

@given(instance=langc::FloatingLiteral_strategy)
def test_langc::floatingliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=langc::FloatingLiteral_strategy)
def test_langc::floatingliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=langc::CharacterLiteral_strategy)
@settings(max_examples=50)
def test_langc::characterliteral_instantiation(instance):
    assert isinstance(instance, langc::CharacterLiteral)

@given(instance=langc::CharacterLiteral_strategy)
def test_langc::characterliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=langc::CharacterLiteral_strategy)
def test_langc::characterliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=langc::IntegralLiteral_strategy)
@settings(max_examples=50)
def test_langc::integralliteral_instantiation(instance):
    assert isinstance(instance, langc::IntegralLiteral)

@given(instance=langc::IntegralLiteral_strategy)
def test_langc::integralliteral_bytes_type(instance):
    assert isinstance(instance.bytes, str)


@given(instance=langc::IntegralLiteral_strategy)
def test_langc::integralliteral_bytes_setter(instance):
    original = instance.bytes
    instance.bytes = original
    assert instance.bytes == original

@given(instance=langc::IntegralLiteral_strategy)
def test_langc::integralliteral_signed_type(instance):
    assert isinstance(instance.signed, bool)


@given(instance=langc::IntegralLiteral_strategy)
def test_langc::integralliteral_signed_setter(instance):
    original = instance.signed
    instance.signed = original
    assert instance.signed == original

@given(instance=langc::IntegralLiteral_strategy)
def test_langc::integralliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=langc::IntegralLiteral_strategy)
def test_langc::integralliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=langc::LogicalComparison_strategy)
@settings(max_examples=50)
def test_langc::logicalcomparison_instantiation(instance):
    assert isinstance(instance, langc::LogicalComparison)

@given(instance=langc::LogicalComparison_strategy)
def test_langc::logicalcomparison_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=langc::LogicalComparison_strategy)
def test_langc::logicalcomparison_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=langc::CastExpr_strategy)
@settings(max_examples=50)
def test_langc::castexpr_instantiation(instance):
    assert isinstance(instance, langc::CastExpr)

@given(instance=langc::ElementAccess_strategy)
@settings(max_examples=50)
def test_langc::elementaccess_instantiation(instance):
    assert isinstance(instance, langc::ElementAccess)

@given(instance=langc::Sizeof_strategy)
@settings(max_examples=50)
def test_langc::sizeof_instantiation(instance):
    assert isinstance(instance, langc::Sizeof)

@given(instance=langc::Literal_strategy)
@settings(max_examples=50)
def test_langc::literal_instantiation(instance):
    assert isinstance(instance, langc::Literal)

@given(instance=langc::Literal_strategy)
def test_langc::literal_primitiveType_type(instance):
    assert isinstance(instance.primitiveType, str)


@given(instance=langc::Literal_strategy)
def test_langc::literal_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original

@given(instance=langc::ExpressionBlob_strategy)
@settings(max_examples=50)
def test_langc::expressionblob_instantiation(instance):
    assert isinstance(instance, langc::ExpressionBlob)

@given(instance=langc::ExpressionBlob_strategy)
def test_langc::expressionblob_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=langc::ExpressionBlob_strategy)
def test_langc::expressionblob_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=langc::FunctionAddress_strategy)
@settings(max_examples=50)
def test_langc::functionaddress_instantiation(instance):
    assert isinstance(instance, langc::FunctionAddress)

@given(instance=langc::IndexExpr_strategy)
@settings(max_examples=50)
def test_langc::indexexpr_instantiation(instance):
    assert isinstance(instance, langc::IndexExpr)

@given(instance=langc::BinaryOperation_strategy)
@settings(max_examples=50)
def test_langc::binaryoperation_instantiation(instance):
    assert isinstance(instance, langc::BinaryOperation)

@given(instance=langc::BinaryOperation_strategy)
def test_langc::binaryoperation_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=langc::BinaryOperation_strategy)
def test_langc::binaryoperation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=langc::StringLiteral_strategy)
@settings(max_examples=50)
def test_langc::stringliteral_instantiation(instance):
    assert isinstance(instance, langc::StringLiteral)

@given(instance=langc::StringLiteral_strategy)
def test_langc::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=langc::StringLiteral_strategy)
def test_langc::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=langc::DereferenceExpr_strategy)
@settings(max_examples=50)
def test_langc::dereferenceexpr_instantiation(instance):
    assert isinstance(instance, langc::DereferenceExpr)

@given(instance=langc::BlockInitializer_strategy)
@settings(max_examples=50)
def test_langc::blockinitializer_instantiation(instance):
    assert isinstance(instance, langc::BlockInitializer)

@given(instance=langc::AddressOfExpr_strategy)
@settings(max_examples=50)
def test_langc::addressofexpr_instantiation(instance):
    assert isinstance(instance, langc::AddressOfExpr)

@given(instance=langc::FunctionCall_strategy)
@settings(max_examples=50)
def test_langc::functioncall_instantiation(instance):
    assert isinstance(instance, langc::FunctionCall)

@given(instance=langc::Expression_strategy)
@settings(max_examples=50)
def test_langc::expression_instantiation(instance):
    assert isinstance(instance, langc::Expression)

@given(instance=langc::Expression_strategy)
def test_langc::expression_precendence_type(instance):
    assert isinstance(instance.precendence, int)


@given(instance=langc::Expression_strategy)
def test_langc::expression_precendence_setter(instance):
    original = instance.precendence
    instance.precendence = original
    assert instance.precendence == original

@given(instance=langc::Element_strategy)
@settings(max_examples=50)
def test_langc::element_instantiation(instance):
    assert isinstance(instance, langc::Element)

@given(instance=langc::NamedReference_strategy)
@settings(max_examples=50)
def test_langc::namedreference_instantiation(instance):
    assert isinstance(instance, langc::NamedReference)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=langc::Enum_strategy)
@settings(max_examples=50)
def test_langc::enum_instantiation(instance):
    assert isinstance(instance, langc::Enum)

@given(instance=langc::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_langc::variabledeclaration_instantiation(instance):
    assert isinstance(instance, langc::VariableDeclaration)

@given(instance=langc::VariableDeclaration_strategy)
def test_langc::variabledeclaration_linkage_type(instance):
    assert isinstance(instance.linkage, str)


@given(instance=langc::VariableDeclaration_strategy)
def test_langc::variabledeclaration_linkage_setter(instance):
    original = instance.linkage
    instance.linkage = original
    assert instance.linkage == original

@given(instance=langc::Typedef_strategy)
@settings(max_examples=50)
def test_langc::typedef_instantiation(instance):
    assert isinstance(instance, langc::Typedef)

@given(instance=langc::Structure_strategy)
@settings(max_examples=50)
def test_langc::structure_instantiation(instance):
    assert isinstance(instance, langc::Structure)

@given(instance=langc::Function_strategy)
@settings(max_examples=50)
def test_langc::function_instantiation(instance):
    assert isinstance(instance, langc::Function)

@given(instance=langc::Function_strategy)
def test_langc::function_linkage_type(instance):
    assert isinstance(instance.linkage, str)


@given(instance=langc::Function_strategy)
def test_langc::function_linkage_setter(instance):
    original = instance.linkage
    instance.linkage = original
    assert instance.linkage == original

@given(instance=Structure_strategy)
@settings(max_examples=50)
def test_structure_instantiation(instance):
    assert isinstance(instance, Structure)

@given(instance=langc::Union_strategy)
@settings(max_examples=50)
def test_langc::union_instantiation(instance):
    assert isinstance(instance, langc::Union)

@given(instance=langc::Struct_strategy)
@settings(max_examples=50)
def test_langc::struct_instantiation(instance):
    assert isinstance(instance, langc::Struct)

@given(instance=langc::Directive_strategy)
@settings(max_examples=50)
def test_langc::directive_instantiation(instance):
    assert isinstance(instance, langc::Directive)

@given(instance=langc::DependencyList_strategy)
@settings(max_examples=50)
def test_langc::dependencylist_instantiation(instance):
    assert isinstance(instance, langc::DependencyList)

@given(instance=langc::FileName_strategy)
@settings(max_examples=50)
def test_langc::filename_instantiation(instance):
    assert isinstance(instance, langc::FileName)

@given(instance=langc::FileName_strategy)
def test_langc::filename_hasObjectCode_type(instance):
    assert isinstance(instance.hasObjectCode, bool)


@given(instance=langc::FileName_strategy)
def test_langc::filename_hasObjectCode_setter(instance):
    original = instance.hasObjectCode
    instance.hasObjectCode = original
    assert instance.hasObjectCode == original

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=langc::BuiltInType_strategy)
@settings(max_examples=50)
def test_langc::builtintype_instantiation(instance):
    assert isinstance(instance, langc::BuiltInType)

@given(instance=langc::BuiltInType_strategy)
def test_langc::builtintype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=langc::BuiltInType_strategy)
def test_langc::builtintype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=langc::UserElement_strategy)
@settings(max_examples=50)
def test_langc::userelement_instantiation(instance):
    assert isinstance(instance, langc::UserElement)

@given(instance=langc::UserElement_strategy)
def test_langc::userelement_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=langc::UserElement_strategy)
def test_langc::userelement_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=langc::ElementList_strategy)
@settings(max_examples=50)
def test_langc::elementlist_instantiation(instance):
    assert isinstance(instance, langc::ElementList)

@given(instance=langc::Name_strategy)
@settings(max_examples=50)
def test_langc::name_instantiation(instance):
    assert isinstance(instance, langc::Name)

@given(instance=langc::Name_strategy)
def test_langc::name_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=langc::Name_strategy)
def test_langc::name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BindableValue_strategy)
@settings(max_examples=50)
def test_bindablevalue_instantiation(instance):
    assert isinstance(instance, BindableValue)

@given(instance=langc::ElementReference_strategy)
@settings(max_examples=50)
def test_langc::elementreference_instantiation(instance):
    assert isinstance(instance, langc::ElementReference)

@given(instance=langc::ElementReference_strategy)
def test_langc::elementreference_cvQualifier_type(instance):
    assert isinstance(instance.cvQualifier, str)


@given(instance=langc::ElementReference_strategy)
def test_langc::elementreference_cvQualifier_setter(instance):
    original = instance.cvQualifier
    instance.cvQualifier = original
    assert instance.cvQualifier == original

@given(instance=langc::ElementReference_strategy)
def test_langc::elementreference_pointerSpec_type(instance):
    assert isinstance(instance.pointerSpec, str)


@given(instance=langc::ElementReference_strategy)
def test_langc::elementreference_pointerSpec_setter(instance):
    original = instance.pointerSpec
    instance.pointerSpec = original
    assert instance.pointerSpec == original

@given(instance=langc::Enumerator_strategy)
@settings(max_examples=50)
def test_langc::enumerator_instantiation(instance):
    assert isinstance(instance, langc::Enumerator)

@given(instance=langc::Macro_strategy)
@settings(max_examples=50)
def test_langc::macro_instantiation(instance):
    assert isinstance(instance, langc::Macro)

@given(instance=UserElement_strategy)
@settings(max_examples=50)
def test_userelement_instantiation(instance):
    assert isinstance(instance, UserElement)

@given(instance=langc::FunctionPointer_strategy)
@settings(max_examples=50)
def test_langc::functionpointer_instantiation(instance):
    assert isinstance(instance, langc::FunctionPointer)

@given(instance=langc::FunctionImplementation_strategy)
@settings(max_examples=50)
def test_langc::functionimplementation_instantiation(instance):
    assert isinstance(instance, langc::FunctionImplementation)

@given(instance=langc::NamedElement_strategy)
@settings(max_examples=50)
def test_langc::namedelement_instantiation(instance):
    assert isinstance(instance, langc::NamedElement)

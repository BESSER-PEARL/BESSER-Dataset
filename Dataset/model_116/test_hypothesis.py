import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dsl::DefaultValue,
    dsl::AnnotationTypeMemberDeclaration,
    dsl::AnnotationTypeBody,
    dsl::MemberValueArrayInitializer,
    DefaultValue,
    dsl::MemberValuePair,
    dsl::MemberValue,
    dsl::MemberValuePairs,
    dsl::Annotation,
    dsl::StatementExpressionList,
    dsl::ForUpdate,
    dsl::ForInit,
    dsl::SwitchLabel,
    dsl::LocalVariableDeclaration,
    dsl::TryStatement,
    dsl::SynchronizedStatement,
    dsl::ThrowStatement,
    dsl::ReturnStatement,
    dsl::ContinueStatement,
    dsl::BreakStatement,
    dsl::ForStatement,
    dsl::DoStatement,
    dsl::WhileStatement,
    dsl::IfStatement,
    dsl::SwitchStatement,
    dsl::StatementExpression,
    dsl::AssertStatement,
    dsl::LabeledStatement,
    dsl::ArrayDimsAndInits,
    dsl::BaseLiteral,
    dsl::ArgumentList,
    dsl::BooleanLiteral,
    dsl::FloatLiteral,
    dsl::IntegerLiteral,
    dsl::SignedIntLiteral,
    dsl::UnsignedIntLiteral,
    dsl::MemberSelector,
    dsl::DecimalNumber,
    dsl::PrimarySuffix,
    dsl::AllocationExpression,
    dsl::PrimaryPrefix,
    dsl::PreDecrementExpression,
    dsl::PreIncrementExpression,
    dsl::EObject,
    dsl::Literal,
    dsl::CastLookahead,
    dsl::PostfixExpression,
    dsl::CastExpression,
    dsl::UnaryExpressionNotPlusMinus,
    dsl::UnaryExpression,
    dsl::MultiplicativeExpression,
    dsl::AdditiveExpression,
    dsl::ShiftExpression,
    dsl::RelationalExpression,
    dsl::InstanceOfExpression,
    dsl::EqualityExpression,
    dsl::AndExpression,
    dsl::ExclusiveOrExpression,
    dsl::InclusiveOrExpression,
    dsl::ConditionalAndExpression,
    IfStatement,
    dsl::ConditionalOrExpression,
    dsl::Statement,
    dsl::ConditionalExpression,
    dsl::WildcardBounds,
    dsl::TypeArgument,
    dsl::TypeArguments,
    dsl::ReferenceType,
    dsl::PrimaryExpression,
    dsl::VariableDeclaratorId,
    dsl::VariableDeclarator,
    dsl::FormalParameter,
    dsl::Block,
    dsl::MethodDeclarator,
    dsl::ResultType,
    dsl::BlockStatement,
    dsl::ExplicitConstructorInvocation,
    dsl::NameList,
    dsl::FormalParameters,
    dsl::Expression,
    dsl::ArrayInitializer,
    dsl::VariableInitializer,
    dsl::Type,
    dsl::FieldDeclaration,
    dsl::MethodOrCtorDeclaration,
    dsl::Initializer,
    dsl::TypeBound,
    dsl::TypeParameter,
    dsl::Arguments,
    dsl::ClassOrInterfaceBodyDeclaration,
    dsl::EnumConstant,
    dsl::EnumBody,
    dsl::ClassOrInterfaceType,
    dsl::ClassOrInterfaceBody,
    dsl::ImplementsList,
    dsl::ExtendsList,
    dsl::TypeParameters,
    dsl::AnnotationTypeDeclaration,
    dsl::EnumDeclaration,
    dsl::ClassOrInterfaceDeclaration,
    dsl::TypeBodyModifier,
    dsl::CommonModifier,
    dsl::Name,
    dsl::TypeDeclaration,
    dsl::ImportDeclaration,
    dsl::PackageDeclaration,
    dsl::CompilationUnit,
    Visibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dsl::defaultvalue_is_not_abstract():
    assert not inspect.isabstract(dsl::DefaultValue)


def test_dsl::defaultvalue_constructor_exists():
    assert callable(dsl::DefaultValue.__init__)


def test_dsl::defaultvalue_constructor_args():
    sig = inspect.signature(dsl::DefaultValue.__init__)
    params = list(sig.parameters.keys())



def test_dsl::annotationtypememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl::AnnotationTypeMemberDeclaration)


def test_dsl::annotationtypememberdeclaration_constructor_exists():
    assert callable(dsl::AnnotationTypeMemberDeclaration.__init__)


def test_dsl::annotationtypememberdeclaration_constructor_args():
    sig = inspect.signature(dsl::AnnotationTypeMemberDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl::annotationtypememberdeclaration_has_id():
    assert hasattr(dsl::AnnotationTypeMemberDeclaration, "id")
    descriptor = None
    for klass in dsl::AnnotationTypeMemberDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl::annotationtypebody_is_not_abstract():
    assert not inspect.isabstract(dsl::AnnotationTypeBody)


def test_dsl::annotationtypebody_constructor_exists():
    assert callable(dsl::AnnotationTypeBody.__init__)


def test_dsl::annotationtypebody_constructor_args():
    sig = inspect.signature(dsl::AnnotationTypeBody.__init__)
    params = list(sig.parameters.keys())



def test_dsl::membervaluearrayinitializer_is_not_abstract():
    assert not inspect.isabstract(dsl::MemberValueArrayInitializer)


def test_dsl::membervaluearrayinitializer_constructor_exists():
    assert callable(dsl::MemberValueArrayInitializer.__init__)


def test_dsl::membervaluearrayinitializer_constructor_args():
    sig = inspect.signature(dsl::MemberValueArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_defaultvalue_is_not_abstract():
    assert not inspect.isabstract(DefaultValue)


def test_defaultvalue_constructor_exists():
    assert callable(DefaultValue.__init__)


def test_defaultvalue_constructor_args():
    sig = inspect.signature(DefaultValue.__init__)
    params = list(sig.parameters.keys())



def test_dsl::membervaluepair_is_not_abstract():
    assert not inspect.isabstract(dsl::MemberValuePair)


def test_dsl::membervaluepair_constructor_exists():
    assert callable(dsl::MemberValuePair.__init__)


def test_dsl::membervaluepair_constructor_args():
    sig = inspect.signature(dsl::MemberValuePair.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl::membervaluepair_has_id():
    assert hasattr(dsl::MemberValuePair, "id")
    descriptor = None
    for klass in dsl::MemberValuePair.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl::membervalue_is_not_abstract():
    assert not inspect.isabstract(dsl::MemberValue)


def test_dsl::membervalue_constructor_exists():
    assert callable(dsl::MemberValue.__init__)


def test_dsl::membervalue_constructor_args():
    sig = inspect.signature(dsl::MemberValue.__init__)
    params = list(sig.parameters.keys())



def test_dsl::membervaluepairs_is_not_abstract():
    assert not inspect.isabstract(dsl::MemberValuePairs)


def test_dsl::membervaluepairs_constructor_exists():
    assert callable(dsl::MemberValuePairs.__init__)


def test_dsl::membervaluepairs_constructor_args():
    sig = inspect.signature(dsl::MemberValuePairs.__init__)
    params = list(sig.parameters.keys())



def test_dsl::annotation_is_not_abstract():
    assert not inspect.isabstract(dsl::Annotation)


def test_dsl::annotation_constructor_exists():
    assert callable(dsl::Annotation.__init__)


def test_dsl::annotation_constructor_args():
    sig = inspect.signature(dsl::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_dsl::statementexpressionlist_is_not_abstract():
    assert not inspect.isabstract(dsl::StatementExpressionList)


def test_dsl::statementexpressionlist_constructor_exists():
    assert callable(dsl::StatementExpressionList.__init__)


def test_dsl::statementexpressionlist_constructor_args():
    sig = inspect.signature(dsl::StatementExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_dsl::forupdate_is_not_abstract():
    assert not inspect.isabstract(dsl::ForUpdate)


def test_dsl::forupdate_constructor_exists():
    assert callable(dsl::ForUpdate.__init__)


def test_dsl::forupdate_constructor_args():
    sig = inspect.signature(dsl::ForUpdate.__init__)
    params = list(sig.parameters.keys())



def test_dsl::forinit_is_not_abstract():
    assert not inspect.isabstract(dsl::ForInit)


def test_dsl::forinit_constructor_exists():
    assert callable(dsl::ForInit.__init__)


def test_dsl::forinit_constructor_args():
    sig = inspect.signature(dsl::ForInit.__init__)
    params = list(sig.parameters.keys())



def test_dsl::switchlabel_is_not_abstract():
    assert not inspect.isabstract(dsl::SwitchLabel)


def test_dsl::switchlabel_constructor_exists():
    assert callable(dsl::SwitchLabel.__init__)


def test_dsl::switchlabel_constructor_args():
    sig = inspect.signature(dsl::SwitchLabel.__init__)
    params = list(sig.parameters.keys())
    assert "defaultOp" in params, "Missing parameter 'defaultOp'"

def test_dsl::switchlabel_has_defaultOp():
    assert hasattr(dsl::SwitchLabel, "defaultOp")
    descriptor = None
    for klass in dsl::SwitchLabel.__mro__:
        if "defaultOp" in klass.__dict__:
            descriptor = klass.__dict__["defaultOp"]
            break
    assert isinstance(descriptor, property)



def test_dsl::localvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl::LocalVariableDeclaration)


def test_dsl::localvariabledeclaration_constructor_exists():
    assert callable(dsl::LocalVariableDeclaration.__init__)


def test_dsl::localvariabledeclaration_constructor_args():
    sig = inspect.signature(dsl::LocalVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "finality" in params, "Missing parameter 'finality'"

def test_dsl::localvariabledeclaration_has_finality():
    assert hasattr(dsl::LocalVariableDeclaration, "finality")
    descriptor = None
    for klass in dsl::LocalVariableDeclaration.__mro__:
        if "finality" in klass.__dict__:
            descriptor = klass.__dict__["finality"]
            break
    assert isinstance(descriptor, property)



def test_dsl::trystatement_is_not_abstract():
    assert not inspect.isabstract(dsl::TryStatement)


def test_dsl::trystatement_constructor_exists():
    assert callable(dsl::TryStatement.__init__)


def test_dsl::trystatement_constructor_args():
    sig = inspect.signature(dsl::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl::synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(dsl::SynchronizedStatement)


def test_dsl::synchronizedstatement_constructor_exists():
    assert callable(dsl::SynchronizedStatement.__init__)


def test_dsl::synchronizedstatement_constructor_args():
    sig = inspect.signature(dsl::SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl::throwstatement_is_not_abstract():
    assert not inspect.isabstract(dsl::ThrowStatement)


def test_dsl::throwstatement_constructor_exists():
    assert callable(dsl::ThrowStatement.__init__)


def test_dsl::throwstatement_constructor_args():
    sig = inspect.signature(dsl::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl::returnstatement_is_not_abstract():
    assert not inspect.isabstract(dsl::ReturnStatement)


def test_dsl::returnstatement_constructor_exists():
    assert callable(dsl::ReturnStatement.__init__)


def test_dsl::returnstatement_constructor_args():
    sig = inspect.signature(dsl::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl::continuestatement_is_not_abstract():
    assert not inspect.isabstract(dsl::ContinueStatement)


def test_dsl::continuestatement_constructor_exists():
    assert callable(dsl::ContinueStatement.__init__)


def test_dsl::continuestatement_constructor_args():
    sig = inspect.signature(dsl::ContinueStatement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl::continuestatement_has_id():
    assert hasattr(dsl::ContinueStatement, "id")
    descriptor = None
    for klass in dsl::ContinueStatement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl::breakstatement_is_not_abstract():
    assert not inspect.isabstract(dsl::BreakStatement)


def test_dsl::breakstatement_constructor_exists():
    assert callable(dsl::BreakStatement.__init__)


def test_dsl::breakstatement_constructor_args():
    sig = inspect.signature(dsl::BreakStatement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl::breakstatement_has_id():
    assert hasattr(dsl::BreakStatement, "id")
    descriptor = None
    for klass in dsl::BreakStatement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl::forstatement_is_not_abstract():
    assert not inspect.isabstract(dsl::ForStatement)


def test_dsl::forstatement_constructor_exists():
    assert callable(dsl::ForStatement.__init__)


def test_dsl::forstatement_constructor_args():
    sig = inspect.signature(dsl::ForStatement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl::forstatement_has_id():
    assert hasattr(dsl::ForStatement, "id")
    descriptor = None
    for klass in dsl::ForStatement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl::dostatement_is_not_abstract():
    assert not inspect.isabstract(dsl::DoStatement)


def test_dsl::dostatement_constructor_exists():
    assert callable(dsl::DoStatement.__init__)


def test_dsl::dostatement_constructor_args():
    sig = inspect.signature(dsl::DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl::whilestatement_is_not_abstract():
    assert not inspect.isabstract(dsl::WhileStatement)


def test_dsl::whilestatement_constructor_exists():
    assert callable(dsl::WhileStatement.__init__)


def test_dsl::whilestatement_constructor_args():
    sig = inspect.signature(dsl::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl::ifstatement_is_not_abstract():
    assert not inspect.isabstract(dsl::IfStatement)


def test_dsl::ifstatement_constructor_exists():
    assert callable(dsl::IfStatement.__init__)


def test_dsl::ifstatement_constructor_args():
    sig = inspect.signature(dsl::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl::switchstatement_is_not_abstract():
    assert not inspect.isabstract(dsl::SwitchStatement)


def test_dsl::switchstatement_constructor_exists():
    assert callable(dsl::SwitchStatement.__init__)


def test_dsl::switchstatement_constructor_args():
    sig = inspect.signature(dsl::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl::statementexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::StatementExpression)


def test_dsl::statementexpression_constructor_exists():
    assert callable(dsl::StatementExpression.__init__)


def test_dsl::statementexpression_constructor_args():
    sig = inspect.signature(dsl::StatementExpression.__init__)
    params = list(sig.parameters.keys())
    assert "assignOp" in params, "Missing parameter 'assignOp'"
    assert "minOp" in params, "Missing parameter 'minOp'"
    assert "plusOp" in params, "Missing parameter 'plusOp'"

def test_dsl::statementexpression_has_assignOp():
    assert hasattr(dsl::StatementExpression, "assignOp")
    descriptor = None
    for klass in dsl::StatementExpression.__mro__:
        if "assignOp" in klass.__dict__:
            descriptor = klass.__dict__["assignOp"]
            break
    assert isinstance(descriptor, property)

def test_dsl::statementexpression_has_minOp():
    assert hasattr(dsl::StatementExpression, "minOp")
    descriptor = None
    for klass in dsl::StatementExpression.__mro__:
        if "minOp" in klass.__dict__:
            descriptor = klass.__dict__["minOp"]
            break
    assert isinstance(descriptor, property)

def test_dsl::statementexpression_has_plusOp():
    assert hasattr(dsl::StatementExpression, "plusOp")
    descriptor = None
    for klass in dsl::StatementExpression.__mro__:
        if "plusOp" in klass.__dict__:
            descriptor = klass.__dict__["plusOp"]
            break
    assert isinstance(descriptor, property)



def test_dsl::assertstatement_is_not_abstract():
    assert not inspect.isabstract(dsl::AssertStatement)


def test_dsl::assertstatement_constructor_exists():
    assert callable(dsl::AssertStatement.__init__)


def test_dsl::assertstatement_constructor_args():
    sig = inspect.signature(dsl::AssertStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl::labeledstatement_is_not_abstract():
    assert not inspect.isabstract(dsl::LabeledStatement)


def test_dsl::labeledstatement_constructor_exists():
    assert callable(dsl::LabeledStatement.__init__)


def test_dsl::labeledstatement_constructor_args():
    sig = inspect.signature(dsl::LabeledStatement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl::labeledstatement_has_id():
    assert hasattr(dsl::LabeledStatement, "id")
    descriptor = None
    for klass in dsl::LabeledStatement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl::arraydimsandinits_is_not_abstract():
    assert not inspect.isabstract(dsl::ArrayDimsAndInits)


def test_dsl::arraydimsandinits_constructor_exists():
    assert callable(dsl::ArrayDimsAndInits.__init__)


def test_dsl::arraydimsandinits_constructor_args():
    sig = inspect.signature(dsl::ArrayDimsAndInits.__init__)
    params = list(sig.parameters.keys())
    assert "squareBrackets" in params, "Missing parameter 'squareBrackets'"

def test_dsl::arraydimsandinits_has_squareBrackets():
    assert hasattr(dsl::ArrayDimsAndInits, "squareBrackets")
    descriptor = None
    for klass in dsl::ArrayDimsAndInits.__mro__:
        if "squareBrackets" in klass.__dict__:
            descriptor = klass.__dict__["squareBrackets"]
            break
    assert isinstance(descriptor, property)



def test_dsl::baseliteral_is_not_abstract():
    assert not inspect.isabstract(dsl::BaseLiteral)


def test_dsl::baseliteral_constructor_exists():
    assert callable(dsl::BaseLiteral.__init__)


def test_dsl::baseliteral_constructor_args():
    sig = inspect.signature(dsl::BaseLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "binDigitsUnderscore" in params, "Missing parameter 'binDigitsUnderscore'"
    assert "decDigitsUnderscore" in params, "Missing parameter 'decDigitsUnderscore'"
    assert "hexDigitsUnderscore" in params, "Missing parameter 'hexDigitsUnderscore'"

def test_dsl::baseliteral_has_binDigitsUnderscore():
    assert hasattr(dsl::BaseLiteral, "binDigitsUnderscore")
    descriptor = None
    for klass in dsl::BaseLiteral.__mro__:
        if "binDigitsUnderscore" in klass.__dict__:
            descriptor = klass.__dict__["binDigitsUnderscore"]
            break
    assert isinstance(descriptor, property)

def test_dsl::baseliteral_has_decDigitsUnderscore():
    assert hasattr(dsl::BaseLiteral, "decDigitsUnderscore")
    descriptor = None
    for klass in dsl::BaseLiteral.__mro__:
        if "decDigitsUnderscore" in klass.__dict__:
            descriptor = klass.__dict__["decDigitsUnderscore"]
            break
    assert isinstance(descriptor, property)

def test_dsl::baseliteral_has_hexDigitsUnderscore():
    assert hasattr(dsl::BaseLiteral, "hexDigitsUnderscore")
    descriptor = None
    for klass in dsl::BaseLiteral.__mro__:
        if "hexDigitsUnderscore" in klass.__dict__:
            descriptor = klass.__dict__["hexDigitsUnderscore"]
            break
    assert isinstance(descriptor, property)



def test_dsl::argumentlist_is_not_abstract():
    assert not inspect.isabstract(dsl::ArgumentList)


def test_dsl::argumentlist_constructor_exists():
    assert callable(dsl::ArgumentList.__init__)


def test_dsl::argumentlist_constructor_args():
    sig = inspect.signature(dsl::ArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_dsl::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(dsl::BooleanLiteral)


def test_dsl::booleanliteral_constructor_exists():
    assert callable(dsl::BooleanLiteral.__init__)


def test_dsl::booleanliteral_constructor_args():
    sig = inspect.signature(dsl::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "truthiness" in params, "Missing parameter 'truthiness'"

def test_dsl::booleanliteral_has_truthiness():
    assert hasattr(dsl::BooleanLiteral, "truthiness")
    descriptor = None
    for klass in dsl::BooleanLiteral.__mro__:
        if "truthiness" in klass.__dict__:
            descriptor = klass.__dict__["truthiness"]
            break
    assert isinstance(descriptor, property)



def test_dsl::floatliteral_is_not_abstract():
    assert not inspect.isabstract(dsl::FloatLiteral)


def test_dsl::floatliteral_constructor_exists():
    assert callable(dsl::FloatLiteral.__init__)


def test_dsl::floatliteral_constructor_args():
    sig = inspect.signature(dsl::FloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "digits" in params, "Missing parameter 'digits'"

def test_dsl::floatliteral_has_digits():
    assert hasattr(dsl::FloatLiteral, "digits")
    descriptor = None
    for klass in dsl::FloatLiteral.__mro__:
        if "digits" in klass.__dict__:
            descriptor = klass.__dict__["digits"]
            break
    assert isinstance(descriptor, property)



def test_dsl::integerliteral_is_not_abstract():
    assert not inspect.isabstract(dsl::IntegerLiteral)


def test_dsl::integerliteral_constructor_exists():
    assert callable(dsl::IntegerLiteral.__init__)


def test_dsl::integerliteral_constructor_args():
    sig = inspect.signature(dsl::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "zero" in params, "Missing parameter 'zero'"
    assert "one" in params, "Missing parameter 'one'"

def test_dsl::integerliteral_has_zero():
    assert hasattr(dsl::IntegerLiteral, "zero")
    descriptor = None
    for klass in dsl::IntegerLiteral.__mro__:
        if "zero" in klass.__dict__:
            descriptor = klass.__dict__["zero"]
            break
    assert isinstance(descriptor, property)

def test_dsl::integerliteral_has_one():
    assert hasattr(dsl::IntegerLiteral, "one")
    descriptor = None
    for klass in dsl::IntegerLiteral.__mro__:
        if "one" in klass.__dict__:
            descriptor = klass.__dict__["one"]
            break
    assert isinstance(descriptor, property)



def test_dsl::signedintliteral_is_not_abstract():
    assert not inspect.isabstract(dsl::SignedIntLiteral)


def test_dsl::signedintliteral_constructor_exists():
    assert callable(dsl::SignedIntLiteral.__init__)


def test_dsl::signedintliteral_constructor_args():
    sig = inspect.signature(dsl::SignedIntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "bitWidth" in params, "Missing parameter 'bitWidth'"

def test_dsl::signedintliteral_has_bitWidth():
    assert hasattr(dsl::SignedIntLiteral, "bitWidth")
    descriptor = None
    for klass in dsl::SignedIntLiteral.__mro__:
        if "bitWidth" in klass.__dict__:
            descriptor = klass.__dict__["bitWidth"]
            break
    assert isinstance(descriptor, property)



def test_dsl::unsignedintliteral_is_not_abstract():
    assert not inspect.isabstract(dsl::UnsignedIntLiteral)


def test_dsl::unsignedintliteral_constructor_exists():
    assert callable(dsl::UnsignedIntLiteral.__init__)


def test_dsl::unsignedintliteral_constructor_args():
    sig = inspect.signature(dsl::UnsignedIntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"

def test_dsl::unsignedintliteral_has_sign():
    assert hasattr(dsl::UnsignedIntLiteral, "sign")
    descriptor = None
    for klass in dsl::UnsignedIntLiteral.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)



def test_dsl::memberselector_is_not_abstract():
    assert not inspect.isabstract(dsl::MemberSelector)


def test_dsl::memberselector_constructor_exists():
    assert callable(dsl::MemberSelector.__init__)


def test_dsl::memberselector_constructor_args():
    sig = inspect.signature(dsl::MemberSelector.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl::memberselector_has_id():
    assert hasattr(dsl::MemberSelector, "id")
    descriptor = None
    for klass in dsl::MemberSelector.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl::decimalnumber_is_not_abstract():
    assert not inspect.isabstract(dsl::DecimalNumber)


def test_dsl::decimalnumber_constructor_exists():
    assert callable(dsl::DecimalNumber.__init__)


def test_dsl::decimalnumber_constructor_args():
    sig = inspect.signature(dsl::DecimalNumber.__init__)
    params = list(sig.parameters.keys())
    assert "decDigitsUnderscore" in params, "Missing parameter 'decDigitsUnderscore'"
    assert "decDigits" in params, "Missing parameter 'decDigits'"

def test_dsl::decimalnumber_has_decDigitsUnderscore():
    assert hasattr(dsl::DecimalNumber, "decDigitsUnderscore")
    descriptor = None
    for klass in dsl::DecimalNumber.__mro__:
        if "decDigitsUnderscore" in klass.__dict__:
            descriptor = klass.__dict__["decDigitsUnderscore"]
            break
    assert isinstance(descriptor, property)

def test_dsl::decimalnumber_has_decDigits():
    assert hasattr(dsl::DecimalNumber, "decDigits")
    descriptor = None
    for klass in dsl::DecimalNumber.__mro__:
        if "decDigits" in klass.__dict__:
            descriptor = klass.__dict__["decDigits"]
            break
    assert isinstance(descriptor, property)



def test_dsl::primarysuffix_is_not_abstract():
    assert not inspect.isabstract(dsl::PrimarySuffix)


def test_dsl::primarysuffix_constructor_exists():
    assert callable(dsl::PrimarySuffix.__init__)


def test_dsl::primarysuffix_constructor_args():
    sig = inspect.signature(dsl::PrimarySuffix.__init__)
    params = list(sig.parameters.keys())
    assert "thisOp" in params, "Missing parameter 'thisOp'"
    assert "id" in params, "Missing parameter 'id'"

def test_dsl::primarysuffix_has_thisOp():
    assert hasattr(dsl::PrimarySuffix, "thisOp")
    descriptor = None
    for klass in dsl::PrimarySuffix.__mro__:
        if "thisOp" in klass.__dict__:
            descriptor = klass.__dict__["thisOp"]
            break
    assert isinstance(descriptor, property)

def test_dsl::primarysuffix_has_id():
    assert hasattr(dsl::PrimarySuffix, "id")
    descriptor = None
    for klass in dsl::PrimarySuffix.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl::allocationexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::AllocationExpression)


def test_dsl::allocationexpression_constructor_exists():
    assert callable(dsl::AllocationExpression.__init__)


def test_dsl::allocationexpression_constructor_args():
    sig = inspect.signature(dsl::AllocationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "primType" in params, "Missing parameter 'primType'"

def test_dsl::allocationexpression_has_primType():
    assert hasattr(dsl::AllocationExpression, "primType")
    descriptor = None
    for klass in dsl::AllocationExpression.__mro__:
        if "primType" in klass.__dict__:
            descriptor = klass.__dict__["primType"]
            break
    assert isinstance(descriptor, property)



def test_dsl::primaryprefix_is_not_abstract():
    assert not inspect.isabstract(dsl::PrimaryPrefix)


def test_dsl::primaryprefix_constructor_exists():
    assert callable(dsl::PrimaryPrefix.__init__)


def test_dsl::primaryprefix_constructor_args():
    sig = inspect.signature(dsl::PrimaryPrefix.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "superOp" in params, "Missing parameter 'superOp'"
    assert "thisOp" in params, "Missing parameter 'thisOp'"

def test_dsl::primaryprefix_has_id():
    assert hasattr(dsl::PrimaryPrefix, "id")
    descriptor = None
    for klass in dsl::PrimaryPrefix.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_dsl::primaryprefix_has_superOp():
    assert hasattr(dsl::PrimaryPrefix, "superOp")
    descriptor = None
    for klass in dsl::PrimaryPrefix.__mro__:
        if "superOp" in klass.__dict__:
            descriptor = klass.__dict__["superOp"]
            break
    assert isinstance(descriptor, property)

def test_dsl::primaryprefix_has_thisOp():
    assert hasattr(dsl::PrimaryPrefix, "thisOp")
    descriptor = None
    for klass in dsl::PrimaryPrefix.__mro__:
        if "thisOp" in klass.__dict__:
            descriptor = klass.__dict__["thisOp"]
            break
    assert isinstance(descriptor, property)



def test_dsl::predecrementexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::PreDecrementExpression)


def test_dsl::predecrementexpression_constructor_exists():
    assert callable(dsl::PreDecrementExpression.__init__)


def test_dsl::predecrementexpression_constructor_args():
    sig = inspect.signature(dsl::PreDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl::preincrementexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::PreIncrementExpression)


def test_dsl::preincrementexpression_constructor_exists():
    assert callable(dsl::PreIncrementExpression.__init__)


def test_dsl::preincrementexpression_constructor_args():
    sig = inspect.signature(dsl::PreIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl::eobject_is_not_abstract():
    assert not inspect.isabstract(dsl::EObject)


def test_dsl::eobject_constructor_exists():
    assert callable(dsl::EObject.__init__)


def test_dsl::eobject_constructor_args():
    sig = inspect.signature(dsl::EObject.__init__)
    params = list(sig.parameters.keys())



def test_dsl::literal_is_not_abstract():
    assert not inspect.isabstract(dsl::Literal)


def test_dsl::literal_constructor_exists():
    assert callable(dsl::Literal.__init__)


def test_dsl::literal_constructor_args():
    sig = inspect.signature(dsl::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "charLit" in params, "Missing parameter 'charLit'"
    assert "stringLit" in params, "Missing parameter 'stringLit'"
    assert "nullLit" in params, "Missing parameter 'nullLit'"

def test_dsl::literal_has_charLit():
    assert hasattr(dsl::Literal, "charLit")
    descriptor = None
    for klass in dsl::Literal.__mro__:
        if "charLit" in klass.__dict__:
            descriptor = klass.__dict__["charLit"]
            break
    assert isinstance(descriptor, property)

def test_dsl::literal_has_stringLit():
    assert hasattr(dsl::Literal, "stringLit")
    descriptor = None
    for klass in dsl::Literal.__mro__:
        if "stringLit" in klass.__dict__:
            descriptor = klass.__dict__["stringLit"]
            break
    assert isinstance(descriptor, property)

def test_dsl::literal_has_nullLit():
    assert hasattr(dsl::Literal, "nullLit")
    descriptor = None
    for klass in dsl::Literal.__mro__:
        if "nullLit" in klass.__dict__:
            descriptor = klass.__dict__["nullLit"]
            break
    assert isinstance(descriptor, property)



def test_dsl::castlookahead_is_not_abstract():
    assert not inspect.isabstract(dsl::CastLookahead)


def test_dsl::castlookahead_constructor_exists():
    assert callable(dsl::CastLookahead.__init__)


def test_dsl::castlookahead_constructor_args():
    sig = inspect.signature(dsl::CastLookahead.__init__)
    params = list(sig.parameters.keys())
    assert "openBracket" in params, "Missing parameter 'openBracket'"
    assert "negOp" in params, "Missing parameter 'negOp'"
    assert "superOp" in params, "Missing parameter 'superOp'"
    assert "id" in params, "Missing parameter 'id'"
    assert "bitNegOp" in params, "Missing parameter 'bitNegOp'"
    assert "thisOp" in params, "Missing parameter 'thisOp'"
    assert "newOp" in params, "Missing parameter 'newOp'"
    assert "primType" in params, "Missing parameter 'primType'"

def test_dsl::castlookahead_has_openBracket():
    assert hasattr(dsl::CastLookahead, "openBracket")
    descriptor = None
    for klass in dsl::CastLookahead.__mro__:
        if "openBracket" in klass.__dict__:
            descriptor = klass.__dict__["openBracket"]
            break
    assert isinstance(descriptor, property)

def test_dsl::castlookahead_has_negOp():
    assert hasattr(dsl::CastLookahead, "negOp")
    descriptor = None
    for klass in dsl::CastLookahead.__mro__:
        if "negOp" in klass.__dict__:
            descriptor = klass.__dict__["negOp"]
            break
    assert isinstance(descriptor, property)

def test_dsl::castlookahead_has_superOp():
    assert hasattr(dsl::CastLookahead, "superOp")
    descriptor = None
    for klass in dsl::CastLookahead.__mro__:
        if "superOp" in klass.__dict__:
            descriptor = klass.__dict__["superOp"]
            break
    assert isinstance(descriptor, property)

def test_dsl::castlookahead_has_id():
    assert hasattr(dsl::CastLookahead, "id")
    descriptor = None
    for klass in dsl::CastLookahead.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_dsl::castlookahead_has_bitNegOp():
    assert hasattr(dsl::CastLookahead, "bitNegOp")
    descriptor = None
    for klass in dsl::CastLookahead.__mro__:
        if "bitNegOp" in klass.__dict__:
            descriptor = klass.__dict__["bitNegOp"]
            break
    assert isinstance(descriptor, property)

def test_dsl::castlookahead_has_thisOp():
    assert hasattr(dsl::CastLookahead, "thisOp")
    descriptor = None
    for klass in dsl::CastLookahead.__mro__:
        if "thisOp" in klass.__dict__:
            descriptor = klass.__dict__["thisOp"]
            break
    assert isinstance(descriptor, property)

def test_dsl::castlookahead_has_newOp():
    assert hasattr(dsl::CastLookahead, "newOp")
    descriptor = None
    for klass in dsl::CastLookahead.__mro__:
        if "newOp" in klass.__dict__:
            descriptor = klass.__dict__["newOp"]
            break
    assert isinstance(descriptor, property)

def test_dsl::castlookahead_has_primType():
    assert hasattr(dsl::CastLookahead, "primType")
    descriptor = None
    for klass in dsl::CastLookahead.__mro__:
        if "primType" in klass.__dict__:
            descriptor = klass.__dict__["primType"]
            break
    assert isinstance(descriptor, property)



def test_dsl::postfixexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::PostfixExpression)


def test_dsl::postfixexpression_constructor_exists():
    assert callable(dsl::PostfixExpression.__init__)


def test_dsl::postfixexpression_constructor_args():
    sig = inspect.signature(dsl::PostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_dsl::postfixexpression_has_op():
    assert hasattr(dsl::PostfixExpression, "op")
    descriptor = None
    for klass in dsl::PostfixExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_dsl::castexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::CastExpression)


def test_dsl::castexpression_constructor_exists():
    assert callable(dsl::CastExpression.__init__)


def test_dsl::castexpression_constructor_args():
    sig = inspect.signature(dsl::CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl::unaryexpressionnotplusminus_is_not_abstract():
    assert not inspect.isabstract(dsl::UnaryExpressionNotPlusMinus)


def test_dsl::unaryexpressionnotplusminus_constructor_exists():
    assert callable(dsl::UnaryExpressionNotPlusMinus.__init__)


def test_dsl::unaryexpressionnotplusminus_constructor_args():
    sig = inspect.signature(dsl::UnaryExpressionNotPlusMinus.__init__)
    params = list(sig.parameters.keys())
    assert "negOp" in params, "Missing parameter 'negOp'"

def test_dsl::unaryexpressionnotplusminus_has_negOp():
    assert hasattr(dsl::UnaryExpressionNotPlusMinus, "negOp")
    descriptor = None
    for klass in dsl::UnaryExpressionNotPlusMinus.__mro__:
        if "negOp" in klass.__dict__:
            descriptor = klass.__dict__["negOp"]
            break
    assert isinstance(descriptor, property)



def test_dsl::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::UnaryExpression)


def test_dsl::unaryexpression_constructor_exists():
    assert callable(dsl::UnaryExpression.__init__)


def test_dsl::unaryexpression_constructor_args():
    sig = inspect.signature(dsl::UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"

def test_dsl::unaryexpression_has_sign():
    assert hasattr(dsl::UnaryExpression, "sign")
    descriptor = None
    for klass in dsl::UnaryExpression.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)



def test_dsl::multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::MultiplicativeExpression)


def test_dsl::multiplicativeexpression_constructor_exists():
    assert callable(dsl::MultiplicativeExpression.__init__)


def test_dsl::multiplicativeexpression_constructor_args():
    sig = inspect.signature(dsl::MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "ops" in params, "Missing parameter 'ops'"

def test_dsl::multiplicativeexpression_has_ops():
    assert hasattr(dsl::MultiplicativeExpression, "ops")
    descriptor = None
    for klass in dsl::MultiplicativeExpression.__mro__:
        if "ops" in klass.__dict__:
            descriptor = klass.__dict__["ops"]
            break
    assert isinstance(descriptor, property)



def test_dsl::additiveexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::AdditiveExpression)


def test_dsl::additiveexpression_constructor_exists():
    assert callable(dsl::AdditiveExpression.__init__)


def test_dsl::additiveexpression_constructor_args():
    sig = inspect.signature(dsl::AdditiveExpression.__init__)
    params = list(sig.parameters.keys())
    assert "ops" in params, "Missing parameter 'ops'"

def test_dsl::additiveexpression_has_ops():
    assert hasattr(dsl::AdditiveExpression, "ops")
    descriptor = None
    for klass in dsl::AdditiveExpression.__mro__:
        if "ops" in klass.__dict__:
            descriptor = klass.__dict__["ops"]
            break
    assert isinstance(descriptor, property)



def test_dsl::shiftexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::ShiftExpression)


def test_dsl::shiftexpression_constructor_exists():
    assert callable(dsl::ShiftExpression.__init__)


def test_dsl::shiftexpression_constructor_args():
    sig = inspect.signature(dsl::ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "ops" in params, "Missing parameter 'ops'"

def test_dsl::shiftexpression_has_ops():
    assert hasattr(dsl::ShiftExpression, "ops")
    descriptor = None
    for klass in dsl::ShiftExpression.__mro__:
        if "ops" in klass.__dict__:
            descriptor = klass.__dict__["ops"]
            break
    assert isinstance(descriptor, property)



def test_dsl::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::RelationalExpression)


def test_dsl::relationalexpression_constructor_exists():
    assert callable(dsl::RelationalExpression.__init__)


def test_dsl::relationalexpression_constructor_args():
    sig = inspect.signature(dsl::RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "ops" in params, "Missing parameter 'ops'"

def test_dsl::relationalexpression_has_ops():
    assert hasattr(dsl::RelationalExpression, "ops")
    descriptor = None
    for klass in dsl::RelationalExpression.__mro__:
        if "ops" in klass.__dict__:
            descriptor = klass.__dict__["ops"]
            break
    assert isinstance(descriptor, property)



def test_dsl::instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::InstanceOfExpression)


def test_dsl::instanceofexpression_constructor_exists():
    assert callable(dsl::InstanceOfExpression.__init__)


def test_dsl::instanceofexpression_constructor_args():
    sig = inspect.signature(dsl::InstanceOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::EqualityExpression)


def test_dsl::equalityexpression_constructor_exists():
    assert callable(dsl::EqualityExpression.__init__)


def test_dsl::equalityexpression_constructor_args():
    sig = inspect.signature(dsl::EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl::andexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::AndExpression)


def test_dsl::andexpression_constructor_exists():
    assert callable(dsl::AndExpression.__init__)


def test_dsl::andexpression_constructor_args():
    sig = inspect.signature(dsl::AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl::exclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::ExclusiveOrExpression)


def test_dsl::exclusiveorexpression_constructor_exists():
    assert callable(dsl::ExclusiveOrExpression.__init__)


def test_dsl::exclusiveorexpression_constructor_args():
    sig = inspect.signature(dsl::ExclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl::inclusiveorexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::InclusiveOrExpression)


def test_dsl::inclusiveorexpression_constructor_exists():
    assert callable(dsl::InclusiveOrExpression.__init__)


def test_dsl::inclusiveorexpression_constructor_args():
    sig = inspect.signature(dsl::InclusiveOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl::conditionalandexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::ConditionalAndExpression)


def test_dsl::conditionalandexpression_constructor_exists():
    assert callable(dsl::ConditionalAndExpression.__init__)


def test_dsl::conditionalandexpression_constructor_args():
    sig = inspect.signature(dsl::ConditionalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_ifstatement_is_not_abstract():
    assert not inspect.isabstract(IfStatement)


def test_ifstatement_constructor_exists():
    assert callable(IfStatement.__init__)


def test_ifstatement_constructor_args():
    sig = inspect.signature(IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl::conditionalorexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::ConditionalOrExpression)


def test_dsl::conditionalorexpression_constructor_exists():
    assert callable(dsl::ConditionalOrExpression.__init__)


def test_dsl::conditionalorexpression_constructor_args():
    sig = inspect.signature(dsl::ConditionalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl::statement_is_not_abstract():
    assert not inspect.isabstract(dsl::Statement)


def test_dsl::statement_constructor_exists():
    assert callable(dsl::Statement.__init__)


def test_dsl::statement_constructor_args():
    sig = inspect.signature(dsl::Statement.__init__)
    params = list(sig.parameters.keys())



def test_dsl::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::ConditionalExpression)


def test_dsl::conditionalexpression_constructor_exists():
    assert callable(dsl::ConditionalExpression.__init__)


def test_dsl::conditionalexpression_constructor_args():
    sig = inspect.signature(dsl::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl::wildcardbounds_is_not_abstract():
    assert not inspect.isabstract(dsl::WildcardBounds)


def test_dsl::wildcardbounds_constructor_exists():
    assert callable(dsl::WildcardBounds.__init__)


def test_dsl::wildcardbounds_constructor_args():
    sig = inspect.signature(dsl::WildcardBounds.__init__)
    params = list(sig.parameters.keys())
    assert "sup" in params, "Missing parameter 'sup'"
    assert "ext" in params, "Missing parameter 'ext'"

def test_dsl::wildcardbounds_has_sup():
    assert hasattr(dsl::WildcardBounds, "sup")
    descriptor = None
    for klass in dsl::WildcardBounds.__mro__:
        if "sup" in klass.__dict__:
            descriptor = klass.__dict__["sup"]
            break
    assert isinstance(descriptor, property)

def test_dsl::wildcardbounds_has_ext():
    assert hasattr(dsl::WildcardBounds, "ext")
    descriptor = None
    for klass in dsl::WildcardBounds.__mro__:
        if "ext" in klass.__dict__:
            descriptor = klass.__dict__["ext"]
            break
    assert isinstance(descriptor, property)



def test_dsl::typeargument_is_not_abstract():
    assert not inspect.isabstract(dsl::TypeArgument)


def test_dsl::typeargument_constructor_exists():
    assert callable(dsl::TypeArgument.__init__)


def test_dsl::typeargument_constructor_args():
    sig = inspect.signature(dsl::TypeArgument.__init__)
    params = list(sig.parameters.keys())



def test_dsl::typearguments_is_not_abstract():
    assert not inspect.isabstract(dsl::TypeArguments)


def test_dsl::typearguments_constructor_exists():
    assert callable(dsl::TypeArguments.__init__)


def test_dsl::typearguments_constructor_args():
    sig = inspect.signature(dsl::TypeArguments.__init__)
    params = list(sig.parameters.keys())



def test_dsl::referencetype_is_not_abstract():
    assert not inspect.isabstract(dsl::ReferenceType)


def test_dsl::referencetype_constructor_exists():
    assert callable(dsl::ReferenceType.__init__)


def test_dsl::referencetype_constructor_args():
    sig = inspect.signature(dsl::ReferenceType.__init__)
    params = list(sig.parameters.keys())
    assert "primType" in params, "Missing parameter 'primType'"
    assert "squareBracketsBeta" in params, "Missing parameter 'squareBracketsBeta'"
    assert "squareBracketsAlpha" in params, "Missing parameter 'squareBracketsAlpha'"

def test_dsl::referencetype_has_primType():
    assert hasattr(dsl::ReferenceType, "primType")
    descriptor = None
    for klass in dsl::ReferenceType.__mro__:
        if "primType" in klass.__dict__:
            descriptor = klass.__dict__["primType"]
            break
    assert isinstance(descriptor, property)

def test_dsl::referencetype_has_squareBracketsBeta():
    assert hasattr(dsl::ReferenceType, "squareBracketsBeta")
    descriptor = None
    for klass in dsl::ReferenceType.__mro__:
        if "squareBracketsBeta" in klass.__dict__:
            descriptor = klass.__dict__["squareBracketsBeta"]
            break
    assert isinstance(descriptor, property)

def test_dsl::referencetype_has_squareBracketsAlpha():
    assert hasattr(dsl::ReferenceType, "squareBracketsAlpha")
    descriptor = None
    for klass in dsl::ReferenceType.__mro__:
        if "squareBracketsAlpha" in klass.__dict__:
            descriptor = klass.__dict__["squareBracketsAlpha"]
            break
    assert isinstance(descriptor, property)



def test_dsl::primaryexpression_is_not_abstract():
    assert not inspect.isabstract(dsl::PrimaryExpression)


def test_dsl::primaryexpression_constructor_exists():
    assert callable(dsl::PrimaryExpression.__init__)


def test_dsl::primaryexpression_constructor_args():
    sig = inspect.signature(dsl::PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl::variabledeclaratorid_is_not_abstract():
    assert not inspect.isabstract(dsl::VariableDeclaratorId)


def test_dsl::variabledeclaratorid_constructor_exists():
    assert callable(dsl::VariableDeclaratorId.__init__)


def test_dsl::variabledeclaratorid_constructor_args():
    sig = inspect.signature(dsl::VariableDeclaratorId.__init__)
    params = list(sig.parameters.keys())
    assert "squareBrackets" in params, "Missing parameter 'squareBrackets'"
    assert "id" in params, "Missing parameter 'id'"

def test_dsl::variabledeclaratorid_has_squareBrackets():
    assert hasattr(dsl::VariableDeclaratorId, "squareBrackets")
    descriptor = None
    for klass in dsl::VariableDeclaratorId.__mro__:
        if "squareBrackets" in klass.__dict__:
            descriptor = klass.__dict__["squareBrackets"]
            break
    assert isinstance(descriptor, property)

def test_dsl::variabledeclaratorid_has_id():
    assert hasattr(dsl::VariableDeclaratorId, "id")
    descriptor = None
    for klass in dsl::VariableDeclaratorId.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl::variabledeclarator_is_not_abstract():
    assert not inspect.isabstract(dsl::VariableDeclarator)


def test_dsl::variabledeclarator_constructor_exists():
    assert callable(dsl::VariableDeclarator.__init__)


def test_dsl::variabledeclarator_constructor_args():
    sig = inspect.signature(dsl::VariableDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_dsl::formalparameter_is_not_abstract():
    assert not inspect.isabstract(dsl::FormalParameter)


def test_dsl::formalparameter_constructor_exists():
    assert callable(dsl::FormalParameter.__init__)


def test_dsl::formalparameter_constructor_args():
    sig = inspect.signature(dsl::FormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"

def test_dsl::formalparameter_has_final():
    assert hasattr(dsl::FormalParameter, "final")
    descriptor = None
    for klass in dsl::FormalParameter.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)



def test_dsl::block_is_not_abstract():
    assert not inspect.isabstract(dsl::Block)


def test_dsl::block_constructor_exists():
    assert callable(dsl::Block.__init__)


def test_dsl::block_constructor_args():
    sig = inspect.signature(dsl::Block.__init__)
    params = list(sig.parameters.keys())



def test_dsl::methoddeclarator_is_not_abstract():
    assert not inspect.isabstract(dsl::MethodDeclarator)


def test_dsl::methoddeclarator_constructor_exists():
    assert callable(dsl::MethodDeclarator.__init__)


def test_dsl::methoddeclarator_constructor_args():
    sig = inspect.signature(dsl::MethodDeclarator.__init__)
    params = list(sig.parameters.keys())
    assert "squareBrackets" in params, "Missing parameter 'squareBrackets'"
    assert "id" in params, "Missing parameter 'id'"

def test_dsl::methoddeclarator_has_squareBrackets():
    assert hasattr(dsl::MethodDeclarator, "squareBrackets")
    descriptor = None
    for klass in dsl::MethodDeclarator.__mro__:
        if "squareBrackets" in klass.__dict__:
            descriptor = klass.__dict__["squareBrackets"]
            break
    assert isinstance(descriptor, property)

def test_dsl::methoddeclarator_has_id():
    assert hasattr(dsl::MethodDeclarator, "id")
    descriptor = None
    for klass in dsl::MethodDeclarator.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl::resulttype_is_not_abstract():
    assert not inspect.isabstract(dsl::ResultType)


def test_dsl::resulttype_constructor_exists():
    assert callable(dsl::ResultType.__init__)


def test_dsl::resulttype_constructor_args():
    sig = inspect.signature(dsl::ResultType.__init__)
    params = list(sig.parameters.keys())



def test_dsl::blockstatement_is_not_abstract():
    assert not inspect.isabstract(dsl::BlockStatement)


def test_dsl::blockstatement_constructor_exists():
    assert callable(dsl::BlockStatement.__init__)


def test_dsl::blockstatement_constructor_args():
    sig = inspect.signature(dsl::BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_dsl::explicitconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(dsl::ExplicitConstructorInvocation)


def test_dsl::explicitconstructorinvocation_constructor_exists():
    assert callable(dsl::ExplicitConstructorInvocation.__init__)


def test_dsl::explicitconstructorinvocation_constructor_args():
    sig = inspect.signature(dsl::ExplicitConstructorInvocation.__init__)
    params = list(sig.parameters.keys())
    assert "self" in params, "Missing parameter 'self'"
    assert "parent" in params, "Missing parameter 'parent'"

def test_dsl::explicitconstructorinvocation_has_self():
    assert hasattr(dsl::ExplicitConstructorInvocation, "self")
    descriptor = None
    for klass in dsl::ExplicitConstructorInvocation.__mro__:
        if "self" in klass.__dict__:
            descriptor = klass.__dict__["self"]
            break
    assert isinstance(descriptor, property)

def test_dsl::explicitconstructorinvocation_has_parent():
    assert hasattr(dsl::ExplicitConstructorInvocation, "parent")
    descriptor = None
    for klass in dsl::ExplicitConstructorInvocation.__mro__:
        if "parent" in klass.__dict__:
            descriptor = klass.__dict__["parent"]
            break
    assert isinstance(descriptor, property)



def test_dsl::namelist_is_not_abstract():
    assert not inspect.isabstract(dsl::NameList)


def test_dsl::namelist_constructor_exists():
    assert callable(dsl::NameList.__init__)


def test_dsl::namelist_constructor_args():
    sig = inspect.signature(dsl::NameList.__init__)
    params = list(sig.parameters.keys())



def test_dsl::formalparameters_is_not_abstract():
    assert not inspect.isabstract(dsl::FormalParameters)


def test_dsl::formalparameters_constructor_exists():
    assert callable(dsl::FormalParameters.__init__)


def test_dsl::formalparameters_constructor_args():
    sig = inspect.signature(dsl::FormalParameters.__init__)
    params = list(sig.parameters.keys())



def test_dsl::expression_is_not_abstract():
    assert not inspect.isabstract(dsl::Expression)


def test_dsl::expression_constructor_exists():
    assert callable(dsl::Expression.__init__)


def test_dsl::expression_constructor_args():
    sig = inspect.signature(dsl::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "assignOp" in params, "Missing parameter 'assignOp'"

def test_dsl::expression_has_assignOp():
    assert hasattr(dsl::Expression, "assignOp")
    descriptor = None
    for klass in dsl::Expression.__mro__:
        if "assignOp" in klass.__dict__:
            descriptor = klass.__dict__["assignOp"]
            break
    assert isinstance(descriptor, property)



def test_dsl::arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(dsl::ArrayInitializer)


def test_dsl::arrayinitializer_constructor_exists():
    assert callable(dsl::ArrayInitializer.__init__)


def test_dsl::arrayinitializer_constructor_args():
    sig = inspect.signature(dsl::ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_dsl::variableinitializer_is_not_abstract():
    assert not inspect.isabstract(dsl::VariableInitializer)


def test_dsl::variableinitializer_constructor_exists():
    assert callable(dsl::VariableInitializer.__init__)


def test_dsl::variableinitializer_constructor_args():
    sig = inspect.signature(dsl::VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_dsl::type_is_not_abstract():
    assert not inspect.isabstract(dsl::Type)


def test_dsl::type_constructor_exists():
    assert callable(dsl::Type.__init__)


def test_dsl::type_constructor_args():
    sig = inspect.signature(dsl::Type.__init__)
    params = list(sig.parameters.keys())
    assert "primType" in params, "Missing parameter 'primType'"

def test_dsl::type_has_primType():
    assert hasattr(dsl::Type, "primType")
    descriptor = None
    for klass in dsl::Type.__mro__:
        if "primType" in klass.__dict__:
            descriptor = klass.__dict__["primType"]
            break
    assert isinstance(descriptor, property)



def test_dsl::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl::FieldDeclaration)


def test_dsl::fielddeclaration_constructor_exists():
    assert callable(dsl::FieldDeclaration.__init__)


def test_dsl::fielddeclaration_constructor_args():
    sig = inspect.signature(dsl::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dsl::methodorctordeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl::MethodOrCtorDeclaration)


def test_dsl::methodorctordeclaration_constructor_exists():
    assert callable(dsl::MethodOrCtorDeclaration.__init__)


def test_dsl::methodorctordeclaration_constructor_args():
    sig = inspect.signature(dsl::MethodOrCtorDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl::methodorctordeclaration_has_id():
    assert hasattr(dsl::MethodOrCtorDeclaration, "id")
    descriptor = None
    for klass in dsl::MethodOrCtorDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl::initializer_is_not_abstract():
    assert not inspect.isabstract(dsl::Initializer)


def test_dsl::initializer_constructor_exists():
    assert callable(dsl::Initializer.__init__)


def test_dsl::initializer_constructor_args():
    sig = inspect.signature(dsl::Initializer.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_dsl::initializer_has_static():
    assert hasattr(dsl::Initializer, "static")
    descriptor = None
    for klass in dsl::Initializer.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_dsl::typebound_is_not_abstract():
    assert not inspect.isabstract(dsl::TypeBound)


def test_dsl::typebound_constructor_exists():
    assert callable(dsl::TypeBound.__init__)


def test_dsl::typebound_constructor_args():
    sig = inspect.signature(dsl::TypeBound.__init__)
    params = list(sig.parameters.keys())



def test_dsl::typeparameter_is_not_abstract():
    assert not inspect.isabstract(dsl::TypeParameter)


def test_dsl::typeparameter_constructor_exists():
    assert callable(dsl::TypeParameter.__init__)


def test_dsl::typeparameter_constructor_args():
    sig = inspect.signature(dsl::TypeParameter.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl::typeparameter_has_id():
    assert hasattr(dsl::TypeParameter, "id")
    descriptor = None
    for klass in dsl::TypeParameter.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl::arguments_is_not_abstract():
    assert not inspect.isabstract(dsl::Arguments)


def test_dsl::arguments_constructor_exists():
    assert callable(dsl::Arguments.__init__)


def test_dsl::arguments_constructor_args():
    sig = inspect.signature(dsl::Arguments.__init__)
    params = list(sig.parameters.keys())



def test_dsl::classorinterfacebodydeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl::ClassOrInterfaceBodyDeclaration)


def test_dsl::classorinterfacebodydeclaration_constructor_exists():
    assert callable(dsl::ClassOrInterfaceBodyDeclaration.__init__)


def test_dsl::classorinterfacebodydeclaration_constructor_args():
    sig = inspect.signature(dsl::ClassOrInterfaceBodyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dsl::enumconstant_is_not_abstract():
    assert not inspect.isabstract(dsl::EnumConstant)


def test_dsl::enumconstant_constructor_exists():
    assert callable(dsl::EnumConstant.__init__)


def test_dsl::enumconstant_constructor_args():
    sig = inspect.signature(dsl::EnumConstant.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl::enumconstant_has_id():
    assert hasattr(dsl::EnumConstant, "id")
    descriptor = None
    for klass in dsl::EnumConstant.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl::enumbody_is_not_abstract():
    assert not inspect.isabstract(dsl::EnumBody)


def test_dsl::enumbody_constructor_exists():
    assert callable(dsl::EnumBody.__init__)


def test_dsl::enumbody_constructor_args():
    sig = inspect.signature(dsl::EnumBody.__init__)
    params = list(sig.parameters.keys())



def test_dsl::classorinterfacetype_is_not_abstract():
    assert not inspect.isabstract(dsl::ClassOrInterfaceType)


def test_dsl::classorinterfacetype_constructor_exists():
    assert callable(dsl::ClassOrInterfaceType.__init__)


def test_dsl::classorinterfacetype_constructor_args():
    sig = inspect.signature(dsl::ClassOrInterfaceType.__init__)
    params = list(sig.parameters.keys())
    assert "ids" in params, "Missing parameter 'ids'"

def test_dsl::classorinterfacetype_has_ids():
    assert hasattr(dsl::ClassOrInterfaceType, "ids")
    descriptor = None
    for klass in dsl::ClassOrInterfaceType.__mro__:
        if "ids" in klass.__dict__:
            descriptor = klass.__dict__["ids"]
            break
    assert isinstance(descriptor, property)



def test_dsl::classorinterfacebody_is_not_abstract():
    assert not inspect.isabstract(dsl::ClassOrInterfaceBody)


def test_dsl::classorinterfacebody_constructor_exists():
    assert callable(dsl::ClassOrInterfaceBody.__init__)


def test_dsl::classorinterfacebody_constructor_args():
    sig = inspect.signature(dsl::ClassOrInterfaceBody.__init__)
    params = list(sig.parameters.keys())



def test_dsl::implementslist_is_not_abstract():
    assert not inspect.isabstract(dsl::ImplementsList)


def test_dsl::implementslist_constructor_exists():
    assert callable(dsl::ImplementsList.__init__)


def test_dsl::implementslist_constructor_args():
    sig = inspect.signature(dsl::ImplementsList.__init__)
    params = list(sig.parameters.keys())



def test_dsl::extendslist_is_not_abstract():
    assert not inspect.isabstract(dsl::ExtendsList)


def test_dsl::extendslist_constructor_exists():
    assert callable(dsl::ExtendsList.__init__)


def test_dsl::extendslist_constructor_args():
    sig = inspect.signature(dsl::ExtendsList.__init__)
    params = list(sig.parameters.keys())



def test_dsl::typeparameters_is_not_abstract():
    assert not inspect.isabstract(dsl::TypeParameters)


def test_dsl::typeparameters_constructor_exists():
    assert callable(dsl::TypeParameters.__init__)


def test_dsl::typeparameters_constructor_args():
    sig = inspect.signature(dsl::TypeParameters.__init__)
    params = list(sig.parameters.keys())



def test_dsl::annotationtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl::AnnotationTypeDeclaration)


def test_dsl::annotationtypedeclaration_constructor_exists():
    assert callable(dsl::AnnotationTypeDeclaration.__init__)


def test_dsl::annotationtypedeclaration_constructor_args():
    sig = inspect.signature(dsl::AnnotationTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl::annotationtypedeclaration_has_id():
    assert hasattr(dsl::AnnotationTypeDeclaration, "id")
    descriptor = None
    for klass in dsl::AnnotationTypeDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl::enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl::EnumDeclaration)


def test_dsl::enumdeclaration_constructor_exists():
    assert callable(dsl::EnumDeclaration.__init__)


def test_dsl::enumdeclaration_constructor_args():
    sig = inspect.signature(dsl::EnumDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dsl::enumdeclaration_has_id():
    assert hasattr(dsl::EnumDeclaration, "id")
    descriptor = None
    for klass in dsl::EnumDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dsl::classorinterfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl::ClassOrInterfaceDeclaration)


def test_dsl::classorinterfacedeclaration_constructor_exists():
    assert callable(dsl::ClassOrInterfaceDeclaration.__init__)


def test_dsl::classorinterfacedeclaration_constructor_args():
    sig = inspect.signature(dsl::ClassOrInterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "typeCategory" in params, "Missing parameter 'typeCategory'"

def test_dsl::classorinterfacedeclaration_has_id():
    assert hasattr(dsl::ClassOrInterfaceDeclaration, "id")
    descriptor = None
    for klass in dsl::ClassOrInterfaceDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_dsl::classorinterfacedeclaration_has_typeCategory():
    assert hasattr(dsl::ClassOrInterfaceDeclaration, "typeCategory")
    descriptor = None
    for klass in dsl::ClassOrInterfaceDeclaration.__mro__:
        if "typeCategory" in klass.__dict__:
            descriptor = klass.__dict__["typeCategory"]
            break
    assert isinstance(descriptor, property)



def test_dsl::typebodymodifier_is_not_abstract():
    assert not inspect.isabstract(dsl::TypeBodyModifier)


def test_dsl::typebodymodifier_constructor_exists():
    assert callable(dsl::TypeBodyModifier.__init__)


def test_dsl::typebodymodifier_constructor_args():
    sig = inspect.signature(dsl::TypeBodyModifier.__init__)
    params = list(sig.parameters.keys())
    assert "transient" in params, "Missing parameter 'transient'"
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "strictfp" in params, "Missing parameter 'strictfp'"
    assert "native" in params, "Missing parameter 'native'"

def test_dsl::typebodymodifier_has_transient():
    assert hasattr(dsl::TypeBodyModifier, "transient")
    descriptor = None
    for klass in dsl::TypeBodyModifier.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_dsl::typebodymodifier_has_volatile():
    assert hasattr(dsl::TypeBodyModifier, "volatile")
    descriptor = None
    for klass in dsl::TypeBodyModifier.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_dsl::typebodymodifier_has_synchronized():
    assert hasattr(dsl::TypeBodyModifier, "synchronized")
    descriptor = None
    for klass in dsl::TypeBodyModifier.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_dsl::typebodymodifier_has_strictfp():
    assert hasattr(dsl::TypeBodyModifier, "strictfp")
    descriptor = None
    for klass in dsl::TypeBodyModifier.__mro__:
        if "strictfp" in klass.__dict__:
            descriptor = klass.__dict__["strictfp"]
            break
    assert isinstance(descriptor, property)

def test_dsl::typebodymodifier_has_native():
    assert hasattr(dsl::TypeBodyModifier, "native")
    descriptor = None
    for klass in dsl::TypeBodyModifier.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)



def test_dsl::commonmodifier_is_not_abstract():
    assert not inspect.isabstract(dsl::CommonModifier)


def test_dsl::commonmodifier_constructor_exists():
    assert callable(dsl::CommonModifier.__init__)


def test_dsl::commonmodifier_constructor_args():
    sig = inspect.signature(dsl::CommonModifier.__init__)
    params = list(sig.parameters.keys())
    assert "final" in params, "Missing parameter 'final'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "static" in params, "Missing parameter 'static'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_dsl::commonmodifier_has_final():
    assert hasattr(dsl::CommonModifier, "final")
    descriptor = None
    for klass in dsl::CommonModifier.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_dsl::commonmodifier_has_visibility():
    assert hasattr(dsl::CommonModifier, "visibility")
    descriptor = None
    for klass in dsl::CommonModifier.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_dsl::commonmodifier_has_static():
    assert hasattr(dsl::CommonModifier, "static")
    descriptor = None
    for klass in dsl::CommonModifier.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_dsl::commonmodifier_has_abstract():
    assert hasattr(dsl::CommonModifier, "abstract")
    descriptor = None
    for klass in dsl::CommonModifier.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_dsl::name_is_not_abstract():
    assert not inspect.isabstract(dsl::Name)


def test_dsl::name_constructor_exists():
    assert callable(dsl::Name.__init__)


def test_dsl::name_constructor_args():
    sig = inspect.signature(dsl::Name.__init__)
    params = list(sig.parameters.keys())
    assert "ids" in params, "Missing parameter 'ids'"

def test_dsl::name_has_ids():
    assert hasattr(dsl::Name, "ids")
    descriptor = None
    for klass in dsl::Name.__mro__:
        if "ids" in klass.__dict__:
            descriptor = klass.__dict__["ids"]
            break
    assert isinstance(descriptor, property)



def test_dsl::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl::TypeDeclaration)


def test_dsl::typedeclaration_constructor_exists():
    assert callable(dsl::TypeDeclaration.__init__)


def test_dsl::typedeclaration_constructor_args():
    sig = inspect.signature(dsl::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dsl::importdeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl::ImportDeclaration)


def test_dsl::importdeclaration_constructor_exists():
    assert callable(dsl::ImportDeclaration.__init__)


def test_dsl::importdeclaration_constructor_args():
    sig = inspect.signature(dsl::ImportDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dsl::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(dsl::PackageDeclaration)


def test_dsl::packagedeclaration_constructor_exists():
    assert callable(dsl::PackageDeclaration.__init__)


def test_dsl::packagedeclaration_constructor_args():
    sig = inspect.signature(dsl::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_dsl::compilationunit_is_not_abstract():
    assert not inspect.isabstract(dsl::CompilationUnit)


def test_dsl::compilationunit_constructor_exists():
    assert callable(dsl::CompilationUnit.__init__)


def test_dsl::compilationunit_constructor_args():
    sig = inspect.signature(dsl::CompilationUnit.__init__)
    params = list(sig.parameters.keys())

def test_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "PRIVATE",
        "PUBLIC",
        "PROTECTED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibility"


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
dsl::DefaultValue_strategy = st.builds(
    dsl::DefaultValue,
)
dsl::AnnotationTypeMemberDeclaration_strategy = st.builds(
    dsl::AnnotationTypeMemberDeclaration,
    id=
        safe_text
)
dsl::AnnotationTypeBody_strategy = st.builds(
    dsl::AnnotationTypeBody,
)
dsl::MemberValueArrayInitializer_strategy = st.builds(
    dsl::MemberValueArrayInitializer,
)
DefaultValue_strategy = st.builds(
    DefaultValue,
)
dsl::MemberValuePair_strategy = st.builds(
    dsl::MemberValuePair,
    id=
        safe_text
)
dsl::MemberValue_strategy = st.builds(
    dsl::MemberValue,
)
dsl::MemberValuePairs_strategy = st.builds(
    dsl::MemberValuePairs,
)
dsl::Annotation_strategy = st.builds(
    dsl::Annotation,
)
dsl::StatementExpressionList_strategy = st.builds(
    dsl::StatementExpressionList,
)
dsl::ForUpdate_strategy = st.builds(
    dsl::ForUpdate,
)
dsl::ForInit_strategy = st.builds(
    dsl::ForInit,
)
dsl::SwitchLabel_strategy = st.builds(
    dsl::SwitchLabel,
    defaultOp=
        safe_text
)
dsl::LocalVariableDeclaration_strategy = st.builds(
    dsl::LocalVariableDeclaration,
    finality=
        safe_text
)
dsl::TryStatement_strategy = st.builds(
    dsl::TryStatement,
)
dsl::SynchronizedStatement_strategy = st.builds(
    dsl::SynchronizedStatement,
)
dsl::ThrowStatement_strategy = st.builds(
    dsl::ThrowStatement,
)
dsl::ReturnStatement_strategy = st.builds(
    dsl::ReturnStatement,
)
dsl::ContinueStatement_strategy = st.builds(
    dsl::ContinueStatement,
    id=
        safe_text
)
dsl::BreakStatement_strategy = st.builds(
    dsl::BreakStatement,
    id=
        safe_text
)
dsl::ForStatement_strategy = st.builds(
    dsl::ForStatement,
    id=
        safe_text
)
dsl::DoStatement_strategy = st.builds(
    dsl::DoStatement,
)
dsl::WhileStatement_strategy = st.builds(
    dsl::WhileStatement,
)
dsl::IfStatement_strategy = st.builds(
    dsl::IfStatement,
)
dsl::SwitchStatement_strategy = st.builds(
    dsl::SwitchStatement,
)
dsl::StatementExpression_strategy = st.builds(
    dsl::StatementExpression,
    assignOp=
        safe_text,
    minOp=
        safe_text,
    plusOp=
        safe_text
)
dsl::AssertStatement_strategy = st.builds(
    dsl::AssertStatement,
)
dsl::LabeledStatement_strategy = st.builds(
    dsl::LabeledStatement,
    id=
        safe_text
)
dsl::ArrayDimsAndInits_strategy = st.builds(
    dsl::ArrayDimsAndInits,
    squareBrackets=
        safe_text
)
dsl::BaseLiteral_strategy = st.builds(
    dsl::BaseLiteral,
    binDigitsUnderscore=
        safe_text,
    decDigitsUnderscore=
        safe_text,
    hexDigitsUnderscore=
        safe_text
)
dsl::ArgumentList_strategy = st.builds(
    dsl::ArgumentList,
)
dsl::BooleanLiteral_strategy = st.builds(
    dsl::BooleanLiteral,
    truthiness=
        safe_text
)
dsl::FloatLiteral_strategy = st.builds(
    dsl::FloatLiteral,
    digits=
        safe_text
)
dsl::IntegerLiteral_strategy = st.builds(
    dsl::IntegerLiteral,
    zero=
        safe_text,
    one=
        safe_text
)
dsl::SignedIntLiteral_strategy = st.builds(
    dsl::SignedIntLiteral,
    bitWidth=
        st.integers()
)
dsl::UnsignedIntLiteral_strategy = st.builds(
    dsl::UnsignedIntLiteral,
    sign=
        safe_text
)
dsl::MemberSelector_strategy = st.builds(
    dsl::MemberSelector,
    id=
        safe_text
)
dsl::DecimalNumber_strategy = st.builds(
    dsl::DecimalNumber,
    decDigitsUnderscore=
        safe_text,
    decDigits=
        st.integers()
)
dsl::PrimarySuffix_strategy = st.builds(
    dsl::PrimarySuffix,
    thisOp=
        st.booleans(),
    id=
        safe_text
)
dsl::AllocationExpression_strategy = st.builds(
    dsl::AllocationExpression,
    primType=
        safe_text
)
dsl::PrimaryPrefix_strategy = st.builds(
    dsl::PrimaryPrefix,
    id=
        safe_text,
    superOp=
        safe_text,
    thisOp=
        safe_text
)
dsl::PreDecrementExpression_strategy = st.builds(
    dsl::PreDecrementExpression,
)
dsl::PreIncrementExpression_strategy = st.builds(
    dsl::PreIncrementExpression,
)
dsl::EObject_strategy = st.builds(
    dsl::EObject,
)
dsl::Literal_strategy = st.builds(
    dsl::Literal,
    charLit=
        safe_text,
    stringLit=
        safe_text,
    nullLit=
        safe_text
)
dsl::CastLookahead_strategy = st.builds(
    dsl::CastLookahead,
    openBracket=
        safe_text,
    negOp=
        safe_text,
    superOp=
        safe_text,
    id=
        safe_text,
    bitNegOp=
        safe_text,
    thisOp=
        safe_text,
    newOp=
        safe_text,
    primType=
        safe_text
)
dsl::PostfixExpression_strategy = st.builds(
    dsl::PostfixExpression,
    op=
        safe_text
)
dsl::CastExpression_strategy = st.builds(
    dsl::CastExpression,
)
dsl::UnaryExpressionNotPlusMinus_strategy = st.builds(
    dsl::UnaryExpressionNotPlusMinus,
    negOp=
        safe_text
)
dsl::UnaryExpression_strategy = st.builds(
    dsl::UnaryExpression,
    sign=
        safe_text
)
dsl::MultiplicativeExpression_strategy = st.builds(
    dsl::MultiplicativeExpression,
    ops=
        safe_text
)
dsl::AdditiveExpression_strategy = st.builds(
    dsl::AdditiveExpression,
    ops=
        safe_text
)
dsl::ShiftExpression_strategy = st.builds(
    dsl::ShiftExpression,
    ops=
        safe_text
)
dsl::RelationalExpression_strategy = st.builds(
    dsl::RelationalExpression,
    ops=
        safe_text
)
dsl::InstanceOfExpression_strategy = st.builds(
    dsl::InstanceOfExpression,
)
dsl::EqualityExpression_strategy = st.builds(
    dsl::EqualityExpression,
)
dsl::AndExpression_strategy = st.builds(
    dsl::AndExpression,
)
dsl::ExclusiveOrExpression_strategy = st.builds(
    dsl::ExclusiveOrExpression,
)
dsl::InclusiveOrExpression_strategy = st.builds(
    dsl::InclusiveOrExpression,
)
dsl::ConditionalAndExpression_strategy = st.builds(
    dsl::ConditionalAndExpression,
)
IfStatement_strategy = st.builds(
    IfStatement,
)
dsl::ConditionalOrExpression_strategy = st.builds(
    dsl::ConditionalOrExpression,
)
dsl::Statement_strategy = st.builds(
    dsl::Statement,
)
dsl::ConditionalExpression_strategy = st.builds(
    dsl::ConditionalExpression,
)
dsl::WildcardBounds_strategy = st.builds(
    dsl::WildcardBounds,
    sup=
        st.booleans(),
    ext=
        st.booleans()
)
dsl::TypeArgument_strategy = st.builds(
    dsl::TypeArgument,
)
dsl::TypeArguments_strategy = st.builds(
    dsl::TypeArguments,
)
dsl::ReferenceType_strategy = st.builds(
    dsl::ReferenceType,
    primType=
        safe_text,
    squareBracketsBeta=
        safe_text,
    squareBracketsAlpha=
        safe_text
)
dsl::PrimaryExpression_strategy = st.builds(
    dsl::PrimaryExpression,
)
dsl::VariableDeclaratorId_strategy = st.builds(
    dsl::VariableDeclaratorId,
    squareBrackets=
        safe_text,
    id=
        safe_text
)
dsl::VariableDeclarator_strategy = st.builds(
    dsl::VariableDeclarator,
)
dsl::FormalParameter_strategy = st.builds(
    dsl::FormalParameter,
    final=
        st.booleans()
)
dsl::Block_strategy = st.builds(
    dsl::Block,
)
dsl::MethodDeclarator_strategy = st.builds(
    dsl::MethodDeclarator,
    squareBrackets=
        safe_text,
    id=
        safe_text
)
dsl::ResultType_strategy = st.builds(
    dsl::ResultType,
)
dsl::BlockStatement_strategy = st.builds(
    dsl::BlockStatement,
)
dsl::ExplicitConstructorInvocation_strategy = st.builds(
    dsl::ExplicitConstructorInvocation,
    self=
        st.booleans(),
    parent=
        safe_text
)
dsl::NameList_strategy = st.builds(
    dsl::NameList,
)
dsl::FormalParameters_strategy = st.builds(
    dsl::FormalParameters,
)
dsl::Expression_strategy = st.builds(
    dsl::Expression,
    assignOp=
        safe_text
)
dsl::ArrayInitializer_strategy = st.builds(
    dsl::ArrayInitializer,
)
dsl::VariableInitializer_strategy = st.builds(
    dsl::VariableInitializer,
)
dsl::Type_strategy = st.builds(
    dsl::Type,
    primType=
        safe_text
)
dsl::FieldDeclaration_strategy = st.builds(
    dsl::FieldDeclaration,
)
dsl::MethodOrCtorDeclaration_strategy = st.builds(
    dsl::MethodOrCtorDeclaration,
    id=
        safe_text
)
dsl::Initializer_strategy = st.builds(
    dsl::Initializer,
    static=
        st.booleans()
)
dsl::TypeBound_strategy = st.builds(
    dsl::TypeBound,
)
dsl::TypeParameter_strategy = st.builds(
    dsl::TypeParameter,
    id=
        safe_text
)
dsl::Arguments_strategy = st.builds(
    dsl::Arguments,
)
dsl::ClassOrInterfaceBodyDeclaration_strategy = st.builds(
    dsl::ClassOrInterfaceBodyDeclaration,
)
dsl::EnumConstant_strategy = st.builds(
    dsl::EnumConstant,
    id=
        safe_text
)
dsl::EnumBody_strategy = st.builds(
    dsl::EnumBody,
)
dsl::ClassOrInterfaceType_strategy = st.builds(
    dsl::ClassOrInterfaceType,
    ids=
        safe_text
)
dsl::ClassOrInterfaceBody_strategy = st.builds(
    dsl::ClassOrInterfaceBody,
)
dsl::ImplementsList_strategy = st.builds(
    dsl::ImplementsList,
)
dsl::ExtendsList_strategy = st.builds(
    dsl::ExtendsList,
)
dsl::TypeParameters_strategy = st.builds(
    dsl::TypeParameters,
)
dsl::AnnotationTypeDeclaration_strategy = st.builds(
    dsl::AnnotationTypeDeclaration,
    id=
        safe_text
)
dsl::EnumDeclaration_strategy = st.builds(
    dsl::EnumDeclaration,
    id=
        safe_text
)
dsl::ClassOrInterfaceDeclaration_strategy = st.builds(
    dsl::ClassOrInterfaceDeclaration,
    id=
        safe_text,
    typeCategory=
        safe_text
)
dsl::TypeBodyModifier_strategy = st.builds(
    dsl::TypeBodyModifier,
    transient=
        st.booleans(),
    volatile=
        st.booleans(),
    synchronized=
        st.booleans(),
    strictfp=
        st.booleans(),
    native=
        st.booleans()
)
dsl::CommonModifier_strategy = st.builds(
    dsl::CommonModifier,
    final=
        st.booleans(),
    visibility=
        safe_text,
    static=
        st.booleans(),
    abstract=
        st.booleans()
)
dsl::Name_strategy = st.builds(
    dsl::Name,
    ids=
        safe_text
)
dsl::TypeDeclaration_strategy = st.builds(
    dsl::TypeDeclaration,
)
dsl::ImportDeclaration_strategy = st.builds(
    dsl::ImportDeclaration,
)
dsl::PackageDeclaration_strategy = st.builds(
    dsl::PackageDeclaration,
)
dsl::CompilationUnit_strategy = st.builds(
    dsl::CompilationUnit,
)

@given(instance=dsl::DefaultValue_strategy)
@settings(max_examples=50)
def test_dsl::defaultvalue_instantiation(instance):
    assert isinstance(instance, dsl::DefaultValue)

@given(instance=dsl::AnnotationTypeMemberDeclaration_strategy)
@settings(max_examples=50)
def test_dsl::annotationtypememberdeclaration_instantiation(instance):
    assert isinstance(instance, dsl::AnnotationTypeMemberDeclaration)

@given(instance=dsl::AnnotationTypeMemberDeclaration_strategy)
def test_dsl::annotationtypememberdeclaration_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dsl::AnnotationTypeMemberDeclaration_strategy)
def test_dsl::annotationtypememberdeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl::AnnotationTypeBody_strategy)
@settings(max_examples=50)
def test_dsl::annotationtypebody_instantiation(instance):
    assert isinstance(instance, dsl::AnnotationTypeBody)

@given(instance=dsl::MemberValueArrayInitializer_strategy)
@settings(max_examples=50)
def test_dsl::membervaluearrayinitializer_instantiation(instance):
    assert isinstance(instance, dsl::MemberValueArrayInitializer)

@given(instance=DefaultValue_strategy)
@settings(max_examples=50)
def test_defaultvalue_instantiation(instance):
    assert isinstance(instance, DefaultValue)

@given(instance=dsl::MemberValuePair_strategy)
@settings(max_examples=50)
def test_dsl::membervaluepair_instantiation(instance):
    assert isinstance(instance, dsl::MemberValuePair)

@given(instance=dsl::MemberValuePair_strategy)
def test_dsl::membervaluepair_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dsl::MemberValuePair_strategy)
def test_dsl::membervaluepair_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl::MemberValue_strategy)
@settings(max_examples=50)
def test_dsl::membervalue_instantiation(instance):
    assert isinstance(instance, dsl::MemberValue)

@given(instance=dsl::MemberValuePairs_strategy)
@settings(max_examples=50)
def test_dsl::membervaluepairs_instantiation(instance):
    assert isinstance(instance, dsl::MemberValuePairs)

@given(instance=dsl::Annotation_strategy)
@settings(max_examples=50)
def test_dsl::annotation_instantiation(instance):
    assert isinstance(instance, dsl::Annotation)

@given(instance=dsl::StatementExpressionList_strategy)
@settings(max_examples=50)
def test_dsl::statementexpressionlist_instantiation(instance):
    assert isinstance(instance, dsl::StatementExpressionList)

@given(instance=dsl::ForUpdate_strategy)
@settings(max_examples=50)
def test_dsl::forupdate_instantiation(instance):
    assert isinstance(instance, dsl::ForUpdate)

@given(instance=dsl::ForInit_strategy)
@settings(max_examples=50)
def test_dsl::forinit_instantiation(instance):
    assert isinstance(instance, dsl::ForInit)

@given(instance=dsl::SwitchLabel_strategy)
@settings(max_examples=50)
def test_dsl::switchlabel_instantiation(instance):
    assert isinstance(instance, dsl::SwitchLabel)

@given(instance=dsl::SwitchLabel_strategy)
def test_dsl::switchlabel_defaultOp_type(instance):
    assert isinstance(instance.defaultOp, str)


@given(instance=dsl::SwitchLabel_strategy)
def test_dsl::switchlabel_defaultOp_setter(instance):
    original = instance.defaultOp
    instance.defaultOp = original
    assert instance.defaultOp == original

@given(instance=dsl::LocalVariableDeclaration_strategy)
@settings(max_examples=50)
def test_dsl::localvariabledeclaration_instantiation(instance):
    assert isinstance(instance, dsl::LocalVariableDeclaration)

@given(instance=dsl::LocalVariableDeclaration_strategy)
def test_dsl::localvariabledeclaration_finality_type(instance):
    assert isinstance(instance.finality, str)


@given(instance=dsl::LocalVariableDeclaration_strategy)
def test_dsl::localvariabledeclaration_finality_setter(instance):
    original = instance.finality
    instance.finality = original
    assert instance.finality == original

@given(instance=dsl::TryStatement_strategy)
@settings(max_examples=50)
def test_dsl::trystatement_instantiation(instance):
    assert isinstance(instance, dsl::TryStatement)

@given(instance=dsl::SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_dsl::synchronizedstatement_instantiation(instance):
    assert isinstance(instance, dsl::SynchronizedStatement)

@given(instance=dsl::ThrowStatement_strategy)
@settings(max_examples=50)
def test_dsl::throwstatement_instantiation(instance):
    assert isinstance(instance, dsl::ThrowStatement)

@given(instance=dsl::ReturnStatement_strategy)
@settings(max_examples=50)
def test_dsl::returnstatement_instantiation(instance):
    assert isinstance(instance, dsl::ReturnStatement)

@given(instance=dsl::ContinueStatement_strategy)
@settings(max_examples=50)
def test_dsl::continuestatement_instantiation(instance):
    assert isinstance(instance, dsl::ContinueStatement)

@given(instance=dsl::ContinueStatement_strategy)
def test_dsl::continuestatement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dsl::ContinueStatement_strategy)
def test_dsl::continuestatement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl::BreakStatement_strategy)
@settings(max_examples=50)
def test_dsl::breakstatement_instantiation(instance):
    assert isinstance(instance, dsl::BreakStatement)

@given(instance=dsl::BreakStatement_strategy)
def test_dsl::breakstatement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dsl::BreakStatement_strategy)
def test_dsl::breakstatement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl::ForStatement_strategy)
@settings(max_examples=50)
def test_dsl::forstatement_instantiation(instance):
    assert isinstance(instance, dsl::ForStatement)

@given(instance=dsl::ForStatement_strategy)
def test_dsl::forstatement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dsl::ForStatement_strategy)
def test_dsl::forstatement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl::DoStatement_strategy)
@settings(max_examples=50)
def test_dsl::dostatement_instantiation(instance):
    assert isinstance(instance, dsl::DoStatement)

@given(instance=dsl::WhileStatement_strategy)
@settings(max_examples=50)
def test_dsl::whilestatement_instantiation(instance):
    assert isinstance(instance, dsl::WhileStatement)

@given(instance=dsl::IfStatement_strategy)
@settings(max_examples=50)
def test_dsl::ifstatement_instantiation(instance):
    assert isinstance(instance, dsl::IfStatement)

@given(instance=dsl::SwitchStatement_strategy)
@settings(max_examples=50)
def test_dsl::switchstatement_instantiation(instance):
    assert isinstance(instance, dsl::SwitchStatement)

@given(instance=dsl::StatementExpression_strategy)
@settings(max_examples=50)
def test_dsl::statementexpression_instantiation(instance):
    assert isinstance(instance, dsl::StatementExpression)

@given(instance=dsl::StatementExpression_strategy)
def test_dsl::statementexpression_assignOp_type(instance):
    assert isinstance(instance.assignOp, str)


@given(instance=dsl::StatementExpression_strategy)
def test_dsl::statementexpression_assignOp_setter(instance):
    original = instance.assignOp
    instance.assignOp = original
    assert instance.assignOp == original

@given(instance=dsl::StatementExpression_strategy)
def test_dsl::statementexpression_minOp_type(instance):
    assert isinstance(instance.minOp, str)


@given(instance=dsl::StatementExpression_strategy)
def test_dsl::statementexpression_minOp_setter(instance):
    original = instance.minOp
    instance.minOp = original
    assert instance.minOp == original

@given(instance=dsl::StatementExpression_strategy)
def test_dsl::statementexpression_plusOp_type(instance):
    assert isinstance(instance.plusOp, str)


@given(instance=dsl::StatementExpression_strategy)
def test_dsl::statementexpression_plusOp_setter(instance):
    original = instance.plusOp
    instance.plusOp = original
    assert instance.plusOp == original

@given(instance=dsl::AssertStatement_strategy)
@settings(max_examples=50)
def test_dsl::assertstatement_instantiation(instance):
    assert isinstance(instance, dsl::AssertStatement)

@given(instance=dsl::LabeledStatement_strategy)
@settings(max_examples=50)
def test_dsl::labeledstatement_instantiation(instance):
    assert isinstance(instance, dsl::LabeledStatement)

@given(instance=dsl::LabeledStatement_strategy)
def test_dsl::labeledstatement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dsl::LabeledStatement_strategy)
def test_dsl::labeledstatement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl::ArrayDimsAndInits_strategy)
@settings(max_examples=50)
def test_dsl::arraydimsandinits_instantiation(instance):
    assert isinstance(instance, dsl::ArrayDimsAndInits)

@given(instance=dsl::ArrayDimsAndInits_strategy)
def test_dsl::arraydimsandinits_squareBrackets_type(instance):
    assert isinstance(instance.squareBrackets, str)


@given(instance=dsl::ArrayDimsAndInits_strategy)
def test_dsl::arraydimsandinits_squareBrackets_setter(instance):
    original = instance.squareBrackets
    instance.squareBrackets = original
    assert instance.squareBrackets == original

@given(instance=dsl::BaseLiteral_strategy)
@settings(max_examples=50)
def test_dsl::baseliteral_instantiation(instance):
    assert isinstance(instance, dsl::BaseLiteral)

@given(instance=dsl::BaseLiteral_strategy)
def test_dsl::baseliteral_binDigitsUnderscore_type(instance):
    assert isinstance(instance.binDigitsUnderscore, str)


@given(instance=dsl::BaseLiteral_strategy)
def test_dsl::baseliteral_binDigitsUnderscore_setter(instance):
    original = instance.binDigitsUnderscore
    instance.binDigitsUnderscore = original
    assert instance.binDigitsUnderscore == original

@given(instance=dsl::BaseLiteral_strategy)
def test_dsl::baseliteral_decDigitsUnderscore_type(instance):
    assert isinstance(instance.decDigitsUnderscore, str)


@given(instance=dsl::BaseLiteral_strategy)
def test_dsl::baseliteral_decDigitsUnderscore_setter(instance):
    original = instance.decDigitsUnderscore
    instance.decDigitsUnderscore = original
    assert instance.decDigitsUnderscore == original

@given(instance=dsl::BaseLiteral_strategy)
def test_dsl::baseliteral_hexDigitsUnderscore_type(instance):
    assert isinstance(instance.hexDigitsUnderscore, str)


@given(instance=dsl::BaseLiteral_strategy)
def test_dsl::baseliteral_hexDigitsUnderscore_setter(instance):
    original = instance.hexDigitsUnderscore
    instance.hexDigitsUnderscore = original
    assert instance.hexDigitsUnderscore == original

@given(instance=dsl::ArgumentList_strategy)
@settings(max_examples=50)
def test_dsl::argumentlist_instantiation(instance):
    assert isinstance(instance, dsl::ArgumentList)

@given(instance=dsl::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_dsl::booleanliteral_instantiation(instance):
    assert isinstance(instance, dsl::BooleanLiteral)

@given(instance=dsl::BooleanLiteral_strategy)
def test_dsl::booleanliteral_truthiness_type(instance):
    assert isinstance(instance.truthiness, str)


@given(instance=dsl::BooleanLiteral_strategy)
def test_dsl::booleanliteral_truthiness_setter(instance):
    original = instance.truthiness
    instance.truthiness = original
    assert instance.truthiness == original

@given(instance=dsl::FloatLiteral_strategy)
@settings(max_examples=50)
def test_dsl::floatliteral_instantiation(instance):
    assert isinstance(instance, dsl::FloatLiteral)

@given(instance=dsl::FloatLiteral_strategy)
def test_dsl::floatliteral_digits_type(instance):
    assert isinstance(instance.digits, str)


@given(instance=dsl::FloatLiteral_strategy)
def test_dsl::floatliteral_digits_setter(instance):
    original = instance.digits
    instance.digits = original
    assert instance.digits == original

@given(instance=dsl::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_dsl::integerliteral_instantiation(instance):
    assert isinstance(instance, dsl::IntegerLiteral)

@given(instance=dsl::IntegerLiteral_strategy)
def test_dsl::integerliteral_zero_type(instance):
    assert isinstance(instance.zero, str)


@given(instance=dsl::IntegerLiteral_strategy)
def test_dsl::integerliteral_zero_setter(instance):
    original = instance.zero
    instance.zero = original
    assert instance.zero == original

@given(instance=dsl::IntegerLiteral_strategy)
def test_dsl::integerliteral_one_type(instance):
    assert isinstance(instance.one, str)


@given(instance=dsl::IntegerLiteral_strategy)
def test_dsl::integerliteral_one_setter(instance):
    original = instance.one
    instance.one = original
    assert instance.one == original

@given(instance=dsl::SignedIntLiteral_strategy)
@settings(max_examples=50)
def test_dsl::signedintliteral_instantiation(instance):
    assert isinstance(instance, dsl::SignedIntLiteral)

@given(instance=dsl::SignedIntLiteral_strategy)
def test_dsl::signedintliteral_bitWidth_type(instance):
    assert isinstance(instance.bitWidth, int)


@given(instance=dsl::SignedIntLiteral_strategy)
def test_dsl::signedintliteral_bitWidth_setter(instance):
    original = instance.bitWidth
    instance.bitWidth = original
    assert instance.bitWidth == original

@given(instance=dsl::UnsignedIntLiteral_strategy)
@settings(max_examples=50)
def test_dsl::unsignedintliteral_instantiation(instance):
    assert isinstance(instance, dsl::UnsignedIntLiteral)

@given(instance=dsl::UnsignedIntLiteral_strategy)
def test_dsl::unsignedintliteral_sign_type(instance):
    assert isinstance(instance.sign, str)


@given(instance=dsl::UnsignedIntLiteral_strategy)
def test_dsl::unsignedintliteral_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original

@given(instance=dsl::MemberSelector_strategy)
@settings(max_examples=50)
def test_dsl::memberselector_instantiation(instance):
    assert isinstance(instance, dsl::MemberSelector)

@given(instance=dsl::MemberSelector_strategy)
def test_dsl::memberselector_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dsl::MemberSelector_strategy)
def test_dsl::memberselector_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl::DecimalNumber_strategy)
@settings(max_examples=50)
def test_dsl::decimalnumber_instantiation(instance):
    assert isinstance(instance, dsl::DecimalNumber)

@given(instance=dsl::DecimalNumber_strategy)
def test_dsl::decimalnumber_decDigitsUnderscore_type(instance):
    assert isinstance(instance.decDigitsUnderscore, str)


@given(instance=dsl::DecimalNumber_strategy)
def test_dsl::decimalnumber_decDigitsUnderscore_setter(instance):
    original = instance.decDigitsUnderscore
    instance.decDigitsUnderscore = original
    assert instance.decDigitsUnderscore == original

@given(instance=dsl::DecimalNumber_strategy)
def test_dsl::decimalnumber_decDigits_type(instance):
    assert isinstance(instance.decDigits, int)


@given(instance=dsl::DecimalNumber_strategy)
def test_dsl::decimalnumber_decDigits_setter(instance):
    original = instance.decDigits
    instance.decDigits = original
    assert instance.decDigits == original

@given(instance=dsl::PrimarySuffix_strategy)
@settings(max_examples=50)
def test_dsl::primarysuffix_instantiation(instance):
    assert isinstance(instance, dsl::PrimarySuffix)

@given(instance=dsl::PrimarySuffix_strategy)
def test_dsl::primarysuffix_thisOp_type(instance):
    assert isinstance(instance.thisOp, bool)


@given(instance=dsl::PrimarySuffix_strategy)
def test_dsl::primarysuffix_thisOp_setter(instance):
    original = instance.thisOp
    instance.thisOp = original
    assert instance.thisOp == original

@given(instance=dsl::PrimarySuffix_strategy)
def test_dsl::primarysuffix_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dsl::PrimarySuffix_strategy)
def test_dsl::primarysuffix_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl::AllocationExpression_strategy)
@settings(max_examples=50)
def test_dsl::allocationexpression_instantiation(instance):
    assert isinstance(instance, dsl::AllocationExpression)

@given(instance=dsl::AllocationExpression_strategy)
def test_dsl::allocationexpression_primType_type(instance):
    assert isinstance(instance.primType, str)


@given(instance=dsl::AllocationExpression_strategy)
def test_dsl::allocationexpression_primType_setter(instance):
    original = instance.primType
    instance.primType = original
    assert instance.primType == original

@given(instance=dsl::PrimaryPrefix_strategy)
@settings(max_examples=50)
def test_dsl::primaryprefix_instantiation(instance):
    assert isinstance(instance, dsl::PrimaryPrefix)

@given(instance=dsl::PrimaryPrefix_strategy)
def test_dsl::primaryprefix_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dsl::PrimaryPrefix_strategy)
def test_dsl::primaryprefix_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl::PrimaryPrefix_strategy)
def test_dsl::primaryprefix_superOp_type(instance):
    assert isinstance(instance.superOp, str)


@given(instance=dsl::PrimaryPrefix_strategy)
def test_dsl::primaryprefix_superOp_setter(instance):
    original = instance.superOp
    instance.superOp = original
    assert instance.superOp == original

@given(instance=dsl::PrimaryPrefix_strategy)
def test_dsl::primaryprefix_thisOp_type(instance):
    assert isinstance(instance.thisOp, str)


@given(instance=dsl::PrimaryPrefix_strategy)
def test_dsl::primaryprefix_thisOp_setter(instance):
    original = instance.thisOp
    instance.thisOp = original
    assert instance.thisOp == original

@given(instance=dsl::PreDecrementExpression_strategy)
@settings(max_examples=50)
def test_dsl::predecrementexpression_instantiation(instance):
    assert isinstance(instance, dsl::PreDecrementExpression)

@given(instance=dsl::PreIncrementExpression_strategy)
@settings(max_examples=50)
def test_dsl::preincrementexpression_instantiation(instance):
    assert isinstance(instance, dsl::PreIncrementExpression)

@given(instance=dsl::EObject_strategy)
@settings(max_examples=50)
def test_dsl::eobject_instantiation(instance):
    assert isinstance(instance, dsl::EObject)

@given(instance=dsl::Literal_strategy)
@settings(max_examples=50)
def test_dsl::literal_instantiation(instance):
    assert isinstance(instance, dsl::Literal)

@given(instance=dsl::Literal_strategy)
def test_dsl::literal_charLit_type(instance):
    assert isinstance(instance.charLit, str)


@given(instance=dsl::Literal_strategy)
def test_dsl::literal_charLit_setter(instance):
    original = instance.charLit
    instance.charLit = original
    assert instance.charLit == original

@given(instance=dsl::Literal_strategy)
def test_dsl::literal_stringLit_type(instance):
    assert isinstance(instance.stringLit, str)


@given(instance=dsl::Literal_strategy)
def test_dsl::literal_stringLit_setter(instance):
    original = instance.stringLit
    instance.stringLit = original
    assert instance.stringLit == original

@given(instance=dsl::Literal_strategy)
def test_dsl::literal_nullLit_type(instance):
    assert isinstance(instance.nullLit, str)


@given(instance=dsl::Literal_strategy)
def test_dsl::literal_nullLit_setter(instance):
    original = instance.nullLit
    instance.nullLit = original
    assert instance.nullLit == original

@given(instance=dsl::CastLookahead_strategy)
@settings(max_examples=50)
def test_dsl::castlookahead_instantiation(instance):
    assert isinstance(instance, dsl::CastLookahead)

@given(instance=dsl::CastLookahead_strategy)
def test_dsl::castlookahead_openBracket_type(instance):
    assert isinstance(instance.openBracket, str)


@given(instance=dsl::CastLookahead_strategy)
def test_dsl::castlookahead_openBracket_setter(instance):
    original = instance.openBracket
    instance.openBracket = original
    assert instance.openBracket == original

@given(instance=dsl::CastLookahead_strategy)
def test_dsl::castlookahead_negOp_type(instance):
    assert isinstance(instance.negOp, str)


@given(instance=dsl::CastLookahead_strategy)
def test_dsl::castlookahead_negOp_setter(instance):
    original = instance.negOp
    instance.negOp = original
    assert instance.negOp == original

@given(instance=dsl::CastLookahead_strategy)
def test_dsl::castlookahead_superOp_type(instance):
    assert isinstance(instance.superOp, str)


@given(instance=dsl::CastLookahead_strategy)
def test_dsl::castlookahead_superOp_setter(instance):
    original = instance.superOp
    instance.superOp = original
    assert instance.superOp == original

@given(instance=dsl::CastLookahead_strategy)
def test_dsl::castlookahead_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dsl::CastLookahead_strategy)
def test_dsl::castlookahead_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl::CastLookahead_strategy)
def test_dsl::castlookahead_bitNegOp_type(instance):
    assert isinstance(instance.bitNegOp, str)


@given(instance=dsl::CastLookahead_strategy)
def test_dsl::castlookahead_bitNegOp_setter(instance):
    original = instance.bitNegOp
    instance.bitNegOp = original
    assert instance.bitNegOp == original

@given(instance=dsl::CastLookahead_strategy)
def test_dsl::castlookahead_thisOp_type(instance):
    assert isinstance(instance.thisOp, str)


@given(instance=dsl::CastLookahead_strategy)
def test_dsl::castlookahead_thisOp_setter(instance):
    original = instance.thisOp
    instance.thisOp = original
    assert instance.thisOp == original

@given(instance=dsl::CastLookahead_strategy)
def test_dsl::castlookahead_newOp_type(instance):
    assert isinstance(instance.newOp, str)


@given(instance=dsl::CastLookahead_strategy)
def test_dsl::castlookahead_newOp_setter(instance):
    original = instance.newOp
    instance.newOp = original
    assert instance.newOp == original

@given(instance=dsl::CastLookahead_strategy)
def test_dsl::castlookahead_primType_type(instance):
    assert isinstance(instance.primType, str)


@given(instance=dsl::CastLookahead_strategy)
def test_dsl::castlookahead_primType_setter(instance):
    original = instance.primType
    instance.primType = original
    assert instance.primType == original

@given(instance=dsl::PostfixExpression_strategy)
@settings(max_examples=50)
def test_dsl::postfixexpression_instantiation(instance):
    assert isinstance(instance, dsl::PostfixExpression)

@given(instance=dsl::PostfixExpression_strategy)
def test_dsl::postfixexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=dsl::PostfixExpression_strategy)
def test_dsl::postfixexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=dsl::CastExpression_strategy)
@settings(max_examples=50)
def test_dsl::castexpression_instantiation(instance):
    assert isinstance(instance, dsl::CastExpression)

@given(instance=dsl::UnaryExpressionNotPlusMinus_strategy)
@settings(max_examples=50)
def test_dsl::unaryexpressionnotplusminus_instantiation(instance):
    assert isinstance(instance, dsl::UnaryExpressionNotPlusMinus)

@given(instance=dsl::UnaryExpressionNotPlusMinus_strategy)
def test_dsl::unaryexpressionnotplusminus_negOp_type(instance):
    assert isinstance(instance.negOp, str)


@given(instance=dsl::UnaryExpressionNotPlusMinus_strategy)
def test_dsl::unaryexpressionnotplusminus_negOp_setter(instance):
    original = instance.negOp
    instance.negOp = original
    assert instance.negOp == original

@given(instance=dsl::UnaryExpression_strategy)
@settings(max_examples=50)
def test_dsl::unaryexpression_instantiation(instance):
    assert isinstance(instance, dsl::UnaryExpression)

@given(instance=dsl::UnaryExpression_strategy)
def test_dsl::unaryexpression_sign_type(instance):
    assert isinstance(instance.sign, str)


@given(instance=dsl::UnaryExpression_strategy)
def test_dsl::unaryexpression_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original

@given(instance=dsl::MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_dsl::multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, dsl::MultiplicativeExpression)

@given(instance=dsl::MultiplicativeExpression_strategy)
def test_dsl::multiplicativeexpression_ops_type(instance):
    assert isinstance(instance.ops, str)


@given(instance=dsl::MultiplicativeExpression_strategy)
def test_dsl::multiplicativeexpression_ops_setter(instance):
    original = instance.ops
    instance.ops = original
    assert instance.ops == original

@given(instance=dsl::AdditiveExpression_strategy)
@settings(max_examples=50)
def test_dsl::additiveexpression_instantiation(instance):
    assert isinstance(instance, dsl::AdditiveExpression)

@given(instance=dsl::AdditiveExpression_strategy)
def test_dsl::additiveexpression_ops_type(instance):
    assert isinstance(instance.ops, str)


@given(instance=dsl::AdditiveExpression_strategy)
def test_dsl::additiveexpression_ops_setter(instance):
    original = instance.ops
    instance.ops = original
    assert instance.ops == original

@given(instance=dsl::ShiftExpression_strategy)
@settings(max_examples=50)
def test_dsl::shiftexpression_instantiation(instance):
    assert isinstance(instance, dsl::ShiftExpression)

@given(instance=dsl::ShiftExpression_strategy)
def test_dsl::shiftexpression_ops_type(instance):
    assert isinstance(instance.ops, str)


@given(instance=dsl::ShiftExpression_strategy)
def test_dsl::shiftexpression_ops_setter(instance):
    original = instance.ops
    instance.ops = original
    assert instance.ops == original

@given(instance=dsl::RelationalExpression_strategy)
@settings(max_examples=50)
def test_dsl::relationalexpression_instantiation(instance):
    assert isinstance(instance, dsl::RelationalExpression)

@given(instance=dsl::RelationalExpression_strategy)
def test_dsl::relationalexpression_ops_type(instance):
    assert isinstance(instance.ops, str)


@given(instance=dsl::RelationalExpression_strategy)
def test_dsl::relationalexpression_ops_setter(instance):
    original = instance.ops
    instance.ops = original
    assert instance.ops == original

@given(instance=dsl::InstanceOfExpression_strategy)
@settings(max_examples=50)
def test_dsl::instanceofexpression_instantiation(instance):
    assert isinstance(instance, dsl::InstanceOfExpression)

@given(instance=dsl::EqualityExpression_strategy)
@settings(max_examples=50)
def test_dsl::equalityexpression_instantiation(instance):
    assert isinstance(instance, dsl::EqualityExpression)

@given(instance=dsl::AndExpression_strategy)
@settings(max_examples=50)
def test_dsl::andexpression_instantiation(instance):
    assert isinstance(instance, dsl::AndExpression)

@given(instance=dsl::ExclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_dsl::exclusiveorexpression_instantiation(instance):
    assert isinstance(instance, dsl::ExclusiveOrExpression)

@given(instance=dsl::InclusiveOrExpression_strategy)
@settings(max_examples=50)
def test_dsl::inclusiveorexpression_instantiation(instance):
    assert isinstance(instance, dsl::InclusiveOrExpression)

@given(instance=dsl::ConditionalAndExpression_strategy)
@settings(max_examples=50)
def test_dsl::conditionalandexpression_instantiation(instance):
    assert isinstance(instance, dsl::ConditionalAndExpression)

@given(instance=IfStatement_strategy)
@settings(max_examples=50)
def test_ifstatement_instantiation(instance):
    assert isinstance(instance, IfStatement)

@given(instance=dsl::ConditionalOrExpression_strategy)
@settings(max_examples=50)
def test_dsl::conditionalorexpression_instantiation(instance):
    assert isinstance(instance, dsl::ConditionalOrExpression)

@given(instance=dsl::Statement_strategy)
@settings(max_examples=50)
def test_dsl::statement_instantiation(instance):
    assert isinstance(instance, dsl::Statement)

@given(instance=dsl::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_dsl::conditionalexpression_instantiation(instance):
    assert isinstance(instance, dsl::ConditionalExpression)

@given(instance=dsl::WildcardBounds_strategy)
@settings(max_examples=50)
def test_dsl::wildcardbounds_instantiation(instance):
    assert isinstance(instance, dsl::WildcardBounds)

@given(instance=dsl::WildcardBounds_strategy)
def test_dsl::wildcardbounds_sup_type(instance):
    assert isinstance(instance.sup, bool)


@given(instance=dsl::WildcardBounds_strategy)
def test_dsl::wildcardbounds_sup_setter(instance):
    original = instance.sup
    instance.sup = original
    assert instance.sup == original

@given(instance=dsl::WildcardBounds_strategy)
def test_dsl::wildcardbounds_ext_type(instance):
    assert isinstance(instance.ext, bool)


@given(instance=dsl::WildcardBounds_strategy)
def test_dsl::wildcardbounds_ext_setter(instance):
    original = instance.ext
    instance.ext = original
    assert instance.ext == original

@given(instance=dsl::TypeArgument_strategy)
@settings(max_examples=50)
def test_dsl::typeargument_instantiation(instance):
    assert isinstance(instance, dsl::TypeArgument)

@given(instance=dsl::TypeArguments_strategy)
@settings(max_examples=50)
def test_dsl::typearguments_instantiation(instance):
    assert isinstance(instance, dsl::TypeArguments)

@given(instance=dsl::ReferenceType_strategy)
@settings(max_examples=50)
def test_dsl::referencetype_instantiation(instance):
    assert isinstance(instance, dsl::ReferenceType)

@given(instance=dsl::ReferenceType_strategy)
def test_dsl::referencetype_primType_type(instance):
    assert isinstance(instance.primType, str)


@given(instance=dsl::ReferenceType_strategy)
def test_dsl::referencetype_primType_setter(instance):
    original = instance.primType
    instance.primType = original
    assert instance.primType == original

@given(instance=dsl::ReferenceType_strategy)
def test_dsl::referencetype_squareBracketsBeta_type(instance):
    assert isinstance(instance.squareBracketsBeta, str)


@given(instance=dsl::ReferenceType_strategy)
def test_dsl::referencetype_squareBracketsBeta_setter(instance):
    original = instance.squareBracketsBeta
    instance.squareBracketsBeta = original
    assert instance.squareBracketsBeta == original

@given(instance=dsl::ReferenceType_strategy)
def test_dsl::referencetype_squareBracketsAlpha_type(instance):
    assert isinstance(instance.squareBracketsAlpha, str)


@given(instance=dsl::ReferenceType_strategy)
def test_dsl::referencetype_squareBracketsAlpha_setter(instance):
    original = instance.squareBracketsAlpha
    instance.squareBracketsAlpha = original
    assert instance.squareBracketsAlpha == original

@given(instance=dsl::PrimaryExpression_strategy)
@settings(max_examples=50)
def test_dsl::primaryexpression_instantiation(instance):
    assert isinstance(instance, dsl::PrimaryExpression)

@given(instance=dsl::VariableDeclaratorId_strategy)
@settings(max_examples=50)
def test_dsl::variabledeclaratorid_instantiation(instance):
    assert isinstance(instance, dsl::VariableDeclaratorId)

@given(instance=dsl::VariableDeclaratorId_strategy)
def test_dsl::variabledeclaratorid_squareBrackets_type(instance):
    assert isinstance(instance.squareBrackets, str)


@given(instance=dsl::VariableDeclaratorId_strategy)
def test_dsl::variabledeclaratorid_squareBrackets_setter(instance):
    original = instance.squareBrackets
    instance.squareBrackets = original
    assert instance.squareBrackets == original

@given(instance=dsl::VariableDeclaratorId_strategy)
def test_dsl::variabledeclaratorid_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dsl::VariableDeclaratorId_strategy)
def test_dsl::variabledeclaratorid_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl::VariableDeclarator_strategy)
@settings(max_examples=50)
def test_dsl::variabledeclarator_instantiation(instance):
    assert isinstance(instance, dsl::VariableDeclarator)

@given(instance=dsl::FormalParameter_strategy)
@settings(max_examples=50)
def test_dsl::formalparameter_instantiation(instance):
    assert isinstance(instance, dsl::FormalParameter)

@given(instance=dsl::FormalParameter_strategy)
def test_dsl::formalparameter_final_type(instance):
    assert isinstance(instance.final, bool)


@given(instance=dsl::FormalParameter_strategy)
def test_dsl::formalparameter_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=dsl::Block_strategy)
@settings(max_examples=50)
def test_dsl::block_instantiation(instance):
    assert isinstance(instance, dsl::Block)

@given(instance=dsl::MethodDeclarator_strategy)
@settings(max_examples=50)
def test_dsl::methoddeclarator_instantiation(instance):
    assert isinstance(instance, dsl::MethodDeclarator)

@given(instance=dsl::MethodDeclarator_strategy)
def test_dsl::methoddeclarator_squareBrackets_type(instance):
    assert isinstance(instance.squareBrackets, str)


@given(instance=dsl::MethodDeclarator_strategy)
def test_dsl::methoddeclarator_squareBrackets_setter(instance):
    original = instance.squareBrackets
    instance.squareBrackets = original
    assert instance.squareBrackets == original

@given(instance=dsl::MethodDeclarator_strategy)
def test_dsl::methoddeclarator_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dsl::MethodDeclarator_strategy)
def test_dsl::methoddeclarator_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl::ResultType_strategy)
@settings(max_examples=50)
def test_dsl::resulttype_instantiation(instance):
    assert isinstance(instance, dsl::ResultType)

@given(instance=dsl::BlockStatement_strategy)
@settings(max_examples=50)
def test_dsl::blockstatement_instantiation(instance):
    assert isinstance(instance, dsl::BlockStatement)

@given(instance=dsl::ExplicitConstructorInvocation_strategy)
@settings(max_examples=50)
def test_dsl::explicitconstructorinvocation_instantiation(instance):
    assert isinstance(instance, dsl::ExplicitConstructorInvocation)

@given(instance=dsl::ExplicitConstructorInvocation_strategy)
def test_dsl::explicitconstructorinvocation_self_type(instance):
    assert isinstance(instance.self, bool)


@given(instance=dsl::ExplicitConstructorInvocation_strategy)
def test_dsl::explicitconstructorinvocation_self_setter(instance):
    original = instance.self
    instance.self = original
    assert instance.self == original

@given(instance=dsl::ExplicitConstructorInvocation_strategy)
def test_dsl::explicitconstructorinvocation_parent_type(instance):
    assert isinstance(instance.parent, str)


@given(instance=dsl::ExplicitConstructorInvocation_strategy)
def test_dsl::explicitconstructorinvocation_parent_setter(instance):
    original = instance.parent
    instance.parent = original
    assert instance.parent == original

@given(instance=dsl::NameList_strategy)
@settings(max_examples=50)
def test_dsl::namelist_instantiation(instance):
    assert isinstance(instance, dsl::NameList)

@given(instance=dsl::FormalParameters_strategy)
@settings(max_examples=50)
def test_dsl::formalparameters_instantiation(instance):
    assert isinstance(instance, dsl::FormalParameters)

@given(instance=dsl::Expression_strategy)
@settings(max_examples=50)
def test_dsl::expression_instantiation(instance):
    assert isinstance(instance, dsl::Expression)

@given(instance=dsl::Expression_strategy)
def test_dsl::expression_assignOp_type(instance):
    assert isinstance(instance.assignOp, str)


@given(instance=dsl::Expression_strategy)
def test_dsl::expression_assignOp_setter(instance):
    original = instance.assignOp
    instance.assignOp = original
    assert instance.assignOp == original

@given(instance=dsl::ArrayInitializer_strategy)
@settings(max_examples=50)
def test_dsl::arrayinitializer_instantiation(instance):
    assert isinstance(instance, dsl::ArrayInitializer)

@given(instance=dsl::VariableInitializer_strategy)
@settings(max_examples=50)
def test_dsl::variableinitializer_instantiation(instance):
    assert isinstance(instance, dsl::VariableInitializer)

@given(instance=dsl::Type_strategy)
@settings(max_examples=50)
def test_dsl::type_instantiation(instance):
    assert isinstance(instance, dsl::Type)

@given(instance=dsl::Type_strategy)
def test_dsl::type_primType_type(instance):
    assert isinstance(instance.primType, str)


@given(instance=dsl::Type_strategy)
def test_dsl::type_primType_setter(instance):
    original = instance.primType
    instance.primType = original
    assert instance.primType == original

@given(instance=dsl::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_dsl::fielddeclaration_instantiation(instance):
    assert isinstance(instance, dsl::FieldDeclaration)

@given(instance=dsl::MethodOrCtorDeclaration_strategy)
@settings(max_examples=50)
def test_dsl::methodorctordeclaration_instantiation(instance):
    assert isinstance(instance, dsl::MethodOrCtorDeclaration)

@given(instance=dsl::MethodOrCtorDeclaration_strategy)
def test_dsl::methodorctordeclaration_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dsl::MethodOrCtorDeclaration_strategy)
def test_dsl::methodorctordeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl::Initializer_strategy)
@settings(max_examples=50)
def test_dsl::initializer_instantiation(instance):
    assert isinstance(instance, dsl::Initializer)

@given(instance=dsl::Initializer_strategy)
def test_dsl::initializer_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=dsl::Initializer_strategy)
def test_dsl::initializer_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=dsl::TypeBound_strategy)
@settings(max_examples=50)
def test_dsl::typebound_instantiation(instance):
    assert isinstance(instance, dsl::TypeBound)

@given(instance=dsl::TypeParameter_strategy)
@settings(max_examples=50)
def test_dsl::typeparameter_instantiation(instance):
    assert isinstance(instance, dsl::TypeParameter)

@given(instance=dsl::TypeParameter_strategy)
def test_dsl::typeparameter_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dsl::TypeParameter_strategy)
def test_dsl::typeparameter_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl::Arguments_strategy)
@settings(max_examples=50)
def test_dsl::arguments_instantiation(instance):
    assert isinstance(instance, dsl::Arguments)

@given(instance=dsl::ClassOrInterfaceBodyDeclaration_strategy)
@settings(max_examples=50)
def test_dsl::classorinterfacebodydeclaration_instantiation(instance):
    assert isinstance(instance, dsl::ClassOrInterfaceBodyDeclaration)

@given(instance=dsl::EnumConstant_strategy)
@settings(max_examples=50)
def test_dsl::enumconstant_instantiation(instance):
    assert isinstance(instance, dsl::EnumConstant)

@given(instance=dsl::EnumConstant_strategy)
def test_dsl::enumconstant_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dsl::EnumConstant_strategy)
def test_dsl::enumconstant_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl::EnumBody_strategy)
@settings(max_examples=50)
def test_dsl::enumbody_instantiation(instance):
    assert isinstance(instance, dsl::EnumBody)

@given(instance=dsl::ClassOrInterfaceType_strategy)
@settings(max_examples=50)
def test_dsl::classorinterfacetype_instantiation(instance):
    assert isinstance(instance, dsl::ClassOrInterfaceType)

@given(instance=dsl::ClassOrInterfaceType_strategy)
def test_dsl::classorinterfacetype_ids_type(instance):
    assert isinstance(instance.ids, str)


@given(instance=dsl::ClassOrInterfaceType_strategy)
def test_dsl::classorinterfacetype_ids_setter(instance):
    original = instance.ids
    instance.ids = original
    assert instance.ids == original

@given(instance=dsl::ClassOrInterfaceBody_strategy)
@settings(max_examples=50)
def test_dsl::classorinterfacebody_instantiation(instance):
    assert isinstance(instance, dsl::ClassOrInterfaceBody)

@given(instance=dsl::ImplementsList_strategy)
@settings(max_examples=50)
def test_dsl::implementslist_instantiation(instance):
    assert isinstance(instance, dsl::ImplementsList)

@given(instance=dsl::ExtendsList_strategy)
@settings(max_examples=50)
def test_dsl::extendslist_instantiation(instance):
    assert isinstance(instance, dsl::ExtendsList)

@given(instance=dsl::TypeParameters_strategy)
@settings(max_examples=50)
def test_dsl::typeparameters_instantiation(instance):
    assert isinstance(instance, dsl::TypeParameters)

@given(instance=dsl::AnnotationTypeDeclaration_strategy)
@settings(max_examples=50)
def test_dsl::annotationtypedeclaration_instantiation(instance):
    assert isinstance(instance, dsl::AnnotationTypeDeclaration)

@given(instance=dsl::AnnotationTypeDeclaration_strategy)
def test_dsl::annotationtypedeclaration_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dsl::AnnotationTypeDeclaration_strategy)
def test_dsl::annotationtypedeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl::EnumDeclaration_strategy)
@settings(max_examples=50)
def test_dsl::enumdeclaration_instantiation(instance):
    assert isinstance(instance, dsl::EnumDeclaration)

@given(instance=dsl::EnumDeclaration_strategy)
def test_dsl::enumdeclaration_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dsl::EnumDeclaration_strategy)
def test_dsl::enumdeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl::ClassOrInterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_dsl::classorinterfacedeclaration_instantiation(instance):
    assert isinstance(instance, dsl::ClassOrInterfaceDeclaration)

@given(instance=dsl::ClassOrInterfaceDeclaration_strategy)
def test_dsl::classorinterfacedeclaration_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dsl::ClassOrInterfaceDeclaration_strategy)
def test_dsl::classorinterfacedeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dsl::ClassOrInterfaceDeclaration_strategy)
def test_dsl::classorinterfacedeclaration_typeCategory_type(instance):
    assert isinstance(instance.typeCategory, str)


@given(instance=dsl::ClassOrInterfaceDeclaration_strategy)
def test_dsl::classorinterfacedeclaration_typeCategory_setter(instance):
    original = instance.typeCategory
    instance.typeCategory = original
    assert instance.typeCategory == original

@given(instance=dsl::TypeBodyModifier_strategy)
@settings(max_examples=50)
def test_dsl::typebodymodifier_instantiation(instance):
    assert isinstance(instance, dsl::TypeBodyModifier)

@given(instance=dsl::TypeBodyModifier_strategy)
def test_dsl::typebodymodifier_transient_type(instance):
    assert isinstance(instance.transient, bool)


@given(instance=dsl::TypeBodyModifier_strategy)
def test_dsl::typebodymodifier_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original

@given(instance=dsl::TypeBodyModifier_strategy)
def test_dsl::typebodymodifier_volatile_type(instance):
    assert isinstance(instance.volatile, bool)


@given(instance=dsl::TypeBodyModifier_strategy)
def test_dsl::typebodymodifier_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original

@given(instance=dsl::TypeBodyModifier_strategy)
def test_dsl::typebodymodifier_synchronized_type(instance):
    assert isinstance(instance.synchronized, bool)


@given(instance=dsl::TypeBodyModifier_strategy)
def test_dsl::typebodymodifier_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=dsl::TypeBodyModifier_strategy)
def test_dsl::typebodymodifier_strictfp_type(instance):
    assert isinstance(instance.strictfp, bool)


@given(instance=dsl::TypeBodyModifier_strategy)
def test_dsl::typebodymodifier_strictfp_setter(instance):
    original = instance.strictfp
    instance.strictfp = original
    assert instance.strictfp == original

@given(instance=dsl::TypeBodyModifier_strategy)
def test_dsl::typebodymodifier_native_type(instance):
    assert isinstance(instance.native, bool)


@given(instance=dsl::TypeBodyModifier_strategy)
def test_dsl::typebodymodifier_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original

@given(instance=dsl::CommonModifier_strategy)
@settings(max_examples=50)
def test_dsl::commonmodifier_instantiation(instance):
    assert isinstance(instance, dsl::CommonModifier)

@given(instance=dsl::CommonModifier_strategy)
def test_dsl::commonmodifier_final_type(instance):
    assert isinstance(instance.final, bool)


@given(instance=dsl::CommonModifier_strategy)
def test_dsl::commonmodifier_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=dsl::CommonModifier_strategy)
def test_dsl::commonmodifier_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=dsl::CommonModifier_strategy)
def test_dsl::commonmodifier_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=dsl::CommonModifier_strategy)
def test_dsl::commonmodifier_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=dsl::CommonModifier_strategy)
def test_dsl::commonmodifier_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=dsl::CommonModifier_strategy)
def test_dsl::commonmodifier_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=dsl::CommonModifier_strategy)
def test_dsl::commonmodifier_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=dsl::Name_strategy)
@settings(max_examples=50)
def test_dsl::name_instantiation(instance):
    assert isinstance(instance, dsl::Name)

@given(instance=dsl::Name_strategy)
def test_dsl::name_ids_type(instance):
    assert isinstance(instance.ids, str)


@given(instance=dsl::Name_strategy)
def test_dsl::name_ids_setter(instance):
    original = instance.ids
    instance.ids = original
    assert instance.ids == original

@given(instance=dsl::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_dsl::typedeclaration_instantiation(instance):
    assert isinstance(instance, dsl::TypeDeclaration)

@given(instance=dsl::ImportDeclaration_strategy)
@settings(max_examples=50)
def test_dsl::importdeclaration_instantiation(instance):
    assert isinstance(instance, dsl::ImportDeclaration)

@given(instance=dsl::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_dsl::packagedeclaration_instantiation(instance):
    assert isinstance(instance, dsl::PackageDeclaration)

@given(instance=dsl::CompilationUnit_strategy)
@settings(max_examples=50)
def test_dsl::compilationunit_instantiation(instance):
    assert isinstance(instance, dsl::CompilationUnit)

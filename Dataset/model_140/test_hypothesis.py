import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    cSharp::FinallyClause,
    cSharp::CatchClauses,
    cSharp::ThrowStatement,
    cSharp::ReturnStatement,
    cSharp::ResourceAquisition,
    cSharp::UsingStatement,
    cSharp::LockStatement,
    cSharp::StatementExpression,
    cSharp::LocalconstantDeclaration,
    cSharp::EmbeddedStatement,
    cSharp::DeclarationStatment,
    cSharp::LabeledStatement,
    cSharp::Statement,
    cSharp::TryStatement,
    cSharp::JumpStatement,
    cSharp::IterationStatement,
    cSharp::SelectionStatement,
    DelegateDeclaration,
    cSharp::FixedParameter,
    FormalParameterList,
    cSharp::FixedParameters,
    cSharp::MethodHeader,
    cSharp::SetAccessorDeclaration,
    cSharp::GetAccessorDeclaration,
    cSharp::RemoveAccessorDeclaration,
    cSharp::AddAccessorDeclaration,
    cSharp::ParameterArray,
    OperatorDeclarator,
    cSharp::UnaryOperatorDeclarator,
    cSharp::BinaryOperatorDeclarator,
    cSharp::ConversionOperatorDeclarator,
    cSharp::OperatorDeclarator,
    cSharp::IndexerDeclarator,
    cSharp::ConstructorDeclarator,
    cSharp::StaticConstructorDeclaration,
    cSharp::DestructorDeclaration,
    cSharp::ConstructorDeclaration,
    cSharp::OperatorDeclaration,
    cSharp::IndexerDeclaration,
    cSharp::EventDeclaration,
    cSharp::PropertyDeclaration,
    cSharp::ConstantDeclaration,
    cSharp::MethodDeclaration,
    cSharp::FieldDeclaration,
    cSharp::Argument,
    ConstructorInitializer,
    TypeOrVoid,
    cSharp::Void,
    BuiltInClassType,
    cSharp::String,
    cSharp::Object,
    IntegralType,
    cSharp::ULong,
    cSharp::Char,
    cSharp::Short,
    cSharp::Long,
    cSharp::UShort,
    cSharp::Byte,
    cSharp::Int,
    cSharp::UInt,
    cSharp::SByte,
    GetAccessorDeclaration,
    SetAccessorDeclaration,
    cSharp::MaybeEmptyBlock,
    MaybeEmptyBlock,
    AddAccessorDeclaration,
    RemoveAccessorDeclaration,
    cSharp::Block,
    cSharp::ElsePart,
    cSharp::SwitchLabel,
    cSharp::SwitchSection,
    cSharp::SwitchStatement,
    cSharp::IfStatement,
    cSharp::StatementExpressionList,
    cSharp::ForInitializer,
    cSharp::ForeachStatement,
    cSharp::ForStatement,
    cSharp::DoStatement,
    cSharp::WhileStatement,
    cSharp::GotoStatement,
    cSharp::ContinueStatement,
    cSharp::BreakStatement,
    cSharp::GeneralCatchclause,
    cSharp::SpecificCatchClause,
    cSharp::ConstructorInitializer,
    cSharp::InterfaceAccessors,
    cSharp::ClassMemberDeclaration,
    cSharp::ClassBody,
    cSharp::ClassBase,
    cSharp::InterfaceEventDeclaration,
    cSharp::InterfaceMethodDeclaration,
    cSharp::InterfaceMemberDeclaration,
    cSharp::InterfaceBody,
    cSharp::EnumMemberDeclaration,
    cSharp::EnumBody,
    cSharp::DelegateDeclaration,
    cSharp::EnumDeclaration,
    cSharp::InterfaceDeclaration,
    cSharp::FormalParameterList,
    cSharp::InterfacePropertyDeclaration,
    cSharp::InterfaceIndexerDeclaration,
    cSharp::TypeDeclaration,
    cSharp::NamespaceDeclaration,
    cSharp::QualifiedIdentifierList,
    ClassBase,
    ArrayType,
    BuiltInType,
    cSharp::Double,
    cSharp::Decimal,
    cSharp::BuiltInClassType,
    cSharp::Float,
    cSharp::Bool,
    cSharp::IntegralType,
    cSharp::ConstantDeclarator,
    cSharp::AccessorDeclarations,
    cSharp::EventAccessorDeclarations,
    cSharp::ClassDeclaration,
    cSharp::NamespaceBody,
    cSharp::VariableInitializer,
    cSharp::PrimaryExpression2,
    cSharp::TypeOrVoid,
    cSharp::ArgumentList,
    cSharp::VariableDeclarator,
    ConstantDeclaration,
    FieldDeclaration,
    PropertyDeclaration,
    EventDeclaration,
    cSharp::Type,
    cSharp::BuiltInType,
    cSharp::NonArrayType,
    cSharp::PrimaryExpression,
    cSharp::Expression2,
    cSharp::UnaryExpression,
    ResourceAquisition,
    cSharp::LocalVariableDeclaration,
    Argument,
    VariableInitializer,
    cSharp::ArrayInitializer,
    cSharp::Expression,
    cSharp::ExpressionList,
    cSharp::AttributeArguments,
    cSharp::AttributeName,
    cSharp::GlobalAttributeSection,
    cSharp::ArrayType,
    cSharp::QualifiedIdentifier,
    cSharp::Identifier,
    cSharp::NamespaceMemberDeclaration,
    cSharp::GlobalAttributes,
    cSharp::UsingDirective,
    cSharp::CompilationUnit,
    cSharp::Attribute,
    AttributeSection,
    cSharp::AttributeSection,
    cSharp::Attributes,
    cSharp::AttributeList,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_csharp::finallyclause_is_not_abstract():
    assert not inspect.isabstract(cSharp::FinallyClause)


def test_csharp::finallyclause_constructor_exists():
    assert callable(cSharp::FinallyClause.__init__)


def test_csharp::finallyclause_constructor_args():
    sig = inspect.signature(cSharp::FinallyClause.__init__)
    params = list(sig.parameters.keys())



def test_csharp::catchclauses_is_not_abstract():
    assert not inspect.isabstract(cSharp::CatchClauses)


def test_csharp::catchclauses_constructor_exists():
    assert callable(cSharp::CatchClauses.__init__)


def test_csharp::catchclauses_constructor_args():
    sig = inspect.signature(cSharp::CatchClauses.__init__)
    params = list(sig.parameters.keys())



def test_csharp::throwstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::ThrowStatement)


def test_csharp::throwstatement_constructor_exists():
    assert callable(cSharp::ThrowStatement.__init__)


def test_csharp::throwstatement_constructor_args():
    sig = inspect.signature(cSharp::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::returnstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::ReturnStatement)


def test_csharp::returnstatement_constructor_exists():
    assert callable(cSharp::ReturnStatement.__init__)


def test_csharp::returnstatement_constructor_args():
    sig = inspect.signature(cSharp::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::resourceaquisition_is_not_abstract():
    assert not inspect.isabstract(cSharp::ResourceAquisition)


def test_csharp::resourceaquisition_constructor_exists():
    assert callable(cSharp::ResourceAquisition.__init__)


def test_csharp::resourceaquisition_constructor_args():
    sig = inspect.signature(cSharp::ResourceAquisition.__init__)
    params = list(sig.parameters.keys())



def test_csharp::usingstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::UsingStatement)


def test_csharp::usingstatement_constructor_exists():
    assert callable(cSharp::UsingStatement.__init__)


def test_csharp::usingstatement_constructor_args():
    sig = inspect.signature(cSharp::UsingStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::lockstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::LockStatement)


def test_csharp::lockstatement_constructor_exists():
    assert callable(cSharp::LockStatement.__init__)


def test_csharp::lockstatement_constructor_args():
    sig = inspect.signature(cSharp::LockStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::statementexpression_is_not_abstract():
    assert not inspect.isabstract(cSharp::StatementExpression)


def test_csharp::statementexpression_constructor_exists():
    assert callable(cSharp::StatementExpression.__init__)


def test_csharp::statementexpression_constructor_args():
    sig = inspect.signature(cSharp::StatementExpression.__init__)
    params = list(sig.parameters.keys())
    assert "incrimentDecrement" in params, "Missing parameter 'incrimentDecrement'"
    assert "assignementOperator" in params, "Missing parameter 'assignementOperator'"

def test_csharp::statementexpression_has_incrimentDecrement():
    assert hasattr(cSharp::StatementExpression, "incrimentDecrement")
    descriptor = None
    for klass in cSharp::StatementExpression.__mro__:
        if "incrimentDecrement" in klass.__dict__:
            descriptor = klass.__dict__["incrimentDecrement"]
            break
    assert isinstance(descriptor, property)

def test_csharp::statementexpression_has_assignementOperator():
    assert hasattr(cSharp::StatementExpression, "assignementOperator")
    descriptor = None
    for klass in cSharp::StatementExpression.__mro__:
        if "assignementOperator" in klass.__dict__:
            descriptor = klass.__dict__["assignementOperator"]
            break
    assert isinstance(descriptor, property)



def test_csharp::localconstantdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::LocalconstantDeclaration)


def test_csharp::localconstantdeclaration_constructor_exists():
    assert callable(cSharp::LocalconstantDeclaration.__init__)


def test_csharp::localconstantdeclaration_constructor_args():
    sig = inspect.signature(cSharp::LocalconstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::embeddedstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::EmbeddedStatement)


def test_csharp::embeddedstatement_constructor_exists():
    assert callable(cSharp::EmbeddedStatement.__init__)


def test_csharp::embeddedstatement_constructor_args():
    sig = inspect.signature(cSharp::EmbeddedStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::declarationstatment_is_not_abstract():
    assert not inspect.isabstract(cSharp::DeclarationStatment)


def test_csharp::declarationstatment_constructor_exists():
    assert callable(cSharp::DeclarationStatment.__init__)


def test_csharp::declarationstatment_constructor_args():
    sig = inspect.signature(cSharp::DeclarationStatment.__init__)
    params = list(sig.parameters.keys())



def test_csharp::labeledstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::LabeledStatement)


def test_csharp::labeledstatement_constructor_exists():
    assert callable(cSharp::LabeledStatement.__init__)


def test_csharp::labeledstatement_constructor_args():
    sig = inspect.signature(cSharp::LabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::statement_is_not_abstract():
    assert not inspect.isabstract(cSharp::Statement)


def test_csharp::statement_constructor_exists():
    assert callable(cSharp::Statement.__init__)


def test_csharp::statement_constructor_args():
    sig = inspect.signature(cSharp::Statement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::trystatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::TryStatement)


def test_csharp::trystatement_constructor_exists():
    assert callable(cSharp::TryStatement.__init__)


def test_csharp::trystatement_constructor_args():
    sig = inspect.signature(cSharp::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::jumpstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::JumpStatement)


def test_csharp::jumpstatement_constructor_exists():
    assert callable(cSharp::JumpStatement.__init__)


def test_csharp::jumpstatement_constructor_args():
    sig = inspect.signature(cSharp::JumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::iterationstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::IterationStatement)


def test_csharp::iterationstatement_constructor_exists():
    assert callable(cSharp::IterationStatement.__init__)


def test_csharp::iterationstatement_constructor_args():
    sig = inspect.signature(cSharp::IterationStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::selectionstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::SelectionStatement)


def test_csharp::selectionstatement_constructor_exists():
    assert callable(cSharp::SelectionStatement.__init__)


def test_csharp::selectionstatement_constructor_args():
    sig = inspect.signature(cSharp::SelectionStatement.__init__)
    params = list(sig.parameters.keys())



def test_delegatedeclaration_is_not_abstract():
    assert not inspect.isabstract(DelegateDeclaration)


def test_delegatedeclaration_constructor_exists():
    assert callable(DelegateDeclaration.__init__)


def test_delegatedeclaration_constructor_args():
    sig = inspect.signature(DelegateDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::fixedparameter_is_not_abstract():
    assert not inspect.isabstract(cSharp::FixedParameter)


def test_csharp::fixedparameter_constructor_exists():
    assert callable(cSharp::FixedParameter.__init__)


def test_csharp::fixedparameter_constructor_args():
    sig = inspect.signature(cSharp::FixedParameter.__init__)
    params = list(sig.parameters.keys())



def test_formalparameterlist_is_not_abstract():
    assert not inspect.isabstract(FormalParameterList)


def test_formalparameterlist_constructor_exists():
    assert callable(FormalParameterList.__init__)


def test_formalparameterlist_constructor_args():
    sig = inspect.signature(FormalParameterList.__init__)
    params = list(sig.parameters.keys())



def test_csharp::fixedparameters_is_not_abstract():
    assert not inspect.isabstract(cSharp::FixedParameters)


def test_csharp::fixedparameters_constructor_exists():
    assert callable(cSharp::FixedParameters.__init__)


def test_csharp::fixedparameters_constructor_args():
    sig = inspect.signature(cSharp::FixedParameters.__init__)
    params = list(sig.parameters.keys())



def test_csharp::methodheader_is_not_abstract():
    assert not inspect.isabstract(cSharp::MethodHeader)


def test_csharp::methodheader_constructor_exists():
    assert callable(cSharp::MethodHeader.__init__)


def test_csharp::methodheader_constructor_args():
    sig = inspect.signature(cSharp::MethodHeader.__init__)
    params = list(sig.parameters.keys())
    assert "modifier" in params, "Missing parameter 'modifier'"

def test_csharp::methodheader_has_modifier():
    assert hasattr(cSharp::MethodHeader, "modifier")
    descriptor = None
    for klass in cSharp::MethodHeader.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)



def test_csharp::setaccessordeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::SetAccessorDeclaration)


def test_csharp::setaccessordeclaration_constructor_exists():
    assert callable(cSharp::SetAccessorDeclaration.__init__)


def test_csharp::setaccessordeclaration_constructor_args():
    sig = inspect.signature(cSharp::SetAccessorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::getaccessordeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::GetAccessorDeclaration)


def test_csharp::getaccessordeclaration_constructor_exists():
    assert callable(cSharp::GetAccessorDeclaration.__init__)


def test_csharp::getaccessordeclaration_constructor_args():
    sig = inspect.signature(cSharp::GetAccessorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::removeaccessordeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::RemoveAccessorDeclaration)


def test_csharp::removeaccessordeclaration_constructor_exists():
    assert callable(cSharp::RemoveAccessorDeclaration.__init__)


def test_csharp::removeaccessordeclaration_constructor_args():
    sig = inspect.signature(cSharp::RemoveAccessorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::addaccessordeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::AddAccessorDeclaration)


def test_csharp::addaccessordeclaration_constructor_exists():
    assert callable(cSharp::AddAccessorDeclaration.__init__)


def test_csharp::addaccessordeclaration_constructor_args():
    sig = inspect.signature(cSharp::AddAccessorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::parameterarray_is_not_abstract():
    assert not inspect.isabstract(cSharp::ParameterArray)


def test_csharp::parameterarray_constructor_exists():
    assert callable(cSharp::ParameterArray.__init__)


def test_csharp::parameterarray_constructor_args():
    sig = inspect.signature(cSharp::ParameterArray.__init__)
    params = list(sig.parameters.keys())



def test_operatordeclarator_is_not_abstract():
    assert not inspect.isabstract(OperatorDeclarator)


def test_operatordeclarator_constructor_exists():
    assert callable(OperatorDeclarator.__init__)


def test_operatordeclarator_constructor_args():
    sig = inspect.signature(OperatorDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_csharp::unaryoperatordeclarator_is_not_abstract():
    assert not inspect.isabstract(cSharp::UnaryOperatorDeclarator)


def test_csharp::unaryoperatordeclarator_constructor_exists():
    assert callable(cSharp::UnaryOperatorDeclarator.__init__)


def test_csharp::unaryoperatordeclarator_constructor_args():
    sig = inspect.signature(cSharp::UnaryOperatorDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_csharp::binaryoperatordeclarator_is_not_abstract():
    assert not inspect.isabstract(cSharp::BinaryOperatorDeclarator)


def test_csharp::binaryoperatordeclarator_constructor_exists():
    assert callable(cSharp::BinaryOperatorDeclarator.__init__)


def test_csharp::binaryoperatordeclarator_constructor_args():
    sig = inspect.signature(cSharp::BinaryOperatorDeclarator.__init__)
    params = list(sig.parameters.keys())
    assert "overBinOperator" in params, "Missing parameter 'overBinOperator'"

def test_csharp::binaryoperatordeclarator_has_overBinOperator():
    assert hasattr(cSharp::BinaryOperatorDeclarator, "overBinOperator")
    descriptor = None
    for klass in cSharp::BinaryOperatorDeclarator.__mro__:
        if "overBinOperator" in klass.__dict__:
            descriptor = klass.__dict__["overBinOperator"]
            break
    assert isinstance(descriptor, property)



def test_csharp::conversionoperatordeclarator_is_not_abstract():
    assert not inspect.isabstract(cSharp::ConversionOperatorDeclarator)


def test_csharp::conversionoperatordeclarator_constructor_exists():
    assert callable(cSharp::ConversionOperatorDeclarator.__init__)


def test_csharp::conversionoperatordeclarator_constructor_args():
    sig = inspect.signature(cSharp::ConversionOperatorDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_csharp::operatordeclarator_is_not_abstract():
    assert not inspect.isabstract(cSharp::OperatorDeclarator)


def test_csharp::operatordeclarator_constructor_exists():
    assert callable(cSharp::OperatorDeclarator.__init__)


def test_csharp::operatordeclarator_constructor_args():
    sig = inspect.signature(cSharp::OperatorDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_csharp::indexerdeclarator_is_not_abstract():
    assert not inspect.isabstract(cSharp::IndexerDeclarator)


def test_csharp::indexerdeclarator_constructor_exists():
    assert callable(cSharp::IndexerDeclarator.__init__)


def test_csharp::indexerdeclarator_constructor_args():
    sig = inspect.signature(cSharp::IndexerDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_csharp::constructordeclarator_is_not_abstract():
    assert not inspect.isabstract(cSharp::ConstructorDeclarator)


def test_csharp::constructordeclarator_constructor_exists():
    assert callable(cSharp::ConstructorDeclarator.__init__)


def test_csharp::constructordeclarator_constructor_args():
    sig = inspect.signature(cSharp::ConstructorDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_csharp::staticconstructordeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::StaticConstructorDeclaration)


def test_csharp::staticconstructordeclaration_constructor_exists():
    assert callable(cSharp::StaticConstructorDeclaration.__init__)


def test_csharp::staticconstructordeclaration_constructor_args():
    sig = inspect.signature(cSharp::StaticConstructorDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "staticCosntModifier" in params, "Missing parameter 'staticCosntModifier'"

def test_csharp::staticconstructordeclaration_has_staticCosntModifier():
    assert hasattr(cSharp::StaticConstructorDeclaration, "staticCosntModifier")
    descriptor = None
    for klass in cSharp::StaticConstructorDeclaration.__mro__:
        if "staticCosntModifier" in klass.__dict__:
            descriptor = klass.__dict__["staticCosntModifier"]
            break
    assert isinstance(descriptor, property)



def test_csharp::destructordeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::DestructorDeclaration)


def test_csharp::destructordeclaration_constructor_exists():
    assert callable(cSharp::DestructorDeclaration.__init__)


def test_csharp::destructordeclaration_constructor_args():
    sig = inspect.signature(cSharp::DestructorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::constructordeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::ConstructorDeclaration)


def test_csharp::constructordeclaration_constructor_exists():
    assert callable(cSharp::ConstructorDeclaration.__init__)


def test_csharp::constructordeclaration_constructor_args():
    sig = inspect.signature(cSharp::ConstructorDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "constModifier" in params, "Missing parameter 'constModifier'"

def test_csharp::constructordeclaration_has_constModifier():
    assert hasattr(cSharp::ConstructorDeclaration, "constModifier")
    descriptor = None
    for klass in cSharp::ConstructorDeclaration.__mro__:
        if "constModifier" in klass.__dict__:
            descriptor = klass.__dict__["constModifier"]
            break
    assert isinstance(descriptor, property)



def test_csharp::operatordeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::OperatorDeclaration)


def test_csharp::operatordeclaration_constructor_exists():
    assert callable(cSharp::OperatorDeclaration.__init__)


def test_csharp::operatordeclaration_constructor_args():
    sig = inspect.signature(cSharp::OperatorDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "opModifier" in params, "Missing parameter 'opModifier'"

def test_csharp::operatordeclaration_has_opModifier():
    assert hasattr(cSharp::OperatorDeclaration, "opModifier")
    descriptor = None
    for klass in cSharp::OperatorDeclaration.__mro__:
        if "opModifier" in klass.__dict__:
            descriptor = klass.__dict__["opModifier"]
            break
    assert isinstance(descriptor, property)



def test_csharp::indexerdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::IndexerDeclaration)


def test_csharp::indexerdeclaration_constructor_exists():
    assert callable(cSharp::IndexerDeclaration.__init__)


def test_csharp::indexerdeclaration_constructor_args():
    sig = inspect.signature(cSharp::IndexerDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "idModifier" in params, "Missing parameter 'idModifier'"

def test_csharp::indexerdeclaration_has_idModifier():
    assert hasattr(cSharp::IndexerDeclaration, "idModifier")
    descriptor = None
    for klass in cSharp::IndexerDeclaration.__mro__:
        if "idModifier" in klass.__dict__:
            descriptor = klass.__dict__["idModifier"]
            break
    assert isinstance(descriptor, property)



def test_csharp::eventdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::EventDeclaration)


def test_csharp::eventdeclaration_constructor_exists():
    assert callable(cSharp::EventDeclaration.__init__)


def test_csharp::eventdeclaration_constructor_args():
    sig = inspect.signature(cSharp::EventDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::propertydeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::PropertyDeclaration)


def test_csharp::propertydeclaration_constructor_exists():
    assert callable(cSharp::PropertyDeclaration.__init__)


def test_csharp::propertydeclaration_constructor_args():
    sig = inspect.signature(cSharp::PropertyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::ConstantDeclaration)


def test_csharp::constantdeclaration_constructor_exists():
    assert callable(cSharp::ConstantDeclaration.__init__)


def test_csharp::constantdeclaration_constructor_args():
    sig = inspect.signature(cSharp::ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::methoddeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::MethodDeclaration)


def test_csharp::methoddeclaration_constructor_exists():
    assert callable(cSharp::MethodDeclaration.__init__)


def test_csharp::methoddeclaration_constructor_args():
    sig = inspect.signature(cSharp::MethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::FieldDeclaration)


def test_csharp::fielddeclaration_constructor_exists():
    assert callable(cSharp::FieldDeclaration.__init__)


def test_csharp::fielddeclaration_constructor_args():
    sig = inspect.signature(cSharp::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::argument_is_not_abstract():
    assert not inspect.isabstract(cSharp::Argument)


def test_csharp::argument_constructor_exists():
    assert callable(cSharp::Argument.__init__)


def test_csharp::argument_constructor_args():
    sig = inspect.signature(cSharp::Argument.__init__)
    params = list(sig.parameters.keys())



def test_constructorinitializer_is_not_abstract():
    assert not inspect.isabstract(ConstructorInitializer)


def test_constructorinitializer_constructor_exists():
    assert callable(ConstructorInitializer.__init__)


def test_constructorinitializer_constructor_args():
    sig = inspect.signature(ConstructorInitializer.__init__)
    params = list(sig.parameters.keys())



def test_typeorvoid_is_not_abstract():
    assert not inspect.isabstract(TypeOrVoid)


def test_typeorvoid_constructor_exists():
    assert callable(TypeOrVoid.__init__)


def test_typeorvoid_constructor_args():
    sig = inspect.signature(TypeOrVoid.__init__)
    params = list(sig.parameters.keys())



def test_csharp::void_is_not_abstract():
    assert not inspect.isabstract(cSharp::Void)


def test_csharp::void_constructor_exists():
    assert callable(cSharp::Void.__init__)


def test_csharp::void_constructor_args():
    sig = inspect.signature(cSharp::Void.__init__)
    params = list(sig.parameters.keys())



def test_builtinclasstype_is_not_abstract():
    assert not inspect.isabstract(BuiltInClassType)


def test_builtinclasstype_constructor_exists():
    assert callable(BuiltInClassType.__init__)


def test_builtinclasstype_constructor_args():
    sig = inspect.signature(BuiltInClassType.__init__)
    params = list(sig.parameters.keys())



def test_csharp::string_is_not_abstract():
    assert not inspect.isabstract(cSharp::String)


def test_csharp::string_constructor_exists():
    assert callable(cSharp::String.__init__)


def test_csharp::string_constructor_args():
    sig = inspect.signature(cSharp::String.__init__)
    params = list(sig.parameters.keys())



def test_csharp::object_is_not_abstract():
    assert not inspect.isabstract(cSharp::Object)


def test_csharp::object_constructor_exists():
    assert callable(cSharp::Object.__init__)


def test_csharp::object_constructor_args():
    sig = inspect.signature(cSharp::Object.__init__)
    params = list(sig.parameters.keys())



def test_integraltype_is_not_abstract():
    assert not inspect.isabstract(IntegralType)


def test_integraltype_constructor_exists():
    assert callable(IntegralType.__init__)


def test_integraltype_constructor_args():
    sig = inspect.signature(IntegralType.__init__)
    params = list(sig.parameters.keys())



def test_csharp::ulong_is_not_abstract():
    assert not inspect.isabstract(cSharp::ULong)


def test_csharp::ulong_constructor_exists():
    assert callable(cSharp::ULong.__init__)


def test_csharp::ulong_constructor_args():
    sig = inspect.signature(cSharp::ULong.__init__)
    params = list(sig.parameters.keys())



def test_csharp::char_is_not_abstract():
    assert not inspect.isabstract(cSharp::Char)


def test_csharp::char_constructor_exists():
    assert callable(cSharp::Char.__init__)


def test_csharp::char_constructor_args():
    sig = inspect.signature(cSharp::Char.__init__)
    params = list(sig.parameters.keys())



def test_csharp::short_is_not_abstract():
    assert not inspect.isabstract(cSharp::Short)


def test_csharp::short_constructor_exists():
    assert callable(cSharp::Short.__init__)


def test_csharp::short_constructor_args():
    sig = inspect.signature(cSharp::Short.__init__)
    params = list(sig.parameters.keys())



def test_csharp::long_is_not_abstract():
    assert not inspect.isabstract(cSharp::Long)


def test_csharp::long_constructor_exists():
    assert callable(cSharp::Long.__init__)


def test_csharp::long_constructor_args():
    sig = inspect.signature(cSharp::Long.__init__)
    params = list(sig.parameters.keys())



def test_csharp::ushort_is_not_abstract():
    assert not inspect.isabstract(cSharp::UShort)


def test_csharp::ushort_constructor_exists():
    assert callable(cSharp::UShort.__init__)


def test_csharp::ushort_constructor_args():
    sig = inspect.signature(cSharp::UShort.__init__)
    params = list(sig.parameters.keys())



def test_csharp::byte_is_not_abstract():
    assert not inspect.isabstract(cSharp::Byte)


def test_csharp::byte_constructor_exists():
    assert callable(cSharp::Byte.__init__)


def test_csharp::byte_constructor_args():
    sig = inspect.signature(cSharp::Byte.__init__)
    params = list(sig.parameters.keys())



def test_csharp::int_is_not_abstract():
    assert not inspect.isabstract(cSharp::Int)


def test_csharp::int_constructor_exists():
    assert callable(cSharp::Int.__init__)


def test_csharp::int_constructor_args():
    sig = inspect.signature(cSharp::Int.__init__)
    params = list(sig.parameters.keys())



def test_csharp::uint_is_not_abstract():
    assert not inspect.isabstract(cSharp::UInt)


def test_csharp::uint_constructor_exists():
    assert callable(cSharp::UInt.__init__)


def test_csharp::uint_constructor_args():
    sig = inspect.signature(cSharp::UInt.__init__)
    params = list(sig.parameters.keys())



def test_csharp::sbyte_is_not_abstract():
    assert not inspect.isabstract(cSharp::SByte)


def test_csharp::sbyte_constructor_exists():
    assert callable(cSharp::SByte.__init__)


def test_csharp::sbyte_constructor_args():
    sig = inspect.signature(cSharp::SByte.__init__)
    params = list(sig.parameters.keys())



def test_getaccessordeclaration_is_not_abstract():
    assert not inspect.isabstract(GetAccessorDeclaration)


def test_getaccessordeclaration_constructor_exists():
    assert callable(GetAccessorDeclaration.__init__)


def test_getaccessordeclaration_constructor_args():
    sig = inspect.signature(GetAccessorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_setaccessordeclaration_is_not_abstract():
    assert not inspect.isabstract(SetAccessorDeclaration)


def test_setaccessordeclaration_constructor_exists():
    assert callable(SetAccessorDeclaration.__init__)


def test_setaccessordeclaration_constructor_args():
    sig = inspect.signature(SetAccessorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::maybeemptyblock_is_not_abstract():
    assert not inspect.isabstract(cSharp::MaybeEmptyBlock)


def test_csharp::maybeemptyblock_constructor_exists():
    assert callable(cSharp::MaybeEmptyBlock.__init__)


def test_csharp::maybeemptyblock_constructor_args():
    sig = inspect.signature(cSharp::MaybeEmptyBlock.__init__)
    params = list(sig.parameters.keys())



def test_maybeemptyblock_is_not_abstract():
    assert not inspect.isabstract(MaybeEmptyBlock)


def test_maybeemptyblock_constructor_exists():
    assert callable(MaybeEmptyBlock.__init__)


def test_maybeemptyblock_constructor_args():
    sig = inspect.signature(MaybeEmptyBlock.__init__)
    params = list(sig.parameters.keys())



def test_addaccessordeclaration_is_not_abstract():
    assert not inspect.isabstract(AddAccessorDeclaration)


def test_addaccessordeclaration_constructor_exists():
    assert callable(AddAccessorDeclaration.__init__)


def test_addaccessordeclaration_constructor_args():
    sig = inspect.signature(AddAccessorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_removeaccessordeclaration_is_not_abstract():
    assert not inspect.isabstract(RemoveAccessorDeclaration)


def test_removeaccessordeclaration_constructor_exists():
    assert callable(RemoveAccessorDeclaration.__init__)


def test_removeaccessordeclaration_constructor_args():
    sig = inspect.signature(RemoveAccessorDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::block_is_not_abstract():
    assert not inspect.isabstract(cSharp::Block)


def test_csharp::block_constructor_exists():
    assert callable(cSharp::Block.__init__)


def test_csharp::block_constructor_args():
    sig = inspect.signature(cSharp::Block.__init__)
    params = list(sig.parameters.keys())



def test_csharp::elsepart_is_not_abstract():
    assert not inspect.isabstract(cSharp::ElsePart)


def test_csharp::elsepart_constructor_exists():
    assert callable(cSharp::ElsePart.__init__)


def test_csharp::elsepart_constructor_args():
    sig = inspect.signature(cSharp::ElsePart.__init__)
    params = list(sig.parameters.keys())



def test_csharp::switchlabel_is_not_abstract():
    assert not inspect.isabstract(cSharp::SwitchLabel)


def test_csharp::switchlabel_constructor_exists():
    assert callable(cSharp::SwitchLabel.__init__)


def test_csharp::switchlabel_constructor_args():
    sig = inspect.signature(cSharp::SwitchLabel.__init__)
    params = list(sig.parameters.keys())



def test_csharp::switchsection_is_not_abstract():
    assert not inspect.isabstract(cSharp::SwitchSection)


def test_csharp::switchsection_constructor_exists():
    assert callable(cSharp::SwitchSection.__init__)


def test_csharp::switchsection_constructor_args():
    sig = inspect.signature(cSharp::SwitchSection.__init__)
    params = list(sig.parameters.keys())



def test_csharp::switchstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::SwitchStatement)


def test_csharp::switchstatement_constructor_exists():
    assert callable(cSharp::SwitchStatement.__init__)


def test_csharp::switchstatement_constructor_args():
    sig = inspect.signature(cSharp::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::ifstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::IfStatement)


def test_csharp::ifstatement_constructor_exists():
    assert callable(cSharp::IfStatement.__init__)


def test_csharp::ifstatement_constructor_args():
    sig = inspect.signature(cSharp::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::statementexpressionlist_is_not_abstract():
    assert not inspect.isabstract(cSharp::StatementExpressionList)


def test_csharp::statementexpressionlist_constructor_exists():
    assert callable(cSharp::StatementExpressionList.__init__)


def test_csharp::statementexpressionlist_constructor_args():
    sig = inspect.signature(cSharp::StatementExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_csharp::forinitializer_is_not_abstract():
    assert not inspect.isabstract(cSharp::ForInitializer)


def test_csharp::forinitializer_constructor_exists():
    assert callable(cSharp::ForInitializer.__init__)


def test_csharp::forinitializer_constructor_args():
    sig = inspect.signature(cSharp::ForInitializer.__init__)
    params = list(sig.parameters.keys())



def test_csharp::foreachstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::ForeachStatement)


def test_csharp::foreachstatement_constructor_exists():
    assert callable(cSharp::ForeachStatement.__init__)


def test_csharp::foreachstatement_constructor_args():
    sig = inspect.signature(cSharp::ForeachStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::forstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::ForStatement)


def test_csharp::forstatement_constructor_exists():
    assert callable(cSharp::ForStatement.__init__)


def test_csharp::forstatement_constructor_args():
    sig = inspect.signature(cSharp::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::dostatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::DoStatement)


def test_csharp::dostatement_constructor_exists():
    assert callable(cSharp::DoStatement.__init__)


def test_csharp::dostatement_constructor_args():
    sig = inspect.signature(cSharp::DoStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::whilestatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::WhileStatement)


def test_csharp::whilestatement_constructor_exists():
    assert callable(cSharp::WhileStatement.__init__)


def test_csharp::whilestatement_constructor_args():
    sig = inspect.signature(cSharp::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::gotostatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::GotoStatement)


def test_csharp::gotostatement_constructor_exists():
    assert callable(cSharp::GotoStatement.__init__)


def test_csharp::gotostatement_constructor_args():
    sig = inspect.signature(cSharp::GotoStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::continuestatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::ContinueStatement)


def test_csharp::continuestatement_constructor_exists():
    assert callable(cSharp::ContinueStatement.__init__)


def test_csharp::continuestatement_constructor_args():
    sig = inspect.signature(cSharp::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::breakstatement_is_not_abstract():
    assert not inspect.isabstract(cSharp::BreakStatement)


def test_csharp::breakstatement_constructor_exists():
    assert callable(cSharp::BreakStatement.__init__)


def test_csharp::breakstatement_constructor_args():
    sig = inspect.signature(cSharp::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_csharp::generalcatchclause_is_not_abstract():
    assert not inspect.isabstract(cSharp::GeneralCatchclause)


def test_csharp::generalcatchclause_constructor_exists():
    assert callable(cSharp::GeneralCatchclause.__init__)


def test_csharp::generalcatchclause_constructor_args():
    sig = inspect.signature(cSharp::GeneralCatchclause.__init__)
    params = list(sig.parameters.keys())



def test_csharp::specificcatchclause_is_not_abstract():
    assert not inspect.isabstract(cSharp::SpecificCatchClause)


def test_csharp::specificcatchclause_constructor_exists():
    assert callable(cSharp::SpecificCatchClause.__init__)


def test_csharp::specificcatchclause_constructor_args():
    sig = inspect.signature(cSharp::SpecificCatchClause.__init__)
    params = list(sig.parameters.keys())



def test_csharp::constructorinitializer_is_not_abstract():
    assert not inspect.isabstract(cSharp::ConstructorInitializer)


def test_csharp::constructorinitializer_constructor_exists():
    assert callable(cSharp::ConstructorInitializer.__init__)


def test_csharp::constructorinitializer_constructor_args():
    sig = inspect.signature(cSharp::ConstructorInitializer.__init__)
    params = list(sig.parameters.keys())



def test_csharp::interfaceaccessors_is_not_abstract():
    assert not inspect.isabstract(cSharp::InterfaceAccessors)


def test_csharp::interfaceaccessors_constructor_exists():
    assert callable(cSharp::InterfaceAccessors.__init__)


def test_csharp::interfaceaccessors_constructor_args():
    sig = inspect.signature(cSharp::InterfaceAccessors.__init__)
    params = list(sig.parameters.keys())



def test_csharp::classmemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::ClassMemberDeclaration)


def test_csharp::classmemberdeclaration_constructor_exists():
    assert callable(cSharp::ClassMemberDeclaration.__init__)


def test_csharp::classmemberdeclaration_constructor_args():
    sig = inspect.signature(cSharp::ClassMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::classbody_is_not_abstract():
    assert not inspect.isabstract(cSharp::ClassBody)


def test_csharp::classbody_constructor_exists():
    assert callable(cSharp::ClassBody.__init__)


def test_csharp::classbody_constructor_args():
    sig = inspect.signature(cSharp::ClassBody.__init__)
    params = list(sig.parameters.keys())



def test_csharp::classbase_is_not_abstract():
    assert not inspect.isabstract(cSharp::ClassBase)


def test_csharp::classbase_constructor_exists():
    assert callable(cSharp::ClassBase.__init__)


def test_csharp::classbase_constructor_args():
    sig = inspect.signature(cSharp::ClassBase.__init__)
    params = list(sig.parameters.keys())



def test_csharp::interfaceeventdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::InterfaceEventDeclaration)


def test_csharp::interfaceeventdeclaration_constructor_exists():
    assert callable(cSharp::InterfaceEventDeclaration.__init__)


def test_csharp::interfaceeventdeclaration_constructor_args():
    sig = inspect.signature(cSharp::InterfaceEventDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::interfacemethoddeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::InterfaceMethodDeclaration)


def test_csharp::interfacemethoddeclaration_constructor_exists():
    assert callable(cSharp::InterfaceMethodDeclaration.__init__)


def test_csharp::interfacemethoddeclaration_constructor_args():
    sig = inspect.signature(cSharp::InterfaceMethodDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::interfacememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::InterfaceMemberDeclaration)


def test_csharp::interfacememberdeclaration_constructor_exists():
    assert callable(cSharp::InterfaceMemberDeclaration.__init__)


def test_csharp::interfacememberdeclaration_constructor_args():
    sig = inspect.signature(cSharp::InterfaceMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::interfacebody_is_not_abstract():
    assert not inspect.isabstract(cSharp::InterfaceBody)


def test_csharp::interfacebody_constructor_exists():
    assert callable(cSharp::InterfaceBody.__init__)


def test_csharp::interfacebody_constructor_args():
    sig = inspect.signature(cSharp::InterfaceBody.__init__)
    params = list(sig.parameters.keys())



def test_csharp::enummemberdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::EnumMemberDeclaration)


def test_csharp::enummemberdeclaration_constructor_exists():
    assert callable(cSharp::EnumMemberDeclaration.__init__)


def test_csharp::enummemberdeclaration_constructor_args():
    sig = inspect.signature(cSharp::EnumMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::enumbody_is_not_abstract():
    assert not inspect.isabstract(cSharp::EnumBody)


def test_csharp::enumbody_constructor_exists():
    assert callable(cSharp::EnumBody.__init__)


def test_csharp::enumbody_constructor_args():
    sig = inspect.signature(cSharp::EnumBody.__init__)
    params = list(sig.parameters.keys())



def test_csharp::delegatedeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::DelegateDeclaration)


def test_csharp::delegatedeclaration_constructor_exists():
    assert callable(cSharp::DelegateDeclaration.__init__)


def test_csharp::delegatedeclaration_constructor_args():
    sig = inspect.signature(cSharp::DelegateDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::enumdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::EnumDeclaration)


def test_csharp::enumdeclaration_constructor_exists():
    assert callable(cSharp::EnumDeclaration.__init__)


def test_csharp::enumdeclaration_constructor_args():
    sig = inspect.signature(cSharp::EnumDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::InterfaceDeclaration)


def test_csharp::interfacedeclaration_constructor_exists():
    assert callable(cSharp::InterfaceDeclaration.__init__)


def test_csharp::interfacedeclaration_constructor_args():
    sig = inspect.signature(cSharp::InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::formalparameterlist_is_not_abstract():
    assert not inspect.isabstract(cSharp::FormalParameterList)


def test_csharp::formalparameterlist_constructor_exists():
    assert callable(cSharp::FormalParameterList.__init__)


def test_csharp::formalparameterlist_constructor_args():
    sig = inspect.signature(cSharp::FormalParameterList.__init__)
    params = list(sig.parameters.keys())



def test_csharp::interfacepropertydeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::InterfacePropertyDeclaration)


def test_csharp::interfacepropertydeclaration_constructor_exists():
    assert callable(cSharp::InterfacePropertyDeclaration.__init__)


def test_csharp::interfacepropertydeclaration_constructor_args():
    sig = inspect.signature(cSharp::InterfacePropertyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::interfaceindexerdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::InterfaceIndexerDeclaration)


def test_csharp::interfaceindexerdeclaration_constructor_exists():
    assert callable(cSharp::InterfaceIndexerDeclaration.__init__)


def test_csharp::interfaceindexerdeclaration_constructor_args():
    sig = inspect.signature(cSharp::InterfaceIndexerDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::TypeDeclaration)


def test_csharp::typedeclaration_constructor_exists():
    assert callable(cSharp::TypeDeclaration.__init__)


def test_csharp::typedeclaration_constructor_args():
    sig = inspect.signature(cSharp::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::namespacedeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::NamespaceDeclaration)


def test_csharp::namespacedeclaration_constructor_exists():
    assert callable(cSharp::NamespaceDeclaration.__init__)


def test_csharp::namespacedeclaration_constructor_args():
    sig = inspect.signature(cSharp::NamespaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::qualifiedidentifierlist_is_not_abstract():
    assert not inspect.isabstract(cSharp::QualifiedIdentifierList)


def test_csharp::qualifiedidentifierlist_constructor_exists():
    assert callable(cSharp::QualifiedIdentifierList.__init__)


def test_csharp::qualifiedidentifierlist_constructor_args():
    sig = inspect.signature(cSharp::QualifiedIdentifierList.__init__)
    params = list(sig.parameters.keys())



def test_classbase_is_not_abstract():
    assert not inspect.isabstract(ClassBase)


def test_classbase_constructor_exists():
    assert callable(ClassBase.__init__)


def test_classbase_constructor_args():
    sig = inspect.signature(ClassBase.__init__)
    params = list(sig.parameters.keys())



def test_arraytype_is_not_abstract():
    assert not inspect.isabstract(ArrayType)


def test_arraytype_constructor_exists():
    assert callable(ArrayType.__init__)


def test_arraytype_constructor_args():
    sig = inspect.signature(ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_builtintype_is_not_abstract():
    assert not inspect.isabstract(BuiltInType)


def test_builtintype_constructor_exists():
    assert callable(BuiltInType.__init__)


def test_builtintype_constructor_args():
    sig = inspect.signature(BuiltInType.__init__)
    params = list(sig.parameters.keys())



def test_csharp::double_is_not_abstract():
    assert not inspect.isabstract(cSharp::Double)


def test_csharp::double_constructor_exists():
    assert callable(cSharp::Double.__init__)


def test_csharp::double_constructor_args():
    sig = inspect.signature(cSharp::Double.__init__)
    params = list(sig.parameters.keys())



def test_csharp::decimal_is_not_abstract():
    assert not inspect.isabstract(cSharp::Decimal)


def test_csharp::decimal_constructor_exists():
    assert callable(cSharp::Decimal.__init__)


def test_csharp::decimal_constructor_args():
    sig = inspect.signature(cSharp::Decimal.__init__)
    params = list(sig.parameters.keys())



def test_csharp::builtinclasstype_is_not_abstract():
    assert not inspect.isabstract(cSharp::BuiltInClassType)


def test_csharp::builtinclasstype_constructor_exists():
    assert callable(cSharp::BuiltInClassType.__init__)


def test_csharp::builtinclasstype_constructor_args():
    sig = inspect.signature(cSharp::BuiltInClassType.__init__)
    params = list(sig.parameters.keys())



def test_csharp::float_is_not_abstract():
    assert not inspect.isabstract(cSharp::Float)


def test_csharp::float_constructor_exists():
    assert callable(cSharp::Float.__init__)


def test_csharp::float_constructor_args():
    sig = inspect.signature(cSharp::Float.__init__)
    params = list(sig.parameters.keys())



def test_csharp::bool_is_not_abstract():
    assert not inspect.isabstract(cSharp::Bool)


def test_csharp::bool_constructor_exists():
    assert callable(cSharp::Bool.__init__)


def test_csharp::bool_constructor_args():
    sig = inspect.signature(cSharp::Bool.__init__)
    params = list(sig.parameters.keys())



def test_csharp::integraltype_is_not_abstract():
    assert not inspect.isabstract(cSharp::IntegralType)


def test_csharp::integraltype_constructor_exists():
    assert callable(cSharp::IntegralType.__init__)


def test_csharp::integraltype_constructor_args():
    sig = inspect.signature(cSharp::IntegralType.__init__)
    params = list(sig.parameters.keys())



def test_csharp::constantdeclarator_is_not_abstract():
    assert not inspect.isabstract(cSharp::ConstantDeclarator)


def test_csharp::constantdeclarator_constructor_exists():
    assert callable(cSharp::ConstantDeclarator.__init__)


def test_csharp::constantdeclarator_constructor_args():
    sig = inspect.signature(cSharp::ConstantDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_csharp::accessordeclarations_is_not_abstract():
    assert not inspect.isabstract(cSharp::AccessorDeclarations)


def test_csharp::accessordeclarations_constructor_exists():
    assert callable(cSharp::AccessorDeclarations.__init__)


def test_csharp::accessordeclarations_constructor_args():
    sig = inspect.signature(cSharp::AccessorDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_csharp::eventaccessordeclarations_is_not_abstract():
    assert not inspect.isabstract(cSharp::EventAccessorDeclarations)


def test_csharp::eventaccessordeclarations_constructor_exists():
    assert callable(cSharp::EventAccessorDeclarations.__init__)


def test_csharp::eventaccessordeclarations_constructor_args():
    sig = inspect.signature(cSharp::EventAccessorDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_csharp::classdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::ClassDeclaration)


def test_csharp::classdeclaration_constructor_exists():
    assert callable(cSharp::ClassDeclaration.__init__)


def test_csharp::classdeclaration_constructor_args():
    sig = inspect.signature(cSharp::ClassDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "classModifier" in params, "Missing parameter 'classModifier'"

def test_csharp::classdeclaration_has_classModifier():
    assert hasattr(cSharp::ClassDeclaration, "classModifier")
    descriptor = None
    for klass in cSharp::ClassDeclaration.__mro__:
        if "classModifier" in klass.__dict__:
            descriptor = klass.__dict__["classModifier"]
            break
    assert isinstance(descriptor, property)



def test_csharp::namespacebody_is_not_abstract():
    assert not inspect.isabstract(cSharp::NamespaceBody)


def test_csharp::namespacebody_constructor_exists():
    assert callable(cSharp::NamespaceBody.__init__)


def test_csharp::namespacebody_constructor_args():
    sig = inspect.signature(cSharp::NamespaceBody.__init__)
    params = list(sig.parameters.keys())



def test_csharp::variableinitializer_is_not_abstract():
    assert not inspect.isabstract(cSharp::VariableInitializer)


def test_csharp::variableinitializer_constructor_exists():
    assert callable(cSharp::VariableInitializer.__init__)


def test_csharp::variableinitializer_constructor_args():
    sig = inspect.signature(cSharp::VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_csharp::primaryexpression2_is_not_abstract():
    assert not inspect.isabstract(cSharp::PrimaryExpression2)


def test_csharp::primaryexpression2_constructor_exists():
    assert callable(cSharp::PrimaryExpression2.__init__)


def test_csharp::primaryexpression2_constructor_args():
    sig = inspect.signature(cSharp::PrimaryExpression2.__init__)
    params = list(sig.parameters.keys())
    assert "incrementeDecrement" in params, "Missing parameter 'incrementeDecrement'"

def test_csharp::primaryexpression2_has_incrementeDecrement():
    assert hasattr(cSharp::PrimaryExpression2, "incrementeDecrement")
    descriptor = None
    for klass in cSharp::PrimaryExpression2.__mro__:
        if "incrementeDecrement" in klass.__dict__:
            descriptor = klass.__dict__["incrementeDecrement"]
            break
    assert isinstance(descriptor, property)



def test_csharp::typeorvoid_is_not_abstract():
    assert not inspect.isabstract(cSharp::TypeOrVoid)


def test_csharp::typeorvoid_constructor_exists():
    assert callable(cSharp::TypeOrVoid.__init__)


def test_csharp::typeorvoid_constructor_args():
    sig = inspect.signature(cSharp::TypeOrVoid.__init__)
    params = list(sig.parameters.keys())



def test_csharp::argumentlist_is_not_abstract():
    assert not inspect.isabstract(cSharp::ArgumentList)


def test_csharp::argumentlist_constructor_exists():
    assert callable(cSharp::ArgumentList.__init__)


def test_csharp::argumentlist_constructor_args():
    sig = inspect.signature(cSharp::ArgumentList.__init__)
    params = list(sig.parameters.keys())



def test_csharp::variabledeclarator_is_not_abstract():
    assert not inspect.isabstract(cSharp::VariableDeclarator)


def test_csharp::variabledeclarator_constructor_exists():
    assert callable(cSharp::VariableDeclarator.__init__)


def test_csharp::variabledeclarator_constructor_args():
    sig = inspect.signature(cSharp::VariableDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(ConstantDeclaration)


def test_constantdeclaration_constructor_exists():
    assert callable(ConstantDeclaration.__init__)


def test_constantdeclaration_constructor_args():
    sig = inspect.signature(ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(FieldDeclaration)


def test_fielddeclaration_constructor_exists():
    assert callable(FieldDeclaration.__init__)


def test_fielddeclaration_constructor_args():
    sig = inspect.signature(FieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_propertydeclaration_is_not_abstract():
    assert not inspect.isabstract(PropertyDeclaration)


def test_propertydeclaration_constructor_exists():
    assert callable(PropertyDeclaration.__init__)


def test_propertydeclaration_constructor_args():
    sig = inspect.signature(PropertyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_eventdeclaration_is_not_abstract():
    assert not inspect.isabstract(EventDeclaration)


def test_eventdeclaration_constructor_exists():
    assert callable(EventDeclaration.__init__)


def test_eventdeclaration_constructor_args():
    sig = inspect.signature(EventDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::type_is_not_abstract():
    assert not inspect.isabstract(cSharp::Type)


def test_csharp::type_constructor_exists():
    assert callable(cSharp::Type.__init__)


def test_csharp::type_constructor_args():
    sig = inspect.signature(cSharp::Type.__init__)
    params = list(sig.parameters.keys())



def test_csharp::builtintype_is_not_abstract():
    assert not inspect.isabstract(cSharp::BuiltInType)


def test_csharp::builtintype_constructor_exists():
    assert callable(cSharp::BuiltInType.__init__)


def test_csharp::builtintype_constructor_args():
    sig = inspect.signature(cSharp::BuiltInType.__init__)
    params = list(sig.parameters.keys())



def test_csharp::nonarraytype_is_not_abstract():
    assert not inspect.isabstract(cSharp::NonArrayType)


def test_csharp::nonarraytype_constructor_exists():
    assert callable(cSharp::NonArrayType.__init__)


def test_csharp::nonarraytype_constructor_args():
    sig = inspect.signature(cSharp::NonArrayType.__init__)
    params = list(sig.parameters.keys())



def test_csharp::primaryexpression_is_not_abstract():
    assert not inspect.isabstract(cSharp::PrimaryExpression)


def test_csharp::primaryexpression_constructor_exists():
    assert callable(cSharp::PrimaryExpression.__init__)


def test_csharp::primaryexpression_constructor_args():
    sig = inspect.signature(cSharp::PrimaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "rankSpecifier" in params, "Missing parameter 'rankSpecifier'"
    assert "predefinedType" in params, "Missing parameter 'predefinedType'"
    assert "literal" in params, "Missing parameter 'literal'"

def test_csharp::primaryexpression_has_rankSpecifier():
    assert hasattr(cSharp::PrimaryExpression, "rankSpecifier")
    descriptor = None
    for klass in cSharp::PrimaryExpression.__mro__:
        if "rankSpecifier" in klass.__dict__:
            descriptor = klass.__dict__["rankSpecifier"]
            break
    assert isinstance(descriptor, property)

def test_csharp::primaryexpression_has_predefinedType():
    assert hasattr(cSharp::PrimaryExpression, "predefinedType")
    descriptor = None
    for klass in cSharp::PrimaryExpression.__mro__:
        if "predefinedType" in klass.__dict__:
            descriptor = klass.__dict__["predefinedType"]
            break
    assert isinstance(descriptor, property)

def test_csharp::primaryexpression_has_literal():
    assert hasattr(cSharp::PrimaryExpression, "literal")
    descriptor = None
    for klass in cSharp::PrimaryExpression.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_csharp::expression2_is_not_abstract():
    assert not inspect.isabstract(cSharp::Expression2)


def test_csharp::expression2_constructor_exists():
    assert callable(cSharp::Expression2.__init__)


def test_csharp::expression2_constructor_args():
    sig = inspect.signature(cSharp::Expression2.__init__)
    params = list(sig.parameters.keys())



def test_csharp::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(cSharp::UnaryExpression)


def test_csharp::unaryexpression_constructor_exists():
    assert callable(cSharp::UnaryExpression.__init__)


def test_csharp::unaryexpression_constructor_args():
    sig = inspect.signature(cSharp::UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expUnaryOperator" in params, "Missing parameter 'expUnaryOperator'"

def test_csharp::unaryexpression_has_expUnaryOperator():
    assert hasattr(cSharp::UnaryExpression, "expUnaryOperator")
    descriptor = None
    for klass in cSharp::UnaryExpression.__mro__:
        if "expUnaryOperator" in klass.__dict__:
            descriptor = klass.__dict__["expUnaryOperator"]
            break
    assert isinstance(descriptor, property)



def test_resourceaquisition_is_not_abstract():
    assert not inspect.isabstract(ResourceAquisition)


def test_resourceaquisition_constructor_exists():
    assert callable(ResourceAquisition.__init__)


def test_resourceaquisition_constructor_args():
    sig = inspect.signature(ResourceAquisition.__init__)
    params = list(sig.parameters.keys())



def test_csharp::localvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::LocalVariableDeclaration)


def test_csharp::localvariabledeclaration_constructor_exists():
    assert callable(cSharp::LocalVariableDeclaration.__init__)


def test_csharp::localvariabledeclaration_constructor_args():
    sig = inspect.signature(cSharp::LocalVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_argument_is_not_abstract():
    assert not inspect.isabstract(Argument)


def test_argument_constructor_exists():
    assert callable(Argument.__init__)


def test_argument_constructor_args():
    sig = inspect.signature(Argument.__init__)
    params = list(sig.parameters.keys())



def test_variableinitializer_is_not_abstract():
    assert not inspect.isabstract(VariableInitializer)


def test_variableinitializer_constructor_exists():
    assert callable(VariableInitializer.__init__)


def test_variableinitializer_constructor_args():
    sig = inspect.signature(VariableInitializer.__init__)
    params = list(sig.parameters.keys())



def test_csharp::arrayinitializer_is_not_abstract():
    assert not inspect.isabstract(cSharp::ArrayInitializer)


def test_csharp::arrayinitializer_constructor_exists():
    assert callable(cSharp::ArrayInitializer.__init__)


def test_csharp::arrayinitializer_constructor_args():
    sig = inspect.signature(cSharp::ArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_csharp::expression_is_not_abstract():
    assert not inspect.isabstract(cSharp::Expression)


def test_csharp::expression_constructor_exists():
    assert callable(cSharp::Expression.__init__)


def test_csharp::expression_constructor_args():
    sig = inspect.signature(cSharp::Expression.__init__)
    params = list(sig.parameters.keys())



def test_csharp::expressionlist_is_not_abstract():
    assert not inspect.isabstract(cSharp::ExpressionList)


def test_csharp::expressionlist_constructor_exists():
    assert callable(cSharp::ExpressionList.__init__)


def test_csharp::expressionlist_constructor_args():
    sig = inspect.signature(cSharp::ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_csharp::attributearguments_is_not_abstract():
    assert not inspect.isabstract(cSharp::AttributeArguments)


def test_csharp::attributearguments_constructor_exists():
    assert callable(cSharp::AttributeArguments.__init__)


def test_csharp::attributearguments_constructor_args():
    sig = inspect.signature(cSharp::AttributeArguments.__init__)
    params = list(sig.parameters.keys())



def test_csharp::attributename_is_not_abstract():
    assert not inspect.isabstract(cSharp::AttributeName)


def test_csharp::attributename_constructor_exists():
    assert callable(cSharp::AttributeName.__init__)


def test_csharp::attributename_constructor_args():
    sig = inspect.signature(cSharp::AttributeName.__init__)
    params = list(sig.parameters.keys())



def test_csharp::globalattributesection_is_not_abstract():
    assert not inspect.isabstract(cSharp::GlobalAttributeSection)


def test_csharp::globalattributesection_constructor_exists():
    assert callable(cSharp::GlobalAttributeSection.__init__)


def test_csharp::globalattributesection_constructor_args():
    sig = inspect.signature(cSharp::GlobalAttributeSection.__init__)
    params = list(sig.parameters.keys())



def test_csharp::arraytype_is_not_abstract():
    assert not inspect.isabstract(cSharp::ArrayType)


def test_csharp::arraytype_constructor_exists():
    assert callable(cSharp::ArrayType.__init__)


def test_csharp::arraytype_constructor_args():
    sig = inspect.signature(cSharp::ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_csharp::qualifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(cSharp::QualifiedIdentifier)


def test_csharp::qualifiedidentifier_constructor_exists():
    assert callable(cSharp::QualifiedIdentifier.__init__)


def test_csharp::qualifiedidentifier_constructor_args():
    sig = inspect.signature(cSharp::QualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_csharp::identifier_is_not_abstract():
    assert not inspect.isabstract(cSharp::Identifier)


def test_csharp::identifier_constructor_exists():
    assert callable(cSharp::Identifier.__init__)


def test_csharp::identifier_constructor_args():
    sig = inspect.signature(cSharp::Identifier.__init__)
    params = list(sig.parameters.keys())



def test_csharp::namespacememberdeclaration_is_not_abstract():
    assert not inspect.isabstract(cSharp::NamespaceMemberDeclaration)


def test_csharp::namespacememberdeclaration_constructor_exists():
    assert callable(cSharp::NamespaceMemberDeclaration.__init__)


def test_csharp::namespacememberdeclaration_constructor_args():
    sig = inspect.signature(cSharp::NamespaceMemberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_csharp::globalattributes_is_not_abstract():
    assert not inspect.isabstract(cSharp::GlobalAttributes)


def test_csharp::globalattributes_constructor_exists():
    assert callable(cSharp::GlobalAttributes.__init__)


def test_csharp::globalattributes_constructor_args():
    sig = inspect.signature(cSharp::GlobalAttributes.__init__)
    params = list(sig.parameters.keys())



def test_csharp::usingdirective_is_not_abstract():
    assert not inspect.isabstract(cSharp::UsingDirective)


def test_csharp::usingdirective_constructor_exists():
    assert callable(cSharp::UsingDirective.__init__)


def test_csharp::usingdirective_constructor_args():
    sig = inspect.signature(cSharp::UsingDirective.__init__)
    params = list(sig.parameters.keys())



def test_csharp::compilationunit_is_not_abstract():
    assert not inspect.isabstract(cSharp::CompilationUnit)


def test_csharp::compilationunit_constructor_exists():
    assert callable(cSharp::CompilationUnit.__init__)


def test_csharp::compilationunit_constructor_args():
    sig = inspect.signature(cSharp::CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_csharp::attribute_is_not_abstract():
    assert not inspect.isabstract(cSharp::Attribute)


def test_csharp::attribute_constructor_exists():
    assert callable(cSharp::Attribute.__init__)


def test_csharp::attribute_constructor_args():
    sig = inspect.signature(cSharp::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_attributesection_is_not_abstract():
    assert not inspect.isabstract(AttributeSection)


def test_attributesection_constructor_exists():
    assert callable(AttributeSection.__init__)


def test_attributesection_constructor_args():
    sig = inspect.signature(AttributeSection.__init__)
    params = list(sig.parameters.keys())



def test_csharp::attributesection_is_not_abstract():
    assert not inspect.isabstract(cSharp::AttributeSection)


def test_csharp::attributesection_constructor_exists():
    assert callable(cSharp::AttributeSection.__init__)


def test_csharp::attributesection_constructor_args():
    sig = inspect.signature(cSharp::AttributeSection.__init__)
    params = list(sig.parameters.keys())



def test_csharp::attributes_is_not_abstract():
    assert not inspect.isabstract(cSharp::Attributes)


def test_csharp::attributes_constructor_exists():
    assert callable(cSharp::Attributes.__init__)


def test_csharp::attributes_constructor_args():
    sig = inspect.signature(cSharp::Attributes.__init__)
    params = list(sig.parameters.keys())



def test_csharp::attributelist_is_not_abstract():
    assert not inspect.isabstract(cSharp::AttributeList)


def test_csharp::attributelist_constructor_exists():
    assert callable(cSharp::AttributeList.__init__)


def test_csharp::attributelist_constructor_args():
    sig = inspect.signature(cSharp::AttributeList.__init__)
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
cSharp::FinallyClause_strategy = st.builds(
    cSharp::FinallyClause,
)
cSharp::CatchClauses_strategy = st.builds(
    cSharp::CatchClauses,
)
cSharp::ThrowStatement_strategy = st.builds(
    cSharp::ThrowStatement,
)
cSharp::ReturnStatement_strategy = st.builds(
    cSharp::ReturnStatement,
)
cSharp::ResourceAquisition_strategy = st.builds(
    cSharp::ResourceAquisition,
)
cSharp::UsingStatement_strategy = st.builds(
    cSharp::UsingStatement,
)
cSharp::LockStatement_strategy = st.builds(
    cSharp::LockStatement,
)
cSharp::StatementExpression_strategy = st.builds(
    cSharp::StatementExpression,
    incrimentDecrement=
        safe_text,
    assignementOperator=
        safe_text
)
cSharp::LocalconstantDeclaration_strategy = st.builds(
    cSharp::LocalconstantDeclaration,
)
cSharp::EmbeddedStatement_strategy = st.builds(
    cSharp::EmbeddedStatement,
)
cSharp::DeclarationStatment_strategy = st.builds(
    cSharp::DeclarationStatment,
)
cSharp::LabeledStatement_strategy = st.builds(
    cSharp::LabeledStatement,
)
cSharp::Statement_strategy = st.builds(
    cSharp::Statement,
)
cSharp::TryStatement_strategy = st.builds(
    cSharp::TryStatement,
)
cSharp::JumpStatement_strategy = st.builds(
    cSharp::JumpStatement,
)
cSharp::IterationStatement_strategy = st.builds(
    cSharp::IterationStatement,
)
cSharp::SelectionStatement_strategy = st.builds(
    cSharp::SelectionStatement,
)
DelegateDeclaration_strategy = st.builds(
    DelegateDeclaration,
)
cSharp::FixedParameter_strategy = st.builds(
    cSharp::FixedParameter,
)
FormalParameterList_strategy = st.builds(
    FormalParameterList,
)
cSharp::FixedParameters_strategy = st.builds(
    cSharp::FixedParameters,
)
cSharp::MethodHeader_strategy = st.builds(
    cSharp::MethodHeader,
    modifier=
        safe_text
)
cSharp::SetAccessorDeclaration_strategy = st.builds(
    cSharp::SetAccessorDeclaration,
)
cSharp::GetAccessorDeclaration_strategy = st.builds(
    cSharp::GetAccessorDeclaration,
)
cSharp::RemoveAccessorDeclaration_strategy = st.builds(
    cSharp::RemoveAccessorDeclaration,
)
cSharp::AddAccessorDeclaration_strategy = st.builds(
    cSharp::AddAccessorDeclaration,
)
cSharp::ParameterArray_strategy = st.builds(
    cSharp::ParameterArray,
)
OperatorDeclarator_strategy = st.builds(
    OperatorDeclarator,
)
cSharp::UnaryOperatorDeclarator_strategy = st.builds(
    cSharp::UnaryOperatorDeclarator,
)
cSharp::BinaryOperatorDeclarator_strategy = st.builds(
    cSharp::BinaryOperatorDeclarator,
    overBinOperator=
        safe_text
)
cSharp::ConversionOperatorDeclarator_strategy = st.builds(
    cSharp::ConversionOperatorDeclarator,
)
cSharp::OperatorDeclarator_strategy = st.builds(
    cSharp::OperatorDeclarator,
)
cSharp::IndexerDeclarator_strategy = st.builds(
    cSharp::IndexerDeclarator,
)
cSharp::ConstructorDeclarator_strategy = st.builds(
    cSharp::ConstructorDeclarator,
)
cSharp::StaticConstructorDeclaration_strategy = st.builds(
    cSharp::StaticConstructorDeclaration,
    staticCosntModifier=
        safe_text
)
cSharp::DestructorDeclaration_strategy = st.builds(
    cSharp::DestructorDeclaration,
)
cSharp::ConstructorDeclaration_strategy = st.builds(
    cSharp::ConstructorDeclaration,
    constModifier=
        safe_text
)
cSharp::OperatorDeclaration_strategy = st.builds(
    cSharp::OperatorDeclaration,
    opModifier=
        safe_text
)
cSharp::IndexerDeclaration_strategy = st.builds(
    cSharp::IndexerDeclaration,
    idModifier=
        safe_text
)
cSharp::EventDeclaration_strategy = st.builds(
    cSharp::EventDeclaration,
)
cSharp::PropertyDeclaration_strategy = st.builds(
    cSharp::PropertyDeclaration,
)
cSharp::ConstantDeclaration_strategy = st.builds(
    cSharp::ConstantDeclaration,
)
cSharp::MethodDeclaration_strategy = st.builds(
    cSharp::MethodDeclaration,
)
cSharp::FieldDeclaration_strategy = st.builds(
    cSharp::FieldDeclaration,
)
cSharp::Argument_strategy = st.builds(
    cSharp::Argument,
)
ConstructorInitializer_strategy = st.builds(
    ConstructorInitializer,
)
TypeOrVoid_strategy = st.builds(
    TypeOrVoid,
)
cSharp::Void_strategy = st.builds(
    cSharp::Void,
)
BuiltInClassType_strategy = st.builds(
    BuiltInClassType,
)
cSharp::String_strategy = st.builds(
    cSharp::String,
)
cSharp::Object_strategy = st.builds(
    cSharp::Object,
)
IntegralType_strategy = st.builds(
    IntegralType,
)
cSharp::ULong_strategy = st.builds(
    cSharp::ULong,
)
cSharp::Char_strategy = st.builds(
    cSharp::Char,
)
cSharp::Short_strategy = st.builds(
    cSharp::Short,
)
cSharp::Long_strategy = st.builds(
    cSharp::Long,
)
cSharp::UShort_strategy = st.builds(
    cSharp::UShort,
)
cSharp::Byte_strategy = st.builds(
    cSharp::Byte,
)
cSharp::Int_strategy = st.builds(
    cSharp::Int,
)
cSharp::UInt_strategy = st.builds(
    cSharp::UInt,
)
cSharp::SByte_strategy = st.builds(
    cSharp::SByte,
)
GetAccessorDeclaration_strategy = st.builds(
    GetAccessorDeclaration,
)
SetAccessorDeclaration_strategy = st.builds(
    SetAccessorDeclaration,
)
cSharp::MaybeEmptyBlock_strategy = st.builds(
    cSharp::MaybeEmptyBlock,
)
MaybeEmptyBlock_strategy = st.builds(
    MaybeEmptyBlock,
)
AddAccessorDeclaration_strategy = st.builds(
    AddAccessorDeclaration,
)
RemoveAccessorDeclaration_strategy = st.builds(
    RemoveAccessorDeclaration,
)
cSharp::Block_strategy = st.builds(
    cSharp::Block,
)
cSharp::ElsePart_strategy = st.builds(
    cSharp::ElsePart,
)
cSharp::SwitchLabel_strategy = st.builds(
    cSharp::SwitchLabel,
)
cSharp::SwitchSection_strategy = st.builds(
    cSharp::SwitchSection,
)
cSharp::SwitchStatement_strategy = st.builds(
    cSharp::SwitchStatement,
)
cSharp::IfStatement_strategy = st.builds(
    cSharp::IfStatement,
)
cSharp::StatementExpressionList_strategy = st.builds(
    cSharp::StatementExpressionList,
)
cSharp::ForInitializer_strategy = st.builds(
    cSharp::ForInitializer,
)
cSharp::ForeachStatement_strategy = st.builds(
    cSharp::ForeachStatement,
)
cSharp::ForStatement_strategy = st.builds(
    cSharp::ForStatement,
)
cSharp::DoStatement_strategy = st.builds(
    cSharp::DoStatement,
)
cSharp::WhileStatement_strategy = st.builds(
    cSharp::WhileStatement,
)
cSharp::GotoStatement_strategy = st.builds(
    cSharp::GotoStatement,
)
cSharp::ContinueStatement_strategy = st.builds(
    cSharp::ContinueStatement,
)
cSharp::BreakStatement_strategy = st.builds(
    cSharp::BreakStatement,
)
cSharp::GeneralCatchclause_strategy = st.builds(
    cSharp::GeneralCatchclause,
)
cSharp::SpecificCatchClause_strategy = st.builds(
    cSharp::SpecificCatchClause,
)
cSharp::ConstructorInitializer_strategy = st.builds(
    cSharp::ConstructorInitializer,
)
cSharp::InterfaceAccessors_strategy = st.builds(
    cSharp::InterfaceAccessors,
)
cSharp::ClassMemberDeclaration_strategy = st.builds(
    cSharp::ClassMemberDeclaration,
)
cSharp::ClassBody_strategy = st.builds(
    cSharp::ClassBody,
)
cSharp::ClassBase_strategy = st.builds(
    cSharp::ClassBase,
)
cSharp::InterfaceEventDeclaration_strategy = st.builds(
    cSharp::InterfaceEventDeclaration,
)
cSharp::InterfaceMethodDeclaration_strategy = st.builds(
    cSharp::InterfaceMethodDeclaration,
)
cSharp::InterfaceMemberDeclaration_strategy = st.builds(
    cSharp::InterfaceMemberDeclaration,
)
cSharp::InterfaceBody_strategy = st.builds(
    cSharp::InterfaceBody,
)
cSharp::EnumMemberDeclaration_strategy = st.builds(
    cSharp::EnumMemberDeclaration,
)
cSharp::EnumBody_strategy = st.builds(
    cSharp::EnumBody,
)
cSharp::DelegateDeclaration_strategy = st.builds(
    cSharp::DelegateDeclaration,
)
cSharp::EnumDeclaration_strategy = st.builds(
    cSharp::EnumDeclaration,
)
cSharp::InterfaceDeclaration_strategy = st.builds(
    cSharp::InterfaceDeclaration,
)
cSharp::FormalParameterList_strategy = st.builds(
    cSharp::FormalParameterList,
)
cSharp::InterfacePropertyDeclaration_strategy = st.builds(
    cSharp::InterfacePropertyDeclaration,
)
cSharp::InterfaceIndexerDeclaration_strategy = st.builds(
    cSharp::InterfaceIndexerDeclaration,
)
cSharp::TypeDeclaration_strategy = st.builds(
    cSharp::TypeDeclaration,
)
cSharp::NamespaceDeclaration_strategy = st.builds(
    cSharp::NamespaceDeclaration,
)
cSharp::QualifiedIdentifierList_strategy = st.builds(
    cSharp::QualifiedIdentifierList,
)
ClassBase_strategy = st.builds(
    ClassBase,
)
ArrayType_strategy = st.builds(
    ArrayType,
)
BuiltInType_strategy = st.builds(
    BuiltInType,
)
cSharp::Double_strategy = st.builds(
    cSharp::Double,
)
cSharp::Decimal_strategy = st.builds(
    cSharp::Decimal,
)
cSharp::BuiltInClassType_strategy = st.builds(
    cSharp::BuiltInClassType,
)
cSharp::Float_strategy = st.builds(
    cSharp::Float,
)
cSharp::Bool_strategy = st.builds(
    cSharp::Bool,
)
cSharp::IntegralType_strategy = st.builds(
    cSharp::IntegralType,
)
cSharp::ConstantDeclarator_strategy = st.builds(
    cSharp::ConstantDeclarator,
)
cSharp::AccessorDeclarations_strategy = st.builds(
    cSharp::AccessorDeclarations,
)
cSharp::EventAccessorDeclarations_strategy = st.builds(
    cSharp::EventAccessorDeclarations,
)
cSharp::ClassDeclaration_strategy = st.builds(
    cSharp::ClassDeclaration,
    classModifier=
        safe_text
)
cSharp::NamespaceBody_strategy = st.builds(
    cSharp::NamespaceBody,
)
cSharp::VariableInitializer_strategy = st.builds(
    cSharp::VariableInitializer,
)
cSharp::PrimaryExpression2_strategy = st.builds(
    cSharp::PrimaryExpression2,
    incrementeDecrement=
        safe_text
)
cSharp::TypeOrVoid_strategy = st.builds(
    cSharp::TypeOrVoid,
)
cSharp::ArgumentList_strategy = st.builds(
    cSharp::ArgumentList,
)
cSharp::VariableDeclarator_strategy = st.builds(
    cSharp::VariableDeclarator,
)
ConstantDeclaration_strategy = st.builds(
    ConstantDeclaration,
)
FieldDeclaration_strategy = st.builds(
    FieldDeclaration,
)
PropertyDeclaration_strategy = st.builds(
    PropertyDeclaration,
)
EventDeclaration_strategy = st.builds(
    EventDeclaration,
)
cSharp::Type_strategy = st.builds(
    cSharp::Type,
)
cSharp::BuiltInType_strategy = st.builds(
    cSharp::BuiltInType,
)
cSharp::NonArrayType_strategy = st.builds(
    cSharp::NonArrayType,
)
cSharp::PrimaryExpression_strategy = st.builds(
    cSharp::PrimaryExpression,
    rankSpecifier=
        safe_text,
    predefinedType=
        safe_text,
    literal=
        safe_text
)
cSharp::Expression2_strategy = st.builds(
    cSharp::Expression2,
)
cSharp::UnaryExpression_strategy = st.builds(
    cSharp::UnaryExpression,
    expUnaryOperator=
        safe_text
)
ResourceAquisition_strategy = st.builds(
    ResourceAquisition,
)
cSharp::LocalVariableDeclaration_strategy = st.builds(
    cSharp::LocalVariableDeclaration,
)
Argument_strategy = st.builds(
    Argument,
)
VariableInitializer_strategy = st.builds(
    VariableInitializer,
)
cSharp::ArrayInitializer_strategy = st.builds(
    cSharp::ArrayInitializer,
)
cSharp::Expression_strategy = st.builds(
    cSharp::Expression,
)
cSharp::ExpressionList_strategy = st.builds(
    cSharp::ExpressionList,
)
cSharp::AttributeArguments_strategy = st.builds(
    cSharp::AttributeArguments,
)
cSharp::AttributeName_strategy = st.builds(
    cSharp::AttributeName,
)
cSharp::GlobalAttributeSection_strategy = st.builds(
    cSharp::GlobalAttributeSection,
)
cSharp::ArrayType_strategy = st.builds(
    cSharp::ArrayType,
)
cSharp::QualifiedIdentifier_strategy = st.builds(
    cSharp::QualifiedIdentifier,
)
cSharp::Identifier_strategy = st.builds(
    cSharp::Identifier,
)
cSharp::NamespaceMemberDeclaration_strategy = st.builds(
    cSharp::NamespaceMemberDeclaration,
)
cSharp::GlobalAttributes_strategy = st.builds(
    cSharp::GlobalAttributes,
)
cSharp::UsingDirective_strategy = st.builds(
    cSharp::UsingDirective,
)
cSharp::CompilationUnit_strategy = st.builds(
    cSharp::CompilationUnit,
)
cSharp::Attribute_strategy = st.builds(
    cSharp::Attribute,
)
AttributeSection_strategy = st.builds(
    AttributeSection,
)
cSharp::AttributeSection_strategy = st.builds(
    cSharp::AttributeSection,
)
cSharp::Attributes_strategy = st.builds(
    cSharp::Attributes,
)
cSharp::AttributeList_strategy = st.builds(
    cSharp::AttributeList,
)

@given(instance=cSharp::FinallyClause_strategy)
@settings(max_examples=50)
def test_csharp::finallyclause_instantiation(instance):
    assert isinstance(instance, cSharp::FinallyClause)

@given(instance=cSharp::CatchClauses_strategy)
@settings(max_examples=50)
def test_csharp::catchclauses_instantiation(instance):
    assert isinstance(instance, cSharp::CatchClauses)

@given(instance=cSharp::ThrowStatement_strategy)
@settings(max_examples=50)
def test_csharp::throwstatement_instantiation(instance):
    assert isinstance(instance, cSharp::ThrowStatement)

@given(instance=cSharp::ReturnStatement_strategy)
@settings(max_examples=50)
def test_csharp::returnstatement_instantiation(instance):
    assert isinstance(instance, cSharp::ReturnStatement)

@given(instance=cSharp::ResourceAquisition_strategy)
@settings(max_examples=50)
def test_csharp::resourceaquisition_instantiation(instance):
    assert isinstance(instance, cSharp::ResourceAquisition)

@given(instance=cSharp::UsingStatement_strategy)
@settings(max_examples=50)
def test_csharp::usingstatement_instantiation(instance):
    assert isinstance(instance, cSharp::UsingStatement)

@given(instance=cSharp::LockStatement_strategy)
@settings(max_examples=50)
def test_csharp::lockstatement_instantiation(instance):
    assert isinstance(instance, cSharp::LockStatement)

@given(instance=cSharp::StatementExpression_strategy)
@settings(max_examples=50)
def test_csharp::statementexpression_instantiation(instance):
    assert isinstance(instance, cSharp::StatementExpression)

@given(instance=cSharp::StatementExpression_strategy)
def test_csharp::statementexpression_incrimentDecrement_type(instance):
    assert isinstance(instance.incrimentDecrement, str)


@given(instance=cSharp::StatementExpression_strategy)
def test_csharp::statementexpression_incrimentDecrement_setter(instance):
    original = instance.incrimentDecrement
    instance.incrimentDecrement = original
    assert instance.incrimentDecrement == original

@given(instance=cSharp::StatementExpression_strategy)
def test_csharp::statementexpression_assignementOperator_type(instance):
    assert isinstance(instance.assignementOperator, str)


@given(instance=cSharp::StatementExpression_strategy)
def test_csharp::statementexpression_assignementOperator_setter(instance):
    original = instance.assignementOperator
    instance.assignementOperator = original
    assert instance.assignementOperator == original

@given(instance=cSharp::LocalconstantDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::localconstantdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::LocalconstantDeclaration)

@given(instance=cSharp::EmbeddedStatement_strategy)
@settings(max_examples=50)
def test_csharp::embeddedstatement_instantiation(instance):
    assert isinstance(instance, cSharp::EmbeddedStatement)

@given(instance=cSharp::DeclarationStatment_strategy)
@settings(max_examples=50)
def test_csharp::declarationstatment_instantiation(instance):
    assert isinstance(instance, cSharp::DeclarationStatment)

@given(instance=cSharp::LabeledStatement_strategy)
@settings(max_examples=50)
def test_csharp::labeledstatement_instantiation(instance):
    assert isinstance(instance, cSharp::LabeledStatement)

@given(instance=cSharp::Statement_strategy)
@settings(max_examples=50)
def test_csharp::statement_instantiation(instance):
    assert isinstance(instance, cSharp::Statement)

@given(instance=cSharp::TryStatement_strategy)
@settings(max_examples=50)
def test_csharp::trystatement_instantiation(instance):
    assert isinstance(instance, cSharp::TryStatement)

@given(instance=cSharp::JumpStatement_strategy)
@settings(max_examples=50)
def test_csharp::jumpstatement_instantiation(instance):
    assert isinstance(instance, cSharp::JumpStatement)

@given(instance=cSharp::IterationStatement_strategy)
@settings(max_examples=50)
def test_csharp::iterationstatement_instantiation(instance):
    assert isinstance(instance, cSharp::IterationStatement)

@given(instance=cSharp::SelectionStatement_strategy)
@settings(max_examples=50)
def test_csharp::selectionstatement_instantiation(instance):
    assert isinstance(instance, cSharp::SelectionStatement)

@given(instance=DelegateDeclaration_strategy)
@settings(max_examples=50)
def test_delegatedeclaration_instantiation(instance):
    assert isinstance(instance, DelegateDeclaration)

@given(instance=cSharp::FixedParameter_strategy)
@settings(max_examples=50)
def test_csharp::fixedparameter_instantiation(instance):
    assert isinstance(instance, cSharp::FixedParameter)

@given(instance=FormalParameterList_strategy)
@settings(max_examples=50)
def test_formalparameterlist_instantiation(instance):
    assert isinstance(instance, FormalParameterList)

@given(instance=cSharp::FixedParameters_strategy)
@settings(max_examples=50)
def test_csharp::fixedparameters_instantiation(instance):
    assert isinstance(instance, cSharp::FixedParameters)

@given(instance=cSharp::MethodHeader_strategy)
@settings(max_examples=50)
def test_csharp::methodheader_instantiation(instance):
    assert isinstance(instance, cSharp::MethodHeader)

@given(instance=cSharp::MethodHeader_strategy)
def test_csharp::methodheader_modifier_type(instance):
    assert isinstance(instance.modifier, str)


@given(instance=cSharp::MethodHeader_strategy)
def test_csharp::methodheader_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=cSharp::SetAccessorDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::setaccessordeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::SetAccessorDeclaration)

@given(instance=cSharp::GetAccessorDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::getaccessordeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::GetAccessorDeclaration)

@given(instance=cSharp::RemoveAccessorDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::removeaccessordeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::RemoveAccessorDeclaration)

@given(instance=cSharp::AddAccessorDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::addaccessordeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::AddAccessorDeclaration)

@given(instance=cSharp::ParameterArray_strategy)
@settings(max_examples=50)
def test_csharp::parameterarray_instantiation(instance):
    assert isinstance(instance, cSharp::ParameterArray)

@given(instance=OperatorDeclarator_strategy)
@settings(max_examples=50)
def test_operatordeclarator_instantiation(instance):
    assert isinstance(instance, OperatorDeclarator)

@given(instance=cSharp::UnaryOperatorDeclarator_strategy)
@settings(max_examples=50)
def test_csharp::unaryoperatordeclarator_instantiation(instance):
    assert isinstance(instance, cSharp::UnaryOperatorDeclarator)

@given(instance=cSharp::BinaryOperatorDeclarator_strategy)
@settings(max_examples=50)
def test_csharp::binaryoperatordeclarator_instantiation(instance):
    assert isinstance(instance, cSharp::BinaryOperatorDeclarator)

@given(instance=cSharp::BinaryOperatorDeclarator_strategy)
def test_csharp::binaryoperatordeclarator_overBinOperator_type(instance):
    assert isinstance(instance.overBinOperator, str)


@given(instance=cSharp::BinaryOperatorDeclarator_strategy)
def test_csharp::binaryoperatordeclarator_overBinOperator_setter(instance):
    original = instance.overBinOperator
    instance.overBinOperator = original
    assert instance.overBinOperator == original

@given(instance=cSharp::ConversionOperatorDeclarator_strategy)
@settings(max_examples=50)
def test_csharp::conversionoperatordeclarator_instantiation(instance):
    assert isinstance(instance, cSharp::ConversionOperatorDeclarator)

@given(instance=cSharp::OperatorDeclarator_strategy)
@settings(max_examples=50)
def test_csharp::operatordeclarator_instantiation(instance):
    assert isinstance(instance, cSharp::OperatorDeclarator)

@given(instance=cSharp::IndexerDeclarator_strategy)
@settings(max_examples=50)
def test_csharp::indexerdeclarator_instantiation(instance):
    assert isinstance(instance, cSharp::IndexerDeclarator)

@given(instance=cSharp::ConstructorDeclarator_strategy)
@settings(max_examples=50)
def test_csharp::constructordeclarator_instantiation(instance):
    assert isinstance(instance, cSharp::ConstructorDeclarator)

@given(instance=cSharp::StaticConstructorDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::staticconstructordeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::StaticConstructorDeclaration)

@given(instance=cSharp::StaticConstructorDeclaration_strategy)
def test_csharp::staticconstructordeclaration_staticCosntModifier_type(instance):
    assert isinstance(instance.staticCosntModifier, str)


@given(instance=cSharp::StaticConstructorDeclaration_strategy)
def test_csharp::staticconstructordeclaration_staticCosntModifier_setter(instance):
    original = instance.staticCosntModifier
    instance.staticCosntModifier = original
    assert instance.staticCosntModifier == original

@given(instance=cSharp::DestructorDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::destructordeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::DestructorDeclaration)

@given(instance=cSharp::ConstructorDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::constructordeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::ConstructorDeclaration)

@given(instance=cSharp::ConstructorDeclaration_strategy)
def test_csharp::constructordeclaration_constModifier_type(instance):
    assert isinstance(instance.constModifier, str)


@given(instance=cSharp::ConstructorDeclaration_strategy)
def test_csharp::constructordeclaration_constModifier_setter(instance):
    original = instance.constModifier
    instance.constModifier = original
    assert instance.constModifier == original

@given(instance=cSharp::OperatorDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::operatordeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::OperatorDeclaration)

@given(instance=cSharp::OperatorDeclaration_strategy)
def test_csharp::operatordeclaration_opModifier_type(instance):
    assert isinstance(instance.opModifier, str)


@given(instance=cSharp::OperatorDeclaration_strategy)
def test_csharp::operatordeclaration_opModifier_setter(instance):
    original = instance.opModifier
    instance.opModifier = original
    assert instance.opModifier == original

@given(instance=cSharp::IndexerDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::indexerdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::IndexerDeclaration)

@given(instance=cSharp::IndexerDeclaration_strategy)
def test_csharp::indexerdeclaration_idModifier_type(instance):
    assert isinstance(instance.idModifier, str)


@given(instance=cSharp::IndexerDeclaration_strategy)
def test_csharp::indexerdeclaration_idModifier_setter(instance):
    original = instance.idModifier
    instance.idModifier = original
    assert instance.idModifier == original

@given(instance=cSharp::EventDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::eventdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::EventDeclaration)

@given(instance=cSharp::PropertyDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::propertydeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::PropertyDeclaration)

@given(instance=cSharp::ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::constantdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::ConstantDeclaration)

@given(instance=cSharp::MethodDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::methoddeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::MethodDeclaration)

@given(instance=cSharp::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::fielddeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::FieldDeclaration)

@given(instance=cSharp::Argument_strategy)
@settings(max_examples=50)
def test_csharp::argument_instantiation(instance):
    assert isinstance(instance, cSharp::Argument)

@given(instance=ConstructorInitializer_strategy)
@settings(max_examples=50)
def test_constructorinitializer_instantiation(instance):
    assert isinstance(instance, ConstructorInitializer)

@given(instance=TypeOrVoid_strategy)
@settings(max_examples=50)
def test_typeorvoid_instantiation(instance):
    assert isinstance(instance, TypeOrVoid)

@given(instance=cSharp::Void_strategy)
@settings(max_examples=50)
def test_csharp::void_instantiation(instance):
    assert isinstance(instance, cSharp::Void)

@given(instance=BuiltInClassType_strategy)
@settings(max_examples=50)
def test_builtinclasstype_instantiation(instance):
    assert isinstance(instance, BuiltInClassType)

@given(instance=cSharp::String_strategy)
@settings(max_examples=50)
def test_csharp::string_instantiation(instance):
    assert isinstance(instance, cSharp::String)

@given(instance=cSharp::Object_strategy)
@settings(max_examples=50)
def test_csharp::object_instantiation(instance):
    assert isinstance(instance, cSharp::Object)

@given(instance=IntegralType_strategy)
@settings(max_examples=50)
def test_integraltype_instantiation(instance):
    assert isinstance(instance, IntegralType)

@given(instance=cSharp::ULong_strategy)
@settings(max_examples=50)
def test_csharp::ulong_instantiation(instance):
    assert isinstance(instance, cSharp::ULong)

@given(instance=cSharp::Char_strategy)
@settings(max_examples=50)
def test_csharp::char_instantiation(instance):
    assert isinstance(instance, cSharp::Char)

@given(instance=cSharp::Short_strategy)
@settings(max_examples=50)
def test_csharp::short_instantiation(instance):
    assert isinstance(instance, cSharp::Short)

@given(instance=cSharp::Long_strategy)
@settings(max_examples=50)
def test_csharp::long_instantiation(instance):
    assert isinstance(instance, cSharp::Long)

@given(instance=cSharp::UShort_strategy)
@settings(max_examples=50)
def test_csharp::ushort_instantiation(instance):
    assert isinstance(instance, cSharp::UShort)

@given(instance=cSharp::Byte_strategy)
@settings(max_examples=50)
def test_csharp::byte_instantiation(instance):
    assert isinstance(instance, cSharp::Byte)

@given(instance=cSharp::Int_strategy)
@settings(max_examples=50)
def test_csharp::int_instantiation(instance):
    assert isinstance(instance, cSharp::Int)

@given(instance=cSharp::UInt_strategy)
@settings(max_examples=50)
def test_csharp::uint_instantiation(instance):
    assert isinstance(instance, cSharp::UInt)

@given(instance=cSharp::SByte_strategy)
@settings(max_examples=50)
def test_csharp::sbyte_instantiation(instance):
    assert isinstance(instance, cSharp::SByte)

@given(instance=GetAccessorDeclaration_strategy)
@settings(max_examples=50)
def test_getaccessordeclaration_instantiation(instance):
    assert isinstance(instance, GetAccessorDeclaration)

@given(instance=SetAccessorDeclaration_strategy)
@settings(max_examples=50)
def test_setaccessordeclaration_instantiation(instance):
    assert isinstance(instance, SetAccessorDeclaration)

@given(instance=cSharp::MaybeEmptyBlock_strategy)
@settings(max_examples=50)
def test_csharp::maybeemptyblock_instantiation(instance):
    assert isinstance(instance, cSharp::MaybeEmptyBlock)

@given(instance=MaybeEmptyBlock_strategy)
@settings(max_examples=50)
def test_maybeemptyblock_instantiation(instance):
    assert isinstance(instance, MaybeEmptyBlock)

@given(instance=AddAccessorDeclaration_strategy)
@settings(max_examples=50)
def test_addaccessordeclaration_instantiation(instance):
    assert isinstance(instance, AddAccessorDeclaration)

@given(instance=RemoveAccessorDeclaration_strategy)
@settings(max_examples=50)
def test_removeaccessordeclaration_instantiation(instance):
    assert isinstance(instance, RemoveAccessorDeclaration)

@given(instance=cSharp::Block_strategy)
@settings(max_examples=50)
def test_csharp::block_instantiation(instance):
    assert isinstance(instance, cSharp::Block)

@given(instance=cSharp::ElsePart_strategy)
@settings(max_examples=50)
def test_csharp::elsepart_instantiation(instance):
    assert isinstance(instance, cSharp::ElsePart)

@given(instance=cSharp::SwitchLabel_strategy)
@settings(max_examples=50)
def test_csharp::switchlabel_instantiation(instance):
    assert isinstance(instance, cSharp::SwitchLabel)

@given(instance=cSharp::SwitchSection_strategy)
@settings(max_examples=50)
def test_csharp::switchsection_instantiation(instance):
    assert isinstance(instance, cSharp::SwitchSection)

@given(instance=cSharp::SwitchStatement_strategy)
@settings(max_examples=50)
def test_csharp::switchstatement_instantiation(instance):
    assert isinstance(instance, cSharp::SwitchStatement)

@given(instance=cSharp::IfStatement_strategy)
@settings(max_examples=50)
def test_csharp::ifstatement_instantiation(instance):
    assert isinstance(instance, cSharp::IfStatement)

@given(instance=cSharp::StatementExpressionList_strategy)
@settings(max_examples=50)
def test_csharp::statementexpressionlist_instantiation(instance):
    assert isinstance(instance, cSharp::StatementExpressionList)

@given(instance=cSharp::ForInitializer_strategy)
@settings(max_examples=50)
def test_csharp::forinitializer_instantiation(instance):
    assert isinstance(instance, cSharp::ForInitializer)

@given(instance=cSharp::ForeachStatement_strategy)
@settings(max_examples=50)
def test_csharp::foreachstatement_instantiation(instance):
    assert isinstance(instance, cSharp::ForeachStatement)

@given(instance=cSharp::ForStatement_strategy)
@settings(max_examples=50)
def test_csharp::forstatement_instantiation(instance):
    assert isinstance(instance, cSharp::ForStatement)

@given(instance=cSharp::DoStatement_strategy)
@settings(max_examples=50)
def test_csharp::dostatement_instantiation(instance):
    assert isinstance(instance, cSharp::DoStatement)

@given(instance=cSharp::WhileStatement_strategy)
@settings(max_examples=50)
def test_csharp::whilestatement_instantiation(instance):
    assert isinstance(instance, cSharp::WhileStatement)

@given(instance=cSharp::GotoStatement_strategy)
@settings(max_examples=50)
def test_csharp::gotostatement_instantiation(instance):
    assert isinstance(instance, cSharp::GotoStatement)

@given(instance=cSharp::ContinueStatement_strategy)
@settings(max_examples=50)
def test_csharp::continuestatement_instantiation(instance):
    assert isinstance(instance, cSharp::ContinueStatement)

@given(instance=cSharp::BreakStatement_strategy)
@settings(max_examples=50)
def test_csharp::breakstatement_instantiation(instance):
    assert isinstance(instance, cSharp::BreakStatement)

@given(instance=cSharp::GeneralCatchclause_strategy)
@settings(max_examples=50)
def test_csharp::generalcatchclause_instantiation(instance):
    assert isinstance(instance, cSharp::GeneralCatchclause)

@given(instance=cSharp::SpecificCatchClause_strategy)
@settings(max_examples=50)
def test_csharp::specificcatchclause_instantiation(instance):
    assert isinstance(instance, cSharp::SpecificCatchClause)

@given(instance=cSharp::ConstructorInitializer_strategy)
@settings(max_examples=50)
def test_csharp::constructorinitializer_instantiation(instance):
    assert isinstance(instance, cSharp::ConstructorInitializer)

@given(instance=cSharp::InterfaceAccessors_strategy)
@settings(max_examples=50)
def test_csharp::interfaceaccessors_instantiation(instance):
    assert isinstance(instance, cSharp::InterfaceAccessors)

@given(instance=cSharp::ClassMemberDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::classmemberdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::ClassMemberDeclaration)

@given(instance=cSharp::ClassBody_strategy)
@settings(max_examples=50)
def test_csharp::classbody_instantiation(instance):
    assert isinstance(instance, cSharp::ClassBody)

@given(instance=cSharp::ClassBase_strategy)
@settings(max_examples=50)
def test_csharp::classbase_instantiation(instance):
    assert isinstance(instance, cSharp::ClassBase)

@given(instance=cSharp::InterfaceEventDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::interfaceeventdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::InterfaceEventDeclaration)

@given(instance=cSharp::InterfaceMethodDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::interfacemethoddeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::InterfaceMethodDeclaration)

@given(instance=cSharp::InterfaceMemberDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::interfacememberdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::InterfaceMemberDeclaration)

@given(instance=cSharp::InterfaceBody_strategy)
@settings(max_examples=50)
def test_csharp::interfacebody_instantiation(instance):
    assert isinstance(instance, cSharp::InterfaceBody)

@given(instance=cSharp::EnumMemberDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::enummemberdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::EnumMemberDeclaration)

@given(instance=cSharp::EnumBody_strategy)
@settings(max_examples=50)
def test_csharp::enumbody_instantiation(instance):
    assert isinstance(instance, cSharp::EnumBody)

@given(instance=cSharp::DelegateDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::delegatedeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::DelegateDeclaration)

@given(instance=cSharp::EnumDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::enumdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::EnumDeclaration)

@given(instance=cSharp::InterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::interfacedeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::InterfaceDeclaration)

@given(instance=cSharp::FormalParameterList_strategy)
@settings(max_examples=50)
def test_csharp::formalparameterlist_instantiation(instance):
    assert isinstance(instance, cSharp::FormalParameterList)

@given(instance=cSharp::InterfacePropertyDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::interfacepropertydeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::InterfacePropertyDeclaration)

@given(instance=cSharp::InterfaceIndexerDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::interfaceindexerdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::InterfaceIndexerDeclaration)

@given(instance=cSharp::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::typedeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::TypeDeclaration)

@given(instance=cSharp::NamespaceDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::namespacedeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::NamespaceDeclaration)

@given(instance=cSharp::QualifiedIdentifierList_strategy)
@settings(max_examples=50)
def test_csharp::qualifiedidentifierlist_instantiation(instance):
    assert isinstance(instance, cSharp::QualifiedIdentifierList)

@given(instance=ClassBase_strategy)
@settings(max_examples=50)
def test_classbase_instantiation(instance):
    assert isinstance(instance, ClassBase)

@given(instance=ArrayType_strategy)
@settings(max_examples=50)
def test_arraytype_instantiation(instance):
    assert isinstance(instance, ArrayType)

@given(instance=BuiltInType_strategy)
@settings(max_examples=50)
def test_builtintype_instantiation(instance):
    assert isinstance(instance, BuiltInType)

@given(instance=cSharp::Double_strategy)
@settings(max_examples=50)
def test_csharp::double_instantiation(instance):
    assert isinstance(instance, cSharp::Double)

@given(instance=cSharp::Decimal_strategy)
@settings(max_examples=50)
def test_csharp::decimal_instantiation(instance):
    assert isinstance(instance, cSharp::Decimal)

@given(instance=cSharp::BuiltInClassType_strategy)
@settings(max_examples=50)
def test_csharp::builtinclasstype_instantiation(instance):
    assert isinstance(instance, cSharp::BuiltInClassType)

@given(instance=cSharp::Float_strategy)
@settings(max_examples=50)
def test_csharp::float_instantiation(instance):
    assert isinstance(instance, cSharp::Float)

@given(instance=cSharp::Bool_strategy)
@settings(max_examples=50)
def test_csharp::bool_instantiation(instance):
    assert isinstance(instance, cSharp::Bool)

@given(instance=cSharp::IntegralType_strategy)
@settings(max_examples=50)
def test_csharp::integraltype_instantiation(instance):
    assert isinstance(instance, cSharp::IntegralType)

@given(instance=cSharp::ConstantDeclarator_strategy)
@settings(max_examples=50)
def test_csharp::constantdeclarator_instantiation(instance):
    assert isinstance(instance, cSharp::ConstantDeclarator)

@given(instance=cSharp::AccessorDeclarations_strategy)
@settings(max_examples=50)
def test_csharp::accessordeclarations_instantiation(instance):
    assert isinstance(instance, cSharp::AccessorDeclarations)

@given(instance=cSharp::EventAccessorDeclarations_strategy)
@settings(max_examples=50)
def test_csharp::eventaccessordeclarations_instantiation(instance):
    assert isinstance(instance, cSharp::EventAccessorDeclarations)

@given(instance=cSharp::ClassDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::classdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::ClassDeclaration)

@given(instance=cSharp::ClassDeclaration_strategy)
def test_csharp::classdeclaration_classModifier_type(instance):
    assert isinstance(instance.classModifier, str)


@given(instance=cSharp::ClassDeclaration_strategy)
def test_csharp::classdeclaration_classModifier_setter(instance):
    original = instance.classModifier
    instance.classModifier = original
    assert instance.classModifier == original

@given(instance=cSharp::NamespaceBody_strategy)
@settings(max_examples=50)
def test_csharp::namespacebody_instantiation(instance):
    assert isinstance(instance, cSharp::NamespaceBody)

@given(instance=cSharp::VariableInitializer_strategy)
@settings(max_examples=50)
def test_csharp::variableinitializer_instantiation(instance):
    assert isinstance(instance, cSharp::VariableInitializer)

@given(instance=cSharp::PrimaryExpression2_strategy)
@settings(max_examples=50)
def test_csharp::primaryexpression2_instantiation(instance):
    assert isinstance(instance, cSharp::PrimaryExpression2)

@given(instance=cSharp::PrimaryExpression2_strategy)
def test_csharp::primaryexpression2_incrementeDecrement_type(instance):
    assert isinstance(instance.incrementeDecrement, str)


@given(instance=cSharp::PrimaryExpression2_strategy)
def test_csharp::primaryexpression2_incrementeDecrement_setter(instance):
    original = instance.incrementeDecrement
    instance.incrementeDecrement = original
    assert instance.incrementeDecrement == original

@given(instance=cSharp::TypeOrVoid_strategy)
@settings(max_examples=50)
def test_csharp::typeorvoid_instantiation(instance):
    assert isinstance(instance, cSharp::TypeOrVoid)

@given(instance=cSharp::ArgumentList_strategy)
@settings(max_examples=50)
def test_csharp::argumentlist_instantiation(instance):
    assert isinstance(instance, cSharp::ArgumentList)

@given(instance=cSharp::VariableDeclarator_strategy)
@settings(max_examples=50)
def test_csharp::variabledeclarator_instantiation(instance):
    assert isinstance(instance, cSharp::VariableDeclarator)

@given(instance=ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_constantdeclaration_instantiation(instance):
    assert isinstance(instance, ConstantDeclaration)

@given(instance=FieldDeclaration_strategy)
@settings(max_examples=50)
def test_fielddeclaration_instantiation(instance):
    assert isinstance(instance, FieldDeclaration)

@given(instance=PropertyDeclaration_strategy)
@settings(max_examples=50)
def test_propertydeclaration_instantiation(instance):
    assert isinstance(instance, PropertyDeclaration)

@given(instance=EventDeclaration_strategy)
@settings(max_examples=50)
def test_eventdeclaration_instantiation(instance):
    assert isinstance(instance, EventDeclaration)

@given(instance=cSharp::Type_strategy)
@settings(max_examples=50)
def test_csharp::type_instantiation(instance):
    assert isinstance(instance, cSharp::Type)

@given(instance=cSharp::BuiltInType_strategy)
@settings(max_examples=50)
def test_csharp::builtintype_instantiation(instance):
    assert isinstance(instance, cSharp::BuiltInType)

@given(instance=cSharp::NonArrayType_strategy)
@settings(max_examples=50)
def test_csharp::nonarraytype_instantiation(instance):
    assert isinstance(instance, cSharp::NonArrayType)

@given(instance=cSharp::PrimaryExpression_strategy)
@settings(max_examples=50)
def test_csharp::primaryexpression_instantiation(instance):
    assert isinstance(instance, cSharp::PrimaryExpression)

@given(instance=cSharp::PrimaryExpression_strategy)
def test_csharp::primaryexpression_rankSpecifier_type(instance):
    assert isinstance(instance.rankSpecifier, str)


@given(instance=cSharp::PrimaryExpression_strategy)
def test_csharp::primaryexpression_rankSpecifier_setter(instance):
    original = instance.rankSpecifier
    instance.rankSpecifier = original
    assert instance.rankSpecifier == original

@given(instance=cSharp::PrimaryExpression_strategy)
def test_csharp::primaryexpression_predefinedType_type(instance):
    assert isinstance(instance.predefinedType, str)


@given(instance=cSharp::PrimaryExpression_strategy)
def test_csharp::primaryexpression_predefinedType_setter(instance):
    original = instance.predefinedType
    instance.predefinedType = original
    assert instance.predefinedType == original

@given(instance=cSharp::PrimaryExpression_strategy)
def test_csharp::primaryexpression_literal_type(instance):
    assert isinstance(instance.literal, str)


@given(instance=cSharp::PrimaryExpression_strategy)
def test_csharp::primaryexpression_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=cSharp::Expression2_strategy)
@settings(max_examples=50)
def test_csharp::expression2_instantiation(instance):
    assert isinstance(instance, cSharp::Expression2)

@given(instance=cSharp::UnaryExpression_strategy)
@settings(max_examples=50)
def test_csharp::unaryexpression_instantiation(instance):
    assert isinstance(instance, cSharp::UnaryExpression)

@given(instance=cSharp::UnaryExpression_strategy)
def test_csharp::unaryexpression_expUnaryOperator_type(instance):
    assert isinstance(instance.expUnaryOperator, str)


@given(instance=cSharp::UnaryExpression_strategy)
def test_csharp::unaryexpression_expUnaryOperator_setter(instance):
    original = instance.expUnaryOperator
    instance.expUnaryOperator = original
    assert instance.expUnaryOperator == original

@given(instance=ResourceAquisition_strategy)
@settings(max_examples=50)
def test_resourceaquisition_instantiation(instance):
    assert isinstance(instance, ResourceAquisition)

@given(instance=cSharp::LocalVariableDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::localvariabledeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::LocalVariableDeclaration)

@given(instance=Argument_strategy)
@settings(max_examples=50)
def test_argument_instantiation(instance):
    assert isinstance(instance, Argument)

@given(instance=VariableInitializer_strategy)
@settings(max_examples=50)
def test_variableinitializer_instantiation(instance):
    assert isinstance(instance, VariableInitializer)

@given(instance=cSharp::ArrayInitializer_strategy)
@settings(max_examples=50)
def test_csharp::arrayinitializer_instantiation(instance):
    assert isinstance(instance, cSharp::ArrayInitializer)

@given(instance=cSharp::Expression_strategy)
@settings(max_examples=50)
def test_csharp::expression_instantiation(instance):
    assert isinstance(instance, cSharp::Expression)

@given(instance=cSharp::ExpressionList_strategy)
@settings(max_examples=50)
def test_csharp::expressionlist_instantiation(instance):
    assert isinstance(instance, cSharp::ExpressionList)

@given(instance=cSharp::AttributeArguments_strategy)
@settings(max_examples=50)
def test_csharp::attributearguments_instantiation(instance):
    assert isinstance(instance, cSharp::AttributeArguments)

@given(instance=cSharp::AttributeName_strategy)
@settings(max_examples=50)
def test_csharp::attributename_instantiation(instance):
    assert isinstance(instance, cSharp::AttributeName)

@given(instance=cSharp::GlobalAttributeSection_strategy)
@settings(max_examples=50)
def test_csharp::globalattributesection_instantiation(instance):
    assert isinstance(instance, cSharp::GlobalAttributeSection)

@given(instance=cSharp::ArrayType_strategy)
@settings(max_examples=50)
def test_csharp::arraytype_instantiation(instance):
    assert isinstance(instance, cSharp::ArrayType)

@given(instance=cSharp::QualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_csharp::qualifiedidentifier_instantiation(instance):
    assert isinstance(instance, cSharp::QualifiedIdentifier)

@given(instance=cSharp::Identifier_strategy)
@settings(max_examples=50)
def test_csharp::identifier_instantiation(instance):
    assert isinstance(instance, cSharp::Identifier)

@given(instance=cSharp::NamespaceMemberDeclaration_strategy)
@settings(max_examples=50)
def test_csharp::namespacememberdeclaration_instantiation(instance):
    assert isinstance(instance, cSharp::NamespaceMemberDeclaration)

@given(instance=cSharp::GlobalAttributes_strategy)
@settings(max_examples=50)
def test_csharp::globalattributes_instantiation(instance):
    assert isinstance(instance, cSharp::GlobalAttributes)

@given(instance=cSharp::UsingDirective_strategy)
@settings(max_examples=50)
def test_csharp::usingdirective_instantiation(instance):
    assert isinstance(instance, cSharp::UsingDirective)

@given(instance=cSharp::CompilationUnit_strategy)
@settings(max_examples=50)
def test_csharp::compilationunit_instantiation(instance):
    assert isinstance(instance, cSharp::CompilationUnit)

@given(instance=cSharp::Attribute_strategy)
@settings(max_examples=50)
def test_csharp::attribute_instantiation(instance):
    assert isinstance(instance, cSharp::Attribute)

@given(instance=AttributeSection_strategy)
@settings(max_examples=50)
def test_attributesection_instantiation(instance):
    assert isinstance(instance, AttributeSection)

@given(instance=cSharp::AttributeSection_strategy)
@settings(max_examples=50)
def test_csharp::attributesection_instantiation(instance):
    assert isinstance(instance, cSharp::AttributeSection)

@given(instance=cSharp::Attributes_strategy)
@settings(max_examples=50)
def test_csharp::attributes_instantiation(instance):
    assert isinstance(instance, cSharp::Attributes)

@given(instance=cSharp::AttributeList_strategy)
@settings(max_examples=50)
def test_csharp::attributelist_instantiation(instance):
    assert isinstance(instance, cSharp::AttributeList)

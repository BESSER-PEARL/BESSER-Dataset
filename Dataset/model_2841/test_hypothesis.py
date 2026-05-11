import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ContinueStatement,
    optGrammar::Continue,
    NamedType,
    optGrammar::UnitsLiteral,
    optGrammar::TimeUnitsLiteral,
    optGrammar::IntLiteral,
    optGrammar::UnitTypes,
    optGrammar::DecimalLiteral,
    optGrammar::HexLiteral,
    optGrammar::SecondOperators,
    optGrammar::PrimaryArithmetic,
    optGrammar::ArithmeticOperations,
    optGrammar::IntParameter,
    Literal,
    optGrammar::EcrecoverFunction,
    optGrammar::SpecialLiteral,
    optGrammar::HashFunction,
    optGrammar::StringLiteral,
    optGrammar::GasleftFunction,
    optGrammar::MathematicalFunction,
    optGrammar::BooleanLiteral,
    optGrammar::BlockhashFunction,
    PrimaryArithmetic,
    optGrammar::NumericLiteral,
    LoopStructures,
    optGrammar::IfStatement,
    optGrammar::FunctionCall,
    optGrammar::Statement,
    optGrammar::ForStatement,
    optGrammar::WhileStatement,
    Qualifier,
    optGrammar::Arguments,
    optGrammar::Index,
    optGrammar::Field,
    optGrammar::Qualifier,
    optGrammar::ReturnParameterDeclaration,
    SimpleStatement2,
    SimpleStatement,
    optGrammar::VarVariableTupleVariableDeclaration,
    optGrammar::StandardVariableDeclaration,
    optGrammar::VarVariableTypeDeclaration,
    optGrammar::StandardTypeWithoutQualifiedIdentifier,
    Type,
    optGrammar::StandardType,
    optGrammar::ArrayType,
    StandardTypeWithoutQualifiedIdentifier,
    StandardType,
    optGrammar::NamedType,
    optGrammar::Type,
    VariableDeclarationOptionalElement,
    optGrammar::IndexedSpecifer,
    optGrammar::LocationSpecifier,
    optGrammar::ConstantSpecifier,
    optGrammar::VisibilitySpecifier,
    optGrammar::VariableDeclarationOptionalElement,
    optGrammar::ExpressionStatement,
    optGrammar::SimpleStatement2,
    Statement,
    optGrammar::BreakStatement,
    optGrammar::ContinueStatement,
    optGrammar::ReturnStatement,
    optGrammar::PlaceHolderStatement,
    optGrammar::EmitStatement,
    optGrammar::LoopStructures,
    optGrammar::DeleteStatement,
    optGrammar::ThrowStatement,
    optGrammar::DoWhileStatement,
    optGrammar::SimpleStatement,
    Expression,
    optGrammar::Assignment,
    optGrammar::PostIncDecExpression,
    optGrammar::Literal,
    optGrammar::Or,
    optGrammar::Exponent,
    optGrammar::QualifiedIdentifier,
    optGrammar::MulDivMod,
    optGrammar::Comparison,
    optGrammar::SpecialExpression,
    optGrammar::TypeCast,
    optGrammar::PreIncExpression,
    optGrammar::PreDecExpression,
    optGrammar::BitAnd,
    optGrammar::BinaryNotExpression,
    optGrammar::VariableDeclarationExpression,
    optGrammar::AddSub,
    optGrammar::TupleSeparator,
    optGrammar::NewExpression,
    optGrammar::SignExpression,
    optGrammar::Shift,
    optGrammar::BitOr,
    optGrammar::And,
    optGrammar::BitXor,
    optGrammar::NotExpression,
    optGrammar::Equality,
    optGrammar::Tuple,
    optGrammar::Mapping,
    optGrammar::Variable,
    optGrammar::EnumValue,
    optGrammar::ReturnsParameterList,
    optGrammar::SizedDeclaration,
    optGrammar::SimpleTypeDeclaration,
    optGrammar::LocationLiteral,
    PrimaryTypeDeclaration,
    optGrammar::ArrayableDeclaration,
    optGrammar::NonArrayableDeclaration,
    PrimaryTypeDefinitionDeclaration,
    optGrammar::PrimaryTypeDeclaration,
    optGrammar::FunctionCallArg,
    optGrammar::FunctionCallArguments,
    optGrammar::Expression,
    FunctionCallArguments,
    optGrammar::FunctionCallListArguments,
    optGrammar::Body,
    optGrammar::VisibilityLiteral,
    optGrammar::InheritanceSpecifier,
    optGrammar::SymbolAlias,
    optGrammar::versionOperator,
    optGrammar::Contract,
    optGrammar::ImportDirective,
    optGrammar::ModifierInvocation,
    optGrammar::Const,
    optGrammar::StateMutability,
    optGrammar::ParameterList,
    DefinitionBody,
    optGrammar::FunctionDefinition,
    optGrammar::Event,
    optGrammar::PrimaryTypeDefinitionDeclaration,
    optGrammar::Modifier,
    optGrammar::EnumDefinition,
    optGrammar::StructDefinition,
    optGrammar::ConstructorDefinition,
    optGrammar::DefinitionBody,
    optGrammar::PragmaDirective,
    optGrammar::Model,
    ReservedWordsEnum,
    ShiftOpEnum,
    ComparisonOpEnum,
    IncDecOpEnum,
    EqualityOpEnum,
    SpecialExpressionTypeEnum,
    MulDivModOpEnum,
    AdditionOpEnum,
    AssignmentOpEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_continuestatement_is_not_abstract():
    assert not inspect.isabstract(ContinueStatement)


def test_continuestatement_constructor_exists():
    assert callable(ContinueStatement.__init__)


def test_continuestatement_constructor_args():
    sig = inspect.signature(ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::continue_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Continue)


def test_optgrammar::continue_constructor_exists():
    assert callable(optGrammar::Continue.__init__)


def test_optgrammar::continue_constructor_args():
    sig = inspect.signature(optGrammar::Continue.__init__)
    params = list(sig.parameters.keys())



def test_namedtype_is_not_abstract():
    assert not inspect.isabstract(NamedType)


def test_namedtype_constructor_exists():
    assert callable(NamedType.__init__)


def test_namedtype_constructor_args():
    sig = inspect.signature(NamedType.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::unitsliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar::UnitsLiteral)


def test_optgrammar::unitsliteral_constructor_exists():
    assert callable(optGrammar::UnitsLiteral.__init__)


def test_optgrammar::unitsliteral_constructor_args():
    sig = inspect.signature(optGrammar::UnitsLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_optgrammar::unitsliteral_has_value():
    assert hasattr(optGrammar::UnitsLiteral, "value")
    descriptor = None
    for klass in optGrammar::UnitsLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::timeunitsliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar::TimeUnitsLiteral)


def test_optgrammar::timeunitsliteral_constructor_exists():
    assert callable(optGrammar::TimeUnitsLiteral.__init__)


def test_optgrammar::timeunitsliteral_constructor_args():
    sig = inspect.signature(optGrammar::TimeUnitsLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_optgrammar::timeunitsliteral_has_value():
    assert hasattr(optGrammar::TimeUnitsLiteral, "value")
    descriptor = None
    for klass in optGrammar::TimeUnitsLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::intliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar::IntLiteral)


def test_optgrammar::intliteral_constructor_exists():
    assert callable(optGrammar::IntLiteral.__init__)


def test_optgrammar::intliteral_constructor_args():
    sig = inspect.signature(optGrammar::IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_optgrammar::intliteral_has_value():
    assert hasattr(optGrammar::IntLiteral, "value")
    descriptor = None
    for klass in optGrammar::IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::unittypes_is_not_abstract():
    assert not inspect.isabstract(optGrammar::UnitTypes)


def test_optgrammar::unittypes_constructor_exists():
    assert callable(optGrammar::UnitTypes.__init__)


def test_optgrammar::unittypes_constructor_args():
    sig = inspect.signature(optGrammar::UnitTypes.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::decimalliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar::DecimalLiteral)


def test_optgrammar::decimalliteral_constructor_exists():
    assert callable(optGrammar::DecimalLiteral.__init__)


def test_optgrammar::decimalliteral_constructor_args():
    sig = inspect.signature(optGrammar::DecimalLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_optgrammar::decimalliteral_has_value():
    assert hasattr(optGrammar::DecimalLiteral, "value")
    descriptor = None
    for klass in optGrammar::DecimalLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::hexliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar::HexLiteral)


def test_optgrammar::hexliteral_constructor_exists():
    assert callable(optGrammar::HexLiteral.__init__)


def test_optgrammar::hexliteral_constructor_args():
    sig = inspect.signature(optGrammar::HexLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_optgrammar::hexliteral_has_value():
    assert hasattr(optGrammar::HexLiteral, "value")
    descriptor = None
    for klass in optGrammar::HexLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::secondoperators_is_not_abstract():
    assert not inspect.isabstract(optGrammar::SecondOperators)


def test_optgrammar::secondoperators_constructor_exists():
    assert callable(optGrammar::SecondOperators.__init__)


def test_optgrammar::secondoperators_constructor_args():
    sig = inspect.signature(optGrammar::SecondOperators.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_optgrammar::secondoperators_has_operator():
    assert hasattr(optGrammar::SecondOperators, "operator")
    descriptor = None
    for klass in optGrammar::SecondOperators.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::primaryarithmetic_is_not_abstract():
    assert not inspect.isabstract(optGrammar::PrimaryArithmetic)


def test_optgrammar::primaryarithmetic_constructor_exists():
    assert callable(optGrammar::PrimaryArithmetic.__init__)


def test_optgrammar::primaryarithmetic_constructor_args():
    sig = inspect.signature(optGrammar::PrimaryArithmetic.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::arithmeticoperations_is_not_abstract():
    assert not inspect.isabstract(optGrammar::ArithmeticOperations)


def test_optgrammar::arithmeticoperations_constructor_exists():
    assert callable(optGrammar::ArithmeticOperations.__init__)


def test_optgrammar::arithmeticoperations_constructor_args():
    sig = inspect.signature(optGrammar::ArithmeticOperations.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::intparameter_is_not_abstract():
    assert not inspect.isabstract(optGrammar::IntParameter)


def test_optgrammar::intparameter_constructor_exists():
    assert callable(optGrammar::IntParameter.__init__)


def test_optgrammar::intparameter_constructor_args():
    sig = inspect.signature(optGrammar::IntParameter.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::ecrecoverfunction_is_not_abstract():
    assert not inspect.isabstract(optGrammar::EcrecoverFunction)


def test_optgrammar::ecrecoverfunction_constructor_exists():
    assert callable(optGrammar::EcrecoverFunction.__init__)


def test_optgrammar::ecrecoverfunction_constructor_args():
    sig = inspect.signature(optGrammar::EcrecoverFunction.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_optgrammar::ecrecoverfunction_has_function():
    assert hasattr(optGrammar::EcrecoverFunction, "function")
    descriptor = None
    for klass in optGrammar::EcrecoverFunction.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::specialliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar::SpecialLiteral)


def test_optgrammar::specialliteral_constructor_exists():
    assert callable(optGrammar::SpecialLiteral.__init__)


def test_optgrammar::specialliteral_constructor_args():
    sig = inspect.signature(optGrammar::SpecialLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar::specialliteral_has_name():
    assert hasattr(optGrammar::SpecialLiteral, "name")
    descriptor = None
    for klass in optGrammar::SpecialLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::hashfunction_is_not_abstract():
    assert not inspect.isabstract(optGrammar::HashFunction)


def test_optgrammar::hashfunction_constructor_exists():
    assert callable(optGrammar::HashFunction.__init__)


def test_optgrammar::hashfunction_constructor_args():
    sig = inspect.signature(optGrammar::HashFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar::hashfunction_has_name():
    assert hasattr(optGrammar::HashFunction, "name")
    descriptor = None
    for klass in optGrammar::HashFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::stringliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar::StringLiteral)


def test_optgrammar::stringliteral_constructor_exists():
    assert callable(optGrammar::StringLiteral.__init__)


def test_optgrammar::stringliteral_constructor_args():
    sig = inspect.signature(optGrammar::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_optgrammar::stringliteral_has_value():
    assert hasattr(optGrammar::StringLiteral, "value")
    descriptor = None
    for klass in optGrammar::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::gasleftfunction_is_not_abstract():
    assert not inspect.isabstract(optGrammar::GasleftFunction)


def test_optgrammar::gasleftfunction_constructor_exists():
    assert callable(optGrammar::GasleftFunction.__init__)


def test_optgrammar::gasleftfunction_constructor_args():
    sig = inspect.signature(optGrammar::GasleftFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar::gasleftfunction_has_name():
    assert hasattr(optGrammar::GasleftFunction, "name")
    descriptor = None
    for klass in optGrammar::GasleftFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::mathematicalfunction_is_not_abstract():
    assert not inspect.isabstract(optGrammar::MathematicalFunction)


def test_optgrammar::mathematicalfunction_constructor_exists():
    assert callable(optGrammar::MathematicalFunction.__init__)


def test_optgrammar::mathematicalfunction_constructor_args():
    sig = inspect.signature(optGrammar::MathematicalFunction.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_optgrammar::mathematicalfunction_has_function():
    assert hasattr(optGrammar::MathematicalFunction, "function")
    descriptor = None
    for klass in optGrammar::MathematicalFunction.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar::BooleanLiteral)


def test_optgrammar::booleanliteral_constructor_exists():
    assert callable(optGrammar::BooleanLiteral.__init__)


def test_optgrammar::booleanliteral_constructor_args():
    sig = inspect.signature(optGrammar::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_optgrammar::booleanliteral_has_value():
    assert hasattr(optGrammar::BooleanLiteral, "value")
    descriptor = None
    for klass in optGrammar::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::blockhashfunction_is_not_abstract():
    assert not inspect.isabstract(optGrammar::BlockhashFunction)


def test_optgrammar::blockhashfunction_constructor_exists():
    assert callable(optGrammar::BlockhashFunction.__init__)


def test_optgrammar::blockhashfunction_constructor_args():
    sig = inspect.signature(optGrammar::BlockhashFunction.__init__)
    params = list(sig.parameters.keys())



def test_primaryarithmetic_is_not_abstract():
    assert not inspect.isabstract(PrimaryArithmetic)


def test_primaryarithmetic_constructor_exists():
    assert callable(PrimaryArithmetic.__init__)


def test_primaryarithmetic_constructor_args():
    sig = inspect.signature(PrimaryArithmetic.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::numericliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar::NumericLiteral)


def test_optgrammar::numericliteral_constructor_exists():
    assert callable(optGrammar::NumericLiteral.__init__)


def test_optgrammar::numericliteral_constructor_args():
    sig = inspect.signature(optGrammar::NumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_loopstructures_is_not_abstract():
    assert not inspect.isabstract(LoopStructures)


def test_loopstructures_constructor_exists():
    assert callable(LoopStructures.__init__)


def test_loopstructures_constructor_args():
    sig = inspect.signature(LoopStructures.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::ifstatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar::IfStatement)


def test_optgrammar::ifstatement_constructor_exists():
    assert callable(optGrammar::IfStatement.__init__)


def test_optgrammar::ifstatement_constructor_args():
    sig = inspect.signature(optGrammar::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::functioncall_is_not_abstract():
    assert not inspect.isabstract(optGrammar::FunctionCall)


def test_optgrammar::functioncall_constructor_exists():
    assert callable(optGrammar::FunctionCall.__init__)


def test_optgrammar::functioncall_constructor_args():
    sig = inspect.signature(optGrammar::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::statement_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Statement)


def test_optgrammar::statement_constructor_exists():
    assert callable(optGrammar::Statement.__init__)


def test_optgrammar::statement_constructor_args():
    sig = inspect.signature(optGrammar::Statement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::forstatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar::ForStatement)


def test_optgrammar::forstatement_constructor_exists():
    assert callable(optGrammar::ForStatement.__init__)


def test_optgrammar::forstatement_constructor_args():
    sig = inspect.signature(optGrammar::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::whilestatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar::WhileStatement)


def test_optgrammar::whilestatement_constructor_exists():
    assert callable(optGrammar::WhileStatement.__init__)


def test_optgrammar::whilestatement_constructor_args():
    sig = inspect.signature(optGrammar::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_qualifier_is_not_abstract():
    assert not inspect.isabstract(Qualifier)


def test_qualifier_constructor_exists():
    assert callable(Qualifier.__init__)


def test_qualifier_constructor_args():
    sig = inspect.signature(Qualifier.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::arguments_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Arguments)


def test_optgrammar::arguments_constructor_exists():
    assert callable(optGrammar::Arguments.__init__)


def test_optgrammar::arguments_constructor_args():
    sig = inspect.signature(optGrammar::Arguments.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::index_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Index)


def test_optgrammar::index_constructor_exists():
    assert callable(optGrammar::Index.__init__)


def test_optgrammar::index_constructor_args():
    sig = inspect.signature(optGrammar::Index.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::field_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Field)


def test_optgrammar::field_constructor_exists():
    assert callable(optGrammar::Field.__init__)


def test_optgrammar::field_constructor_args():
    sig = inspect.signature(optGrammar::Field.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_optgrammar::field_has_field():
    assert hasattr(optGrammar::Field, "field")
    descriptor = None
    for klass in optGrammar::Field.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::qualifier_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Qualifier)


def test_optgrammar::qualifier_constructor_exists():
    assert callable(optGrammar::Qualifier.__init__)


def test_optgrammar::qualifier_constructor_args():
    sig = inspect.signature(optGrammar::Qualifier.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::returnparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar::ReturnParameterDeclaration)


def test_optgrammar::returnparameterdeclaration_constructor_exists():
    assert callable(optGrammar::ReturnParameterDeclaration.__init__)


def test_optgrammar::returnparameterdeclaration_constructor_args():
    sig = inspect.signature(optGrammar::ReturnParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_simplestatement2_is_not_abstract():
    assert not inspect.isabstract(SimpleStatement2)


def test_simplestatement2_constructor_exists():
    assert callable(SimpleStatement2.__init__)


def test_simplestatement2_constructor_args():
    sig = inspect.signature(SimpleStatement2.__init__)
    params = list(sig.parameters.keys())



def test_simplestatement_is_not_abstract():
    assert not inspect.isabstract(SimpleStatement)


def test_simplestatement_constructor_exists():
    assert callable(SimpleStatement.__init__)


def test_simplestatement_constructor_args():
    sig = inspect.signature(SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::varvariabletuplevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar::VarVariableTupleVariableDeclaration)


def test_optgrammar::varvariabletuplevariabledeclaration_constructor_exists():
    assert callable(optGrammar::VarVariableTupleVariableDeclaration.__init__)


def test_optgrammar::varvariabletuplevariabledeclaration_constructor_args():
    sig = inspect.signature(optGrammar::VarVariableTupleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_optgrammar::varvariabletuplevariabledeclaration_has_semicolon():
    assert hasattr(optGrammar::VarVariableTupleVariableDeclaration, "semicolon")
    descriptor = None
    for klass in optGrammar::VarVariableTupleVariableDeclaration.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::standardvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar::StandardVariableDeclaration)


def test_optgrammar::standardvariabledeclaration_constructor_exists():
    assert callable(optGrammar::StandardVariableDeclaration.__init__)


def test_optgrammar::standardvariabledeclaration_constructor_args():
    sig = inspect.signature(optGrammar::StandardVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_optgrammar::standardvariabledeclaration_has_semicolon():
    assert hasattr(optGrammar::StandardVariableDeclaration, "semicolon")
    descriptor = None
    for klass in optGrammar::StandardVariableDeclaration.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::varvariabletypedeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar::VarVariableTypeDeclaration)


def test_optgrammar::varvariabletypedeclaration_constructor_exists():
    assert callable(optGrammar::VarVariableTypeDeclaration.__init__)


def test_optgrammar::varvariabletypedeclaration_constructor_args():
    sig = inspect.signature(optGrammar::VarVariableTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_optgrammar::varvariabletypedeclaration_has_semicolon():
    assert hasattr(optGrammar::VarVariableTypeDeclaration, "semicolon")
    descriptor = None
    for klass in optGrammar::VarVariableTypeDeclaration.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::standardtypewithoutqualifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(optGrammar::StandardTypeWithoutQualifiedIdentifier)


def test_optgrammar::standardtypewithoutqualifiedidentifier_constructor_exists():
    assert callable(optGrammar::StandardTypeWithoutQualifiedIdentifier.__init__)


def test_optgrammar::standardtypewithoutqualifiedidentifier_constructor_args():
    sig = inspect.signature(optGrammar::StandardTypeWithoutQualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::standardtype_is_not_abstract():
    assert not inspect.isabstract(optGrammar::StandardType)


def test_optgrammar::standardtype_constructor_exists():
    assert callable(optGrammar::StandardType.__init__)


def test_optgrammar::standardtype_constructor_args():
    sig = inspect.signature(optGrammar::StandardType.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::arraytype_is_not_abstract():
    assert not inspect.isabstract(optGrammar::ArrayType)


def test_optgrammar::arraytype_constructor_exists():
    assert callable(optGrammar::ArrayType.__init__)


def test_optgrammar::arraytype_constructor_args():
    sig = inspect.signature(optGrammar::ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_standardtypewithoutqualifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(StandardTypeWithoutQualifiedIdentifier)


def test_standardtypewithoutqualifiedidentifier_constructor_exists():
    assert callable(StandardTypeWithoutQualifiedIdentifier.__init__)


def test_standardtypewithoutqualifiedidentifier_constructor_args():
    sig = inspect.signature(StandardTypeWithoutQualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_standardtype_is_not_abstract():
    assert not inspect.isabstract(StandardType)


def test_standardtype_constructor_exists():
    assert callable(StandardType.__init__)


def test_standardtype_constructor_args():
    sig = inspect.signature(StandardType.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::namedtype_is_not_abstract():
    assert not inspect.isabstract(optGrammar::NamedType)


def test_optgrammar::namedtype_constructor_exists():
    assert callable(optGrammar::NamedType.__init__)


def test_optgrammar::namedtype_constructor_args():
    sig = inspect.signature(optGrammar::NamedType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_optgrammar::namedtype_has_type():
    assert hasattr(optGrammar::NamedType, "type")
    descriptor = None
    for klass in optGrammar::NamedType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::type_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Type)


def test_optgrammar::type_constructor_exists():
    assert callable(optGrammar::Type.__init__)


def test_optgrammar::type_constructor_args():
    sig = inspect.signature(optGrammar::Type.__init__)
    params = list(sig.parameters.keys())
    assert "isVarType" in params, "Missing parameter 'isVarType'"

def test_optgrammar::type_has_isVarType():
    assert hasattr(optGrammar::Type, "isVarType")
    descriptor = None
    for klass in optGrammar::Type.__mro__:
        if "isVarType" in klass.__dict__:
            descriptor = klass.__dict__["isVarType"]
            break
    assert isinstance(descriptor, property)



def test_variabledeclarationoptionalelement_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarationOptionalElement)


def test_variabledeclarationoptionalelement_constructor_exists():
    assert callable(VariableDeclarationOptionalElement.__init__)


def test_variabledeclarationoptionalelement_constructor_args():
    sig = inspect.signature(VariableDeclarationOptionalElement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::indexedspecifer_is_not_abstract():
    assert not inspect.isabstract(optGrammar::IndexedSpecifer)


def test_optgrammar::indexedspecifer_constructor_exists():
    assert callable(optGrammar::IndexedSpecifer.__init__)


def test_optgrammar::indexedspecifer_constructor_args():
    sig = inspect.signature(optGrammar::IndexedSpecifer.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::locationspecifier_is_not_abstract():
    assert not inspect.isabstract(optGrammar::LocationSpecifier)


def test_optgrammar::locationspecifier_constructor_exists():
    assert callable(optGrammar::LocationSpecifier.__init__)


def test_optgrammar::locationspecifier_constructor_args():
    sig = inspect.signature(optGrammar::LocationSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::constantspecifier_is_not_abstract():
    assert not inspect.isabstract(optGrammar::ConstantSpecifier)


def test_optgrammar::constantspecifier_constructor_exists():
    assert callable(optGrammar::ConstantSpecifier.__init__)


def test_optgrammar::constantspecifier_constructor_args():
    sig = inspect.signature(optGrammar::ConstantSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::visibilityspecifier_is_not_abstract():
    assert not inspect.isabstract(optGrammar::VisibilitySpecifier)


def test_optgrammar::visibilityspecifier_constructor_exists():
    assert callable(optGrammar::VisibilitySpecifier.__init__)


def test_optgrammar::visibilityspecifier_constructor_args():
    sig = inspect.signature(optGrammar::VisibilitySpecifier.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::variabledeclarationoptionalelement_is_not_abstract():
    assert not inspect.isabstract(optGrammar::VariableDeclarationOptionalElement)


def test_optgrammar::variabledeclarationoptionalelement_constructor_exists():
    assert callable(optGrammar::VariableDeclarationOptionalElement.__init__)


def test_optgrammar::variabledeclarationoptionalelement_constructor_args():
    sig = inspect.signature(optGrammar::VariableDeclarationOptionalElement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar::ExpressionStatement)


def test_optgrammar::expressionstatement_constructor_exists():
    assert callable(optGrammar::ExpressionStatement.__init__)


def test_optgrammar::expressionstatement_constructor_args():
    sig = inspect.signature(optGrammar::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_optgrammar::expressionstatement_has_semicolon():
    assert hasattr(optGrammar::ExpressionStatement, "semicolon")
    descriptor = None
    for klass in optGrammar::ExpressionStatement.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::simplestatement2_is_not_abstract():
    assert not inspect.isabstract(optGrammar::SimpleStatement2)


def test_optgrammar::simplestatement2_constructor_exists():
    assert callable(optGrammar::SimpleStatement2.__init__)


def test_optgrammar::simplestatement2_constructor_args():
    sig = inspect.signature(optGrammar::SimpleStatement2.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::breakstatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar::BreakStatement)


def test_optgrammar::breakstatement_constructor_exists():
    assert callable(optGrammar::BreakStatement.__init__)


def test_optgrammar::breakstatement_constructor_args():
    sig = inspect.signature(optGrammar::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::continuestatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar::ContinueStatement)


def test_optgrammar::continuestatement_constructor_exists():
    assert callable(optGrammar::ContinueStatement.__init__)


def test_optgrammar::continuestatement_constructor_args():
    sig = inspect.signature(optGrammar::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::returnstatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar::ReturnStatement)


def test_optgrammar::returnstatement_constructor_exists():
    assert callable(optGrammar::ReturnStatement.__init__)


def test_optgrammar::returnstatement_constructor_args():
    sig = inspect.signature(optGrammar::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::placeholderstatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar::PlaceHolderStatement)


def test_optgrammar::placeholderstatement_constructor_exists():
    assert callable(optGrammar::PlaceHolderStatement.__init__)


def test_optgrammar::placeholderstatement_constructor_args():
    sig = inspect.signature(optGrammar::PlaceHolderStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::emitstatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar::EmitStatement)


def test_optgrammar::emitstatement_constructor_exists():
    assert callable(optGrammar::EmitStatement.__init__)


def test_optgrammar::emitstatement_constructor_args():
    sig = inspect.signature(optGrammar::EmitStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::loopstructures_is_not_abstract():
    assert not inspect.isabstract(optGrammar::LoopStructures)


def test_optgrammar::loopstructures_constructor_exists():
    assert callable(optGrammar::LoopStructures.__init__)


def test_optgrammar::loopstructures_constructor_args():
    sig = inspect.signature(optGrammar::LoopStructures.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_optgrammar::loopstructures_has_type():
    assert hasattr(optGrammar::LoopStructures, "type")
    descriptor = None
    for klass in optGrammar::LoopStructures.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::deletestatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar::DeleteStatement)


def test_optgrammar::deletestatement_constructor_exists():
    assert callable(optGrammar::DeleteStatement.__init__)


def test_optgrammar::deletestatement_constructor_args():
    sig = inspect.signature(optGrammar::DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::throwstatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar::ThrowStatement)


def test_optgrammar::throwstatement_constructor_exists():
    assert callable(optGrammar::ThrowStatement.__init__)


def test_optgrammar::throwstatement_constructor_args():
    sig = inspect.signature(optGrammar::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::dowhilestatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar::DoWhileStatement)


def test_optgrammar::dowhilestatement_constructor_exists():
    assert callable(optGrammar::DoWhileStatement.__init__)


def test_optgrammar::dowhilestatement_constructor_args():
    sig = inspect.signature(optGrammar::DoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::simplestatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar::SimpleStatement)


def test_optgrammar::simplestatement_constructor_exists():
    assert callable(optGrammar::SimpleStatement.__init__)


def test_optgrammar::simplestatement_constructor_args():
    sig = inspect.signature(optGrammar::SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::assignment_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Assignment)


def test_optgrammar::assignment_constructor_exists():
    assert callable(optGrammar::Assignment.__init__)


def test_optgrammar::assignment_constructor_args():
    sig = inspect.signature(optGrammar::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "assignmentOp" in params, "Missing parameter 'assignmentOp'"

def test_optgrammar::assignment_has_assignmentOp():
    assert hasattr(optGrammar::Assignment, "assignmentOp")
    descriptor = None
    for klass in optGrammar::Assignment.__mro__:
        if "assignmentOp" in klass.__dict__:
            descriptor = klass.__dict__["assignmentOp"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::postincdecexpression_is_not_abstract():
    assert not inspect.isabstract(optGrammar::PostIncDecExpression)


def test_optgrammar::postincdecexpression_constructor_exists():
    assert callable(optGrammar::PostIncDecExpression.__init__)


def test_optgrammar::postincdecexpression_constructor_args():
    sig = inspect.signature(optGrammar::PostIncDecExpression.__init__)
    params = list(sig.parameters.keys())
    assert "postOp" in params, "Missing parameter 'postOp'"

def test_optgrammar::postincdecexpression_has_postOp():
    assert hasattr(optGrammar::PostIncDecExpression, "postOp")
    descriptor = None
    for klass in optGrammar::PostIncDecExpression.__mro__:
        if "postOp" in klass.__dict__:
            descriptor = klass.__dict__["postOp"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::literal_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Literal)


def test_optgrammar::literal_constructor_exists():
    assert callable(optGrammar::Literal.__init__)


def test_optgrammar::literal_constructor_args():
    sig = inspect.signature(optGrammar::Literal.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::or_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Or)


def test_optgrammar::or_constructor_exists():
    assert callable(optGrammar::Or.__init__)


def test_optgrammar::or_constructor_args():
    sig = inspect.signature(optGrammar::Or.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::exponent_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Exponent)


def test_optgrammar::exponent_constructor_exists():
    assert callable(optGrammar::Exponent.__init__)


def test_optgrammar::exponent_constructor_args():
    sig = inspect.signature(optGrammar::Exponent.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::qualifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(optGrammar::QualifiedIdentifier)


def test_optgrammar::qualifiedidentifier_constructor_exists():
    assert callable(optGrammar::QualifiedIdentifier.__init__)


def test_optgrammar::qualifiedidentifier_constructor_args():
    sig = inspect.signature(optGrammar::QualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_optgrammar::qualifiedidentifier_has_identifier():
    assert hasattr(optGrammar::QualifiedIdentifier, "identifier")
    descriptor = None
    for klass in optGrammar::QualifiedIdentifier.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::muldivmod_is_not_abstract():
    assert not inspect.isabstract(optGrammar::MulDivMod)


def test_optgrammar::muldivmod_constructor_exists():
    assert callable(optGrammar::MulDivMod.__init__)


def test_optgrammar::muldivmod_constructor_args():
    sig = inspect.signature(optGrammar::MulDivMod.__init__)
    params = list(sig.parameters.keys())
    assert "multipliciativeOp" in params, "Missing parameter 'multipliciativeOp'"

def test_optgrammar::muldivmod_has_multipliciativeOp():
    assert hasattr(optGrammar::MulDivMod, "multipliciativeOp")
    descriptor = None
    for klass in optGrammar::MulDivMod.__mro__:
        if "multipliciativeOp" in klass.__dict__:
            descriptor = klass.__dict__["multipliciativeOp"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::comparison_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Comparison)


def test_optgrammar::comparison_constructor_exists():
    assert callable(optGrammar::Comparison.__init__)


def test_optgrammar::comparison_constructor_args():
    sig = inspect.signature(optGrammar::Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "comparisonOp" in params, "Missing parameter 'comparisonOp'"

def test_optgrammar::comparison_has_comparisonOp():
    assert hasattr(optGrammar::Comparison, "comparisonOp")
    descriptor = None
    for klass in optGrammar::Comparison.__mro__:
        if "comparisonOp" in klass.__dict__:
            descriptor = klass.__dict__["comparisonOp"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::specialexpression_is_not_abstract():
    assert not inspect.isabstract(optGrammar::SpecialExpression)


def test_optgrammar::specialexpression_constructor_exists():
    assert callable(optGrammar::SpecialExpression.__init__)


def test_optgrammar::specialexpression_constructor_args():
    sig = inspect.signature(optGrammar::SpecialExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_optgrammar::specialexpression_has_type():
    assert hasattr(optGrammar::SpecialExpression, "type")
    descriptor = None
    for klass in optGrammar::SpecialExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::typecast_is_not_abstract():
    assert not inspect.isabstract(optGrammar::TypeCast)


def test_optgrammar::typecast_constructor_exists():
    assert callable(optGrammar::TypeCast.__init__)


def test_optgrammar::typecast_constructor_args():
    sig = inspect.signature(optGrammar::TypeCast.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::preincexpression_is_not_abstract():
    assert not inspect.isabstract(optGrammar::PreIncExpression)


def test_optgrammar::preincexpression_constructor_exists():
    assert callable(optGrammar::PreIncExpression.__init__)


def test_optgrammar::preincexpression_constructor_args():
    sig = inspect.signature(optGrammar::PreIncExpression.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::predecexpression_is_not_abstract():
    assert not inspect.isabstract(optGrammar::PreDecExpression)


def test_optgrammar::predecexpression_constructor_exists():
    assert callable(optGrammar::PreDecExpression.__init__)


def test_optgrammar::predecexpression_constructor_args():
    sig = inspect.signature(optGrammar::PreDecExpression.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::bitand_is_not_abstract():
    assert not inspect.isabstract(optGrammar::BitAnd)


def test_optgrammar::bitand_constructor_exists():
    assert callable(optGrammar::BitAnd.__init__)


def test_optgrammar::bitand_constructor_args():
    sig = inspect.signature(optGrammar::BitAnd.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::binarynotexpression_is_not_abstract():
    assert not inspect.isabstract(optGrammar::BinaryNotExpression)


def test_optgrammar::binarynotexpression_constructor_exists():
    assert callable(optGrammar::BinaryNotExpression.__init__)


def test_optgrammar::binarynotexpression_constructor_args():
    sig = inspect.signature(optGrammar::BinaryNotExpression.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(optGrammar::VariableDeclarationExpression)


def test_optgrammar::variabledeclarationexpression_constructor_exists():
    assert callable(optGrammar::VariableDeclarationExpression.__init__)


def test_optgrammar::variabledeclarationexpression_constructor_args():
    sig = inspect.signature(optGrammar::VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::addsub_is_not_abstract():
    assert not inspect.isabstract(optGrammar::AddSub)


def test_optgrammar::addsub_constructor_exists():
    assert callable(optGrammar::AddSub.__init__)


def test_optgrammar::addsub_constructor_args():
    sig = inspect.signature(optGrammar::AddSub.__init__)
    params = list(sig.parameters.keys())
    assert "additionOp" in params, "Missing parameter 'additionOp'"

def test_optgrammar::addsub_has_additionOp():
    assert hasattr(optGrammar::AddSub, "additionOp")
    descriptor = None
    for klass in optGrammar::AddSub.__mro__:
        if "additionOp" in klass.__dict__:
            descriptor = klass.__dict__["additionOp"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::tupleseparator_is_not_abstract():
    assert not inspect.isabstract(optGrammar::TupleSeparator)


def test_optgrammar::tupleseparator_constructor_exists():
    assert callable(optGrammar::TupleSeparator.__init__)


def test_optgrammar::tupleseparator_constructor_args():
    sig = inspect.signature(optGrammar::TupleSeparator.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::newexpression_is_not_abstract():
    assert not inspect.isabstract(optGrammar::NewExpression)


def test_optgrammar::newexpression_constructor_exists():
    assert callable(optGrammar::NewExpression.__init__)


def test_optgrammar::newexpression_constructor_args():
    sig = inspect.signature(optGrammar::NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::signexpression_is_not_abstract():
    assert not inspect.isabstract(optGrammar::SignExpression)


def test_optgrammar::signexpression_constructor_exists():
    assert callable(optGrammar::SignExpression.__init__)


def test_optgrammar::signexpression_constructor_args():
    sig = inspect.signature(optGrammar::SignExpression.__init__)
    params = list(sig.parameters.keys())
    assert "signOp" in params, "Missing parameter 'signOp'"

def test_optgrammar::signexpression_has_signOp():
    assert hasattr(optGrammar::SignExpression, "signOp")
    descriptor = None
    for klass in optGrammar::SignExpression.__mro__:
        if "signOp" in klass.__dict__:
            descriptor = klass.__dict__["signOp"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::shift_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Shift)


def test_optgrammar::shift_constructor_exists():
    assert callable(optGrammar::Shift.__init__)


def test_optgrammar::shift_constructor_args():
    sig = inspect.signature(optGrammar::Shift.__init__)
    params = list(sig.parameters.keys())
    assert "shiftOp" in params, "Missing parameter 'shiftOp'"

def test_optgrammar::shift_has_shiftOp():
    assert hasattr(optGrammar::Shift, "shiftOp")
    descriptor = None
    for klass in optGrammar::Shift.__mro__:
        if "shiftOp" in klass.__dict__:
            descriptor = klass.__dict__["shiftOp"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::bitor_is_not_abstract():
    assert not inspect.isabstract(optGrammar::BitOr)


def test_optgrammar::bitor_constructor_exists():
    assert callable(optGrammar::BitOr.__init__)


def test_optgrammar::bitor_constructor_args():
    sig = inspect.signature(optGrammar::BitOr.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::and_is_not_abstract():
    assert not inspect.isabstract(optGrammar::And)


def test_optgrammar::and_constructor_exists():
    assert callable(optGrammar::And.__init__)


def test_optgrammar::and_constructor_args():
    sig = inspect.signature(optGrammar::And.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::bitxor_is_not_abstract():
    assert not inspect.isabstract(optGrammar::BitXor)


def test_optgrammar::bitxor_constructor_exists():
    assert callable(optGrammar::BitXor.__init__)


def test_optgrammar::bitxor_constructor_args():
    sig = inspect.signature(optGrammar::BitXor.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::notexpression_is_not_abstract():
    assert not inspect.isabstract(optGrammar::NotExpression)


def test_optgrammar::notexpression_constructor_exists():
    assert callable(optGrammar::NotExpression.__init__)


def test_optgrammar::notexpression_constructor_args():
    sig = inspect.signature(optGrammar::NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::equality_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Equality)


def test_optgrammar::equality_constructor_exists():
    assert callable(optGrammar::Equality.__init__)


def test_optgrammar::equality_constructor_args():
    sig = inspect.signature(optGrammar::Equality.__init__)
    params = list(sig.parameters.keys())
    assert "equalityOp" in params, "Missing parameter 'equalityOp'"

def test_optgrammar::equality_has_equalityOp():
    assert hasattr(optGrammar::Equality, "equalityOp")
    descriptor = None
    for klass in optGrammar::Equality.__mro__:
        if "equalityOp" in klass.__dict__:
            descriptor = klass.__dict__["equalityOp"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::tuple_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Tuple)


def test_optgrammar::tuple_constructor_exists():
    assert callable(optGrammar::Tuple.__init__)


def test_optgrammar::tuple_constructor_args():
    sig = inspect.signature(optGrammar::Tuple.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::mapping_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Mapping)


def test_optgrammar::mapping_constructor_exists():
    assert callable(optGrammar::Mapping.__init__)


def test_optgrammar::mapping_constructor_args():
    sig = inspect.signature(optGrammar::Mapping.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::variable_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Variable)


def test_optgrammar::variable_constructor_exists():
    assert callable(optGrammar::Variable.__init__)


def test_optgrammar::variable_constructor_args():
    sig = inspect.signature(optGrammar::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar::variable_has_name():
    assert hasattr(optGrammar::Variable, "name")
    descriptor = None
    for klass in optGrammar::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::enumvalue_is_not_abstract():
    assert not inspect.isabstract(optGrammar::EnumValue)


def test_optgrammar::enumvalue_constructor_exists():
    assert callable(optGrammar::EnumValue.__init__)


def test_optgrammar::enumvalue_constructor_args():
    sig = inspect.signature(optGrammar::EnumValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar::enumvalue_has_name():
    assert hasattr(optGrammar::EnumValue, "name")
    descriptor = None
    for klass in optGrammar::EnumValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::returnsparameterlist_is_not_abstract():
    assert not inspect.isabstract(optGrammar::ReturnsParameterList)


def test_optgrammar::returnsparameterlist_constructor_exists():
    assert callable(optGrammar::ReturnsParameterList.__init__)


def test_optgrammar::returnsparameterlist_constructor_args():
    sig = inspect.signature(optGrammar::ReturnsParameterList.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::sizeddeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar::SizedDeclaration)


def test_optgrammar::sizeddeclaration_constructor_exists():
    assert callable(optGrammar::SizedDeclaration.__init__)


def test_optgrammar::sizeddeclaration_constructor_args():
    sig = inspect.signature(optGrammar::SizedDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::simpletypedeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar::SimpleTypeDeclaration)


def test_optgrammar::simpletypedeclaration_constructor_exists():
    assert callable(optGrammar::SimpleTypeDeclaration.__init__)


def test_optgrammar::simpletypedeclaration_constructor_args():
    sig = inspect.signature(optGrammar::SimpleTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::locationliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar::LocationLiteral)


def test_optgrammar::locationliteral_constructor_exists():
    assert callable(optGrammar::LocationLiteral.__init__)


def test_optgrammar::locationliteral_constructor_args():
    sig = inspect.signature(optGrammar::LocationLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_optgrammar::locationliteral_has_type():
    assert hasattr(optGrammar::LocationLiteral, "type")
    descriptor = None
    for klass in optGrammar::LocationLiteral.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_primarytypedeclaration_is_not_abstract():
    assert not inspect.isabstract(PrimaryTypeDeclaration)


def test_primarytypedeclaration_constructor_exists():
    assert callable(PrimaryTypeDeclaration.__init__)


def test_primarytypedeclaration_constructor_args():
    sig = inspect.signature(PrimaryTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::arrayabledeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar::ArrayableDeclaration)


def test_optgrammar::arrayabledeclaration_constructor_exists():
    assert callable(optGrammar::ArrayableDeclaration.__init__)


def test_optgrammar::arrayabledeclaration_constructor_args():
    sig = inspect.signature(optGrammar::ArrayableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::nonarrayabledeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar::NonArrayableDeclaration)


def test_optgrammar::nonarrayabledeclaration_constructor_exists():
    assert callable(optGrammar::NonArrayableDeclaration.__init__)


def test_optgrammar::nonarrayabledeclaration_constructor_args():
    sig = inspect.signature(optGrammar::NonArrayableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_primarytypedefinitiondeclaration_is_not_abstract():
    assert not inspect.isabstract(PrimaryTypeDefinitionDeclaration)


def test_primarytypedefinitiondeclaration_constructor_exists():
    assert callable(PrimaryTypeDefinitionDeclaration.__init__)


def test_primarytypedefinitiondeclaration_constructor_args():
    sig = inspect.signature(PrimaryTypeDefinitionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::primarytypedeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar::PrimaryTypeDeclaration)


def test_optgrammar::primarytypedeclaration_constructor_exists():
    assert callable(optGrammar::PrimaryTypeDeclaration.__init__)


def test_optgrammar::primarytypedeclaration_constructor_args():
    sig = inspect.signature(optGrammar::PrimaryTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar::primarytypedeclaration_has_constant():
    assert hasattr(optGrammar::PrimaryTypeDeclaration, "constant")
    descriptor = None
    for klass in optGrammar::PrimaryTypeDeclaration.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)

def test_optgrammar::primarytypedeclaration_has_name():
    assert hasattr(optGrammar::PrimaryTypeDeclaration, "name")
    descriptor = None
    for klass in optGrammar::PrimaryTypeDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::functioncallarg_is_not_abstract():
    assert not inspect.isabstract(optGrammar::FunctionCallArg)


def test_optgrammar::functioncallarg_constructor_exists():
    assert callable(optGrammar::FunctionCallArg.__init__)


def test_optgrammar::functioncallarg_constructor_args():
    sig = inspect.signature(optGrammar::FunctionCallArg.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar::functioncallarg_has_name():
    assert hasattr(optGrammar::FunctionCallArg, "name")
    descriptor = None
    for klass in optGrammar::FunctionCallArg.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::functioncallarguments_is_not_abstract():
    assert not inspect.isabstract(optGrammar::FunctionCallArguments)


def test_optgrammar::functioncallarguments_constructor_exists():
    assert callable(optGrammar::FunctionCallArguments.__init__)


def test_optgrammar::functioncallarguments_constructor_args():
    sig = inspect.signature(optGrammar::FunctionCallArguments.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::expression_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Expression)


def test_optgrammar::expression_constructor_exists():
    assert callable(optGrammar::Expression.__init__)


def test_optgrammar::expression_constructor_args():
    sig = inspect.signature(optGrammar::Expression.__init__)
    params = list(sig.parameters.keys())



def test_functioncallarguments_is_not_abstract():
    assert not inspect.isabstract(FunctionCallArguments)


def test_functioncallarguments_constructor_exists():
    assert callable(FunctionCallArguments.__init__)


def test_functioncallarguments_constructor_args():
    sig = inspect.signature(FunctionCallArguments.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::functioncalllistarguments_is_not_abstract():
    assert not inspect.isabstract(optGrammar::FunctionCallListArguments)


def test_optgrammar::functioncalllistarguments_constructor_exists():
    assert callable(optGrammar::FunctionCallListArguments.__init__)


def test_optgrammar::functioncalllistarguments_constructor_args():
    sig = inspect.signature(optGrammar::FunctionCallListArguments.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::body_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Body)


def test_optgrammar::body_constructor_exists():
    assert callable(optGrammar::Body.__init__)


def test_optgrammar::body_constructor_args():
    sig = inspect.signature(optGrammar::Body.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::visibilityliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar::VisibilityLiteral)


def test_optgrammar::visibilityliteral_constructor_exists():
    assert callable(optGrammar::VisibilityLiteral.__init__)


def test_optgrammar::visibilityliteral_constructor_args():
    sig = inspect.signature(optGrammar::VisibilityLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_optgrammar::visibilityliteral_has_type():
    assert hasattr(optGrammar::VisibilityLiteral, "type")
    descriptor = None
    for klass in optGrammar::VisibilityLiteral.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::inheritancespecifier_is_not_abstract():
    assert not inspect.isabstract(optGrammar::InheritanceSpecifier)


def test_optgrammar::inheritancespecifier_constructor_exists():
    assert callable(optGrammar::InheritanceSpecifier.__init__)


def test_optgrammar::inheritancespecifier_constructor_args():
    sig = inspect.signature(optGrammar::InheritanceSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::symbolalias_is_not_abstract():
    assert not inspect.isabstract(optGrammar::SymbolAlias)


def test_optgrammar::symbolalias_constructor_exists():
    assert callable(optGrammar::SymbolAlias.__init__)


def test_optgrammar::symbolalias_constructor_args():
    sig = inspect.signature(optGrammar::SymbolAlias.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_optgrammar::symbolalias_has_symbol():
    assert hasattr(optGrammar::SymbolAlias, "symbol")
    descriptor = None
    for klass in optGrammar::SymbolAlias.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_optgrammar::symbolalias_has_alias():
    assert hasattr(optGrammar::SymbolAlias, "alias")
    descriptor = None
    for klass in optGrammar::SymbolAlias.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::versionoperator_is_not_abstract():
    assert not inspect.isabstract(optGrammar::versionOperator)


def test_optgrammar::versionoperator_constructor_exists():
    assert callable(optGrammar::versionOperator.__init__)


def test_optgrammar::versionoperator_constructor_args():
    sig = inspect.signature(optGrammar::versionOperator.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_optgrammar::versionoperator_has_value():
    assert hasattr(optGrammar::versionOperator, "value")
    descriptor = None
    for klass in optGrammar::versionOperator.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::contract_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Contract)


def test_optgrammar::contract_constructor_exists():
    assert callable(optGrammar::Contract.__init__)


def test_optgrammar::contract_constructor_args():
    sig = inspect.signature(optGrammar::Contract.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar::contract_has_name():
    assert hasattr(optGrammar::Contract, "name")
    descriptor = None
    for klass in optGrammar::Contract.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::importdirective_is_not_abstract():
    assert not inspect.isabstract(optGrammar::ImportDirective)


def test_optgrammar::importdirective_constructor_exists():
    assert callable(optGrammar::ImportDirective.__init__)


def test_optgrammar::importdirective_constructor_args():
    sig = inspect.signature(optGrammar::ImportDirective.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"
    assert "unitAlias" in params, "Missing parameter 'unitAlias'"

def test_optgrammar::importdirective_has_importURI():
    assert hasattr(optGrammar::ImportDirective, "importURI")
    descriptor = None
    for klass in optGrammar::ImportDirective.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)

def test_optgrammar::importdirective_has_unitAlias():
    assert hasattr(optGrammar::ImportDirective, "unitAlias")
    descriptor = None
    for klass in optGrammar::ImportDirective.__mro__:
        if "unitAlias" in klass.__dict__:
            descriptor = klass.__dict__["unitAlias"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::modifierinvocation_is_not_abstract():
    assert not inspect.isabstract(optGrammar::ModifierInvocation)


def test_optgrammar::modifierinvocation_constructor_exists():
    assert callable(optGrammar::ModifierInvocation.__init__)


def test_optgrammar::modifierinvocation_constructor_args():
    sig = inspect.signature(optGrammar::ModifierInvocation.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::const_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Const)


def test_optgrammar::const_constructor_exists():
    assert callable(optGrammar::Const.__init__)


def test_optgrammar::const_constructor_args():
    sig = inspect.signature(optGrammar::Const.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::statemutability_is_not_abstract():
    assert not inspect.isabstract(optGrammar::StateMutability)


def test_optgrammar::statemutability_constructor_exists():
    assert callable(optGrammar::StateMutability.__init__)


def test_optgrammar::statemutability_constructor_args():
    sig = inspect.signature(optGrammar::StateMutability.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_optgrammar::statemutability_has_type():
    assert hasattr(optGrammar::StateMutability, "type")
    descriptor = None
    for klass in optGrammar::StateMutability.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::parameterlist_is_not_abstract():
    assert not inspect.isabstract(optGrammar::ParameterList)


def test_optgrammar::parameterlist_constructor_exists():
    assert callable(optGrammar::ParameterList.__init__)


def test_optgrammar::parameterlist_constructor_args():
    sig = inspect.signature(optGrammar::ParameterList.__init__)
    params = list(sig.parameters.keys())



def test_definitionbody_is_not_abstract():
    assert not inspect.isabstract(DefinitionBody)


def test_definitionbody_constructor_exists():
    assert callable(DefinitionBody.__init__)


def test_definitionbody_constructor_args():
    sig = inspect.signature(DefinitionBody.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::functiondefinition_is_not_abstract():
    assert not inspect.isabstract(optGrammar::FunctionDefinition)


def test_optgrammar::functiondefinition_constructor_exists():
    assert callable(optGrammar::FunctionDefinition.__init__)


def test_optgrammar::functiondefinition_constructor_args():
    sig = inspect.signature(optGrammar::FunctionDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar::functiondefinition_has_name():
    assert hasattr(optGrammar::FunctionDefinition, "name")
    descriptor = None
    for klass in optGrammar::FunctionDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::event_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Event)


def test_optgrammar::event_constructor_exists():
    assert callable(optGrammar::Event.__init__)


def test_optgrammar::event_constructor_args():
    sig = inspect.signature(optGrammar::Event.__init__)
    params = list(sig.parameters.keys())
    assert "isAnonymous" in params, "Missing parameter 'isAnonymous'"
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar::event_has_isAnonymous():
    assert hasattr(optGrammar::Event, "isAnonymous")
    descriptor = None
    for klass in optGrammar::Event.__mro__:
        if "isAnonymous" in klass.__dict__:
            descriptor = klass.__dict__["isAnonymous"]
            break
    assert isinstance(descriptor, property)

def test_optgrammar::event_has_name():
    assert hasattr(optGrammar::Event, "name")
    descriptor = None
    for klass in optGrammar::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::primarytypedefinitiondeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar::PrimaryTypeDefinitionDeclaration)


def test_optgrammar::primarytypedefinitiondeclaration_constructor_exists():
    assert callable(optGrammar::PrimaryTypeDefinitionDeclaration.__init__)


def test_optgrammar::primarytypedefinitiondeclaration_constructor_args():
    sig = inspect.signature(optGrammar::PrimaryTypeDefinitionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::modifier_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Modifier)


def test_optgrammar::modifier_constructor_exists():
    assert callable(optGrammar::Modifier.__init__)


def test_optgrammar::modifier_constructor_args():
    sig = inspect.signature(optGrammar::Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar::modifier_has_name():
    assert hasattr(optGrammar::Modifier, "name")
    descriptor = None
    for klass in optGrammar::Modifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::enumdefinition_is_not_abstract():
    assert not inspect.isabstract(optGrammar::EnumDefinition)


def test_optgrammar::enumdefinition_constructor_exists():
    assert callable(optGrammar::EnumDefinition.__init__)


def test_optgrammar::enumdefinition_constructor_args():
    sig = inspect.signature(optGrammar::EnumDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar::enumdefinition_has_name():
    assert hasattr(optGrammar::EnumDefinition, "name")
    descriptor = None
    for klass in optGrammar::EnumDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::structdefinition_is_not_abstract():
    assert not inspect.isabstract(optGrammar::StructDefinition)


def test_optgrammar::structdefinition_constructor_exists():
    assert callable(optGrammar::StructDefinition.__init__)


def test_optgrammar::structdefinition_constructor_args():
    sig = inspect.signature(optGrammar::StructDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar::structdefinition_has_name():
    assert hasattr(optGrammar::StructDefinition, "name")
    descriptor = None
    for klass in optGrammar::StructDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::constructordefinition_is_not_abstract():
    assert not inspect.isabstract(optGrammar::ConstructorDefinition)


def test_optgrammar::constructordefinition_constructor_exists():
    assert callable(optGrammar::ConstructorDefinition.__init__)


def test_optgrammar::constructordefinition_constructor_args():
    sig = inspect.signature(optGrammar::ConstructorDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar::constructordefinition_has_name():
    assert hasattr(optGrammar::ConstructorDefinition, "name")
    descriptor = None
    for klass in optGrammar::ConstructorDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar::definitionbody_is_not_abstract():
    assert not inspect.isabstract(optGrammar::DefinitionBody)


def test_optgrammar::definitionbody_constructor_exists():
    assert callable(optGrammar::DefinitionBody.__init__)


def test_optgrammar::definitionbody_constructor_args():
    sig = inspect.signature(optGrammar::DefinitionBody.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::pragmadirective_is_not_abstract():
    assert not inspect.isabstract(optGrammar::PragmaDirective)


def test_optgrammar::pragmadirective_constructor_exists():
    assert callable(optGrammar::PragmaDirective.__init__)


def test_optgrammar::pragmadirective_constructor_args():
    sig = inspect.signature(optGrammar::PragmaDirective.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar::model_is_not_abstract():
    assert not inspect.isabstract(optGrammar::Model)


def test_optgrammar::model_constructor_exists():
    assert callable(optGrammar::Model.__init__)


def test_optgrammar::model_constructor_args():
    sig = inspect.signature(optGrammar::Model.__init__)
    params = list(sig.parameters.keys())

def test_reservedwordsenum_exists():
    # Check that the Enumeration exists
    assert ReservedWordsEnum is not None

def test_reservedwordsenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReservedWordsEnum]
    expected_literals = [
        "RELOCATABLE",
        "LET",
        "TYPE",
        "OF",
        "MATCH",
        "TRY",
        "USING",
        "CATCH",
        "CASE",
        "AS",
        "ILLEGAL",
        "TYPEOF",
        "FINAL",
        "SWITCH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReservedWordsEnum"

def test_shiftopenum_exists():
    # Check that the Enumeration exists
    assert ShiftOpEnum is not None

def test_shiftopenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShiftOpEnum]
    expected_literals = [
        "LEFT_SHIFT",
        "ARITHMETIC_RIGHT_SHIFT",
        "RIGHT_SHIFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShiftOpEnum"

def test_comparisonopenum_exists():
    # Check that the Enumeration exists
    assert ComparisonOpEnum is not None

def test_comparisonopenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonOpEnum]
    expected_literals = [
        "LT",
        "LTE",
        "GTE",
        "IN",
        "GT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisonOpEnum"

def test_incdecopenum_exists():
    # Check that the Enumeration exists
    assert IncDecOpEnum is not None

def test_incdecopenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IncDecOpEnum]
    expected_literals = [
        "INC",
        "DEC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IncDecOpEnum"

def test_equalityopenum_exists():
    # Check that the Enumeration exists
    assert EqualityOpEnum is not None

def test_equalityopenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EqualityOpEnum]
    expected_literals = [
        "EQ",
        "NOTEQ",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EqualityOpEnum"

def test_specialexpressiontypeenum_exists():
    # Check that the Enumeration exists
    assert SpecialExpressionTypeEnum is not None

def test_specialexpressiontypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpecialExpressionTypeEnum]
    expected_literals = [
        "THIS",
        "SUPER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpecialExpressionTypeEnum"

def test_muldivmodopenum_exists():
    # Check that the Enumeration exists
    assert MulDivModOpEnum is not None

def test_muldivmodopenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MulDivModOpEnum]
    expected_literals = [
        "MOD",
        "MULT",
        "DIV",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MulDivModOpEnum"

def test_additionopenum_exists():
    # Check that the Enumeration exists
    assert AdditionOpEnum is not None

def test_additionopenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdditionOpEnum]
    expected_literals = [
        "ADD",
        "SUB",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdditionOpEnum"

def test_assignmentopenum_exists():
    # Check that the Enumeration exists
    assert AssignmentOpEnum is not None

def test_assignmentopenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOpEnum]
    expected_literals = [
        "ASSIGN_XOR",
        "ASSIGN_OR",
        "ASSIGN_SUB",
        "ASSIGN_MULT",
        "ASSIGN_MOD",
        "ASSIGN_SHIFT_RIGHT_ARIMETIC",
        "ASSIGN_ADD",
        "ASSIGN_SHIFT_LEFT",
        "ASSIGN_AND",
        "ASSIGN_SHIFT_RIGHT",
        "ASSIGN",
        "ASSIGN_DIV",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOpEnum"


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
ContinueStatement_strategy = st.builds(
    ContinueStatement,
)
optGrammar::Continue_strategy = st.builds(
    optGrammar::Continue,
)
NamedType_strategy = st.builds(
    NamedType,
)
optGrammar::UnitsLiteral_strategy = st.builds(
    optGrammar::UnitsLiteral,
    value=
        safe_text
)
optGrammar::TimeUnitsLiteral_strategy = st.builds(
    optGrammar::TimeUnitsLiteral,
    value=
        safe_text
)
optGrammar::IntLiteral_strategy = st.builds(
    optGrammar::IntLiteral,
    value=
        st.integers()
)
optGrammar::UnitTypes_strategy = st.builds(
    optGrammar::UnitTypes,
)
optGrammar::DecimalLiteral_strategy = st.builds(
    optGrammar::DecimalLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
optGrammar::HexLiteral_strategy = st.builds(
    optGrammar::HexLiteral,
    value=
        safe_text
)
optGrammar::SecondOperators_strategy = st.builds(
    optGrammar::SecondOperators,
    operator=
        safe_text
)
optGrammar::PrimaryArithmetic_strategy = st.builds(
    optGrammar::PrimaryArithmetic,
)
optGrammar::ArithmeticOperations_strategy = st.builds(
    optGrammar::ArithmeticOperations,
)
optGrammar::IntParameter_strategy = st.builds(
    optGrammar::IntParameter,
)
Literal_strategy = st.builds(
    Literal,
)
optGrammar::EcrecoverFunction_strategy = st.builds(
    optGrammar::EcrecoverFunction,
    function=
        safe_text
)
optGrammar::SpecialLiteral_strategy = st.builds(
    optGrammar::SpecialLiteral,
    name=
        safe_text
)
optGrammar::HashFunction_strategy = st.builds(
    optGrammar::HashFunction,
    name=
        safe_text
)
optGrammar::StringLiteral_strategy = st.builds(
    optGrammar::StringLiteral,
    value=
        safe_text
)
optGrammar::GasleftFunction_strategy = st.builds(
    optGrammar::GasleftFunction,
    name=
        safe_text
)
optGrammar::MathematicalFunction_strategy = st.builds(
    optGrammar::MathematicalFunction,
    function=
        safe_text
)
optGrammar::BooleanLiteral_strategy = st.builds(
    optGrammar::BooleanLiteral,
    value=
        safe_text
)
optGrammar::BlockhashFunction_strategy = st.builds(
    optGrammar::BlockhashFunction,
)
PrimaryArithmetic_strategy = st.builds(
    PrimaryArithmetic,
)
optGrammar::NumericLiteral_strategy = st.builds(
    optGrammar::NumericLiteral,
)
LoopStructures_strategy = st.builds(
    LoopStructures,
)
optGrammar::IfStatement_strategy = st.builds(
    optGrammar::IfStatement,
)
optGrammar::FunctionCall_strategy = st.builds(
    optGrammar::FunctionCall,
)
optGrammar::Statement_strategy = st.builds(
    optGrammar::Statement,
)
optGrammar::ForStatement_strategy = st.builds(
    optGrammar::ForStatement,
)
optGrammar::WhileStatement_strategy = st.builds(
    optGrammar::WhileStatement,
)
Qualifier_strategy = st.builds(
    Qualifier,
)
optGrammar::Arguments_strategy = st.builds(
    optGrammar::Arguments,
)
optGrammar::Index_strategy = st.builds(
    optGrammar::Index,
)
optGrammar::Field_strategy = st.builds(
    optGrammar::Field,
    field=
        safe_text
)
optGrammar::Qualifier_strategy = st.builds(
    optGrammar::Qualifier,
)
optGrammar::ReturnParameterDeclaration_strategy = st.builds(
    optGrammar::ReturnParameterDeclaration,
)
SimpleStatement2_strategy = st.builds(
    SimpleStatement2,
)
SimpleStatement_strategy = st.builds(
    SimpleStatement,
)
optGrammar::VarVariableTupleVariableDeclaration_strategy = st.builds(
    optGrammar::VarVariableTupleVariableDeclaration,
    semicolon=
        st.booleans()
)
optGrammar::StandardVariableDeclaration_strategy = st.builds(
    optGrammar::StandardVariableDeclaration,
    semicolon=
        st.booleans()
)
optGrammar::VarVariableTypeDeclaration_strategy = st.builds(
    optGrammar::VarVariableTypeDeclaration,
    semicolon=
        st.booleans()
)
optGrammar::StandardTypeWithoutQualifiedIdentifier_strategy = st.builds(
    optGrammar::StandardTypeWithoutQualifiedIdentifier,
)
Type_strategy = st.builds(
    Type,
)
optGrammar::StandardType_strategy = st.builds(
    optGrammar::StandardType,
)
optGrammar::ArrayType_strategy = st.builds(
    optGrammar::ArrayType,
)
StandardTypeWithoutQualifiedIdentifier_strategy = st.builds(
    StandardTypeWithoutQualifiedIdentifier,
)
StandardType_strategy = st.builds(
    StandardType,
)
optGrammar::NamedType_strategy = st.builds(
    optGrammar::NamedType,
    type=
        safe_text
)
optGrammar::Type_strategy = st.builds(
    optGrammar::Type,
    isVarType=
        st.booleans()
)
VariableDeclarationOptionalElement_strategy = st.builds(
    VariableDeclarationOptionalElement,
)
optGrammar::IndexedSpecifer_strategy = st.builds(
    optGrammar::IndexedSpecifer,
)
optGrammar::LocationSpecifier_strategy = st.builds(
    optGrammar::LocationSpecifier,
)
optGrammar::ConstantSpecifier_strategy = st.builds(
    optGrammar::ConstantSpecifier,
)
optGrammar::VisibilitySpecifier_strategy = st.builds(
    optGrammar::VisibilitySpecifier,
)
optGrammar::VariableDeclarationOptionalElement_strategy = st.builds(
    optGrammar::VariableDeclarationOptionalElement,
)
optGrammar::ExpressionStatement_strategy = st.builds(
    optGrammar::ExpressionStatement,
    semicolon=
        st.booleans()
)
optGrammar::SimpleStatement2_strategy = st.builds(
    optGrammar::SimpleStatement2,
)
Statement_strategy = st.builds(
    Statement,
)
optGrammar::BreakStatement_strategy = st.builds(
    optGrammar::BreakStatement,
)
optGrammar::ContinueStatement_strategy = st.builds(
    optGrammar::ContinueStatement,
)
optGrammar::ReturnStatement_strategy = st.builds(
    optGrammar::ReturnStatement,
)
optGrammar::PlaceHolderStatement_strategy = st.builds(
    optGrammar::PlaceHolderStatement,
)
optGrammar::EmitStatement_strategy = st.builds(
    optGrammar::EmitStatement,
)
optGrammar::LoopStructures_strategy = st.builds(
    optGrammar::LoopStructures,
    type=
        safe_text
)
optGrammar::DeleteStatement_strategy = st.builds(
    optGrammar::DeleteStatement,
)
optGrammar::ThrowStatement_strategy = st.builds(
    optGrammar::ThrowStatement,
)
optGrammar::DoWhileStatement_strategy = st.builds(
    optGrammar::DoWhileStatement,
)
optGrammar::SimpleStatement_strategy = st.builds(
    optGrammar::SimpleStatement,
)
Expression_strategy = st.builds(
    Expression,
)
optGrammar::Assignment_strategy = st.builds(
    optGrammar::Assignment,
    assignmentOp=
        safe_text
)
optGrammar::PostIncDecExpression_strategy = st.builds(
    optGrammar::PostIncDecExpression,
    postOp=
        safe_text
)
optGrammar::Literal_strategy = st.builds(
    optGrammar::Literal,
)
optGrammar::Or_strategy = st.builds(
    optGrammar::Or,
)
optGrammar::Exponent_strategy = st.builds(
    optGrammar::Exponent,
)
optGrammar::QualifiedIdentifier_strategy = st.builds(
    optGrammar::QualifiedIdentifier,
    identifier=
        safe_text
)
optGrammar::MulDivMod_strategy = st.builds(
    optGrammar::MulDivMod,
    multipliciativeOp=
        safe_text
)
optGrammar::Comparison_strategy = st.builds(
    optGrammar::Comparison,
    comparisonOp=
        safe_text
)
optGrammar::SpecialExpression_strategy = st.builds(
    optGrammar::SpecialExpression,
    type=
        safe_text
)
optGrammar::TypeCast_strategy = st.builds(
    optGrammar::TypeCast,
)
optGrammar::PreIncExpression_strategy = st.builds(
    optGrammar::PreIncExpression,
)
optGrammar::PreDecExpression_strategy = st.builds(
    optGrammar::PreDecExpression,
)
optGrammar::BitAnd_strategy = st.builds(
    optGrammar::BitAnd,
)
optGrammar::BinaryNotExpression_strategy = st.builds(
    optGrammar::BinaryNotExpression,
)
optGrammar::VariableDeclarationExpression_strategy = st.builds(
    optGrammar::VariableDeclarationExpression,
)
optGrammar::AddSub_strategy = st.builds(
    optGrammar::AddSub,
    additionOp=
        safe_text
)
optGrammar::TupleSeparator_strategy = st.builds(
    optGrammar::TupleSeparator,
)
optGrammar::NewExpression_strategy = st.builds(
    optGrammar::NewExpression,
)
optGrammar::SignExpression_strategy = st.builds(
    optGrammar::SignExpression,
    signOp=
        safe_text
)
optGrammar::Shift_strategy = st.builds(
    optGrammar::Shift,
    shiftOp=
        safe_text
)
optGrammar::BitOr_strategy = st.builds(
    optGrammar::BitOr,
)
optGrammar::And_strategy = st.builds(
    optGrammar::And,
)
optGrammar::BitXor_strategy = st.builds(
    optGrammar::BitXor,
)
optGrammar::NotExpression_strategy = st.builds(
    optGrammar::NotExpression,
)
optGrammar::Equality_strategy = st.builds(
    optGrammar::Equality,
    equalityOp=
        safe_text
)
optGrammar::Tuple_strategy = st.builds(
    optGrammar::Tuple,
)
optGrammar::Mapping_strategy = st.builds(
    optGrammar::Mapping,
)
optGrammar::Variable_strategy = st.builds(
    optGrammar::Variable,
    name=
        safe_text
)
optGrammar::EnumValue_strategy = st.builds(
    optGrammar::EnumValue,
    name=
        safe_text
)
optGrammar::ReturnsParameterList_strategy = st.builds(
    optGrammar::ReturnsParameterList,
)
optGrammar::SizedDeclaration_strategy = st.builds(
    optGrammar::SizedDeclaration,
)
optGrammar::SimpleTypeDeclaration_strategy = st.builds(
    optGrammar::SimpleTypeDeclaration,
)
optGrammar::LocationLiteral_strategy = st.builds(
    optGrammar::LocationLiteral,
    type=
        safe_text
)
PrimaryTypeDeclaration_strategy = st.builds(
    PrimaryTypeDeclaration,
)
optGrammar::ArrayableDeclaration_strategy = st.builds(
    optGrammar::ArrayableDeclaration,
)
optGrammar::NonArrayableDeclaration_strategy = st.builds(
    optGrammar::NonArrayableDeclaration,
)
PrimaryTypeDefinitionDeclaration_strategy = st.builds(
    PrimaryTypeDefinitionDeclaration,
)
optGrammar::PrimaryTypeDeclaration_strategy = st.builds(
    optGrammar::PrimaryTypeDeclaration,
    constant=
        st.booleans(),
    name=
        safe_text
)
optGrammar::FunctionCallArg_strategy = st.builds(
    optGrammar::FunctionCallArg,
    name=
        safe_text
)
optGrammar::FunctionCallArguments_strategy = st.builds(
    optGrammar::FunctionCallArguments,
)
optGrammar::Expression_strategy = st.builds(
    optGrammar::Expression,
)
FunctionCallArguments_strategy = st.builds(
    FunctionCallArguments,
)
optGrammar::FunctionCallListArguments_strategy = st.builds(
    optGrammar::FunctionCallListArguments,
)
optGrammar::Body_strategy = st.builds(
    optGrammar::Body,
)
optGrammar::VisibilityLiteral_strategy = st.builds(
    optGrammar::VisibilityLiteral,
    type=
        safe_text
)
optGrammar::InheritanceSpecifier_strategy = st.builds(
    optGrammar::InheritanceSpecifier,
)
optGrammar::SymbolAlias_strategy = st.builds(
    optGrammar::SymbolAlias,
    symbol=
        safe_text,
    alias=
        safe_text
)
optGrammar::versionOperator_strategy = st.builds(
    optGrammar::versionOperator,
    value=
        safe_text
)
optGrammar::Contract_strategy = st.builds(
    optGrammar::Contract,
    name=
        safe_text
)
optGrammar::ImportDirective_strategy = st.builds(
    optGrammar::ImportDirective,
    importURI=
        safe_text,
    unitAlias=
        safe_text
)
optGrammar::ModifierInvocation_strategy = st.builds(
    optGrammar::ModifierInvocation,
)
optGrammar::Const_strategy = st.builds(
    optGrammar::Const,
)
optGrammar::StateMutability_strategy = st.builds(
    optGrammar::StateMutability,
    type=
        safe_text
)
optGrammar::ParameterList_strategy = st.builds(
    optGrammar::ParameterList,
)
DefinitionBody_strategy = st.builds(
    DefinitionBody,
)
optGrammar::FunctionDefinition_strategy = st.builds(
    optGrammar::FunctionDefinition,
    name=
        safe_text
)
optGrammar::Event_strategy = st.builds(
    optGrammar::Event,
    isAnonymous=
        st.booleans(),
    name=
        safe_text
)
optGrammar::PrimaryTypeDefinitionDeclaration_strategy = st.builds(
    optGrammar::PrimaryTypeDefinitionDeclaration,
)
optGrammar::Modifier_strategy = st.builds(
    optGrammar::Modifier,
    name=
        safe_text
)
optGrammar::EnumDefinition_strategy = st.builds(
    optGrammar::EnumDefinition,
    name=
        safe_text
)
optGrammar::StructDefinition_strategy = st.builds(
    optGrammar::StructDefinition,
    name=
        safe_text
)
optGrammar::ConstructorDefinition_strategy = st.builds(
    optGrammar::ConstructorDefinition,
    name=
        safe_text
)
optGrammar::DefinitionBody_strategy = st.builds(
    optGrammar::DefinitionBody,
)
optGrammar::PragmaDirective_strategy = st.builds(
    optGrammar::PragmaDirective,
)
optGrammar::Model_strategy = st.builds(
    optGrammar::Model,
)

@given(instance=ContinueStatement_strategy)
@settings(max_examples=50)
def test_continuestatement_instantiation(instance):
    assert isinstance(instance, ContinueStatement)

@given(instance=optGrammar::Continue_strategy)
@settings(max_examples=50)
def test_optgrammar::continue_instantiation(instance):
    assert isinstance(instance, optGrammar::Continue)

@given(instance=NamedType_strategy)
@settings(max_examples=50)
def test_namedtype_instantiation(instance):
    assert isinstance(instance, NamedType)

@given(instance=optGrammar::UnitsLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar::unitsliteral_instantiation(instance):
    assert isinstance(instance, optGrammar::UnitsLiteral)

@given(instance=optGrammar::UnitsLiteral_strategy)
def test_optgrammar::unitsliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=optGrammar::UnitsLiteral_strategy)
def test_optgrammar::unitsliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=optGrammar::TimeUnitsLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar::timeunitsliteral_instantiation(instance):
    assert isinstance(instance, optGrammar::TimeUnitsLiteral)

@given(instance=optGrammar::TimeUnitsLiteral_strategy)
def test_optgrammar::timeunitsliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=optGrammar::TimeUnitsLiteral_strategy)
def test_optgrammar::timeunitsliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=optGrammar::IntLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar::intliteral_instantiation(instance):
    assert isinstance(instance, optGrammar::IntLiteral)

@given(instance=optGrammar::IntLiteral_strategy)
def test_optgrammar::intliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=optGrammar::IntLiteral_strategy)
def test_optgrammar::intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=optGrammar::UnitTypes_strategy)
@settings(max_examples=50)
def test_optgrammar::unittypes_instantiation(instance):
    assert isinstance(instance, optGrammar::UnitTypes)

@given(instance=optGrammar::DecimalLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar::decimalliteral_instantiation(instance):
    assert isinstance(instance, optGrammar::DecimalLiteral)

@given(instance=optGrammar::DecimalLiteral_strategy)
def test_optgrammar::decimalliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=optGrammar::DecimalLiteral_strategy)
def test_optgrammar::decimalliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=optGrammar::HexLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar::hexliteral_instantiation(instance):
    assert isinstance(instance, optGrammar::HexLiteral)

@given(instance=optGrammar::HexLiteral_strategy)
def test_optgrammar::hexliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=optGrammar::HexLiteral_strategy)
def test_optgrammar::hexliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=optGrammar::SecondOperators_strategy)
@settings(max_examples=50)
def test_optgrammar::secondoperators_instantiation(instance):
    assert isinstance(instance, optGrammar::SecondOperators)

@given(instance=optGrammar::SecondOperators_strategy)
def test_optgrammar::secondoperators_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=optGrammar::SecondOperators_strategy)
def test_optgrammar::secondoperators_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=optGrammar::PrimaryArithmetic_strategy)
@settings(max_examples=50)
def test_optgrammar::primaryarithmetic_instantiation(instance):
    assert isinstance(instance, optGrammar::PrimaryArithmetic)

@given(instance=optGrammar::ArithmeticOperations_strategy)
@settings(max_examples=50)
def test_optgrammar::arithmeticoperations_instantiation(instance):
    assert isinstance(instance, optGrammar::ArithmeticOperations)

@given(instance=optGrammar::IntParameter_strategy)
@settings(max_examples=50)
def test_optgrammar::intparameter_instantiation(instance):
    assert isinstance(instance, optGrammar::IntParameter)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=optGrammar::EcrecoverFunction_strategy)
@settings(max_examples=50)
def test_optgrammar::ecrecoverfunction_instantiation(instance):
    assert isinstance(instance, optGrammar::EcrecoverFunction)

@given(instance=optGrammar::EcrecoverFunction_strategy)
def test_optgrammar::ecrecoverfunction_function_type(instance):
    assert isinstance(instance.function, str)


@given(instance=optGrammar::EcrecoverFunction_strategy)
def test_optgrammar::ecrecoverfunction_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=optGrammar::SpecialLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar::specialliteral_instantiation(instance):
    assert isinstance(instance, optGrammar::SpecialLiteral)

@given(instance=optGrammar::SpecialLiteral_strategy)
def test_optgrammar::specialliteral_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=optGrammar::SpecialLiteral_strategy)
def test_optgrammar::specialliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar::HashFunction_strategy)
@settings(max_examples=50)
def test_optgrammar::hashfunction_instantiation(instance):
    assert isinstance(instance, optGrammar::HashFunction)

@given(instance=optGrammar::HashFunction_strategy)
def test_optgrammar::hashfunction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=optGrammar::HashFunction_strategy)
def test_optgrammar::hashfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar::StringLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar::stringliteral_instantiation(instance):
    assert isinstance(instance, optGrammar::StringLiteral)

@given(instance=optGrammar::StringLiteral_strategy)
def test_optgrammar::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=optGrammar::StringLiteral_strategy)
def test_optgrammar::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=optGrammar::GasleftFunction_strategy)
@settings(max_examples=50)
def test_optgrammar::gasleftfunction_instantiation(instance):
    assert isinstance(instance, optGrammar::GasleftFunction)

@given(instance=optGrammar::GasleftFunction_strategy)
def test_optgrammar::gasleftfunction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=optGrammar::GasleftFunction_strategy)
def test_optgrammar::gasleftfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar::MathematicalFunction_strategy)
@settings(max_examples=50)
def test_optgrammar::mathematicalfunction_instantiation(instance):
    assert isinstance(instance, optGrammar::MathematicalFunction)

@given(instance=optGrammar::MathematicalFunction_strategy)
def test_optgrammar::mathematicalfunction_function_type(instance):
    assert isinstance(instance.function, str)


@given(instance=optGrammar::MathematicalFunction_strategy)
def test_optgrammar::mathematicalfunction_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=optGrammar::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar::booleanliteral_instantiation(instance):
    assert isinstance(instance, optGrammar::BooleanLiteral)

@given(instance=optGrammar::BooleanLiteral_strategy)
def test_optgrammar::booleanliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=optGrammar::BooleanLiteral_strategy)
def test_optgrammar::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=optGrammar::BlockhashFunction_strategy)
@settings(max_examples=50)
def test_optgrammar::blockhashfunction_instantiation(instance):
    assert isinstance(instance, optGrammar::BlockhashFunction)

@given(instance=PrimaryArithmetic_strategy)
@settings(max_examples=50)
def test_primaryarithmetic_instantiation(instance):
    assert isinstance(instance, PrimaryArithmetic)

@given(instance=optGrammar::NumericLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar::numericliteral_instantiation(instance):
    assert isinstance(instance, optGrammar::NumericLiteral)

@given(instance=LoopStructures_strategy)
@settings(max_examples=50)
def test_loopstructures_instantiation(instance):
    assert isinstance(instance, LoopStructures)

@given(instance=optGrammar::IfStatement_strategy)
@settings(max_examples=50)
def test_optgrammar::ifstatement_instantiation(instance):
    assert isinstance(instance, optGrammar::IfStatement)

@given(instance=optGrammar::FunctionCall_strategy)
@settings(max_examples=50)
def test_optgrammar::functioncall_instantiation(instance):
    assert isinstance(instance, optGrammar::FunctionCall)

@given(instance=optGrammar::Statement_strategy)
@settings(max_examples=50)
def test_optgrammar::statement_instantiation(instance):
    assert isinstance(instance, optGrammar::Statement)

@given(instance=optGrammar::ForStatement_strategy)
@settings(max_examples=50)
def test_optgrammar::forstatement_instantiation(instance):
    assert isinstance(instance, optGrammar::ForStatement)

@given(instance=optGrammar::WhileStatement_strategy)
@settings(max_examples=50)
def test_optgrammar::whilestatement_instantiation(instance):
    assert isinstance(instance, optGrammar::WhileStatement)

@given(instance=Qualifier_strategy)
@settings(max_examples=50)
def test_qualifier_instantiation(instance):
    assert isinstance(instance, Qualifier)

@given(instance=optGrammar::Arguments_strategy)
@settings(max_examples=50)
def test_optgrammar::arguments_instantiation(instance):
    assert isinstance(instance, optGrammar::Arguments)

@given(instance=optGrammar::Index_strategy)
@settings(max_examples=50)
def test_optgrammar::index_instantiation(instance):
    assert isinstance(instance, optGrammar::Index)

@given(instance=optGrammar::Field_strategy)
@settings(max_examples=50)
def test_optgrammar::field_instantiation(instance):
    assert isinstance(instance, optGrammar::Field)

@given(instance=optGrammar::Field_strategy)
def test_optgrammar::field_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=optGrammar::Field_strategy)
def test_optgrammar::field_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=optGrammar::Qualifier_strategy)
@settings(max_examples=50)
def test_optgrammar::qualifier_instantiation(instance):
    assert isinstance(instance, optGrammar::Qualifier)

@given(instance=optGrammar::ReturnParameterDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar::returnparameterdeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar::ReturnParameterDeclaration)

@given(instance=SimpleStatement2_strategy)
@settings(max_examples=50)
def test_simplestatement2_instantiation(instance):
    assert isinstance(instance, SimpleStatement2)

@given(instance=SimpleStatement_strategy)
@settings(max_examples=50)
def test_simplestatement_instantiation(instance):
    assert isinstance(instance, SimpleStatement)

@given(instance=optGrammar::VarVariableTupleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar::varvariabletuplevariabledeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar::VarVariableTupleVariableDeclaration)

@given(instance=optGrammar::VarVariableTupleVariableDeclaration_strategy)
def test_optgrammar::varvariabletuplevariabledeclaration_semicolon_type(instance):
    assert isinstance(instance.semicolon, bool)


@given(instance=optGrammar::VarVariableTupleVariableDeclaration_strategy)
def test_optgrammar::varvariabletuplevariabledeclaration_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=optGrammar::StandardVariableDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar::standardvariabledeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar::StandardVariableDeclaration)

@given(instance=optGrammar::StandardVariableDeclaration_strategy)
def test_optgrammar::standardvariabledeclaration_semicolon_type(instance):
    assert isinstance(instance.semicolon, bool)


@given(instance=optGrammar::StandardVariableDeclaration_strategy)
def test_optgrammar::standardvariabledeclaration_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=optGrammar::VarVariableTypeDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar::varvariabletypedeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar::VarVariableTypeDeclaration)

@given(instance=optGrammar::VarVariableTypeDeclaration_strategy)
def test_optgrammar::varvariabletypedeclaration_semicolon_type(instance):
    assert isinstance(instance.semicolon, bool)


@given(instance=optGrammar::VarVariableTypeDeclaration_strategy)
def test_optgrammar::varvariabletypedeclaration_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=optGrammar::StandardTypeWithoutQualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_optgrammar::standardtypewithoutqualifiedidentifier_instantiation(instance):
    assert isinstance(instance, optGrammar::StandardTypeWithoutQualifiedIdentifier)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=optGrammar::StandardType_strategy)
@settings(max_examples=50)
def test_optgrammar::standardtype_instantiation(instance):
    assert isinstance(instance, optGrammar::StandardType)

@given(instance=optGrammar::ArrayType_strategy)
@settings(max_examples=50)
def test_optgrammar::arraytype_instantiation(instance):
    assert isinstance(instance, optGrammar::ArrayType)

@given(instance=StandardTypeWithoutQualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_standardtypewithoutqualifiedidentifier_instantiation(instance):
    assert isinstance(instance, StandardTypeWithoutQualifiedIdentifier)

@given(instance=StandardType_strategy)
@settings(max_examples=50)
def test_standardtype_instantiation(instance):
    assert isinstance(instance, StandardType)

@given(instance=optGrammar::NamedType_strategy)
@settings(max_examples=50)
def test_optgrammar::namedtype_instantiation(instance):
    assert isinstance(instance, optGrammar::NamedType)

@given(instance=optGrammar::NamedType_strategy)
def test_optgrammar::namedtype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=optGrammar::NamedType_strategy)
def test_optgrammar::namedtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=optGrammar::Type_strategy)
@settings(max_examples=50)
def test_optgrammar::type_instantiation(instance):
    assert isinstance(instance, optGrammar::Type)

@given(instance=optGrammar::Type_strategy)
def test_optgrammar::type_isVarType_type(instance):
    assert isinstance(instance.isVarType, bool)


@given(instance=optGrammar::Type_strategy)
def test_optgrammar::type_isVarType_setter(instance):
    original = instance.isVarType
    instance.isVarType = original
    assert instance.isVarType == original

@given(instance=VariableDeclarationOptionalElement_strategy)
@settings(max_examples=50)
def test_variabledeclarationoptionalelement_instantiation(instance):
    assert isinstance(instance, VariableDeclarationOptionalElement)

@given(instance=optGrammar::IndexedSpecifer_strategy)
@settings(max_examples=50)
def test_optgrammar::indexedspecifer_instantiation(instance):
    assert isinstance(instance, optGrammar::IndexedSpecifer)

@given(instance=optGrammar::LocationSpecifier_strategy)
@settings(max_examples=50)
def test_optgrammar::locationspecifier_instantiation(instance):
    assert isinstance(instance, optGrammar::LocationSpecifier)

@given(instance=optGrammar::ConstantSpecifier_strategy)
@settings(max_examples=50)
def test_optgrammar::constantspecifier_instantiation(instance):
    assert isinstance(instance, optGrammar::ConstantSpecifier)

@given(instance=optGrammar::VisibilitySpecifier_strategy)
@settings(max_examples=50)
def test_optgrammar::visibilityspecifier_instantiation(instance):
    assert isinstance(instance, optGrammar::VisibilitySpecifier)

@given(instance=optGrammar::VariableDeclarationOptionalElement_strategy)
@settings(max_examples=50)
def test_optgrammar::variabledeclarationoptionalelement_instantiation(instance):
    assert isinstance(instance, optGrammar::VariableDeclarationOptionalElement)

@given(instance=optGrammar::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_optgrammar::expressionstatement_instantiation(instance):
    assert isinstance(instance, optGrammar::ExpressionStatement)

@given(instance=optGrammar::ExpressionStatement_strategy)
def test_optgrammar::expressionstatement_semicolon_type(instance):
    assert isinstance(instance.semicolon, bool)


@given(instance=optGrammar::ExpressionStatement_strategy)
def test_optgrammar::expressionstatement_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=optGrammar::SimpleStatement2_strategy)
@settings(max_examples=50)
def test_optgrammar::simplestatement2_instantiation(instance):
    assert isinstance(instance, optGrammar::SimpleStatement2)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=optGrammar::BreakStatement_strategy)
@settings(max_examples=50)
def test_optgrammar::breakstatement_instantiation(instance):
    assert isinstance(instance, optGrammar::BreakStatement)

@given(instance=optGrammar::ContinueStatement_strategy)
@settings(max_examples=50)
def test_optgrammar::continuestatement_instantiation(instance):
    assert isinstance(instance, optGrammar::ContinueStatement)

@given(instance=optGrammar::ReturnStatement_strategy)
@settings(max_examples=50)
def test_optgrammar::returnstatement_instantiation(instance):
    assert isinstance(instance, optGrammar::ReturnStatement)

@given(instance=optGrammar::PlaceHolderStatement_strategy)
@settings(max_examples=50)
def test_optgrammar::placeholderstatement_instantiation(instance):
    assert isinstance(instance, optGrammar::PlaceHolderStatement)

@given(instance=optGrammar::EmitStatement_strategy)
@settings(max_examples=50)
def test_optgrammar::emitstatement_instantiation(instance):
    assert isinstance(instance, optGrammar::EmitStatement)

@given(instance=optGrammar::LoopStructures_strategy)
@settings(max_examples=50)
def test_optgrammar::loopstructures_instantiation(instance):
    assert isinstance(instance, optGrammar::LoopStructures)

@given(instance=optGrammar::LoopStructures_strategy)
def test_optgrammar::loopstructures_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=optGrammar::LoopStructures_strategy)
def test_optgrammar::loopstructures_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=optGrammar::DeleteStatement_strategy)
@settings(max_examples=50)
def test_optgrammar::deletestatement_instantiation(instance):
    assert isinstance(instance, optGrammar::DeleteStatement)

@given(instance=optGrammar::ThrowStatement_strategy)
@settings(max_examples=50)
def test_optgrammar::throwstatement_instantiation(instance):
    assert isinstance(instance, optGrammar::ThrowStatement)

@given(instance=optGrammar::DoWhileStatement_strategy)
@settings(max_examples=50)
def test_optgrammar::dowhilestatement_instantiation(instance):
    assert isinstance(instance, optGrammar::DoWhileStatement)

@given(instance=optGrammar::SimpleStatement_strategy)
@settings(max_examples=50)
def test_optgrammar::simplestatement_instantiation(instance):
    assert isinstance(instance, optGrammar::SimpleStatement)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=optGrammar::Assignment_strategy)
@settings(max_examples=50)
def test_optgrammar::assignment_instantiation(instance):
    assert isinstance(instance, optGrammar::Assignment)

@given(instance=optGrammar::Assignment_strategy)
def test_optgrammar::assignment_assignmentOp_type(instance):
    assert isinstance(instance.assignmentOp, str)


@given(instance=optGrammar::Assignment_strategy)
def test_optgrammar::assignment_assignmentOp_setter(instance):
    original = instance.assignmentOp
    instance.assignmentOp = original
    assert instance.assignmentOp == original

@given(instance=optGrammar::PostIncDecExpression_strategy)
@settings(max_examples=50)
def test_optgrammar::postincdecexpression_instantiation(instance):
    assert isinstance(instance, optGrammar::PostIncDecExpression)

@given(instance=optGrammar::PostIncDecExpression_strategy)
def test_optgrammar::postincdecexpression_postOp_type(instance):
    assert isinstance(instance.postOp, str)


@given(instance=optGrammar::PostIncDecExpression_strategy)
def test_optgrammar::postincdecexpression_postOp_setter(instance):
    original = instance.postOp
    instance.postOp = original
    assert instance.postOp == original

@given(instance=optGrammar::Literal_strategy)
@settings(max_examples=50)
def test_optgrammar::literal_instantiation(instance):
    assert isinstance(instance, optGrammar::Literal)

@given(instance=optGrammar::Or_strategy)
@settings(max_examples=50)
def test_optgrammar::or_instantiation(instance):
    assert isinstance(instance, optGrammar::Or)

@given(instance=optGrammar::Exponent_strategy)
@settings(max_examples=50)
def test_optgrammar::exponent_instantiation(instance):
    assert isinstance(instance, optGrammar::Exponent)

@given(instance=optGrammar::QualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_optgrammar::qualifiedidentifier_instantiation(instance):
    assert isinstance(instance, optGrammar::QualifiedIdentifier)

@given(instance=optGrammar::QualifiedIdentifier_strategy)
def test_optgrammar::qualifiedidentifier_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=optGrammar::QualifiedIdentifier_strategy)
def test_optgrammar::qualifiedidentifier_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=optGrammar::MulDivMod_strategy)
@settings(max_examples=50)
def test_optgrammar::muldivmod_instantiation(instance):
    assert isinstance(instance, optGrammar::MulDivMod)

@given(instance=optGrammar::MulDivMod_strategy)
def test_optgrammar::muldivmod_multipliciativeOp_type(instance):
    assert isinstance(instance.multipliciativeOp, str)


@given(instance=optGrammar::MulDivMod_strategy)
def test_optgrammar::muldivmod_multipliciativeOp_setter(instance):
    original = instance.multipliciativeOp
    instance.multipliciativeOp = original
    assert instance.multipliciativeOp == original

@given(instance=optGrammar::Comparison_strategy)
@settings(max_examples=50)
def test_optgrammar::comparison_instantiation(instance):
    assert isinstance(instance, optGrammar::Comparison)

@given(instance=optGrammar::Comparison_strategy)
def test_optgrammar::comparison_comparisonOp_type(instance):
    assert isinstance(instance.comparisonOp, str)


@given(instance=optGrammar::Comparison_strategy)
def test_optgrammar::comparison_comparisonOp_setter(instance):
    original = instance.comparisonOp
    instance.comparisonOp = original
    assert instance.comparisonOp == original

@given(instance=optGrammar::SpecialExpression_strategy)
@settings(max_examples=50)
def test_optgrammar::specialexpression_instantiation(instance):
    assert isinstance(instance, optGrammar::SpecialExpression)

@given(instance=optGrammar::SpecialExpression_strategy)
def test_optgrammar::specialexpression_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=optGrammar::SpecialExpression_strategy)
def test_optgrammar::specialexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=optGrammar::TypeCast_strategy)
@settings(max_examples=50)
def test_optgrammar::typecast_instantiation(instance):
    assert isinstance(instance, optGrammar::TypeCast)

@given(instance=optGrammar::PreIncExpression_strategy)
@settings(max_examples=50)
def test_optgrammar::preincexpression_instantiation(instance):
    assert isinstance(instance, optGrammar::PreIncExpression)

@given(instance=optGrammar::PreDecExpression_strategy)
@settings(max_examples=50)
def test_optgrammar::predecexpression_instantiation(instance):
    assert isinstance(instance, optGrammar::PreDecExpression)

@given(instance=optGrammar::BitAnd_strategy)
@settings(max_examples=50)
def test_optgrammar::bitand_instantiation(instance):
    assert isinstance(instance, optGrammar::BitAnd)

@given(instance=optGrammar::BinaryNotExpression_strategy)
@settings(max_examples=50)
def test_optgrammar::binarynotexpression_instantiation(instance):
    assert isinstance(instance, optGrammar::BinaryNotExpression)

@given(instance=optGrammar::VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_optgrammar::variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, optGrammar::VariableDeclarationExpression)

@given(instance=optGrammar::AddSub_strategy)
@settings(max_examples=50)
def test_optgrammar::addsub_instantiation(instance):
    assert isinstance(instance, optGrammar::AddSub)

@given(instance=optGrammar::AddSub_strategy)
def test_optgrammar::addsub_additionOp_type(instance):
    assert isinstance(instance.additionOp, str)


@given(instance=optGrammar::AddSub_strategy)
def test_optgrammar::addsub_additionOp_setter(instance):
    original = instance.additionOp
    instance.additionOp = original
    assert instance.additionOp == original

@given(instance=optGrammar::TupleSeparator_strategy)
@settings(max_examples=50)
def test_optgrammar::tupleseparator_instantiation(instance):
    assert isinstance(instance, optGrammar::TupleSeparator)

@given(instance=optGrammar::NewExpression_strategy)
@settings(max_examples=50)
def test_optgrammar::newexpression_instantiation(instance):
    assert isinstance(instance, optGrammar::NewExpression)

@given(instance=optGrammar::SignExpression_strategy)
@settings(max_examples=50)
def test_optgrammar::signexpression_instantiation(instance):
    assert isinstance(instance, optGrammar::SignExpression)

@given(instance=optGrammar::SignExpression_strategy)
def test_optgrammar::signexpression_signOp_type(instance):
    assert isinstance(instance.signOp, str)


@given(instance=optGrammar::SignExpression_strategy)
def test_optgrammar::signexpression_signOp_setter(instance):
    original = instance.signOp
    instance.signOp = original
    assert instance.signOp == original

@given(instance=optGrammar::Shift_strategy)
@settings(max_examples=50)
def test_optgrammar::shift_instantiation(instance):
    assert isinstance(instance, optGrammar::Shift)

@given(instance=optGrammar::Shift_strategy)
def test_optgrammar::shift_shiftOp_type(instance):
    assert isinstance(instance.shiftOp, str)


@given(instance=optGrammar::Shift_strategy)
def test_optgrammar::shift_shiftOp_setter(instance):
    original = instance.shiftOp
    instance.shiftOp = original
    assert instance.shiftOp == original

@given(instance=optGrammar::BitOr_strategy)
@settings(max_examples=50)
def test_optgrammar::bitor_instantiation(instance):
    assert isinstance(instance, optGrammar::BitOr)

@given(instance=optGrammar::And_strategy)
@settings(max_examples=50)
def test_optgrammar::and_instantiation(instance):
    assert isinstance(instance, optGrammar::And)

@given(instance=optGrammar::BitXor_strategy)
@settings(max_examples=50)
def test_optgrammar::bitxor_instantiation(instance):
    assert isinstance(instance, optGrammar::BitXor)

@given(instance=optGrammar::NotExpression_strategy)
@settings(max_examples=50)
def test_optgrammar::notexpression_instantiation(instance):
    assert isinstance(instance, optGrammar::NotExpression)

@given(instance=optGrammar::Equality_strategy)
@settings(max_examples=50)
def test_optgrammar::equality_instantiation(instance):
    assert isinstance(instance, optGrammar::Equality)

@given(instance=optGrammar::Equality_strategy)
def test_optgrammar::equality_equalityOp_type(instance):
    assert isinstance(instance.equalityOp, str)


@given(instance=optGrammar::Equality_strategy)
def test_optgrammar::equality_equalityOp_setter(instance):
    original = instance.equalityOp
    instance.equalityOp = original
    assert instance.equalityOp == original

@given(instance=optGrammar::Tuple_strategy)
@settings(max_examples=50)
def test_optgrammar::tuple_instantiation(instance):
    assert isinstance(instance, optGrammar::Tuple)

@given(instance=optGrammar::Mapping_strategy)
@settings(max_examples=50)
def test_optgrammar::mapping_instantiation(instance):
    assert isinstance(instance, optGrammar::Mapping)

@given(instance=optGrammar::Variable_strategy)
@settings(max_examples=50)
def test_optgrammar::variable_instantiation(instance):
    assert isinstance(instance, optGrammar::Variable)

@given(instance=optGrammar::Variable_strategy)
def test_optgrammar::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=optGrammar::Variable_strategy)
def test_optgrammar::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar::EnumValue_strategy)
@settings(max_examples=50)
def test_optgrammar::enumvalue_instantiation(instance):
    assert isinstance(instance, optGrammar::EnumValue)

@given(instance=optGrammar::EnumValue_strategy)
def test_optgrammar::enumvalue_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=optGrammar::EnumValue_strategy)
def test_optgrammar::enumvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar::ReturnsParameterList_strategy)
@settings(max_examples=50)
def test_optgrammar::returnsparameterlist_instantiation(instance):
    assert isinstance(instance, optGrammar::ReturnsParameterList)

@given(instance=optGrammar::SizedDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar::sizeddeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar::SizedDeclaration)

@given(instance=optGrammar::SimpleTypeDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar::simpletypedeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar::SimpleTypeDeclaration)

@given(instance=optGrammar::LocationLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar::locationliteral_instantiation(instance):
    assert isinstance(instance, optGrammar::LocationLiteral)

@given(instance=optGrammar::LocationLiteral_strategy)
def test_optgrammar::locationliteral_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=optGrammar::LocationLiteral_strategy)
def test_optgrammar::locationliteral_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=PrimaryTypeDeclaration_strategy)
@settings(max_examples=50)
def test_primarytypedeclaration_instantiation(instance):
    assert isinstance(instance, PrimaryTypeDeclaration)

@given(instance=optGrammar::ArrayableDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar::arrayabledeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar::ArrayableDeclaration)

@given(instance=optGrammar::NonArrayableDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar::nonarrayabledeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar::NonArrayableDeclaration)

@given(instance=PrimaryTypeDefinitionDeclaration_strategy)
@settings(max_examples=50)
def test_primarytypedefinitiondeclaration_instantiation(instance):
    assert isinstance(instance, PrimaryTypeDefinitionDeclaration)

@given(instance=optGrammar::PrimaryTypeDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar::primarytypedeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar::PrimaryTypeDeclaration)

@given(instance=optGrammar::PrimaryTypeDeclaration_strategy)
def test_optgrammar::primarytypedeclaration_constant_type(instance):
    assert isinstance(instance.constant, bool)


@given(instance=optGrammar::PrimaryTypeDeclaration_strategy)
def test_optgrammar::primarytypedeclaration_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=optGrammar::PrimaryTypeDeclaration_strategy)
def test_optgrammar::primarytypedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=optGrammar::PrimaryTypeDeclaration_strategy)
def test_optgrammar::primarytypedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar::FunctionCallArg_strategy)
@settings(max_examples=50)
def test_optgrammar::functioncallarg_instantiation(instance):
    assert isinstance(instance, optGrammar::FunctionCallArg)

@given(instance=optGrammar::FunctionCallArg_strategy)
def test_optgrammar::functioncallarg_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=optGrammar::FunctionCallArg_strategy)
def test_optgrammar::functioncallarg_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar::FunctionCallArguments_strategy)
@settings(max_examples=50)
def test_optgrammar::functioncallarguments_instantiation(instance):
    assert isinstance(instance, optGrammar::FunctionCallArguments)

@given(instance=optGrammar::Expression_strategy)
@settings(max_examples=50)
def test_optgrammar::expression_instantiation(instance):
    assert isinstance(instance, optGrammar::Expression)

@given(instance=FunctionCallArguments_strategy)
@settings(max_examples=50)
def test_functioncallarguments_instantiation(instance):
    assert isinstance(instance, FunctionCallArguments)

@given(instance=optGrammar::FunctionCallListArguments_strategy)
@settings(max_examples=50)
def test_optgrammar::functioncalllistarguments_instantiation(instance):
    assert isinstance(instance, optGrammar::FunctionCallListArguments)

@given(instance=optGrammar::Body_strategy)
@settings(max_examples=50)
def test_optgrammar::body_instantiation(instance):
    assert isinstance(instance, optGrammar::Body)

@given(instance=optGrammar::VisibilityLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar::visibilityliteral_instantiation(instance):
    assert isinstance(instance, optGrammar::VisibilityLiteral)

@given(instance=optGrammar::VisibilityLiteral_strategy)
def test_optgrammar::visibilityliteral_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=optGrammar::VisibilityLiteral_strategy)
def test_optgrammar::visibilityliteral_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=optGrammar::InheritanceSpecifier_strategy)
@settings(max_examples=50)
def test_optgrammar::inheritancespecifier_instantiation(instance):
    assert isinstance(instance, optGrammar::InheritanceSpecifier)

@given(instance=optGrammar::SymbolAlias_strategy)
@settings(max_examples=50)
def test_optgrammar::symbolalias_instantiation(instance):
    assert isinstance(instance, optGrammar::SymbolAlias)

@given(instance=optGrammar::SymbolAlias_strategy)
def test_optgrammar::symbolalias_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=optGrammar::SymbolAlias_strategy)
def test_optgrammar::symbolalias_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=optGrammar::SymbolAlias_strategy)
def test_optgrammar::symbolalias_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=optGrammar::SymbolAlias_strategy)
def test_optgrammar::symbolalias_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=optGrammar::versionOperator_strategy)
@settings(max_examples=50)
def test_optgrammar::versionoperator_instantiation(instance):
    assert isinstance(instance, optGrammar::versionOperator)

@given(instance=optGrammar::versionOperator_strategy)
def test_optgrammar::versionoperator_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=optGrammar::versionOperator_strategy)
def test_optgrammar::versionoperator_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=optGrammar::Contract_strategy)
@settings(max_examples=50)
def test_optgrammar::contract_instantiation(instance):
    assert isinstance(instance, optGrammar::Contract)

@given(instance=optGrammar::Contract_strategy)
def test_optgrammar::contract_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=optGrammar::Contract_strategy)
def test_optgrammar::contract_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar::ImportDirective_strategy)
@settings(max_examples=50)
def test_optgrammar::importdirective_instantiation(instance):
    assert isinstance(instance, optGrammar::ImportDirective)

@given(instance=optGrammar::ImportDirective_strategy)
def test_optgrammar::importdirective_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=optGrammar::ImportDirective_strategy)
def test_optgrammar::importdirective_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=optGrammar::ImportDirective_strategy)
def test_optgrammar::importdirective_unitAlias_type(instance):
    assert isinstance(instance.unitAlias, str)


@given(instance=optGrammar::ImportDirective_strategy)
def test_optgrammar::importdirective_unitAlias_setter(instance):
    original = instance.unitAlias
    instance.unitAlias = original
    assert instance.unitAlias == original

@given(instance=optGrammar::ModifierInvocation_strategy)
@settings(max_examples=50)
def test_optgrammar::modifierinvocation_instantiation(instance):
    assert isinstance(instance, optGrammar::ModifierInvocation)

@given(instance=optGrammar::Const_strategy)
@settings(max_examples=50)
def test_optgrammar::const_instantiation(instance):
    assert isinstance(instance, optGrammar::Const)

@given(instance=optGrammar::StateMutability_strategy)
@settings(max_examples=50)
def test_optgrammar::statemutability_instantiation(instance):
    assert isinstance(instance, optGrammar::StateMutability)

@given(instance=optGrammar::StateMutability_strategy)
def test_optgrammar::statemutability_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=optGrammar::StateMutability_strategy)
def test_optgrammar::statemutability_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=optGrammar::ParameterList_strategy)
@settings(max_examples=50)
def test_optgrammar::parameterlist_instantiation(instance):
    assert isinstance(instance, optGrammar::ParameterList)

@given(instance=DefinitionBody_strategy)
@settings(max_examples=50)
def test_definitionbody_instantiation(instance):
    assert isinstance(instance, DefinitionBody)

@given(instance=optGrammar::FunctionDefinition_strategy)
@settings(max_examples=50)
def test_optgrammar::functiondefinition_instantiation(instance):
    assert isinstance(instance, optGrammar::FunctionDefinition)

@given(instance=optGrammar::FunctionDefinition_strategy)
def test_optgrammar::functiondefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=optGrammar::FunctionDefinition_strategy)
def test_optgrammar::functiondefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar::Event_strategy)
@settings(max_examples=50)
def test_optgrammar::event_instantiation(instance):
    assert isinstance(instance, optGrammar::Event)

@given(instance=optGrammar::Event_strategy)
def test_optgrammar::event_isAnonymous_type(instance):
    assert isinstance(instance.isAnonymous, bool)


@given(instance=optGrammar::Event_strategy)
def test_optgrammar::event_isAnonymous_setter(instance):
    original = instance.isAnonymous
    instance.isAnonymous = original
    assert instance.isAnonymous == original

@given(instance=optGrammar::Event_strategy)
def test_optgrammar::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=optGrammar::Event_strategy)
def test_optgrammar::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar::PrimaryTypeDefinitionDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar::primarytypedefinitiondeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar::PrimaryTypeDefinitionDeclaration)

@given(instance=optGrammar::Modifier_strategy)
@settings(max_examples=50)
def test_optgrammar::modifier_instantiation(instance):
    assert isinstance(instance, optGrammar::Modifier)

@given(instance=optGrammar::Modifier_strategy)
def test_optgrammar::modifier_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=optGrammar::Modifier_strategy)
def test_optgrammar::modifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar::EnumDefinition_strategy)
@settings(max_examples=50)
def test_optgrammar::enumdefinition_instantiation(instance):
    assert isinstance(instance, optGrammar::EnumDefinition)

@given(instance=optGrammar::EnumDefinition_strategy)
def test_optgrammar::enumdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=optGrammar::EnumDefinition_strategy)
def test_optgrammar::enumdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar::StructDefinition_strategy)
@settings(max_examples=50)
def test_optgrammar::structdefinition_instantiation(instance):
    assert isinstance(instance, optGrammar::StructDefinition)

@given(instance=optGrammar::StructDefinition_strategy)
def test_optgrammar::structdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=optGrammar::StructDefinition_strategy)
def test_optgrammar::structdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar::ConstructorDefinition_strategy)
@settings(max_examples=50)
def test_optgrammar::constructordefinition_instantiation(instance):
    assert isinstance(instance, optGrammar::ConstructorDefinition)

@given(instance=optGrammar::ConstructorDefinition_strategy)
def test_optgrammar::constructordefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=optGrammar::ConstructorDefinition_strategy)
def test_optgrammar::constructordefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar::DefinitionBody_strategy)
@settings(max_examples=50)
def test_optgrammar::definitionbody_instantiation(instance):
    assert isinstance(instance, optGrammar::DefinitionBody)

@given(instance=optGrammar::PragmaDirective_strategy)
@settings(max_examples=50)
def test_optgrammar::pragmadirective_instantiation(instance):
    assert isinstance(instance, optGrammar::PragmaDirective)

@given(instance=optGrammar::Model_strategy)
@settings(max_examples=50)
def test_optgrammar::model_instantiation(instance):
    assert isinstance(instance, optGrammar::Model)

import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ContinueStatement,
    optGrammar_Continue,
    NamedType,
    optGrammar_UnitsLiteral,
    optGrammar_TimeUnitsLiteral,
    optGrammar_IntLiteral,
    optGrammar_UnitTypes,
    optGrammar_DecimalLiteral,
    optGrammar_HexLiteral,
    optGrammar_SecondOperators,
    optGrammar_PrimaryArithmetic,
    optGrammar_ArithmeticOperations,
    optGrammar_IntParameter,
    Literal,
    optGrammar_GasleftFunction,
    optGrammar_HashFunction,
    optGrammar_BooleanLiteral,
    optGrammar_EcrecoverFunction,
    optGrammar_MathematicalFunction,
    optGrammar_StringLiteral,
    optGrammar_SpecialLiteral,
    optGrammar_BlockhashFunction,
    PrimaryArithmetic,
    optGrammar_NumericLiteral,
    LoopStructures,
    optGrammar_IfStatement,
    optGrammar_FunctionCall,
    optGrammar_Statement,
    optGrammar_ForStatement,
    optGrammar_WhileStatement,
    Qualifier,
    optGrammar_Index,
    optGrammar_Arguments,
    optGrammar_Field,
    optGrammar_Qualifier,
    optGrammar_ReturnParameterDeclaration,
    SimpleStatement2,
    SimpleStatement,
    optGrammar_VarVariableTupleVariableDeclaration,
    optGrammar_StandardVariableDeclaration,
    optGrammar_VarVariableTypeDeclaration,
    optGrammar_StandardTypeWithoutQualifiedIdentifier,
    Type,
    optGrammar_StandardType,
    optGrammar_ArrayType,
    StandardTypeWithoutQualifiedIdentifier,
    StandardType,
    optGrammar_NamedType,
    optGrammar_Type,
    VariableDeclarationOptionalElement,
    optGrammar_IndexedSpecifer,
    optGrammar_ConstantSpecifier,
    optGrammar_LocationSpecifier,
    optGrammar_VisibilitySpecifier,
    optGrammar_VariableDeclarationOptionalElement,
    optGrammar_ExpressionStatement,
    optGrammar_SimpleStatement2,
    Statement,
    optGrammar_ContinueStatement,
    optGrammar_PlaceHolderStatement,
    optGrammar_BreakStatement,
    optGrammar_EmitStatement,
    optGrammar_LoopStructures,
    optGrammar_ThrowStatement,
    optGrammar_DoWhileStatement,
    optGrammar_ReturnStatement,
    optGrammar_DeleteStatement,
    optGrammar_SimpleStatement,
    Expression,
    optGrammar_BinaryNotExpression,
    optGrammar_QualifiedIdentifier,
    optGrammar_NotExpression,
    optGrammar_Or,
    optGrammar_SpecialExpression,
    optGrammar_BitAnd,
    optGrammar_Shift,
    optGrammar_MulDivMod,
    optGrammar_Exponent,
    optGrammar_BitOr,
    optGrammar_Equality,
    optGrammar_PostIncDecExpression,
    optGrammar_TupleSeparator,
    optGrammar_PreIncExpression,
    optGrammar_Literal,
    optGrammar_NewExpression,
    optGrammar_AddSub,
    optGrammar_And,
    optGrammar_Assignment,
    optGrammar_Comparison,
    optGrammar_BitXor,
    optGrammar_PreDecExpression,
    optGrammar_TypeCast,
    optGrammar_SignExpression,
    optGrammar_VariableDeclarationExpression,
    optGrammar_Tuple,
    optGrammar_Mapping,
    optGrammar_Variable,
    optGrammar_EnumValue,
    optGrammar_ReturnsParameterList,
    optGrammar_SizedDeclaration,
    optGrammar_SimpleTypeDeclaration,
    optGrammar_LocationLiteral,
    PrimaryTypeDeclaration,
    optGrammar_ArrayableDeclaration,
    optGrammar_NonArrayableDeclaration,
    PrimaryTypeDefinitionDeclaration,
    optGrammar_PrimaryTypeDeclaration,
    optGrammar_FunctionCallArg,
    optGrammar_FunctionCallArguments,
    optGrammar_Expression,
    FunctionCallArguments,
    optGrammar_FunctionCallListArguments,
    optGrammar_Body,
    optGrammar_VisibilityLiteral,
    optGrammar_InheritanceSpecifier,
    optGrammar_SymbolAlias,
    optGrammar_versionOperator,
    optGrammar_Contract,
    optGrammar_ImportDirective,
    optGrammar_ModifierInvocation,
    optGrammar_Const,
    optGrammar_StateMutability,
    optGrammar_ParameterList,
    DefinitionBody,
    optGrammar_StructDefinition,
    optGrammar_Event,
    optGrammar_EnumDefinition,
    optGrammar_PrimaryTypeDefinitionDeclaration,
    optGrammar_Modifier,
    optGrammar_FunctionDefinition,
    optGrammar_ConstructorDefinition,
    optGrammar_DefinitionBody,
    optGrammar_PragmaDirective,
    optGrammar_Model,
    AssignmentOpEnum,
    ReservedWordsEnum,
    SpecialExpressionTypeEnum,
    MulDivModOpEnum,
    EqualityOpEnum,
    AdditionOpEnum,
    IncDecOpEnum,
    ComparisonOpEnum,
    ShiftOpEnum,
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



def test_optgrammar_continue_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Continue)


def test_optgrammar_continue_constructor_exists():
    assert callable(optGrammar_Continue.__init__)


def test_optgrammar_continue_constructor_args():
    sig = inspect.signature(optGrammar_Continue.__init__)
    params = list(sig.parameters.keys())



def test_namedtype_is_not_abstract():
    assert not inspect.isabstract(NamedType)


def test_namedtype_constructor_exists():
    assert callable(NamedType.__init__)


def test_namedtype_constructor_args():
    sig = inspect.signature(NamedType.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_unitsliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar_UnitsLiteral)


def test_optgrammar_unitsliteral_constructor_exists():
    assert callable(optGrammar_UnitsLiteral.__init__)


def test_optgrammar_unitsliteral_constructor_args():
    sig = inspect.signature(optGrammar_UnitsLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_optgrammar_unitsliteral_has_value():
    assert hasattr(optGrammar_UnitsLiteral, "value")
    descriptor = None
    for klass in optGrammar_UnitsLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_timeunitsliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar_TimeUnitsLiteral)


def test_optgrammar_timeunitsliteral_constructor_exists():
    assert callable(optGrammar_TimeUnitsLiteral.__init__)


def test_optgrammar_timeunitsliteral_constructor_args():
    sig = inspect.signature(optGrammar_TimeUnitsLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_optgrammar_timeunitsliteral_has_value():
    assert hasattr(optGrammar_TimeUnitsLiteral, "value")
    descriptor = None
    for klass in optGrammar_TimeUnitsLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_intliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar_IntLiteral)


def test_optgrammar_intliteral_constructor_exists():
    assert callable(optGrammar_IntLiteral.__init__)


def test_optgrammar_intliteral_constructor_args():
    sig = inspect.signature(optGrammar_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_optgrammar_intliteral_has_value():
    assert hasattr(optGrammar_IntLiteral, "value")
    descriptor = None
    for klass in optGrammar_IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_unittypes_is_not_abstract():
    assert not inspect.isabstract(optGrammar_UnitTypes)


def test_optgrammar_unittypes_constructor_exists():
    assert callable(optGrammar_UnitTypes.__init__)


def test_optgrammar_unittypes_constructor_args():
    sig = inspect.signature(optGrammar_UnitTypes.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_decimalliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar_DecimalLiteral)


def test_optgrammar_decimalliteral_constructor_exists():
    assert callable(optGrammar_DecimalLiteral.__init__)


def test_optgrammar_decimalliteral_constructor_args():
    sig = inspect.signature(optGrammar_DecimalLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_optgrammar_decimalliteral_has_value():
    assert hasattr(optGrammar_DecimalLiteral, "value")
    descriptor = None
    for klass in optGrammar_DecimalLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_hexliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar_HexLiteral)


def test_optgrammar_hexliteral_constructor_exists():
    assert callable(optGrammar_HexLiteral.__init__)


def test_optgrammar_hexliteral_constructor_args():
    sig = inspect.signature(optGrammar_HexLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_optgrammar_hexliteral_has_value():
    assert hasattr(optGrammar_HexLiteral, "value")
    descriptor = None
    for klass in optGrammar_HexLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_secondoperators_is_not_abstract():
    assert not inspect.isabstract(optGrammar_SecondOperators)


def test_optgrammar_secondoperators_constructor_exists():
    assert callable(optGrammar_SecondOperators.__init__)


def test_optgrammar_secondoperators_constructor_args():
    sig = inspect.signature(optGrammar_SecondOperators.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_optgrammar_secondoperators_has_operator():
    assert hasattr(optGrammar_SecondOperators, "operator")
    descriptor = None
    for klass in optGrammar_SecondOperators.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_primaryarithmetic_is_not_abstract():
    assert not inspect.isabstract(optGrammar_PrimaryArithmetic)


def test_optgrammar_primaryarithmetic_constructor_exists():
    assert callable(optGrammar_PrimaryArithmetic.__init__)


def test_optgrammar_primaryarithmetic_constructor_args():
    sig = inspect.signature(optGrammar_PrimaryArithmetic.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_arithmeticoperations_is_not_abstract():
    assert not inspect.isabstract(optGrammar_ArithmeticOperations)


def test_optgrammar_arithmeticoperations_constructor_exists():
    assert callable(optGrammar_ArithmeticOperations.__init__)


def test_optgrammar_arithmeticoperations_constructor_args():
    sig = inspect.signature(optGrammar_ArithmeticOperations.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_intparameter_is_not_abstract():
    assert not inspect.isabstract(optGrammar_IntParameter)


def test_optgrammar_intparameter_constructor_exists():
    assert callable(optGrammar_IntParameter.__init__)


def test_optgrammar_intparameter_constructor_args():
    sig = inspect.signature(optGrammar_IntParameter.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_gasleftfunction_is_not_abstract():
    assert not inspect.isabstract(optGrammar_GasleftFunction)


def test_optgrammar_gasleftfunction_constructor_exists():
    assert callable(optGrammar_GasleftFunction.__init__)


def test_optgrammar_gasleftfunction_constructor_args():
    sig = inspect.signature(optGrammar_GasleftFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar_gasleftfunction_has_name():
    assert hasattr(optGrammar_GasleftFunction, "name")
    descriptor = None
    for klass in optGrammar_GasleftFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_hashfunction_is_not_abstract():
    assert not inspect.isabstract(optGrammar_HashFunction)


def test_optgrammar_hashfunction_constructor_exists():
    assert callable(optGrammar_HashFunction.__init__)


def test_optgrammar_hashfunction_constructor_args():
    sig = inspect.signature(optGrammar_HashFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar_hashfunction_has_name():
    assert hasattr(optGrammar_HashFunction, "name")
    descriptor = None
    for klass in optGrammar_HashFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar_BooleanLiteral)


def test_optgrammar_booleanliteral_constructor_exists():
    assert callable(optGrammar_BooleanLiteral.__init__)


def test_optgrammar_booleanliteral_constructor_args():
    sig = inspect.signature(optGrammar_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_optgrammar_booleanliteral_has_value():
    assert hasattr(optGrammar_BooleanLiteral, "value")
    descriptor = None
    for klass in optGrammar_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_ecrecoverfunction_is_not_abstract():
    assert not inspect.isabstract(optGrammar_EcrecoverFunction)


def test_optgrammar_ecrecoverfunction_constructor_exists():
    assert callable(optGrammar_EcrecoverFunction.__init__)


def test_optgrammar_ecrecoverfunction_constructor_args():
    sig = inspect.signature(optGrammar_EcrecoverFunction.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_optgrammar_ecrecoverfunction_has_function():
    assert hasattr(optGrammar_EcrecoverFunction, "function")
    descriptor = None
    for klass in optGrammar_EcrecoverFunction.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_mathematicalfunction_is_not_abstract():
    assert not inspect.isabstract(optGrammar_MathematicalFunction)


def test_optgrammar_mathematicalfunction_constructor_exists():
    assert callable(optGrammar_MathematicalFunction.__init__)


def test_optgrammar_mathematicalfunction_constructor_args():
    sig = inspect.signature(optGrammar_MathematicalFunction.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_optgrammar_mathematicalfunction_has_function():
    assert hasattr(optGrammar_MathematicalFunction, "function")
    descriptor = None
    for klass in optGrammar_MathematicalFunction.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_stringliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar_StringLiteral)


def test_optgrammar_stringliteral_constructor_exists():
    assert callable(optGrammar_StringLiteral.__init__)


def test_optgrammar_stringliteral_constructor_args():
    sig = inspect.signature(optGrammar_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_optgrammar_stringliteral_has_value():
    assert hasattr(optGrammar_StringLiteral, "value")
    descriptor = None
    for klass in optGrammar_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_specialliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar_SpecialLiteral)


def test_optgrammar_specialliteral_constructor_exists():
    assert callable(optGrammar_SpecialLiteral.__init__)


def test_optgrammar_specialliteral_constructor_args():
    sig = inspect.signature(optGrammar_SpecialLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar_specialliteral_has_name():
    assert hasattr(optGrammar_SpecialLiteral, "name")
    descriptor = None
    for klass in optGrammar_SpecialLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_blockhashfunction_is_not_abstract():
    assert not inspect.isabstract(optGrammar_BlockhashFunction)


def test_optgrammar_blockhashfunction_constructor_exists():
    assert callable(optGrammar_BlockhashFunction.__init__)


def test_optgrammar_blockhashfunction_constructor_args():
    sig = inspect.signature(optGrammar_BlockhashFunction.__init__)
    params = list(sig.parameters.keys())



def test_primaryarithmetic_is_not_abstract():
    assert not inspect.isabstract(PrimaryArithmetic)


def test_primaryarithmetic_constructor_exists():
    assert callable(PrimaryArithmetic.__init__)


def test_primaryarithmetic_constructor_args():
    sig = inspect.signature(PrimaryArithmetic.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_numericliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar_NumericLiteral)


def test_optgrammar_numericliteral_constructor_exists():
    assert callable(optGrammar_NumericLiteral.__init__)


def test_optgrammar_numericliteral_constructor_args():
    sig = inspect.signature(optGrammar_NumericLiteral.__init__)
    params = list(sig.parameters.keys())



def test_loopstructures_is_not_abstract():
    assert not inspect.isabstract(LoopStructures)


def test_loopstructures_constructor_exists():
    assert callable(LoopStructures.__init__)


def test_loopstructures_constructor_args():
    sig = inspect.signature(LoopStructures.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_ifstatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar_IfStatement)


def test_optgrammar_ifstatement_constructor_exists():
    assert callable(optGrammar_IfStatement.__init__)


def test_optgrammar_ifstatement_constructor_args():
    sig = inspect.signature(optGrammar_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_functioncall_is_not_abstract():
    assert not inspect.isabstract(optGrammar_FunctionCall)


def test_optgrammar_functioncall_constructor_exists():
    assert callable(optGrammar_FunctionCall.__init__)


def test_optgrammar_functioncall_constructor_args():
    sig = inspect.signature(optGrammar_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_statement_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Statement)


def test_optgrammar_statement_constructor_exists():
    assert callable(optGrammar_Statement.__init__)


def test_optgrammar_statement_constructor_args():
    sig = inspect.signature(optGrammar_Statement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_forstatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar_ForStatement)


def test_optgrammar_forstatement_constructor_exists():
    assert callable(optGrammar_ForStatement.__init__)


def test_optgrammar_forstatement_constructor_args():
    sig = inspect.signature(optGrammar_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_whilestatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar_WhileStatement)


def test_optgrammar_whilestatement_constructor_exists():
    assert callable(optGrammar_WhileStatement.__init__)


def test_optgrammar_whilestatement_constructor_args():
    sig = inspect.signature(optGrammar_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_qualifier_is_not_abstract():
    assert not inspect.isabstract(Qualifier)


def test_qualifier_constructor_exists():
    assert callable(Qualifier.__init__)


def test_qualifier_constructor_args():
    sig = inspect.signature(Qualifier.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_index_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Index)


def test_optgrammar_index_constructor_exists():
    assert callable(optGrammar_Index.__init__)


def test_optgrammar_index_constructor_args():
    sig = inspect.signature(optGrammar_Index.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_arguments_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Arguments)


def test_optgrammar_arguments_constructor_exists():
    assert callable(optGrammar_Arguments.__init__)


def test_optgrammar_arguments_constructor_args():
    sig = inspect.signature(optGrammar_Arguments.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_field_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Field)


def test_optgrammar_field_constructor_exists():
    assert callable(optGrammar_Field.__init__)


def test_optgrammar_field_constructor_args():
    sig = inspect.signature(optGrammar_Field.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_optgrammar_field_has_field():
    assert hasattr(optGrammar_Field, "field")
    descriptor = None
    for klass in optGrammar_Field.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_qualifier_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Qualifier)


def test_optgrammar_qualifier_constructor_exists():
    assert callable(optGrammar_Qualifier.__init__)


def test_optgrammar_qualifier_constructor_args():
    sig = inspect.signature(optGrammar_Qualifier.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_returnparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar_ReturnParameterDeclaration)


def test_optgrammar_returnparameterdeclaration_constructor_exists():
    assert callable(optGrammar_ReturnParameterDeclaration.__init__)


def test_optgrammar_returnparameterdeclaration_constructor_args():
    sig = inspect.signature(optGrammar_ReturnParameterDeclaration.__init__)
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



def test_optgrammar_varvariabletuplevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar_VarVariableTupleVariableDeclaration)


def test_optgrammar_varvariabletuplevariabledeclaration_constructor_exists():
    assert callable(optGrammar_VarVariableTupleVariableDeclaration.__init__)


def test_optgrammar_varvariabletuplevariabledeclaration_constructor_args():
    sig = inspect.signature(optGrammar_VarVariableTupleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_optgrammar_varvariabletuplevariabledeclaration_has_semicolon():
    assert hasattr(optGrammar_VarVariableTupleVariableDeclaration, "semicolon")
    descriptor = None
    for klass in optGrammar_VarVariableTupleVariableDeclaration.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_standardvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar_StandardVariableDeclaration)


def test_optgrammar_standardvariabledeclaration_constructor_exists():
    assert callable(optGrammar_StandardVariableDeclaration.__init__)


def test_optgrammar_standardvariabledeclaration_constructor_args():
    sig = inspect.signature(optGrammar_StandardVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_optgrammar_standardvariabledeclaration_has_semicolon():
    assert hasattr(optGrammar_StandardVariableDeclaration, "semicolon")
    descriptor = None
    for klass in optGrammar_StandardVariableDeclaration.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_varvariabletypedeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar_VarVariableTypeDeclaration)


def test_optgrammar_varvariabletypedeclaration_constructor_exists():
    assert callable(optGrammar_VarVariableTypeDeclaration.__init__)


def test_optgrammar_varvariabletypedeclaration_constructor_args():
    sig = inspect.signature(optGrammar_VarVariableTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_optgrammar_varvariabletypedeclaration_has_semicolon():
    assert hasattr(optGrammar_VarVariableTypeDeclaration, "semicolon")
    descriptor = None
    for klass in optGrammar_VarVariableTypeDeclaration.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_standardtypewithoutqualifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(optGrammar_StandardTypeWithoutQualifiedIdentifier)


def test_optgrammar_standardtypewithoutqualifiedidentifier_constructor_exists():
    assert callable(optGrammar_StandardTypeWithoutQualifiedIdentifier.__init__)


def test_optgrammar_standardtypewithoutqualifiedidentifier_constructor_args():
    sig = inspect.signature(optGrammar_StandardTypeWithoutQualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_standardtype_is_not_abstract():
    assert not inspect.isabstract(optGrammar_StandardType)


def test_optgrammar_standardtype_constructor_exists():
    assert callable(optGrammar_StandardType.__init__)


def test_optgrammar_standardtype_constructor_args():
    sig = inspect.signature(optGrammar_StandardType.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_arraytype_is_not_abstract():
    assert not inspect.isabstract(optGrammar_ArrayType)


def test_optgrammar_arraytype_constructor_exists():
    assert callable(optGrammar_ArrayType.__init__)


def test_optgrammar_arraytype_constructor_args():
    sig = inspect.signature(optGrammar_ArrayType.__init__)
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



def test_optgrammar_namedtype_is_not_abstract():
    assert not inspect.isabstract(optGrammar_NamedType)


def test_optgrammar_namedtype_constructor_exists():
    assert callable(optGrammar_NamedType.__init__)


def test_optgrammar_namedtype_constructor_args():
    sig = inspect.signature(optGrammar_NamedType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_optgrammar_namedtype_has_type():
    assert hasattr(optGrammar_NamedType, "type")
    descriptor = None
    for klass in optGrammar_NamedType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_type_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Type)


def test_optgrammar_type_constructor_exists():
    assert callable(optGrammar_Type.__init__)


def test_optgrammar_type_constructor_args():
    sig = inspect.signature(optGrammar_Type.__init__)
    params = list(sig.parameters.keys())
    assert "isVarType" in params, "Missing parameter 'isVarType'"

def test_optgrammar_type_has_isVarType():
    assert hasattr(optGrammar_Type, "isVarType")
    descriptor = None
    for klass in optGrammar_Type.__mro__:
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



def test_optgrammar_indexedspecifer_is_not_abstract():
    assert not inspect.isabstract(optGrammar_IndexedSpecifer)


def test_optgrammar_indexedspecifer_constructor_exists():
    assert callable(optGrammar_IndexedSpecifer.__init__)


def test_optgrammar_indexedspecifer_constructor_args():
    sig = inspect.signature(optGrammar_IndexedSpecifer.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_constantspecifier_is_not_abstract():
    assert not inspect.isabstract(optGrammar_ConstantSpecifier)


def test_optgrammar_constantspecifier_constructor_exists():
    assert callable(optGrammar_ConstantSpecifier.__init__)


def test_optgrammar_constantspecifier_constructor_args():
    sig = inspect.signature(optGrammar_ConstantSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_locationspecifier_is_not_abstract():
    assert not inspect.isabstract(optGrammar_LocationSpecifier)


def test_optgrammar_locationspecifier_constructor_exists():
    assert callable(optGrammar_LocationSpecifier.__init__)


def test_optgrammar_locationspecifier_constructor_args():
    sig = inspect.signature(optGrammar_LocationSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_visibilityspecifier_is_not_abstract():
    assert not inspect.isabstract(optGrammar_VisibilitySpecifier)


def test_optgrammar_visibilityspecifier_constructor_exists():
    assert callable(optGrammar_VisibilitySpecifier.__init__)


def test_optgrammar_visibilityspecifier_constructor_args():
    sig = inspect.signature(optGrammar_VisibilitySpecifier.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_variabledeclarationoptionalelement_is_not_abstract():
    assert not inspect.isabstract(optGrammar_VariableDeclarationOptionalElement)


def test_optgrammar_variabledeclarationoptionalelement_constructor_exists():
    assert callable(optGrammar_VariableDeclarationOptionalElement.__init__)


def test_optgrammar_variabledeclarationoptionalelement_constructor_args():
    sig = inspect.signature(optGrammar_VariableDeclarationOptionalElement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar_ExpressionStatement)


def test_optgrammar_expressionstatement_constructor_exists():
    assert callable(optGrammar_ExpressionStatement.__init__)


def test_optgrammar_expressionstatement_constructor_args():
    sig = inspect.signature(optGrammar_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_optgrammar_expressionstatement_has_semicolon():
    assert hasattr(optGrammar_ExpressionStatement, "semicolon")
    descriptor = None
    for klass in optGrammar_ExpressionStatement.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_simplestatement2_is_not_abstract():
    assert not inspect.isabstract(optGrammar_SimpleStatement2)


def test_optgrammar_simplestatement2_constructor_exists():
    assert callable(optGrammar_SimpleStatement2.__init__)


def test_optgrammar_simplestatement2_constructor_args():
    sig = inspect.signature(optGrammar_SimpleStatement2.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_continuestatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar_ContinueStatement)


def test_optgrammar_continuestatement_constructor_exists():
    assert callable(optGrammar_ContinueStatement.__init__)


def test_optgrammar_continuestatement_constructor_args():
    sig = inspect.signature(optGrammar_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_placeholderstatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar_PlaceHolderStatement)


def test_optgrammar_placeholderstatement_constructor_exists():
    assert callable(optGrammar_PlaceHolderStatement.__init__)


def test_optgrammar_placeholderstatement_constructor_args():
    sig = inspect.signature(optGrammar_PlaceHolderStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_breakstatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar_BreakStatement)


def test_optgrammar_breakstatement_constructor_exists():
    assert callable(optGrammar_BreakStatement.__init__)


def test_optgrammar_breakstatement_constructor_args():
    sig = inspect.signature(optGrammar_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_emitstatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar_EmitStatement)


def test_optgrammar_emitstatement_constructor_exists():
    assert callable(optGrammar_EmitStatement.__init__)


def test_optgrammar_emitstatement_constructor_args():
    sig = inspect.signature(optGrammar_EmitStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_loopstructures_is_not_abstract():
    assert not inspect.isabstract(optGrammar_LoopStructures)


def test_optgrammar_loopstructures_constructor_exists():
    assert callable(optGrammar_LoopStructures.__init__)


def test_optgrammar_loopstructures_constructor_args():
    sig = inspect.signature(optGrammar_LoopStructures.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_optgrammar_loopstructures_has_type():
    assert hasattr(optGrammar_LoopStructures, "type")
    descriptor = None
    for klass in optGrammar_LoopStructures.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_throwstatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar_ThrowStatement)


def test_optgrammar_throwstatement_constructor_exists():
    assert callable(optGrammar_ThrowStatement.__init__)


def test_optgrammar_throwstatement_constructor_args():
    sig = inspect.signature(optGrammar_ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_dowhilestatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar_DoWhileStatement)


def test_optgrammar_dowhilestatement_constructor_exists():
    assert callable(optGrammar_DoWhileStatement.__init__)


def test_optgrammar_dowhilestatement_constructor_args():
    sig = inspect.signature(optGrammar_DoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_returnstatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar_ReturnStatement)


def test_optgrammar_returnstatement_constructor_exists():
    assert callable(optGrammar_ReturnStatement.__init__)


def test_optgrammar_returnstatement_constructor_args():
    sig = inspect.signature(optGrammar_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_deletestatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar_DeleteStatement)


def test_optgrammar_deletestatement_constructor_exists():
    assert callable(optGrammar_DeleteStatement.__init__)


def test_optgrammar_deletestatement_constructor_args():
    sig = inspect.signature(optGrammar_DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_simplestatement_is_not_abstract():
    assert not inspect.isabstract(optGrammar_SimpleStatement)


def test_optgrammar_simplestatement_constructor_exists():
    assert callable(optGrammar_SimpleStatement.__init__)


def test_optgrammar_simplestatement_constructor_args():
    sig = inspect.signature(optGrammar_SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_binarynotexpression_is_not_abstract():
    assert not inspect.isabstract(optGrammar_BinaryNotExpression)


def test_optgrammar_binarynotexpression_constructor_exists():
    assert callable(optGrammar_BinaryNotExpression.__init__)


def test_optgrammar_binarynotexpression_constructor_args():
    sig = inspect.signature(optGrammar_BinaryNotExpression.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_qualifiedidentifier_is_not_abstract():
    assert not inspect.isabstract(optGrammar_QualifiedIdentifier)


def test_optgrammar_qualifiedidentifier_constructor_exists():
    assert callable(optGrammar_QualifiedIdentifier.__init__)


def test_optgrammar_qualifiedidentifier_constructor_args():
    sig = inspect.signature(optGrammar_QualifiedIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_optgrammar_qualifiedidentifier_has_identifier():
    assert hasattr(optGrammar_QualifiedIdentifier, "identifier")
    descriptor = None
    for klass in optGrammar_QualifiedIdentifier.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_notexpression_is_not_abstract():
    assert not inspect.isabstract(optGrammar_NotExpression)


def test_optgrammar_notexpression_constructor_exists():
    assert callable(optGrammar_NotExpression.__init__)


def test_optgrammar_notexpression_constructor_args():
    sig = inspect.signature(optGrammar_NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_or_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Or)


def test_optgrammar_or_constructor_exists():
    assert callable(optGrammar_Or.__init__)


def test_optgrammar_or_constructor_args():
    sig = inspect.signature(optGrammar_Or.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_specialexpression_is_not_abstract():
    assert not inspect.isabstract(optGrammar_SpecialExpression)


def test_optgrammar_specialexpression_constructor_exists():
    assert callable(optGrammar_SpecialExpression.__init__)


def test_optgrammar_specialexpression_constructor_args():
    sig = inspect.signature(optGrammar_SpecialExpression.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_optgrammar_specialexpression_has_type():
    assert hasattr(optGrammar_SpecialExpression, "type")
    descriptor = None
    for klass in optGrammar_SpecialExpression.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_bitand_is_not_abstract():
    assert not inspect.isabstract(optGrammar_BitAnd)


def test_optgrammar_bitand_constructor_exists():
    assert callable(optGrammar_BitAnd.__init__)


def test_optgrammar_bitand_constructor_args():
    sig = inspect.signature(optGrammar_BitAnd.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_shift_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Shift)


def test_optgrammar_shift_constructor_exists():
    assert callable(optGrammar_Shift.__init__)


def test_optgrammar_shift_constructor_args():
    sig = inspect.signature(optGrammar_Shift.__init__)
    params = list(sig.parameters.keys())
    assert "shiftOp" in params, "Missing parameter 'shiftOp'"

def test_optgrammar_shift_has_shiftOp():
    assert hasattr(optGrammar_Shift, "shiftOp")
    descriptor = None
    for klass in optGrammar_Shift.__mro__:
        if "shiftOp" in klass.__dict__:
            descriptor = klass.__dict__["shiftOp"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_muldivmod_is_not_abstract():
    assert not inspect.isabstract(optGrammar_MulDivMod)


def test_optgrammar_muldivmod_constructor_exists():
    assert callable(optGrammar_MulDivMod.__init__)


def test_optgrammar_muldivmod_constructor_args():
    sig = inspect.signature(optGrammar_MulDivMod.__init__)
    params = list(sig.parameters.keys())
    assert "multipliciativeOp" in params, "Missing parameter 'multipliciativeOp'"

def test_optgrammar_muldivmod_has_multipliciativeOp():
    assert hasattr(optGrammar_MulDivMod, "multipliciativeOp")
    descriptor = None
    for klass in optGrammar_MulDivMod.__mro__:
        if "multipliciativeOp" in klass.__dict__:
            descriptor = klass.__dict__["multipliciativeOp"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_exponent_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Exponent)


def test_optgrammar_exponent_constructor_exists():
    assert callable(optGrammar_Exponent.__init__)


def test_optgrammar_exponent_constructor_args():
    sig = inspect.signature(optGrammar_Exponent.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_bitor_is_not_abstract():
    assert not inspect.isabstract(optGrammar_BitOr)


def test_optgrammar_bitor_constructor_exists():
    assert callable(optGrammar_BitOr.__init__)


def test_optgrammar_bitor_constructor_args():
    sig = inspect.signature(optGrammar_BitOr.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_equality_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Equality)


def test_optgrammar_equality_constructor_exists():
    assert callable(optGrammar_Equality.__init__)


def test_optgrammar_equality_constructor_args():
    sig = inspect.signature(optGrammar_Equality.__init__)
    params = list(sig.parameters.keys())
    assert "equalityOp" in params, "Missing parameter 'equalityOp'"

def test_optgrammar_equality_has_equalityOp():
    assert hasattr(optGrammar_Equality, "equalityOp")
    descriptor = None
    for klass in optGrammar_Equality.__mro__:
        if "equalityOp" in klass.__dict__:
            descriptor = klass.__dict__["equalityOp"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_postincdecexpression_is_not_abstract():
    assert not inspect.isabstract(optGrammar_PostIncDecExpression)


def test_optgrammar_postincdecexpression_constructor_exists():
    assert callable(optGrammar_PostIncDecExpression.__init__)


def test_optgrammar_postincdecexpression_constructor_args():
    sig = inspect.signature(optGrammar_PostIncDecExpression.__init__)
    params = list(sig.parameters.keys())
    assert "postOp" in params, "Missing parameter 'postOp'"

def test_optgrammar_postincdecexpression_has_postOp():
    assert hasattr(optGrammar_PostIncDecExpression, "postOp")
    descriptor = None
    for klass in optGrammar_PostIncDecExpression.__mro__:
        if "postOp" in klass.__dict__:
            descriptor = klass.__dict__["postOp"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_tupleseparator_is_not_abstract():
    assert not inspect.isabstract(optGrammar_TupleSeparator)


def test_optgrammar_tupleseparator_constructor_exists():
    assert callable(optGrammar_TupleSeparator.__init__)


def test_optgrammar_tupleseparator_constructor_args():
    sig = inspect.signature(optGrammar_TupleSeparator.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_preincexpression_is_not_abstract():
    assert not inspect.isabstract(optGrammar_PreIncExpression)


def test_optgrammar_preincexpression_constructor_exists():
    assert callable(optGrammar_PreIncExpression.__init__)


def test_optgrammar_preincexpression_constructor_args():
    sig = inspect.signature(optGrammar_PreIncExpression.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_literal_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Literal)


def test_optgrammar_literal_constructor_exists():
    assert callable(optGrammar_Literal.__init__)


def test_optgrammar_literal_constructor_args():
    sig = inspect.signature(optGrammar_Literal.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_newexpression_is_not_abstract():
    assert not inspect.isabstract(optGrammar_NewExpression)


def test_optgrammar_newexpression_constructor_exists():
    assert callable(optGrammar_NewExpression.__init__)


def test_optgrammar_newexpression_constructor_args():
    sig = inspect.signature(optGrammar_NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_addsub_is_not_abstract():
    assert not inspect.isabstract(optGrammar_AddSub)


def test_optgrammar_addsub_constructor_exists():
    assert callable(optGrammar_AddSub.__init__)


def test_optgrammar_addsub_constructor_args():
    sig = inspect.signature(optGrammar_AddSub.__init__)
    params = list(sig.parameters.keys())
    assert "additionOp" in params, "Missing parameter 'additionOp'"

def test_optgrammar_addsub_has_additionOp():
    assert hasattr(optGrammar_AddSub, "additionOp")
    descriptor = None
    for klass in optGrammar_AddSub.__mro__:
        if "additionOp" in klass.__dict__:
            descriptor = klass.__dict__["additionOp"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_and_is_not_abstract():
    assert not inspect.isabstract(optGrammar_And)


def test_optgrammar_and_constructor_exists():
    assert callable(optGrammar_And.__init__)


def test_optgrammar_and_constructor_args():
    sig = inspect.signature(optGrammar_And.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_assignment_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Assignment)


def test_optgrammar_assignment_constructor_exists():
    assert callable(optGrammar_Assignment.__init__)


def test_optgrammar_assignment_constructor_args():
    sig = inspect.signature(optGrammar_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "assignmentOp" in params, "Missing parameter 'assignmentOp'"

def test_optgrammar_assignment_has_assignmentOp():
    assert hasattr(optGrammar_Assignment, "assignmentOp")
    descriptor = None
    for klass in optGrammar_Assignment.__mro__:
        if "assignmentOp" in klass.__dict__:
            descriptor = klass.__dict__["assignmentOp"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_comparison_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Comparison)


def test_optgrammar_comparison_constructor_exists():
    assert callable(optGrammar_Comparison.__init__)


def test_optgrammar_comparison_constructor_args():
    sig = inspect.signature(optGrammar_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "comparisonOp" in params, "Missing parameter 'comparisonOp'"

def test_optgrammar_comparison_has_comparisonOp():
    assert hasattr(optGrammar_Comparison, "comparisonOp")
    descriptor = None
    for klass in optGrammar_Comparison.__mro__:
        if "comparisonOp" in klass.__dict__:
            descriptor = klass.__dict__["comparisonOp"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_bitxor_is_not_abstract():
    assert not inspect.isabstract(optGrammar_BitXor)


def test_optgrammar_bitxor_constructor_exists():
    assert callable(optGrammar_BitXor.__init__)


def test_optgrammar_bitxor_constructor_args():
    sig = inspect.signature(optGrammar_BitXor.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_predecexpression_is_not_abstract():
    assert not inspect.isabstract(optGrammar_PreDecExpression)


def test_optgrammar_predecexpression_constructor_exists():
    assert callable(optGrammar_PreDecExpression.__init__)


def test_optgrammar_predecexpression_constructor_args():
    sig = inspect.signature(optGrammar_PreDecExpression.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_typecast_is_not_abstract():
    assert not inspect.isabstract(optGrammar_TypeCast)


def test_optgrammar_typecast_constructor_exists():
    assert callable(optGrammar_TypeCast.__init__)


def test_optgrammar_typecast_constructor_args():
    sig = inspect.signature(optGrammar_TypeCast.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_signexpression_is_not_abstract():
    assert not inspect.isabstract(optGrammar_SignExpression)


def test_optgrammar_signexpression_constructor_exists():
    assert callable(optGrammar_SignExpression.__init__)


def test_optgrammar_signexpression_constructor_args():
    sig = inspect.signature(optGrammar_SignExpression.__init__)
    params = list(sig.parameters.keys())
    assert "signOp" in params, "Missing parameter 'signOp'"

def test_optgrammar_signexpression_has_signOp():
    assert hasattr(optGrammar_SignExpression, "signOp")
    descriptor = None
    for klass in optGrammar_SignExpression.__mro__:
        if "signOp" in klass.__dict__:
            descriptor = klass.__dict__["signOp"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(optGrammar_VariableDeclarationExpression)


def test_optgrammar_variabledeclarationexpression_constructor_exists():
    assert callable(optGrammar_VariableDeclarationExpression.__init__)


def test_optgrammar_variabledeclarationexpression_constructor_args():
    sig = inspect.signature(optGrammar_VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_tuple_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Tuple)


def test_optgrammar_tuple_constructor_exists():
    assert callable(optGrammar_Tuple.__init__)


def test_optgrammar_tuple_constructor_args():
    sig = inspect.signature(optGrammar_Tuple.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_mapping_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Mapping)


def test_optgrammar_mapping_constructor_exists():
    assert callable(optGrammar_Mapping.__init__)


def test_optgrammar_mapping_constructor_args():
    sig = inspect.signature(optGrammar_Mapping.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_variable_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Variable)


def test_optgrammar_variable_constructor_exists():
    assert callable(optGrammar_Variable.__init__)


def test_optgrammar_variable_constructor_args():
    sig = inspect.signature(optGrammar_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar_variable_has_name():
    assert hasattr(optGrammar_Variable, "name")
    descriptor = None
    for klass in optGrammar_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_enumvalue_is_not_abstract():
    assert not inspect.isabstract(optGrammar_EnumValue)


def test_optgrammar_enumvalue_constructor_exists():
    assert callable(optGrammar_EnumValue.__init__)


def test_optgrammar_enumvalue_constructor_args():
    sig = inspect.signature(optGrammar_EnumValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar_enumvalue_has_name():
    assert hasattr(optGrammar_EnumValue, "name")
    descriptor = None
    for klass in optGrammar_EnumValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_returnsparameterlist_is_not_abstract():
    assert not inspect.isabstract(optGrammar_ReturnsParameterList)


def test_optgrammar_returnsparameterlist_constructor_exists():
    assert callable(optGrammar_ReturnsParameterList.__init__)


def test_optgrammar_returnsparameterlist_constructor_args():
    sig = inspect.signature(optGrammar_ReturnsParameterList.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_sizeddeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar_SizedDeclaration)


def test_optgrammar_sizeddeclaration_constructor_exists():
    assert callable(optGrammar_SizedDeclaration.__init__)


def test_optgrammar_sizeddeclaration_constructor_args():
    sig = inspect.signature(optGrammar_SizedDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_simpletypedeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar_SimpleTypeDeclaration)


def test_optgrammar_simpletypedeclaration_constructor_exists():
    assert callable(optGrammar_SimpleTypeDeclaration.__init__)


def test_optgrammar_simpletypedeclaration_constructor_args():
    sig = inspect.signature(optGrammar_SimpleTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_locationliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar_LocationLiteral)


def test_optgrammar_locationliteral_constructor_exists():
    assert callable(optGrammar_LocationLiteral.__init__)


def test_optgrammar_locationliteral_constructor_args():
    sig = inspect.signature(optGrammar_LocationLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_optgrammar_locationliteral_has_type():
    assert hasattr(optGrammar_LocationLiteral, "type")
    descriptor = None
    for klass in optGrammar_LocationLiteral.__mro__:
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



def test_optgrammar_arrayabledeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar_ArrayableDeclaration)


def test_optgrammar_arrayabledeclaration_constructor_exists():
    assert callable(optGrammar_ArrayableDeclaration.__init__)


def test_optgrammar_arrayabledeclaration_constructor_args():
    sig = inspect.signature(optGrammar_ArrayableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_nonarrayabledeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar_NonArrayableDeclaration)


def test_optgrammar_nonarrayabledeclaration_constructor_exists():
    assert callable(optGrammar_NonArrayableDeclaration.__init__)


def test_optgrammar_nonarrayabledeclaration_constructor_args():
    sig = inspect.signature(optGrammar_NonArrayableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_primarytypedefinitiondeclaration_is_not_abstract():
    assert not inspect.isabstract(PrimaryTypeDefinitionDeclaration)


def test_primarytypedefinitiondeclaration_constructor_exists():
    assert callable(PrimaryTypeDefinitionDeclaration.__init__)


def test_primarytypedefinitiondeclaration_constructor_args():
    sig = inspect.signature(PrimaryTypeDefinitionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_primarytypedeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar_PrimaryTypeDeclaration)


def test_optgrammar_primarytypedeclaration_constructor_exists():
    assert callable(optGrammar_PrimaryTypeDeclaration.__init__)


def test_optgrammar_primarytypedeclaration_constructor_args():
    sig = inspect.signature(optGrammar_PrimaryTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "constant" in params, "Missing parameter 'constant'"

def test_optgrammar_primarytypedeclaration_has_name():
    assert hasattr(optGrammar_PrimaryTypeDeclaration, "name")
    descriptor = None
    for klass in optGrammar_PrimaryTypeDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_optgrammar_primarytypedeclaration_has_constant():
    assert hasattr(optGrammar_PrimaryTypeDeclaration, "constant")
    descriptor = None
    for klass in optGrammar_PrimaryTypeDeclaration.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_functioncallarg_is_not_abstract():
    assert not inspect.isabstract(optGrammar_FunctionCallArg)


def test_optgrammar_functioncallarg_constructor_exists():
    assert callable(optGrammar_FunctionCallArg.__init__)


def test_optgrammar_functioncallarg_constructor_args():
    sig = inspect.signature(optGrammar_FunctionCallArg.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar_functioncallarg_has_name():
    assert hasattr(optGrammar_FunctionCallArg, "name")
    descriptor = None
    for klass in optGrammar_FunctionCallArg.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_functioncallarguments_is_not_abstract():
    assert not inspect.isabstract(optGrammar_FunctionCallArguments)


def test_optgrammar_functioncallarguments_constructor_exists():
    assert callable(optGrammar_FunctionCallArguments.__init__)


def test_optgrammar_functioncallarguments_constructor_args():
    sig = inspect.signature(optGrammar_FunctionCallArguments.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_expression_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Expression)


def test_optgrammar_expression_constructor_exists():
    assert callable(optGrammar_Expression.__init__)


def test_optgrammar_expression_constructor_args():
    sig = inspect.signature(optGrammar_Expression.__init__)
    params = list(sig.parameters.keys())



def test_functioncallarguments_is_not_abstract():
    assert not inspect.isabstract(FunctionCallArguments)


def test_functioncallarguments_constructor_exists():
    assert callable(FunctionCallArguments.__init__)


def test_functioncallarguments_constructor_args():
    sig = inspect.signature(FunctionCallArguments.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_functioncalllistarguments_is_not_abstract():
    assert not inspect.isabstract(optGrammar_FunctionCallListArguments)


def test_optgrammar_functioncalllistarguments_constructor_exists():
    assert callable(optGrammar_FunctionCallListArguments.__init__)


def test_optgrammar_functioncalllistarguments_constructor_args():
    sig = inspect.signature(optGrammar_FunctionCallListArguments.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_body_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Body)


def test_optgrammar_body_constructor_exists():
    assert callable(optGrammar_Body.__init__)


def test_optgrammar_body_constructor_args():
    sig = inspect.signature(optGrammar_Body.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_visibilityliteral_is_not_abstract():
    assert not inspect.isabstract(optGrammar_VisibilityLiteral)


def test_optgrammar_visibilityliteral_constructor_exists():
    assert callable(optGrammar_VisibilityLiteral.__init__)


def test_optgrammar_visibilityliteral_constructor_args():
    sig = inspect.signature(optGrammar_VisibilityLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_optgrammar_visibilityliteral_has_type():
    assert hasattr(optGrammar_VisibilityLiteral, "type")
    descriptor = None
    for klass in optGrammar_VisibilityLiteral.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_inheritancespecifier_is_not_abstract():
    assert not inspect.isabstract(optGrammar_InheritanceSpecifier)


def test_optgrammar_inheritancespecifier_constructor_exists():
    assert callable(optGrammar_InheritanceSpecifier.__init__)


def test_optgrammar_inheritancespecifier_constructor_args():
    sig = inspect.signature(optGrammar_InheritanceSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_symbolalias_is_not_abstract():
    assert not inspect.isabstract(optGrammar_SymbolAlias)


def test_optgrammar_symbolalias_constructor_exists():
    assert callable(optGrammar_SymbolAlias.__init__)


def test_optgrammar_symbolalias_constructor_args():
    sig = inspect.signature(optGrammar_SymbolAlias.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_optgrammar_symbolalias_has_symbol():
    assert hasattr(optGrammar_SymbolAlias, "symbol")
    descriptor = None
    for klass in optGrammar_SymbolAlias.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_optgrammar_symbolalias_has_alias():
    assert hasattr(optGrammar_SymbolAlias, "alias")
    descriptor = None
    for klass in optGrammar_SymbolAlias.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_versionoperator_is_not_abstract():
    assert not inspect.isabstract(optGrammar_versionOperator)


def test_optgrammar_versionoperator_constructor_exists():
    assert callable(optGrammar_versionOperator.__init__)


def test_optgrammar_versionoperator_constructor_args():
    sig = inspect.signature(optGrammar_versionOperator.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_optgrammar_versionoperator_has_value():
    assert hasattr(optGrammar_versionOperator, "value")
    descriptor = None
    for klass in optGrammar_versionOperator.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_contract_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Contract)


def test_optgrammar_contract_constructor_exists():
    assert callable(optGrammar_Contract.__init__)


def test_optgrammar_contract_constructor_args():
    sig = inspect.signature(optGrammar_Contract.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar_contract_has_name():
    assert hasattr(optGrammar_Contract, "name")
    descriptor = None
    for klass in optGrammar_Contract.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_importdirective_is_not_abstract():
    assert not inspect.isabstract(optGrammar_ImportDirective)


def test_optgrammar_importdirective_constructor_exists():
    assert callable(optGrammar_ImportDirective.__init__)


def test_optgrammar_importdirective_constructor_args():
    sig = inspect.signature(optGrammar_ImportDirective.__init__)
    params = list(sig.parameters.keys())
    assert "unitAlias" in params, "Missing parameter 'unitAlias'"
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_optgrammar_importdirective_has_unitAlias():
    assert hasattr(optGrammar_ImportDirective, "unitAlias")
    descriptor = None
    for klass in optGrammar_ImportDirective.__mro__:
        if "unitAlias" in klass.__dict__:
            descriptor = klass.__dict__["unitAlias"]
            break
    assert isinstance(descriptor, property)

def test_optgrammar_importdirective_has_importURI():
    assert hasattr(optGrammar_ImportDirective, "importURI")
    descriptor = None
    for klass in optGrammar_ImportDirective.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_modifierinvocation_is_not_abstract():
    assert not inspect.isabstract(optGrammar_ModifierInvocation)


def test_optgrammar_modifierinvocation_constructor_exists():
    assert callable(optGrammar_ModifierInvocation.__init__)


def test_optgrammar_modifierinvocation_constructor_args():
    sig = inspect.signature(optGrammar_ModifierInvocation.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_const_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Const)


def test_optgrammar_const_constructor_exists():
    assert callable(optGrammar_Const.__init__)


def test_optgrammar_const_constructor_args():
    sig = inspect.signature(optGrammar_Const.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_statemutability_is_not_abstract():
    assert not inspect.isabstract(optGrammar_StateMutability)


def test_optgrammar_statemutability_constructor_exists():
    assert callable(optGrammar_StateMutability.__init__)


def test_optgrammar_statemutability_constructor_args():
    sig = inspect.signature(optGrammar_StateMutability.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_optgrammar_statemutability_has_type():
    assert hasattr(optGrammar_StateMutability, "type")
    descriptor = None
    for klass in optGrammar_StateMutability.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_parameterlist_is_not_abstract():
    assert not inspect.isabstract(optGrammar_ParameterList)


def test_optgrammar_parameterlist_constructor_exists():
    assert callable(optGrammar_ParameterList.__init__)


def test_optgrammar_parameterlist_constructor_args():
    sig = inspect.signature(optGrammar_ParameterList.__init__)
    params = list(sig.parameters.keys())



def test_definitionbody_is_not_abstract():
    assert not inspect.isabstract(DefinitionBody)


def test_definitionbody_constructor_exists():
    assert callable(DefinitionBody.__init__)


def test_definitionbody_constructor_args():
    sig = inspect.signature(DefinitionBody.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_structdefinition_is_not_abstract():
    assert not inspect.isabstract(optGrammar_StructDefinition)


def test_optgrammar_structdefinition_constructor_exists():
    assert callable(optGrammar_StructDefinition.__init__)


def test_optgrammar_structdefinition_constructor_args():
    sig = inspect.signature(optGrammar_StructDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar_structdefinition_has_name():
    assert hasattr(optGrammar_StructDefinition, "name")
    descriptor = None
    for klass in optGrammar_StructDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_event_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Event)


def test_optgrammar_event_constructor_exists():
    assert callable(optGrammar_Event.__init__)


def test_optgrammar_event_constructor_args():
    sig = inspect.signature(optGrammar_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isAnonymous" in params, "Missing parameter 'isAnonymous'"

def test_optgrammar_event_has_name():
    assert hasattr(optGrammar_Event, "name")
    descriptor = None
    for klass in optGrammar_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_optgrammar_event_has_isAnonymous():
    assert hasattr(optGrammar_Event, "isAnonymous")
    descriptor = None
    for klass in optGrammar_Event.__mro__:
        if "isAnonymous" in klass.__dict__:
            descriptor = klass.__dict__["isAnonymous"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_enumdefinition_is_not_abstract():
    assert not inspect.isabstract(optGrammar_EnumDefinition)


def test_optgrammar_enumdefinition_constructor_exists():
    assert callable(optGrammar_EnumDefinition.__init__)


def test_optgrammar_enumdefinition_constructor_args():
    sig = inspect.signature(optGrammar_EnumDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar_enumdefinition_has_name():
    assert hasattr(optGrammar_EnumDefinition, "name")
    descriptor = None
    for klass in optGrammar_EnumDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_primarytypedefinitiondeclaration_is_not_abstract():
    assert not inspect.isabstract(optGrammar_PrimaryTypeDefinitionDeclaration)


def test_optgrammar_primarytypedefinitiondeclaration_constructor_exists():
    assert callable(optGrammar_PrimaryTypeDefinitionDeclaration.__init__)


def test_optgrammar_primarytypedefinitiondeclaration_constructor_args():
    sig = inspect.signature(optGrammar_PrimaryTypeDefinitionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_modifier_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Modifier)


def test_optgrammar_modifier_constructor_exists():
    assert callable(optGrammar_Modifier.__init__)


def test_optgrammar_modifier_constructor_args():
    sig = inspect.signature(optGrammar_Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar_modifier_has_name():
    assert hasattr(optGrammar_Modifier, "name")
    descriptor = None
    for klass in optGrammar_Modifier.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_functiondefinition_is_not_abstract():
    assert not inspect.isabstract(optGrammar_FunctionDefinition)


def test_optgrammar_functiondefinition_constructor_exists():
    assert callable(optGrammar_FunctionDefinition.__init__)


def test_optgrammar_functiondefinition_constructor_args():
    sig = inspect.signature(optGrammar_FunctionDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar_functiondefinition_has_name():
    assert hasattr(optGrammar_FunctionDefinition, "name")
    descriptor = None
    for klass in optGrammar_FunctionDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_constructordefinition_is_not_abstract():
    assert not inspect.isabstract(optGrammar_ConstructorDefinition)


def test_optgrammar_constructordefinition_constructor_exists():
    assert callable(optGrammar_ConstructorDefinition.__init__)


def test_optgrammar_constructordefinition_constructor_args():
    sig = inspect.signature(optGrammar_ConstructorDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_optgrammar_constructordefinition_has_name():
    assert hasattr(optGrammar_ConstructorDefinition, "name")
    descriptor = None
    for klass in optGrammar_ConstructorDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_optgrammar_definitionbody_is_not_abstract():
    assert not inspect.isabstract(optGrammar_DefinitionBody)


def test_optgrammar_definitionbody_constructor_exists():
    assert callable(optGrammar_DefinitionBody.__init__)


def test_optgrammar_definitionbody_constructor_args():
    sig = inspect.signature(optGrammar_DefinitionBody.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_pragmadirective_is_not_abstract():
    assert not inspect.isabstract(optGrammar_PragmaDirective)


def test_optgrammar_pragmadirective_constructor_exists():
    assert callable(optGrammar_PragmaDirective.__init__)


def test_optgrammar_pragmadirective_constructor_args():
    sig = inspect.signature(optGrammar_PragmaDirective.__init__)
    params = list(sig.parameters.keys())



def test_optgrammar_model_is_not_abstract():
    assert not inspect.isabstract(optGrammar_Model)


def test_optgrammar_model_constructor_exists():
    assert callable(optGrammar_Model.__init__)


def test_optgrammar_model_constructor_args():
    sig = inspect.signature(optGrammar_Model.__init__)
    params = list(sig.parameters.keys())

def test_assignmentopenum_exists():
    # Check that the Enumeration exists
    assert AssignmentOpEnum is not None

def test_assignmentopenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOpEnum]
    expected_literals = [
        "ASSIGN_SHIFT_RIGHT_ARIMETIC",
        "ASSIGN_ADD",
        "ASSIGN_SHIFT_LEFT",
        "ASSIGN",
        "ASSIGN_DIV",
        "ASSIGN_MULT",
        "ASSIGN_OR",
        "ASSIGN_SHIFT_RIGHT",
        "ASSIGN_MOD",
        "ASSIGN_AND",
        "ASSIGN_SUB",
        "ASSIGN_XOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOpEnum"

def test_reservedwordsenum_exists():
    # Check that the Enumeration exists
    assert ReservedWordsEnum is not None

def test_reservedwordsenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReservedWordsEnum]
    expected_literals = [
        "SWITCH",
        "TYPEOF",
        "RELOCATABLE",
        "TRY",
        "CATCH",
        "ILLEGAL",
        "CASE",
        "TYPE",
        "USING",
        "FINAL",
        "OF",
        "MATCH",
        "AS",
        "LET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReservedWordsEnum"

def test_specialexpressiontypeenum_exists():
    # Check that the Enumeration exists
    assert SpecialExpressionTypeEnum is not None

def test_specialexpressiontypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpecialExpressionTypeEnum]
    expected_literals = [
        "SUPER",
        "THIS",
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
        "DIV",
        "MULT",
        "MOD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MulDivModOpEnum"

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

def test_additionopenum_exists():
    # Check that the Enumeration exists
    assert AdditionOpEnum is not None

def test_additionopenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdditionOpEnum]
    expected_literals = [
        "SUB",
        "ADD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdditionOpEnum"

def test_incdecopenum_exists():
    # Check that the Enumeration exists
    assert IncDecOpEnum is not None

def test_incdecopenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IncDecOpEnum]
    expected_literals = [
        "DEC",
        "INC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IncDecOpEnum"

def test_comparisonopenum_exists():
    # Check that the Enumeration exists
    assert ComparisonOpEnum is not None

def test_comparisonopenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonOpEnum]
    expected_literals = [
        "LTE",
        "GT",
        "LT",
        "GTE",
        "IN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisonOpEnum"

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
optGrammar_Continue_strategy = st.builds(
    optGrammar_Continue,
)
NamedType_strategy = st.builds(
    NamedType,
)
optGrammar_UnitsLiteral_strategy = st.builds(
    optGrammar_UnitsLiteral,
    value=
        safe_text
)
optGrammar_TimeUnitsLiteral_strategy = st.builds(
    optGrammar_TimeUnitsLiteral,
    value=
        safe_text
)
optGrammar_IntLiteral_strategy = st.builds(
    optGrammar_IntLiteral,
    value=
        st.integers()
)
optGrammar_UnitTypes_strategy = st.builds(
    optGrammar_UnitTypes,
)
optGrammar_DecimalLiteral_strategy = st.builds(
    optGrammar_DecimalLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
optGrammar_HexLiteral_strategy = st.builds(
    optGrammar_HexLiteral,
    value=
        safe_text
)
optGrammar_SecondOperators_strategy = st.builds(
    optGrammar_SecondOperators,
    operator=
        safe_text
)
optGrammar_PrimaryArithmetic_strategy = st.builds(
    optGrammar_PrimaryArithmetic,
)
optGrammar_ArithmeticOperations_strategy = st.builds(
    optGrammar_ArithmeticOperations,
)
optGrammar_IntParameter_strategy = st.builds(
    optGrammar_IntParameter,
)
Literal_strategy = st.builds(
    Literal,
)
optGrammar_GasleftFunction_strategy = st.builds(
    optGrammar_GasleftFunction,
    name=
        safe_text
)
optGrammar_HashFunction_strategy = st.builds(
    optGrammar_HashFunction,
    name=
        safe_text
)
optGrammar_BooleanLiteral_strategy = st.builds(
    optGrammar_BooleanLiteral,
    value=
        safe_text
)
optGrammar_EcrecoverFunction_strategy = st.builds(
    optGrammar_EcrecoverFunction,
    function=
        safe_text
)
optGrammar_MathematicalFunction_strategy = st.builds(
    optGrammar_MathematicalFunction,
    function=
        safe_text
)
optGrammar_StringLiteral_strategy = st.builds(
    optGrammar_StringLiteral,
    value=
        safe_text
)
optGrammar_SpecialLiteral_strategy = st.builds(
    optGrammar_SpecialLiteral,
    name=
        safe_text
)
optGrammar_BlockhashFunction_strategy = st.builds(
    optGrammar_BlockhashFunction,
)
PrimaryArithmetic_strategy = st.builds(
    PrimaryArithmetic,
)
optGrammar_NumericLiteral_strategy = st.builds(
    optGrammar_NumericLiteral,
)
LoopStructures_strategy = st.builds(
    LoopStructures,
)
optGrammar_IfStatement_strategy = st.builds(
    optGrammar_IfStatement,
)
optGrammar_FunctionCall_strategy = st.builds(
    optGrammar_FunctionCall,
)
optGrammar_Statement_strategy = st.builds(
    optGrammar_Statement,
)
optGrammar_ForStatement_strategy = st.builds(
    optGrammar_ForStatement,
)
optGrammar_WhileStatement_strategy = st.builds(
    optGrammar_WhileStatement,
)
Qualifier_strategy = st.builds(
    Qualifier,
)
optGrammar_Index_strategy = st.builds(
    optGrammar_Index,
)
optGrammar_Arguments_strategy = st.builds(
    optGrammar_Arguments,
)
optGrammar_Field_strategy = st.builds(
    optGrammar_Field,
    field=
        safe_text
)
optGrammar_Qualifier_strategy = st.builds(
    optGrammar_Qualifier,
)
optGrammar_ReturnParameterDeclaration_strategy = st.builds(
    optGrammar_ReturnParameterDeclaration,
)
SimpleStatement2_strategy = st.builds(
    SimpleStatement2,
)
SimpleStatement_strategy = st.builds(
    SimpleStatement,
)
optGrammar_VarVariableTupleVariableDeclaration_strategy = st.builds(
    optGrammar_VarVariableTupleVariableDeclaration,
    semicolon=
        st.booleans()
)
optGrammar_StandardVariableDeclaration_strategy = st.builds(
    optGrammar_StandardVariableDeclaration,
    semicolon=
        st.booleans()
)
optGrammar_VarVariableTypeDeclaration_strategy = st.builds(
    optGrammar_VarVariableTypeDeclaration,
    semicolon=
        st.booleans()
)
optGrammar_StandardTypeWithoutQualifiedIdentifier_strategy = st.builds(
    optGrammar_StandardTypeWithoutQualifiedIdentifier,
)
Type_strategy = st.builds(
    Type,
)
optGrammar_StandardType_strategy = st.builds(
    optGrammar_StandardType,
)
optGrammar_ArrayType_strategy = st.builds(
    optGrammar_ArrayType,
)
StandardTypeWithoutQualifiedIdentifier_strategy = st.builds(
    StandardTypeWithoutQualifiedIdentifier,
)
StandardType_strategy = st.builds(
    StandardType,
)
optGrammar_NamedType_strategy = st.builds(
    optGrammar_NamedType,
    type=
        safe_text
)
optGrammar_Type_strategy = st.builds(
    optGrammar_Type,
    isVarType=
        st.booleans()
)
VariableDeclarationOptionalElement_strategy = st.builds(
    VariableDeclarationOptionalElement,
)
optGrammar_IndexedSpecifer_strategy = st.builds(
    optGrammar_IndexedSpecifer,
)
optGrammar_ConstantSpecifier_strategy = st.builds(
    optGrammar_ConstantSpecifier,
)
optGrammar_LocationSpecifier_strategy = st.builds(
    optGrammar_LocationSpecifier,
)
optGrammar_VisibilitySpecifier_strategy = st.builds(
    optGrammar_VisibilitySpecifier,
)
optGrammar_VariableDeclarationOptionalElement_strategy = st.builds(
    optGrammar_VariableDeclarationOptionalElement,
)
optGrammar_ExpressionStatement_strategy = st.builds(
    optGrammar_ExpressionStatement,
    semicolon=
        st.booleans()
)
optGrammar_SimpleStatement2_strategy = st.builds(
    optGrammar_SimpleStatement2,
)
Statement_strategy = st.builds(
    Statement,
)
optGrammar_ContinueStatement_strategy = st.builds(
    optGrammar_ContinueStatement,
)
optGrammar_PlaceHolderStatement_strategy = st.builds(
    optGrammar_PlaceHolderStatement,
)
optGrammar_BreakStatement_strategy = st.builds(
    optGrammar_BreakStatement,
)
optGrammar_EmitStatement_strategy = st.builds(
    optGrammar_EmitStatement,
)
optGrammar_LoopStructures_strategy = st.builds(
    optGrammar_LoopStructures,
    type=
        safe_text
)
optGrammar_ThrowStatement_strategy = st.builds(
    optGrammar_ThrowStatement,
)
optGrammar_DoWhileStatement_strategy = st.builds(
    optGrammar_DoWhileStatement,
)
optGrammar_ReturnStatement_strategy = st.builds(
    optGrammar_ReturnStatement,
)
optGrammar_DeleteStatement_strategy = st.builds(
    optGrammar_DeleteStatement,
)
optGrammar_SimpleStatement_strategy = st.builds(
    optGrammar_SimpleStatement,
)
Expression_strategy = st.builds(
    Expression,
)
optGrammar_BinaryNotExpression_strategy = st.builds(
    optGrammar_BinaryNotExpression,
)
optGrammar_QualifiedIdentifier_strategy = st.builds(
    optGrammar_QualifiedIdentifier,
    identifier=
        safe_text
)
optGrammar_NotExpression_strategy = st.builds(
    optGrammar_NotExpression,
)
optGrammar_Or_strategy = st.builds(
    optGrammar_Or,
)
optGrammar_SpecialExpression_strategy = st.builds(
    optGrammar_SpecialExpression,
    type=
        safe_text
)
optGrammar_BitAnd_strategy = st.builds(
    optGrammar_BitAnd,
)
optGrammar_Shift_strategy = st.builds(
    optGrammar_Shift,
    shiftOp=
        safe_text
)
optGrammar_MulDivMod_strategy = st.builds(
    optGrammar_MulDivMod,
    multipliciativeOp=
        safe_text
)
optGrammar_Exponent_strategy = st.builds(
    optGrammar_Exponent,
)
optGrammar_BitOr_strategy = st.builds(
    optGrammar_BitOr,
)
optGrammar_Equality_strategy = st.builds(
    optGrammar_Equality,
    equalityOp=
        safe_text
)
optGrammar_PostIncDecExpression_strategy = st.builds(
    optGrammar_PostIncDecExpression,
    postOp=
        safe_text
)
optGrammar_TupleSeparator_strategy = st.builds(
    optGrammar_TupleSeparator,
)
optGrammar_PreIncExpression_strategy = st.builds(
    optGrammar_PreIncExpression,
)
optGrammar_Literal_strategy = st.builds(
    optGrammar_Literal,
)
optGrammar_NewExpression_strategy = st.builds(
    optGrammar_NewExpression,
)
optGrammar_AddSub_strategy = st.builds(
    optGrammar_AddSub,
    additionOp=
        safe_text
)
optGrammar_And_strategy = st.builds(
    optGrammar_And,
)
optGrammar_Assignment_strategy = st.builds(
    optGrammar_Assignment,
    assignmentOp=
        safe_text
)
optGrammar_Comparison_strategy = st.builds(
    optGrammar_Comparison,
    comparisonOp=
        safe_text
)
optGrammar_BitXor_strategy = st.builds(
    optGrammar_BitXor,
)
optGrammar_PreDecExpression_strategy = st.builds(
    optGrammar_PreDecExpression,
)
optGrammar_TypeCast_strategy = st.builds(
    optGrammar_TypeCast,
)
optGrammar_SignExpression_strategy = st.builds(
    optGrammar_SignExpression,
    signOp=
        safe_text
)
optGrammar_VariableDeclarationExpression_strategy = st.builds(
    optGrammar_VariableDeclarationExpression,
)
optGrammar_Tuple_strategy = st.builds(
    optGrammar_Tuple,
)
optGrammar_Mapping_strategy = st.builds(
    optGrammar_Mapping,
)
optGrammar_Variable_strategy = st.builds(
    optGrammar_Variable,
    name=
        safe_text
)
optGrammar_EnumValue_strategy = st.builds(
    optGrammar_EnumValue,
    name=
        safe_text
)
optGrammar_ReturnsParameterList_strategy = st.builds(
    optGrammar_ReturnsParameterList,
)
optGrammar_SizedDeclaration_strategy = st.builds(
    optGrammar_SizedDeclaration,
)
optGrammar_SimpleTypeDeclaration_strategy = st.builds(
    optGrammar_SimpleTypeDeclaration,
)
optGrammar_LocationLiteral_strategy = st.builds(
    optGrammar_LocationLiteral,
    type=
        safe_text
)
PrimaryTypeDeclaration_strategy = st.builds(
    PrimaryTypeDeclaration,
)
optGrammar_ArrayableDeclaration_strategy = st.builds(
    optGrammar_ArrayableDeclaration,
)
optGrammar_NonArrayableDeclaration_strategy = st.builds(
    optGrammar_NonArrayableDeclaration,
)
PrimaryTypeDefinitionDeclaration_strategy = st.builds(
    PrimaryTypeDefinitionDeclaration,
)
optGrammar_PrimaryTypeDeclaration_strategy = st.builds(
    optGrammar_PrimaryTypeDeclaration,
    name=
        safe_text,
    constant=
        st.booleans()
)
optGrammar_FunctionCallArg_strategy = st.builds(
    optGrammar_FunctionCallArg,
    name=
        safe_text
)
optGrammar_FunctionCallArguments_strategy = st.builds(
    optGrammar_FunctionCallArguments,
)
optGrammar_Expression_strategy = st.builds(
    optGrammar_Expression,
)
FunctionCallArguments_strategy = st.builds(
    FunctionCallArguments,
)
optGrammar_FunctionCallListArguments_strategy = st.builds(
    optGrammar_FunctionCallListArguments,
)
optGrammar_Body_strategy = st.builds(
    optGrammar_Body,
)
optGrammar_VisibilityLiteral_strategy = st.builds(
    optGrammar_VisibilityLiteral,
    type=
        safe_text
)
optGrammar_InheritanceSpecifier_strategy = st.builds(
    optGrammar_InheritanceSpecifier,
)
optGrammar_SymbolAlias_strategy = st.builds(
    optGrammar_SymbolAlias,
    symbol=
        safe_text,
    alias=
        safe_text
)
optGrammar_versionOperator_strategy = st.builds(
    optGrammar_versionOperator,
    value=
        safe_text
)
optGrammar_Contract_strategy = st.builds(
    optGrammar_Contract,
    name=
        safe_text
)
optGrammar_ImportDirective_strategy = st.builds(
    optGrammar_ImportDirective,
    unitAlias=
        safe_text,
    importURI=
        safe_text
)
optGrammar_ModifierInvocation_strategy = st.builds(
    optGrammar_ModifierInvocation,
)
optGrammar_Const_strategy = st.builds(
    optGrammar_Const,
)
optGrammar_StateMutability_strategy = st.builds(
    optGrammar_StateMutability,
    type=
        safe_text
)
optGrammar_ParameterList_strategy = st.builds(
    optGrammar_ParameterList,
)
DefinitionBody_strategy = st.builds(
    DefinitionBody,
)
optGrammar_StructDefinition_strategy = st.builds(
    optGrammar_StructDefinition,
    name=
        safe_text
)
optGrammar_Event_strategy = st.builds(
    optGrammar_Event,
    name=
        safe_text,
    isAnonymous=
        st.booleans()
)
optGrammar_EnumDefinition_strategy = st.builds(
    optGrammar_EnumDefinition,
    name=
        safe_text
)
optGrammar_PrimaryTypeDefinitionDeclaration_strategy = st.builds(
    optGrammar_PrimaryTypeDefinitionDeclaration,
)
optGrammar_Modifier_strategy = st.builds(
    optGrammar_Modifier,
    name=
        safe_text
)
optGrammar_FunctionDefinition_strategy = st.builds(
    optGrammar_FunctionDefinition,
    name=
        safe_text
)
optGrammar_ConstructorDefinition_strategy = st.builds(
    optGrammar_ConstructorDefinition,
    name=
        safe_text
)
optGrammar_DefinitionBody_strategy = st.builds(
    optGrammar_DefinitionBody,
)
optGrammar_PragmaDirective_strategy = st.builds(
    optGrammar_PragmaDirective,
)
optGrammar_Model_strategy = st.builds(
    optGrammar_Model,
)

@given(instance=ContinueStatement_strategy)
@settings(max_examples=50)
def test_continuestatement_instantiation(instance):
    assert isinstance(instance, ContinueStatement)

@given(instance=optGrammar_Continue_strategy)
@settings(max_examples=50)
def test_optgrammar_continue_instantiation(instance):
    assert isinstance(instance, optGrammar_Continue)

@given(instance=NamedType_strategy)
@settings(max_examples=50)
def test_namedtype_instantiation(instance):
    assert isinstance(instance, NamedType)

@given(instance=optGrammar_UnitsLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar_unitsliteral_instantiation(instance):
    assert isinstance(instance, optGrammar_UnitsLiteral)



@given(instance=optGrammar_UnitsLiteral_strategy)
def test_optgrammar_unitsliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=optGrammar_TimeUnitsLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar_timeunitsliteral_instantiation(instance):
    assert isinstance(instance, optGrammar_TimeUnitsLiteral)



@given(instance=optGrammar_TimeUnitsLiteral_strategy)
def test_optgrammar_timeunitsliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=optGrammar_IntLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar_intliteral_instantiation(instance):
    assert isinstance(instance, optGrammar_IntLiteral)



@given(instance=optGrammar_IntLiteral_strategy)
def test_optgrammar_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=optGrammar_UnitTypes_strategy)
@settings(max_examples=50)
def test_optgrammar_unittypes_instantiation(instance):
    assert isinstance(instance, optGrammar_UnitTypes)

@given(instance=optGrammar_DecimalLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar_decimalliteral_instantiation(instance):
    assert isinstance(instance, optGrammar_DecimalLiteral)



@given(instance=optGrammar_DecimalLiteral_strategy)
def test_optgrammar_decimalliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=optGrammar_HexLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar_hexliteral_instantiation(instance):
    assert isinstance(instance, optGrammar_HexLiteral)



@given(instance=optGrammar_HexLiteral_strategy)
def test_optgrammar_hexliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=optGrammar_SecondOperators_strategy)
@settings(max_examples=50)
def test_optgrammar_secondoperators_instantiation(instance):
    assert isinstance(instance, optGrammar_SecondOperators)



@given(instance=optGrammar_SecondOperators_strategy)
def test_optgrammar_secondoperators_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=optGrammar_PrimaryArithmetic_strategy)
@settings(max_examples=50)
def test_optgrammar_primaryarithmetic_instantiation(instance):
    assert isinstance(instance, optGrammar_PrimaryArithmetic)

@given(instance=optGrammar_ArithmeticOperations_strategy)
@settings(max_examples=50)
def test_optgrammar_arithmeticoperations_instantiation(instance):
    assert isinstance(instance, optGrammar_ArithmeticOperations)

@given(instance=optGrammar_IntParameter_strategy)
@settings(max_examples=50)
def test_optgrammar_intparameter_instantiation(instance):
    assert isinstance(instance, optGrammar_IntParameter)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=optGrammar_GasleftFunction_strategy)
@settings(max_examples=50)
def test_optgrammar_gasleftfunction_instantiation(instance):
    assert isinstance(instance, optGrammar_GasleftFunction)



@given(instance=optGrammar_GasleftFunction_strategy)
def test_optgrammar_gasleftfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar_HashFunction_strategy)
@settings(max_examples=50)
def test_optgrammar_hashfunction_instantiation(instance):
    assert isinstance(instance, optGrammar_HashFunction)



@given(instance=optGrammar_HashFunction_strategy)
def test_optgrammar_hashfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar_booleanliteral_instantiation(instance):
    assert isinstance(instance, optGrammar_BooleanLiteral)



@given(instance=optGrammar_BooleanLiteral_strategy)
def test_optgrammar_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=optGrammar_EcrecoverFunction_strategy)
@settings(max_examples=50)
def test_optgrammar_ecrecoverfunction_instantiation(instance):
    assert isinstance(instance, optGrammar_EcrecoverFunction)



@given(instance=optGrammar_EcrecoverFunction_strategy)
def test_optgrammar_ecrecoverfunction_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=optGrammar_MathematicalFunction_strategy)
@settings(max_examples=50)
def test_optgrammar_mathematicalfunction_instantiation(instance):
    assert isinstance(instance, optGrammar_MathematicalFunction)



@given(instance=optGrammar_MathematicalFunction_strategy)
def test_optgrammar_mathematicalfunction_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=optGrammar_StringLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar_stringliteral_instantiation(instance):
    assert isinstance(instance, optGrammar_StringLiteral)



@given(instance=optGrammar_StringLiteral_strategy)
def test_optgrammar_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=optGrammar_SpecialLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar_specialliteral_instantiation(instance):
    assert isinstance(instance, optGrammar_SpecialLiteral)



@given(instance=optGrammar_SpecialLiteral_strategy)
def test_optgrammar_specialliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar_BlockhashFunction_strategy)
@settings(max_examples=50)
def test_optgrammar_blockhashfunction_instantiation(instance):
    assert isinstance(instance, optGrammar_BlockhashFunction)

@given(instance=PrimaryArithmetic_strategy)
@settings(max_examples=50)
def test_primaryarithmetic_instantiation(instance):
    assert isinstance(instance, PrimaryArithmetic)

@given(instance=optGrammar_NumericLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar_numericliteral_instantiation(instance):
    assert isinstance(instance, optGrammar_NumericLiteral)

@given(instance=LoopStructures_strategy)
@settings(max_examples=50)
def test_loopstructures_instantiation(instance):
    assert isinstance(instance, LoopStructures)

@given(instance=optGrammar_IfStatement_strategy)
@settings(max_examples=50)
def test_optgrammar_ifstatement_instantiation(instance):
    assert isinstance(instance, optGrammar_IfStatement)

@given(instance=optGrammar_FunctionCall_strategy)
@settings(max_examples=50)
def test_optgrammar_functioncall_instantiation(instance):
    assert isinstance(instance, optGrammar_FunctionCall)

@given(instance=optGrammar_Statement_strategy)
@settings(max_examples=50)
def test_optgrammar_statement_instantiation(instance):
    assert isinstance(instance, optGrammar_Statement)

@given(instance=optGrammar_ForStatement_strategy)
@settings(max_examples=50)
def test_optgrammar_forstatement_instantiation(instance):
    assert isinstance(instance, optGrammar_ForStatement)

@given(instance=optGrammar_WhileStatement_strategy)
@settings(max_examples=50)
def test_optgrammar_whilestatement_instantiation(instance):
    assert isinstance(instance, optGrammar_WhileStatement)

@given(instance=Qualifier_strategy)
@settings(max_examples=50)
def test_qualifier_instantiation(instance):
    assert isinstance(instance, Qualifier)

@given(instance=optGrammar_Index_strategy)
@settings(max_examples=50)
def test_optgrammar_index_instantiation(instance):
    assert isinstance(instance, optGrammar_Index)

@given(instance=optGrammar_Arguments_strategy)
@settings(max_examples=50)
def test_optgrammar_arguments_instantiation(instance):
    assert isinstance(instance, optGrammar_Arguments)

@given(instance=optGrammar_Field_strategy)
@settings(max_examples=50)
def test_optgrammar_field_instantiation(instance):
    assert isinstance(instance, optGrammar_Field)



@given(instance=optGrammar_Field_strategy)
def test_optgrammar_field_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=optGrammar_Qualifier_strategy)
@settings(max_examples=50)
def test_optgrammar_qualifier_instantiation(instance):
    assert isinstance(instance, optGrammar_Qualifier)

@given(instance=optGrammar_ReturnParameterDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar_returnparameterdeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar_ReturnParameterDeclaration)

@given(instance=SimpleStatement2_strategy)
@settings(max_examples=50)
def test_simplestatement2_instantiation(instance):
    assert isinstance(instance, SimpleStatement2)

@given(instance=SimpleStatement_strategy)
@settings(max_examples=50)
def test_simplestatement_instantiation(instance):
    assert isinstance(instance, SimpleStatement)

@given(instance=optGrammar_VarVariableTupleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar_varvariabletuplevariabledeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar_VarVariableTupleVariableDeclaration)



@given(instance=optGrammar_VarVariableTupleVariableDeclaration_strategy)
def test_optgrammar_varvariabletuplevariabledeclaration_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=optGrammar_StandardVariableDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar_standardvariabledeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar_StandardVariableDeclaration)



@given(instance=optGrammar_StandardVariableDeclaration_strategy)
def test_optgrammar_standardvariabledeclaration_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=optGrammar_VarVariableTypeDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar_varvariabletypedeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar_VarVariableTypeDeclaration)



@given(instance=optGrammar_VarVariableTypeDeclaration_strategy)
def test_optgrammar_varvariabletypedeclaration_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=optGrammar_StandardTypeWithoutQualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_optgrammar_standardtypewithoutqualifiedidentifier_instantiation(instance):
    assert isinstance(instance, optGrammar_StandardTypeWithoutQualifiedIdentifier)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=optGrammar_StandardType_strategy)
@settings(max_examples=50)
def test_optgrammar_standardtype_instantiation(instance):
    assert isinstance(instance, optGrammar_StandardType)

@given(instance=optGrammar_ArrayType_strategy)
@settings(max_examples=50)
def test_optgrammar_arraytype_instantiation(instance):
    assert isinstance(instance, optGrammar_ArrayType)

@given(instance=StandardTypeWithoutQualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_standardtypewithoutqualifiedidentifier_instantiation(instance):
    assert isinstance(instance, StandardTypeWithoutQualifiedIdentifier)

@given(instance=StandardType_strategy)
@settings(max_examples=50)
def test_standardtype_instantiation(instance):
    assert isinstance(instance, StandardType)

@given(instance=optGrammar_NamedType_strategy)
@settings(max_examples=50)
def test_optgrammar_namedtype_instantiation(instance):
    assert isinstance(instance, optGrammar_NamedType)



@given(instance=optGrammar_NamedType_strategy)
def test_optgrammar_namedtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=optGrammar_Type_strategy)
@settings(max_examples=50)
def test_optgrammar_type_instantiation(instance):
    assert isinstance(instance, optGrammar_Type)



@given(instance=optGrammar_Type_strategy)
def test_optgrammar_type_isVarType_setter(instance):
    original = instance.isVarType
    instance.isVarType = original
    assert instance.isVarType == original

@given(instance=VariableDeclarationOptionalElement_strategy)
@settings(max_examples=50)
def test_variabledeclarationoptionalelement_instantiation(instance):
    assert isinstance(instance, VariableDeclarationOptionalElement)

@given(instance=optGrammar_IndexedSpecifer_strategy)
@settings(max_examples=50)
def test_optgrammar_indexedspecifer_instantiation(instance):
    assert isinstance(instance, optGrammar_IndexedSpecifer)

@given(instance=optGrammar_ConstantSpecifier_strategy)
@settings(max_examples=50)
def test_optgrammar_constantspecifier_instantiation(instance):
    assert isinstance(instance, optGrammar_ConstantSpecifier)

@given(instance=optGrammar_LocationSpecifier_strategy)
@settings(max_examples=50)
def test_optgrammar_locationspecifier_instantiation(instance):
    assert isinstance(instance, optGrammar_LocationSpecifier)

@given(instance=optGrammar_VisibilitySpecifier_strategy)
@settings(max_examples=50)
def test_optgrammar_visibilityspecifier_instantiation(instance):
    assert isinstance(instance, optGrammar_VisibilitySpecifier)

@given(instance=optGrammar_VariableDeclarationOptionalElement_strategy)
@settings(max_examples=50)
def test_optgrammar_variabledeclarationoptionalelement_instantiation(instance):
    assert isinstance(instance, optGrammar_VariableDeclarationOptionalElement)

@given(instance=optGrammar_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_optgrammar_expressionstatement_instantiation(instance):
    assert isinstance(instance, optGrammar_ExpressionStatement)



@given(instance=optGrammar_ExpressionStatement_strategy)
def test_optgrammar_expressionstatement_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=optGrammar_SimpleStatement2_strategy)
@settings(max_examples=50)
def test_optgrammar_simplestatement2_instantiation(instance):
    assert isinstance(instance, optGrammar_SimpleStatement2)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=optGrammar_ContinueStatement_strategy)
@settings(max_examples=50)
def test_optgrammar_continuestatement_instantiation(instance):
    assert isinstance(instance, optGrammar_ContinueStatement)

@given(instance=optGrammar_PlaceHolderStatement_strategy)
@settings(max_examples=50)
def test_optgrammar_placeholderstatement_instantiation(instance):
    assert isinstance(instance, optGrammar_PlaceHolderStatement)

@given(instance=optGrammar_BreakStatement_strategy)
@settings(max_examples=50)
def test_optgrammar_breakstatement_instantiation(instance):
    assert isinstance(instance, optGrammar_BreakStatement)

@given(instance=optGrammar_EmitStatement_strategy)
@settings(max_examples=50)
def test_optgrammar_emitstatement_instantiation(instance):
    assert isinstance(instance, optGrammar_EmitStatement)

@given(instance=optGrammar_LoopStructures_strategy)
@settings(max_examples=50)
def test_optgrammar_loopstructures_instantiation(instance):
    assert isinstance(instance, optGrammar_LoopStructures)



@given(instance=optGrammar_LoopStructures_strategy)
def test_optgrammar_loopstructures_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=optGrammar_ThrowStatement_strategy)
@settings(max_examples=50)
def test_optgrammar_throwstatement_instantiation(instance):
    assert isinstance(instance, optGrammar_ThrowStatement)

@given(instance=optGrammar_DoWhileStatement_strategy)
@settings(max_examples=50)
def test_optgrammar_dowhilestatement_instantiation(instance):
    assert isinstance(instance, optGrammar_DoWhileStatement)

@given(instance=optGrammar_ReturnStatement_strategy)
@settings(max_examples=50)
def test_optgrammar_returnstatement_instantiation(instance):
    assert isinstance(instance, optGrammar_ReturnStatement)

@given(instance=optGrammar_DeleteStatement_strategy)
@settings(max_examples=50)
def test_optgrammar_deletestatement_instantiation(instance):
    assert isinstance(instance, optGrammar_DeleteStatement)

@given(instance=optGrammar_SimpleStatement_strategy)
@settings(max_examples=50)
def test_optgrammar_simplestatement_instantiation(instance):
    assert isinstance(instance, optGrammar_SimpleStatement)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=optGrammar_BinaryNotExpression_strategy)
@settings(max_examples=50)
def test_optgrammar_binarynotexpression_instantiation(instance):
    assert isinstance(instance, optGrammar_BinaryNotExpression)

@given(instance=optGrammar_QualifiedIdentifier_strategy)
@settings(max_examples=50)
def test_optgrammar_qualifiedidentifier_instantiation(instance):
    assert isinstance(instance, optGrammar_QualifiedIdentifier)



@given(instance=optGrammar_QualifiedIdentifier_strategy)
def test_optgrammar_qualifiedidentifier_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=optGrammar_NotExpression_strategy)
@settings(max_examples=50)
def test_optgrammar_notexpression_instantiation(instance):
    assert isinstance(instance, optGrammar_NotExpression)

@given(instance=optGrammar_Or_strategy)
@settings(max_examples=50)
def test_optgrammar_or_instantiation(instance):
    assert isinstance(instance, optGrammar_Or)

@given(instance=optGrammar_SpecialExpression_strategy)
@settings(max_examples=50)
def test_optgrammar_specialexpression_instantiation(instance):
    assert isinstance(instance, optGrammar_SpecialExpression)



@given(instance=optGrammar_SpecialExpression_strategy)
def test_optgrammar_specialexpression_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=optGrammar_BitAnd_strategy)
@settings(max_examples=50)
def test_optgrammar_bitand_instantiation(instance):
    assert isinstance(instance, optGrammar_BitAnd)

@given(instance=optGrammar_Shift_strategy)
@settings(max_examples=50)
def test_optgrammar_shift_instantiation(instance):
    assert isinstance(instance, optGrammar_Shift)



@given(instance=optGrammar_Shift_strategy)
def test_optgrammar_shift_shiftOp_setter(instance):
    original = instance.shiftOp
    instance.shiftOp = original
    assert instance.shiftOp == original

@given(instance=optGrammar_MulDivMod_strategy)
@settings(max_examples=50)
def test_optgrammar_muldivmod_instantiation(instance):
    assert isinstance(instance, optGrammar_MulDivMod)



@given(instance=optGrammar_MulDivMod_strategy)
def test_optgrammar_muldivmod_multipliciativeOp_setter(instance):
    original = instance.multipliciativeOp
    instance.multipliciativeOp = original
    assert instance.multipliciativeOp == original

@given(instance=optGrammar_Exponent_strategy)
@settings(max_examples=50)
def test_optgrammar_exponent_instantiation(instance):
    assert isinstance(instance, optGrammar_Exponent)

@given(instance=optGrammar_BitOr_strategy)
@settings(max_examples=50)
def test_optgrammar_bitor_instantiation(instance):
    assert isinstance(instance, optGrammar_BitOr)

@given(instance=optGrammar_Equality_strategy)
@settings(max_examples=50)
def test_optgrammar_equality_instantiation(instance):
    assert isinstance(instance, optGrammar_Equality)



@given(instance=optGrammar_Equality_strategy)
def test_optgrammar_equality_equalityOp_setter(instance):
    original = instance.equalityOp
    instance.equalityOp = original
    assert instance.equalityOp == original

@given(instance=optGrammar_PostIncDecExpression_strategy)
@settings(max_examples=50)
def test_optgrammar_postincdecexpression_instantiation(instance):
    assert isinstance(instance, optGrammar_PostIncDecExpression)



@given(instance=optGrammar_PostIncDecExpression_strategy)
def test_optgrammar_postincdecexpression_postOp_setter(instance):
    original = instance.postOp
    instance.postOp = original
    assert instance.postOp == original

@given(instance=optGrammar_TupleSeparator_strategy)
@settings(max_examples=50)
def test_optgrammar_tupleseparator_instantiation(instance):
    assert isinstance(instance, optGrammar_TupleSeparator)

@given(instance=optGrammar_PreIncExpression_strategy)
@settings(max_examples=50)
def test_optgrammar_preincexpression_instantiation(instance):
    assert isinstance(instance, optGrammar_PreIncExpression)

@given(instance=optGrammar_Literal_strategy)
@settings(max_examples=50)
def test_optgrammar_literal_instantiation(instance):
    assert isinstance(instance, optGrammar_Literal)

@given(instance=optGrammar_NewExpression_strategy)
@settings(max_examples=50)
def test_optgrammar_newexpression_instantiation(instance):
    assert isinstance(instance, optGrammar_NewExpression)

@given(instance=optGrammar_AddSub_strategy)
@settings(max_examples=50)
def test_optgrammar_addsub_instantiation(instance):
    assert isinstance(instance, optGrammar_AddSub)



@given(instance=optGrammar_AddSub_strategy)
def test_optgrammar_addsub_additionOp_setter(instance):
    original = instance.additionOp
    instance.additionOp = original
    assert instance.additionOp == original

@given(instance=optGrammar_And_strategy)
@settings(max_examples=50)
def test_optgrammar_and_instantiation(instance):
    assert isinstance(instance, optGrammar_And)

@given(instance=optGrammar_Assignment_strategy)
@settings(max_examples=50)
def test_optgrammar_assignment_instantiation(instance):
    assert isinstance(instance, optGrammar_Assignment)



@given(instance=optGrammar_Assignment_strategy)
def test_optgrammar_assignment_assignmentOp_setter(instance):
    original = instance.assignmentOp
    instance.assignmentOp = original
    assert instance.assignmentOp == original

@given(instance=optGrammar_Comparison_strategy)
@settings(max_examples=50)
def test_optgrammar_comparison_instantiation(instance):
    assert isinstance(instance, optGrammar_Comparison)



@given(instance=optGrammar_Comparison_strategy)
def test_optgrammar_comparison_comparisonOp_setter(instance):
    original = instance.comparisonOp
    instance.comparisonOp = original
    assert instance.comparisonOp == original

@given(instance=optGrammar_BitXor_strategy)
@settings(max_examples=50)
def test_optgrammar_bitxor_instantiation(instance):
    assert isinstance(instance, optGrammar_BitXor)

@given(instance=optGrammar_PreDecExpression_strategy)
@settings(max_examples=50)
def test_optgrammar_predecexpression_instantiation(instance):
    assert isinstance(instance, optGrammar_PreDecExpression)

@given(instance=optGrammar_TypeCast_strategy)
@settings(max_examples=50)
def test_optgrammar_typecast_instantiation(instance):
    assert isinstance(instance, optGrammar_TypeCast)

@given(instance=optGrammar_SignExpression_strategy)
@settings(max_examples=50)
def test_optgrammar_signexpression_instantiation(instance):
    assert isinstance(instance, optGrammar_SignExpression)



@given(instance=optGrammar_SignExpression_strategy)
def test_optgrammar_signexpression_signOp_setter(instance):
    original = instance.signOp
    instance.signOp = original
    assert instance.signOp == original

@given(instance=optGrammar_VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_optgrammar_variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, optGrammar_VariableDeclarationExpression)

@given(instance=optGrammar_Tuple_strategy)
@settings(max_examples=50)
def test_optgrammar_tuple_instantiation(instance):
    assert isinstance(instance, optGrammar_Tuple)

@given(instance=optGrammar_Mapping_strategy)
@settings(max_examples=50)
def test_optgrammar_mapping_instantiation(instance):
    assert isinstance(instance, optGrammar_Mapping)

@given(instance=optGrammar_Variable_strategy)
@settings(max_examples=50)
def test_optgrammar_variable_instantiation(instance):
    assert isinstance(instance, optGrammar_Variable)



@given(instance=optGrammar_Variable_strategy)
def test_optgrammar_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar_EnumValue_strategy)
@settings(max_examples=50)
def test_optgrammar_enumvalue_instantiation(instance):
    assert isinstance(instance, optGrammar_EnumValue)



@given(instance=optGrammar_EnumValue_strategy)
def test_optgrammar_enumvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar_ReturnsParameterList_strategy)
@settings(max_examples=50)
def test_optgrammar_returnsparameterlist_instantiation(instance):
    assert isinstance(instance, optGrammar_ReturnsParameterList)

@given(instance=optGrammar_SizedDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar_sizeddeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar_SizedDeclaration)

@given(instance=optGrammar_SimpleTypeDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar_simpletypedeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar_SimpleTypeDeclaration)

@given(instance=optGrammar_LocationLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar_locationliteral_instantiation(instance):
    assert isinstance(instance, optGrammar_LocationLiteral)



@given(instance=optGrammar_LocationLiteral_strategy)
def test_optgrammar_locationliteral_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=PrimaryTypeDeclaration_strategy)
@settings(max_examples=50)
def test_primarytypedeclaration_instantiation(instance):
    assert isinstance(instance, PrimaryTypeDeclaration)

@given(instance=optGrammar_ArrayableDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar_arrayabledeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar_ArrayableDeclaration)

@given(instance=optGrammar_NonArrayableDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar_nonarrayabledeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar_NonArrayableDeclaration)

@given(instance=PrimaryTypeDefinitionDeclaration_strategy)
@settings(max_examples=50)
def test_primarytypedefinitiondeclaration_instantiation(instance):
    assert isinstance(instance, PrimaryTypeDefinitionDeclaration)

@given(instance=optGrammar_PrimaryTypeDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar_primarytypedeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar_PrimaryTypeDeclaration)



@given(instance=optGrammar_PrimaryTypeDeclaration_strategy)
def test_optgrammar_primarytypedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=optGrammar_PrimaryTypeDeclaration_strategy)
def test_optgrammar_primarytypedeclaration_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=optGrammar_FunctionCallArg_strategy)
@settings(max_examples=50)
def test_optgrammar_functioncallarg_instantiation(instance):
    assert isinstance(instance, optGrammar_FunctionCallArg)



@given(instance=optGrammar_FunctionCallArg_strategy)
def test_optgrammar_functioncallarg_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar_FunctionCallArguments_strategy)
@settings(max_examples=50)
def test_optgrammar_functioncallarguments_instantiation(instance):
    assert isinstance(instance, optGrammar_FunctionCallArguments)

@given(instance=optGrammar_Expression_strategy)
@settings(max_examples=50)
def test_optgrammar_expression_instantiation(instance):
    assert isinstance(instance, optGrammar_Expression)

@given(instance=FunctionCallArguments_strategy)
@settings(max_examples=50)
def test_functioncallarguments_instantiation(instance):
    assert isinstance(instance, FunctionCallArguments)

@given(instance=optGrammar_FunctionCallListArguments_strategy)
@settings(max_examples=50)
def test_optgrammar_functioncalllistarguments_instantiation(instance):
    assert isinstance(instance, optGrammar_FunctionCallListArguments)

@given(instance=optGrammar_Body_strategy)
@settings(max_examples=50)
def test_optgrammar_body_instantiation(instance):
    assert isinstance(instance, optGrammar_Body)

@given(instance=optGrammar_VisibilityLiteral_strategy)
@settings(max_examples=50)
def test_optgrammar_visibilityliteral_instantiation(instance):
    assert isinstance(instance, optGrammar_VisibilityLiteral)



@given(instance=optGrammar_VisibilityLiteral_strategy)
def test_optgrammar_visibilityliteral_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=optGrammar_InheritanceSpecifier_strategy)
@settings(max_examples=50)
def test_optgrammar_inheritancespecifier_instantiation(instance):
    assert isinstance(instance, optGrammar_InheritanceSpecifier)

@given(instance=optGrammar_SymbolAlias_strategy)
@settings(max_examples=50)
def test_optgrammar_symbolalias_instantiation(instance):
    assert isinstance(instance, optGrammar_SymbolAlias)



@given(instance=optGrammar_SymbolAlias_strategy)
def test_optgrammar_symbolalias_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original



@given(instance=optGrammar_SymbolAlias_strategy)
def test_optgrammar_symbolalias_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=optGrammar_versionOperator_strategy)
@settings(max_examples=50)
def test_optgrammar_versionoperator_instantiation(instance):
    assert isinstance(instance, optGrammar_versionOperator)



@given(instance=optGrammar_versionOperator_strategy)
def test_optgrammar_versionoperator_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=optGrammar_Contract_strategy)
@settings(max_examples=50)
def test_optgrammar_contract_instantiation(instance):
    assert isinstance(instance, optGrammar_Contract)



@given(instance=optGrammar_Contract_strategy)
def test_optgrammar_contract_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar_ImportDirective_strategy)
@settings(max_examples=50)
def test_optgrammar_importdirective_instantiation(instance):
    assert isinstance(instance, optGrammar_ImportDirective)



@given(instance=optGrammar_ImportDirective_strategy)
def test_optgrammar_importdirective_unitAlias_setter(instance):
    original = instance.unitAlias
    instance.unitAlias = original
    assert instance.unitAlias == original



@given(instance=optGrammar_ImportDirective_strategy)
def test_optgrammar_importdirective_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=optGrammar_ModifierInvocation_strategy)
@settings(max_examples=50)
def test_optgrammar_modifierinvocation_instantiation(instance):
    assert isinstance(instance, optGrammar_ModifierInvocation)

@given(instance=optGrammar_Const_strategy)
@settings(max_examples=50)
def test_optgrammar_const_instantiation(instance):
    assert isinstance(instance, optGrammar_Const)

@given(instance=optGrammar_StateMutability_strategy)
@settings(max_examples=50)
def test_optgrammar_statemutability_instantiation(instance):
    assert isinstance(instance, optGrammar_StateMutability)



@given(instance=optGrammar_StateMutability_strategy)
def test_optgrammar_statemutability_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=optGrammar_ParameterList_strategy)
@settings(max_examples=50)
def test_optgrammar_parameterlist_instantiation(instance):
    assert isinstance(instance, optGrammar_ParameterList)

@given(instance=DefinitionBody_strategy)
@settings(max_examples=50)
def test_definitionbody_instantiation(instance):
    assert isinstance(instance, DefinitionBody)

@given(instance=optGrammar_StructDefinition_strategy)
@settings(max_examples=50)
def test_optgrammar_structdefinition_instantiation(instance):
    assert isinstance(instance, optGrammar_StructDefinition)



@given(instance=optGrammar_StructDefinition_strategy)
def test_optgrammar_structdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar_Event_strategy)
@settings(max_examples=50)
def test_optgrammar_event_instantiation(instance):
    assert isinstance(instance, optGrammar_Event)



@given(instance=optGrammar_Event_strategy)
def test_optgrammar_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=optGrammar_Event_strategy)
def test_optgrammar_event_isAnonymous_setter(instance):
    original = instance.isAnonymous
    instance.isAnonymous = original
    assert instance.isAnonymous == original

@given(instance=optGrammar_EnumDefinition_strategy)
@settings(max_examples=50)
def test_optgrammar_enumdefinition_instantiation(instance):
    assert isinstance(instance, optGrammar_EnumDefinition)



@given(instance=optGrammar_EnumDefinition_strategy)
def test_optgrammar_enumdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar_PrimaryTypeDefinitionDeclaration_strategy)
@settings(max_examples=50)
def test_optgrammar_primarytypedefinitiondeclaration_instantiation(instance):
    assert isinstance(instance, optGrammar_PrimaryTypeDefinitionDeclaration)

@given(instance=optGrammar_Modifier_strategy)
@settings(max_examples=50)
def test_optgrammar_modifier_instantiation(instance):
    assert isinstance(instance, optGrammar_Modifier)



@given(instance=optGrammar_Modifier_strategy)
def test_optgrammar_modifier_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar_FunctionDefinition_strategy)
@settings(max_examples=50)
def test_optgrammar_functiondefinition_instantiation(instance):
    assert isinstance(instance, optGrammar_FunctionDefinition)



@given(instance=optGrammar_FunctionDefinition_strategy)
def test_optgrammar_functiondefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar_ConstructorDefinition_strategy)
@settings(max_examples=50)
def test_optgrammar_constructordefinition_instantiation(instance):
    assert isinstance(instance, optGrammar_ConstructorDefinition)



@given(instance=optGrammar_ConstructorDefinition_strategy)
def test_optgrammar_constructordefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=optGrammar_DefinitionBody_strategy)
@settings(max_examples=50)
def test_optgrammar_definitionbody_instantiation(instance):
    assert isinstance(instance, optGrammar_DefinitionBody)

@given(instance=optGrammar_PragmaDirective_strategy)
@settings(max_examples=50)
def test_optgrammar_pragmadirective_instantiation(instance):
    assert isinstance(instance, optGrammar_PragmaDirective)

@given(instance=optGrammar_Model_strategy)
@settings(max_examples=50)
def test_optgrammar_model_instantiation(instance):
    assert isinstance(instance, optGrammar_Model)

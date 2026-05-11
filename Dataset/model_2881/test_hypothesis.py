import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Index,
    express::IndexTerminal,
    IndexTerminal,
    express::IntLiteral,
    express::VarLiteral,
    express::Index,
    VarOrAttrib,
    express::IndexedVar,
    express::AttributeVar,
    express::SimpleVar,
    express::VarOrAttrib,
    express::CaseAction,
    Statement,
    express::EscapeStatement,
    express::Assignment,
    express::ReturnStatement,
    express::CaseStatement,
    express::IfStatement,
    express::RepeatStatement,
    express::SequenceStatement,
    express::LiteralType,
    BuiltInType,
    express::BinaryType,
    express::IntegerType,
    express::RealType,
    express::LogicalType,
    express::NumberType,
    express::BooleanType,
    express::StringType,
    DataType,
    express::EnumType,
    express::SelectType,
    express::CollectionType,
    express::GenericType,
    express::ReferenceType,
    express::BuiltInType,
    express::Intervall,
    express::FormalParam,
    express::ParameterList,
    express::FunctionExpression,
    express::Line,
    express::Statement,
    express::LocalVar,
    express::Function,
    express::ConstantVal,
    express::TypeNameList,
    express::Reference,
    express::UniqueRule,
    express::Attribute,
    express::DataType,
    ExpressConcept,
    express::Entity,
    express::WhereRule,
    express::ExpressConcept,
    express::Rule,
    express::Type,
    express::Schema,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_index_is_not_abstract():
    assert not inspect.isabstract(Index)


def test_index_constructor_exists():
    assert callable(Index.__init__)


def test_index_constructor_args():
    sig = inspect.signature(Index.__init__)
    params = list(sig.parameters.keys())



def test_express::indexterminal_is_not_abstract():
    assert not inspect.isabstract(express::IndexTerminal)


def test_express::indexterminal_constructor_exists():
    assert callable(express::IndexTerminal.__init__)


def test_express::indexterminal_constructor_args():
    sig = inspect.signature(express::IndexTerminal.__init__)
    params = list(sig.parameters.keys())



def test_indexterminal_is_not_abstract():
    assert not inspect.isabstract(IndexTerminal)


def test_indexterminal_constructor_exists():
    assert callable(IndexTerminal.__init__)


def test_indexterminal_constructor_args():
    sig = inspect.signature(IndexTerminal.__init__)
    params = list(sig.parameters.keys())



def test_express::intliteral_is_not_abstract():
    assert not inspect.isabstract(express::IntLiteral)


def test_express::intliteral_constructor_exists():
    assert callable(express::IntLiteral.__init__)


def test_express::intliteral_constructor_args():
    sig = inspect.signature(express::IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_express::intliteral_has_value():
    assert hasattr(express::IntLiteral, "value")
    descriptor = None
    for klass in express::IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_express::varliteral_is_not_abstract():
    assert not inspect.isabstract(express::VarLiteral)


def test_express::varliteral_constructor_exists():
    assert callable(express::VarLiteral.__init__)


def test_express::varliteral_constructor_args():
    sig = inspect.signature(express::VarLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_express::varliteral_has_value():
    assert hasattr(express::VarLiteral, "value")
    descriptor = None
    for klass in express::VarLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_express::index_is_not_abstract():
    assert not inspect.isabstract(express::Index)


def test_express::index_constructor_exists():
    assert callable(express::Index.__init__)


def test_express::index_constructor_args():
    sig = inspect.signature(express::Index.__init__)
    params = list(sig.parameters.keys())



def test_varorattrib_is_not_abstract():
    assert not inspect.isabstract(VarOrAttrib)


def test_varorattrib_constructor_exists():
    assert callable(VarOrAttrib.__init__)


def test_varorattrib_constructor_args():
    sig = inspect.signature(VarOrAttrib.__init__)
    params = list(sig.parameters.keys())



def test_express::indexedvar_is_not_abstract():
    assert not inspect.isabstract(express::IndexedVar)


def test_express::indexedvar_constructor_exists():
    assert callable(express::IndexedVar.__init__)


def test_express::indexedvar_constructor_args():
    sig = inspect.signature(express::IndexedVar.__init__)
    params = list(sig.parameters.keys())



def test_express::attributevar_is_not_abstract():
    assert not inspect.isabstract(express::AttributeVar)


def test_express::attributevar_constructor_exists():
    assert callable(express::AttributeVar.__init__)


def test_express::attributevar_constructor_args():
    sig = inspect.signature(express::AttributeVar.__init__)
    params = list(sig.parameters.keys())



def test_express::simplevar_is_not_abstract():
    assert not inspect.isabstract(express::SimpleVar)


def test_express::simplevar_constructor_exists():
    assert callable(express::SimpleVar.__init__)


def test_express::simplevar_constructor_args():
    sig = inspect.signature(express::SimpleVar.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_express::simplevar_has_name():
    assert hasattr(express::SimpleVar, "name")
    descriptor = None
    for klass in express::SimpleVar.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_express::varorattrib_is_not_abstract():
    assert not inspect.isabstract(express::VarOrAttrib)


def test_express::varorattrib_constructor_exists():
    assert callable(express::VarOrAttrib.__init__)


def test_express::varorattrib_constructor_args():
    sig = inspect.signature(express::VarOrAttrib.__init__)
    params = list(sig.parameters.keys())



def test_express::caseaction_is_not_abstract():
    assert not inspect.isabstract(express::CaseAction)


def test_express::caseaction_constructor_exists():
    assert callable(express::CaseAction.__init__)


def test_express::caseaction_constructor_args():
    sig = inspect.signature(express::CaseAction.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_express::caseaction_has_value():
    assert hasattr(express::CaseAction, "value")
    descriptor = None
    for klass in express::CaseAction.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_express::escapestatement_is_not_abstract():
    assert not inspect.isabstract(express::EscapeStatement)


def test_express::escapestatement_constructor_exists():
    assert callable(express::EscapeStatement.__init__)


def test_express::escapestatement_constructor_args():
    sig = inspect.signature(express::EscapeStatement.__init__)
    params = list(sig.parameters.keys())



def test_express::assignment_is_not_abstract():
    assert not inspect.isabstract(express::Assignment)


def test_express::assignment_constructor_exists():
    assert callable(express::Assignment.__init__)


def test_express::assignment_constructor_args():
    sig = inspect.signature(express::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_express::assignment_has_expression():
    assert hasattr(express::Assignment, "expression")
    descriptor = None
    for klass in express::Assignment.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_express::returnstatement_is_not_abstract():
    assert not inspect.isabstract(express::ReturnStatement)


def test_express::returnstatement_constructor_exists():
    assert callable(express::ReturnStatement.__init__)


def test_express::returnstatement_constructor_args():
    sig = inspect.signature(express::ReturnStatement.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_express::returnstatement_has_expression():
    assert hasattr(express::ReturnStatement, "expression")
    descriptor = None
    for klass in express::ReturnStatement.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_express::casestatement_is_not_abstract():
    assert not inspect.isabstract(express::CaseStatement)


def test_express::casestatement_constructor_exists():
    assert callable(express::CaseStatement.__init__)


def test_express::casestatement_constructor_args():
    sig = inspect.signature(express::CaseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_express::casestatement_has_variable():
    assert hasattr(express::CaseStatement, "variable")
    descriptor = None
    for klass in express::CaseStatement.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_express::ifstatement_is_not_abstract():
    assert not inspect.isabstract(express::IfStatement)


def test_express::ifstatement_constructor_exists():
    assert callable(express::IfStatement.__init__)


def test_express::ifstatement_constructor_args():
    sig = inspect.signature(express::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_express::repeatstatement_is_not_abstract():
    assert not inspect.isabstract(express::RepeatStatement)


def test_express::repeatstatement_constructor_exists():
    assert callable(express::RepeatStatement.__init__)


def test_express::repeatstatement_constructor_args():
    sig = inspect.signature(express::RepeatStatement.__init__)
    params = list(sig.parameters.keys())
    assert "idx" in params, "Missing parameter 'idx'"
    assert "end" in params, "Missing parameter 'end'"
    assert "start" in params, "Missing parameter 'start'"

def test_express::repeatstatement_has_idx():
    assert hasattr(express::RepeatStatement, "idx")
    descriptor = None
    for klass in express::RepeatStatement.__mro__:
        if "idx" in klass.__dict__:
            descriptor = klass.__dict__["idx"]
            break
    assert isinstance(descriptor, property)

def test_express::repeatstatement_has_end():
    assert hasattr(express::RepeatStatement, "end")
    descriptor = None
    for klass in express::RepeatStatement.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_express::repeatstatement_has_start():
    assert hasattr(express::RepeatStatement, "start")
    descriptor = None
    for klass in express::RepeatStatement.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_express::sequencestatement_is_not_abstract():
    assert not inspect.isabstract(express::SequenceStatement)


def test_express::sequencestatement_constructor_exists():
    assert callable(express::SequenceStatement.__init__)


def test_express::sequencestatement_constructor_args():
    sig = inspect.signature(express::SequenceStatement.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_express::sequencestatement_has_expression():
    assert hasattr(express::SequenceStatement, "expression")
    descriptor = None
    for klass in express::SequenceStatement.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_express::literaltype_is_not_abstract():
    assert not inspect.isabstract(express::LiteralType)


def test_express::literaltype_constructor_exists():
    assert callable(express::LiteralType.__init__)


def test_express::literaltype_constructor_args():
    sig = inspect.signature(express::LiteralType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_express::literaltype_has_name():
    assert hasattr(express::LiteralType, "name")
    descriptor = None
    for klass in express::LiteralType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_builtintype_is_not_abstract():
    assert not inspect.isabstract(BuiltInType)


def test_builtintype_constructor_exists():
    assert callable(BuiltInType.__init__)


def test_builtintype_constructor_args():
    sig = inspect.signature(BuiltInType.__init__)
    params = list(sig.parameters.keys())



def test_express::binarytype_is_not_abstract():
    assert not inspect.isabstract(express::BinaryType)


def test_express::binarytype_constructor_exists():
    assert callable(express::BinaryType.__init__)


def test_express::binarytype_constructor_args():
    sig = inspect.signature(express::BinaryType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_express::binarytype_has_size():
    assert hasattr(express::BinaryType, "size")
    descriptor = None
    for klass in express::BinaryType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_express::integertype_is_not_abstract():
    assert not inspect.isabstract(express::IntegerType)


def test_express::integertype_constructor_exists():
    assert callable(express::IntegerType.__init__)


def test_express::integertype_constructor_args():
    sig = inspect.signature(express::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_express::realtype_is_not_abstract():
    assert not inspect.isabstract(express::RealType)


def test_express::realtype_constructor_exists():
    assert callable(express::RealType.__init__)


def test_express::realtype_constructor_args():
    sig = inspect.signature(express::RealType.__init__)
    params = list(sig.parameters.keys())



def test_express::logicaltype_is_not_abstract():
    assert not inspect.isabstract(express::LogicalType)


def test_express::logicaltype_constructor_exists():
    assert callable(express::LogicalType.__init__)


def test_express::logicaltype_constructor_args():
    sig = inspect.signature(express::LogicalType.__init__)
    params = list(sig.parameters.keys())



def test_express::numbertype_is_not_abstract():
    assert not inspect.isabstract(express::NumberType)


def test_express::numbertype_constructor_exists():
    assert callable(express::NumberType.__init__)


def test_express::numbertype_constructor_args():
    sig = inspect.signature(express::NumberType.__init__)
    params = list(sig.parameters.keys())



def test_express::booleantype_is_not_abstract():
    assert not inspect.isabstract(express::BooleanType)


def test_express::booleantype_constructor_exists():
    assert callable(express::BooleanType.__init__)


def test_express::booleantype_constructor_args():
    sig = inspect.signature(express::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_express::stringtype_is_not_abstract():
    assert not inspect.isabstract(express::StringType)


def test_express::stringtype_constructor_exists():
    assert callable(express::StringType.__init__)


def test_express::stringtype_constructor_args():
    sig = inspect.signature(express::StringType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "fixed" in params, "Missing parameter 'fixed'"

def test_express::stringtype_has_size():
    assert hasattr(express::StringType, "size")
    descriptor = None
    for klass in express::StringType.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_express::stringtype_has_fixed():
    assert hasattr(express::StringType, "fixed")
    descriptor = None
    for klass in express::StringType.__mro__:
        if "fixed" in klass.__dict__:
            descriptor = klass.__dict__["fixed"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_express::enumtype_is_not_abstract():
    assert not inspect.isabstract(express::EnumType)


def test_express::enumtype_constructor_exists():
    assert callable(express::EnumType.__init__)


def test_express::enumtype_constructor_args():
    sig = inspect.signature(express::EnumType.__init__)
    params = list(sig.parameters.keys())



def test_express::selecttype_is_not_abstract():
    assert not inspect.isabstract(express::SelectType)


def test_express::selecttype_constructor_exists():
    assert callable(express::SelectType.__init__)


def test_express::selecttype_constructor_args():
    sig = inspect.signature(express::SelectType.__init__)
    params = list(sig.parameters.keys())



def test_express::collectiontype_is_not_abstract():
    assert not inspect.isabstract(express::CollectionType)


def test_express::collectiontype_constructor_exists():
    assert callable(express::CollectionType.__init__)


def test_express::collectiontype_constructor_args():
    sig = inspect.signature(express::CollectionType.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"
    assert "opt" in params, "Missing parameter 'opt'"
    assert "unique" in params, "Missing parameter 'unique'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_express::collectiontype_has_lowerBound():
    assert hasattr(express::CollectionType, "lowerBound")
    descriptor = None
    for klass in express::CollectionType.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_express::collectiontype_has_many():
    assert hasattr(express::CollectionType, "many")
    descriptor = None
    for klass in express::CollectionType.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_express::collectiontype_has_name():
    assert hasattr(express::CollectionType, "name")
    descriptor = None
    for klass in express::CollectionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_express::collectiontype_has_opt():
    assert hasattr(express::CollectionType, "opt")
    descriptor = None
    for klass in express::CollectionType.__mro__:
        if "opt" in klass.__dict__:
            descriptor = klass.__dict__["opt"]
            break
    assert isinstance(descriptor, property)

def test_express::collectiontype_has_unique():
    assert hasattr(express::CollectionType, "unique")
    descriptor = None
    for klass in express::CollectionType.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)

def test_express::collectiontype_has_upperBound():
    assert hasattr(express::CollectionType, "upperBound")
    descriptor = None
    for klass in express::CollectionType.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_express::generictype_is_not_abstract():
    assert not inspect.isabstract(express::GenericType)


def test_express::generictype_constructor_exists():
    assert callable(express::GenericType.__init__)


def test_express::generictype_constructor_args():
    sig = inspect.signature(express::GenericType.__init__)
    params = list(sig.parameters.keys())
    assert "typelabel" in params, "Missing parameter 'typelabel'"

def test_express::generictype_has_typelabel():
    assert hasattr(express::GenericType, "typelabel")
    descriptor = None
    for klass in express::GenericType.__mro__:
        if "typelabel" in klass.__dict__:
            descriptor = klass.__dict__["typelabel"]
            break
    assert isinstance(descriptor, property)



def test_express::referencetype_is_not_abstract():
    assert not inspect.isabstract(express::ReferenceType)


def test_express::referencetype_constructor_exists():
    assert callable(express::ReferenceType.__init__)


def test_express::referencetype_constructor_args():
    sig = inspect.signature(express::ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_express::builtintype_is_not_abstract():
    assert not inspect.isabstract(express::BuiltInType)


def test_express::builtintype_constructor_exists():
    assert callable(express::BuiltInType.__init__)


def test_express::builtintype_constructor_args():
    sig = inspect.signature(express::BuiltInType.__init__)
    params = list(sig.parameters.keys())



def test_express::intervall_is_not_abstract():
    assert not inspect.isabstract(express::Intervall)


def test_express::intervall_constructor_exists():
    assert callable(express::Intervall.__init__)


def test_express::intervall_constructor_args():
    sig = inspect.signature(express::Intervall.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_express::intervall_has_expression():
    assert hasattr(express::Intervall, "expression")
    descriptor = None
    for klass in express::Intervall.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_express::formalparam_is_not_abstract():
    assert not inspect.isabstract(express::FormalParam)


def test_express::formalparam_constructor_exists():
    assert callable(express::FormalParam.__init__)


def test_express::formalparam_constructor_args():
    sig = inspect.signature(express::FormalParam.__init__)
    params = list(sig.parameters.keys())
    assert "paramName" in params, "Missing parameter 'paramName'"

def test_express::formalparam_has_paramName():
    assert hasattr(express::FormalParam, "paramName")
    descriptor = None
    for klass in express::FormalParam.__mro__:
        if "paramName" in klass.__dict__:
            descriptor = klass.__dict__["paramName"]
            break
    assert isinstance(descriptor, property)



def test_express::parameterlist_is_not_abstract():
    assert not inspect.isabstract(express::ParameterList)


def test_express::parameterlist_constructor_exists():
    assert callable(express::ParameterList.__init__)


def test_express::parameterlist_constructor_args():
    sig = inspect.signature(express::ParameterList.__init__)
    params = list(sig.parameters.keys())



def test_express::functionexpression_is_not_abstract():
    assert not inspect.isabstract(express::FunctionExpression)


def test_express::functionexpression_constructor_exists():
    assert callable(express::FunctionExpression.__init__)


def test_express::functionexpression_constructor_args():
    sig = inspect.signature(express::FunctionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_express::functionexpression_has_name():
    assert hasattr(express::FunctionExpression, "name")
    descriptor = None
    for klass in express::FunctionExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_express::line_is_not_abstract():
    assert not inspect.isabstract(express::Line)


def test_express::line_constructor_exists():
    assert callable(express::Line.__init__)


def test_express::line_constructor_args():
    sig = inspect.signature(express::Line.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_express::line_has_text():
    assert hasattr(express::Line, "text")
    descriptor = None
    for klass in express::Line.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_express::statement_is_not_abstract():
    assert not inspect.isabstract(express::Statement)


def test_express::statement_constructor_exists():
    assert callable(express::Statement.__init__)


def test_express::statement_constructor_args():
    sig = inspect.signature(express::Statement.__init__)
    params = list(sig.parameters.keys())



def test_express::localvar_is_not_abstract():
    assert not inspect.isabstract(express::LocalVar)


def test_express::localvar_constructor_exists():
    assert callable(express::LocalVar.__init__)


def test_express::localvar_constructor_args():
    sig = inspect.signature(express::LocalVar.__init__)
    params = list(sig.parameters.keys())
    assert "varname" in params, "Missing parameter 'varname'"

def test_express::localvar_has_varname():
    assert hasattr(express::LocalVar, "varname")
    descriptor = None
    for klass in express::LocalVar.__mro__:
        if "varname" in klass.__dict__:
            descriptor = klass.__dict__["varname"]
            break
    assert isinstance(descriptor, property)



def test_express::function_is_not_abstract():
    assert not inspect.isabstract(express::Function)


def test_express::function_constructor_exists():
    assert callable(express::Function.__init__)


def test_express::function_constructor_args():
    sig = inspect.signature(express::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_express::function_has_name():
    assert hasattr(express::Function, "name")
    descriptor = None
    for klass in express::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_express::constantval_is_not_abstract():
    assert not inspect.isabstract(express::ConstantVal)


def test_express::constantval_constructor_exists():
    assert callable(express::ConstantVal.__init__)


def test_express::constantval_constructor_args():
    sig = inspect.signature(express::ConstantVal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_express::constantval_has_name():
    assert hasattr(express::ConstantVal, "name")
    descriptor = None
    for klass in express::ConstantVal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_express::typenamelist_is_not_abstract():
    assert not inspect.isabstract(express::TypeNameList)


def test_express::typenamelist_constructor_exists():
    assert callable(express::TypeNameList.__init__)


def test_express::typenamelist_constructor_args():
    sig = inspect.signature(express::TypeNameList.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_express::typenamelist_has_type():
    assert hasattr(express::TypeNameList, "type")
    descriptor = None
    for klass in express::TypeNameList.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_express::reference_is_not_abstract():
    assert not inspect.isabstract(express::Reference)


def test_express::reference_constructor_exists():
    assert callable(express::Reference.__init__)


def test_express::reference_constructor_args():
    sig = inspect.signature(express::Reference.__init__)
    params = list(sig.parameters.keys())
    assert "self" in params, "Missing parameter 'self'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "name" in params, "Missing parameter 'name'"
    assert "qualifier" in params, "Missing parameter 'qualifier'"

def test_express::reference_has_self():
    assert hasattr(express::Reference, "self")
    descriptor = None
    for klass in express::Reference.__mro__:
        if "self" in klass.__dict__:
            descriptor = klass.__dict__["self"]
            break
    assert isinstance(descriptor, property)

def test_express::reference_has_optional():
    assert hasattr(express::Reference, "optional")
    descriptor = None
    for klass in express::Reference.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_express::reference_has_name():
    assert hasattr(express::Reference, "name")
    descriptor = None
    for klass in express::Reference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_express::reference_has_qualifier():
    assert hasattr(express::Reference, "qualifier")
    descriptor = None
    for klass in express::Reference.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)



def test_express::uniquerule_is_not_abstract():
    assert not inspect.isabstract(express::UniqueRule)


def test_express::uniquerule_constructor_exists():
    assert callable(express::UniqueRule.__init__)


def test_express::uniquerule_constructor_args():
    sig = inspect.signature(express::UniqueRule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_express::uniquerule_has_name():
    assert hasattr(express::UniqueRule, "name")
    descriptor = None
    for klass in express::UniqueRule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_express::uniquerule_has_attribute():
    assert hasattr(express::UniqueRule, "attribute")
    descriptor = None
    for klass in express::UniqueRule.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_express::attribute_is_not_abstract():
    assert not inspect.isabstract(express::Attribute)


def test_express::attribute_constructor_exists():
    assert callable(express::Attribute.__init__)


def test_express::attribute_constructor_args():
    sig = inspect.signature(express::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "self" in params, "Missing parameter 'self'"
    assert "qualifier" in params, "Missing parameter 'qualifier'"
    assert "expression" in params, "Missing parameter 'expression'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_express::attribute_has_name():
    assert hasattr(express::Attribute, "name")
    descriptor = None
    for klass in express::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_express::attribute_has_self():
    assert hasattr(express::Attribute, "self")
    descriptor = None
    for klass in express::Attribute.__mro__:
        if "self" in klass.__dict__:
            descriptor = klass.__dict__["self"]
            break
    assert isinstance(descriptor, property)

def test_express::attribute_has_qualifier():
    assert hasattr(express::Attribute, "qualifier")
    descriptor = None
    for klass in express::Attribute.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)

def test_express::attribute_has_expression():
    assert hasattr(express::Attribute, "expression")
    descriptor = None
    for klass in express::Attribute.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_express::attribute_has_optional():
    assert hasattr(express::Attribute, "optional")
    descriptor = None
    for klass in express::Attribute.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_express::datatype_is_not_abstract():
    assert not inspect.isabstract(express::DataType)


def test_express::datatype_constructor_exists():
    assert callable(express::DataType.__init__)


def test_express::datatype_constructor_args():
    sig = inspect.signature(express::DataType.__init__)
    params = list(sig.parameters.keys())



def test_expressconcept_is_not_abstract():
    assert not inspect.isabstract(ExpressConcept)


def test_expressconcept_constructor_exists():
    assert callable(ExpressConcept.__init__)


def test_expressconcept_constructor_args():
    sig = inspect.signature(ExpressConcept.__init__)
    params = list(sig.parameters.keys())



def test_express::entity_is_not_abstract():
    assert not inspect.isabstract(express::Entity)


def test_express::entity_constructor_exists():
    assert callable(express::Entity.__init__)


def test_express::entity_constructor_args():
    sig = inspect.signature(express::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_express::entity_has_abstract():
    assert hasattr(express::Entity, "abstract")
    descriptor = None
    for klass in express::Entity.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_express::whererule_is_not_abstract():
    assert not inspect.isabstract(express::WhereRule)


def test_express::whererule_constructor_exists():
    assert callable(express::WhereRule.__init__)


def test_express::whererule_constructor_args():
    sig = inspect.signature(express::WhereRule.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"
    assert "name" in params, "Missing parameter 'name'"

def test_express::whererule_has_expression():
    assert hasattr(express::WhereRule, "expression")
    descriptor = None
    for klass in express::WhereRule.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)

def test_express::whererule_has_name():
    assert hasattr(express::WhereRule, "name")
    descriptor = None
    for klass in express::WhereRule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_express::expressconcept_is_not_abstract():
    assert not inspect.isabstract(express::ExpressConcept)


def test_express::expressconcept_constructor_exists():
    assert callable(express::ExpressConcept.__init__)


def test_express::expressconcept_constructor_args():
    sig = inspect.signature(express::ExpressConcept.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_express::expressconcept_has_name():
    assert hasattr(express::ExpressConcept, "name")
    descriptor = None
    for klass in express::ExpressConcept.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_express::rule_is_not_abstract():
    assert not inspect.isabstract(express::Rule)


def test_express::rule_constructor_exists():
    assert callable(express::Rule.__init__)


def test_express::rule_constructor_args():
    sig = inspect.signature(express::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_express::rule_has_name():
    assert hasattr(express::Rule, "name")
    descriptor = None
    for klass in express::Rule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_express::type_is_not_abstract():
    assert not inspect.isabstract(express::Type)


def test_express::type_constructor_exists():
    assert callable(express::Type.__init__)


def test_express::type_constructor_args():
    sig = inspect.signature(express::Type.__init__)
    params = list(sig.parameters.keys())



def test_express::schema_is_not_abstract():
    assert not inspect.isabstract(express::Schema)


def test_express::schema_constructor_exists():
    assert callable(express::Schema.__init__)


def test_express::schema_constructor_args():
    sig = inspect.signature(express::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_express::schema_has_name():
    assert hasattr(express::Schema, "name")
    descriptor = None
    for klass in express::Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
Index_strategy = st.builds(
    Index,
)
express::IndexTerminal_strategy = st.builds(
    express::IndexTerminal,
)
IndexTerminal_strategy = st.builds(
    IndexTerminal,
)
express::IntLiteral_strategy = st.builds(
    express::IntLiteral,
    value=
        st.integers()
)
express::VarLiteral_strategy = st.builds(
    express::VarLiteral,
    value=
        safe_text
)
express::Index_strategy = st.builds(
    express::Index,
)
VarOrAttrib_strategy = st.builds(
    VarOrAttrib,
)
express::IndexedVar_strategy = st.builds(
    express::IndexedVar,
)
express::AttributeVar_strategy = st.builds(
    express::AttributeVar,
)
express::SimpleVar_strategy = st.builds(
    express::SimpleVar,
    name=
        safe_text
)
express::VarOrAttrib_strategy = st.builds(
    express::VarOrAttrib,
)
express::CaseAction_strategy = st.builds(
    express::CaseAction,
    value=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
express::EscapeStatement_strategy = st.builds(
    express::EscapeStatement,
)
express::Assignment_strategy = st.builds(
    express::Assignment,
    expression=
        safe_text
)
express::ReturnStatement_strategy = st.builds(
    express::ReturnStatement,
    expression=
        safe_text
)
express::CaseStatement_strategy = st.builds(
    express::CaseStatement,
    variable=
        safe_text
)
express::IfStatement_strategy = st.builds(
    express::IfStatement,
)
express::RepeatStatement_strategy = st.builds(
    express::RepeatStatement,
    idx=
        safe_text,
    end=
        safe_text,
    start=
        safe_text
)
express::SequenceStatement_strategy = st.builds(
    express::SequenceStatement,
    expression=
        safe_text
)
express::LiteralType_strategy = st.builds(
    express::LiteralType,
    name=
        safe_text
)
BuiltInType_strategy = st.builds(
    BuiltInType,
)
express::BinaryType_strategy = st.builds(
    express::BinaryType,
    size=
        st.integers()
)
express::IntegerType_strategy = st.builds(
    express::IntegerType,
)
express::RealType_strategy = st.builds(
    express::RealType,
)
express::LogicalType_strategy = st.builds(
    express::LogicalType,
)
express::NumberType_strategy = st.builds(
    express::NumberType,
)
express::BooleanType_strategy = st.builds(
    express::BooleanType,
)
express::StringType_strategy = st.builds(
    express::StringType,
    size=
        st.integers(),
    fixed=
        st.booleans()
)
DataType_strategy = st.builds(
    DataType,
)
express::EnumType_strategy = st.builds(
    express::EnumType,
)
express::SelectType_strategy = st.builds(
    express::SelectType,
)
express::CollectionType_strategy = st.builds(
    express::CollectionType,
    lowerBound=
        st.integers(),
    many=
        st.booleans(),
    name=
        safe_text,
    opt=
        st.booleans(),
    unique=
        st.booleans(),
    upperBound=
        st.integers()
)
express::GenericType_strategy = st.builds(
    express::GenericType,
    typelabel=
        safe_text
)
express::ReferenceType_strategy = st.builds(
    express::ReferenceType,
)
express::BuiltInType_strategy = st.builds(
    express::BuiltInType,
)
express::Intervall_strategy = st.builds(
    express::Intervall,
    expression=
        safe_text
)
express::FormalParam_strategy = st.builds(
    express::FormalParam,
    paramName=
        safe_text
)
express::ParameterList_strategy = st.builds(
    express::ParameterList,
)
express::FunctionExpression_strategy = st.builds(
    express::FunctionExpression,
    name=
        safe_text
)
express::Line_strategy = st.builds(
    express::Line,
    text=
        safe_text
)
express::Statement_strategy = st.builds(
    express::Statement,
)
express::LocalVar_strategy = st.builds(
    express::LocalVar,
    varname=
        safe_text
)
express::Function_strategy = st.builds(
    express::Function,
    name=
        safe_text
)
express::ConstantVal_strategy = st.builds(
    express::ConstantVal,
    name=
        safe_text
)
express::TypeNameList_strategy = st.builds(
    express::TypeNameList,
    type=
        safe_text
)
express::Reference_strategy = st.builds(
    express::Reference,
    self=
        st.booleans(),
    optional=
        st.booleans(),
    name=
        safe_text,
    qualifier=
        safe_text
)
express::UniqueRule_strategy = st.builds(
    express::UniqueRule,
    name=
        safe_text,
    attribute=
        safe_text
)
express::Attribute_strategy = st.builds(
    express::Attribute,
    name=
        safe_text,
    self=
        st.booleans(),
    qualifier=
        safe_text,
    expression=
        safe_text,
    optional=
        st.booleans()
)
express::DataType_strategy = st.builds(
    express::DataType,
)
ExpressConcept_strategy = st.builds(
    ExpressConcept,
)
express::Entity_strategy = st.builds(
    express::Entity,
    abstract=
        st.booleans()
)
express::WhereRule_strategy = st.builds(
    express::WhereRule,
    expression=
        safe_text,
    name=
        safe_text
)
express::ExpressConcept_strategy = st.builds(
    express::ExpressConcept,
    name=
        safe_text
)
express::Rule_strategy = st.builds(
    express::Rule,
    name=
        safe_text
)
express::Type_strategy = st.builds(
    express::Type,
)
express::Schema_strategy = st.builds(
    express::Schema,
    name=
        safe_text
)

@given(instance=Index_strategy)
@settings(max_examples=50)
def test_index_instantiation(instance):
    assert isinstance(instance, Index)

@given(instance=express::IndexTerminal_strategy)
@settings(max_examples=50)
def test_express::indexterminal_instantiation(instance):
    assert isinstance(instance, express::IndexTerminal)

@given(instance=IndexTerminal_strategy)
@settings(max_examples=50)
def test_indexterminal_instantiation(instance):
    assert isinstance(instance, IndexTerminal)

@given(instance=express::IntLiteral_strategy)
@settings(max_examples=50)
def test_express::intliteral_instantiation(instance):
    assert isinstance(instance, express::IntLiteral)

@given(instance=express::IntLiteral_strategy)
def test_express::intliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=express::IntLiteral_strategy)
def test_express::intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=express::VarLiteral_strategy)
@settings(max_examples=50)
def test_express::varliteral_instantiation(instance):
    assert isinstance(instance, express::VarLiteral)

@given(instance=express::VarLiteral_strategy)
def test_express::varliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=express::VarLiteral_strategy)
def test_express::varliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=express::Index_strategy)
@settings(max_examples=50)
def test_express::index_instantiation(instance):
    assert isinstance(instance, express::Index)

@given(instance=VarOrAttrib_strategy)
@settings(max_examples=50)
def test_varorattrib_instantiation(instance):
    assert isinstance(instance, VarOrAttrib)

@given(instance=express::IndexedVar_strategy)
@settings(max_examples=50)
def test_express::indexedvar_instantiation(instance):
    assert isinstance(instance, express::IndexedVar)

@given(instance=express::AttributeVar_strategy)
@settings(max_examples=50)
def test_express::attributevar_instantiation(instance):
    assert isinstance(instance, express::AttributeVar)

@given(instance=express::SimpleVar_strategy)
@settings(max_examples=50)
def test_express::simplevar_instantiation(instance):
    assert isinstance(instance, express::SimpleVar)

@given(instance=express::SimpleVar_strategy)
def test_express::simplevar_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=express::SimpleVar_strategy)
def test_express::simplevar_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express::VarOrAttrib_strategy)
@settings(max_examples=50)
def test_express::varorattrib_instantiation(instance):
    assert isinstance(instance, express::VarOrAttrib)

@given(instance=express::CaseAction_strategy)
@settings(max_examples=50)
def test_express::caseaction_instantiation(instance):
    assert isinstance(instance, express::CaseAction)

@given(instance=express::CaseAction_strategy)
def test_express::caseaction_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=express::CaseAction_strategy)
def test_express::caseaction_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=express::EscapeStatement_strategy)
@settings(max_examples=50)
def test_express::escapestatement_instantiation(instance):
    assert isinstance(instance, express::EscapeStatement)

@given(instance=express::Assignment_strategy)
@settings(max_examples=50)
def test_express::assignment_instantiation(instance):
    assert isinstance(instance, express::Assignment)

@given(instance=express::Assignment_strategy)
def test_express::assignment_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=express::Assignment_strategy)
def test_express::assignment_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=express::ReturnStatement_strategy)
@settings(max_examples=50)
def test_express::returnstatement_instantiation(instance):
    assert isinstance(instance, express::ReturnStatement)

@given(instance=express::ReturnStatement_strategy)
def test_express::returnstatement_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=express::ReturnStatement_strategy)
def test_express::returnstatement_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=express::CaseStatement_strategy)
@settings(max_examples=50)
def test_express::casestatement_instantiation(instance):
    assert isinstance(instance, express::CaseStatement)

@given(instance=express::CaseStatement_strategy)
def test_express::casestatement_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=express::CaseStatement_strategy)
def test_express::casestatement_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=express::IfStatement_strategy)
@settings(max_examples=50)
def test_express::ifstatement_instantiation(instance):
    assert isinstance(instance, express::IfStatement)

@given(instance=express::RepeatStatement_strategy)
@settings(max_examples=50)
def test_express::repeatstatement_instantiation(instance):
    assert isinstance(instance, express::RepeatStatement)

@given(instance=express::RepeatStatement_strategy)
def test_express::repeatstatement_idx_type(instance):
    assert isinstance(instance.idx, str)


@given(instance=express::RepeatStatement_strategy)
def test_express::repeatstatement_idx_setter(instance):
    original = instance.idx
    instance.idx = original
    assert instance.idx == original

@given(instance=express::RepeatStatement_strategy)
def test_express::repeatstatement_end_type(instance):
    assert isinstance(instance.end, str)


@given(instance=express::RepeatStatement_strategy)
def test_express::repeatstatement_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=express::RepeatStatement_strategy)
def test_express::repeatstatement_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=express::RepeatStatement_strategy)
def test_express::repeatstatement_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=express::SequenceStatement_strategy)
@settings(max_examples=50)
def test_express::sequencestatement_instantiation(instance):
    assert isinstance(instance, express::SequenceStatement)

@given(instance=express::SequenceStatement_strategy)
def test_express::sequencestatement_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=express::SequenceStatement_strategy)
def test_express::sequencestatement_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=express::LiteralType_strategy)
@settings(max_examples=50)
def test_express::literaltype_instantiation(instance):
    assert isinstance(instance, express::LiteralType)

@given(instance=express::LiteralType_strategy)
def test_express::literaltype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=express::LiteralType_strategy)
def test_express::literaltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BuiltInType_strategy)
@settings(max_examples=50)
def test_builtintype_instantiation(instance):
    assert isinstance(instance, BuiltInType)

@given(instance=express::BinaryType_strategy)
@settings(max_examples=50)
def test_express::binarytype_instantiation(instance):
    assert isinstance(instance, express::BinaryType)

@given(instance=express::BinaryType_strategy)
def test_express::binarytype_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=express::BinaryType_strategy)
def test_express::binarytype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=express::IntegerType_strategy)
@settings(max_examples=50)
def test_express::integertype_instantiation(instance):
    assert isinstance(instance, express::IntegerType)

@given(instance=express::RealType_strategy)
@settings(max_examples=50)
def test_express::realtype_instantiation(instance):
    assert isinstance(instance, express::RealType)

@given(instance=express::LogicalType_strategy)
@settings(max_examples=50)
def test_express::logicaltype_instantiation(instance):
    assert isinstance(instance, express::LogicalType)

@given(instance=express::NumberType_strategy)
@settings(max_examples=50)
def test_express::numbertype_instantiation(instance):
    assert isinstance(instance, express::NumberType)

@given(instance=express::BooleanType_strategy)
@settings(max_examples=50)
def test_express::booleantype_instantiation(instance):
    assert isinstance(instance, express::BooleanType)

@given(instance=express::StringType_strategy)
@settings(max_examples=50)
def test_express::stringtype_instantiation(instance):
    assert isinstance(instance, express::StringType)

@given(instance=express::StringType_strategy)
def test_express::stringtype_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=express::StringType_strategy)
def test_express::stringtype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=express::StringType_strategy)
def test_express::stringtype_fixed_type(instance):
    assert isinstance(instance.fixed, bool)


@given(instance=express::StringType_strategy)
def test_express::stringtype_fixed_setter(instance):
    original = instance.fixed
    instance.fixed = original
    assert instance.fixed == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=express::EnumType_strategy)
@settings(max_examples=50)
def test_express::enumtype_instantiation(instance):
    assert isinstance(instance, express::EnumType)

@given(instance=express::SelectType_strategy)
@settings(max_examples=50)
def test_express::selecttype_instantiation(instance):
    assert isinstance(instance, express::SelectType)

@given(instance=express::CollectionType_strategy)
@settings(max_examples=50)
def test_express::collectiontype_instantiation(instance):
    assert isinstance(instance, express::CollectionType)

@given(instance=express::CollectionType_strategy)
def test_express::collectiontype_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=express::CollectionType_strategy)
def test_express::collectiontype_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=express::CollectionType_strategy)
def test_express::collectiontype_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=express::CollectionType_strategy)
def test_express::collectiontype_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=express::CollectionType_strategy)
def test_express::collectiontype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=express::CollectionType_strategy)
def test_express::collectiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express::CollectionType_strategy)
def test_express::collectiontype_opt_type(instance):
    assert isinstance(instance.opt, bool)


@given(instance=express::CollectionType_strategy)
def test_express::collectiontype_opt_setter(instance):
    original = instance.opt
    instance.opt = original
    assert instance.opt == original

@given(instance=express::CollectionType_strategy)
def test_express::collectiontype_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=express::CollectionType_strategy)
def test_express::collectiontype_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=express::CollectionType_strategy)
def test_express::collectiontype_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=express::CollectionType_strategy)
def test_express::collectiontype_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=express::GenericType_strategy)
@settings(max_examples=50)
def test_express::generictype_instantiation(instance):
    assert isinstance(instance, express::GenericType)

@given(instance=express::GenericType_strategy)
def test_express::generictype_typelabel_type(instance):
    assert isinstance(instance.typelabel, str)


@given(instance=express::GenericType_strategy)
def test_express::generictype_typelabel_setter(instance):
    original = instance.typelabel
    instance.typelabel = original
    assert instance.typelabel == original

@given(instance=express::ReferenceType_strategy)
@settings(max_examples=50)
def test_express::referencetype_instantiation(instance):
    assert isinstance(instance, express::ReferenceType)

@given(instance=express::BuiltInType_strategy)
@settings(max_examples=50)
def test_express::builtintype_instantiation(instance):
    assert isinstance(instance, express::BuiltInType)

@given(instance=express::Intervall_strategy)
@settings(max_examples=50)
def test_express::intervall_instantiation(instance):
    assert isinstance(instance, express::Intervall)

@given(instance=express::Intervall_strategy)
def test_express::intervall_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=express::Intervall_strategy)
def test_express::intervall_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=express::FormalParam_strategy)
@settings(max_examples=50)
def test_express::formalparam_instantiation(instance):
    assert isinstance(instance, express::FormalParam)

@given(instance=express::FormalParam_strategy)
def test_express::formalparam_paramName_type(instance):
    assert isinstance(instance.paramName, str)


@given(instance=express::FormalParam_strategy)
def test_express::formalparam_paramName_setter(instance):
    original = instance.paramName
    instance.paramName = original
    assert instance.paramName == original

@given(instance=express::ParameterList_strategy)
@settings(max_examples=50)
def test_express::parameterlist_instantiation(instance):
    assert isinstance(instance, express::ParameterList)

@given(instance=express::FunctionExpression_strategy)
@settings(max_examples=50)
def test_express::functionexpression_instantiation(instance):
    assert isinstance(instance, express::FunctionExpression)

@given(instance=express::FunctionExpression_strategy)
def test_express::functionexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=express::FunctionExpression_strategy)
def test_express::functionexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express::Line_strategy)
@settings(max_examples=50)
def test_express::line_instantiation(instance):
    assert isinstance(instance, express::Line)

@given(instance=express::Line_strategy)
def test_express::line_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=express::Line_strategy)
def test_express::line_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=express::Statement_strategy)
@settings(max_examples=50)
def test_express::statement_instantiation(instance):
    assert isinstance(instance, express::Statement)

@given(instance=express::LocalVar_strategy)
@settings(max_examples=50)
def test_express::localvar_instantiation(instance):
    assert isinstance(instance, express::LocalVar)

@given(instance=express::LocalVar_strategy)
def test_express::localvar_varname_type(instance):
    assert isinstance(instance.varname, str)


@given(instance=express::LocalVar_strategy)
def test_express::localvar_varname_setter(instance):
    original = instance.varname
    instance.varname = original
    assert instance.varname == original

@given(instance=express::Function_strategy)
@settings(max_examples=50)
def test_express::function_instantiation(instance):
    assert isinstance(instance, express::Function)

@given(instance=express::Function_strategy)
def test_express::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=express::Function_strategy)
def test_express::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express::ConstantVal_strategy)
@settings(max_examples=50)
def test_express::constantval_instantiation(instance):
    assert isinstance(instance, express::ConstantVal)

@given(instance=express::ConstantVal_strategy)
def test_express::constantval_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=express::ConstantVal_strategy)
def test_express::constantval_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express::TypeNameList_strategy)
@settings(max_examples=50)
def test_express::typenamelist_instantiation(instance):
    assert isinstance(instance, express::TypeNameList)

@given(instance=express::TypeNameList_strategy)
def test_express::typenamelist_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=express::TypeNameList_strategy)
def test_express::typenamelist_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=express::Reference_strategy)
@settings(max_examples=50)
def test_express::reference_instantiation(instance):
    assert isinstance(instance, express::Reference)

@given(instance=express::Reference_strategy)
def test_express::reference_self_type(instance):
    assert isinstance(instance.self, bool)


@given(instance=express::Reference_strategy)
def test_express::reference_self_setter(instance):
    original = instance.self
    instance.self = original
    assert instance.self == original

@given(instance=express::Reference_strategy)
def test_express::reference_optional_type(instance):
    assert isinstance(instance.optional, bool)


@given(instance=express::Reference_strategy)
def test_express::reference_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=express::Reference_strategy)
def test_express::reference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=express::Reference_strategy)
def test_express::reference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express::Reference_strategy)
def test_express::reference_qualifier_type(instance):
    assert isinstance(instance.qualifier, str)


@given(instance=express::Reference_strategy)
def test_express::reference_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=express::UniqueRule_strategy)
@settings(max_examples=50)
def test_express::uniquerule_instantiation(instance):
    assert isinstance(instance, express::UniqueRule)

@given(instance=express::UniqueRule_strategy)
def test_express::uniquerule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=express::UniqueRule_strategy)
def test_express::uniquerule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express::UniqueRule_strategy)
def test_express::uniquerule_attribute_type(instance):
    assert isinstance(instance.attribute, str)


@given(instance=express::UniqueRule_strategy)
def test_express::uniquerule_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=express::Attribute_strategy)
@settings(max_examples=50)
def test_express::attribute_instantiation(instance):
    assert isinstance(instance, express::Attribute)

@given(instance=express::Attribute_strategy)
def test_express::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=express::Attribute_strategy)
def test_express::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express::Attribute_strategy)
def test_express::attribute_self_type(instance):
    assert isinstance(instance.self, bool)


@given(instance=express::Attribute_strategy)
def test_express::attribute_self_setter(instance):
    original = instance.self
    instance.self = original
    assert instance.self == original

@given(instance=express::Attribute_strategy)
def test_express::attribute_qualifier_type(instance):
    assert isinstance(instance.qualifier, str)


@given(instance=express::Attribute_strategy)
def test_express::attribute_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=express::Attribute_strategy)
def test_express::attribute_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=express::Attribute_strategy)
def test_express::attribute_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=express::Attribute_strategy)
def test_express::attribute_optional_type(instance):
    assert isinstance(instance.optional, bool)


@given(instance=express::Attribute_strategy)
def test_express::attribute_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=express::DataType_strategy)
@settings(max_examples=50)
def test_express::datatype_instantiation(instance):
    assert isinstance(instance, express::DataType)

@given(instance=ExpressConcept_strategy)
@settings(max_examples=50)
def test_expressconcept_instantiation(instance):
    assert isinstance(instance, ExpressConcept)

@given(instance=express::Entity_strategy)
@settings(max_examples=50)
def test_express::entity_instantiation(instance):
    assert isinstance(instance, express::Entity)

@given(instance=express::Entity_strategy)
def test_express::entity_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=express::Entity_strategy)
def test_express::entity_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=express::WhereRule_strategy)
@settings(max_examples=50)
def test_express::whererule_instantiation(instance):
    assert isinstance(instance, express::WhereRule)

@given(instance=express::WhereRule_strategy)
def test_express::whererule_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=express::WhereRule_strategy)
def test_express::whererule_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=express::WhereRule_strategy)
def test_express::whererule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=express::WhereRule_strategy)
def test_express::whererule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express::ExpressConcept_strategy)
@settings(max_examples=50)
def test_express::expressconcept_instantiation(instance):
    assert isinstance(instance, express::ExpressConcept)

@given(instance=express::ExpressConcept_strategy)
def test_express::expressconcept_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=express::ExpressConcept_strategy)
def test_express::expressconcept_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express::Rule_strategy)
@settings(max_examples=50)
def test_express::rule_instantiation(instance):
    assert isinstance(instance, express::Rule)

@given(instance=express::Rule_strategy)
def test_express::rule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=express::Rule_strategy)
def test_express::rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=express::Type_strategy)
@settings(max_examples=50)
def test_express::type_instantiation(instance):
    assert isinstance(instance, express::Type)

@given(instance=express::Schema_strategy)
@settings(max_examples=50)
def test_express::schema_instantiation(instance):
    assert isinstance(instance, express::Schema)

@given(instance=express::Schema_strategy)
def test_express::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=express::Schema_strategy)
def test_express::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

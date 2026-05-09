import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ValueExpression,
    vhdl::UnitValueExpression,
    vhdl::ValueExpression,
    ArrayTypeDefinition,
    vhdl::ConstrainedArrayTypeDefinition,
    vhdl::UnconstrainedArrayTypeDefinition,
    CompositeTypeDefinition,
    vhdl::ArrayTypeDefinition,
    vhdl::RecordTypeDefinition,
    vhdl::RecordField,
    TypeDefinition,
    vhdl::FileTypeDefinition,
    vhdl::EnumerationTypeDefinition,
    vhdl::CompositeTypeDefinition,
    vhdl::AccessTypeDefinition,
    vhdl::TypeDefinition,
    Type,
    vhdl::TypeDeclaration,
    vhdl::SubtypeDeclaration,
    Expression,
    vhdl::ConditionalWaveformExpression,
    vhdl::Boolean,
    vhdl::Open,
    vhdl::ShiftExpression,
    vhdl::RelationalExpression,
    vhdl::AddingExpression,
    vhdl::BuiltinFuncs,
    vhdl::MultiplyingExpression,
    vhdl::ChoiceExpression,
    vhdl::Char,
    vhdl::MemberExpression,
    vhdl::Variable,
    vhdl::Value,
    vhdl::SliceExpression,
    vhdl::String,
    vhdl::LogicalExpression,
    vhdl::Member,
    vhdl::Factor,
    vhdl::Others,
    vhdl::BitString,
    vhdl::RangeExpression,
    vhdl::MultiExpression,
    vhdl::IfStatementTest,
    IterationScheme,
    vhdl::ForIterationScheme,
    vhdl::CaseAlternative,
    vhdl::GenericMapAssociation,
    vhdl::PortMapAssociation,
    SequentialStatement,
    vhdl::SequentialSignalAssignmentStatement,
    vhdl::LoopStatement,
    vhdl::IfStatement,
    vhdl::CaseStatement,
    vhdl::WaitStatement,
    vhdl::PortMap,
    vhdl::GenericMap,
    vhdl::SequentialStatement,
    vhdl::IdList,
    ArchitectureStatement,
    vhdl::ComponentInstantiationStatement,
    vhdl::IfGenerateStatement,
    vhdl::EntityInstantiationStatement,
    vhdl::ConditionalSignalAssignmentStatement,
    vhdl::ForGenerateStatement,
    vhdl::ProcessStatement,
    vhdl::SubtypeIndication,
    Variable,
    vhdl::LoopVariable,
    vhdl::Constant,
    vhdl::Port,
    vhdl::Ports,
    vhdl::Generics,
    vhdl::Var,
    vhdl::Signal,
    package::declarative::item,
    BlockDeclarativeItem,
    vhdl::VariableDeclaration,
    vhdl::AttributeSpecification,
    vhdl::SignalDeclaration,
    vhdl::Type,
    vhdl::ConstantDeclaration,
    vhdl::Component,
    vhdl::AttributeDeclaration,
    vhdl::Alias,
    vhdl::Generic,
    vhdl::Expression,
    vhdl::DesignFile,
    vhdl::ArchitectureStatement,
    vhdl::BlockDeclarativeItem,
    vhdl::package::declarative::part,
    vhdl::package::declarative::item,
    LibraryUnit,
    vhdl::Entity,
    vhdl::Architecture,
    vhdl::Package,
    vhdl::Library,
    ContextItem,
    vhdl::LibraryClause,
    vhdl::UseClause,
    vhdl::LibraryUnit,
    vhdl::ContextItem,
    vhdl::WhileIterationScheme,
    vhdl::IterationScheme,
    RangeDirection,
    UnaryOperator,
    AddingOperator,
    Sign,
    EString,
    MultiplyingOperator,
    EntityClass,
    LogicalOperator,
    BuiltinLibs,
    SignalKind,
    ShiftOperator,
    Mode,
    Purity,
    RelationalOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_valueexpression_is_not_abstract():
    assert not inspect.isabstract(ValueExpression)


def test_valueexpression_constructor_exists():
    assert callable(ValueExpression.__init__)


def test_valueexpression_constructor_args():
    sig = inspect.signature(ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::unitvalueexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::UnitValueExpression)


def test_vhdl::unitvalueexpression_constructor_exists():
    assert callable(vhdl::UnitValueExpression.__init__)


def test_vhdl::unitvalueexpression_constructor_args():
    sig = inspect.signature(vhdl::UnitValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"

def test_vhdl::unitvalueexpression_has_unit():
    assert hasattr(vhdl::UnitValueExpression, "unit")
    descriptor = None
    for klass in vhdl::UnitValueExpression.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::valueexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::ValueExpression)


def test_vhdl::valueexpression_constructor_exists():
    assert callable(vhdl::ValueExpression.__init__)


def test_vhdl::valueexpression_constructor_args():
    sig = inspect.signature(vhdl::ValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl::valueexpression_has_value():
    assert hasattr(vhdl::ValueExpression, "value")
    descriptor = None
    for klass in vhdl::ValueExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(ArrayTypeDefinition)


def test_arraytypedefinition_constructor_exists():
    assert callable(ArrayTypeDefinition.__init__)


def test_arraytypedefinition_constructor_args():
    sig = inspect.signature(ArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::constrainedarraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::ConstrainedArrayTypeDefinition)


def test_vhdl::constrainedarraytypedefinition_constructor_exists():
    assert callable(vhdl::ConstrainedArrayTypeDefinition.__init__)


def test_vhdl::constrainedarraytypedefinition_constructor_args():
    sig = inspect.signature(vhdl::ConstrainedArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::unconstrainedarraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::UnconstrainedArrayTypeDefinition)


def test_vhdl::unconstrainedarraytypedefinition_constructor_exists():
    assert callable(vhdl::UnconstrainedArrayTypeDefinition.__init__)


def test_vhdl::unconstrainedarraytypedefinition_constructor_args():
    sig = inspect.signature(vhdl::UnconstrainedArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_vhdl::unconstrainedarraytypedefinition_has_index():
    assert hasattr(vhdl::UnconstrainedArrayTypeDefinition, "index")
    descriptor = None
    for klass in vhdl::UnconstrainedArrayTypeDefinition.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_compositetypedefinition_is_not_abstract():
    assert not inspect.isabstract(CompositeTypeDefinition)


def test_compositetypedefinition_constructor_exists():
    assert callable(CompositeTypeDefinition.__init__)


def test_compositetypedefinition_constructor_args():
    sig = inspect.signature(CompositeTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::arraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::ArrayTypeDefinition)


def test_vhdl::arraytypedefinition_constructor_exists():
    assert callable(vhdl::ArrayTypeDefinition.__init__)


def test_vhdl::arraytypedefinition_constructor_args():
    sig = inspect.signature(vhdl::ArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::recordtypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::RecordTypeDefinition)


def test_vhdl::recordtypedefinition_constructor_exists():
    assert callable(vhdl::RecordTypeDefinition.__init__)


def test_vhdl::recordtypedefinition_constructor_args():
    sig = inspect.signature(vhdl::RecordTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::recordfield_is_not_abstract():
    assert not inspect.isabstract(vhdl::RecordField)


def test_vhdl::recordfield_constructor_exists():
    assert callable(vhdl::RecordField.__init__)


def test_vhdl::recordfield_constructor_args():
    sig = inspect.signature(vhdl::RecordField.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl::recordfield_has_name():
    assert hasattr(vhdl::RecordField, "name")
    descriptor = None
    for klass in vhdl::RecordField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::filetypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::FileTypeDefinition)


def test_vhdl::filetypedefinition_constructor_exists():
    assert callable(vhdl::FileTypeDefinition.__init__)


def test_vhdl::filetypedefinition_constructor_args():
    sig = inspect.signature(vhdl::FileTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_vhdl::filetypedefinition_has_type():
    assert hasattr(vhdl::FileTypeDefinition, "type")
    descriptor = None
    for klass in vhdl::FileTypeDefinition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::enumerationtypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::EnumerationTypeDefinition)


def test_vhdl::enumerationtypedefinition_constructor_exists():
    assert callable(vhdl::EnumerationTypeDefinition.__init__)


def test_vhdl::enumerationtypedefinition_constructor_args():
    sig = inspect.signature(vhdl::EnumerationTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"

def test_vhdl::enumerationtypedefinition_has_literal():
    assert hasattr(vhdl::EnumerationTypeDefinition, "literal")
    descriptor = None
    for klass in vhdl::EnumerationTypeDefinition.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::compositetypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::CompositeTypeDefinition)


def test_vhdl::compositetypedefinition_constructor_exists():
    assert callable(vhdl::CompositeTypeDefinition.__init__)


def test_vhdl::compositetypedefinition_constructor_args():
    sig = inspect.signature(vhdl::CompositeTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::accesstypedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::AccessTypeDefinition)


def test_vhdl::accesstypedefinition_constructor_exists():
    assert callable(vhdl::AccessTypeDefinition.__init__)


def test_vhdl::accesstypedefinition_constructor_args():
    sig = inspect.signature(vhdl::AccessTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::typedefinition_is_not_abstract():
    assert not inspect.isabstract(vhdl::TypeDefinition)


def test_vhdl::typedefinition_constructor_exists():
    assert callable(vhdl::TypeDefinition.__init__)


def test_vhdl::typedefinition_constructor_args():
    sig = inspect.signature(vhdl::TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::TypeDeclaration)


def test_vhdl::typedeclaration_constructor_exists():
    assert callable(vhdl::TypeDeclaration.__init__)


def test_vhdl::typedeclaration_constructor_args():
    sig = inspect.signature(vhdl::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::subtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::SubtypeDeclaration)


def test_vhdl::subtypedeclaration_constructor_exists():
    assert callable(vhdl::SubtypeDeclaration.__init__)


def test_vhdl::subtypedeclaration_constructor_args():
    sig = inspect.signature(vhdl::SubtypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::conditionalwaveformexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::ConditionalWaveformExpression)


def test_vhdl::conditionalwaveformexpression_constructor_exists():
    assert callable(vhdl::ConditionalWaveformExpression.__init__)


def test_vhdl::conditionalwaveformexpression_constructor_args():
    sig = inspect.signature(vhdl::ConditionalWaveformExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::boolean_is_not_abstract():
    assert not inspect.isabstract(vhdl::Boolean)


def test_vhdl::boolean_constructor_exists():
    assert callable(vhdl::Boolean.__init__)


def test_vhdl::boolean_constructor_args():
    sig = inspect.signature(vhdl::Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl::boolean_has_value():
    assert hasattr(vhdl::Boolean, "value")
    descriptor = None
    for klass in vhdl::Boolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::open_is_not_abstract():
    assert not inspect.isabstract(vhdl::Open)


def test_vhdl::open_constructor_exists():
    assert callable(vhdl::Open.__init__)


def test_vhdl::open_constructor_args():
    sig = inspect.signature(vhdl::Open.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl::open_has_value():
    assert hasattr(vhdl::Open, "value")
    descriptor = None
    for klass in vhdl::Open.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::shiftexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::ShiftExpression)


def test_vhdl::shiftexpression_constructor_exists():
    assert callable(vhdl::ShiftExpression.__init__)


def test_vhdl::shiftexpression_constructor_args():
    sig = inspect.signature(vhdl::ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl::shiftexpression_has_operator():
    assert hasattr(vhdl::ShiftExpression, "operator")
    descriptor = None
    for klass in vhdl::ShiftExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::RelationalExpression)


def test_vhdl::relationalexpression_constructor_exists():
    assert callable(vhdl::RelationalExpression.__init__)


def test_vhdl::relationalexpression_constructor_args():
    sig = inspect.signature(vhdl::RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl::relationalexpression_has_operator():
    assert hasattr(vhdl::RelationalExpression, "operator")
    descriptor = None
    for klass in vhdl::RelationalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::addingexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::AddingExpression)


def test_vhdl::addingexpression_constructor_exists():
    assert callable(vhdl::AddingExpression.__init__)


def test_vhdl::addingexpression_constructor_args():
    sig = inspect.signature(vhdl::AddingExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl::addingexpression_has_operator():
    assert hasattr(vhdl::AddingExpression, "operator")
    descriptor = None
    for klass in vhdl::AddingExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::builtinfuncs_is_not_abstract():
    assert not inspect.isabstract(vhdl::BuiltinFuncs)


def test_vhdl::builtinfuncs_constructor_exists():
    assert callable(vhdl::BuiltinFuncs.__init__)


def test_vhdl::builtinfuncs_constructor_args():
    sig = inspect.signature(vhdl::BuiltinFuncs.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl::builtinfuncs_has_value():
    assert hasattr(vhdl::BuiltinFuncs, "value")
    descriptor = None
    for klass in vhdl::BuiltinFuncs.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::multiplyingexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::MultiplyingExpression)


def test_vhdl::multiplyingexpression_constructor_exists():
    assert callable(vhdl::MultiplyingExpression.__init__)


def test_vhdl::multiplyingexpression_constructor_args():
    sig = inspect.signature(vhdl::MultiplyingExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl::multiplyingexpression_has_operator():
    assert hasattr(vhdl::MultiplyingExpression, "operator")
    descriptor = None
    for klass in vhdl::MultiplyingExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::choiceexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::ChoiceExpression)


def test_vhdl::choiceexpression_constructor_exists():
    assert callable(vhdl::ChoiceExpression.__init__)


def test_vhdl::choiceexpression_constructor_args():
    sig = inspect.signature(vhdl::ChoiceExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::char_is_not_abstract():
    assert not inspect.isabstract(vhdl::Char)


def test_vhdl::char_constructor_exists():
    assert callable(vhdl::Char.__init__)


def test_vhdl::char_constructor_args():
    sig = inspect.signature(vhdl::Char.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl::char_has_value():
    assert hasattr(vhdl::Char, "value")
    descriptor = None
    for klass in vhdl::Char.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::memberexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::MemberExpression)


def test_vhdl::memberexpression_constructor_exists():
    assert callable(vhdl::MemberExpression.__init__)


def test_vhdl::memberexpression_constructor_args():
    sig = inspect.signature(vhdl::MemberExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::variable_is_not_abstract():
    assert not inspect.isabstract(vhdl::Variable)


def test_vhdl::variable_constructor_exists():
    assert callable(vhdl::Variable.__init__)


def test_vhdl::variable_constructor_args():
    sig = inspect.signature(vhdl::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl::variable_has_name():
    assert hasattr(vhdl::Variable, "name")
    descriptor = None
    for klass in vhdl::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::value_is_not_abstract():
    assert not inspect.isabstract(vhdl::Value)


def test_vhdl::value_constructor_exists():
    assert callable(vhdl::Value.__init__)


def test_vhdl::value_constructor_args():
    sig = inspect.signature(vhdl::Value.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::sliceexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::SliceExpression)


def test_vhdl::sliceexpression_constructor_exists():
    assert callable(vhdl::SliceExpression.__init__)


def test_vhdl::sliceexpression_constructor_args():
    sig = inspect.signature(vhdl::SliceExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::string_is_not_abstract():
    assert not inspect.isabstract(vhdl::String)


def test_vhdl::string_constructor_exists():
    assert callable(vhdl::String.__init__)


def test_vhdl::string_constructor_args():
    sig = inspect.signature(vhdl::String.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl::string_has_value():
    assert hasattr(vhdl::String, "value")
    descriptor = None
    for klass in vhdl::String.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::logicalexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::LogicalExpression)


def test_vhdl::logicalexpression_constructor_exists():
    assert callable(vhdl::LogicalExpression.__init__)


def test_vhdl::logicalexpression_constructor_args():
    sig = inspect.signature(vhdl::LogicalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl::logicalexpression_has_operator():
    assert hasattr(vhdl::LogicalExpression, "operator")
    descriptor = None
    for klass in vhdl::LogicalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::member_is_not_abstract():
    assert not inspect.isabstract(vhdl::Member)


def test_vhdl::member_constructor_exists():
    assert callable(vhdl::Member.__init__)


def test_vhdl::member_constructor_args():
    sig = inspect.signature(vhdl::Member.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::factor_is_not_abstract():
    assert not inspect.isabstract(vhdl::Factor)


def test_vhdl::factor_constructor_exists():
    assert callable(vhdl::Factor.__init__)


def test_vhdl::factor_constructor_args():
    sig = inspect.signature(vhdl::Factor.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::others_is_not_abstract():
    assert not inspect.isabstract(vhdl::Others)


def test_vhdl::others_constructor_exists():
    assert callable(vhdl::Others.__init__)


def test_vhdl::others_constructor_args():
    sig = inspect.signature(vhdl::Others.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl::others_has_value():
    assert hasattr(vhdl::Others, "value")
    descriptor = None
    for klass in vhdl::Others.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::bitstring_is_not_abstract():
    assert not inspect.isabstract(vhdl::BitString)


def test_vhdl::bitstring_constructor_exists():
    assert callable(vhdl::BitString.__init__)


def test_vhdl::bitstring_constructor_args():
    sig = inspect.signature(vhdl::BitString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl::bitstring_has_value():
    assert hasattr(vhdl::BitString, "value")
    descriptor = None
    for klass in vhdl::BitString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::rangeexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::RangeExpression)


def test_vhdl::rangeexpression_constructor_exists():
    assert callable(vhdl::RangeExpression.__init__)


def test_vhdl::rangeexpression_constructor_args():
    sig = inspect.signature(vhdl::RangeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_vhdl::rangeexpression_has_direction():
    assert hasattr(vhdl::RangeExpression, "direction")
    descriptor = None
    for klass in vhdl::RangeExpression.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_vhdl::rangeexpression_has_operator():
    assert hasattr(vhdl::RangeExpression, "operator")
    descriptor = None
    for klass in vhdl::RangeExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::multiexpression_is_not_abstract():
    assert not inspect.isabstract(vhdl::MultiExpression)


def test_vhdl::multiexpression_constructor_exists():
    assert callable(vhdl::MultiExpression.__init__)


def test_vhdl::multiexpression_constructor_args():
    sig = inspect.signature(vhdl::MultiExpression.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::ifstatementtest_is_not_abstract():
    assert not inspect.isabstract(vhdl::IfStatementTest)


def test_vhdl::ifstatementtest_constructor_exists():
    assert callable(vhdl::IfStatementTest.__init__)


def test_vhdl::ifstatementtest_constructor_args():
    sig = inspect.signature(vhdl::IfStatementTest.__init__)
    params = list(sig.parameters.keys())



def test_iterationscheme_is_not_abstract():
    assert not inspect.isabstract(IterationScheme)


def test_iterationscheme_constructor_exists():
    assert callable(IterationScheme.__init__)


def test_iterationscheme_constructor_args():
    sig = inspect.signature(IterationScheme.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::foriterationscheme_is_not_abstract():
    assert not inspect.isabstract(vhdl::ForIterationScheme)


def test_vhdl::foriterationscheme_constructor_exists():
    assert callable(vhdl::ForIterationScheme.__init__)


def test_vhdl::foriterationscheme_constructor_args():
    sig = inspect.signature(vhdl::ForIterationScheme.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_vhdl::foriterationscheme_has_variable():
    assert hasattr(vhdl::ForIterationScheme, "variable")
    descriptor = None
    for klass in vhdl::ForIterationScheme.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::casealternative_is_not_abstract():
    assert not inspect.isabstract(vhdl::CaseAlternative)


def test_vhdl::casealternative_constructor_exists():
    assert callable(vhdl::CaseAlternative.__init__)


def test_vhdl::casealternative_constructor_args():
    sig = inspect.signature(vhdl::CaseAlternative.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::genericmapassociation_is_not_abstract():
    assert not inspect.isabstract(vhdl::GenericMapAssociation)


def test_vhdl::genericmapassociation_constructor_exists():
    assert callable(vhdl::GenericMapAssociation.__init__)


def test_vhdl::genericmapassociation_constructor_args():
    sig = inspect.signature(vhdl::GenericMapAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "formal" in params, "Missing parameter 'formal'"

def test_vhdl::genericmapassociation_has_formal():
    assert hasattr(vhdl::GenericMapAssociation, "formal")
    descriptor = None
    for klass in vhdl::GenericMapAssociation.__mro__:
        if "formal" in klass.__dict__:
            descriptor = klass.__dict__["formal"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::portmapassociation_is_not_abstract():
    assert not inspect.isabstract(vhdl::PortMapAssociation)


def test_vhdl::portmapassociation_constructor_exists():
    assert callable(vhdl::PortMapAssociation.__init__)


def test_vhdl::portmapassociation_constructor_args():
    sig = inspect.signature(vhdl::PortMapAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "formal" in params, "Missing parameter 'formal'"

def test_vhdl::portmapassociation_has_formal():
    assert hasattr(vhdl::PortMapAssociation, "formal")
    descriptor = None
    for klass in vhdl::PortMapAssociation.__mro__:
        if "formal" in klass.__dict__:
            descriptor = klass.__dict__["formal"]
            break
    assert isinstance(descriptor, property)



def test_sequentialstatement_is_not_abstract():
    assert not inspect.isabstract(SequentialStatement)


def test_sequentialstatement_constructor_exists():
    assert callable(SequentialStatement.__init__)


def test_sequentialstatement_constructor_args():
    sig = inspect.signature(SequentialStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::sequentialsignalassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::SequentialSignalAssignmentStatement)


def test_vhdl::sequentialsignalassignmentstatement_constructor_exists():
    assert callable(vhdl::SequentialSignalAssignmentStatement.__init__)


def test_vhdl::sequentialsignalassignmentstatement_constructor_args():
    sig = inspect.signature(vhdl::SequentialSignalAssignmentStatement.__init__)
    params = list(sig.parameters.keys())
    assert "postponed" in params, "Missing parameter 'postponed'"
    assert "label" in params, "Missing parameter 'label'"
    assert "guarded" in params, "Missing parameter 'guarded'"

def test_vhdl::sequentialsignalassignmentstatement_has_postponed():
    assert hasattr(vhdl::SequentialSignalAssignmentStatement, "postponed")
    descriptor = None
    for klass in vhdl::SequentialSignalAssignmentStatement.__mro__:
        if "postponed" in klass.__dict__:
            descriptor = klass.__dict__["postponed"]
            break
    assert isinstance(descriptor, property)

def test_vhdl::sequentialsignalassignmentstatement_has_label():
    assert hasattr(vhdl::SequentialSignalAssignmentStatement, "label")
    descriptor = None
    for klass in vhdl::SequentialSignalAssignmentStatement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_vhdl::sequentialsignalassignmentstatement_has_guarded():
    assert hasattr(vhdl::SequentialSignalAssignmentStatement, "guarded")
    descriptor = None
    for klass in vhdl::SequentialSignalAssignmentStatement.__mro__:
        if "guarded" in klass.__dict__:
            descriptor = klass.__dict__["guarded"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::loopstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::LoopStatement)


def test_vhdl::loopstatement_constructor_exists():
    assert callable(vhdl::LoopStatement.__init__)


def test_vhdl::loopstatement_constructor_args():
    sig = inspect.signature(vhdl::LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::ifstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::IfStatement)


def test_vhdl::ifstatement_constructor_exists():
    assert callable(vhdl::IfStatement.__init__)


def test_vhdl::ifstatement_constructor_args():
    sig = inspect.signature(vhdl::IfStatement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_vhdl::ifstatement_has_label():
    assert hasattr(vhdl::IfStatement, "label")
    descriptor = None
    for klass in vhdl::IfStatement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::casestatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::CaseStatement)


def test_vhdl::casestatement_constructor_exists():
    assert callable(vhdl::CaseStatement.__init__)


def test_vhdl::casestatement_constructor_args():
    sig = inspect.signature(vhdl::CaseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_vhdl::casestatement_has_label():
    assert hasattr(vhdl::CaseStatement, "label")
    descriptor = None
    for klass in vhdl::CaseStatement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::waitstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::WaitStatement)


def test_vhdl::waitstatement_constructor_exists():
    assert callable(vhdl::WaitStatement.__init__)


def test_vhdl::waitstatement_constructor_args():
    sig = inspect.signature(vhdl::WaitStatement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_vhdl::waitstatement_has_label():
    assert hasattr(vhdl::WaitStatement, "label")
    descriptor = None
    for klass in vhdl::WaitStatement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::portmap_is_not_abstract():
    assert not inspect.isabstract(vhdl::PortMap)


def test_vhdl::portmap_constructor_exists():
    assert callable(vhdl::PortMap.__init__)


def test_vhdl::portmap_constructor_args():
    sig = inspect.signature(vhdl::PortMap.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::genericmap_is_not_abstract():
    assert not inspect.isabstract(vhdl::GenericMap)


def test_vhdl::genericmap_constructor_exists():
    assert callable(vhdl::GenericMap.__init__)


def test_vhdl::genericmap_constructor_args():
    sig = inspect.signature(vhdl::GenericMap.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::sequentialstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::SequentialStatement)


def test_vhdl::sequentialstatement_constructor_exists():
    assert callable(vhdl::SequentialStatement.__init__)


def test_vhdl::sequentialstatement_constructor_args():
    sig = inspect.signature(vhdl::SequentialStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::idlist_is_not_abstract():
    assert not inspect.isabstract(vhdl::IdList)


def test_vhdl::idlist_constructor_exists():
    assert callable(vhdl::IdList.__init__)


def test_vhdl::idlist_constructor_args():
    sig = inspect.signature(vhdl::IdList.__init__)
    params = list(sig.parameters.keys())



def test_architecturestatement_is_not_abstract():
    assert not inspect.isabstract(ArchitectureStatement)


def test_architecturestatement_constructor_exists():
    assert callable(ArchitectureStatement.__init__)


def test_architecturestatement_constructor_args():
    sig = inspect.signature(ArchitectureStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::componentinstantiationstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::ComponentInstantiationStatement)


def test_vhdl::componentinstantiationstatement_constructor_exists():
    assert callable(vhdl::ComponentInstantiationStatement.__init__)


def test_vhdl::componentinstantiationstatement_constructor_args():
    sig = inspect.signature(vhdl::ComponentInstantiationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl::componentinstantiationstatement_has_name():
    assert hasattr(vhdl::ComponentInstantiationStatement, "name")
    descriptor = None
    for klass in vhdl::ComponentInstantiationStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::ifgeneratestatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::IfGenerateStatement)


def test_vhdl::ifgeneratestatement_constructor_exists():
    assert callable(vhdl::IfGenerateStatement.__init__)


def test_vhdl::ifgeneratestatement_constructor_args():
    sig = inspect.signature(vhdl::IfGenerateStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::entityinstantiationstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::EntityInstantiationStatement)


def test_vhdl::entityinstantiationstatement_constructor_exists():
    assert callable(vhdl::EntityInstantiationStatement.__init__)


def test_vhdl::entityinstantiationstatement_constructor_args():
    sig = inspect.signature(vhdl::EntityInstantiationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl::entityinstantiationstatement_has_name():
    assert hasattr(vhdl::EntityInstantiationStatement, "name")
    descriptor = None
    for klass in vhdl::EntityInstantiationStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::conditionalsignalassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::ConditionalSignalAssignmentStatement)


def test_vhdl::conditionalsignalassignmentstatement_constructor_exists():
    assert callable(vhdl::ConditionalSignalAssignmentStatement.__init__)


def test_vhdl::conditionalsignalassignmentstatement_constructor_args():
    sig = inspect.signature(vhdl::ConditionalSignalAssignmentStatement.__init__)
    params = list(sig.parameters.keys())
    assert "guarded" in params, "Missing parameter 'guarded'"
    assert "postponed" in params, "Missing parameter 'postponed'"

def test_vhdl::conditionalsignalassignmentstatement_has_guarded():
    assert hasattr(vhdl::ConditionalSignalAssignmentStatement, "guarded")
    descriptor = None
    for klass in vhdl::ConditionalSignalAssignmentStatement.__mro__:
        if "guarded" in klass.__dict__:
            descriptor = klass.__dict__["guarded"]
            break
    assert isinstance(descriptor, property)

def test_vhdl::conditionalsignalassignmentstatement_has_postponed():
    assert hasattr(vhdl::ConditionalSignalAssignmentStatement, "postponed")
    descriptor = None
    for klass in vhdl::ConditionalSignalAssignmentStatement.__mro__:
        if "postponed" in klass.__dict__:
            descriptor = klass.__dict__["postponed"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::forgeneratestatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::ForGenerateStatement)


def test_vhdl::forgeneratestatement_constructor_exists():
    assert callable(vhdl::ForGenerateStatement.__init__)


def test_vhdl::forgeneratestatement_constructor_args():
    sig = inspect.signature(vhdl::ForGenerateStatement.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::processstatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::ProcessStatement)


def test_vhdl::processstatement_constructor_exists():
    assert callable(vhdl::ProcessStatement.__init__)


def test_vhdl::processstatement_constructor_args():
    sig = inspect.signature(vhdl::ProcessStatement.__init__)
    params = list(sig.parameters.keys())
    assert "postponed" in params, "Missing parameter 'postponed'"

def test_vhdl::processstatement_has_postponed():
    assert hasattr(vhdl::ProcessStatement, "postponed")
    descriptor = None
    for klass in vhdl::ProcessStatement.__mro__:
        if "postponed" in klass.__dict__:
            descriptor = klass.__dict__["postponed"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::subtypeindication_is_not_abstract():
    assert not inspect.isabstract(vhdl::SubtypeIndication)


def test_vhdl::subtypeindication_constructor_exists():
    assert callable(vhdl::SubtypeIndication.__init__)


def test_vhdl::subtypeindication_constructor_args():
    sig = inspect.signature(vhdl::SubtypeIndication.__init__)
    params = list(sig.parameters.keys())
    assert "builtin_type" in params, "Missing parameter 'builtin_type'"

def test_vhdl::subtypeindication_has_builtin_type():
    assert hasattr(vhdl::SubtypeIndication, "builtin_type")
    descriptor = None
    for klass in vhdl::SubtypeIndication.__mro__:
        if "builtin_type" in klass.__dict__:
            descriptor = klass.__dict__["builtin_type"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::loopvariable_is_not_abstract():
    assert not inspect.isabstract(vhdl::LoopVariable)


def test_vhdl::loopvariable_constructor_exists():
    assert callable(vhdl::LoopVariable.__init__)


def test_vhdl::loopvariable_constructor_args():
    sig = inspect.signature(vhdl::LoopVariable.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::constant_is_not_abstract():
    assert not inspect.isabstract(vhdl::Constant)


def test_vhdl::constant_constructor_exists():
    assert callable(vhdl::Constant.__init__)


def test_vhdl::constant_constructor_args():
    sig = inspect.signature(vhdl::Constant.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::port_is_not_abstract():
    assert not inspect.isabstract(vhdl::Port)


def test_vhdl::port_constructor_exists():
    assert callable(vhdl::Port.__init__)


def test_vhdl::port_constructor_args():
    sig = inspect.signature(vhdl::Port.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "mode" in params, "Missing parameter 'mode'"

def test_vhdl::port_has_kind():
    assert hasattr(vhdl::Port, "kind")
    descriptor = None
    for klass in vhdl::Port.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_vhdl::port_has_mode():
    assert hasattr(vhdl::Port, "mode")
    descriptor = None
    for klass in vhdl::Port.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::ports_is_not_abstract():
    assert not inspect.isabstract(vhdl::Ports)


def test_vhdl::ports_constructor_exists():
    assert callable(vhdl::Ports.__init__)


def test_vhdl::ports_constructor_args():
    sig = inspect.signature(vhdl::Ports.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::generics_is_not_abstract():
    assert not inspect.isabstract(vhdl::Generics)


def test_vhdl::generics_constructor_exists():
    assert callable(vhdl::Generics.__init__)


def test_vhdl::generics_constructor_args():
    sig = inspect.signature(vhdl::Generics.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::var_is_not_abstract():
    assert not inspect.isabstract(vhdl::Var)


def test_vhdl::var_constructor_exists():
    assert callable(vhdl::Var.__init__)


def test_vhdl::var_constructor_args():
    sig = inspect.signature(vhdl::Var.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::signal_is_not_abstract():
    assert not inspect.isabstract(vhdl::Signal)


def test_vhdl::signal_constructor_exists():
    assert callable(vhdl::Signal.__init__)


def test_vhdl::signal_constructor_args():
    sig = inspect.signature(vhdl::Signal.__init__)
    params = list(sig.parameters.keys())



def test_package::declarative::item_is_not_abstract():
    assert not inspect.isabstract(package::declarative::item)


def test_package::declarative::item_constructor_exists():
    assert callable(package::declarative::item.__init__)


def test_package::declarative::item_constructor_args():
    sig = inspect.signature(package::declarative::item.__init__)
    params = list(sig.parameters.keys())



def test_blockdeclarativeitem_is_not_abstract():
    assert not inspect.isabstract(BlockDeclarativeItem)


def test_blockdeclarativeitem_constructor_exists():
    assert callable(BlockDeclarativeItem.__init__)


def test_blockdeclarativeitem_constructor_args():
    sig = inspect.signature(BlockDeclarativeItem.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::VariableDeclaration)


def test_vhdl::variabledeclaration_constructor_exists():
    assert callable(vhdl::VariableDeclaration.__init__)


def test_vhdl::variabledeclaration_constructor_args():
    sig = inspect.signature(vhdl::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "shared" in params, "Missing parameter 'shared'"

def test_vhdl::variabledeclaration_has_shared():
    assert hasattr(vhdl::VariableDeclaration, "shared")
    descriptor = None
    for klass in vhdl::VariableDeclaration.__mro__:
        if "shared" in klass.__dict__:
            descriptor = klass.__dict__["shared"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::attributespecification_is_not_abstract():
    assert not inspect.isabstract(vhdl::AttributeSpecification)


def test_vhdl::attributespecification_constructor_exists():
    assert callable(vhdl::AttributeSpecification.__init__)


def test_vhdl::attributespecification_constructor_args():
    sig = inspect.signature(vhdl::AttributeSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "entity" in params, "Missing parameter 'entity'"
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl::attributespecification_has_class_():
    assert hasattr(vhdl::AttributeSpecification, "class_")
    descriptor = None
    for klass in vhdl::AttributeSpecification.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_vhdl::attributespecification_has_entity():
    assert hasattr(vhdl::AttributeSpecification, "entity")
    descriptor = None
    for klass in vhdl::AttributeSpecification.__mro__:
        if "entity" in klass.__dict__:
            descriptor = klass.__dict__["entity"]
            break
    assert isinstance(descriptor, property)

def test_vhdl::attributespecification_has_name():
    assert hasattr(vhdl::AttributeSpecification, "name")
    descriptor = None
    for klass in vhdl::AttributeSpecification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::signaldeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::SignalDeclaration)


def test_vhdl::signaldeclaration_constructor_exists():
    assert callable(vhdl::SignalDeclaration.__init__)


def test_vhdl::signaldeclaration_constructor_args():
    sig = inspect.signature(vhdl::SignalDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_vhdl::signaldeclaration_has_kind():
    assert hasattr(vhdl::SignalDeclaration, "kind")
    descriptor = None
    for klass in vhdl::SignalDeclaration.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::type_is_not_abstract():
    assert not inspect.isabstract(vhdl::Type)


def test_vhdl::type_constructor_exists():
    assert callable(vhdl::Type.__init__)


def test_vhdl::type_constructor_args():
    sig = inspect.signature(vhdl::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_vhdl::type_has_name():
    assert hasattr(vhdl::Type, "name")
    descriptor = None
    for klass in vhdl::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_vhdl::type_has_value():
    assert hasattr(vhdl::Type, "value")
    descriptor = None
    for klass in vhdl::Type.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::ConstantDeclaration)


def test_vhdl::constantdeclaration_constructor_exists():
    assert callable(vhdl::ConstantDeclaration.__init__)


def test_vhdl::constantdeclaration_constructor_args():
    sig = inspect.signature(vhdl::ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::component_is_not_abstract():
    assert not inspect.isabstract(vhdl::Component)


def test_vhdl::component_constructor_exists():
    assert callable(vhdl::Component.__init__)


def test_vhdl::component_constructor_args():
    sig = inspect.signature(vhdl::Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl::component_has_name():
    assert hasattr(vhdl::Component, "name")
    descriptor = None
    for klass in vhdl::Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::attributedeclaration_is_not_abstract():
    assert not inspect.isabstract(vhdl::AttributeDeclaration)


def test_vhdl::attributedeclaration_constructor_exists():
    assert callable(vhdl::AttributeDeclaration.__init__)


def test_vhdl::attributedeclaration_constructor_args():
    sig = inspect.signature(vhdl::AttributeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "type_keyword" in params, "Missing parameter 'type_keyword'"
    assert "type_id" in params, "Missing parameter 'type_id'"
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl::attributedeclaration_has_type_keyword():
    assert hasattr(vhdl::AttributeDeclaration, "type_keyword")
    descriptor = None
    for klass in vhdl::AttributeDeclaration.__mro__:
        if "type_keyword" in klass.__dict__:
            descriptor = klass.__dict__["type_keyword"]
            break
    assert isinstance(descriptor, property)

def test_vhdl::attributedeclaration_has_type_id():
    assert hasattr(vhdl::AttributeDeclaration, "type_id")
    descriptor = None
    for klass in vhdl::AttributeDeclaration.__mro__:
        if "type_id" in klass.__dict__:
            descriptor = klass.__dict__["type_id"]
            break
    assert isinstance(descriptor, property)

def test_vhdl::attributedeclaration_has_name():
    assert hasattr(vhdl::AttributeDeclaration, "name")
    descriptor = None
    for klass in vhdl::AttributeDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::alias_is_not_abstract():
    assert not inspect.isabstract(vhdl::Alias)


def test_vhdl::alias_constructor_exists():
    assert callable(vhdl::Alias.__init__)


def test_vhdl::alias_constructor_args():
    sig = inspect.signature(vhdl::Alias.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::generic_is_not_abstract():
    assert not inspect.isabstract(vhdl::Generic)


def test_vhdl::generic_constructor_exists():
    assert callable(vhdl::Generic.__init__)


def test_vhdl::generic_constructor_args():
    sig = inspect.signature(vhdl::Generic.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::expression_is_not_abstract():
    assert not inspect.isabstract(vhdl::Expression)


def test_vhdl::expression_constructor_exists():
    assert callable(vhdl::Expression.__init__)


def test_vhdl::expression_constructor_args():
    sig = inspect.signature(vhdl::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "unary_operator" in params, "Missing parameter 'unary_operator'"

def test_vhdl::expression_has_attribute():
    assert hasattr(vhdl::Expression, "attribute")
    descriptor = None
    for klass in vhdl::Expression.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_vhdl::expression_has_unary_operator():
    assert hasattr(vhdl::Expression, "unary_operator")
    descriptor = None
    for klass in vhdl::Expression.__mro__:
        if "unary_operator" in klass.__dict__:
            descriptor = klass.__dict__["unary_operator"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::designfile_is_not_abstract():
    assert not inspect.isabstract(vhdl::DesignFile)


def test_vhdl::designfile_constructor_exists():
    assert callable(vhdl::DesignFile.__init__)


def test_vhdl::designfile_constructor_args():
    sig = inspect.signature(vhdl::DesignFile.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::architecturestatement_is_not_abstract():
    assert not inspect.isabstract(vhdl::ArchitectureStatement)


def test_vhdl::architecturestatement_constructor_exists():
    assert callable(vhdl::ArchitectureStatement.__init__)


def test_vhdl::architecturestatement_constructor_args():
    sig = inspect.signature(vhdl::ArchitectureStatement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_vhdl::architecturestatement_has_label():
    assert hasattr(vhdl::ArchitectureStatement, "label")
    descriptor = None
    for klass in vhdl::ArchitectureStatement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::blockdeclarativeitem_is_not_abstract():
    assert not inspect.isabstract(vhdl::BlockDeclarativeItem)


def test_vhdl::blockdeclarativeitem_constructor_exists():
    assert callable(vhdl::BlockDeclarativeItem.__init__)


def test_vhdl::blockdeclarativeitem_constructor_args():
    sig = inspect.signature(vhdl::BlockDeclarativeItem.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::package::declarative::part_is_not_abstract():
    assert not inspect.isabstract(vhdl::package::declarative::part)


def test_vhdl::package::declarative::part_constructor_exists():
    assert callable(vhdl::package::declarative::part.__init__)


def test_vhdl::package::declarative::part_constructor_args():
    sig = inspect.signature(vhdl::package::declarative::part.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::package::declarative::item_is_not_abstract():
    assert not inspect.isabstract(vhdl::package::declarative::item)


def test_vhdl::package::declarative::item_constructor_exists():
    assert callable(vhdl::package::declarative::item.__init__)


def test_vhdl::package::declarative::item_constructor_args():
    sig = inspect.signature(vhdl::package::declarative::item.__init__)
    params = list(sig.parameters.keys())



def test_libraryunit_is_not_abstract():
    assert not inspect.isabstract(LibraryUnit)


def test_libraryunit_constructor_exists():
    assert callable(LibraryUnit.__init__)


def test_libraryunit_constructor_args():
    sig = inspect.signature(LibraryUnit.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::entity_is_not_abstract():
    assert not inspect.isabstract(vhdl::Entity)


def test_vhdl::entity_constructor_exists():
    assert callable(vhdl::Entity.__init__)


def test_vhdl::entity_constructor_args():
    sig = inspect.signature(vhdl::Entity.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::architecture_is_not_abstract():
    assert not inspect.isabstract(vhdl::Architecture)


def test_vhdl::architecture_constructor_exists():
    assert callable(vhdl::Architecture.__init__)


def test_vhdl::architecture_constructor_args():
    sig = inspect.signature(vhdl::Architecture.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::package_is_not_abstract():
    assert not inspect.isabstract(vhdl::Package)


def test_vhdl::package_constructor_exists():
    assert callable(vhdl::Package.__init__)


def test_vhdl::package_constructor_args():
    sig = inspect.signature(vhdl::Package.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::library_is_not_abstract():
    assert not inspect.isabstract(vhdl::Library)


def test_vhdl::library_constructor_exists():
    assert callable(vhdl::Library.__init__)


def test_vhdl::library_constructor_args():
    sig = inspect.signature(vhdl::Library.__init__)
    params = list(sig.parameters.keys())
    assert "builtin_lib" in params, "Missing parameter 'builtin_lib'"

def test_vhdl::library_has_builtin_lib():
    assert hasattr(vhdl::Library, "builtin_lib")
    descriptor = None
    for klass in vhdl::Library.__mro__:
        if "builtin_lib" in klass.__dict__:
            descriptor = klass.__dict__["builtin_lib"]
            break
    assert isinstance(descriptor, property)



def test_contextitem_is_not_abstract():
    assert not inspect.isabstract(ContextItem)


def test_contextitem_constructor_exists():
    assert callable(ContextItem.__init__)


def test_contextitem_constructor_args():
    sig = inspect.signature(ContextItem.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::libraryclause_is_not_abstract():
    assert not inspect.isabstract(vhdl::LibraryClause)


def test_vhdl::libraryclause_constructor_exists():
    assert callable(vhdl::LibraryClause.__init__)


def test_vhdl::libraryclause_constructor_args():
    sig = inspect.signature(vhdl::LibraryClause.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl::libraryclause_has_name():
    assert hasattr(vhdl::LibraryClause, "name")
    descriptor = None
    for klass in vhdl::LibraryClause.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::useclause_is_not_abstract():
    assert not inspect.isabstract(vhdl::UseClause)


def test_vhdl::useclause_constructor_exists():
    assert callable(vhdl::UseClause.__init__)


def test_vhdl::useclause_constructor_args():
    sig = inspect.signature(vhdl::UseClause.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_vhdl::useclause_has_importedNamespace():
    assert hasattr(vhdl::UseClause, "importedNamespace")
    descriptor = None
    for klass in vhdl::UseClause.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::libraryunit_is_not_abstract():
    assert not inspect.isabstract(vhdl::LibraryUnit)


def test_vhdl::libraryunit_constructor_exists():
    assert callable(vhdl::LibraryUnit.__init__)


def test_vhdl::libraryunit_constructor_args():
    sig = inspect.signature(vhdl::LibraryUnit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vhdl::libraryunit_has_name():
    assert hasattr(vhdl::LibraryUnit, "name")
    descriptor = None
    for klass in vhdl::LibraryUnit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vhdl::contextitem_is_not_abstract():
    assert not inspect.isabstract(vhdl::ContextItem)


def test_vhdl::contextitem_constructor_exists():
    assert callable(vhdl::ContextItem.__init__)


def test_vhdl::contextitem_constructor_args():
    sig = inspect.signature(vhdl::ContextItem.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::whileiterationscheme_is_not_abstract():
    assert not inspect.isabstract(vhdl::WhileIterationScheme)


def test_vhdl::whileiterationscheme_constructor_exists():
    assert callable(vhdl::WhileIterationScheme.__init__)


def test_vhdl::whileiterationscheme_constructor_args():
    sig = inspect.signature(vhdl::WhileIterationScheme.__init__)
    params = list(sig.parameters.keys())



def test_vhdl::iterationscheme_is_not_abstract():
    assert not inspect.isabstract(vhdl::IterationScheme)


def test_vhdl::iterationscheme_constructor_exists():
    assert callable(vhdl::IterationScheme.__init__)


def test_vhdl::iterationscheme_constructor_args():
    sig = inspect.signature(vhdl::IterationScheme.__init__)
    params = list(sig.parameters.keys())

def test_rangedirection_exists():
    # Check that the Enumeration exists
    assert RangeDirection is not None

def test_rangedirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RangeDirection]
    expected_literals = [
        "TO",
        "DOWNTO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RangeDirection"

def test_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "ABS",
        "NOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

def test_addingoperator_exists():
    # Check that the Enumeration exists
    assert AddingOperator is not None

def test_addingoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AddingOperator]
    expected_literals = [
        "MINUS",
        "AMPERSAND",
        "PLUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AddingOperator"

def test_sign_exists():
    # Check that the Enumeration exists
    assert Sign is not None

def test_sign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sign]
    expected_literals = [
        "MINUS",
        "PLUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sign"

def test_estring_exists():
    # Check that the Enumeration exists
    assert EString is not None

def test_estring_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EString]
    expected_literals = [
        "NATURAL",
        "TO_UNSIGNED",
        "UNSIGNED",
        "STRING",
        "FALLING_EDGE",
        "STD_LOGIC",
        "RISING_EDGE",
        "INTEGER",
        "STD_LOGIC_VECTOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EString"

def test_multiplyingoperator_exists():
    # Check that the Enumeration exists
    assert MultiplyingOperator is not None

def test_multiplyingoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplyingOperator]
    expected_literals = [
        "REM",
        "MUL",
        "DIV",
        "MOD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplyingOperator"

def test_entityclass_exists():
    # Check that the Enumeration exists
    assert EntityClass is not None

def test_entityclass_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EntityClass]
    expected_literals = [
        "PROCEDURE",
        "NATURE",
        "GROUP",
        "CONFIGURATION",
        "VARIABLE",
        "SUBNATURE",
        "ARCHITECTURE",
        "TYPE",
        "TERMINAL",
        "QUANTITY",
        "LABEL",
        "PACKAGE",
        "SIGNAL",
        "FUNCTION",
        "UNITS",
        "COMPONENT",
        "CONSTANT",
        "FILE",
        "SUBTYPE",
        "LITERAL",
        "ENTITY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EntityClass"

def test_logicaloperator_exists():
    # Check that the Enumeration exists
    assert LogicalOperator is not None

def test_logicaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOperator]
    expected_literals = [
        "AND",
        "NAND",
        "OR",
        "XOR",
        "NOR",
        "XNOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalOperator"

def test_builtinlibs_exists():
    # Check that the Enumeration exists
    assert BuiltinLibs is not None

def test_builtinlibs_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuiltinLibs]
    expected_literals = [
        "WORK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuiltinLibs"

def test_signalkind_exists():
    # Check that the Enumeration exists
    assert SignalKind is not None

def test_signalkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SignalKind]
    expected_literals = [
        "BUS",
        "REGISTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SignalKind"

def test_shiftoperator_exists():
    # Check that the Enumeration exists
    assert ShiftOperator is not None

def test_shiftoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShiftOperator]
    expected_literals = [
        "ROL",
        "SRL",
        "SRA",
        "SLL",
        "ROR",
        "SLA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShiftOperator"

def test_mode_exists():
    # Check that the Enumeration exists
    assert Mode is not None

def test_mode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Mode]
    expected_literals = [
        "IN",
        "BUFFER",
        "OUT",
        "INOUT",
        "LINKAGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Mode"

def test_purity_exists():
    # Check that the Enumeration exists
    assert Purity is not None

def test_purity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Purity]
    expected_literals = [
        "IMPURE",
        "PURE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Purity"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "LOWERTHAN",
        "EQ",
        "LE",
        "ASSOCIATE",
        "GE",
        "NEQ",
        "GREATERTHAN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"


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
ValueExpression_strategy = st.builds(
    ValueExpression,
)
vhdl::UnitValueExpression_strategy = st.builds(
    vhdl::UnitValueExpression,
    unit=
        safe_text
)
vhdl::ValueExpression_strategy = st.builds(
    vhdl::ValueExpression,
    value=
        safe_text
)
ArrayTypeDefinition_strategy = st.builds(
    ArrayTypeDefinition,
)
vhdl::ConstrainedArrayTypeDefinition_strategy = st.builds(
    vhdl::ConstrainedArrayTypeDefinition,
)
vhdl::UnconstrainedArrayTypeDefinition_strategy = st.builds(
    vhdl::UnconstrainedArrayTypeDefinition,
    index=
        safe_text
)
CompositeTypeDefinition_strategy = st.builds(
    CompositeTypeDefinition,
)
vhdl::ArrayTypeDefinition_strategy = st.builds(
    vhdl::ArrayTypeDefinition,
)
vhdl::RecordTypeDefinition_strategy = st.builds(
    vhdl::RecordTypeDefinition,
)
vhdl::RecordField_strategy = st.builds(
    vhdl::RecordField,
    name=
        safe_text
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
vhdl::FileTypeDefinition_strategy = st.builds(
    vhdl::FileTypeDefinition,
    type=
        safe_text
)
vhdl::EnumerationTypeDefinition_strategy = st.builds(
    vhdl::EnumerationTypeDefinition,
    literal=
        safe_text
)
vhdl::CompositeTypeDefinition_strategy = st.builds(
    vhdl::CompositeTypeDefinition,
)
vhdl::AccessTypeDefinition_strategy = st.builds(
    vhdl::AccessTypeDefinition,
)
vhdl::TypeDefinition_strategy = st.builds(
    vhdl::TypeDefinition,
)
Type_strategy = st.builds(
    Type,
)
vhdl::TypeDeclaration_strategy = st.builds(
    vhdl::TypeDeclaration,
)
vhdl::SubtypeDeclaration_strategy = st.builds(
    vhdl::SubtypeDeclaration,
)
Expression_strategy = st.builds(
    Expression,
)
vhdl::ConditionalWaveformExpression_strategy = st.builds(
    vhdl::ConditionalWaveformExpression,
)
vhdl::Boolean_strategy = st.builds(
    vhdl::Boolean,
    value=
        safe_text
)
vhdl::Open_strategy = st.builds(
    vhdl::Open,
    value=
        safe_text
)
vhdl::ShiftExpression_strategy = st.builds(
    vhdl::ShiftExpression,
    operator=
        safe_text
)
vhdl::RelationalExpression_strategy = st.builds(
    vhdl::RelationalExpression,
    operator=
        safe_text
)
vhdl::AddingExpression_strategy = st.builds(
    vhdl::AddingExpression,
    operator=
        safe_text
)
vhdl::BuiltinFuncs_strategy = st.builds(
    vhdl::BuiltinFuncs,
    value=
        safe_text
)
vhdl::MultiplyingExpression_strategy = st.builds(
    vhdl::MultiplyingExpression,
    operator=
        safe_text
)
vhdl::ChoiceExpression_strategy = st.builds(
    vhdl::ChoiceExpression,
)
vhdl::Char_strategy = st.builds(
    vhdl::Char,
    value=
        safe_text
)
vhdl::MemberExpression_strategy = st.builds(
    vhdl::MemberExpression,
)
vhdl::Variable_strategy = st.builds(
    vhdl::Variable,
    name=
        safe_text
)
vhdl::Value_strategy = st.builds(
    vhdl::Value,
)
vhdl::SliceExpression_strategy = st.builds(
    vhdl::SliceExpression,
)
vhdl::String_strategy = st.builds(
    vhdl::String,
    value=
        safe_text
)
vhdl::LogicalExpression_strategy = st.builds(
    vhdl::LogicalExpression,
    operator=
        safe_text
)
vhdl::Member_strategy = st.builds(
    vhdl::Member,
)
vhdl::Factor_strategy = st.builds(
    vhdl::Factor,
)
vhdl::Others_strategy = st.builds(
    vhdl::Others,
    value=
        safe_text
)
vhdl::BitString_strategy = st.builds(
    vhdl::BitString,
    value=
        safe_text
)
vhdl::RangeExpression_strategy = st.builds(
    vhdl::RangeExpression,
    direction=
        safe_text,
    operator=
        safe_text
)
vhdl::MultiExpression_strategy = st.builds(
    vhdl::MultiExpression,
)
vhdl::IfStatementTest_strategy = st.builds(
    vhdl::IfStatementTest,
)
IterationScheme_strategy = st.builds(
    IterationScheme,
)
vhdl::ForIterationScheme_strategy = st.builds(
    vhdl::ForIterationScheme,
    variable=
        safe_text
)
vhdl::CaseAlternative_strategy = st.builds(
    vhdl::CaseAlternative,
)
vhdl::GenericMapAssociation_strategy = st.builds(
    vhdl::GenericMapAssociation,
    formal=
        safe_text
)
vhdl::PortMapAssociation_strategy = st.builds(
    vhdl::PortMapAssociation,
    formal=
        safe_text
)
SequentialStatement_strategy = st.builds(
    SequentialStatement,
)
vhdl::SequentialSignalAssignmentStatement_strategy = st.builds(
    vhdl::SequentialSignalAssignmentStatement,
    postponed=
        st.booleans(),
    label=
        safe_text,
    guarded=
        st.booleans()
)
vhdl::LoopStatement_strategy = st.builds(
    vhdl::LoopStatement,
)
vhdl::IfStatement_strategy = st.builds(
    vhdl::IfStatement,
    label=
        safe_text
)
vhdl::CaseStatement_strategy = st.builds(
    vhdl::CaseStatement,
    label=
        safe_text
)
vhdl::WaitStatement_strategy = st.builds(
    vhdl::WaitStatement,
    label=
        safe_text
)
vhdl::PortMap_strategy = st.builds(
    vhdl::PortMap,
)
vhdl::GenericMap_strategy = st.builds(
    vhdl::GenericMap,
)
vhdl::SequentialStatement_strategy = st.builds(
    vhdl::SequentialStatement,
)
vhdl::IdList_strategy = st.builds(
    vhdl::IdList,
)
ArchitectureStatement_strategy = st.builds(
    ArchitectureStatement,
)
vhdl::ComponentInstantiationStatement_strategy = st.builds(
    vhdl::ComponentInstantiationStatement,
    name=
        safe_text
)
vhdl::IfGenerateStatement_strategy = st.builds(
    vhdl::IfGenerateStatement,
)
vhdl::EntityInstantiationStatement_strategy = st.builds(
    vhdl::EntityInstantiationStatement,
    name=
        safe_text
)
vhdl::ConditionalSignalAssignmentStatement_strategy = st.builds(
    vhdl::ConditionalSignalAssignmentStatement,
    guarded=
        st.booleans(),
    postponed=
        st.booleans()
)
vhdl::ForGenerateStatement_strategy = st.builds(
    vhdl::ForGenerateStatement,
)
vhdl::ProcessStatement_strategy = st.builds(
    vhdl::ProcessStatement,
    postponed=
        st.booleans()
)
vhdl::SubtypeIndication_strategy = st.builds(
    vhdl::SubtypeIndication,
    builtin_type=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
vhdl::LoopVariable_strategy = st.builds(
    vhdl::LoopVariable,
)
vhdl::Constant_strategy = st.builds(
    vhdl::Constant,
)
vhdl::Port_strategy = st.builds(
    vhdl::Port,
    kind=
        safe_text,
    mode=
        safe_text
)
vhdl::Ports_strategy = st.builds(
    vhdl::Ports,
)
vhdl::Generics_strategy = st.builds(
    vhdl::Generics,
)
vhdl::Var_strategy = st.builds(
    vhdl::Var,
)
vhdl::Signal_strategy = st.builds(
    vhdl::Signal,
)
package::declarative::item_strategy = st.builds(
    package::declarative::item,
)
BlockDeclarativeItem_strategy = st.builds(
    BlockDeclarativeItem,
)
vhdl::VariableDeclaration_strategy = st.builds(
    vhdl::VariableDeclaration,
    shared=
        st.booleans()
)
vhdl::AttributeSpecification_strategy = st.builds(
    vhdl::AttributeSpecification,
    class_=
        safe_text,
    entity=
        safe_text,
    name=
        safe_text
)
vhdl::SignalDeclaration_strategy = st.builds(
    vhdl::SignalDeclaration,
    kind=
        safe_text
)
vhdl::Type_strategy = st.builds(
    vhdl::Type,
    name=
        safe_text,
    value=
        safe_text
)
vhdl::ConstantDeclaration_strategy = st.builds(
    vhdl::ConstantDeclaration,
)
vhdl::Component_strategy = st.builds(
    vhdl::Component,
    name=
        safe_text
)
vhdl::AttributeDeclaration_strategy = st.builds(
    vhdl::AttributeDeclaration,
    type_keyword=
        safe_text,
    type_id=
        safe_text,
    name=
        safe_text
)
vhdl::Alias_strategy = st.builds(
    vhdl::Alias,
)
vhdl::Generic_strategy = st.builds(
    vhdl::Generic,
)
vhdl::Expression_strategy = st.builds(
    vhdl::Expression,
    attribute=
        safe_text,
    unary_operator=
        safe_text
)
vhdl::DesignFile_strategy = st.builds(
    vhdl::DesignFile,
)
vhdl::ArchitectureStatement_strategy = st.builds(
    vhdl::ArchitectureStatement,
    label=
        safe_text
)
vhdl::BlockDeclarativeItem_strategy = st.builds(
    vhdl::BlockDeclarativeItem,
)
vhdl::package::declarative::part_strategy = st.builds(
    vhdl::package::declarative::part,
)
vhdl::package::declarative::item_strategy = st.builds(
    vhdl::package::declarative::item,
)
LibraryUnit_strategy = st.builds(
    LibraryUnit,
)
vhdl::Entity_strategy = st.builds(
    vhdl::Entity,
)
vhdl::Architecture_strategy = st.builds(
    vhdl::Architecture,
)
vhdl::Package_strategy = st.builds(
    vhdl::Package,
)
vhdl::Library_strategy = st.builds(
    vhdl::Library,
    builtin_lib=
        safe_text
)
ContextItem_strategy = st.builds(
    ContextItem,
)
vhdl::LibraryClause_strategy = st.builds(
    vhdl::LibraryClause,
    name=
        safe_text
)
vhdl::UseClause_strategy = st.builds(
    vhdl::UseClause,
    importedNamespace=
        safe_text
)
vhdl::LibraryUnit_strategy = st.builds(
    vhdl::LibraryUnit,
    name=
        safe_text
)
vhdl::ContextItem_strategy = st.builds(
    vhdl::ContextItem,
)
vhdl::WhileIterationScheme_strategy = st.builds(
    vhdl::WhileIterationScheme,
)
vhdl::IterationScheme_strategy = st.builds(
    vhdl::IterationScheme,
)

@given(instance=ValueExpression_strategy)
@settings(max_examples=50)
def test_valueexpression_instantiation(instance):
    assert isinstance(instance, ValueExpression)

@given(instance=vhdl::UnitValueExpression_strategy)
@settings(max_examples=50)
def test_vhdl::unitvalueexpression_instantiation(instance):
    assert isinstance(instance, vhdl::UnitValueExpression)

@given(instance=vhdl::UnitValueExpression_strategy)
def test_vhdl::unitvalueexpression_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=vhdl::UnitValueExpression_strategy)
def test_vhdl::unitvalueexpression_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=vhdl::ValueExpression_strategy)
@settings(max_examples=50)
def test_vhdl::valueexpression_instantiation(instance):
    assert isinstance(instance, vhdl::ValueExpression)

@given(instance=vhdl::ValueExpression_strategy)
def test_vhdl::valueexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vhdl::ValueExpression_strategy)
def test_vhdl::valueexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_arraytypedefinition_instantiation(instance):
    assert isinstance(instance, ArrayTypeDefinition)

@given(instance=vhdl::ConstrainedArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::constrainedarraytypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::ConstrainedArrayTypeDefinition)

@given(instance=vhdl::UnconstrainedArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::unconstrainedarraytypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::UnconstrainedArrayTypeDefinition)

@given(instance=vhdl::UnconstrainedArrayTypeDefinition_strategy)
def test_vhdl::unconstrainedarraytypedefinition_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=vhdl::UnconstrainedArrayTypeDefinition_strategy)
def test_vhdl::unconstrainedarraytypedefinition_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=CompositeTypeDefinition_strategy)
@settings(max_examples=50)
def test_compositetypedefinition_instantiation(instance):
    assert isinstance(instance, CompositeTypeDefinition)

@given(instance=vhdl::ArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::arraytypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::ArrayTypeDefinition)

@given(instance=vhdl::RecordTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::recordtypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::RecordTypeDefinition)

@given(instance=vhdl::RecordField_strategy)
@settings(max_examples=50)
def test_vhdl::recordfield_instantiation(instance):
    assert isinstance(instance, vhdl::RecordField)

@given(instance=vhdl::RecordField_strategy)
def test_vhdl::recordfield_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vhdl::RecordField_strategy)
def test_vhdl::recordfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=vhdl::FileTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::filetypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::FileTypeDefinition)

@given(instance=vhdl::FileTypeDefinition_strategy)
def test_vhdl::filetypedefinition_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=vhdl::FileTypeDefinition_strategy)
def test_vhdl::filetypedefinition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=vhdl::EnumerationTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::enumerationtypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::EnumerationTypeDefinition)

@given(instance=vhdl::EnumerationTypeDefinition_strategy)
def test_vhdl::enumerationtypedefinition_literal_type(instance):
    assert isinstance(instance.literal, str)


@given(instance=vhdl::EnumerationTypeDefinition_strategy)
def test_vhdl::enumerationtypedefinition_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=vhdl::CompositeTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::compositetypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::CompositeTypeDefinition)

@given(instance=vhdl::AccessTypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::accesstypedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::AccessTypeDefinition)

@given(instance=vhdl::TypeDefinition_strategy)
@settings(max_examples=50)
def test_vhdl::typedefinition_instantiation(instance):
    assert isinstance(instance, vhdl::TypeDefinition)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=vhdl::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::typedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::TypeDeclaration)

@given(instance=vhdl::SubtypeDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::subtypedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::SubtypeDeclaration)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=vhdl::ConditionalWaveformExpression_strategy)
@settings(max_examples=50)
def test_vhdl::conditionalwaveformexpression_instantiation(instance):
    assert isinstance(instance, vhdl::ConditionalWaveformExpression)

@given(instance=vhdl::Boolean_strategy)
@settings(max_examples=50)
def test_vhdl::boolean_instantiation(instance):
    assert isinstance(instance, vhdl::Boolean)

@given(instance=vhdl::Boolean_strategy)
def test_vhdl::boolean_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vhdl::Boolean_strategy)
def test_vhdl::boolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vhdl::Open_strategy)
@settings(max_examples=50)
def test_vhdl::open_instantiation(instance):
    assert isinstance(instance, vhdl::Open)

@given(instance=vhdl::Open_strategy)
def test_vhdl::open_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vhdl::Open_strategy)
def test_vhdl::open_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vhdl::ShiftExpression_strategy)
@settings(max_examples=50)
def test_vhdl::shiftexpression_instantiation(instance):
    assert isinstance(instance, vhdl::ShiftExpression)

@given(instance=vhdl::ShiftExpression_strategy)
def test_vhdl::shiftexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=vhdl::ShiftExpression_strategy)
def test_vhdl::shiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl::RelationalExpression_strategy)
@settings(max_examples=50)
def test_vhdl::relationalexpression_instantiation(instance):
    assert isinstance(instance, vhdl::RelationalExpression)

@given(instance=vhdl::RelationalExpression_strategy)
def test_vhdl::relationalexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=vhdl::RelationalExpression_strategy)
def test_vhdl::relationalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl::AddingExpression_strategy)
@settings(max_examples=50)
def test_vhdl::addingexpression_instantiation(instance):
    assert isinstance(instance, vhdl::AddingExpression)

@given(instance=vhdl::AddingExpression_strategy)
def test_vhdl::addingexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=vhdl::AddingExpression_strategy)
def test_vhdl::addingexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl::BuiltinFuncs_strategy)
@settings(max_examples=50)
def test_vhdl::builtinfuncs_instantiation(instance):
    assert isinstance(instance, vhdl::BuiltinFuncs)

@given(instance=vhdl::BuiltinFuncs_strategy)
def test_vhdl::builtinfuncs_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vhdl::BuiltinFuncs_strategy)
def test_vhdl::builtinfuncs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vhdl::MultiplyingExpression_strategy)
@settings(max_examples=50)
def test_vhdl::multiplyingexpression_instantiation(instance):
    assert isinstance(instance, vhdl::MultiplyingExpression)

@given(instance=vhdl::MultiplyingExpression_strategy)
def test_vhdl::multiplyingexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=vhdl::MultiplyingExpression_strategy)
def test_vhdl::multiplyingexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl::ChoiceExpression_strategy)
@settings(max_examples=50)
def test_vhdl::choiceexpression_instantiation(instance):
    assert isinstance(instance, vhdl::ChoiceExpression)

@given(instance=vhdl::Char_strategy)
@settings(max_examples=50)
def test_vhdl::char_instantiation(instance):
    assert isinstance(instance, vhdl::Char)

@given(instance=vhdl::Char_strategy)
def test_vhdl::char_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vhdl::Char_strategy)
def test_vhdl::char_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vhdl::MemberExpression_strategy)
@settings(max_examples=50)
def test_vhdl::memberexpression_instantiation(instance):
    assert isinstance(instance, vhdl::MemberExpression)

@given(instance=vhdl::Variable_strategy)
@settings(max_examples=50)
def test_vhdl::variable_instantiation(instance):
    assert isinstance(instance, vhdl::Variable)

@given(instance=vhdl::Variable_strategy)
def test_vhdl::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vhdl::Variable_strategy)
def test_vhdl::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vhdl::Value_strategy)
@settings(max_examples=50)
def test_vhdl::value_instantiation(instance):
    assert isinstance(instance, vhdl::Value)

@given(instance=vhdl::SliceExpression_strategy)
@settings(max_examples=50)
def test_vhdl::sliceexpression_instantiation(instance):
    assert isinstance(instance, vhdl::SliceExpression)

@given(instance=vhdl::String_strategy)
@settings(max_examples=50)
def test_vhdl::string_instantiation(instance):
    assert isinstance(instance, vhdl::String)

@given(instance=vhdl::String_strategy)
def test_vhdl::string_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vhdl::String_strategy)
def test_vhdl::string_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vhdl::LogicalExpression_strategy)
@settings(max_examples=50)
def test_vhdl::logicalexpression_instantiation(instance):
    assert isinstance(instance, vhdl::LogicalExpression)

@given(instance=vhdl::LogicalExpression_strategy)
def test_vhdl::logicalexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=vhdl::LogicalExpression_strategy)
def test_vhdl::logicalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl::Member_strategy)
@settings(max_examples=50)
def test_vhdl::member_instantiation(instance):
    assert isinstance(instance, vhdl::Member)

@given(instance=vhdl::Factor_strategy)
@settings(max_examples=50)
def test_vhdl::factor_instantiation(instance):
    assert isinstance(instance, vhdl::Factor)

@given(instance=vhdl::Others_strategy)
@settings(max_examples=50)
def test_vhdl::others_instantiation(instance):
    assert isinstance(instance, vhdl::Others)

@given(instance=vhdl::Others_strategy)
def test_vhdl::others_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vhdl::Others_strategy)
def test_vhdl::others_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vhdl::BitString_strategy)
@settings(max_examples=50)
def test_vhdl::bitstring_instantiation(instance):
    assert isinstance(instance, vhdl::BitString)

@given(instance=vhdl::BitString_strategy)
def test_vhdl::bitstring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vhdl::BitString_strategy)
def test_vhdl::bitstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vhdl::RangeExpression_strategy)
@settings(max_examples=50)
def test_vhdl::rangeexpression_instantiation(instance):
    assert isinstance(instance, vhdl::RangeExpression)

@given(instance=vhdl::RangeExpression_strategy)
def test_vhdl::rangeexpression_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=vhdl::RangeExpression_strategy)
def test_vhdl::rangeexpression_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=vhdl::RangeExpression_strategy)
def test_vhdl::rangeexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=vhdl::RangeExpression_strategy)
def test_vhdl::rangeexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=vhdl::MultiExpression_strategy)
@settings(max_examples=50)
def test_vhdl::multiexpression_instantiation(instance):
    assert isinstance(instance, vhdl::MultiExpression)

@given(instance=vhdl::IfStatementTest_strategy)
@settings(max_examples=50)
def test_vhdl::ifstatementtest_instantiation(instance):
    assert isinstance(instance, vhdl::IfStatementTest)

@given(instance=IterationScheme_strategy)
@settings(max_examples=50)
def test_iterationscheme_instantiation(instance):
    assert isinstance(instance, IterationScheme)

@given(instance=vhdl::ForIterationScheme_strategy)
@settings(max_examples=50)
def test_vhdl::foriterationscheme_instantiation(instance):
    assert isinstance(instance, vhdl::ForIterationScheme)

@given(instance=vhdl::ForIterationScheme_strategy)
def test_vhdl::foriterationscheme_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=vhdl::ForIterationScheme_strategy)
def test_vhdl::foriterationscheme_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=vhdl::CaseAlternative_strategy)
@settings(max_examples=50)
def test_vhdl::casealternative_instantiation(instance):
    assert isinstance(instance, vhdl::CaseAlternative)

@given(instance=vhdl::GenericMapAssociation_strategy)
@settings(max_examples=50)
def test_vhdl::genericmapassociation_instantiation(instance):
    assert isinstance(instance, vhdl::GenericMapAssociation)

@given(instance=vhdl::GenericMapAssociation_strategy)
def test_vhdl::genericmapassociation_formal_type(instance):
    assert isinstance(instance.formal, str)


@given(instance=vhdl::GenericMapAssociation_strategy)
def test_vhdl::genericmapassociation_formal_setter(instance):
    original = instance.formal
    instance.formal = original
    assert instance.formal == original

@given(instance=vhdl::PortMapAssociation_strategy)
@settings(max_examples=50)
def test_vhdl::portmapassociation_instantiation(instance):
    assert isinstance(instance, vhdl::PortMapAssociation)

@given(instance=vhdl::PortMapAssociation_strategy)
def test_vhdl::portmapassociation_formal_type(instance):
    assert isinstance(instance.formal, str)


@given(instance=vhdl::PortMapAssociation_strategy)
def test_vhdl::portmapassociation_formal_setter(instance):
    original = instance.formal
    instance.formal = original
    assert instance.formal == original

@given(instance=SequentialStatement_strategy)
@settings(max_examples=50)
def test_sequentialstatement_instantiation(instance):
    assert isinstance(instance, SequentialStatement)

@given(instance=vhdl::SequentialSignalAssignmentStatement_strategy)
@settings(max_examples=50)
def test_vhdl::sequentialsignalassignmentstatement_instantiation(instance):
    assert isinstance(instance, vhdl::SequentialSignalAssignmentStatement)

@given(instance=vhdl::SequentialSignalAssignmentStatement_strategy)
def test_vhdl::sequentialsignalassignmentstatement_postponed_type(instance):
    assert isinstance(instance.postponed, bool)


@given(instance=vhdl::SequentialSignalAssignmentStatement_strategy)
def test_vhdl::sequentialsignalassignmentstatement_postponed_setter(instance):
    original = instance.postponed
    instance.postponed = original
    assert instance.postponed == original

@given(instance=vhdl::SequentialSignalAssignmentStatement_strategy)
def test_vhdl::sequentialsignalassignmentstatement_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=vhdl::SequentialSignalAssignmentStatement_strategy)
def test_vhdl::sequentialsignalassignmentstatement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=vhdl::SequentialSignalAssignmentStatement_strategy)
def test_vhdl::sequentialsignalassignmentstatement_guarded_type(instance):
    assert isinstance(instance.guarded, bool)


@given(instance=vhdl::SequentialSignalAssignmentStatement_strategy)
def test_vhdl::sequentialsignalassignmentstatement_guarded_setter(instance):
    original = instance.guarded
    instance.guarded = original
    assert instance.guarded == original

@given(instance=vhdl::LoopStatement_strategy)
@settings(max_examples=50)
def test_vhdl::loopstatement_instantiation(instance):
    assert isinstance(instance, vhdl::LoopStatement)

@given(instance=vhdl::IfStatement_strategy)
@settings(max_examples=50)
def test_vhdl::ifstatement_instantiation(instance):
    assert isinstance(instance, vhdl::IfStatement)

@given(instance=vhdl::IfStatement_strategy)
def test_vhdl::ifstatement_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=vhdl::IfStatement_strategy)
def test_vhdl::ifstatement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=vhdl::CaseStatement_strategy)
@settings(max_examples=50)
def test_vhdl::casestatement_instantiation(instance):
    assert isinstance(instance, vhdl::CaseStatement)

@given(instance=vhdl::CaseStatement_strategy)
def test_vhdl::casestatement_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=vhdl::CaseStatement_strategy)
def test_vhdl::casestatement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=vhdl::WaitStatement_strategy)
@settings(max_examples=50)
def test_vhdl::waitstatement_instantiation(instance):
    assert isinstance(instance, vhdl::WaitStatement)

@given(instance=vhdl::WaitStatement_strategy)
def test_vhdl::waitstatement_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=vhdl::WaitStatement_strategy)
def test_vhdl::waitstatement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=vhdl::PortMap_strategy)
@settings(max_examples=50)
def test_vhdl::portmap_instantiation(instance):
    assert isinstance(instance, vhdl::PortMap)

@given(instance=vhdl::GenericMap_strategy)
@settings(max_examples=50)
def test_vhdl::genericmap_instantiation(instance):
    assert isinstance(instance, vhdl::GenericMap)

@given(instance=vhdl::SequentialStatement_strategy)
@settings(max_examples=50)
def test_vhdl::sequentialstatement_instantiation(instance):
    assert isinstance(instance, vhdl::SequentialStatement)

@given(instance=vhdl::IdList_strategy)
@settings(max_examples=50)
def test_vhdl::idlist_instantiation(instance):
    assert isinstance(instance, vhdl::IdList)

@given(instance=ArchitectureStatement_strategy)
@settings(max_examples=50)
def test_architecturestatement_instantiation(instance):
    assert isinstance(instance, ArchitectureStatement)

@given(instance=vhdl::ComponentInstantiationStatement_strategy)
@settings(max_examples=50)
def test_vhdl::componentinstantiationstatement_instantiation(instance):
    assert isinstance(instance, vhdl::ComponentInstantiationStatement)

@given(instance=vhdl::ComponentInstantiationStatement_strategy)
def test_vhdl::componentinstantiationstatement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vhdl::ComponentInstantiationStatement_strategy)
def test_vhdl::componentinstantiationstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vhdl::IfGenerateStatement_strategy)
@settings(max_examples=50)
def test_vhdl::ifgeneratestatement_instantiation(instance):
    assert isinstance(instance, vhdl::IfGenerateStatement)

@given(instance=vhdl::EntityInstantiationStatement_strategy)
@settings(max_examples=50)
def test_vhdl::entityinstantiationstatement_instantiation(instance):
    assert isinstance(instance, vhdl::EntityInstantiationStatement)

@given(instance=vhdl::EntityInstantiationStatement_strategy)
def test_vhdl::entityinstantiationstatement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vhdl::EntityInstantiationStatement_strategy)
def test_vhdl::entityinstantiationstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vhdl::ConditionalSignalAssignmentStatement_strategy)
@settings(max_examples=50)
def test_vhdl::conditionalsignalassignmentstatement_instantiation(instance):
    assert isinstance(instance, vhdl::ConditionalSignalAssignmentStatement)

@given(instance=vhdl::ConditionalSignalAssignmentStatement_strategy)
def test_vhdl::conditionalsignalassignmentstatement_guarded_type(instance):
    assert isinstance(instance.guarded, bool)


@given(instance=vhdl::ConditionalSignalAssignmentStatement_strategy)
def test_vhdl::conditionalsignalassignmentstatement_guarded_setter(instance):
    original = instance.guarded
    instance.guarded = original
    assert instance.guarded == original

@given(instance=vhdl::ConditionalSignalAssignmentStatement_strategy)
def test_vhdl::conditionalsignalassignmentstatement_postponed_type(instance):
    assert isinstance(instance.postponed, bool)


@given(instance=vhdl::ConditionalSignalAssignmentStatement_strategy)
def test_vhdl::conditionalsignalassignmentstatement_postponed_setter(instance):
    original = instance.postponed
    instance.postponed = original
    assert instance.postponed == original

@given(instance=vhdl::ForGenerateStatement_strategy)
@settings(max_examples=50)
def test_vhdl::forgeneratestatement_instantiation(instance):
    assert isinstance(instance, vhdl::ForGenerateStatement)

@given(instance=vhdl::ProcessStatement_strategy)
@settings(max_examples=50)
def test_vhdl::processstatement_instantiation(instance):
    assert isinstance(instance, vhdl::ProcessStatement)

@given(instance=vhdl::ProcessStatement_strategy)
def test_vhdl::processstatement_postponed_type(instance):
    assert isinstance(instance.postponed, bool)


@given(instance=vhdl::ProcessStatement_strategy)
def test_vhdl::processstatement_postponed_setter(instance):
    original = instance.postponed
    instance.postponed = original
    assert instance.postponed == original

@given(instance=vhdl::SubtypeIndication_strategy)
@settings(max_examples=50)
def test_vhdl::subtypeindication_instantiation(instance):
    assert isinstance(instance, vhdl::SubtypeIndication)

@given(instance=vhdl::SubtypeIndication_strategy)
def test_vhdl::subtypeindication_builtin_type_type(instance):
    assert isinstance(instance.builtin_type, str)


@given(instance=vhdl::SubtypeIndication_strategy)
def test_vhdl::subtypeindication_builtin_type_setter(instance):
    original = instance.builtin_type
    instance.builtin_type = original
    assert instance.builtin_type == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=vhdl::LoopVariable_strategy)
@settings(max_examples=50)
def test_vhdl::loopvariable_instantiation(instance):
    assert isinstance(instance, vhdl::LoopVariable)

@given(instance=vhdl::Constant_strategy)
@settings(max_examples=50)
def test_vhdl::constant_instantiation(instance):
    assert isinstance(instance, vhdl::Constant)

@given(instance=vhdl::Port_strategy)
@settings(max_examples=50)
def test_vhdl::port_instantiation(instance):
    assert isinstance(instance, vhdl::Port)

@given(instance=vhdl::Port_strategy)
def test_vhdl::port_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=vhdl::Port_strategy)
def test_vhdl::port_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=vhdl::Port_strategy)
def test_vhdl::port_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=vhdl::Port_strategy)
def test_vhdl::port_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=vhdl::Ports_strategy)
@settings(max_examples=50)
def test_vhdl::ports_instantiation(instance):
    assert isinstance(instance, vhdl::Ports)

@given(instance=vhdl::Generics_strategy)
@settings(max_examples=50)
def test_vhdl::generics_instantiation(instance):
    assert isinstance(instance, vhdl::Generics)

@given(instance=vhdl::Var_strategy)
@settings(max_examples=50)
def test_vhdl::var_instantiation(instance):
    assert isinstance(instance, vhdl::Var)

@given(instance=vhdl::Signal_strategy)
@settings(max_examples=50)
def test_vhdl::signal_instantiation(instance):
    assert isinstance(instance, vhdl::Signal)

@given(instance=package::declarative::item_strategy)
@settings(max_examples=50)
def test_package::declarative::item_instantiation(instance):
    assert isinstance(instance, package::declarative::item)

@given(instance=BlockDeclarativeItem_strategy)
@settings(max_examples=50)
def test_blockdeclarativeitem_instantiation(instance):
    assert isinstance(instance, BlockDeclarativeItem)

@given(instance=vhdl::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::variabledeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::VariableDeclaration)

@given(instance=vhdl::VariableDeclaration_strategy)
def test_vhdl::variabledeclaration_shared_type(instance):
    assert isinstance(instance.shared, bool)


@given(instance=vhdl::VariableDeclaration_strategy)
def test_vhdl::variabledeclaration_shared_setter(instance):
    original = instance.shared
    instance.shared = original
    assert instance.shared == original

@given(instance=vhdl::AttributeSpecification_strategy)
@settings(max_examples=50)
def test_vhdl::attributespecification_instantiation(instance):
    assert isinstance(instance, vhdl::AttributeSpecification)

@given(instance=vhdl::AttributeSpecification_strategy)
def test_vhdl::attributespecification_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=vhdl::AttributeSpecification_strategy)
def test_vhdl::attributespecification_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=vhdl::AttributeSpecification_strategy)
def test_vhdl::attributespecification_entity_type(instance):
    assert isinstance(instance.entity, str)


@given(instance=vhdl::AttributeSpecification_strategy)
def test_vhdl::attributespecification_entity_setter(instance):
    original = instance.entity
    instance.entity = original
    assert instance.entity == original

@given(instance=vhdl::AttributeSpecification_strategy)
def test_vhdl::attributespecification_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vhdl::AttributeSpecification_strategy)
def test_vhdl::attributespecification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vhdl::SignalDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::signaldeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::SignalDeclaration)

@given(instance=vhdl::SignalDeclaration_strategy)
def test_vhdl::signaldeclaration_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=vhdl::SignalDeclaration_strategy)
def test_vhdl::signaldeclaration_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=vhdl::Type_strategy)
@settings(max_examples=50)
def test_vhdl::type_instantiation(instance):
    assert isinstance(instance, vhdl::Type)

@given(instance=vhdl::Type_strategy)
def test_vhdl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vhdl::Type_strategy)
def test_vhdl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vhdl::Type_strategy)
def test_vhdl::type_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vhdl::Type_strategy)
def test_vhdl::type_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vhdl::ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::constantdeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::ConstantDeclaration)

@given(instance=vhdl::Component_strategy)
@settings(max_examples=50)
def test_vhdl::component_instantiation(instance):
    assert isinstance(instance, vhdl::Component)

@given(instance=vhdl::Component_strategy)
def test_vhdl::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vhdl::Component_strategy)
def test_vhdl::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vhdl::AttributeDeclaration_strategy)
@settings(max_examples=50)
def test_vhdl::attributedeclaration_instantiation(instance):
    assert isinstance(instance, vhdl::AttributeDeclaration)

@given(instance=vhdl::AttributeDeclaration_strategy)
def test_vhdl::attributedeclaration_type_keyword_type(instance):
    assert isinstance(instance.type_keyword, str)


@given(instance=vhdl::AttributeDeclaration_strategy)
def test_vhdl::attributedeclaration_type_keyword_setter(instance):
    original = instance.type_keyword
    instance.type_keyword = original
    assert instance.type_keyword == original

@given(instance=vhdl::AttributeDeclaration_strategy)
def test_vhdl::attributedeclaration_type_id_type(instance):
    assert isinstance(instance.type_id, str)


@given(instance=vhdl::AttributeDeclaration_strategy)
def test_vhdl::attributedeclaration_type_id_setter(instance):
    original = instance.type_id
    instance.type_id = original
    assert instance.type_id == original

@given(instance=vhdl::AttributeDeclaration_strategy)
def test_vhdl::attributedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vhdl::AttributeDeclaration_strategy)
def test_vhdl::attributedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vhdl::Alias_strategy)
@settings(max_examples=50)
def test_vhdl::alias_instantiation(instance):
    assert isinstance(instance, vhdl::Alias)

@given(instance=vhdl::Generic_strategy)
@settings(max_examples=50)
def test_vhdl::generic_instantiation(instance):
    assert isinstance(instance, vhdl::Generic)

@given(instance=vhdl::Expression_strategy)
@settings(max_examples=50)
def test_vhdl::expression_instantiation(instance):
    assert isinstance(instance, vhdl::Expression)

@given(instance=vhdl::Expression_strategy)
def test_vhdl::expression_attribute_type(instance):
    assert isinstance(instance.attribute, str)


@given(instance=vhdl::Expression_strategy)
def test_vhdl::expression_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=vhdl::Expression_strategy)
def test_vhdl::expression_unary_operator_type(instance):
    assert isinstance(instance.unary_operator, str)


@given(instance=vhdl::Expression_strategy)
def test_vhdl::expression_unary_operator_setter(instance):
    original = instance.unary_operator
    instance.unary_operator = original
    assert instance.unary_operator == original

@given(instance=vhdl::DesignFile_strategy)
@settings(max_examples=50)
def test_vhdl::designfile_instantiation(instance):
    assert isinstance(instance, vhdl::DesignFile)

@given(instance=vhdl::ArchitectureStatement_strategy)
@settings(max_examples=50)
def test_vhdl::architecturestatement_instantiation(instance):
    assert isinstance(instance, vhdl::ArchitectureStatement)

@given(instance=vhdl::ArchitectureStatement_strategy)
def test_vhdl::architecturestatement_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=vhdl::ArchitectureStatement_strategy)
def test_vhdl::architecturestatement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=vhdl::BlockDeclarativeItem_strategy)
@settings(max_examples=50)
def test_vhdl::blockdeclarativeitem_instantiation(instance):
    assert isinstance(instance, vhdl::BlockDeclarativeItem)

@given(instance=vhdl::package::declarative::part_strategy)
@settings(max_examples=50)
def test_vhdl::package::declarative::part_instantiation(instance):
    assert isinstance(instance, vhdl::package::declarative::part)

@given(instance=vhdl::package::declarative::item_strategy)
@settings(max_examples=50)
def test_vhdl::package::declarative::item_instantiation(instance):
    assert isinstance(instance, vhdl::package::declarative::item)

@given(instance=LibraryUnit_strategy)
@settings(max_examples=50)
def test_libraryunit_instantiation(instance):
    assert isinstance(instance, LibraryUnit)

@given(instance=vhdl::Entity_strategy)
@settings(max_examples=50)
def test_vhdl::entity_instantiation(instance):
    assert isinstance(instance, vhdl::Entity)

@given(instance=vhdl::Architecture_strategy)
@settings(max_examples=50)
def test_vhdl::architecture_instantiation(instance):
    assert isinstance(instance, vhdl::Architecture)

@given(instance=vhdl::Package_strategy)
@settings(max_examples=50)
def test_vhdl::package_instantiation(instance):
    assert isinstance(instance, vhdl::Package)

@given(instance=vhdl::Library_strategy)
@settings(max_examples=50)
def test_vhdl::library_instantiation(instance):
    assert isinstance(instance, vhdl::Library)

@given(instance=vhdl::Library_strategy)
def test_vhdl::library_builtin_lib_type(instance):
    assert isinstance(instance.builtin_lib, str)


@given(instance=vhdl::Library_strategy)
def test_vhdl::library_builtin_lib_setter(instance):
    original = instance.builtin_lib
    instance.builtin_lib = original
    assert instance.builtin_lib == original

@given(instance=ContextItem_strategy)
@settings(max_examples=50)
def test_contextitem_instantiation(instance):
    assert isinstance(instance, ContextItem)

@given(instance=vhdl::LibraryClause_strategy)
@settings(max_examples=50)
def test_vhdl::libraryclause_instantiation(instance):
    assert isinstance(instance, vhdl::LibraryClause)

@given(instance=vhdl::LibraryClause_strategy)
def test_vhdl::libraryclause_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vhdl::LibraryClause_strategy)
def test_vhdl::libraryclause_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vhdl::UseClause_strategy)
@settings(max_examples=50)
def test_vhdl::useclause_instantiation(instance):
    assert isinstance(instance, vhdl::UseClause)

@given(instance=vhdl::UseClause_strategy)
def test_vhdl::useclause_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=vhdl::UseClause_strategy)
def test_vhdl::useclause_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=vhdl::LibraryUnit_strategy)
@settings(max_examples=50)
def test_vhdl::libraryunit_instantiation(instance):
    assert isinstance(instance, vhdl::LibraryUnit)

@given(instance=vhdl::LibraryUnit_strategy)
def test_vhdl::libraryunit_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vhdl::LibraryUnit_strategy)
def test_vhdl::libraryunit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vhdl::ContextItem_strategy)
@settings(max_examples=50)
def test_vhdl::contextitem_instantiation(instance):
    assert isinstance(instance, vhdl::ContextItem)

@given(instance=vhdl::WhileIterationScheme_strategy)
@settings(max_examples=50)
def test_vhdl::whileiterationscheme_instantiation(instance):
    assert isinstance(instance, vhdl::WhileIterationScheme)

@given(instance=vhdl::IterationScheme_strategy)
@settings(max_examples=50)
def test_vhdl::iterationscheme_instantiation(instance):
    assert isinstance(instance, vhdl::IterationScheme)

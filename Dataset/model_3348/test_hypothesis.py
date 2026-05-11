import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Method,
    swrtj::ProvidedMethod,
    swrtj::RequiredMethod,
    Field,
    swrtj::RequiredField,
    swrtj::FieldDeclaration,
    GenericExpression,
    swrtj::Expression,
    swrtj::BooleanExpression,
    Parameter,
    swrtj::LocalParameter,
    swrtj::FormalParameter,
    Message,
    swrtj::MethodInvocation,
    TraitOperation,
    swrtj::TraitFieldRename,
    swrtj::TraitAlias,
    swrtj::TraitMethodRename,
    swrtj::TraitExclude,
    RecordOperation,
    swrtj::RecordRename,
    swrtj::RecordExclude,
    swrtj::FieldAccess,
    AtomicBooleanExpression,
    swrtj::SimpleComparation,
    swrtj::AtomicBooleanExpression,
    swrtj::BooleanOperator,
    Start,
    swrtj::Input,
    swrtj::ConstructorInvocation,
    swrtj::BooleanConstant,
    swrtj::Args,
    swrtj::NestedExpression,
    swrtj::ParameterReference,
    swrtj::Cast,
    swrtj::StringConstant,
    swrtj::Output,
    swrtj::This,
    swrtj::Number,
    swrtj::ParameterAssignment,
    swrtj::Null,
    swrtj::Message,
    swrtj::Start,
    swrtj::DottedExpression,
    swrtj::NestedBooleanExpression,
    swrtj::CompareOperator,
    swrtj::FieldName,
    swrtj::Type,
    TraitElement,
    swrtj::TraitElement,
    BaseTrait,
    swrtj::TraitName,
    swrtj::NestedTraitExpression,
    swrtj::AnonimousTrait,
    swrtj::TraitOperation,
    swrtj::BaseTrait,
    Statement,
    swrtj::WhileStatement,
    swrtj::IfThenElseStatement,
    swrtj::ExpressionStatement,
    swrtj::Statement,
    swrtj::GenericExpression,
    swrtj::ReturnStatement,
    swrtj::Parameter,
    swrtj::MethodName,
    swrtj::TraitExpression,
    swrtj::RecordExpression,
    swrtj::Method,
    Element,
    swrtj::Class,
    swrtj::Trait,
    swrtj::Record,
    swrtj::Interface,
    swrtj::Element,
    swrtj::Field,
    BaseRecord,
    swrtj::RecordName,
    swrtj::NestedRecordExpression,
    swrtj::AnonimousRecord,
    swrtj::RecordOperation,
    swrtj::BaseRecord,
    swrtj::Block,
    swrtj::Program,
    swrtj::Constructor,
    swrtj::Import,
    swrtj::File,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_method_is_not_abstract():
    assert not inspect.isabstract(Method)


def test_method_constructor_exists():
    assert callable(Method.__init__)


def test_method_constructor_args():
    sig = inspect.signature(Method.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::providedmethod_is_not_abstract():
    assert not inspect.isabstract(swrtj::ProvidedMethod)


def test_swrtj::providedmethod_constructor_exists():
    assert callable(swrtj::ProvidedMethod.__init__)


def test_swrtj::providedmethod_constructor_args():
    sig = inspect.signature(swrtj::ProvidedMethod.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronized" in params, "Missing parameter 'isSynchronized'"

def test_swrtj::providedmethod_has_isSynchronized():
    assert hasattr(swrtj::ProvidedMethod, "isSynchronized")
    descriptor = None
    for klass in swrtj::ProvidedMethod.__mro__:
        if "isSynchronized" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronized"]
            break
    assert isinstance(descriptor, property)



def test_swrtj::requiredmethod_is_not_abstract():
    assert not inspect.isabstract(swrtj::RequiredMethod)


def test_swrtj::requiredmethod_constructor_exists():
    assert callable(swrtj::RequiredMethod.__init__)


def test_swrtj::requiredmethod_constructor_args():
    sig = inspect.signature(swrtj::RequiredMethod.__init__)
    params = list(sig.parameters.keys())



def test_field_is_not_abstract():
    assert not inspect.isabstract(Field)


def test_field_constructor_exists():
    assert callable(Field.__init__)


def test_field_constructor_args():
    sig = inspect.signature(Field.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::requiredfield_is_not_abstract():
    assert not inspect.isabstract(swrtj::RequiredField)


def test_swrtj::requiredfield_constructor_exists():
    assert callable(swrtj::RequiredField.__init__)


def test_swrtj::requiredfield_constructor_args():
    sig = inspect.signature(swrtj::RequiredField.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(swrtj::FieldDeclaration)


def test_swrtj::fielddeclaration_constructor_exists():
    assert callable(swrtj::FieldDeclaration.__init__)


def test_swrtj::fielddeclaration_constructor_args():
    sig = inspect.signature(swrtj::FieldDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "modifier" in params, "Missing parameter 'modifier'"

def test_swrtj::fielddeclaration_has_modifier():
    assert hasattr(swrtj::FieldDeclaration, "modifier")
    descriptor = None
    for klass in swrtj::FieldDeclaration.__mro__:
        if "modifier" in klass.__dict__:
            descriptor = klass.__dict__["modifier"]
            break
    assert isinstance(descriptor, property)



def test_genericexpression_is_not_abstract():
    assert not inspect.isabstract(GenericExpression)


def test_genericexpression_constructor_exists():
    assert callable(GenericExpression.__init__)


def test_genericexpression_constructor_args():
    sig = inspect.signature(GenericExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::expression_is_not_abstract():
    assert not inspect.isabstract(swrtj::Expression)


def test_swrtj::expression_constructor_exists():
    assert callable(swrtj::Expression.__init__)


def test_swrtj::expression_constructor_args():
    sig = inspect.signature(swrtj::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "sign" in params, "Missing parameter 'sign'"
    assert "operatorList" in params, "Missing parameter 'operatorList'"

def test_swrtj::expression_has_sign():
    assert hasattr(swrtj::Expression, "sign")
    descriptor = None
    for klass in swrtj::Expression.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)

def test_swrtj::expression_has_operatorList():
    assert hasattr(swrtj::Expression, "operatorList")
    descriptor = None
    for klass in swrtj::Expression.__mro__:
        if "operatorList" in klass.__dict__:
            descriptor = klass.__dict__["operatorList"]
            break
    assert isinstance(descriptor, property)



def test_swrtj::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj::BooleanExpression)


def test_swrtj::booleanexpression_constructor_exists():
    assert callable(swrtj::BooleanExpression.__init__)


def test_swrtj::booleanexpression_constructor_args():
    sig = inspect.signature(swrtj::BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::localparameter_is_not_abstract():
    assert not inspect.isabstract(swrtj::LocalParameter)


def test_swrtj::localparameter_constructor_exists():
    assert callable(swrtj::LocalParameter.__init__)


def test_swrtj::localparameter_constructor_args():
    sig = inspect.signature(swrtj::LocalParameter.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::formalparameter_is_not_abstract():
    assert not inspect.isabstract(swrtj::FormalParameter)


def test_swrtj::formalparameter_constructor_exists():
    assert callable(swrtj::FormalParameter.__init__)


def test_swrtj::formalparameter_constructor_args():
    sig = inspect.signature(swrtj::FormalParameter.__init__)
    params = list(sig.parameters.keys())



def test_message_is_not_abstract():
    assert not inspect.isabstract(Message)


def test_message_constructor_exists():
    assert callable(Message.__init__)


def test_message_constructor_args():
    sig = inspect.signature(Message.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::methodinvocation_is_not_abstract():
    assert not inspect.isabstract(swrtj::MethodInvocation)


def test_swrtj::methodinvocation_constructor_exists():
    assert callable(swrtj::MethodInvocation.__init__)


def test_swrtj::methodinvocation_constructor_args():
    sig = inspect.signature(swrtj::MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_traitoperation_is_not_abstract():
    assert not inspect.isabstract(TraitOperation)


def test_traitoperation_constructor_exists():
    assert callable(TraitOperation.__init__)


def test_traitoperation_constructor_args():
    sig = inspect.signature(TraitOperation.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::traitfieldrename_is_not_abstract():
    assert not inspect.isabstract(swrtj::TraitFieldRename)


def test_swrtj::traitfieldrename_constructor_exists():
    assert callable(swrtj::TraitFieldRename.__init__)


def test_swrtj::traitfieldrename_constructor_args():
    sig = inspect.signature(swrtj::TraitFieldRename.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::traitalias_is_not_abstract():
    assert not inspect.isabstract(swrtj::TraitAlias)


def test_swrtj::traitalias_constructor_exists():
    assert callable(swrtj::TraitAlias.__init__)


def test_swrtj::traitalias_constructor_args():
    sig = inspect.signature(swrtj::TraitAlias.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::traitmethodrename_is_not_abstract():
    assert not inspect.isabstract(swrtj::TraitMethodRename)


def test_swrtj::traitmethodrename_constructor_exists():
    assert callable(swrtj::TraitMethodRename.__init__)


def test_swrtj::traitmethodrename_constructor_args():
    sig = inspect.signature(swrtj::TraitMethodRename.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::traitexclude_is_not_abstract():
    assert not inspect.isabstract(swrtj::TraitExclude)


def test_swrtj::traitexclude_constructor_exists():
    assert callable(swrtj::TraitExclude.__init__)


def test_swrtj::traitexclude_constructor_args():
    sig = inspect.signature(swrtj::TraitExclude.__init__)
    params = list(sig.parameters.keys())



def test_recordoperation_is_not_abstract():
    assert not inspect.isabstract(RecordOperation)


def test_recordoperation_constructor_exists():
    assert callable(RecordOperation.__init__)


def test_recordoperation_constructor_args():
    sig = inspect.signature(RecordOperation.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::recordrename_is_not_abstract():
    assert not inspect.isabstract(swrtj::RecordRename)


def test_swrtj::recordrename_constructor_exists():
    assert callable(swrtj::RecordRename.__init__)


def test_swrtj::recordrename_constructor_args():
    sig = inspect.signature(swrtj::RecordRename.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::recordexclude_is_not_abstract():
    assert not inspect.isabstract(swrtj::RecordExclude)


def test_swrtj::recordexclude_constructor_exists():
    assert callable(swrtj::RecordExclude.__init__)


def test_swrtj::recordexclude_constructor_args():
    sig = inspect.signature(swrtj::RecordExclude.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::fieldaccess_is_not_abstract():
    assert not inspect.isabstract(swrtj::FieldAccess)


def test_swrtj::fieldaccess_constructor_exists():
    assert callable(swrtj::FieldAccess.__init__)


def test_swrtj::fieldaccess_constructor_args():
    sig = inspect.signature(swrtj::FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_atomicbooleanexpression_is_not_abstract():
    assert not inspect.isabstract(AtomicBooleanExpression)


def test_atomicbooleanexpression_constructor_exists():
    assert callable(AtomicBooleanExpression.__init__)


def test_atomicbooleanexpression_constructor_args():
    sig = inspect.signature(AtomicBooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::simplecomparation_is_not_abstract():
    assert not inspect.isabstract(swrtj::SimpleComparation)


def test_swrtj::simplecomparation_constructor_exists():
    assert callable(swrtj::SimpleComparation.__init__)


def test_swrtj::simplecomparation_constructor_args():
    sig = inspect.signature(swrtj::SimpleComparation.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::atomicbooleanexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj::AtomicBooleanExpression)


def test_swrtj::atomicbooleanexpression_constructor_exists():
    assert callable(swrtj::AtomicBooleanExpression.__init__)


def test_swrtj::atomicbooleanexpression_constructor_args():
    sig = inspect.signature(swrtj::AtomicBooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "negated" in params, "Missing parameter 'negated'"

def test_swrtj::atomicbooleanexpression_has_negated():
    assert hasattr(swrtj::AtomicBooleanExpression, "negated")
    descriptor = None
    for klass in swrtj::AtomicBooleanExpression.__mro__:
        if "negated" in klass.__dict__:
            descriptor = klass.__dict__["negated"]
            break
    assert isinstance(descriptor, property)



def test_swrtj::booleanoperator_is_not_abstract():
    assert not inspect.isabstract(swrtj::BooleanOperator)


def test_swrtj::booleanoperator_constructor_exists():
    assert callable(swrtj::BooleanOperator.__init__)


def test_swrtj::booleanoperator_constructor_args():
    sig = inspect.signature(swrtj::BooleanOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_swrtj::booleanoperator_has_operator():
    assert hasattr(swrtj::BooleanOperator, "operator")
    descriptor = None
    for klass in swrtj::BooleanOperator.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_start_is_not_abstract():
    assert not inspect.isabstract(Start)


def test_start_constructor_exists():
    assert callable(Start.__init__)


def test_start_constructor_args():
    sig = inspect.signature(Start.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::input_is_not_abstract():
    assert not inspect.isabstract(swrtj::Input)


def test_swrtj::input_constructor_exists():
    assert callable(swrtj::Input.__init__)


def test_swrtj::input_constructor_args():
    sig = inspect.signature(swrtj::Input.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_swrtj::input_has_input():
    assert hasattr(swrtj::Input, "input")
    descriptor = None
    for klass in swrtj::Input.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_swrtj::constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(swrtj::ConstructorInvocation)


def test_swrtj::constructorinvocation_constructor_exists():
    assert callable(swrtj::ConstructorInvocation.__init__)


def test_swrtj::constructorinvocation_constructor_args():
    sig = inspect.signature(swrtj::ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::booleanconstant_is_not_abstract():
    assert not inspect.isabstract(swrtj::BooleanConstant)


def test_swrtj::booleanconstant_constructor_exists():
    assert callable(swrtj::BooleanConstant.__init__)


def test_swrtj::booleanconstant_constructor_args():
    sig = inspect.signature(swrtj::BooleanConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_swrtj::booleanconstant_has_value():
    assert hasattr(swrtj::BooleanConstant, "value")
    descriptor = None
    for klass in swrtj::BooleanConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_swrtj::args_is_not_abstract():
    assert not inspect.isabstract(swrtj::Args)


def test_swrtj::args_constructor_exists():
    assert callable(swrtj::Args.__init__)


def test_swrtj::args_constructor_args():
    sig = inspect.signature(swrtj::Args.__init__)
    params = list(sig.parameters.keys())
    assert "args" in params, "Missing parameter 'args'"

def test_swrtj::args_has_args():
    assert hasattr(swrtj::Args, "args")
    descriptor = None
    for klass in swrtj::Args.__mro__:
        if "args" in klass.__dict__:
            descriptor = klass.__dict__["args"]
            break
    assert isinstance(descriptor, property)



def test_swrtj::nestedexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj::NestedExpression)


def test_swrtj::nestedexpression_constructor_exists():
    assert callable(swrtj::NestedExpression.__init__)


def test_swrtj::nestedexpression_constructor_args():
    sig = inspect.signature(swrtj::NestedExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::parameterreference_is_not_abstract():
    assert not inspect.isabstract(swrtj::ParameterReference)


def test_swrtj::parameterreference_constructor_exists():
    assert callable(swrtj::ParameterReference.__init__)


def test_swrtj::parameterreference_constructor_args():
    sig = inspect.signature(swrtj::ParameterReference.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::cast_is_not_abstract():
    assert not inspect.isabstract(swrtj::Cast)


def test_swrtj::cast_constructor_exists():
    assert callable(swrtj::Cast.__init__)


def test_swrtj::cast_constructor_args():
    sig = inspect.signature(swrtj::Cast.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::stringconstant_is_not_abstract():
    assert not inspect.isabstract(swrtj::StringConstant)


def test_swrtj::stringconstant_constructor_exists():
    assert callable(swrtj::StringConstant.__init__)


def test_swrtj::stringconstant_constructor_args():
    sig = inspect.signature(swrtj::StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_swrtj::stringconstant_has_value():
    assert hasattr(swrtj::StringConstant, "value")
    descriptor = None
    for klass in swrtj::StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_swrtj::output_is_not_abstract():
    assert not inspect.isabstract(swrtj::Output)


def test_swrtj::output_constructor_exists():
    assert callable(swrtj::Output.__init__)


def test_swrtj::output_constructor_args():
    sig = inspect.signature(swrtj::Output.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"

def test_swrtj::output_has_output():
    assert hasattr(swrtj::Output, "output")
    descriptor = None
    for klass in swrtj::Output.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_swrtj::this_is_not_abstract():
    assert not inspect.isabstract(swrtj::This)


def test_swrtj::this_constructor_exists():
    assert callable(swrtj::This.__init__)


def test_swrtj::this_constructor_args():
    sig = inspect.signature(swrtj::This.__init__)
    params = list(sig.parameters.keys())
    assert "this" in params, "Missing parameter 'this'"

def test_swrtj::this_has_this():
    assert hasattr(swrtj::This, "this")
    descriptor = None
    for klass in swrtj::This.__mro__:
        if "this" in klass.__dict__:
            descriptor = klass.__dict__["this"]
            break
    assert isinstance(descriptor, property)



def test_swrtj::number_is_not_abstract():
    assert not inspect.isabstract(swrtj::Number)


def test_swrtj::number_constructor_exists():
    assert callable(swrtj::Number.__init__)


def test_swrtj::number_constructor_args():
    sig = inspect.signature(swrtj::Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_swrtj::number_has_value():
    assert hasattr(swrtj::Number, "value")
    descriptor = None
    for klass in swrtj::Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_swrtj::parameterassignment_is_not_abstract():
    assert not inspect.isabstract(swrtj::ParameterAssignment)


def test_swrtj::parameterassignment_constructor_exists():
    assert callable(swrtj::ParameterAssignment.__init__)


def test_swrtj::parameterassignment_constructor_args():
    sig = inspect.signature(swrtj::ParameterAssignment.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::null_is_not_abstract():
    assert not inspect.isabstract(swrtj::Null)


def test_swrtj::null_constructor_exists():
    assert callable(swrtj::Null.__init__)


def test_swrtj::null_constructor_args():
    sig = inspect.signature(swrtj::Null.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"

def test_swrtj::null_has_null():
    assert hasattr(swrtj::Null, "null")
    descriptor = None
    for klass in swrtj::Null.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)



def test_swrtj::message_is_not_abstract():
    assert not inspect.isabstract(swrtj::Message)


def test_swrtj::message_constructor_exists():
    assert callable(swrtj::Message.__init__)


def test_swrtj::message_constructor_args():
    sig = inspect.signature(swrtj::Message.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::start_is_not_abstract():
    assert not inspect.isabstract(swrtj::Start)


def test_swrtj::start_constructor_exists():
    assert callable(swrtj::Start.__init__)


def test_swrtj::start_constructor_args():
    sig = inspect.signature(swrtj::Start.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::dottedexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj::DottedExpression)


def test_swrtj::dottedexpression_constructor_exists():
    assert callable(swrtj::DottedExpression.__init__)


def test_swrtj::dottedexpression_constructor_args():
    sig = inspect.signature(swrtj::DottedExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::nestedbooleanexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj::NestedBooleanExpression)


def test_swrtj::nestedbooleanexpression_constructor_exists():
    assert callable(swrtj::NestedBooleanExpression.__init__)


def test_swrtj::nestedbooleanexpression_constructor_args():
    sig = inspect.signature(swrtj::NestedBooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::compareoperator_is_not_abstract():
    assert not inspect.isabstract(swrtj::CompareOperator)


def test_swrtj::compareoperator_constructor_exists():
    assert callable(swrtj::CompareOperator.__init__)


def test_swrtj::compareoperator_constructor_args():
    sig = inspect.signature(swrtj::CompareOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_swrtj::compareoperator_has_operator():
    assert hasattr(swrtj::CompareOperator, "operator")
    descriptor = None
    for klass in swrtj::CompareOperator.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_swrtj::fieldname_is_not_abstract():
    assert not inspect.isabstract(swrtj::FieldName)


def test_swrtj::fieldname_constructor_exists():
    assert callable(swrtj::FieldName.__init__)


def test_swrtj::fieldname_constructor_args():
    sig = inspect.signature(swrtj::FieldName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swrtj::fieldname_has_name():
    assert hasattr(swrtj::FieldName, "name")
    descriptor = None
    for klass in swrtj::FieldName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swrtj::type_is_not_abstract():
    assert not inspect.isabstract(swrtj::Type)


def test_swrtj::type_constructor_exists():
    assert callable(swrtj::Type.__init__)


def test_swrtj::type_constructor_args():
    sig = inspect.signature(swrtj::Type.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"

def test_swrtj::type_has_primitiveType():
    assert hasattr(swrtj::Type, "primitiveType")
    descriptor = None
    for klass in swrtj::Type.__mro__:
        if "primitiveType" in klass.__dict__:
            descriptor = klass.__dict__["primitiveType"]
            break
    assert isinstance(descriptor, property)



def test_traitelement_is_not_abstract():
    assert not inspect.isabstract(TraitElement)


def test_traitelement_constructor_exists():
    assert callable(TraitElement.__init__)


def test_traitelement_constructor_args():
    sig = inspect.signature(TraitElement.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::traitelement_is_not_abstract():
    assert not inspect.isabstract(swrtj::TraitElement)


def test_swrtj::traitelement_constructor_exists():
    assert callable(swrtj::TraitElement.__init__)


def test_swrtj::traitelement_constructor_args():
    sig = inspect.signature(swrtj::TraitElement.__init__)
    params = list(sig.parameters.keys())



def test_basetrait_is_not_abstract():
    assert not inspect.isabstract(BaseTrait)


def test_basetrait_constructor_exists():
    assert callable(BaseTrait.__init__)


def test_basetrait_constructor_args():
    sig = inspect.signature(BaseTrait.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::traitname_is_not_abstract():
    assert not inspect.isabstract(swrtj::TraitName)


def test_swrtj::traitname_constructor_exists():
    assert callable(swrtj::TraitName.__init__)


def test_swrtj::traitname_constructor_args():
    sig = inspect.signature(swrtj::TraitName.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::nestedtraitexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj::NestedTraitExpression)


def test_swrtj::nestedtraitexpression_constructor_exists():
    assert callable(swrtj::NestedTraitExpression.__init__)


def test_swrtj::nestedtraitexpression_constructor_args():
    sig = inspect.signature(swrtj::NestedTraitExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::anonimoustrait_is_not_abstract():
    assert not inspect.isabstract(swrtj::AnonimousTrait)


def test_swrtj::anonimoustrait_constructor_exists():
    assert callable(swrtj::AnonimousTrait.__init__)


def test_swrtj::anonimoustrait_constructor_args():
    sig = inspect.signature(swrtj::AnonimousTrait.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::traitoperation_is_not_abstract():
    assert not inspect.isabstract(swrtj::TraitOperation)


def test_swrtj::traitoperation_constructor_exists():
    assert callable(swrtj::TraitOperation.__init__)


def test_swrtj::traitoperation_constructor_args():
    sig = inspect.signature(swrtj::TraitOperation.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::basetrait_is_not_abstract():
    assert not inspect.isabstract(swrtj::BaseTrait)


def test_swrtj::basetrait_constructor_exists():
    assert callable(swrtj::BaseTrait.__init__)


def test_swrtj::basetrait_constructor_args():
    sig = inspect.signature(swrtj::BaseTrait.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::whilestatement_is_not_abstract():
    assert not inspect.isabstract(swrtj::WhileStatement)


def test_swrtj::whilestatement_constructor_exists():
    assert callable(swrtj::WhileStatement.__init__)


def test_swrtj::whilestatement_constructor_args():
    sig = inspect.signature(swrtj::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::ifthenelsestatement_is_not_abstract():
    assert not inspect.isabstract(swrtj::IfThenElseStatement)


def test_swrtj::ifthenelsestatement_constructor_exists():
    assert callable(swrtj::IfThenElseStatement.__init__)


def test_swrtj::ifthenelsestatement_constructor_args():
    sig = inspect.signature(swrtj::IfThenElseStatement.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(swrtj::ExpressionStatement)


def test_swrtj::expressionstatement_constructor_exists():
    assert callable(swrtj::ExpressionStatement.__init__)


def test_swrtj::expressionstatement_constructor_args():
    sig = inspect.signature(swrtj::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::statement_is_not_abstract():
    assert not inspect.isabstract(swrtj::Statement)


def test_swrtj::statement_constructor_exists():
    assert callable(swrtj::Statement.__init__)


def test_swrtj::statement_constructor_args():
    sig = inspect.signature(swrtj::Statement.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::genericexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj::GenericExpression)


def test_swrtj::genericexpression_constructor_exists():
    assert callable(swrtj::GenericExpression.__init__)


def test_swrtj::genericexpression_constructor_args():
    sig = inspect.signature(swrtj::GenericExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::returnstatement_is_not_abstract():
    assert not inspect.isabstract(swrtj::ReturnStatement)


def test_swrtj::returnstatement_constructor_exists():
    assert callable(swrtj::ReturnStatement.__init__)


def test_swrtj::returnstatement_constructor_args():
    sig = inspect.signature(swrtj::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::parameter_is_not_abstract():
    assert not inspect.isabstract(swrtj::Parameter)


def test_swrtj::parameter_constructor_exists():
    assert callable(swrtj::Parameter.__init__)


def test_swrtj::parameter_constructor_args():
    sig = inspect.signature(swrtj::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swrtj::parameter_has_name():
    assert hasattr(swrtj::Parameter, "name")
    descriptor = None
    for klass in swrtj::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swrtj::methodname_is_not_abstract():
    assert not inspect.isabstract(swrtj::MethodName)


def test_swrtj::methodname_constructor_exists():
    assert callable(swrtj::MethodName.__init__)


def test_swrtj::methodname_constructor_args():
    sig = inspect.signature(swrtj::MethodName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swrtj::methodname_has_name():
    assert hasattr(swrtj::MethodName, "name")
    descriptor = None
    for klass in swrtj::MethodName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swrtj::traitexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj::TraitExpression)


def test_swrtj::traitexpression_constructor_exists():
    assert callable(swrtj::TraitExpression.__init__)


def test_swrtj::traitexpression_constructor_args():
    sig = inspect.signature(swrtj::TraitExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::recordexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj::RecordExpression)


def test_swrtj::recordexpression_constructor_exists():
    assert callable(swrtj::RecordExpression.__init__)


def test_swrtj::recordexpression_constructor_args():
    sig = inspect.signature(swrtj::RecordExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::method_is_not_abstract():
    assert not inspect.isabstract(swrtj::Method)


def test_swrtj::method_constructor_exists():
    assert callable(swrtj::Method.__init__)


def test_swrtj::method_constructor_args():
    sig = inspect.signature(swrtj::Method.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::class_is_not_abstract():
    assert not inspect.isabstract(swrtj::Class)


def test_swrtj::class_constructor_exists():
    assert callable(swrtj::Class.__init__)


def test_swrtj::class_constructor_args():
    sig = inspect.signature(swrtj::Class.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::trait_is_not_abstract():
    assert not inspect.isabstract(swrtj::Trait)


def test_swrtj::trait_constructor_exists():
    assert callable(swrtj::Trait.__init__)


def test_swrtj::trait_constructor_args():
    sig = inspect.signature(swrtj::Trait.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::record_is_not_abstract():
    assert not inspect.isabstract(swrtj::Record)


def test_swrtj::record_constructor_exists():
    assert callable(swrtj::Record.__init__)


def test_swrtj::record_constructor_args():
    sig = inspect.signature(swrtj::Record.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::interface_is_not_abstract():
    assert not inspect.isabstract(swrtj::Interface)


def test_swrtj::interface_constructor_exists():
    assert callable(swrtj::Interface.__init__)


def test_swrtj::interface_constructor_args():
    sig = inspect.signature(swrtj::Interface.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::element_is_not_abstract():
    assert not inspect.isabstract(swrtj::Element)


def test_swrtj::element_constructor_exists():
    assert callable(swrtj::Element.__init__)


def test_swrtj::element_constructor_args():
    sig = inspect.signature(swrtj::Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "construct" in params, "Missing parameter 'construct'"

def test_swrtj::element_has_name():
    assert hasattr(swrtj::Element, "name")
    descriptor = None
    for klass in swrtj::Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_swrtj::element_has_construct():
    assert hasattr(swrtj::Element, "construct")
    descriptor = None
    for klass in swrtj::Element.__mro__:
        if "construct" in klass.__dict__:
            descriptor = klass.__dict__["construct"]
            break
    assert isinstance(descriptor, property)



def test_swrtj::field_is_not_abstract():
    assert not inspect.isabstract(swrtj::Field)


def test_swrtj::field_constructor_exists():
    assert callable(swrtj::Field.__init__)


def test_swrtj::field_constructor_args():
    sig = inspect.signature(swrtj::Field.__init__)
    params = list(sig.parameters.keys())



def test_baserecord_is_not_abstract():
    assert not inspect.isabstract(BaseRecord)


def test_baserecord_constructor_exists():
    assert callable(BaseRecord.__init__)


def test_baserecord_constructor_args():
    sig = inspect.signature(BaseRecord.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::recordname_is_not_abstract():
    assert not inspect.isabstract(swrtj::RecordName)


def test_swrtj::recordname_constructor_exists():
    assert callable(swrtj::RecordName.__init__)


def test_swrtj::recordname_constructor_args():
    sig = inspect.signature(swrtj::RecordName.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::nestedrecordexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj::NestedRecordExpression)


def test_swrtj::nestedrecordexpression_constructor_exists():
    assert callable(swrtj::NestedRecordExpression.__init__)


def test_swrtj::nestedrecordexpression_constructor_args():
    sig = inspect.signature(swrtj::NestedRecordExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::anonimousrecord_is_not_abstract():
    assert not inspect.isabstract(swrtj::AnonimousRecord)


def test_swrtj::anonimousrecord_constructor_exists():
    assert callable(swrtj::AnonimousRecord.__init__)


def test_swrtj::anonimousrecord_constructor_args():
    sig = inspect.signature(swrtj::AnonimousRecord.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::recordoperation_is_not_abstract():
    assert not inspect.isabstract(swrtj::RecordOperation)


def test_swrtj::recordoperation_constructor_exists():
    assert callable(swrtj::RecordOperation.__init__)


def test_swrtj::recordoperation_constructor_args():
    sig = inspect.signature(swrtj::RecordOperation.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::baserecord_is_not_abstract():
    assert not inspect.isabstract(swrtj::BaseRecord)


def test_swrtj::baserecord_constructor_exists():
    assert callable(swrtj::BaseRecord.__init__)


def test_swrtj::baserecord_constructor_args():
    sig = inspect.signature(swrtj::BaseRecord.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::block_is_not_abstract():
    assert not inspect.isabstract(swrtj::Block)


def test_swrtj::block_constructor_exists():
    assert callable(swrtj::Block.__init__)


def test_swrtj::block_constructor_args():
    sig = inspect.signature(swrtj::Block.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::program_is_not_abstract():
    assert not inspect.isabstract(swrtj::Program)


def test_swrtj::program_constructor_exists():
    assert callable(swrtj::Program.__init__)


def test_swrtj::program_constructor_args():
    sig = inspect.signature(swrtj::Program.__init__)
    params = list(sig.parameters.keys())



def test_swrtj::constructor_is_not_abstract():
    assert not inspect.isabstract(swrtj::Constructor)


def test_swrtj::constructor_constructor_exists():
    assert callable(swrtj::Constructor.__init__)


def test_swrtj::constructor_constructor_args():
    sig = inspect.signature(swrtj::Constructor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swrtj::constructor_has_name():
    assert hasattr(swrtj::Constructor, "name")
    descriptor = None
    for klass in swrtj::Constructor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swrtj::import_is_not_abstract():
    assert not inspect.isabstract(swrtj::Import)


def test_swrtj::import_constructor_exists():
    assert callable(swrtj::Import.__init__)


def test_swrtj::import_constructor_args():
    sig = inspect.signature(swrtj::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_swrtj::import_has_importURI():
    assert hasattr(swrtj::Import, "importURI")
    descriptor = None
    for klass in swrtj::Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_swrtj::file_is_not_abstract():
    assert not inspect.isabstract(swrtj::File)


def test_swrtj::file_constructor_exists():
    assert callable(swrtj::File.__init__)


def test_swrtj::file_constructor_args():
    sig = inspect.signature(swrtj::File.__init__)
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
Method_strategy = st.builds(
    Method,
)
swrtj::ProvidedMethod_strategy = st.builds(
    swrtj::ProvidedMethod,
    isSynchronized=
        st.booleans()
)
swrtj::RequiredMethod_strategy = st.builds(
    swrtj::RequiredMethod,
)
Field_strategy = st.builds(
    Field,
)
swrtj::RequiredField_strategy = st.builds(
    swrtj::RequiredField,
)
swrtj::FieldDeclaration_strategy = st.builds(
    swrtj::FieldDeclaration,
    modifier=
        safe_text
)
GenericExpression_strategy = st.builds(
    GenericExpression,
)
swrtj::Expression_strategy = st.builds(
    swrtj::Expression,
    sign=
        safe_text,
    operatorList=
        safe_text
)
swrtj::BooleanExpression_strategy = st.builds(
    swrtj::BooleanExpression,
)
Parameter_strategy = st.builds(
    Parameter,
)
swrtj::LocalParameter_strategy = st.builds(
    swrtj::LocalParameter,
)
swrtj::FormalParameter_strategy = st.builds(
    swrtj::FormalParameter,
)
Message_strategy = st.builds(
    Message,
)
swrtj::MethodInvocation_strategy = st.builds(
    swrtj::MethodInvocation,
)
TraitOperation_strategy = st.builds(
    TraitOperation,
)
swrtj::TraitFieldRename_strategy = st.builds(
    swrtj::TraitFieldRename,
)
swrtj::TraitAlias_strategy = st.builds(
    swrtj::TraitAlias,
)
swrtj::TraitMethodRename_strategy = st.builds(
    swrtj::TraitMethodRename,
)
swrtj::TraitExclude_strategy = st.builds(
    swrtj::TraitExclude,
)
RecordOperation_strategy = st.builds(
    RecordOperation,
)
swrtj::RecordRename_strategy = st.builds(
    swrtj::RecordRename,
)
swrtj::RecordExclude_strategy = st.builds(
    swrtj::RecordExclude,
)
swrtj::FieldAccess_strategy = st.builds(
    swrtj::FieldAccess,
)
AtomicBooleanExpression_strategy = st.builds(
    AtomicBooleanExpression,
)
swrtj::SimpleComparation_strategy = st.builds(
    swrtj::SimpleComparation,
)
swrtj::AtomicBooleanExpression_strategy = st.builds(
    swrtj::AtomicBooleanExpression,
    negated=
        st.booleans()
)
swrtj::BooleanOperator_strategy = st.builds(
    swrtj::BooleanOperator,
    operator=
        safe_text
)
Start_strategy = st.builds(
    Start,
)
swrtj::Input_strategy = st.builds(
    swrtj::Input,
    input=
        st.booleans()
)
swrtj::ConstructorInvocation_strategy = st.builds(
    swrtj::ConstructorInvocation,
)
swrtj::BooleanConstant_strategy = st.builds(
    swrtj::BooleanConstant,
    value=
        safe_text
)
swrtj::Args_strategy = st.builds(
    swrtj::Args,
    args=
        st.booleans()
)
swrtj::NestedExpression_strategy = st.builds(
    swrtj::NestedExpression,
)
swrtj::ParameterReference_strategy = st.builds(
    swrtj::ParameterReference,
)
swrtj::Cast_strategy = st.builds(
    swrtj::Cast,
)
swrtj::StringConstant_strategy = st.builds(
    swrtj::StringConstant,
    value=
        safe_text
)
swrtj::Output_strategy = st.builds(
    swrtj::Output,
    output=
        st.booleans()
)
swrtj::This_strategy = st.builds(
    swrtj::This,
    this=
        st.booleans()
)
swrtj::Number_strategy = st.builds(
    swrtj::Number,
    value=
        st.integers()
)
swrtj::ParameterAssignment_strategy = st.builds(
    swrtj::ParameterAssignment,
)
swrtj::Null_strategy = st.builds(
    swrtj::Null,
    null=
        st.booleans()
)
swrtj::Message_strategy = st.builds(
    swrtj::Message,
)
swrtj::Start_strategy = st.builds(
    swrtj::Start,
)
swrtj::DottedExpression_strategy = st.builds(
    swrtj::DottedExpression,
)
swrtj::NestedBooleanExpression_strategy = st.builds(
    swrtj::NestedBooleanExpression,
)
swrtj::CompareOperator_strategy = st.builds(
    swrtj::CompareOperator,
    operator=
        safe_text
)
swrtj::FieldName_strategy = st.builds(
    swrtj::FieldName,
    name=
        safe_text
)
swrtj::Type_strategy = st.builds(
    swrtj::Type,
    primitiveType=
        safe_text
)
TraitElement_strategy = st.builds(
    TraitElement,
)
swrtj::TraitElement_strategy = st.builds(
    swrtj::TraitElement,
)
BaseTrait_strategy = st.builds(
    BaseTrait,
)
swrtj::TraitName_strategy = st.builds(
    swrtj::TraitName,
)
swrtj::NestedTraitExpression_strategy = st.builds(
    swrtj::NestedTraitExpression,
)
swrtj::AnonimousTrait_strategy = st.builds(
    swrtj::AnonimousTrait,
)
swrtj::TraitOperation_strategy = st.builds(
    swrtj::TraitOperation,
)
swrtj::BaseTrait_strategy = st.builds(
    swrtj::BaseTrait,
)
Statement_strategy = st.builds(
    Statement,
)
swrtj::WhileStatement_strategy = st.builds(
    swrtj::WhileStatement,
)
swrtj::IfThenElseStatement_strategy = st.builds(
    swrtj::IfThenElseStatement,
)
swrtj::ExpressionStatement_strategy = st.builds(
    swrtj::ExpressionStatement,
)
swrtj::Statement_strategy = st.builds(
    swrtj::Statement,
)
swrtj::GenericExpression_strategy = st.builds(
    swrtj::GenericExpression,
)
swrtj::ReturnStatement_strategy = st.builds(
    swrtj::ReturnStatement,
)
swrtj::Parameter_strategy = st.builds(
    swrtj::Parameter,
    name=
        safe_text
)
swrtj::MethodName_strategy = st.builds(
    swrtj::MethodName,
    name=
        safe_text
)
swrtj::TraitExpression_strategy = st.builds(
    swrtj::TraitExpression,
)
swrtj::RecordExpression_strategy = st.builds(
    swrtj::RecordExpression,
)
swrtj::Method_strategy = st.builds(
    swrtj::Method,
)
Element_strategy = st.builds(
    Element,
)
swrtj::Class_strategy = st.builds(
    swrtj::Class,
)
swrtj::Trait_strategy = st.builds(
    swrtj::Trait,
)
swrtj::Record_strategy = st.builds(
    swrtj::Record,
)
swrtj::Interface_strategy = st.builds(
    swrtj::Interface,
)
swrtj::Element_strategy = st.builds(
    swrtj::Element,
    name=
        safe_text,
    construct=
        safe_text
)
swrtj::Field_strategy = st.builds(
    swrtj::Field,
)
BaseRecord_strategy = st.builds(
    BaseRecord,
)
swrtj::RecordName_strategy = st.builds(
    swrtj::RecordName,
)
swrtj::NestedRecordExpression_strategy = st.builds(
    swrtj::NestedRecordExpression,
)
swrtj::AnonimousRecord_strategy = st.builds(
    swrtj::AnonimousRecord,
)
swrtj::RecordOperation_strategy = st.builds(
    swrtj::RecordOperation,
)
swrtj::BaseRecord_strategy = st.builds(
    swrtj::BaseRecord,
)
swrtj::Block_strategy = st.builds(
    swrtj::Block,
)
swrtj::Program_strategy = st.builds(
    swrtj::Program,
)
swrtj::Constructor_strategy = st.builds(
    swrtj::Constructor,
    name=
        safe_text
)
swrtj::Import_strategy = st.builds(
    swrtj::Import,
    importURI=
        safe_text
)
swrtj::File_strategy = st.builds(
    swrtj::File,
)

@given(instance=Method_strategy)
@settings(max_examples=50)
def test_method_instantiation(instance):
    assert isinstance(instance, Method)

@given(instance=swrtj::ProvidedMethod_strategy)
@settings(max_examples=50)
def test_swrtj::providedmethod_instantiation(instance):
    assert isinstance(instance, swrtj::ProvidedMethod)

@given(instance=swrtj::ProvidedMethod_strategy)
def test_swrtj::providedmethod_isSynchronized_type(instance):
    assert isinstance(instance.isSynchronized, bool)


@given(instance=swrtj::ProvidedMethod_strategy)
def test_swrtj::providedmethod_isSynchronized_setter(instance):
    original = instance.isSynchronized
    instance.isSynchronized = original
    assert instance.isSynchronized == original

@given(instance=swrtj::RequiredMethod_strategy)
@settings(max_examples=50)
def test_swrtj::requiredmethod_instantiation(instance):
    assert isinstance(instance, swrtj::RequiredMethod)

@given(instance=Field_strategy)
@settings(max_examples=50)
def test_field_instantiation(instance):
    assert isinstance(instance, Field)

@given(instance=swrtj::RequiredField_strategy)
@settings(max_examples=50)
def test_swrtj::requiredfield_instantiation(instance):
    assert isinstance(instance, swrtj::RequiredField)

@given(instance=swrtj::FieldDeclaration_strategy)
@settings(max_examples=50)
def test_swrtj::fielddeclaration_instantiation(instance):
    assert isinstance(instance, swrtj::FieldDeclaration)

@given(instance=swrtj::FieldDeclaration_strategy)
def test_swrtj::fielddeclaration_modifier_type(instance):
    assert isinstance(instance.modifier, str)


@given(instance=swrtj::FieldDeclaration_strategy)
def test_swrtj::fielddeclaration_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=GenericExpression_strategy)
@settings(max_examples=50)
def test_genericexpression_instantiation(instance):
    assert isinstance(instance, GenericExpression)

@given(instance=swrtj::Expression_strategy)
@settings(max_examples=50)
def test_swrtj::expression_instantiation(instance):
    assert isinstance(instance, swrtj::Expression)

@given(instance=swrtj::Expression_strategy)
def test_swrtj::expression_sign_type(instance):
    assert isinstance(instance.sign, str)


@given(instance=swrtj::Expression_strategy)
def test_swrtj::expression_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original

@given(instance=swrtj::Expression_strategy)
def test_swrtj::expression_operatorList_type(instance):
    assert isinstance(instance.operatorList, str)


@given(instance=swrtj::Expression_strategy)
def test_swrtj::expression_operatorList_setter(instance):
    original = instance.operatorList
    instance.operatorList = original
    assert instance.operatorList == original

@given(instance=swrtj::BooleanExpression_strategy)
@settings(max_examples=50)
def test_swrtj::booleanexpression_instantiation(instance):
    assert isinstance(instance, swrtj::BooleanExpression)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=swrtj::LocalParameter_strategy)
@settings(max_examples=50)
def test_swrtj::localparameter_instantiation(instance):
    assert isinstance(instance, swrtj::LocalParameter)

@given(instance=swrtj::FormalParameter_strategy)
@settings(max_examples=50)
def test_swrtj::formalparameter_instantiation(instance):
    assert isinstance(instance, swrtj::FormalParameter)

@given(instance=Message_strategy)
@settings(max_examples=50)
def test_message_instantiation(instance):
    assert isinstance(instance, Message)

@given(instance=swrtj::MethodInvocation_strategy)
@settings(max_examples=50)
def test_swrtj::methodinvocation_instantiation(instance):
    assert isinstance(instance, swrtj::MethodInvocation)

@given(instance=TraitOperation_strategy)
@settings(max_examples=50)
def test_traitoperation_instantiation(instance):
    assert isinstance(instance, TraitOperation)

@given(instance=swrtj::TraitFieldRename_strategy)
@settings(max_examples=50)
def test_swrtj::traitfieldrename_instantiation(instance):
    assert isinstance(instance, swrtj::TraitFieldRename)

@given(instance=swrtj::TraitAlias_strategy)
@settings(max_examples=50)
def test_swrtj::traitalias_instantiation(instance):
    assert isinstance(instance, swrtj::TraitAlias)

@given(instance=swrtj::TraitMethodRename_strategy)
@settings(max_examples=50)
def test_swrtj::traitmethodrename_instantiation(instance):
    assert isinstance(instance, swrtj::TraitMethodRename)

@given(instance=swrtj::TraitExclude_strategy)
@settings(max_examples=50)
def test_swrtj::traitexclude_instantiation(instance):
    assert isinstance(instance, swrtj::TraitExclude)

@given(instance=RecordOperation_strategy)
@settings(max_examples=50)
def test_recordoperation_instantiation(instance):
    assert isinstance(instance, RecordOperation)

@given(instance=swrtj::RecordRename_strategy)
@settings(max_examples=50)
def test_swrtj::recordrename_instantiation(instance):
    assert isinstance(instance, swrtj::RecordRename)

@given(instance=swrtj::RecordExclude_strategy)
@settings(max_examples=50)
def test_swrtj::recordexclude_instantiation(instance):
    assert isinstance(instance, swrtj::RecordExclude)

@given(instance=swrtj::FieldAccess_strategy)
@settings(max_examples=50)
def test_swrtj::fieldaccess_instantiation(instance):
    assert isinstance(instance, swrtj::FieldAccess)

@given(instance=AtomicBooleanExpression_strategy)
@settings(max_examples=50)
def test_atomicbooleanexpression_instantiation(instance):
    assert isinstance(instance, AtomicBooleanExpression)

@given(instance=swrtj::SimpleComparation_strategy)
@settings(max_examples=50)
def test_swrtj::simplecomparation_instantiation(instance):
    assert isinstance(instance, swrtj::SimpleComparation)

@given(instance=swrtj::AtomicBooleanExpression_strategy)
@settings(max_examples=50)
def test_swrtj::atomicbooleanexpression_instantiation(instance):
    assert isinstance(instance, swrtj::AtomicBooleanExpression)

@given(instance=swrtj::AtomicBooleanExpression_strategy)
def test_swrtj::atomicbooleanexpression_negated_type(instance):
    assert isinstance(instance.negated, bool)


@given(instance=swrtj::AtomicBooleanExpression_strategy)
def test_swrtj::atomicbooleanexpression_negated_setter(instance):
    original = instance.negated
    instance.negated = original
    assert instance.negated == original

@given(instance=swrtj::BooleanOperator_strategy)
@settings(max_examples=50)
def test_swrtj::booleanoperator_instantiation(instance):
    assert isinstance(instance, swrtj::BooleanOperator)

@given(instance=swrtj::BooleanOperator_strategy)
def test_swrtj::booleanoperator_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=swrtj::BooleanOperator_strategy)
def test_swrtj::booleanoperator_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Start_strategy)
@settings(max_examples=50)
def test_start_instantiation(instance):
    assert isinstance(instance, Start)

@given(instance=swrtj::Input_strategy)
@settings(max_examples=50)
def test_swrtj::input_instantiation(instance):
    assert isinstance(instance, swrtj::Input)

@given(instance=swrtj::Input_strategy)
def test_swrtj::input_input_type(instance):
    assert isinstance(instance.input, bool)


@given(instance=swrtj::Input_strategy)
def test_swrtj::input_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=swrtj::ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_swrtj::constructorinvocation_instantiation(instance):
    assert isinstance(instance, swrtj::ConstructorInvocation)

@given(instance=swrtj::BooleanConstant_strategy)
@settings(max_examples=50)
def test_swrtj::booleanconstant_instantiation(instance):
    assert isinstance(instance, swrtj::BooleanConstant)

@given(instance=swrtj::BooleanConstant_strategy)
def test_swrtj::booleanconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=swrtj::BooleanConstant_strategy)
def test_swrtj::booleanconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=swrtj::Args_strategy)
@settings(max_examples=50)
def test_swrtj::args_instantiation(instance):
    assert isinstance(instance, swrtj::Args)

@given(instance=swrtj::Args_strategy)
def test_swrtj::args_args_type(instance):
    assert isinstance(instance.args, bool)


@given(instance=swrtj::Args_strategy)
def test_swrtj::args_args_setter(instance):
    original = instance.args
    instance.args = original
    assert instance.args == original

@given(instance=swrtj::NestedExpression_strategy)
@settings(max_examples=50)
def test_swrtj::nestedexpression_instantiation(instance):
    assert isinstance(instance, swrtj::NestedExpression)

@given(instance=swrtj::ParameterReference_strategy)
@settings(max_examples=50)
def test_swrtj::parameterreference_instantiation(instance):
    assert isinstance(instance, swrtj::ParameterReference)

@given(instance=swrtj::Cast_strategy)
@settings(max_examples=50)
def test_swrtj::cast_instantiation(instance):
    assert isinstance(instance, swrtj::Cast)

@given(instance=swrtj::StringConstant_strategy)
@settings(max_examples=50)
def test_swrtj::stringconstant_instantiation(instance):
    assert isinstance(instance, swrtj::StringConstant)

@given(instance=swrtj::StringConstant_strategy)
def test_swrtj::stringconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=swrtj::StringConstant_strategy)
def test_swrtj::stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=swrtj::Output_strategy)
@settings(max_examples=50)
def test_swrtj::output_instantiation(instance):
    assert isinstance(instance, swrtj::Output)

@given(instance=swrtj::Output_strategy)
def test_swrtj::output_output_type(instance):
    assert isinstance(instance.output, bool)


@given(instance=swrtj::Output_strategy)
def test_swrtj::output_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=swrtj::This_strategy)
@settings(max_examples=50)
def test_swrtj::this_instantiation(instance):
    assert isinstance(instance, swrtj::This)

@given(instance=swrtj::This_strategy)
def test_swrtj::this_this_type(instance):
    assert isinstance(instance.this, bool)


@given(instance=swrtj::This_strategy)
def test_swrtj::this_this_setter(instance):
    original = instance.this
    instance.this = original
    assert instance.this == original

@given(instance=swrtj::Number_strategy)
@settings(max_examples=50)
def test_swrtj::number_instantiation(instance):
    assert isinstance(instance, swrtj::Number)

@given(instance=swrtj::Number_strategy)
def test_swrtj::number_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=swrtj::Number_strategy)
def test_swrtj::number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=swrtj::ParameterAssignment_strategy)
@settings(max_examples=50)
def test_swrtj::parameterassignment_instantiation(instance):
    assert isinstance(instance, swrtj::ParameterAssignment)

@given(instance=swrtj::Null_strategy)
@settings(max_examples=50)
def test_swrtj::null_instantiation(instance):
    assert isinstance(instance, swrtj::Null)

@given(instance=swrtj::Null_strategy)
def test_swrtj::null_null_type(instance):
    assert isinstance(instance.null, bool)


@given(instance=swrtj::Null_strategy)
def test_swrtj::null_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original

@given(instance=swrtj::Message_strategy)
@settings(max_examples=50)
def test_swrtj::message_instantiation(instance):
    assert isinstance(instance, swrtj::Message)

@given(instance=swrtj::Start_strategy)
@settings(max_examples=50)
def test_swrtj::start_instantiation(instance):
    assert isinstance(instance, swrtj::Start)

@given(instance=swrtj::DottedExpression_strategy)
@settings(max_examples=50)
def test_swrtj::dottedexpression_instantiation(instance):
    assert isinstance(instance, swrtj::DottedExpression)

@given(instance=swrtj::NestedBooleanExpression_strategy)
@settings(max_examples=50)
def test_swrtj::nestedbooleanexpression_instantiation(instance):
    assert isinstance(instance, swrtj::NestedBooleanExpression)

@given(instance=swrtj::CompareOperator_strategy)
@settings(max_examples=50)
def test_swrtj::compareoperator_instantiation(instance):
    assert isinstance(instance, swrtj::CompareOperator)

@given(instance=swrtj::CompareOperator_strategy)
def test_swrtj::compareoperator_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=swrtj::CompareOperator_strategy)
def test_swrtj::compareoperator_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=swrtj::FieldName_strategy)
@settings(max_examples=50)
def test_swrtj::fieldname_instantiation(instance):
    assert isinstance(instance, swrtj::FieldName)

@given(instance=swrtj::FieldName_strategy)
def test_swrtj::fieldname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=swrtj::FieldName_strategy)
def test_swrtj::fieldname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swrtj::Type_strategy)
@settings(max_examples=50)
def test_swrtj::type_instantiation(instance):
    assert isinstance(instance, swrtj::Type)

@given(instance=swrtj::Type_strategy)
def test_swrtj::type_primitiveType_type(instance):
    assert isinstance(instance.primitiveType, str)


@given(instance=swrtj::Type_strategy)
def test_swrtj::type_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original

@given(instance=TraitElement_strategy)
@settings(max_examples=50)
def test_traitelement_instantiation(instance):
    assert isinstance(instance, TraitElement)

@given(instance=swrtj::TraitElement_strategy)
@settings(max_examples=50)
def test_swrtj::traitelement_instantiation(instance):
    assert isinstance(instance, swrtj::TraitElement)

@given(instance=BaseTrait_strategy)
@settings(max_examples=50)
def test_basetrait_instantiation(instance):
    assert isinstance(instance, BaseTrait)

@given(instance=swrtj::TraitName_strategy)
@settings(max_examples=50)
def test_swrtj::traitname_instantiation(instance):
    assert isinstance(instance, swrtj::TraitName)

@given(instance=swrtj::NestedTraitExpression_strategy)
@settings(max_examples=50)
def test_swrtj::nestedtraitexpression_instantiation(instance):
    assert isinstance(instance, swrtj::NestedTraitExpression)

@given(instance=swrtj::AnonimousTrait_strategy)
@settings(max_examples=50)
def test_swrtj::anonimoustrait_instantiation(instance):
    assert isinstance(instance, swrtj::AnonimousTrait)

@given(instance=swrtj::TraitOperation_strategy)
@settings(max_examples=50)
def test_swrtj::traitoperation_instantiation(instance):
    assert isinstance(instance, swrtj::TraitOperation)

@given(instance=swrtj::BaseTrait_strategy)
@settings(max_examples=50)
def test_swrtj::basetrait_instantiation(instance):
    assert isinstance(instance, swrtj::BaseTrait)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=swrtj::WhileStatement_strategy)
@settings(max_examples=50)
def test_swrtj::whilestatement_instantiation(instance):
    assert isinstance(instance, swrtj::WhileStatement)

@given(instance=swrtj::IfThenElseStatement_strategy)
@settings(max_examples=50)
def test_swrtj::ifthenelsestatement_instantiation(instance):
    assert isinstance(instance, swrtj::IfThenElseStatement)

@given(instance=swrtj::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_swrtj::expressionstatement_instantiation(instance):
    assert isinstance(instance, swrtj::ExpressionStatement)

@given(instance=swrtj::Statement_strategy)
@settings(max_examples=50)
def test_swrtj::statement_instantiation(instance):
    assert isinstance(instance, swrtj::Statement)

@given(instance=swrtj::GenericExpression_strategy)
@settings(max_examples=50)
def test_swrtj::genericexpression_instantiation(instance):
    assert isinstance(instance, swrtj::GenericExpression)

@given(instance=swrtj::ReturnStatement_strategy)
@settings(max_examples=50)
def test_swrtj::returnstatement_instantiation(instance):
    assert isinstance(instance, swrtj::ReturnStatement)

@given(instance=swrtj::Parameter_strategy)
@settings(max_examples=50)
def test_swrtj::parameter_instantiation(instance):
    assert isinstance(instance, swrtj::Parameter)

@given(instance=swrtj::Parameter_strategy)
def test_swrtj::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=swrtj::Parameter_strategy)
def test_swrtj::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swrtj::MethodName_strategy)
@settings(max_examples=50)
def test_swrtj::methodname_instantiation(instance):
    assert isinstance(instance, swrtj::MethodName)

@given(instance=swrtj::MethodName_strategy)
def test_swrtj::methodname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=swrtj::MethodName_strategy)
def test_swrtj::methodname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swrtj::TraitExpression_strategy)
@settings(max_examples=50)
def test_swrtj::traitexpression_instantiation(instance):
    assert isinstance(instance, swrtj::TraitExpression)

@given(instance=swrtj::RecordExpression_strategy)
@settings(max_examples=50)
def test_swrtj::recordexpression_instantiation(instance):
    assert isinstance(instance, swrtj::RecordExpression)

@given(instance=swrtj::Method_strategy)
@settings(max_examples=50)
def test_swrtj::method_instantiation(instance):
    assert isinstance(instance, swrtj::Method)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=swrtj::Class_strategy)
@settings(max_examples=50)
def test_swrtj::class_instantiation(instance):
    assert isinstance(instance, swrtj::Class)

@given(instance=swrtj::Trait_strategy)
@settings(max_examples=50)
def test_swrtj::trait_instantiation(instance):
    assert isinstance(instance, swrtj::Trait)

@given(instance=swrtj::Record_strategy)
@settings(max_examples=50)
def test_swrtj::record_instantiation(instance):
    assert isinstance(instance, swrtj::Record)

@given(instance=swrtj::Interface_strategy)
@settings(max_examples=50)
def test_swrtj::interface_instantiation(instance):
    assert isinstance(instance, swrtj::Interface)

@given(instance=swrtj::Element_strategy)
@settings(max_examples=50)
def test_swrtj::element_instantiation(instance):
    assert isinstance(instance, swrtj::Element)

@given(instance=swrtj::Element_strategy)
def test_swrtj::element_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=swrtj::Element_strategy)
def test_swrtj::element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swrtj::Element_strategy)
def test_swrtj::element_construct_type(instance):
    assert isinstance(instance.construct, str)


@given(instance=swrtj::Element_strategy)
def test_swrtj::element_construct_setter(instance):
    original = instance.construct
    instance.construct = original
    assert instance.construct == original

@given(instance=swrtj::Field_strategy)
@settings(max_examples=50)
def test_swrtj::field_instantiation(instance):
    assert isinstance(instance, swrtj::Field)

@given(instance=BaseRecord_strategy)
@settings(max_examples=50)
def test_baserecord_instantiation(instance):
    assert isinstance(instance, BaseRecord)

@given(instance=swrtj::RecordName_strategy)
@settings(max_examples=50)
def test_swrtj::recordname_instantiation(instance):
    assert isinstance(instance, swrtj::RecordName)

@given(instance=swrtj::NestedRecordExpression_strategy)
@settings(max_examples=50)
def test_swrtj::nestedrecordexpression_instantiation(instance):
    assert isinstance(instance, swrtj::NestedRecordExpression)

@given(instance=swrtj::AnonimousRecord_strategy)
@settings(max_examples=50)
def test_swrtj::anonimousrecord_instantiation(instance):
    assert isinstance(instance, swrtj::AnonimousRecord)

@given(instance=swrtj::RecordOperation_strategy)
@settings(max_examples=50)
def test_swrtj::recordoperation_instantiation(instance):
    assert isinstance(instance, swrtj::RecordOperation)

@given(instance=swrtj::BaseRecord_strategy)
@settings(max_examples=50)
def test_swrtj::baserecord_instantiation(instance):
    assert isinstance(instance, swrtj::BaseRecord)

@given(instance=swrtj::Block_strategy)
@settings(max_examples=50)
def test_swrtj::block_instantiation(instance):
    assert isinstance(instance, swrtj::Block)

@given(instance=swrtj::Program_strategy)
@settings(max_examples=50)
def test_swrtj::program_instantiation(instance):
    assert isinstance(instance, swrtj::Program)

@given(instance=swrtj::Constructor_strategy)
@settings(max_examples=50)
def test_swrtj::constructor_instantiation(instance):
    assert isinstance(instance, swrtj::Constructor)

@given(instance=swrtj::Constructor_strategy)
def test_swrtj::constructor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=swrtj::Constructor_strategy)
def test_swrtj::constructor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swrtj::Import_strategy)
@settings(max_examples=50)
def test_swrtj::import_instantiation(instance):
    assert isinstance(instance, swrtj::Import)

@given(instance=swrtj::Import_strategy)
def test_swrtj::import_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=swrtj::Import_strategy)
def test_swrtj::import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=swrtj::File_strategy)
@settings(max_examples=50)
def test_swrtj::file_instantiation(instance):
    assert isinstance(instance, swrtj::File)

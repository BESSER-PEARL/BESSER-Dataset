import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Method,
    swrtj_ProvidedMethod,
    swrtj_RequiredMethod,
    Field,
    swrtj_RequiredField,
    swrtj_FieldDeclaration,
    GenericExpression,
    swrtj_Expression,
    swrtj_BooleanExpression,
    Parameter,
    swrtj_LocalParameter,
    swrtj_FormalParameter,
    Message,
    swrtj_MethodInvocation,
    TraitOperation,
    swrtj_TraitMethodRename,
    swrtj_TraitFieldRename,
    swrtj_TraitAlias,
    swrtj_TraitExclude,
    RecordOperation,
    swrtj_RecordRename,
    swrtj_RecordExclude,
    swrtj_FieldAccess,
    AtomicBooleanExpression,
    swrtj_SimpleComparation,
    swrtj_AtomicBooleanExpression,
    swrtj_BooleanOperator,
    Start,
    swrtj_NestedExpression,
    swrtj_ParameterReference,
    swrtj_Args,
    swrtj_This,
    swrtj_Output,
    swrtj_Number,
    swrtj_Input,
    swrtj_BooleanConstant,
    swrtj_ParameterAssignment,
    swrtj_StringConstant,
    swrtj_Cast,
    swrtj_ConstructorInvocation,
    swrtj_Null,
    swrtj_Message,
    swrtj_Start,
    swrtj_DottedExpression,
    swrtj_NestedBooleanExpression,
    swrtj_CompareOperator,
    swrtj_FieldName,
    swrtj_Type,
    TraitElement,
    swrtj_TraitElement,
    BaseTrait,
    swrtj_TraitName,
    swrtj_NestedTraitExpression,
    swrtj_AnonimousTrait,
    swrtj_TraitOperation,
    swrtj_BaseTrait,
    Statement,
    swrtj_WhileStatement,
    swrtj_IfThenElseStatement,
    swrtj_ExpressionStatement,
    swrtj_Statement,
    swrtj_GenericExpression,
    swrtj_ReturnStatement,
    swrtj_Parameter,
    swrtj_MethodName,
    swrtj_TraitExpression,
    swrtj_RecordExpression,
    swrtj_Method,
    Element,
    swrtj_Class,
    swrtj_Trait,
    swrtj_Record,
    swrtj_Interface,
    swrtj_Element,
    swrtj_Field,
    BaseRecord,
    swrtj_NestedRecordExpression,
    swrtj_RecordName,
    swrtj_AnonimousRecord,
    swrtj_RecordOperation,
    swrtj_BaseRecord,
    swrtj_Block,
    swrtj_Program,
    swrtj_Constructor,
    swrtj_Import,
    swrtj_File,
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



def test_swrtj_providedmethod_is_not_abstract():
    assert not inspect.isabstract(swrtj_ProvidedMethod)


def test_swrtj_providedmethod_constructor_exists():
    assert callable(swrtj_ProvidedMethod.__init__)


def test_swrtj_providedmethod_constructor_args():
    sig = inspect.signature(swrtj_ProvidedMethod.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronized" in params, "Missing parameter 'isSynchronized'"

def test_swrtj_providedmethod_has_isSynchronized():
    assert hasattr(swrtj_ProvidedMethod, "isSynchronized")
    descriptor = None
    for klass in swrtj_ProvidedMethod.__mro__:
        if "isSynchronized" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronized"]
            break
    assert isinstance(descriptor, property)



def test_swrtj_requiredmethod_is_not_abstract():
    assert not inspect.isabstract(swrtj_RequiredMethod)


def test_swrtj_requiredmethod_constructor_exists():
    assert callable(swrtj_RequiredMethod.__init__)


def test_swrtj_requiredmethod_constructor_args():
    sig = inspect.signature(swrtj_RequiredMethod.__init__)
    params = list(sig.parameters.keys())



def test_field_is_not_abstract():
    assert not inspect.isabstract(Field)


def test_field_constructor_exists():
    assert callable(Field.__init__)


def test_field_constructor_args():
    sig = inspect.signature(Field.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_requiredfield_is_not_abstract():
    assert not inspect.isabstract(swrtj_RequiredField)


def test_swrtj_requiredfield_constructor_exists():
    assert callable(swrtj_RequiredField.__init__)


def test_swrtj_requiredfield_constructor_args():
    sig = inspect.signature(swrtj_RequiredField.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_fielddeclaration_is_not_abstract():
    assert not inspect.isabstract(swrtj_FieldDeclaration)


def test_swrtj_fielddeclaration_constructor_exists():
    assert callable(swrtj_FieldDeclaration.__init__)


def test_swrtj_fielddeclaration_constructor_args():
    sig = inspect.signature(swrtj_FieldDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "modifier" in params, "Missing parameter 'modifier'"

def test_swrtj_fielddeclaration_has_modifier():
    assert hasattr(swrtj_FieldDeclaration, "modifier")
    descriptor = None
    for klass in swrtj_FieldDeclaration.__mro__:
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



def test_swrtj_expression_is_not_abstract():
    assert not inspect.isabstract(swrtj_Expression)


def test_swrtj_expression_constructor_exists():
    assert callable(swrtj_Expression.__init__)


def test_swrtj_expression_constructor_args():
    sig = inspect.signature(swrtj_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "operatorList" in params, "Missing parameter 'operatorList'"
    assert "sign" in params, "Missing parameter 'sign'"

def test_swrtj_expression_has_operatorList():
    assert hasattr(swrtj_Expression, "operatorList")
    descriptor = None
    for klass in swrtj_Expression.__mro__:
        if "operatorList" in klass.__dict__:
            descriptor = klass.__dict__["operatorList"]
            break
    assert isinstance(descriptor, property)

def test_swrtj_expression_has_sign():
    assert hasattr(swrtj_Expression, "sign")
    descriptor = None
    for klass in swrtj_Expression.__mro__:
        if "sign" in klass.__dict__:
            descriptor = klass.__dict__["sign"]
            break
    assert isinstance(descriptor, property)



def test_swrtj_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj_BooleanExpression)


def test_swrtj_booleanexpression_constructor_exists():
    assert callable(swrtj_BooleanExpression.__init__)


def test_swrtj_booleanexpression_constructor_args():
    sig = inspect.signature(swrtj_BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_localparameter_is_not_abstract():
    assert not inspect.isabstract(swrtj_LocalParameter)


def test_swrtj_localparameter_constructor_exists():
    assert callable(swrtj_LocalParameter.__init__)


def test_swrtj_localparameter_constructor_args():
    sig = inspect.signature(swrtj_LocalParameter.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_formalparameter_is_not_abstract():
    assert not inspect.isabstract(swrtj_FormalParameter)


def test_swrtj_formalparameter_constructor_exists():
    assert callable(swrtj_FormalParameter.__init__)


def test_swrtj_formalparameter_constructor_args():
    sig = inspect.signature(swrtj_FormalParameter.__init__)
    params = list(sig.parameters.keys())



def test_message_is_not_abstract():
    assert not inspect.isabstract(Message)


def test_message_constructor_exists():
    assert callable(Message.__init__)


def test_message_constructor_args():
    sig = inspect.signature(Message.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_methodinvocation_is_not_abstract():
    assert not inspect.isabstract(swrtj_MethodInvocation)


def test_swrtj_methodinvocation_constructor_exists():
    assert callable(swrtj_MethodInvocation.__init__)


def test_swrtj_methodinvocation_constructor_args():
    sig = inspect.signature(swrtj_MethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_traitoperation_is_not_abstract():
    assert not inspect.isabstract(TraitOperation)


def test_traitoperation_constructor_exists():
    assert callable(TraitOperation.__init__)


def test_traitoperation_constructor_args():
    sig = inspect.signature(TraitOperation.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_traitmethodrename_is_not_abstract():
    assert not inspect.isabstract(swrtj_TraitMethodRename)


def test_swrtj_traitmethodrename_constructor_exists():
    assert callable(swrtj_TraitMethodRename.__init__)


def test_swrtj_traitmethodrename_constructor_args():
    sig = inspect.signature(swrtj_TraitMethodRename.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_traitfieldrename_is_not_abstract():
    assert not inspect.isabstract(swrtj_TraitFieldRename)


def test_swrtj_traitfieldrename_constructor_exists():
    assert callable(swrtj_TraitFieldRename.__init__)


def test_swrtj_traitfieldrename_constructor_args():
    sig = inspect.signature(swrtj_TraitFieldRename.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_traitalias_is_not_abstract():
    assert not inspect.isabstract(swrtj_TraitAlias)


def test_swrtj_traitalias_constructor_exists():
    assert callable(swrtj_TraitAlias.__init__)


def test_swrtj_traitalias_constructor_args():
    sig = inspect.signature(swrtj_TraitAlias.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_traitexclude_is_not_abstract():
    assert not inspect.isabstract(swrtj_TraitExclude)


def test_swrtj_traitexclude_constructor_exists():
    assert callable(swrtj_TraitExclude.__init__)


def test_swrtj_traitexclude_constructor_args():
    sig = inspect.signature(swrtj_TraitExclude.__init__)
    params = list(sig.parameters.keys())



def test_recordoperation_is_not_abstract():
    assert not inspect.isabstract(RecordOperation)


def test_recordoperation_constructor_exists():
    assert callable(RecordOperation.__init__)


def test_recordoperation_constructor_args():
    sig = inspect.signature(RecordOperation.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_recordrename_is_not_abstract():
    assert not inspect.isabstract(swrtj_RecordRename)


def test_swrtj_recordrename_constructor_exists():
    assert callable(swrtj_RecordRename.__init__)


def test_swrtj_recordrename_constructor_args():
    sig = inspect.signature(swrtj_RecordRename.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_recordexclude_is_not_abstract():
    assert not inspect.isabstract(swrtj_RecordExclude)


def test_swrtj_recordexclude_constructor_exists():
    assert callable(swrtj_RecordExclude.__init__)


def test_swrtj_recordexclude_constructor_args():
    sig = inspect.signature(swrtj_RecordExclude.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_fieldaccess_is_not_abstract():
    assert not inspect.isabstract(swrtj_FieldAccess)


def test_swrtj_fieldaccess_constructor_exists():
    assert callable(swrtj_FieldAccess.__init__)


def test_swrtj_fieldaccess_constructor_args():
    sig = inspect.signature(swrtj_FieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_atomicbooleanexpression_is_not_abstract():
    assert not inspect.isabstract(AtomicBooleanExpression)


def test_atomicbooleanexpression_constructor_exists():
    assert callable(AtomicBooleanExpression.__init__)


def test_atomicbooleanexpression_constructor_args():
    sig = inspect.signature(AtomicBooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_simplecomparation_is_not_abstract():
    assert not inspect.isabstract(swrtj_SimpleComparation)


def test_swrtj_simplecomparation_constructor_exists():
    assert callable(swrtj_SimpleComparation.__init__)


def test_swrtj_simplecomparation_constructor_args():
    sig = inspect.signature(swrtj_SimpleComparation.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_atomicbooleanexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj_AtomicBooleanExpression)


def test_swrtj_atomicbooleanexpression_constructor_exists():
    assert callable(swrtj_AtomicBooleanExpression.__init__)


def test_swrtj_atomicbooleanexpression_constructor_args():
    sig = inspect.signature(swrtj_AtomicBooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "negated" in params, "Missing parameter 'negated'"

def test_swrtj_atomicbooleanexpression_has_negated():
    assert hasattr(swrtj_AtomicBooleanExpression, "negated")
    descriptor = None
    for klass in swrtj_AtomicBooleanExpression.__mro__:
        if "negated" in klass.__dict__:
            descriptor = klass.__dict__["negated"]
            break
    assert isinstance(descriptor, property)



def test_swrtj_booleanoperator_is_not_abstract():
    assert not inspect.isabstract(swrtj_BooleanOperator)


def test_swrtj_booleanoperator_constructor_exists():
    assert callable(swrtj_BooleanOperator.__init__)


def test_swrtj_booleanoperator_constructor_args():
    sig = inspect.signature(swrtj_BooleanOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_swrtj_booleanoperator_has_operator():
    assert hasattr(swrtj_BooleanOperator, "operator")
    descriptor = None
    for klass in swrtj_BooleanOperator.__mro__:
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



def test_swrtj_nestedexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj_NestedExpression)


def test_swrtj_nestedexpression_constructor_exists():
    assert callable(swrtj_NestedExpression.__init__)


def test_swrtj_nestedexpression_constructor_args():
    sig = inspect.signature(swrtj_NestedExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_parameterreference_is_not_abstract():
    assert not inspect.isabstract(swrtj_ParameterReference)


def test_swrtj_parameterreference_constructor_exists():
    assert callable(swrtj_ParameterReference.__init__)


def test_swrtj_parameterreference_constructor_args():
    sig = inspect.signature(swrtj_ParameterReference.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_args_is_not_abstract():
    assert not inspect.isabstract(swrtj_Args)


def test_swrtj_args_constructor_exists():
    assert callable(swrtj_Args.__init__)


def test_swrtj_args_constructor_args():
    sig = inspect.signature(swrtj_Args.__init__)
    params = list(sig.parameters.keys())
    assert "args" in params, "Missing parameter 'args'"

def test_swrtj_args_has_args():
    assert hasattr(swrtj_Args, "args")
    descriptor = None
    for klass in swrtj_Args.__mro__:
        if "args" in klass.__dict__:
            descriptor = klass.__dict__["args"]
            break
    assert isinstance(descriptor, property)



def test_swrtj_this_is_not_abstract():
    assert not inspect.isabstract(swrtj_This)


def test_swrtj_this_constructor_exists():
    assert callable(swrtj_This.__init__)


def test_swrtj_this_constructor_args():
    sig = inspect.signature(swrtj_This.__init__)
    params = list(sig.parameters.keys())
    assert "this" in params, "Missing parameter 'this'"

def test_swrtj_this_has_this():
    assert hasattr(swrtj_This, "this")
    descriptor = None
    for klass in swrtj_This.__mro__:
        if "this" in klass.__dict__:
            descriptor = klass.__dict__["this"]
            break
    assert isinstance(descriptor, property)



def test_swrtj_output_is_not_abstract():
    assert not inspect.isabstract(swrtj_Output)


def test_swrtj_output_constructor_exists():
    assert callable(swrtj_Output.__init__)


def test_swrtj_output_constructor_args():
    sig = inspect.signature(swrtj_Output.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"

def test_swrtj_output_has_output():
    assert hasattr(swrtj_Output, "output")
    descriptor = None
    for klass in swrtj_Output.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_swrtj_number_is_not_abstract():
    assert not inspect.isabstract(swrtj_Number)


def test_swrtj_number_constructor_exists():
    assert callable(swrtj_Number.__init__)


def test_swrtj_number_constructor_args():
    sig = inspect.signature(swrtj_Number.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_swrtj_number_has_value():
    assert hasattr(swrtj_Number, "value")
    descriptor = None
    for klass in swrtj_Number.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_swrtj_input_is_not_abstract():
    assert not inspect.isabstract(swrtj_Input)


def test_swrtj_input_constructor_exists():
    assert callable(swrtj_Input.__init__)


def test_swrtj_input_constructor_args():
    sig = inspect.signature(swrtj_Input.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"

def test_swrtj_input_has_input():
    assert hasattr(swrtj_Input, "input")
    descriptor = None
    for klass in swrtj_Input.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_swrtj_booleanconstant_is_not_abstract():
    assert not inspect.isabstract(swrtj_BooleanConstant)


def test_swrtj_booleanconstant_constructor_exists():
    assert callable(swrtj_BooleanConstant.__init__)


def test_swrtj_booleanconstant_constructor_args():
    sig = inspect.signature(swrtj_BooleanConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_swrtj_booleanconstant_has_value():
    assert hasattr(swrtj_BooleanConstant, "value")
    descriptor = None
    for klass in swrtj_BooleanConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_swrtj_parameterassignment_is_not_abstract():
    assert not inspect.isabstract(swrtj_ParameterAssignment)


def test_swrtj_parameterassignment_constructor_exists():
    assert callable(swrtj_ParameterAssignment.__init__)


def test_swrtj_parameterassignment_constructor_args():
    sig = inspect.signature(swrtj_ParameterAssignment.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_stringconstant_is_not_abstract():
    assert not inspect.isabstract(swrtj_StringConstant)


def test_swrtj_stringconstant_constructor_exists():
    assert callable(swrtj_StringConstant.__init__)


def test_swrtj_stringconstant_constructor_args():
    sig = inspect.signature(swrtj_StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_swrtj_stringconstant_has_value():
    assert hasattr(swrtj_StringConstant, "value")
    descriptor = None
    for klass in swrtj_StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_swrtj_cast_is_not_abstract():
    assert not inspect.isabstract(swrtj_Cast)


def test_swrtj_cast_constructor_exists():
    assert callable(swrtj_Cast.__init__)


def test_swrtj_cast_constructor_args():
    sig = inspect.signature(swrtj_Cast.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_constructorinvocation_is_not_abstract():
    assert not inspect.isabstract(swrtj_ConstructorInvocation)


def test_swrtj_constructorinvocation_constructor_exists():
    assert callable(swrtj_ConstructorInvocation.__init__)


def test_swrtj_constructorinvocation_constructor_args():
    sig = inspect.signature(swrtj_ConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_null_is_not_abstract():
    assert not inspect.isabstract(swrtj_Null)


def test_swrtj_null_constructor_exists():
    assert callable(swrtj_Null.__init__)


def test_swrtj_null_constructor_args():
    sig = inspect.signature(swrtj_Null.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"

def test_swrtj_null_has_null():
    assert hasattr(swrtj_Null, "null")
    descriptor = None
    for klass in swrtj_Null.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)



def test_swrtj_message_is_not_abstract():
    assert not inspect.isabstract(swrtj_Message)


def test_swrtj_message_constructor_exists():
    assert callable(swrtj_Message.__init__)


def test_swrtj_message_constructor_args():
    sig = inspect.signature(swrtj_Message.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_start_is_not_abstract():
    assert not inspect.isabstract(swrtj_Start)


def test_swrtj_start_constructor_exists():
    assert callable(swrtj_Start.__init__)


def test_swrtj_start_constructor_args():
    sig = inspect.signature(swrtj_Start.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_dottedexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj_DottedExpression)


def test_swrtj_dottedexpression_constructor_exists():
    assert callable(swrtj_DottedExpression.__init__)


def test_swrtj_dottedexpression_constructor_args():
    sig = inspect.signature(swrtj_DottedExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_nestedbooleanexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj_NestedBooleanExpression)


def test_swrtj_nestedbooleanexpression_constructor_exists():
    assert callable(swrtj_NestedBooleanExpression.__init__)


def test_swrtj_nestedbooleanexpression_constructor_args():
    sig = inspect.signature(swrtj_NestedBooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_compareoperator_is_not_abstract():
    assert not inspect.isabstract(swrtj_CompareOperator)


def test_swrtj_compareoperator_constructor_exists():
    assert callable(swrtj_CompareOperator.__init__)


def test_swrtj_compareoperator_constructor_args():
    sig = inspect.signature(swrtj_CompareOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_swrtj_compareoperator_has_operator():
    assert hasattr(swrtj_CompareOperator, "operator")
    descriptor = None
    for klass in swrtj_CompareOperator.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_swrtj_fieldname_is_not_abstract():
    assert not inspect.isabstract(swrtj_FieldName)


def test_swrtj_fieldname_constructor_exists():
    assert callable(swrtj_FieldName.__init__)


def test_swrtj_fieldname_constructor_args():
    sig = inspect.signature(swrtj_FieldName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swrtj_fieldname_has_name():
    assert hasattr(swrtj_FieldName, "name")
    descriptor = None
    for klass in swrtj_FieldName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swrtj_type_is_not_abstract():
    assert not inspect.isabstract(swrtj_Type)


def test_swrtj_type_constructor_exists():
    assert callable(swrtj_Type.__init__)


def test_swrtj_type_constructor_args():
    sig = inspect.signature(swrtj_Type.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"

def test_swrtj_type_has_primitiveType():
    assert hasattr(swrtj_Type, "primitiveType")
    descriptor = None
    for klass in swrtj_Type.__mro__:
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



def test_swrtj_traitelement_is_not_abstract():
    assert not inspect.isabstract(swrtj_TraitElement)


def test_swrtj_traitelement_constructor_exists():
    assert callable(swrtj_TraitElement.__init__)


def test_swrtj_traitelement_constructor_args():
    sig = inspect.signature(swrtj_TraitElement.__init__)
    params = list(sig.parameters.keys())



def test_basetrait_is_not_abstract():
    assert not inspect.isabstract(BaseTrait)


def test_basetrait_constructor_exists():
    assert callable(BaseTrait.__init__)


def test_basetrait_constructor_args():
    sig = inspect.signature(BaseTrait.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_traitname_is_not_abstract():
    assert not inspect.isabstract(swrtj_TraitName)


def test_swrtj_traitname_constructor_exists():
    assert callable(swrtj_TraitName.__init__)


def test_swrtj_traitname_constructor_args():
    sig = inspect.signature(swrtj_TraitName.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_nestedtraitexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj_NestedTraitExpression)


def test_swrtj_nestedtraitexpression_constructor_exists():
    assert callable(swrtj_NestedTraitExpression.__init__)


def test_swrtj_nestedtraitexpression_constructor_args():
    sig = inspect.signature(swrtj_NestedTraitExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_anonimoustrait_is_not_abstract():
    assert not inspect.isabstract(swrtj_AnonimousTrait)


def test_swrtj_anonimoustrait_constructor_exists():
    assert callable(swrtj_AnonimousTrait.__init__)


def test_swrtj_anonimoustrait_constructor_args():
    sig = inspect.signature(swrtj_AnonimousTrait.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_traitoperation_is_not_abstract():
    assert not inspect.isabstract(swrtj_TraitOperation)


def test_swrtj_traitoperation_constructor_exists():
    assert callable(swrtj_TraitOperation.__init__)


def test_swrtj_traitoperation_constructor_args():
    sig = inspect.signature(swrtj_TraitOperation.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_basetrait_is_not_abstract():
    assert not inspect.isabstract(swrtj_BaseTrait)


def test_swrtj_basetrait_constructor_exists():
    assert callable(swrtj_BaseTrait.__init__)


def test_swrtj_basetrait_constructor_args():
    sig = inspect.signature(swrtj_BaseTrait.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_whilestatement_is_not_abstract():
    assert not inspect.isabstract(swrtj_WhileStatement)


def test_swrtj_whilestatement_constructor_exists():
    assert callable(swrtj_WhileStatement.__init__)


def test_swrtj_whilestatement_constructor_args():
    sig = inspect.signature(swrtj_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_ifthenelsestatement_is_not_abstract():
    assert not inspect.isabstract(swrtj_IfThenElseStatement)


def test_swrtj_ifthenelsestatement_constructor_exists():
    assert callable(swrtj_IfThenElseStatement.__init__)


def test_swrtj_ifthenelsestatement_constructor_args():
    sig = inspect.signature(swrtj_IfThenElseStatement.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(swrtj_ExpressionStatement)


def test_swrtj_expressionstatement_constructor_exists():
    assert callable(swrtj_ExpressionStatement.__init__)


def test_swrtj_expressionstatement_constructor_args():
    sig = inspect.signature(swrtj_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_statement_is_not_abstract():
    assert not inspect.isabstract(swrtj_Statement)


def test_swrtj_statement_constructor_exists():
    assert callable(swrtj_Statement.__init__)


def test_swrtj_statement_constructor_args():
    sig = inspect.signature(swrtj_Statement.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_genericexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj_GenericExpression)


def test_swrtj_genericexpression_constructor_exists():
    assert callable(swrtj_GenericExpression.__init__)


def test_swrtj_genericexpression_constructor_args():
    sig = inspect.signature(swrtj_GenericExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_returnstatement_is_not_abstract():
    assert not inspect.isabstract(swrtj_ReturnStatement)


def test_swrtj_returnstatement_constructor_exists():
    assert callable(swrtj_ReturnStatement.__init__)


def test_swrtj_returnstatement_constructor_args():
    sig = inspect.signature(swrtj_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_parameter_is_not_abstract():
    assert not inspect.isabstract(swrtj_Parameter)


def test_swrtj_parameter_constructor_exists():
    assert callable(swrtj_Parameter.__init__)


def test_swrtj_parameter_constructor_args():
    sig = inspect.signature(swrtj_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swrtj_parameter_has_name():
    assert hasattr(swrtj_Parameter, "name")
    descriptor = None
    for klass in swrtj_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swrtj_methodname_is_not_abstract():
    assert not inspect.isabstract(swrtj_MethodName)


def test_swrtj_methodname_constructor_exists():
    assert callable(swrtj_MethodName.__init__)


def test_swrtj_methodname_constructor_args():
    sig = inspect.signature(swrtj_MethodName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swrtj_methodname_has_name():
    assert hasattr(swrtj_MethodName, "name")
    descriptor = None
    for klass in swrtj_MethodName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swrtj_traitexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj_TraitExpression)


def test_swrtj_traitexpression_constructor_exists():
    assert callable(swrtj_TraitExpression.__init__)


def test_swrtj_traitexpression_constructor_args():
    sig = inspect.signature(swrtj_TraitExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_recordexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj_RecordExpression)


def test_swrtj_recordexpression_constructor_exists():
    assert callable(swrtj_RecordExpression.__init__)


def test_swrtj_recordexpression_constructor_args():
    sig = inspect.signature(swrtj_RecordExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_method_is_not_abstract():
    assert not inspect.isabstract(swrtj_Method)


def test_swrtj_method_constructor_exists():
    assert callable(swrtj_Method.__init__)


def test_swrtj_method_constructor_args():
    sig = inspect.signature(swrtj_Method.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_class_is_not_abstract():
    assert not inspect.isabstract(swrtj_Class)


def test_swrtj_class_constructor_exists():
    assert callable(swrtj_Class.__init__)


def test_swrtj_class_constructor_args():
    sig = inspect.signature(swrtj_Class.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_trait_is_not_abstract():
    assert not inspect.isabstract(swrtj_Trait)


def test_swrtj_trait_constructor_exists():
    assert callable(swrtj_Trait.__init__)


def test_swrtj_trait_constructor_args():
    sig = inspect.signature(swrtj_Trait.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_record_is_not_abstract():
    assert not inspect.isabstract(swrtj_Record)


def test_swrtj_record_constructor_exists():
    assert callable(swrtj_Record.__init__)


def test_swrtj_record_constructor_args():
    sig = inspect.signature(swrtj_Record.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_interface_is_not_abstract():
    assert not inspect.isabstract(swrtj_Interface)


def test_swrtj_interface_constructor_exists():
    assert callable(swrtj_Interface.__init__)


def test_swrtj_interface_constructor_args():
    sig = inspect.signature(swrtj_Interface.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_element_is_not_abstract():
    assert not inspect.isabstract(swrtj_Element)


def test_swrtj_element_constructor_exists():
    assert callable(swrtj_Element.__init__)


def test_swrtj_element_constructor_args():
    sig = inspect.signature(swrtj_Element.__init__)
    params = list(sig.parameters.keys())
    assert "construct" in params, "Missing parameter 'construct'"
    assert "name" in params, "Missing parameter 'name'"

def test_swrtj_element_has_construct():
    assert hasattr(swrtj_Element, "construct")
    descriptor = None
    for klass in swrtj_Element.__mro__:
        if "construct" in klass.__dict__:
            descriptor = klass.__dict__["construct"]
            break
    assert isinstance(descriptor, property)

def test_swrtj_element_has_name():
    assert hasattr(swrtj_Element, "name")
    descriptor = None
    for klass in swrtj_Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swrtj_field_is_not_abstract():
    assert not inspect.isabstract(swrtj_Field)


def test_swrtj_field_constructor_exists():
    assert callable(swrtj_Field.__init__)


def test_swrtj_field_constructor_args():
    sig = inspect.signature(swrtj_Field.__init__)
    params = list(sig.parameters.keys())



def test_baserecord_is_not_abstract():
    assert not inspect.isabstract(BaseRecord)


def test_baserecord_constructor_exists():
    assert callable(BaseRecord.__init__)


def test_baserecord_constructor_args():
    sig = inspect.signature(BaseRecord.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_nestedrecordexpression_is_not_abstract():
    assert not inspect.isabstract(swrtj_NestedRecordExpression)


def test_swrtj_nestedrecordexpression_constructor_exists():
    assert callable(swrtj_NestedRecordExpression.__init__)


def test_swrtj_nestedrecordexpression_constructor_args():
    sig = inspect.signature(swrtj_NestedRecordExpression.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_recordname_is_not_abstract():
    assert not inspect.isabstract(swrtj_RecordName)


def test_swrtj_recordname_constructor_exists():
    assert callable(swrtj_RecordName.__init__)


def test_swrtj_recordname_constructor_args():
    sig = inspect.signature(swrtj_RecordName.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_anonimousrecord_is_not_abstract():
    assert not inspect.isabstract(swrtj_AnonimousRecord)


def test_swrtj_anonimousrecord_constructor_exists():
    assert callable(swrtj_AnonimousRecord.__init__)


def test_swrtj_anonimousrecord_constructor_args():
    sig = inspect.signature(swrtj_AnonimousRecord.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_recordoperation_is_not_abstract():
    assert not inspect.isabstract(swrtj_RecordOperation)


def test_swrtj_recordoperation_constructor_exists():
    assert callable(swrtj_RecordOperation.__init__)


def test_swrtj_recordoperation_constructor_args():
    sig = inspect.signature(swrtj_RecordOperation.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_baserecord_is_not_abstract():
    assert not inspect.isabstract(swrtj_BaseRecord)


def test_swrtj_baserecord_constructor_exists():
    assert callable(swrtj_BaseRecord.__init__)


def test_swrtj_baserecord_constructor_args():
    sig = inspect.signature(swrtj_BaseRecord.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_block_is_not_abstract():
    assert not inspect.isabstract(swrtj_Block)


def test_swrtj_block_constructor_exists():
    assert callable(swrtj_Block.__init__)


def test_swrtj_block_constructor_args():
    sig = inspect.signature(swrtj_Block.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_program_is_not_abstract():
    assert not inspect.isabstract(swrtj_Program)


def test_swrtj_program_constructor_exists():
    assert callable(swrtj_Program.__init__)


def test_swrtj_program_constructor_args():
    sig = inspect.signature(swrtj_Program.__init__)
    params = list(sig.parameters.keys())



def test_swrtj_constructor_is_not_abstract():
    assert not inspect.isabstract(swrtj_Constructor)


def test_swrtj_constructor_constructor_exists():
    assert callable(swrtj_Constructor.__init__)


def test_swrtj_constructor_constructor_args():
    sig = inspect.signature(swrtj_Constructor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_swrtj_constructor_has_name():
    assert hasattr(swrtj_Constructor, "name")
    descriptor = None
    for klass in swrtj_Constructor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_swrtj_import_is_not_abstract():
    assert not inspect.isabstract(swrtj_Import)


def test_swrtj_import_constructor_exists():
    assert callable(swrtj_Import.__init__)


def test_swrtj_import_constructor_args():
    sig = inspect.signature(swrtj_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_swrtj_import_has_importURI():
    assert hasattr(swrtj_Import, "importURI")
    descriptor = None
    for klass in swrtj_Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_swrtj_file_is_not_abstract():
    assert not inspect.isabstract(swrtj_File)


def test_swrtj_file_constructor_exists():
    assert callable(swrtj_File.__init__)


def test_swrtj_file_constructor_args():
    sig = inspect.signature(swrtj_File.__init__)
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
swrtj_ProvidedMethod_strategy = st.builds(
    swrtj_ProvidedMethod,
    isSynchronized=
        st.booleans()
)
swrtj_RequiredMethod_strategy = st.builds(
    swrtj_RequiredMethod,
)
Field_strategy = st.builds(
    Field,
)
swrtj_RequiredField_strategy = st.builds(
    swrtj_RequiredField,
)
swrtj_FieldDeclaration_strategy = st.builds(
    swrtj_FieldDeclaration,
    modifier=
        safe_text
)
GenericExpression_strategy = st.builds(
    GenericExpression,
)
swrtj_Expression_strategy = st.builds(
    swrtj_Expression,
    operatorList=
        safe_text,
    sign=
        safe_text
)
swrtj_BooleanExpression_strategy = st.builds(
    swrtj_BooleanExpression,
)
Parameter_strategy = st.builds(
    Parameter,
)
swrtj_LocalParameter_strategy = st.builds(
    swrtj_LocalParameter,
)
swrtj_FormalParameter_strategy = st.builds(
    swrtj_FormalParameter,
)
Message_strategy = st.builds(
    Message,
)
swrtj_MethodInvocation_strategy = st.builds(
    swrtj_MethodInvocation,
)
TraitOperation_strategy = st.builds(
    TraitOperation,
)
swrtj_TraitMethodRename_strategy = st.builds(
    swrtj_TraitMethodRename,
)
swrtj_TraitFieldRename_strategy = st.builds(
    swrtj_TraitFieldRename,
)
swrtj_TraitAlias_strategy = st.builds(
    swrtj_TraitAlias,
)
swrtj_TraitExclude_strategy = st.builds(
    swrtj_TraitExclude,
)
RecordOperation_strategy = st.builds(
    RecordOperation,
)
swrtj_RecordRename_strategy = st.builds(
    swrtj_RecordRename,
)
swrtj_RecordExclude_strategy = st.builds(
    swrtj_RecordExclude,
)
swrtj_FieldAccess_strategy = st.builds(
    swrtj_FieldAccess,
)
AtomicBooleanExpression_strategy = st.builds(
    AtomicBooleanExpression,
)
swrtj_SimpleComparation_strategy = st.builds(
    swrtj_SimpleComparation,
)
swrtj_AtomicBooleanExpression_strategy = st.builds(
    swrtj_AtomicBooleanExpression,
    negated=
        st.booleans()
)
swrtj_BooleanOperator_strategy = st.builds(
    swrtj_BooleanOperator,
    operator=
        safe_text
)
Start_strategy = st.builds(
    Start,
)
swrtj_NestedExpression_strategy = st.builds(
    swrtj_NestedExpression,
)
swrtj_ParameterReference_strategy = st.builds(
    swrtj_ParameterReference,
)
swrtj_Args_strategy = st.builds(
    swrtj_Args,
    args=
        st.booleans()
)
swrtj_This_strategy = st.builds(
    swrtj_This,
    this=
        st.booleans()
)
swrtj_Output_strategy = st.builds(
    swrtj_Output,
    output=
        st.booleans()
)
swrtj_Number_strategy = st.builds(
    swrtj_Number,
    value=
        st.integers()
)
swrtj_Input_strategy = st.builds(
    swrtj_Input,
    input=
        st.booleans()
)
swrtj_BooleanConstant_strategy = st.builds(
    swrtj_BooleanConstant,
    value=
        safe_text
)
swrtj_ParameterAssignment_strategy = st.builds(
    swrtj_ParameterAssignment,
)
swrtj_StringConstant_strategy = st.builds(
    swrtj_StringConstant,
    value=
        safe_text
)
swrtj_Cast_strategy = st.builds(
    swrtj_Cast,
)
swrtj_ConstructorInvocation_strategy = st.builds(
    swrtj_ConstructorInvocation,
)
swrtj_Null_strategy = st.builds(
    swrtj_Null,
    null=
        st.booleans()
)
swrtj_Message_strategy = st.builds(
    swrtj_Message,
)
swrtj_Start_strategy = st.builds(
    swrtj_Start,
)
swrtj_DottedExpression_strategy = st.builds(
    swrtj_DottedExpression,
)
swrtj_NestedBooleanExpression_strategy = st.builds(
    swrtj_NestedBooleanExpression,
)
swrtj_CompareOperator_strategy = st.builds(
    swrtj_CompareOperator,
    operator=
        safe_text
)
swrtj_FieldName_strategy = st.builds(
    swrtj_FieldName,
    name=
        safe_text
)
swrtj_Type_strategy = st.builds(
    swrtj_Type,
    primitiveType=
        safe_text
)
TraitElement_strategy = st.builds(
    TraitElement,
)
swrtj_TraitElement_strategy = st.builds(
    swrtj_TraitElement,
)
BaseTrait_strategy = st.builds(
    BaseTrait,
)
swrtj_TraitName_strategy = st.builds(
    swrtj_TraitName,
)
swrtj_NestedTraitExpression_strategy = st.builds(
    swrtj_NestedTraitExpression,
)
swrtj_AnonimousTrait_strategy = st.builds(
    swrtj_AnonimousTrait,
)
swrtj_TraitOperation_strategy = st.builds(
    swrtj_TraitOperation,
)
swrtj_BaseTrait_strategy = st.builds(
    swrtj_BaseTrait,
)
Statement_strategy = st.builds(
    Statement,
)
swrtj_WhileStatement_strategy = st.builds(
    swrtj_WhileStatement,
)
swrtj_IfThenElseStatement_strategy = st.builds(
    swrtj_IfThenElseStatement,
)
swrtj_ExpressionStatement_strategy = st.builds(
    swrtj_ExpressionStatement,
)
swrtj_Statement_strategy = st.builds(
    swrtj_Statement,
)
swrtj_GenericExpression_strategy = st.builds(
    swrtj_GenericExpression,
)
swrtj_ReturnStatement_strategy = st.builds(
    swrtj_ReturnStatement,
)
swrtj_Parameter_strategy = st.builds(
    swrtj_Parameter,
    name=
        safe_text
)
swrtj_MethodName_strategy = st.builds(
    swrtj_MethodName,
    name=
        safe_text
)
swrtj_TraitExpression_strategy = st.builds(
    swrtj_TraitExpression,
)
swrtj_RecordExpression_strategy = st.builds(
    swrtj_RecordExpression,
)
swrtj_Method_strategy = st.builds(
    swrtj_Method,
)
Element_strategy = st.builds(
    Element,
)
swrtj_Class_strategy = st.builds(
    swrtj_Class,
)
swrtj_Trait_strategy = st.builds(
    swrtj_Trait,
)
swrtj_Record_strategy = st.builds(
    swrtj_Record,
)
swrtj_Interface_strategy = st.builds(
    swrtj_Interface,
)
swrtj_Element_strategy = st.builds(
    swrtj_Element,
    construct=
        safe_text,
    name=
        safe_text
)
swrtj_Field_strategy = st.builds(
    swrtj_Field,
)
BaseRecord_strategy = st.builds(
    BaseRecord,
)
swrtj_NestedRecordExpression_strategy = st.builds(
    swrtj_NestedRecordExpression,
)
swrtj_RecordName_strategy = st.builds(
    swrtj_RecordName,
)
swrtj_AnonimousRecord_strategy = st.builds(
    swrtj_AnonimousRecord,
)
swrtj_RecordOperation_strategy = st.builds(
    swrtj_RecordOperation,
)
swrtj_BaseRecord_strategy = st.builds(
    swrtj_BaseRecord,
)
swrtj_Block_strategy = st.builds(
    swrtj_Block,
)
swrtj_Program_strategy = st.builds(
    swrtj_Program,
)
swrtj_Constructor_strategy = st.builds(
    swrtj_Constructor,
    name=
        safe_text
)
swrtj_Import_strategy = st.builds(
    swrtj_Import,
    importURI=
        safe_text
)
swrtj_File_strategy = st.builds(
    swrtj_File,
)

@given(instance=Method_strategy)
@settings(max_examples=50)
def test_method_instantiation(instance):
    assert isinstance(instance, Method)

@given(instance=swrtj_ProvidedMethod_strategy)
@settings(max_examples=50)
def test_swrtj_providedmethod_instantiation(instance):
    assert isinstance(instance, swrtj_ProvidedMethod)



@given(instance=swrtj_ProvidedMethod_strategy)
def test_swrtj_providedmethod_isSynchronized_setter(instance):
    original = instance.isSynchronized
    instance.isSynchronized = original
    assert instance.isSynchronized == original

@given(instance=swrtj_RequiredMethod_strategy)
@settings(max_examples=50)
def test_swrtj_requiredmethod_instantiation(instance):
    assert isinstance(instance, swrtj_RequiredMethod)

@given(instance=Field_strategy)
@settings(max_examples=50)
def test_field_instantiation(instance):
    assert isinstance(instance, Field)

@given(instance=swrtj_RequiredField_strategy)
@settings(max_examples=50)
def test_swrtj_requiredfield_instantiation(instance):
    assert isinstance(instance, swrtj_RequiredField)

@given(instance=swrtj_FieldDeclaration_strategy)
@settings(max_examples=50)
def test_swrtj_fielddeclaration_instantiation(instance):
    assert isinstance(instance, swrtj_FieldDeclaration)



@given(instance=swrtj_FieldDeclaration_strategy)
def test_swrtj_fielddeclaration_modifier_setter(instance):
    original = instance.modifier
    instance.modifier = original
    assert instance.modifier == original

@given(instance=GenericExpression_strategy)
@settings(max_examples=50)
def test_genericexpression_instantiation(instance):
    assert isinstance(instance, GenericExpression)

@given(instance=swrtj_Expression_strategy)
@settings(max_examples=50)
def test_swrtj_expression_instantiation(instance):
    assert isinstance(instance, swrtj_Expression)



@given(instance=swrtj_Expression_strategy)
def test_swrtj_expression_operatorList_setter(instance):
    original = instance.operatorList
    instance.operatorList = original
    assert instance.operatorList == original



@given(instance=swrtj_Expression_strategy)
def test_swrtj_expression_sign_setter(instance):
    original = instance.sign
    instance.sign = original
    assert instance.sign == original

@given(instance=swrtj_BooleanExpression_strategy)
@settings(max_examples=50)
def test_swrtj_booleanexpression_instantiation(instance):
    assert isinstance(instance, swrtj_BooleanExpression)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=swrtj_LocalParameter_strategy)
@settings(max_examples=50)
def test_swrtj_localparameter_instantiation(instance):
    assert isinstance(instance, swrtj_LocalParameter)

@given(instance=swrtj_FormalParameter_strategy)
@settings(max_examples=50)
def test_swrtj_formalparameter_instantiation(instance):
    assert isinstance(instance, swrtj_FormalParameter)

@given(instance=Message_strategy)
@settings(max_examples=50)
def test_message_instantiation(instance):
    assert isinstance(instance, Message)

@given(instance=swrtj_MethodInvocation_strategy)
@settings(max_examples=50)
def test_swrtj_methodinvocation_instantiation(instance):
    assert isinstance(instance, swrtj_MethodInvocation)

@given(instance=TraitOperation_strategy)
@settings(max_examples=50)
def test_traitoperation_instantiation(instance):
    assert isinstance(instance, TraitOperation)

@given(instance=swrtj_TraitMethodRename_strategy)
@settings(max_examples=50)
def test_swrtj_traitmethodrename_instantiation(instance):
    assert isinstance(instance, swrtj_TraitMethodRename)

@given(instance=swrtj_TraitFieldRename_strategy)
@settings(max_examples=50)
def test_swrtj_traitfieldrename_instantiation(instance):
    assert isinstance(instance, swrtj_TraitFieldRename)

@given(instance=swrtj_TraitAlias_strategy)
@settings(max_examples=50)
def test_swrtj_traitalias_instantiation(instance):
    assert isinstance(instance, swrtj_TraitAlias)

@given(instance=swrtj_TraitExclude_strategy)
@settings(max_examples=50)
def test_swrtj_traitexclude_instantiation(instance):
    assert isinstance(instance, swrtj_TraitExclude)

@given(instance=RecordOperation_strategy)
@settings(max_examples=50)
def test_recordoperation_instantiation(instance):
    assert isinstance(instance, RecordOperation)

@given(instance=swrtj_RecordRename_strategy)
@settings(max_examples=50)
def test_swrtj_recordrename_instantiation(instance):
    assert isinstance(instance, swrtj_RecordRename)

@given(instance=swrtj_RecordExclude_strategy)
@settings(max_examples=50)
def test_swrtj_recordexclude_instantiation(instance):
    assert isinstance(instance, swrtj_RecordExclude)

@given(instance=swrtj_FieldAccess_strategy)
@settings(max_examples=50)
def test_swrtj_fieldaccess_instantiation(instance):
    assert isinstance(instance, swrtj_FieldAccess)

@given(instance=AtomicBooleanExpression_strategy)
@settings(max_examples=50)
def test_atomicbooleanexpression_instantiation(instance):
    assert isinstance(instance, AtomicBooleanExpression)

@given(instance=swrtj_SimpleComparation_strategy)
@settings(max_examples=50)
def test_swrtj_simplecomparation_instantiation(instance):
    assert isinstance(instance, swrtj_SimpleComparation)

@given(instance=swrtj_AtomicBooleanExpression_strategy)
@settings(max_examples=50)
def test_swrtj_atomicbooleanexpression_instantiation(instance):
    assert isinstance(instance, swrtj_AtomicBooleanExpression)



@given(instance=swrtj_AtomicBooleanExpression_strategy)
def test_swrtj_atomicbooleanexpression_negated_setter(instance):
    original = instance.negated
    instance.negated = original
    assert instance.negated == original

@given(instance=swrtj_BooleanOperator_strategy)
@settings(max_examples=50)
def test_swrtj_booleanoperator_instantiation(instance):
    assert isinstance(instance, swrtj_BooleanOperator)



@given(instance=swrtj_BooleanOperator_strategy)
def test_swrtj_booleanoperator_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Start_strategy)
@settings(max_examples=50)
def test_start_instantiation(instance):
    assert isinstance(instance, Start)

@given(instance=swrtj_NestedExpression_strategy)
@settings(max_examples=50)
def test_swrtj_nestedexpression_instantiation(instance):
    assert isinstance(instance, swrtj_NestedExpression)

@given(instance=swrtj_ParameterReference_strategy)
@settings(max_examples=50)
def test_swrtj_parameterreference_instantiation(instance):
    assert isinstance(instance, swrtj_ParameterReference)

@given(instance=swrtj_Args_strategy)
@settings(max_examples=50)
def test_swrtj_args_instantiation(instance):
    assert isinstance(instance, swrtj_Args)



@given(instance=swrtj_Args_strategy)
def test_swrtj_args_args_setter(instance):
    original = instance.args
    instance.args = original
    assert instance.args == original

@given(instance=swrtj_This_strategy)
@settings(max_examples=50)
def test_swrtj_this_instantiation(instance):
    assert isinstance(instance, swrtj_This)



@given(instance=swrtj_This_strategy)
def test_swrtj_this_this_setter(instance):
    original = instance.this
    instance.this = original
    assert instance.this == original

@given(instance=swrtj_Output_strategy)
@settings(max_examples=50)
def test_swrtj_output_instantiation(instance):
    assert isinstance(instance, swrtj_Output)



@given(instance=swrtj_Output_strategy)
def test_swrtj_output_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=swrtj_Number_strategy)
@settings(max_examples=50)
def test_swrtj_number_instantiation(instance):
    assert isinstance(instance, swrtj_Number)



@given(instance=swrtj_Number_strategy)
def test_swrtj_number_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=swrtj_Input_strategy)
@settings(max_examples=50)
def test_swrtj_input_instantiation(instance):
    assert isinstance(instance, swrtj_Input)



@given(instance=swrtj_Input_strategy)
def test_swrtj_input_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=swrtj_BooleanConstant_strategy)
@settings(max_examples=50)
def test_swrtj_booleanconstant_instantiation(instance):
    assert isinstance(instance, swrtj_BooleanConstant)



@given(instance=swrtj_BooleanConstant_strategy)
def test_swrtj_booleanconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=swrtj_ParameterAssignment_strategy)
@settings(max_examples=50)
def test_swrtj_parameterassignment_instantiation(instance):
    assert isinstance(instance, swrtj_ParameterAssignment)

@given(instance=swrtj_StringConstant_strategy)
@settings(max_examples=50)
def test_swrtj_stringconstant_instantiation(instance):
    assert isinstance(instance, swrtj_StringConstant)



@given(instance=swrtj_StringConstant_strategy)
def test_swrtj_stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=swrtj_Cast_strategy)
@settings(max_examples=50)
def test_swrtj_cast_instantiation(instance):
    assert isinstance(instance, swrtj_Cast)

@given(instance=swrtj_ConstructorInvocation_strategy)
@settings(max_examples=50)
def test_swrtj_constructorinvocation_instantiation(instance):
    assert isinstance(instance, swrtj_ConstructorInvocation)

@given(instance=swrtj_Null_strategy)
@settings(max_examples=50)
def test_swrtj_null_instantiation(instance):
    assert isinstance(instance, swrtj_Null)



@given(instance=swrtj_Null_strategy)
def test_swrtj_null_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original

@given(instance=swrtj_Message_strategy)
@settings(max_examples=50)
def test_swrtj_message_instantiation(instance):
    assert isinstance(instance, swrtj_Message)

@given(instance=swrtj_Start_strategy)
@settings(max_examples=50)
def test_swrtj_start_instantiation(instance):
    assert isinstance(instance, swrtj_Start)

@given(instance=swrtj_DottedExpression_strategy)
@settings(max_examples=50)
def test_swrtj_dottedexpression_instantiation(instance):
    assert isinstance(instance, swrtj_DottedExpression)

@given(instance=swrtj_NestedBooleanExpression_strategy)
@settings(max_examples=50)
def test_swrtj_nestedbooleanexpression_instantiation(instance):
    assert isinstance(instance, swrtj_NestedBooleanExpression)

@given(instance=swrtj_CompareOperator_strategy)
@settings(max_examples=50)
def test_swrtj_compareoperator_instantiation(instance):
    assert isinstance(instance, swrtj_CompareOperator)



@given(instance=swrtj_CompareOperator_strategy)
def test_swrtj_compareoperator_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=swrtj_FieldName_strategy)
@settings(max_examples=50)
def test_swrtj_fieldname_instantiation(instance):
    assert isinstance(instance, swrtj_FieldName)



@given(instance=swrtj_FieldName_strategy)
def test_swrtj_fieldname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swrtj_Type_strategy)
@settings(max_examples=50)
def test_swrtj_type_instantiation(instance):
    assert isinstance(instance, swrtj_Type)



@given(instance=swrtj_Type_strategy)
def test_swrtj_type_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original

@given(instance=TraitElement_strategy)
@settings(max_examples=50)
def test_traitelement_instantiation(instance):
    assert isinstance(instance, TraitElement)

@given(instance=swrtj_TraitElement_strategy)
@settings(max_examples=50)
def test_swrtj_traitelement_instantiation(instance):
    assert isinstance(instance, swrtj_TraitElement)

@given(instance=BaseTrait_strategy)
@settings(max_examples=50)
def test_basetrait_instantiation(instance):
    assert isinstance(instance, BaseTrait)

@given(instance=swrtj_TraitName_strategy)
@settings(max_examples=50)
def test_swrtj_traitname_instantiation(instance):
    assert isinstance(instance, swrtj_TraitName)

@given(instance=swrtj_NestedTraitExpression_strategy)
@settings(max_examples=50)
def test_swrtj_nestedtraitexpression_instantiation(instance):
    assert isinstance(instance, swrtj_NestedTraitExpression)

@given(instance=swrtj_AnonimousTrait_strategy)
@settings(max_examples=50)
def test_swrtj_anonimoustrait_instantiation(instance):
    assert isinstance(instance, swrtj_AnonimousTrait)

@given(instance=swrtj_TraitOperation_strategy)
@settings(max_examples=50)
def test_swrtj_traitoperation_instantiation(instance):
    assert isinstance(instance, swrtj_TraitOperation)

@given(instance=swrtj_BaseTrait_strategy)
@settings(max_examples=50)
def test_swrtj_basetrait_instantiation(instance):
    assert isinstance(instance, swrtj_BaseTrait)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=swrtj_WhileStatement_strategy)
@settings(max_examples=50)
def test_swrtj_whilestatement_instantiation(instance):
    assert isinstance(instance, swrtj_WhileStatement)

@given(instance=swrtj_IfThenElseStatement_strategy)
@settings(max_examples=50)
def test_swrtj_ifthenelsestatement_instantiation(instance):
    assert isinstance(instance, swrtj_IfThenElseStatement)

@given(instance=swrtj_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_swrtj_expressionstatement_instantiation(instance):
    assert isinstance(instance, swrtj_ExpressionStatement)

@given(instance=swrtj_Statement_strategy)
@settings(max_examples=50)
def test_swrtj_statement_instantiation(instance):
    assert isinstance(instance, swrtj_Statement)

@given(instance=swrtj_GenericExpression_strategy)
@settings(max_examples=50)
def test_swrtj_genericexpression_instantiation(instance):
    assert isinstance(instance, swrtj_GenericExpression)

@given(instance=swrtj_ReturnStatement_strategy)
@settings(max_examples=50)
def test_swrtj_returnstatement_instantiation(instance):
    assert isinstance(instance, swrtj_ReturnStatement)

@given(instance=swrtj_Parameter_strategy)
@settings(max_examples=50)
def test_swrtj_parameter_instantiation(instance):
    assert isinstance(instance, swrtj_Parameter)



@given(instance=swrtj_Parameter_strategy)
def test_swrtj_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swrtj_MethodName_strategy)
@settings(max_examples=50)
def test_swrtj_methodname_instantiation(instance):
    assert isinstance(instance, swrtj_MethodName)



@given(instance=swrtj_MethodName_strategy)
def test_swrtj_methodname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swrtj_TraitExpression_strategy)
@settings(max_examples=50)
def test_swrtj_traitexpression_instantiation(instance):
    assert isinstance(instance, swrtj_TraitExpression)

@given(instance=swrtj_RecordExpression_strategy)
@settings(max_examples=50)
def test_swrtj_recordexpression_instantiation(instance):
    assert isinstance(instance, swrtj_RecordExpression)

@given(instance=swrtj_Method_strategy)
@settings(max_examples=50)
def test_swrtj_method_instantiation(instance):
    assert isinstance(instance, swrtj_Method)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=swrtj_Class_strategy)
@settings(max_examples=50)
def test_swrtj_class_instantiation(instance):
    assert isinstance(instance, swrtj_Class)

@given(instance=swrtj_Trait_strategy)
@settings(max_examples=50)
def test_swrtj_trait_instantiation(instance):
    assert isinstance(instance, swrtj_Trait)

@given(instance=swrtj_Record_strategy)
@settings(max_examples=50)
def test_swrtj_record_instantiation(instance):
    assert isinstance(instance, swrtj_Record)

@given(instance=swrtj_Interface_strategy)
@settings(max_examples=50)
def test_swrtj_interface_instantiation(instance):
    assert isinstance(instance, swrtj_Interface)

@given(instance=swrtj_Element_strategy)
@settings(max_examples=50)
def test_swrtj_element_instantiation(instance):
    assert isinstance(instance, swrtj_Element)



@given(instance=swrtj_Element_strategy)
def test_swrtj_element_construct_setter(instance):
    original = instance.construct
    instance.construct = original
    assert instance.construct == original



@given(instance=swrtj_Element_strategy)
def test_swrtj_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swrtj_Field_strategy)
@settings(max_examples=50)
def test_swrtj_field_instantiation(instance):
    assert isinstance(instance, swrtj_Field)

@given(instance=BaseRecord_strategy)
@settings(max_examples=50)
def test_baserecord_instantiation(instance):
    assert isinstance(instance, BaseRecord)

@given(instance=swrtj_NestedRecordExpression_strategy)
@settings(max_examples=50)
def test_swrtj_nestedrecordexpression_instantiation(instance):
    assert isinstance(instance, swrtj_NestedRecordExpression)

@given(instance=swrtj_RecordName_strategy)
@settings(max_examples=50)
def test_swrtj_recordname_instantiation(instance):
    assert isinstance(instance, swrtj_RecordName)

@given(instance=swrtj_AnonimousRecord_strategy)
@settings(max_examples=50)
def test_swrtj_anonimousrecord_instantiation(instance):
    assert isinstance(instance, swrtj_AnonimousRecord)

@given(instance=swrtj_RecordOperation_strategy)
@settings(max_examples=50)
def test_swrtj_recordoperation_instantiation(instance):
    assert isinstance(instance, swrtj_RecordOperation)

@given(instance=swrtj_BaseRecord_strategy)
@settings(max_examples=50)
def test_swrtj_baserecord_instantiation(instance):
    assert isinstance(instance, swrtj_BaseRecord)

@given(instance=swrtj_Block_strategy)
@settings(max_examples=50)
def test_swrtj_block_instantiation(instance):
    assert isinstance(instance, swrtj_Block)

@given(instance=swrtj_Program_strategy)
@settings(max_examples=50)
def test_swrtj_program_instantiation(instance):
    assert isinstance(instance, swrtj_Program)

@given(instance=swrtj_Constructor_strategy)
@settings(max_examples=50)
def test_swrtj_constructor_instantiation(instance):
    assert isinstance(instance, swrtj_Constructor)



@given(instance=swrtj_Constructor_strategy)
def test_swrtj_constructor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=swrtj_Import_strategy)
@settings(max_examples=50)
def test_swrtj_import_instantiation(instance):
    assert isinstance(instance, swrtj_Import)



@given(instance=swrtj_Import_strategy)
def test_swrtj_import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=swrtj_File_strategy)
@settings(max_examples=50)
def test_swrtj_file_instantiation(instance):
    assert isinstance(instance, swrtj_File)

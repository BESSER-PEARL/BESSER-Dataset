import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Relation,
    Expression,
    PagosPim_TerminalValue,
    PagosPim_Add,
    PagosPim_Mult,
    PagosPim_Body,
    PagosPim_ParameterList,
    PagosPim_Expression,
    AttributeDefinition,
    PagosPim_Parameter,
    PagosPim_NewEClass21,
    PagosPim_LogicalExpression,
    PagosPim_ProgramIfExpression,
    PagosPim_ElseSegment,
    PagosPim_IfCondition,
    PagosPim_IfBlock,
    PagosPim_Return,
    PagosPim_EObject,
    PagosPim_AttributeDefinition,
    Attribute,
    PagosPim_Field,
    Control,
    PagosPim_Input,
    PagosPim_Control,
    PagosPim_Operation,
    PagosPim_Relation,
    PagosPim_Attribute,
    PagosPim_GenericComponent,
    PagosPim_SubComponent,
    GenericComponent,
    PagosPim_ViewComponent,
    PagosPim_DaoComponent,
    Operation,
    PagosPim_Action,
    PagosPim_Output,
    PagosPim_FrontService,
    PagosPim_DataLayerComponent,
    PagosPim_ServerService,
    PagosPim_LogicComponent,
    PagosPim_Application,
    DataTypes,
    AddOper,
    LogicalOperator,
    LogicalCononnector,
    Cardinality,
    MultOper,
    RelationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_terminalvalue_is_not_abstract():
    assert not inspect.isabstract(PagosPim_TerminalValue)


def test_pagospim_terminalvalue_constructor_exists():
    assert callable(PagosPim_TerminalValue.__init__)


def test_pagospim_terminalvalue_constructor_args():
    sig = inspect.signature(PagosPim_TerminalValue.__init__)
    params = list(sig.parameters.keys())
    assert "method" in params, "Missing parameter 'method'"
    assert "value" in params, "Missing parameter 'value'"

def test_pagospim_terminalvalue_has_method():
    assert hasattr(PagosPim_TerminalValue, "method")
    descriptor = None
    for klass in PagosPim_TerminalValue.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)

def test_pagospim_terminalvalue_has_value():
    assert hasattr(PagosPim_TerminalValue, "value")
    descriptor = None
    for klass in PagosPim_TerminalValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pagospim_add_is_not_abstract():
    assert not inspect.isabstract(PagosPim_Add)


def test_pagospim_add_constructor_exists():
    assert callable(PagosPim_Add.__init__)


def test_pagospim_add_constructor_args():
    sig = inspect.signature(PagosPim_Add.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_pagospim_add_has_operator():
    assert hasattr(PagosPim_Add, "operator")
    descriptor = None
    for klass in PagosPim_Add.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_pagospim_mult_is_not_abstract():
    assert not inspect.isabstract(PagosPim_Mult)


def test_pagospim_mult_constructor_exists():
    assert callable(PagosPim_Mult.__init__)


def test_pagospim_mult_constructor_args():
    sig = inspect.signature(PagosPim_Mult.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_pagospim_mult_has_operator():
    assert hasattr(PagosPim_Mult, "operator")
    descriptor = None
    for klass in PagosPim_Mult.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_pagospim_body_is_not_abstract():
    assert not inspect.isabstract(PagosPim_Body)


def test_pagospim_body_constructor_exists():
    assert callable(PagosPim_Body.__init__)


def test_pagospim_body_constructor_args():
    sig = inspect.signature(PagosPim_Body.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_parameterlist_is_not_abstract():
    assert not inspect.isabstract(PagosPim_ParameterList)


def test_pagospim_parameterlist_constructor_exists():
    assert callable(PagosPim_ParameterList.__init__)


def test_pagospim_parameterlist_constructor_args():
    sig = inspect.signature(PagosPim_ParameterList.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_expression_is_not_abstract():
    assert not inspect.isabstract(PagosPim_Expression)


def test_pagospim_expression_constructor_exists():
    assert callable(PagosPim_Expression.__init__)


def test_pagospim_expression_constructor_args():
    sig = inspect.signature(PagosPim_Expression.__init__)
    params = list(sig.parameters.keys())



def test_attributedefinition_is_not_abstract():
    assert not inspect.isabstract(AttributeDefinition)


def test_attributedefinition_constructor_exists():
    assert callable(AttributeDefinition.__init__)


def test_attributedefinition_constructor_args():
    sig = inspect.signature(AttributeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_parameter_is_not_abstract():
    assert not inspect.isabstract(PagosPim_Parameter)


def test_pagospim_parameter_constructor_exists():
    assert callable(PagosPim_Parameter.__init__)


def test_pagospim_parameter_constructor_args():
    sig = inspect.signature(PagosPim_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_neweclass21_is_not_abstract():
    assert not inspect.isabstract(PagosPim_NewEClass21)


def test_pagospim_neweclass21_constructor_exists():
    assert callable(PagosPim_NewEClass21.__init__)


def test_pagospim_neweclass21_constructor_args():
    sig = inspect.signature(PagosPim_NewEClass21.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(PagosPim_LogicalExpression)


def test_pagospim_logicalexpression_constructor_exists():
    assert callable(PagosPim_LogicalExpression.__init__)


def test_pagospim_logicalexpression_constructor_args():
    sig = inspect.signature(PagosPim_LogicalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "conOper" in params, "Missing parameter 'conOper'"
    assert "logicalOperator" in params, "Missing parameter 'logicalOperator'"
    assert "literal" in params, "Missing parameter 'literal'"

def test_pagospim_logicalexpression_has_conOper():
    assert hasattr(PagosPim_LogicalExpression, "conOper")
    descriptor = None
    for klass in PagosPim_LogicalExpression.__mro__:
        if "conOper" in klass.__dict__:
            descriptor = klass.__dict__["conOper"]
            break
    assert isinstance(descriptor, property)

def test_pagospim_logicalexpression_has_logicalOperator():
    assert hasattr(PagosPim_LogicalExpression, "logicalOperator")
    descriptor = None
    for klass in PagosPim_LogicalExpression.__mro__:
        if "logicalOperator" in klass.__dict__:
            descriptor = klass.__dict__["logicalOperator"]
            break
    assert isinstance(descriptor, property)

def test_pagospim_logicalexpression_has_literal():
    assert hasattr(PagosPim_LogicalExpression, "literal")
    descriptor = None
    for klass in PagosPim_LogicalExpression.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_pagospim_programifexpression_is_not_abstract():
    assert not inspect.isabstract(PagosPim_ProgramIfExpression)


def test_pagospim_programifexpression_constructor_exists():
    assert callable(PagosPim_ProgramIfExpression.__init__)


def test_pagospim_programifexpression_constructor_args():
    sig = inspect.signature(PagosPim_ProgramIfExpression.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_elsesegment_is_not_abstract():
    assert not inspect.isabstract(PagosPim_ElseSegment)


def test_pagospim_elsesegment_constructor_exists():
    assert callable(PagosPim_ElseSegment.__init__)


def test_pagospim_elsesegment_constructor_args():
    sig = inspect.signature(PagosPim_ElseSegment.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_ifcondition_is_not_abstract():
    assert not inspect.isabstract(PagosPim_IfCondition)


def test_pagospim_ifcondition_constructor_exists():
    assert callable(PagosPim_IfCondition.__init__)


def test_pagospim_ifcondition_constructor_args():
    sig = inspect.signature(PagosPim_IfCondition.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_ifblock_is_not_abstract():
    assert not inspect.isabstract(PagosPim_IfBlock)


def test_pagospim_ifblock_constructor_exists():
    assert callable(PagosPim_IfBlock.__init__)


def test_pagospim_ifblock_constructor_args():
    sig = inspect.signature(PagosPim_IfBlock.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_return_is_not_abstract():
    assert not inspect.isabstract(PagosPim_Return)


def test_pagospim_return_constructor_exists():
    assert callable(PagosPim_Return.__init__)


def test_pagospim_return_constructor_args():
    sig = inspect.signature(PagosPim_Return.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_pagospim_return_has_type():
    assert hasattr(PagosPim_Return, "type")
    descriptor = None
    for klass in PagosPim_Return.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_pagospim_eobject_is_not_abstract():
    assert not inspect.isabstract(PagosPim_EObject)


def test_pagospim_eobject_constructor_exists():
    assert callable(PagosPim_EObject.__init__)


def test_pagospim_eobject_constructor_args():
    sig = inspect.signature(PagosPim_EObject.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_attributedefinition_is_not_abstract():
    assert not inspect.isabstract(PagosPim_AttributeDefinition)


def test_pagospim_attributedefinition_constructor_exists():
    assert callable(PagosPim_AttributeDefinition.__init__)


def test_pagospim_attributedefinition_constructor_args():
    sig = inspect.signature(PagosPim_AttributeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_pagospim_attributedefinition_has_name():
    assert hasattr(PagosPim_AttributeDefinition, "name")
    descriptor = None
    for klass in PagosPim_AttributeDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pagospim_attributedefinition_has_type():
    assert hasattr(PagosPim_AttributeDefinition, "type")
    descriptor = None
    for klass in PagosPim_AttributeDefinition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_field_is_not_abstract():
    assert not inspect.isabstract(PagosPim_Field)


def test_pagospim_field_constructor_exists():
    assert callable(PagosPim_Field.__init__)


def test_pagospim_field_constructor_args():
    sig = inspect.signature(PagosPim_Field.__init__)
    params = list(sig.parameters.keys())



def test_control_is_not_abstract():
    assert not inspect.isabstract(Control)


def test_control_constructor_exists():
    assert callable(Control.__init__)


def test_control_constructor_args():
    sig = inspect.signature(Control.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_input_is_not_abstract():
    assert not inspect.isabstract(PagosPim_Input)


def test_pagospim_input_constructor_exists():
    assert callable(PagosPim_Input.__init__)


def test_pagospim_input_constructor_args():
    sig = inspect.signature(PagosPim_Input.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_control_is_not_abstract():
    assert not inspect.isabstract(PagosPim_Control)


def test_pagospim_control_constructor_exists():
    assert callable(PagosPim_Control.__init__)


def test_pagospim_control_constructor_args():
    sig = inspect.signature(PagosPim_Control.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_pagospim_control_has_label():
    assert hasattr(PagosPim_Control, "label")
    descriptor = None
    for klass in PagosPim_Control.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_pagospim_operation_is_not_abstract():
    assert not inspect.isabstract(PagosPim_Operation)


def test_pagospim_operation_constructor_exists():
    assert callable(PagosPim_Operation.__init__)


def test_pagospim_operation_constructor_args():
    sig = inspect.signature(PagosPim_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pagospim_operation_has_name():
    assert hasattr(PagosPim_Operation, "name")
    descriptor = None
    for klass in PagosPim_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pagospim_relation_is_not_abstract():
    assert not inspect.isabstract(PagosPim_Relation)


def test_pagospim_relation_constructor_exists():
    assert callable(PagosPim_Relation.__init__)


def test_pagospim_relation_constructor_args():
    sig = inspect.signature(PagosPim_Relation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_pagospim_relation_has_name():
    assert hasattr(PagosPim_Relation, "name")
    descriptor = None
    for klass in PagosPim_Relation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pagospim_relation_has_type():
    assert hasattr(PagosPim_Relation, "type")
    descriptor = None
    for klass in PagosPim_Relation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_pagospim_relation_has_cardinality():
    assert hasattr(PagosPim_Relation, "cardinality")
    descriptor = None
    for klass in PagosPim_Relation.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_pagospim_attribute_is_not_abstract():
    assert not inspect.isabstract(PagosPim_Attribute)


def test_pagospim_attribute_constructor_exists():
    assert callable(PagosPim_Attribute.__init__)


def test_pagospim_attribute_constructor_args():
    sig = inspect.signature(PagosPim_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "isIndex" in params, "Missing parameter 'isIndex'"

def test_pagospim_attribute_has_isIndex():
    assert hasattr(PagosPim_Attribute, "isIndex")
    descriptor = None
    for klass in PagosPim_Attribute.__mro__:
        if "isIndex" in klass.__dict__:
            descriptor = klass.__dict__["isIndex"]
            break
    assert isinstance(descriptor, property)



def test_pagospim_genericcomponent_is_not_abstract():
    assert not inspect.isabstract(PagosPim_GenericComponent)


def test_pagospim_genericcomponent_constructor_exists():
    assert callable(PagosPim_GenericComponent.__init__)


def test_pagospim_genericcomponent_constructor_args():
    sig = inspect.signature(PagosPim_GenericComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pagospim_genericcomponent_has_name():
    assert hasattr(PagosPim_GenericComponent, "name")
    descriptor = None
    for klass in PagosPim_GenericComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pagospim_subcomponent_is_not_abstract():
    assert not inspect.isabstract(PagosPim_SubComponent)


def test_pagospim_subcomponent_constructor_exists():
    assert callable(PagosPim_SubComponent.__init__)


def test_pagospim_subcomponent_constructor_args():
    sig = inspect.signature(PagosPim_SubComponent.__init__)
    params = list(sig.parameters.keys())



def test_genericcomponent_is_not_abstract():
    assert not inspect.isabstract(GenericComponent)


def test_genericcomponent_constructor_exists():
    assert callable(GenericComponent.__init__)


def test_genericcomponent_constructor_args():
    sig = inspect.signature(GenericComponent.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_viewcomponent_is_not_abstract():
    assert not inspect.isabstract(PagosPim_ViewComponent)


def test_pagospim_viewcomponent_constructor_exists():
    assert callable(PagosPim_ViewComponent.__init__)


def test_pagospim_viewcomponent_constructor_args():
    sig = inspect.signature(PagosPim_ViewComponent.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_pagospim_viewcomponent_has_title():
    assert hasattr(PagosPim_ViewComponent, "title")
    descriptor = None
    for klass in PagosPim_ViewComponent.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_pagospim_daocomponent_is_not_abstract():
    assert not inspect.isabstract(PagosPim_DaoComponent)


def test_pagospim_daocomponent_constructor_exists():
    assert callable(PagosPim_DaoComponent.__init__)


def test_pagospim_daocomponent_constructor_args():
    sig = inspect.signature(PagosPim_DaoComponent.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_action_is_not_abstract():
    assert not inspect.isabstract(PagosPim_Action)


def test_pagospim_action_constructor_exists():
    assert callable(PagosPim_Action.__init__)


def test_pagospim_action_constructor_args():
    sig = inspect.signature(PagosPim_Action.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_output_is_not_abstract():
    assert not inspect.isabstract(PagosPim_Output)


def test_pagospim_output_constructor_exists():
    assert callable(PagosPim_Output.__init__)


def test_pagospim_output_constructor_args():
    sig = inspect.signature(PagosPim_Output.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_frontservice_is_not_abstract():
    assert not inspect.isabstract(PagosPim_FrontService)


def test_pagospim_frontservice_constructor_exists():
    assert callable(PagosPim_FrontService.__init__)


def test_pagospim_frontservice_constructor_args():
    sig = inspect.signature(PagosPim_FrontService.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_pagospim_frontservice_has_fullName():
    assert hasattr(PagosPim_FrontService, "fullName")
    descriptor = None
    for klass in PagosPim_FrontService.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)



def test_pagospim_datalayercomponent_is_not_abstract():
    assert not inspect.isabstract(PagosPim_DataLayerComponent)


def test_pagospim_datalayercomponent_constructor_exists():
    assert callable(PagosPim_DataLayerComponent.__init__)


def test_pagospim_datalayercomponent_constructor_args():
    sig = inspect.signature(PagosPim_DataLayerComponent.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_serverservice_is_not_abstract():
    assert not inspect.isabstract(PagosPim_ServerService)


def test_pagospim_serverservice_constructor_exists():
    assert callable(PagosPim_ServerService.__init__)


def test_pagospim_serverservice_constructor_args():
    sig = inspect.signature(PagosPim_ServerService.__init__)
    params = list(sig.parameters.keys())



def test_pagospim_logiccomponent_is_not_abstract():
    assert not inspect.isabstract(PagosPim_LogicComponent)


def test_pagospim_logiccomponent_constructor_exists():
    assert callable(PagosPim_LogicComponent.__init__)


def test_pagospim_logiccomponent_constructor_args():
    sig = inspect.signature(PagosPim_LogicComponent.__init__)
    params = list(sig.parameters.keys())
    assert "persistible" in params, "Missing parameter 'persistible'"

def test_pagospim_logiccomponent_has_persistible():
    assert hasattr(PagosPim_LogicComponent, "persistible")
    descriptor = None
    for klass in PagosPim_LogicComponent.__mro__:
        if "persistible" in klass.__dict__:
            descriptor = klass.__dict__["persistible"]
            break
    assert isinstance(descriptor, property)



def test_pagospim_application_is_not_abstract():
    assert not inspect.isabstract(PagosPim_Application)


def test_pagospim_application_constructor_exists():
    assert callable(PagosPim_Application.__init__)


def test_pagospim_application_constructor_args():
    sig = inspect.signature(PagosPim_Application.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pagospim_application_has_name():
    assert hasattr(PagosPim_Application, "name")
    descriptor = None
    for klass in PagosPim_Application.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datatypes_exists():
    # Check that the Enumeration exists
    assert DataTypes is not None

def test_datatypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataTypes]
    expected_literals = [
        "number",
        "long",
        "Date",
        "double",
        "String",
        "int",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataTypes"

def test_addoper_exists():
    # Check that the Enumeration exists
    assert AddOper is not None

def test_addoper_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AddOper]
    expected_literals = [
        "ADD",
        "MINUS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AddOper"

def test_logicaloperator_exists():
    # Check that the Enumeration exists
    assert LogicalOperator is not None

def test_logicaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOperator]
    expected_literals = [
        "EQUALTO",
        "DIFFERENT",
        "LESSTHAN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalOperator"

def test_logicalcononnector_exists():
    # Check that the Enumeration exists
    assert LogicalCononnector is not None

def test_logicalcononnector_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalCononnector]
    expected_literals = [
        "AND",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalCononnector"

def test_cardinality_exists():
    # Check that the Enumeration exists
    assert Cardinality is not None

def test_cardinality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cardinality]
    expected_literals = [
        "CEROTOONE",
        "CEROTOMANY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Cardinality"

def test_multoper_exists():
    # Check that the Enumeration exists
    assert MultOper is not None

def test_multoper_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultOper]
    expected_literals = [
        "MULT",
        "DIV",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultOper"

def test_relationtype_exists():
    # Check that the Enumeration exists
    assert RelationType is not None

def test_relationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationType]
    expected_literals = [
        "REFERENCE",
        "COMPOSITION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationType"


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
Relation_strategy = st.builds(
    Relation,
)
Expression_strategy = st.builds(
    Expression,
)
PagosPim_TerminalValue_strategy = st.builds(
    PagosPim_TerminalValue,
    method=
        safe_text,
    value=
        safe_text
)
PagosPim_Add_strategy = st.builds(
    PagosPim_Add,
    operator=
        safe_text
)
PagosPim_Mult_strategy = st.builds(
    PagosPim_Mult,
    operator=
        safe_text
)
PagosPim_Body_strategy = st.builds(
    PagosPim_Body,
)
PagosPim_ParameterList_strategy = st.builds(
    PagosPim_ParameterList,
)
PagosPim_Expression_strategy = st.builds(
    PagosPim_Expression,
)
AttributeDefinition_strategy = st.builds(
    AttributeDefinition,
)
PagosPim_Parameter_strategy = st.builds(
    PagosPim_Parameter,
)
PagosPim_NewEClass21_strategy = st.builds(
    PagosPim_NewEClass21,
)
PagosPim_LogicalExpression_strategy = st.builds(
    PagosPim_LogicalExpression,
    conOper=
        safe_text,
    logicalOperator=
        safe_text,
    literal=
        safe_text
)
PagosPim_ProgramIfExpression_strategy = st.builds(
    PagosPim_ProgramIfExpression,
)
PagosPim_ElseSegment_strategy = st.builds(
    PagosPim_ElseSegment,
)
PagosPim_IfCondition_strategy = st.builds(
    PagosPim_IfCondition,
)
PagosPim_IfBlock_strategy = st.builds(
    PagosPim_IfBlock,
)
PagosPim_Return_strategy = st.builds(
    PagosPim_Return,
    type=
        safe_text
)
PagosPim_EObject_strategy = st.builds(
    PagosPim_EObject,
)
PagosPim_AttributeDefinition_strategy = st.builds(
    PagosPim_AttributeDefinition,
    name=
        safe_text,
    type=
        safe_text
)
Attribute_strategy = st.builds(
    Attribute,
)
PagosPim_Field_strategy = st.builds(
    PagosPim_Field,
)
Control_strategy = st.builds(
    Control,
)
PagosPim_Input_strategy = st.builds(
    PagosPim_Input,
)
PagosPim_Control_strategy = st.builds(
    PagosPim_Control,
    label=
        safe_text
)
PagosPim_Operation_strategy = st.builds(
    PagosPim_Operation,
    name=
        safe_text
)
PagosPim_Relation_strategy = st.builds(
    PagosPim_Relation,
    name=
        safe_text,
    type=
        safe_text,
    cardinality=
        safe_text
)
PagosPim_Attribute_strategy = st.builds(
    PagosPim_Attribute,
    isIndex=
        safe_text
)
PagosPim_GenericComponent_strategy = st.builds(
    PagosPim_GenericComponent,
    name=
        safe_text
)
PagosPim_SubComponent_strategy = st.builds(
    PagosPim_SubComponent,
)
GenericComponent_strategy = st.builds(
    GenericComponent,
)
PagosPim_ViewComponent_strategy = st.builds(
    PagosPim_ViewComponent,
    title=
        safe_text
)
PagosPim_DaoComponent_strategy = st.builds(
    PagosPim_DaoComponent,
)
Operation_strategy = st.builds(
    Operation,
)
PagosPim_Action_strategy = st.builds(
    PagosPim_Action,
)
PagosPim_Output_strategy = st.builds(
    PagosPim_Output,
)
PagosPim_FrontService_strategy = st.builds(
    PagosPim_FrontService,
    fullName=
        safe_text
)
PagosPim_DataLayerComponent_strategy = st.builds(
    PagosPim_DataLayerComponent,
)
PagosPim_ServerService_strategy = st.builds(
    PagosPim_ServerService,
)
PagosPim_LogicComponent_strategy = st.builds(
    PagosPim_LogicComponent,
    persistible=
        st.booleans()
)
PagosPim_Application_strategy = st.builds(
    PagosPim_Application,
    name=
        safe_text
)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=PagosPim_TerminalValue_strategy)
@settings(max_examples=50)
def test_pagospim_terminalvalue_instantiation(instance):
    assert isinstance(instance, PagosPim_TerminalValue)



@given(instance=PagosPim_TerminalValue_strategy)
def test_pagospim_terminalvalue_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original



@given(instance=PagosPim_TerminalValue_strategy)
def test_pagospim_terminalvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=PagosPim_Add_strategy)
@settings(max_examples=50)
def test_pagospim_add_instantiation(instance):
    assert isinstance(instance, PagosPim_Add)



@given(instance=PagosPim_Add_strategy)
def test_pagospim_add_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=PagosPim_Mult_strategy)
@settings(max_examples=50)
def test_pagospim_mult_instantiation(instance):
    assert isinstance(instance, PagosPim_Mult)



@given(instance=PagosPim_Mult_strategy)
def test_pagospim_mult_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=PagosPim_Body_strategy)
@settings(max_examples=50)
def test_pagospim_body_instantiation(instance):
    assert isinstance(instance, PagosPim_Body)

@given(instance=PagosPim_ParameterList_strategy)
@settings(max_examples=50)
def test_pagospim_parameterlist_instantiation(instance):
    assert isinstance(instance, PagosPim_ParameterList)

@given(instance=PagosPim_Expression_strategy)
@settings(max_examples=50)
def test_pagospim_expression_instantiation(instance):
    assert isinstance(instance, PagosPim_Expression)

@given(instance=AttributeDefinition_strategy)
@settings(max_examples=50)
def test_attributedefinition_instantiation(instance):
    assert isinstance(instance, AttributeDefinition)

@given(instance=PagosPim_Parameter_strategy)
@settings(max_examples=50)
def test_pagospim_parameter_instantiation(instance):
    assert isinstance(instance, PagosPim_Parameter)

@given(instance=PagosPim_NewEClass21_strategy)
@settings(max_examples=50)
def test_pagospim_neweclass21_instantiation(instance):
    assert isinstance(instance, PagosPim_NewEClass21)

@given(instance=PagosPim_LogicalExpression_strategy)
@settings(max_examples=50)
def test_pagospim_logicalexpression_instantiation(instance):
    assert isinstance(instance, PagosPim_LogicalExpression)



@given(instance=PagosPim_LogicalExpression_strategy)
def test_pagospim_logicalexpression_conOper_setter(instance):
    original = instance.conOper
    instance.conOper = original
    assert instance.conOper == original



@given(instance=PagosPim_LogicalExpression_strategy)
def test_pagospim_logicalexpression_logicalOperator_setter(instance):
    original = instance.logicalOperator
    instance.logicalOperator = original
    assert instance.logicalOperator == original



@given(instance=PagosPim_LogicalExpression_strategy)
def test_pagospim_logicalexpression_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=PagosPim_ProgramIfExpression_strategy)
@settings(max_examples=50)
def test_pagospim_programifexpression_instantiation(instance):
    assert isinstance(instance, PagosPim_ProgramIfExpression)

@given(instance=PagosPim_ElseSegment_strategy)
@settings(max_examples=50)
def test_pagospim_elsesegment_instantiation(instance):
    assert isinstance(instance, PagosPim_ElseSegment)

@given(instance=PagosPim_IfCondition_strategy)
@settings(max_examples=50)
def test_pagospim_ifcondition_instantiation(instance):
    assert isinstance(instance, PagosPim_IfCondition)

@given(instance=PagosPim_IfBlock_strategy)
@settings(max_examples=50)
def test_pagospim_ifblock_instantiation(instance):
    assert isinstance(instance, PagosPim_IfBlock)

@given(instance=PagosPim_Return_strategy)
@settings(max_examples=50)
def test_pagospim_return_instantiation(instance):
    assert isinstance(instance, PagosPim_Return)



@given(instance=PagosPim_Return_strategy)
def test_pagospim_return_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=PagosPim_EObject_strategy)
@settings(max_examples=50)
def test_pagospim_eobject_instantiation(instance):
    assert isinstance(instance, PagosPim_EObject)

@given(instance=PagosPim_AttributeDefinition_strategy)
@settings(max_examples=50)
def test_pagospim_attributedefinition_instantiation(instance):
    assert isinstance(instance, PagosPim_AttributeDefinition)



@given(instance=PagosPim_AttributeDefinition_strategy)
def test_pagospim_attributedefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=PagosPim_AttributeDefinition_strategy)
def test_pagospim_attributedefinition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=PagosPim_Field_strategy)
@settings(max_examples=50)
def test_pagospim_field_instantiation(instance):
    assert isinstance(instance, PagosPim_Field)

@given(instance=Control_strategy)
@settings(max_examples=50)
def test_control_instantiation(instance):
    assert isinstance(instance, Control)

@given(instance=PagosPim_Input_strategy)
@settings(max_examples=50)
def test_pagospim_input_instantiation(instance):
    assert isinstance(instance, PagosPim_Input)

@given(instance=PagosPim_Control_strategy)
@settings(max_examples=50)
def test_pagospim_control_instantiation(instance):
    assert isinstance(instance, PagosPim_Control)



@given(instance=PagosPim_Control_strategy)
def test_pagospim_control_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=PagosPim_Operation_strategy)
@settings(max_examples=50)
def test_pagospim_operation_instantiation(instance):
    assert isinstance(instance, PagosPim_Operation)



@given(instance=PagosPim_Operation_strategy)
def test_pagospim_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PagosPim_Relation_strategy)
@settings(max_examples=50)
def test_pagospim_relation_instantiation(instance):
    assert isinstance(instance, PagosPim_Relation)



@given(instance=PagosPim_Relation_strategy)
def test_pagospim_relation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=PagosPim_Relation_strategy)
def test_pagospim_relation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=PagosPim_Relation_strategy)
def test_pagospim_relation_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=PagosPim_Attribute_strategy)
@settings(max_examples=50)
def test_pagospim_attribute_instantiation(instance):
    assert isinstance(instance, PagosPim_Attribute)



@given(instance=PagosPim_Attribute_strategy)
def test_pagospim_attribute_isIndex_setter(instance):
    original = instance.isIndex
    instance.isIndex = original
    assert instance.isIndex == original

@given(instance=PagosPim_GenericComponent_strategy)
@settings(max_examples=50)
def test_pagospim_genericcomponent_instantiation(instance):
    assert isinstance(instance, PagosPim_GenericComponent)



@given(instance=PagosPim_GenericComponent_strategy)
def test_pagospim_genericcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PagosPim_SubComponent_strategy)
@settings(max_examples=50)
def test_pagospim_subcomponent_instantiation(instance):
    assert isinstance(instance, PagosPim_SubComponent)

@given(instance=GenericComponent_strategy)
@settings(max_examples=50)
def test_genericcomponent_instantiation(instance):
    assert isinstance(instance, GenericComponent)

@given(instance=PagosPim_ViewComponent_strategy)
@settings(max_examples=50)
def test_pagospim_viewcomponent_instantiation(instance):
    assert isinstance(instance, PagosPim_ViewComponent)



@given(instance=PagosPim_ViewComponent_strategy)
def test_pagospim_viewcomponent_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=PagosPim_DaoComponent_strategy)
@settings(max_examples=50)
def test_pagospim_daocomponent_instantiation(instance):
    assert isinstance(instance, PagosPim_DaoComponent)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=PagosPim_Action_strategy)
@settings(max_examples=50)
def test_pagospim_action_instantiation(instance):
    assert isinstance(instance, PagosPim_Action)

@given(instance=PagosPim_Output_strategy)
@settings(max_examples=50)
def test_pagospim_output_instantiation(instance):
    assert isinstance(instance, PagosPim_Output)

@given(instance=PagosPim_FrontService_strategy)
@settings(max_examples=50)
def test_pagospim_frontservice_instantiation(instance):
    assert isinstance(instance, PagosPim_FrontService)



@given(instance=PagosPim_FrontService_strategy)
def test_pagospim_frontservice_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

@given(instance=PagosPim_DataLayerComponent_strategy)
@settings(max_examples=50)
def test_pagospim_datalayercomponent_instantiation(instance):
    assert isinstance(instance, PagosPim_DataLayerComponent)

@given(instance=PagosPim_ServerService_strategy)
@settings(max_examples=50)
def test_pagospim_serverservice_instantiation(instance):
    assert isinstance(instance, PagosPim_ServerService)

@given(instance=PagosPim_LogicComponent_strategy)
@settings(max_examples=50)
def test_pagospim_logiccomponent_instantiation(instance):
    assert isinstance(instance, PagosPim_LogicComponent)



@given(instance=PagosPim_LogicComponent_strategy)
def test_pagospim_logiccomponent_persistible_setter(instance):
    original = instance.persistible
    instance.persistible = original
    assert instance.persistible == original

@given(instance=PagosPim_Application_strategy)
@settings(max_examples=50)
def test_pagospim_application_instantiation(instance):
    assert isinstance(instance, PagosPim_Application)



@given(instance=PagosPim_Application_strategy)
def test_pagospim_application_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

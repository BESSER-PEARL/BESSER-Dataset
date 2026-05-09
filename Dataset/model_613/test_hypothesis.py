import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Relation,
    Expression,
    PagosPim::TerminalValue,
    PagosPim::Add,
    PagosPim::Mult,
    PagosPim::Body,
    PagosPim::ParameterList,
    PagosPim::Expression,
    AttributeDefinition,
    PagosPim::Parameter,
    PagosPim::NewEClass21,
    PagosPim::LogicalExpression,
    PagosPim::ProgramIfExpression,
    PagosPim::ElseSegment,
    PagosPim::IfCondition,
    PagosPim::IfBlock,
    PagosPim::Return,
    PagosPim::EObject,
    PagosPim::AttributeDefinition,
    Attribute,
    PagosPim::Field,
    Control,
    PagosPim::Input,
    PagosPim::Control,
    PagosPim::Operation,
    PagosPim::Relation,
    PagosPim::Attribute,
    PagosPim::GenericComponent,
    PagosPim::SubComponent,
    GenericComponent,
    PagosPim::ViewComponent,
    PagosPim::DaoComponent,
    Operation,
    PagosPim::Action,
    PagosPim::Output,
    PagosPim::FrontService,
    PagosPim::DataLayerComponent,
    PagosPim::ServerService,
    PagosPim::LogicComponent,
    PagosPim::Application,
    LogicalCononnector,
    RelationType,
    DataTypes,
    Cardinality,
    MultOper,
    LogicalOperator,
    AddOper,
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



def test_pagospim::terminalvalue_is_not_abstract():
    assert not inspect.isabstract(PagosPim::TerminalValue)


def test_pagospim::terminalvalue_constructor_exists():
    assert callable(PagosPim::TerminalValue.__init__)


def test_pagospim::terminalvalue_constructor_args():
    sig = inspect.signature(PagosPim::TerminalValue.__init__)
    params = list(sig.parameters.keys())
    assert "method" in params, "Missing parameter 'method'"
    assert "value" in params, "Missing parameter 'value'"

def test_pagospim::terminalvalue_has_method():
    assert hasattr(PagosPim::TerminalValue, "method")
    descriptor = None
    for klass in PagosPim::TerminalValue.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)

def test_pagospim::terminalvalue_has_value():
    assert hasattr(PagosPim::TerminalValue, "value")
    descriptor = None
    for klass in PagosPim::TerminalValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pagospim::add_is_not_abstract():
    assert not inspect.isabstract(PagosPim::Add)


def test_pagospim::add_constructor_exists():
    assert callable(PagosPim::Add.__init__)


def test_pagospim::add_constructor_args():
    sig = inspect.signature(PagosPim::Add.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_pagospim::add_has_operator():
    assert hasattr(PagosPim::Add, "operator")
    descriptor = None
    for klass in PagosPim::Add.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_pagospim::mult_is_not_abstract():
    assert not inspect.isabstract(PagosPim::Mult)


def test_pagospim::mult_constructor_exists():
    assert callable(PagosPim::Mult.__init__)


def test_pagospim::mult_constructor_args():
    sig = inspect.signature(PagosPim::Mult.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_pagospim::mult_has_operator():
    assert hasattr(PagosPim::Mult, "operator")
    descriptor = None
    for klass in PagosPim::Mult.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_pagospim::body_is_not_abstract():
    assert not inspect.isabstract(PagosPim::Body)


def test_pagospim::body_constructor_exists():
    assert callable(PagosPim::Body.__init__)


def test_pagospim::body_constructor_args():
    sig = inspect.signature(PagosPim::Body.__init__)
    params = list(sig.parameters.keys())



def test_pagospim::parameterlist_is_not_abstract():
    assert not inspect.isabstract(PagosPim::ParameterList)


def test_pagospim::parameterlist_constructor_exists():
    assert callable(PagosPim::ParameterList.__init__)


def test_pagospim::parameterlist_constructor_args():
    sig = inspect.signature(PagosPim::ParameterList.__init__)
    params = list(sig.parameters.keys())



def test_pagospim::expression_is_not_abstract():
    assert not inspect.isabstract(PagosPim::Expression)


def test_pagospim::expression_constructor_exists():
    assert callable(PagosPim::Expression.__init__)


def test_pagospim::expression_constructor_args():
    sig = inspect.signature(PagosPim::Expression.__init__)
    params = list(sig.parameters.keys())



def test_attributedefinition_is_not_abstract():
    assert not inspect.isabstract(AttributeDefinition)


def test_attributedefinition_constructor_exists():
    assert callable(AttributeDefinition.__init__)


def test_attributedefinition_constructor_args():
    sig = inspect.signature(AttributeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_pagospim::parameter_is_not_abstract():
    assert not inspect.isabstract(PagosPim::Parameter)


def test_pagospim::parameter_constructor_exists():
    assert callable(PagosPim::Parameter.__init__)


def test_pagospim::parameter_constructor_args():
    sig = inspect.signature(PagosPim::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_pagospim::neweclass21_is_not_abstract():
    assert not inspect.isabstract(PagosPim::NewEClass21)


def test_pagospim::neweclass21_constructor_exists():
    assert callable(PagosPim::NewEClass21.__init__)


def test_pagospim::neweclass21_constructor_args():
    sig = inspect.signature(PagosPim::NewEClass21.__init__)
    params = list(sig.parameters.keys())



def test_pagospim::logicalexpression_is_not_abstract():
    assert not inspect.isabstract(PagosPim::LogicalExpression)


def test_pagospim::logicalexpression_constructor_exists():
    assert callable(PagosPim::LogicalExpression.__init__)


def test_pagospim::logicalexpression_constructor_args():
    sig = inspect.signature(PagosPim::LogicalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "conOper" in params, "Missing parameter 'conOper'"
    assert "logicalOperator" in params, "Missing parameter 'logicalOperator'"
    assert "literal" in params, "Missing parameter 'literal'"

def test_pagospim::logicalexpression_has_conOper():
    assert hasattr(PagosPim::LogicalExpression, "conOper")
    descriptor = None
    for klass in PagosPim::LogicalExpression.__mro__:
        if "conOper" in klass.__dict__:
            descriptor = klass.__dict__["conOper"]
            break
    assert isinstance(descriptor, property)

def test_pagospim::logicalexpression_has_logicalOperator():
    assert hasattr(PagosPim::LogicalExpression, "logicalOperator")
    descriptor = None
    for klass in PagosPim::LogicalExpression.__mro__:
        if "logicalOperator" in klass.__dict__:
            descriptor = klass.__dict__["logicalOperator"]
            break
    assert isinstance(descriptor, property)

def test_pagospim::logicalexpression_has_literal():
    assert hasattr(PagosPim::LogicalExpression, "literal")
    descriptor = None
    for klass in PagosPim::LogicalExpression.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_pagospim::programifexpression_is_not_abstract():
    assert not inspect.isabstract(PagosPim::ProgramIfExpression)


def test_pagospim::programifexpression_constructor_exists():
    assert callable(PagosPim::ProgramIfExpression.__init__)


def test_pagospim::programifexpression_constructor_args():
    sig = inspect.signature(PagosPim::ProgramIfExpression.__init__)
    params = list(sig.parameters.keys())



def test_pagospim::elsesegment_is_not_abstract():
    assert not inspect.isabstract(PagosPim::ElseSegment)


def test_pagospim::elsesegment_constructor_exists():
    assert callable(PagosPim::ElseSegment.__init__)


def test_pagospim::elsesegment_constructor_args():
    sig = inspect.signature(PagosPim::ElseSegment.__init__)
    params = list(sig.parameters.keys())



def test_pagospim::ifcondition_is_not_abstract():
    assert not inspect.isabstract(PagosPim::IfCondition)


def test_pagospim::ifcondition_constructor_exists():
    assert callable(PagosPim::IfCondition.__init__)


def test_pagospim::ifcondition_constructor_args():
    sig = inspect.signature(PagosPim::IfCondition.__init__)
    params = list(sig.parameters.keys())



def test_pagospim::ifblock_is_not_abstract():
    assert not inspect.isabstract(PagosPim::IfBlock)


def test_pagospim::ifblock_constructor_exists():
    assert callable(PagosPim::IfBlock.__init__)


def test_pagospim::ifblock_constructor_args():
    sig = inspect.signature(PagosPim::IfBlock.__init__)
    params = list(sig.parameters.keys())



def test_pagospim::return_is_not_abstract():
    assert not inspect.isabstract(PagosPim::Return)


def test_pagospim::return_constructor_exists():
    assert callable(PagosPim::Return.__init__)


def test_pagospim::return_constructor_args():
    sig = inspect.signature(PagosPim::Return.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_pagospim::return_has_type():
    assert hasattr(PagosPim::Return, "type")
    descriptor = None
    for klass in PagosPim::Return.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_pagospim::eobject_is_not_abstract():
    assert not inspect.isabstract(PagosPim::EObject)


def test_pagospim::eobject_constructor_exists():
    assert callable(PagosPim::EObject.__init__)


def test_pagospim::eobject_constructor_args():
    sig = inspect.signature(PagosPim::EObject.__init__)
    params = list(sig.parameters.keys())



def test_pagospim::attributedefinition_is_not_abstract():
    assert not inspect.isabstract(PagosPim::AttributeDefinition)


def test_pagospim::attributedefinition_constructor_exists():
    assert callable(PagosPim::AttributeDefinition.__init__)


def test_pagospim::attributedefinition_constructor_args():
    sig = inspect.signature(PagosPim::AttributeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_pagospim::attributedefinition_has_name():
    assert hasattr(PagosPim::AttributeDefinition, "name")
    descriptor = None
    for klass in PagosPim::AttributeDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pagospim::attributedefinition_has_type():
    assert hasattr(PagosPim::AttributeDefinition, "type")
    descriptor = None
    for klass in PagosPim::AttributeDefinition.__mro__:
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



def test_pagospim::field_is_not_abstract():
    assert not inspect.isabstract(PagosPim::Field)


def test_pagospim::field_constructor_exists():
    assert callable(PagosPim::Field.__init__)


def test_pagospim::field_constructor_args():
    sig = inspect.signature(PagosPim::Field.__init__)
    params = list(sig.parameters.keys())



def test_control_is_not_abstract():
    assert not inspect.isabstract(Control)


def test_control_constructor_exists():
    assert callable(Control.__init__)


def test_control_constructor_args():
    sig = inspect.signature(Control.__init__)
    params = list(sig.parameters.keys())



def test_pagospim::input_is_not_abstract():
    assert not inspect.isabstract(PagosPim::Input)


def test_pagospim::input_constructor_exists():
    assert callable(PagosPim::Input.__init__)


def test_pagospim::input_constructor_args():
    sig = inspect.signature(PagosPim::Input.__init__)
    params = list(sig.parameters.keys())



def test_pagospim::control_is_not_abstract():
    assert not inspect.isabstract(PagosPim::Control)


def test_pagospim::control_constructor_exists():
    assert callable(PagosPim::Control.__init__)


def test_pagospim::control_constructor_args():
    sig = inspect.signature(PagosPim::Control.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_pagospim::control_has_label():
    assert hasattr(PagosPim::Control, "label")
    descriptor = None
    for klass in PagosPim::Control.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_pagospim::operation_is_not_abstract():
    assert not inspect.isabstract(PagosPim::Operation)


def test_pagospim::operation_constructor_exists():
    assert callable(PagosPim::Operation.__init__)


def test_pagospim::operation_constructor_args():
    sig = inspect.signature(PagosPim::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pagospim::operation_has_name():
    assert hasattr(PagosPim::Operation, "name")
    descriptor = None
    for klass in PagosPim::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pagospim::relation_is_not_abstract():
    assert not inspect.isabstract(PagosPim::Relation)


def test_pagospim::relation_constructor_exists():
    assert callable(PagosPim::Relation.__init__)


def test_pagospim::relation_constructor_args():
    sig = inspect.signature(PagosPim::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "cardinality" in params, "Missing parameter 'cardinality'"
    assert "name" in params, "Missing parameter 'name'"

def test_pagospim::relation_has_type():
    assert hasattr(PagosPim::Relation, "type")
    descriptor = None
    for klass in PagosPim::Relation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_pagospim::relation_has_cardinality():
    assert hasattr(PagosPim::Relation, "cardinality")
    descriptor = None
    for klass in PagosPim::Relation.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)

def test_pagospim::relation_has_name():
    assert hasattr(PagosPim::Relation, "name")
    descriptor = None
    for klass in PagosPim::Relation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pagospim::attribute_is_not_abstract():
    assert not inspect.isabstract(PagosPim::Attribute)


def test_pagospim::attribute_constructor_exists():
    assert callable(PagosPim::Attribute.__init__)


def test_pagospim::attribute_constructor_args():
    sig = inspect.signature(PagosPim::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "isIndex" in params, "Missing parameter 'isIndex'"

def test_pagospim::attribute_has_isIndex():
    assert hasattr(PagosPim::Attribute, "isIndex")
    descriptor = None
    for klass in PagosPim::Attribute.__mro__:
        if "isIndex" in klass.__dict__:
            descriptor = klass.__dict__["isIndex"]
            break
    assert isinstance(descriptor, property)



def test_pagospim::genericcomponent_is_not_abstract():
    assert not inspect.isabstract(PagosPim::GenericComponent)


def test_pagospim::genericcomponent_constructor_exists():
    assert callable(PagosPim::GenericComponent.__init__)


def test_pagospim::genericcomponent_constructor_args():
    sig = inspect.signature(PagosPim::GenericComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pagospim::genericcomponent_has_name():
    assert hasattr(PagosPim::GenericComponent, "name")
    descriptor = None
    for klass in PagosPim::GenericComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pagospim::subcomponent_is_not_abstract():
    assert not inspect.isabstract(PagosPim::SubComponent)


def test_pagospim::subcomponent_constructor_exists():
    assert callable(PagosPim::SubComponent.__init__)


def test_pagospim::subcomponent_constructor_args():
    sig = inspect.signature(PagosPim::SubComponent.__init__)
    params = list(sig.parameters.keys())



def test_genericcomponent_is_not_abstract():
    assert not inspect.isabstract(GenericComponent)


def test_genericcomponent_constructor_exists():
    assert callable(GenericComponent.__init__)


def test_genericcomponent_constructor_args():
    sig = inspect.signature(GenericComponent.__init__)
    params = list(sig.parameters.keys())



def test_pagospim::viewcomponent_is_not_abstract():
    assert not inspect.isabstract(PagosPim::ViewComponent)


def test_pagospim::viewcomponent_constructor_exists():
    assert callable(PagosPim::ViewComponent.__init__)


def test_pagospim::viewcomponent_constructor_args():
    sig = inspect.signature(PagosPim::ViewComponent.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_pagospim::viewcomponent_has_title():
    assert hasattr(PagosPim::ViewComponent, "title")
    descriptor = None
    for klass in PagosPim::ViewComponent.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_pagospim::daocomponent_is_not_abstract():
    assert not inspect.isabstract(PagosPim::DaoComponent)


def test_pagospim::daocomponent_constructor_exists():
    assert callable(PagosPim::DaoComponent.__init__)


def test_pagospim::daocomponent_constructor_args():
    sig = inspect.signature(PagosPim::DaoComponent.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_pagospim::action_is_not_abstract():
    assert not inspect.isabstract(PagosPim::Action)


def test_pagospim::action_constructor_exists():
    assert callable(PagosPim::Action.__init__)


def test_pagospim::action_constructor_args():
    sig = inspect.signature(PagosPim::Action.__init__)
    params = list(sig.parameters.keys())



def test_pagospim::output_is_not_abstract():
    assert not inspect.isabstract(PagosPim::Output)


def test_pagospim::output_constructor_exists():
    assert callable(PagosPim::Output.__init__)


def test_pagospim::output_constructor_args():
    sig = inspect.signature(PagosPim::Output.__init__)
    params = list(sig.parameters.keys())



def test_pagospim::frontservice_is_not_abstract():
    assert not inspect.isabstract(PagosPim::FrontService)


def test_pagospim::frontservice_constructor_exists():
    assert callable(PagosPim::FrontService.__init__)


def test_pagospim::frontservice_constructor_args():
    sig = inspect.signature(PagosPim::FrontService.__init__)
    params = list(sig.parameters.keys())
    assert "fullName" in params, "Missing parameter 'fullName'"

def test_pagospim::frontservice_has_fullName():
    assert hasattr(PagosPim::FrontService, "fullName")
    descriptor = None
    for klass in PagosPim::FrontService.__mro__:
        if "fullName" in klass.__dict__:
            descriptor = klass.__dict__["fullName"]
            break
    assert isinstance(descriptor, property)



def test_pagospim::datalayercomponent_is_not_abstract():
    assert not inspect.isabstract(PagosPim::DataLayerComponent)


def test_pagospim::datalayercomponent_constructor_exists():
    assert callable(PagosPim::DataLayerComponent.__init__)


def test_pagospim::datalayercomponent_constructor_args():
    sig = inspect.signature(PagosPim::DataLayerComponent.__init__)
    params = list(sig.parameters.keys())



def test_pagospim::serverservice_is_not_abstract():
    assert not inspect.isabstract(PagosPim::ServerService)


def test_pagospim::serverservice_constructor_exists():
    assert callable(PagosPim::ServerService.__init__)


def test_pagospim::serverservice_constructor_args():
    sig = inspect.signature(PagosPim::ServerService.__init__)
    params = list(sig.parameters.keys())



def test_pagospim::logiccomponent_is_not_abstract():
    assert not inspect.isabstract(PagosPim::LogicComponent)


def test_pagospim::logiccomponent_constructor_exists():
    assert callable(PagosPim::LogicComponent.__init__)


def test_pagospim::logiccomponent_constructor_args():
    sig = inspect.signature(PagosPim::LogicComponent.__init__)
    params = list(sig.parameters.keys())
    assert "persistible" in params, "Missing parameter 'persistible'"

def test_pagospim::logiccomponent_has_persistible():
    assert hasattr(PagosPim::LogicComponent, "persistible")
    descriptor = None
    for klass in PagosPim::LogicComponent.__mro__:
        if "persistible" in klass.__dict__:
            descriptor = klass.__dict__["persistible"]
            break
    assert isinstance(descriptor, property)



def test_pagospim::application_is_not_abstract():
    assert not inspect.isabstract(PagosPim::Application)


def test_pagospim::application_constructor_exists():
    assert callable(PagosPim::Application.__init__)


def test_pagospim::application_constructor_args():
    sig = inspect.signature(PagosPim::Application.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pagospim::application_has_name():
    assert hasattr(PagosPim::Application, "name")
    descriptor = None
    for klass in PagosPim::Application.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_logicalcononnector_exists():
    # Check that the Enumeration exists
    assert LogicalCononnector is not None

def test_logicalcononnector_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalCononnector]
    expected_literals = [
        "OR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalCononnector"

def test_relationtype_exists():
    # Check that the Enumeration exists
    assert RelationType is not None

def test_relationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationType]
    expected_literals = [
        "COMPOSITION",
        "REFERENCE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationType"

def test_datatypes_exists():
    # Check that the Enumeration exists
    assert DataTypes is not None

def test_datatypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataTypes]
    expected_literals = [
        "double",
        "number",
        "Date",
        "String",
        "int",
        "long",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataTypes"

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

def test_logicaloperator_exists():
    # Check that the Enumeration exists
    assert LogicalOperator is not None

def test_logicaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOperator]
    expected_literals = [
        "EQUALTO",
        "LESSTHAN",
        "DIFFERENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalOperator"

def test_addoper_exists():
    # Check that the Enumeration exists
    assert AddOper is not None

def test_addoper_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AddOper]
    expected_literals = [
        "MINUS",
        "ADD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AddOper"


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
PagosPim::TerminalValue_strategy = st.builds(
    PagosPim::TerminalValue,
    method=
        safe_text,
    value=
        safe_text
)
PagosPim::Add_strategy = st.builds(
    PagosPim::Add,
    operator=
        safe_text
)
PagosPim::Mult_strategy = st.builds(
    PagosPim::Mult,
    operator=
        safe_text
)
PagosPim::Body_strategy = st.builds(
    PagosPim::Body,
)
PagosPim::ParameterList_strategy = st.builds(
    PagosPim::ParameterList,
)
PagosPim::Expression_strategy = st.builds(
    PagosPim::Expression,
)
AttributeDefinition_strategy = st.builds(
    AttributeDefinition,
)
PagosPim::Parameter_strategy = st.builds(
    PagosPim::Parameter,
)
PagosPim::NewEClass21_strategy = st.builds(
    PagosPim::NewEClass21,
)
PagosPim::LogicalExpression_strategy = st.builds(
    PagosPim::LogicalExpression,
    conOper=
        safe_text,
    logicalOperator=
        safe_text,
    literal=
        safe_text
)
PagosPim::ProgramIfExpression_strategy = st.builds(
    PagosPim::ProgramIfExpression,
)
PagosPim::ElseSegment_strategy = st.builds(
    PagosPim::ElseSegment,
)
PagosPim::IfCondition_strategy = st.builds(
    PagosPim::IfCondition,
)
PagosPim::IfBlock_strategy = st.builds(
    PagosPim::IfBlock,
)
PagosPim::Return_strategy = st.builds(
    PagosPim::Return,
    type=
        safe_text
)
PagosPim::EObject_strategy = st.builds(
    PagosPim::EObject,
)
PagosPim::AttributeDefinition_strategy = st.builds(
    PagosPim::AttributeDefinition,
    name=
        safe_text,
    type=
        safe_text
)
Attribute_strategy = st.builds(
    Attribute,
)
PagosPim::Field_strategy = st.builds(
    PagosPim::Field,
)
Control_strategy = st.builds(
    Control,
)
PagosPim::Input_strategy = st.builds(
    PagosPim::Input,
)
PagosPim::Control_strategy = st.builds(
    PagosPim::Control,
    label=
        safe_text
)
PagosPim::Operation_strategy = st.builds(
    PagosPim::Operation,
    name=
        safe_text
)
PagosPim::Relation_strategy = st.builds(
    PagosPim::Relation,
    type=
        safe_text,
    cardinality=
        safe_text,
    name=
        safe_text
)
PagosPim::Attribute_strategy = st.builds(
    PagosPim::Attribute,
    isIndex=
        safe_text
)
PagosPim::GenericComponent_strategy = st.builds(
    PagosPim::GenericComponent,
    name=
        safe_text
)
PagosPim::SubComponent_strategy = st.builds(
    PagosPim::SubComponent,
)
GenericComponent_strategy = st.builds(
    GenericComponent,
)
PagosPim::ViewComponent_strategy = st.builds(
    PagosPim::ViewComponent,
    title=
        safe_text
)
PagosPim::DaoComponent_strategy = st.builds(
    PagosPim::DaoComponent,
)
Operation_strategy = st.builds(
    Operation,
)
PagosPim::Action_strategy = st.builds(
    PagosPim::Action,
)
PagosPim::Output_strategy = st.builds(
    PagosPim::Output,
)
PagosPim::FrontService_strategy = st.builds(
    PagosPim::FrontService,
    fullName=
        safe_text
)
PagosPim::DataLayerComponent_strategy = st.builds(
    PagosPim::DataLayerComponent,
)
PagosPim::ServerService_strategy = st.builds(
    PagosPim::ServerService,
)
PagosPim::LogicComponent_strategy = st.builds(
    PagosPim::LogicComponent,
    persistible=
        st.booleans()
)
PagosPim::Application_strategy = st.builds(
    PagosPim::Application,
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

@given(instance=PagosPim::TerminalValue_strategy)
@settings(max_examples=50)
def test_pagospim::terminalvalue_instantiation(instance):
    assert isinstance(instance, PagosPim::TerminalValue)

@given(instance=PagosPim::TerminalValue_strategy)
def test_pagospim::terminalvalue_method_type(instance):
    assert isinstance(instance.method, str)


@given(instance=PagosPim::TerminalValue_strategy)
def test_pagospim::terminalvalue_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=PagosPim::TerminalValue_strategy)
def test_pagospim::terminalvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=PagosPim::TerminalValue_strategy)
def test_pagospim::terminalvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=PagosPim::Add_strategy)
@settings(max_examples=50)
def test_pagospim::add_instantiation(instance):
    assert isinstance(instance, PagosPim::Add)

@given(instance=PagosPim::Add_strategy)
def test_pagospim::add_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=PagosPim::Add_strategy)
def test_pagospim::add_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=PagosPim::Mult_strategy)
@settings(max_examples=50)
def test_pagospim::mult_instantiation(instance):
    assert isinstance(instance, PagosPim::Mult)

@given(instance=PagosPim::Mult_strategy)
def test_pagospim::mult_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=PagosPim::Mult_strategy)
def test_pagospim::mult_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=PagosPim::Body_strategy)
@settings(max_examples=50)
def test_pagospim::body_instantiation(instance):
    assert isinstance(instance, PagosPim::Body)

@given(instance=PagosPim::ParameterList_strategy)
@settings(max_examples=50)
def test_pagospim::parameterlist_instantiation(instance):
    assert isinstance(instance, PagosPim::ParameterList)

@given(instance=PagosPim::Expression_strategy)
@settings(max_examples=50)
def test_pagospim::expression_instantiation(instance):
    assert isinstance(instance, PagosPim::Expression)

@given(instance=AttributeDefinition_strategy)
@settings(max_examples=50)
def test_attributedefinition_instantiation(instance):
    assert isinstance(instance, AttributeDefinition)

@given(instance=PagosPim::Parameter_strategy)
@settings(max_examples=50)
def test_pagospim::parameter_instantiation(instance):
    assert isinstance(instance, PagosPim::Parameter)

@given(instance=PagosPim::NewEClass21_strategy)
@settings(max_examples=50)
def test_pagospim::neweclass21_instantiation(instance):
    assert isinstance(instance, PagosPim::NewEClass21)

@given(instance=PagosPim::LogicalExpression_strategy)
@settings(max_examples=50)
def test_pagospim::logicalexpression_instantiation(instance):
    assert isinstance(instance, PagosPim::LogicalExpression)

@given(instance=PagosPim::LogicalExpression_strategy)
def test_pagospim::logicalexpression_conOper_type(instance):
    assert isinstance(instance.conOper, str)


@given(instance=PagosPim::LogicalExpression_strategy)
def test_pagospim::logicalexpression_conOper_setter(instance):
    original = instance.conOper
    instance.conOper = original
    assert instance.conOper == original

@given(instance=PagosPim::LogicalExpression_strategy)
def test_pagospim::logicalexpression_logicalOperator_type(instance):
    assert isinstance(instance.logicalOperator, str)


@given(instance=PagosPim::LogicalExpression_strategy)
def test_pagospim::logicalexpression_logicalOperator_setter(instance):
    original = instance.logicalOperator
    instance.logicalOperator = original
    assert instance.logicalOperator == original

@given(instance=PagosPim::LogicalExpression_strategy)
def test_pagospim::logicalexpression_literal_type(instance):
    assert isinstance(instance.literal, str)


@given(instance=PagosPim::LogicalExpression_strategy)
def test_pagospim::logicalexpression_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=PagosPim::ProgramIfExpression_strategy)
@settings(max_examples=50)
def test_pagospim::programifexpression_instantiation(instance):
    assert isinstance(instance, PagosPim::ProgramIfExpression)

@given(instance=PagosPim::ElseSegment_strategy)
@settings(max_examples=50)
def test_pagospim::elsesegment_instantiation(instance):
    assert isinstance(instance, PagosPim::ElseSegment)

@given(instance=PagosPim::IfCondition_strategy)
@settings(max_examples=50)
def test_pagospim::ifcondition_instantiation(instance):
    assert isinstance(instance, PagosPim::IfCondition)

@given(instance=PagosPim::IfBlock_strategy)
@settings(max_examples=50)
def test_pagospim::ifblock_instantiation(instance):
    assert isinstance(instance, PagosPim::IfBlock)

@given(instance=PagosPim::Return_strategy)
@settings(max_examples=50)
def test_pagospim::return_instantiation(instance):
    assert isinstance(instance, PagosPim::Return)

@given(instance=PagosPim::Return_strategy)
def test_pagospim::return_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=PagosPim::Return_strategy)
def test_pagospim::return_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=PagosPim::EObject_strategy)
@settings(max_examples=50)
def test_pagospim::eobject_instantiation(instance):
    assert isinstance(instance, PagosPim::EObject)

@given(instance=PagosPim::AttributeDefinition_strategy)
@settings(max_examples=50)
def test_pagospim::attributedefinition_instantiation(instance):
    assert isinstance(instance, PagosPim::AttributeDefinition)

@given(instance=PagosPim::AttributeDefinition_strategy)
def test_pagospim::attributedefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PagosPim::AttributeDefinition_strategy)
def test_pagospim::attributedefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PagosPim::AttributeDefinition_strategy)
def test_pagospim::attributedefinition_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=PagosPim::AttributeDefinition_strategy)
def test_pagospim::attributedefinition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=PagosPim::Field_strategy)
@settings(max_examples=50)
def test_pagospim::field_instantiation(instance):
    assert isinstance(instance, PagosPim::Field)

@given(instance=Control_strategy)
@settings(max_examples=50)
def test_control_instantiation(instance):
    assert isinstance(instance, Control)

@given(instance=PagosPim::Input_strategy)
@settings(max_examples=50)
def test_pagospim::input_instantiation(instance):
    assert isinstance(instance, PagosPim::Input)

@given(instance=PagosPim::Control_strategy)
@settings(max_examples=50)
def test_pagospim::control_instantiation(instance):
    assert isinstance(instance, PagosPim::Control)

@given(instance=PagosPim::Control_strategy)
def test_pagospim::control_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=PagosPim::Control_strategy)
def test_pagospim::control_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=PagosPim::Operation_strategy)
@settings(max_examples=50)
def test_pagospim::operation_instantiation(instance):
    assert isinstance(instance, PagosPim::Operation)

@given(instance=PagosPim::Operation_strategy)
def test_pagospim::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PagosPim::Operation_strategy)
def test_pagospim::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PagosPim::Relation_strategy)
@settings(max_examples=50)
def test_pagospim::relation_instantiation(instance):
    assert isinstance(instance, PagosPim::Relation)

@given(instance=PagosPim::Relation_strategy)
def test_pagospim::relation_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=PagosPim::Relation_strategy)
def test_pagospim::relation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=PagosPim::Relation_strategy)
def test_pagospim::relation_cardinality_type(instance):
    assert isinstance(instance.cardinality, str)


@given(instance=PagosPim::Relation_strategy)
def test_pagospim::relation_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=PagosPim::Relation_strategy)
def test_pagospim::relation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PagosPim::Relation_strategy)
def test_pagospim::relation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PagosPim::Attribute_strategy)
@settings(max_examples=50)
def test_pagospim::attribute_instantiation(instance):
    assert isinstance(instance, PagosPim::Attribute)

@given(instance=PagosPim::Attribute_strategy)
def test_pagospim::attribute_isIndex_type(instance):
    assert isinstance(instance.isIndex, str)


@given(instance=PagosPim::Attribute_strategy)
def test_pagospim::attribute_isIndex_setter(instance):
    original = instance.isIndex
    instance.isIndex = original
    assert instance.isIndex == original

@given(instance=PagosPim::GenericComponent_strategy)
@settings(max_examples=50)
def test_pagospim::genericcomponent_instantiation(instance):
    assert isinstance(instance, PagosPim::GenericComponent)

@given(instance=PagosPim::GenericComponent_strategy)
def test_pagospim::genericcomponent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PagosPim::GenericComponent_strategy)
def test_pagospim::genericcomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PagosPim::SubComponent_strategy)
@settings(max_examples=50)
def test_pagospim::subcomponent_instantiation(instance):
    assert isinstance(instance, PagosPim::SubComponent)

@given(instance=GenericComponent_strategy)
@settings(max_examples=50)
def test_genericcomponent_instantiation(instance):
    assert isinstance(instance, GenericComponent)

@given(instance=PagosPim::ViewComponent_strategy)
@settings(max_examples=50)
def test_pagospim::viewcomponent_instantiation(instance):
    assert isinstance(instance, PagosPim::ViewComponent)

@given(instance=PagosPim::ViewComponent_strategy)
def test_pagospim::viewcomponent_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=PagosPim::ViewComponent_strategy)
def test_pagospim::viewcomponent_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=PagosPim::DaoComponent_strategy)
@settings(max_examples=50)
def test_pagospim::daocomponent_instantiation(instance):
    assert isinstance(instance, PagosPim::DaoComponent)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=PagosPim::Action_strategy)
@settings(max_examples=50)
def test_pagospim::action_instantiation(instance):
    assert isinstance(instance, PagosPim::Action)

@given(instance=PagosPim::Output_strategy)
@settings(max_examples=50)
def test_pagospim::output_instantiation(instance):
    assert isinstance(instance, PagosPim::Output)

@given(instance=PagosPim::FrontService_strategy)
@settings(max_examples=50)
def test_pagospim::frontservice_instantiation(instance):
    assert isinstance(instance, PagosPim::FrontService)

@given(instance=PagosPim::FrontService_strategy)
def test_pagospim::frontservice_fullName_type(instance):
    assert isinstance(instance.fullName, str)


@given(instance=PagosPim::FrontService_strategy)
def test_pagospim::frontservice_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

@given(instance=PagosPim::DataLayerComponent_strategy)
@settings(max_examples=50)
def test_pagospim::datalayercomponent_instantiation(instance):
    assert isinstance(instance, PagosPim::DataLayerComponent)

@given(instance=PagosPim::ServerService_strategy)
@settings(max_examples=50)
def test_pagospim::serverservice_instantiation(instance):
    assert isinstance(instance, PagosPim::ServerService)

@given(instance=PagosPim::LogicComponent_strategy)
@settings(max_examples=50)
def test_pagospim::logiccomponent_instantiation(instance):
    assert isinstance(instance, PagosPim::LogicComponent)

@given(instance=PagosPim::LogicComponent_strategy)
def test_pagospim::logiccomponent_persistible_type(instance):
    assert isinstance(instance.persistible, bool)


@given(instance=PagosPim::LogicComponent_strategy)
def test_pagospim::logiccomponent_persistible_setter(instance):
    original = instance.persistible
    instance.persistible = original
    assert instance.persistible == original

@given(instance=PagosPim::Application_strategy)
@settings(max_examples=50)
def test_pagospim::application_instantiation(instance):
    assert isinstance(instance, PagosPim::Application)

@given(instance=PagosPim::Application_strategy)
def test_pagospim::application_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PagosPim::Application_strategy)
def test_pagospim::application_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

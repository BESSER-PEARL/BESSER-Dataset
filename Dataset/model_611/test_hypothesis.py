import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    appBuilderDSL::Feature,
    appBuilderDSL::Expression,
    Value,
    appBuilderDSL::Value,
    Type,
    appBuilderDSL::Entity,
    appBuilderDSL::DataType,
    appBuilderDSL::Type,
    appBuilderDSL::Import,
    appBuilderDSL::SetInstructionAssignment,
    Instruction,
    appBuilderDSL::SetInstruction,
    Action,
    appBuilderDSL::UiAction,
    ConditionExpression,
    appBuilderDSL::CompositeConditionExpression,
    appBuilderDSL::SimpleConditionExpression,
    appBuilderDSL::ConditionExpression,
    Layout,
    appBuilderDSL::RowLayout,
    appBuilderDSL::GridLayout,
    appBuilderDSL::Control,
    appBuilderDSL::Condition,
    appBuilderDSL::ExecuteAction,
    appBuilderDSL::Navigate,
    appBuilderDSL::ValidationBinding,
    appBuilderDSL::UiListenerBinding,
    appBuilderDSL::DataBinding,
    appBuilderDSL::Action,
    appBuilderDSL::Validator,
    appBuilderDSL::InitAction,
    appBuilderDSL::Attribute,
    appBuilderDSL::Controller,
    appBuilderDSL::View,
    appBuilderDSL::Model,
    appBuilderDSL::EntryParameters,
    Screen,
    appBuilderDSL::CompositeScreen,
    appBuilderDSL::SimpleScreen,
    appBuilderDSL::Screen,
    appBuilderDSL::Main,
    appBuilderDSL::Instruction,
    appBuilderDSL::Service,
    appBuilderDSL::Ui,
    appBuilderDSL::Business,
    AbstractElement,
    appBuilderDSL::System,
    appBuilderDSL::NamespaceDeclation,
    appBuilderDSL::AbstractElement,
    appBuilderDSL::AppBuilder,
    Service,
    appBuilderDSL::InstanceService,
    Control,
    appBuilderDSL::Text,
    appBuilderDSL::List,
    appBuilderDSL::Button,
    appBuilderDSL::ScreenLayout,
    appBuilderDSL::Label,
    DataBinding,
    appBuilderDSL::EnumDataBinding,
    appBuilderDSL::SimpleDataBinding,
    appBuilderDSL::Layout,
    SetInstructionAssignment,
    appBuilderDSL::DynamicValue,
    appBuilderDSL::ControlValue,
    appBuilderDSL::RestCall,
    Device,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_appbuilderdsl::feature_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Feature)


def test_appbuilderdsl::feature_constructor_exists():
    assert callable(appBuilderDSL::Feature.__init__)


def test_appbuilderdsl::feature_constructor_args():
    sig = inspect.signature(appBuilderDSL::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"
    assert "name" in params, "Missing parameter 'name'"

def test_appbuilderdsl::feature_has_many():
    assert hasattr(appBuilderDSL::Feature, "many")
    descriptor = None
    for klass in appBuilderDSL::Feature.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)

def test_appbuilderdsl::feature_has_name():
    assert hasattr(appBuilderDSL::Feature, "name")
    descriptor = None
    for klass in appBuilderDSL::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::expression_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Expression)


def test_appbuilderdsl::expression_constructor_exists():
    assert callable(appBuilderDSL::Expression.__init__)


def test_appbuilderdsl::expression_constructor_args():
    sig = inspect.signature(appBuilderDSL::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "terms" in params, "Missing parameter 'terms'"

def test_appbuilderdsl::expression_has_terms():
    assert hasattr(appBuilderDSL::Expression, "terms")
    descriptor = None
    for klass in appBuilderDSL::Expression.__mro__:
        if "terms" in klass.__dict__:
            descriptor = klass.__dict__["terms"]
            break
    assert isinstance(descriptor, property)



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::value_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Value)


def test_appbuilderdsl::value_constructor_exists():
    assert callable(appBuilderDSL::Value.__init__)


def test_appbuilderdsl::value_constructor_args():
    sig = inspect.signature(appBuilderDSL::Value.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::entity_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Entity)


def test_appbuilderdsl::entity_constructor_exists():
    assert callable(appBuilderDSL::Entity.__init__)


def test_appbuilderdsl::entity_constructor_args():
    sig = inspect.signature(appBuilderDSL::Entity.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::datatype_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::DataType)


def test_appbuilderdsl::datatype_constructor_exists():
    assert callable(appBuilderDSL::DataType.__init__)


def test_appbuilderdsl::datatype_constructor_args():
    sig = inspect.signature(appBuilderDSL::DataType.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::type_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Type)


def test_appbuilderdsl::type_constructor_exists():
    assert callable(appBuilderDSL::Type.__init__)


def test_appbuilderdsl::type_constructor_args():
    sig = inspect.signature(appBuilderDSL::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_appbuilderdsl::type_has_name():
    assert hasattr(appBuilderDSL::Type, "name")
    descriptor = None
    for klass in appBuilderDSL::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::import_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Import)


def test_appbuilderdsl::import_constructor_exists():
    assert callable(appBuilderDSL::Import.__init__)


def test_appbuilderdsl::import_constructor_args():
    sig = inspect.signature(appBuilderDSL::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_appbuilderdsl::import_has_importedNamespace():
    assert hasattr(appBuilderDSL::Import, "importedNamespace")
    descriptor = None
    for klass in appBuilderDSL::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::setinstructionassignment_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::SetInstructionAssignment)


def test_appbuilderdsl::setinstructionassignment_constructor_exists():
    assert callable(appBuilderDSL::SetInstructionAssignment.__init__)


def test_appbuilderdsl::setinstructionassignment_constructor_args():
    sig = inspect.signature(appBuilderDSL::SetInstructionAssignment.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::setinstruction_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::SetInstruction)


def test_appbuilderdsl::setinstruction_constructor_exists():
    assert callable(appBuilderDSL::SetInstruction.__init__)


def test_appbuilderdsl::setinstruction_constructor_args():
    sig = inspect.signature(appBuilderDSL::SetInstruction.__init__)
    params = list(sig.parameters.keys())
    assert "modelAccess" in params, "Missing parameter 'modelAccess'"

def test_appbuilderdsl::setinstruction_has_modelAccess():
    assert hasattr(appBuilderDSL::SetInstruction, "modelAccess")
    descriptor = None
    for klass in appBuilderDSL::SetInstruction.__mro__:
        if "modelAccess" in klass.__dict__:
            descriptor = klass.__dict__["modelAccess"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::uiaction_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::UiAction)


def test_appbuilderdsl::uiaction_constructor_exists():
    assert callable(appBuilderDSL::UiAction.__init__)


def test_appbuilderdsl::uiaction_constructor_args():
    sig = inspect.signature(appBuilderDSL::UiAction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_appbuilderdsl::uiaction_has_name():
    assert hasattr(appBuilderDSL::UiAction, "name")
    descriptor = None
    for klass in appBuilderDSL::UiAction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_conditionexpression_is_not_abstract():
    assert not inspect.isabstract(ConditionExpression)


def test_conditionexpression_constructor_exists():
    assert callable(ConditionExpression.__init__)


def test_conditionexpression_constructor_args():
    sig = inspect.signature(ConditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::compositeconditionexpression_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::CompositeConditionExpression)


def test_appbuilderdsl::compositeconditionexpression_constructor_exists():
    assert callable(appBuilderDSL::CompositeConditionExpression.__init__)


def test_appbuilderdsl::compositeconditionexpression_constructor_args():
    sig = inspect.signature(appBuilderDSL::CompositeConditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::simpleconditionexpression_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::SimpleConditionExpression)


def test_appbuilderdsl::simpleconditionexpression_constructor_exists():
    assert callable(appBuilderDSL::SimpleConditionExpression.__init__)


def test_appbuilderdsl::simpleconditionexpression_constructor_args():
    sig = inspect.signature(appBuilderDSL::SimpleConditionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_appbuilderdsl::simpleconditionexpression_has_variableName():
    assert hasattr(appBuilderDSL::SimpleConditionExpression, "variableName")
    descriptor = None
    for klass in appBuilderDSL::SimpleConditionExpression.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::conditionexpression_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::ConditionExpression)


def test_appbuilderdsl::conditionexpression_constructor_exists():
    assert callable(appBuilderDSL::ConditionExpression.__init__)


def test_appbuilderdsl::conditionexpression_constructor_args():
    sig = inspect.signature(appBuilderDSL::ConditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_layout_is_not_abstract():
    assert not inspect.isabstract(Layout)


def test_layout_constructor_exists():
    assert callable(Layout.__init__)


def test_layout_constructor_args():
    sig = inspect.signature(Layout.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::rowlayout_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::RowLayout)


def test_appbuilderdsl::rowlayout_constructor_exists():
    assert callable(appBuilderDSL::RowLayout.__init__)


def test_appbuilderdsl::rowlayout_constructor_args():
    sig = inspect.signature(appBuilderDSL::RowLayout.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::gridlayout_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::GridLayout)


def test_appbuilderdsl::gridlayout_constructor_exists():
    assert callable(appBuilderDSL::GridLayout.__init__)


def test_appbuilderdsl::gridlayout_constructor_args():
    sig = inspect.signature(appBuilderDSL::GridLayout.__init__)
    params = list(sig.parameters.keys())
    assert "columns" in params, "Missing parameter 'columns'"

def test_appbuilderdsl::gridlayout_has_columns():
    assert hasattr(appBuilderDSL::GridLayout, "columns")
    descriptor = None
    for klass in appBuilderDSL::GridLayout.__mro__:
        if "columns" in klass.__dict__:
            descriptor = klass.__dict__["columns"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::control_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Control)


def test_appbuilderdsl::control_constructor_exists():
    assert callable(appBuilderDSL::Control.__init__)


def test_appbuilderdsl::control_constructor_args():
    sig = inspect.signature(appBuilderDSL::Control.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::condition_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Condition)


def test_appbuilderdsl::condition_constructor_exists():
    assert callable(appBuilderDSL::Condition.__init__)


def test_appbuilderdsl::condition_constructor_args():
    sig = inspect.signature(appBuilderDSL::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_appbuilderdsl::condition_has_name():
    assert hasattr(appBuilderDSL::Condition, "name")
    descriptor = None
    for klass in appBuilderDSL::Condition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::executeaction_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::ExecuteAction)


def test_appbuilderdsl::executeaction_constructor_exists():
    assert callable(appBuilderDSL::ExecuteAction.__init__)


def test_appbuilderdsl::executeaction_constructor_args():
    sig = inspect.signature(appBuilderDSL::ExecuteAction.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::navigate_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Navigate)


def test_appbuilderdsl::navigate_constructor_exists():
    assert callable(appBuilderDSL::Navigate.__init__)


def test_appbuilderdsl::navigate_constructor_args():
    sig = inspect.signature(appBuilderDSL::Navigate.__init__)
    params = list(sig.parameters.keys())
    assert "params" in params, "Missing parameter 'params'"

def test_appbuilderdsl::navigate_has_params():
    assert hasattr(appBuilderDSL::Navigate, "params")
    descriptor = None
    for klass in appBuilderDSL::Navigate.__mro__:
        if "params" in klass.__dict__:
            descriptor = klass.__dict__["params"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::validationbinding_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::ValidationBinding)


def test_appbuilderdsl::validationbinding_constructor_exists():
    assert callable(appBuilderDSL::ValidationBinding.__init__)


def test_appbuilderdsl::validationbinding_constructor_args():
    sig = inspect.signature(appBuilderDSL::ValidationBinding.__init__)
    params = list(sig.parameters.keys())
    assert "controlAccess" in params, "Missing parameter 'controlAccess'"

def test_appbuilderdsl::validationbinding_has_controlAccess():
    assert hasattr(appBuilderDSL::ValidationBinding, "controlAccess")
    descriptor = None
    for klass in appBuilderDSL::ValidationBinding.__mro__:
        if "controlAccess" in klass.__dict__:
            descriptor = klass.__dict__["controlAccess"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::uilistenerbinding_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::UiListenerBinding)


def test_appbuilderdsl::uilistenerbinding_constructor_exists():
    assert callable(appBuilderDSL::UiListenerBinding.__init__)


def test_appbuilderdsl::uilistenerbinding_constructor_args():
    sig = inspect.signature(appBuilderDSL::UiListenerBinding.__init__)
    params = list(sig.parameters.keys())
    assert "controlAccess" in params, "Missing parameter 'controlAccess'"

def test_appbuilderdsl::uilistenerbinding_has_controlAccess():
    assert hasattr(appBuilderDSL::UiListenerBinding, "controlAccess")
    descriptor = None
    for klass in appBuilderDSL::UiListenerBinding.__mro__:
        if "controlAccess" in klass.__dict__:
            descriptor = klass.__dict__["controlAccess"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::databinding_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::DataBinding)


def test_appbuilderdsl::databinding_constructor_exists():
    assert callable(appBuilderDSL::DataBinding.__init__)


def test_appbuilderdsl::databinding_constructor_args():
    sig = inspect.signature(appBuilderDSL::DataBinding.__init__)
    params = list(sig.parameters.keys())
    assert "controlAccess" in params, "Missing parameter 'controlAccess'"

def test_appbuilderdsl::databinding_has_controlAccess():
    assert hasattr(appBuilderDSL::DataBinding, "controlAccess")
    descriptor = None
    for klass in appBuilderDSL::DataBinding.__mro__:
        if "controlAccess" in klass.__dict__:
            descriptor = klass.__dict__["controlAccess"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::action_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Action)


def test_appbuilderdsl::action_constructor_exists():
    assert callable(appBuilderDSL::Action.__init__)


def test_appbuilderdsl::action_constructor_args():
    sig = inspect.signature(appBuilderDSL::Action.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::validator_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Validator)


def test_appbuilderdsl::validator_constructor_exists():
    assert callable(appBuilderDSL::Validator.__init__)


def test_appbuilderdsl::validator_constructor_args():
    sig = inspect.signature(appBuilderDSL::Validator.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::initaction_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::InitAction)


def test_appbuilderdsl::initaction_constructor_exists():
    assert callable(appBuilderDSL::InitAction.__init__)


def test_appbuilderdsl::initaction_constructor_args():
    sig = inspect.signature(appBuilderDSL::InitAction.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::attribute_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Attribute)


def test_appbuilderdsl::attribute_constructor_exists():
    assert callable(appBuilderDSL::Attribute.__init__)


def test_appbuilderdsl::attribute_constructor_args():
    sig = inspect.signature(appBuilderDSL::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_appbuilderdsl::attribute_has_name():
    assert hasattr(appBuilderDSL::Attribute, "name")
    descriptor = None
    for klass in appBuilderDSL::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_appbuilderdsl::attribute_has_type():
    assert hasattr(appBuilderDSL::Attribute, "type")
    descriptor = None
    for klass in appBuilderDSL::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::controller_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Controller)


def test_appbuilderdsl::controller_constructor_exists():
    assert callable(appBuilderDSL::Controller.__init__)


def test_appbuilderdsl::controller_constructor_args():
    sig = inspect.signature(appBuilderDSL::Controller.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::view_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::View)


def test_appbuilderdsl::view_constructor_exists():
    assert callable(appBuilderDSL::View.__init__)


def test_appbuilderdsl::view_constructor_args():
    sig = inspect.signature(appBuilderDSL::View.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::model_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Model)


def test_appbuilderdsl::model_constructor_exists():
    assert callable(appBuilderDSL::Model.__init__)


def test_appbuilderdsl::model_constructor_args():
    sig = inspect.signature(appBuilderDSL::Model.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::entryparameters_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::EntryParameters)


def test_appbuilderdsl::entryparameters_constructor_exists():
    assert callable(appBuilderDSL::EntryParameters.__init__)


def test_appbuilderdsl::entryparameters_constructor_args():
    sig = inspect.signature(appBuilderDSL::EntryParameters.__init__)
    params = list(sig.parameters.keys())



def test_screen_is_not_abstract():
    assert not inspect.isabstract(Screen)


def test_screen_constructor_exists():
    assert callable(Screen.__init__)


def test_screen_constructor_args():
    sig = inspect.signature(Screen.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::compositescreen_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::CompositeScreen)


def test_appbuilderdsl::compositescreen_constructor_exists():
    assert callable(appBuilderDSL::CompositeScreen.__init__)


def test_appbuilderdsl::compositescreen_constructor_args():
    sig = inspect.signature(appBuilderDSL::CompositeScreen.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::simplescreen_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::SimpleScreen)


def test_appbuilderdsl::simplescreen_constructor_exists():
    assert callable(appBuilderDSL::SimpleScreen.__init__)


def test_appbuilderdsl::simplescreen_constructor_args():
    sig = inspect.signature(appBuilderDSL::SimpleScreen.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::screen_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Screen)


def test_appbuilderdsl::screen_constructor_exists():
    assert callable(appBuilderDSL::Screen.__init__)


def test_appbuilderdsl::screen_constructor_args():
    sig = inspect.signature(appBuilderDSL::Screen.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_appbuilderdsl::screen_has_name():
    assert hasattr(appBuilderDSL::Screen, "name")
    descriptor = None
    for klass in appBuilderDSL::Screen.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::main_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Main)


def test_appbuilderdsl::main_constructor_exists():
    assert callable(appBuilderDSL::Main.__init__)


def test_appbuilderdsl::main_constructor_args():
    sig = inspect.signature(appBuilderDSL::Main.__init__)
    params = list(sig.parameters.keys())
    assert "appName" in params, "Missing parameter 'appName'"
    assert "appVersion" in params, "Missing parameter 'appVersion'"
    assert "devices" in params, "Missing parameter 'devices'"
    assert "generalStyle" in params, "Missing parameter 'generalStyle'"

def test_appbuilderdsl::main_has_appName():
    assert hasattr(appBuilderDSL::Main, "appName")
    descriptor = None
    for klass in appBuilderDSL::Main.__mro__:
        if "appName" in klass.__dict__:
            descriptor = klass.__dict__["appName"]
            break
    assert isinstance(descriptor, property)

def test_appbuilderdsl::main_has_appVersion():
    assert hasattr(appBuilderDSL::Main, "appVersion")
    descriptor = None
    for klass in appBuilderDSL::Main.__mro__:
        if "appVersion" in klass.__dict__:
            descriptor = klass.__dict__["appVersion"]
            break
    assert isinstance(descriptor, property)

def test_appbuilderdsl::main_has_devices():
    assert hasattr(appBuilderDSL::Main, "devices")
    descriptor = None
    for klass in appBuilderDSL::Main.__mro__:
        if "devices" in klass.__dict__:
            descriptor = klass.__dict__["devices"]
            break
    assert isinstance(descriptor, property)

def test_appbuilderdsl::main_has_generalStyle():
    assert hasattr(appBuilderDSL::Main, "generalStyle")
    descriptor = None
    for klass in appBuilderDSL::Main.__mro__:
        if "generalStyle" in klass.__dict__:
            descriptor = klass.__dict__["generalStyle"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::instruction_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Instruction)


def test_appbuilderdsl::instruction_constructor_exists():
    assert callable(appBuilderDSL::Instruction.__init__)


def test_appbuilderdsl::instruction_constructor_args():
    sig = inspect.signature(appBuilderDSL::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::service_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Service)


def test_appbuilderdsl::service_constructor_exists():
    assert callable(appBuilderDSL::Service.__init__)


def test_appbuilderdsl::service_constructor_args():
    sig = inspect.signature(appBuilderDSL::Service.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::ui_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Ui)


def test_appbuilderdsl::ui_constructor_exists():
    assert callable(appBuilderDSL::Ui.__init__)


def test_appbuilderdsl::ui_constructor_args():
    sig = inspect.signature(appBuilderDSL::Ui.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::business_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Business)


def test_appbuilderdsl::business_constructor_exists():
    assert callable(appBuilderDSL::Business.__init__)


def test_appbuilderdsl::business_constructor_args():
    sig = inspect.signature(appBuilderDSL::Business.__init__)
    params = list(sig.parameters.keys())



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::system_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::System)


def test_appbuilderdsl::system_constructor_exists():
    assert callable(appBuilderDSL::System.__init__)


def test_appbuilderdsl::system_constructor_args():
    sig = inspect.signature(appBuilderDSL::System.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::namespacedeclation_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::NamespaceDeclation)


def test_appbuilderdsl::namespacedeclation_constructor_exists():
    assert callable(appBuilderDSL::NamespaceDeclation.__init__)


def test_appbuilderdsl::namespacedeclation_constructor_args():
    sig = inspect.signature(appBuilderDSL::NamespaceDeclation.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::abstractelement_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::AbstractElement)


def test_appbuilderdsl::abstractelement_constructor_exists():
    assert callable(appBuilderDSL::AbstractElement.__init__)


def test_appbuilderdsl::abstractelement_constructor_args():
    sig = inspect.signature(appBuilderDSL::AbstractElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_appbuilderdsl::abstractelement_has_name():
    assert hasattr(appBuilderDSL::AbstractElement, "name")
    descriptor = None
    for klass in appBuilderDSL::AbstractElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::appbuilder_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::AppBuilder)


def test_appbuilderdsl::appbuilder_constructor_exists():
    assert callable(appBuilderDSL::AppBuilder.__init__)


def test_appbuilderdsl::appbuilder_constructor_args():
    sig = inspect.signature(appBuilderDSL::AppBuilder.__init__)
    params = list(sig.parameters.keys())



def test_service_is_not_abstract():
    assert not inspect.isabstract(Service)


def test_service_constructor_exists():
    assert callable(Service.__init__)


def test_service_constructor_args():
    sig = inspect.signature(Service.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::instanceservice_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::InstanceService)


def test_appbuilderdsl::instanceservice_constructor_exists():
    assert callable(appBuilderDSL::InstanceService.__init__)


def test_appbuilderdsl::instanceservice_constructor_args():
    sig = inspect.signature(appBuilderDSL::InstanceService.__init__)
    params = list(sig.parameters.keys())
    assert "instanceName" in params, "Missing parameter 'instanceName'"

def test_appbuilderdsl::instanceservice_has_instanceName():
    assert hasattr(appBuilderDSL::InstanceService, "instanceName")
    descriptor = None
    for klass in appBuilderDSL::InstanceService.__mro__:
        if "instanceName" in klass.__dict__:
            descriptor = klass.__dict__["instanceName"]
            break
    assert isinstance(descriptor, property)



def test_control_is_not_abstract():
    assert not inspect.isabstract(Control)


def test_control_constructor_exists():
    assert callable(Control.__init__)


def test_control_constructor_args():
    sig = inspect.signature(Control.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::text_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Text)


def test_appbuilderdsl::text_constructor_exists():
    assert callable(appBuilderDSL::Text.__init__)


def test_appbuilderdsl::text_constructor_args():
    sig = inspect.signature(appBuilderDSL::Text.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_appbuilderdsl::text_has_name():
    assert hasattr(appBuilderDSL::Text, "name")
    descriptor = None
    for klass in appBuilderDSL::Text.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::list_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::List)


def test_appbuilderdsl::list_constructor_exists():
    assert callable(appBuilderDSL::List.__init__)


def test_appbuilderdsl::list_constructor_args():
    sig = inspect.signature(appBuilderDSL::List.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_appbuilderdsl::list_has_name():
    assert hasattr(appBuilderDSL::List, "name")
    descriptor = None
    for klass in appBuilderDSL::List.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::button_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Button)


def test_appbuilderdsl::button_constructor_exists():
    assert callable(appBuilderDSL::Button.__init__)


def test_appbuilderdsl::button_constructor_args():
    sig = inspect.signature(appBuilderDSL::Button.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_appbuilderdsl::button_has_name():
    assert hasattr(appBuilderDSL::Button, "name")
    descriptor = None
    for klass in appBuilderDSL::Button.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::screenlayout_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::ScreenLayout)


def test_appbuilderdsl::screenlayout_constructor_exists():
    assert callable(appBuilderDSL::ScreenLayout.__init__)


def test_appbuilderdsl::screenlayout_constructor_args():
    sig = inspect.signature(appBuilderDSL::ScreenLayout.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::label_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Label)


def test_appbuilderdsl::label_constructor_exists():
    assert callable(appBuilderDSL::Label.__init__)


def test_appbuilderdsl::label_constructor_args():
    sig = inspect.signature(appBuilderDSL::Label.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_appbuilderdsl::label_has_name():
    assert hasattr(appBuilderDSL::Label, "name")
    descriptor = None
    for klass in appBuilderDSL::Label.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_databinding_is_not_abstract():
    assert not inspect.isabstract(DataBinding)


def test_databinding_constructor_exists():
    assert callable(DataBinding.__init__)


def test_databinding_constructor_args():
    sig = inspect.signature(DataBinding.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::enumdatabinding_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::EnumDataBinding)


def test_appbuilderdsl::enumdatabinding_constructor_exists():
    assert callable(appBuilderDSL::EnumDataBinding.__init__)


def test_appbuilderdsl::enumdatabinding_constructor_args():
    sig = inspect.signature(appBuilderDSL::EnumDataBinding.__init__)
    params = list(sig.parameters.keys())
    assert "enumClassName" in params, "Missing parameter 'enumClassName'"

def test_appbuilderdsl::enumdatabinding_has_enumClassName():
    assert hasattr(appBuilderDSL::EnumDataBinding, "enumClassName")
    descriptor = None
    for klass in appBuilderDSL::EnumDataBinding.__mro__:
        if "enumClassName" in klass.__dict__:
            descriptor = klass.__dict__["enumClassName"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::simpledatabinding_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::SimpleDataBinding)


def test_appbuilderdsl::simpledatabinding_constructor_exists():
    assert callable(appBuilderDSL::SimpleDataBinding.__init__)


def test_appbuilderdsl::simpledatabinding_constructor_args():
    sig = inspect.signature(appBuilderDSL::SimpleDataBinding.__init__)
    params = list(sig.parameters.keys())
    assert "modelAccess" in params, "Missing parameter 'modelAccess'"

def test_appbuilderdsl::simpledatabinding_has_modelAccess():
    assert hasattr(appBuilderDSL::SimpleDataBinding, "modelAccess")
    descriptor = None
    for klass in appBuilderDSL::SimpleDataBinding.__mro__:
        if "modelAccess" in klass.__dict__:
            descriptor = klass.__dict__["modelAccess"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::layout_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::Layout)


def test_appbuilderdsl::layout_constructor_exists():
    assert callable(appBuilderDSL::Layout.__init__)


def test_appbuilderdsl::layout_constructor_args():
    sig = inspect.signature(appBuilderDSL::Layout.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_appbuilderdsl::layout_has_type():
    assert hasattr(appBuilderDSL::Layout, "type")
    descriptor = None
    for klass in appBuilderDSL::Layout.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_setinstructionassignment_is_not_abstract():
    assert not inspect.isabstract(SetInstructionAssignment)


def test_setinstructionassignment_constructor_exists():
    assert callable(SetInstructionAssignment.__init__)


def test_setinstructionassignment_constructor_args():
    sig = inspect.signature(SetInstructionAssignment.__init__)
    params = list(sig.parameters.keys())



def test_appbuilderdsl::dynamicvalue_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::DynamicValue)


def test_appbuilderdsl::dynamicvalue_constructor_exists():
    assert callable(appBuilderDSL::DynamicValue.__init__)


def test_appbuilderdsl::dynamicvalue_constructor_args():
    sig = inspect.signature(appBuilderDSL::DynamicValue.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_appbuilderdsl::dynamicvalue_has_type():
    assert hasattr(appBuilderDSL::DynamicValue, "type")
    descriptor = None
    for klass in appBuilderDSL::DynamicValue.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_appbuilderdsl::dynamicvalue_has_variableName():
    assert hasattr(appBuilderDSL::DynamicValue, "variableName")
    descriptor = None
    for klass in appBuilderDSL::DynamicValue.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::controlvalue_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::ControlValue)


def test_appbuilderdsl::controlvalue_constructor_exists():
    assert callable(appBuilderDSL::ControlValue.__init__)


def test_appbuilderdsl::controlvalue_constructor_args():
    sig = inspect.signature(appBuilderDSL::ControlValue.__init__)
    params = list(sig.parameters.keys())
    assert "controlAccess" in params, "Missing parameter 'controlAccess'"

def test_appbuilderdsl::controlvalue_has_controlAccess():
    assert hasattr(appBuilderDSL::ControlValue, "controlAccess")
    descriptor = None
    for klass in appBuilderDSL::ControlValue.__mro__:
        if "controlAccess" in klass.__dict__:
            descriptor = klass.__dict__["controlAccess"]
            break
    assert isinstance(descriptor, property)



def test_appbuilderdsl::restcall_is_not_abstract():
    assert not inspect.isabstract(appBuilderDSL::RestCall)


def test_appbuilderdsl::restcall_constructor_exists():
    assert callable(appBuilderDSL::RestCall.__init__)


def test_appbuilderdsl::restcall_constructor_args():
    sig = inspect.signature(appBuilderDSL::RestCall.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"

def test_appbuilderdsl::restcall_has_url():
    assert hasattr(appBuilderDSL::RestCall, "url")
    descriptor = None
    for klass in appBuilderDSL::RestCall.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_device_exists():
    # Check that the Enumeration exists
    assert Device is not None

def test_device_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Device]
    expected_literals = [
        "ipad",
        "iphone",
        "android4",
        "android2",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Device"


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
appBuilderDSL::Feature_strategy = st.builds(
    appBuilderDSL::Feature,
    many=
        st.booleans(),
    name=
        safe_text
)
appBuilderDSL::Expression_strategy = st.builds(
    appBuilderDSL::Expression,
    terms=
        safe_text
)
Value_strategy = st.builds(
    Value,
)
appBuilderDSL::Value_strategy = st.builds(
    appBuilderDSL::Value,
)
Type_strategy = st.builds(
    Type,
)
appBuilderDSL::Entity_strategy = st.builds(
    appBuilderDSL::Entity,
)
appBuilderDSL::DataType_strategy = st.builds(
    appBuilderDSL::DataType,
)
appBuilderDSL::Type_strategy = st.builds(
    appBuilderDSL::Type,
    name=
        safe_text
)
appBuilderDSL::Import_strategy = st.builds(
    appBuilderDSL::Import,
    importedNamespace=
        safe_text
)
appBuilderDSL::SetInstructionAssignment_strategy = st.builds(
    appBuilderDSL::SetInstructionAssignment,
)
Instruction_strategy = st.builds(
    Instruction,
)
appBuilderDSL::SetInstruction_strategy = st.builds(
    appBuilderDSL::SetInstruction,
    modelAccess=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
appBuilderDSL::UiAction_strategy = st.builds(
    appBuilderDSL::UiAction,
    name=
        safe_text
)
ConditionExpression_strategy = st.builds(
    ConditionExpression,
)
appBuilderDSL::CompositeConditionExpression_strategy = st.builds(
    appBuilderDSL::CompositeConditionExpression,
)
appBuilderDSL::SimpleConditionExpression_strategy = st.builds(
    appBuilderDSL::SimpleConditionExpression,
    variableName=
        safe_text
)
appBuilderDSL::ConditionExpression_strategy = st.builds(
    appBuilderDSL::ConditionExpression,
)
Layout_strategy = st.builds(
    Layout,
)
appBuilderDSL::RowLayout_strategy = st.builds(
    appBuilderDSL::RowLayout,
)
appBuilderDSL::GridLayout_strategy = st.builds(
    appBuilderDSL::GridLayout,
    columns=
        st.integers()
)
appBuilderDSL::Control_strategy = st.builds(
    appBuilderDSL::Control,
)
appBuilderDSL::Condition_strategy = st.builds(
    appBuilderDSL::Condition,
    name=
        safe_text
)
appBuilderDSL::ExecuteAction_strategy = st.builds(
    appBuilderDSL::ExecuteAction,
)
appBuilderDSL::Navigate_strategy = st.builds(
    appBuilderDSL::Navigate,
    params=
        safe_text
)
appBuilderDSL::ValidationBinding_strategy = st.builds(
    appBuilderDSL::ValidationBinding,
    controlAccess=
        safe_text
)
appBuilderDSL::UiListenerBinding_strategy = st.builds(
    appBuilderDSL::UiListenerBinding,
    controlAccess=
        safe_text
)
appBuilderDSL::DataBinding_strategy = st.builds(
    appBuilderDSL::DataBinding,
    controlAccess=
        safe_text
)
appBuilderDSL::Action_strategy = st.builds(
    appBuilderDSL::Action,
)
appBuilderDSL::Validator_strategy = st.builds(
    appBuilderDSL::Validator,
)
appBuilderDSL::InitAction_strategy = st.builds(
    appBuilderDSL::InitAction,
)
appBuilderDSL::Attribute_strategy = st.builds(
    appBuilderDSL::Attribute,
    name=
        safe_text,
    type=
        safe_text
)
appBuilderDSL::Controller_strategy = st.builds(
    appBuilderDSL::Controller,
)
appBuilderDSL::View_strategy = st.builds(
    appBuilderDSL::View,
)
appBuilderDSL::Model_strategy = st.builds(
    appBuilderDSL::Model,
)
appBuilderDSL::EntryParameters_strategy = st.builds(
    appBuilderDSL::EntryParameters,
)
Screen_strategy = st.builds(
    Screen,
)
appBuilderDSL::CompositeScreen_strategy = st.builds(
    appBuilderDSL::CompositeScreen,
)
appBuilderDSL::SimpleScreen_strategy = st.builds(
    appBuilderDSL::SimpleScreen,
)
appBuilderDSL::Screen_strategy = st.builds(
    appBuilderDSL::Screen,
    name=
        safe_text
)
appBuilderDSL::Main_strategy = st.builds(
    appBuilderDSL::Main,
    appName=
        safe_text,
    appVersion=
        safe_text,
    devices=
        safe_text,
    generalStyle=
        safe_text
)
appBuilderDSL::Instruction_strategy = st.builds(
    appBuilderDSL::Instruction,
)
appBuilderDSL::Service_strategy = st.builds(
    appBuilderDSL::Service,
)
appBuilderDSL::Ui_strategy = st.builds(
    appBuilderDSL::Ui,
)
appBuilderDSL::Business_strategy = st.builds(
    appBuilderDSL::Business,
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
appBuilderDSL::System_strategy = st.builds(
    appBuilderDSL::System,
)
appBuilderDSL::NamespaceDeclation_strategy = st.builds(
    appBuilderDSL::NamespaceDeclation,
)
appBuilderDSL::AbstractElement_strategy = st.builds(
    appBuilderDSL::AbstractElement,
    name=
        safe_text
)
appBuilderDSL::AppBuilder_strategy = st.builds(
    appBuilderDSL::AppBuilder,
)
Service_strategy = st.builds(
    Service,
)
appBuilderDSL::InstanceService_strategy = st.builds(
    appBuilderDSL::InstanceService,
    instanceName=
        safe_text
)
Control_strategy = st.builds(
    Control,
)
appBuilderDSL::Text_strategy = st.builds(
    appBuilderDSL::Text,
    name=
        safe_text
)
appBuilderDSL::List_strategy = st.builds(
    appBuilderDSL::List,
    name=
        safe_text
)
appBuilderDSL::Button_strategy = st.builds(
    appBuilderDSL::Button,
    name=
        safe_text
)
appBuilderDSL::ScreenLayout_strategy = st.builds(
    appBuilderDSL::ScreenLayout,
)
appBuilderDSL::Label_strategy = st.builds(
    appBuilderDSL::Label,
    name=
        safe_text
)
DataBinding_strategy = st.builds(
    DataBinding,
)
appBuilderDSL::EnumDataBinding_strategy = st.builds(
    appBuilderDSL::EnumDataBinding,
    enumClassName=
        safe_text
)
appBuilderDSL::SimpleDataBinding_strategy = st.builds(
    appBuilderDSL::SimpleDataBinding,
    modelAccess=
        safe_text
)
appBuilderDSL::Layout_strategy = st.builds(
    appBuilderDSL::Layout,
    type=
        safe_text
)
SetInstructionAssignment_strategy = st.builds(
    SetInstructionAssignment,
)
appBuilderDSL::DynamicValue_strategy = st.builds(
    appBuilderDSL::DynamicValue,
    type=
        safe_text,
    variableName=
        safe_text
)
appBuilderDSL::ControlValue_strategy = st.builds(
    appBuilderDSL::ControlValue,
    controlAccess=
        safe_text
)
appBuilderDSL::RestCall_strategy = st.builds(
    appBuilderDSL::RestCall,
    url=
        safe_text
)

@given(instance=appBuilderDSL::Feature_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::feature_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Feature)

@given(instance=appBuilderDSL::Feature_strategy)
def test_appbuilderdsl::feature_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=appBuilderDSL::Feature_strategy)
def test_appbuilderdsl::feature_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=appBuilderDSL::Feature_strategy)
def test_appbuilderdsl::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=appBuilderDSL::Feature_strategy)
def test_appbuilderdsl::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=appBuilderDSL::Expression_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::expression_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Expression)

@given(instance=appBuilderDSL::Expression_strategy)
def test_appbuilderdsl::expression_terms_type(instance):
    assert isinstance(instance.terms, str)


@given(instance=appBuilderDSL::Expression_strategy)
def test_appbuilderdsl::expression_terms_setter(instance):
    original = instance.terms
    instance.terms = original
    assert instance.terms == original

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=appBuilderDSL::Value_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::value_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Value)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=appBuilderDSL::Entity_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::entity_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Entity)

@given(instance=appBuilderDSL::DataType_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::datatype_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::DataType)

@given(instance=appBuilderDSL::Type_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::type_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Type)

@given(instance=appBuilderDSL::Type_strategy)
def test_appbuilderdsl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=appBuilderDSL::Type_strategy)
def test_appbuilderdsl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=appBuilderDSL::Import_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::import_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Import)

@given(instance=appBuilderDSL::Import_strategy)
def test_appbuilderdsl::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=appBuilderDSL::Import_strategy)
def test_appbuilderdsl::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=appBuilderDSL::SetInstructionAssignment_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::setinstructionassignment_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::SetInstructionAssignment)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=appBuilderDSL::SetInstruction_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::setinstruction_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::SetInstruction)

@given(instance=appBuilderDSL::SetInstruction_strategy)
def test_appbuilderdsl::setinstruction_modelAccess_type(instance):
    assert isinstance(instance.modelAccess, str)


@given(instance=appBuilderDSL::SetInstruction_strategy)
def test_appbuilderdsl::setinstruction_modelAccess_setter(instance):
    original = instance.modelAccess
    instance.modelAccess = original
    assert instance.modelAccess == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=appBuilderDSL::UiAction_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::uiaction_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::UiAction)

@given(instance=appBuilderDSL::UiAction_strategy)
def test_appbuilderdsl::uiaction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=appBuilderDSL::UiAction_strategy)
def test_appbuilderdsl::uiaction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ConditionExpression_strategy)
@settings(max_examples=50)
def test_conditionexpression_instantiation(instance):
    assert isinstance(instance, ConditionExpression)

@given(instance=appBuilderDSL::CompositeConditionExpression_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::compositeconditionexpression_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::CompositeConditionExpression)

@given(instance=appBuilderDSL::SimpleConditionExpression_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::simpleconditionexpression_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::SimpleConditionExpression)

@given(instance=appBuilderDSL::SimpleConditionExpression_strategy)
def test_appbuilderdsl::simpleconditionexpression_variableName_type(instance):
    assert isinstance(instance.variableName, str)


@given(instance=appBuilderDSL::SimpleConditionExpression_strategy)
def test_appbuilderdsl::simpleconditionexpression_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=appBuilderDSL::ConditionExpression_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::conditionexpression_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::ConditionExpression)

@given(instance=Layout_strategy)
@settings(max_examples=50)
def test_layout_instantiation(instance):
    assert isinstance(instance, Layout)

@given(instance=appBuilderDSL::RowLayout_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::rowlayout_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::RowLayout)

@given(instance=appBuilderDSL::GridLayout_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::gridlayout_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::GridLayout)

@given(instance=appBuilderDSL::GridLayout_strategy)
def test_appbuilderdsl::gridlayout_columns_type(instance):
    assert isinstance(instance.columns, int)


@given(instance=appBuilderDSL::GridLayout_strategy)
def test_appbuilderdsl::gridlayout_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original

@given(instance=appBuilderDSL::Control_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::control_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Control)

@given(instance=appBuilderDSL::Condition_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::condition_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Condition)

@given(instance=appBuilderDSL::Condition_strategy)
def test_appbuilderdsl::condition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=appBuilderDSL::Condition_strategy)
def test_appbuilderdsl::condition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=appBuilderDSL::ExecuteAction_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::executeaction_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::ExecuteAction)

@given(instance=appBuilderDSL::Navigate_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::navigate_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Navigate)

@given(instance=appBuilderDSL::Navigate_strategy)
def test_appbuilderdsl::navigate_params_type(instance):
    assert isinstance(instance.params, str)


@given(instance=appBuilderDSL::Navigate_strategy)
def test_appbuilderdsl::navigate_params_setter(instance):
    original = instance.params
    instance.params = original
    assert instance.params == original

@given(instance=appBuilderDSL::ValidationBinding_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::validationbinding_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::ValidationBinding)

@given(instance=appBuilderDSL::ValidationBinding_strategy)
def test_appbuilderdsl::validationbinding_controlAccess_type(instance):
    assert isinstance(instance.controlAccess, str)


@given(instance=appBuilderDSL::ValidationBinding_strategy)
def test_appbuilderdsl::validationbinding_controlAccess_setter(instance):
    original = instance.controlAccess
    instance.controlAccess = original
    assert instance.controlAccess == original

@given(instance=appBuilderDSL::UiListenerBinding_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::uilistenerbinding_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::UiListenerBinding)

@given(instance=appBuilderDSL::UiListenerBinding_strategy)
def test_appbuilderdsl::uilistenerbinding_controlAccess_type(instance):
    assert isinstance(instance.controlAccess, str)


@given(instance=appBuilderDSL::UiListenerBinding_strategy)
def test_appbuilderdsl::uilistenerbinding_controlAccess_setter(instance):
    original = instance.controlAccess
    instance.controlAccess = original
    assert instance.controlAccess == original

@given(instance=appBuilderDSL::DataBinding_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::databinding_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::DataBinding)

@given(instance=appBuilderDSL::DataBinding_strategy)
def test_appbuilderdsl::databinding_controlAccess_type(instance):
    assert isinstance(instance.controlAccess, str)


@given(instance=appBuilderDSL::DataBinding_strategy)
def test_appbuilderdsl::databinding_controlAccess_setter(instance):
    original = instance.controlAccess
    instance.controlAccess = original
    assert instance.controlAccess == original

@given(instance=appBuilderDSL::Action_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::action_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Action)

@given(instance=appBuilderDSL::Validator_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::validator_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Validator)

@given(instance=appBuilderDSL::InitAction_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::initaction_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::InitAction)

@given(instance=appBuilderDSL::Attribute_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::attribute_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Attribute)

@given(instance=appBuilderDSL::Attribute_strategy)
def test_appbuilderdsl::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=appBuilderDSL::Attribute_strategy)
def test_appbuilderdsl::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=appBuilderDSL::Attribute_strategy)
def test_appbuilderdsl::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=appBuilderDSL::Attribute_strategy)
def test_appbuilderdsl::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=appBuilderDSL::Controller_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::controller_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Controller)

@given(instance=appBuilderDSL::View_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::view_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::View)

@given(instance=appBuilderDSL::Model_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::model_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Model)

@given(instance=appBuilderDSL::EntryParameters_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::entryparameters_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::EntryParameters)

@given(instance=Screen_strategy)
@settings(max_examples=50)
def test_screen_instantiation(instance):
    assert isinstance(instance, Screen)

@given(instance=appBuilderDSL::CompositeScreen_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::compositescreen_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::CompositeScreen)

@given(instance=appBuilderDSL::SimpleScreen_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::simplescreen_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::SimpleScreen)

@given(instance=appBuilderDSL::Screen_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::screen_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Screen)

@given(instance=appBuilderDSL::Screen_strategy)
def test_appbuilderdsl::screen_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=appBuilderDSL::Screen_strategy)
def test_appbuilderdsl::screen_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=appBuilderDSL::Main_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::main_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Main)

@given(instance=appBuilderDSL::Main_strategy)
def test_appbuilderdsl::main_appName_type(instance):
    assert isinstance(instance.appName, str)


@given(instance=appBuilderDSL::Main_strategy)
def test_appbuilderdsl::main_appName_setter(instance):
    original = instance.appName
    instance.appName = original
    assert instance.appName == original

@given(instance=appBuilderDSL::Main_strategy)
def test_appbuilderdsl::main_appVersion_type(instance):
    assert isinstance(instance.appVersion, str)


@given(instance=appBuilderDSL::Main_strategy)
def test_appbuilderdsl::main_appVersion_setter(instance):
    original = instance.appVersion
    instance.appVersion = original
    assert instance.appVersion == original

@given(instance=appBuilderDSL::Main_strategy)
def test_appbuilderdsl::main_devices_type(instance):
    assert isinstance(instance.devices, str)


@given(instance=appBuilderDSL::Main_strategy)
def test_appbuilderdsl::main_devices_setter(instance):
    original = instance.devices
    instance.devices = original
    assert instance.devices == original

@given(instance=appBuilderDSL::Main_strategy)
def test_appbuilderdsl::main_generalStyle_type(instance):
    assert isinstance(instance.generalStyle, str)


@given(instance=appBuilderDSL::Main_strategy)
def test_appbuilderdsl::main_generalStyle_setter(instance):
    original = instance.generalStyle
    instance.generalStyle = original
    assert instance.generalStyle == original

@given(instance=appBuilderDSL::Instruction_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::instruction_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Instruction)

@given(instance=appBuilderDSL::Service_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::service_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Service)

@given(instance=appBuilderDSL::Ui_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::ui_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Ui)

@given(instance=appBuilderDSL::Business_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::business_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Business)

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=appBuilderDSL::System_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::system_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::System)

@given(instance=appBuilderDSL::NamespaceDeclation_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::namespacedeclation_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::NamespaceDeclation)

@given(instance=appBuilderDSL::AbstractElement_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::abstractelement_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::AbstractElement)

@given(instance=appBuilderDSL::AbstractElement_strategy)
def test_appbuilderdsl::abstractelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=appBuilderDSL::AbstractElement_strategy)
def test_appbuilderdsl::abstractelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=appBuilderDSL::AppBuilder_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::appbuilder_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::AppBuilder)

@given(instance=Service_strategy)
@settings(max_examples=50)
def test_service_instantiation(instance):
    assert isinstance(instance, Service)

@given(instance=appBuilderDSL::InstanceService_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::instanceservice_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::InstanceService)

@given(instance=appBuilderDSL::InstanceService_strategy)
def test_appbuilderdsl::instanceservice_instanceName_type(instance):
    assert isinstance(instance.instanceName, str)


@given(instance=appBuilderDSL::InstanceService_strategy)
def test_appbuilderdsl::instanceservice_instanceName_setter(instance):
    original = instance.instanceName
    instance.instanceName = original
    assert instance.instanceName == original

@given(instance=Control_strategy)
@settings(max_examples=50)
def test_control_instantiation(instance):
    assert isinstance(instance, Control)

@given(instance=appBuilderDSL::Text_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::text_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Text)

@given(instance=appBuilderDSL::Text_strategy)
def test_appbuilderdsl::text_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=appBuilderDSL::Text_strategy)
def test_appbuilderdsl::text_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=appBuilderDSL::List_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::list_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::List)

@given(instance=appBuilderDSL::List_strategy)
def test_appbuilderdsl::list_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=appBuilderDSL::List_strategy)
def test_appbuilderdsl::list_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=appBuilderDSL::Button_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::button_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Button)

@given(instance=appBuilderDSL::Button_strategy)
def test_appbuilderdsl::button_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=appBuilderDSL::Button_strategy)
def test_appbuilderdsl::button_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=appBuilderDSL::ScreenLayout_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::screenlayout_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::ScreenLayout)

@given(instance=appBuilderDSL::Label_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::label_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Label)

@given(instance=appBuilderDSL::Label_strategy)
def test_appbuilderdsl::label_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=appBuilderDSL::Label_strategy)
def test_appbuilderdsl::label_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DataBinding_strategy)
@settings(max_examples=50)
def test_databinding_instantiation(instance):
    assert isinstance(instance, DataBinding)

@given(instance=appBuilderDSL::EnumDataBinding_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::enumdatabinding_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::EnumDataBinding)

@given(instance=appBuilderDSL::EnumDataBinding_strategy)
def test_appbuilderdsl::enumdatabinding_enumClassName_type(instance):
    assert isinstance(instance.enumClassName, str)


@given(instance=appBuilderDSL::EnumDataBinding_strategy)
def test_appbuilderdsl::enumdatabinding_enumClassName_setter(instance):
    original = instance.enumClassName
    instance.enumClassName = original
    assert instance.enumClassName == original

@given(instance=appBuilderDSL::SimpleDataBinding_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::simpledatabinding_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::SimpleDataBinding)

@given(instance=appBuilderDSL::SimpleDataBinding_strategy)
def test_appbuilderdsl::simpledatabinding_modelAccess_type(instance):
    assert isinstance(instance.modelAccess, str)


@given(instance=appBuilderDSL::SimpleDataBinding_strategy)
def test_appbuilderdsl::simpledatabinding_modelAccess_setter(instance):
    original = instance.modelAccess
    instance.modelAccess = original
    assert instance.modelAccess == original

@given(instance=appBuilderDSL::Layout_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::layout_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::Layout)

@given(instance=appBuilderDSL::Layout_strategy)
def test_appbuilderdsl::layout_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=appBuilderDSL::Layout_strategy)
def test_appbuilderdsl::layout_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=SetInstructionAssignment_strategy)
@settings(max_examples=50)
def test_setinstructionassignment_instantiation(instance):
    assert isinstance(instance, SetInstructionAssignment)

@given(instance=appBuilderDSL::DynamicValue_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::dynamicvalue_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::DynamicValue)

@given(instance=appBuilderDSL::DynamicValue_strategy)
def test_appbuilderdsl::dynamicvalue_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=appBuilderDSL::DynamicValue_strategy)
def test_appbuilderdsl::dynamicvalue_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=appBuilderDSL::DynamicValue_strategy)
def test_appbuilderdsl::dynamicvalue_variableName_type(instance):
    assert isinstance(instance.variableName, str)


@given(instance=appBuilderDSL::DynamicValue_strategy)
def test_appbuilderdsl::dynamicvalue_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=appBuilderDSL::ControlValue_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::controlvalue_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::ControlValue)

@given(instance=appBuilderDSL::ControlValue_strategy)
def test_appbuilderdsl::controlvalue_controlAccess_type(instance):
    assert isinstance(instance.controlAccess, str)


@given(instance=appBuilderDSL::ControlValue_strategy)
def test_appbuilderdsl::controlvalue_controlAccess_setter(instance):
    original = instance.controlAccess
    instance.controlAccess = original
    assert instance.controlAccess == original

@given(instance=appBuilderDSL::RestCall_strategy)
@settings(max_examples=50)
def test_appbuilderdsl::restcall_instantiation(instance):
    assert isinstance(instance, appBuilderDSL::RestCall)

@given(instance=appBuilderDSL::RestCall_strategy)
def test_appbuilderdsl::restcall_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=appBuilderDSL::RestCall_strategy)
def test_appbuilderdsl::restcall_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

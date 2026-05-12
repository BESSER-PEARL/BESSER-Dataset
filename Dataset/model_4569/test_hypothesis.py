import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    iotdsl_Feature,
    Node,
    iotdsl_Device,
    Capability,
    iotdsl_Sensing,
    iotdsl_Actuating,
    iotdsl_Parameter,
    iotdsl_Value,
    Feature,
    iotdsl_Capability,
    iotdsl_Property,
    Content,
    iotdsl_Type,
    iotdsl_Content,
    iotdsl_EnumLiteral,
    DeclaredType,
    iotdsl_Node,
    iotdsl_Enumeration,
    Type,
    iotdsl_DeclaredType,
    iotdsl_PrimitiveType,
    iotdsl_Import,
    iotdsl_IotModel,
    TimingExpression,
    iotdsl_WithinExpression,
    Value,
    iotdsl_BoolConstant,
    iotdsl_IntConstant,
    iotdsl_StringConstant,
    iotdsl_AfterExpression,
    iotdsl_Delay,
    iotdsl_Reaction,
    iotdsl_Expression,
    iotdsl_Attribute,
    Expression,
    iotdsl_EventOccurrence,
    iotdsl_TimingExpression,
    iotdsl_AndExpression,
    iotdsl_NotExpression,
    iotdsl_CommunicationPath,
    iotdsl_NodeInstance,
    iotdsl_Configuration,
    iotdsl_Rule,
    iotdsl_Gateway,
    Protocol,
    Operator,
    DefaultType,
    Unit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iotdsl_feature_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Feature)


def test_iotdsl_feature_constructor_exists():
    assert callable(iotdsl_Feature.__init__)


def test_iotdsl_feature_constructor_args():
    sig = inspect.signature(iotdsl_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl_feature_has_name():
    assert hasattr(iotdsl_Feature, "name")
    descriptor = None
    for klass in iotdsl_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_device_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Device)


def test_iotdsl_device_constructor_exists():
    assert callable(iotdsl_Device.__init__)


def test_iotdsl_device_constructor_args():
    sig = inspect.signature(iotdsl_Device.__init__)
    params = list(sig.parameters.keys())



def test_capability_is_not_abstract():
    assert not inspect.isabstract(Capability)


def test_capability_constructor_exists():
    assert callable(Capability.__init__)


def test_capability_constructor_args():
    sig = inspect.signature(Capability.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_sensing_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Sensing)


def test_iotdsl_sensing_constructor_exists():
    assert callable(iotdsl_Sensing.__init__)


def test_iotdsl_sensing_constructor_args():
    sig = inspect.signature(iotdsl_Sensing.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_actuating_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Actuating)


def test_iotdsl_actuating_constructor_exists():
    assert callable(iotdsl_Actuating.__init__)


def test_iotdsl_actuating_constructor_args():
    sig = inspect.signature(iotdsl_Actuating.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_parameter_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Parameter)


def test_iotdsl_parameter_constructor_exists():
    assert callable(iotdsl_Parameter.__init__)


def test_iotdsl_parameter_constructor_args():
    sig = inspect.signature(iotdsl_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl_parameter_has_name():
    assert hasattr(iotdsl_Parameter, "name")
    descriptor = None
    for klass in iotdsl_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl_value_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Value)


def test_iotdsl_value_constructor_exists():
    assert callable(iotdsl_Value.__init__)


def test_iotdsl_value_constructor_args():
    sig = inspect.signature(iotdsl_Value.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_capability_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Capability)


def test_iotdsl_capability_constructor_exists():
    assert callable(iotdsl_Capability.__init__)


def test_iotdsl_capability_constructor_args():
    sig = inspect.signature(iotdsl_Capability.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_property_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Property)


def test_iotdsl_property_constructor_exists():
    assert callable(iotdsl_Property.__init__)


def test_iotdsl_property_constructor_args():
    sig = inspect.signature(iotdsl_Property.__init__)
    params = list(sig.parameters.keys())



def test_content_is_not_abstract():
    assert not inspect.isabstract(Content)


def test_content_constructor_exists():
    assert callable(Content.__init__)


def test_content_constructor_args():
    sig = inspect.signature(Content.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_type_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Type)


def test_iotdsl_type_constructor_exists():
    assert callable(iotdsl_Type.__init__)


def test_iotdsl_type_constructor_args():
    sig = inspect.signature(iotdsl_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl_type_has_name():
    assert hasattr(iotdsl_Type, "name")
    descriptor = None
    for klass in iotdsl_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl_content_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Content)


def test_iotdsl_content_constructor_exists():
    assert callable(iotdsl_Content.__init__)


def test_iotdsl_content_constructor_args():
    sig = inspect.signature(iotdsl_Content.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_enumliteral_is_not_abstract():
    assert not inspect.isabstract(iotdsl_EnumLiteral)


def test_iotdsl_enumliteral_constructor_exists():
    assert callable(iotdsl_EnumLiteral.__init__)


def test_iotdsl_enumliteral_constructor_args():
    sig = inspect.signature(iotdsl_EnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl_enumliteral_has_name():
    assert hasattr(iotdsl_EnumLiteral, "name")
    descriptor = None
    for klass in iotdsl_EnumLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_declaredtype_is_not_abstract():
    assert not inspect.isabstract(DeclaredType)


def test_declaredtype_constructor_exists():
    assert callable(DeclaredType.__init__)


def test_declaredtype_constructor_args():
    sig = inspect.signature(DeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_node_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Node)


def test_iotdsl_node_constructor_exists():
    assert callable(iotdsl_Node.__init__)


def test_iotdsl_node_constructor_args():
    sig = inspect.signature(iotdsl_Node.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_enumeration_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Enumeration)


def test_iotdsl_enumeration_constructor_exists():
    assert callable(iotdsl_Enumeration.__init__)


def test_iotdsl_enumeration_constructor_args():
    sig = inspect.signature(iotdsl_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_declaredtype_is_not_abstract():
    assert not inspect.isabstract(iotdsl_DeclaredType)


def test_iotdsl_declaredtype_constructor_exists():
    assert callable(iotdsl_DeclaredType.__init__)


def test_iotdsl_declaredtype_constructor_args():
    sig = inspect.signature(iotdsl_DeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_primitivetype_is_not_abstract():
    assert not inspect.isabstract(iotdsl_PrimitiveType)


def test_iotdsl_primitivetype_constructor_exists():
    assert callable(iotdsl_PrimitiveType.__init__)


def test_iotdsl_primitivetype_constructor_args():
    sig = inspect.signature(iotdsl_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_import_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Import)


def test_iotdsl_import_constructor_exists():
    assert callable(iotdsl_Import.__init__)


def test_iotdsl_import_constructor_args():
    sig = inspect.signature(iotdsl_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_iotdsl_import_has_importedNamespace():
    assert hasattr(iotdsl_Import, "importedNamespace")
    descriptor = None
    for klass in iotdsl_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl_iotmodel_is_not_abstract():
    assert not inspect.isabstract(iotdsl_IotModel)


def test_iotdsl_iotmodel_constructor_exists():
    assert callable(iotdsl_IotModel.__init__)


def test_iotdsl_iotmodel_constructor_args():
    sig = inspect.signature(iotdsl_IotModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl_iotmodel_has_name():
    assert hasattr(iotdsl_IotModel, "name")
    descriptor = None
    for klass in iotdsl_IotModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_timingexpression_is_not_abstract():
    assert not inspect.isabstract(TimingExpression)


def test_timingexpression_constructor_exists():
    assert callable(TimingExpression.__init__)


def test_timingexpression_constructor_args():
    sig = inspect.signature(TimingExpression.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_withinexpression_is_not_abstract():
    assert not inspect.isabstract(iotdsl_WithinExpression)


def test_iotdsl_withinexpression_constructor_exists():
    assert callable(iotdsl_WithinExpression.__init__)


def test_iotdsl_withinexpression_constructor_args():
    sig = inspect.signature(iotdsl_WithinExpression.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_boolconstant_is_not_abstract():
    assert not inspect.isabstract(iotdsl_BoolConstant)


def test_iotdsl_boolconstant_constructor_exists():
    assert callable(iotdsl_BoolConstant.__init__)


def test_iotdsl_boolconstant_constructor_args():
    sig = inspect.signature(iotdsl_BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iotdsl_boolconstant_has_value():
    assert hasattr(iotdsl_BoolConstant, "value")
    descriptor = None
    for klass in iotdsl_BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl_intconstant_is_not_abstract():
    assert not inspect.isabstract(iotdsl_IntConstant)


def test_iotdsl_intconstant_constructor_exists():
    assert callable(iotdsl_IntConstant.__init__)


def test_iotdsl_intconstant_constructor_args():
    sig = inspect.signature(iotdsl_IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iotdsl_intconstant_has_value():
    assert hasattr(iotdsl_IntConstant, "value")
    descriptor = None
    for klass in iotdsl_IntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl_stringconstant_is_not_abstract():
    assert not inspect.isabstract(iotdsl_StringConstant)


def test_iotdsl_stringconstant_constructor_exists():
    assert callable(iotdsl_StringConstant.__init__)


def test_iotdsl_stringconstant_constructor_args():
    sig = inspect.signature(iotdsl_StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iotdsl_stringconstant_has_value():
    assert hasattr(iotdsl_StringConstant, "value")
    descriptor = None
    for klass in iotdsl_StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl_afterexpression_is_not_abstract():
    assert not inspect.isabstract(iotdsl_AfterExpression)


def test_iotdsl_afterexpression_constructor_exists():
    assert callable(iotdsl_AfterExpression.__init__)


def test_iotdsl_afterexpression_constructor_args():
    sig = inspect.signature(iotdsl_AfterExpression.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_delay_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Delay)


def test_iotdsl_delay_constructor_exists():
    assert callable(iotdsl_Delay.__init__)


def test_iotdsl_delay_constructor_args():
    sig = inspect.signature(iotdsl_Delay.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_iotdsl_delay_has_time():
    assert hasattr(iotdsl_Delay, "time")
    descriptor = None
    for klass in iotdsl_Delay.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_iotdsl_delay_has_unit():
    assert hasattr(iotdsl_Delay, "unit")
    descriptor = None
    for klass in iotdsl_Delay.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl_reaction_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Reaction)


def test_iotdsl_reaction_constructor_exists():
    assert callable(iotdsl_Reaction.__init__)


def test_iotdsl_reaction_constructor_args():
    sig = inspect.signature(iotdsl_Reaction.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_expression_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Expression)


def test_iotdsl_expression_constructor_exists():
    assert callable(iotdsl_Expression.__init__)


def test_iotdsl_expression_constructor_args():
    sig = inspect.signature(iotdsl_Expression.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_attribute_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Attribute)


def test_iotdsl_attribute_constructor_exists():
    assert callable(iotdsl_Attribute.__init__)


def test_iotdsl_attribute_constructor_args():
    sig = inspect.signature(iotdsl_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl_attribute_has_name():
    assert hasattr(iotdsl_Attribute, "name")
    descriptor = None
    for klass in iotdsl_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(iotdsl_EventOccurrence)


def test_iotdsl_eventoccurrence_constructor_exists():
    assert callable(iotdsl_EventOccurrence.__init__)


def test_iotdsl_eventoccurrence_constructor_args():
    sig = inspect.signature(iotdsl_EventOccurrence.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_iotdsl_eventoccurrence_has_operator():
    assert hasattr(iotdsl_EventOccurrence, "operator")
    descriptor = None
    for klass in iotdsl_EventOccurrence.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl_timingexpression_is_not_abstract():
    assert not inspect.isabstract(iotdsl_TimingExpression)


def test_iotdsl_timingexpression_constructor_exists():
    assert callable(iotdsl_TimingExpression.__init__)


def test_iotdsl_timingexpression_constructor_args():
    sig = inspect.signature(iotdsl_TimingExpression.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_andexpression_is_not_abstract():
    assert not inspect.isabstract(iotdsl_AndExpression)


def test_iotdsl_andexpression_constructor_exists():
    assert callable(iotdsl_AndExpression.__init__)


def test_iotdsl_andexpression_constructor_args():
    sig = inspect.signature(iotdsl_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_notexpression_is_not_abstract():
    assert not inspect.isabstract(iotdsl_NotExpression)


def test_iotdsl_notexpression_constructor_exists():
    assert callable(iotdsl_NotExpression.__init__)


def test_iotdsl_notexpression_constructor_args():
    sig = inspect.signature(iotdsl_NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl_communicationpath_is_not_abstract():
    assert not inspect.isabstract(iotdsl_CommunicationPath)


def test_iotdsl_communicationpath_constructor_exists():
    assert callable(iotdsl_CommunicationPath.__init__)


def test_iotdsl_communicationpath_constructor_args():
    sig = inspect.signature(iotdsl_CommunicationPath.__init__)
    params = list(sig.parameters.keys())
    assert "protocol" in params, "Missing parameter 'protocol'"

def test_iotdsl_communicationpath_has_protocol():
    assert hasattr(iotdsl_CommunicationPath, "protocol")
    descriptor = None
    for klass in iotdsl_CommunicationPath.__mro__:
        if "protocol" in klass.__dict__:
            descriptor = klass.__dict__["protocol"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl_nodeinstance_is_not_abstract():
    assert not inspect.isabstract(iotdsl_NodeInstance)


def test_iotdsl_nodeinstance_constructor_exists():
    assert callable(iotdsl_NodeInstance.__init__)


def test_iotdsl_nodeinstance_constructor_args():
    sig = inspect.signature(iotdsl_NodeInstance.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl_nodeinstance_has_name():
    assert hasattr(iotdsl_NodeInstance, "name")
    descriptor = None
    for klass in iotdsl_NodeInstance.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl_configuration_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Configuration)


def test_iotdsl_configuration_constructor_exists():
    assert callable(iotdsl_Configuration.__init__)


def test_iotdsl_configuration_constructor_args():
    sig = inspect.signature(iotdsl_Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "confname" in params, "Missing parameter 'confname'"

def test_iotdsl_configuration_has_confname():
    assert hasattr(iotdsl_Configuration, "confname")
    descriptor = None
    for klass in iotdsl_Configuration.__mro__:
        if "confname" in klass.__dict__:
            descriptor = klass.__dict__["confname"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl_rule_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Rule)


def test_iotdsl_rule_constructor_exists():
    assert callable(iotdsl_Rule.__init__)


def test_iotdsl_rule_constructor_args():
    sig = inspect.signature(iotdsl_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl_rule_has_name():
    assert hasattr(iotdsl_Rule, "name")
    descriptor = None
    for klass in iotdsl_Rule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl_gateway_is_not_abstract():
    assert not inspect.isabstract(iotdsl_Gateway)


def test_iotdsl_gateway_constructor_exists():
    assert callable(iotdsl_Gateway.__init__)


def test_iotdsl_gateway_constructor_args():
    sig = inspect.signature(iotdsl_Gateway.__init__)
    params = list(sig.parameters.keys())

def test_protocol_exists():
    # Check that the Enumeration exists
    assert Protocol is not None

def test_protocol_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Protocol]
    expected_literals = [
        "zigbee",
        "mqtt",
        "dds",
        "ip",
        "zwave",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Protocol"

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "equal",
        "lesser",
        "neq",
        "leq",
        "greater",
        "geq",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"

def test_defaulttype_exists():
    # Check that the Enumeration exists
    assert DefaultType is not None

def test_defaulttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DefaultType]
    expected_literals = [
        "Integer",
        "Boolean",
        "Void",
        "Real",
        "String",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DefaultType"

def test_unit_exists():
    # Check that the Enumeration exists
    assert Unit is not None

def test_unit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Unit]
    expected_literals = [
        "hour",
        "milli",
        "min",
        "sec",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Unit"


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
iotdsl_Feature_strategy = st.builds(
    iotdsl_Feature,
    name=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
iotdsl_Device_strategy = st.builds(
    iotdsl_Device,
)
Capability_strategy = st.builds(
    Capability,
)
iotdsl_Sensing_strategy = st.builds(
    iotdsl_Sensing,
)
iotdsl_Actuating_strategy = st.builds(
    iotdsl_Actuating,
)
iotdsl_Parameter_strategy = st.builds(
    iotdsl_Parameter,
    name=
        safe_text
)
iotdsl_Value_strategy = st.builds(
    iotdsl_Value,
)
Feature_strategy = st.builds(
    Feature,
)
iotdsl_Capability_strategy = st.builds(
    iotdsl_Capability,
)
iotdsl_Property_strategy = st.builds(
    iotdsl_Property,
)
Content_strategy = st.builds(
    Content,
)
iotdsl_Type_strategy = st.builds(
    iotdsl_Type,
    name=
        safe_text
)
iotdsl_Content_strategy = st.builds(
    iotdsl_Content,
)
iotdsl_EnumLiteral_strategy = st.builds(
    iotdsl_EnumLiteral,
    name=
        safe_text
)
DeclaredType_strategy = st.builds(
    DeclaredType,
)
iotdsl_Node_strategy = st.builds(
    iotdsl_Node,
)
iotdsl_Enumeration_strategy = st.builds(
    iotdsl_Enumeration,
)
Type_strategy = st.builds(
    Type,
)
iotdsl_DeclaredType_strategy = st.builds(
    iotdsl_DeclaredType,
)
iotdsl_PrimitiveType_strategy = st.builds(
    iotdsl_PrimitiveType,
)
iotdsl_Import_strategy = st.builds(
    iotdsl_Import,
    importedNamespace=
        safe_text
)
iotdsl_IotModel_strategy = st.builds(
    iotdsl_IotModel,
    name=
        safe_text
)
TimingExpression_strategy = st.builds(
    TimingExpression,
)
iotdsl_WithinExpression_strategy = st.builds(
    iotdsl_WithinExpression,
)
Value_strategy = st.builds(
    Value,
)
iotdsl_BoolConstant_strategy = st.builds(
    iotdsl_BoolConstant,
    value=
        safe_text
)
iotdsl_IntConstant_strategy = st.builds(
    iotdsl_IntConstant,
    value=
        st.integers()
)
iotdsl_StringConstant_strategy = st.builds(
    iotdsl_StringConstant,
    value=
        safe_text
)
iotdsl_AfterExpression_strategy = st.builds(
    iotdsl_AfterExpression,
)
iotdsl_Delay_strategy = st.builds(
    iotdsl_Delay,
    time=
        st.integers(),
    unit=
        safe_text
)
iotdsl_Reaction_strategy = st.builds(
    iotdsl_Reaction,
)
iotdsl_Expression_strategy = st.builds(
    iotdsl_Expression,
)
iotdsl_Attribute_strategy = st.builds(
    iotdsl_Attribute,
    name=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
iotdsl_EventOccurrence_strategy = st.builds(
    iotdsl_EventOccurrence,
    operator=
        safe_text
)
iotdsl_TimingExpression_strategy = st.builds(
    iotdsl_TimingExpression,
)
iotdsl_AndExpression_strategy = st.builds(
    iotdsl_AndExpression,
)
iotdsl_NotExpression_strategy = st.builds(
    iotdsl_NotExpression,
)
iotdsl_CommunicationPath_strategy = st.builds(
    iotdsl_CommunicationPath,
    protocol=
        safe_text
)
iotdsl_NodeInstance_strategy = st.builds(
    iotdsl_NodeInstance,
    name=
        safe_text
)
iotdsl_Configuration_strategy = st.builds(
    iotdsl_Configuration,
    confname=
        safe_text
)
iotdsl_Rule_strategy = st.builds(
    iotdsl_Rule,
    name=
        safe_text
)
iotdsl_Gateway_strategy = st.builds(
    iotdsl_Gateway,
)

@given(instance=iotdsl_Feature_strategy)
@settings(max_examples=50)
def test_iotdsl_feature_instantiation(instance):
    assert isinstance(instance, iotdsl_Feature)



@given(instance=iotdsl_Feature_strategy)
def test_iotdsl_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=iotdsl_Device_strategy)
@settings(max_examples=50)
def test_iotdsl_device_instantiation(instance):
    assert isinstance(instance, iotdsl_Device)

@given(instance=Capability_strategy)
@settings(max_examples=50)
def test_capability_instantiation(instance):
    assert isinstance(instance, Capability)

@given(instance=iotdsl_Sensing_strategy)
@settings(max_examples=50)
def test_iotdsl_sensing_instantiation(instance):
    assert isinstance(instance, iotdsl_Sensing)

@given(instance=iotdsl_Actuating_strategy)
@settings(max_examples=50)
def test_iotdsl_actuating_instantiation(instance):
    assert isinstance(instance, iotdsl_Actuating)

@given(instance=iotdsl_Parameter_strategy)
@settings(max_examples=50)
def test_iotdsl_parameter_instantiation(instance):
    assert isinstance(instance, iotdsl_Parameter)



@given(instance=iotdsl_Parameter_strategy)
def test_iotdsl_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iotdsl_Value_strategy)
@settings(max_examples=50)
def test_iotdsl_value_instantiation(instance):
    assert isinstance(instance, iotdsl_Value)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=iotdsl_Capability_strategy)
@settings(max_examples=50)
def test_iotdsl_capability_instantiation(instance):
    assert isinstance(instance, iotdsl_Capability)

@given(instance=iotdsl_Property_strategy)
@settings(max_examples=50)
def test_iotdsl_property_instantiation(instance):
    assert isinstance(instance, iotdsl_Property)

@given(instance=Content_strategy)
@settings(max_examples=50)
def test_content_instantiation(instance):
    assert isinstance(instance, Content)

@given(instance=iotdsl_Type_strategy)
@settings(max_examples=50)
def test_iotdsl_type_instantiation(instance):
    assert isinstance(instance, iotdsl_Type)



@given(instance=iotdsl_Type_strategy)
def test_iotdsl_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iotdsl_Content_strategy)
@settings(max_examples=50)
def test_iotdsl_content_instantiation(instance):
    assert isinstance(instance, iotdsl_Content)

@given(instance=iotdsl_EnumLiteral_strategy)
@settings(max_examples=50)
def test_iotdsl_enumliteral_instantiation(instance):
    assert isinstance(instance, iotdsl_EnumLiteral)



@given(instance=iotdsl_EnumLiteral_strategy)
def test_iotdsl_enumliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DeclaredType_strategy)
@settings(max_examples=50)
def test_declaredtype_instantiation(instance):
    assert isinstance(instance, DeclaredType)

@given(instance=iotdsl_Node_strategy)
@settings(max_examples=50)
def test_iotdsl_node_instantiation(instance):
    assert isinstance(instance, iotdsl_Node)

@given(instance=iotdsl_Enumeration_strategy)
@settings(max_examples=50)
def test_iotdsl_enumeration_instantiation(instance):
    assert isinstance(instance, iotdsl_Enumeration)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=iotdsl_DeclaredType_strategy)
@settings(max_examples=50)
def test_iotdsl_declaredtype_instantiation(instance):
    assert isinstance(instance, iotdsl_DeclaredType)

@given(instance=iotdsl_PrimitiveType_strategy)
@settings(max_examples=50)
def test_iotdsl_primitivetype_instantiation(instance):
    assert isinstance(instance, iotdsl_PrimitiveType)

@given(instance=iotdsl_Import_strategy)
@settings(max_examples=50)
def test_iotdsl_import_instantiation(instance):
    assert isinstance(instance, iotdsl_Import)



@given(instance=iotdsl_Import_strategy)
def test_iotdsl_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=iotdsl_IotModel_strategy)
@settings(max_examples=50)
def test_iotdsl_iotmodel_instantiation(instance):
    assert isinstance(instance, iotdsl_IotModel)



@given(instance=iotdsl_IotModel_strategy)
def test_iotdsl_iotmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TimingExpression_strategy)
@settings(max_examples=50)
def test_timingexpression_instantiation(instance):
    assert isinstance(instance, TimingExpression)

@given(instance=iotdsl_WithinExpression_strategy)
@settings(max_examples=50)
def test_iotdsl_withinexpression_instantiation(instance):
    assert isinstance(instance, iotdsl_WithinExpression)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=iotdsl_BoolConstant_strategy)
@settings(max_examples=50)
def test_iotdsl_boolconstant_instantiation(instance):
    assert isinstance(instance, iotdsl_BoolConstant)



@given(instance=iotdsl_BoolConstant_strategy)
def test_iotdsl_boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iotdsl_IntConstant_strategy)
@settings(max_examples=50)
def test_iotdsl_intconstant_instantiation(instance):
    assert isinstance(instance, iotdsl_IntConstant)



@given(instance=iotdsl_IntConstant_strategy)
def test_iotdsl_intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iotdsl_StringConstant_strategy)
@settings(max_examples=50)
def test_iotdsl_stringconstant_instantiation(instance):
    assert isinstance(instance, iotdsl_StringConstant)



@given(instance=iotdsl_StringConstant_strategy)
def test_iotdsl_stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iotdsl_AfterExpression_strategy)
@settings(max_examples=50)
def test_iotdsl_afterexpression_instantiation(instance):
    assert isinstance(instance, iotdsl_AfterExpression)

@given(instance=iotdsl_Delay_strategy)
@settings(max_examples=50)
def test_iotdsl_delay_instantiation(instance):
    assert isinstance(instance, iotdsl_Delay)



@given(instance=iotdsl_Delay_strategy)
def test_iotdsl_delay_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=iotdsl_Delay_strategy)
def test_iotdsl_delay_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=iotdsl_Reaction_strategy)
@settings(max_examples=50)
def test_iotdsl_reaction_instantiation(instance):
    assert isinstance(instance, iotdsl_Reaction)

@given(instance=iotdsl_Expression_strategy)
@settings(max_examples=50)
def test_iotdsl_expression_instantiation(instance):
    assert isinstance(instance, iotdsl_Expression)

@given(instance=iotdsl_Attribute_strategy)
@settings(max_examples=50)
def test_iotdsl_attribute_instantiation(instance):
    assert isinstance(instance, iotdsl_Attribute)



@given(instance=iotdsl_Attribute_strategy)
def test_iotdsl_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=iotdsl_EventOccurrence_strategy)
@settings(max_examples=50)
def test_iotdsl_eventoccurrence_instantiation(instance):
    assert isinstance(instance, iotdsl_EventOccurrence)



@given(instance=iotdsl_EventOccurrence_strategy)
def test_iotdsl_eventoccurrence_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=iotdsl_TimingExpression_strategy)
@settings(max_examples=50)
def test_iotdsl_timingexpression_instantiation(instance):
    assert isinstance(instance, iotdsl_TimingExpression)

@given(instance=iotdsl_AndExpression_strategy)
@settings(max_examples=50)
def test_iotdsl_andexpression_instantiation(instance):
    assert isinstance(instance, iotdsl_AndExpression)

@given(instance=iotdsl_NotExpression_strategy)
@settings(max_examples=50)
def test_iotdsl_notexpression_instantiation(instance):
    assert isinstance(instance, iotdsl_NotExpression)

@given(instance=iotdsl_CommunicationPath_strategy)
@settings(max_examples=50)
def test_iotdsl_communicationpath_instantiation(instance):
    assert isinstance(instance, iotdsl_CommunicationPath)



@given(instance=iotdsl_CommunicationPath_strategy)
def test_iotdsl_communicationpath_protocol_setter(instance):
    original = instance.protocol
    instance.protocol = original
    assert instance.protocol == original

@given(instance=iotdsl_NodeInstance_strategy)
@settings(max_examples=50)
def test_iotdsl_nodeinstance_instantiation(instance):
    assert isinstance(instance, iotdsl_NodeInstance)



@given(instance=iotdsl_NodeInstance_strategy)
def test_iotdsl_nodeinstance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iotdsl_Configuration_strategy)
@settings(max_examples=50)
def test_iotdsl_configuration_instantiation(instance):
    assert isinstance(instance, iotdsl_Configuration)



@given(instance=iotdsl_Configuration_strategy)
def test_iotdsl_configuration_confname_setter(instance):
    original = instance.confname
    instance.confname = original
    assert instance.confname == original

@given(instance=iotdsl_Rule_strategy)
@settings(max_examples=50)
def test_iotdsl_rule_instantiation(instance):
    assert isinstance(instance, iotdsl_Rule)



@given(instance=iotdsl_Rule_strategy)
def test_iotdsl_rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iotdsl_Gateway_strategy)
@settings(max_examples=50)
def test_iotdsl_gateway_instantiation(instance):
    assert isinstance(instance, iotdsl_Gateway)

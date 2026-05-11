import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TimingExpression,
    iotdsl::WithinExpression,
    Value,
    iotdsl::BoolConstant,
    iotdsl::IntConstant,
    iotdsl::StringConstant,
    iotdsl::AfterExpression,
    iotdsl::Delay,
    iotdsl::Reaction,
    iotdsl::Expression,
    iotdsl::Attribute,
    Expression,
    iotdsl::TimingExpression,
    iotdsl::EventOccurrence,
    iotdsl::AndExpression,
    iotdsl::NotExpression,
    iotdsl::CommunicationPath,
    iotdsl::NodeInstance,
    iotdsl::Feature,
    Node,
    iotdsl::Gateway,
    iotdsl::Device,
    Capability,
    iotdsl::Sensing,
    iotdsl::Actuating,
    iotdsl::Parameter,
    iotdsl::Value,
    Feature,
    iotdsl::Capability,
    iotdsl::Property,
    Content,
    iotdsl::Configuration,
    iotdsl::Rule,
    iotdsl::Type,
    iotdsl::Content,
    iotdsl::EnumLiteral,
    DeclaredType,
    iotdsl::Node,
    iotdsl::Enumeration,
    Type,
    iotdsl::DeclaredType,
    iotdsl::PrimitiveType,
    iotdsl::Import,
    iotdsl::IotModel,
    Protocol,
    DefaultType,
    Operator,
    Unit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_timingexpression_is_not_abstract():
    assert not inspect.isabstract(TimingExpression)


def test_timingexpression_constructor_exists():
    assert callable(TimingExpression.__init__)


def test_timingexpression_constructor_args():
    sig = inspect.signature(TimingExpression.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::withinexpression_is_not_abstract():
    assert not inspect.isabstract(iotdsl::WithinExpression)


def test_iotdsl::withinexpression_constructor_exists():
    assert callable(iotdsl::WithinExpression.__init__)


def test_iotdsl::withinexpression_constructor_args():
    sig = inspect.signature(iotdsl::WithinExpression.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::boolconstant_is_not_abstract():
    assert not inspect.isabstract(iotdsl::BoolConstant)


def test_iotdsl::boolconstant_constructor_exists():
    assert callable(iotdsl::BoolConstant.__init__)


def test_iotdsl::boolconstant_constructor_args():
    sig = inspect.signature(iotdsl::BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iotdsl::boolconstant_has_value():
    assert hasattr(iotdsl::BoolConstant, "value")
    descriptor = None
    for klass in iotdsl::BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::intconstant_is_not_abstract():
    assert not inspect.isabstract(iotdsl::IntConstant)


def test_iotdsl::intconstant_constructor_exists():
    assert callable(iotdsl::IntConstant.__init__)


def test_iotdsl::intconstant_constructor_args():
    sig = inspect.signature(iotdsl::IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iotdsl::intconstant_has_value():
    assert hasattr(iotdsl::IntConstant, "value")
    descriptor = None
    for klass in iotdsl::IntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::stringconstant_is_not_abstract():
    assert not inspect.isabstract(iotdsl::StringConstant)


def test_iotdsl::stringconstant_constructor_exists():
    assert callable(iotdsl::StringConstant.__init__)


def test_iotdsl::stringconstant_constructor_args():
    sig = inspect.signature(iotdsl::StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iotdsl::stringconstant_has_value():
    assert hasattr(iotdsl::StringConstant, "value")
    descriptor = None
    for klass in iotdsl::StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::afterexpression_is_not_abstract():
    assert not inspect.isabstract(iotdsl::AfterExpression)


def test_iotdsl::afterexpression_constructor_exists():
    assert callable(iotdsl::AfterExpression.__init__)


def test_iotdsl::afterexpression_constructor_args():
    sig = inspect.signature(iotdsl::AfterExpression.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::delay_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Delay)


def test_iotdsl::delay_constructor_exists():
    assert callable(iotdsl::Delay.__init__)


def test_iotdsl::delay_constructor_args():
    sig = inspect.signature(iotdsl::Delay.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_iotdsl::delay_has_time():
    assert hasattr(iotdsl::Delay, "time")
    descriptor = None
    for klass in iotdsl::Delay.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_iotdsl::delay_has_unit():
    assert hasattr(iotdsl::Delay, "unit")
    descriptor = None
    for klass in iotdsl::Delay.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::reaction_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Reaction)


def test_iotdsl::reaction_constructor_exists():
    assert callable(iotdsl::Reaction.__init__)


def test_iotdsl::reaction_constructor_args():
    sig = inspect.signature(iotdsl::Reaction.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::expression_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Expression)


def test_iotdsl::expression_constructor_exists():
    assert callable(iotdsl::Expression.__init__)


def test_iotdsl::expression_constructor_args():
    sig = inspect.signature(iotdsl::Expression.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::attribute_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Attribute)


def test_iotdsl::attribute_constructor_exists():
    assert callable(iotdsl::Attribute.__init__)


def test_iotdsl::attribute_constructor_args():
    sig = inspect.signature(iotdsl::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl::attribute_has_name():
    assert hasattr(iotdsl::Attribute, "name")
    descriptor = None
    for klass in iotdsl::Attribute.__mro__:
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



def test_iotdsl::timingexpression_is_not_abstract():
    assert not inspect.isabstract(iotdsl::TimingExpression)


def test_iotdsl::timingexpression_constructor_exists():
    assert callable(iotdsl::TimingExpression.__init__)


def test_iotdsl::timingexpression_constructor_args():
    sig = inspect.signature(iotdsl::TimingExpression.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(iotdsl::EventOccurrence)


def test_iotdsl::eventoccurrence_constructor_exists():
    assert callable(iotdsl::EventOccurrence.__init__)


def test_iotdsl::eventoccurrence_constructor_args():
    sig = inspect.signature(iotdsl::EventOccurrence.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_iotdsl::eventoccurrence_has_operator():
    assert hasattr(iotdsl::EventOccurrence, "operator")
    descriptor = None
    for klass in iotdsl::EventOccurrence.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::andexpression_is_not_abstract():
    assert not inspect.isabstract(iotdsl::AndExpression)


def test_iotdsl::andexpression_constructor_exists():
    assert callable(iotdsl::AndExpression.__init__)


def test_iotdsl::andexpression_constructor_args():
    sig = inspect.signature(iotdsl::AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::notexpression_is_not_abstract():
    assert not inspect.isabstract(iotdsl::NotExpression)


def test_iotdsl::notexpression_constructor_exists():
    assert callable(iotdsl::NotExpression.__init__)


def test_iotdsl::notexpression_constructor_args():
    sig = inspect.signature(iotdsl::NotExpression.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::communicationpath_is_not_abstract():
    assert not inspect.isabstract(iotdsl::CommunicationPath)


def test_iotdsl::communicationpath_constructor_exists():
    assert callable(iotdsl::CommunicationPath.__init__)


def test_iotdsl::communicationpath_constructor_args():
    sig = inspect.signature(iotdsl::CommunicationPath.__init__)
    params = list(sig.parameters.keys())
    assert "protocol" in params, "Missing parameter 'protocol'"

def test_iotdsl::communicationpath_has_protocol():
    assert hasattr(iotdsl::CommunicationPath, "protocol")
    descriptor = None
    for klass in iotdsl::CommunicationPath.__mro__:
        if "protocol" in klass.__dict__:
            descriptor = klass.__dict__["protocol"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::nodeinstance_is_not_abstract():
    assert not inspect.isabstract(iotdsl::NodeInstance)


def test_iotdsl::nodeinstance_constructor_exists():
    assert callable(iotdsl::NodeInstance.__init__)


def test_iotdsl::nodeinstance_constructor_args():
    sig = inspect.signature(iotdsl::NodeInstance.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl::nodeinstance_has_name():
    assert hasattr(iotdsl::NodeInstance, "name")
    descriptor = None
    for klass in iotdsl::NodeInstance.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::feature_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Feature)


def test_iotdsl::feature_constructor_exists():
    assert callable(iotdsl::Feature.__init__)


def test_iotdsl::feature_constructor_args():
    sig = inspect.signature(iotdsl::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl::feature_has_name():
    assert hasattr(iotdsl::Feature, "name")
    descriptor = None
    for klass in iotdsl::Feature.__mro__:
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



def test_iotdsl::gateway_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Gateway)


def test_iotdsl::gateway_constructor_exists():
    assert callable(iotdsl::Gateway.__init__)


def test_iotdsl::gateway_constructor_args():
    sig = inspect.signature(iotdsl::Gateway.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::device_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Device)


def test_iotdsl::device_constructor_exists():
    assert callable(iotdsl::Device.__init__)


def test_iotdsl::device_constructor_args():
    sig = inspect.signature(iotdsl::Device.__init__)
    params = list(sig.parameters.keys())



def test_capability_is_not_abstract():
    assert not inspect.isabstract(Capability)


def test_capability_constructor_exists():
    assert callable(Capability.__init__)


def test_capability_constructor_args():
    sig = inspect.signature(Capability.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::sensing_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Sensing)


def test_iotdsl::sensing_constructor_exists():
    assert callable(iotdsl::Sensing.__init__)


def test_iotdsl::sensing_constructor_args():
    sig = inspect.signature(iotdsl::Sensing.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::actuating_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Actuating)


def test_iotdsl::actuating_constructor_exists():
    assert callable(iotdsl::Actuating.__init__)


def test_iotdsl::actuating_constructor_args():
    sig = inspect.signature(iotdsl::Actuating.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::parameter_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Parameter)


def test_iotdsl::parameter_constructor_exists():
    assert callable(iotdsl::Parameter.__init__)


def test_iotdsl::parameter_constructor_args():
    sig = inspect.signature(iotdsl::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl::parameter_has_name():
    assert hasattr(iotdsl::Parameter, "name")
    descriptor = None
    for klass in iotdsl::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::value_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Value)


def test_iotdsl::value_constructor_exists():
    assert callable(iotdsl::Value.__init__)


def test_iotdsl::value_constructor_args():
    sig = inspect.signature(iotdsl::Value.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::capability_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Capability)


def test_iotdsl::capability_constructor_exists():
    assert callable(iotdsl::Capability.__init__)


def test_iotdsl::capability_constructor_args():
    sig = inspect.signature(iotdsl::Capability.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::property_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Property)


def test_iotdsl::property_constructor_exists():
    assert callable(iotdsl::Property.__init__)


def test_iotdsl::property_constructor_args():
    sig = inspect.signature(iotdsl::Property.__init__)
    params = list(sig.parameters.keys())



def test_content_is_not_abstract():
    assert not inspect.isabstract(Content)


def test_content_constructor_exists():
    assert callable(Content.__init__)


def test_content_constructor_args():
    sig = inspect.signature(Content.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::configuration_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Configuration)


def test_iotdsl::configuration_constructor_exists():
    assert callable(iotdsl::Configuration.__init__)


def test_iotdsl::configuration_constructor_args():
    sig = inspect.signature(iotdsl::Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "confname" in params, "Missing parameter 'confname'"

def test_iotdsl::configuration_has_confname():
    assert hasattr(iotdsl::Configuration, "confname")
    descriptor = None
    for klass in iotdsl::Configuration.__mro__:
        if "confname" in klass.__dict__:
            descriptor = klass.__dict__["confname"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::rule_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Rule)


def test_iotdsl::rule_constructor_exists():
    assert callable(iotdsl::Rule.__init__)


def test_iotdsl::rule_constructor_args():
    sig = inspect.signature(iotdsl::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl::rule_has_name():
    assert hasattr(iotdsl::Rule, "name")
    descriptor = None
    for klass in iotdsl::Rule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::type_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Type)


def test_iotdsl::type_constructor_exists():
    assert callable(iotdsl::Type.__init__)


def test_iotdsl::type_constructor_args():
    sig = inspect.signature(iotdsl::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl::type_has_name():
    assert hasattr(iotdsl::Type, "name")
    descriptor = None
    for klass in iotdsl::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::content_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Content)


def test_iotdsl::content_constructor_exists():
    assert callable(iotdsl::Content.__init__)


def test_iotdsl::content_constructor_args():
    sig = inspect.signature(iotdsl::Content.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::enumliteral_is_not_abstract():
    assert not inspect.isabstract(iotdsl::EnumLiteral)


def test_iotdsl::enumliteral_constructor_exists():
    assert callable(iotdsl::EnumLiteral.__init__)


def test_iotdsl::enumliteral_constructor_args():
    sig = inspect.signature(iotdsl::EnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl::enumliteral_has_name():
    assert hasattr(iotdsl::EnumLiteral, "name")
    descriptor = None
    for klass in iotdsl::EnumLiteral.__mro__:
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



def test_iotdsl::node_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Node)


def test_iotdsl::node_constructor_exists():
    assert callable(iotdsl::Node.__init__)


def test_iotdsl::node_constructor_args():
    sig = inspect.signature(iotdsl::Node.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::enumeration_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Enumeration)


def test_iotdsl::enumeration_constructor_exists():
    assert callable(iotdsl::Enumeration.__init__)


def test_iotdsl::enumeration_constructor_args():
    sig = inspect.signature(iotdsl::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::declaredtype_is_not_abstract():
    assert not inspect.isabstract(iotdsl::DeclaredType)


def test_iotdsl::declaredtype_constructor_exists():
    assert callable(iotdsl::DeclaredType.__init__)


def test_iotdsl::declaredtype_constructor_args():
    sig = inspect.signature(iotdsl::DeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::primitivetype_is_not_abstract():
    assert not inspect.isabstract(iotdsl::PrimitiveType)


def test_iotdsl::primitivetype_constructor_exists():
    assert callable(iotdsl::PrimitiveType.__init__)


def test_iotdsl::primitivetype_constructor_args():
    sig = inspect.signature(iotdsl::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::import_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Import)


def test_iotdsl::import_constructor_exists():
    assert callable(iotdsl::Import.__init__)


def test_iotdsl::import_constructor_args():
    sig = inspect.signature(iotdsl::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_iotdsl::import_has_importedNamespace():
    assert hasattr(iotdsl::Import, "importedNamespace")
    descriptor = None
    for klass in iotdsl::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::iotmodel_is_not_abstract():
    assert not inspect.isabstract(iotdsl::IotModel)


def test_iotdsl::iotmodel_constructor_exists():
    assert callable(iotdsl::IotModel.__init__)


def test_iotdsl::iotmodel_constructor_args():
    sig = inspect.signature(iotdsl::IotModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl::iotmodel_has_name():
    assert hasattr(iotdsl::IotModel, "name")
    descriptor = None
    for klass in iotdsl::IotModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_protocol_exists():
    # Check that the Enumeration exists
    assert Protocol is not None

def test_protocol_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Protocol]
    expected_literals = [
        "ip",
        "zwave",
        "dds",
        "mqtt",
        "zigbee",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Protocol"

def test_defaulttype_exists():
    # Check that the Enumeration exists
    assert DefaultType is not None

def test_defaulttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DefaultType]
    expected_literals = [
        "Void",
        "Integer",
        "Boolean",
        "Real",
        "String",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DefaultType"

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "equal",
        "lesser",
        "leq",
        "neq",
        "geq",
        "greater",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"

def test_unit_exists():
    # Check that the Enumeration exists
    assert Unit is not None

def test_unit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Unit]
    expected_literals = [
        "sec",
        "milli",
        "min",
        "hour",
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
TimingExpression_strategy = st.builds(
    TimingExpression,
)
iotdsl::WithinExpression_strategy = st.builds(
    iotdsl::WithinExpression,
)
Value_strategy = st.builds(
    Value,
)
iotdsl::BoolConstant_strategy = st.builds(
    iotdsl::BoolConstant,
    value=
        safe_text
)
iotdsl::IntConstant_strategy = st.builds(
    iotdsl::IntConstant,
    value=
        st.integers()
)
iotdsl::StringConstant_strategy = st.builds(
    iotdsl::StringConstant,
    value=
        safe_text
)
iotdsl::AfterExpression_strategy = st.builds(
    iotdsl::AfterExpression,
)
iotdsl::Delay_strategy = st.builds(
    iotdsl::Delay,
    time=
        st.integers(),
    unit=
        safe_text
)
iotdsl::Reaction_strategy = st.builds(
    iotdsl::Reaction,
)
iotdsl::Expression_strategy = st.builds(
    iotdsl::Expression,
)
iotdsl::Attribute_strategy = st.builds(
    iotdsl::Attribute,
    name=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
iotdsl::TimingExpression_strategy = st.builds(
    iotdsl::TimingExpression,
)
iotdsl::EventOccurrence_strategy = st.builds(
    iotdsl::EventOccurrence,
    operator=
        safe_text
)
iotdsl::AndExpression_strategy = st.builds(
    iotdsl::AndExpression,
)
iotdsl::NotExpression_strategy = st.builds(
    iotdsl::NotExpression,
)
iotdsl::CommunicationPath_strategy = st.builds(
    iotdsl::CommunicationPath,
    protocol=
        safe_text
)
iotdsl::NodeInstance_strategy = st.builds(
    iotdsl::NodeInstance,
    name=
        safe_text
)
iotdsl::Feature_strategy = st.builds(
    iotdsl::Feature,
    name=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
iotdsl::Gateway_strategy = st.builds(
    iotdsl::Gateway,
)
iotdsl::Device_strategy = st.builds(
    iotdsl::Device,
)
Capability_strategy = st.builds(
    Capability,
)
iotdsl::Sensing_strategy = st.builds(
    iotdsl::Sensing,
)
iotdsl::Actuating_strategy = st.builds(
    iotdsl::Actuating,
)
iotdsl::Parameter_strategy = st.builds(
    iotdsl::Parameter,
    name=
        safe_text
)
iotdsl::Value_strategy = st.builds(
    iotdsl::Value,
)
Feature_strategy = st.builds(
    Feature,
)
iotdsl::Capability_strategy = st.builds(
    iotdsl::Capability,
)
iotdsl::Property_strategy = st.builds(
    iotdsl::Property,
)
Content_strategy = st.builds(
    Content,
)
iotdsl::Configuration_strategy = st.builds(
    iotdsl::Configuration,
    confname=
        safe_text
)
iotdsl::Rule_strategy = st.builds(
    iotdsl::Rule,
    name=
        safe_text
)
iotdsl::Type_strategy = st.builds(
    iotdsl::Type,
    name=
        safe_text
)
iotdsl::Content_strategy = st.builds(
    iotdsl::Content,
)
iotdsl::EnumLiteral_strategy = st.builds(
    iotdsl::EnumLiteral,
    name=
        safe_text
)
DeclaredType_strategy = st.builds(
    DeclaredType,
)
iotdsl::Node_strategy = st.builds(
    iotdsl::Node,
)
iotdsl::Enumeration_strategy = st.builds(
    iotdsl::Enumeration,
)
Type_strategy = st.builds(
    Type,
)
iotdsl::DeclaredType_strategy = st.builds(
    iotdsl::DeclaredType,
)
iotdsl::PrimitiveType_strategy = st.builds(
    iotdsl::PrimitiveType,
)
iotdsl::Import_strategy = st.builds(
    iotdsl::Import,
    importedNamespace=
        safe_text
)
iotdsl::IotModel_strategy = st.builds(
    iotdsl::IotModel,
    name=
        safe_text
)

@given(instance=TimingExpression_strategy)
@settings(max_examples=50)
def test_timingexpression_instantiation(instance):
    assert isinstance(instance, TimingExpression)

@given(instance=iotdsl::WithinExpression_strategy)
@settings(max_examples=50)
def test_iotdsl::withinexpression_instantiation(instance):
    assert isinstance(instance, iotdsl::WithinExpression)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=iotdsl::BoolConstant_strategy)
@settings(max_examples=50)
def test_iotdsl::boolconstant_instantiation(instance):
    assert isinstance(instance, iotdsl::BoolConstant)

@given(instance=iotdsl::BoolConstant_strategy)
def test_iotdsl::boolconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=iotdsl::BoolConstant_strategy)
def test_iotdsl::boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iotdsl::IntConstant_strategy)
@settings(max_examples=50)
def test_iotdsl::intconstant_instantiation(instance):
    assert isinstance(instance, iotdsl::IntConstant)

@given(instance=iotdsl::IntConstant_strategy)
def test_iotdsl::intconstant_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=iotdsl::IntConstant_strategy)
def test_iotdsl::intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iotdsl::StringConstant_strategy)
@settings(max_examples=50)
def test_iotdsl::stringconstant_instantiation(instance):
    assert isinstance(instance, iotdsl::StringConstant)

@given(instance=iotdsl::StringConstant_strategy)
def test_iotdsl::stringconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=iotdsl::StringConstant_strategy)
def test_iotdsl::stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iotdsl::AfterExpression_strategy)
@settings(max_examples=50)
def test_iotdsl::afterexpression_instantiation(instance):
    assert isinstance(instance, iotdsl::AfterExpression)

@given(instance=iotdsl::Delay_strategy)
@settings(max_examples=50)
def test_iotdsl::delay_instantiation(instance):
    assert isinstance(instance, iotdsl::Delay)

@given(instance=iotdsl::Delay_strategy)
def test_iotdsl::delay_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=iotdsl::Delay_strategy)
def test_iotdsl::delay_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=iotdsl::Delay_strategy)
def test_iotdsl::delay_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=iotdsl::Delay_strategy)
def test_iotdsl::delay_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=iotdsl::Reaction_strategy)
@settings(max_examples=50)
def test_iotdsl::reaction_instantiation(instance):
    assert isinstance(instance, iotdsl::Reaction)

@given(instance=iotdsl::Expression_strategy)
@settings(max_examples=50)
def test_iotdsl::expression_instantiation(instance):
    assert isinstance(instance, iotdsl::Expression)

@given(instance=iotdsl::Attribute_strategy)
@settings(max_examples=50)
def test_iotdsl::attribute_instantiation(instance):
    assert isinstance(instance, iotdsl::Attribute)

@given(instance=iotdsl::Attribute_strategy)
def test_iotdsl::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iotdsl::Attribute_strategy)
def test_iotdsl::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=iotdsl::TimingExpression_strategy)
@settings(max_examples=50)
def test_iotdsl::timingexpression_instantiation(instance):
    assert isinstance(instance, iotdsl::TimingExpression)

@given(instance=iotdsl::EventOccurrence_strategy)
@settings(max_examples=50)
def test_iotdsl::eventoccurrence_instantiation(instance):
    assert isinstance(instance, iotdsl::EventOccurrence)

@given(instance=iotdsl::EventOccurrence_strategy)
def test_iotdsl::eventoccurrence_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=iotdsl::EventOccurrence_strategy)
def test_iotdsl::eventoccurrence_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=iotdsl::AndExpression_strategy)
@settings(max_examples=50)
def test_iotdsl::andexpression_instantiation(instance):
    assert isinstance(instance, iotdsl::AndExpression)

@given(instance=iotdsl::NotExpression_strategy)
@settings(max_examples=50)
def test_iotdsl::notexpression_instantiation(instance):
    assert isinstance(instance, iotdsl::NotExpression)

@given(instance=iotdsl::CommunicationPath_strategy)
@settings(max_examples=50)
def test_iotdsl::communicationpath_instantiation(instance):
    assert isinstance(instance, iotdsl::CommunicationPath)

@given(instance=iotdsl::CommunicationPath_strategy)
def test_iotdsl::communicationpath_protocol_type(instance):
    assert isinstance(instance.protocol, str)


@given(instance=iotdsl::CommunicationPath_strategy)
def test_iotdsl::communicationpath_protocol_setter(instance):
    original = instance.protocol
    instance.protocol = original
    assert instance.protocol == original

@given(instance=iotdsl::NodeInstance_strategy)
@settings(max_examples=50)
def test_iotdsl::nodeinstance_instantiation(instance):
    assert isinstance(instance, iotdsl::NodeInstance)

@given(instance=iotdsl::NodeInstance_strategy)
def test_iotdsl::nodeinstance_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iotdsl::NodeInstance_strategy)
def test_iotdsl::nodeinstance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iotdsl::Feature_strategy)
@settings(max_examples=50)
def test_iotdsl::feature_instantiation(instance):
    assert isinstance(instance, iotdsl::Feature)

@given(instance=iotdsl::Feature_strategy)
def test_iotdsl::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iotdsl::Feature_strategy)
def test_iotdsl::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=iotdsl::Gateway_strategy)
@settings(max_examples=50)
def test_iotdsl::gateway_instantiation(instance):
    assert isinstance(instance, iotdsl::Gateway)

@given(instance=iotdsl::Device_strategy)
@settings(max_examples=50)
def test_iotdsl::device_instantiation(instance):
    assert isinstance(instance, iotdsl::Device)

@given(instance=Capability_strategy)
@settings(max_examples=50)
def test_capability_instantiation(instance):
    assert isinstance(instance, Capability)

@given(instance=iotdsl::Sensing_strategy)
@settings(max_examples=50)
def test_iotdsl::sensing_instantiation(instance):
    assert isinstance(instance, iotdsl::Sensing)

@given(instance=iotdsl::Actuating_strategy)
@settings(max_examples=50)
def test_iotdsl::actuating_instantiation(instance):
    assert isinstance(instance, iotdsl::Actuating)

@given(instance=iotdsl::Parameter_strategy)
@settings(max_examples=50)
def test_iotdsl::parameter_instantiation(instance):
    assert isinstance(instance, iotdsl::Parameter)

@given(instance=iotdsl::Parameter_strategy)
def test_iotdsl::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iotdsl::Parameter_strategy)
def test_iotdsl::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iotdsl::Value_strategy)
@settings(max_examples=50)
def test_iotdsl::value_instantiation(instance):
    assert isinstance(instance, iotdsl::Value)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=iotdsl::Capability_strategy)
@settings(max_examples=50)
def test_iotdsl::capability_instantiation(instance):
    assert isinstance(instance, iotdsl::Capability)

@given(instance=iotdsl::Property_strategy)
@settings(max_examples=50)
def test_iotdsl::property_instantiation(instance):
    assert isinstance(instance, iotdsl::Property)

@given(instance=Content_strategy)
@settings(max_examples=50)
def test_content_instantiation(instance):
    assert isinstance(instance, Content)

@given(instance=iotdsl::Configuration_strategy)
@settings(max_examples=50)
def test_iotdsl::configuration_instantiation(instance):
    assert isinstance(instance, iotdsl::Configuration)

@given(instance=iotdsl::Configuration_strategy)
def test_iotdsl::configuration_confname_type(instance):
    assert isinstance(instance.confname, str)


@given(instance=iotdsl::Configuration_strategy)
def test_iotdsl::configuration_confname_setter(instance):
    original = instance.confname
    instance.confname = original
    assert instance.confname == original

@given(instance=iotdsl::Rule_strategy)
@settings(max_examples=50)
def test_iotdsl::rule_instantiation(instance):
    assert isinstance(instance, iotdsl::Rule)

@given(instance=iotdsl::Rule_strategy)
def test_iotdsl::rule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iotdsl::Rule_strategy)
def test_iotdsl::rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iotdsl::Type_strategy)
@settings(max_examples=50)
def test_iotdsl::type_instantiation(instance):
    assert isinstance(instance, iotdsl::Type)

@given(instance=iotdsl::Type_strategy)
def test_iotdsl::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iotdsl::Type_strategy)
def test_iotdsl::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iotdsl::Content_strategy)
@settings(max_examples=50)
def test_iotdsl::content_instantiation(instance):
    assert isinstance(instance, iotdsl::Content)

@given(instance=iotdsl::EnumLiteral_strategy)
@settings(max_examples=50)
def test_iotdsl::enumliteral_instantiation(instance):
    assert isinstance(instance, iotdsl::EnumLiteral)

@given(instance=iotdsl::EnumLiteral_strategy)
def test_iotdsl::enumliteral_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iotdsl::EnumLiteral_strategy)
def test_iotdsl::enumliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DeclaredType_strategy)
@settings(max_examples=50)
def test_declaredtype_instantiation(instance):
    assert isinstance(instance, DeclaredType)

@given(instance=iotdsl::Node_strategy)
@settings(max_examples=50)
def test_iotdsl::node_instantiation(instance):
    assert isinstance(instance, iotdsl::Node)

@given(instance=iotdsl::Enumeration_strategy)
@settings(max_examples=50)
def test_iotdsl::enumeration_instantiation(instance):
    assert isinstance(instance, iotdsl::Enumeration)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=iotdsl::DeclaredType_strategy)
@settings(max_examples=50)
def test_iotdsl::declaredtype_instantiation(instance):
    assert isinstance(instance, iotdsl::DeclaredType)

@given(instance=iotdsl::PrimitiveType_strategy)
@settings(max_examples=50)
def test_iotdsl::primitivetype_instantiation(instance):
    assert isinstance(instance, iotdsl::PrimitiveType)

@given(instance=iotdsl::Import_strategy)
@settings(max_examples=50)
def test_iotdsl::import_instantiation(instance):
    assert isinstance(instance, iotdsl::Import)

@given(instance=iotdsl::Import_strategy)
def test_iotdsl::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=iotdsl::Import_strategy)
def test_iotdsl::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=iotdsl::IotModel_strategy)
@settings(max_examples=50)
def test_iotdsl::iotmodel_instantiation(instance):
    assert isinstance(instance, iotdsl::IotModel)

@given(instance=iotdsl::IotModel_strategy)
def test_iotdsl::iotmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iotdsl::IotModel_strategy)
def test_iotdsl::iotmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

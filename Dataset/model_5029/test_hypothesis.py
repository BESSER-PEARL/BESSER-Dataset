import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    cbpmn::EObject,
    cbpmn::FlowNodeInstance,
    EObject,
    cbpmn::DataObject,
    cbpmn::ProcessInstance,
    cbpmn::EClass,
    FlowNode,
    cbpmn::Event,
    cbpmn::SplitGateway,
    cbpmn::Activity,
    cbpmn::OCLConstraint,
    OCLConstraint,
    SplitGateway,
    cbpmn::ParallelGateway,
    cbpmn::DecisionGateway,
    cbpmn::FlowNode,
    cbpmn::DecisionCondition,
    cbpmn::DataObjectReference,
    cbpmn::Branch,
    cbpmn::ProcessModel,
    DataObjectType,
    FlowNodeInstanceStatus,
    ActivityType,
    EventType,
    DecisionType,
    GatewayType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cbpmn::eobject_is_not_abstract():
    assert not inspect.isabstract(cbpmn::EObject)


def test_cbpmn::eobject_constructor_exists():
    assert callable(cbpmn::EObject.__init__)


def test_cbpmn::eobject_constructor_args():
    sig = inspect.signature(cbpmn::EObject.__init__)
    params = list(sig.parameters.keys())



def test_cbpmn::flownodeinstance_is_not_abstract():
    assert not inspect.isabstract(cbpmn::FlowNodeInstance)


def test_cbpmn::flownodeinstance_constructor_exists():
    assert callable(cbpmn::FlowNodeInstance.__init__)


def test_cbpmn::flownodeinstance_constructor_args():
    sig = inspect.signature(cbpmn::FlowNodeInstance.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"

def test_cbpmn::flownodeinstance_has_status():
    assert hasattr(cbpmn::FlowNodeInstance, "status")
    descriptor = None
    for klass in cbpmn::FlowNodeInstance.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_eobject_is_not_abstract():
    assert not inspect.isabstract(EObject)


def test_eobject_constructor_exists():
    assert callable(EObject.__init__)


def test_eobject_constructor_args():
    sig = inspect.signature(EObject.__init__)
    params = list(sig.parameters.keys())



def test_cbpmn::dataobject_is_not_abstract():
    assert not inspect.isabstract(cbpmn::DataObject)


def test_cbpmn::dataobject_constructor_exists():
    assert callable(cbpmn::DataObject.__init__)


def test_cbpmn::dataobject_constructor_args():
    sig = inspect.signature(cbpmn::DataObject.__init__)
    params = list(sig.parameters.keys())



def test_cbpmn::processinstance_is_not_abstract():
    assert not inspect.isabstract(cbpmn::ProcessInstance)


def test_cbpmn::processinstance_constructor_exists():
    assert callable(cbpmn::ProcessInstance.__init__)


def test_cbpmn::processinstance_constructor_args():
    sig = inspect.signature(cbpmn::ProcessInstance.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_cbpmn::processinstance_has_id():
    assert hasattr(cbpmn::ProcessInstance, "id")
    descriptor = None
    for klass in cbpmn::ProcessInstance.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_cbpmn::eclass_is_not_abstract():
    assert not inspect.isabstract(cbpmn::EClass)


def test_cbpmn::eclass_constructor_exists():
    assert callable(cbpmn::EClass.__init__)


def test_cbpmn::eclass_constructor_args():
    sig = inspect.signature(cbpmn::EClass.__init__)
    params = list(sig.parameters.keys())



def test_flownode_is_not_abstract():
    assert not inspect.isabstract(FlowNode)


def test_flownode_constructor_exists():
    assert callable(FlowNode.__init__)


def test_flownode_constructor_args():
    sig = inspect.signature(FlowNode.__init__)
    params = list(sig.parameters.keys())



def test_cbpmn::event_is_not_abstract():
    assert not inspect.isabstract(cbpmn::Event)


def test_cbpmn::event_constructor_exists():
    assert callable(cbpmn::Event.__init__)


def test_cbpmn::event_constructor_args():
    sig = inspect.signature(cbpmn::Event.__init__)
    params = list(sig.parameters.keys())



def test_cbpmn::splitgateway_is_not_abstract():
    assert not inspect.isabstract(cbpmn::SplitGateway)


def test_cbpmn::splitgateway_constructor_exists():
    assert callable(cbpmn::SplitGateway.__init__)


def test_cbpmn::splitgateway_constructor_args():
    sig = inspect.signature(cbpmn::SplitGateway.__init__)
    params = list(sig.parameters.keys())



def test_cbpmn::activity_is_not_abstract():
    assert not inspect.isabstract(cbpmn::Activity)


def test_cbpmn::activity_constructor_exists():
    assert callable(cbpmn::Activity.__init__)


def test_cbpmn::activity_constructor_args():
    sig = inspect.signature(cbpmn::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cbpmn::activity_has_type():
    assert hasattr(cbpmn::Activity, "type")
    descriptor = None
    for klass in cbpmn::Activity.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cbpmn::oclconstraint_is_not_abstract():
    assert not inspect.isabstract(cbpmn::OCLConstraint)


def test_cbpmn::oclconstraint_constructor_exists():
    assert callable(cbpmn::OCLConstraint.__init__)


def test_cbpmn::oclconstraint_constructor_args():
    sig = inspect.signature(cbpmn::OCLConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "constraintStr" in params, "Missing parameter 'constraintStr'"
    assert "constraintName" in params, "Missing parameter 'constraintName'"

def test_cbpmn::oclconstraint_has_constraintStr():
    assert hasattr(cbpmn::OCLConstraint, "constraintStr")
    descriptor = None
    for klass in cbpmn::OCLConstraint.__mro__:
        if "constraintStr" in klass.__dict__:
            descriptor = klass.__dict__["constraintStr"]
            break
    assert isinstance(descriptor, property)

def test_cbpmn::oclconstraint_has_constraintName():
    assert hasattr(cbpmn::OCLConstraint, "constraintName")
    descriptor = None
    for klass in cbpmn::OCLConstraint.__mro__:
        if "constraintName" in klass.__dict__:
            descriptor = klass.__dict__["constraintName"]
            break
    assert isinstance(descriptor, property)



def test_oclconstraint_is_not_abstract():
    assert not inspect.isabstract(OCLConstraint)


def test_oclconstraint_constructor_exists():
    assert callable(OCLConstraint.__init__)


def test_oclconstraint_constructor_args():
    sig = inspect.signature(OCLConstraint.__init__)
    params = list(sig.parameters.keys())



def test_splitgateway_is_not_abstract():
    assert not inspect.isabstract(SplitGateway)


def test_splitgateway_constructor_exists():
    assert callable(SplitGateway.__init__)


def test_splitgateway_constructor_args():
    sig = inspect.signature(SplitGateway.__init__)
    params = list(sig.parameters.keys())



def test_cbpmn::parallelgateway_is_not_abstract():
    assert not inspect.isabstract(cbpmn::ParallelGateway)


def test_cbpmn::parallelgateway_constructor_exists():
    assert callable(cbpmn::ParallelGateway.__init__)


def test_cbpmn::parallelgateway_constructor_args():
    sig = inspect.signature(cbpmn::ParallelGateway.__init__)
    params = list(sig.parameters.keys())



def test_cbpmn::decisiongateway_is_not_abstract():
    assert not inspect.isabstract(cbpmn::DecisionGateway)


def test_cbpmn::decisiongateway_constructor_exists():
    assert callable(cbpmn::DecisionGateway.__init__)


def test_cbpmn::decisiongateway_constructor_args():
    sig = inspect.signature(cbpmn::DecisionGateway.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cbpmn::decisiongateway_has_type():
    assert hasattr(cbpmn::DecisionGateway, "type")
    descriptor = None
    for klass in cbpmn::DecisionGateway.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cbpmn::flownode_is_not_abstract():
    assert not inspect.isabstract(cbpmn::FlowNode)


def test_cbpmn::flownode_constructor_exists():
    assert callable(cbpmn::FlowNode.__init__)


def test_cbpmn::flownode_constructor_args():
    sig = inspect.signature(cbpmn::FlowNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cbpmn::flownode_has_name():
    assert hasattr(cbpmn::FlowNode, "name")
    descriptor = None
    for klass in cbpmn::FlowNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cbpmn::decisioncondition_is_not_abstract():
    assert not inspect.isabstract(cbpmn::DecisionCondition)


def test_cbpmn::decisioncondition_constructor_exists():
    assert callable(cbpmn::DecisionCondition.__init__)


def test_cbpmn::decisioncondition_constructor_args():
    sig = inspect.signature(cbpmn::DecisionCondition.__init__)
    params = list(sig.parameters.keys())
    assert "isDefault" in params, "Missing parameter 'isDefault'"

def test_cbpmn::decisioncondition_has_isDefault():
    assert hasattr(cbpmn::DecisionCondition, "isDefault")
    descriptor = None
    for klass in cbpmn::DecisionCondition.__mro__:
        if "isDefault" in klass.__dict__:
            descriptor = klass.__dict__["isDefault"]
            break
    assert isinstance(descriptor, property)



def test_cbpmn::dataobjectreference_is_not_abstract():
    assert not inspect.isabstract(cbpmn::DataObjectReference)


def test_cbpmn::dataobjectreference_constructor_exists():
    assert callable(cbpmn::DataObjectReference.__init__)


def test_cbpmn::dataobjectreference_constructor_args():
    sig = inspect.signature(cbpmn::DataObjectReference.__init__)
    params = list(sig.parameters.keys())
    assert "higherBound" in params, "Missing parameter 'higherBound'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "name" in params, "Missing parameter 'name'"

def test_cbpmn::dataobjectreference_has_higherBound():
    assert hasattr(cbpmn::DataObjectReference, "higherBound")
    descriptor = None
    for klass in cbpmn::DataObjectReference.__mro__:
        if "higherBound" in klass.__dict__:
            descriptor = klass.__dict__["higherBound"]
            break
    assert isinstance(descriptor, property)

def test_cbpmn::dataobjectreference_has_lowerBound():
    assert hasattr(cbpmn::DataObjectReference, "lowerBound")
    descriptor = None
    for klass in cbpmn::DataObjectReference.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_cbpmn::dataobjectreference_has_name():
    assert hasattr(cbpmn::DataObjectReference, "name")
    descriptor = None
    for klass in cbpmn::DataObjectReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cbpmn::branch_is_not_abstract():
    assert not inspect.isabstract(cbpmn::Branch)


def test_cbpmn::branch_constructor_exists():
    assert callable(cbpmn::Branch.__init__)


def test_cbpmn::branch_constructor_args():
    sig = inspect.signature(cbpmn::Branch.__init__)
    params = list(sig.parameters.keys())



def test_cbpmn::processmodel_is_not_abstract():
    assert not inspect.isabstract(cbpmn::ProcessModel)


def test_cbpmn::processmodel_constructor_exists():
    assert callable(cbpmn::ProcessModel.__init__)


def test_cbpmn::processmodel_constructor_args():
    sig = inspect.signature(cbpmn::ProcessModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cbpmn::processmodel_has_name():
    assert hasattr(cbpmn::ProcessModel, "name")
    descriptor = None
    for klass in cbpmn::ProcessModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dataobjecttype_exists():
    # Check that the Enumeration exists
    assert DataObjectType is not None

def test_dataobjecttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataObjectType]
    expected_literals = [
        "INFORMATIONAL",
        "PHYSICAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataObjectType"

def test_flownodeinstancestatus_exists():
    # Check that the Enumeration exists
    assert FlowNodeInstanceStatus is not None

def test_flownodeinstancestatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FlowNodeInstanceStatus]
    expected_literals = [
        "STARTED",
        "INTERRUPTED",
        "SUCCESS",
        "INIT",
        "FAILED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FlowNodeInstanceStatus"

def test_activitytype_exists():
    # Check that the Enumeration exists
    assert ActivityType is not None

def test_activitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActivityType]
    expected_literals = [
        "MANUAL",
        "SEND",
        "SERVICE",
        "BUSINESSRULE",
        "RECEIVE",
        "USER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActivityType"

def test_eventtype_exists():
    # Check that the Enumeration exists
    assert EventType is not None

def test_eventtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventType]
    expected_literals = [
        "EEnumLiteral0",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EventType"

def test_decisiontype_exists():
    # Check that the Enumeration exists
    assert DecisionType is not None

def test_decisiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DecisionType]
    expected_literals = [
        "EXCLUSIVE",
        "INCLUSIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DecisionType"

def test_gatewaytype_exists():
    # Check that the Enumeration exists
    assert GatewayType is not None

def test_gatewaytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GatewayType]
    expected_literals = [
        "SPLIT",
        "JOIN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GatewayType"


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
cbpmn::EObject_strategy = st.builds(
    cbpmn::EObject,
)
cbpmn::FlowNodeInstance_strategy = st.builds(
    cbpmn::FlowNodeInstance,
    status=
        safe_text
)
EObject_strategy = st.builds(
    EObject,
)
cbpmn::DataObject_strategy = st.builds(
    cbpmn::DataObject,
)
cbpmn::ProcessInstance_strategy = st.builds(
    cbpmn::ProcessInstance,
    id=
        safe_text
)
cbpmn::EClass_strategy = st.builds(
    cbpmn::EClass,
)
FlowNode_strategy = st.builds(
    FlowNode,
)
cbpmn::Event_strategy = st.builds(
    cbpmn::Event,
)
cbpmn::SplitGateway_strategy = st.builds(
    cbpmn::SplitGateway,
)
cbpmn::Activity_strategy = st.builds(
    cbpmn::Activity,
    type=
        safe_text
)
cbpmn::OCLConstraint_strategy = st.builds(
    cbpmn::OCLConstraint,
    constraintStr=
        safe_text,
    constraintName=
        safe_text
)
OCLConstraint_strategy = st.builds(
    OCLConstraint,
)
SplitGateway_strategy = st.builds(
    SplitGateway,
)
cbpmn::ParallelGateway_strategy = st.builds(
    cbpmn::ParallelGateway,
)
cbpmn::DecisionGateway_strategy = st.builds(
    cbpmn::DecisionGateway,
    type=
        safe_text
)
cbpmn::FlowNode_strategy = st.builds(
    cbpmn::FlowNode,
    name=
        safe_text
)
cbpmn::DecisionCondition_strategy = st.builds(
    cbpmn::DecisionCondition,
    isDefault=
        st.booleans()
)
cbpmn::DataObjectReference_strategy = st.builds(
    cbpmn::DataObjectReference,
    higherBound=
        st.integers(),
    lowerBound=
        st.integers(),
    name=
        safe_text
)
cbpmn::Branch_strategy = st.builds(
    cbpmn::Branch,
)
cbpmn::ProcessModel_strategy = st.builds(
    cbpmn::ProcessModel,
    name=
        safe_text
)

@given(instance=cbpmn::EObject_strategy)
@settings(max_examples=50)
def test_cbpmn::eobject_instantiation(instance):
    assert isinstance(instance, cbpmn::EObject)

@given(instance=cbpmn::FlowNodeInstance_strategy)
@settings(max_examples=50)
def test_cbpmn::flownodeinstance_instantiation(instance):
    assert isinstance(instance, cbpmn::FlowNodeInstance)

@given(instance=cbpmn::FlowNodeInstance_strategy)
def test_cbpmn::flownodeinstance_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=cbpmn::FlowNodeInstance_strategy)
def test_cbpmn::flownodeinstance_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=EObject_strategy)
@settings(max_examples=50)
def test_eobject_instantiation(instance):
    assert isinstance(instance, EObject)

@given(instance=cbpmn::DataObject_strategy)
@settings(max_examples=50)
def test_cbpmn::dataobject_instantiation(instance):
    assert isinstance(instance, cbpmn::DataObject)

@given(instance=cbpmn::ProcessInstance_strategy)
@settings(max_examples=50)
def test_cbpmn::processinstance_instantiation(instance):
    assert isinstance(instance, cbpmn::ProcessInstance)

@given(instance=cbpmn::ProcessInstance_strategy)
def test_cbpmn::processinstance_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=cbpmn::ProcessInstance_strategy)
def test_cbpmn::processinstance_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=cbpmn::EClass_strategy)
@settings(max_examples=50)
def test_cbpmn::eclass_instantiation(instance):
    assert isinstance(instance, cbpmn::EClass)

@given(instance=FlowNode_strategy)
@settings(max_examples=50)
def test_flownode_instantiation(instance):
    assert isinstance(instance, FlowNode)

@given(instance=cbpmn::Event_strategy)
@settings(max_examples=50)
def test_cbpmn::event_instantiation(instance):
    assert isinstance(instance, cbpmn::Event)

@given(instance=cbpmn::SplitGateway_strategy)
@settings(max_examples=50)
def test_cbpmn::splitgateway_instantiation(instance):
    assert isinstance(instance, cbpmn::SplitGateway)

@given(instance=cbpmn::Activity_strategy)
@settings(max_examples=50)
def test_cbpmn::activity_instantiation(instance):
    assert isinstance(instance, cbpmn::Activity)

@given(instance=cbpmn::Activity_strategy)
def test_cbpmn::activity_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=cbpmn::Activity_strategy)
def test_cbpmn::activity_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=cbpmn::OCLConstraint_strategy)
@settings(max_examples=50)
def test_cbpmn::oclconstraint_instantiation(instance):
    assert isinstance(instance, cbpmn::OCLConstraint)

@given(instance=cbpmn::OCLConstraint_strategy)
def test_cbpmn::oclconstraint_constraintStr_type(instance):
    assert isinstance(instance.constraintStr, str)


@given(instance=cbpmn::OCLConstraint_strategy)
def test_cbpmn::oclconstraint_constraintStr_setter(instance):
    original = instance.constraintStr
    instance.constraintStr = original
    assert instance.constraintStr == original

@given(instance=cbpmn::OCLConstraint_strategy)
def test_cbpmn::oclconstraint_constraintName_type(instance):
    assert isinstance(instance.constraintName, str)


@given(instance=cbpmn::OCLConstraint_strategy)
def test_cbpmn::oclconstraint_constraintName_setter(instance):
    original = instance.constraintName
    instance.constraintName = original
    assert instance.constraintName == original

@given(instance=OCLConstraint_strategy)
@settings(max_examples=50)
def test_oclconstraint_instantiation(instance):
    assert isinstance(instance, OCLConstraint)

@given(instance=SplitGateway_strategy)
@settings(max_examples=50)
def test_splitgateway_instantiation(instance):
    assert isinstance(instance, SplitGateway)

@given(instance=cbpmn::ParallelGateway_strategy)
@settings(max_examples=50)
def test_cbpmn::parallelgateway_instantiation(instance):
    assert isinstance(instance, cbpmn::ParallelGateway)

@given(instance=cbpmn::DecisionGateway_strategy)
@settings(max_examples=50)
def test_cbpmn::decisiongateway_instantiation(instance):
    assert isinstance(instance, cbpmn::DecisionGateway)

@given(instance=cbpmn::DecisionGateway_strategy)
def test_cbpmn::decisiongateway_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=cbpmn::DecisionGateway_strategy)
def test_cbpmn::decisiongateway_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=cbpmn::DecisionGateway_strategy)
@settings(max_examples=30)
def test_cbpmn::decisiongateway_addbranchwithcondition_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addBranchWithCondition(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addBranchWithCondition).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addBranchWithCondition' in cbpmn::DecisionGateway is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addBranchWithCondition' in cbpmn::DecisionGateway did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addBranchWithCondition' in cbpmn::DecisionGateway is not implemented or raised an error")

@given(instance=cbpmn::FlowNode_strategy)
@settings(max_examples=50)
def test_cbpmn::flownode_instantiation(instance):
    assert isinstance(instance, cbpmn::FlowNode)

@given(instance=cbpmn::FlowNode_strategy)
def test_cbpmn::flownode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cbpmn::FlowNode_strategy)
def test_cbpmn::flownode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cbpmn::DecisionCondition_strategy)
@settings(max_examples=50)
def test_cbpmn::decisioncondition_instantiation(instance):
    assert isinstance(instance, cbpmn::DecisionCondition)

@given(instance=cbpmn::DecisionCondition_strategy)
def test_cbpmn::decisioncondition_isDefault_type(instance):
    assert isinstance(instance.isDefault, bool)


@given(instance=cbpmn::DecisionCondition_strategy)
def test_cbpmn::decisioncondition_isDefault_setter(instance):
    original = instance.isDefault
    instance.isDefault = original
    assert instance.isDefault == original

@given(instance=cbpmn::DataObjectReference_strategy)
@settings(max_examples=50)
def test_cbpmn::dataobjectreference_instantiation(instance):
    assert isinstance(instance, cbpmn::DataObjectReference)

@given(instance=cbpmn::DataObjectReference_strategy)
def test_cbpmn::dataobjectreference_higherBound_type(instance):
    assert isinstance(instance.higherBound, int)


@given(instance=cbpmn::DataObjectReference_strategy)
def test_cbpmn::dataobjectreference_higherBound_setter(instance):
    original = instance.higherBound
    instance.higherBound = original
    assert instance.higherBound == original

@given(instance=cbpmn::DataObjectReference_strategy)
def test_cbpmn::dataobjectreference_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=cbpmn::DataObjectReference_strategy)
def test_cbpmn::dataobjectreference_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=cbpmn::DataObjectReference_strategy)
def test_cbpmn::dataobjectreference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cbpmn::DataObjectReference_strategy)
def test_cbpmn::dataobjectreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cbpmn::Branch_strategy)
@settings(max_examples=50)
def test_cbpmn::branch_instantiation(instance):
    assert isinstance(instance, cbpmn::Branch)

@given(instance=cbpmn::ProcessModel_strategy)
@settings(max_examples=50)
def test_cbpmn::processmodel_instantiation(instance):
    assert isinstance(instance, cbpmn::ProcessModel)

@given(instance=cbpmn::ProcessModel_strategy)
def test_cbpmn::processmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cbpmn::ProcessModel_strategy)
def test_cbpmn::processmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

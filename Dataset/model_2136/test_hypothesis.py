import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::batch::Operation,
    Operation,
    model::batch::BatchOperation,
    model::administration::ProblemDetail,
    INamed,
    model::export::Export,
    model::history::HistoryEntry,
    HistoryEntry,
    model::history::History,
    model::administration::Status,
    model::history::Change,
    Change,
    TestParameter,
    base::IPositionable,
    ParameterAssignment,
    IContainer,
    model::testspecification::TestSpecification,
    ProcessNode,
    model::processes::ProcessDecision,
    model::processes::ProcessStart,
    model::processes::ProcessEnd,
    model::processes::ProcessStep,
    model::processes::Process,
    base::IContentElement,
    model::testspecification::TestStep,
    base::IExternal,
    base::ISpecmateModelObject,
    model::requirements::Requirement,
    model::base::IRecycled,
    ITracingElement,
    model::base::ITracingElement,
    model::base::IPositionable,
    ISpecmateModelObject,
    model::requirements::CEGModel,
    model::base::Folder,
    base::ITracingElement,
    base::IContainer,
    model::testspecification::TestProcedure,
    model::testspecification::TestCase,
    model::base::ISpecmateModelObject,
    IContentElement,
    model::testspecification::TestParameter,
    model::testspecification::ParameterAssignment,
    model::base::IContainer,
    base::IRecycled,
    base::IDescribed,
    base::INamed,
    base::IID,
    model::base::IContentElement,
    model::base::IID,
    IModelConnection,
    model::requirements::CEGConnection,
    model::processes::ProcessConnection,
    ISpecmatePositionableModelObject,
    model::base::IModelNode,
    IModelNode,
    model::requirements::CEGNode,
    model::processes::ProcessNode,
    model::base::IModelConnection,
    model::base::ISpecmatePositionableModelObject,
    model::base::IExternal,
    model::base::IDescribed,
    model::base::INamed,
    NodeType,
    ParameterType,
    ErrorCode,
    OperationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::batch::operation_is_not_abstract():
    assert not inspect.isabstract(model::batch::Operation)


def test_model::batch::operation_constructor_exists():
    assert callable(model::batch::Operation.__init__)


def test_model::batch::operation_constructor_args():
    sig = inspect.signature(model::batch::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_model::batch::operation_has_type():
    assert hasattr(model::batch::Operation, "type")
    descriptor = None
    for klass in model::batch::Operation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_model::batch::batchoperation_is_not_abstract():
    assert not inspect.isabstract(model::batch::BatchOperation)


def test_model::batch::batchoperation_constructor_exists():
    assert callable(model::batch::BatchOperation.__init__)


def test_model::batch::batchoperation_constructor_args():
    sig = inspect.signature(model::batch::BatchOperation.__init__)
    params = list(sig.parameters.keys())



def test_model::administration::problemdetail_is_not_abstract():
    assert not inspect.isabstract(model::administration::ProblemDetail)


def test_model::administration::problemdetail_constructor_exists():
    assert callable(model::administration::ProblemDetail.__init__)


def test_model::administration::problemdetail_constructor_args():
    sig = inspect.signature(model::administration::ProblemDetail.__init__)
    params = list(sig.parameters.keys())
    assert "ecode" in params, "Missing parameter 'ecode'"
    assert "detail" in params, "Missing parameter 'detail'"
    assert "instance" in params, "Missing parameter 'instance'"
    assert "status" in params, "Missing parameter 'status'"

def test_model::administration::problemdetail_has_ecode():
    assert hasattr(model::administration::ProblemDetail, "ecode")
    descriptor = None
    for klass in model::administration::ProblemDetail.__mro__:
        if "ecode" in klass.__dict__:
            descriptor = klass.__dict__["ecode"]
            break
    assert isinstance(descriptor, property)

def test_model::administration::problemdetail_has_detail():
    assert hasattr(model::administration::ProblemDetail, "detail")
    descriptor = None
    for klass in model::administration::ProblemDetail.__mro__:
        if "detail" in klass.__dict__:
            descriptor = klass.__dict__["detail"]
            break
    assert isinstance(descriptor, property)

def test_model::administration::problemdetail_has_instance():
    assert hasattr(model::administration::ProblemDetail, "instance")
    descriptor = None
    for klass in model::administration::ProblemDetail.__mro__:
        if "instance" in klass.__dict__:
            descriptor = klass.__dict__["instance"]
            break
    assert isinstance(descriptor, property)

def test_model::administration::problemdetail_has_status():
    assert hasattr(model::administration::ProblemDetail, "status")
    descriptor = None
    for klass in model::administration::ProblemDetail.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_inamed_is_not_abstract():
    assert not inspect.isabstract(INamed)


def test_inamed_constructor_exists():
    assert callable(INamed.__init__)


def test_inamed_constructor_args():
    sig = inspect.signature(INamed.__init__)
    params = list(sig.parameters.keys())



def test_model::export::export_is_not_abstract():
    assert not inspect.isabstract(model::export::Export)


def test_model::export::export_constructor_exists():
    assert callable(model::export::Export.__init__)


def test_model::export::export_constructor_args():
    sig = inspect.signature(model::export::Export.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "type" in params, "Missing parameter 'type'"

def test_model::export::export_has_content():
    assert hasattr(model::export::Export, "content")
    descriptor = None
    for klass in model::export::Export.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_model::export::export_has_type():
    assert hasattr(model::export::Export, "type")
    descriptor = None
    for klass in model::export::Export.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_model::history::historyentry_is_not_abstract():
    assert not inspect.isabstract(model::history::HistoryEntry)


def test_model::history::historyentry_constructor_exists():
    assert callable(model::history::HistoryEntry.__init__)


def test_model::history::historyentry_constructor_args():
    sig = inspect.signature(model::history::HistoryEntry.__init__)
    params = list(sig.parameters.keys())
    assert "user" in params, "Missing parameter 'user'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "deletedObjects" in params, "Missing parameter 'deletedObjects'"

def test_model::history::historyentry_has_user():
    assert hasattr(model::history::HistoryEntry, "user")
    descriptor = None
    for klass in model::history::HistoryEntry.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)

def test_model::history::historyentry_has_comment():
    assert hasattr(model::history::HistoryEntry, "comment")
    descriptor = None
    for klass in model::history::HistoryEntry.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_model::history::historyentry_has_timestamp():
    assert hasattr(model::history::HistoryEntry, "timestamp")
    descriptor = None
    for klass in model::history::HistoryEntry.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)

def test_model::history::historyentry_has_deletedObjects():
    assert hasattr(model::history::HistoryEntry, "deletedObjects")
    descriptor = None
    for klass in model::history::HistoryEntry.__mro__:
        if "deletedObjects" in klass.__dict__:
            descriptor = klass.__dict__["deletedObjects"]
            break
    assert isinstance(descriptor, property)



def test_historyentry_is_not_abstract():
    assert not inspect.isabstract(HistoryEntry)


def test_historyentry_constructor_exists():
    assert callable(HistoryEntry.__init__)


def test_historyentry_constructor_args():
    sig = inspect.signature(HistoryEntry.__init__)
    params = list(sig.parameters.keys())



def test_model::history::history_is_not_abstract():
    assert not inspect.isabstract(model::history::History)


def test_model::history::history_constructor_exists():
    assert callable(model::history::History.__init__)


def test_model::history::history_constructor_args():
    sig = inspect.signature(model::history::History.__init__)
    params = list(sig.parameters.keys())



def test_model::administration::status_is_not_abstract():
    assert not inspect.isabstract(model::administration::Status)


def test_model::administration::status_constructor_exists():
    assert callable(model::administration::Status.__init__)


def test_model::administration::status_constructor_args():
    sig = inspect.signature(model::administration::Status.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model::administration::status_has_value():
    assert hasattr(model::administration::Status, "value")
    descriptor = None
    for klass in model::administration::Status.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model::history::change_is_not_abstract():
    assert not inspect.isabstract(model::history::Change)


def test_model::history::change_constructor_exists():
    assert callable(model::history::Change.__init__)


def test_model::history::change_constructor_args():
    sig = inspect.signature(model::history::Change.__init__)
    params = list(sig.parameters.keys())
    assert "objectType" in params, "Missing parameter 'objectType'"
    assert "oldValue" in params, "Missing parameter 'oldValue'"
    assert "feature" in params, "Missing parameter 'feature'"
    assert "isCreate" in params, "Missing parameter 'isCreate'"
    assert "newValue" in params, "Missing parameter 'newValue'"
    assert "objectName" in params, "Missing parameter 'objectName'"
    assert "isDelete" in params, "Missing parameter 'isDelete'"

def test_model::history::change_has_objectType():
    assert hasattr(model::history::Change, "objectType")
    descriptor = None
    for klass in model::history::Change.__mro__:
        if "objectType" in klass.__dict__:
            descriptor = klass.__dict__["objectType"]
            break
    assert isinstance(descriptor, property)

def test_model::history::change_has_oldValue():
    assert hasattr(model::history::Change, "oldValue")
    descriptor = None
    for klass in model::history::Change.__mro__:
        if "oldValue" in klass.__dict__:
            descriptor = klass.__dict__["oldValue"]
            break
    assert isinstance(descriptor, property)

def test_model::history::change_has_feature():
    assert hasattr(model::history::Change, "feature")
    descriptor = None
    for klass in model::history::Change.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)

def test_model::history::change_has_isCreate():
    assert hasattr(model::history::Change, "isCreate")
    descriptor = None
    for klass in model::history::Change.__mro__:
        if "isCreate" in klass.__dict__:
            descriptor = klass.__dict__["isCreate"]
            break
    assert isinstance(descriptor, property)

def test_model::history::change_has_newValue():
    assert hasattr(model::history::Change, "newValue")
    descriptor = None
    for klass in model::history::Change.__mro__:
        if "newValue" in klass.__dict__:
            descriptor = klass.__dict__["newValue"]
            break
    assert isinstance(descriptor, property)

def test_model::history::change_has_objectName():
    assert hasattr(model::history::Change, "objectName")
    descriptor = None
    for klass in model::history::Change.__mro__:
        if "objectName" in klass.__dict__:
            descriptor = klass.__dict__["objectName"]
            break
    assert isinstance(descriptor, property)

def test_model::history::change_has_isDelete():
    assert hasattr(model::history::Change, "isDelete")
    descriptor = None
    for klass in model::history::Change.__mro__:
        if "isDelete" in klass.__dict__:
            descriptor = klass.__dict__["isDelete"]
            break
    assert isinstance(descriptor, property)



def test_change_is_not_abstract():
    assert not inspect.isabstract(Change)


def test_change_constructor_exists():
    assert callable(Change.__init__)


def test_change_constructor_args():
    sig = inspect.signature(Change.__init__)
    params = list(sig.parameters.keys())



def test_testparameter_is_not_abstract():
    assert not inspect.isabstract(TestParameter)


def test_testparameter_constructor_exists():
    assert callable(TestParameter.__init__)


def test_testparameter_constructor_args():
    sig = inspect.signature(TestParameter.__init__)
    params = list(sig.parameters.keys())



def test_base::ipositionable_is_not_abstract():
    assert not inspect.isabstract(base::IPositionable)


def test_base::ipositionable_constructor_exists():
    assert callable(base::IPositionable.__init__)


def test_base::ipositionable_constructor_args():
    sig = inspect.signature(base::IPositionable.__init__)
    params = list(sig.parameters.keys())



def test_parameterassignment_is_not_abstract():
    assert not inspect.isabstract(ParameterAssignment)


def test_parameterassignment_constructor_exists():
    assert callable(ParameterAssignment.__init__)


def test_parameterassignment_constructor_args():
    sig = inspect.signature(ParameterAssignment.__init__)
    params = list(sig.parameters.keys())



def test_icontainer_is_not_abstract():
    assert not inspect.isabstract(IContainer)


def test_icontainer_constructor_exists():
    assert callable(IContainer.__init__)


def test_icontainer_constructor_args():
    sig = inspect.signature(IContainer.__init__)
    params = list(sig.parameters.keys())



def test_model::testspecification::testspecification_is_not_abstract():
    assert not inspect.isabstract(model::testspecification::TestSpecification)


def test_model::testspecification::testspecification_constructor_exists():
    assert callable(model::testspecification::TestSpecification.__init__)


def test_model::testspecification::testspecification_constructor_args():
    sig = inspect.signature(model::testspecification::TestSpecification.__init__)
    params = list(sig.parameters.keys())



def test_processnode_is_not_abstract():
    assert not inspect.isabstract(ProcessNode)


def test_processnode_constructor_exists():
    assert callable(ProcessNode.__init__)


def test_processnode_constructor_args():
    sig = inspect.signature(ProcessNode.__init__)
    params = list(sig.parameters.keys())



def test_model::processes::processdecision_is_not_abstract():
    assert not inspect.isabstract(model::processes::ProcessDecision)


def test_model::processes::processdecision_constructor_exists():
    assert callable(model::processes::ProcessDecision.__init__)


def test_model::processes::processdecision_constructor_args():
    sig = inspect.signature(model::processes::ProcessDecision.__init__)
    params = list(sig.parameters.keys())



def test_model::processes::processstart_is_not_abstract():
    assert not inspect.isabstract(model::processes::ProcessStart)


def test_model::processes::processstart_constructor_exists():
    assert callable(model::processes::ProcessStart.__init__)


def test_model::processes::processstart_constructor_args():
    sig = inspect.signature(model::processes::ProcessStart.__init__)
    params = list(sig.parameters.keys())



def test_model::processes::processend_is_not_abstract():
    assert not inspect.isabstract(model::processes::ProcessEnd)


def test_model::processes::processend_constructor_exists():
    assert callable(model::processes::ProcessEnd.__init__)


def test_model::processes::processend_constructor_args():
    sig = inspect.signature(model::processes::ProcessEnd.__init__)
    params = list(sig.parameters.keys())



def test_model::processes::processstep_is_not_abstract():
    assert not inspect.isabstract(model::processes::ProcessStep)


def test_model::processes::processstep_constructor_exists():
    assert callable(model::processes::ProcessStep.__init__)


def test_model::processes::processstep_constructor_args():
    sig = inspect.signature(model::processes::ProcessStep.__init__)
    params = list(sig.parameters.keys())
    assert "expectedOutcome" in params, "Missing parameter 'expectedOutcome'"

def test_model::processes::processstep_has_expectedOutcome():
    assert hasattr(model::processes::ProcessStep, "expectedOutcome")
    descriptor = None
    for klass in model::processes::ProcessStep.__mro__:
        if "expectedOutcome" in klass.__dict__:
            descriptor = klass.__dict__["expectedOutcome"]
            break
    assert isinstance(descriptor, property)



def test_model::processes::process_is_not_abstract():
    assert not inspect.isabstract(model::processes::Process)


def test_model::processes::process_constructor_exists():
    assert callable(model::processes::Process.__init__)


def test_model::processes::process_constructor_args():
    sig = inspect.signature(model::processes::Process.__init__)
    params = list(sig.parameters.keys())



def test_base::icontentelement_is_not_abstract():
    assert not inspect.isabstract(base::IContentElement)


def test_base::icontentelement_constructor_exists():
    assert callable(base::IContentElement.__init__)


def test_base::icontentelement_constructor_args():
    sig = inspect.signature(base::IContentElement.__init__)
    params = list(sig.parameters.keys())



def test_model::testspecification::teststep_is_not_abstract():
    assert not inspect.isabstract(model::testspecification::TestStep)


def test_model::testspecification::teststep_constructor_exists():
    assert callable(model::testspecification::TestStep.__init__)


def test_model::testspecification::teststep_constructor_args():
    sig = inspect.signature(model::testspecification::TestStep.__init__)
    params = list(sig.parameters.keys())
    assert "expectedOutcome" in params, "Missing parameter 'expectedOutcome'"

def test_model::testspecification::teststep_has_expectedOutcome():
    assert hasattr(model::testspecification::TestStep, "expectedOutcome")
    descriptor = None
    for klass in model::testspecification::TestStep.__mro__:
        if "expectedOutcome" in klass.__dict__:
            descriptor = klass.__dict__["expectedOutcome"]
            break
    assert isinstance(descriptor, property)



def test_base::iexternal_is_not_abstract():
    assert not inspect.isabstract(base::IExternal)


def test_base::iexternal_constructor_exists():
    assert callable(base::IExternal.__init__)


def test_base::iexternal_constructor_args():
    sig = inspect.signature(base::IExternal.__init__)
    params = list(sig.parameters.keys())



def test_base::ispecmatemodelobject_is_not_abstract():
    assert not inspect.isabstract(base::ISpecmateModelObject)


def test_base::ispecmatemodelobject_constructor_exists():
    assert callable(base::ISpecmateModelObject.__init__)


def test_base::ispecmatemodelobject_constructor_args():
    sig = inspect.signature(base::ISpecmateModelObject.__init__)
    params = list(sig.parameters.keys())



def test_model::requirements::requirement_is_not_abstract():
    assert not inspect.isabstract(model::requirements::Requirement)


def test_model::requirements::requirement_constructor_exists():
    assert callable(model::requirements::Requirement.__init__)


def test_model::requirements::requirement_constructor_args():
    sig = inspect.signature(model::requirements::Requirement.__init__)
    params = list(sig.parameters.keys())
    assert "implementingITTeam" in params, "Missing parameter 'implementingITTeam'"
    assert "tac" in params, "Missing parameter 'tac'"
    assert "numberOfTests" in params, "Missing parameter 'numberOfTests'"
    assert "isRegressionRequirement" in params, "Missing parameter 'isRegressionRequirement'"
    assert "platform" in params, "Missing parameter 'platform'"
    assert "plannedRelease" in params, "Missing parameter 'plannedRelease'"
    assert "status" in params, "Missing parameter 'status'"
    assert "implementingUnit" in params, "Missing parameter 'implementingUnit'"
    assert "implementingBOTeam" in params, "Missing parameter 'implementingBOTeam'"

def test_model::requirements::requirement_has_implementingITTeam():
    assert hasattr(model::requirements::Requirement, "implementingITTeam")
    descriptor = None
    for klass in model::requirements::Requirement.__mro__:
        if "implementingITTeam" in klass.__dict__:
            descriptor = klass.__dict__["implementingITTeam"]
            break
    assert isinstance(descriptor, property)

def test_model::requirements::requirement_has_tac():
    assert hasattr(model::requirements::Requirement, "tac")
    descriptor = None
    for klass in model::requirements::Requirement.__mro__:
        if "tac" in klass.__dict__:
            descriptor = klass.__dict__["tac"]
            break
    assert isinstance(descriptor, property)

def test_model::requirements::requirement_has_numberOfTests():
    assert hasattr(model::requirements::Requirement, "numberOfTests")
    descriptor = None
    for klass in model::requirements::Requirement.__mro__:
        if "numberOfTests" in klass.__dict__:
            descriptor = klass.__dict__["numberOfTests"]
            break
    assert isinstance(descriptor, property)

def test_model::requirements::requirement_has_isRegressionRequirement():
    assert hasattr(model::requirements::Requirement, "isRegressionRequirement")
    descriptor = None
    for klass in model::requirements::Requirement.__mro__:
        if "isRegressionRequirement" in klass.__dict__:
            descriptor = klass.__dict__["isRegressionRequirement"]
            break
    assert isinstance(descriptor, property)

def test_model::requirements::requirement_has_platform():
    assert hasattr(model::requirements::Requirement, "platform")
    descriptor = None
    for klass in model::requirements::Requirement.__mro__:
        if "platform" in klass.__dict__:
            descriptor = klass.__dict__["platform"]
            break
    assert isinstance(descriptor, property)

def test_model::requirements::requirement_has_plannedRelease():
    assert hasattr(model::requirements::Requirement, "plannedRelease")
    descriptor = None
    for klass in model::requirements::Requirement.__mro__:
        if "plannedRelease" in klass.__dict__:
            descriptor = klass.__dict__["plannedRelease"]
            break
    assert isinstance(descriptor, property)

def test_model::requirements::requirement_has_status():
    assert hasattr(model::requirements::Requirement, "status")
    descriptor = None
    for klass in model::requirements::Requirement.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_model::requirements::requirement_has_implementingUnit():
    assert hasattr(model::requirements::Requirement, "implementingUnit")
    descriptor = None
    for klass in model::requirements::Requirement.__mro__:
        if "implementingUnit" in klass.__dict__:
            descriptor = klass.__dict__["implementingUnit"]
            break
    assert isinstance(descriptor, property)

def test_model::requirements::requirement_has_implementingBOTeam():
    assert hasattr(model::requirements::Requirement, "implementingBOTeam")
    descriptor = None
    for klass in model::requirements::Requirement.__mro__:
        if "implementingBOTeam" in klass.__dict__:
            descriptor = klass.__dict__["implementingBOTeam"]
            break
    assert isinstance(descriptor, property)



def test_model::base::irecycled_is_not_abstract():
    assert not inspect.isabstract(model::base::IRecycled)


def test_model::base::irecycled_constructor_exists():
    assert callable(model::base::IRecycled.__init__)


def test_model::base::irecycled_constructor_args():
    sig = inspect.signature(model::base::IRecycled.__init__)
    params = list(sig.parameters.keys())
    assert "hasRecycledChildren" in params, "Missing parameter 'hasRecycledChildren'"
    assert "recycled" in params, "Missing parameter 'recycled'"

def test_model::base::irecycled_has_hasRecycledChildren():
    assert hasattr(model::base::IRecycled, "hasRecycledChildren")
    descriptor = None
    for klass in model::base::IRecycled.__mro__:
        if "hasRecycledChildren" in klass.__dict__:
            descriptor = klass.__dict__["hasRecycledChildren"]
            break
    assert isinstance(descriptor, property)

def test_model::base::irecycled_has_recycled():
    assert hasattr(model::base::IRecycled, "recycled")
    descriptor = None
    for klass in model::base::IRecycled.__mro__:
        if "recycled" in klass.__dict__:
            descriptor = klass.__dict__["recycled"]
            break
    assert isinstance(descriptor, property)



def test_itracingelement_is_not_abstract():
    assert not inspect.isabstract(ITracingElement)


def test_itracingelement_constructor_exists():
    assert callable(ITracingElement.__init__)


def test_itracingelement_constructor_args():
    sig = inspect.signature(ITracingElement.__init__)
    params = list(sig.parameters.keys())



def test_model::base::itracingelement_is_not_abstract():
    assert not inspect.isabstract(model::base::ITracingElement)


def test_model::base::itracingelement_constructor_exists():
    assert callable(model::base::ITracingElement.__init__)


def test_model::base::itracingelement_constructor_args():
    sig = inspect.signature(model::base::ITracingElement.__init__)
    params = list(sig.parameters.keys())



def test_model::base::ipositionable_is_not_abstract():
    assert not inspect.isabstract(model::base::IPositionable)


def test_model::base::ipositionable_constructor_exists():
    assert callable(model::base::IPositionable.__init__)


def test_model::base::ipositionable_constructor_args():
    sig = inspect.signature(model::base::IPositionable.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_model::base::ipositionable_has_position():
    assert hasattr(model::base::IPositionable, "position")
    descriptor = None
    for klass in model::base::IPositionable.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_ispecmatemodelobject_is_not_abstract():
    assert not inspect.isabstract(ISpecmateModelObject)


def test_ispecmatemodelobject_constructor_exists():
    assert callable(ISpecmateModelObject.__init__)


def test_ispecmatemodelobject_constructor_args():
    sig = inspect.signature(ISpecmateModelObject.__init__)
    params = list(sig.parameters.keys())



def test_model::requirements::cegmodel_is_not_abstract():
    assert not inspect.isabstract(model::requirements::CEGModel)


def test_model::requirements::cegmodel_constructor_exists():
    assert callable(model::requirements::CEGModel.__init__)


def test_model::requirements::cegmodel_constructor_args():
    sig = inspect.signature(model::requirements::CEGModel.__init__)
    params = list(sig.parameters.keys())
    assert "modelRequirements" in params, "Missing parameter 'modelRequirements'"

def test_model::requirements::cegmodel_has_modelRequirements():
    assert hasattr(model::requirements::CEGModel, "modelRequirements")
    descriptor = None
    for klass in model::requirements::CEGModel.__mro__:
        if "modelRequirements" in klass.__dict__:
            descriptor = klass.__dict__["modelRequirements"]
            break
    assert isinstance(descriptor, property)



def test_model::base::folder_is_not_abstract():
    assert not inspect.isabstract(model::base::Folder)


def test_model::base::folder_constructor_exists():
    assert callable(model::base::Folder.__init__)


def test_model::base::folder_constructor_args():
    sig = inspect.signature(model::base::Folder.__init__)
    params = list(sig.parameters.keys())
    assert "library" in params, "Missing parameter 'library'"

def test_model::base::folder_has_library():
    assert hasattr(model::base::Folder, "library")
    descriptor = None
    for klass in model::base::Folder.__mro__:
        if "library" in klass.__dict__:
            descriptor = klass.__dict__["library"]
            break
    assert isinstance(descriptor, property)



def test_base::itracingelement_is_not_abstract():
    assert not inspect.isabstract(base::ITracingElement)


def test_base::itracingelement_constructor_exists():
    assert callable(base::ITracingElement.__init__)


def test_base::itracingelement_constructor_args():
    sig = inspect.signature(base::ITracingElement.__init__)
    params = list(sig.parameters.keys())



def test_base::icontainer_is_not_abstract():
    assert not inspect.isabstract(base::IContainer)


def test_base::icontainer_constructor_exists():
    assert callable(base::IContainer.__init__)


def test_base::icontainer_constructor_args():
    sig = inspect.signature(base::IContainer.__init__)
    params = list(sig.parameters.keys())



def test_model::testspecification::testprocedure_is_not_abstract():
    assert not inspect.isabstract(model::testspecification::TestProcedure)


def test_model::testspecification::testprocedure_constructor_exists():
    assert callable(model::testspecification::TestProcedure.__init__)


def test_model::testspecification::testprocedure_constructor_args():
    sig = inspect.signature(model::testspecification::TestProcedure.__init__)
    params = list(sig.parameters.keys())
    assert "isRegressionTest" in params, "Missing parameter 'isRegressionTest'"

def test_model::testspecification::testprocedure_has_isRegressionTest():
    assert hasattr(model::testspecification::TestProcedure, "isRegressionTest")
    descriptor = None
    for klass in model::testspecification::TestProcedure.__mro__:
        if "isRegressionTest" in klass.__dict__:
            descriptor = klass.__dict__["isRegressionTest"]
            break
    assert isinstance(descriptor, property)



def test_model::testspecification::testcase_is_not_abstract():
    assert not inspect.isabstract(model::testspecification::TestCase)


def test_model::testspecification::testcase_constructor_exists():
    assert callable(model::testspecification::TestCase.__init__)


def test_model::testspecification::testcase_constructor_args():
    sig = inspect.signature(model::testspecification::TestCase.__init__)
    params = list(sig.parameters.keys())
    assert "consistent" in params, "Missing parameter 'consistent'"

def test_model::testspecification::testcase_has_consistent():
    assert hasattr(model::testspecification::TestCase, "consistent")
    descriptor = None
    for klass in model::testspecification::TestCase.__mro__:
        if "consistent" in klass.__dict__:
            descriptor = klass.__dict__["consistent"]
            break
    assert isinstance(descriptor, property)



def test_model::base::ispecmatemodelobject_is_not_abstract():
    assert not inspect.isabstract(model::base::ISpecmateModelObject)


def test_model::base::ispecmatemodelobject_constructor_exists():
    assert callable(model::base::ISpecmateModelObject.__init__)


def test_model::base::ispecmatemodelobject_constructor_args():
    sig = inspect.signature(model::base::ISpecmateModelObject.__init__)
    params = list(sig.parameters.keys())



def test_icontentelement_is_not_abstract():
    assert not inspect.isabstract(IContentElement)


def test_icontentelement_constructor_exists():
    assert callable(IContentElement.__init__)


def test_icontentelement_constructor_args():
    sig = inspect.signature(IContentElement.__init__)
    params = list(sig.parameters.keys())



def test_model::testspecification::testparameter_is_not_abstract():
    assert not inspect.isabstract(model::testspecification::TestParameter)


def test_model::testspecification::testparameter_constructor_exists():
    assert callable(model::testspecification::TestParameter.__init__)


def test_model::testspecification::testparameter_constructor_args():
    sig = inspect.signature(model::testspecification::TestParameter.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_model::testspecification::testparameter_has_type():
    assert hasattr(model::testspecification::TestParameter, "type")
    descriptor = None
    for klass in model::testspecification::TestParameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_model::testspecification::parameterassignment_is_not_abstract():
    assert not inspect.isabstract(model::testspecification::ParameterAssignment)


def test_model::testspecification::parameterassignment_constructor_exists():
    assert callable(model::testspecification::ParameterAssignment.__init__)


def test_model::testspecification::parameterassignment_constructor_args():
    sig = inspect.signature(model::testspecification::ParameterAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"
    assert "value" in params, "Missing parameter 'value'"

def test_model::testspecification::parameterassignment_has_condition():
    assert hasattr(model::testspecification::ParameterAssignment, "condition")
    descriptor = None
    for klass in model::testspecification::ParameterAssignment.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)

def test_model::testspecification::parameterassignment_has_value():
    assert hasattr(model::testspecification::ParameterAssignment, "value")
    descriptor = None
    for klass in model::testspecification::ParameterAssignment.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model::base::icontainer_is_not_abstract():
    assert not inspect.isabstract(model::base::IContainer)


def test_model::base::icontainer_constructor_exists():
    assert callable(model::base::IContainer.__init__)


def test_model::base::icontainer_constructor_args():
    sig = inspect.signature(model::base::IContainer.__init__)
    params = list(sig.parameters.keys())



def test_base::irecycled_is_not_abstract():
    assert not inspect.isabstract(base::IRecycled)


def test_base::irecycled_constructor_exists():
    assert callable(base::IRecycled.__init__)


def test_base::irecycled_constructor_args():
    sig = inspect.signature(base::IRecycled.__init__)
    params = list(sig.parameters.keys())



def test_base::idescribed_is_not_abstract():
    assert not inspect.isabstract(base::IDescribed)


def test_base::idescribed_constructor_exists():
    assert callable(base::IDescribed.__init__)


def test_base::idescribed_constructor_args():
    sig = inspect.signature(base::IDescribed.__init__)
    params = list(sig.parameters.keys())



def test_base::inamed_is_not_abstract():
    assert not inspect.isabstract(base::INamed)


def test_base::inamed_constructor_exists():
    assert callable(base::INamed.__init__)


def test_base::inamed_constructor_args():
    sig = inspect.signature(base::INamed.__init__)
    params = list(sig.parameters.keys())



def test_base::iid_is_not_abstract():
    assert not inspect.isabstract(base::IID)


def test_base::iid_constructor_exists():
    assert callable(base::IID.__init__)


def test_base::iid_constructor_args():
    sig = inspect.signature(base::IID.__init__)
    params = list(sig.parameters.keys())



def test_model::base::icontentelement_is_not_abstract():
    assert not inspect.isabstract(model::base::IContentElement)


def test_model::base::icontentelement_constructor_exists():
    assert callable(model::base::IContentElement.__init__)


def test_model::base::icontentelement_constructor_args():
    sig = inspect.signature(model::base::IContentElement.__init__)
    params = list(sig.parameters.keys())



def test_model::base::iid_is_not_abstract():
    assert not inspect.isabstract(model::base::IID)


def test_model::base::iid_constructor_exists():
    assert callable(model::base::IID.__init__)


def test_model::base::iid_constructor_args():
    sig = inspect.signature(model::base::IID.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_model::base::iid_has_id():
    assert hasattr(model::base::IID, "id")
    descriptor = None
    for klass in model::base::IID.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_imodelconnection_is_not_abstract():
    assert not inspect.isabstract(IModelConnection)


def test_imodelconnection_constructor_exists():
    assert callable(IModelConnection.__init__)


def test_imodelconnection_constructor_args():
    sig = inspect.signature(IModelConnection.__init__)
    params = list(sig.parameters.keys())



def test_model::requirements::cegconnection_is_not_abstract():
    assert not inspect.isabstract(model::requirements::CEGConnection)


def test_model::requirements::cegconnection_constructor_exists():
    assert callable(model::requirements::CEGConnection.__init__)


def test_model::requirements::cegconnection_constructor_args():
    sig = inspect.signature(model::requirements::CEGConnection.__init__)
    params = list(sig.parameters.keys())
    assert "negate" in params, "Missing parameter 'negate'"

def test_model::requirements::cegconnection_has_negate():
    assert hasattr(model::requirements::CEGConnection, "negate")
    descriptor = None
    for klass in model::requirements::CEGConnection.__mro__:
        if "negate" in klass.__dict__:
            descriptor = klass.__dict__["negate"]
            break
    assert isinstance(descriptor, property)



def test_model::processes::processconnection_is_not_abstract():
    assert not inspect.isabstract(model::processes::ProcessConnection)


def test_model::processes::processconnection_constructor_exists():
    assert callable(model::processes::ProcessConnection.__init__)


def test_model::processes::processconnection_constructor_args():
    sig = inspect.signature(model::processes::ProcessConnection.__init__)
    params = list(sig.parameters.keys())
    assert "labelX" in params, "Missing parameter 'labelX'"
    assert "labelY" in params, "Missing parameter 'labelY'"
    assert "condition" in params, "Missing parameter 'condition'"

def test_model::processes::processconnection_has_labelX():
    assert hasattr(model::processes::ProcessConnection, "labelX")
    descriptor = None
    for klass in model::processes::ProcessConnection.__mro__:
        if "labelX" in klass.__dict__:
            descriptor = klass.__dict__["labelX"]
            break
    assert isinstance(descriptor, property)

def test_model::processes::processconnection_has_labelY():
    assert hasattr(model::processes::ProcessConnection, "labelY")
    descriptor = None
    for klass in model::processes::ProcessConnection.__mro__:
        if "labelY" in klass.__dict__:
            descriptor = klass.__dict__["labelY"]
            break
    assert isinstance(descriptor, property)

def test_model::processes::processconnection_has_condition():
    assert hasattr(model::processes::ProcessConnection, "condition")
    descriptor = None
    for klass in model::processes::ProcessConnection.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_ispecmatepositionablemodelobject_is_not_abstract():
    assert not inspect.isabstract(ISpecmatePositionableModelObject)


def test_ispecmatepositionablemodelobject_constructor_exists():
    assert callable(ISpecmatePositionableModelObject.__init__)


def test_ispecmatepositionablemodelobject_constructor_args():
    sig = inspect.signature(ISpecmatePositionableModelObject.__init__)
    params = list(sig.parameters.keys())



def test_model::base::imodelnode_is_not_abstract():
    assert not inspect.isabstract(model::base::IModelNode)


def test_model::base::imodelnode_constructor_exists():
    assert callable(model::base::IModelNode.__init__)


def test_model::base::imodelnode_constructor_args():
    sig = inspect.signature(model::base::IModelNode.__init__)
    params = list(sig.parameters.keys())



def test_imodelnode_is_not_abstract():
    assert not inspect.isabstract(IModelNode)


def test_imodelnode_constructor_exists():
    assert callable(IModelNode.__init__)


def test_imodelnode_constructor_args():
    sig = inspect.signature(IModelNode.__init__)
    params = list(sig.parameters.keys())



def test_model::requirements::cegnode_is_not_abstract():
    assert not inspect.isabstract(model::requirements::CEGNode)


def test_model::requirements::cegnode_constructor_exists():
    assert callable(model::requirements::CEGNode.__init__)


def test_model::requirements::cegnode_constructor_args():
    sig = inspect.signature(model::requirements::CEGNode.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"
    assert "type" in params, "Missing parameter 'type'"
    assert "variable" in params, "Missing parameter 'variable'"

def test_model::requirements::cegnode_has_condition():
    assert hasattr(model::requirements::CEGNode, "condition")
    descriptor = None
    for klass in model::requirements::CEGNode.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)

def test_model::requirements::cegnode_has_type():
    assert hasattr(model::requirements::CEGNode, "type")
    descriptor = None
    for klass in model::requirements::CEGNode.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_model::requirements::cegnode_has_variable():
    assert hasattr(model::requirements::CEGNode, "variable")
    descriptor = None
    for klass in model::requirements::CEGNode.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_model::processes::processnode_is_not_abstract():
    assert not inspect.isabstract(model::processes::ProcessNode)


def test_model::processes::processnode_constructor_exists():
    assert callable(model::processes::ProcessNode.__init__)


def test_model::processes::processnode_constructor_args():
    sig = inspect.signature(model::processes::ProcessNode.__init__)
    params = list(sig.parameters.keys())



def test_model::base::imodelconnection_is_not_abstract():
    assert not inspect.isabstract(model::base::IModelConnection)


def test_model::base::imodelconnection_constructor_exists():
    assert callable(model::base::IModelConnection.__init__)


def test_model::base::imodelconnection_constructor_args():
    sig = inspect.signature(model::base::IModelConnection.__init__)
    params = list(sig.parameters.keys())



def test_model::base::ispecmatepositionablemodelobject_is_not_abstract():
    assert not inspect.isabstract(model::base::ISpecmatePositionableModelObject)


def test_model::base::ispecmatepositionablemodelobject_constructor_exists():
    assert callable(model::base::ISpecmatePositionableModelObject.__init__)


def test_model::base::ispecmatepositionablemodelobject_constructor_args():
    sig = inspect.signature(model::base::ISpecmatePositionableModelObject.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_model::base::ispecmatepositionablemodelobject_has_width():
    assert hasattr(model::base::ISpecmatePositionableModelObject, "width")
    descriptor = None
    for klass in model::base::ISpecmatePositionableModelObject.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_model::base::ispecmatepositionablemodelobject_has_height():
    assert hasattr(model::base::ISpecmatePositionableModelObject, "height")
    descriptor = None
    for klass in model::base::ISpecmatePositionableModelObject.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_model::base::ispecmatepositionablemodelobject_has_x():
    assert hasattr(model::base::ISpecmatePositionableModelObject, "x")
    descriptor = None
    for klass in model::base::ISpecmatePositionableModelObject.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_model::base::ispecmatepositionablemodelobject_has_y():
    assert hasattr(model::base::ISpecmatePositionableModelObject, "y")
    descriptor = None
    for klass in model::base::ISpecmatePositionableModelObject.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_model::base::iexternal_is_not_abstract():
    assert not inspect.isabstract(model::base::IExternal)


def test_model::base::iexternal_constructor_exists():
    assert callable(model::base::IExternal.__init__)


def test_model::base::iexternal_constructor_args():
    sig = inspect.signature(model::base::IExternal.__init__)
    params = list(sig.parameters.keys())
    assert "extId" in params, "Missing parameter 'extId'"
    assert "extId2" in params, "Missing parameter 'extId2'"
    assert "live" in params, "Missing parameter 'live'"
    assert "source" in params, "Missing parameter 'source'"

def test_model::base::iexternal_has_extId():
    assert hasattr(model::base::IExternal, "extId")
    descriptor = None
    for klass in model::base::IExternal.__mro__:
        if "extId" in klass.__dict__:
            descriptor = klass.__dict__["extId"]
            break
    assert isinstance(descriptor, property)

def test_model::base::iexternal_has_extId2():
    assert hasattr(model::base::IExternal, "extId2")
    descriptor = None
    for klass in model::base::IExternal.__mro__:
        if "extId2" in klass.__dict__:
            descriptor = klass.__dict__["extId2"]
            break
    assert isinstance(descriptor, property)

def test_model::base::iexternal_has_live():
    assert hasattr(model::base::IExternal, "live")
    descriptor = None
    for klass in model::base::IExternal.__mro__:
        if "live" in klass.__dict__:
            descriptor = klass.__dict__["live"]
            break
    assert isinstance(descriptor, property)

def test_model::base::iexternal_has_source():
    assert hasattr(model::base::IExternal, "source")
    descriptor = None
    for klass in model::base::IExternal.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_model::base::idescribed_is_not_abstract():
    assert not inspect.isabstract(model::base::IDescribed)


def test_model::base::idescribed_constructor_exists():
    assert callable(model::base::IDescribed.__init__)


def test_model::base::idescribed_constructor_args():
    sig = inspect.signature(model::base::IDescribed.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_model::base::idescribed_has_description():
    assert hasattr(model::base::IDescribed, "description")
    descriptor = None
    for klass in model::base::IDescribed.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_model::base::inamed_is_not_abstract():
    assert not inspect.isabstract(model::base::INamed)


def test_model::base::inamed_constructor_exists():
    assert callable(model::base::INamed.__init__)


def test_model::base::inamed_constructor_args():
    sig = inspect.signature(model::base::INamed.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::base::inamed_has_name():
    assert hasattr(model::base::INamed, "name")
    descriptor = None
    for klass in model::base::INamed.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_nodetype_exists():
    # Check that the Enumeration exists
    assert NodeType is not None

def test_nodetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NodeType]
    expected_literals = [
        "AND",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NodeType"

def test_parametertype_exists():
    # Check that the Enumeration exists
    assert ParameterType is not None

def test_parametertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterType]
    expected_literals = [
        "INPUT",
        "OUTPUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterType"

def test_errorcode_exists():
    # Check that the Enumeration exists
    assert ErrorCode is not None

def test_errorcode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ErrorCode]
    expected_literals = [
        "scheduler",
        "noAuthorization",
        "trello",
        "noSuchService",
        "testgeneration",
        "seralization",
        "persistency",
        "search",
        "inMaintenanceMode",
        "metrics",
        "methodNotAllowed",
        "configuration",
        "hpProxy",
        "nlp",
        "jira",
        "validator",
        "invalidData",
        "restService",
        "internalProblem",
        "userSession",
        "migration",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ErrorCode"

def test_operationtype_exists():
    # Check that the Enumeration exists
    assert OperationType is not None

def test_operationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperationType]
    expected_literals = [
        "UPDATE",
        "DELETE",
        "CREATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperationType"


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
model::batch::Operation_strategy = st.builds(
    model::batch::Operation,
    type=
        safe_text
)
Operation_strategy = st.builds(
    Operation,
)
model::batch::BatchOperation_strategy = st.builds(
    model::batch::BatchOperation,
)
model::administration::ProblemDetail_strategy = st.builds(
    model::administration::ProblemDetail,
    ecode=
        safe_text,
    detail=
        safe_text,
    instance=
        safe_text,
    status=
        st.integers()
)
INamed_strategy = st.builds(
    INamed,
)
model::export::Export_strategy = st.builds(
    model::export::Export,
    content=
        safe_text,
    type=
        safe_text
)
model::history::HistoryEntry_strategy = st.builds(
    model::history::HistoryEntry,
    user=
        safe_text,
    comment=
        safe_text,
    timestamp=
        safe_text,
    deletedObjects=
        safe_text
)
HistoryEntry_strategy = st.builds(
    HistoryEntry,
)
model::history::History_strategy = st.builds(
    model::history::History,
)
model::administration::Status_strategy = st.builds(
    model::administration::Status,
    value=
        safe_text
)
model::history::Change_strategy = st.builds(
    model::history::Change,
    objectType=
        safe_text,
    oldValue=
        safe_text,
    feature=
        safe_text,
    isCreate=
        st.booleans(),
    newValue=
        safe_text,
    objectName=
        safe_text,
    isDelete=
        st.booleans()
)
Change_strategy = st.builds(
    Change,
)
TestParameter_strategy = st.builds(
    TestParameter,
)
base::IPositionable_strategy = st.builds(
    base::IPositionable,
)
ParameterAssignment_strategy = st.builds(
    ParameterAssignment,
)
IContainer_strategy = st.builds(
    IContainer,
)
model::testspecification::TestSpecification_strategy = st.builds(
    model::testspecification::TestSpecification,
)
ProcessNode_strategy = st.builds(
    ProcessNode,
)
model::processes::ProcessDecision_strategy = st.builds(
    model::processes::ProcessDecision,
)
model::processes::ProcessStart_strategy = st.builds(
    model::processes::ProcessStart,
)
model::processes::ProcessEnd_strategy = st.builds(
    model::processes::ProcessEnd,
)
model::processes::ProcessStep_strategy = st.builds(
    model::processes::ProcessStep,
    expectedOutcome=
        safe_text
)
model::processes::Process_strategy = st.builds(
    model::processes::Process,
)
base::IContentElement_strategy = st.builds(
    base::IContentElement,
)
model::testspecification::TestStep_strategy = st.builds(
    model::testspecification::TestStep,
    expectedOutcome=
        safe_text
)
base::IExternal_strategy = st.builds(
    base::IExternal,
)
base::ISpecmateModelObject_strategy = st.builds(
    base::ISpecmateModelObject,
)
model::requirements::Requirement_strategy = st.builds(
    model::requirements::Requirement,
    implementingITTeam=
        safe_text,
    tac=
        safe_text,
    numberOfTests=
        st.integers(),
    isRegressionRequirement=
        st.booleans(),
    platform=
        safe_text,
    plannedRelease=
        safe_text,
    status=
        safe_text,
    implementingUnit=
        safe_text,
    implementingBOTeam=
        safe_text
)
model::base::IRecycled_strategy = st.builds(
    model::base::IRecycled,
    hasRecycledChildren=
        st.booleans(),
    recycled=
        st.booleans()
)
ITracingElement_strategy = st.builds(
    ITracingElement,
)
model::base::ITracingElement_strategy = st.builds(
    model::base::ITracingElement,
)
model::base::IPositionable_strategy = st.builds(
    model::base::IPositionable,
    position=
        st.integers()
)
ISpecmateModelObject_strategy = st.builds(
    ISpecmateModelObject,
)
model::requirements::CEGModel_strategy = st.builds(
    model::requirements::CEGModel,
    modelRequirements=
        safe_text
)
model::base::Folder_strategy = st.builds(
    model::base::Folder,
    library=
        st.booleans()
)
base::ITracingElement_strategy = st.builds(
    base::ITracingElement,
)
base::IContainer_strategy = st.builds(
    base::IContainer,
)
model::testspecification::TestProcedure_strategy = st.builds(
    model::testspecification::TestProcedure,
    isRegressionTest=
        st.booleans()
)
model::testspecification::TestCase_strategy = st.builds(
    model::testspecification::TestCase,
    consistent=
        st.booleans()
)
model::base::ISpecmateModelObject_strategy = st.builds(
    model::base::ISpecmateModelObject,
)
IContentElement_strategy = st.builds(
    IContentElement,
)
model::testspecification::TestParameter_strategy = st.builds(
    model::testspecification::TestParameter,
    type=
        safe_text
)
model::testspecification::ParameterAssignment_strategy = st.builds(
    model::testspecification::ParameterAssignment,
    condition=
        safe_text,
    value=
        safe_text
)
model::base::IContainer_strategy = st.builds(
    model::base::IContainer,
)
base::IRecycled_strategy = st.builds(
    base::IRecycled,
)
base::IDescribed_strategy = st.builds(
    base::IDescribed,
)
base::INamed_strategy = st.builds(
    base::INamed,
)
base::IID_strategy = st.builds(
    base::IID,
)
model::base::IContentElement_strategy = st.builds(
    model::base::IContentElement,
)
model::base::IID_strategy = st.builds(
    model::base::IID,
    id=
        safe_text
)
IModelConnection_strategy = st.builds(
    IModelConnection,
)
model::requirements::CEGConnection_strategy = st.builds(
    model::requirements::CEGConnection,
    negate=
        st.booleans()
)
model::processes::ProcessConnection_strategy = st.builds(
    model::processes::ProcessConnection,
    labelX=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    labelY=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    condition=
        safe_text
)
ISpecmatePositionableModelObject_strategy = st.builds(
    ISpecmatePositionableModelObject,
)
model::base::IModelNode_strategy = st.builds(
    model::base::IModelNode,
)
IModelNode_strategy = st.builds(
    IModelNode,
)
model::requirements::CEGNode_strategy = st.builds(
    model::requirements::CEGNode,
    condition=
        safe_text,
    type=
        safe_text,
    variable=
        safe_text
)
model::processes::ProcessNode_strategy = st.builds(
    model::processes::ProcessNode,
)
model::base::IModelConnection_strategy = st.builds(
    model::base::IModelConnection,
)
model::base::ISpecmatePositionableModelObject_strategy = st.builds(
    model::base::ISpecmatePositionableModelObject,
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model::base::IExternal_strategy = st.builds(
    model::base::IExternal,
    extId=
        safe_text,
    extId2=
        safe_text,
    live=
        st.booleans(),
    source=
        safe_text
)
model::base::IDescribed_strategy = st.builds(
    model::base::IDescribed,
    description=
        safe_text
)
model::base::INamed_strategy = st.builds(
    model::base::INamed,
    name=
        safe_text
)

@given(instance=model::batch::Operation_strategy)
@settings(max_examples=50)
def test_model::batch::operation_instantiation(instance):
    assert isinstance(instance, model::batch::Operation)

@given(instance=model::batch::Operation_strategy)
def test_model::batch::operation_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::batch::Operation_strategy)
def test_model::batch::operation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=model::batch::BatchOperation_strategy)
@settings(max_examples=50)
def test_model::batch::batchoperation_instantiation(instance):
    assert isinstance(instance, model::batch::BatchOperation)

@given(instance=model::administration::ProblemDetail_strategy)
@settings(max_examples=50)
def test_model::administration::problemdetail_instantiation(instance):
    assert isinstance(instance, model::administration::ProblemDetail)

@given(instance=model::administration::ProblemDetail_strategy)
def test_model::administration::problemdetail_ecode_type(instance):
    assert isinstance(instance.ecode, str)


@given(instance=model::administration::ProblemDetail_strategy)
def test_model::administration::problemdetail_ecode_setter(instance):
    original = instance.ecode
    instance.ecode = original
    assert instance.ecode == original

@given(instance=model::administration::ProblemDetail_strategy)
def test_model::administration::problemdetail_detail_type(instance):
    assert isinstance(instance.detail, str)


@given(instance=model::administration::ProblemDetail_strategy)
def test_model::administration::problemdetail_detail_setter(instance):
    original = instance.detail
    instance.detail = original
    assert instance.detail == original

@given(instance=model::administration::ProblemDetail_strategy)
def test_model::administration::problemdetail_instance_type(instance):
    assert isinstance(instance.instance, str)


@given(instance=model::administration::ProblemDetail_strategy)
def test_model::administration::problemdetail_instance_setter(instance):
    original = instance.instance
    instance.instance = original
    assert instance.instance == original

@given(instance=model::administration::ProblemDetail_strategy)
def test_model::administration::problemdetail_status_type(instance):
    assert isinstance(instance.status, int)


@given(instance=model::administration::ProblemDetail_strategy)
def test_model::administration::problemdetail_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=INamed_strategy)
@settings(max_examples=50)
def test_inamed_instantiation(instance):
    assert isinstance(instance, INamed)

@given(instance=model::export::Export_strategy)
@settings(max_examples=50)
def test_model::export::export_instantiation(instance):
    assert isinstance(instance, model::export::Export)

@given(instance=model::export::Export_strategy)
def test_model::export::export_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=model::export::Export_strategy)
def test_model::export::export_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=model::export::Export_strategy)
def test_model::export::export_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::export::Export_strategy)
def test_model::export::export_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model::history::HistoryEntry_strategy)
@settings(max_examples=50)
def test_model::history::historyentry_instantiation(instance):
    assert isinstance(instance, model::history::HistoryEntry)

@given(instance=model::history::HistoryEntry_strategy)
def test_model::history::historyentry_user_type(instance):
    assert isinstance(instance.user, str)


@given(instance=model::history::HistoryEntry_strategy)
def test_model::history::historyentry_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original

@given(instance=model::history::HistoryEntry_strategy)
def test_model::history::historyentry_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=model::history::HistoryEntry_strategy)
def test_model::history::historyentry_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=model::history::HistoryEntry_strategy)
def test_model::history::historyentry_timestamp_type(instance):
    assert isinstance(instance.timestamp, str)


@given(instance=model::history::HistoryEntry_strategy)
def test_model::history::historyentry_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=model::history::HistoryEntry_strategy)
def test_model::history::historyentry_deletedObjects_type(instance):
    assert isinstance(instance.deletedObjects, str)


@given(instance=model::history::HistoryEntry_strategy)
def test_model::history::historyentry_deletedObjects_setter(instance):
    original = instance.deletedObjects
    instance.deletedObjects = original
    assert instance.deletedObjects == original

@given(instance=HistoryEntry_strategy)
@settings(max_examples=50)
def test_historyentry_instantiation(instance):
    assert isinstance(instance, HistoryEntry)

@given(instance=model::history::History_strategy)
@settings(max_examples=50)
def test_model::history::history_instantiation(instance):
    assert isinstance(instance, model::history::History)

@given(instance=model::administration::Status_strategy)
@settings(max_examples=50)
def test_model::administration::status_instantiation(instance):
    assert isinstance(instance, model::administration::Status)

@given(instance=model::administration::Status_strategy)
def test_model::administration::status_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=model::administration::Status_strategy)
def test_model::administration::status_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::history::Change_strategy)
@settings(max_examples=50)
def test_model::history::change_instantiation(instance):
    assert isinstance(instance, model::history::Change)

@given(instance=model::history::Change_strategy)
def test_model::history::change_objectType_type(instance):
    assert isinstance(instance.objectType, str)


@given(instance=model::history::Change_strategy)
def test_model::history::change_objectType_setter(instance):
    original = instance.objectType
    instance.objectType = original
    assert instance.objectType == original

@given(instance=model::history::Change_strategy)
def test_model::history::change_oldValue_type(instance):
    assert isinstance(instance.oldValue, str)


@given(instance=model::history::Change_strategy)
def test_model::history::change_oldValue_setter(instance):
    original = instance.oldValue
    instance.oldValue = original
    assert instance.oldValue == original

@given(instance=model::history::Change_strategy)
def test_model::history::change_feature_type(instance):
    assert isinstance(instance.feature, str)


@given(instance=model::history::Change_strategy)
def test_model::history::change_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=model::history::Change_strategy)
def test_model::history::change_isCreate_type(instance):
    assert isinstance(instance.isCreate, bool)


@given(instance=model::history::Change_strategy)
def test_model::history::change_isCreate_setter(instance):
    original = instance.isCreate
    instance.isCreate = original
    assert instance.isCreate == original

@given(instance=model::history::Change_strategy)
def test_model::history::change_newValue_type(instance):
    assert isinstance(instance.newValue, str)


@given(instance=model::history::Change_strategy)
def test_model::history::change_newValue_setter(instance):
    original = instance.newValue
    instance.newValue = original
    assert instance.newValue == original

@given(instance=model::history::Change_strategy)
def test_model::history::change_objectName_type(instance):
    assert isinstance(instance.objectName, str)


@given(instance=model::history::Change_strategy)
def test_model::history::change_objectName_setter(instance):
    original = instance.objectName
    instance.objectName = original
    assert instance.objectName == original

@given(instance=model::history::Change_strategy)
def test_model::history::change_isDelete_type(instance):
    assert isinstance(instance.isDelete, bool)


@given(instance=model::history::Change_strategy)
def test_model::history::change_isDelete_setter(instance):
    original = instance.isDelete
    instance.isDelete = original
    assert instance.isDelete == original

@given(instance=Change_strategy)
@settings(max_examples=50)
def test_change_instantiation(instance):
    assert isinstance(instance, Change)

@given(instance=TestParameter_strategy)
@settings(max_examples=50)
def test_testparameter_instantiation(instance):
    assert isinstance(instance, TestParameter)

@given(instance=base::IPositionable_strategy)
@settings(max_examples=50)
def test_base::ipositionable_instantiation(instance):
    assert isinstance(instance, base::IPositionable)

@given(instance=ParameterAssignment_strategy)
@settings(max_examples=50)
def test_parameterassignment_instantiation(instance):
    assert isinstance(instance, ParameterAssignment)

@given(instance=IContainer_strategy)
@settings(max_examples=50)
def test_icontainer_instantiation(instance):
    assert isinstance(instance, IContainer)

@given(instance=model::testspecification::TestSpecification_strategy)
@settings(max_examples=50)
def test_model::testspecification::testspecification_instantiation(instance):
    assert isinstance(instance, model::testspecification::TestSpecification)

@given(instance=ProcessNode_strategy)
@settings(max_examples=50)
def test_processnode_instantiation(instance):
    assert isinstance(instance, ProcessNode)

@given(instance=model::processes::ProcessDecision_strategy)
@settings(max_examples=50)
def test_model::processes::processdecision_instantiation(instance):
    assert isinstance(instance, model::processes::ProcessDecision)

@given(instance=model::processes::ProcessStart_strategy)
@settings(max_examples=50)
def test_model::processes::processstart_instantiation(instance):
    assert isinstance(instance, model::processes::ProcessStart)

@given(instance=model::processes::ProcessEnd_strategy)
@settings(max_examples=50)
def test_model::processes::processend_instantiation(instance):
    assert isinstance(instance, model::processes::ProcessEnd)

@given(instance=model::processes::ProcessStep_strategy)
@settings(max_examples=50)
def test_model::processes::processstep_instantiation(instance):
    assert isinstance(instance, model::processes::ProcessStep)

@given(instance=model::processes::ProcessStep_strategy)
def test_model::processes::processstep_expectedOutcome_type(instance):
    assert isinstance(instance.expectedOutcome, str)


@given(instance=model::processes::ProcessStep_strategy)
def test_model::processes::processstep_expectedOutcome_setter(instance):
    original = instance.expectedOutcome
    instance.expectedOutcome = original
    assert instance.expectedOutcome == original

@given(instance=model::processes::Process_strategy)
@settings(max_examples=50)
def test_model::processes::process_instantiation(instance):
    assert isinstance(instance, model::processes::Process)

@given(instance=base::IContentElement_strategy)
@settings(max_examples=50)
def test_base::icontentelement_instantiation(instance):
    assert isinstance(instance, base::IContentElement)

@given(instance=model::testspecification::TestStep_strategy)
@settings(max_examples=50)
def test_model::testspecification::teststep_instantiation(instance):
    assert isinstance(instance, model::testspecification::TestStep)

@given(instance=model::testspecification::TestStep_strategy)
def test_model::testspecification::teststep_expectedOutcome_type(instance):
    assert isinstance(instance.expectedOutcome, str)


@given(instance=model::testspecification::TestStep_strategy)
def test_model::testspecification::teststep_expectedOutcome_setter(instance):
    original = instance.expectedOutcome
    instance.expectedOutcome = original
    assert instance.expectedOutcome == original

@given(instance=base::IExternal_strategy)
@settings(max_examples=50)
def test_base::iexternal_instantiation(instance):
    assert isinstance(instance, base::IExternal)

@given(instance=base::ISpecmateModelObject_strategy)
@settings(max_examples=50)
def test_base::ispecmatemodelobject_instantiation(instance):
    assert isinstance(instance, base::ISpecmateModelObject)

@given(instance=model::requirements::Requirement_strategy)
@settings(max_examples=50)
def test_model::requirements::requirement_instantiation(instance):
    assert isinstance(instance, model::requirements::Requirement)

@given(instance=model::requirements::Requirement_strategy)
def test_model::requirements::requirement_implementingITTeam_type(instance):
    assert isinstance(instance.implementingITTeam, str)


@given(instance=model::requirements::Requirement_strategy)
def test_model::requirements::requirement_implementingITTeam_setter(instance):
    original = instance.implementingITTeam
    instance.implementingITTeam = original
    assert instance.implementingITTeam == original

@given(instance=model::requirements::Requirement_strategy)
def test_model::requirements::requirement_tac_type(instance):
    assert isinstance(instance.tac, str)


@given(instance=model::requirements::Requirement_strategy)
def test_model::requirements::requirement_tac_setter(instance):
    original = instance.tac
    instance.tac = original
    assert instance.tac == original

@given(instance=model::requirements::Requirement_strategy)
def test_model::requirements::requirement_numberOfTests_type(instance):
    assert isinstance(instance.numberOfTests, int)


@given(instance=model::requirements::Requirement_strategy)
def test_model::requirements::requirement_numberOfTests_setter(instance):
    original = instance.numberOfTests
    instance.numberOfTests = original
    assert instance.numberOfTests == original

@given(instance=model::requirements::Requirement_strategy)
def test_model::requirements::requirement_isRegressionRequirement_type(instance):
    assert isinstance(instance.isRegressionRequirement, bool)


@given(instance=model::requirements::Requirement_strategy)
def test_model::requirements::requirement_isRegressionRequirement_setter(instance):
    original = instance.isRegressionRequirement
    instance.isRegressionRequirement = original
    assert instance.isRegressionRequirement == original

@given(instance=model::requirements::Requirement_strategy)
def test_model::requirements::requirement_platform_type(instance):
    assert isinstance(instance.platform, str)


@given(instance=model::requirements::Requirement_strategy)
def test_model::requirements::requirement_platform_setter(instance):
    original = instance.platform
    instance.platform = original
    assert instance.platform == original

@given(instance=model::requirements::Requirement_strategy)
def test_model::requirements::requirement_plannedRelease_type(instance):
    assert isinstance(instance.plannedRelease, str)


@given(instance=model::requirements::Requirement_strategy)
def test_model::requirements::requirement_plannedRelease_setter(instance):
    original = instance.plannedRelease
    instance.plannedRelease = original
    assert instance.plannedRelease == original

@given(instance=model::requirements::Requirement_strategy)
def test_model::requirements::requirement_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=model::requirements::Requirement_strategy)
def test_model::requirements::requirement_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=model::requirements::Requirement_strategy)
def test_model::requirements::requirement_implementingUnit_type(instance):
    assert isinstance(instance.implementingUnit, str)


@given(instance=model::requirements::Requirement_strategy)
def test_model::requirements::requirement_implementingUnit_setter(instance):
    original = instance.implementingUnit
    instance.implementingUnit = original
    assert instance.implementingUnit == original

@given(instance=model::requirements::Requirement_strategy)
def test_model::requirements::requirement_implementingBOTeam_type(instance):
    assert isinstance(instance.implementingBOTeam, str)


@given(instance=model::requirements::Requirement_strategy)
def test_model::requirements::requirement_implementingBOTeam_setter(instance):
    original = instance.implementingBOTeam
    instance.implementingBOTeam = original
    assert instance.implementingBOTeam == original

@given(instance=model::base::IRecycled_strategy)
@settings(max_examples=50)
def test_model::base::irecycled_instantiation(instance):
    assert isinstance(instance, model::base::IRecycled)

@given(instance=model::base::IRecycled_strategy)
def test_model::base::irecycled_hasRecycledChildren_type(instance):
    assert isinstance(instance.hasRecycledChildren, bool)


@given(instance=model::base::IRecycled_strategy)
def test_model::base::irecycled_hasRecycledChildren_setter(instance):
    original = instance.hasRecycledChildren
    instance.hasRecycledChildren = original
    assert instance.hasRecycledChildren == original

@given(instance=model::base::IRecycled_strategy)
def test_model::base::irecycled_recycled_type(instance):
    assert isinstance(instance.recycled, bool)


@given(instance=model::base::IRecycled_strategy)
def test_model::base::irecycled_recycled_setter(instance):
    original = instance.recycled
    instance.recycled = original
    assert instance.recycled == original

@given(instance=ITracingElement_strategy)
@settings(max_examples=50)
def test_itracingelement_instantiation(instance):
    assert isinstance(instance, ITracingElement)

@given(instance=model::base::ITracingElement_strategy)
@settings(max_examples=50)
def test_model::base::itracingelement_instantiation(instance):
    assert isinstance(instance, model::base::ITracingElement)

@given(instance=model::base::IPositionable_strategy)
@settings(max_examples=50)
def test_model::base::ipositionable_instantiation(instance):
    assert isinstance(instance, model::base::IPositionable)

@given(instance=model::base::IPositionable_strategy)
def test_model::base::ipositionable_position_type(instance):
    assert isinstance(instance.position, int)


@given(instance=model::base::IPositionable_strategy)
def test_model::base::ipositionable_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=ISpecmateModelObject_strategy)
@settings(max_examples=50)
def test_ispecmatemodelobject_instantiation(instance):
    assert isinstance(instance, ISpecmateModelObject)

@given(instance=model::requirements::CEGModel_strategy)
@settings(max_examples=50)
def test_model::requirements::cegmodel_instantiation(instance):
    assert isinstance(instance, model::requirements::CEGModel)

@given(instance=model::requirements::CEGModel_strategy)
def test_model::requirements::cegmodel_modelRequirements_type(instance):
    assert isinstance(instance.modelRequirements, str)


@given(instance=model::requirements::CEGModel_strategy)
def test_model::requirements::cegmodel_modelRequirements_setter(instance):
    original = instance.modelRequirements
    instance.modelRequirements = original
    assert instance.modelRequirements == original

@given(instance=model::base::Folder_strategy)
@settings(max_examples=50)
def test_model::base::folder_instantiation(instance):
    assert isinstance(instance, model::base::Folder)

@given(instance=model::base::Folder_strategy)
def test_model::base::folder_library_type(instance):
    assert isinstance(instance.library, bool)


@given(instance=model::base::Folder_strategy)
def test_model::base::folder_library_setter(instance):
    original = instance.library
    instance.library = original
    assert instance.library == original

@given(instance=base::ITracingElement_strategy)
@settings(max_examples=50)
def test_base::itracingelement_instantiation(instance):
    assert isinstance(instance, base::ITracingElement)

@given(instance=base::IContainer_strategy)
@settings(max_examples=50)
def test_base::icontainer_instantiation(instance):
    assert isinstance(instance, base::IContainer)

@given(instance=model::testspecification::TestProcedure_strategy)
@settings(max_examples=50)
def test_model::testspecification::testprocedure_instantiation(instance):
    assert isinstance(instance, model::testspecification::TestProcedure)

@given(instance=model::testspecification::TestProcedure_strategy)
def test_model::testspecification::testprocedure_isRegressionTest_type(instance):
    assert isinstance(instance.isRegressionTest, bool)


@given(instance=model::testspecification::TestProcedure_strategy)
def test_model::testspecification::testprocedure_isRegressionTest_setter(instance):
    original = instance.isRegressionTest
    instance.isRegressionTest = original
    assert instance.isRegressionTest == original

@given(instance=model::testspecification::TestCase_strategy)
@settings(max_examples=50)
def test_model::testspecification::testcase_instantiation(instance):
    assert isinstance(instance, model::testspecification::TestCase)

@given(instance=model::testspecification::TestCase_strategy)
def test_model::testspecification::testcase_consistent_type(instance):
    assert isinstance(instance.consistent, bool)


@given(instance=model::testspecification::TestCase_strategy)
def test_model::testspecification::testcase_consistent_setter(instance):
    original = instance.consistent
    instance.consistent = original
    assert instance.consistent == original

@given(instance=model::base::ISpecmateModelObject_strategy)
@settings(max_examples=50)
def test_model::base::ispecmatemodelobject_instantiation(instance):
    assert isinstance(instance, model::base::ISpecmateModelObject)

@given(instance=IContentElement_strategy)
@settings(max_examples=50)
def test_icontentelement_instantiation(instance):
    assert isinstance(instance, IContentElement)

@given(instance=model::testspecification::TestParameter_strategy)
@settings(max_examples=50)
def test_model::testspecification::testparameter_instantiation(instance):
    assert isinstance(instance, model::testspecification::TestParameter)

@given(instance=model::testspecification::TestParameter_strategy)
def test_model::testspecification::testparameter_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::testspecification::TestParameter_strategy)
def test_model::testspecification::testparameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model::testspecification::ParameterAssignment_strategy)
@settings(max_examples=50)
def test_model::testspecification::parameterassignment_instantiation(instance):
    assert isinstance(instance, model::testspecification::ParameterAssignment)

@given(instance=model::testspecification::ParameterAssignment_strategy)
def test_model::testspecification::parameterassignment_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=model::testspecification::ParameterAssignment_strategy)
def test_model::testspecification::parameterassignment_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=model::testspecification::ParameterAssignment_strategy)
def test_model::testspecification::parameterassignment_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=model::testspecification::ParameterAssignment_strategy)
def test_model::testspecification::parameterassignment_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::base::IContainer_strategy)
@settings(max_examples=50)
def test_model::base::icontainer_instantiation(instance):
    assert isinstance(instance, model::base::IContainer)

@given(instance=base::IRecycled_strategy)
@settings(max_examples=50)
def test_base::irecycled_instantiation(instance):
    assert isinstance(instance, base::IRecycled)

@given(instance=base::IDescribed_strategy)
@settings(max_examples=50)
def test_base::idescribed_instantiation(instance):
    assert isinstance(instance, base::IDescribed)

@given(instance=base::INamed_strategy)
@settings(max_examples=50)
def test_base::inamed_instantiation(instance):
    assert isinstance(instance, base::INamed)

@given(instance=base::IID_strategy)
@settings(max_examples=50)
def test_base::iid_instantiation(instance):
    assert isinstance(instance, base::IID)

@given(instance=model::base::IContentElement_strategy)
@settings(max_examples=50)
def test_model::base::icontentelement_instantiation(instance):
    assert isinstance(instance, model::base::IContentElement)

@given(instance=model::base::IID_strategy)
@settings(max_examples=50)
def test_model::base::iid_instantiation(instance):
    assert isinstance(instance, model::base::IID)

@given(instance=model::base::IID_strategy)
def test_model::base::iid_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=model::base::IID_strategy)
def test_model::base::iid_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=IModelConnection_strategy)
@settings(max_examples=50)
def test_imodelconnection_instantiation(instance):
    assert isinstance(instance, IModelConnection)

@given(instance=model::requirements::CEGConnection_strategy)
@settings(max_examples=50)
def test_model::requirements::cegconnection_instantiation(instance):
    assert isinstance(instance, model::requirements::CEGConnection)

@given(instance=model::requirements::CEGConnection_strategy)
def test_model::requirements::cegconnection_negate_type(instance):
    assert isinstance(instance.negate, bool)


@given(instance=model::requirements::CEGConnection_strategy)
def test_model::requirements::cegconnection_negate_setter(instance):
    original = instance.negate
    instance.negate = original
    assert instance.negate == original

@given(instance=model::processes::ProcessConnection_strategy)
@settings(max_examples=50)
def test_model::processes::processconnection_instantiation(instance):
    assert isinstance(instance, model::processes::ProcessConnection)

@given(instance=model::processes::ProcessConnection_strategy)
def test_model::processes::processconnection_labelX_type(instance):
    assert isinstance(instance.labelX, float)


@given(instance=model::processes::ProcessConnection_strategy)
def test_model::processes::processconnection_labelX_setter(instance):
    original = instance.labelX
    instance.labelX = original
    assert instance.labelX == original

@given(instance=model::processes::ProcessConnection_strategy)
def test_model::processes::processconnection_labelY_type(instance):
    assert isinstance(instance.labelY, float)


@given(instance=model::processes::ProcessConnection_strategy)
def test_model::processes::processconnection_labelY_setter(instance):
    original = instance.labelY
    instance.labelY = original
    assert instance.labelY == original

@given(instance=model::processes::ProcessConnection_strategy)
def test_model::processes::processconnection_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=model::processes::ProcessConnection_strategy)
def test_model::processes::processconnection_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=ISpecmatePositionableModelObject_strategy)
@settings(max_examples=50)
def test_ispecmatepositionablemodelobject_instantiation(instance):
    assert isinstance(instance, ISpecmatePositionableModelObject)

@given(instance=model::base::IModelNode_strategy)
@settings(max_examples=50)
def test_model::base::imodelnode_instantiation(instance):
    assert isinstance(instance, model::base::IModelNode)

@given(instance=IModelNode_strategy)
@settings(max_examples=50)
def test_imodelnode_instantiation(instance):
    assert isinstance(instance, IModelNode)

@given(instance=model::requirements::CEGNode_strategy)
@settings(max_examples=50)
def test_model::requirements::cegnode_instantiation(instance):
    assert isinstance(instance, model::requirements::CEGNode)

@given(instance=model::requirements::CEGNode_strategy)
def test_model::requirements::cegnode_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=model::requirements::CEGNode_strategy)
def test_model::requirements::cegnode_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=model::requirements::CEGNode_strategy)
def test_model::requirements::cegnode_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::requirements::CEGNode_strategy)
def test_model::requirements::cegnode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model::requirements::CEGNode_strategy)
def test_model::requirements::cegnode_variable_type(instance):
    assert isinstance(instance.variable, str)


@given(instance=model::requirements::CEGNode_strategy)
def test_model::requirements::cegnode_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=model::processes::ProcessNode_strategy)
@settings(max_examples=50)
def test_model::processes::processnode_instantiation(instance):
    assert isinstance(instance, model::processes::ProcessNode)

@given(instance=model::base::IModelConnection_strategy)
@settings(max_examples=50)
def test_model::base::imodelconnection_instantiation(instance):
    assert isinstance(instance, model::base::IModelConnection)

@given(instance=model::base::ISpecmatePositionableModelObject_strategy)
@settings(max_examples=50)
def test_model::base::ispecmatepositionablemodelobject_instantiation(instance):
    assert isinstance(instance, model::base::ISpecmatePositionableModelObject)

@given(instance=model::base::ISpecmatePositionableModelObject_strategy)
def test_model::base::ispecmatepositionablemodelobject_width_type(instance):
    assert isinstance(instance.width, float)


@given(instance=model::base::ISpecmatePositionableModelObject_strategy)
def test_model::base::ispecmatepositionablemodelobject_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=model::base::ISpecmatePositionableModelObject_strategy)
def test_model::base::ispecmatepositionablemodelobject_height_type(instance):
    assert isinstance(instance.height, float)


@given(instance=model::base::ISpecmatePositionableModelObject_strategy)
def test_model::base::ispecmatepositionablemodelobject_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=model::base::ISpecmatePositionableModelObject_strategy)
def test_model::base::ispecmatepositionablemodelobject_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=model::base::ISpecmatePositionableModelObject_strategy)
def test_model::base::ispecmatepositionablemodelobject_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=model::base::ISpecmatePositionableModelObject_strategy)
def test_model::base::ispecmatepositionablemodelobject_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=model::base::ISpecmatePositionableModelObject_strategy)
def test_model::base::ispecmatepositionablemodelobject_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=model::base::IExternal_strategy)
@settings(max_examples=50)
def test_model::base::iexternal_instantiation(instance):
    assert isinstance(instance, model::base::IExternal)

@given(instance=model::base::IExternal_strategy)
def test_model::base::iexternal_extId_type(instance):
    assert isinstance(instance.extId, str)


@given(instance=model::base::IExternal_strategy)
def test_model::base::iexternal_extId_setter(instance):
    original = instance.extId
    instance.extId = original
    assert instance.extId == original

@given(instance=model::base::IExternal_strategy)
def test_model::base::iexternal_extId2_type(instance):
    assert isinstance(instance.extId2, str)


@given(instance=model::base::IExternal_strategy)
def test_model::base::iexternal_extId2_setter(instance):
    original = instance.extId2
    instance.extId2 = original
    assert instance.extId2 == original

@given(instance=model::base::IExternal_strategy)
def test_model::base::iexternal_live_type(instance):
    assert isinstance(instance.live, bool)


@given(instance=model::base::IExternal_strategy)
def test_model::base::iexternal_live_setter(instance):
    original = instance.live
    instance.live = original
    assert instance.live == original

@given(instance=model::base::IExternal_strategy)
def test_model::base::iexternal_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=model::base::IExternal_strategy)
def test_model::base::iexternal_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=model::base::IDescribed_strategy)
@settings(max_examples=50)
def test_model::base::idescribed_instantiation(instance):
    assert isinstance(instance, model::base::IDescribed)

@given(instance=model::base::IDescribed_strategy)
def test_model::base::idescribed_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=model::base::IDescribed_strategy)
def test_model::base::idescribed_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=model::base::INamed_strategy)
@settings(max_examples=50)
def test_model::base::inamed_instantiation(instance):
    assert isinstance(instance, model::base::INamed)

@given(instance=model::base::INamed_strategy)
def test_model::base::inamed_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::base::INamed_strategy)
def test_model::base::inamed_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

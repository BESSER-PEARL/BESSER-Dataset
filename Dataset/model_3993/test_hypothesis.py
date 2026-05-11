import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    xpdl1::TypeDeclarationsType,
    xpdl1::TypeDeclarationType,
    xpdl1::WorkflowProcessesType,
    xpdl1::WorkflowProcessType,
    xpdl1::TransitionRefType,
    xpdl1::TransitionType,
    xpdl1::ToolType,
    xpdl1::TransitionRestrictionType,
    xpdl1::TransitionRefsType,
    xpdl1::ResponsiblesType,
    xpdl1::TimeEstimationType,
    xpdl1::SubFlowType,
    xpdl1::SplitType,
    xpdl1::ScriptType,
    xpdl1::ParticipantsType,
    xpdl1::ParticipantType,
    xpdl1::PackageHeaderType,
    xpdl1::RedefinableHeaderType,
    xpdl1::ProcessHeaderType,
    xpdl1::ParticipantTypeType,
    xpdl1::JoinType,
    xpdl1::PackageType,
    xpdl1::NoType,
    xpdl1::MemberType,
    xpdl1::ManualType,
    xpdl1::ExternalPackageType,
    xpdl1::ExtendedAttributeType,
    xpdl1::FormalParameterType,
    xpdl1::ExternalPackagesType,
    xpdl1::EnumerationValueType,
    xpdl1::EStringToStringMapEntry,
    xpdl1::DocumentRoot,
    xpdl1::EObject,
    xpdl1::DataTypeType,
    xpdl1::DataFieldType,
    xpdl1::DataFieldsType,
    xpdl1::ConformanceClassType,
    xpdl1::ListTypeType,
    xpdl1::EnumerationTypeType,
    xpdl1::XpressionType,
    xpdl1::ConditionType,
    xpdl1::AutomaticType,
    xpdl1::ExternalReferenceType,
    xpdl1::FormalParametersType,
    xpdl1::UnionTypeType,
    xpdl1::RecordTypeType,
    xpdl1::SchemaTypeType,
    xpdl1::DeclaredTypeType,
    xpdl1::BasicTypeType,
    xpdl1::ArrayTypeType,
    xpdl1::SimulationInformationType,
    xpdl1::DeadlineType,
    xpdl1::ApplicationType,
    xpdl1::ApplicationsType,
    xpdl1::ActualParametersType,
    xpdl1::ExtendedAttributesType,
    xpdl1::TransitionRestrictionsType,
    xpdl1::TransitionsType,
    xpdl1::ActivitySetType,
    xpdl1::ActivitySetsType,
    xpdl1::FinishModeType,
    xpdl1::StartModeType,
    xpdl1::BlockActivityType,
    xpdl1::ImplementationType,
    xpdl1::RouteType,
    xpdl1::ActivityType,
    xpdl1::ActivitiesType,
    TypeType,
    ModeType,
    TypeType4,
    TypeType1,
    InstantiationType,
    TypeType3,
    DurationUnitType,
    PublicationStatusType,
    TypeType5,
    ExecutionType,
    IsArrayType,
    GraphConformanceType,
    ExecutionType1,
    AccessLevelType,
    TypeType2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_xpdl1::typedeclarationstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::TypeDeclarationsType)


def test_xpdl1::typedeclarationstype_constructor_exists():
    assert callable(xpdl1::TypeDeclarationsType.__init__)


def test_xpdl1::typedeclarationstype_constructor_args():
    sig = inspect.signature(xpdl1::TypeDeclarationsType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::typedeclarationtype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::TypeDeclarationType)


def test_xpdl1::typedeclarationtype_constructor_exists():
    assert callable(xpdl1::TypeDeclarationType.__init__)


def test_xpdl1::typedeclarationtype_constructor_args():
    sig = inspect.signature(xpdl1::TypeDeclarationType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_xpdl1::typedeclarationtype_has_id():
    assert hasattr(xpdl1::TypeDeclarationType, "id")
    descriptor = None
    for klass in xpdl1::TypeDeclarationType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::typedeclarationtype_has_description():
    assert hasattr(xpdl1::TypeDeclarationType, "description")
    descriptor = None
    for klass in xpdl1::TypeDeclarationType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::typedeclarationtype_has_name():
    assert hasattr(xpdl1::TypeDeclarationType, "name")
    descriptor = None
    for klass in xpdl1::TypeDeclarationType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::workflowprocessestype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::WorkflowProcessesType)


def test_xpdl1::workflowprocessestype_constructor_exists():
    assert callable(xpdl1::WorkflowProcessesType.__init__)


def test_xpdl1::workflowprocessestype_constructor_args():
    sig = inspect.signature(xpdl1::WorkflowProcessesType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::workflowprocesstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::WorkflowProcessType)


def test_xpdl1::workflowprocesstype_constructor_exists():
    assert callable(xpdl1::WorkflowProcessType.__init__)


def test_xpdl1::workflowprocesstype_constructor_args():
    sig = inspect.signature(xpdl1::WorkflowProcessType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "accessLevel" in params, "Missing parameter 'accessLevel'"

def test_xpdl1::workflowprocesstype_has_id():
    assert hasattr(xpdl1::WorkflowProcessType, "id")
    descriptor = None
    for klass in xpdl1::WorkflowProcessType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::workflowprocesstype_has_name():
    assert hasattr(xpdl1::WorkflowProcessType, "name")
    descriptor = None
    for klass in xpdl1::WorkflowProcessType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::workflowprocesstype_has_accessLevel():
    assert hasattr(xpdl1::WorkflowProcessType, "accessLevel")
    descriptor = None
    for klass in xpdl1::WorkflowProcessType.__mro__:
        if "accessLevel" in klass.__dict__:
            descriptor = klass.__dict__["accessLevel"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::transitionreftype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::TransitionRefType)


def test_xpdl1::transitionreftype_constructor_exists():
    assert callable(xpdl1::TransitionRefType.__init__)


def test_xpdl1::transitionreftype_constructor_args():
    sig = inspect.signature(xpdl1::TransitionRefType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_xpdl1::transitionreftype_has_id():
    assert hasattr(xpdl1::TransitionRefType, "id")
    descriptor = None
    for klass in xpdl1::TransitionRefType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::transitiontype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::TransitionType)


def test_xpdl1::transitiontype_constructor_exists():
    assert callable(xpdl1::TransitionType.__init__)


def test_xpdl1::transitiontype_constructor_args():
    sig = inspect.signature(xpdl1::TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "from_" in params, "Missing parameter 'from_'"
    assert "id" in params, "Missing parameter 'id'"
    assert "to" in params, "Missing parameter 'to'"
    assert "description" in params, "Missing parameter 'description'"

def test_xpdl1::transitiontype_has_name():
    assert hasattr(xpdl1::TransitionType, "name")
    descriptor = None
    for klass in xpdl1::TransitionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::transitiontype_has_from_():
    assert hasattr(xpdl1::TransitionType, "from_")
    descriptor = None
    for klass in xpdl1::TransitionType.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::transitiontype_has_id():
    assert hasattr(xpdl1::TransitionType, "id")
    descriptor = None
    for klass in xpdl1::TransitionType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::transitiontype_has_to():
    assert hasattr(xpdl1::TransitionType, "to")
    descriptor = None
    for klass in xpdl1::TransitionType.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::transitiontype_has_description():
    assert hasattr(xpdl1::TransitionType, "description")
    descriptor = None
    for klass in xpdl1::TransitionType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::tooltype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ToolType)


def test_xpdl1::tooltype_constructor_exists():
    assert callable(xpdl1::ToolType.__init__)


def test_xpdl1::tooltype_constructor_args():
    sig = inspect.signature(xpdl1::ToolType.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"

def test_xpdl1::tooltype_has_description():
    assert hasattr(xpdl1::ToolType, "description")
    descriptor = None
    for klass in xpdl1::ToolType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::tooltype_has_id():
    assert hasattr(xpdl1::ToolType, "id")
    descriptor = None
    for klass in xpdl1::ToolType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::tooltype_has_type():
    assert hasattr(xpdl1::ToolType, "type")
    descriptor = None
    for klass in xpdl1::ToolType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::transitionrestrictiontype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::TransitionRestrictionType)


def test_xpdl1::transitionrestrictiontype_constructor_exists():
    assert callable(xpdl1::TransitionRestrictionType.__init__)


def test_xpdl1::transitionrestrictiontype_constructor_args():
    sig = inspect.signature(xpdl1::TransitionRestrictionType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::transitionrefstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::TransitionRefsType)


def test_xpdl1::transitionrefstype_constructor_exists():
    assert callable(xpdl1::TransitionRefsType.__init__)


def test_xpdl1::transitionrefstype_constructor_args():
    sig = inspect.signature(xpdl1::TransitionRefsType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::responsiblestype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ResponsiblesType)


def test_xpdl1::responsiblestype_constructor_exists():
    assert callable(xpdl1::ResponsiblesType.__init__)


def test_xpdl1::responsiblestype_constructor_args():
    sig = inspect.signature(xpdl1::ResponsiblesType.__init__)
    params = list(sig.parameters.keys())
    assert "responsible" in params, "Missing parameter 'responsible'"

def test_xpdl1::responsiblestype_has_responsible():
    assert hasattr(xpdl1::ResponsiblesType, "responsible")
    descriptor = None
    for klass in xpdl1::ResponsiblesType.__mro__:
        if "responsible" in klass.__dict__:
            descriptor = klass.__dict__["responsible"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::timeestimationtype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::TimeEstimationType)


def test_xpdl1::timeestimationtype_constructor_exists():
    assert callable(xpdl1::TimeEstimationType.__init__)


def test_xpdl1::timeestimationtype_constructor_args():
    sig = inspect.signature(xpdl1::TimeEstimationType.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"
    assert "waitingTime" in params, "Missing parameter 'waitingTime'"
    assert "workingTime" in params, "Missing parameter 'workingTime'"

def test_xpdl1::timeestimationtype_has_duration():
    assert hasattr(xpdl1::TimeEstimationType, "duration")
    descriptor = None
    for klass in xpdl1::TimeEstimationType.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::timeestimationtype_has_waitingTime():
    assert hasattr(xpdl1::TimeEstimationType, "waitingTime")
    descriptor = None
    for klass in xpdl1::TimeEstimationType.__mro__:
        if "waitingTime" in klass.__dict__:
            descriptor = klass.__dict__["waitingTime"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::timeestimationtype_has_workingTime():
    assert hasattr(xpdl1::TimeEstimationType, "workingTime")
    descriptor = None
    for klass in xpdl1::TimeEstimationType.__mro__:
        if "workingTime" in klass.__dict__:
            descriptor = klass.__dict__["workingTime"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::subflowtype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::SubFlowType)


def test_xpdl1::subflowtype_constructor_exists():
    assert callable(xpdl1::SubFlowType.__init__)


def test_xpdl1::subflowtype_constructor_args():
    sig = inspect.signature(xpdl1::SubFlowType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "execution" in params, "Missing parameter 'execution'"

def test_xpdl1::subflowtype_has_id():
    assert hasattr(xpdl1::SubFlowType, "id")
    descriptor = None
    for klass in xpdl1::SubFlowType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::subflowtype_has_execution():
    assert hasattr(xpdl1::SubFlowType, "execution")
    descriptor = None
    for klass in xpdl1::SubFlowType.__mro__:
        if "execution" in klass.__dict__:
            descriptor = klass.__dict__["execution"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::splittype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::SplitType)


def test_xpdl1::splittype_constructor_exists():
    assert callable(xpdl1::SplitType.__init__)


def test_xpdl1::splittype_constructor_args():
    sig = inspect.signature(xpdl1::SplitType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_xpdl1::splittype_has_type():
    assert hasattr(xpdl1::SplitType, "type")
    descriptor = None
    for klass in xpdl1::SplitType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::scripttype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ScriptType)


def test_xpdl1::scripttype_constructor_exists():
    assert callable(xpdl1::ScriptType.__init__)


def test_xpdl1::scripttype_constructor_args():
    sig = inspect.signature(xpdl1::ScriptType.__init__)
    params = list(sig.parameters.keys())
    assert "grammar" in params, "Missing parameter 'grammar'"
    assert "version" in params, "Missing parameter 'version'"
    assert "type" in params, "Missing parameter 'type'"

def test_xpdl1::scripttype_has_grammar():
    assert hasattr(xpdl1::ScriptType, "grammar")
    descriptor = None
    for klass in xpdl1::ScriptType.__mro__:
        if "grammar" in klass.__dict__:
            descriptor = klass.__dict__["grammar"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::scripttype_has_version():
    assert hasattr(xpdl1::ScriptType, "version")
    descriptor = None
    for klass in xpdl1::ScriptType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::scripttype_has_type():
    assert hasattr(xpdl1::ScriptType, "type")
    descriptor = None
    for klass in xpdl1::ScriptType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::participantstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ParticipantsType)


def test_xpdl1::participantstype_constructor_exists():
    assert callable(xpdl1::ParticipantsType.__init__)


def test_xpdl1::participantstype_constructor_args():
    sig = inspect.signature(xpdl1::ParticipantsType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::participanttype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ParticipantType)


def test_xpdl1::participanttype_constructor_exists():
    assert callable(xpdl1::ParticipantType.__init__)


def test_xpdl1::participanttype_constructor_args():
    sig = inspect.signature(xpdl1::ParticipantType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"

def test_xpdl1::participanttype_has_name():
    assert hasattr(xpdl1::ParticipantType, "name")
    descriptor = None
    for klass in xpdl1::ParticipantType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::participanttype_has_description():
    assert hasattr(xpdl1::ParticipantType, "description")
    descriptor = None
    for klass in xpdl1::ParticipantType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::participanttype_has_id():
    assert hasattr(xpdl1::ParticipantType, "id")
    descriptor = None
    for klass in xpdl1::ParticipantType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::packageheadertype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::PackageHeaderType)


def test_xpdl1::packageheadertype_constructor_exists():
    assert callable(xpdl1::PackageHeaderType.__init__)


def test_xpdl1::packageheadertype_constructor_args():
    sig = inspect.signature(xpdl1::PackageHeaderType.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "created" in params, "Missing parameter 'created'"
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "priorityUnit" in params, "Missing parameter 'priorityUnit'"
    assert "costUnit" in params, "Missing parameter 'costUnit'"
    assert "xPDLVersion" in params, "Missing parameter 'xPDLVersion'"
    assert "vendor" in params, "Missing parameter 'vendor'"

def test_xpdl1::packageheadertype_has_description():
    assert hasattr(xpdl1::PackageHeaderType, "description")
    descriptor = None
    for klass in xpdl1::PackageHeaderType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::packageheadertype_has_created():
    assert hasattr(xpdl1::PackageHeaderType, "created")
    descriptor = None
    for klass in xpdl1::PackageHeaderType.__mro__:
        if "created" in klass.__dict__:
            descriptor = klass.__dict__["created"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::packageheadertype_has_documentation():
    assert hasattr(xpdl1::PackageHeaderType, "documentation")
    descriptor = None
    for klass in xpdl1::PackageHeaderType.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::packageheadertype_has_priorityUnit():
    assert hasattr(xpdl1::PackageHeaderType, "priorityUnit")
    descriptor = None
    for klass in xpdl1::PackageHeaderType.__mro__:
        if "priorityUnit" in klass.__dict__:
            descriptor = klass.__dict__["priorityUnit"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::packageheadertype_has_costUnit():
    assert hasattr(xpdl1::PackageHeaderType, "costUnit")
    descriptor = None
    for klass in xpdl1::PackageHeaderType.__mro__:
        if "costUnit" in klass.__dict__:
            descriptor = klass.__dict__["costUnit"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::packageheadertype_has_xPDLVersion():
    assert hasattr(xpdl1::PackageHeaderType, "xPDLVersion")
    descriptor = None
    for klass in xpdl1::PackageHeaderType.__mro__:
        if "xPDLVersion" in klass.__dict__:
            descriptor = klass.__dict__["xPDLVersion"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::packageheadertype_has_vendor():
    assert hasattr(xpdl1::PackageHeaderType, "vendor")
    descriptor = None
    for klass in xpdl1::PackageHeaderType.__mro__:
        if "vendor" in klass.__dict__:
            descriptor = klass.__dict__["vendor"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::redefinableheadertype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::RedefinableHeaderType)


def test_xpdl1::redefinableheadertype_constructor_exists():
    assert callable(xpdl1::RedefinableHeaderType.__init__)


def test_xpdl1::redefinableheadertype_constructor_args():
    sig = inspect.signature(xpdl1::RedefinableHeaderType.__init__)
    params = list(sig.parameters.keys())
    assert "countrykey" in params, "Missing parameter 'countrykey'"
    assert "author" in params, "Missing parameter 'author'"
    assert "codepage" in params, "Missing parameter 'codepage'"
    assert "publicationStatus" in params, "Missing parameter 'publicationStatus'"
    assert "version" in params, "Missing parameter 'version'"

def test_xpdl1::redefinableheadertype_has_countrykey():
    assert hasattr(xpdl1::RedefinableHeaderType, "countrykey")
    descriptor = None
    for klass in xpdl1::RedefinableHeaderType.__mro__:
        if "countrykey" in klass.__dict__:
            descriptor = klass.__dict__["countrykey"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::redefinableheadertype_has_author():
    assert hasattr(xpdl1::RedefinableHeaderType, "author")
    descriptor = None
    for klass in xpdl1::RedefinableHeaderType.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::redefinableheadertype_has_codepage():
    assert hasattr(xpdl1::RedefinableHeaderType, "codepage")
    descriptor = None
    for klass in xpdl1::RedefinableHeaderType.__mro__:
        if "codepage" in klass.__dict__:
            descriptor = klass.__dict__["codepage"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::redefinableheadertype_has_publicationStatus():
    assert hasattr(xpdl1::RedefinableHeaderType, "publicationStatus")
    descriptor = None
    for klass in xpdl1::RedefinableHeaderType.__mro__:
        if "publicationStatus" in klass.__dict__:
            descriptor = klass.__dict__["publicationStatus"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::redefinableheadertype_has_version():
    assert hasattr(xpdl1::RedefinableHeaderType, "version")
    descriptor = None
    for klass in xpdl1::RedefinableHeaderType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::processheadertype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ProcessHeaderType)


def test_xpdl1::processheadertype_constructor_exists():
    assert callable(xpdl1::ProcessHeaderType.__init__)


def test_xpdl1::processheadertype_constructor_args():
    sig = inspect.signature(xpdl1::ProcessHeaderType.__init__)
    params = list(sig.parameters.keys())
    assert "durationUnit" in params, "Missing parameter 'durationUnit'"
    assert "limit" in params, "Missing parameter 'limit'"
    assert "validTo" in params, "Missing parameter 'validTo'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "validFrom" in params, "Missing parameter 'validFrom'"
    assert "description" in params, "Missing parameter 'description'"
    assert "created" in params, "Missing parameter 'created'"

def test_xpdl1::processheadertype_has_durationUnit():
    assert hasattr(xpdl1::ProcessHeaderType, "durationUnit")
    descriptor = None
    for klass in xpdl1::ProcessHeaderType.__mro__:
        if "durationUnit" in klass.__dict__:
            descriptor = klass.__dict__["durationUnit"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::processheadertype_has_limit():
    assert hasattr(xpdl1::ProcessHeaderType, "limit")
    descriptor = None
    for klass in xpdl1::ProcessHeaderType.__mro__:
        if "limit" in klass.__dict__:
            descriptor = klass.__dict__["limit"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::processheadertype_has_validTo():
    assert hasattr(xpdl1::ProcessHeaderType, "validTo")
    descriptor = None
    for klass in xpdl1::ProcessHeaderType.__mro__:
        if "validTo" in klass.__dict__:
            descriptor = klass.__dict__["validTo"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::processheadertype_has_priority():
    assert hasattr(xpdl1::ProcessHeaderType, "priority")
    descriptor = None
    for klass in xpdl1::ProcessHeaderType.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::processheadertype_has_validFrom():
    assert hasattr(xpdl1::ProcessHeaderType, "validFrom")
    descriptor = None
    for klass in xpdl1::ProcessHeaderType.__mro__:
        if "validFrom" in klass.__dict__:
            descriptor = klass.__dict__["validFrom"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::processheadertype_has_description():
    assert hasattr(xpdl1::ProcessHeaderType, "description")
    descriptor = None
    for klass in xpdl1::ProcessHeaderType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::processheadertype_has_created():
    assert hasattr(xpdl1::ProcessHeaderType, "created")
    descriptor = None
    for klass in xpdl1::ProcessHeaderType.__mro__:
        if "created" in klass.__dict__:
            descriptor = klass.__dict__["created"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::participanttypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ParticipantTypeType)


def test_xpdl1::participanttypetype_constructor_exists():
    assert callable(xpdl1::ParticipantTypeType.__init__)


def test_xpdl1::participanttypetype_constructor_args():
    sig = inspect.signature(xpdl1::ParticipantTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_xpdl1::participanttypetype_has_type():
    assert hasattr(xpdl1::ParticipantTypeType, "type")
    descriptor = None
    for klass in xpdl1::ParticipantTypeType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::jointype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::JoinType)


def test_xpdl1::jointype_constructor_exists():
    assert callable(xpdl1::JoinType.__init__)


def test_xpdl1::jointype_constructor_args():
    sig = inspect.signature(xpdl1::JoinType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_xpdl1::jointype_has_type():
    assert hasattr(xpdl1::JoinType, "type")
    descriptor = None
    for klass in xpdl1::JoinType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::packagetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::PackageType)


def test_xpdl1::packagetype_constructor_exists():
    assert callable(xpdl1::PackageType.__init__)


def test_xpdl1::packagetype_constructor_args():
    sig = inspect.signature(xpdl1::PackageType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_xpdl1::packagetype_has_name():
    assert hasattr(xpdl1::PackageType, "name")
    descriptor = None
    for klass in xpdl1::PackageType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::packagetype_has_id():
    assert hasattr(xpdl1::PackageType, "id")
    descriptor = None
    for klass in xpdl1::PackageType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::notype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::NoType)


def test_xpdl1::notype_constructor_exists():
    assert callable(xpdl1::NoType.__init__)


def test_xpdl1::notype_constructor_args():
    sig = inspect.signature(xpdl1::NoType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::membertype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::MemberType)


def test_xpdl1::membertype_constructor_exists():
    assert callable(xpdl1::MemberType.__init__)


def test_xpdl1::membertype_constructor_args():
    sig = inspect.signature(xpdl1::MemberType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::manualtype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ManualType)


def test_xpdl1::manualtype_constructor_exists():
    assert callable(xpdl1::ManualType.__init__)


def test_xpdl1::manualtype_constructor_args():
    sig = inspect.signature(xpdl1::ManualType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::externalpackagetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ExternalPackageType)


def test_xpdl1::externalpackagetype_constructor_exists():
    assert callable(xpdl1::ExternalPackageType.__init__)


def test_xpdl1::externalpackagetype_constructor_args():
    sig = inspect.signature(xpdl1::ExternalPackageType.__init__)
    params = list(sig.parameters.keys())
    assert "href" in params, "Missing parameter 'href'"

def test_xpdl1::externalpackagetype_has_href():
    assert hasattr(xpdl1::ExternalPackageType, "href")
    descriptor = None
    for klass in xpdl1::ExternalPackageType.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::extendedattributetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ExtendedAttributeType)


def test_xpdl1::extendedattributetype_constructor_exists():
    assert callable(xpdl1::ExtendedAttributeType.__init__)


def test_xpdl1::extendedattributetype_constructor_args():
    sig = inspect.signature(xpdl1::ExtendedAttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"
    assert "any" in params, "Missing parameter 'any'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"

def test_xpdl1::extendedattributetype_has_name():
    assert hasattr(xpdl1::ExtendedAttributeType, "name")
    descriptor = None
    for klass in xpdl1::ExtendedAttributeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::extendedattributetype_has_value():
    assert hasattr(xpdl1::ExtendedAttributeType, "value")
    descriptor = None
    for klass in xpdl1::ExtendedAttributeType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::extendedattributetype_has_any():
    assert hasattr(xpdl1::ExtendedAttributeType, "any")
    descriptor = None
    for klass in xpdl1::ExtendedAttributeType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::extendedattributetype_has_mixed():
    assert hasattr(xpdl1::ExtendedAttributeType, "mixed")
    descriptor = None
    for klass in xpdl1::ExtendedAttributeType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::extendedattributetype_has_group():
    assert hasattr(xpdl1::ExtendedAttributeType, "group")
    descriptor = None
    for klass in xpdl1::ExtendedAttributeType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::formalparametertype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::FormalParameterType)


def test_xpdl1::formalparametertype_constructor_exists():
    assert callable(xpdl1::FormalParameterType.__init__)


def test_xpdl1::formalparametertype_constructor_args():
    sig = inspect.signature(xpdl1::FormalParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "mode" in params, "Missing parameter 'mode'"
    assert "index" in params, "Missing parameter 'index'"
    assert "description" in params, "Missing parameter 'description'"

def test_xpdl1::formalparametertype_has_id():
    assert hasattr(xpdl1::FormalParameterType, "id")
    descriptor = None
    for klass in xpdl1::FormalParameterType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::formalparametertype_has_mode():
    assert hasattr(xpdl1::FormalParameterType, "mode")
    descriptor = None
    for klass in xpdl1::FormalParameterType.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::formalparametertype_has_index():
    assert hasattr(xpdl1::FormalParameterType, "index")
    descriptor = None
    for klass in xpdl1::FormalParameterType.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::formalparametertype_has_description():
    assert hasattr(xpdl1::FormalParameterType, "description")
    descriptor = None
    for klass in xpdl1::FormalParameterType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::externalpackagestype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ExternalPackagesType)


def test_xpdl1::externalpackagestype_constructor_exists():
    assert callable(xpdl1::ExternalPackagesType.__init__)


def test_xpdl1::externalpackagestype_constructor_args():
    sig = inspect.signature(xpdl1::ExternalPackagesType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::enumerationvaluetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::EnumerationValueType)


def test_xpdl1::enumerationvaluetype_constructor_exists():
    assert callable(xpdl1::EnumerationValueType.__init__)


def test_xpdl1::enumerationvaluetype_constructor_args():
    sig = inspect.signature(xpdl1::EnumerationValueType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_xpdl1::enumerationvaluetype_has_name():
    assert hasattr(xpdl1::EnumerationValueType, "name")
    descriptor = None
    for klass in xpdl1::EnumerationValueType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(xpdl1::EStringToStringMapEntry)


def test_xpdl1::estringtostringmapentry_constructor_exists():
    assert callable(xpdl1::EStringToStringMapEntry.__init__)


def test_xpdl1::estringtostringmapentry_constructor_args():
    sig = inspect.signature(xpdl1::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::documentroot_is_not_abstract():
    assert not inspect.isabstract(xpdl1::DocumentRoot)


def test_xpdl1::documentroot_constructor_exists():
    assert callable(xpdl1::DocumentRoot.__init__)


def test_xpdl1::documentroot_constructor_args():
    sig = inspect.signature(xpdl1::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "workingTime" in params, "Missing parameter 'workingTime'"
    assert "initialValue" in params, "Missing parameter 'initialValue'"
    assert "codepage" in params, "Missing parameter 'codepage'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "waitingTime" in params, "Missing parameter 'waitingTime'"
    assert "countrykey" in params, "Missing parameter 'countrykey'"
    assert "costUnit" in params, "Missing parameter 'costUnit'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "description" in params, "Missing parameter 'description'"
    assert "priorityUnit" in params, "Missing parameter 'priorityUnit'"
    assert "xPDLVersion" in params, "Missing parameter 'xPDLVersion'"
    assert "length" in params, "Missing parameter 'length'"
    assert "validTo" in params, "Missing parameter 'validTo'"
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "version" in params, "Missing parameter 'version'"
    assert "performer" in params, "Missing parameter 'performer'"
    assert "limit" in params, "Missing parameter 'limit'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "author" in params, "Missing parameter 'author'"
    assert "vendor" in params, "Missing parameter 'vendor'"
    assert "actualParameter" in params, "Missing parameter 'actualParameter'"
    assert "responsible" in params, "Missing parameter 'responsible'"
    assert "validFrom" in params, "Missing parameter 'validFrom'"
    assert "created" in params, "Missing parameter 'created'"
    assert "cost" in params, "Missing parameter 'cost'"

def test_xpdl1::documentroot_has_workingTime():
    assert hasattr(xpdl1::DocumentRoot, "workingTime")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "workingTime" in klass.__dict__:
            descriptor = klass.__dict__["workingTime"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_initialValue():
    assert hasattr(xpdl1::DocumentRoot, "initialValue")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "initialValue" in klass.__dict__:
            descriptor = klass.__dict__["initialValue"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_codepage():
    assert hasattr(xpdl1::DocumentRoot, "codepage")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "codepage" in klass.__dict__:
            descriptor = klass.__dict__["codepage"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_icon():
    assert hasattr(xpdl1::DocumentRoot, "icon")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_duration():
    assert hasattr(xpdl1::DocumentRoot, "duration")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_waitingTime():
    assert hasattr(xpdl1::DocumentRoot, "waitingTime")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "waitingTime" in klass.__dict__:
            descriptor = klass.__dict__["waitingTime"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_countrykey():
    assert hasattr(xpdl1::DocumentRoot, "countrykey")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "countrykey" in klass.__dict__:
            descriptor = klass.__dict__["countrykey"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_costUnit():
    assert hasattr(xpdl1::DocumentRoot, "costUnit")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "costUnit" in klass.__dict__:
            descriptor = klass.__dict__["costUnit"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_priority():
    assert hasattr(xpdl1::DocumentRoot, "priority")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_description():
    assert hasattr(xpdl1::DocumentRoot, "description")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_priorityUnit():
    assert hasattr(xpdl1::DocumentRoot, "priorityUnit")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "priorityUnit" in klass.__dict__:
            descriptor = klass.__dict__["priorityUnit"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_xPDLVersion():
    assert hasattr(xpdl1::DocumentRoot, "xPDLVersion")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "xPDLVersion" in klass.__dict__:
            descriptor = klass.__dict__["xPDLVersion"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_length():
    assert hasattr(xpdl1::DocumentRoot, "length")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_validTo():
    assert hasattr(xpdl1::DocumentRoot, "validTo")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "validTo" in klass.__dict__:
            descriptor = klass.__dict__["validTo"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_documentation():
    assert hasattr(xpdl1::DocumentRoot, "documentation")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_version():
    assert hasattr(xpdl1::DocumentRoot, "version")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_performer():
    assert hasattr(xpdl1::DocumentRoot, "performer")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "performer" in klass.__dict__:
            descriptor = klass.__dict__["performer"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_limit():
    assert hasattr(xpdl1::DocumentRoot, "limit")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "limit" in klass.__dict__:
            descriptor = klass.__dict__["limit"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_mixed():
    assert hasattr(xpdl1::DocumentRoot, "mixed")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_author():
    assert hasattr(xpdl1::DocumentRoot, "author")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_vendor():
    assert hasattr(xpdl1::DocumentRoot, "vendor")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "vendor" in klass.__dict__:
            descriptor = klass.__dict__["vendor"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_actualParameter():
    assert hasattr(xpdl1::DocumentRoot, "actualParameter")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "actualParameter" in klass.__dict__:
            descriptor = klass.__dict__["actualParameter"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_responsible():
    assert hasattr(xpdl1::DocumentRoot, "responsible")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "responsible" in klass.__dict__:
            descriptor = klass.__dict__["responsible"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_validFrom():
    assert hasattr(xpdl1::DocumentRoot, "validFrom")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "validFrom" in klass.__dict__:
            descriptor = klass.__dict__["validFrom"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_created():
    assert hasattr(xpdl1::DocumentRoot, "created")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "created" in klass.__dict__:
            descriptor = klass.__dict__["created"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::documentroot_has_cost():
    assert hasattr(xpdl1::DocumentRoot, "cost")
    descriptor = None
    for klass in xpdl1::DocumentRoot.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::eobject_is_not_abstract():
    assert not inspect.isabstract(xpdl1::EObject)


def test_xpdl1::eobject_constructor_exists():
    assert callable(xpdl1::EObject.__init__)


def test_xpdl1::eobject_constructor_args():
    sig = inspect.signature(xpdl1::EObject.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::datatypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::DataTypeType)


def test_xpdl1::datatypetype_constructor_exists():
    assert callable(xpdl1::DataTypeType.__init__)


def test_xpdl1::datatypetype_constructor_args():
    sig = inspect.signature(xpdl1::DataTypeType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::datafieldtype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::DataFieldType)


def test_xpdl1::datafieldtype_constructor_exists():
    assert callable(xpdl1::DataFieldType.__init__)


def test_xpdl1::datafieldtype_constructor_args():
    sig = inspect.signature(xpdl1::DataFieldType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "length" in params, "Missing parameter 'length'"
    assert "initialValue" in params, "Missing parameter 'initialValue'"
    assert "isArray" in params, "Missing parameter 'isArray'"
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"

def test_xpdl1::datafieldtype_has_name():
    assert hasattr(xpdl1::DataFieldType, "name")
    descriptor = None
    for klass in xpdl1::DataFieldType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::datafieldtype_has_length():
    assert hasattr(xpdl1::DataFieldType, "length")
    descriptor = None
    for klass in xpdl1::DataFieldType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::datafieldtype_has_initialValue():
    assert hasattr(xpdl1::DataFieldType, "initialValue")
    descriptor = None
    for klass in xpdl1::DataFieldType.__mro__:
        if "initialValue" in klass.__dict__:
            descriptor = klass.__dict__["initialValue"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::datafieldtype_has_isArray():
    assert hasattr(xpdl1::DataFieldType, "isArray")
    descriptor = None
    for klass in xpdl1::DataFieldType.__mro__:
        if "isArray" in klass.__dict__:
            descriptor = klass.__dict__["isArray"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::datafieldtype_has_description():
    assert hasattr(xpdl1::DataFieldType, "description")
    descriptor = None
    for klass in xpdl1::DataFieldType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::datafieldtype_has_id():
    assert hasattr(xpdl1::DataFieldType, "id")
    descriptor = None
    for klass in xpdl1::DataFieldType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::datafieldstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::DataFieldsType)


def test_xpdl1::datafieldstype_constructor_exists():
    assert callable(xpdl1::DataFieldsType.__init__)


def test_xpdl1::datafieldstype_constructor_args():
    sig = inspect.signature(xpdl1::DataFieldsType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::conformanceclasstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ConformanceClassType)


def test_xpdl1::conformanceclasstype_constructor_exists():
    assert callable(xpdl1::ConformanceClassType.__init__)


def test_xpdl1::conformanceclasstype_constructor_args():
    sig = inspect.signature(xpdl1::ConformanceClassType.__init__)
    params = list(sig.parameters.keys())
    assert "graphConformance" in params, "Missing parameter 'graphConformance'"

def test_xpdl1::conformanceclasstype_has_graphConformance():
    assert hasattr(xpdl1::ConformanceClassType, "graphConformance")
    descriptor = None
    for klass in xpdl1::ConformanceClassType.__mro__:
        if "graphConformance" in klass.__dict__:
            descriptor = klass.__dict__["graphConformance"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::listtypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ListTypeType)


def test_xpdl1::listtypetype_constructor_exists():
    assert callable(xpdl1::ListTypeType.__init__)


def test_xpdl1::listtypetype_constructor_args():
    sig = inspect.signature(xpdl1::ListTypeType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::enumerationtypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::EnumerationTypeType)


def test_xpdl1::enumerationtypetype_constructor_exists():
    assert callable(xpdl1::EnumerationTypeType.__init__)


def test_xpdl1::enumerationtypetype_constructor_args():
    sig = inspect.signature(xpdl1::EnumerationTypeType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::xpressiontype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::XpressionType)


def test_xpdl1::xpressiontype_constructor_exists():
    assert callable(xpdl1::XpressionType.__init__)


def test_xpdl1::xpressiontype_constructor_args():
    sig = inspect.signature(xpdl1::XpressionType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"

def test_xpdl1::xpressiontype_has_any():
    assert hasattr(xpdl1::XpressionType, "any")
    descriptor = None
    for klass in xpdl1::XpressionType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::xpressiontype_has_mixed():
    assert hasattr(xpdl1::XpressionType, "mixed")
    descriptor = None
    for klass in xpdl1::XpressionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::xpressiontype_has_group():
    assert hasattr(xpdl1::XpressionType, "group")
    descriptor = None
    for klass in xpdl1::XpressionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::conditiontype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ConditionType)


def test_xpdl1::conditiontype_constructor_exists():
    assert callable(xpdl1::ConditionType.__init__)


def test_xpdl1::conditiontype_constructor_args():
    sig = inspect.signature(xpdl1::ConditionType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "group" in params, "Missing parameter 'group'"

def test_xpdl1::conditiontype_has_mixed():
    assert hasattr(xpdl1::ConditionType, "mixed")
    descriptor = None
    for klass in xpdl1::ConditionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::conditiontype_has_type():
    assert hasattr(xpdl1::ConditionType, "type")
    descriptor = None
    for klass in xpdl1::ConditionType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::conditiontype_has_group():
    assert hasattr(xpdl1::ConditionType, "group")
    descriptor = None
    for klass in xpdl1::ConditionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::automatictype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::AutomaticType)


def test_xpdl1::automatictype_constructor_exists():
    assert callable(xpdl1::AutomaticType.__init__)


def test_xpdl1::automatictype_constructor_args():
    sig = inspect.signature(xpdl1::AutomaticType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::externalreferencetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ExternalReferenceType)


def test_xpdl1::externalreferencetype_constructor_exists():
    assert callable(xpdl1::ExternalReferenceType.__init__)


def test_xpdl1::externalreferencetype_constructor_args():
    sig = inspect.signature(xpdl1::ExternalReferenceType.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "location" in params, "Missing parameter 'location'"
    assert "xref" in params, "Missing parameter 'xref'"

def test_xpdl1::externalreferencetype_has_namespace():
    assert hasattr(xpdl1::ExternalReferenceType, "namespace")
    descriptor = None
    for klass in xpdl1::ExternalReferenceType.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::externalreferencetype_has_location():
    assert hasattr(xpdl1::ExternalReferenceType, "location")
    descriptor = None
    for klass in xpdl1::ExternalReferenceType.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::externalreferencetype_has_xref():
    assert hasattr(xpdl1::ExternalReferenceType, "xref")
    descriptor = None
    for klass in xpdl1::ExternalReferenceType.__mro__:
        if "xref" in klass.__dict__:
            descriptor = klass.__dict__["xref"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::formalparameterstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::FormalParametersType)


def test_xpdl1::formalparameterstype_constructor_exists():
    assert callable(xpdl1::FormalParametersType.__init__)


def test_xpdl1::formalparameterstype_constructor_args():
    sig = inspect.signature(xpdl1::FormalParametersType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::uniontypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::UnionTypeType)


def test_xpdl1::uniontypetype_constructor_exists():
    assert callable(xpdl1::UnionTypeType.__init__)


def test_xpdl1::uniontypetype_constructor_args():
    sig = inspect.signature(xpdl1::UnionTypeType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::recordtypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::RecordTypeType)


def test_xpdl1::recordtypetype_constructor_exists():
    assert callable(xpdl1::RecordTypeType.__init__)


def test_xpdl1::recordtypetype_constructor_args():
    sig = inspect.signature(xpdl1::RecordTypeType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::schematypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::SchemaTypeType)


def test_xpdl1::schematypetype_constructor_exists():
    assert callable(xpdl1::SchemaTypeType.__init__)


def test_xpdl1::schematypetype_constructor_args():
    sig = inspect.signature(xpdl1::SchemaTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"

def test_xpdl1::schematypetype_has_any():
    assert hasattr(xpdl1::SchemaTypeType, "any")
    descriptor = None
    for klass in xpdl1::SchemaTypeType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::declaredtypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::DeclaredTypeType)


def test_xpdl1::declaredtypetype_constructor_exists():
    assert callable(xpdl1::DeclaredTypeType.__init__)


def test_xpdl1::declaredtypetype_constructor_args():
    sig = inspect.signature(xpdl1::DeclaredTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_xpdl1::declaredtypetype_has_id():
    assert hasattr(xpdl1::DeclaredTypeType, "id")
    descriptor = None
    for klass in xpdl1::DeclaredTypeType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::basictypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::BasicTypeType)


def test_xpdl1::basictypetype_constructor_exists():
    assert callable(xpdl1::BasicTypeType.__init__)


def test_xpdl1::basictypetype_constructor_args():
    sig = inspect.signature(xpdl1::BasicTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_xpdl1::basictypetype_has_type():
    assert hasattr(xpdl1::BasicTypeType, "type")
    descriptor = None
    for klass in xpdl1::BasicTypeType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::arraytypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ArrayTypeType)


def test_xpdl1::arraytypetype_constructor_exists():
    assert callable(xpdl1::ArrayTypeType.__init__)


def test_xpdl1::arraytypetype_constructor_args():
    sig = inspect.signature(xpdl1::ArrayTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "lowerIndex" in params, "Missing parameter 'lowerIndex'"
    assert "upperIndex" in params, "Missing parameter 'upperIndex'"

def test_xpdl1::arraytypetype_has_lowerIndex():
    assert hasattr(xpdl1::ArrayTypeType, "lowerIndex")
    descriptor = None
    for klass in xpdl1::ArrayTypeType.__mro__:
        if "lowerIndex" in klass.__dict__:
            descriptor = klass.__dict__["lowerIndex"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::arraytypetype_has_upperIndex():
    assert hasattr(xpdl1::ArrayTypeType, "upperIndex")
    descriptor = None
    for klass in xpdl1::ArrayTypeType.__mro__:
        if "upperIndex" in klass.__dict__:
            descriptor = klass.__dict__["upperIndex"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::simulationinformationtype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::SimulationInformationType)


def test_xpdl1::simulationinformationtype_constructor_exists():
    assert callable(xpdl1::SimulationInformationType.__init__)


def test_xpdl1::simulationinformationtype_constructor_args():
    sig = inspect.signature(xpdl1::SimulationInformationType.__init__)
    params = list(sig.parameters.keys())
    assert "cost" in params, "Missing parameter 'cost'"
    assert "instantiation" in params, "Missing parameter 'instantiation'"

def test_xpdl1::simulationinformationtype_has_cost():
    assert hasattr(xpdl1::SimulationInformationType, "cost")
    descriptor = None
    for klass in xpdl1::SimulationInformationType.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::simulationinformationtype_has_instantiation():
    assert hasattr(xpdl1::SimulationInformationType, "instantiation")
    descriptor = None
    for klass in xpdl1::SimulationInformationType.__mro__:
        if "instantiation" in klass.__dict__:
            descriptor = klass.__dict__["instantiation"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::deadlinetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::DeadlineType)


def test_xpdl1::deadlinetype_constructor_exists():
    assert callable(xpdl1::DeadlineType.__init__)


def test_xpdl1::deadlinetype_constructor_args():
    sig = inspect.signature(xpdl1::DeadlineType.__init__)
    params = list(sig.parameters.keys())
    assert "execution" in params, "Missing parameter 'execution'"

def test_xpdl1::deadlinetype_has_execution():
    assert hasattr(xpdl1::DeadlineType, "execution")
    descriptor = None
    for klass in xpdl1::DeadlineType.__mro__:
        if "execution" in klass.__dict__:
            descriptor = klass.__dict__["execution"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::applicationtype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ApplicationType)


def test_xpdl1::applicationtype_constructor_exists():
    assert callable(xpdl1::ApplicationType.__init__)


def test_xpdl1::applicationtype_constructor_args():
    sig = inspect.signature(xpdl1::ApplicationType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"

def test_xpdl1::applicationtype_has_name():
    assert hasattr(xpdl1::ApplicationType, "name")
    descriptor = None
    for klass in xpdl1::ApplicationType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::applicationtype_has_description():
    assert hasattr(xpdl1::ApplicationType, "description")
    descriptor = None
    for klass in xpdl1::ApplicationType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::applicationtype_has_id():
    assert hasattr(xpdl1::ApplicationType, "id")
    descriptor = None
    for klass in xpdl1::ApplicationType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::applicationstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ApplicationsType)


def test_xpdl1::applicationstype_constructor_exists():
    assert callable(xpdl1::ApplicationsType.__init__)


def test_xpdl1::applicationstype_constructor_args():
    sig = inspect.signature(xpdl1::ApplicationsType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::actualparameterstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ActualParametersType)


def test_xpdl1::actualparameterstype_constructor_exists():
    assert callable(xpdl1::ActualParametersType.__init__)


def test_xpdl1::actualparameterstype_constructor_args():
    sig = inspect.signature(xpdl1::ActualParametersType.__init__)
    params = list(sig.parameters.keys())
    assert "actualParameter" in params, "Missing parameter 'actualParameter'"

def test_xpdl1::actualparameterstype_has_actualParameter():
    assert hasattr(xpdl1::ActualParametersType, "actualParameter")
    descriptor = None
    for klass in xpdl1::ActualParametersType.__mro__:
        if "actualParameter" in klass.__dict__:
            descriptor = klass.__dict__["actualParameter"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::extendedattributestype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ExtendedAttributesType)


def test_xpdl1::extendedattributestype_constructor_exists():
    assert callable(xpdl1::ExtendedAttributesType.__init__)


def test_xpdl1::extendedattributestype_constructor_args():
    sig = inspect.signature(xpdl1::ExtendedAttributesType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::transitionrestrictionstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::TransitionRestrictionsType)


def test_xpdl1::transitionrestrictionstype_constructor_exists():
    assert callable(xpdl1::TransitionRestrictionsType.__init__)


def test_xpdl1::transitionrestrictionstype_constructor_args():
    sig = inspect.signature(xpdl1::TransitionRestrictionsType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::transitionstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::TransitionsType)


def test_xpdl1::transitionstype_constructor_exists():
    assert callable(xpdl1::TransitionsType.__init__)


def test_xpdl1::transitionstype_constructor_args():
    sig = inspect.signature(xpdl1::TransitionsType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::activitysettype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ActivitySetType)


def test_xpdl1::activitysettype_constructor_exists():
    assert callable(xpdl1::ActivitySetType.__init__)


def test_xpdl1::activitysettype_constructor_args():
    sig = inspect.signature(xpdl1::ActivitySetType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_xpdl1::activitysettype_has_id():
    assert hasattr(xpdl1::ActivitySetType, "id")
    descriptor = None
    for klass in xpdl1::ActivitySetType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::activitysetstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ActivitySetsType)


def test_xpdl1::activitysetstype_constructor_exists():
    assert callable(xpdl1::ActivitySetsType.__init__)


def test_xpdl1::activitysetstype_constructor_args():
    sig = inspect.signature(xpdl1::ActivitySetsType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::finishmodetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::FinishModeType)


def test_xpdl1::finishmodetype_constructor_exists():
    assert callable(xpdl1::FinishModeType.__init__)


def test_xpdl1::finishmodetype_constructor_args():
    sig = inspect.signature(xpdl1::FinishModeType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::startmodetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::StartModeType)


def test_xpdl1::startmodetype_constructor_exists():
    assert callable(xpdl1::StartModeType.__init__)


def test_xpdl1::startmodetype_constructor_args():
    sig = inspect.signature(xpdl1::StartModeType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::blockactivitytype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::BlockActivityType)


def test_xpdl1::blockactivitytype_constructor_exists():
    assert callable(xpdl1::BlockActivityType.__init__)


def test_xpdl1::blockactivitytype_constructor_args():
    sig = inspect.signature(xpdl1::BlockActivityType.__init__)
    params = list(sig.parameters.keys())
    assert "blockId" in params, "Missing parameter 'blockId'"

def test_xpdl1::blockactivitytype_has_blockId():
    assert hasattr(xpdl1::BlockActivityType, "blockId")
    descriptor = None
    for klass in xpdl1::BlockActivityType.__mro__:
        if "blockId" in klass.__dict__:
            descriptor = klass.__dict__["blockId"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::implementationtype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ImplementationType)


def test_xpdl1::implementationtype_constructor_exists():
    assert callable(xpdl1::ImplementationType.__init__)


def test_xpdl1::implementationtype_constructor_args():
    sig = inspect.signature(xpdl1::ImplementationType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::routetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::RouteType)


def test_xpdl1::routetype_constructor_exists():
    assert callable(xpdl1::RouteType.__init__)


def test_xpdl1::routetype_constructor_args():
    sig = inspect.signature(xpdl1::RouteType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1::activitytype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ActivityType)


def test_xpdl1::activitytype_constructor_exists():
    assert callable(xpdl1::ActivityType.__init__)


def test_xpdl1::activitytype_constructor_args():
    sig = inspect.signature(xpdl1::ActivityType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "performer" in params, "Missing parameter 'performer'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "limit" in params, "Missing parameter 'limit'"
    assert "documentation" in params, "Missing parameter 'documentation'"

def test_xpdl1::activitytype_has_id():
    assert hasattr(xpdl1::ActivityType, "id")
    descriptor = None
    for klass in xpdl1::ActivityType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::activitytype_has_performer():
    assert hasattr(xpdl1::ActivityType, "performer")
    descriptor = None
    for klass in xpdl1::ActivityType.__mro__:
        if "performer" in klass.__dict__:
            descriptor = klass.__dict__["performer"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::activitytype_has_icon():
    assert hasattr(xpdl1::ActivityType, "icon")
    descriptor = None
    for klass in xpdl1::ActivityType.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::activitytype_has_description():
    assert hasattr(xpdl1::ActivityType, "description")
    descriptor = None
    for klass in xpdl1::ActivityType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::activitytype_has_name():
    assert hasattr(xpdl1::ActivityType, "name")
    descriptor = None
    for klass in xpdl1::ActivityType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::activitytype_has_priority():
    assert hasattr(xpdl1::ActivityType, "priority")
    descriptor = None
    for klass in xpdl1::ActivityType.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::activitytype_has_limit():
    assert hasattr(xpdl1::ActivityType, "limit")
    descriptor = None
    for klass in xpdl1::ActivityType.__mro__:
        if "limit" in klass.__dict__:
            descriptor = klass.__dict__["limit"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1::activitytype_has_documentation():
    assert hasattr(xpdl1::ActivityType, "documentation")
    descriptor = None
    for klass in xpdl1::ActivityType.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1::activitiestype_is_not_abstract():
    assert not inspect.isabstract(xpdl1::ActivitiesType)


def test_xpdl1::activitiestype_constructor_exists():
    assert callable(xpdl1::ActivitiesType.__init__)


def test_xpdl1::activitiestype_constructor_args():
    sig = inspect.signature(xpdl1::ActivitiesType.__init__)
    params = list(sig.parameters.keys())

def test_typetype_exists():
    # Check that the Enumeration exists
    assert TypeType is not None

def test_typetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeType]
    expected_literals = [
        "XOR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeType"

def test_modetype_exists():
    # Check that the Enumeration exists
    assert ModeType is not None

def test_modetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ModeType]
    expected_literals = [
        "INOUT",
        "IN",
        "OUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModeType"

def test_typetype4_exists():
    # Check that the Enumeration exists
    assert TypeType4 is not None

def test_typetype4_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeType4]
    expected_literals = [
        "AND",
        "XOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeType4"

def test_typetype1_exists():
    # Check that the Enumeration exists
    assert TypeType1 is not None

def test_typetype1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeType1]
    expected_literals = [
        "RESOURCESET",
        "ORGANIZATIONALUNIT",
        "SYSTEM",
        "RESOURCE",
        "HUMAN",
        "ROLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeType1"

def test_instantiationtype_exists():
    # Check that the Enumeration exists
    assert InstantiationType is not None

def test_instantiationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InstantiationType]
    expected_literals = [
        "ONCE",
        "MULTIPLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InstantiationType"

def test_typetype3_exists():
    # Check that the Enumeration exists
    assert TypeType3 is not None

def test_typetype3_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeType3]
    expected_literals = [
        "PERFORMER",
        "DATETIME",
        "BOOLEAN",
        "STRING",
        "INTEGER",
        "FLOAT",
        "REFERENCE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeType3"

def test_durationunittype_exists():
    # Check that the Enumeration exists
    assert DurationUnitType is not None

def test_durationunittype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DurationUnitType]
    expected_literals = [
        "Y",
        "m1",
        "M",
        "D",
        "s",
        "h",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DurationUnitType"

def test_publicationstatustype_exists():
    # Check that the Enumeration exists
    assert PublicationStatusType is not None

def test_publicationstatustype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PublicationStatusType]
    expected_literals = [
        "RELEASED",
        "UNDERTEST",
        "UNDERREVISION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PublicationStatusType"

def test_typetype5_exists():
    # Check that the Enumeration exists
    assert TypeType5 is not None

def test_typetype5_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeType5]
    expected_literals = [
        "APPLICATION",
        "PROCEDURE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeType5"

def test_executiontype_exists():
    # Check that the Enumeration exists
    assert ExecutionType is not None

def test_executiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExecutionType]
    expected_literals = [
        "SYNCHR",
        "ASYNCHR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExecutionType"

def test_isarraytype_exists():
    # Check that the Enumeration exists
    assert IsArrayType is not None

def test_isarraytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IsArrayType]
    expected_literals = [
        "TRUE",
        "FALSE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IsArrayType"

def test_graphconformancetype_exists():
    # Check that the Enumeration exists
    assert GraphConformanceType is not None

def test_graphconformancetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GraphConformanceType]
    expected_literals = [
        "LOOPBLOCKED",
        "NONBLOCKED",
        "FULLBLOCKED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GraphConformanceType"

def test_executiontype1_exists():
    # Check that the Enumeration exists
    assert ExecutionType1 is not None

def test_executiontype1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExecutionType1]
    expected_literals = [
        "SYNCHR",
        "ASYNCHR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExecutionType1"

def test_accessleveltype_exists():
    # Check that the Enumeration exists
    assert AccessLevelType is not None

def test_accessleveltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessLevelType]
    expected_literals = [
        "PUBLIC",
        "PRIVATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessLevelType"

def test_typetype2_exists():
    # Check that the Enumeration exists
    assert TypeType2 is not None

def test_typetype2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeType2]
    expected_literals = [
        "CONDITION",
        "OTHERWISE",
        "EXCEPTION",
        "DEFAULTEXCEPTION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeType2"


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
xpdl1::TypeDeclarationsType_strategy = st.builds(
    xpdl1::TypeDeclarationsType,
)
xpdl1::TypeDeclarationType_strategy = st.builds(
    xpdl1::TypeDeclarationType,
    id=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
xpdl1::WorkflowProcessesType_strategy = st.builds(
    xpdl1::WorkflowProcessesType,
)
xpdl1::WorkflowProcessType_strategy = st.builds(
    xpdl1::WorkflowProcessType,
    id=
        safe_text,
    name=
        safe_text,
    accessLevel=
        safe_text
)
xpdl1::TransitionRefType_strategy = st.builds(
    xpdl1::TransitionRefType,
    id=
        safe_text
)
xpdl1::TransitionType_strategy = st.builds(
    xpdl1::TransitionType,
    name=
        safe_text,
    from_=
        safe_text,
    id=
        safe_text,
    to=
        safe_text,
    description=
        safe_text
)
xpdl1::ToolType_strategy = st.builds(
    xpdl1::ToolType,
    description=
        safe_text,
    id=
        safe_text,
    type=
        safe_text
)
xpdl1::TransitionRestrictionType_strategy = st.builds(
    xpdl1::TransitionRestrictionType,
)
xpdl1::TransitionRefsType_strategy = st.builds(
    xpdl1::TransitionRefsType,
)
xpdl1::ResponsiblesType_strategy = st.builds(
    xpdl1::ResponsiblesType,
    responsible=
        safe_text
)
xpdl1::TimeEstimationType_strategy = st.builds(
    xpdl1::TimeEstimationType,
    duration=
        safe_text,
    waitingTime=
        safe_text,
    workingTime=
        safe_text
)
xpdl1::SubFlowType_strategy = st.builds(
    xpdl1::SubFlowType,
    id=
        safe_text,
    execution=
        safe_text
)
xpdl1::SplitType_strategy = st.builds(
    xpdl1::SplitType,
    type=
        safe_text
)
xpdl1::ScriptType_strategy = st.builds(
    xpdl1::ScriptType,
    grammar=
        safe_text,
    version=
        safe_text,
    type=
        safe_text
)
xpdl1::ParticipantsType_strategy = st.builds(
    xpdl1::ParticipantsType,
)
xpdl1::ParticipantType_strategy = st.builds(
    xpdl1::ParticipantType,
    name=
        safe_text,
    description=
        safe_text,
    id=
        safe_text
)
xpdl1::PackageHeaderType_strategy = st.builds(
    xpdl1::PackageHeaderType,
    description=
        safe_text,
    created=
        safe_text,
    documentation=
        safe_text,
    priorityUnit=
        safe_text,
    costUnit=
        safe_text,
    xPDLVersion=
        safe_text,
    vendor=
        safe_text
)
xpdl1::RedefinableHeaderType_strategy = st.builds(
    xpdl1::RedefinableHeaderType,
    countrykey=
        safe_text,
    author=
        safe_text,
    codepage=
        safe_text,
    publicationStatus=
        safe_text,
    version=
        safe_text
)
xpdl1::ProcessHeaderType_strategy = st.builds(
    xpdl1::ProcessHeaderType,
    durationUnit=
        safe_text,
    limit=
        safe_text,
    validTo=
        safe_text,
    priority=
        safe_text,
    validFrom=
        safe_text,
    description=
        safe_text,
    created=
        safe_text
)
xpdl1::ParticipantTypeType_strategy = st.builds(
    xpdl1::ParticipantTypeType,
    type=
        safe_text
)
xpdl1::JoinType_strategy = st.builds(
    xpdl1::JoinType,
    type=
        safe_text
)
xpdl1::PackageType_strategy = st.builds(
    xpdl1::PackageType,
    name=
        safe_text,
    id=
        safe_text
)
xpdl1::NoType_strategy = st.builds(
    xpdl1::NoType,
)
xpdl1::MemberType_strategy = st.builds(
    xpdl1::MemberType,
)
xpdl1::ManualType_strategy = st.builds(
    xpdl1::ManualType,
)
xpdl1::ExternalPackageType_strategy = st.builds(
    xpdl1::ExternalPackageType,
    href=
        safe_text
)
xpdl1::ExtendedAttributeType_strategy = st.builds(
    xpdl1::ExtendedAttributeType,
    name=
        safe_text,
    value=
        safe_text,
    any=
        safe_text,
    mixed=
        safe_text,
    group=
        safe_text
)
xpdl1::FormalParameterType_strategy = st.builds(
    xpdl1::FormalParameterType,
    id=
        safe_text,
    mode=
        safe_text,
    index=
        safe_text,
    description=
        safe_text
)
xpdl1::ExternalPackagesType_strategy = st.builds(
    xpdl1::ExternalPackagesType,
)
xpdl1::EnumerationValueType_strategy = st.builds(
    xpdl1::EnumerationValueType,
    name=
        safe_text
)
xpdl1::EStringToStringMapEntry_strategy = st.builds(
    xpdl1::EStringToStringMapEntry,
)
xpdl1::DocumentRoot_strategy = st.builds(
    xpdl1::DocumentRoot,
    workingTime=
        safe_text,
    initialValue=
        safe_text,
    codepage=
        safe_text,
    icon=
        safe_text,
    duration=
        safe_text,
    waitingTime=
        safe_text,
    countrykey=
        safe_text,
    costUnit=
        safe_text,
    priority=
        safe_text,
    description=
        safe_text,
    priorityUnit=
        safe_text,
    xPDLVersion=
        safe_text,
    length=
        safe_text,
    validTo=
        safe_text,
    documentation=
        safe_text,
    version=
        safe_text,
    performer=
        safe_text,
    limit=
        safe_text,
    mixed=
        safe_text,
    author=
        safe_text,
    vendor=
        safe_text,
    actualParameter=
        safe_text,
    responsible=
        safe_text,
    validFrom=
        safe_text,
    created=
        safe_text,
    cost=
        safe_text
)
xpdl1::EObject_strategy = st.builds(
    xpdl1::EObject,
)
xpdl1::DataTypeType_strategy = st.builds(
    xpdl1::DataTypeType,
)
xpdl1::DataFieldType_strategy = st.builds(
    xpdl1::DataFieldType,
    name=
        safe_text,
    length=
        safe_text,
    initialValue=
        safe_text,
    isArray=
        safe_text,
    description=
        safe_text,
    id=
        safe_text
)
xpdl1::DataFieldsType_strategy = st.builds(
    xpdl1::DataFieldsType,
)
xpdl1::ConformanceClassType_strategy = st.builds(
    xpdl1::ConformanceClassType,
    graphConformance=
        safe_text
)
xpdl1::ListTypeType_strategy = st.builds(
    xpdl1::ListTypeType,
)
xpdl1::EnumerationTypeType_strategy = st.builds(
    xpdl1::EnumerationTypeType,
)
xpdl1::XpressionType_strategy = st.builds(
    xpdl1::XpressionType,
    any=
        safe_text,
    mixed=
        safe_text,
    group=
        safe_text
)
xpdl1::ConditionType_strategy = st.builds(
    xpdl1::ConditionType,
    mixed=
        safe_text,
    type=
        safe_text,
    group=
        safe_text
)
xpdl1::AutomaticType_strategy = st.builds(
    xpdl1::AutomaticType,
)
xpdl1::ExternalReferenceType_strategy = st.builds(
    xpdl1::ExternalReferenceType,
    namespace=
        safe_text,
    location=
        safe_text,
    xref=
        safe_text
)
xpdl1::FormalParametersType_strategy = st.builds(
    xpdl1::FormalParametersType,
)
xpdl1::UnionTypeType_strategy = st.builds(
    xpdl1::UnionTypeType,
)
xpdl1::RecordTypeType_strategy = st.builds(
    xpdl1::RecordTypeType,
)
xpdl1::SchemaTypeType_strategy = st.builds(
    xpdl1::SchemaTypeType,
    any=
        safe_text
)
xpdl1::DeclaredTypeType_strategy = st.builds(
    xpdl1::DeclaredTypeType,
    id=
        safe_text
)
xpdl1::BasicTypeType_strategy = st.builds(
    xpdl1::BasicTypeType,
    type=
        safe_text
)
xpdl1::ArrayTypeType_strategy = st.builds(
    xpdl1::ArrayTypeType,
    lowerIndex=
        safe_text,
    upperIndex=
        safe_text
)
xpdl1::SimulationInformationType_strategy = st.builds(
    xpdl1::SimulationInformationType,
    cost=
        safe_text,
    instantiation=
        safe_text
)
xpdl1::DeadlineType_strategy = st.builds(
    xpdl1::DeadlineType,
    execution=
        safe_text
)
xpdl1::ApplicationType_strategy = st.builds(
    xpdl1::ApplicationType,
    name=
        safe_text,
    description=
        safe_text,
    id=
        safe_text
)
xpdl1::ApplicationsType_strategy = st.builds(
    xpdl1::ApplicationsType,
)
xpdl1::ActualParametersType_strategy = st.builds(
    xpdl1::ActualParametersType,
    actualParameter=
        safe_text
)
xpdl1::ExtendedAttributesType_strategy = st.builds(
    xpdl1::ExtendedAttributesType,
)
xpdl1::TransitionRestrictionsType_strategy = st.builds(
    xpdl1::TransitionRestrictionsType,
)
xpdl1::TransitionsType_strategy = st.builds(
    xpdl1::TransitionsType,
)
xpdl1::ActivitySetType_strategy = st.builds(
    xpdl1::ActivitySetType,
    id=
        safe_text
)
xpdl1::ActivitySetsType_strategy = st.builds(
    xpdl1::ActivitySetsType,
)
xpdl1::FinishModeType_strategy = st.builds(
    xpdl1::FinishModeType,
)
xpdl1::StartModeType_strategy = st.builds(
    xpdl1::StartModeType,
)
xpdl1::BlockActivityType_strategy = st.builds(
    xpdl1::BlockActivityType,
    blockId=
        safe_text
)
xpdl1::ImplementationType_strategy = st.builds(
    xpdl1::ImplementationType,
)
xpdl1::RouteType_strategy = st.builds(
    xpdl1::RouteType,
)
xpdl1::ActivityType_strategy = st.builds(
    xpdl1::ActivityType,
    id=
        safe_text,
    performer=
        safe_text,
    icon=
        safe_text,
    description=
        safe_text,
    name=
        safe_text,
    priority=
        safe_text,
    limit=
        safe_text,
    documentation=
        safe_text
)
xpdl1::ActivitiesType_strategy = st.builds(
    xpdl1::ActivitiesType,
)

@given(instance=xpdl1::TypeDeclarationsType_strategy)
@settings(max_examples=50)
def test_xpdl1::typedeclarationstype_instantiation(instance):
    assert isinstance(instance, xpdl1::TypeDeclarationsType)

@given(instance=xpdl1::TypeDeclarationType_strategy)
@settings(max_examples=50)
def test_xpdl1::typedeclarationtype_instantiation(instance):
    assert isinstance(instance, xpdl1::TypeDeclarationType)

@given(instance=xpdl1::TypeDeclarationType_strategy)
def test_xpdl1::typedeclarationtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xpdl1::TypeDeclarationType_strategy)
def test_xpdl1::typedeclarationtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1::TypeDeclarationType_strategy)
def test_xpdl1::typedeclarationtype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=xpdl1::TypeDeclarationType_strategy)
def test_xpdl1::typedeclarationtype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=xpdl1::TypeDeclarationType_strategy)
def test_xpdl1::typedeclarationtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xpdl1::TypeDeclarationType_strategy)
def test_xpdl1::typedeclarationtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl1::WorkflowProcessesType_strategy)
@settings(max_examples=50)
def test_xpdl1::workflowprocessestype_instantiation(instance):
    assert isinstance(instance, xpdl1::WorkflowProcessesType)

@given(instance=xpdl1::WorkflowProcessType_strategy)
@settings(max_examples=50)
def test_xpdl1::workflowprocesstype_instantiation(instance):
    assert isinstance(instance, xpdl1::WorkflowProcessType)

@given(instance=xpdl1::WorkflowProcessType_strategy)
def test_xpdl1::workflowprocesstype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xpdl1::WorkflowProcessType_strategy)
def test_xpdl1::workflowprocesstype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1::WorkflowProcessType_strategy)
def test_xpdl1::workflowprocesstype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xpdl1::WorkflowProcessType_strategy)
def test_xpdl1::workflowprocesstype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl1::WorkflowProcessType_strategy)
def test_xpdl1::workflowprocesstype_accessLevel_type(instance):
    assert isinstance(instance.accessLevel, str)


@given(instance=xpdl1::WorkflowProcessType_strategy)
def test_xpdl1::workflowprocesstype_accessLevel_setter(instance):
    original = instance.accessLevel
    instance.accessLevel = original
    assert instance.accessLevel == original

@given(instance=xpdl1::TransitionRefType_strategy)
@settings(max_examples=50)
def test_xpdl1::transitionreftype_instantiation(instance):
    assert isinstance(instance, xpdl1::TransitionRefType)

@given(instance=xpdl1::TransitionRefType_strategy)
def test_xpdl1::transitionreftype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xpdl1::TransitionRefType_strategy)
def test_xpdl1::transitionreftype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1::TransitionType_strategy)
@settings(max_examples=50)
def test_xpdl1::transitiontype_instantiation(instance):
    assert isinstance(instance, xpdl1::TransitionType)

@given(instance=xpdl1::TransitionType_strategy)
def test_xpdl1::transitiontype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xpdl1::TransitionType_strategy)
def test_xpdl1::transitiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl1::TransitionType_strategy)
def test_xpdl1::transitiontype_from__type(instance):
    assert isinstance(instance.from_, str)


@given(instance=xpdl1::TransitionType_strategy)
def test_xpdl1::transitiontype_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=xpdl1::TransitionType_strategy)
def test_xpdl1::transitiontype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xpdl1::TransitionType_strategy)
def test_xpdl1::transitiontype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1::TransitionType_strategy)
def test_xpdl1::transitiontype_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=xpdl1::TransitionType_strategy)
def test_xpdl1::transitiontype_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=xpdl1::TransitionType_strategy)
def test_xpdl1::transitiontype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=xpdl1::TransitionType_strategy)
def test_xpdl1::transitiontype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=xpdl1::ToolType_strategy)
@settings(max_examples=50)
def test_xpdl1::tooltype_instantiation(instance):
    assert isinstance(instance, xpdl1::ToolType)

@given(instance=xpdl1::ToolType_strategy)
def test_xpdl1::tooltype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=xpdl1::ToolType_strategy)
def test_xpdl1::tooltype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=xpdl1::ToolType_strategy)
def test_xpdl1::tooltype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xpdl1::ToolType_strategy)
def test_xpdl1::tooltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1::ToolType_strategy)
def test_xpdl1::tooltype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xpdl1::ToolType_strategy)
def test_xpdl1::tooltype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xpdl1::TransitionRestrictionType_strategy)
@settings(max_examples=50)
def test_xpdl1::transitionrestrictiontype_instantiation(instance):
    assert isinstance(instance, xpdl1::TransitionRestrictionType)

@given(instance=xpdl1::TransitionRefsType_strategy)
@settings(max_examples=50)
def test_xpdl1::transitionrefstype_instantiation(instance):
    assert isinstance(instance, xpdl1::TransitionRefsType)

@given(instance=xpdl1::ResponsiblesType_strategy)
@settings(max_examples=50)
def test_xpdl1::responsiblestype_instantiation(instance):
    assert isinstance(instance, xpdl1::ResponsiblesType)

@given(instance=xpdl1::ResponsiblesType_strategy)
def test_xpdl1::responsiblestype_responsible_type(instance):
    assert isinstance(instance.responsible, str)


@given(instance=xpdl1::ResponsiblesType_strategy)
def test_xpdl1::responsiblestype_responsible_setter(instance):
    original = instance.responsible
    instance.responsible = original
    assert instance.responsible == original

@given(instance=xpdl1::TimeEstimationType_strategy)
@settings(max_examples=50)
def test_xpdl1::timeestimationtype_instantiation(instance):
    assert isinstance(instance, xpdl1::TimeEstimationType)

@given(instance=xpdl1::TimeEstimationType_strategy)
def test_xpdl1::timeestimationtype_duration_type(instance):
    assert isinstance(instance.duration, str)


@given(instance=xpdl1::TimeEstimationType_strategy)
def test_xpdl1::timeestimationtype_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=xpdl1::TimeEstimationType_strategy)
def test_xpdl1::timeestimationtype_waitingTime_type(instance):
    assert isinstance(instance.waitingTime, str)


@given(instance=xpdl1::TimeEstimationType_strategy)
def test_xpdl1::timeestimationtype_waitingTime_setter(instance):
    original = instance.waitingTime
    instance.waitingTime = original
    assert instance.waitingTime == original

@given(instance=xpdl1::TimeEstimationType_strategy)
def test_xpdl1::timeestimationtype_workingTime_type(instance):
    assert isinstance(instance.workingTime, str)


@given(instance=xpdl1::TimeEstimationType_strategy)
def test_xpdl1::timeestimationtype_workingTime_setter(instance):
    original = instance.workingTime
    instance.workingTime = original
    assert instance.workingTime == original

@given(instance=xpdl1::SubFlowType_strategy)
@settings(max_examples=50)
def test_xpdl1::subflowtype_instantiation(instance):
    assert isinstance(instance, xpdl1::SubFlowType)

@given(instance=xpdl1::SubFlowType_strategy)
def test_xpdl1::subflowtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xpdl1::SubFlowType_strategy)
def test_xpdl1::subflowtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1::SubFlowType_strategy)
def test_xpdl1::subflowtype_execution_type(instance):
    assert isinstance(instance.execution, str)


@given(instance=xpdl1::SubFlowType_strategy)
def test_xpdl1::subflowtype_execution_setter(instance):
    original = instance.execution
    instance.execution = original
    assert instance.execution == original

@given(instance=xpdl1::SplitType_strategy)
@settings(max_examples=50)
def test_xpdl1::splittype_instantiation(instance):
    assert isinstance(instance, xpdl1::SplitType)

@given(instance=xpdl1::SplitType_strategy)
def test_xpdl1::splittype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xpdl1::SplitType_strategy)
def test_xpdl1::splittype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xpdl1::ScriptType_strategy)
@settings(max_examples=50)
def test_xpdl1::scripttype_instantiation(instance):
    assert isinstance(instance, xpdl1::ScriptType)

@given(instance=xpdl1::ScriptType_strategy)
def test_xpdl1::scripttype_grammar_type(instance):
    assert isinstance(instance.grammar, str)


@given(instance=xpdl1::ScriptType_strategy)
def test_xpdl1::scripttype_grammar_setter(instance):
    original = instance.grammar
    instance.grammar = original
    assert instance.grammar == original

@given(instance=xpdl1::ScriptType_strategy)
def test_xpdl1::scripttype_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=xpdl1::ScriptType_strategy)
def test_xpdl1::scripttype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=xpdl1::ScriptType_strategy)
def test_xpdl1::scripttype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xpdl1::ScriptType_strategy)
def test_xpdl1::scripttype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xpdl1::ParticipantsType_strategy)
@settings(max_examples=50)
def test_xpdl1::participantstype_instantiation(instance):
    assert isinstance(instance, xpdl1::ParticipantsType)

@given(instance=xpdl1::ParticipantType_strategy)
@settings(max_examples=50)
def test_xpdl1::participanttype_instantiation(instance):
    assert isinstance(instance, xpdl1::ParticipantType)

@given(instance=xpdl1::ParticipantType_strategy)
def test_xpdl1::participanttype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xpdl1::ParticipantType_strategy)
def test_xpdl1::participanttype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl1::ParticipantType_strategy)
def test_xpdl1::participanttype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=xpdl1::ParticipantType_strategy)
def test_xpdl1::participanttype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=xpdl1::ParticipantType_strategy)
def test_xpdl1::participanttype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xpdl1::ParticipantType_strategy)
def test_xpdl1::participanttype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1::PackageHeaderType_strategy)
@settings(max_examples=50)
def test_xpdl1::packageheadertype_instantiation(instance):
    assert isinstance(instance, xpdl1::PackageHeaderType)

@given(instance=xpdl1::PackageHeaderType_strategy)
def test_xpdl1::packageheadertype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=xpdl1::PackageHeaderType_strategy)
def test_xpdl1::packageheadertype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=xpdl1::PackageHeaderType_strategy)
def test_xpdl1::packageheadertype_created_type(instance):
    assert isinstance(instance.created, str)


@given(instance=xpdl1::PackageHeaderType_strategy)
def test_xpdl1::packageheadertype_created_setter(instance):
    original = instance.created
    instance.created = original
    assert instance.created == original

@given(instance=xpdl1::PackageHeaderType_strategy)
def test_xpdl1::packageheadertype_documentation_type(instance):
    assert isinstance(instance.documentation, str)


@given(instance=xpdl1::PackageHeaderType_strategy)
def test_xpdl1::packageheadertype_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original

@given(instance=xpdl1::PackageHeaderType_strategy)
def test_xpdl1::packageheadertype_priorityUnit_type(instance):
    assert isinstance(instance.priorityUnit, str)


@given(instance=xpdl1::PackageHeaderType_strategy)
def test_xpdl1::packageheadertype_priorityUnit_setter(instance):
    original = instance.priorityUnit
    instance.priorityUnit = original
    assert instance.priorityUnit == original

@given(instance=xpdl1::PackageHeaderType_strategy)
def test_xpdl1::packageheadertype_costUnit_type(instance):
    assert isinstance(instance.costUnit, str)


@given(instance=xpdl1::PackageHeaderType_strategy)
def test_xpdl1::packageheadertype_costUnit_setter(instance):
    original = instance.costUnit
    instance.costUnit = original
    assert instance.costUnit == original

@given(instance=xpdl1::PackageHeaderType_strategy)
def test_xpdl1::packageheadertype_xPDLVersion_type(instance):
    assert isinstance(instance.xPDLVersion, str)


@given(instance=xpdl1::PackageHeaderType_strategy)
def test_xpdl1::packageheadertype_xPDLVersion_setter(instance):
    original = instance.xPDLVersion
    instance.xPDLVersion = original
    assert instance.xPDLVersion == original

@given(instance=xpdl1::PackageHeaderType_strategy)
def test_xpdl1::packageheadertype_vendor_type(instance):
    assert isinstance(instance.vendor, str)


@given(instance=xpdl1::PackageHeaderType_strategy)
def test_xpdl1::packageheadertype_vendor_setter(instance):
    original = instance.vendor
    instance.vendor = original
    assert instance.vendor == original

@given(instance=xpdl1::RedefinableHeaderType_strategy)
@settings(max_examples=50)
def test_xpdl1::redefinableheadertype_instantiation(instance):
    assert isinstance(instance, xpdl1::RedefinableHeaderType)

@given(instance=xpdl1::RedefinableHeaderType_strategy)
def test_xpdl1::redefinableheadertype_countrykey_type(instance):
    assert isinstance(instance.countrykey, str)


@given(instance=xpdl1::RedefinableHeaderType_strategy)
def test_xpdl1::redefinableheadertype_countrykey_setter(instance):
    original = instance.countrykey
    instance.countrykey = original
    assert instance.countrykey == original

@given(instance=xpdl1::RedefinableHeaderType_strategy)
def test_xpdl1::redefinableheadertype_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=xpdl1::RedefinableHeaderType_strategy)
def test_xpdl1::redefinableheadertype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=xpdl1::RedefinableHeaderType_strategy)
def test_xpdl1::redefinableheadertype_codepage_type(instance):
    assert isinstance(instance.codepage, str)


@given(instance=xpdl1::RedefinableHeaderType_strategy)
def test_xpdl1::redefinableheadertype_codepage_setter(instance):
    original = instance.codepage
    instance.codepage = original
    assert instance.codepage == original

@given(instance=xpdl1::RedefinableHeaderType_strategy)
def test_xpdl1::redefinableheadertype_publicationStatus_type(instance):
    assert isinstance(instance.publicationStatus, str)


@given(instance=xpdl1::RedefinableHeaderType_strategy)
def test_xpdl1::redefinableheadertype_publicationStatus_setter(instance):
    original = instance.publicationStatus
    instance.publicationStatus = original
    assert instance.publicationStatus == original

@given(instance=xpdl1::RedefinableHeaderType_strategy)
def test_xpdl1::redefinableheadertype_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=xpdl1::RedefinableHeaderType_strategy)
def test_xpdl1::redefinableheadertype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=xpdl1::ProcessHeaderType_strategy)
@settings(max_examples=50)
def test_xpdl1::processheadertype_instantiation(instance):
    assert isinstance(instance, xpdl1::ProcessHeaderType)

@given(instance=xpdl1::ProcessHeaderType_strategy)
def test_xpdl1::processheadertype_durationUnit_type(instance):
    assert isinstance(instance.durationUnit, str)


@given(instance=xpdl1::ProcessHeaderType_strategy)
def test_xpdl1::processheadertype_durationUnit_setter(instance):
    original = instance.durationUnit
    instance.durationUnit = original
    assert instance.durationUnit == original

@given(instance=xpdl1::ProcessHeaderType_strategy)
def test_xpdl1::processheadertype_limit_type(instance):
    assert isinstance(instance.limit, str)


@given(instance=xpdl1::ProcessHeaderType_strategy)
def test_xpdl1::processheadertype_limit_setter(instance):
    original = instance.limit
    instance.limit = original
    assert instance.limit == original

@given(instance=xpdl1::ProcessHeaderType_strategy)
def test_xpdl1::processheadertype_validTo_type(instance):
    assert isinstance(instance.validTo, str)


@given(instance=xpdl1::ProcessHeaderType_strategy)
def test_xpdl1::processheadertype_validTo_setter(instance):
    original = instance.validTo
    instance.validTo = original
    assert instance.validTo == original

@given(instance=xpdl1::ProcessHeaderType_strategy)
def test_xpdl1::processheadertype_priority_type(instance):
    assert isinstance(instance.priority, str)


@given(instance=xpdl1::ProcessHeaderType_strategy)
def test_xpdl1::processheadertype_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=xpdl1::ProcessHeaderType_strategy)
def test_xpdl1::processheadertype_validFrom_type(instance):
    assert isinstance(instance.validFrom, str)


@given(instance=xpdl1::ProcessHeaderType_strategy)
def test_xpdl1::processheadertype_validFrom_setter(instance):
    original = instance.validFrom
    instance.validFrom = original
    assert instance.validFrom == original

@given(instance=xpdl1::ProcessHeaderType_strategy)
def test_xpdl1::processheadertype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=xpdl1::ProcessHeaderType_strategy)
def test_xpdl1::processheadertype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=xpdl1::ProcessHeaderType_strategy)
def test_xpdl1::processheadertype_created_type(instance):
    assert isinstance(instance.created, str)


@given(instance=xpdl1::ProcessHeaderType_strategy)
def test_xpdl1::processheadertype_created_setter(instance):
    original = instance.created
    instance.created = original
    assert instance.created == original

@given(instance=xpdl1::ParticipantTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1::participanttypetype_instantiation(instance):
    assert isinstance(instance, xpdl1::ParticipantTypeType)

@given(instance=xpdl1::ParticipantTypeType_strategy)
def test_xpdl1::participanttypetype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xpdl1::ParticipantTypeType_strategy)
def test_xpdl1::participanttypetype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xpdl1::JoinType_strategy)
@settings(max_examples=50)
def test_xpdl1::jointype_instantiation(instance):
    assert isinstance(instance, xpdl1::JoinType)

@given(instance=xpdl1::JoinType_strategy)
def test_xpdl1::jointype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xpdl1::JoinType_strategy)
def test_xpdl1::jointype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xpdl1::PackageType_strategy)
@settings(max_examples=50)
def test_xpdl1::packagetype_instantiation(instance):
    assert isinstance(instance, xpdl1::PackageType)

@given(instance=xpdl1::PackageType_strategy)
def test_xpdl1::packagetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xpdl1::PackageType_strategy)
def test_xpdl1::packagetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl1::PackageType_strategy)
def test_xpdl1::packagetype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xpdl1::PackageType_strategy)
def test_xpdl1::packagetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1::NoType_strategy)
@settings(max_examples=50)
def test_xpdl1::notype_instantiation(instance):
    assert isinstance(instance, xpdl1::NoType)

@given(instance=xpdl1::MemberType_strategy)
@settings(max_examples=50)
def test_xpdl1::membertype_instantiation(instance):
    assert isinstance(instance, xpdl1::MemberType)

@given(instance=xpdl1::ManualType_strategy)
@settings(max_examples=50)
def test_xpdl1::manualtype_instantiation(instance):
    assert isinstance(instance, xpdl1::ManualType)

@given(instance=xpdl1::ExternalPackageType_strategy)
@settings(max_examples=50)
def test_xpdl1::externalpackagetype_instantiation(instance):
    assert isinstance(instance, xpdl1::ExternalPackageType)

@given(instance=xpdl1::ExternalPackageType_strategy)
def test_xpdl1::externalpackagetype_href_type(instance):
    assert isinstance(instance.href, str)


@given(instance=xpdl1::ExternalPackageType_strategy)
def test_xpdl1::externalpackagetype_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original

@given(instance=xpdl1::ExtendedAttributeType_strategy)
@settings(max_examples=50)
def test_xpdl1::extendedattributetype_instantiation(instance):
    assert isinstance(instance, xpdl1::ExtendedAttributeType)

@given(instance=xpdl1::ExtendedAttributeType_strategy)
def test_xpdl1::extendedattributetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xpdl1::ExtendedAttributeType_strategy)
def test_xpdl1::extendedattributetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl1::ExtendedAttributeType_strategy)
def test_xpdl1::extendedattributetype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=xpdl1::ExtendedAttributeType_strategy)
def test_xpdl1::extendedattributetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xpdl1::ExtendedAttributeType_strategy)
def test_xpdl1::extendedattributetype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xpdl1::ExtendedAttributeType_strategy)
def test_xpdl1::extendedattributetype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xpdl1::ExtendedAttributeType_strategy)
def test_xpdl1::extendedattributetype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xpdl1::ExtendedAttributeType_strategy)
def test_xpdl1::extendedattributetype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xpdl1::ExtendedAttributeType_strategy)
def test_xpdl1::extendedattributetype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=xpdl1::ExtendedAttributeType_strategy)
def test_xpdl1::extendedattributetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xpdl1::FormalParameterType_strategy)
@settings(max_examples=50)
def test_xpdl1::formalparametertype_instantiation(instance):
    assert isinstance(instance, xpdl1::FormalParameterType)

@given(instance=xpdl1::FormalParameterType_strategy)
def test_xpdl1::formalparametertype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xpdl1::FormalParameterType_strategy)
def test_xpdl1::formalparametertype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1::FormalParameterType_strategy)
def test_xpdl1::formalparametertype_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=xpdl1::FormalParameterType_strategy)
def test_xpdl1::formalparametertype_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=xpdl1::FormalParameterType_strategy)
def test_xpdl1::formalparametertype_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=xpdl1::FormalParameterType_strategy)
def test_xpdl1::formalparametertype_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=xpdl1::FormalParameterType_strategy)
def test_xpdl1::formalparametertype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=xpdl1::FormalParameterType_strategy)
def test_xpdl1::formalparametertype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=xpdl1::ExternalPackagesType_strategy)
@settings(max_examples=50)
def test_xpdl1::externalpackagestype_instantiation(instance):
    assert isinstance(instance, xpdl1::ExternalPackagesType)

@given(instance=xpdl1::EnumerationValueType_strategy)
@settings(max_examples=50)
def test_xpdl1::enumerationvaluetype_instantiation(instance):
    assert isinstance(instance, xpdl1::EnumerationValueType)

@given(instance=xpdl1::EnumerationValueType_strategy)
def test_xpdl1::enumerationvaluetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xpdl1::EnumerationValueType_strategy)
def test_xpdl1::enumerationvaluetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl1::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_xpdl1::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, xpdl1::EStringToStringMapEntry)

@given(instance=xpdl1::DocumentRoot_strategy)
@settings(max_examples=50)
def test_xpdl1::documentroot_instantiation(instance):
    assert isinstance(instance, xpdl1::DocumentRoot)

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_workingTime_type(instance):
    assert isinstance(instance.workingTime, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_workingTime_setter(instance):
    original = instance.workingTime
    instance.workingTime = original
    assert instance.workingTime == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_initialValue_type(instance):
    assert isinstance(instance.initialValue, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_initialValue_setter(instance):
    original = instance.initialValue
    instance.initialValue = original
    assert instance.initialValue == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_codepage_type(instance):
    assert isinstance(instance.codepage, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_codepage_setter(instance):
    original = instance.codepage
    instance.codepage = original
    assert instance.codepage == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_icon_type(instance):
    assert isinstance(instance.icon, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_duration_type(instance):
    assert isinstance(instance.duration, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_waitingTime_type(instance):
    assert isinstance(instance.waitingTime, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_waitingTime_setter(instance):
    original = instance.waitingTime
    instance.waitingTime = original
    assert instance.waitingTime == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_countrykey_type(instance):
    assert isinstance(instance.countrykey, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_countrykey_setter(instance):
    original = instance.countrykey
    instance.countrykey = original
    assert instance.countrykey == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_costUnit_type(instance):
    assert isinstance(instance.costUnit, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_costUnit_setter(instance):
    original = instance.costUnit
    instance.costUnit = original
    assert instance.costUnit == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_priority_type(instance):
    assert isinstance(instance.priority, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_priorityUnit_type(instance):
    assert isinstance(instance.priorityUnit, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_priorityUnit_setter(instance):
    original = instance.priorityUnit
    instance.priorityUnit = original
    assert instance.priorityUnit == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_xPDLVersion_type(instance):
    assert isinstance(instance.xPDLVersion, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_xPDLVersion_setter(instance):
    original = instance.xPDLVersion
    instance.xPDLVersion = original
    assert instance.xPDLVersion == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_length_type(instance):
    assert isinstance(instance.length, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_validTo_type(instance):
    assert isinstance(instance.validTo, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_validTo_setter(instance):
    original = instance.validTo
    instance.validTo = original
    assert instance.validTo == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_documentation_type(instance):
    assert isinstance(instance.documentation, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_performer_type(instance):
    assert isinstance(instance.performer, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_performer_setter(instance):
    original = instance.performer
    instance.performer = original
    assert instance.performer == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_limit_type(instance):
    assert isinstance(instance.limit, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_limit_setter(instance):
    original = instance.limit
    instance.limit = original
    assert instance.limit == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_vendor_type(instance):
    assert isinstance(instance.vendor, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_vendor_setter(instance):
    original = instance.vendor
    instance.vendor = original
    assert instance.vendor == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_actualParameter_type(instance):
    assert isinstance(instance.actualParameter, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_actualParameter_setter(instance):
    original = instance.actualParameter
    instance.actualParameter = original
    assert instance.actualParameter == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_responsible_type(instance):
    assert isinstance(instance.responsible, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_responsible_setter(instance):
    original = instance.responsible
    instance.responsible = original
    assert instance.responsible == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_validFrom_type(instance):
    assert isinstance(instance.validFrom, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_validFrom_setter(instance):
    original = instance.validFrom
    instance.validFrom = original
    assert instance.validFrom == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_created_type(instance):
    assert isinstance(instance.created, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_created_setter(instance):
    original = instance.created
    instance.created = original
    assert instance.created == original

@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_cost_type(instance):
    assert isinstance(instance.cost, str)


@given(instance=xpdl1::DocumentRoot_strategy)
def test_xpdl1::documentroot_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original

@given(instance=xpdl1::EObject_strategy)
@settings(max_examples=50)
def test_xpdl1::eobject_instantiation(instance):
    assert isinstance(instance, xpdl1::EObject)

@given(instance=xpdl1::DataTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1::datatypetype_instantiation(instance):
    assert isinstance(instance, xpdl1::DataTypeType)

@given(instance=xpdl1::DataFieldType_strategy)
@settings(max_examples=50)
def test_xpdl1::datafieldtype_instantiation(instance):
    assert isinstance(instance, xpdl1::DataFieldType)

@given(instance=xpdl1::DataFieldType_strategy)
def test_xpdl1::datafieldtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xpdl1::DataFieldType_strategy)
def test_xpdl1::datafieldtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl1::DataFieldType_strategy)
def test_xpdl1::datafieldtype_length_type(instance):
    assert isinstance(instance.length, str)


@given(instance=xpdl1::DataFieldType_strategy)
def test_xpdl1::datafieldtype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=xpdl1::DataFieldType_strategy)
def test_xpdl1::datafieldtype_initialValue_type(instance):
    assert isinstance(instance.initialValue, str)


@given(instance=xpdl1::DataFieldType_strategy)
def test_xpdl1::datafieldtype_initialValue_setter(instance):
    original = instance.initialValue
    instance.initialValue = original
    assert instance.initialValue == original

@given(instance=xpdl1::DataFieldType_strategy)
def test_xpdl1::datafieldtype_isArray_type(instance):
    assert isinstance(instance.isArray, str)


@given(instance=xpdl1::DataFieldType_strategy)
def test_xpdl1::datafieldtype_isArray_setter(instance):
    original = instance.isArray
    instance.isArray = original
    assert instance.isArray == original

@given(instance=xpdl1::DataFieldType_strategy)
def test_xpdl1::datafieldtype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=xpdl1::DataFieldType_strategy)
def test_xpdl1::datafieldtype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=xpdl1::DataFieldType_strategy)
def test_xpdl1::datafieldtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xpdl1::DataFieldType_strategy)
def test_xpdl1::datafieldtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1::DataFieldsType_strategy)
@settings(max_examples=50)
def test_xpdl1::datafieldstype_instantiation(instance):
    assert isinstance(instance, xpdl1::DataFieldsType)

@given(instance=xpdl1::ConformanceClassType_strategy)
@settings(max_examples=50)
def test_xpdl1::conformanceclasstype_instantiation(instance):
    assert isinstance(instance, xpdl1::ConformanceClassType)

@given(instance=xpdl1::ConformanceClassType_strategy)
def test_xpdl1::conformanceclasstype_graphConformance_type(instance):
    assert isinstance(instance.graphConformance, str)


@given(instance=xpdl1::ConformanceClassType_strategy)
def test_xpdl1::conformanceclasstype_graphConformance_setter(instance):
    original = instance.graphConformance
    instance.graphConformance = original
    assert instance.graphConformance == original

@given(instance=xpdl1::ListTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1::listtypetype_instantiation(instance):
    assert isinstance(instance, xpdl1::ListTypeType)

@given(instance=xpdl1::EnumerationTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1::enumerationtypetype_instantiation(instance):
    assert isinstance(instance, xpdl1::EnumerationTypeType)

@given(instance=xpdl1::XpressionType_strategy)
@settings(max_examples=50)
def test_xpdl1::xpressiontype_instantiation(instance):
    assert isinstance(instance, xpdl1::XpressionType)

@given(instance=xpdl1::XpressionType_strategy)
def test_xpdl1::xpressiontype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xpdl1::XpressionType_strategy)
def test_xpdl1::xpressiontype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xpdl1::XpressionType_strategy)
def test_xpdl1::xpressiontype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xpdl1::XpressionType_strategy)
def test_xpdl1::xpressiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xpdl1::XpressionType_strategy)
def test_xpdl1::xpressiontype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=xpdl1::XpressionType_strategy)
def test_xpdl1::xpressiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xpdl1::ConditionType_strategy)
@settings(max_examples=50)
def test_xpdl1::conditiontype_instantiation(instance):
    assert isinstance(instance, xpdl1::ConditionType)

@given(instance=xpdl1::ConditionType_strategy)
def test_xpdl1::conditiontype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xpdl1::ConditionType_strategy)
def test_xpdl1::conditiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xpdl1::ConditionType_strategy)
def test_xpdl1::conditiontype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xpdl1::ConditionType_strategy)
def test_xpdl1::conditiontype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xpdl1::ConditionType_strategy)
def test_xpdl1::conditiontype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=xpdl1::ConditionType_strategy)
def test_xpdl1::conditiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xpdl1::AutomaticType_strategy)
@settings(max_examples=50)
def test_xpdl1::automatictype_instantiation(instance):
    assert isinstance(instance, xpdl1::AutomaticType)

@given(instance=xpdl1::ExternalReferenceType_strategy)
@settings(max_examples=50)
def test_xpdl1::externalreferencetype_instantiation(instance):
    assert isinstance(instance, xpdl1::ExternalReferenceType)

@given(instance=xpdl1::ExternalReferenceType_strategy)
def test_xpdl1::externalreferencetype_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=xpdl1::ExternalReferenceType_strategy)
def test_xpdl1::externalreferencetype_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=xpdl1::ExternalReferenceType_strategy)
def test_xpdl1::externalreferencetype_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=xpdl1::ExternalReferenceType_strategy)
def test_xpdl1::externalreferencetype_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=xpdl1::ExternalReferenceType_strategy)
def test_xpdl1::externalreferencetype_xref_type(instance):
    assert isinstance(instance.xref, str)


@given(instance=xpdl1::ExternalReferenceType_strategy)
def test_xpdl1::externalreferencetype_xref_setter(instance):
    original = instance.xref
    instance.xref = original
    assert instance.xref == original

@given(instance=xpdl1::FormalParametersType_strategy)
@settings(max_examples=50)
def test_xpdl1::formalparameterstype_instantiation(instance):
    assert isinstance(instance, xpdl1::FormalParametersType)

@given(instance=xpdl1::UnionTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1::uniontypetype_instantiation(instance):
    assert isinstance(instance, xpdl1::UnionTypeType)

@given(instance=xpdl1::RecordTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1::recordtypetype_instantiation(instance):
    assert isinstance(instance, xpdl1::RecordTypeType)

@given(instance=xpdl1::SchemaTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1::schematypetype_instantiation(instance):
    assert isinstance(instance, xpdl1::SchemaTypeType)

@given(instance=xpdl1::SchemaTypeType_strategy)
def test_xpdl1::schematypetype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xpdl1::SchemaTypeType_strategy)
def test_xpdl1::schematypetype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xpdl1::DeclaredTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1::declaredtypetype_instantiation(instance):
    assert isinstance(instance, xpdl1::DeclaredTypeType)

@given(instance=xpdl1::DeclaredTypeType_strategy)
def test_xpdl1::declaredtypetype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xpdl1::DeclaredTypeType_strategy)
def test_xpdl1::declaredtypetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1::BasicTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1::basictypetype_instantiation(instance):
    assert isinstance(instance, xpdl1::BasicTypeType)

@given(instance=xpdl1::BasicTypeType_strategy)
def test_xpdl1::basictypetype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xpdl1::BasicTypeType_strategy)
def test_xpdl1::basictypetype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xpdl1::ArrayTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1::arraytypetype_instantiation(instance):
    assert isinstance(instance, xpdl1::ArrayTypeType)

@given(instance=xpdl1::ArrayTypeType_strategy)
def test_xpdl1::arraytypetype_lowerIndex_type(instance):
    assert isinstance(instance.lowerIndex, str)


@given(instance=xpdl1::ArrayTypeType_strategy)
def test_xpdl1::arraytypetype_lowerIndex_setter(instance):
    original = instance.lowerIndex
    instance.lowerIndex = original
    assert instance.lowerIndex == original

@given(instance=xpdl1::ArrayTypeType_strategy)
def test_xpdl1::arraytypetype_upperIndex_type(instance):
    assert isinstance(instance.upperIndex, str)


@given(instance=xpdl1::ArrayTypeType_strategy)
def test_xpdl1::arraytypetype_upperIndex_setter(instance):
    original = instance.upperIndex
    instance.upperIndex = original
    assert instance.upperIndex == original

@given(instance=xpdl1::SimulationInformationType_strategy)
@settings(max_examples=50)
def test_xpdl1::simulationinformationtype_instantiation(instance):
    assert isinstance(instance, xpdl1::SimulationInformationType)

@given(instance=xpdl1::SimulationInformationType_strategy)
def test_xpdl1::simulationinformationtype_cost_type(instance):
    assert isinstance(instance.cost, str)


@given(instance=xpdl1::SimulationInformationType_strategy)
def test_xpdl1::simulationinformationtype_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original

@given(instance=xpdl1::SimulationInformationType_strategy)
def test_xpdl1::simulationinformationtype_instantiation_type(instance):
    assert isinstance(instance.instantiation, str)


@given(instance=xpdl1::SimulationInformationType_strategy)
def test_xpdl1::simulationinformationtype_instantiation_setter(instance):
    original = instance.instantiation
    instance.instantiation = original
    assert instance.instantiation == original

@given(instance=xpdl1::DeadlineType_strategy)
@settings(max_examples=50)
def test_xpdl1::deadlinetype_instantiation(instance):
    assert isinstance(instance, xpdl1::DeadlineType)

@given(instance=xpdl1::DeadlineType_strategy)
def test_xpdl1::deadlinetype_execution_type(instance):
    assert isinstance(instance.execution, str)


@given(instance=xpdl1::DeadlineType_strategy)
def test_xpdl1::deadlinetype_execution_setter(instance):
    original = instance.execution
    instance.execution = original
    assert instance.execution == original

@given(instance=xpdl1::ApplicationType_strategy)
@settings(max_examples=50)
def test_xpdl1::applicationtype_instantiation(instance):
    assert isinstance(instance, xpdl1::ApplicationType)

@given(instance=xpdl1::ApplicationType_strategy)
def test_xpdl1::applicationtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xpdl1::ApplicationType_strategy)
def test_xpdl1::applicationtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl1::ApplicationType_strategy)
def test_xpdl1::applicationtype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=xpdl1::ApplicationType_strategy)
def test_xpdl1::applicationtype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=xpdl1::ApplicationType_strategy)
def test_xpdl1::applicationtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xpdl1::ApplicationType_strategy)
def test_xpdl1::applicationtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1::ApplicationsType_strategy)
@settings(max_examples=50)
def test_xpdl1::applicationstype_instantiation(instance):
    assert isinstance(instance, xpdl1::ApplicationsType)

@given(instance=xpdl1::ActualParametersType_strategy)
@settings(max_examples=50)
def test_xpdl1::actualparameterstype_instantiation(instance):
    assert isinstance(instance, xpdl1::ActualParametersType)

@given(instance=xpdl1::ActualParametersType_strategy)
def test_xpdl1::actualparameterstype_actualParameter_type(instance):
    assert isinstance(instance.actualParameter, str)


@given(instance=xpdl1::ActualParametersType_strategy)
def test_xpdl1::actualparameterstype_actualParameter_setter(instance):
    original = instance.actualParameter
    instance.actualParameter = original
    assert instance.actualParameter == original

@given(instance=xpdl1::ExtendedAttributesType_strategy)
@settings(max_examples=50)
def test_xpdl1::extendedattributestype_instantiation(instance):
    assert isinstance(instance, xpdl1::ExtendedAttributesType)

@given(instance=xpdl1::TransitionRestrictionsType_strategy)
@settings(max_examples=50)
def test_xpdl1::transitionrestrictionstype_instantiation(instance):
    assert isinstance(instance, xpdl1::TransitionRestrictionsType)

@given(instance=xpdl1::TransitionsType_strategy)
@settings(max_examples=50)
def test_xpdl1::transitionstype_instantiation(instance):
    assert isinstance(instance, xpdl1::TransitionsType)

@given(instance=xpdl1::ActivitySetType_strategy)
@settings(max_examples=50)
def test_xpdl1::activitysettype_instantiation(instance):
    assert isinstance(instance, xpdl1::ActivitySetType)

@given(instance=xpdl1::ActivitySetType_strategy)
def test_xpdl1::activitysettype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xpdl1::ActivitySetType_strategy)
def test_xpdl1::activitysettype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1::ActivitySetsType_strategy)
@settings(max_examples=50)
def test_xpdl1::activitysetstype_instantiation(instance):
    assert isinstance(instance, xpdl1::ActivitySetsType)

@given(instance=xpdl1::FinishModeType_strategy)
@settings(max_examples=50)
def test_xpdl1::finishmodetype_instantiation(instance):
    assert isinstance(instance, xpdl1::FinishModeType)

@given(instance=xpdl1::StartModeType_strategy)
@settings(max_examples=50)
def test_xpdl1::startmodetype_instantiation(instance):
    assert isinstance(instance, xpdl1::StartModeType)

@given(instance=xpdl1::BlockActivityType_strategy)
@settings(max_examples=50)
def test_xpdl1::blockactivitytype_instantiation(instance):
    assert isinstance(instance, xpdl1::BlockActivityType)

@given(instance=xpdl1::BlockActivityType_strategy)
def test_xpdl1::blockactivitytype_blockId_type(instance):
    assert isinstance(instance.blockId, str)


@given(instance=xpdl1::BlockActivityType_strategy)
def test_xpdl1::blockactivitytype_blockId_setter(instance):
    original = instance.blockId
    instance.blockId = original
    assert instance.blockId == original

@given(instance=xpdl1::ImplementationType_strategy)
@settings(max_examples=50)
def test_xpdl1::implementationtype_instantiation(instance):
    assert isinstance(instance, xpdl1::ImplementationType)

@given(instance=xpdl1::RouteType_strategy)
@settings(max_examples=50)
def test_xpdl1::routetype_instantiation(instance):
    assert isinstance(instance, xpdl1::RouteType)

@given(instance=xpdl1::ActivityType_strategy)
@settings(max_examples=50)
def test_xpdl1::activitytype_instantiation(instance):
    assert isinstance(instance, xpdl1::ActivityType)

@given(instance=xpdl1::ActivityType_strategy)
def test_xpdl1::activitytype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xpdl1::ActivityType_strategy)
def test_xpdl1::activitytype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1::ActivityType_strategy)
def test_xpdl1::activitytype_performer_type(instance):
    assert isinstance(instance.performer, str)


@given(instance=xpdl1::ActivityType_strategy)
def test_xpdl1::activitytype_performer_setter(instance):
    original = instance.performer
    instance.performer = original
    assert instance.performer == original

@given(instance=xpdl1::ActivityType_strategy)
def test_xpdl1::activitytype_icon_type(instance):
    assert isinstance(instance.icon, str)


@given(instance=xpdl1::ActivityType_strategy)
def test_xpdl1::activitytype_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=xpdl1::ActivityType_strategy)
def test_xpdl1::activitytype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=xpdl1::ActivityType_strategy)
def test_xpdl1::activitytype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=xpdl1::ActivityType_strategy)
def test_xpdl1::activitytype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xpdl1::ActivityType_strategy)
def test_xpdl1::activitytype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl1::ActivityType_strategy)
def test_xpdl1::activitytype_priority_type(instance):
    assert isinstance(instance.priority, str)


@given(instance=xpdl1::ActivityType_strategy)
def test_xpdl1::activitytype_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=xpdl1::ActivityType_strategy)
def test_xpdl1::activitytype_limit_type(instance):
    assert isinstance(instance.limit, str)


@given(instance=xpdl1::ActivityType_strategy)
def test_xpdl1::activitytype_limit_setter(instance):
    original = instance.limit
    instance.limit = original
    assert instance.limit == original

@given(instance=xpdl1::ActivityType_strategy)
def test_xpdl1::activitytype_documentation_type(instance):
    assert isinstance(instance.documentation, str)


@given(instance=xpdl1::ActivityType_strategy)
def test_xpdl1::activitytype_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original

@given(instance=xpdl1::ActivitiesType_strategy)
@settings(max_examples=50)
def test_xpdl1::activitiestype_instantiation(instance):
    assert isinstance(instance, xpdl1::ActivitiesType)

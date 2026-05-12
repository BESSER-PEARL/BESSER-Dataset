import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    xpdl1_WorkflowProcessType,
    xpdl1_WorkflowProcessesType,
    xpdl1_TransitionRestrictionType,
    xpdl1_TransitionRefsType,
    xpdl1_TypeDeclarationsType,
    xpdl1_TypeDeclarationType,
    xpdl1_TimeEstimationType,
    xpdl1_SubFlowType,
    xpdl1_SplitType,
    xpdl1_TransitionRefType,
    xpdl1_TransitionType,
    xpdl1_ToolType,
    xpdl1_ResponsiblesType,
    xpdl1_RedefinableHeaderType,
    xpdl1_ScriptType,
    xpdl1_ParticipantTypeType,
    xpdl1_ParticipantsType,
    xpdl1_ParticipantType,
    xpdl1_ProcessHeaderType,
    xpdl1_NoType,
    xpdl1_MemberType,
    xpdl1_ManualType,
    xpdl1_PackageHeaderType,
    xpdl1_PackageType,
    xpdl1_FormalParameterType,
    xpdl1_JoinType,
    xpdl1_ExtendedAttributeType,
    xpdl1_EnumerationValueType,
    xpdl1_ExternalPackagesType,
    xpdl1_ExternalPackageType,
    xpdl1_EObject,
    xpdl1_EStringToStringMapEntry,
    xpdl1_DocumentRoot,
    xpdl1_DataTypeType,
    xpdl1_DataFieldType,
    xpdl1_DataFieldsType,
    xpdl1_ConformanceClassType,
    xpdl1_XpressionType,
    xpdl1_AutomaticType,
    xpdl1_ListTypeType,
    xpdl1_EnumerationTypeType,
    xpdl1_ConditionType,
    xpdl1_SchemaTypeType,
    xpdl1_DeclaredTypeType,
    xpdl1_BasicTypeType,
    xpdl1_ArrayTypeType,
    xpdl1_UnionTypeType,
    xpdl1_RecordTypeType,
    xpdl1_ApplicationType,
    xpdl1_ApplicationsType,
    xpdl1_ActualParametersType,
    xpdl1_ExtendedAttributesType,
    xpdl1_ExternalReferenceType,
    xpdl1_FormalParametersType,
    xpdl1_SimulationInformationType,
    xpdl1_DeadlineType,
    xpdl1_FinishModeType,
    xpdl1_StartModeType,
    xpdl1_BlockActivityType,
    xpdl1_TransitionRestrictionsType,
    xpdl1_TransitionsType,
    xpdl1_ImplementationType,
    xpdl1_RouteType,
    xpdl1_ActivitiesType,
    xpdl1_ActivitySetType,
    xpdl1_ActivitySetsType,
    xpdl1_ActivityType,
    TypeType1,
    PublicationStatusType,
    ModeType,
    TypeType,
    ExecutionType1,
    AccessLevelType,
    TypeType2,
    TypeType5,
    InstantiationType,
    IsArrayType,
    ExecutionType,
    TypeType3,
    TypeType4,
    GraphConformanceType,
    DurationUnitType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_xpdl1_workflowprocesstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_WorkflowProcessType)


def test_xpdl1_workflowprocesstype_constructor_exists():
    assert callable(xpdl1_WorkflowProcessType.__init__)


def test_xpdl1_workflowprocesstype_constructor_args():
    sig = inspect.signature(xpdl1_WorkflowProcessType.__init__)
    params = list(sig.parameters.keys())
    assert "accessLevel" in params, "Missing parameter 'accessLevel'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_xpdl1_workflowprocesstype_has_accessLevel():
    assert hasattr(xpdl1_WorkflowProcessType, "accessLevel")
    descriptor = None
    for klass in xpdl1_WorkflowProcessType.__mro__:
        if "accessLevel" in klass.__dict__:
            descriptor = klass.__dict__["accessLevel"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_workflowprocesstype_has_id():
    assert hasattr(xpdl1_WorkflowProcessType, "id")
    descriptor = None
    for klass in xpdl1_WorkflowProcessType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_workflowprocesstype_has_name():
    assert hasattr(xpdl1_WorkflowProcessType, "name")
    descriptor = None
    for klass in xpdl1_WorkflowProcessType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_workflowprocessestype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_WorkflowProcessesType)


def test_xpdl1_workflowprocessestype_constructor_exists():
    assert callable(xpdl1_WorkflowProcessesType.__init__)


def test_xpdl1_workflowprocessestype_constructor_args():
    sig = inspect.signature(xpdl1_WorkflowProcessesType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_transitionrestrictiontype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_TransitionRestrictionType)


def test_xpdl1_transitionrestrictiontype_constructor_exists():
    assert callable(xpdl1_TransitionRestrictionType.__init__)


def test_xpdl1_transitionrestrictiontype_constructor_args():
    sig = inspect.signature(xpdl1_TransitionRestrictionType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_transitionrefstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_TransitionRefsType)


def test_xpdl1_transitionrefstype_constructor_exists():
    assert callable(xpdl1_TransitionRefsType.__init__)


def test_xpdl1_transitionrefstype_constructor_args():
    sig = inspect.signature(xpdl1_TransitionRefsType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_typedeclarationstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_TypeDeclarationsType)


def test_xpdl1_typedeclarationstype_constructor_exists():
    assert callable(xpdl1_TypeDeclarationsType.__init__)


def test_xpdl1_typedeclarationstype_constructor_args():
    sig = inspect.signature(xpdl1_TypeDeclarationsType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_typedeclarationtype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_TypeDeclarationType)


def test_xpdl1_typedeclarationtype_constructor_exists():
    assert callable(xpdl1_TypeDeclarationType.__init__)


def test_xpdl1_typedeclarationtype_constructor_args():
    sig = inspect.signature(xpdl1_TypeDeclarationType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_xpdl1_typedeclarationtype_has_id():
    assert hasattr(xpdl1_TypeDeclarationType, "id")
    descriptor = None
    for klass in xpdl1_TypeDeclarationType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_typedeclarationtype_has_description():
    assert hasattr(xpdl1_TypeDeclarationType, "description")
    descriptor = None
    for klass in xpdl1_TypeDeclarationType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_typedeclarationtype_has_name():
    assert hasattr(xpdl1_TypeDeclarationType, "name")
    descriptor = None
    for klass in xpdl1_TypeDeclarationType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_timeestimationtype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_TimeEstimationType)


def test_xpdl1_timeestimationtype_constructor_exists():
    assert callable(xpdl1_TimeEstimationType.__init__)


def test_xpdl1_timeestimationtype_constructor_args():
    sig = inspect.signature(xpdl1_TimeEstimationType.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"
    assert "workingTime" in params, "Missing parameter 'workingTime'"
    assert "waitingTime" in params, "Missing parameter 'waitingTime'"

def test_xpdl1_timeestimationtype_has_duration():
    assert hasattr(xpdl1_TimeEstimationType, "duration")
    descriptor = None
    for klass in xpdl1_TimeEstimationType.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_timeestimationtype_has_workingTime():
    assert hasattr(xpdl1_TimeEstimationType, "workingTime")
    descriptor = None
    for klass in xpdl1_TimeEstimationType.__mro__:
        if "workingTime" in klass.__dict__:
            descriptor = klass.__dict__["workingTime"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_timeestimationtype_has_waitingTime():
    assert hasattr(xpdl1_TimeEstimationType, "waitingTime")
    descriptor = None
    for klass in xpdl1_TimeEstimationType.__mro__:
        if "waitingTime" in klass.__dict__:
            descriptor = klass.__dict__["waitingTime"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_subflowtype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_SubFlowType)


def test_xpdl1_subflowtype_constructor_exists():
    assert callable(xpdl1_SubFlowType.__init__)


def test_xpdl1_subflowtype_constructor_args():
    sig = inspect.signature(xpdl1_SubFlowType.__init__)
    params = list(sig.parameters.keys())
    assert "execution" in params, "Missing parameter 'execution'"
    assert "id" in params, "Missing parameter 'id'"

def test_xpdl1_subflowtype_has_execution():
    assert hasattr(xpdl1_SubFlowType, "execution")
    descriptor = None
    for klass in xpdl1_SubFlowType.__mro__:
        if "execution" in klass.__dict__:
            descriptor = klass.__dict__["execution"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_subflowtype_has_id():
    assert hasattr(xpdl1_SubFlowType, "id")
    descriptor = None
    for klass in xpdl1_SubFlowType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_splittype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_SplitType)


def test_xpdl1_splittype_constructor_exists():
    assert callable(xpdl1_SplitType.__init__)


def test_xpdl1_splittype_constructor_args():
    sig = inspect.signature(xpdl1_SplitType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_xpdl1_splittype_has_type():
    assert hasattr(xpdl1_SplitType, "type")
    descriptor = None
    for klass in xpdl1_SplitType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_transitionreftype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_TransitionRefType)


def test_xpdl1_transitionreftype_constructor_exists():
    assert callable(xpdl1_TransitionRefType.__init__)


def test_xpdl1_transitionreftype_constructor_args():
    sig = inspect.signature(xpdl1_TransitionRefType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_xpdl1_transitionreftype_has_id():
    assert hasattr(xpdl1_TransitionRefType, "id")
    descriptor = None
    for klass in xpdl1_TransitionRefType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_transitiontype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_TransitionType)


def test_xpdl1_transitiontype_constructor_exists():
    assert callable(xpdl1_TransitionType.__init__)


def test_xpdl1_transitiontype_constructor_args():
    sig = inspect.signature(xpdl1_TransitionType.__init__)
    params = list(sig.parameters.keys())
    assert "from_" in params, "Missing parameter 'from_'"
    assert "description" in params, "Missing parameter 'description'"
    assert "to" in params, "Missing parameter 'to'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_xpdl1_transitiontype_has_from_():
    assert hasattr(xpdl1_TransitionType, "from_")
    descriptor = None
    for klass in xpdl1_TransitionType.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_transitiontype_has_description():
    assert hasattr(xpdl1_TransitionType, "description")
    descriptor = None
    for klass in xpdl1_TransitionType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_transitiontype_has_to():
    assert hasattr(xpdl1_TransitionType, "to")
    descriptor = None
    for klass in xpdl1_TransitionType.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_transitiontype_has_name():
    assert hasattr(xpdl1_TransitionType, "name")
    descriptor = None
    for klass in xpdl1_TransitionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_transitiontype_has_id():
    assert hasattr(xpdl1_TransitionType, "id")
    descriptor = None
    for klass in xpdl1_TransitionType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_tooltype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ToolType)


def test_xpdl1_tooltype_constructor_exists():
    assert callable(xpdl1_ToolType.__init__)


def test_xpdl1_tooltype_constructor_args():
    sig = inspect.signature(xpdl1_ToolType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"
    assert "description" in params, "Missing parameter 'description'"

def test_xpdl1_tooltype_has_id():
    assert hasattr(xpdl1_ToolType, "id")
    descriptor = None
    for klass in xpdl1_ToolType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_tooltype_has_type():
    assert hasattr(xpdl1_ToolType, "type")
    descriptor = None
    for klass in xpdl1_ToolType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_tooltype_has_description():
    assert hasattr(xpdl1_ToolType, "description")
    descriptor = None
    for klass in xpdl1_ToolType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_responsiblestype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ResponsiblesType)


def test_xpdl1_responsiblestype_constructor_exists():
    assert callable(xpdl1_ResponsiblesType.__init__)


def test_xpdl1_responsiblestype_constructor_args():
    sig = inspect.signature(xpdl1_ResponsiblesType.__init__)
    params = list(sig.parameters.keys())
    assert "responsible" in params, "Missing parameter 'responsible'"

def test_xpdl1_responsiblestype_has_responsible():
    assert hasattr(xpdl1_ResponsiblesType, "responsible")
    descriptor = None
    for klass in xpdl1_ResponsiblesType.__mro__:
        if "responsible" in klass.__dict__:
            descriptor = klass.__dict__["responsible"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_redefinableheadertype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_RedefinableHeaderType)


def test_xpdl1_redefinableheadertype_constructor_exists():
    assert callable(xpdl1_RedefinableHeaderType.__init__)


def test_xpdl1_redefinableheadertype_constructor_args():
    sig = inspect.signature(xpdl1_RedefinableHeaderType.__init__)
    params = list(sig.parameters.keys())
    assert "countrykey" in params, "Missing parameter 'countrykey'"
    assert "version" in params, "Missing parameter 'version'"
    assert "author" in params, "Missing parameter 'author'"
    assert "publicationStatus" in params, "Missing parameter 'publicationStatus'"
    assert "codepage" in params, "Missing parameter 'codepage'"

def test_xpdl1_redefinableheadertype_has_countrykey():
    assert hasattr(xpdl1_RedefinableHeaderType, "countrykey")
    descriptor = None
    for klass in xpdl1_RedefinableHeaderType.__mro__:
        if "countrykey" in klass.__dict__:
            descriptor = klass.__dict__["countrykey"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_redefinableheadertype_has_version():
    assert hasattr(xpdl1_RedefinableHeaderType, "version")
    descriptor = None
    for klass in xpdl1_RedefinableHeaderType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_redefinableheadertype_has_author():
    assert hasattr(xpdl1_RedefinableHeaderType, "author")
    descriptor = None
    for klass in xpdl1_RedefinableHeaderType.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_redefinableheadertype_has_publicationStatus():
    assert hasattr(xpdl1_RedefinableHeaderType, "publicationStatus")
    descriptor = None
    for klass in xpdl1_RedefinableHeaderType.__mro__:
        if "publicationStatus" in klass.__dict__:
            descriptor = klass.__dict__["publicationStatus"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_redefinableheadertype_has_codepage():
    assert hasattr(xpdl1_RedefinableHeaderType, "codepage")
    descriptor = None
    for klass in xpdl1_RedefinableHeaderType.__mro__:
        if "codepage" in klass.__dict__:
            descriptor = klass.__dict__["codepage"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_scripttype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ScriptType)


def test_xpdl1_scripttype_constructor_exists():
    assert callable(xpdl1_ScriptType.__init__)


def test_xpdl1_scripttype_constructor_args():
    sig = inspect.signature(xpdl1_ScriptType.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "type" in params, "Missing parameter 'type'"
    assert "grammar" in params, "Missing parameter 'grammar'"

def test_xpdl1_scripttype_has_version():
    assert hasattr(xpdl1_ScriptType, "version")
    descriptor = None
    for klass in xpdl1_ScriptType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_scripttype_has_type():
    assert hasattr(xpdl1_ScriptType, "type")
    descriptor = None
    for klass in xpdl1_ScriptType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_scripttype_has_grammar():
    assert hasattr(xpdl1_ScriptType, "grammar")
    descriptor = None
    for klass in xpdl1_ScriptType.__mro__:
        if "grammar" in klass.__dict__:
            descriptor = klass.__dict__["grammar"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_participanttypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ParticipantTypeType)


def test_xpdl1_participanttypetype_constructor_exists():
    assert callable(xpdl1_ParticipantTypeType.__init__)


def test_xpdl1_participanttypetype_constructor_args():
    sig = inspect.signature(xpdl1_ParticipantTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_xpdl1_participanttypetype_has_type():
    assert hasattr(xpdl1_ParticipantTypeType, "type")
    descriptor = None
    for klass in xpdl1_ParticipantTypeType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_participantstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ParticipantsType)


def test_xpdl1_participantstype_constructor_exists():
    assert callable(xpdl1_ParticipantsType.__init__)


def test_xpdl1_participantstype_constructor_args():
    sig = inspect.signature(xpdl1_ParticipantsType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_participanttype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ParticipantType)


def test_xpdl1_participanttype_constructor_exists():
    assert callable(xpdl1_ParticipantType.__init__)


def test_xpdl1_participanttype_constructor_args():
    sig = inspect.signature(xpdl1_ParticipantType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_xpdl1_participanttype_has_id():
    assert hasattr(xpdl1_ParticipantType, "id")
    descriptor = None
    for klass in xpdl1_ParticipantType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_participanttype_has_name():
    assert hasattr(xpdl1_ParticipantType, "name")
    descriptor = None
    for klass in xpdl1_ParticipantType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_participanttype_has_description():
    assert hasattr(xpdl1_ParticipantType, "description")
    descriptor = None
    for klass in xpdl1_ParticipantType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_processheadertype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ProcessHeaderType)


def test_xpdl1_processheadertype_constructor_exists():
    assert callable(xpdl1_ProcessHeaderType.__init__)


def test_xpdl1_processheadertype_constructor_args():
    sig = inspect.signature(xpdl1_ProcessHeaderType.__init__)
    params = list(sig.parameters.keys())
    assert "validFrom" in params, "Missing parameter 'validFrom'"
    assert "limit" in params, "Missing parameter 'limit'"
    assert "durationUnit" in params, "Missing parameter 'durationUnit'"
    assert "validTo" in params, "Missing parameter 'validTo'"
    assert "description" in params, "Missing parameter 'description'"
    assert "created" in params, "Missing parameter 'created'"
    assert "priority" in params, "Missing parameter 'priority'"

def test_xpdl1_processheadertype_has_validFrom():
    assert hasattr(xpdl1_ProcessHeaderType, "validFrom")
    descriptor = None
    for klass in xpdl1_ProcessHeaderType.__mro__:
        if "validFrom" in klass.__dict__:
            descriptor = klass.__dict__["validFrom"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_processheadertype_has_limit():
    assert hasattr(xpdl1_ProcessHeaderType, "limit")
    descriptor = None
    for klass in xpdl1_ProcessHeaderType.__mro__:
        if "limit" in klass.__dict__:
            descriptor = klass.__dict__["limit"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_processheadertype_has_durationUnit():
    assert hasattr(xpdl1_ProcessHeaderType, "durationUnit")
    descriptor = None
    for klass in xpdl1_ProcessHeaderType.__mro__:
        if "durationUnit" in klass.__dict__:
            descriptor = klass.__dict__["durationUnit"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_processheadertype_has_validTo():
    assert hasattr(xpdl1_ProcessHeaderType, "validTo")
    descriptor = None
    for klass in xpdl1_ProcessHeaderType.__mro__:
        if "validTo" in klass.__dict__:
            descriptor = klass.__dict__["validTo"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_processheadertype_has_description():
    assert hasattr(xpdl1_ProcessHeaderType, "description")
    descriptor = None
    for klass in xpdl1_ProcessHeaderType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_processheadertype_has_created():
    assert hasattr(xpdl1_ProcessHeaderType, "created")
    descriptor = None
    for klass in xpdl1_ProcessHeaderType.__mro__:
        if "created" in klass.__dict__:
            descriptor = klass.__dict__["created"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_processheadertype_has_priority():
    assert hasattr(xpdl1_ProcessHeaderType, "priority")
    descriptor = None
    for klass in xpdl1_ProcessHeaderType.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_notype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_NoType)


def test_xpdl1_notype_constructor_exists():
    assert callable(xpdl1_NoType.__init__)


def test_xpdl1_notype_constructor_args():
    sig = inspect.signature(xpdl1_NoType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_membertype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_MemberType)


def test_xpdl1_membertype_constructor_exists():
    assert callable(xpdl1_MemberType.__init__)


def test_xpdl1_membertype_constructor_args():
    sig = inspect.signature(xpdl1_MemberType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_manualtype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ManualType)


def test_xpdl1_manualtype_constructor_exists():
    assert callable(xpdl1_ManualType.__init__)


def test_xpdl1_manualtype_constructor_args():
    sig = inspect.signature(xpdl1_ManualType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_packageheadertype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_PackageHeaderType)


def test_xpdl1_packageheadertype_constructor_exists():
    assert callable(xpdl1_PackageHeaderType.__init__)


def test_xpdl1_packageheadertype_constructor_args():
    sig = inspect.signature(xpdl1_PackageHeaderType.__init__)
    params = list(sig.parameters.keys())
    assert "vendor" in params, "Missing parameter 'vendor'"
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "description" in params, "Missing parameter 'description'"
    assert "xPDLVersion" in params, "Missing parameter 'xPDLVersion'"
    assert "created" in params, "Missing parameter 'created'"
    assert "priorityUnit" in params, "Missing parameter 'priorityUnit'"
    assert "costUnit" in params, "Missing parameter 'costUnit'"

def test_xpdl1_packageheadertype_has_vendor():
    assert hasattr(xpdl1_PackageHeaderType, "vendor")
    descriptor = None
    for klass in xpdl1_PackageHeaderType.__mro__:
        if "vendor" in klass.__dict__:
            descriptor = klass.__dict__["vendor"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_packageheadertype_has_documentation():
    assert hasattr(xpdl1_PackageHeaderType, "documentation")
    descriptor = None
    for klass in xpdl1_PackageHeaderType.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_packageheadertype_has_description():
    assert hasattr(xpdl1_PackageHeaderType, "description")
    descriptor = None
    for klass in xpdl1_PackageHeaderType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_packageheadertype_has_xPDLVersion():
    assert hasattr(xpdl1_PackageHeaderType, "xPDLVersion")
    descriptor = None
    for klass in xpdl1_PackageHeaderType.__mro__:
        if "xPDLVersion" in klass.__dict__:
            descriptor = klass.__dict__["xPDLVersion"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_packageheadertype_has_created():
    assert hasattr(xpdl1_PackageHeaderType, "created")
    descriptor = None
    for klass in xpdl1_PackageHeaderType.__mro__:
        if "created" in klass.__dict__:
            descriptor = klass.__dict__["created"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_packageheadertype_has_priorityUnit():
    assert hasattr(xpdl1_PackageHeaderType, "priorityUnit")
    descriptor = None
    for klass in xpdl1_PackageHeaderType.__mro__:
        if "priorityUnit" in klass.__dict__:
            descriptor = klass.__dict__["priorityUnit"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_packageheadertype_has_costUnit():
    assert hasattr(xpdl1_PackageHeaderType, "costUnit")
    descriptor = None
    for klass in xpdl1_PackageHeaderType.__mro__:
        if "costUnit" in klass.__dict__:
            descriptor = klass.__dict__["costUnit"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_packagetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_PackageType)


def test_xpdl1_packagetype_constructor_exists():
    assert callable(xpdl1_PackageType.__init__)


def test_xpdl1_packagetype_constructor_args():
    sig = inspect.signature(xpdl1_PackageType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_xpdl1_packagetype_has_name():
    assert hasattr(xpdl1_PackageType, "name")
    descriptor = None
    for klass in xpdl1_PackageType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_packagetype_has_id():
    assert hasattr(xpdl1_PackageType, "id")
    descriptor = None
    for klass in xpdl1_PackageType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_formalparametertype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_FormalParameterType)


def test_xpdl1_formalparametertype_constructor_exists():
    assert callable(xpdl1_FormalParameterType.__init__)


def test_xpdl1_formalparametertype_constructor_args():
    sig = inspect.signature(xpdl1_FormalParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "mode" in params, "Missing parameter 'mode'"
    assert "index" in params, "Missing parameter 'index'"
    assert "id" in params, "Missing parameter 'id'"

def test_xpdl1_formalparametertype_has_description():
    assert hasattr(xpdl1_FormalParameterType, "description")
    descriptor = None
    for klass in xpdl1_FormalParameterType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_formalparametertype_has_mode():
    assert hasattr(xpdl1_FormalParameterType, "mode")
    descriptor = None
    for klass in xpdl1_FormalParameterType.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_formalparametertype_has_index():
    assert hasattr(xpdl1_FormalParameterType, "index")
    descriptor = None
    for klass in xpdl1_FormalParameterType.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_formalparametertype_has_id():
    assert hasattr(xpdl1_FormalParameterType, "id")
    descriptor = None
    for klass in xpdl1_FormalParameterType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_jointype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_JoinType)


def test_xpdl1_jointype_constructor_exists():
    assert callable(xpdl1_JoinType.__init__)


def test_xpdl1_jointype_constructor_args():
    sig = inspect.signature(xpdl1_JoinType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_xpdl1_jointype_has_type():
    assert hasattr(xpdl1_JoinType, "type")
    descriptor = None
    for klass in xpdl1_JoinType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_extendedattributetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ExtendedAttributeType)


def test_xpdl1_extendedattributetype_constructor_exists():
    assert callable(xpdl1_ExtendedAttributeType.__init__)


def test_xpdl1_extendedattributetype_constructor_args():
    sig = inspect.signature(xpdl1_ExtendedAttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "any" in params, "Missing parameter 'any'"
    assert "value" in params, "Missing parameter 'value'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "name" in params, "Missing parameter 'name'"

def test_xpdl1_extendedattributetype_has_group():
    assert hasattr(xpdl1_ExtendedAttributeType, "group")
    descriptor = None
    for klass in xpdl1_ExtendedAttributeType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_extendedattributetype_has_any():
    assert hasattr(xpdl1_ExtendedAttributeType, "any")
    descriptor = None
    for klass in xpdl1_ExtendedAttributeType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_extendedattributetype_has_value():
    assert hasattr(xpdl1_ExtendedAttributeType, "value")
    descriptor = None
    for klass in xpdl1_ExtendedAttributeType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_extendedattributetype_has_mixed():
    assert hasattr(xpdl1_ExtendedAttributeType, "mixed")
    descriptor = None
    for klass in xpdl1_ExtendedAttributeType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_extendedattributetype_has_name():
    assert hasattr(xpdl1_ExtendedAttributeType, "name")
    descriptor = None
    for klass in xpdl1_ExtendedAttributeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_enumerationvaluetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_EnumerationValueType)


def test_xpdl1_enumerationvaluetype_constructor_exists():
    assert callable(xpdl1_EnumerationValueType.__init__)


def test_xpdl1_enumerationvaluetype_constructor_args():
    sig = inspect.signature(xpdl1_EnumerationValueType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_xpdl1_enumerationvaluetype_has_name():
    assert hasattr(xpdl1_EnumerationValueType, "name")
    descriptor = None
    for klass in xpdl1_EnumerationValueType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_externalpackagestype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ExternalPackagesType)


def test_xpdl1_externalpackagestype_constructor_exists():
    assert callable(xpdl1_ExternalPackagesType.__init__)


def test_xpdl1_externalpackagestype_constructor_args():
    sig = inspect.signature(xpdl1_ExternalPackagesType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_externalpackagetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ExternalPackageType)


def test_xpdl1_externalpackagetype_constructor_exists():
    assert callable(xpdl1_ExternalPackageType.__init__)


def test_xpdl1_externalpackagetype_constructor_args():
    sig = inspect.signature(xpdl1_ExternalPackageType.__init__)
    params = list(sig.parameters.keys())
    assert "href" in params, "Missing parameter 'href'"

def test_xpdl1_externalpackagetype_has_href():
    assert hasattr(xpdl1_ExternalPackageType, "href")
    descriptor = None
    for klass in xpdl1_ExternalPackageType.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_eobject_is_not_abstract():
    assert not inspect.isabstract(xpdl1_EObject)


def test_xpdl1_eobject_constructor_exists():
    assert callable(xpdl1_EObject.__init__)


def test_xpdl1_eobject_constructor_args():
    sig = inspect.signature(xpdl1_EObject.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(xpdl1_EStringToStringMapEntry)


def test_xpdl1_estringtostringmapentry_constructor_exists():
    assert callable(xpdl1_EStringToStringMapEntry.__init__)


def test_xpdl1_estringtostringmapentry_constructor_args():
    sig = inspect.signature(xpdl1_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_documentroot_is_not_abstract():
    assert not inspect.isabstract(xpdl1_DocumentRoot)


def test_xpdl1_documentroot_constructor_exists():
    assert callable(xpdl1_DocumentRoot.__init__)


def test_xpdl1_documentroot_constructor_args():
    sig = inspect.signature(xpdl1_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "vendor" in params, "Missing parameter 'vendor'"
    assert "cost" in params, "Missing parameter 'cost'"
    assert "description" in params, "Missing parameter 'description'"
    assert "validTo" in params, "Missing parameter 'validTo'"
    assert "priorityUnit" in params, "Missing parameter 'priorityUnit'"
    assert "limit" in params, "Missing parameter 'limit'"
    assert "codepage" in params, "Missing parameter 'codepage'"
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "version" in params, "Missing parameter 'version'"
    assert "countrykey" in params, "Missing parameter 'countrykey'"
    assert "length" in params, "Missing parameter 'length'"
    assert "responsible" in params, "Missing parameter 'responsible'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "actualParameter" in params, "Missing parameter 'actualParameter'"
    assert "xPDLVersion" in params, "Missing parameter 'xPDLVersion'"
    assert "initialValue" in params, "Missing parameter 'initialValue'"
    assert "costUnit" in params, "Missing parameter 'costUnit'"
    assert "waitingTime" in params, "Missing parameter 'waitingTime'"
    assert "validFrom" in params, "Missing parameter 'validFrom'"
    assert "workingTime" in params, "Missing parameter 'workingTime'"
    assert "performer" in params, "Missing parameter 'performer'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "author" in params, "Missing parameter 'author'"
    assert "created" in params, "Missing parameter 'created'"

def test_xpdl1_documentroot_has_vendor():
    assert hasattr(xpdl1_DocumentRoot, "vendor")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "vendor" in klass.__dict__:
            descriptor = klass.__dict__["vendor"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_cost():
    assert hasattr(xpdl1_DocumentRoot, "cost")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_description():
    assert hasattr(xpdl1_DocumentRoot, "description")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_validTo():
    assert hasattr(xpdl1_DocumentRoot, "validTo")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "validTo" in klass.__dict__:
            descriptor = klass.__dict__["validTo"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_priorityUnit():
    assert hasattr(xpdl1_DocumentRoot, "priorityUnit")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "priorityUnit" in klass.__dict__:
            descriptor = klass.__dict__["priorityUnit"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_limit():
    assert hasattr(xpdl1_DocumentRoot, "limit")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "limit" in klass.__dict__:
            descriptor = klass.__dict__["limit"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_codepage():
    assert hasattr(xpdl1_DocumentRoot, "codepage")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "codepage" in klass.__dict__:
            descriptor = klass.__dict__["codepage"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_documentation():
    assert hasattr(xpdl1_DocumentRoot, "documentation")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_version():
    assert hasattr(xpdl1_DocumentRoot, "version")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_countrykey():
    assert hasattr(xpdl1_DocumentRoot, "countrykey")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "countrykey" in klass.__dict__:
            descriptor = klass.__dict__["countrykey"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_length():
    assert hasattr(xpdl1_DocumentRoot, "length")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_responsible():
    assert hasattr(xpdl1_DocumentRoot, "responsible")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "responsible" in klass.__dict__:
            descriptor = klass.__dict__["responsible"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_mixed():
    assert hasattr(xpdl1_DocumentRoot, "mixed")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_actualParameter():
    assert hasattr(xpdl1_DocumentRoot, "actualParameter")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "actualParameter" in klass.__dict__:
            descriptor = klass.__dict__["actualParameter"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_xPDLVersion():
    assert hasattr(xpdl1_DocumentRoot, "xPDLVersion")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "xPDLVersion" in klass.__dict__:
            descriptor = klass.__dict__["xPDLVersion"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_initialValue():
    assert hasattr(xpdl1_DocumentRoot, "initialValue")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "initialValue" in klass.__dict__:
            descriptor = klass.__dict__["initialValue"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_costUnit():
    assert hasattr(xpdl1_DocumentRoot, "costUnit")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "costUnit" in klass.__dict__:
            descriptor = klass.__dict__["costUnit"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_waitingTime():
    assert hasattr(xpdl1_DocumentRoot, "waitingTime")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "waitingTime" in klass.__dict__:
            descriptor = klass.__dict__["waitingTime"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_validFrom():
    assert hasattr(xpdl1_DocumentRoot, "validFrom")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "validFrom" in klass.__dict__:
            descriptor = klass.__dict__["validFrom"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_workingTime():
    assert hasattr(xpdl1_DocumentRoot, "workingTime")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "workingTime" in klass.__dict__:
            descriptor = klass.__dict__["workingTime"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_performer():
    assert hasattr(xpdl1_DocumentRoot, "performer")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "performer" in klass.__dict__:
            descriptor = klass.__dict__["performer"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_icon():
    assert hasattr(xpdl1_DocumentRoot, "icon")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_priority():
    assert hasattr(xpdl1_DocumentRoot, "priority")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_duration():
    assert hasattr(xpdl1_DocumentRoot, "duration")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_author():
    assert hasattr(xpdl1_DocumentRoot, "author")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_documentroot_has_created():
    assert hasattr(xpdl1_DocumentRoot, "created")
    descriptor = None
    for klass in xpdl1_DocumentRoot.__mro__:
        if "created" in klass.__dict__:
            descriptor = klass.__dict__["created"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_datatypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_DataTypeType)


def test_xpdl1_datatypetype_constructor_exists():
    assert callable(xpdl1_DataTypeType.__init__)


def test_xpdl1_datatypetype_constructor_args():
    sig = inspect.signature(xpdl1_DataTypeType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_datafieldtype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_DataFieldType)


def test_xpdl1_datafieldtype_constructor_exists():
    assert callable(xpdl1_DataFieldType.__init__)


def test_xpdl1_datafieldtype_constructor_args():
    sig = inspect.signature(xpdl1_DataFieldType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "isArray" in params, "Missing parameter 'isArray'"
    assert "description" in params, "Missing parameter 'description'"
    assert "initialValue" in params, "Missing parameter 'initialValue'"
    assert "length" in params, "Missing parameter 'length'"
    assert "name" in params, "Missing parameter 'name'"

def test_xpdl1_datafieldtype_has_id():
    assert hasattr(xpdl1_DataFieldType, "id")
    descriptor = None
    for klass in xpdl1_DataFieldType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_datafieldtype_has_isArray():
    assert hasattr(xpdl1_DataFieldType, "isArray")
    descriptor = None
    for klass in xpdl1_DataFieldType.__mro__:
        if "isArray" in klass.__dict__:
            descriptor = klass.__dict__["isArray"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_datafieldtype_has_description():
    assert hasattr(xpdl1_DataFieldType, "description")
    descriptor = None
    for klass in xpdl1_DataFieldType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_datafieldtype_has_initialValue():
    assert hasattr(xpdl1_DataFieldType, "initialValue")
    descriptor = None
    for klass in xpdl1_DataFieldType.__mro__:
        if "initialValue" in klass.__dict__:
            descriptor = klass.__dict__["initialValue"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_datafieldtype_has_length():
    assert hasattr(xpdl1_DataFieldType, "length")
    descriptor = None
    for klass in xpdl1_DataFieldType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_datafieldtype_has_name():
    assert hasattr(xpdl1_DataFieldType, "name")
    descriptor = None
    for klass in xpdl1_DataFieldType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_datafieldstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_DataFieldsType)


def test_xpdl1_datafieldstype_constructor_exists():
    assert callable(xpdl1_DataFieldsType.__init__)


def test_xpdl1_datafieldstype_constructor_args():
    sig = inspect.signature(xpdl1_DataFieldsType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_conformanceclasstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ConformanceClassType)


def test_xpdl1_conformanceclasstype_constructor_exists():
    assert callable(xpdl1_ConformanceClassType.__init__)


def test_xpdl1_conformanceclasstype_constructor_args():
    sig = inspect.signature(xpdl1_ConformanceClassType.__init__)
    params = list(sig.parameters.keys())
    assert "graphConformance" in params, "Missing parameter 'graphConformance'"

def test_xpdl1_conformanceclasstype_has_graphConformance():
    assert hasattr(xpdl1_ConformanceClassType, "graphConformance")
    descriptor = None
    for klass in xpdl1_ConformanceClassType.__mro__:
        if "graphConformance" in klass.__dict__:
            descriptor = klass.__dict__["graphConformance"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_xpressiontype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_XpressionType)


def test_xpdl1_xpressiontype_constructor_exists():
    assert callable(xpdl1_XpressionType.__init__)


def test_xpdl1_xpressiontype_constructor_args():
    sig = inspect.signature(xpdl1_XpressionType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "any" in params, "Missing parameter 'any'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xpdl1_xpressiontype_has_group():
    assert hasattr(xpdl1_XpressionType, "group")
    descriptor = None
    for klass in xpdl1_XpressionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_xpressiontype_has_any():
    assert hasattr(xpdl1_XpressionType, "any")
    descriptor = None
    for klass in xpdl1_XpressionType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_xpressiontype_has_mixed():
    assert hasattr(xpdl1_XpressionType, "mixed")
    descriptor = None
    for klass in xpdl1_XpressionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_automatictype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_AutomaticType)


def test_xpdl1_automatictype_constructor_exists():
    assert callable(xpdl1_AutomaticType.__init__)


def test_xpdl1_automatictype_constructor_args():
    sig = inspect.signature(xpdl1_AutomaticType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_listtypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ListTypeType)


def test_xpdl1_listtypetype_constructor_exists():
    assert callable(xpdl1_ListTypeType.__init__)


def test_xpdl1_listtypetype_constructor_args():
    sig = inspect.signature(xpdl1_ListTypeType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_enumerationtypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_EnumerationTypeType)


def test_xpdl1_enumerationtypetype_constructor_exists():
    assert callable(xpdl1_EnumerationTypeType.__init__)


def test_xpdl1_enumerationtypetype_constructor_args():
    sig = inspect.signature(xpdl1_EnumerationTypeType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_conditiontype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ConditionType)


def test_xpdl1_conditiontype_constructor_exists():
    assert callable(xpdl1_ConditionType.__init__)


def test_xpdl1_conditiontype_constructor_args():
    sig = inspect.signature(xpdl1_ConditionType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"
    assert "type" in params, "Missing parameter 'type'"

def test_xpdl1_conditiontype_has_mixed():
    assert hasattr(xpdl1_ConditionType, "mixed")
    descriptor = None
    for klass in xpdl1_ConditionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_conditiontype_has_group():
    assert hasattr(xpdl1_ConditionType, "group")
    descriptor = None
    for klass in xpdl1_ConditionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_conditiontype_has_type():
    assert hasattr(xpdl1_ConditionType, "type")
    descriptor = None
    for klass in xpdl1_ConditionType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_schematypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_SchemaTypeType)


def test_xpdl1_schematypetype_constructor_exists():
    assert callable(xpdl1_SchemaTypeType.__init__)


def test_xpdl1_schematypetype_constructor_args():
    sig = inspect.signature(xpdl1_SchemaTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"

def test_xpdl1_schematypetype_has_any():
    assert hasattr(xpdl1_SchemaTypeType, "any")
    descriptor = None
    for klass in xpdl1_SchemaTypeType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_declaredtypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_DeclaredTypeType)


def test_xpdl1_declaredtypetype_constructor_exists():
    assert callable(xpdl1_DeclaredTypeType.__init__)


def test_xpdl1_declaredtypetype_constructor_args():
    sig = inspect.signature(xpdl1_DeclaredTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_xpdl1_declaredtypetype_has_id():
    assert hasattr(xpdl1_DeclaredTypeType, "id")
    descriptor = None
    for klass in xpdl1_DeclaredTypeType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_basictypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_BasicTypeType)


def test_xpdl1_basictypetype_constructor_exists():
    assert callable(xpdl1_BasicTypeType.__init__)


def test_xpdl1_basictypetype_constructor_args():
    sig = inspect.signature(xpdl1_BasicTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_xpdl1_basictypetype_has_type():
    assert hasattr(xpdl1_BasicTypeType, "type")
    descriptor = None
    for klass in xpdl1_BasicTypeType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_arraytypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ArrayTypeType)


def test_xpdl1_arraytypetype_constructor_exists():
    assert callable(xpdl1_ArrayTypeType.__init__)


def test_xpdl1_arraytypetype_constructor_args():
    sig = inspect.signature(xpdl1_ArrayTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "upperIndex" in params, "Missing parameter 'upperIndex'"
    assert "lowerIndex" in params, "Missing parameter 'lowerIndex'"

def test_xpdl1_arraytypetype_has_upperIndex():
    assert hasattr(xpdl1_ArrayTypeType, "upperIndex")
    descriptor = None
    for klass in xpdl1_ArrayTypeType.__mro__:
        if "upperIndex" in klass.__dict__:
            descriptor = klass.__dict__["upperIndex"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_arraytypetype_has_lowerIndex():
    assert hasattr(xpdl1_ArrayTypeType, "lowerIndex")
    descriptor = None
    for klass in xpdl1_ArrayTypeType.__mro__:
        if "lowerIndex" in klass.__dict__:
            descriptor = klass.__dict__["lowerIndex"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_uniontypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_UnionTypeType)


def test_xpdl1_uniontypetype_constructor_exists():
    assert callable(xpdl1_UnionTypeType.__init__)


def test_xpdl1_uniontypetype_constructor_args():
    sig = inspect.signature(xpdl1_UnionTypeType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_recordtypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_RecordTypeType)


def test_xpdl1_recordtypetype_constructor_exists():
    assert callable(xpdl1_RecordTypeType.__init__)


def test_xpdl1_recordtypetype_constructor_args():
    sig = inspect.signature(xpdl1_RecordTypeType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_applicationtype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ApplicationType)


def test_xpdl1_applicationtype_constructor_exists():
    assert callable(xpdl1_ApplicationType.__init__)


def test_xpdl1_applicationtype_constructor_args():
    sig = inspect.signature(xpdl1_ApplicationType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_xpdl1_applicationtype_has_id():
    assert hasattr(xpdl1_ApplicationType, "id")
    descriptor = None
    for klass in xpdl1_ApplicationType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_applicationtype_has_description():
    assert hasattr(xpdl1_ApplicationType, "description")
    descriptor = None
    for klass in xpdl1_ApplicationType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_applicationtype_has_name():
    assert hasattr(xpdl1_ApplicationType, "name")
    descriptor = None
    for klass in xpdl1_ApplicationType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_applicationstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ApplicationsType)


def test_xpdl1_applicationstype_constructor_exists():
    assert callable(xpdl1_ApplicationsType.__init__)


def test_xpdl1_applicationstype_constructor_args():
    sig = inspect.signature(xpdl1_ApplicationsType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_actualparameterstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ActualParametersType)


def test_xpdl1_actualparameterstype_constructor_exists():
    assert callable(xpdl1_ActualParametersType.__init__)


def test_xpdl1_actualparameterstype_constructor_args():
    sig = inspect.signature(xpdl1_ActualParametersType.__init__)
    params = list(sig.parameters.keys())
    assert "actualParameter" in params, "Missing parameter 'actualParameter'"

def test_xpdl1_actualparameterstype_has_actualParameter():
    assert hasattr(xpdl1_ActualParametersType, "actualParameter")
    descriptor = None
    for klass in xpdl1_ActualParametersType.__mro__:
        if "actualParameter" in klass.__dict__:
            descriptor = klass.__dict__["actualParameter"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_extendedattributestype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ExtendedAttributesType)


def test_xpdl1_extendedattributestype_constructor_exists():
    assert callable(xpdl1_ExtendedAttributesType.__init__)


def test_xpdl1_extendedattributestype_constructor_args():
    sig = inspect.signature(xpdl1_ExtendedAttributesType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_externalreferencetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ExternalReferenceType)


def test_xpdl1_externalreferencetype_constructor_exists():
    assert callable(xpdl1_ExternalReferenceType.__init__)


def test_xpdl1_externalreferencetype_constructor_args():
    sig = inspect.signature(xpdl1_ExternalReferenceType.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "xref" in params, "Missing parameter 'xref'"
    assert "location" in params, "Missing parameter 'location'"

def test_xpdl1_externalreferencetype_has_namespace():
    assert hasattr(xpdl1_ExternalReferenceType, "namespace")
    descriptor = None
    for klass in xpdl1_ExternalReferenceType.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_externalreferencetype_has_xref():
    assert hasattr(xpdl1_ExternalReferenceType, "xref")
    descriptor = None
    for klass in xpdl1_ExternalReferenceType.__mro__:
        if "xref" in klass.__dict__:
            descriptor = klass.__dict__["xref"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_externalreferencetype_has_location():
    assert hasattr(xpdl1_ExternalReferenceType, "location")
    descriptor = None
    for klass in xpdl1_ExternalReferenceType.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_formalparameterstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_FormalParametersType)


def test_xpdl1_formalparameterstype_constructor_exists():
    assert callable(xpdl1_FormalParametersType.__init__)


def test_xpdl1_formalparameterstype_constructor_args():
    sig = inspect.signature(xpdl1_FormalParametersType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_simulationinformationtype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_SimulationInformationType)


def test_xpdl1_simulationinformationtype_constructor_exists():
    assert callable(xpdl1_SimulationInformationType.__init__)


def test_xpdl1_simulationinformationtype_constructor_args():
    sig = inspect.signature(xpdl1_SimulationInformationType.__init__)
    params = list(sig.parameters.keys())
    assert "cost" in params, "Missing parameter 'cost'"
    assert "instantiation" in params, "Missing parameter 'instantiation'"

def test_xpdl1_simulationinformationtype_has_cost():
    assert hasattr(xpdl1_SimulationInformationType, "cost")
    descriptor = None
    for klass in xpdl1_SimulationInformationType.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_simulationinformationtype_has_instantiation():
    assert hasattr(xpdl1_SimulationInformationType, "instantiation")
    descriptor = None
    for klass in xpdl1_SimulationInformationType.__mro__:
        if "instantiation" in klass.__dict__:
            descriptor = klass.__dict__["instantiation"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_deadlinetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_DeadlineType)


def test_xpdl1_deadlinetype_constructor_exists():
    assert callable(xpdl1_DeadlineType.__init__)


def test_xpdl1_deadlinetype_constructor_args():
    sig = inspect.signature(xpdl1_DeadlineType.__init__)
    params = list(sig.parameters.keys())
    assert "execution" in params, "Missing parameter 'execution'"

def test_xpdl1_deadlinetype_has_execution():
    assert hasattr(xpdl1_DeadlineType, "execution")
    descriptor = None
    for klass in xpdl1_DeadlineType.__mro__:
        if "execution" in klass.__dict__:
            descriptor = klass.__dict__["execution"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_finishmodetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_FinishModeType)


def test_xpdl1_finishmodetype_constructor_exists():
    assert callable(xpdl1_FinishModeType.__init__)


def test_xpdl1_finishmodetype_constructor_args():
    sig = inspect.signature(xpdl1_FinishModeType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_startmodetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_StartModeType)


def test_xpdl1_startmodetype_constructor_exists():
    assert callable(xpdl1_StartModeType.__init__)


def test_xpdl1_startmodetype_constructor_args():
    sig = inspect.signature(xpdl1_StartModeType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_blockactivitytype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_BlockActivityType)


def test_xpdl1_blockactivitytype_constructor_exists():
    assert callable(xpdl1_BlockActivityType.__init__)


def test_xpdl1_blockactivitytype_constructor_args():
    sig = inspect.signature(xpdl1_BlockActivityType.__init__)
    params = list(sig.parameters.keys())
    assert "blockId" in params, "Missing parameter 'blockId'"

def test_xpdl1_blockactivitytype_has_blockId():
    assert hasattr(xpdl1_BlockActivityType, "blockId")
    descriptor = None
    for klass in xpdl1_BlockActivityType.__mro__:
        if "blockId" in klass.__dict__:
            descriptor = klass.__dict__["blockId"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_transitionrestrictionstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_TransitionRestrictionsType)


def test_xpdl1_transitionrestrictionstype_constructor_exists():
    assert callable(xpdl1_TransitionRestrictionsType.__init__)


def test_xpdl1_transitionrestrictionstype_constructor_args():
    sig = inspect.signature(xpdl1_TransitionRestrictionsType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_transitionstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_TransitionsType)


def test_xpdl1_transitionstype_constructor_exists():
    assert callable(xpdl1_TransitionsType.__init__)


def test_xpdl1_transitionstype_constructor_args():
    sig = inspect.signature(xpdl1_TransitionsType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_implementationtype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ImplementationType)


def test_xpdl1_implementationtype_constructor_exists():
    assert callable(xpdl1_ImplementationType.__init__)


def test_xpdl1_implementationtype_constructor_args():
    sig = inspect.signature(xpdl1_ImplementationType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_routetype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_RouteType)


def test_xpdl1_routetype_constructor_exists():
    assert callable(xpdl1_RouteType.__init__)


def test_xpdl1_routetype_constructor_args():
    sig = inspect.signature(xpdl1_RouteType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_activitiestype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ActivitiesType)


def test_xpdl1_activitiestype_constructor_exists():
    assert callable(xpdl1_ActivitiesType.__init__)


def test_xpdl1_activitiestype_constructor_args():
    sig = inspect.signature(xpdl1_ActivitiesType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_activitysettype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ActivitySetType)


def test_xpdl1_activitysettype_constructor_exists():
    assert callable(xpdl1_ActivitySetType.__init__)


def test_xpdl1_activitysettype_constructor_args():
    sig = inspect.signature(xpdl1_ActivitySetType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_xpdl1_activitysettype_has_id():
    assert hasattr(xpdl1_ActivitySetType, "id")
    descriptor = None
    for klass in xpdl1_ActivitySetType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xpdl1_activitysetstype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ActivitySetsType)


def test_xpdl1_activitysetstype_constructor_exists():
    assert callable(xpdl1_ActivitySetsType.__init__)


def test_xpdl1_activitysetstype_constructor_args():
    sig = inspect.signature(xpdl1_ActivitySetsType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl1_activitytype_is_not_abstract():
    assert not inspect.isabstract(xpdl1_ActivityType)


def test_xpdl1_activitytype_constructor_exists():
    assert callable(xpdl1_ActivityType.__init__)


def test_xpdl1_activitytype_constructor_args():
    sig = inspect.signature(xpdl1_ActivityType.__init__)
    params = list(sig.parameters.keys())
    assert "performer" in params, "Missing parameter 'performer'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "limit" in params, "Missing parameter 'limit'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "id" in params, "Missing parameter 'id'"
    assert "documentation" in params, "Missing parameter 'documentation'"

def test_xpdl1_activitytype_has_performer():
    assert hasattr(xpdl1_ActivityType, "performer")
    descriptor = None
    for klass in xpdl1_ActivityType.__mro__:
        if "performer" in klass.__dict__:
            descriptor = klass.__dict__["performer"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_activitytype_has_description():
    assert hasattr(xpdl1_ActivityType, "description")
    descriptor = None
    for klass in xpdl1_ActivityType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_activitytype_has_name():
    assert hasattr(xpdl1_ActivityType, "name")
    descriptor = None
    for klass in xpdl1_ActivityType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_activitytype_has_limit():
    assert hasattr(xpdl1_ActivityType, "limit")
    descriptor = None
    for klass in xpdl1_ActivityType.__mro__:
        if "limit" in klass.__dict__:
            descriptor = klass.__dict__["limit"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_activitytype_has_icon():
    assert hasattr(xpdl1_ActivityType, "icon")
    descriptor = None
    for klass in xpdl1_ActivityType.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_activitytype_has_priority():
    assert hasattr(xpdl1_ActivityType, "priority")
    descriptor = None
    for klass in xpdl1_ActivityType.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_activitytype_has_id():
    assert hasattr(xpdl1_ActivityType, "id")
    descriptor = None
    for klass in xpdl1_ActivityType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl1_activitytype_has_documentation():
    assert hasattr(xpdl1_ActivityType, "documentation")
    descriptor = None
    for klass in xpdl1_ActivityType.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)

def test_typetype1_exists():
    # Check that the Enumeration exists
    assert TypeType1 is not None

def test_typetype1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeType1]
    expected_literals = [
        "ROLE",
        "ORGANIZATIONALUNIT",
        "RESOURCE",
        "SYSTEM",
        "HUMAN",
        "RESOURCESET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeType1"

def test_publicationstatustype_exists():
    # Check that the Enumeration exists
    assert PublicationStatusType is not None

def test_publicationstatustype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PublicationStatusType]
    expected_literals = [
        "UNDERREVISION",
        "UNDERTEST",
        "RELEASED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PublicationStatusType"

def test_modetype_exists():
    # Check that the Enumeration exists
    assert ModeType is not None

def test_modetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ModeType]
    expected_literals = [
        "IN",
        "INOUT",
        "OUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModeType"

def test_typetype_exists():
    # Check that the Enumeration exists
    assert TypeType is not None

def test_typetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeType]
    expected_literals = [
        "AND",
        "XOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeType"

def test_executiontype1_exists():
    # Check that the Enumeration exists
    assert ExecutionType1 is not None

def test_executiontype1_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExecutionType1]
    expected_literals = [
        "ASYNCHR",
        "SYNCHR",
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
        "PRIVATE",
        "PUBLIC",
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
        "DEFAULTEXCEPTION",
        "EXCEPTION",
        "OTHERWISE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeType2"

def test_typetype5_exists():
    # Check that the Enumeration exists
    assert TypeType5 is not None

def test_typetype5_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeType5]
    expected_literals = [
        "PROCEDURE",
        "APPLICATION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeType5"

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

def test_isarraytype_exists():
    # Check that the Enumeration exists
    assert IsArrayType is not None

def test_isarraytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IsArrayType]
    expected_literals = [
        "FALSE",
        "TRUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IsArrayType"

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

def test_typetype3_exists():
    # Check that the Enumeration exists
    assert TypeType3 is not None

def test_typetype3_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeType3]
    expected_literals = [
        "FLOAT",
        "INTEGER",
        "PERFORMER",
        "BOOLEAN",
        "STRING",
        "DATETIME",
        "REFERENCE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeType3"

def test_typetype4_exists():
    # Check that the Enumeration exists
    assert TypeType4 is not None

def test_typetype4_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeType4]
    expected_literals = [
        "XOR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeType4"

def test_graphconformancetype_exists():
    # Check that the Enumeration exists
    assert GraphConformanceType is not None

def test_graphconformancetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GraphConformanceType]
    expected_literals = [
        "NONBLOCKED",
        "LOOPBLOCKED",
        "FULLBLOCKED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GraphConformanceType"

def test_durationunittype_exists():
    # Check that the Enumeration exists
    assert DurationUnitType is not None

def test_durationunittype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DurationUnitType]
    expected_literals = [
        "D",
        "h",
        "Y",
        "s",
        "m1",
        "M",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DurationUnitType"


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
xpdl1_WorkflowProcessType_strategy = st.builds(
    xpdl1_WorkflowProcessType,
    accessLevel=
        safe_text,
    id=
        safe_text,
    name=
        safe_text
)
xpdl1_WorkflowProcessesType_strategy = st.builds(
    xpdl1_WorkflowProcessesType,
)
xpdl1_TransitionRestrictionType_strategy = st.builds(
    xpdl1_TransitionRestrictionType,
)
xpdl1_TransitionRefsType_strategy = st.builds(
    xpdl1_TransitionRefsType,
)
xpdl1_TypeDeclarationsType_strategy = st.builds(
    xpdl1_TypeDeclarationsType,
)
xpdl1_TypeDeclarationType_strategy = st.builds(
    xpdl1_TypeDeclarationType,
    id=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
xpdl1_TimeEstimationType_strategy = st.builds(
    xpdl1_TimeEstimationType,
    duration=
        safe_text,
    workingTime=
        safe_text,
    waitingTime=
        safe_text
)
xpdl1_SubFlowType_strategy = st.builds(
    xpdl1_SubFlowType,
    execution=
        safe_text,
    id=
        safe_text
)
xpdl1_SplitType_strategy = st.builds(
    xpdl1_SplitType,
    type=
        safe_text
)
xpdl1_TransitionRefType_strategy = st.builds(
    xpdl1_TransitionRefType,
    id=
        safe_text
)
xpdl1_TransitionType_strategy = st.builds(
    xpdl1_TransitionType,
    from_=
        safe_text,
    description=
        safe_text,
    to=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)
xpdl1_ToolType_strategy = st.builds(
    xpdl1_ToolType,
    id=
        safe_text,
    type=
        safe_text,
    description=
        safe_text
)
xpdl1_ResponsiblesType_strategy = st.builds(
    xpdl1_ResponsiblesType,
    responsible=
        safe_text
)
xpdl1_RedefinableHeaderType_strategy = st.builds(
    xpdl1_RedefinableHeaderType,
    countrykey=
        safe_text,
    version=
        safe_text,
    author=
        safe_text,
    publicationStatus=
        safe_text,
    codepage=
        safe_text
)
xpdl1_ScriptType_strategy = st.builds(
    xpdl1_ScriptType,
    version=
        safe_text,
    type=
        safe_text,
    grammar=
        safe_text
)
xpdl1_ParticipantTypeType_strategy = st.builds(
    xpdl1_ParticipantTypeType,
    type=
        safe_text
)
xpdl1_ParticipantsType_strategy = st.builds(
    xpdl1_ParticipantsType,
)
xpdl1_ParticipantType_strategy = st.builds(
    xpdl1_ParticipantType,
    id=
        safe_text,
    name=
        safe_text,
    description=
        safe_text
)
xpdl1_ProcessHeaderType_strategy = st.builds(
    xpdl1_ProcessHeaderType,
    validFrom=
        safe_text,
    limit=
        safe_text,
    durationUnit=
        safe_text,
    validTo=
        safe_text,
    description=
        safe_text,
    created=
        safe_text,
    priority=
        safe_text
)
xpdl1_NoType_strategy = st.builds(
    xpdl1_NoType,
)
xpdl1_MemberType_strategy = st.builds(
    xpdl1_MemberType,
)
xpdl1_ManualType_strategy = st.builds(
    xpdl1_ManualType,
)
xpdl1_PackageHeaderType_strategy = st.builds(
    xpdl1_PackageHeaderType,
    vendor=
        safe_text,
    documentation=
        safe_text,
    description=
        safe_text,
    xPDLVersion=
        safe_text,
    created=
        safe_text,
    priorityUnit=
        safe_text,
    costUnit=
        safe_text
)
xpdl1_PackageType_strategy = st.builds(
    xpdl1_PackageType,
    name=
        safe_text,
    id=
        safe_text
)
xpdl1_FormalParameterType_strategy = st.builds(
    xpdl1_FormalParameterType,
    description=
        safe_text,
    mode=
        safe_text,
    index=
        safe_text,
    id=
        safe_text
)
xpdl1_JoinType_strategy = st.builds(
    xpdl1_JoinType,
    type=
        safe_text
)
xpdl1_ExtendedAttributeType_strategy = st.builds(
    xpdl1_ExtendedAttributeType,
    group=
        safe_text,
    any=
        safe_text,
    value=
        safe_text,
    mixed=
        safe_text,
    name=
        safe_text
)
xpdl1_EnumerationValueType_strategy = st.builds(
    xpdl1_EnumerationValueType,
    name=
        safe_text
)
xpdl1_ExternalPackagesType_strategy = st.builds(
    xpdl1_ExternalPackagesType,
)
xpdl1_ExternalPackageType_strategy = st.builds(
    xpdl1_ExternalPackageType,
    href=
        safe_text
)
xpdl1_EObject_strategy = st.builds(
    xpdl1_EObject,
)
xpdl1_EStringToStringMapEntry_strategy = st.builds(
    xpdl1_EStringToStringMapEntry,
)
xpdl1_DocumentRoot_strategy = st.builds(
    xpdl1_DocumentRoot,
    vendor=
        safe_text,
    cost=
        safe_text,
    description=
        safe_text,
    validTo=
        safe_text,
    priorityUnit=
        safe_text,
    limit=
        safe_text,
    codepage=
        safe_text,
    documentation=
        safe_text,
    version=
        safe_text,
    countrykey=
        safe_text,
    length=
        safe_text,
    responsible=
        safe_text,
    mixed=
        safe_text,
    actualParameter=
        safe_text,
    xPDLVersion=
        safe_text,
    initialValue=
        safe_text,
    costUnit=
        safe_text,
    waitingTime=
        safe_text,
    validFrom=
        safe_text,
    workingTime=
        safe_text,
    performer=
        safe_text,
    icon=
        safe_text,
    priority=
        safe_text,
    duration=
        safe_text,
    author=
        safe_text,
    created=
        safe_text
)
xpdl1_DataTypeType_strategy = st.builds(
    xpdl1_DataTypeType,
)
xpdl1_DataFieldType_strategy = st.builds(
    xpdl1_DataFieldType,
    id=
        safe_text,
    isArray=
        safe_text,
    description=
        safe_text,
    initialValue=
        safe_text,
    length=
        safe_text,
    name=
        safe_text
)
xpdl1_DataFieldsType_strategy = st.builds(
    xpdl1_DataFieldsType,
)
xpdl1_ConformanceClassType_strategy = st.builds(
    xpdl1_ConformanceClassType,
    graphConformance=
        safe_text
)
xpdl1_XpressionType_strategy = st.builds(
    xpdl1_XpressionType,
    group=
        safe_text,
    any=
        safe_text,
    mixed=
        safe_text
)
xpdl1_AutomaticType_strategy = st.builds(
    xpdl1_AutomaticType,
)
xpdl1_ListTypeType_strategy = st.builds(
    xpdl1_ListTypeType,
)
xpdl1_EnumerationTypeType_strategy = st.builds(
    xpdl1_EnumerationTypeType,
)
xpdl1_ConditionType_strategy = st.builds(
    xpdl1_ConditionType,
    mixed=
        safe_text,
    group=
        safe_text,
    type=
        safe_text
)
xpdl1_SchemaTypeType_strategy = st.builds(
    xpdl1_SchemaTypeType,
    any=
        safe_text
)
xpdl1_DeclaredTypeType_strategy = st.builds(
    xpdl1_DeclaredTypeType,
    id=
        safe_text
)
xpdl1_BasicTypeType_strategy = st.builds(
    xpdl1_BasicTypeType,
    type=
        safe_text
)
xpdl1_ArrayTypeType_strategy = st.builds(
    xpdl1_ArrayTypeType,
    upperIndex=
        safe_text,
    lowerIndex=
        safe_text
)
xpdl1_UnionTypeType_strategy = st.builds(
    xpdl1_UnionTypeType,
)
xpdl1_RecordTypeType_strategy = st.builds(
    xpdl1_RecordTypeType,
)
xpdl1_ApplicationType_strategy = st.builds(
    xpdl1_ApplicationType,
    id=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
xpdl1_ApplicationsType_strategy = st.builds(
    xpdl1_ApplicationsType,
)
xpdl1_ActualParametersType_strategy = st.builds(
    xpdl1_ActualParametersType,
    actualParameter=
        safe_text
)
xpdl1_ExtendedAttributesType_strategy = st.builds(
    xpdl1_ExtendedAttributesType,
)
xpdl1_ExternalReferenceType_strategy = st.builds(
    xpdl1_ExternalReferenceType,
    namespace=
        safe_text,
    xref=
        safe_text,
    location=
        safe_text
)
xpdl1_FormalParametersType_strategy = st.builds(
    xpdl1_FormalParametersType,
)
xpdl1_SimulationInformationType_strategy = st.builds(
    xpdl1_SimulationInformationType,
    cost=
        safe_text,
    instantiation=
        safe_text
)
xpdl1_DeadlineType_strategy = st.builds(
    xpdl1_DeadlineType,
    execution=
        safe_text
)
xpdl1_FinishModeType_strategy = st.builds(
    xpdl1_FinishModeType,
)
xpdl1_StartModeType_strategy = st.builds(
    xpdl1_StartModeType,
)
xpdl1_BlockActivityType_strategy = st.builds(
    xpdl1_BlockActivityType,
    blockId=
        safe_text
)
xpdl1_TransitionRestrictionsType_strategy = st.builds(
    xpdl1_TransitionRestrictionsType,
)
xpdl1_TransitionsType_strategy = st.builds(
    xpdl1_TransitionsType,
)
xpdl1_ImplementationType_strategy = st.builds(
    xpdl1_ImplementationType,
)
xpdl1_RouteType_strategy = st.builds(
    xpdl1_RouteType,
)
xpdl1_ActivitiesType_strategy = st.builds(
    xpdl1_ActivitiesType,
)
xpdl1_ActivitySetType_strategy = st.builds(
    xpdl1_ActivitySetType,
    id=
        safe_text
)
xpdl1_ActivitySetsType_strategy = st.builds(
    xpdl1_ActivitySetsType,
)
xpdl1_ActivityType_strategy = st.builds(
    xpdl1_ActivityType,
    performer=
        safe_text,
    description=
        safe_text,
    name=
        safe_text,
    limit=
        safe_text,
    icon=
        safe_text,
    priority=
        safe_text,
    id=
        safe_text,
    documentation=
        safe_text
)

@given(instance=xpdl1_WorkflowProcessType_strategy)
@settings(max_examples=50)
def test_xpdl1_workflowprocesstype_instantiation(instance):
    assert isinstance(instance, xpdl1_WorkflowProcessType)



@given(instance=xpdl1_WorkflowProcessType_strategy)
def test_xpdl1_workflowprocesstype_accessLevel_setter(instance):
    original = instance.accessLevel
    instance.accessLevel = original
    assert instance.accessLevel == original



@given(instance=xpdl1_WorkflowProcessType_strategy)
def test_xpdl1_workflowprocesstype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xpdl1_WorkflowProcessType_strategy)
def test_xpdl1_workflowprocesstype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl1_WorkflowProcessesType_strategy)
@settings(max_examples=50)
def test_xpdl1_workflowprocessestype_instantiation(instance):
    assert isinstance(instance, xpdl1_WorkflowProcessesType)

@given(instance=xpdl1_TransitionRestrictionType_strategy)
@settings(max_examples=50)
def test_xpdl1_transitionrestrictiontype_instantiation(instance):
    assert isinstance(instance, xpdl1_TransitionRestrictionType)

@given(instance=xpdl1_TransitionRefsType_strategy)
@settings(max_examples=50)
def test_xpdl1_transitionrefstype_instantiation(instance):
    assert isinstance(instance, xpdl1_TransitionRefsType)

@given(instance=xpdl1_TypeDeclarationsType_strategy)
@settings(max_examples=50)
def test_xpdl1_typedeclarationstype_instantiation(instance):
    assert isinstance(instance, xpdl1_TypeDeclarationsType)

@given(instance=xpdl1_TypeDeclarationType_strategy)
@settings(max_examples=50)
def test_xpdl1_typedeclarationtype_instantiation(instance):
    assert isinstance(instance, xpdl1_TypeDeclarationType)



@given(instance=xpdl1_TypeDeclarationType_strategy)
def test_xpdl1_typedeclarationtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xpdl1_TypeDeclarationType_strategy)
def test_xpdl1_typedeclarationtype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=xpdl1_TypeDeclarationType_strategy)
def test_xpdl1_typedeclarationtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl1_TimeEstimationType_strategy)
@settings(max_examples=50)
def test_xpdl1_timeestimationtype_instantiation(instance):
    assert isinstance(instance, xpdl1_TimeEstimationType)



@given(instance=xpdl1_TimeEstimationType_strategy)
def test_xpdl1_timeestimationtype_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=xpdl1_TimeEstimationType_strategy)
def test_xpdl1_timeestimationtype_workingTime_setter(instance):
    original = instance.workingTime
    instance.workingTime = original
    assert instance.workingTime == original



@given(instance=xpdl1_TimeEstimationType_strategy)
def test_xpdl1_timeestimationtype_waitingTime_setter(instance):
    original = instance.waitingTime
    instance.waitingTime = original
    assert instance.waitingTime == original

@given(instance=xpdl1_SubFlowType_strategy)
@settings(max_examples=50)
def test_xpdl1_subflowtype_instantiation(instance):
    assert isinstance(instance, xpdl1_SubFlowType)



@given(instance=xpdl1_SubFlowType_strategy)
def test_xpdl1_subflowtype_execution_setter(instance):
    original = instance.execution
    instance.execution = original
    assert instance.execution == original



@given(instance=xpdl1_SubFlowType_strategy)
def test_xpdl1_subflowtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1_SplitType_strategy)
@settings(max_examples=50)
def test_xpdl1_splittype_instantiation(instance):
    assert isinstance(instance, xpdl1_SplitType)



@given(instance=xpdl1_SplitType_strategy)
def test_xpdl1_splittype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xpdl1_TransitionRefType_strategy)
@settings(max_examples=50)
def test_xpdl1_transitionreftype_instantiation(instance):
    assert isinstance(instance, xpdl1_TransitionRefType)



@given(instance=xpdl1_TransitionRefType_strategy)
def test_xpdl1_transitionreftype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1_TransitionType_strategy)
@settings(max_examples=50)
def test_xpdl1_transitiontype_instantiation(instance):
    assert isinstance(instance, xpdl1_TransitionType)



@given(instance=xpdl1_TransitionType_strategy)
def test_xpdl1_transitiontype_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original



@given(instance=xpdl1_TransitionType_strategy)
def test_xpdl1_transitiontype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=xpdl1_TransitionType_strategy)
def test_xpdl1_transitiontype_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original



@given(instance=xpdl1_TransitionType_strategy)
def test_xpdl1_transitiontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xpdl1_TransitionType_strategy)
def test_xpdl1_transitiontype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1_ToolType_strategy)
@settings(max_examples=50)
def test_xpdl1_tooltype_instantiation(instance):
    assert isinstance(instance, xpdl1_ToolType)



@given(instance=xpdl1_ToolType_strategy)
def test_xpdl1_tooltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xpdl1_ToolType_strategy)
def test_xpdl1_tooltype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xpdl1_ToolType_strategy)
def test_xpdl1_tooltype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=xpdl1_ResponsiblesType_strategy)
@settings(max_examples=50)
def test_xpdl1_responsiblestype_instantiation(instance):
    assert isinstance(instance, xpdl1_ResponsiblesType)



@given(instance=xpdl1_ResponsiblesType_strategy)
def test_xpdl1_responsiblestype_responsible_setter(instance):
    original = instance.responsible
    instance.responsible = original
    assert instance.responsible == original

@given(instance=xpdl1_RedefinableHeaderType_strategy)
@settings(max_examples=50)
def test_xpdl1_redefinableheadertype_instantiation(instance):
    assert isinstance(instance, xpdl1_RedefinableHeaderType)



@given(instance=xpdl1_RedefinableHeaderType_strategy)
def test_xpdl1_redefinableheadertype_countrykey_setter(instance):
    original = instance.countrykey
    instance.countrykey = original
    assert instance.countrykey == original



@given(instance=xpdl1_RedefinableHeaderType_strategy)
def test_xpdl1_redefinableheadertype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=xpdl1_RedefinableHeaderType_strategy)
def test_xpdl1_redefinableheadertype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=xpdl1_RedefinableHeaderType_strategy)
def test_xpdl1_redefinableheadertype_publicationStatus_setter(instance):
    original = instance.publicationStatus
    instance.publicationStatus = original
    assert instance.publicationStatus == original



@given(instance=xpdl1_RedefinableHeaderType_strategy)
def test_xpdl1_redefinableheadertype_codepage_setter(instance):
    original = instance.codepage
    instance.codepage = original
    assert instance.codepage == original

@given(instance=xpdl1_ScriptType_strategy)
@settings(max_examples=50)
def test_xpdl1_scripttype_instantiation(instance):
    assert isinstance(instance, xpdl1_ScriptType)



@given(instance=xpdl1_ScriptType_strategy)
def test_xpdl1_scripttype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=xpdl1_ScriptType_strategy)
def test_xpdl1_scripttype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xpdl1_ScriptType_strategy)
def test_xpdl1_scripttype_grammar_setter(instance):
    original = instance.grammar
    instance.grammar = original
    assert instance.grammar == original

@given(instance=xpdl1_ParticipantTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1_participanttypetype_instantiation(instance):
    assert isinstance(instance, xpdl1_ParticipantTypeType)



@given(instance=xpdl1_ParticipantTypeType_strategy)
def test_xpdl1_participanttypetype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xpdl1_ParticipantsType_strategy)
@settings(max_examples=50)
def test_xpdl1_participantstype_instantiation(instance):
    assert isinstance(instance, xpdl1_ParticipantsType)

@given(instance=xpdl1_ParticipantType_strategy)
@settings(max_examples=50)
def test_xpdl1_participanttype_instantiation(instance):
    assert isinstance(instance, xpdl1_ParticipantType)



@given(instance=xpdl1_ParticipantType_strategy)
def test_xpdl1_participanttype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xpdl1_ParticipantType_strategy)
def test_xpdl1_participanttype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xpdl1_ParticipantType_strategy)
def test_xpdl1_participanttype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=xpdl1_ProcessHeaderType_strategy)
@settings(max_examples=50)
def test_xpdl1_processheadertype_instantiation(instance):
    assert isinstance(instance, xpdl1_ProcessHeaderType)



@given(instance=xpdl1_ProcessHeaderType_strategy)
def test_xpdl1_processheadertype_validFrom_setter(instance):
    original = instance.validFrom
    instance.validFrom = original
    assert instance.validFrom == original



@given(instance=xpdl1_ProcessHeaderType_strategy)
def test_xpdl1_processheadertype_limit_setter(instance):
    original = instance.limit
    instance.limit = original
    assert instance.limit == original



@given(instance=xpdl1_ProcessHeaderType_strategy)
def test_xpdl1_processheadertype_durationUnit_setter(instance):
    original = instance.durationUnit
    instance.durationUnit = original
    assert instance.durationUnit == original



@given(instance=xpdl1_ProcessHeaderType_strategy)
def test_xpdl1_processheadertype_validTo_setter(instance):
    original = instance.validTo
    instance.validTo = original
    assert instance.validTo == original



@given(instance=xpdl1_ProcessHeaderType_strategy)
def test_xpdl1_processheadertype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=xpdl1_ProcessHeaderType_strategy)
def test_xpdl1_processheadertype_created_setter(instance):
    original = instance.created
    instance.created = original
    assert instance.created == original



@given(instance=xpdl1_ProcessHeaderType_strategy)
def test_xpdl1_processheadertype_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=xpdl1_NoType_strategy)
@settings(max_examples=50)
def test_xpdl1_notype_instantiation(instance):
    assert isinstance(instance, xpdl1_NoType)

@given(instance=xpdl1_MemberType_strategy)
@settings(max_examples=50)
def test_xpdl1_membertype_instantiation(instance):
    assert isinstance(instance, xpdl1_MemberType)

@given(instance=xpdl1_ManualType_strategy)
@settings(max_examples=50)
def test_xpdl1_manualtype_instantiation(instance):
    assert isinstance(instance, xpdl1_ManualType)

@given(instance=xpdl1_PackageHeaderType_strategy)
@settings(max_examples=50)
def test_xpdl1_packageheadertype_instantiation(instance):
    assert isinstance(instance, xpdl1_PackageHeaderType)



@given(instance=xpdl1_PackageHeaderType_strategy)
def test_xpdl1_packageheadertype_vendor_setter(instance):
    original = instance.vendor
    instance.vendor = original
    assert instance.vendor == original



@given(instance=xpdl1_PackageHeaderType_strategy)
def test_xpdl1_packageheadertype_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original



@given(instance=xpdl1_PackageHeaderType_strategy)
def test_xpdl1_packageheadertype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=xpdl1_PackageHeaderType_strategy)
def test_xpdl1_packageheadertype_xPDLVersion_setter(instance):
    original = instance.xPDLVersion
    instance.xPDLVersion = original
    assert instance.xPDLVersion == original



@given(instance=xpdl1_PackageHeaderType_strategy)
def test_xpdl1_packageheadertype_created_setter(instance):
    original = instance.created
    instance.created = original
    assert instance.created == original



@given(instance=xpdl1_PackageHeaderType_strategy)
def test_xpdl1_packageheadertype_priorityUnit_setter(instance):
    original = instance.priorityUnit
    instance.priorityUnit = original
    assert instance.priorityUnit == original



@given(instance=xpdl1_PackageHeaderType_strategy)
def test_xpdl1_packageheadertype_costUnit_setter(instance):
    original = instance.costUnit
    instance.costUnit = original
    assert instance.costUnit == original

@given(instance=xpdl1_PackageType_strategy)
@settings(max_examples=50)
def test_xpdl1_packagetype_instantiation(instance):
    assert isinstance(instance, xpdl1_PackageType)



@given(instance=xpdl1_PackageType_strategy)
def test_xpdl1_packagetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xpdl1_PackageType_strategy)
def test_xpdl1_packagetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1_FormalParameterType_strategy)
@settings(max_examples=50)
def test_xpdl1_formalparametertype_instantiation(instance):
    assert isinstance(instance, xpdl1_FormalParameterType)



@given(instance=xpdl1_FormalParameterType_strategy)
def test_xpdl1_formalparametertype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=xpdl1_FormalParameterType_strategy)
def test_xpdl1_formalparametertype_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original



@given(instance=xpdl1_FormalParameterType_strategy)
def test_xpdl1_formalparametertype_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=xpdl1_FormalParameterType_strategy)
def test_xpdl1_formalparametertype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1_JoinType_strategy)
@settings(max_examples=50)
def test_xpdl1_jointype_instantiation(instance):
    assert isinstance(instance, xpdl1_JoinType)



@given(instance=xpdl1_JoinType_strategy)
def test_xpdl1_jointype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xpdl1_ExtendedAttributeType_strategy)
@settings(max_examples=50)
def test_xpdl1_extendedattributetype_instantiation(instance):
    assert isinstance(instance, xpdl1_ExtendedAttributeType)



@given(instance=xpdl1_ExtendedAttributeType_strategy)
def test_xpdl1_extendedattributetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=xpdl1_ExtendedAttributeType_strategy)
def test_xpdl1_extendedattributetype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xpdl1_ExtendedAttributeType_strategy)
def test_xpdl1_extendedattributetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=xpdl1_ExtendedAttributeType_strategy)
def test_xpdl1_extendedattributetype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xpdl1_ExtendedAttributeType_strategy)
def test_xpdl1_extendedattributetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl1_EnumerationValueType_strategy)
@settings(max_examples=50)
def test_xpdl1_enumerationvaluetype_instantiation(instance):
    assert isinstance(instance, xpdl1_EnumerationValueType)



@given(instance=xpdl1_EnumerationValueType_strategy)
def test_xpdl1_enumerationvaluetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl1_ExternalPackagesType_strategy)
@settings(max_examples=50)
def test_xpdl1_externalpackagestype_instantiation(instance):
    assert isinstance(instance, xpdl1_ExternalPackagesType)

@given(instance=xpdl1_ExternalPackageType_strategy)
@settings(max_examples=50)
def test_xpdl1_externalpackagetype_instantiation(instance):
    assert isinstance(instance, xpdl1_ExternalPackageType)



@given(instance=xpdl1_ExternalPackageType_strategy)
def test_xpdl1_externalpackagetype_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original

@given(instance=xpdl1_EObject_strategy)
@settings(max_examples=50)
def test_xpdl1_eobject_instantiation(instance):
    assert isinstance(instance, xpdl1_EObject)

@given(instance=xpdl1_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_xpdl1_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, xpdl1_EStringToStringMapEntry)

@given(instance=xpdl1_DocumentRoot_strategy)
@settings(max_examples=50)
def test_xpdl1_documentroot_instantiation(instance):
    assert isinstance(instance, xpdl1_DocumentRoot)



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_vendor_setter(instance):
    original = instance.vendor
    instance.vendor = original
    assert instance.vendor == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_validTo_setter(instance):
    original = instance.validTo
    instance.validTo = original
    assert instance.validTo == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_priorityUnit_setter(instance):
    original = instance.priorityUnit
    instance.priorityUnit = original
    assert instance.priorityUnit == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_limit_setter(instance):
    original = instance.limit
    instance.limit = original
    assert instance.limit == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_codepage_setter(instance):
    original = instance.codepage
    instance.codepage = original
    assert instance.codepage == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_countrykey_setter(instance):
    original = instance.countrykey
    instance.countrykey = original
    assert instance.countrykey == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_responsible_setter(instance):
    original = instance.responsible
    instance.responsible = original
    assert instance.responsible == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_actualParameter_setter(instance):
    original = instance.actualParameter
    instance.actualParameter = original
    assert instance.actualParameter == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_xPDLVersion_setter(instance):
    original = instance.xPDLVersion
    instance.xPDLVersion = original
    assert instance.xPDLVersion == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_initialValue_setter(instance):
    original = instance.initialValue
    instance.initialValue = original
    assert instance.initialValue == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_costUnit_setter(instance):
    original = instance.costUnit
    instance.costUnit = original
    assert instance.costUnit == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_waitingTime_setter(instance):
    original = instance.waitingTime
    instance.waitingTime = original
    assert instance.waitingTime == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_validFrom_setter(instance):
    original = instance.validFrom
    instance.validFrom = original
    assert instance.validFrom == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_workingTime_setter(instance):
    original = instance.workingTime
    instance.workingTime = original
    assert instance.workingTime == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_performer_setter(instance):
    original = instance.performer
    instance.performer = original
    assert instance.performer == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=xpdl1_DocumentRoot_strategy)
def test_xpdl1_documentroot_created_setter(instance):
    original = instance.created
    instance.created = original
    assert instance.created == original

@given(instance=xpdl1_DataTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1_datatypetype_instantiation(instance):
    assert isinstance(instance, xpdl1_DataTypeType)

@given(instance=xpdl1_DataFieldType_strategy)
@settings(max_examples=50)
def test_xpdl1_datafieldtype_instantiation(instance):
    assert isinstance(instance, xpdl1_DataFieldType)



@given(instance=xpdl1_DataFieldType_strategy)
def test_xpdl1_datafieldtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xpdl1_DataFieldType_strategy)
def test_xpdl1_datafieldtype_isArray_setter(instance):
    original = instance.isArray
    instance.isArray = original
    assert instance.isArray == original



@given(instance=xpdl1_DataFieldType_strategy)
def test_xpdl1_datafieldtype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=xpdl1_DataFieldType_strategy)
def test_xpdl1_datafieldtype_initialValue_setter(instance):
    original = instance.initialValue
    instance.initialValue = original
    assert instance.initialValue == original



@given(instance=xpdl1_DataFieldType_strategy)
def test_xpdl1_datafieldtype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=xpdl1_DataFieldType_strategy)
def test_xpdl1_datafieldtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl1_DataFieldsType_strategy)
@settings(max_examples=50)
def test_xpdl1_datafieldstype_instantiation(instance):
    assert isinstance(instance, xpdl1_DataFieldsType)

@given(instance=xpdl1_ConformanceClassType_strategy)
@settings(max_examples=50)
def test_xpdl1_conformanceclasstype_instantiation(instance):
    assert isinstance(instance, xpdl1_ConformanceClassType)



@given(instance=xpdl1_ConformanceClassType_strategy)
def test_xpdl1_conformanceclasstype_graphConformance_setter(instance):
    original = instance.graphConformance
    instance.graphConformance = original
    assert instance.graphConformance == original

@given(instance=xpdl1_XpressionType_strategy)
@settings(max_examples=50)
def test_xpdl1_xpressiontype_instantiation(instance):
    assert isinstance(instance, xpdl1_XpressionType)



@given(instance=xpdl1_XpressionType_strategy)
def test_xpdl1_xpressiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=xpdl1_XpressionType_strategy)
def test_xpdl1_xpressiontype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xpdl1_XpressionType_strategy)
def test_xpdl1_xpressiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xpdl1_AutomaticType_strategy)
@settings(max_examples=50)
def test_xpdl1_automatictype_instantiation(instance):
    assert isinstance(instance, xpdl1_AutomaticType)

@given(instance=xpdl1_ListTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1_listtypetype_instantiation(instance):
    assert isinstance(instance, xpdl1_ListTypeType)

@given(instance=xpdl1_EnumerationTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1_enumerationtypetype_instantiation(instance):
    assert isinstance(instance, xpdl1_EnumerationTypeType)

@given(instance=xpdl1_ConditionType_strategy)
@settings(max_examples=50)
def test_xpdl1_conditiontype_instantiation(instance):
    assert isinstance(instance, xpdl1_ConditionType)



@given(instance=xpdl1_ConditionType_strategy)
def test_xpdl1_conditiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xpdl1_ConditionType_strategy)
def test_xpdl1_conditiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=xpdl1_ConditionType_strategy)
def test_xpdl1_conditiontype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xpdl1_SchemaTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1_schematypetype_instantiation(instance):
    assert isinstance(instance, xpdl1_SchemaTypeType)



@given(instance=xpdl1_SchemaTypeType_strategy)
def test_xpdl1_schematypetype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xpdl1_DeclaredTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1_declaredtypetype_instantiation(instance):
    assert isinstance(instance, xpdl1_DeclaredTypeType)



@given(instance=xpdl1_DeclaredTypeType_strategy)
def test_xpdl1_declaredtypetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1_BasicTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1_basictypetype_instantiation(instance):
    assert isinstance(instance, xpdl1_BasicTypeType)



@given(instance=xpdl1_BasicTypeType_strategy)
def test_xpdl1_basictypetype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xpdl1_ArrayTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1_arraytypetype_instantiation(instance):
    assert isinstance(instance, xpdl1_ArrayTypeType)



@given(instance=xpdl1_ArrayTypeType_strategy)
def test_xpdl1_arraytypetype_upperIndex_setter(instance):
    original = instance.upperIndex
    instance.upperIndex = original
    assert instance.upperIndex == original



@given(instance=xpdl1_ArrayTypeType_strategy)
def test_xpdl1_arraytypetype_lowerIndex_setter(instance):
    original = instance.lowerIndex
    instance.lowerIndex = original
    assert instance.lowerIndex == original

@given(instance=xpdl1_UnionTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1_uniontypetype_instantiation(instance):
    assert isinstance(instance, xpdl1_UnionTypeType)

@given(instance=xpdl1_RecordTypeType_strategy)
@settings(max_examples=50)
def test_xpdl1_recordtypetype_instantiation(instance):
    assert isinstance(instance, xpdl1_RecordTypeType)

@given(instance=xpdl1_ApplicationType_strategy)
@settings(max_examples=50)
def test_xpdl1_applicationtype_instantiation(instance):
    assert isinstance(instance, xpdl1_ApplicationType)



@given(instance=xpdl1_ApplicationType_strategy)
def test_xpdl1_applicationtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xpdl1_ApplicationType_strategy)
def test_xpdl1_applicationtype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=xpdl1_ApplicationType_strategy)
def test_xpdl1_applicationtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl1_ApplicationsType_strategy)
@settings(max_examples=50)
def test_xpdl1_applicationstype_instantiation(instance):
    assert isinstance(instance, xpdl1_ApplicationsType)

@given(instance=xpdl1_ActualParametersType_strategy)
@settings(max_examples=50)
def test_xpdl1_actualparameterstype_instantiation(instance):
    assert isinstance(instance, xpdl1_ActualParametersType)



@given(instance=xpdl1_ActualParametersType_strategy)
def test_xpdl1_actualparameterstype_actualParameter_setter(instance):
    original = instance.actualParameter
    instance.actualParameter = original
    assert instance.actualParameter == original

@given(instance=xpdl1_ExtendedAttributesType_strategy)
@settings(max_examples=50)
def test_xpdl1_extendedattributestype_instantiation(instance):
    assert isinstance(instance, xpdl1_ExtendedAttributesType)

@given(instance=xpdl1_ExternalReferenceType_strategy)
@settings(max_examples=50)
def test_xpdl1_externalreferencetype_instantiation(instance):
    assert isinstance(instance, xpdl1_ExternalReferenceType)



@given(instance=xpdl1_ExternalReferenceType_strategy)
def test_xpdl1_externalreferencetype_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original



@given(instance=xpdl1_ExternalReferenceType_strategy)
def test_xpdl1_externalreferencetype_xref_setter(instance):
    original = instance.xref
    instance.xref = original
    assert instance.xref == original



@given(instance=xpdl1_ExternalReferenceType_strategy)
def test_xpdl1_externalreferencetype_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=xpdl1_FormalParametersType_strategy)
@settings(max_examples=50)
def test_xpdl1_formalparameterstype_instantiation(instance):
    assert isinstance(instance, xpdl1_FormalParametersType)

@given(instance=xpdl1_SimulationInformationType_strategy)
@settings(max_examples=50)
def test_xpdl1_simulationinformationtype_instantiation(instance):
    assert isinstance(instance, xpdl1_SimulationInformationType)



@given(instance=xpdl1_SimulationInformationType_strategy)
def test_xpdl1_simulationinformationtype_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original



@given(instance=xpdl1_SimulationInformationType_strategy)
def test_xpdl1_simulationinformationtype_instantiation_setter(instance):
    original = instance.instantiation
    instance.instantiation = original
    assert instance.instantiation == original

@given(instance=xpdl1_DeadlineType_strategy)
@settings(max_examples=50)
def test_xpdl1_deadlinetype_instantiation(instance):
    assert isinstance(instance, xpdl1_DeadlineType)



@given(instance=xpdl1_DeadlineType_strategy)
def test_xpdl1_deadlinetype_execution_setter(instance):
    original = instance.execution
    instance.execution = original
    assert instance.execution == original

@given(instance=xpdl1_FinishModeType_strategy)
@settings(max_examples=50)
def test_xpdl1_finishmodetype_instantiation(instance):
    assert isinstance(instance, xpdl1_FinishModeType)

@given(instance=xpdl1_StartModeType_strategy)
@settings(max_examples=50)
def test_xpdl1_startmodetype_instantiation(instance):
    assert isinstance(instance, xpdl1_StartModeType)

@given(instance=xpdl1_BlockActivityType_strategy)
@settings(max_examples=50)
def test_xpdl1_blockactivitytype_instantiation(instance):
    assert isinstance(instance, xpdl1_BlockActivityType)



@given(instance=xpdl1_BlockActivityType_strategy)
def test_xpdl1_blockactivitytype_blockId_setter(instance):
    original = instance.blockId
    instance.blockId = original
    assert instance.blockId == original

@given(instance=xpdl1_TransitionRestrictionsType_strategy)
@settings(max_examples=50)
def test_xpdl1_transitionrestrictionstype_instantiation(instance):
    assert isinstance(instance, xpdl1_TransitionRestrictionsType)

@given(instance=xpdl1_TransitionsType_strategy)
@settings(max_examples=50)
def test_xpdl1_transitionstype_instantiation(instance):
    assert isinstance(instance, xpdl1_TransitionsType)

@given(instance=xpdl1_ImplementationType_strategy)
@settings(max_examples=50)
def test_xpdl1_implementationtype_instantiation(instance):
    assert isinstance(instance, xpdl1_ImplementationType)

@given(instance=xpdl1_RouteType_strategy)
@settings(max_examples=50)
def test_xpdl1_routetype_instantiation(instance):
    assert isinstance(instance, xpdl1_RouteType)

@given(instance=xpdl1_ActivitiesType_strategy)
@settings(max_examples=50)
def test_xpdl1_activitiestype_instantiation(instance):
    assert isinstance(instance, xpdl1_ActivitiesType)

@given(instance=xpdl1_ActivitySetType_strategy)
@settings(max_examples=50)
def test_xpdl1_activitysettype_instantiation(instance):
    assert isinstance(instance, xpdl1_ActivitySetType)



@given(instance=xpdl1_ActivitySetType_strategy)
def test_xpdl1_activitysettype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl1_ActivitySetsType_strategy)
@settings(max_examples=50)
def test_xpdl1_activitysetstype_instantiation(instance):
    assert isinstance(instance, xpdl1_ActivitySetsType)

@given(instance=xpdl1_ActivityType_strategy)
@settings(max_examples=50)
def test_xpdl1_activitytype_instantiation(instance):
    assert isinstance(instance, xpdl1_ActivityType)



@given(instance=xpdl1_ActivityType_strategy)
def test_xpdl1_activitytype_performer_setter(instance):
    original = instance.performer
    instance.performer = original
    assert instance.performer == original



@given(instance=xpdl1_ActivityType_strategy)
def test_xpdl1_activitytype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=xpdl1_ActivityType_strategy)
def test_xpdl1_activitytype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xpdl1_ActivityType_strategy)
def test_xpdl1_activitytype_limit_setter(instance):
    original = instance.limit
    instance.limit = original
    assert instance.limit == original



@given(instance=xpdl1_ActivityType_strategy)
def test_xpdl1_activitytype_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original



@given(instance=xpdl1_ActivityType_strategy)
def test_xpdl1_activitytype_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=xpdl1_ActivityType_strategy)
def test_xpdl1_activitytype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xpdl1_ActivityType_strategy)
def test_xpdl1_activitytype_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original

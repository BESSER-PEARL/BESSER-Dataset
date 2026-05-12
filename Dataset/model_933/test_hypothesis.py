import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ProcessPackage,
    uma_ProcessComponent,
    NamedElement,
    uma_PackageableElement,
    uma_WorkOrder,
    Concept,
    uma_Whitepaper,
    Descriptor,
    uma_WorkProductDescriptor,
    uma_RoleDescriptor,
    Element,
    uma_NamedElement,
    ActivityDescription,
    uma_ProcessDescription,
    Activity,
    uma_Phase,
    uma_Process,
    uma_Iteration,
    uma_Element,
    uma_EStringToStringMapEntry,
    uma_DocumentRoot,
    BreakdownElement,
    uma_ProcessComponentInterface,
    uma_WorkBreakdownElement,
    uma_TeamProfile,
    uma_Descriptor,
    ProcessDescription,
    uma_DeliveryProcessDescription,
    ContentCategory,
    uma_Tool,
    uma_WorkProductType,
    uma_DisciplineGrouping,
    uma_Discipline,
    uma_RoleSetGrouping,
    uma_Domain,
    uma_RoleSet,
    uma_CustomCategory,
    WorkBreakdownElement,
    uma_Milestone,
    uma_TaskDescriptor,
    uma_Activity,
    DescribableElement,
    uma_ProcessElement,
    uma_ContentElement,
    MethodUnit,
    uma_MethodPlugin,
    uma_MethodLibrary,
    uma_MethodConfiguration,
    uma_ContentDescription,
    MethodPackage,
    uma_ProcessPackage,
    uma_ContentPackage,
    uma_ContentCategoryPackage,
    ContentElement,
    uma_Kind,
    uma_Guidance,
    uma_Task,
    uma_WorkProduct,
    uma_ContentCategory,
    MethodElement,
    uma_MethodPackage,
    uma_MethodUnit,
    uma_DescribableElement,
    uma_Section,
    uma_WorkDefinition,
    uma_Constraint,
    uma_Role,
    RoleDescriptor,
    uma_CompositeRole,
    Guidance,
    uma_EstimatingMetric,
    uma_ToolMentor,
    uma_Concept,
    uma_Report,
    uma_Estimate,
    uma_Practice,
    uma_ReusableAsset,
    uma_Example,
    uma_Template,
    uma_Guideline,
    uma_EstimationConsiderations,
    uma_SupportingMaterial,
    uma_Roadmap,
    uma_TermDefinition,
    uma_Checklist,
    Process,
    uma_ProcessPlanningTemplate,
    uma_DeliveryProcess,
    uma_CapabilityPattern,
    ContentDescription,
    uma_RoleDescription,
    uma_TaskDescription,
    uma_WorkProductDescription,
    uma_PracticeDescription,
    uma_GuidanceDescription,
    uma_BreakdownElementDescription,
    ProcessElement,
    uma_PlanningData,
    uma_BreakdownElement,
    WorkProductDescription,
    uma_DeliverableDescription,
    uma_ArtifactDescription,
    WorkProduct,
    uma_Outcome,
    uma_Deliverable,
    uma_Artifact,
    PackageableElement,
    uma_MethodElement,
    uma_MethodElementProperty,
    uma_ApplicableMetaClassInfo,
    BreakdownElementDescription,
    uma_DescriptorDescription,
    uma_ActivityDescription,
    WorkOrderType,
    VariabilityType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_processpackage_is_not_abstract():
    assert not inspect.isabstract(ProcessPackage)


def test_processpackage_constructor_exists():
    assert callable(ProcessPackage.__init__)


def test_processpackage_constructor_args():
    sig = inspect.signature(ProcessPackage.__init__)
    params = list(sig.parameters.keys())



def test_uma_processcomponent_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessComponent)


def test_uma_processcomponent_constructor_exists():
    assert callable(uma_ProcessComponent.__init__)


def test_uma_processcomponent_constructor_args():
    sig = inspect.signature(uma_ProcessComponent.__init__)
    params = list(sig.parameters.keys())
    assert "copyright" in params, "Missing parameter 'copyright'"
    assert "changeDate" in params, "Missing parameter 'changeDate'"
    assert "changeDescription" in params, "Missing parameter 'changeDescription'"
    assert "authors" in params, "Missing parameter 'authors'"
    assert "version" in params, "Missing parameter 'version'"

def test_uma_processcomponent_has_copyright():
    assert hasattr(uma_ProcessComponent, "copyright")
    descriptor = None
    for klass in uma_ProcessComponent.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)

def test_uma_processcomponent_has_changeDate():
    assert hasattr(uma_ProcessComponent, "changeDate")
    descriptor = None
    for klass in uma_ProcessComponent.__mro__:
        if "changeDate" in klass.__dict__:
            descriptor = klass.__dict__["changeDate"]
            break
    assert isinstance(descriptor, property)

def test_uma_processcomponent_has_changeDescription():
    assert hasattr(uma_ProcessComponent, "changeDescription")
    descriptor = None
    for klass in uma_ProcessComponent.__mro__:
        if "changeDescription" in klass.__dict__:
            descriptor = klass.__dict__["changeDescription"]
            break
    assert isinstance(descriptor, property)

def test_uma_processcomponent_has_authors():
    assert hasattr(uma_ProcessComponent, "authors")
    descriptor = None
    for klass in uma_ProcessComponent.__mro__:
        if "authors" in klass.__dict__:
            descriptor = klass.__dict__["authors"]
            break
    assert isinstance(descriptor, property)

def test_uma_processcomponent_has_version():
    assert hasattr(uma_ProcessComponent, "version")
    descriptor = None
    for klass in uma_ProcessComponent.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_packageableelement_is_not_abstract():
    assert not inspect.isabstract(uma_PackageableElement)


def test_uma_packageableelement_constructor_exists():
    assert callable(uma_PackageableElement.__init__)


def test_uma_packageableelement_constructor_args():
    sig = inspect.signature(uma_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_workorder_is_not_abstract():
    assert not inspect.isabstract(uma_WorkOrder)


def test_uma_workorder_constructor_exists():
    assert callable(uma_WorkOrder.__init__)


def test_uma_workorder_constructor_args():
    sig = inspect.signature(uma_WorkOrder.__init__)
    params = list(sig.parameters.keys())
    assert "linkType" in params, "Missing parameter 'linkType'"
    assert "properties" in params, "Missing parameter 'properties'"
    assert "value" in params, "Missing parameter 'value'"
    assert "id" in params, "Missing parameter 'id'"

def test_uma_workorder_has_linkType():
    assert hasattr(uma_WorkOrder, "linkType")
    descriptor = None
    for klass in uma_WorkOrder.__mro__:
        if "linkType" in klass.__dict__:
            descriptor = klass.__dict__["linkType"]
            break
    assert isinstance(descriptor, property)

def test_uma_workorder_has_properties():
    assert hasattr(uma_WorkOrder, "properties")
    descriptor = None
    for klass in uma_WorkOrder.__mro__:
        if "properties" in klass.__dict__:
            descriptor = klass.__dict__["properties"]
            break
    assert isinstance(descriptor, property)

def test_uma_workorder_has_value():
    assert hasattr(uma_WorkOrder, "value")
    descriptor = None
    for klass in uma_WorkOrder.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_uma_workorder_has_id():
    assert hasattr(uma_WorkOrder, "id")
    descriptor = None
    for klass in uma_WorkOrder.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_concept_is_not_abstract():
    assert not inspect.isabstract(Concept)


def test_concept_constructor_exists():
    assert callable(Concept.__init__)


def test_concept_constructor_args():
    sig = inspect.signature(Concept.__init__)
    params = list(sig.parameters.keys())



def test_uma_whitepaper_is_not_abstract():
    assert not inspect.isabstract(uma_Whitepaper)


def test_uma_whitepaper_constructor_exists():
    assert callable(uma_Whitepaper.__init__)


def test_uma_whitepaper_constructor_args():
    sig = inspect.signature(uma_Whitepaper.__init__)
    params = list(sig.parameters.keys())



def test_descriptor_is_not_abstract():
    assert not inspect.isabstract(Descriptor)


def test_descriptor_constructor_exists():
    assert callable(Descriptor.__init__)


def test_descriptor_constructor_args():
    sig = inspect.signature(Descriptor.__init__)
    params = list(sig.parameters.keys())



def test_uma_workproductdescriptor_is_not_abstract():
    assert not inspect.isabstract(uma_WorkProductDescriptor)


def test_uma_workproductdescriptor_constructor_exists():
    assert callable(uma_WorkProductDescriptor.__init__)


def test_uma_workproductdescriptor_constructor_args():
    sig = inspect.signature(uma_WorkProductDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "externalInputTo" in params, "Missing parameter 'externalInputTo'"
    assert "outputFrom" in params, "Missing parameter 'outputFrom'"
    assert "deliverableParts" in params, "Missing parameter 'deliverableParts'"
    assert "activityEntryState" in params, "Missing parameter 'activityEntryState'"
    assert "optionalInputTo" in params, "Missing parameter 'optionalInputTo'"
    assert "activityExitState" in params, "Missing parameter 'activityExitState'"
    assert "impactedBy" in params, "Missing parameter 'impactedBy'"
    assert "workProduct" in params, "Missing parameter 'workProduct'"
    assert "group2" in params, "Missing parameter 'group2'"
    assert "responsibleRole" in params, "Missing parameter 'responsibleRole'"
    assert "mandatoryInputTo" in params, "Missing parameter 'mandatoryInputTo'"
    assert "impacts" in params, "Missing parameter 'impacts'"

def test_uma_workproductdescriptor_has_externalInputTo():
    assert hasattr(uma_WorkProductDescriptor, "externalInputTo")
    descriptor = None
    for klass in uma_WorkProductDescriptor.__mro__:
        if "externalInputTo" in klass.__dict__:
            descriptor = klass.__dict__["externalInputTo"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproductdescriptor_has_outputFrom():
    assert hasattr(uma_WorkProductDescriptor, "outputFrom")
    descriptor = None
    for klass in uma_WorkProductDescriptor.__mro__:
        if "outputFrom" in klass.__dict__:
            descriptor = klass.__dict__["outputFrom"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproductdescriptor_has_deliverableParts():
    assert hasattr(uma_WorkProductDescriptor, "deliverableParts")
    descriptor = None
    for klass in uma_WorkProductDescriptor.__mro__:
        if "deliverableParts" in klass.__dict__:
            descriptor = klass.__dict__["deliverableParts"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproductdescriptor_has_activityEntryState():
    assert hasattr(uma_WorkProductDescriptor, "activityEntryState")
    descriptor = None
    for klass in uma_WorkProductDescriptor.__mro__:
        if "activityEntryState" in klass.__dict__:
            descriptor = klass.__dict__["activityEntryState"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproductdescriptor_has_optionalInputTo():
    assert hasattr(uma_WorkProductDescriptor, "optionalInputTo")
    descriptor = None
    for klass in uma_WorkProductDescriptor.__mro__:
        if "optionalInputTo" in klass.__dict__:
            descriptor = klass.__dict__["optionalInputTo"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproductdescriptor_has_activityExitState():
    assert hasattr(uma_WorkProductDescriptor, "activityExitState")
    descriptor = None
    for klass in uma_WorkProductDescriptor.__mro__:
        if "activityExitState" in klass.__dict__:
            descriptor = klass.__dict__["activityExitState"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproductdescriptor_has_impactedBy():
    assert hasattr(uma_WorkProductDescriptor, "impactedBy")
    descriptor = None
    for klass in uma_WorkProductDescriptor.__mro__:
        if "impactedBy" in klass.__dict__:
            descriptor = klass.__dict__["impactedBy"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproductdescriptor_has_workProduct():
    assert hasattr(uma_WorkProductDescriptor, "workProduct")
    descriptor = None
    for klass in uma_WorkProductDescriptor.__mro__:
        if "workProduct" in klass.__dict__:
            descriptor = klass.__dict__["workProduct"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproductdescriptor_has_group2():
    assert hasattr(uma_WorkProductDescriptor, "group2")
    descriptor = None
    for klass in uma_WorkProductDescriptor.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproductdescriptor_has_responsibleRole():
    assert hasattr(uma_WorkProductDescriptor, "responsibleRole")
    descriptor = None
    for klass in uma_WorkProductDescriptor.__mro__:
        if "responsibleRole" in klass.__dict__:
            descriptor = klass.__dict__["responsibleRole"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproductdescriptor_has_mandatoryInputTo():
    assert hasattr(uma_WorkProductDescriptor, "mandatoryInputTo")
    descriptor = None
    for klass in uma_WorkProductDescriptor.__mro__:
        if "mandatoryInputTo" in klass.__dict__:
            descriptor = klass.__dict__["mandatoryInputTo"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproductdescriptor_has_impacts():
    assert hasattr(uma_WorkProductDescriptor, "impacts")
    descriptor = None
    for klass in uma_WorkProductDescriptor.__mro__:
        if "impacts" in klass.__dict__:
            descriptor = klass.__dict__["impacts"]
            break
    assert isinstance(descriptor, property)



def test_uma_roledescriptor_is_not_abstract():
    assert not inspect.isabstract(uma_RoleDescriptor)


def test_uma_roledescriptor_constructor_exists():
    assert callable(uma_RoleDescriptor.__init__)


def test_uma_roledescriptor_constructor_args():
    sig = inspect.signature(uma_RoleDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "role" in params, "Missing parameter 'role'"
    assert "responsibleFor" in params, "Missing parameter 'responsibleFor'"

def test_uma_roledescriptor_has_role():
    assert hasattr(uma_RoleDescriptor, "role")
    descriptor = None
    for klass in uma_RoleDescriptor.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_uma_roledescriptor_has_responsibleFor():
    assert hasattr(uma_RoleDescriptor, "responsibleFor")
    descriptor = None
    for klass in uma_RoleDescriptor.__mro__:
        if "responsibleFor" in klass.__dict__:
            descriptor = klass.__dict__["responsibleFor"]
            break
    assert isinstance(descriptor, property)



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_uma_namedelement_is_not_abstract():
    assert not inspect.isabstract(uma_NamedElement)


def test_uma_namedelement_constructor_exists():
    assert callable(uma_NamedElement.__init__)


def test_uma_namedelement_constructor_args():
    sig = inspect.signature(uma_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uma_namedelement_has_name():
    assert hasattr(uma_NamedElement, "name")
    descriptor = None
    for klass in uma_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_activitydescription_is_not_abstract():
    assert not inspect.isabstract(ActivityDescription)


def test_activitydescription_constructor_exists():
    assert callable(ActivityDescription.__init__)


def test_activitydescription_constructor_args():
    sig = inspect.signature(ActivityDescription.__init__)
    params = list(sig.parameters.keys())



def test_uma_processdescription_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessDescription)


def test_uma_processdescription_constructor_exists():
    assert callable(uma_ProcessDescription.__init__)


def test_uma_processdescription_constructor_args():
    sig = inspect.signature(uma_ProcessDescription.__init__)
    params = list(sig.parameters.keys())
    assert "usageNotes" in params, "Missing parameter 'usageNotes'"
    assert "scope" in params, "Missing parameter 'scope'"

def test_uma_processdescription_has_usageNotes():
    assert hasattr(uma_ProcessDescription, "usageNotes")
    descriptor = None
    for klass in uma_ProcessDescription.__mro__:
        if "usageNotes" in klass.__dict__:
            descriptor = klass.__dict__["usageNotes"]
            break
    assert isinstance(descriptor, property)

def test_uma_processdescription_has_scope():
    assert hasattr(uma_ProcessDescription, "scope")
    descriptor = None
    for klass in uma_ProcessDescription.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_activity_is_not_abstract():
    assert not inspect.isabstract(Activity)


def test_activity_constructor_exists():
    assert callable(Activity.__init__)


def test_activity_constructor_args():
    sig = inspect.signature(Activity.__init__)
    params = list(sig.parameters.keys())



def test_uma_phase_is_not_abstract():
    assert not inspect.isabstract(uma_Phase)


def test_uma_phase_constructor_exists():
    assert callable(uma_Phase.__init__)


def test_uma_phase_constructor_args():
    sig = inspect.signature(uma_Phase.__init__)
    params = list(sig.parameters.keys())



def test_uma_process_is_not_abstract():
    assert not inspect.isabstract(uma_Process)


def test_uma_process_constructor_exists():
    assert callable(uma_Process.__init__)


def test_uma_process_constructor_args():
    sig = inspect.signature(uma_Process.__init__)
    params = list(sig.parameters.keys())
    assert "includesPattern" in params, "Missing parameter 'includesPattern'"
    assert "diagramURI" in params, "Missing parameter 'diagramURI'"
    assert "defaultContext" in params, "Missing parameter 'defaultContext'"
    assert "validContext" in params, "Missing parameter 'validContext'"

def test_uma_process_has_includesPattern():
    assert hasattr(uma_Process, "includesPattern")
    descriptor = None
    for klass in uma_Process.__mro__:
        if "includesPattern" in klass.__dict__:
            descriptor = klass.__dict__["includesPattern"]
            break
    assert isinstance(descriptor, property)

def test_uma_process_has_diagramURI():
    assert hasattr(uma_Process, "diagramURI")
    descriptor = None
    for klass in uma_Process.__mro__:
        if "diagramURI" in klass.__dict__:
            descriptor = klass.__dict__["diagramURI"]
            break
    assert isinstance(descriptor, property)

def test_uma_process_has_defaultContext():
    assert hasattr(uma_Process, "defaultContext")
    descriptor = None
    for klass in uma_Process.__mro__:
        if "defaultContext" in klass.__dict__:
            descriptor = klass.__dict__["defaultContext"]
            break
    assert isinstance(descriptor, property)

def test_uma_process_has_validContext():
    assert hasattr(uma_Process, "validContext")
    descriptor = None
    for klass in uma_Process.__mro__:
        if "validContext" in klass.__dict__:
            descriptor = klass.__dict__["validContext"]
            break
    assert isinstance(descriptor, property)



def test_uma_iteration_is_not_abstract():
    assert not inspect.isabstract(uma_Iteration)


def test_uma_iteration_constructor_exists():
    assert callable(uma_Iteration.__init__)


def test_uma_iteration_constructor_args():
    sig = inspect.signature(uma_Iteration.__init__)
    params = list(sig.parameters.keys())



def test_uma_element_is_not_abstract():
    assert not inspect.isabstract(uma_Element)


def test_uma_element_constructor_exists():
    assert callable(uma_Element.__init__)


def test_uma_element_constructor_args():
    sig = inspect.signature(uma_Element.__init__)
    params = list(sig.parameters.keys())



def test_uma_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(uma_EStringToStringMapEntry)


def test_uma_estringtostringmapentry_constructor_exists():
    assert callable(uma_EStringToStringMapEntry.__init__)


def test_uma_estringtostringmapentry_constructor_args():
    sig = inspect.signature(uma_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_uma_documentroot_is_not_abstract():
    assert not inspect.isabstract(uma_DocumentRoot)


def test_uma_documentroot_constructor_exists():
    assert callable(uma_DocumentRoot.__init__)


def test_uma_documentroot_constructor_args():
    sig = inspect.signature(uma_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uma_documentroot_has_mixed():
    assert hasattr(uma_DocumentRoot, "mixed")
    descriptor = None
    for klass in uma_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_breakdownelement_is_not_abstract():
    assert not inspect.isabstract(BreakdownElement)


def test_breakdownelement_constructor_exists():
    assert callable(BreakdownElement.__init__)


def test_breakdownelement_constructor_args():
    sig = inspect.signature(BreakdownElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_processcomponentinterface_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessComponentInterface)


def test_uma_processcomponentinterface_constructor_exists():
    assert callable(uma_ProcessComponentInterface.__init__)


def test_uma_processcomponentinterface_constructor_args():
    sig = inspect.signature(uma_ProcessComponentInterface.__init__)
    params = list(sig.parameters.keys())
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma_processcomponentinterface_has_group2():
    assert hasattr(uma_ProcessComponentInterface, "group2")
    descriptor = None
    for klass in uma_ProcessComponentInterface.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma_workbreakdownelement_is_not_abstract():
    assert not inspect.isabstract(uma_WorkBreakdownElement)


def test_uma_workbreakdownelement_constructor_exists():
    assert callable(uma_WorkBreakdownElement.__init__)


def test_uma_workbreakdownelement_constructor_args():
    sig = inspect.signature(uma_WorkBreakdownElement.__init__)
    params = list(sig.parameters.keys())
    assert "isRepeatable" in params, "Missing parameter 'isRepeatable'"
    assert "group2" in params, "Missing parameter 'group2'"
    assert "isEventDriven" in params, "Missing parameter 'isEventDriven'"
    assert "isOngoing" in params, "Missing parameter 'isOngoing'"

def test_uma_workbreakdownelement_has_isRepeatable():
    assert hasattr(uma_WorkBreakdownElement, "isRepeatable")
    descriptor = None
    for klass in uma_WorkBreakdownElement.__mro__:
        if "isRepeatable" in klass.__dict__:
            descriptor = klass.__dict__["isRepeatable"]
            break
    assert isinstance(descriptor, property)

def test_uma_workbreakdownelement_has_group2():
    assert hasattr(uma_WorkBreakdownElement, "group2")
    descriptor = None
    for klass in uma_WorkBreakdownElement.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)

def test_uma_workbreakdownelement_has_isEventDriven():
    assert hasattr(uma_WorkBreakdownElement, "isEventDriven")
    descriptor = None
    for klass in uma_WorkBreakdownElement.__mro__:
        if "isEventDriven" in klass.__dict__:
            descriptor = klass.__dict__["isEventDriven"]
            break
    assert isinstance(descriptor, property)

def test_uma_workbreakdownelement_has_isOngoing():
    assert hasattr(uma_WorkBreakdownElement, "isOngoing")
    descriptor = None
    for klass in uma_WorkBreakdownElement.__mro__:
        if "isOngoing" in klass.__dict__:
            descriptor = klass.__dict__["isOngoing"]
            break
    assert isinstance(descriptor, property)



def test_uma_teamprofile_is_not_abstract():
    assert not inspect.isabstract(uma_TeamProfile)


def test_uma_teamprofile_constructor_exists():
    assert callable(uma_TeamProfile.__init__)


def test_uma_teamprofile_constructor_args():
    sig = inspect.signature(uma_TeamProfile.__init__)
    params = list(sig.parameters.keys())
    assert "group2" in params, "Missing parameter 'group2'"
    assert "superTeam" in params, "Missing parameter 'superTeam'"
    assert "subTeam" in params, "Missing parameter 'subTeam'"
    assert "role" in params, "Missing parameter 'role'"

def test_uma_teamprofile_has_group2():
    assert hasattr(uma_TeamProfile, "group2")
    descriptor = None
    for klass in uma_TeamProfile.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)

def test_uma_teamprofile_has_superTeam():
    assert hasattr(uma_TeamProfile, "superTeam")
    descriptor = None
    for klass in uma_TeamProfile.__mro__:
        if "superTeam" in klass.__dict__:
            descriptor = klass.__dict__["superTeam"]
            break
    assert isinstance(descriptor, property)

def test_uma_teamprofile_has_subTeam():
    assert hasattr(uma_TeamProfile, "subTeam")
    descriptor = None
    for klass in uma_TeamProfile.__mro__:
        if "subTeam" in klass.__dict__:
            descriptor = klass.__dict__["subTeam"]
            break
    assert isinstance(descriptor, property)

def test_uma_teamprofile_has_role():
    assert hasattr(uma_TeamProfile, "role")
    descriptor = None
    for klass in uma_TeamProfile.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)



def test_uma_descriptor_is_not_abstract():
    assert not inspect.isabstract(uma_Descriptor)


def test_uma_descriptor_constructor_exists():
    assert callable(uma_Descriptor.__init__)


def test_uma_descriptor_constructor_args():
    sig = inspect.signature(uma_Descriptor.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronizedWithSource" in params, "Missing parameter 'isSynchronizedWithSource'"

def test_uma_descriptor_has_isSynchronizedWithSource():
    assert hasattr(uma_Descriptor, "isSynchronizedWithSource")
    descriptor = None
    for klass in uma_Descriptor.__mro__:
        if "isSynchronizedWithSource" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronizedWithSource"]
            break
    assert isinstance(descriptor, property)



def test_processdescription_is_not_abstract():
    assert not inspect.isabstract(ProcessDescription)


def test_processdescription_constructor_exists():
    assert callable(ProcessDescription.__init__)


def test_processdescription_constructor_args():
    sig = inspect.signature(ProcessDescription.__init__)
    params = list(sig.parameters.keys())



def test_uma_deliveryprocessdescription_is_not_abstract():
    assert not inspect.isabstract(uma_DeliveryProcessDescription)


def test_uma_deliveryprocessdescription_constructor_exists():
    assert callable(uma_DeliveryProcessDescription.__init__)


def test_uma_deliveryprocessdescription_constructor_args():
    sig = inspect.signature(uma_DeliveryProcessDescription.__init__)
    params = list(sig.parameters.keys())
    assert "projectMemberExpertise" in params, "Missing parameter 'projectMemberExpertise'"
    assert "estimatingTechnique" in params, "Missing parameter 'estimatingTechnique'"
    assert "projectCharacteristics" in params, "Missing parameter 'projectCharacteristics'"
    assert "riskLevel" in params, "Missing parameter 'riskLevel'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "typeOfContract" in params, "Missing parameter 'typeOfContract'"

def test_uma_deliveryprocessdescription_has_projectMemberExpertise():
    assert hasattr(uma_DeliveryProcessDescription, "projectMemberExpertise")
    descriptor = None
    for klass in uma_DeliveryProcessDescription.__mro__:
        if "projectMemberExpertise" in klass.__dict__:
            descriptor = klass.__dict__["projectMemberExpertise"]
            break
    assert isinstance(descriptor, property)

def test_uma_deliveryprocessdescription_has_estimatingTechnique():
    assert hasattr(uma_DeliveryProcessDescription, "estimatingTechnique")
    descriptor = None
    for klass in uma_DeliveryProcessDescription.__mro__:
        if "estimatingTechnique" in klass.__dict__:
            descriptor = klass.__dict__["estimatingTechnique"]
            break
    assert isinstance(descriptor, property)

def test_uma_deliveryprocessdescription_has_projectCharacteristics():
    assert hasattr(uma_DeliveryProcessDescription, "projectCharacteristics")
    descriptor = None
    for klass in uma_DeliveryProcessDescription.__mro__:
        if "projectCharacteristics" in klass.__dict__:
            descriptor = klass.__dict__["projectCharacteristics"]
            break
    assert isinstance(descriptor, property)

def test_uma_deliveryprocessdescription_has_riskLevel():
    assert hasattr(uma_DeliveryProcessDescription, "riskLevel")
    descriptor = None
    for klass in uma_DeliveryProcessDescription.__mro__:
        if "riskLevel" in klass.__dict__:
            descriptor = klass.__dict__["riskLevel"]
            break
    assert isinstance(descriptor, property)

def test_uma_deliveryprocessdescription_has_scale():
    assert hasattr(uma_DeliveryProcessDescription, "scale")
    descriptor = None
    for klass in uma_DeliveryProcessDescription.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_uma_deliveryprocessdescription_has_typeOfContract():
    assert hasattr(uma_DeliveryProcessDescription, "typeOfContract")
    descriptor = None
    for klass in uma_DeliveryProcessDescription.__mro__:
        if "typeOfContract" in klass.__dict__:
            descriptor = klass.__dict__["typeOfContract"]
            break
    assert isinstance(descriptor, property)



def test_contentcategory_is_not_abstract():
    assert not inspect.isabstract(ContentCategory)


def test_contentcategory_constructor_exists():
    assert callable(ContentCategory.__init__)


def test_contentcategory_constructor_args():
    sig = inspect.signature(ContentCategory.__init__)
    params = list(sig.parameters.keys())



def test_uma_tool_is_not_abstract():
    assert not inspect.isabstract(uma_Tool)


def test_uma_tool_constructor_exists():
    assert callable(uma_Tool.__init__)


def test_uma_tool_constructor_args():
    sig = inspect.signature(uma_Tool.__init__)
    params = list(sig.parameters.keys())
    assert "toolMentor" in params, "Missing parameter 'toolMentor'"
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma_tool_has_toolMentor():
    assert hasattr(uma_Tool, "toolMentor")
    descriptor = None
    for klass in uma_Tool.__mro__:
        if "toolMentor" in klass.__dict__:
            descriptor = klass.__dict__["toolMentor"]
            break
    assert isinstance(descriptor, property)

def test_uma_tool_has_group2():
    assert hasattr(uma_Tool, "group2")
    descriptor = None
    for klass in uma_Tool.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma_workproducttype_is_not_abstract():
    assert not inspect.isabstract(uma_WorkProductType)


def test_uma_workproducttype_constructor_exists():
    assert callable(uma_WorkProductType.__init__)


def test_uma_workproducttype_constructor_args():
    sig = inspect.signature(uma_WorkProductType.__init__)
    params = list(sig.parameters.keys())
    assert "group2" in params, "Missing parameter 'group2'"
    assert "workProduct" in params, "Missing parameter 'workProduct'"

def test_uma_workproducttype_has_group2():
    assert hasattr(uma_WorkProductType, "group2")
    descriptor = None
    for klass in uma_WorkProductType.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproducttype_has_workProduct():
    assert hasattr(uma_WorkProductType, "workProduct")
    descriptor = None
    for klass in uma_WorkProductType.__mro__:
        if "workProduct" in klass.__dict__:
            descriptor = klass.__dict__["workProduct"]
            break
    assert isinstance(descriptor, property)



def test_uma_disciplinegrouping_is_not_abstract():
    assert not inspect.isabstract(uma_DisciplineGrouping)


def test_uma_disciplinegrouping_constructor_exists():
    assert callable(uma_DisciplineGrouping.__init__)


def test_uma_disciplinegrouping_constructor_args():
    sig = inspect.signature(uma_DisciplineGrouping.__init__)
    params = list(sig.parameters.keys())
    assert "discipline" in params, "Missing parameter 'discipline'"
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma_disciplinegrouping_has_discipline():
    assert hasattr(uma_DisciplineGrouping, "discipline")
    descriptor = None
    for klass in uma_DisciplineGrouping.__mro__:
        if "discipline" in klass.__dict__:
            descriptor = klass.__dict__["discipline"]
            break
    assert isinstance(descriptor, property)

def test_uma_disciplinegrouping_has_group2():
    assert hasattr(uma_DisciplineGrouping, "group2")
    descriptor = None
    for klass in uma_DisciplineGrouping.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma_discipline_is_not_abstract():
    assert not inspect.isabstract(uma_Discipline)


def test_uma_discipline_constructor_exists():
    assert callable(uma_Discipline.__init__)


def test_uma_discipline_constructor_args():
    sig = inspect.signature(uma_Discipline.__init__)
    params = list(sig.parameters.keys())
    assert "referenceWorkflow" in params, "Missing parameter 'referenceWorkflow'"
    assert "group2" in params, "Missing parameter 'group2'"
    assert "task" in params, "Missing parameter 'task'"

def test_uma_discipline_has_referenceWorkflow():
    assert hasattr(uma_Discipline, "referenceWorkflow")
    descriptor = None
    for klass in uma_Discipline.__mro__:
        if "referenceWorkflow" in klass.__dict__:
            descriptor = klass.__dict__["referenceWorkflow"]
            break
    assert isinstance(descriptor, property)

def test_uma_discipline_has_group2():
    assert hasattr(uma_Discipline, "group2")
    descriptor = None
    for klass in uma_Discipline.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)

def test_uma_discipline_has_task():
    assert hasattr(uma_Discipline, "task")
    descriptor = None
    for klass in uma_Discipline.__mro__:
        if "task" in klass.__dict__:
            descriptor = klass.__dict__["task"]
            break
    assert isinstance(descriptor, property)



def test_uma_rolesetgrouping_is_not_abstract():
    assert not inspect.isabstract(uma_RoleSetGrouping)


def test_uma_rolesetgrouping_constructor_exists():
    assert callable(uma_RoleSetGrouping.__init__)


def test_uma_rolesetgrouping_constructor_args():
    sig = inspect.signature(uma_RoleSetGrouping.__init__)
    params = list(sig.parameters.keys())
    assert "roleSet" in params, "Missing parameter 'roleSet'"
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma_rolesetgrouping_has_roleSet():
    assert hasattr(uma_RoleSetGrouping, "roleSet")
    descriptor = None
    for klass in uma_RoleSetGrouping.__mro__:
        if "roleSet" in klass.__dict__:
            descriptor = klass.__dict__["roleSet"]
            break
    assert isinstance(descriptor, property)

def test_uma_rolesetgrouping_has_group2():
    assert hasattr(uma_RoleSetGrouping, "group2")
    descriptor = None
    for klass in uma_RoleSetGrouping.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma_domain_is_not_abstract():
    assert not inspect.isabstract(uma_Domain)


def test_uma_domain_constructor_exists():
    assert callable(uma_Domain.__init__)


def test_uma_domain_constructor_args():
    sig = inspect.signature(uma_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "workProduct" in params, "Missing parameter 'workProduct'"
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma_domain_has_workProduct():
    assert hasattr(uma_Domain, "workProduct")
    descriptor = None
    for klass in uma_Domain.__mro__:
        if "workProduct" in klass.__dict__:
            descriptor = klass.__dict__["workProduct"]
            break
    assert isinstance(descriptor, property)

def test_uma_domain_has_group2():
    assert hasattr(uma_Domain, "group2")
    descriptor = None
    for klass in uma_Domain.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma_roleset_is_not_abstract():
    assert not inspect.isabstract(uma_RoleSet)


def test_uma_roleset_constructor_exists():
    assert callable(uma_RoleSet.__init__)


def test_uma_roleset_constructor_args():
    sig = inspect.signature(uma_RoleSet.__init__)
    params = list(sig.parameters.keys())
    assert "role" in params, "Missing parameter 'role'"
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma_roleset_has_role():
    assert hasattr(uma_RoleSet, "role")
    descriptor = None
    for klass in uma_RoleSet.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_uma_roleset_has_group2():
    assert hasattr(uma_RoleSet, "group2")
    descriptor = None
    for klass in uma_RoleSet.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma_customcategory_is_not_abstract():
    assert not inspect.isabstract(uma_CustomCategory)


def test_uma_customcategory_constructor_exists():
    assert callable(uma_CustomCategory.__init__)


def test_uma_customcategory_constructor_args():
    sig = inspect.signature(uma_CustomCategory.__init__)
    params = list(sig.parameters.keys())
    assert "group2" in params, "Missing parameter 'group2'"
    assert "subCategory" in params, "Missing parameter 'subCategory'"
    assert "categorizedElement" in params, "Missing parameter 'categorizedElement'"

def test_uma_customcategory_has_group2():
    assert hasattr(uma_CustomCategory, "group2")
    descriptor = None
    for klass in uma_CustomCategory.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)

def test_uma_customcategory_has_subCategory():
    assert hasattr(uma_CustomCategory, "subCategory")
    descriptor = None
    for klass in uma_CustomCategory.__mro__:
        if "subCategory" in klass.__dict__:
            descriptor = klass.__dict__["subCategory"]
            break
    assert isinstance(descriptor, property)

def test_uma_customcategory_has_categorizedElement():
    assert hasattr(uma_CustomCategory, "categorizedElement")
    descriptor = None
    for klass in uma_CustomCategory.__mro__:
        if "categorizedElement" in klass.__dict__:
            descriptor = klass.__dict__["categorizedElement"]
            break
    assert isinstance(descriptor, property)



def test_workbreakdownelement_is_not_abstract():
    assert not inspect.isabstract(WorkBreakdownElement)


def test_workbreakdownelement_constructor_exists():
    assert callable(WorkBreakdownElement.__init__)


def test_workbreakdownelement_constructor_args():
    sig = inspect.signature(WorkBreakdownElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_milestone_is_not_abstract():
    assert not inspect.isabstract(uma_Milestone)


def test_uma_milestone_constructor_exists():
    assert callable(uma_Milestone.__init__)


def test_uma_milestone_constructor_args():
    sig = inspect.signature(uma_Milestone.__init__)
    params = list(sig.parameters.keys())
    assert "requiredResult" in params, "Missing parameter 'requiredResult'"

def test_uma_milestone_has_requiredResult():
    assert hasattr(uma_Milestone, "requiredResult")
    descriptor = None
    for klass in uma_Milestone.__mro__:
        if "requiredResult" in klass.__dict__:
            descriptor = klass.__dict__["requiredResult"]
            break
    assert isinstance(descriptor, property)



def test_uma_taskdescriptor_is_not_abstract():
    assert not inspect.isabstract(uma_TaskDescriptor)


def test_uma_taskdescriptor_constructor_exists():
    assert callable(uma_TaskDescriptor.__init__)


def test_uma_taskdescriptor_constructor_args():
    sig = inspect.signature(uma_TaskDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronizedWithSource" in params, "Missing parameter 'isSynchronizedWithSource'"
    assert "group3" in params, "Missing parameter 'group3'"
    assert "mandatoryInput" in params, "Missing parameter 'mandatoryInput'"
    assert "output" in params, "Missing parameter 'output'"
    assert "task" in params, "Missing parameter 'task'"
    assert "optionalInput" in params, "Missing parameter 'optionalInput'"
    assert "performedPrimarilyBy" in params, "Missing parameter 'performedPrimarilyBy'"
    assert "externalInput" in params, "Missing parameter 'externalInput'"
    assert "assistedBy" in params, "Missing parameter 'assistedBy'"
    assert "additionallyPerformedBy" in params, "Missing parameter 'additionallyPerformedBy'"

def test_uma_taskdescriptor_has_isSynchronizedWithSource():
    assert hasattr(uma_TaskDescriptor, "isSynchronizedWithSource")
    descriptor = None
    for klass in uma_TaskDescriptor.__mro__:
        if "isSynchronizedWithSource" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronizedWithSource"]
            break
    assert isinstance(descriptor, property)

def test_uma_taskdescriptor_has_group3():
    assert hasattr(uma_TaskDescriptor, "group3")
    descriptor = None
    for klass in uma_TaskDescriptor.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)

def test_uma_taskdescriptor_has_mandatoryInput():
    assert hasattr(uma_TaskDescriptor, "mandatoryInput")
    descriptor = None
    for klass in uma_TaskDescriptor.__mro__:
        if "mandatoryInput" in klass.__dict__:
            descriptor = klass.__dict__["mandatoryInput"]
            break
    assert isinstance(descriptor, property)

def test_uma_taskdescriptor_has_output():
    assert hasattr(uma_TaskDescriptor, "output")
    descriptor = None
    for klass in uma_TaskDescriptor.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_uma_taskdescriptor_has_task():
    assert hasattr(uma_TaskDescriptor, "task")
    descriptor = None
    for klass in uma_TaskDescriptor.__mro__:
        if "task" in klass.__dict__:
            descriptor = klass.__dict__["task"]
            break
    assert isinstance(descriptor, property)

def test_uma_taskdescriptor_has_optionalInput():
    assert hasattr(uma_TaskDescriptor, "optionalInput")
    descriptor = None
    for klass in uma_TaskDescriptor.__mro__:
        if "optionalInput" in klass.__dict__:
            descriptor = klass.__dict__["optionalInput"]
            break
    assert isinstance(descriptor, property)

def test_uma_taskdescriptor_has_performedPrimarilyBy():
    assert hasattr(uma_TaskDescriptor, "performedPrimarilyBy")
    descriptor = None
    for klass in uma_TaskDescriptor.__mro__:
        if "performedPrimarilyBy" in klass.__dict__:
            descriptor = klass.__dict__["performedPrimarilyBy"]
            break
    assert isinstance(descriptor, property)

def test_uma_taskdescriptor_has_externalInput():
    assert hasattr(uma_TaskDescriptor, "externalInput")
    descriptor = None
    for klass in uma_TaskDescriptor.__mro__:
        if "externalInput" in klass.__dict__:
            descriptor = klass.__dict__["externalInput"]
            break
    assert isinstance(descriptor, property)

def test_uma_taskdescriptor_has_assistedBy():
    assert hasattr(uma_TaskDescriptor, "assistedBy")
    descriptor = None
    for klass in uma_TaskDescriptor.__mro__:
        if "assistedBy" in klass.__dict__:
            descriptor = klass.__dict__["assistedBy"]
            break
    assert isinstance(descriptor, property)

def test_uma_taskdescriptor_has_additionallyPerformedBy():
    assert hasattr(uma_TaskDescriptor, "additionallyPerformedBy")
    descriptor = None
    for klass in uma_TaskDescriptor.__mro__:
        if "additionallyPerformedBy" in klass.__dict__:
            descriptor = klass.__dict__["additionallyPerformedBy"]
            break
    assert isinstance(descriptor, property)



def test_uma_activity_is_not_abstract():
    assert not inspect.isabstract(uma_Activity)


def test_uma_activity_constructor_exists():
    assert callable(uma_Activity.__init__)


def test_uma_activity_constructor_args():
    sig = inspect.signature(uma_Activity.__init__)
    params = list(sig.parameters.keys())
    assert "postcondition" in params, "Missing parameter 'postcondition'"
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "variabilityBasedOnElement" in params, "Missing parameter 'variabilityBasedOnElement'"
    assert "variabilityType" in params, "Missing parameter 'variabilityType'"
    assert "roadmap" in params, "Missing parameter 'roadmap'"
    assert "group3" in params, "Missing parameter 'group3'"
    assert "isEnactable" in params, "Missing parameter 'isEnactable'"

def test_uma_activity_has_postcondition():
    assert hasattr(uma_Activity, "postcondition")
    descriptor = None
    for klass in uma_Activity.__mro__:
        if "postcondition" in klass.__dict__:
            descriptor = klass.__dict__["postcondition"]
            break
    assert isinstance(descriptor, property)

def test_uma_activity_has_precondition():
    assert hasattr(uma_Activity, "precondition")
    descriptor = None
    for klass in uma_Activity.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_uma_activity_has_variabilityBasedOnElement():
    assert hasattr(uma_Activity, "variabilityBasedOnElement")
    descriptor = None
    for klass in uma_Activity.__mro__:
        if "variabilityBasedOnElement" in klass.__dict__:
            descriptor = klass.__dict__["variabilityBasedOnElement"]
            break
    assert isinstance(descriptor, property)

def test_uma_activity_has_variabilityType():
    assert hasattr(uma_Activity, "variabilityType")
    descriptor = None
    for klass in uma_Activity.__mro__:
        if "variabilityType" in klass.__dict__:
            descriptor = klass.__dict__["variabilityType"]
            break
    assert isinstance(descriptor, property)

def test_uma_activity_has_roadmap():
    assert hasattr(uma_Activity, "roadmap")
    descriptor = None
    for klass in uma_Activity.__mro__:
        if "roadmap" in klass.__dict__:
            descriptor = klass.__dict__["roadmap"]
            break
    assert isinstance(descriptor, property)

def test_uma_activity_has_group3():
    assert hasattr(uma_Activity, "group3")
    descriptor = None
    for klass in uma_Activity.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)

def test_uma_activity_has_isEnactable():
    assert hasattr(uma_Activity, "isEnactable")
    descriptor = None
    for klass in uma_Activity.__mro__:
        if "isEnactable" in klass.__dict__:
            descriptor = klass.__dict__["isEnactable"]
            break
    assert isinstance(descriptor, property)



def test_describableelement_is_not_abstract():
    assert not inspect.isabstract(DescribableElement)


def test_describableelement_constructor_exists():
    assert callable(DescribableElement.__init__)


def test_describableelement_constructor_args():
    sig = inspect.signature(DescribableElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_processelement_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessElement)


def test_uma_processelement_constructor_exists():
    assert callable(uma_ProcessElement.__init__)


def test_uma_processelement_constructor_args():
    sig = inspect.signature(uma_ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_contentelement_is_not_abstract():
    assert not inspect.isabstract(uma_ContentElement)


def test_uma_contentelement_constructor_exists():
    assert callable(uma_ContentElement.__init__)


def test_uma_contentelement_constructor_args():
    sig = inspect.signature(uma_ContentElement.__init__)
    params = list(sig.parameters.keys())
    assert "concept" in params, "Missing parameter 'concept'"
    assert "whitepaper" in params, "Missing parameter 'whitepaper'"
    assert "reusableAsset" in params, "Missing parameter 'reusableAsset'"
    assert "guideline" in params, "Missing parameter 'guideline'"
    assert "example" in params, "Missing parameter 'example'"
    assert "variabilityType" in params, "Missing parameter 'variabilityType'"
    assert "group1" in params, "Missing parameter 'group1'"
    assert "checklist" in params, "Missing parameter 'checklist'"
    assert "variabilityBasedOnElement" in params, "Missing parameter 'variabilityBasedOnElement'"
    assert "supportingMaterial" in params, "Missing parameter 'supportingMaterial'"

def test_uma_contentelement_has_concept():
    assert hasattr(uma_ContentElement, "concept")
    descriptor = None
    for klass in uma_ContentElement.__mro__:
        if "concept" in klass.__dict__:
            descriptor = klass.__dict__["concept"]
            break
    assert isinstance(descriptor, property)

def test_uma_contentelement_has_whitepaper():
    assert hasattr(uma_ContentElement, "whitepaper")
    descriptor = None
    for klass in uma_ContentElement.__mro__:
        if "whitepaper" in klass.__dict__:
            descriptor = klass.__dict__["whitepaper"]
            break
    assert isinstance(descriptor, property)

def test_uma_contentelement_has_reusableAsset():
    assert hasattr(uma_ContentElement, "reusableAsset")
    descriptor = None
    for klass in uma_ContentElement.__mro__:
        if "reusableAsset" in klass.__dict__:
            descriptor = klass.__dict__["reusableAsset"]
            break
    assert isinstance(descriptor, property)

def test_uma_contentelement_has_guideline():
    assert hasattr(uma_ContentElement, "guideline")
    descriptor = None
    for klass in uma_ContentElement.__mro__:
        if "guideline" in klass.__dict__:
            descriptor = klass.__dict__["guideline"]
            break
    assert isinstance(descriptor, property)

def test_uma_contentelement_has_example():
    assert hasattr(uma_ContentElement, "example")
    descriptor = None
    for klass in uma_ContentElement.__mro__:
        if "example" in klass.__dict__:
            descriptor = klass.__dict__["example"]
            break
    assert isinstance(descriptor, property)

def test_uma_contentelement_has_variabilityType():
    assert hasattr(uma_ContentElement, "variabilityType")
    descriptor = None
    for klass in uma_ContentElement.__mro__:
        if "variabilityType" in klass.__dict__:
            descriptor = klass.__dict__["variabilityType"]
            break
    assert isinstance(descriptor, property)

def test_uma_contentelement_has_group1():
    assert hasattr(uma_ContentElement, "group1")
    descriptor = None
    for klass in uma_ContentElement.__mro__:
        if "group1" in klass.__dict__:
            descriptor = klass.__dict__["group1"]
            break
    assert isinstance(descriptor, property)

def test_uma_contentelement_has_checklist():
    assert hasattr(uma_ContentElement, "checklist")
    descriptor = None
    for klass in uma_ContentElement.__mro__:
        if "checklist" in klass.__dict__:
            descriptor = klass.__dict__["checklist"]
            break
    assert isinstance(descriptor, property)

def test_uma_contentelement_has_variabilityBasedOnElement():
    assert hasattr(uma_ContentElement, "variabilityBasedOnElement")
    descriptor = None
    for klass in uma_ContentElement.__mro__:
        if "variabilityBasedOnElement" in klass.__dict__:
            descriptor = klass.__dict__["variabilityBasedOnElement"]
            break
    assert isinstance(descriptor, property)

def test_uma_contentelement_has_supportingMaterial():
    assert hasattr(uma_ContentElement, "supportingMaterial")
    descriptor = None
    for klass in uma_ContentElement.__mro__:
        if "supportingMaterial" in klass.__dict__:
            descriptor = klass.__dict__["supportingMaterial"]
            break
    assert isinstance(descriptor, property)



def test_methodunit_is_not_abstract():
    assert not inspect.isabstract(MethodUnit)


def test_methodunit_constructor_exists():
    assert callable(MethodUnit.__init__)


def test_methodunit_constructor_args():
    sig = inspect.signature(MethodUnit.__init__)
    params = list(sig.parameters.keys())



def test_uma_methodplugin_is_not_abstract():
    assert not inspect.isabstract(uma_MethodPlugin)


def test_uma_methodplugin_constructor_exists():
    assert callable(uma_MethodPlugin.__init__)


def test_uma_methodplugin_constructor_args():
    sig = inspect.signature(uma_MethodPlugin.__init__)
    params = list(sig.parameters.keys())
    assert "referencedMethodPlugin" in params, "Missing parameter 'referencedMethodPlugin'"
    assert "userChangeable" in params, "Missing parameter 'userChangeable'"
    assert "supporting" in params, "Missing parameter 'supporting'"

def test_uma_methodplugin_has_referencedMethodPlugin():
    assert hasattr(uma_MethodPlugin, "referencedMethodPlugin")
    descriptor = None
    for klass in uma_MethodPlugin.__mro__:
        if "referencedMethodPlugin" in klass.__dict__:
            descriptor = klass.__dict__["referencedMethodPlugin"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodplugin_has_userChangeable():
    assert hasattr(uma_MethodPlugin, "userChangeable")
    descriptor = None
    for klass in uma_MethodPlugin.__mro__:
        if "userChangeable" in klass.__dict__:
            descriptor = klass.__dict__["userChangeable"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodplugin_has_supporting():
    assert hasattr(uma_MethodPlugin, "supporting")
    descriptor = None
    for klass in uma_MethodPlugin.__mro__:
        if "supporting" in klass.__dict__:
            descriptor = klass.__dict__["supporting"]
            break
    assert isinstance(descriptor, property)



def test_uma_methodlibrary_is_not_abstract():
    assert not inspect.isabstract(uma_MethodLibrary)


def test_uma_methodlibrary_constructor_exists():
    assert callable(uma_MethodLibrary.__init__)


def test_uma_methodlibrary_constructor_args():
    sig = inspect.signature(uma_MethodLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "tool" in params, "Missing parameter 'tool'"

def test_uma_methodlibrary_has_tool():
    assert hasattr(uma_MethodLibrary, "tool")
    descriptor = None
    for klass in uma_MethodLibrary.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)



def test_uma_methodconfiguration_is_not_abstract():
    assert not inspect.isabstract(uma_MethodConfiguration)


def test_uma_methodconfiguration_constructor_exists():
    assert callable(uma_MethodConfiguration.__init__)


def test_uma_methodconfiguration_constructor_args():
    sig = inspect.signature(uma_MethodConfiguration.__init__)
    params = list(sig.parameters.keys())
    assert "subtractedCategory" in params, "Missing parameter 'subtractedCategory'"
    assert "methodPackageSelection" in params, "Missing parameter 'methodPackageSelection'"
    assert "addedCategory" in params, "Missing parameter 'addedCategory'"
    assert "methodPluginSelection" in params, "Missing parameter 'methodPluginSelection'"
    assert "baseConfiguration" in params, "Missing parameter 'baseConfiguration'"
    assert "processView" in params, "Missing parameter 'processView'"
    assert "defaultView" in params, "Missing parameter 'defaultView'"

def test_uma_methodconfiguration_has_subtractedCategory():
    assert hasattr(uma_MethodConfiguration, "subtractedCategory")
    descriptor = None
    for klass in uma_MethodConfiguration.__mro__:
        if "subtractedCategory" in klass.__dict__:
            descriptor = klass.__dict__["subtractedCategory"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodconfiguration_has_methodPackageSelection():
    assert hasattr(uma_MethodConfiguration, "methodPackageSelection")
    descriptor = None
    for klass in uma_MethodConfiguration.__mro__:
        if "methodPackageSelection" in klass.__dict__:
            descriptor = klass.__dict__["methodPackageSelection"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodconfiguration_has_addedCategory():
    assert hasattr(uma_MethodConfiguration, "addedCategory")
    descriptor = None
    for klass in uma_MethodConfiguration.__mro__:
        if "addedCategory" in klass.__dict__:
            descriptor = klass.__dict__["addedCategory"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodconfiguration_has_methodPluginSelection():
    assert hasattr(uma_MethodConfiguration, "methodPluginSelection")
    descriptor = None
    for klass in uma_MethodConfiguration.__mro__:
        if "methodPluginSelection" in klass.__dict__:
            descriptor = klass.__dict__["methodPluginSelection"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodconfiguration_has_baseConfiguration():
    assert hasattr(uma_MethodConfiguration, "baseConfiguration")
    descriptor = None
    for klass in uma_MethodConfiguration.__mro__:
        if "baseConfiguration" in klass.__dict__:
            descriptor = klass.__dict__["baseConfiguration"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodconfiguration_has_processView():
    assert hasattr(uma_MethodConfiguration, "processView")
    descriptor = None
    for klass in uma_MethodConfiguration.__mro__:
        if "processView" in klass.__dict__:
            descriptor = klass.__dict__["processView"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodconfiguration_has_defaultView():
    assert hasattr(uma_MethodConfiguration, "defaultView")
    descriptor = None
    for klass in uma_MethodConfiguration.__mro__:
        if "defaultView" in klass.__dict__:
            descriptor = klass.__dict__["defaultView"]
            break
    assert isinstance(descriptor, property)



def test_uma_contentdescription_is_not_abstract():
    assert not inspect.isabstract(uma_ContentDescription)


def test_uma_contentdescription_constructor_exists():
    assert callable(uma_ContentDescription.__init__)


def test_uma_contentdescription_constructor_args():
    sig = inspect.signature(uma_ContentDescription.__init__)
    params = list(sig.parameters.keys())
    assert "keyConsiderations" in params, "Missing parameter 'keyConsiderations'"
    assert "externalId" in params, "Missing parameter 'externalId'"
    assert "mainDescription" in params, "Missing parameter 'mainDescription'"

def test_uma_contentdescription_has_keyConsiderations():
    assert hasattr(uma_ContentDescription, "keyConsiderations")
    descriptor = None
    for klass in uma_ContentDescription.__mro__:
        if "keyConsiderations" in klass.__dict__:
            descriptor = klass.__dict__["keyConsiderations"]
            break
    assert isinstance(descriptor, property)

def test_uma_contentdescription_has_externalId():
    assert hasattr(uma_ContentDescription, "externalId")
    descriptor = None
    for klass in uma_ContentDescription.__mro__:
        if "externalId" in klass.__dict__:
            descriptor = klass.__dict__["externalId"]
            break
    assert isinstance(descriptor, property)

def test_uma_contentdescription_has_mainDescription():
    assert hasattr(uma_ContentDescription, "mainDescription")
    descriptor = None
    for klass in uma_ContentDescription.__mro__:
        if "mainDescription" in klass.__dict__:
            descriptor = klass.__dict__["mainDescription"]
            break
    assert isinstance(descriptor, property)



def test_methodpackage_is_not_abstract():
    assert not inspect.isabstract(MethodPackage)


def test_methodpackage_constructor_exists():
    assert callable(MethodPackage.__init__)


def test_methodpackage_constructor_args():
    sig = inspect.signature(MethodPackage.__init__)
    params = list(sig.parameters.keys())



def test_uma_processpackage_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessPackage)


def test_uma_processpackage_constructor_exists():
    assert callable(uma_ProcessPackage.__init__)


def test_uma_processpackage_constructor_args():
    sig = inspect.signature(uma_ProcessPackage.__init__)
    params = list(sig.parameters.keys())
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma_processpackage_has_group2():
    assert hasattr(uma_ProcessPackage, "group2")
    descriptor = None
    for klass in uma_ProcessPackage.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma_contentpackage_is_not_abstract():
    assert not inspect.isabstract(uma_ContentPackage)


def test_uma_contentpackage_constructor_exists():
    assert callable(uma_ContentPackage.__init__)


def test_uma_contentpackage_constructor_args():
    sig = inspect.signature(uma_ContentPackage.__init__)
    params = list(sig.parameters.keys())
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma_contentpackage_has_group2():
    assert hasattr(uma_ContentPackage, "group2")
    descriptor = None
    for klass in uma_ContentPackage.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma_contentcategorypackage_is_not_abstract():
    assert not inspect.isabstract(uma_ContentCategoryPackage)


def test_uma_contentcategorypackage_constructor_exists():
    assert callable(uma_ContentCategoryPackage.__init__)


def test_uma_contentcategorypackage_constructor_args():
    sig = inspect.signature(uma_ContentCategoryPackage.__init__)
    params = list(sig.parameters.keys())
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma_contentcategorypackage_has_group2():
    assert hasattr(uma_ContentCategoryPackage, "group2")
    descriptor = None
    for klass in uma_ContentCategoryPackage.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_contentelement_is_not_abstract():
    assert not inspect.isabstract(ContentElement)


def test_contentelement_constructor_exists():
    assert callable(ContentElement.__init__)


def test_contentelement_constructor_args():
    sig = inspect.signature(ContentElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_kind_is_not_abstract():
    assert not inspect.isabstract(uma_Kind)


def test_uma_kind_constructor_exists():
    assert callable(uma_Kind.__init__)


def test_uma_kind_constructor_args():
    sig = inspect.signature(uma_Kind.__init__)
    params = list(sig.parameters.keys())
    assert "applicableMetaClassInfo" in params, "Missing parameter 'applicableMetaClassInfo'"

def test_uma_kind_has_applicableMetaClassInfo():
    assert hasattr(uma_Kind, "applicableMetaClassInfo")
    descriptor = None
    for klass in uma_Kind.__mro__:
        if "applicableMetaClassInfo" in klass.__dict__:
            descriptor = klass.__dict__["applicableMetaClassInfo"]
            break
    assert isinstance(descriptor, property)



def test_uma_guidance_is_not_abstract():
    assert not inspect.isabstract(uma_Guidance)


def test_uma_guidance_constructor_exists():
    assert callable(uma_Guidance.__init__)


def test_uma_guidance_constructor_args():
    sig = inspect.signature(uma_Guidance.__init__)
    params = list(sig.parameters.keys())



def test_uma_task_is_not_abstract():
    assert not inspect.isabstract(uma_Task)


def test_uma_task_constructor_exists():
    assert callable(uma_Task.__init__)


def test_uma_task_constructor_args():
    sig = inspect.signature(uma_Task.__init__)
    params = list(sig.parameters.keys())
    assert "group2" in params, "Missing parameter 'group2'"
    assert "mandatoryInput" in params, "Missing parameter 'mandatoryInput'"
    assert "postcondition" in params, "Missing parameter 'postcondition'"
    assert "optionalInput" in params, "Missing parameter 'optionalInput'"
    assert "toolMentor" in params, "Missing parameter 'toolMentor'"
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "estimate" in params, "Missing parameter 'estimate'"
    assert "estimationConsiderations" in params, "Missing parameter 'estimationConsiderations'"
    assert "performedBy" in params, "Missing parameter 'performedBy'"
    assert "additionallyPerformedBy" in params, "Missing parameter 'additionallyPerformedBy'"
    assert "output" in params, "Missing parameter 'output'"

def test_uma_task_has_group2():
    assert hasattr(uma_Task, "group2")
    descriptor = None
    for klass in uma_Task.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)

def test_uma_task_has_mandatoryInput():
    assert hasattr(uma_Task, "mandatoryInput")
    descriptor = None
    for klass in uma_Task.__mro__:
        if "mandatoryInput" in klass.__dict__:
            descriptor = klass.__dict__["mandatoryInput"]
            break
    assert isinstance(descriptor, property)

def test_uma_task_has_postcondition():
    assert hasattr(uma_Task, "postcondition")
    descriptor = None
    for klass in uma_Task.__mro__:
        if "postcondition" in klass.__dict__:
            descriptor = klass.__dict__["postcondition"]
            break
    assert isinstance(descriptor, property)

def test_uma_task_has_optionalInput():
    assert hasattr(uma_Task, "optionalInput")
    descriptor = None
    for klass in uma_Task.__mro__:
        if "optionalInput" in klass.__dict__:
            descriptor = klass.__dict__["optionalInput"]
            break
    assert isinstance(descriptor, property)

def test_uma_task_has_toolMentor():
    assert hasattr(uma_Task, "toolMentor")
    descriptor = None
    for klass in uma_Task.__mro__:
        if "toolMentor" in klass.__dict__:
            descriptor = klass.__dict__["toolMentor"]
            break
    assert isinstance(descriptor, property)

def test_uma_task_has_precondition():
    assert hasattr(uma_Task, "precondition")
    descriptor = None
    for klass in uma_Task.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_uma_task_has_estimate():
    assert hasattr(uma_Task, "estimate")
    descriptor = None
    for klass in uma_Task.__mro__:
        if "estimate" in klass.__dict__:
            descriptor = klass.__dict__["estimate"]
            break
    assert isinstance(descriptor, property)

def test_uma_task_has_estimationConsiderations():
    assert hasattr(uma_Task, "estimationConsiderations")
    descriptor = None
    for klass in uma_Task.__mro__:
        if "estimationConsiderations" in klass.__dict__:
            descriptor = klass.__dict__["estimationConsiderations"]
            break
    assert isinstance(descriptor, property)

def test_uma_task_has_performedBy():
    assert hasattr(uma_Task, "performedBy")
    descriptor = None
    for klass in uma_Task.__mro__:
        if "performedBy" in klass.__dict__:
            descriptor = klass.__dict__["performedBy"]
            break
    assert isinstance(descriptor, property)

def test_uma_task_has_additionallyPerformedBy():
    assert hasattr(uma_Task, "additionallyPerformedBy")
    descriptor = None
    for klass in uma_Task.__mro__:
        if "additionallyPerformedBy" in klass.__dict__:
            descriptor = klass.__dict__["additionallyPerformedBy"]
            break
    assert isinstance(descriptor, property)

def test_uma_task_has_output():
    assert hasattr(uma_Task, "output")
    descriptor = None
    for klass in uma_Task.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_uma_workproduct_is_not_abstract():
    assert not inspect.isabstract(uma_WorkProduct)


def test_uma_workproduct_constructor_exists():
    assert callable(uma_WorkProduct.__init__)


def test_uma_workproduct_constructor_args():
    sig = inspect.signature(uma_WorkProduct.__init__)
    params = list(sig.parameters.keys())
    assert "toolMentor" in params, "Missing parameter 'toolMentor'"
    assert "template" in params, "Missing parameter 'template'"
    assert "group2" in params, "Missing parameter 'group2'"
    assert "report" in params, "Missing parameter 'report'"
    assert "estimationConsiderations" in params, "Missing parameter 'estimationConsiderations'"
    assert "estimate" in params, "Missing parameter 'estimate'"

def test_uma_workproduct_has_toolMentor():
    assert hasattr(uma_WorkProduct, "toolMentor")
    descriptor = None
    for klass in uma_WorkProduct.__mro__:
        if "toolMentor" in klass.__dict__:
            descriptor = klass.__dict__["toolMentor"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproduct_has_template():
    assert hasattr(uma_WorkProduct, "template")
    descriptor = None
    for klass in uma_WorkProduct.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproduct_has_group2():
    assert hasattr(uma_WorkProduct, "group2")
    descriptor = None
    for klass in uma_WorkProduct.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproduct_has_report():
    assert hasattr(uma_WorkProduct, "report")
    descriptor = None
    for klass in uma_WorkProduct.__mro__:
        if "report" in klass.__dict__:
            descriptor = klass.__dict__["report"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproduct_has_estimationConsiderations():
    assert hasattr(uma_WorkProduct, "estimationConsiderations")
    descriptor = None
    for klass in uma_WorkProduct.__mro__:
        if "estimationConsiderations" in klass.__dict__:
            descriptor = klass.__dict__["estimationConsiderations"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproduct_has_estimate():
    assert hasattr(uma_WorkProduct, "estimate")
    descriptor = None
    for klass in uma_WorkProduct.__mro__:
        if "estimate" in klass.__dict__:
            descriptor = klass.__dict__["estimate"]
            break
    assert isinstance(descriptor, property)



def test_uma_contentcategory_is_not_abstract():
    assert not inspect.isabstract(uma_ContentCategory)


def test_uma_contentcategory_constructor_exists():
    assert callable(uma_ContentCategory.__init__)


def test_uma_contentcategory_constructor_args():
    sig = inspect.signature(uma_ContentCategory.__init__)
    params = list(sig.parameters.keys())



def test_methodelement_is_not_abstract():
    assert not inspect.isabstract(MethodElement)


def test_methodelement_constructor_exists():
    assert callable(MethodElement.__init__)


def test_methodelement_constructor_args():
    sig = inspect.signature(MethodElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_methodpackage_is_not_abstract():
    assert not inspect.isabstract(uma_MethodPackage)


def test_uma_methodpackage_constructor_exists():
    assert callable(uma_MethodPackage.__init__)


def test_uma_methodpackage_constructor_args():
    sig = inspect.signature(uma_MethodPackage.__init__)
    params = list(sig.parameters.keys())
    assert "reusedPackage" in params, "Missing parameter 'reusedPackage'"
    assert "group1" in params, "Missing parameter 'group1'"
    assert "global_" in params, "Missing parameter 'global_'"

def test_uma_methodpackage_has_reusedPackage():
    assert hasattr(uma_MethodPackage, "reusedPackage")
    descriptor = None
    for klass in uma_MethodPackage.__mro__:
        if "reusedPackage" in klass.__dict__:
            descriptor = klass.__dict__["reusedPackage"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodpackage_has_group1():
    assert hasattr(uma_MethodPackage, "group1")
    descriptor = None
    for klass in uma_MethodPackage.__mro__:
        if "group1" in klass.__dict__:
            descriptor = klass.__dict__["group1"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodpackage_has_global_():
    assert hasattr(uma_MethodPackage, "global_")
    descriptor = None
    for klass in uma_MethodPackage.__mro__:
        if "global_" in klass.__dict__:
            descriptor = klass.__dict__["global_"]
            break
    assert isinstance(descriptor, property)



def test_uma_methodunit_is_not_abstract():
    assert not inspect.isabstract(uma_MethodUnit)


def test_uma_methodunit_constructor_exists():
    assert callable(uma_MethodUnit.__init__)


def test_uma_methodunit_constructor_args():
    sig = inspect.signature(uma_MethodUnit.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "changeDate" in params, "Missing parameter 'changeDate'"
    assert "authors" in params, "Missing parameter 'authors'"
    assert "copyright" in params, "Missing parameter 'copyright'"
    assert "changeDescription" in params, "Missing parameter 'changeDescription'"

def test_uma_methodunit_has_version():
    assert hasattr(uma_MethodUnit, "version")
    descriptor = None
    for klass in uma_MethodUnit.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodunit_has_changeDate():
    assert hasattr(uma_MethodUnit, "changeDate")
    descriptor = None
    for klass in uma_MethodUnit.__mro__:
        if "changeDate" in klass.__dict__:
            descriptor = klass.__dict__["changeDate"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodunit_has_authors():
    assert hasattr(uma_MethodUnit, "authors")
    descriptor = None
    for klass in uma_MethodUnit.__mro__:
        if "authors" in klass.__dict__:
            descriptor = klass.__dict__["authors"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodunit_has_copyright():
    assert hasattr(uma_MethodUnit, "copyright")
    descriptor = None
    for klass in uma_MethodUnit.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodunit_has_changeDescription():
    assert hasattr(uma_MethodUnit, "changeDescription")
    descriptor = None
    for klass in uma_MethodUnit.__mro__:
        if "changeDescription" in klass.__dict__:
            descriptor = klass.__dict__["changeDescription"]
            break
    assert isinstance(descriptor, property)



def test_uma_describableelement_is_not_abstract():
    assert not inspect.isabstract(uma_DescribableElement)


def test_uma_describableelement_constructor_exists():
    assert callable(uma_DescribableElement.__init__)


def test_uma_describableelement_constructor_args():
    sig = inspect.signature(uma_DescribableElement.__init__)
    params = list(sig.parameters.keys())
    assert "nodeicon" in params, "Missing parameter 'nodeicon'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "fulfill" in params, "Missing parameter 'fulfill'"
    assert "shapeicon" in params, "Missing parameter 'shapeicon'"

def test_uma_describableelement_has_nodeicon():
    assert hasattr(uma_DescribableElement, "nodeicon")
    descriptor = None
    for klass in uma_DescribableElement.__mro__:
        if "nodeicon" in klass.__dict__:
            descriptor = klass.__dict__["nodeicon"]
            break
    assert isinstance(descriptor, property)

def test_uma_describableelement_has_isAbstract():
    assert hasattr(uma_DescribableElement, "isAbstract")
    descriptor = None
    for klass in uma_DescribableElement.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_uma_describableelement_has_fulfill():
    assert hasattr(uma_DescribableElement, "fulfill")
    descriptor = None
    for klass in uma_DescribableElement.__mro__:
        if "fulfill" in klass.__dict__:
            descriptor = klass.__dict__["fulfill"]
            break
    assert isinstance(descriptor, property)

def test_uma_describableelement_has_shapeicon():
    assert hasattr(uma_DescribableElement, "shapeicon")
    descriptor = None
    for klass in uma_DescribableElement.__mro__:
        if "shapeicon" in klass.__dict__:
            descriptor = klass.__dict__["shapeicon"]
            break
    assert isinstance(descriptor, property)



def test_uma_section_is_not_abstract():
    assert not inspect.isabstract(uma_Section)


def test_uma_section_constructor_exists():
    assert callable(uma_Section.__init__)


def test_uma_section_constructor_args():
    sig = inspect.signature(uma_Section.__init__)
    params = list(sig.parameters.keys())
    assert "variabilityType" in params, "Missing parameter 'variabilityType'"
    assert "sectionName" in params, "Missing parameter 'sectionName'"
    assert "variabilityBasedOnElement" in params, "Missing parameter 'variabilityBasedOnElement'"
    assert "predecessor" in params, "Missing parameter 'predecessor'"
    assert "description" in params, "Missing parameter 'description'"

def test_uma_section_has_variabilityType():
    assert hasattr(uma_Section, "variabilityType")
    descriptor = None
    for klass in uma_Section.__mro__:
        if "variabilityType" in klass.__dict__:
            descriptor = klass.__dict__["variabilityType"]
            break
    assert isinstance(descriptor, property)

def test_uma_section_has_sectionName():
    assert hasattr(uma_Section, "sectionName")
    descriptor = None
    for klass in uma_Section.__mro__:
        if "sectionName" in klass.__dict__:
            descriptor = klass.__dict__["sectionName"]
            break
    assert isinstance(descriptor, property)

def test_uma_section_has_variabilityBasedOnElement():
    assert hasattr(uma_Section, "variabilityBasedOnElement")
    descriptor = None
    for klass in uma_Section.__mro__:
        if "variabilityBasedOnElement" in klass.__dict__:
            descriptor = klass.__dict__["variabilityBasedOnElement"]
            break
    assert isinstance(descriptor, property)

def test_uma_section_has_predecessor():
    assert hasattr(uma_Section, "predecessor")
    descriptor = None
    for klass in uma_Section.__mro__:
        if "predecessor" in klass.__dict__:
            descriptor = klass.__dict__["predecessor"]
            break
    assert isinstance(descriptor, property)

def test_uma_section_has_description():
    assert hasattr(uma_Section, "description")
    descriptor = None
    for klass in uma_Section.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_uma_workdefinition_is_not_abstract():
    assert not inspect.isabstract(uma_WorkDefinition)


def test_uma_workdefinition_constructor_exists():
    assert callable(uma_WorkDefinition.__init__)


def test_uma_workdefinition_constructor_args():
    sig = inspect.signature(uma_WorkDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "postcondition" in params, "Missing parameter 'postcondition'"

def test_uma_workdefinition_has_precondition():
    assert hasattr(uma_WorkDefinition, "precondition")
    descriptor = None
    for klass in uma_WorkDefinition.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_uma_workdefinition_has_postcondition():
    assert hasattr(uma_WorkDefinition, "postcondition")
    descriptor = None
    for klass in uma_WorkDefinition.__mro__:
        if "postcondition" in klass.__dict__:
            descriptor = klass.__dict__["postcondition"]
            break
    assert isinstance(descriptor, property)



def test_uma_constraint_is_not_abstract():
    assert not inspect.isabstract(uma_Constraint)


def test_uma_constraint_constructor_exists():
    assert callable(uma_Constraint.__init__)


def test_uma_constraint_constructor_args():
    sig = inspect.signature(uma_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "mainDescription" in params, "Missing parameter 'mainDescription'"

def test_uma_constraint_has_mainDescription():
    assert hasattr(uma_Constraint, "mainDescription")
    descriptor = None
    for klass in uma_Constraint.__mro__:
        if "mainDescription" in klass.__dict__:
            descriptor = klass.__dict__["mainDescription"]
            break
    assert isinstance(descriptor, property)



def test_uma_role_is_not_abstract():
    assert not inspect.isabstract(uma_Role)


def test_uma_role_constructor_exists():
    assert callable(uma_Role.__init__)


def test_uma_role_constructor_args():
    sig = inspect.signature(uma_Role.__init__)
    params = list(sig.parameters.keys())
    assert "responsibleFor" in params, "Missing parameter 'responsibleFor'"
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma_role_has_responsibleFor():
    assert hasattr(uma_Role, "responsibleFor")
    descriptor = None
    for klass in uma_Role.__mro__:
        if "responsibleFor" in klass.__dict__:
            descriptor = klass.__dict__["responsibleFor"]
            break
    assert isinstance(descriptor, property)

def test_uma_role_has_group2():
    assert hasattr(uma_Role, "group2")
    descriptor = None
    for klass in uma_Role.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_roledescriptor_is_not_abstract():
    assert not inspect.isabstract(RoleDescriptor)


def test_roledescriptor_constructor_exists():
    assert callable(RoleDescriptor.__init__)


def test_roledescriptor_constructor_args():
    sig = inspect.signature(RoleDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_uma_compositerole_is_not_abstract():
    assert not inspect.isabstract(uma_CompositeRole)


def test_uma_compositerole_constructor_exists():
    assert callable(uma_CompositeRole.__init__)


def test_uma_compositerole_constructor_args():
    sig = inspect.signature(uma_CompositeRole.__init__)
    params = list(sig.parameters.keys())
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma_compositerole_has_group2():
    assert hasattr(uma_CompositeRole, "group2")
    descriptor = None
    for klass in uma_CompositeRole.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_guidance_is_not_abstract():
    assert not inspect.isabstract(Guidance)


def test_guidance_constructor_exists():
    assert callable(Guidance.__init__)


def test_guidance_constructor_args():
    sig = inspect.signature(Guidance.__init__)
    params = list(sig.parameters.keys())



def test_uma_estimatingmetric_is_not_abstract():
    assert not inspect.isabstract(uma_EstimatingMetric)


def test_uma_estimatingmetric_constructor_exists():
    assert callable(uma_EstimatingMetric.__init__)


def test_uma_estimatingmetric_constructor_args():
    sig = inspect.signature(uma_EstimatingMetric.__init__)
    params = list(sig.parameters.keys())



def test_uma_toolmentor_is_not_abstract():
    assert not inspect.isabstract(uma_ToolMentor)


def test_uma_toolmentor_constructor_exists():
    assert callable(uma_ToolMentor.__init__)


def test_uma_toolmentor_constructor_args():
    sig = inspect.signature(uma_ToolMentor.__init__)
    params = list(sig.parameters.keys())



def test_uma_concept_is_not_abstract():
    assert not inspect.isabstract(uma_Concept)


def test_uma_concept_constructor_exists():
    assert callable(uma_Concept.__init__)


def test_uma_concept_constructor_args():
    sig = inspect.signature(uma_Concept.__init__)
    params = list(sig.parameters.keys())



def test_uma_report_is_not_abstract():
    assert not inspect.isabstract(uma_Report)


def test_uma_report_constructor_exists():
    assert callable(uma_Report.__init__)


def test_uma_report_constructor_args():
    sig = inspect.signature(uma_Report.__init__)
    params = list(sig.parameters.keys())



def test_uma_estimate_is_not_abstract():
    assert not inspect.isabstract(uma_Estimate)


def test_uma_estimate_constructor_exists():
    assert callable(uma_Estimate.__init__)


def test_uma_estimate_constructor_args():
    sig = inspect.signature(uma_Estimate.__init__)
    params = list(sig.parameters.keys())
    assert "estimationMetric" in params, "Missing parameter 'estimationMetric'"
    assert "group2" in params, "Missing parameter 'group2'"
    assert "estimationConsiderations" in params, "Missing parameter 'estimationConsiderations'"

def test_uma_estimate_has_estimationMetric():
    assert hasattr(uma_Estimate, "estimationMetric")
    descriptor = None
    for klass in uma_Estimate.__mro__:
        if "estimationMetric" in klass.__dict__:
            descriptor = klass.__dict__["estimationMetric"]
            break
    assert isinstance(descriptor, property)

def test_uma_estimate_has_group2():
    assert hasattr(uma_Estimate, "group2")
    descriptor = None
    for klass in uma_Estimate.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)

def test_uma_estimate_has_estimationConsiderations():
    assert hasattr(uma_Estimate, "estimationConsiderations")
    descriptor = None
    for klass in uma_Estimate.__mro__:
        if "estimationConsiderations" in klass.__dict__:
            descriptor = klass.__dict__["estimationConsiderations"]
            break
    assert isinstance(descriptor, property)



def test_uma_practice_is_not_abstract():
    assert not inspect.isabstract(uma_Practice)


def test_uma_practice_constructor_exists():
    assert callable(uma_Practice.__init__)


def test_uma_practice_constructor_args():
    sig = inspect.signature(uma_Practice.__init__)
    params = list(sig.parameters.keys())
    assert "group2" in params, "Missing parameter 'group2'"
    assert "activityReference" in params, "Missing parameter 'activityReference'"
    assert "contentReference" in params, "Missing parameter 'contentReference'"

def test_uma_practice_has_group2():
    assert hasattr(uma_Practice, "group2")
    descriptor = None
    for klass in uma_Practice.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)

def test_uma_practice_has_activityReference():
    assert hasattr(uma_Practice, "activityReference")
    descriptor = None
    for klass in uma_Practice.__mro__:
        if "activityReference" in klass.__dict__:
            descriptor = klass.__dict__["activityReference"]
            break
    assert isinstance(descriptor, property)

def test_uma_practice_has_contentReference():
    assert hasattr(uma_Practice, "contentReference")
    descriptor = None
    for klass in uma_Practice.__mro__:
        if "contentReference" in klass.__dict__:
            descriptor = klass.__dict__["contentReference"]
            break
    assert isinstance(descriptor, property)



def test_uma_reusableasset_is_not_abstract():
    assert not inspect.isabstract(uma_ReusableAsset)


def test_uma_reusableasset_constructor_exists():
    assert callable(uma_ReusableAsset.__init__)


def test_uma_reusableasset_constructor_args():
    sig = inspect.signature(uma_ReusableAsset.__init__)
    params = list(sig.parameters.keys())



def test_uma_example_is_not_abstract():
    assert not inspect.isabstract(uma_Example)


def test_uma_example_constructor_exists():
    assert callable(uma_Example.__init__)


def test_uma_example_constructor_args():
    sig = inspect.signature(uma_Example.__init__)
    params = list(sig.parameters.keys())



def test_uma_template_is_not_abstract():
    assert not inspect.isabstract(uma_Template)


def test_uma_template_constructor_exists():
    assert callable(uma_Template.__init__)


def test_uma_template_constructor_args():
    sig = inspect.signature(uma_Template.__init__)
    params = list(sig.parameters.keys())



def test_uma_guideline_is_not_abstract():
    assert not inspect.isabstract(uma_Guideline)


def test_uma_guideline_constructor_exists():
    assert callable(uma_Guideline.__init__)


def test_uma_guideline_constructor_args():
    sig = inspect.signature(uma_Guideline.__init__)
    params = list(sig.parameters.keys())



def test_uma_estimationconsiderations_is_not_abstract():
    assert not inspect.isabstract(uma_EstimationConsiderations)


def test_uma_estimationconsiderations_constructor_exists():
    assert callable(uma_EstimationConsiderations.__init__)


def test_uma_estimationconsiderations_constructor_args():
    sig = inspect.signature(uma_EstimationConsiderations.__init__)
    params = list(sig.parameters.keys())



def test_uma_supportingmaterial_is_not_abstract():
    assert not inspect.isabstract(uma_SupportingMaterial)


def test_uma_supportingmaterial_constructor_exists():
    assert callable(uma_SupportingMaterial.__init__)


def test_uma_supportingmaterial_constructor_args():
    sig = inspect.signature(uma_SupportingMaterial.__init__)
    params = list(sig.parameters.keys())



def test_uma_roadmap_is_not_abstract():
    assert not inspect.isabstract(uma_Roadmap)


def test_uma_roadmap_constructor_exists():
    assert callable(uma_Roadmap.__init__)


def test_uma_roadmap_constructor_args():
    sig = inspect.signature(uma_Roadmap.__init__)
    params = list(sig.parameters.keys())



def test_uma_termdefinition_is_not_abstract():
    assert not inspect.isabstract(uma_TermDefinition)


def test_uma_termdefinition_constructor_exists():
    assert callable(uma_TermDefinition.__init__)


def test_uma_termdefinition_constructor_args():
    sig = inspect.signature(uma_TermDefinition.__init__)
    params = list(sig.parameters.keys())



def test_uma_checklist_is_not_abstract():
    assert not inspect.isabstract(uma_Checklist)


def test_uma_checklist_constructor_exists():
    assert callable(uma_Checklist.__init__)


def test_uma_checklist_constructor_args():
    sig = inspect.signature(uma_Checklist.__init__)
    params = list(sig.parameters.keys())



def test_process_is_not_abstract():
    assert not inspect.isabstract(Process)


def test_process_constructor_exists():
    assert callable(Process.__init__)


def test_process_constructor_args():
    sig = inspect.signature(Process.__init__)
    params = list(sig.parameters.keys())



def test_uma_processplanningtemplate_is_not_abstract():
    assert not inspect.isabstract(uma_ProcessPlanningTemplate)


def test_uma_processplanningtemplate_constructor_exists():
    assert callable(uma_ProcessPlanningTemplate.__init__)


def test_uma_processplanningtemplate_constructor_args():
    sig = inspect.signature(uma_ProcessPlanningTemplate.__init__)
    params = list(sig.parameters.keys())
    assert "baseProcess" in params, "Missing parameter 'baseProcess'"
    assert "group4" in params, "Missing parameter 'group4'"

def test_uma_processplanningtemplate_has_baseProcess():
    assert hasattr(uma_ProcessPlanningTemplate, "baseProcess")
    descriptor = None
    for klass in uma_ProcessPlanningTemplate.__mro__:
        if "baseProcess" in klass.__dict__:
            descriptor = klass.__dict__["baseProcess"]
            break
    assert isinstance(descriptor, property)

def test_uma_processplanningtemplate_has_group4():
    assert hasattr(uma_ProcessPlanningTemplate, "group4")
    descriptor = None
    for klass in uma_ProcessPlanningTemplate.__mro__:
        if "group4" in klass.__dict__:
            descriptor = klass.__dict__["group4"]
            break
    assert isinstance(descriptor, property)



def test_uma_deliveryprocess_is_not_abstract():
    assert not inspect.isabstract(uma_DeliveryProcess)


def test_uma_deliveryprocess_constructor_exists():
    assert callable(uma_DeliveryProcess.__init__)


def test_uma_deliveryprocess_constructor_args():
    sig = inspect.signature(uma_DeliveryProcess.__init__)
    params = list(sig.parameters.keys())
    assert "group4" in params, "Missing parameter 'group4'"
    assert "communicationsMaterial" in params, "Missing parameter 'communicationsMaterial'"
    assert "educationMaterial" in params, "Missing parameter 'educationMaterial'"

def test_uma_deliveryprocess_has_group4():
    assert hasattr(uma_DeliveryProcess, "group4")
    descriptor = None
    for klass in uma_DeliveryProcess.__mro__:
        if "group4" in klass.__dict__:
            descriptor = klass.__dict__["group4"]
            break
    assert isinstance(descriptor, property)

def test_uma_deliveryprocess_has_communicationsMaterial():
    assert hasattr(uma_DeliveryProcess, "communicationsMaterial")
    descriptor = None
    for klass in uma_DeliveryProcess.__mro__:
        if "communicationsMaterial" in klass.__dict__:
            descriptor = klass.__dict__["communicationsMaterial"]
            break
    assert isinstance(descriptor, property)

def test_uma_deliveryprocess_has_educationMaterial():
    assert hasattr(uma_DeliveryProcess, "educationMaterial")
    descriptor = None
    for klass in uma_DeliveryProcess.__mro__:
        if "educationMaterial" in klass.__dict__:
            descriptor = klass.__dict__["educationMaterial"]
            break
    assert isinstance(descriptor, property)



def test_uma_capabilitypattern_is_not_abstract():
    assert not inspect.isabstract(uma_CapabilityPattern)


def test_uma_capabilitypattern_constructor_exists():
    assert callable(uma_CapabilityPattern.__init__)


def test_uma_capabilitypattern_constructor_args():
    sig = inspect.signature(uma_CapabilityPattern.__init__)
    params = list(sig.parameters.keys())



def test_contentdescription_is_not_abstract():
    assert not inspect.isabstract(ContentDescription)


def test_contentdescription_constructor_exists():
    assert callable(ContentDescription.__init__)


def test_contentdescription_constructor_args():
    sig = inspect.signature(ContentDescription.__init__)
    params = list(sig.parameters.keys())



def test_uma_roledescription_is_not_abstract():
    assert not inspect.isabstract(uma_RoleDescription)


def test_uma_roledescription_constructor_exists():
    assert callable(uma_RoleDescription.__init__)


def test_uma_roledescription_constructor_args():
    sig = inspect.signature(uma_RoleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "synonyms" in params, "Missing parameter 'synonyms'"
    assert "skills" in params, "Missing parameter 'skills'"
    assert "assignmentApproaches" in params, "Missing parameter 'assignmentApproaches'"

def test_uma_roledescription_has_synonyms():
    assert hasattr(uma_RoleDescription, "synonyms")
    descriptor = None
    for klass in uma_RoleDescription.__mro__:
        if "synonyms" in klass.__dict__:
            descriptor = klass.__dict__["synonyms"]
            break
    assert isinstance(descriptor, property)

def test_uma_roledescription_has_skills():
    assert hasattr(uma_RoleDescription, "skills")
    descriptor = None
    for klass in uma_RoleDescription.__mro__:
        if "skills" in klass.__dict__:
            descriptor = klass.__dict__["skills"]
            break
    assert isinstance(descriptor, property)

def test_uma_roledescription_has_assignmentApproaches():
    assert hasattr(uma_RoleDescription, "assignmentApproaches")
    descriptor = None
    for klass in uma_RoleDescription.__mro__:
        if "assignmentApproaches" in klass.__dict__:
            descriptor = klass.__dict__["assignmentApproaches"]
            break
    assert isinstance(descriptor, property)



def test_uma_taskdescription_is_not_abstract():
    assert not inspect.isabstract(uma_TaskDescription)


def test_uma_taskdescription_constructor_exists():
    assert callable(uma_TaskDescription.__init__)


def test_uma_taskdescription_constructor_args():
    sig = inspect.signature(uma_TaskDescription.__init__)
    params = list(sig.parameters.keys())
    assert "purpose" in params, "Missing parameter 'purpose'"
    assert "alternatives" in params, "Missing parameter 'alternatives'"

def test_uma_taskdescription_has_purpose():
    assert hasattr(uma_TaskDescription, "purpose")
    descriptor = None
    for klass in uma_TaskDescription.__mro__:
        if "purpose" in klass.__dict__:
            descriptor = klass.__dict__["purpose"]
            break
    assert isinstance(descriptor, property)

def test_uma_taskdescription_has_alternatives():
    assert hasattr(uma_TaskDescription, "alternatives")
    descriptor = None
    for klass in uma_TaskDescription.__mro__:
        if "alternatives" in klass.__dict__:
            descriptor = klass.__dict__["alternatives"]
            break
    assert isinstance(descriptor, property)



def test_uma_workproductdescription_is_not_abstract():
    assert not inspect.isabstract(uma_WorkProductDescription)


def test_uma_workproductdescription_constructor_exists():
    assert callable(uma_WorkProductDescription.__init__)


def test_uma_workproductdescription_constructor_args():
    sig = inspect.signature(uma_WorkProductDescription.__init__)
    params = list(sig.parameters.keys())
    assert "impactOfNotHaving" in params, "Missing parameter 'impactOfNotHaving'"
    assert "reasonsForNotNeeding" in params, "Missing parameter 'reasonsForNotNeeding'"
    assert "purpose" in params, "Missing parameter 'purpose'"

def test_uma_workproductdescription_has_impactOfNotHaving():
    assert hasattr(uma_WorkProductDescription, "impactOfNotHaving")
    descriptor = None
    for klass in uma_WorkProductDescription.__mro__:
        if "impactOfNotHaving" in klass.__dict__:
            descriptor = klass.__dict__["impactOfNotHaving"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproductdescription_has_reasonsForNotNeeding():
    assert hasattr(uma_WorkProductDescription, "reasonsForNotNeeding")
    descriptor = None
    for klass in uma_WorkProductDescription.__mro__:
        if "reasonsForNotNeeding" in klass.__dict__:
            descriptor = klass.__dict__["reasonsForNotNeeding"]
            break
    assert isinstance(descriptor, property)

def test_uma_workproductdescription_has_purpose():
    assert hasattr(uma_WorkProductDescription, "purpose")
    descriptor = None
    for klass in uma_WorkProductDescription.__mro__:
        if "purpose" in klass.__dict__:
            descriptor = klass.__dict__["purpose"]
            break
    assert isinstance(descriptor, property)



def test_uma_practicedescription_is_not_abstract():
    assert not inspect.isabstract(uma_PracticeDescription)


def test_uma_practicedescription_constructor_exists():
    assert callable(uma_PracticeDescription.__init__)


def test_uma_practicedescription_constructor_args():
    sig = inspect.signature(uma_PracticeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "levelsOfAdoption" in params, "Missing parameter 'levelsOfAdoption'"
    assert "problem" in params, "Missing parameter 'problem'"
    assert "application" in params, "Missing parameter 'application'"
    assert "additionalInfo" in params, "Missing parameter 'additionalInfo'"
    assert "background" in params, "Missing parameter 'background'"
    assert "goals" in params, "Missing parameter 'goals'"

def test_uma_practicedescription_has_levelsOfAdoption():
    assert hasattr(uma_PracticeDescription, "levelsOfAdoption")
    descriptor = None
    for klass in uma_PracticeDescription.__mro__:
        if "levelsOfAdoption" in klass.__dict__:
            descriptor = klass.__dict__["levelsOfAdoption"]
            break
    assert isinstance(descriptor, property)

def test_uma_practicedescription_has_problem():
    assert hasattr(uma_PracticeDescription, "problem")
    descriptor = None
    for klass in uma_PracticeDescription.__mro__:
        if "problem" in klass.__dict__:
            descriptor = klass.__dict__["problem"]
            break
    assert isinstance(descriptor, property)

def test_uma_practicedescription_has_application():
    assert hasattr(uma_PracticeDescription, "application")
    descriptor = None
    for klass in uma_PracticeDescription.__mro__:
        if "application" in klass.__dict__:
            descriptor = klass.__dict__["application"]
            break
    assert isinstance(descriptor, property)

def test_uma_practicedescription_has_additionalInfo():
    assert hasattr(uma_PracticeDescription, "additionalInfo")
    descriptor = None
    for klass in uma_PracticeDescription.__mro__:
        if "additionalInfo" in klass.__dict__:
            descriptor = klass.__dict__["additionalInfo"]
            break
    assert isinstance(descriptor, property)

def test_uma_practicedescription_has_background():
    assert hasattr(uma_PracticeDescription, "background")
    descriptor = None
    for klass in uma_PracticeDescription.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_uma_practicedescription_has_goals():
    assert hasattr(uma_PracticeDescription, "goals")
    descriptor = None
    for klass in uma_PracticeDescription.__mro__:
        if "goals" in klass.__dict__:
            descriptor = klass.__dict__["goals"]
            break
    assert isinstance(descriptor, property)



def test_uma_guidancedescription_is_not_abstract():
    assert not inspect.isabstract(uma_GuidanceDescription)


def test_uma_guidancedescription_constructor_exists():
    assert callable(uma_GuidanceDescription.__init__)


def test_uma_guidancedescription_constructor_args():
    sig = inspect.signature(uma_GuidanceDescription.__init__)
    params = list(sig.parameters.keys())
    assert "attachment" in params, "Missing parameter 'attachment'"

def test_uma_guidancedescription_has_attachment():
    assert hasattr(uma_GuidanceDescription, "attachment")
    descriptor = None
    for klass in uma_GuidanceDescription.__mro__:
        if "attachment" in klass.__dict__:
            descriptor = klass.__dict__["attachment"]
            break
    assert isinstance(descriptor, property)



def test_uma_breakdownelementdescription_is_not_abstract():
    assert not inspect.isabstract(uma_BreakdownElementDescription)


def test_uma_breakdownelementdescription_constructor_exists():
    assert callable(uma_BreakdownElementDescription.__init__)


def test_uma_breakdownelementdescription_constructor_args():
    sig = inspect.signature(uma_BreakdownElementDescription.__init__)
    params = list(sig.parameters.keys())
    assert "usageGuidance" in params, "Missing parameter 'usageGuidance'"

def test_uma_breakdownelementdescription_has_usageGuidance():
    assert hasattr(uma_BreakdownElementDescription, "usageGuidance")
    descriptor = None
    for klass in uma_BreakdownElementDescription.__mro__:
        if "usageGuidance" in klass.__dict__:
            descriptor = klass.__dict__["usageGuidance"]
            break
    assert isinstance(descriptor, property)



def test_processelement_is_not_abstract():
    assert not inspect.isabstract(ProcessElement)


def test_processelement_constructor_exists():
    assert callable(ProcessElement.__init__)


def test_processelement_constructor_args():
    sig = inspect.signature(ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_planningdata_is_not_abstract():
    assert not inspect.isabstract(uma_PlanningData)


def test_uma_planningdata_constructor_exists():
    assert callable(uma_PlanningData.__init__)


def test_uma_planningdata_constructor_args():
    sig = inspect.signature(uma_PlanningData.__init__)
    params = list(sig.parameters.keys())
    assert "finishDate" in params, "Missing parameter 'finishDate'"
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "rank" in params, "Missing parameter 'rank'"

def test_uma_planningdata_has_finishDate():
    assert hasattr(uma_PlanningData, "finishDate")
    descriptor = None
    for klass in uma_PlanningData.__mro__:
        if "finishDate" in klass.__dict__:
            descriptor = klass.__dict__["finishDate"]
            break
    assert isinstance(descriptor, property)

def test_uma_planningdata_has_startDate():
    assert hasattr(uma_PlanningData, "startDate")
    descriptor = None
    for klass in uma_PlanningData.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_uma_planningdata_has_rank():
    assert hasattr(uma_PlanningData, "rank")
    descriptor = None
    for klass in uma_PlanningData.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)



def test_uma_breakdownelement_is_not_abstract():
    assert not inspect.isabstract(uma_BreakdownElement)


def test_uma_breakdownelement_constructor_exists():
    assert callable(uma_BreakdownElement.__init__)


def test_uma_breakdownelement_constructor_args():
    sig = inspect.signature(uma_BreakdownElement.__init__)
    params = list(sig.parameters.keys())
    assert "hasMultipleOccurrences" in params, "Missing parameter 'hasMultipleOccurrences'"
    assert "group1" in params, "Missing parameter 'group1'"
    assert "whitepaper" in params, "Missing parameter 'whitepaper'"
    assert "example" in params, "Missing parameter 'example'"
    assert "presentedBefore" in params, "Missing parameter 'presentedBefore'"
    assert "superActivity" in params, "Missing parameter 'superActivity'"
    assert "concept" in params, "Missing parameter 'concept'"
    assert "presentedAfter" in params, "Missing parameter 'presentedAfter'"
    assert "guideline" in params, "Missing parameter 'guideline'"
    assert "prefix" in params, "Missing parameter 'prefix'"
    assert "isOptional" in params, "Missing parameter 'isOptional'"
    assert "isPlanned" in params, "Missing parameter 'isPlanned'"
    assert "reusableAsset" in params, "Missing parameter 'reusableAsset'"
    assert "supportingMaterial" in params, "Missing parameter 'supportingMaterial'"
    assert "planningData" in params, "Missing parameter 'planningData'"
    assert "checklist" in params, "Missing parameter 'checklist'"

def test_uma_breakdownelement_has_hasMultipleOccurrences():
    assert hasattr(uma_BreakdownElement, "hasMultipleOccurrences")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "hasMultipleOccurrences" in klass.__dict__:
            descriptor = klass.__dict__["hasMultipleOccurrences"]
            break
    assert isinstance(descriptor, property)

def test_uma_breakdownelement_has_group1():
    assert hasattr(uma_BreakdownElement, "group1")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "group1" in klass.__dict__:
            descriptor = klass.__dict__["group1"]
            break
    assert isinstance(descriptor, property)

def test_uma_breakdownelement_has_whitepaper():
    assert hasattr(uma_BreakdownElement, "whitepaper")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "whitepaper" in klass.__dict__:
            descriptor = klass.__dict__["whitepaper"]
            break
    assert isinstance(descriptor, property)

def test_uma_breakdownelement_has_example():
    assert hasattr(uma_BreakdownElement, "example")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "example" in klass.__dict__:
            descriptor = klass.__dict__["example"]
            break
    assert isinstance(descriptor, property)

def test_uma_breakdownelement_has_presentedBefore():
    assert hasattr(uma_BreakdownElement, "presentedBefore")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "presentedBefore" in klass.__dict__:
            descriptor = klass.__dict__["presentedBefore"]
            break
    assert isinstance(descriptor, property)

def test_uma_breakdownelement_has_superActivity():
    assert hasattr(uma_BreakdownElement, "superActivity")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "superActivity" in klass.__dict__:
            descriptor = klass.__dict__["superActivity"]
            break
    assert isinstance(descriptor, property)

def test_uma_breakdownelement_has_concept():
    assert hasattr(uma_BreakdownElement, "concept")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "concept" in klass.__dict__:
            descriptor = klass.__dict__["concept"]
            break
    assert isinstance(descriptor, property)

def test_uma_breakdownelement_has_presentedAfter():
    assert hasattr(uma_BreakdownElement, "presentedAfter")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "presentedAfter" in klass.__dict__:
            descriptor = klass.__dict__["presentedAfter"]
            break
    assert isinstance(descriptor, property)

def test_uma_breakdownelement_has_guideline():
    assert hasattr(uma_BreakdownElement, "guideline")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "guideline" in klass.__dict__:
            descriptor = klass.__dict__["guideline"]
            break
    assert isinstance(descriptor, property)

def test_uma_breakdownelement_has_prefix():
    assert hasattr(uma_BreakdownElement, "prefix")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)

def test_uma_breakdownelement_has_isOptional():
    assert hasattr(uma_BreakdownElement, "isOptional")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)

def test_uma_breakdownelement_has_isPlanned():
    assert hasattr(uma_BreakdownElement, "isPlanned")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "isPlanned" in klass.__dict__:
            descriptor = klass.__dict__["isPlanned"]
            break
    assert isinstance(descriptor, property)

def test_uma_breakdownelement_has_reusableAsset():
    assert hasattr(uma_BreakdownElement, "reusableAsset")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "reusableAsset" in klass.__dict__:
            descriptor = klass.__dict__["reusableAsset"]
            break
    assert isinstance(descriptor, property)

def test_uma_breakdownelement_has_supportingMaterial():
    assert hasattr(uma_BreakdownElement, "supportingMaterial")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "supportingMaterial" in klass.__dict__:
            descriptor = klass.__dict__["supportingMaterial"]
            break
    assert isinstance(descriptor, property)

def test_uma_breakdownelement_has_planningData():
    assert hasattr(uma_BreakdownElement, "planningData")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "planningData" in klass.__dict__:
            descriptor = klass.__dict__["planningData"]
            break
    assert isinstance(descriptor, property)

def test_uma_breakdownelement_has_checklist():
    assert hasattr(uma_BreakdownElement, "checklist")
    descriptor = None
    for klass in uma_BreakdownElement.__mro__:
        if "checklist" in klass.__dict__:
            descriptor = klass.__dict__["checklist"]
            break
    assert isinstance(descriptor, property)



def test_workproductdescription_is_not_abstract():
    assert not inspect.isabstract(WorkProductDescription)


def test_workproductdescription_constructor_exists():
    assert callable(WorkProductDescription.__init__)


def test_workproductdescription_constructor_args():
    sig = inspect.signature(WorkProductDescription.__init__)
    params = list(sig.parameters.keys())



def test_uma_deliverabledescription_is_not_abstract():
    assert not inspect.isabstract(uma_DeliverableDescription)


def test_uma_deliverabledescription_constructor_exists():
    assert callable(uma_DeliverableDescription.__init__)


def test_uma_deliverabledescription_constructor_args():
    sig = inspect.signature(uma_DeliverableDescription.__init__)
    params = list(sig.parameters.keys())
    assert "externalDescription" in params, "Missing parameter 'externalDescription'"
    assert "packagingGuidance" in params, "Missing parameter 'packagingGuidance'"

def test_uma_deliverabledescription_has_externalDescription():
    assert hasattr(uma_DeliverableDescription, "externalDescription")
    descriptor = None
    for klass in uma_DeliverableDescription.__mro__:
        if "externalDescription" in klass.__dict__:
            descriptor = klass.__dict__["externalDescription"]
            break
    assert isinstance(descriptor, property)

def test_uma_deliverabledescription_has_packagingGuidance():
    assert hasattr(uma_DeliverableDescription, "packagingGuidance")
    descriptor = None
    for klass in uma_DeliverableDescription.__mro__:
        if "packagingGuidance" in klass.__dict__:
            descriptor = klass.__dict__["packagingGuidance"]
            break
    assert isinstance(descriptor, property)



def test_uma_artifactdescription_is_not_abstract():
    assert not inspect.isabstract(uma_ArtifactDescription)


def test_uma_artifactdescription_constructor_exists():
    assert callable(uma_ArtifactDescription.__init__)


def test_uma_artifactdescription_constructor_args():
    sig = inspect.signature(uma_ArtifactDescription.__init__)
    params = list(sig.parameters.keys())
    assert "briefOutline" in params, "Missing parameter 'briefOutline'"
    assert "representation" in params, "Missing parameter 'representation'"
    assert "representationOptions" in params, "Missing parameter 'representationOptions'"
    assert "notation" in params, "Missing parameter 'notation'"

def test_uma_artifactdescription_has_briefOutline():
    assert hasattr(uma_ArtifactDescription, "briefOutline")
    descriptor = None
    for klass in uma_ArtifactDescription.__mro__:
        if "briefOutline" in klass.__dict__:
            descriptor = klass.__dict__["briefOutline"]
            break
    assert isinstance(descriptor, property)

def test_uma_artifactdescription_has_representation():
    assert hasattr(uma_ArtifactDescription, "representation")
    descriptor = None
    for klass in uma_ArtifactDescription.__mro__:
        if "representation" in klass.__dict__:
            descriptor = klass.__dict__["representation"]
            break
    assert isinstance(descriptor, property)

def test_uma_artifactdescription_has_representationOptions():
    assert hasattr(uma_ArtifactDescription, "representationOptions")
    descriptor = None
    for klass in uma_ArtifactDescription.__mro__:
        if "representationOptions" in klass.__dict__:
            descriptor = klass.__dict__["representationOptions"]
            break
    assert isinstance(descriptor, property)

def test_uma_artifactdescription_has_notation():
    assert hasattr(uma_ArtifactDescription, "notation")
    descriptor = None
    for klass in uma_ArtifactDescription.__mro__:
        if "notation" in klass.__dict__:
            descriptor = klass.__dict__["notation"]
            break
    assert isinstance(descriptor, property)



def test_workproduct_is_not_abstract():
    assert not inspect.isabstract(WorkProduct)


def test_workproduct_constructor_exists():
    assert callable(WorkProduct.__init__)


def test_workproduct_constructor_args():
    sig = inspect.signature(WorkProduct.__init__)
    params = list(sig.parameters.keys())



def test_uma_outcome_is_not_abstract():
    assert not inspect.isabstract(uma_Outcome)


def test_uma_outcome_constructor_exists():
    assert callable(uma_Outcome.__init__)


def test_uma_outcome_constructor_args():
    sig = inspect.signature(uma_Outcome.__init__)
    params = list(sig.parameters.keys())



def test_uma_deliverable_is_not_abstract():
    assert not inspect.isabstract(uma_Deliverable)


def test_uma_deliverable_constructor_exists():
    assert callable(uma_Deliverable.__init__)


def test_uma_deliverable_constructor_args():
    sig = inspect.signature(uma_Deliverable.__init__)
    params = list(sig.parameters.keys())
    assert "group3" in params, "Missing parameter 'group3'"
    assert "deliveredWorkProduct" in params, "Missing parameter 'deliveredWorkProduct'"

def test_uma_deliverable_has_group3():
    assert hasattr(uma_Deliverable, "group3")
    descriptor = None
    for klass in uma_Deliverable.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)

def test_uma_deliverable_has_deliveredWorkProduct():
    assert hasattr(uma_Deliverable, "deliveredWorkProduct")
    descriptor = None
    for klass in uma_Deliverable.__mro__:
        if "deliveredWorkProduct" in klass.__dict__:
            descriptor = klass.__dict__["deliveredWorkProduct"]
            break
    assert isinstance(descriptor, property)



def test_uma_artifact_is_not_abstract():
    assert not inspect.isabstract(uma_Artifact)


def test_uma_artifact_constructor_exists():
    assert callable(uma_Artifact.__init__)


def test_uma_artifact_constructor_args():
    sig = inspect.signature(uma_Artifact.__init__)
    params = list(sig.parameters.keys())
    assert "group3" in params, "Missing parameter 'group3'"

def test_uma_artifact_has_group3():
    assert hasattr(uma_Artifact, "group3")
    descriptor = None
    for klass in uma_Artifact.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_methodelement_is_not_abstract():
    assert not inspect.isabstract(uma_MethodElement)


def test_uma_methodelement_constructor_exists():
    assert callable(uma_MethodElement.__init__)


def test_uma_methodelement_constructor_args():
    sig = inspect.signature(uma_MethodElement.__init__)
    params = list(sig.parameters.keys())
    assert "presentationName" in params, "Missing parameter 'presentationName'"
    assert "id" in params, "Missing parameter 'id'"
    assert "group" in params, "Missing parameter 'group'"
    assert "briefDescription" in params, "Missing parameter 'briefDescription'"
    assert "orderingGuide" in params, "Missing parameter 'orderingGuide'"
    assert "suppressed" in params, "Missing parameter 'suppressed'"

def test_uma_methodelement_has_presentationName():
    assert hasattr(uma_MethodElement, "presentationName")
    descriptor = None
    for klass in uma_MethodElement.__mro__:
        if "presentationName" in klass.__dict__:
            descriptor = klass.__dict__["presentationName"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodelement_has_id():
    assert hasattr(uma_MethodElement, "id")
    descriptor = None
    for klass in uma_MethodElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodelement_has_group():
    assert hasattr(uma_MethodElement, "group")
    descriptor = None
    for klass in uma_MethodElement.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodelement_has_briefDescription():
    assert hasattr(uma_MethodElement, "briefDescription")
    descriptor = None
    for klass in uma_MethodElement.__mro__:
        if "briefDescription" in klass.__dict__:
            descriptor = klass.__dict__["briefDescription"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodelement_has_orderingGuide():
    assert hasattr(uma_MethodElement, "orderingGuide")
    descriptor = None
    for klass in uma_MethodElement.__mro__:
        if "orderingGuide" in klass.__dict__:
            descriptor = klass.__dict__["orderingGuide"]
            break
    assert isinstance(descriptor, property)

def test_uma_methodelement_has_suppressed():
    assert hasattr(uma_MethodElement, "suppressed")
    descriptor = None
    for klass in uma_MethodElement.__mro__:
        if "suppressed" in klass.__dict__:
            descriptor = klass.__dict__["suppressed"]
            break
    assert isinstance(descriptor, property)



def test_uma_methodelementproperty_is_not_abstract():
    assert not inspect.isabstract(uma_MethodElementProperty)


def test_uma_methodelementproperty_constructor_exists():
    assert callable(uma_MethodElementProperty.__init__)


def test_uma_methodelementproperty_constructor_args():
    sig = inspect.signature(uma_MethodElementProperty.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uma_methodelementproperty_has_value():
    assert hasattr(uma_MethodElementProperty, "value")
    descriptor = None
    for klass in uma_MethodElementProperty.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uma_applicablemetaclassinfo_is_not_abstract():
    assert not inspect.isabstract(uma_ApplicableMetaClassInfo)


def test_uma_applicablemetaclassinfo_constructor_exists():
    assert callable(uma_ApplicableMetaClassInfo.__init__)


def test_uma_applicablemetaclassinfo_constructor_args():
    sig = inspect.signature(uma_ApplicableMetaClassInfo.__init__)
    params = list(sig.parameters.keys())
    assert "isPrimaryExtension" in params, "Missing parameter 'isPrimaryExtension'"

def test_uma_applicablemetaclassinfo_has_isPrimaryExtension():
    assert hasattr(uma_ApplicableMetaClassInfo, "isPrimaryExtension")
    descriptor = None
    for klass in uma_ApplicableMetaClassInfo.__mro__:
        if "isPrimaryExtension" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryExtension"]
            break
    assert isinstance(descriptor, property)



def test_breakdownelementdescription_is_not_abstract():
    assert not inspect.isabstract(BreakdownElementDescription)


def test_breakdownelementdescription_constructor_exists():
    assert callable(BreakdownElementDescription.__init__)


def test_breakdownelementdescription_constructor_args():
    sig = inspect.signature(BreakdownElementDescription.__init__)
    params = list(sig.parameters.keys())



def test_uma_descriptordescription_is_not_abstract():
    assert not inspect.isabstract(uma_DescriptorDescription)


def test_uma_descriptordescription_constructor_exists():
    assert callable(uma_DescriptorDescription.__init__)


def test_uma_descriptordescription_constructor_args():
    sig = inspect.signature(uma_DescriptorDescription.__init__)
    params = list(sig.parameters.keys())
    assert "refinedDescription" in params, "Missing parameter 'refinedDescription'"

def test_uma_descriptordescription_has_refinedDescription():
    assert hasattr(uma_DescriptorDescription, "refinedDescription")
    descriptor = None
    for klass in uma_DescriptorDescription.__mro__:
        if "refinedDescription" in klass.__dict__:
            descriptor = klass.__dict__["refinedDescription"]
            break
    assert isinstance(descriptor, property)



def test_uma_activitydescription_is_not_abstract():
    assert not inspect.isabstract(uma_ActivityDescription)


def test_uma_activitydescription_constructor_exists():
    assert callable(uma_ActivityDescription.__init__)


def test_uma_activitydescription_constructor_args():
    sig = inspect.signature(uma_ActivityDescription.__init__)
    params = list(sig.parameters.keys())
    assert "alternatives" in params, "Missing parameter 'alternatives'"
    assert "purpose" in params, "Missing parameter 'purpose'"
    assert "howToStaff" in params, "Missing parameter 'howToStaff'"

def test_uma_activitydescription_has_alternatives():
    assert hasattr(uma_ActivityDescription, "alternatives")
    descriptor = None
    for klass in uma_ActivityDescription.__mro__:
        if "alternatives" in klass.__dict__:
            descriptor = klass.__dict__["alternatives"]
            break
    assert isinstance(descriptor, property)

def test_uma_activitydescription_has_purpose():
    assert hasattr(uma_ActivityDescription, "purpose")
    descriptor = None
    for klass in uma_ActivityDescription.__mro__:
        if "purpose" in klass.__dict__:
            descriptor = klass.__dict__["purpose"]
            break
    assert isinstance(descriptor, property)

def test_uma_activitydescription_has_howToStaff():
    assert hasattr(uma_ActivityDescription, "howToStaff")
    descriptor = None
    for klass in uma_ActivityDescription.__mro__:
        if "howToStaff" in klass.__dict__:
            descriptor = klass.__dict__["howToStaff"]
            break
    assert isinstance(descriptor, property)

def test_workordertype_exists():
    # Check that the Enumeration exists
    assert WorkOrderType is not None

def test_workordertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkOrderType]
    expected_literals = [
        "startToFinish",
        "finishToFinish",
        "startToStart",
        "finishToStart",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WorkOrderType"

def test_variabilitytype_exists():
    # Check that the Enumeration exists
    assert VariabilityType is not None

def test_variabilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariabilityType]
    expected_literals = [
        "localReplacement",
        "replaces",
        "extendsReplaces",
        "na",
        "contributes",
        "extends",
        "localContribution",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VariabilityType"


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
ProcessPackage_strategy = st.builds(
    ProcessPackage,
)
uma_ProcessComponent_strategy = st.builds(
    uma_ProcessComponent,
    copyright=
        safe_text,
    changeDate=
        safe_text,
    changeDescription=
        safe_text,
    authors=
        safe_text,
    version=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uma_PackageableElement_strategy = st.builds(
    uma_PackageableElement,
)
uma_WorkOrder_strategy = st.builds(
    uma_WorkOrder,
    linkType=
        safe_text,
    properties=
        safe_text,
    value=
        safe_text,
    id=
        safe_text
)
Concept_strategy = st.builds(
    Concept,
)
uma_Whitepaper_strategy = st.builds(
    uma_Whitepaper,
)
Descriptor_strategy = st.builds(
    Descriptor,
)
uma_WorkProductDescriptor_strategy = st.builds(
    uma_WorkProductDescriptor,
    externalInputTo=
        safe_text,
    outputFrom=
        safe_text,
    deliverableParts=
        safe_text,
    activityEntryState=
        safe_text,
    optionalInputTo=
        safe_text,
    activityExitState=
        safe_text,
    impactedBy=
        safe_text,
    workProduct=
        safe_text,
    group2=
        safe_text,
    responsibleRole=
        safe_text,
    mandatoryInputTo=
        safe_text,
    impacts=
        safe_text
)
uma_RoleDescriptor_strategy = st.builds(
    uma_RoleDescriptor,
    role=
        safe_text,
    responsibleFor=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
uma_NamedElement_strategy = st.builds(
    uma_NamedElement,
    name=
        safe_text
)
ActivityDescription_strategy = st.builds(
    ActivityDescription,
)
uma_ProcessDescription_strategy = st.builds(
    uma_ProcessDescription,
    usageNotes=
        safe_text,
    scope=
        safe_text
)
Activity_strategy = st.builds(
    Activity,
)
uma_Phase_strategy = st.builds(
    uma_Phase,
)
uma_Process_strategy = st.builds(
    uma_Process,
    includesPattern=
        safe_text,
    diagramURI=
        safe_text,
    defaultContext=
        safe_text,
    validContext=
        safe_text
)
uma_Iteration_strategy = st.builds(
    uma_Iteration,
)
uma_Element_strategy = st.builds(
    uma_Element,
)
uma_EStringToStringMapEntry_strategy = st.builds(
    uma_EStringToStringMapEntry,
)
uma_DocumentRoot_strategy = st.builds(
    uma_DocumentRoot,
    mixed=
        safe_text
)
BreakdownElement_strategy = st.builds(
    BreakdownElement,
)
uma_ProcessComponentInterface_strategy = st.builds(
    uma_ProcessComponentInterface,
    group2=
        safe_text
)
uma_WorkBreakdownElement_strategy = st.builds(
    uma_WorkBreakdownElement,
    isRepeatable=
        safe_text,
    group2=
        safe_text,
    isEventDriven=
        safe_text,
    isOngoing=
        safe_text
)
uma_TeamProfile_strategy = st.builds(
    uma_TeamProfile,
    group2=
        safe_text,
    superTeam=
        safe_text,
    subTeam=
        safe_text,
    role=
        safe_text
)
uma_Descriptor_strategy = st.builds(
    uma_Descriptor,
    isSynchronizedWithSource=
        safe_text
)
ProcessDescription_strategy = st.builds(
    ProcessDescription,
)
uma_DeliveryProcessDescription_strategy = st.builds(
    uma_DeliveryProcessDescription,
    projectMemberExpertise=
        safe_text,
    estimatingTechnique=
        safe_text,
    projectCharacteristics=
        safe_text,
    riskLevel=
        safe_text,
    scale=
        safe_text,
    typeOfContract=
        safe_text
)
ContentCategory_strategy = st.builds(
    ContentCategory,
)
uma_Tool_strategy = st.builds(
    uma_Tool,
    toolMentor=
        safe_text,
    group2=
        safe_text
)
uma_WorkProductType_strategy = st.builds(
    uma_WorkProductType,
    group2=
        safe_text,
    workProduct=
        safe_text
)
uma_DisciplineGrouping_strategy = st.builds(
    uma_DisciplineGrouping,
    discipline=
        safe_text,
    group2=
        safe_text
)
uma_Discipline_strategy = st.builds(
    uma_Discipline,
    referenceWorkflow=
        safe_text,
    group2=
        safe_text,
    task=
        safe_text
)
uma_RoleSetGrouping_strategy = st.builds(
    uma_RoleSetGrouping,
    roleSet=
        safe_text,
    group2=
        safe_text
)
uma_Domain_strategy = st.builds(
    uma_Domain,
    workProduct=
        safe_text,
    group2=
        safe_text
)
uma_RoleSet_strategy = st.builds(
    uma_RoleSet,
    role=
        safe_text,
    group2=
        safe_text
)
uma_CustomCategory_strategy = st.builds(
    uma_CustomCategory,
    group2=
        safe_text,
    subCategory=
        safe_text,
    categorizedElement=
        safe_text
)
WorkBreakdownElement_strategy = st.builds(
    WorkBreakdownElement,
)
uma_Milestone_strategy = st.builds(
    uma_Milestone,
    requiredResult=
        safe_text
)
uma_TaskDescriptor_strategy = st.builds(
    uma_TaskDescriptor,
    isSynchronizedWithSource=
        safe_text,
    group3=
        safe_text,
    mandatoryInput=
        safe_text,
    output=
        safe_text,
    task=
        safe_text,
    optionalInput=
        safe_text,
    performedPrimarilyBy=
        safe_text,
    externalInput=
        safe_text,
    assistedBy=
        safe_text,
    additionallyPerformedBy=
        safe_text
)
uma_Activity_strategy = st.builds(
    uma_Activity,
    postcondition=
        safe_text,
    precondition=
        safe_text,
    variabilityBasedOnElement=
        safe_text,
    variabilityType=
        safe_text,
    roadmap=
        safe_text,
    group3=
        safe_text,
    isEnactable=
        safe_text
)
DescribableElement_strategy = st.builds(
    DescribableElement,
)
uma_ProcessElement_strategy = st.builds(
    uma_ProcessElement,
)
uma_ContentElement_strategy = st.builds(
    uma_ContentElement,
    concept=
        safe_text,
    whitepaper=
        safe_text,
    reusableAsset=
        safe_text,
    guideline=
        safe_text,
    example=
        safe_text,
    variabilityType=
        safe_text,
    group1=
        safe_text,
    checklist=
        safe_text,
    variabilityBasedOnElement=
        safe_text,
    supportingMaterial=
        safe_text
)
MethodUnit_strategy = st.builds(
    MethodUnit,
)
uma_MethodPlugin_strategy = st.builds(
    uma_MethodPlugin,
    referencedMethodPlugin=
        safe_text,
    userChangeable=
        safe_text,
    supporting=
        safe_text
)
uma_MethodLibrary_strategy = st.builds(
    uma_MethodLibrary,
    tool=
        safe_text
)
uma_MethodConfiguration_strategy = st.builds(
    uma_MethodConfiguration,
    subtractedCategory=
        safe_text,
    methodPackageSelection=
        safe_text,
    addedCategory=
        safe_text,
    methodPluginSelection=
        safe_text,
    baseConfiguration=
        safe_text,
    processView=
        safe_text,
    defaultView=
        safe_text
)
uma_ContentDescription_strategy = st.builds(
    uma_ContentDescription,
    keyConsiderations=
        safe_text,
    externalId=
        safe_text,
    mainDescription=
        safe_text
)
MethodPackage_strategy = st.builds(
    MethodPackage,
)
uma_ProcessPackage_strategy = st.builds(
    uma_ProcessPackage,
    group2=
        safe_text
)
uma_ContentPackage_strategy = st.builds(
    uma_ContentPackage,
    group2=
        safe_text
)
uma_ContentCategoryPackage_strategy = st.builds(
    uma_ContentCategoryPackage,
    group2=
        safe_text
)
ContentElement_strategy = st.builds(
    ContentElement,
)
uma_Kind_strategy = st.builds(
    uma_Kind,
    applicableMetaClassInfo=
        safe_text
)
uma_Guidance_strategy = st.builds(
    uma_Guidance,
)
uma_Task_strategy = st.builds(
    uma_Task,
    group2=
        safe_text,
    mandatoryInput=
        safe_text,
    postcondition=
        safe_text,
    optionalInput=
        safe_text,
    toolMentor=
        safe_text,
    precondition=
        safe_text,
    estimate=
        safe_text,
    estimationConsiderations=
        safe_text,
    performedBy=
        safe_text,
    additionallyPerformedBy=
        safe_text,
    output=
        safe_text
)
uma_WorkProduct_strategy = st.builds(
    uma_WorkProduct,
    toolMentor=
        safe_text,
    template=
        safe_text,
    group2=
        safe_text,
    report=
        safe_text,
    estimationConsiderations=
        safe_text,
    estimate=
        safe_text
)
uma_ContentCategory_strategy = st.builds(
    uma_ContentCategory,
)
MethodElement_strategy = st.builds(
    MethodElement,
)
uma_MethodPackage_strategy = st.builds(
    uma_MethodPackage,
    reusedPackage=
        safe_text,
    group1=
        safe_text,
    global_=
        safe_text
)
uma_MethodUnit_strategy = st.builds(
    uma_MethodUnit,
    version=
        safe_text,
    changeDate=
        safe_text,
    authors=
        safe_text,
    copyright=
        safe_text,
    changeDescription=
        safe_text
)
uma_DescribableElement_strategy = st.builds(
    uma_DescribableElement,
    nodeicon=
        safe_text,
    isAbstract=
        safe_text,
    fulfill=
        safe_text,
    shapeicon=
        safe_text
)
uma_Section_strategy = st.builds(
    uma_Section,
    variabilityType=
        safe_text,
    sectionName=
        safe_text,
    variabilityBasedOnElement=
        safe_text,
    predecessor=
        safe_text,
    description=
        safe_text
)
uma_WorkDefinition_strategy = st.builds(
    uma_WorkDefinition,
    precondition=
        safe_text,
    postcondition=
        safe_text
)
uma_Constraint_strategy = st.builds(
    uma_Constraint,
    mainDescription=
        safe_text
)
uma_Role_strategy = st.builds(
    uma_Role,
    responsibleFor=
        safe_text,
    group2=
        safe_text
)
RoleDescriptor_strategy = st.builds(
    RoleDescriptor,
)
uma_CompositeRole_strategy = st.builds(
    uma_CompositeRole,
    group2=
        safe_text
)
Guidance_strategy = st.builds(
    Guidance,
)
uma_EstimatingMetric_strategy = st.builds(
    uma_EstimatingMetric,
)
uma_ToolMentor_strategy = st.builds(
    uma_ToolMentor,
)
uma_Concept_strategy = st.builds(
    uma_Concept,
)
uma_Report_strategy = st.builds(
    uma_Report,
)
uma_Estimate_strategy = st.builds(
    uma_Estimate,
    estimationMetric=
        safe_text,
    group2=
        safe_text,
    estimationConsiderations=
        safe_text
)
uma_Practice_strategy = st.builds(
    uma_Practice,
    group2=
        safe_text,
    activityReference=
        safe_text,
    contentReference=
        safe_text
)
uma_ReusableAsset_strategy = st.builds(
    uma_ReusableAsset,
)
uma_Example_strategy = st.builds(
    uma_Example,
)
uma_Template_strategy = st.builds(
    uma_Template,
)
uma_Guideline_strategy = st.builds(
    uma_Guideline,
)
uma_EstimationConsiderations_strategy = st.builds(
    uma_EstimationConsiderations,
)
uma_SupportingMaterial_strategy = st.builds(
    uma_SupportingMaterial,
)
uma_Roadmap_strategy = st.builds(
    uma_Roadmap,
)
uma_TermDefinition_strategy = st.builds(
    uma_TermDefinition,
)
uma_Checklist_strategy = st.builds(
    uma_Checklist,
)
Process_strategy = st.builds(
    Process,
)
uma_ProcessPlanningTemplate_strategy = st.builds(
    uma_ProcessPlanningTemplate,
    baseProcess=
        safe_text,
    group4=
        safe_text
)
uma_DeliveryProcess_strategy = st.builds(
    uma_DeliveryProcess,
    group4=
        safe_text,
    communicationsMaterial=
        safe_text,
    educationMaterial=
        safe_text
)
uma_CapabilityPattern_strategy = st.builds(
    uma_CapabilityPattern,
)
ContentDescription_strategy = st.builds(
    ContentDescription,
)
uma_RoleDescription_strategy = st.builds(
    uma_RoleDescription,
    synonyms=
        safe_text,
    skills=
        safe_text,
    assignmentApproaches=
        safe_text
)
uma_TaskDescription_strategy = st.builds(
    uma_TaskDescription,
    purpose=
        safe_text,
    alternatives=
        safe_text
)
uma_WorkProductDescription_strategy = st.builds(
    uma_WorkProductDescription,
    impactOfNotHaving=
        safe_text,
    reasonsForNotNeeding=
        safe_text,
    purpose=
        safe_text
)
uma_PracticeDescription_strategy = st.builds(
    uma_PracticeDescription,
    levelsOfAdoption=
        safe_text,
    problem=
        safe_text,
    application=
        safe_text,
    additionalInfo=
        safe_text,
    background=
        safe_text,
    goals=
        safe_text
)
uma_GuidanceDescription_strategy = st.builds(
    uma_GuidanceDescription,
    attachment=
        safe_text
)
uma_BreakdownElementDescription_strategy = st.builds(
    uma_BreakdownElementDescription,
    usageGuidance=
        safe_text
)
ProcessElement_strategy = st.builds(
    ProcessElement,
)
uma_PlanningData_strategy = st.builds(
    uma_PlanningData,
    finishDate=
        safe_text,
    startDate=
        safe_text,
    rank=
        safe_text
)
uma_BreakdownElement_strategy = st.builds(
    uma_BreakdownElement,
    hasMultipleOccurrences=
        safe_text,
    group1=
        safe_text,
    whitepaper=
        safe_text,
    example=
        safe_text,
    presentedBefore=
        safe_text,
    superActivity=
        safe_text,
    concept=
        safe_text,
    presentedAfter=
        safe_text,
    guideline=
        safe_text,
    prefix=
        safe_text,
    isOptional=
        safe_text,
    isPlanned=
        safe_text,
    reusableAsset=
        safe_text,
    supportingMaterial=
        safe_text,
    planningData=
        safe_text,
    checklist=
        safe_text
)
WorkProductDescription_strategy = st.builds(
    WorkProductDescription,
)
uma_DeliverableDescription_strategy = st.builds(
    uma_DeliverableDescription,
    externalDescription=
        safe_text,
    packagingGuidance=
        safe_text
)
uma_ArtifactDescription_strategy = st.builds(
    uma_ArtifactDescription,
    briefOutline=
        safe_text,
    representation=
        safe_text,
    representationOptions=
        safe_text,
    notation=
        safe_text
)
WorkProduct_strategy = st.builds(
    WorkProduct,
)
uma_Outcome_strategy = st.builds(
    uma_Outcome,
)
uma_Deliverable_strategy = st.builds(
    uma_Deliverable,
    group3=
        safe_text,
    deliveredWorkProduct=
        safe_text
)
uma_Artifact_strategy = st.builds(
    uma_Artifact,
    group3=
        safe_text
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
uma_MethodElement_strategy = st.builds(
    uma_MethodElement,
    presentationName=
        safe_text,
    id=
        safe_text,
    group=
        safe_text,
    briefDescription=
        safe_text,
    orderingGuide=
        safe_text,
    suppressed=
        safe_text
)
uma_MethodElementProperty_strategy = st.builds(
    uma_MethodElementProperty,
    value=
        safe_text
)
uma_ApplicableMetaClassInfo_strategy = st.builds(
    uma_ApplicableMetaClassInfo,
    isPrimaryExtension=
        safe_text
)
BreakdownElementDescription_strategy = st.builds(
    BreakdownElementDescription,
)
uma_DescriptorDescription_strategy = st.builds(
    uma_DescriptorDescription,
    refinedDescription=
        safe_text
)
uma_ActivityDescription_strategy = st.builds(
    uma_ActivityDescription,
    alternatives=
        safe_text,
    purpose=
        safe_text,
    howToStaff=
        safe_text
)

@given(instance=ProcessPackage_strategy)
@settings(max_examples=50)
def test_processpackage_instantiation(instance):
    assert isinstance(instance, ProcessPackage)

@given(instance=uma_ProcessComponent_strategy)
@settings(max_examples=50)
def test_uma_processcomponent_instantiation(instance):
    assert isinstance(instance, uma_ProcessComponent)



@given(instance=uma_ProcessComponent_strategy)
def test_uma_processcomponent_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original



@given(instance=uma_ProcessComponent_strategy)
def test_uma_processcomponent_changeDate_setter(instance):
    original = instance.changeDate
    instance.changeDate = original
    assert instance.changeDate == original



@given(instance=uma_ProcessComponent_strategy)
def test_uma_processcomponent_changeDescription_setter(instance):
    original = instance.changeDescription
    instance.changeDescription = original
    assert instance.changeDescription == original



@given(instance=uma_ProcessComponent_strategy)
def test_uma_processcomponent_authors_setter(instance):
    original = instance.authors
    instance.authors = original
    assert instance.authors == original



@given(instance=uma_ProcessComponent_strategy)
def test_uma_processcomponent_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=uma_PackageableElement_strategy)
@settings(max_examples=50)
def test_uma_packageableelement_instantiation(instance):
    assert isinstance(instance, uma_PackageableElement)

@given(instance=uma_WorkOrder_strategy)
@settings(max_examples=50)
def test_uma_workorder_instantiation(instance):
    assert isinstance(instance, uma_WorkOrder)



@given(instance=uma_WorkOrder_strategy)
def test_uma_workorder_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original



@given(instance=uma_WorkOrder_strategy)
def test_uma_workorder_properties_setter(instance):
    original = instance.properties
    instance.properties = original
    assert instance.properties == original



@given(instance=uma_WorkOrder_strategy)
def test_uma_workorder_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=uma_WorkOrder_strategy)
def test_uma_workorder_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Concept_strategy)
@settings(max_examples=50)
def test_concept_instantiation(instance):
    assert isinstance(instance, Concept)

@given(instance=uma_Whitepaper_strategy)
@settings(max_examples=50)
def test_uma_whitepaper_instantiation(instance):
    assert isinstance(instance, uma_Whitepaper)

@given(instance=Descriptor_strategy)
@settings(max_examples=50)
def test_descriptor_instantiation(instance):
    assert isinstance(instance, Descriptor)

@given(instance=uma_WorkProductDescriptor_strategy)
@settings(max_examples=50)
def test_uma_workproductdescriptor_instantiation(instance):
    assert isinstance(instance, uma_WorkProductDescriptor)



@given(instance=uma_WorkProductDescriptor_strategy)
def test_uma_workproductdescriptor_externalInputTo_setter(instance):
    original = instance.externalInputTo
    instance.externalInputTo = original
    assert instance.externalInputTo == original



@given(instance=uma_WorkProductDescriptor_strategy)
def test_uma_workproductdescriptor_outputFrom_setter(instance):
    original = instance.outputFrom
    instance.outputFrom = original
    assert instance.outputFrom == original



@given(instance=uma_WorkProductDescriptor_strategy)
def test_uma_workproductdescriptor_deliverableParts_setter(instance):
    original = instance.deliverableParts
    instance.deliverableParts = original
    assert instance.deliverableParts == original



@given(instance=uma_WorkProductDescriptor_strategy)
def test_uma_workproductdescriptor_activityEntryState_setter(instance):
    original = instance.activityEntryState
    instance.activityEntryState = original
    assert instance.activityEntryState == original



@given(instance=uma_WorkProductDescriptor_strategy)
def test_uma_workproductdescriptor_optionalInputTo_setter(instance):
    original = instance.optionalInputTo
    instance.optionalInputTo = original
    assert instance.optionalInputTo == original



@given(instance=uma_WorkProductDescriptor_strategy)
def test_uma_workproductdescriptor_activityExitState_setter(instance):
    original = instance.activityExitState
    instance.activityExitState = original
    assert instance.activityExitState == original



@given(instance=uma_WorkProductDescriptor_strategy)
def test_uma_workproductdescriptor_impactedBy_setter(instance):
    original = instance.impactedBy
    instance.impactedBy = original
    assert instance.impactedBy == original



@given(instance=uma_WorkProductDescriptor_strategy)
def test_uma_workproductdescriptor_workProduct_setter(instance):
    original = instance.workProduct
    instance.workProduct = original
    assert instance.workProduct == original



@given(instance=uma_WorkProductDescriptor_strategy)
def test_uma_workproductdescriptor_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original



@given(instance=uma_WorkProductDescriptor_strategy)
def test_uma_workproductdescriptor_responsibleRole_setter(instance):
    original = instance.responsibleRole
    instance.responsibleRole = original
    assert instance.responsibleRole == original



@given(instance=uma_WorkProductDescriptor_strategy)
def test_uma_workproductdescriptor_mandatoryInputTo_setter(instance):
    original = instance.mandatoryInputTo
    instance.mandatoryInputTo = original
    assert instance.mandatoryInputTo == original



@given(instance=uma_WorkProductDescriptor_strategy)
def test_uma_workproductdescriptor_impacts_setter(instance):
    original = instance.impacts
    instance.impacts = original
    assert instance.impacts == original

@given(instance=uma_RoleDescriptor_strategy)
@settings(max_examples=50)
def test_uma_roledescriptor_instantiation(instance):
    assert isinstance(instance, uma_RoleDescriptor)



@given(instance=uma_RoleDescriptor_strategy)
def test_uma_roledescriptor_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original



@given(instance=uma_RoleDescriptor_strategy)
def test_uma_roledescriptor_responsibleFor_setter(instance):
    original = instance.responsibleFor
    instance.responsibleFor = original
    assert instance.responsibleFor == original

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=uma_NamedElement_strategy)
@settings(max_examples=50)
def test_uma_namedelement_instantiation(instance):
    assert isinstance(instance, uma_NamedElement)



@given(instance=uma_NamedElement_strategy)
def test_uma_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ActivityDescription_strategy)
@settings(max_examples=50)
def test_activitydescription_instantiation(instance):
    assert isinstance(instance, ActivityDescription)

@given(instance=uma_ProcessDescription_strategy)
@settings(max_examples=50)
def test_uma_processdescription_instantiation(instance):
    assert isinstance(instance, uma_ProcessDescription)



@given(instance=uma_ProcessDescription_strategy)
def test_uma_processdescription_usageNotes_setter(instance):
    original = instance.usageNotes
    instance.usageNotes = original
    assert instance.usageNotes == original



@given(instance=uma_ProcessDescription_strategy)
def test_uma_processdescription_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=uma_Phase_strategy)
@settings(max_examples=50)
def test_uma_phase_instantiation(instance):
    assert isinstance(instance, uma_Phase)

@given(instance=uma_Process_strategy)
@settings(max_examples=50)
def test_uma_process_instantiation(instance):
    assert isinstance(instance, uma_Process)



@given(instance=uma_Process_strategy)
def test_uma_process_includesPattern_setter(instance):
    original = instance.includesPattern
    instance.includesPattern = original
    assert instance.includesPattern == original



@given(instance=uma_Process_strategy)
def test_uma_process_diagramURI_setter(instance):
    original = instance.diagramURI
    instance.diagramURI = original
    assert instance.diagramURI == original



@given(instance=uma_Process_strategy)
def test_uma_process_defaultContext_setter(instance):
    original = instance.defaultContext
    instance.defaultContext = original
    assert instance.defaultContext == original



@given(instance=uma_Process_strategy)
def test_uma_process_validContext_setter(instance):
    original = instance.validContext
    instance.validContext = original
    assert instance.validContext == original

@given(instance=uma_Iteration_strategy)
@settings(max_examples=50)
def test_uma_iteration_instantiation(instance):
    assert isinstance(instance, uma_Iteration)

@given(instance=uma_Element_strategy)
@settings(max_examples=50)
def test_uma_element_instantiation(instance):
    assert isinstance(instance, uma_Element)

@given(instance=uma_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_uma_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, uma_EStringToStringMapEntry)

@given(instance=uma_DocumentRoot_strategy)
@settings(max_examples=50)
def test_uma_documentroot_instantiation(instance):
    assert isinstance(instance, uma_DocumentRoot)



@given(instance=uma_DocumentRoot_strategy)
def test_uma_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=BreakdownElement_strategy)
@settings(max_examples=50)
def test_breakdownelement_instantiation(instance):
    assert isinstance(instance, BreakdownElement)

@given(instance=uma_ProcessComponentInterface_strategy)
@settings(max_examples=50)
def test_uma_processcomponentinterface_instantiation(instance):
    assert isinstance(instance, uma_ProcessComponentInterface)



@given(instance=uma_ProcessComponentInterface_strategy)
def test_uma_processcomponentinterface_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma_WorkBreakdownElement_strategy)
@settings(max_examples=50)
def test_uma_workbreakdownelement_instantiation(instance):
    assert isinstance(instance, uma_WorkBreakdownElement)



@given(instance=uma_WorkBreakdownElement_strategy)
def test_uma_workbreakdownelement_isRepeatable_setter(instance):
    original = instance.isRepeatable
    instance.isRepeatable = original
    assert instance.isRepeatable == original



@given(instance=uma_WorkBreakdownElement_strategy)
def test_uma_workbreakdownelement_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original



@given(instance=uma_WorkBreakdownElement_strategy)
def test_uma_workbreakdownelement_isEventDriven_setter(instance):
    original = instance.isEventDriven
    instance.isEventDriven = original
    assert instance.isEventDriven == original



@given(instance=uma_WorkBreakdownElement_strategy)
def test_uma_workbreakdownelement_isOngoing_setter(instance):
    original = instance.isOngoing
    instance.isOngoing = original
    assert instance.isOngoing == original

@given(instance=uma_TeamProfile_strategy)
@settings(max_examples=50)
def test_uma_teamprofile_instantiation(instance):
    assert isinstance(instance, uma_TeamProfile)



@given(instance=uma_TeamProfile_strategy)
def test_uma_teamprofile_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original



@given(instance=uma_TeamProfile_strategy)
def test_uma_teamprofile_superTeam_setter(instance):
    original = instance.superTeam
    instance.superTeam = original
    assert instance.superTeam == original



@given(instance=uma_TeamProfile_strategy)
def test_uma_teamprofile_subTeam_setter(instance):
    original = instance.subTeam
    instance.subTeam = original
    assert instance.subTeam == original



@given(instance=uma_TeamProfile_strategy)
def test_uma_teamprofile_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=uma_Descriptor_strategy)
@settings(max_examples=50)
def test_uma_descriptor_instantiation(instance):
    assert isinstance(instance, uma_Descriptor)



@given(instance=uma_Descriptor_strategy)
def test_uma_descriptor_isSynchronizedWithSource_setter(instance):
    original = instance.isSynchronizedWithSource
    instance.isSynchronizedWithSource = original
    assert instance.isSynchronizedWithSource == original

@given(instance=ProcessDescription_strategy)
@settings(max_examples=50)
def test_processdescription_instantiation(instance):
    assert isinstance(instance, ProcessDescription)

@given(instance=uma_DeliveryProcessDescription_strategy)
@settings(max_examples=50)
def test_uma_deliveryprocessdescription_instantiation(instance):
    assert isinstance(instance, uma_DeliveryProcessDescription)



@given(instance=uma_DeliveryProcessDescription_strategy)
def test_uma_deliveryprocessdescription_projectMemberExpertise_setter(instance):
    original = instance.projectMemberExpertise
    instance.projectMemberExpertise = original
    assert instance.projectMemberExpertise == original



@given(instance=uma_DeliveryProcessDescription_strategy)
def test_uma_deliveryprocessdescription_estimatingTechnique_setter(instance):
    original = instance.estimatingTechnique
    instance.estimatingTechnique = original
    assert instance.estimatingTechnique == original



@given(instance=uma_DeliveryProcessDescription_strategy)
def test_uma_deliveryprocessdescription_projectCharacteristics_setter(instance):
    original = instance.projectCharacteristics
    instance.projectCharacteristics = original
    assert instance.projectCharacteristics == original



@given(instance=uma_DeliveryProcessDescription_strategy)
def test_uma_deliveryprocessdescription_riskLevel_setter(instance):
    original = instance.riskLevel
    instance.riskLevel = original
    assert instance.riskLevel == original



@given(instance=uma_DeliveryProcessDescription_strategy)
def test_uma_deliveryprocessdescription_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=uma_DeliveryProcessDescription_strategy)
def test_uma_deliveryprocessdescription_typeOfContract_setter(instance):
    original = instance.typeOfContract
    instance.typeOfContract = original
    assert instance.typeOfContract == original

@given(instance=ContentCategory_strategy)
@settings(max_examples=50)
def test_contentcategory_instantiation(instance):
    assert isinstance(instance, ContentCategory)

@given(instance=uma_Tool_strategy)
@settings(max_examples=50)
def test_uma_tool_instantiation(instance):
    assert isinstance(instance, uma_Tool)



@given(instance=uma_Tool_strategy)
def test_uma_tool_toolMentor_setter(instance):
    original = instance.toolMentor
    instance.toolMentor = original
    assert instance.toolMentor == original



@given(instance=uma_Tool_strategy)
def test_uma_tool_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma_WorkProductType_strategy)
@settings(max_examples=50)
def test_uma_workproducttype_instantiation(instance):
    assert isinstance(instance, uma_WorkProductType)



@given(instance=uma_WorkProductType_strategy)
def test_uma_workproducttype_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original



@given(instance=uma_WorkProductType_strategy)
def test_uma_workproducttype_workProduct_setter(instance):
    original = instance.workProduct
    instance.workProduct = original
    assert instance.workProduct == original

@given(instance=uma_DisciplineGrouping_strategy)
@settings(max_examples=50)
def test_uma_disciplinegrouping_instantiation(instance):
    assert isinstance(instance, uma_DisciplineGrouping)



@given(instance=uma_DisciplineGrouping_strategy)
def test_uma_disciplinegrouping_discipline_setter(instance):
    original = instance.discipline
    instance.discipline = original
    assert instance.discipline == original



@given(instance=uma_DisciplineGrouping_strategy)
def test_uma_disciplinegrouping_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma_Discipline_strategy)
@settings(max_examples=50)
def test_uma_discipline_instantiation(instance):
    assert isinstance(instance, uma_Discipline)



@given(instance=uma_Discipline_strategy)
def test_uma_discipline_referenceWorkflow_setter(instance):
    original = instance.referenceWorkflow
    instance.referenceWorkflow = original
    assert instance.referenceWorkflow == original



@given(instance=uma_Discipline_strategy)
def test_uma_discipline_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original



@given(instance=uma_Discipline_strategy)
def test_uma_discipline_task_setter(instance):
    original = instance.task
    instance.task = original
    assert instance.task == original

@given(instance=uma_RoleSetGrouping_strategy)
@settings(max_examples=50)
def test_uma_rolesetgrouping_instantiation(instance):
    assert isinstance(instance, uma_RoleSetGrouping)



@given(instance=uma_RoleSetGrouping_strategy)
def test_uma_rolesetgrouping_roleSet_setter(instance):
    original = instance.roleSet
    instance.roleSet = original
    assert instance.roleSet == original



@given(instance=uma_RoleSetGrouping_strategy)
def test_uma_rolesetgrouping_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma_Domain_strategy)
@settings(max_examples=50)
def test_uma_domain_instantiation(instance):
    assert isinstance(instance, uma_Domain)



@given(instance=uma_Domain_strategy)
def test_uma_domain_workProduct_setter(instance):
    original = instance.workProduct
    instance.workProduct = original
    assert instance.workProduct == original



@given(instance=uma_Domain_strategy)
def test_uma_domain_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma_RoleSet_strategy)
@settings(max_examples=50)
def test_uma_roleset_instantiation(instance):
    assert isinstance(instance, uma_RoleSet)



@given(instance=uma_RoleSet_strategy)
def test_uma_roleset_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original



@given(instance=uma_RoleSet_strategy)
def test_uma_roleset_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma_CustomCategory_strategy)
@settings(max_examples=50)
def test_uma_customcategory_instantiation(instance):
    assert isinstance(instance, uma_CustomCategory)



@given(instance=uma_CustomCategory_strategy)
def test_uma_customcategory_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original



@given(instance=uma_CustomCategory_strategy)
def test_uma_customcategory_subCategory_setter(instance):
    original = instance.subCategory
    instance.subCategory = original
    assert instance.subCategory == original



@given(instance=uma_CustomCategory_strategy)
def test_uma_customcategory_categorizedElement_setter(instance):
    original = instance.categorizedElement
    instance.categorizedElement = original
    assert instance.categorizedElement == original

@given(instance=WorkBreakdownElement_strategy)
@settings(max_examples=50)
def test_workbreakdownelement_instantiation(instance):
    assert isinstance(instance, WorkBreakdownElement)

@given(instance=uma_Milestone_strategy)
@settings(max_examples=50)
def test_uma_milestone_instantiation(instance):
    assert isinstance(instance, uma_Milestone)



@given(instance=uma_Milestone_strategy)
def test_uma_milestone_requiredResult_setter(instance):
    original = instance.requiredResult
    instance.requiredResult = original
    assert instance.requiredResult == original

@given(instance=uma_TaskDescriptor_strategy)
@settings(max_examples=50)
def test_uma_taskdescriptor_instantiation(instance):
    assert isinstance(instance, uma_TaskDescriptor)



@given(instance=uma_TaskDescriptor_strategy)
def test_uma_taskdescriptor_isSynchronizedWithSource_setter(instance):
    original = instance.isSynchronizedWithSource
    instance.isSynchronizedWithSource = original
    assert instance.isSynchronizedWithSource == original



@given(instance=uma_TaskDescriptor_strategy)
def test_uma_taskdescriptor_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original



@given(instance=uma_TaskDescriptor_strategy)
def test_uma_taskdescriptor_mandatoryInput_setter(instance):
    original = instance.mandatoryInput
    instance.mandatoryInput = original
    assert instance.mandatoryInput == original



@given(instance=uma_TaskDescriptor_strategy)
def test_uma_taskdescriptor_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original



@given(instance=uma_TaskDescriptor_strategy)
def test_uma_taskdescriptor_task_setter(instance):
    original = instance.task
    instance.task = original
    assert instance.task == original



@given(instance=uma_TaskDescriptor_strategy)
def test_uma_taskdescriptor_optionalInput_setter(instance):
    original = instance.optionalInput
    instance.optionalInput = original
    assert instance.optionalInput == original



@given(instance=uma_TaskDescriptor_strategy)
def test_uma_taskdescriptor_performedPrimarilyBy_setter(instance):
    original = instance.performedPrimarilyBy
    instance.performedPrimarilyBy = original
    assert instance.performedPrimarilyBy == original



@given(instance=uma_TaskDescriptor_strategy)
def test_uma_taskdescriptor_externalInput_setter(instance):
    original = instance.externalInput
    instance.externalInput = original
    assert instance.externalInput == original



@given(instance=uma_TaskDescriptor_strategy)
def test_uma_taskdescriptor_assistedBy_setter(instance):
    original = instance.assistedBy
    instance.assistedBy = original
    assert instance.assistedBy == original



@given(instance=uma_TaskDescriptor_strategy)
def test_uma_taskdescriptor_additionallyPerformedBy_setter(instance):
    original = instance.additionallyPerformedBy
    instance.additionallyPerformedBy = original
    assert instance.additionallyPerformedBy == original

@given(instance=uma_Activity_strategy)
@settings(max_examples=50)
def test_uma_activity_instantiation(instance):
    assert isinstance(instance, uma_Activity)



@given(instance=uma_Activity_strategy)
def test_uma_activity_postcondition_setter(instance):
    original = instance.postcondition
    instance.postcondition = original
    assert instance.postcondition == original



@given(instance=uma_Activity_strategy)
def test_uma_activity_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original



@given(instance=uma_Activity_strategy)
def test_uma_activity_variabilityBasedOnElement_setter(instance):
    original = instance.variabilityBasedOnElement
    instance.variabilityBasedOnElement = original
    assert instance.variabilityBasedOnElement == original



@given(instance=uma_Activity_strategy)
def test_uma_activity_variabilityType_setter(instance):
    original = instance.variabilityType
    instance.variabilityType = original
    assert instance.variabilityType == original



@given(instance=uma_Activity_strategy)
def test_uma_activity_roadmap_setter(instance):
    original = instance.roadmap
    instance.roadmap = original
    assert instance.roadmap == original



@given(instance=uma_Activity_strategy)
def test_uma_activity_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original



@given(instance=uma_Activity_strategy)
def test_uma_activity_isEnactable_setter(instance):
    original = instance.isEnactable
    instance.isEnactable = original
    assert instance.isEnactable == original

@given(instance=DescribableElement_strategy)
@settings(max_examples=50)
def test_describableelement_instantiation(instance):
    assert isinstance(instance, DescribableElement)

@given(instance=uma_ProcessElement_strategy)
@settings(max_examples=50)
def test_uma_processelement_instantiation(instance):
    assert isinstance(instance, uma_ProcessElement)

@given(instance=uma_ContentElement_strategy)
@settings(max_examples=50)
def test_uma_contentelement_instantiation(instance):
    assert isinstance(instance, uma_ContentElement)



@given(instance=uma_ContentElement_strategy)
def test_uma_contentelement_concept_setter(instance):
    original = instance.concept
    instance.concept = original
    assert instance.concept == original



@given(instance=uma_ContentElement_strategy)
def test_uma_contentelement_whitepaper_setter(instance):
    original = instance.whitepaper
    instance.whitepaper = original
    assert instance.whitepaper == original



@given(instance=uma_ContentElement_strategy)
def test_uma_contentelement_reusableAsset_setter(instance):
    original = instance.reusableAsset
    instance.reusableAsset = original
    assert instance.reusableAsset == original



@given(instance=uma_ContentElement_strategy)
def test_uma_contentelement_guideline_setter(instance):
    original = instance.guideline
    instance.guideline = original
    assert instance.guideline == original



@given(instance=uma_ContentElement_strategy)
def test_uma_contentelement_example_setter(instance):
    original = instance.example
    instance.example = original
    assert instance.example == original



@given(instance=uma_ContentElement_strategy)
def test_uma_contentelement_variabilityType_setter(instance):
    original = instance.variabilityType
    instance.variabilityType = original
    assert instance.variabilityType == original



@given(instance=uma_ContentElement_strategy)
def test_uma_contentelement_group1_setter(instance):
    original = instance.group1
    instance.group1 = original
    assert instance.group1 == original



@given(instance=uma_ContentElement_strategy)
def test_uma_contentelement_checklist_setter(instance):
    original = instance.checklist
    instance.checklist = original
    assert instance.checklist == original



@given(instance=uma_ContentElement_strategy)
def test_uma_contentelement_variabilityBasedOnElement_setter(instance):
    original = instance.variabilityBasedOnElement
    instance.variabilityBasedOnElement = original
    assert instance.variabilityBasedOnElement == original



@given(instance=uma_ContentElement_strategy)
def test_uma_contentelement_supportingMaterial_setter(instance):
    original = instance.supportingMaterial
    instance.supportingMaterial = original
    assert instance.supportingMaterial == original

@given(instance=MethodUnit_strategy)
@settings(max_examples=50)
def test_methodunit_instantiation(instance):
    assert isinstance(instance, MethodUnit)

@given(instance=uma_MethodPlugin_strategy)
@settings(max_examples=50)
def test_uma_methodplugin_instantiation(instance):
    assert isinstance(instance, uma_MethodPlugin)



@given(instance=uma_MethodPlugin_strategy)
def test_uma_methodplugin_referencedMethodPlugin_setter(instance):
    original = instance.referencedMethodPlugin
    instance.referencedMethodPlugin = original
    assert instance.referencedMethodPlugin == original



@given(instance=uma_MethodPlugin_strategy)
def test_uma_methodplugin_userChangeable_setter(instance):
    original = instance.userChangeable
    instance.userChangeable = original
    assert instance.userChangeable == original



@given(instance=uma_MethodPlugin_strategy)
def test_uma_methodplugin_supporting_setter(instance):
    original = instance.supporting
    instance.supporting = original
    assert instance.supporting == original

@given(instance=uma_MethodLibrary_strategy)
@settings(max_examples=50)
def test_uma_methodlibrary_instantiation(instance):
    assert isinstance(instance, uma_MethodLibrary)



@given(instance=uma_MethodLibrary_strategy)
def test_uma_methodlibrary_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original

@given(instance=uma_MethodConfiguration_strategy)
@settings(max_examples=50)
def test_uma_methodconfiguration_instantiation(instance):
    assert isinstance(instance, uma_MethodConfiguration)



@given(instance=uma_MethodConfiguration_strategy)
def test_uma_methodconfiguration_subtractedCategory_setter(instance):
    original = instance.subtractedCategory
    instance.subtractedCategory = original
    assert instance.subtractedCategory == original



@given(instance=uma_MethodConfiguration_strategy)
def test_uma_methodconfiguration_methodPackageSelection_setter(instance):
    original = instance.methodPackageSelection
    instance.methodPackageSelection = original
    assert instance.methodPackageSelection == original



@given(instance=uma_MethodConfiguration_strategy)
def test_uma_methodconfiguration_addedCategory_setter(instance):
    original = instance.addedCategory
    instance.addedCategory = original
    assert instance.addedCategory == original



@given(instance=uma_MethodConfiguration_strategy)
def test_uma_methodconfiguration_methodPluginSelection_setter(instance):
    original = instance.methodPluginSelection
    instance.methodPluginSelection = original
    assert instance.methodPluginSelection == original



@given(instance=uma_MethodConfiguration_strategy)
def test_uma_methodconfiguration_baseConfiguration_setter(instance):
    original = instance.baseConfiguration
    instance.baseConfiguration = original
    assert instance.baseConfiguration == original



@given(instance=uma_MethodConfiguration_strategy)
def test_uma_methodconfiguration_processView_setter(instance):
    original = instance.processView
    instance.processView = original
    assert instance.processView == original



@given(instance=uma_MethodConfiguration_strategy)
def test_uma_methodconfiguration_defaultView_setter(instance):
    original = instance.defaultView
    instance.defaultView = original
    assert instance.defaultView == original

@given(instance=uma_ContentDescription_strategy)
@settings(max_examples=50)
def test_uma_contentdescription_instantiation(instance):
    assert isinstance(instance, uma_ContentDescription)



@given(instance=uma_ContentDescription_strategy)
def test_uma_contentdescription_keyConsiderations_setter(instance):
    original = instance.keyConsiderations
    instance.keyConsiderations = original
    assert instance.keyConsiderations == original



@given(instance=uma_ContentDescription_strategy)
def test_uma_contentdescription_externalId_setter(instance):
    original = instance.externalId
    instance.externalId = original
    assert instance.externalId == original



@given(instance=uma_ContentDescription_strategy)
def test_uma_contentdescription_mainDescription_setter(instance):
    original = instance.mainDescription
    instance.mainDescription = original
    assert instance.mainDescription == original

@given(instance=MethodPackage_strategy)
@settings(max_examples=50)
def test_methodpackage_instantiation(instance):
    assert isinstance(instance, MethodPackage)

@given(instance=uma_ProcessPackage_strategy)
@settings(max_examples=50)
def test_uma_processpackage_instantiation(instance):
    assert isinstance(instance, uma_ProcessPackage)



@given(instance=uma_ProcessPackage_strategy)
def test_uma_processpackage_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma_ContentPackage_strategy)
@settings(max_examples=50)
def test_uma_contentpackage_instantiation(instance):
    assert isinstance(instance, uma_ContentPackage)



@given(instance=uma_ContentPackage_strategy)
def test_uma_contentpackage_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma_ContentCategoryPackage_strategy)
@settings(max_examples=50)
def test_uma_contentcategorypackage_instantiation(instance):
    assert isinstance(instance, uma_ContentCategoryPackage)



@given(instance=uma_ContentCategoryPackage_strategy)
def test_uma_contentcategorypackage_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=ContentElement_strategy)
@settings(max_examples=50)
def test_contentelement_instantiation(instance):
    assert isinstance(instance, ContentElement)

@given(instance=uma_Kind_strategy)
@settings(max_examples=50)
def test_uma_kind_instantiation(instance):
    assert isinstance(instance, uma_Kind)



@given(instance=uma_Kind_strategy)
def test_uma_kind_applicableMetaClassInfo_setter(instance):
    original = instance.applicableMetaClassInfo
    instance.applicableMetaClassInfo = original
    assert instance.applicableMetaClassInfo == original

@given(instance=uma_Guidance_strategy)
@settings(max_examples=50)
def test_uma_guidance_instantiation(instance):
    assert isinstance(instance, uma_Guidance)

@given(instance=uma_Task_strategy)
@settings(max_examples=50)
def test_uma_task_instantiation(instance):
    assert isinstance(instance, uma_Task)



@given(instance=uma_Task_strategy)
def test_uma_task_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original



@given(instance=uma_Task_strategy)
def test_uma_task_mandatoryInput_setter(instance):
    original = instance.mandatoryInput
    instance.mandatoryInput = original
    assert instance.mandatoryInput == original



@given(instance=uma_Task_strategy)
def test_uma_task_postcondition_setter(instance):
    original = instance.postcondition
    instance.postcondition = original
    assert instance.postcondition == original



@given(instance=uma_Task_strategy)
def test_uma_task_optionalInput_setter(instance):
    original = instance.optionalInput
    instance.optionalInput = original
    assert instance.optionalInput == original



@given(instance=uma_Task_strategy)
def test_uma_task_toolMentor_setter(instance):
    original = instance.toolMentor
    instance.toolMentor = original
    assert instance.toolMentor == original



@given(instance=uma_Task_strategy)
def test_uma_task_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original



@given(instance=uma_Task_strategy)
def test_uma_task_estimate_setter(instance):
    original = instance.estimate
    instance.estimate = original
    assert instance.estimate == original



@given(instance=uma_Task_strategy)
def test_uma_task_estimationConsiderations_setter(instance):
    original = instance.estimationConsiderations
    instance.estimationConsiderations = original
    assert instance.estimationConsiderations == original



@given(instance=uma_Task_strategy)
def test_uma_task_performedBy_setter(instance):
    original = instance.performedBy
    instance.performedBy = original
    assert instance.performedBy == original



@given(instance=uma_Task_strategy)
def test_uma_task_additionallyPerformedBy_setter(instance):
    original = instance.additionallyPerformedBy
    instance.additionallyPerformedBy = original
    assert instance.additionallyPerformedBy == original



@given(instance=uma_Task_strategy)
def test_uma_task_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=uma_WorkProduct_strategy)
@settings(max_examples=50)
def test_uma_workproduct_instantiation(instance):
    assert isinstance(instance, uma_WorkProduct)



@given(instance=uma_WorkProduct_strategy)
def test_uma_workproduct_toolMentor_setter(instance):
    original = instance.toolMentor
    instance.toolMentor = original
    assert instance.toolMentor == original



@given(instance=uma_WorkProduct_strategy)
def test_uma_workproduct_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original



@given(instance=uma_WorkProduct_strategy)
def test_uma_workproduct_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original



@given(instance=uma_WorkProduct_strategy)
def test_uma_workproduct_report_setter(instance):
    original = instance.report
    instance.report = original
    assert instance.report == original



@given(instance=uma_WorkProduct_strategy)
def test_uma_workproduct_estimationConsiderations_setter(instance):
    original = instance.estimationConsiderations
    instance.estimationConsiderations = original
    assert instance.estimationConsiderations == original



@given(instance=uma_WorkProduct_strategy)
def test_uma_workproduct_estimate_setter(instance):
    original = instance.estimate
    instance.estimate = original
    assert instance.estimate == original

@given(instance=uma_ContentCategory_strategy)
@settings(max_examples=50)
def test_uma_contentcategory_instantiation(instance):
    assert isinstance(instance, uma_ContentCategory)

@given(instance=MethodElement_strategy)
@settings(max_examples=50)
def test_methodelement_instantiation(instance):
    assert isinstance(instance, MethodElement)

@given(instance=uma_MethodPackage_strategy)
@settings(max_examples=50)
def test_uma_methodpackage_instantiation(instance):
    assert isinstance(instance, uma_MethodPackage)



@given(instance=uma_MethodPackage_strategy)
def test_uma_methodpackage_reusedPackage_setter(instance):
    original = instance.reusedPackage
    instance.reusedPackage = original
    assert instance.reusedPackage == original



@given(instance=uma_MethodPackage_strategy)
def test_uma_methodpackage_group1_setter(instance):
    original = instance.group1
    instance.group1 = original
    assert instance.group1 == original



@given(instance=uma_MethodPackage_strategy)
def test_uma_methodpackage_global__setter(instance):
    original = instance.global_
    instance.global_ = original
    assert instance.global_ == original

@given(instance=uma_MethodUnit_strategy)
@settings(max_examples=50)
def test_uma_methodunit_instantiation(instance):
    assert isinstance(instance, uma_MethodUnit)



@given(instance=uma_MethodUnit_strategy)
def test_uma_methodunit_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=uma_MethodUnit_strategy)
def test_uma_methodunit_changeDate_setter(instance):
    original = instance.changeDate
    instance.changeDate = original
    assert instance.changeDate == original



@given(instance=uma_MethodUnit_strategy)
def test_uma_methodunit_authors_setter(instance):
    original = instance.authors
    instance.authors = original
    assert instance.authors == original



@given(instance=uma_MethodUnit_strategy)
def test_uma_methodunit_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original



@given(instance=uma_MethodUnit_strategy)
def test_uma_methodunit_changeDescription_setter(instance):
    original = instance.changeDescription
    instance.changeDescription = original
    assert instance.changeDescription == original

@given(instance=uma_DescribableElement_strategy)
@settings(max_examples=50)
def test_uma_describableelement_instantiation(instance):
    assert isinstance(instance, uma_DescribableElement)



@given(instance=uma_DescribableElement_strategy)
def test_uma_describableelement_nodeicon_setter(instance):
    original = instance.nodeicon
    instance.nodeicon = original
    assert instance.nodeicon == original



@given(instance=uma_DescribableElement_strategy)
def test_uma_describableelement_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original



@given(instance=uma_DescribableElement_strategy)
def test_uma_describableelement_fulfill_setter(instance):
    original = instance.fulfill
    instance.fulfill = original
    assert instance.fulfill == original



@given(instance=uma_DescribableElement_strategy)
def test_uma_describableelement_shapeicon_setter(instance):
    original = instance.shapeicon
    instance.shapeicon = original
    assert instance.shapeicon == original

@given(instance=uma_Section_strategy)
@settings(max_examples=50)
def test_uma_section_instantiation(instance):
    assert isinstance(instance, uma_Section)



@given(instance=uma_Section_strategy)
def test_uma_section_variabilityType_setter(instance):
    original = instance.variabilityType
    instance.variabilityType = original
    assert instance.variabilityType == original



@given(instance=uma_Section_strategy)
def test_uma_section_sectionName_setter(instance):
    original = instance.sectionName
    instance.sectionName = original
    assert instance.sectionName == original



@given(instance=uma_Section_strategy)
def test_uma_section_variabilityBasedOnElement_setter(instance):
    original = instance.variabilityBasedOnElement
    instance.variabilityBasedOnElement = original
    assert instance.variabilityBasedOnElement == original



@given(instance=uma_Section_strategy)
def test_uma_section_predecessor_setter(instance):
    original = instance.predecessor
    instance.predecessor = original
    assert instance.predecessor == original



@given(instance=uma_Section_strategy)
def test_uma_section_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=uma_WorkDefinition_strategy)
@settings(max_examples=50)
def test_uma_workdefinition_instantiation(instance):
    assert isinstance(instance, uma_WorkDefinition)



@given(instance=uma_WorkDefinition_strategy)
def test_uma_workdefinition_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original



@given(instance=uma_WorkDefinition_strategy)
def test_uma_workdefinition_postcondition_setter(instance):
    original = instance.postcondition
    instance.postcondition = original
    assert instance.postcondition == original

@given(instance=uma_Constraint_strategy)
@settings(max_examples=50)
def test_uma_constraint_instantiation(instance):
    assert isinstance(instance, uma_Constraint)



@given(instance=uma_Constraint_strategy)
def test_uma_constraint_mainDescription_setter(instance):
    original = instance.mainDescription
    instance.mainDescription = original
    assert instance.mainDescription == original

@given(instance=uma_Role_strategy)
@settings(max_examples=50)
def test_uma_role_instantiation(instance):
    assert isinstance(instance, uma_Role)



@given(instance=uma_Role_strategy)
def test_uma_role_responsibleFor_setter(instance):
    original = instance.responsibleFor
    instance.responsibleFor = original
    assert instance.responsibleFor == original



@given(instance=uma_Role_strategy)
def test_uma_role_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=RoleDescriptor_strategy)
@settings(max_examples=50)
def test_roledescriptor_instantiation(instance):
    assert isinstance(instance, RoleDescriptor)

@given(instance=uma_CompositeRole_strategy)
@settings(max_examples=50)
def test_uma_compositerole_instantiation(instance):
    assert isinstance(instance, uma_CompositeRole)



@given(instance=uma_CompositeRole_strategy)
def test_uma_compositerole_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=Guidance_strategy)
@settings(max_examples=50)
def test_guidance_instantiation(instance):
    assert isinstance(instance, Guidance)

@given(instance=uma_EstimatingMetric_strategy)
@settings(max_examples=50)
def test_uma_estimatingmetric_instantiation(instance):
    assert isinstance(instance, uma_EstimatingMetric)

@given(instance=uma_ToolMentor_strategy)
@settings(max_examples=50)
def test_uma_toolmentor_instantiation(instance):
    assert isinstance(instance, uma_ToolMentor)

@given(instance=uma_Concept_strategy)
@settings(max_examples=50)
def test_uma_concept_instantiation(instance):
    assert isinstance(instance, uma_Concept)

@given(instance=uma_Report_strategy)
@settings(max_examples=50)
def test_uma_report_instantiation(instance):
    assert isinstance(instance, uma_Report)

@given(instance=uma_Estimate_strategy)
@settings(max_examples=50)
def test_uma_estimate_instantiation(instance):
    assert isinstance(instance, uma_Estimate)



@given(instance=uma_Estimate_strategy)
def test_uma_estimate_estimationMetric_setter(instance):
    original = instance.estimationMetric
    instance.estimationMetric = original
    assert instance.estimationMetric == original



@given(instance=uma_Estimate_strategy)
def test_uma_estimate_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original



@given(instance=uma_Estimate_strategy)
def test_uma_estimate_estimationConsiderations_setter(instance):
    original = instance.estimationConsiderations
    instance.estimationConsiderations = original
    assert instance.estimationConsiderations == original

@given(instance=uma_Practice_strategy)
@settings(max_examples=50)
def test_uma_practice_instantiation(instance):
    assert isinstance(instance, uma_Practice)



@given(instance=uma_Practice_strategy)
def test_uma_practice_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original



@given(instance=uma_Practice_strategy)
def test_uma_practice_activityReference_setter(instance):
    original = instance.activityReference
    instance.activityReference = original
    assert instance.activityReference == original



@given(instance=uma_Practice_strategy)
def test_uma_practice_contentReference_setter(instance):
    original = instance.contentReference
    instance.contentReference = original
    assert instance.contentReference == original

@given(instance=uma_ReusableAsset_strategy)
@settings(max_examples=50)
def test_uma_reusableasset_instantiation(instance):
    assert isinstance(instance, uma_ReusableAsset)

@given(instance=uma_Example_strategy)
@settings(max_examples=50)
def test_uma_example_instantiation(instance):
    assert isinstance(instance, uma_Example)

@given(instance=uma_Template_strategy)
@settings(max_examples=50)
def test_uma_template_instantiation(instance):
    assert isinstance(instance, uma_Template)

@given(instance=uma_Guideline_strategy)
@settings(max_examples=50)
def test_uma_guideline_instantiation(instance):
    assert isinstance(instance, uma_Guideline)

@given(instance=uma_EstimationConsiderations_strategy)
@settings(max_examples=50)
def test_uma_estimationconsiderations_instantiation(instance):
    assert isinstance(instance, uma_EstimationConsiderations)

@given(instance=uma_SupportingMaterial_strategy)
@settings(max_examples=50)
def test_uma_supportingmaterial_instantiation(instance):
    assert isinstance(instance, uma_SupportingMaterial)

@given(instance=uma_Roadmap_strategy)
@settings(max_examples=50)
def test_uma_roadmap_instantiation(instance):
    assert isinstance(instance, uma_Roadmap)

@given(instance=uma_TermDefinition_strategy)
@settings(max_examples=50)
def test_uma_termdefinition_instantiation(instance):
    assert isinstance(instance, uma_TermDefinition)

@given(instance=uma_Checklist_strategy)
@settings(max_examples=50)
def test_uma_checklist_instantiation(instance):
    assert isinstance(instance, uma_Checklist)

@given(instance=Process_strategy)
@settings(max_examples=50)
def test_process_instantiation(instance):
    assert isinstance(instance, Process)

@given(instance=uma_ProcessPlanningTemplate_strategy)
@settings(max_examples=50)
def test_uma_processplanningtemplate_instantiation(instance):
    assert isinstance(instance, uma_ProcessPlanningTemplate)



@given(instance=uma_ProcessPlanningTemplate_strategy)
def test_uma_processplanningtemplate_baseProcess_setter(instance):
    original = instance.baseProcess
    instance.baseProcess = original
    assert instance.baseProcess == original



@given(instance=uma_ProcessPlanningTemplate_strategy)
def test_uma_processplanningtemplate_group4_setter(instance):
    original = instance.group4
    instance.group4 = original
    assert instance.group4 == original

@given(instance=uma_DeliveryProcess_strategy)
@settings(max_examples=50)
def test_uma_deliveryprocess_instantiation(instance):
    assert isinstance(instance, uma_DeliveryProcess)



@given(instance=uma_DeliveryProcess_strategy)
def test_uma_deliveryprocess_group4_setter(instance):
    original = instance.group4
    instance.group4 = original
    assert instance.group4 == original



@given(instance=uma_DeliveryProcess_strategy)
def test_uma_deliveryprocess_communicationsMaterial_setter(instance):
    original = instance.communicationsMaterial
    instance.communicationsMaterial = original
    assert instance.communicationsMaterial == original



@given(instance=uma_DeliveryProcess_strategy)
def test_uma_deliveryprocess_educationMaterial_setter(instance):
    original = instance.educationMaterial
    instance.educationMaterial = original
    assert instance.educationMaterial == original

@given(instance=uma_CapabilityPattern_strategy)
@settings(max_examples=50)
def test_uma_capabilitypattern_instantiation(instance):
    assert isinstance(instance, uma_CapabilityPattern)

@given(instance=ContentDescription_strategy)
@settings(max_examples=50)
def test_contentdescription_instantiation(instance):
    assert isinstance(instance, ContentDescription)

@given(instance=uma_RoleDescription_strategy)
@settings(max_examples=50)
def test_uma_roledescription_instantiation(instance):
    assert isinstance(instance, uma_RoleDescription)



@given(instance=uma_RoleDescription_strategy)
def test_uma_roledescription_synonyms_setter(instance):
    original = instance.synonyms
    instance.synonyms = original
    assert instance.synonyms == original



@given(instance=uma_RoleDescription_strategy)
def test_uma_roledescription_skills_setter(instance):
    original = instance.skills
    instance.skills = original
    assert instance.skills == original



@given(instance=uma_RoleDescription_strategy)
def test_uma_roledescription_assignmentApproaches_setter(instance):
    original = instance.assignmentApproaches
    instance.assignmentApproaches = original
    assert instance.assignmentApproaches == original

@given(instance=uma_TaskDescription_strategy)
@settings(max_examples=50)
def test_uma_taskdescription_instantiation(instance):
    assert isinstance(instance, uma_TaskDescription)



@given(instance=uma_TaskDescription_strategy)
def test_uma_taskdescription_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original



@given(instance=uma_TaskDescription_strategy)
def test_uma_taskdescription_alternatives_setter(instance):
    original = instance.alternatives
    instance.alternatives = original
    assert instance.alternatives == original

@given(instance=uma_WorkProductDescription_strategy)
@settings(max_examples=50)
def test_uma_workproductdescription_instantiation(instance):
    assert isinstance(instance, uma_WorkProductDescription)



@given(instance=uma_WorkProductDescription_strategy)
def test_uma_workproductdescription_impactOfNotHaving_setter(instance):
    original = instance.impactOfNotHaving
    instance.impactOfNotHaving = original
    assert instance.impactOfNotHaving == original



@given(instance=uma_WorkProductDescription_strategy)
def test_uma_workproductdescription_reasonsForNotNeeding_setter(instance):
    original = instance.reasonsForNotNeeding
    instance.reasonsForNotNeeding = original
    assert instance.reasonsForNotNeeding == original



@given(instance=uma_WorkProductDescription_strategy)
def test_uma_workproductdescription_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original

@given(instance=uma_PracticeDescription_strategy)
@settings(max_examples=50)
def test_uma_practicedescription_instantiation(instance):
    assert isinstance(instance, uma_PracticeDescription)



@given(instance=uma_PracticeDescription_strategy)
def test_uma_practicedescription_levelsOfAdoption_setter(instance):
    original = instance.levelsOfAdoption
    instance.levelsOfAdoption = original
    assert instance.levelsOfAdoption == original



@given(instance=uma_PracticeDescription_strategy)
def test_uma_practicedescription_problem_setter(instance):
    original = instance.problem
    instance.problem = original
    assert instance.problem == original



@given(instance=uma_PracticeDescription_strategy)
def test_uma_practicedescription_application_setter(instance):
    original = instance.application
    instance.application = original
    assert instance.application == original



@given(instance=uma_PracticeDescription_strategy)
def test_uma_practicedescription_additionalInfo_setter(instance):
    original = instance.additionalInfo
    instance.additionalInfo = original
    assert instance.additionalInfo == original



@given(instance=uma_PracticeDescription_strategy)
def test_uma_practicedescription_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original



@given(instance=uma_PracticeDescription_strategy)
def test_uma_practicedescription_goals_setter(instance):
    original = instance.goals
    instance.goals = original
    assert instance.goals == original

@given(instance=uma_GuidanceDescription_strategy)
@settings(max_examples=50)
def test_uma_guidancedescription_instantiation(instance):
    assert isinstance(instance, uma_GuidanceDescription)



@given(instance=uma_GuidanceDescription_strategy)
def test_uma_guidancedescription_attachment_setter(instance):
    original = instance.attachment
    instance.attachment = original
    assert instance.attachment == original

@given(instance=uma_BreakdownElementDescription_strategy)
@settings(max_examples=50)
def test_uma_breakdownelementdescription_instantiation(instance):
    assert isinstance(instance, uma_BreakdownElementDescription)



@given(instance=uma_BreakdownElementDescription_strategy)
def test_uma_breakdownelementdescription_usageGuidance_setter(instance):
    original = instance.usageGuidance
    instance.usageGuidance = original
    assert instance.usageGuidance == original

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

@given(instance=uma_PlanningData_strategy)
@settings(max_examples=50)
def test_uma_planningdata_instantiation(instance):
    assert isinstance(instance, uma_PlanningData)



@given(instance=uma_PlanningData_strategy)
def test_uma_planningdata_finishDate_setter(instance):
    original = instance.finishDate
    instance.finishDate = original
    assert instance.finishDate == original



@given(instance=uma_PlanningData_strategy)
def test_uma_planningdata_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original



@given(instance=uma_PlanningData_strategy)
def test_uma_planningdata_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=uma_BreakdownElement_strategy)
@settings(max_examples=50)
def test_uma_breakdownelement_instantiation(instance):
    assert isinstance(instance, uma_BreakdownElement)



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_hasMultipleOccurrences_setter(instance):
    original = instance.hasMultipleOccurrences
    instance.hasMultipleOccurrences = original
    assert instance.hasMultipleOccurrences == original



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_group1_setter(instance):
    original = instance.group1
    instance.group1 = original
    assert instance.group1 == original



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_whitepaper_setter(instance):
    original = instance.whitepaper
    instance.whitepaper = original
    assert instance.whitepaper == original



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_example_setter(instance):
    original = instance.example
    instance.example = original
    assert instance.example == original



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_presentedBefore_setter(instance):
    original = instance.presentedBefore
    instance.presentedBefore = original
    assert instance.presentedBefore == original



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_superActivity_setter(instance):
    original = instance.superActivity
    instance.superActivity = original
    assert instance.superActivity == original



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_concept_setter(instance):
    original = instance.concept
    instance.concept = original
    assert instance.concept == original



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_presentedAfter_setter(instance):
    original = instance.presentedAfter
    instance.presentedAfter = original
    assert instance.presentedAfter == original



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_guideline_setter(instance):
    original = instance.guideline
    instance.guideline = original
    assert instance.guideline == original



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_isPlanned_setter(instance):
    original = instance.isPlanned
    instance.isPlanned = original
    assert instance.isPlanned == original



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_reusableAsset_setter(instance):
    original = instance.reusableAsset
    instance.reusableAsset = original
    assert instance.reusableAsset == original



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_supportingMaterial_setter(instance):
    original = instance.supportingMaterial
    instance.supportingMaterial = original
    assert instance.supportingMaterial == original



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_planningData_setter(instance):
    original = instance.planningData
    instance.planningData = original
    assert instance.planningData == original



@given(instance=uma_BreakdownElement_strategy)
def test_uma_breakdownelement_checklist_setter(instance):
    original = instance.checklist
    instance.checklist = original
    assert instance.checklist == original

@given(instance=WorkProductDescription_strategy)
@settings(max_examples=50)
def test_workproductdescription_instantiation(instance):
    assert isinstance(instance, WorkProductDescription)

@given(instance=uma_DeliverableDescription_strategy)
@settings(max_examples=50)
def test_uma_deliverabledescription_instantiation(instance):
    assert isinstance(instance, uma_DeliverableDescription)



@given(instance=uma_DeliverableDescription_strategy)
def test_uma_deliverabledescription_externalDescription_setter(instance):
    original = instance.externalDescription
    instance.externalDescription = original
    assert instance.externalDescription == original



@given(instance=uma_DeliverableDescription_strategy)
def test_uma_deliverabledescription_packagingGuidance_setter(instance):
    original = instance.packagingGuidance
    instance.packagingGuidance = original
    assert instance.packagingGuidance == original

@given(instance=uma_ArtifactDescription_strategy)
@settings(max_examples=50)
def test_uma_artifactdescription_instantiation(instance):
    assert isinstance(instance, uma_ArtifactDescription)



@given(instance=uma_ArtifactDescription_strategy)
def test_uma_artifactdescription_briefOutline_setter(instance):
    original = instance.briefOutline
    instance.briefOutline = original
    assert instance.briefOutline == original



@given(instance=uma_ArtifactDescription_strategy)
def test_uma_artifactdescription_representation_setter(instance):
    original = instance.representation
    instance.representation = original
    assert instance.representation == original



@given(instance=uma_ArtifactDescription_strategy)
def test_uma_artifactdescription_representationOptions_setter(instance):
    original = instance.representationOptions
    instance.representationOptions = original
    assert instance.representationOptions == original



@given(instance=uma_ArtifactDescription_strategy)
def test_uma_artifactdescription_notation_setter(instance):
    original = instance.notation
    instance.notation = original
    assert instance.notation == original

@given(instance=WorkProduct_strategy)
@settings(max_examples=50)
def test_workproduct_instantiation(instance):
    assert isinstance(instance, WorkProduct)

@given(instance=uma_Outcome_strategy)
@settings(max_examples=50)
def test_uma_outcome_instantiation(instance):
    assert isinstance(instance, uma_Outcome)

@given(instance=uma_Deliverable_strategy)
@settings(max_examples=50)
def test_uma_deliverable_instantiation(instance):
    assert isinstance(instance, uma_Deliverable)



@given(instance=uma_Deliverable_strategy)
def test_uma_deliverable_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original



@given(instance=uma_Deliverable_strategy)
def test_uma_deliverable_deliveredWorkProduct_setter(instance):
    original = instance.deliveredWorkProduct
    instance.deliveredWorkProduct = original
    assert instance.deliveredWorkProduct == original

@given(instance=uma_Artifact_strategy)
@settings(max_examples=50)
def test_uma_artifact_instantiation(instance):
    assert isinstance(instance, uma_Artifact)



@given(instance=uma_Artifact_strategy)
def test_uma_artifact_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=uma_MethodElement_strategy)
@settings(max_examples=50)
def test_uma_methodelement_instantiation(instance):
    assert isinstance(instance, uma_MethodElement)



@given(instance=uma_MethodElement_strategy)
def test_uma_methodelement_presentationName_setter(instance):
    original = instance.presentationName
    instance.presentationName = original
    assert instance.presentationName == original



@given(instance=uma_MethodElement_strategy)
def test_uma_methodelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=uma_MethodElement_strategy)
def test_uma_methodelement_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=uma_MethodElement_strategy)
def test_uma_methodelement_briefDescription_setter(instance):
    original = instance.briefDescription
    instance.briefDescription = original
    assert instance.briefDescription == original



@given(instance=uma_MethodElement_strategy)
def test_uma_methodelement_orderingGuide_setter(instance):
    original = instance.orderingGuide
    instance.orderingGuide = original
    assert instance.orderingGuide == original



@given(instance=uma_MethodElement_strategy)
def test_uma_methodelement_suppressed_setter(instance):
    original = instance.suppressed
    instance.suppressed = original
    assert instance.suppressed == original

@given(instance=uma_MethodElementProperty_strategy)
@settings(max_examples=50)
def test_uma_methodelementproperty_instantiation(instance):
    assert isinstance(instance, uma_MethodElementProperty)



@given(instance=uma_MethodElementProperty_strategy)
def test_uma_methodelementproperty_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uma_ApplicableMetaClassInfo_strategy)
@settings(max_examples=50)
def test_uma_applicablemetaclassinfo_instantiation(instance):
    assert isinstance(instance, uma_ApplicableMetaClassInfo)



@given(instance=uma_ApplicableMetaClassInfo_strategy)
def test_uma_applicablemetaclassinfo_isPrimaryExtension_setter(instance):
    original = instance.isPrimaryExtension
    instance.isPrimaryExtension = original
    assert instance.isPrimaryExtension == original

@given(instance=BreakdownElementDescription_strategy)
@settings(max_examples=50)
def test_breakdownelementdescription_instantiation(instance):
    assert isinstance(instance, BreakdownElementDescription)

@given(instance=uma_DescriptorDescription_strategy)
@settings(max_examples=50)
def test_uma_descriptordescription_instantiation(instance):
    assert isinstance(instance, uma_DescriptorDescription)



@given(instance=uma_DescriptorDescription_strategy)
def test_uma_descriptordescription_refinedDescription_setter(instance):
    original = instance.refinedDescription
    instance.refinedDescription = original
    assert instance.refinedDescription == original

@given(instance=uma_ActivityDescription_strategy)
@settings(max_examples=50)
def test_uma_activitydescription_instantiation(instance):
    assert isinstance(instance, uma_ActivityDescription)



@given(instance=uma_ActivityDescription_strategy)
def test_uma_activitydescription_alternatives_setter(instance):
    original = instance.alternatives
    instance.alternatives = original
    assert instance.alternatives == original



@given(instance=uma_ActivityDescription_strategy)
def test_uma_activitydescription_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original



@given(instance=uma_ActivityDescription_strategy)
def test_uma_activitydescription_howToStaff_setter(instance):
    original = instance.howToStaff
    instance.howToStaff = original
    assert instance.howToStaff == original

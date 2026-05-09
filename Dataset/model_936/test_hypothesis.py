import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ActivityDescription,
    uma::ProcessDescription,
    ProcessPackage,
    uma::ProcessComponent,
    NamedElement,
    uma::PackageableElement,
    Element,
    uma::NamedElement,
    Activity,
    uma::Phase,
    uma::Process,
    uma::Iteration,
    uma::EStringToStringMapEntry,
    uma::Element,
    BreakdownElement,
    uma::ProcessComponentInterface,
    uma::Descriptor,
    uma::DocumentRoot,
    ProcessDescription,
    uma::DeliveryProcessDescription,
    ContentCategory,
    uma::DisciplineGrouping,
    uma::Domain,
    uma::Discipline,
    uma::CustomCategory,
    WorkBreakdownElement,
    uma::TaskDescriptor,
    uma::Milestone,
    uma::Activity,
    DescribableElement,
    uma::ProcessElement,
    uma::ContentElement,
    MethodUnit,
    uma::MethodConfiguration,
    uma::MethodLibrary,
    uma::MethodPlugin,
    uma::ContentDescription,
    MethodPackage,
    uma::ContentPackage,
    uma::ProcessPackage,
    uma::ContentCategoryPackage,
    RoleDescriptor,
    uma::CompositeRole,
    Guidance,
    uma::Practice,
    uma::Example,
    uma::EstimatingMetric,
    uma::EstimationConsiderations,
    uma::Estimate,
    uma::Guideline,
    uma::Concept,
    uma::Checklist,
    Process,
    uma::ProcessPlanningTemplate,
    uma::DeliveryProcess,
    uma::CapabilityPattern,
    ContentElement,
    uma::Role,
    uma::Guidance,
    uma::Kind,
    uma::ContentCategory,
    MethodElement,
    uma::MethodPackage,
    uma::MethodUnit,
    uma::Section,
    uma::DescribableElement,
    uma::Constraint,
    ContentDescription,
    uma::GuidanceDescription,
    uma::PracticeDescription,
    uma::RoleDescription,
    uma::BreakdownElementDescription,
    WorkProductDescription,
    uma::DeliverableDescription,
    uma::ArtifactDescription,
    WorkProduct,
    uma::Outcome,
    uma::Deliverable,
    uma::Artifact,
    PackageableElement,
    uma::MethodElementProperty,
    uma::MethodElement,
    uma::ApplicableMetaClassInfo,
    ProcessElement,
    uma::PlanningData,
    uma::BreakdownElement,
    BreakdownElementDescription,
    uma::DescriptorDescription,
    uma::WorkProductType,
    uma::WorkProduct,
    uma::WorkProductDescription,
    uma::WorkOrder,
    uma::WorkBreakdownElement,
    Concept,
    uma::Whitepaper,
    uma::WorkDefinition,
    uma::TermDefinition,
    uma::Template,
    uma::TeamProfile,
    uma::ToolMentor,
    uma::Tool,
    uma::TaskDescription,
    uma::Task,
    uma::SupportingMaterial,
    uma::RoleSetGrouping,
    uma::RoleSet,
    Descriptor,
    uma::WorkProductDescriptor,
    uma::RoleDescriptor,
    uma::Roadmap,
    uma::ReusableAsset,
    uma::Report,
    uma::ActivityDescription,
    VariabilityType,
    WorkOrderType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_activitydescription_is_not_abstract():
    assert not inspect.isabstract(ActivityDescription)


def test_activitydescription_constructor_exists():
    assert callable(ActivityDescription.__init__)


def test_activitydescription_constructor_args():
    sig = inspect.signature(ActivityDescription.__init__)
    params = list(sig.parameters.keys())



def test_uma::processdescription_is_not_abstract():
    assert not inspect.isabstract(uma::ProcessDescription)


def test_uma::processdescription_constructor_exists():
    assert callable(uma::ProcessDescription.__init__)


def test_uma::processdescription_constructor_args():
    sig = inspect.signature(uma::ProcessDescription.__init__)
    params = list(sig.parameters.keys())
    assert "usageNotes" in params, "Missing parameter 'usageNotes'"
    assert "scope" in params, "Missing parameter 'scope'"

def test_uma::processdescription_has_usageNotes():
    assert hasattr(uma::ProcessDescription, "usageNotes")
    descriptor = None
    for klass in uma::ProcessDescription.__mro__:
        if "usageNotes" in klass.__dict__:
            descriptor = klass.__dict__["usageNotes"]
            break
    assert isinstance(descriptor, property)

def test_uma::processdescription_has_scope():
    assert hasattr(uma::ProcessDescription, "scope")
    descriptor = None
    for klass in uma::ProcessDescription.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_processpackage_is_not_abstract():
    assert not inspect.isabstract(ProcessPackage)


def test_processpackage_constructor_exists():
    assert callable(ProcessPackage.__init__)


def test_processpackage_constructor_args():
    sig = inspect.signature(ProcessPackage.__init__)
    params = list(sig.parameters.keys())



def test_uma::processcomponent_is_not_abstract():
    assert not inspect.isabstract(uma::ProcessComponent)


def test_uma::processcomponent_constructor_exists():
    assert callable(uma::ProcessComponent.__init__)


def test_uma::processcomponent_constructor_args():
    sig = inspect.signature(uma::ProcessComponent.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "copyright" in params, "Missing parameter 'copyright'"
    assert "changeDescription" in params, "Missing parameter 'changeDescription'"
    assert "authors" in params, "Missing parameter 'authors'"
    assert "changeDate" in params, "Missing parameter 'changeDate'"

def test_uma::processcomponent_has_version():
    assert hasattr(uma::ProcessComponent, "version")
    descriptor = None
    for klass in uma::ProcessComponent.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_uma::processcomponent_has_copyright():
    assert hasattr(uma::ProcessComponent, "copyright")
    descriptor = None
    for klass in uma::ProcessComponent.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)

def test_uma::processcomponent_has_changeDescription():
    assert hasattr(uma::ProcessComponent, "changeDescription")
    descriptor = None
    for klass in uma::ProcessComponent.__mro__:
        if "changeDescription" in klass.__dict__:
            descriptor = klass.__dict__["changeDescription"]
            break
    assert isinstance(descriptor, property)

def test_uma::processcomponent_has_authors():
    assert hasattr(uma::ProcessComponent, "authors")
    descriptor = None
    for klass in uma::ProcessComponent.__mro__:
        if "authors" in klass.__dict__:
            descriptor = klass.__dict__["authors"]
            break
    assert isinstance(descriptor, property)

def test_uma::processcomponent_has_changeDate():
    assert hasattr(uma::ProcessComponent, "changeDate")
    descriptor = None
    for klass in uma::ProcessComponent.__mro__:
        if "changeDate" in klass.__dict__:
            descriptor = klass.__dict__["changeDate"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::packageableelement_is_not_abstract():
    assert not inspect.isabstract(uma::PackageableElement)


def test_uma::packageableelement_constructor_exists():
    assert callable(uma::PackageableElement.__init__)


def test_uma::packageableelement_constructor_args():
    sig = inspect.signature(uma::PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_uma::namedelement_is_not_abstract():
    assert not inspect.isabstract(uma::NamedElement)


def test_uma::namedelement_constructor_exists():
    assert callable(uma::NamedElement.__init__)


def test_uma::namedelement_constructor_args():
    sig = inspect.signature(uma::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uma::namedelement_has_name():
    assert hasattr(uma::NamedElement, "name")
    descriptor = None
    for klass in uma::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_activity_is_not_abstract():
    assert not inspect.isabstract(Activity)


def test_activity_constructor_exists():
    assert callable(Activity.__init__)


def test_activity_constructor_args():
    sig = inspect.signature(Activity.__init__)
    params = list(sig.parameters.keys())



def test_uma::phase_is_not_abstract():
    assert not inspect.isabstract(uma::Phase)


def test_uma::phase_constructor_exists():
    assert callable(uma::Phase.__init__)


def test_uma::phase_constructor_args():
    sig = inspect.signature(uma::Phase.__init__)
    params = list(sig.parameters.keys())



def test_uma::process_is_not_abstract():
    assert not inspect.isabstract(uma::Process)


def test_uma::process_constructor_exists():
    assert callable(uma::Process.__init__)


def test_uma::process_constructor_args():
    sig = inspect.signature(uma::Process.__init__)
    params = list(sig.parameters.keys())
    assert "includesPattern" in params, "Missing parameter 'includesPattern'"
    assert "validContext" in params, "Missing parameter 'validContext'"
    assert "diagramURI" in params, "Missing parameter 'diagramURI'"
    assert "defaultContext" in params, "Missing parameter 'defaultContext'"

def test_uma::process_has_includesPattern():
    assert hasattr(uma::Process, "includesPattern")
    descriptor = None
    for klass in uma::Process.__mro__:
        if "includesPattern" in klass.__dict__:
            descriptor = klass.__dict__["includesPattern"]
            break
    assert isinstance(descriptor, property)

def test_uma::process_has_validContext():
    assert hasattr(uma::Process, "validContext")
    descriptor = None
    for klass in uma::Process.__mro__:
        if "validContext" in klass.__dict__:
            descriptor = klass.__dict__["validContext"]
            break
    assert isinstance(descriptor, property)

def test_uma::process_has_diagramURI():
    assert hasattr(uma::Process, "diagramURI")
    descriptor = None
    for klass in uma::Process.__mro__:
        if "diagramURI" in klass.__dict__:
            descriptor = klass.__dict__["diagramURI"]
            break
    assert isinstance(descriptor, property)

def test_uma::process_has_defaultContext():
    assert hasattr(uma::Process, "defaultContext")
    descriptor = None
    for klass in uma::Process.__mro__:
        if "defaultContext" in klass.__dict__:
            descriptor = klass.__dict__["defaultContext"]
            break
    assert isinstance(descriptor, property)



def test_uma::iteration_is_not_abstract():
    assert not inspect.isabstract(uma::Iteration)


def test_uma::iteration_constructor_exists():
    assert callable(uma::Iteration.__init__)


def test_uma::iteration_constructor_args():
    sig = inspect.signature(uma::Iteration.__init__)
    params = list(sig.parameters.keys())



def test_uma::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(uma::EStringToStringMapEntry)


def test_uma::estringtostringmapentry_constructor_exists():
    assert callable(uma::EStringToStringMapEntry.__init__)


def test_uma::estringtostringmapentry_constructor_args():
    sig = inspect.signature(uma::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_uma::element_is_not_abstract():
    assert not inspect.isabstract(uma::Element)


def test_uma::element_constructor_exists():
    assert callable(uma::Element.__init__)


def test_uma::element_constructor_args():
    sig = inspect.signature(uma::Element.__init__)
    params = list(sig.parameters.keys())



def test_breakdownelement_is_not_abstract():
    assert not inspect.isabstract(BreakdownElement)


def test_breakdownelement_constructor_exists():
    assert callable(BreakdownElement.__init__)


def test_breakdownelement_constructor_args():
    sig = inspect.signature(BreakdownElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::processcomponentinterface_is_not_abstract():
    assert not inspect.isabstract(uma::ProcessComponentInterface)


def test_uma::processcomponentinterface_constructor_exists():
    assert callable(uma::ProcessComponentInterface.__init__)


def test_uma::processcomponentinterface_constructor_args():
    sig = inspect.signature(uma::ProcessComponentInterface.__init__)
    params = list(sig.parameters.keys())
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma::processcomponentinterface_has_group2():
    assert hasattr(uma::ProcessComponentInterface, "group2")
    descriptor = None
    for klass in uma::ProcessComponentInterface.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma::descriptor_is_not_abstract():
    assert not inspect.isabstract(uma::Descriptor)


def test_uma::descriptor_constructor_exists():
    assert callable(uma::Descriptor.__init__)


def test_uma::descriptor_constructor_args():
    sig = inspect.signature(uma::Descriptor.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronizedWithSource" in params, "Missing parameter 'isSynchronizedWithSource'"

def test_uma::descriptor_has_isSynchronizedWithSource():
    assert hasattr(uma::Descriptor, "isSynchronizedWithSource")
    descriptor = None
    for klass in uma::Descriptor.__mro__:
        if "isSynchronizedWithSource" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronizedWithSource"]
            break
    assert isinstance(descriptor, property)



def test_uma::documentroot_is_not_abstract():
    assert not inspect.isabstract(uma::DocumentRoot)


def test_uma::documentroot_constructor_exists():
    assert callable(uma::DocumentRoot.__init__)


def test_uma::documentroot_constructor_args():
    sig = inspect.signature(uma::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_uma::documentroot_has_mixed():
    assert hasattr(uma::DocumentRoot, "mixed")
    descriptor = None
    for klass in uma::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_processdescription_is_not_abstract():
    assert not inspect.isabstract(ProcessDescription)


def test_processdescription_constructor_exists():
    assert callable(ProcessDescription.__init__)


def test_processdescription_constructor_args():
    sig = inspect.signature(ProcessDescription.__init__)
    params = list(sig.parameters.keys())



def test_uma::deliveryprocessdescription_is_not_abstract():
    assert not inspect.isabstract(uma::DeliveryProcessDescription)


def test_uma::deliveryprocessdescription_constructor_exists():
    assert callable(uma::DeliveryProcessDescription.__init__)


def test_uma::deliveryprocessdescription_constructor_args():
    sig = inspect.signature(uma::DeliveryProcessDescription.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"
    assert "estimatingTechnique" in params, "Missing parameter 'estimatingTechnique'"
    assert "typeOfContract" in params, "Missing parameter 'typeOfContract'"
    assert "riskLevel" in params, "Missing parameter 'riskLevel'"
    assert "projectCharacteristics" in params, "Missing parameter 'projectCharacteristics'"
    assert "projectMemberExpertise" in params, "Missing parameter 'projectMemberExpertise'"

def test_uma::deliveryprocessdescription_has_scale():
    assert hasattr(uma::DeliveryProcessDescription, "scale")
    descriptor = None
    for klass in uma::DeliveryProcessDescription.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_uma::deliveryprocessdescription_has_estimatingTechnique():
    assert hasattr(uma::DeliveryProcessDescription, "estimatingTechnique")
    descriptor = None
    for klass in uma::DeliveryProcessDescription.__mro__:
        if "estimatingTechnique" in klass.__dict__:
            descriptor = klass.__dict__["estimatingTechnique"]
            break
    assert isinstance(descriptor, property)

def test_uma::deliveryprocessdescription_has_typeOfContract():
    assert hasattr(uma::DeliveryProcessDescription, "typeOfContract")
    descriptor = None
    for klass in uma::DeliveryProcessDescription.__mro__:
        if "typeOfContract" in klass.__dict__:
            descriptor = klass.__dict__["typeOfContract"]
            break
    assert isinstance(descriptor, property)

def test_uma::deliveryprocessdescription_has_riskLevel():
    assert hasattr(uma::DeliveryProcessDescription, "riskLevel")
    descriptor = None
    for klass in uma::DeliveryProcessDescription.__mro__:
        if "riskLevel" in klass.__dict__:
            descriptor = klass.__dict__["riskLevel"]
            break
    assert isinstance(descriptor, property)

def test_uma::deliveryprocessdescription_has_projectCharacteristics():
    assert hasattr(uma::DeliveryProcessDescription, "projectCharacteristics")
    descriptor = None
    for klass in uma::DeliveryProcessDescription.__mro__:
        if "projectCharacteristics" in klass.__dict__:
            descriptor = klass.__dict__["projectCharacteristics"]
            break
    assert isinstance(descriptor, property)

def test_uma::deliveryprocessdescription_has_projectMemberExpertise():
    assert hasattr(uma::DeliveryProcessDescription, "projectMemberExpertise")
    descriptor = None
    for klass in uma::DeliveryProcessDescription.__mro__:
        if "projectMemberExpertise" in klass.__dict__:
            descriptor = klass.__dict__["projectMemberExpertise"]
            break
    assert isinstance(descriptor, property)



def test_contentcategory_is_not_abstract():
    assert not inspect.isabstract(ContentCategory)


def test_contentcategory_constructor_exists():
    assert callable(ContentCategory.__init__)


def test_contentcategory_constructor_args():
    sig = inspect.signature(ContentCategory.__init__)
    params = list(sig.parameters.keys())



def test_uma::disciplinegrouping_is_not_abstract():
    assert not inspect.isabstract(uma::DisciplineGrouping)


def test_uma::disciplinegrouping_constructor_exists():
    assert callable(uma::DisciplineGrouping.__init__)


def test_uma::disciplinegrouping_constructor_args():
    sig = inspect.signature(uma::DisciplineGrouping.__init__)
    params = list(sig.parameters.keys())
    assert "discipline" in params, "Missing parameter 'discipline'"
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma::disciplinegrouping_has_discipline():
    assert hasattr(uma::DisciplineGrouping, "discipline")
    descriptor = None
    for klass in uma::DisciplineGrouping.__mro__:
        if "discipline" in klass.__dict__:
            descriptor = klass.__dict__["discipline"]
            break
    assert isinstance(descriptor, property)

def test_uma::disciplinegrouping_has_group2():
    assert hasattr(uma::DisciplineGrouping, "group2")
    descriptor = None
    for klass in uma::DisciplineGrouping.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma::domain_is_not_abstract():
    assert not inspect.isabstract(uma::Domain)


def test_uma::domain_constructor_exists():
    assert callable(uma::Domain.__init__)


def test_uma::domain_constructor_args():
    sig = inspect.signature(uma::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "workProduct" in params, "Missing parameter 'workProduct'"
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma::domain_has_workProduct():
    assert hasattr(uma::Domain, "workProduct")
    descriptor = None
    for klass in uma::Domain.__mro__:
        if "workProduct" in klass.__dict__:
            descriptor = klass.__dict__["workProduct"]
            break
    assert isinstance(descriptor, property)

def test_uma::domain_has_group2():
    assert hasattr(uma::Domain, "group2")
    descriptor = None
    for klass in uma::Domain.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma::discipline_is_not_abstract():
    assert not inspect.isabstract(uma::Discipline)


def test_uma::discipline_constructor_exists():
    assert callable(uma::Discipline.__init__)


def test_uma::discipline_constructor_args():
    sig = inspect.signature(uma::Discipline.__init__)
    params = list(sig.parameters.keys())
    assert "referenceWorkflow" in params, "Missing parameter 'referenceWorkflow'"
    assert "task" in params, "Missing parameter 'task'"
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma::discipline_has_referenceWorkflow():
    assert hasattr(uma::Discipline, "referenceWorkflow")
    descriptor = None
    for klass in uma::Discipline.__mro__:
        if "referenceWorkflow" in klass.__dict__:
            descriptor = klass.__dict__["referenceWorkflow"]
            break
    assert isinstance(descriptor, property)

def test_uma::discipline_has_task():
    assert hasattr(uma::Discipline, "task")
    descriptor = None
    for klass in uma::Discipline.__mro__:
        if "task" in klass.__dict__:
            descriptor = klass.__dict__["task"]
            break
    assert isinstance(descriptor, property)

def test_uma::discipline_has_group2():
    assert hasattr(uma::Discipline, "group2")
    descriptor = None
    for klass in uma::Discipline.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma::customcategory_is_not_abstract():
    assert not inspect.isabstract(uma::CustomCategory)


def test_uma::customcategory_constructor_exists():
    assert callable(uma::CustomCategory.__init__)


def test_uma::customcategory_constructor_args():
    sig = inspect.signature(uma::CustomCategory.__init__)
    params = list(sig.parameters.keys())
    assert "categorizedElement" in params, "Missing parameter 'categorizedElement'"
    assert "group2" in params, "Missing parameter 'group2'"
    assert "subCategory" in params, "Missing parameter 'subCategory'"

def test_uma::customcategory_has_categorizedElement():
    assert hasattr(uma::CustomCategory, "categorizedElement")
    descriptor = None
    for klass in uma::CustomCategory.__mro__:
        if "categorizedElement" in klass.__dict__:
            descriptor = klass.__dict__["categorizedElement"]
            break
    assert isinstance(descriptor, property)

def test_uma::customcategory_has_group2():
    assert hasattr(uma::CustomCategory, "group2")
    descriptor = None
    for klass in uma::CustomCategory.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)

def test_uma::customcategory_has_subCategory():
    assert hasattr(uma::CustomCategory, "subCategory")
    descriptor = None
    for klass in uma::CustomCategory.__mro__:
        if "subCategory" in klass.__dict__:
            descriptor = klass.__dict__["subCategory"]
            break
    assert isinstance(descriptor, property)



def test_workbreakdownelement_is_not_abstract():
    assert not inspect.isabstract(WorkBreakdownElement)


def test_workbreakdownelement_constructor_exists():
    assert callable(WorkBreakdownElement.__init__)


def test_workbreakdownelement_constructor_args():
    sig = inspect.signature(WorkBreakdownElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::taskdescriptor_is_not_abstract():
    assert not inspect.isabstract(uma::TaskDescriptor)


def test_uma::taskdescriptor_constructor_exists():
    assert callable(uma::TaskDescriptor.__init__)


def test_uma::taskdescriptor_constructor_args():
    sig = inspect.signature(uma::TaskDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "performedPrimarilyBy" in params, "Missing parameter 'performedPrimarilyBy'"
    assert "assistedBy" in params, "Missing parameter 'assistedBy'"
    assert "externalInput" in params, "Missing parameter 'externalInput'"
    assert "mandatoryInput" in params, "Missing parameter 'mandatoryInput'"
    assert "group3" in params, "Missing parameter 'group3'"
    assert "additionallyPerformedBy" in params, "Missing parameter 'additionallyPerformedBy'"
    assert "optionalInput" in params, "Missing parameter 'optionalInput'"
    assert "isSynchronizedWithSource" in params, "Missing parameter 'isSynchronizedWithSource'"
    assert "task" in params, "Missing parameter 'task'"
    assert "output" in params, "Missing parameter 'output'"

def test_uma::taskdescriptor_has_performedPrimarilyBy():
    assert hasattr(uma::TaskDescriptor, "performedPrimarilyBy")
    descriptor = None
    for klass in uma::TaskDescriptor.__mro__:
        if "performedPrimarilyBy" in klass.__dict__:
            descriptor = klass.__dict__["performedPrimarilyBy"]
            break
    assert isinstance(descriptor, property)

def test_uma::taskdescriptor_has_assistedBy():
    assert hasattr(uma::TaskDescriptor, "assistedBy")
    descriptor = None
    for klass in uma::TaskDescriptor.__mro__:
        if "assistedBy" in klass.__dict__:
            descriptor = klass.__dict__["assistedBy"]
            break
    assert isinstance(descriptor, property)

def test_uma::taskdescriptor_has_externalInput():
    assert hasattr(uma::TaskDescriptor, "externalInput")
    descriptor = None
    for klass in uma::TaskDescriptor.__mro__:
        if "externalInput" in klass.__dict__:
            descriptor = klass.__dict__["externalInput"]
            break
    assert isinstance(descriptor, property)

def test_uma::taskdescriptor_has_mandatoryInput():
    assert hasattr(uma::TaskDescriptor, "mandatoryInput")
    descriptor = None
    for klass in uma::TaskDescriptor.__mro__:
        if "mandatoryInput" in klass.__dict__:
            descriptor = klass.__dict__["mandatoryInput"]
            break
    assert isinstance(descriptor, property)

def test_uma::taskdescriptor_has_group3():
    assert hasattr(uma::TaskDescriptor, "group3")
    descriptor = None
    for klass in uma::TaskDescriptor.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)

def test_uma::taskdescriptor_has_additionallyPerformedBy():
    assert hasattr(uma::TaskDescriptor, "additionallyPerformedBy")
    descriptor = None
    for klass in uma::TaskDescriptor.__mro__:
        if "additionallyPerformedBy" in klass.__dict__:
            descriptor = klass.__dict__["additionallyPerformedBy"]
            break
    assert isinstance(descriptor, property)

def test_uma::taskdescriptor_has_optionalInput():
    assert hasattr(uma::TaskDescriptor, "optionalInput")
    descriptor = None
    for klass in uma::TaskDescriptor.__mro__:
        if "optionalInput" in klass.__dict__:
            descriptor = klass.__dict__["optionalInput"]
            break
    assert isinstance(descriptor, property)

def test_uma::taskdescriptor_has_isSynchronizedWithSource():
    assert hasattr(uma::TaskDescriptor, "isSynchronizedWithSource")
    descriptor = None
    for klass in uma::TaskDescriptor.__mro__:
        if "isSynchronizedWithSource" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronizedWithSource"]
            break
    assert isinstance(descriptor, property)

def test_uma::taskdescriptor_has_task():
    assert hasattr(uma::TaskDescriptor, "task")
    descriptor = None
    for klass in uma::TaskDescriptor.__mro__:
        if "task" in klass.__dict__:
            descriptor = klass.__dict__["task"]
            break
    assert isinstance(descriptor, property)

def test_uma::taskdescriptor_has_output():
    assert hasattr(uma::TaskDescriptor, "output")
    descriptor = None
    for klass in uma::TaskDescriptor.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_uma::milestone_is_not_abstract():
    assert not inspect.isabstract(uma::Milestone)


def test_uma::milestone_constructor_exists():
    assert callable(uma::Milestone.__init__)


def test_uma::milestone_constructor_args():
    sig = inspect.signature(uma::Milestone.__init__)
    params = list(sig.parameters.keys())
    assert "requiredResult" in params, "Missing parameter 'requiredResult'"

def test_uma::milestone_has_requiredResult():
    assert hasattr(uma::Milestone, "requiredResult")
    descriptor = None
    for klass in uma::Milestone.__mro__:
        if "requiredResult" in klass.__dict__:
            descriptor = klass.__dict__["requiredResult"]
            break
    assert isinstance(descriptor, property)



def test_uma::activity_is_not_abstract():
    assert not inspect.isabstract(uma::Activity)


def test_uma::activity_constructor_exists():
    assert callable(uma::Activity.__init__)


def test_uma::activity_constructor_args():
    sig = inspect.signature(uma::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "group3" in params, "Missing parameter 'group3'"
    assert "roadmap" in params, "Missing parameter 'roadmap'"
    assert "variabilityBasedOnElement" in params, "Missing parameter 'variabilityBasedOnElement'"
    assert "postcondition" in params, "Missing parameter 'postcondition'"
    assert "variabilityType" in params, "Missing parameter 'variabilityType'"
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "isEnactable" in params, "Missing parameter 'isEnactable'"

def test_uma::activity_has_group3():
    assert hasattr(uma::Activity, "group3")
    descriptor = None
    for klass in uma::Activity.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)

def test_uma::activity_has_roadmap():
    assert hasattr(uma::Activity, "roadmap")
    descriptor = None
    for klass in uma::Activity.__mro__:
        if "roadmap" in klass.__dict__:
            descriptor = klass.__dict__["roadmap"]
            break
    assert isinstance(descriptor, property)

def test_uma::activity_has_variabilityBasedOnElement():
    assert hasattr(uma::Activity, "variabilityBasedOnElement")
    descriptor = None
    for klass in uma::Activity.__mro__:
        if "variabilityBasedOnElement" in klass.__dict__:
            descriptor = klass.__dict__["variabilityBasedOnElement"]
            break
    assert isinstance(descriptor, property)

def test_uma::activity_has_postcondition():
    assert hasattr(uma::Activity, "postcondition")
    descriptor = None
    for klass in uma::Activity.__mro__:
        if "postcondition" in klass.__dict__:
            descriptor = klass.__dict__["postcondition"]
            break
    assert isinstance(descriptor, property)

def test_uma::activity_has_variabilityType():
    assert hasattr(uma::Activity, "variabilityType")
    descriptor = None
    for klass in uma::Activity.__mro__:
        if "variabilityType" in klass.__dict__:
            descriptor = klass.__dict__["variabilityType"]
            break
    assert isinstance(descriptor, property)

def test_uma::activity_has_precondition():
    assert hasattr(uma::Activity, "precondition")
    descriptor = None
    for klass in uma::Activity.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_uma::activity_has_isEnactable():
    assert hasattr(uma::Activity, "isEnactable")
    descriptor = None
    for klass in uma::Activity.__mro__:
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



def test_uma::processelement_is_not_abstract():
    assert not inspect.isabstract(uma::ProcessElement)


def test_uma::processelement_constructor_exists():
    assert callable(uma::ProcessElement.__init__)


def test_uma::processelement_constructor_args():
    sig = inspect.signature(uma::ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::contentelement_is_not_abstract():
    assert not inspect.isabstract(uma::ContentElement)


def test_uma::contentelement_constructor_exists():
    assert callable(uma::ContentElement.__init__)


def test_uma::contentelement_constructor_args():
    sig = inspect.signature(uma::ContentElement.__init__)
    params = list(sig.parameters.keys())
    assert "variabilityBasedOnElement" in params, "Missing parameter 'variabilityBasedOnElement'"
    assert "guideline" in params, "Missing parameter 'guideline'"
    assert "concept" in params, "Missing parameter 'concept'"
    assert "supportingMaterial" in params, "Missing parameter 'supportingMaterial'"
    assert "variabilityType" in params, "Missing parameter 'variabilityType'"
    assert "checklist" in params, "Missing parameter 'checklist'"
    assert "reusableAsset" in params, "Missing parameter 'reusableAsset'"
    assert "whitepaper" in params, "Missing parameter 'whitepaper'"
    assert "group1" in params, "Missing parameter 'group1'"
    assert "example" in params, "Missing parameter 'example'"

def test_uma::contentelement_has_variabilityBasedOnElement():
    assert hasattr(uma::ContentElement, "variabilityBasedOnElement")
    descriptor = None
    for klass in uma::ContentElement.__mro__:
        if "variabilityBasedOnElement" in klass.__dict__:
            descriptor = klass.__dict__["variabilityBasedOnElement"]
            break
    assert isinstance(descriptor, property)

def test_uma::contentelement_has_guideline():
    assert hasattr(uma::ContentElement, "guideline")
    descriptor = None
    for klass in uma::ContentElement.__mro__:
        if "guideline" in klass.__dict__:
            descriptor = klass.__dict__["guideline"]
            break
    assert isinstance(descriptor, property)

def test_uma::contentelement_has_concept():
    assert hasattr(uma::ContentElement, "concept")
    descriptor = None
    for klass in uma::ContentElement.__mro__:
        if "concept" in klass.__dict__:
            descriptor = klass.__dict__["concept"]
            break
    assert isinstance(descriptor, property)

def test_uma::contentelement_has_supportingMaterial():
    assert hasattr(uma::ContentElement, "supportingMaterial")
    descriptor = None
    for klass in uma::ContentElement.__mro__:
        if "supportingMaterial" in klass.__dict__:
            descriptor = klass.__dict__["supportingMaterial"]
            break
    assert isinstance(descriptor, property)

def test_uma::contentelement_has_variabilityType():
    assert hasattr(uma::ContentElement, "variabilityType")
    descriptor = None
    for klass in uma::ContentElement.__mro__:
        if "variabilityType" in klass.__dict__:
            descriptor = klass.__dict__["variabilityType"]
            break
    assert isinstance(descriptor, property)

def test_uma::contentelement_has_checklist():
    assert hasattr(uma::ContentElement, "checklist")
    descriptor = None
    for klass in uma::ContentElement.__mro__:
        if "checklist" in klass.__dict__:
            descriptor = klass.__dict__["checklist"]
            break
    assert isinstance(descriptor, property)

def test_uma::contentelement_has_reusableAsset():
    assert hasattr(uma::ContentElement, "reusableAsset")
    descriptor = None
    for klass in uma::ContentElement.__mro__:
        if "reusableAsset" in klass.__dict__:
            descriptor = klass.__dict__["reusableAsset"]
            break
    assert isinstance(descriptor, property)

def test_uma::contentelement_has_whitepaper():
    assert hasattr(uma::ContentElement, "whitepaper")
    descriptor = None
    for klass in uma::ContentElement.__mro__:
        if "whitepaper" in klass.__dict__:
            descriptor = klass.__dict__["whitepaper"]
            break
    assert isinstance(descriptor, property)

def test_uma::contentelement_has_group1():
    assert hasattr(uma::ContentElement, "group1")
    descriptor = None
    for klass in uma::ContentElement.__mro__:
        if "group1" in klass.__dict__:
            descriptor = klass.__dict__["group1"]
            break
    assert isinstance(descriptor, property)

def test_uma::contentelement_has_example():
    assert hasattr(uma::ContentElement, "example")
    descriptor = None
    for klass in uma::ContentElement.__mro__:
        if "example" in klass.__dict__:
            descriptor = klass.__dict__["example"]
            break
    assert isinstance(descriptor, property)



def test_methodunit_is_not_abstract():
    assert not inspect.isabstract(MethodUnit)


def test_methodunit_constructor_exists():
    assert callable(MethodUnit.__init__)


def test_methodunit_constructor_args():
    sig = inspect.signature(MethodUnit.__init__)
    params = list(sig.parameters.keys())



def test_uma::methodconfiguration_is_not_abstract():
    assert not inspect.isabstract(uma::MethodConfiguration)


def test_uma::methodconfiguration_constructor_exists():
    assert callable(uma::MethodConfiguration.__init__)


def test_uma::methodconfiguration_constructor_args():
    sig = inspect.signature(uma::MethodConfiguration.__init__)
    params = list(sig.parameters.keys())
    assert "methodPackageSelection" in params, "Missing parameter 'methodPackageSelection'"
    assert "baseConfiguration" in params, "Missing parameter 'baseConfiguration'"
    assert "methodPluginSelection" in params, "Missing parameter 'methodPluginSelection'"
    assert "addedCategory" in params, "Missing parameter 'addedCategory'"
    assert "processView" in params, "Missing parameter 'processView'"
    assert "subtractedCategory" in params, "Missing parameter 'subtractedCategory'"
    assert "defaultView" in params, "Missing parameter 'defaultView'"

def test_uma::methodconfiguration_has_methodPackageSelection():
    assert hasattr(uma::MethodConfiguration, "methodPackageSelection")
    descriptor = None
    for klass in uma::MethodConfiguration.__mro__:
        if "methodPackageSelection" in klass.__dict__:
            descriptor = klass.__dict__["methodPackageSelection"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodconfiguration_has_baseConfiguration():
    assert hasattr(uma::MethodConfiguration, "baseConfiguration")
    descriptor = None
    for klass in uma::MethodConfiguration.__mro__:
        if "baseConfiguration" in klass.__dict__:
            descriptor = klass.__dict__["baseConfiguration"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodconfiguration_has_methodPluginSelection():
    assert hasattr(uma::MethodConfiguration, "methodPluginSelection")
    descriptor = None
    for klass in uma::MethodConfiguration.__mro__:
        if "methodPluginSelection" in klass.__dict__:
            descriptor = klass.__dict__["methodPluginSelection"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodconfiguration_has_addedCategory():
    assert hasattr(uma::MethodConfiguration, "addedCategory")
    descriptor = None
    for klass in uma::MethodConfiguration.__mro__:
        if "addedCategory" in klass.__dict__:
            descriptor = klass.__dict__["addedCategory"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodconfiguration_has_processView():
    assert hasattr(uma::MethodConfiguration, "processView")
    descriptor = None
    for klass in uma::MethodConfiguration.__mro__:
        if "processView" in klass.__dict__:
            descriptor = klass.__dict__["processView"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodconfiguration_has_subtractedCategory():
    assert hasattr(uma::MethodConfiguration, "subtractedCategory")
    descriptor = None
    for klass in uma::MethodConfiguration.__mro__:
        if "subtractedCategory" in klass.__dict__:
            descriptor = klass.__dict__["subtractedCategory"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodconfiguration_has_defaultView():
    assert hasattr(uma::MethodConfiguration, "defaultView")
    descriptor = None
    for klass in uma::MethodConfiguration.__mro__:
        if "defaultView" in klass.__dict__:
            descriptor = klass.__dict__["defaultView"]
            break
    assert isinstance(descriptor, property)



def test_uma::methodlibrary_is_not_abstract():
    assert not inspect.isabstract(uma::MethodLibrary)


def test_uma::methodlibrary_constructor_exists():
    assert callable(uma::MethodLibrary.__init__)


def test_uma::methodlibrary_constructor_args():
    sig = inspect.signature(uma::MethodLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "tool" in params, "Missing parameter 'tool'"

def test_uma::methodlibrary_has_tool():
    assert hasattr(uma::MethodLibrary, "tool")
    descriptor = None
    for klass in uma::MethodLibrary.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)



def test_uma::methodplugin_is_not_abstract():
    assert not inspect.isabstract(uma::MethodPlugin)


def test_uma::methodplugin_constructor_exists():
    assert callable(uma::MethodPlugin.__init__)


def test_uma::methodplugin_constructor_args():
    sig = inspect.signature(uma::MethodPlugin.__init__)
    params = list(sig.parameters.keys())
    assert "referencedMethodPlugin" in params, "Missing parameter 'referencedMethodPlugin'"
    assert "userChangeable" in params, "Missing parameter 'userChangeable'"
    assert "supporting" in params, "Missing parameter 'supporting'"

def test_uma::methodplugin_has_referencedMethodPlugin():
    assert hasattr(uma::MethodPlugin, "referencedMethodPlugin")
    descriptor = None
    for klass in uma::MethodPlugin.__mro__:
        if "referencedMethodPlugin" in klass.__dict__:
            descriptor = klass.__dict__["referencedMethodPlugin"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodplugin_has_userChangeable():
    assert hasattr(uma::MethodPlugin, "userChangeable")
    descriptor = None
    for klass in uma::MethodPlugin.__mro__:
        if "userChangeable" in klass.__dict__:
            descriptor = klass.__dict__["userChangeable"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodplugin_has_supporting():
    assert hasattr(uma::MethodPlugin, "supporting")
    descriptor = None
    for klass in uma::MethodPlugin.__mro__:
        if "supporting" in klass.__dict__:
            descriptor = klass.__dict__["supporting"]
            break
    assert isinstance(descriptor, property)



def test_uma::contentdescription_is_not_abstract():
    assert not inspect.isabstract(uma::ContentDescription)


def test_uma::contentdescription_constructor_exists():
    assert callable(uma::ContentDescription.__init__)


def test_uma::contentdescription_constructor_args():
    sig = inspect.signature(uma::ContentDescription.__init__)
    params = list(sig.parameters.keys())
    assert "mainDescription" in params, "Missing parameter 'mainDescription'"
    assert "keyConsiderations" in params, "Missing parameter 'keyConsiderations'"
    assert "externalId" in params, "Missing parameter 'externalId'"

def test_uma::contentdescription_has_mainDescription():
    assert hasattr(uma::ContentDescription, "mainDescription")
    descriptor = None
    for klass in uma::ContentDescription.__mro__:
        if "mainDescription" in klass.__dict__:
            descriptor = klass.__dict__["mainDescription"]
            break
    assert isinstance(descriptor, property)

def test_uma::contentdescription_has_keyConsiderations():
    assert hasattr(uma::ContentDescription, "keyConsiderations")
    descriptor = None
    for klass in uma::ContentDescription.__mro__:
        if "keyConsiderations" in klass.__dict__:
            descriptor = klass.__dict__["keyConsiderations"]
            break
    assert isinstance(descriptor, property)

def test_uma::contentdescription_has_externalId():
    assert hasattr(uma::ContentDescription, "externalId")
    descriptor = None
    for klass in uma::ContentDescription.__mro__:
        if "externalId" in klass.__dict__:
            descriptor = klass.__dict__["externalId"]
            break
    assert isinstance(descriptor, property)



def test_methodpackage_is_not_abstract():
    assert not inspect.isabstract(MethodPackage)


def test_methodpackage_constructor_exists():
    assert callable(MethodPackage.__init__)


def test_methodpackage_constructor_args():
    sig = inspect.signature(MethodPackage.__init__)
    params = list(sig.parameters.keys())



def test_uma::contentpackage_is_not_abstract():
    assert not inspect.isabstract(uma::ContentPackage)


def test_uma::contentpackage_constructor_exists():
    assert callable(uma::ContentPackage.__init__)


def test_uma::contentpackage_constructor_args():
    sig = inspect.signature(uma::ContentPackage.__init__)
    params = list(sig.parameters.keys())
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma::contentpackage_has_group2():
    assert hasattr(uma::ContentPackage, "group2")
    descriptor = None
    for klass in uma::ContentPackage.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma::processpackage_is_not_abstract():
    assert not inspect.isabstract(uma::ProcessPackage)


def test_uma::processpackage_constructor_exists():
    assert callable(uma::ProcessPackage.__init__)


def test_uma::processpackage_constructor_args():
    sig = inspect.signature(uma::ProcessPackage.__init__)
    params = list(sig.parameters.keys())
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma::processpackage_has_group2():
    assert hasattr(uma::ProcessPackage, "group2")
    descriptor = None
    for klass in uma::ProcessPackage.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma::contentcategorypackage_is_not_abstract():
    assert not inspect.isabstract(uma::ContentCategoryPackage)


def test_uma::contentcategorypackage_constructor_exists():
    assert callable(uma::ContentCategoryPackage.__init__)


def test_uma::contentcategorypackage_constructor_args():
    sig = inspect.signature(uma::ContentCategoryPackage.__init__)
    params = list(sig.parameters.keys())
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma::contentcategorypackage_has_group2():
    assert hasattr(uma::ContentCategoryPackage, "group2")
    descriptor = None
    for klass in uma::ContentCategoryPackage.__mro__:
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



def test_uma::compositerole_is_not_abstract():
    assert not inspect.isabstract(uma::CompositeRole)


def test_uma::compositerole_constructor_exists():
    assert callable(uma::CompositeRole.__init__)


def test_uma::compositerole_constructor_args():
    sig = inspect.signature(uma::CompositeRole.__init__)
    params = list(sig.parameters.keys())
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma::compositerole_has_group2():
    assert hasattr(uma::CompositeRole, "group2")
    descriptor = None
    for klass in uma::CompositeRole.__mro__:
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



def test_uma::practice_is_not_abstract():
    assert not inspect.isabstract(uma::Practice)


def test_uma::practice_constructor_exists():
    assert callable(uma::Practice.__init__)


def test_uma::practice_constructor_args():
    sig = inspect.signature(uma::Practice.__init__)
    params = list(sig.parameters.keys())
    assert "activityReference" in params, "Missing parameter 'activityReference'"
    assert "group2" in params, "Missing parameter 'group2'"
    assert "contentReference" in params, "Missing parameter 'contentReference'"

def test_uma::practice_has_activityReference():
    assert hasattr(uma::Practice, "activityReference")
    descriptor = None
    for klass in uma::Practice.__mro__:
        if "activityReference" in klass.__dict__:
            descriptor = klass.__dict__["activityReference"]
            break
    assert isinstance(descriptor, property)

def test_uma::practice_has_group2():
    assert hasattr(uma::Practice, "group2")
    descriptor = None
    for klass in uma::Practice.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)

def test_uma::practice_has_contentReference():
    assert hasattr(uma::Practice, "contentReference")
    descriptor = None
    for klass in uma::Practice.__mro__:
        if "contentReference" in klass.__dict__:
            descriptor = klass.__dict__["contentReference"]
            break
    assert isinstance(descriptor, property)



def test_uma::example_is_not_abstract():
    assert not inspect.isabstract(uma::Example)


def test_uma::example_constructor_exists():
    assert callable(uma::Example.__init__)


def test_uma::example_constructor_args():
    sig = inspect.signature(uma::Example.__init__)
    params = list(sig.parameters.keys())



def test_uma::estimatingmetric_is_not_abstract():
    assert not inspect.isabstract(uma::EstimatingMetric)


def test_uma::estimatingmetric_constructor_exists():
    assert callable(uma::EstimatingMetric.__init__)


def test_uma::estimatingmetric_constructor_args():
    sig = inspect.signature(uma::EstimatingMetric.__init__)
    params = list(sig.parameters.keys())



def test_uma::estimationconsiderations_is_not_abstract():
    assert not inspect.isabstract(uma::EstimationConsiderations)


def test_uma::estimationconsiderations_constructor_exists():
    assert callable(uma::EstimationConsiderations.__init__)


def test_uma::estimationconsiderations_constructor_args():
    sig = inspect.signature(uma::EstimationConsiderations.__init__)
    params = list(sig.parameters.keys())



def test_uma::estimate_is_not_abstract():
    assert not inspect.isabstract(uma::Estimate)


def test_uma::estimate_constructor_exists():
    assert callable(uma::Estimate.__init__)


def test_uma::estimate_constructor_args():
    sig = inspect.signature(uma::Estimate.__init__)
    params = list(sig.parameters.keys())
    assert "estimationConsiderations" in params, "Missing parameter 'estimationConsiderations'"
    assert "estimationMetric" in params, "Missing parameter 'estimationMetric'"
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma::estimate_has_estimationConsiderations():
    assert hasattr(uma::Estimate, "estimationConsiderations")
    descriptor = None
    for klass in uma::Estimate.__mro__:
        if "estimationConsiderations" in klass.__dict__:
            descriptor = klass.__dict__["estimationConsiderations"]
            break
    assert isinstance(descriptor, property)

def test_uma::estimate_has_estimationMetric():
    assert hasattr(uma::Estimate, "estimationMetric")
    descriptor = None
    for klass in uma::Estimate.__mro__:
        if "estimationMetric" in klass.__dict__:
            descriptor = klass.__dict__["estimationMetric"]
            break
    assert isinstance(descriptor, property)

def test_uma::estimate_has_group2():
    assert hasattr(uma::Estimate, "group2")
    descriptor = None
    for klass in uma::Estimate.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma::guideline_is_not_abstract():
    assert not inspect.isabstract(uma::Guideline)


def test_uma::guideline_constructor_exists():
    assert callable(uma::Guideline.__init__)


def test_uma::guideline_constructor_args():
    sig = inspect.signature(uma::Guideline.__init__)
    params = list(sig.parameters.keys())



def test_uma::concept_is_not_abstract():
    assert not inspect.isabstract(uma::Concept)


def test_uma::concept_constructor_exists():
    assert callable(uma::Concept.__init__)


def test_uma::concept_constructor_args():
    sig = inspect.signature(uma::Concept.__init__)
    params = list(sig.parameters.keys())



def test_uma::checklist_is_not_abstract():
    assert not inspect.isabstract(uma::Checklist)


def test_uma::checklist_constructor_exists():
    assert callable(uma::Checklist.__init__)


def test_uma::checklist_constructor_args():
    sig = inspect.signature(uma::Checklist.__init__)
    params = list(sig.parameters.keys())



def test_process_is_not_abstract():
    assert not inspect.isabstract(Process)


def test_process_constructor_exists():
    assert callable(Process.__init__)


def test_process_constructor_args():
    sig = inspect.signature(Process.__init__)
    params = list(sig.parameters.keys())



def test_uma::processplanningtemplate_is_not_abstract():
    assert not inspect.isabstract(uma::ProcessPlanningTemplate)


def test_uma::processplanningtemplate_constructor_exists():
    assert callable(uma::ProcessPlanningTemplate.__init__)


def test_uma::processplanningtemplate_constructor_args():
    sig = inspect.signature(uma::ProcessPlanningTemplate.__init__)
    params = list(sig.parameters.keys())
    assert "group4" in params, "Missing parameter 'group4'"
    assert "baseProcess" in params, "Missing parameter 'baseProcess'"

def test_uma::processplanningtemplate_has_group4():
    assert hasattr(uma::ProcessPlanningTemplate, "group4")
    descriptor = None
    for klass in uma::ProcessPlanningTemplate.__mro__:
        if "group4" in klass.__dict__:
            descriptor = klass.__dict__["group4"]
            break
    assert isinstance(descriptor, property)

def test_uma::processplanningtemplate_has_baseProcess():
    assert hasattr(uma::ProcessPlanningTemplate, "baseProcess")
    descriptor = None
    for klass in uma::ProcessPlanningTemplate.__mro__:
        if "baseProcess" in klass.__dict__:
            descriptor = klass.__dict__["baseProcess"]
            break
    assert isinstance(descriptor, property)



def test_uma::deliveryprocess_is_not_abstract():
    assert not inspect.isabstract(uma::DeliveryProcess)


def test_uma::deliveryprocess_constructor_exists():
    assert callable(uma::DeliveryProcess.__init__)


def test_uma::deliveryprocess_constructor_args():
    sig = inspect.signature(uma::DeliveryProcess.__init__)
    params = list(sig.parameters.keys())
    assert "educationMaterial" in params, "Missing parameter 'educationMaterial'"
    assert "communicationsMaterial" in params, "Missing parameter 'communicationsMaterial'"
    assert "group4" in params, "Missing parameter 'group4'"

def test_uma::deliveryprocess_has_educationMaterial():
    assert hasattr(uma::DeliveryProcess, "educationMaterial")
    descriptor = None
    for klass in uma::DeliveryProcess.__mro__:
        if "educationMaterial" in klass.__dict__:
            descriptor = klass.__dict__["educationMaterial"]
            break
    assert isinstance(descriptor, property)

def test_uma::deliveryprocess_has_communicationsMaterial():
    assert hasattr(uma::DeliveryProcess, "communicationsMaterial")
    descriptor = None
    for klass in uma::DeliveryProcess.__mro__:
        if "communicationsMaterial" in klass.__dict__:
            descriptor = klass.__dict__["communicationsMaterial"]
            break
    assert isinstance(descriptor, property)

def test_uma::deliveryprocess_has_group4():
    assert hasattr(uma::DeliveryProcess, "group4")
    descriptor = None
    for klass in uma::DeliveryProcess.__mro__:
        if "group4" in klass.__dict__:
            descriptor = klass.__dict__["group4"]
            break
    assert isinstance(descriptor, property)



def test_uma::capabilitypattern_is_not_abstract():
    assert not inspect.isabstract(uma::CapabilityPattern)


def test_uma::capabilitypattern_constructor_exists():
    assert callable(uma::CapabilityPattern.__init__)


def test_uma::capabilitypattern_constructor_args():
    sig = inspect.signature(uma::CapabilityPattern.__init__)
    params = list(sig.parameters.keys())



def test_contentelement_is_not_abstract():
    assert not inspect.isabstract(ContentElement)


def test_contentelement_constructor_exists():
    assert callable(ContentElement.__init__)


def test_contentelement_constructor_args():
    sig = inspect.signature(ContentElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::role_is_not_abstract():
    assert not inspect.isabstract(uma::Role)


def test_uma::role_constructor_exists():
    assert callable(uma::Role.__init__)


def test_uma::role_constructor_args():
    sig = inspect.signature(uma::Role.__init__)
    params = list(sig.parameters.keys())
    assert "responsibleFor" in params, "Missing parameter 'responsibleFor'"
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma::role_has_responsibleFor():
    assert hasattr(uma::Role, "responsibleFor")
    descriptor = None
    for klass in uma::Role.__mro__:
        if "responsibleFor" in klass.__dict__:
            descriptor = klass.__dict__["responsibleFor"]
            break
    assert isinstance(descriptor, property)

def test_uma::role_has_group2():
    assert hasattr(uma::Role, "group2")
    descriptor = None
    for klass in uma::Role.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma::guidance_is_not_abstract():
    assert not inspect.isabstract(uma::Guidance)


def test_uma::guidance_constructor_exists():
    assert callable(uma::Guidance.__init__)


def test_uma::guidance_constructor_args():
    sig = inspect.signature(uma::Guidance.__init__)
    params = list(sig.parameters.keys())



def test_uma::kind_is_not_abstract():
    assert not inspect.isabstract(uma::Kind)


def test_uma::kind_constructor_exists():
    assert callable(uma::Kind.__init__)


def test_uma::kind_constructor_args():
    sig = inspect.signature(uma::Kind.__init__)
    params = list(sig.parameters.keys())
    assert "applicableMetaClassInfo" in params, "Missing parameter 'applicableMetaClassInfo'"

def test_uma::kind_has_applicableMetaClassInfo():
    assert hasattr(uma::Kind, "applicableMetaClassInfo")
    descriptor = None
    for klass in uma::Kind.__mro__:
        if "applicableMetaClassInfo" in klass.__dict__:
            descriptor = klass.__dict__["applicableMetaClassInfo"]
            break
    assert isinstance(descriptor, property)



def test_uma::contentcategory_is_not_abstract():
    assert not inspect.isabstract(uma::ContentCategory)


def test_uma::contentcategory_constructor_exists():
    assert callable(uma::ContentCategory.__init__)


def test_uma::contentcategory_constructor_args():
    sig = inspect.signature(uma::ContentCategory.__init__)
    params = list(sig.parameters.keys())



def test_methodelement_is_not_abstract():
    assert not inspect.isabstract(MethodElement)


def test_methodelement_constructor_exists():
    assert callable(MethodElement.__init__)


def test_methodelement_constructor_args():
    sig = inspect.signature(MethodElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::methodpackage_is_not_abstract():
    assert not inspect.isabstract(uma::MethodPackage)


def test_uma::methodpackage_constructor_exists():
    assert callable(uma::MethodPackage.__init__)


def test_uma::methodpackage_constructor_args():
    sig = inspect.signature(uma::MethodPackage.__init__)
    params = list(sig.parameters.keys())
    assert "global_" in params, "Missing parameter 'global_'"
    assert "group1" in params, "Missing parameter 'group1'"
    assert "reusedPackage" in params, "Missing parameter 'reusedPackage'"

def test_uma::methodpackage_has_global_():
    assert hasattr(uma::MethodPackage, "global_")
    descriptor = None
    for klass in uma::MethodPackage.__mro__:
        if "global_" in klass.__dict__:
            descriptor = klass.__dict__["global_"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodpackage_has_group1():
    assert hasattr(uma::MethodPackage, "group1")
    descriptor = None
    for klass in uma::MethodPackage.__mro__:
        if "group1" in klass.__dict__:
            descriptor = klass.__dict__["group1"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodpackage_has_reusedPackage():
    assert hasattr(uma::MethodPackage, "reusedPackage")
    descriptor = None
    for klass in uma::MethodPackage.__mro__:
        if "reusedPackage" in klass.__dict__:
            descriptor = klass.__dict__["reusedPackage"]
            break
    assert isinstance(descriptor, property)



def test_uma::methodunit_is_not_abstract():
    assert not inspect.isabstract(uma::MethodUnit)


def test_uma::methodunit_constructor_exists():
    assert callable(uma::MethodUnit.__init__)


def test_uma::methodunit_constructor_args():
    sig = inspect.signature(uma::MethodUnit.__init__)
    params = list(sig.parameters.keys())
    assert "authors" in params, "Missing parameter 'authors'"
    assert "copyright" in params, "Missing parameter 'copyright'"
    assert "changeDate" in params, "Missing parameter 'changeDate'"
    assert "version" in params, "Missing parameter 'version'"
    assert "changeDescription" in params, "Missing parameter 'changeDescription'"

def test_uma::methodunit_has_authors():
    assert hasattr(uma::MethodUnit, "authors")
    descriptor = None
    for klass in uma::MethodUnit.__mro__:
        if "authors" in klass.__dict__:
            descriptor = klass.__dict__["authors"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodunit_has_copyright():
    assert hasattr(uma::MethodUnit, "copyright")
    descriptor = None
    for klass in uma::MethodUnit.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodunit_has_changeDate():
    assert hasattr(uma::MethodUnit, "changeDate")
    descriptor = None
    for klass in uma::MethodUnit.__mro__:
        if "changeDate" in klass.__dict__:
            descriptor = klass.__dict__["changeDate"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodunit_has_version():
    assert hasattr(uma::MethodUnit, "version")
    descriptor = None
    for klass in uma::MethodUnit.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodunit_has_changeDescription():
    assert hasattr(uma::MethodUnit, "changeDescription")
    descriptor = None
    for klass in uma::MethodUnit.__mro__:
        if "changeDescription" in klass.__dict__:
            descriptor = klass.__dict__["changeDescription"]
            break
    assert isinstance(descriptor, property)



def test_uma::section_is_not_abstract():
    assert not inspect.isabstract(uma::Section)


def test_uma::section_constructor_exists():
    assert callable(uma::Section.__init__)


def test_uma::section_constructor_args():
    sig = inspect.signature(uma::Section.__init__)
    params = list(sig.parameters.keys())
    assert "sectionName" in params, "Missing parameter 'sectionName'"
    assert "variabilityType" in params, "Missing parameter 'variabilityType'"
    assert "predecessor" in params, "Missing parameter 'predecessor'"
    assert "variabilityBasedOnElement" in params, "Missing parameter 'variabilityBasedOnElement'"
    assert "description" in params, "Missing parameter 'description'"

def test_uma::section_has_sectionName():
    assert hasattr(uma::Section, "sectionName")
    descriptor = None
    for klass in uma::Section.__mro__:
        if "sectionName" in klass.__dict__:
            descriptor = klass.__dict__["sectionName"]
            break
    assert isinstance(descriptor, property)

def test_uma::section_has_variabilityType():
    assert hasattr(uma::Section, "variabilityType")
    descriptor = None
    for klass in uma::Section.__mro__:
        if "variabilityType" in klass.__dict__:
            descriptor = klass.__dict__["variabilityType"]
            break
    assert isinstance(descriptor, property)

def test_uma::section_has_predecessor():
    assert hasattr(uma::Section, "predecessor")
    descriptor = None
    for klass in uma::Section.__mro__:
        if "predecessor" in klass.__dict__:
            descriptor = klass.__dict__["predecessor"]
            break
    assert isinstance(descriptor, property)

def test_uma::section_has_variabilityBasedOnElement():
    assert hasattr(uma::Section, "variabilityBasedOnElement")
    descriptor = None
    for klass in uma::Section.__mro__:
        if "variabilityBasedOnElement" in klass.__dict__:
            descriptor = klass.__dict__["variabilityBasedOnElement"]
            break
    assert isinstance(descriptor, property)

def test_uma::section_has_description():
    assert hasattr(uma::Section, "description")
    descriptor = None
    for klass in uma::Section.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_uma::describableelement_is_not_abstract():
    assert not inspect.isabstract(uma::DescribableElement)


def test_uma::describableelement_constructor_exists():
    assert callable(uma::DescribableElement.__init__)


def test_uma::describableelement_constructor_args():
    sig = inspect.signature(uma::DescribableElement.__init__)
    params = list(sig.parameters.keys())
    assert "shapeicon" in params, "Missing parameter 'shapeicon'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "nodeicon" in params, "Missing parameter 'nodeicon'"
    assert "fulfill" in params, "Missing parameter 'fulfill'"

def test_uma::describableelement_has_shapeicon():
    assert hasattr(uma::DescribableElement, "shapeicon")
    descriptor = None
    for klass in uma::DescribableElement.__mro__:
        if "shapeicon" in klass.__dict__:
            descriptor = klass.__dict__["shapeicon"]
            break
    assert isinstance(descriptor, property)

def test_uma::describableelement_has_isAbstract():
    assert hasattr(uma::DescribableElement, "isAbstract")
    descriptor = None
    for klass in uma::DescribableElement.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_uma::describableelement_has_nodeicon():
    assert hasattr(uma::DescribableElement, "nodeicon")
    descriptor = None
    for klass in uma::DescribableElement.__mro__:
        if "nodeicon" in klass.__dict__:
            descriptor = klass.__dict__["nodeicon"]
            break
    assert isinstance(descriptor, property)

def test_uma::describableelement_has_fulfill():
    assert hasattr(uma::DescribableElement, "fulfill")
    descriptor = None
    for klass in uma::DescribableElement.__mro__:
        if "fulfill" in klass.__dict__:
            descriptor = klass.__dict__["fulfill"]
            break
    assert isinstance(descriptor, property)



def test_uma::constraint_is_not_abstract():
    assert not inspect.isabstract(uma::Constraint)


def test_uma::constraint_constructor_exists():
    assert callable(uma::Constraint.__init__)


def test_uma::constraint_constructor_args():
    sig = inspect.signature(uma::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "mainDescription" in params, "Missing parameter 'mainDescription'"

def test_uma::constraint_has_mainDescription():
    assert hasattr(uma::Constraint, "mainDescription")
    descriptor = None
    for klass in uma::Constraint.__mro__:
        if "mainDescription" in klass.__dict__:
            descriptor = klass.__dict__["mainDescription"]
            break
    assert isinstance(descriptor, property)



def test_contentdescription_is_not_abstract():
    assert not inspect.isabstract(ContentDescription)


def test_contentdescription_constructor_exists():
    assert callable(ContentDescription.__init__)


def test_contentdescription_constructor_args():
    sig = inspect.signature(ContentDescription.__init__)
    params = list(sig.parameters.keys())



def test_uma::guidancedescription_is_not_abstract():
    assert not inspect.isabstract(uma::GuidanceDescription)


def test_uma::guidancedescription_constructor_exists():
    assert callable(uma::GuidanceDescription.__init__)


def test_uma::guidancedescription_constructor_args():
    sig = inspect.signature(uma::GuidanceDescription.__init__)
    params = list(sig.parameters.keys())
    assert "attachment" in params, "Missing parameter 'attachment'"

def test_uma::guidancedescription_has_attachment():
    assert hasattr(uma::GuidanceDescription, "attachment")
    descriptor = None
    for klass in uma::GuidanceDescription.__mro__:
        if "attachment" in klass.__dict__:
            descriptor = klass.__dict__["attachment"]
            break
    assert isinstance(descriptor, property)



def test_uma::practicedescription_is_not_abstract():
    assert not inspect.isabstract(uma::PracticeDescription)


def test_uma::practicedescription_constructor_exists():
    assert callable(uma::PracticeDescription.__init__)


def test_uma::practicedescription_constructor_args():
    sig = inspect.signature(uma::PracticeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "application" in params, "Missing parameter 'application'"
    assert "goals" in params, "Missing parameter 'goals'"
    assert "background" in params, "Missing parameter 'background'"
    assert "levelsOfAdoption" in params, "Missing parameter 'levelsOfAdoption'"
    assert "problem" in params, "Missing parameter 'problem'"
    assert "additionalInfo" in params, "Missing parameter 'additionalInfo'"

def test_uma::practicedescription_has_application():
    assert hasattr(uma::PracticeDescription, "application")
    descriptor = None
    for klass in uma::PracticeDescription.__mro__:
        if "application" in klass.__dict__:
            descriptor = klass.__dict__["application"]
            break
    assert isinstance(descriptor, property)

def test_uma::practicedescription_has_goals():
    assert hasattr(uma::PracticeDescription, "goals")
    descriptor = None
    for klass in uma::PracticeDescription.__mro__:
        if "goals" in klass.__dict__:
            descriptor = klass.__dict__["goals"]
            break
    assert isinstance(descriptor, property)

def test_uma::practicedescription_has_background():
    assert hasattr(uma::PracticeDescription, "background")
    descriptor = None
    for klass in uma::PracticeDescription.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_uma::practicedescription_has_levelsOfAdoption():
    assert hasattr(uma::PracticeDescription, "levelsOfAdoption")
    descriptor = None
    for klass in uma::PracticeDescription.__mro__:
        if "levelsOfAdoption" in klass.__dict__:
            descriptor = klass.__dict__["levelsOfAdoption"]
            break
    assert isinstance(descriptor, property)

def test_uma::practicedescription_has_problem():
    assert hasattr(uma::PracticeDescription, "problem")
    descriptor = None
    for klass in uma::PracticeDescription.__mro__:
        if "problem" in klass.__dict__:
            descriptor = klass.__dict__["problem"]
            break
    assert isinstance(descriptor, property)

def test_uma::practicedescription_has_additionalInfo():
    assert hasattr(uma::PracticeDescription, "additionalInfo")
    descriptor = None
    for klass in uma::PracticeDescription.__mro__:
        if "additionalInfo" in klass.__dict__:
            descriptor = klass.__dict__["additionalInfo"]
            break
    assert isinstance(descriptor, property)



def test_uma::roledescription_is_not_abstract():
    assert not inspect.isabstract(uma::RoleDescription)


def test_uma::roledescription_constructor_exists():
    assert callable(uma::RoleDescription.__init__)


def test_uma::roledescription_constructor_args():
    sig = inspect.signature(uma::RoleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "assignmentApproaches" in params, "Missing parameter 'assignmentApproaches'"
    assert "skills" in params, "Missing parameter 'skills'"
    assert "synonyms" in params, "Missing parameter 'synonyms'"

def test_uma::roledescription_has_assignmentApproaches():
    assert hasattr(uma::RoleDescription, "assignmentApproaches")
    descriptor = None
    for klass in uma::RoleDescription.__mro__:
        if "assignmentApproaches" in klass.__dict__:
            descriptor = klass.__dict__["assignmentApproaches"]
            break
    assert isinstance(descriptor, property)

def test_uma::roledescription_has_skills():
    assert hasattr(uma::RoleDescription, "skills")
    descriptor = None
    for klass in uma::RoleDescription.__mro__:
        if "skills" in klass.__dict__:
            descriptor = klass.__dict__["skills"]
            break
    assert isinstance(descriptor, property)

def test_uma::roledescription_has_synonyms():
    assert hasattr(uma::RoleDescription, "synonyms")
    descriptor = None
    for klass in uma::RoleDescription.__mro__:
        if "synonyms" in klass.__dict__:
            descriptor = klass.__dict__["synonyms"]
            break
    assert isinstance(descriptor, property)



def test_uma::breakdownelementdescription_is_not_abstract():
    assert not inspect.isabstract(uma::BreakdownElementDescription)


def test_uma::breakdownelementdescription_constructor_exists():
    assert callable(uma::BreakdownElementDescription.__init__)


def test_uma::breakdownelementdescription_constructor_args():
    sig = inspect.signature(uma::BreakdownElementDescription.__init__)
    params = list(sig.parameters.keys())
    assert "usageGuidance" in params, "Missing parameter 'usageGuidance'"

def test_uma::breakdownelementdescription_has_usageGuidance():
    assert hasattr(uma::BreakdownElementDescription, "usageGuidance")
    descriptor = None
    for klass in uma::BreakdownElementDescription.__mro__:
        if "usageGuidance" in klass.__dict__:
            descriptor = klass.__dict__["usageGuidance"]
            break
    assert isinstance(descriptor, property)



def test_workproductdescription_is_not_abstract():
    assert not inspect.isabstract(WorkProductDescription)


def test_workproductdescription_constructor_exists():
    assert callable(WorkProductDescription.__init__)


def test_workproductdescription_constructor_args():
    sig = inspect.signature(WorkProductDescription.__init__)
    params = list(sig.parameters.keys())



def test_uma::deliverabledescription_is_not_abstract():
    assert not inspect.isabstract(uma::DeliverableDescription)


def test_uma::deliverabledescription_constructor_exists():
    assert callable(uma::DeliverableDescription.__init__)


def test_uma::deliverabledescription_constructor_args():
    sig = inspect.signature(uma::DeliverableDescription.__init__)
    params = list(sig.parameters.keys())
    assert "externalDescription" in params, "Missing parameter 'externalDescription'"
    assert "packagingGuidance" in params, "Missing parameter 'packagingGuidance'"

def test_uma::deliverabledescription_has_externalDescription():
    assert hasattr(uma::DeliverableDescription, "externalDescription")
    descriptor = None
    for klass in uma::DeliverableDescription.__mro__:
        if "externalDescription" in klass.__dict__:
            descriptor = klass.__dict__["externalDescription"]
            break
    assert isinstance(descriptor, property)

def test_uma::deliverabledescription_has_packagingGuidance():
    assert hasattr(uma::DeliverableDescription, "packagingGuidance")
    descriptor = None
    for klass in uma::DeliverableDescription.__mro__:
        if "packagingGuidance" in klass.__dict__:
            descriptor = klass.__dict__["packagingGuidance"]
            break
    assert isinstance(descriptor, property)



def test_uma::artifactdescription_is_not_abstract():
    assert not inspect.isabstract(uma::ArtifactDescription)


def test_uma::artifactdescription_constructor_exists():
    assert callable(uma::ArtifactDescription.__init__)


def test_uma::artifactdescription_constructor_args():
    sig = inspect.signature(uma::ArtifactDescription.__init__)
    params = list(sig.parameters.keys())
    assert "notation" in params, "Missing parameter 'notation'"
    assert "representation" in params, "Missing parameter 'representation'"
    assert "representationOptions" in params, "Missing parameter 'representationOptions'"
    assert "briefOutline" in params, "Missing parameter 'briefOutline'"

def test_uma::artifactdescription_has_notation():
    assert hasattr(uma::ArtifactDescription, "notation")
    descriptor = None
    for klass in uma::ArtifactDescription.__mro__:
        if "notation" in klass.__dict__:
            descriptor = klass.__dict__["notation"]
            break
    assert isinstance(descriptor, property)

def test_uma::artifactdescription_has_representation():
    assert hasattr(uma::ArtifactDescription, "representation")
    descriptor = None
    for klass in uma::ArtifactDescription.__mro__:
        if "representation" in klass.__dict__:
            descriptor = klass.__dict__["representation"]
            break
    assert isinstance(descriptor, property)

def test_uma::artifactdescription_has_representationOptions():
    assert hasattr(uma::ArtifactDescription, "representationOptions")
    descriptor = None
    for klass in uma::ArtifactDescription.__mro__:
        if "representationOptions" in klass.__dict__:
            descriptor = klass.__dict__["representationOptions"]
            break
    assert isinstance(descriptor, property)

def test_uma::artifactdescription_has_briefOutline():
    assert hasattr(uma::ArtifactDescription, "briefOutline")
    descriptor = None
    for klass in uma::ArtifactDescription.__mro__:
        if "briefOutline" in klass.__dict__:
            descriptor = klass.__dict__["briefOutline"]
            break
    assert isinstance(descriptor, property)



def test_workproduct_is_not_abstract():
    assert not inspect.isabstract(WorkProduct)


def test_workproduct_constructor_exists():
    assert callable(WorkProduct.__init__)


def test_workproduct_constructor_args():
    sig = inspect.signature(WorkProduct.__init__)
    params = list(sig.parameters.keys())



def test_uma::outcome_is_not_abstract():
    assert not inspect.isabstract(uma::Outcome)


def test_uma::outcome_constructor_exists():
    assert callable(uma::Outcome.__init__)


def test_uma::outcome_constructor_args():
    sig = inspect.signature(uma::Outcome.__init__)
    params = list(sig.parameters.keys())



def test_uma::deliverable_is_not_abstract():
    assert not inspect.isabstract(uma::Deliverable)


def test_uma::deliverable_constructor_exists():
    assert callable(uma::Deliverable.__init__)


def test_uma::deliverable_constructor_args():
    sig = inspect.signature(uma::Deliverable.__init__)
    params = list(sig.parameters.keys())
    assert "group3" in params, "Missing parameter 'group3'"
    assert "deliveredWorkProduct" in params, "Missing parameter 'deliveredWorkProduct'"

def test_uma::deliverable_has_group3():
    assert hasattr(uma::Deliverable, "group3")
    descriptor = None
    for klass in uma::Deliverable.__mro__:
        if "group3" in klass.__dict__:
            descriptor = klass.__dict__["group3"]
            break
    assert isinstance(descriptor, property)

def test_uma::deliverable_has_deliveredWorkProduct():
    assert hasattr(uma::Deliverable, "deliveredWorkProduct")
    descriptor = None
    for klass in uma::Deliverable.__mro__:
        if "deliveredWorkProduct" in klass.__dict__:
            descriptor = klass.__dict__["deliveredWorkProduct"]
            break
    assert isinstance(descriptor, property)



def test_uma::artifact_is_not_abstract():
    assert not inspect.isabstract(uma::Artifact)


def test_uma::artifact_constructor_exists():
    assert callable(uma::Artifact.__init__)


def test_uma::artifact_constructor_args():
    sig = inspect.signature(uma::Artifact.__init__)
    params = list(sig.parameters.keys())
    assert "group3" in params, "Missing parameter 'group3'"

def test_uma::artifact_has_group3():
    assert hasattr(uma::Artifact, "group3")
    descriptor = None
    for klass in uma::Artifact.__mro__:
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



def test_uma::methodelementproperty_is_not_abstract():
    assert not inspect.isabstract(uma::MethodElementProperty)


def test_uma::methodelementproperty_constructor_exists():
    assert callable(uma::MethodElementProperty.__init__)


def test_uma::methodelementproperty_constructor_args():
    sig = inspect.signature(uma::MethodElementProperty.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uma::methodelementproperty_has_value():
    assert hasattr(uma::MethodElementProperty, "value")
    descriptor = None
    for klass in uma::MethodElementProperty.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uma::methodelement_is_not_abstract():
    assert not inspect.isabstract(uma::MethodElement)


def test_uma::methodelement_constructor_exists():
    assert callable(uma::MethodElement.__init__)


def test_uma::methodelement_constructor_args():
    sig = inspect.signature(uma::MethodElement.__init__)
    params = list(sig.parameters.keys())
    assert "orderingGuide" in params, "Missing parameter 'orderingGuide'"
    assert "group" in params, "Missing parameter 'group'"
    assert "presentationName" in params, "Missing parameter 'presentationName'"
    assert "id" in params, "Missing parameter 'id'"
    assert "suppressed" in params, "Missing parameter 'suppressed'"
    assert "briefDescription" in params, "Missing parameter 'briefDescription'"

def test_uma::methodelement_has_orderingGuide():
    assert hasattr(uma::MethodElement, "orderingGuide")
    descriptor = None
    for klass in uma::MethodElement.__mro__:
        if "orderingGuide" in klass.__dict__:
            descriptor = klass.__dict__["orderingGuide"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodelement_has_group():
    assert hasattr(uma::MethodElement, "group")
    descriptor = None
    for klass in uma::MethodElement.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodelement_has_presentationName():
    assert hasattr(uma::MethodElement, "presentationName")
    descriptor = None
    for klass in uma::MethodElement.__mro__:
        if "presentationName" in klass.__dict__:
            descriptor = klass.__dict__["presentationName"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodelement_has_id():
    assert hasattr(uma::MethodElement, "id")
    descriptor = None
    for klass in uma::MethodElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodelement_has_suppressed():
    assert hasattr(uma::MethodElement, "suppressed")
    descriptor = None
    for klass in uma::MethodElement.__mro__:
        if "suppressed" in klass.__dict__:
            descriptor = klass.__dict__["suppressed"]
            break
    assert isinstance(descriptor, property)

def test_uma::methodelement_has_briefDescription():
    assert hasattr(uma::MethodElement, "briefDescription")
    descriptor = None
    for klass in uma::MethodElement.__mro__:
        if "briefDescription" in klass.__dict__:
            descriptor = klass.__dict__["briefDescription"]
            break
    assert isinstance(descriptor, property)



def test_uma::applicablemetaclassinfo_is_not_abstract():
    assert not inspect.isabstract(uma::ApplicableMetaClassInfo)


def test_uma::applicablemetaclassinfo_constructor_exists():
    assert callable(uma::ApplicableMetaClassInfo.__init__)


def test_uma::applicablemetaclassinfo_constructor_args():
    sig = inspect.signature(uma::ApplicableMetaClassInfo.__init__)
    params = list(sig.parameters.keys())
    assert "isPrimaryExtension" in params, "Missing parameter 'isPrimaryExtension'"

def test_uma::applicablemetaclassinfo_has_isPrimaryExtension():
    assert hasattr(uma::ApplicableMetaClassInfo, "isPrimaryExtension")
    descriptor = None
    for klass in uma::ApplicableMetaClassInfo.__mro__:
        if "isPrimaryExtension" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryExtension"]
            break
    assert isinstance(descriptor, property)



def test_processelement_is_not_abstract():
    assert not inspect.isabstract(ProcessElement)


def test_processelement_constructor_exists():
    assert callable(ProcessElement.__init__)


def test_processelement_constructor_args():
    sig = inspect.signature(ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::planningdata_is_not_abstract():
    assert not inspect.isabstract(uma::PlanningData)


def test_uma::planningdata_constructor_exists():
    assert callable(uma::PlanningData.__init__)


def test_uma::planningdata_constructor_args():
    sig = inspect.signature(uma::PlanningData.__init__)
    params = list(sig.parameters.keys())
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "rank" in params, "Missing parameter 'rank'"
    assert "finishDate" in params, "Missing parameter 'finishDate'"

def test_uma::planningdata_has_startDate():
    assert hasattr(uma::PlanningData, "startDate")
    descriptor = None
    for klass in uma::PlanningData.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_uma::planningdata_has_rank():
    assert hasattr(uma::PlanningData, "rank")
    descriptor = None
    for klass in uma::PlanningData.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)

def test_uma::planningdata_has_finishDate():
    assert hasattr(uma::PlanningData, "finishDate")
    descriptor = None
    for klass in uma::PlanningData.__mro__:
        if "finishDate" in klass.__dict__:
            descriptor = klass.__dict__["finishDate"]
            break
    assert isinstance(descriptor, property)



def test_uma::breakdownelement_is_not_abstract():
    assert not inspect.isabstract(uma::BreakdownElement)


def test_uma::breakdownelement_constructor_exists():
    assert callable(uma::BreakdownElement.__init__)


def test_uma::breakdownelement_constructor_args():
    sig = inspect.signature(uma::BreakdownElement.__init__)
    params = list(sig.parameters.keys())
    assert "presentedBefore" in params, "Missing parameter 'presentedBefore'"
    assert "isPlanned" in params, "Missing parameter 'isPlanned'"
    assert "concept" in params, "Missing parameter 'concept'"
    assert "example" in params, "Missing parameter 'example'"
    assert "hasMultipleOccurrences" in params, "Missing parameter 'hasMultipleOccurrences'"
    assert "group1" in params, "Missing parameter 'group1'"
    assert "isOptional" in params, "Missing parameter 'isOptional'"
    assert "superActivity" in params, "Missing parameter 'superActivity'"
    assert "guideline" in params, "Missing parameter 'guideline'"
    assert "whitepaper" in params, "Missing parameter 'whitepaper'"
    assert "presentedAfter" in params, "Missing parameter 'presentedAfter'"
    assert "checklist" in params, "Missing parameter 'checklist'"
    assert "prefix" in params, "Missing parameter 'prefix'"
    assert "reusableAsset" in params, "Missing parameter 'reusableAsset'"
    assert "supportingMaterial" in params, "Missing parameter 'supportingMaterial'"
    assert "planningData" in params, "Missing parameter 'planningData'"

def test_uma::breakdownelement_has_presentedBefore():
    assert hasattr(uma::BreakdownElement, "presentedBefore")
    descriptor = None
    for klass in uma::BreakdownElement.__mro__:
        if "presentedBefore" in klass.__dict__:
            descriptor = klass.__dict__["presentedBefore"]
            break
    assert isinstance(descriptor, property)

def test_uma::breakdownelement_has_isPlanned():
    assert hasattr(uma::BreakdownElement, "isPlanned")
    descriptor = None
    for klass in uma::BreakdownElement.__mro__:
        if "isPlanned" in klass.__dict__:
            descriptor = klass.__dict__["isPlanned"]
            break
    assert isinstance(descriptor, property)

def test_uma::breakdownelement_has_concept():
    assert hasattr(uma::BreakdownElement, "concept")
    descriptor = None
    for klass in uma::BreakdownElement.__mro__:
        if "concept" in klass.__dict__:
            descriptor = klass.__dict__["concept"]
            break
    assert isinstance(descriptor, property)

def test_uma::breakdownelement_has_example():
    assert hasattr(uma::BreakdownElement, "example")
    descriptor = None
    for klass in uma::BreakdownElement.__mro__:
        if "example" in klass.__dict__:
            descriptor = klass.__dict__["example"]
            break
    assert isinstance(descriptor, property)

def test_uma::breakdownelement_has_hasMultipleOccurrences():
    assert hasattr(uma::BreakdownElement, "hasMultipleOccurrences")
    descriptor = None
    for klass in uma::BreakdownElement.__mro__:
        if "hasMultipleOccurrences" in klass.__dict__:
            descriptor = klass.__dict__["hasMultipleOccurrences"]
            break
    assert isinstance(descriptor, property)

def test_uma::breakdownelement_has_group1():
    assert hasattr(uma::BreakdownElement, "group1")
    descriptor = None
    for klass in uma::BreakdownElement.__mro__:
        if "group1" in klass.__dict__:
            descriptor = klass.__dict__["group1"]
            break
    assert isinstance(descriptor, property)

def test_uma::breakdownelement_has_isOptional():
    assert hasattr(uma::BreakdownElement, "isOptional")
    descriptor = None
    for klass in uma::BreakdownElement.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)

def test_uma::breakdownelement_has_superActivity():
    assert hasattr(uma::BreakdownElement, "superActivity")
    descriptor = None
    for klass in uma::BreakdownElement.__mro__:
        if "superActivity" in klass.__dict__:
            descriptor = klass.__dict__["superActivity"]
            break
    assert isinstance(descriptor, property)

def test_uma::breakdownelement_has_guideline():
    assert hasattr(uma::BreakdownElement, "guideline")
    descriptor = None
    for klass in uma::BreakdownElement.__mro__:
        if "guideline" in klass.__dict__:
            descriptor = klass.__dict__["guideline"]
            break
    assert isinstance(descriptor, property)

def test_uma::breakdownelement_has_whitepaper():
    assert hasattr(uma::BreakdownElement, "whitepaper")
    descriptor = None
    for klass in uma::BreakdownElement.__mro__:
        if "whitepaper" in klass.__dict__:
            descriptor = klass.__dict__["whitepaper"]
            break
    assert isinstance(descriptor, property)

def test_uma::breakdownelement_has_presentedAfter():
    assert hasattr(uma::BreakdownElement, "presentedAfter")
    descriptor = None
    for klass in uma::BreakdownElement.__mro__:
        if "presentedAfter" in klass.__dict__:
            descriptor = klass.__dict__["presentedAfter"]
            break
    assert isinstance(descriptor, property)

def test_uma::breakdownelement_has_checklist():
    assert hasattr(uma::BreakdownElement, "checklist")
    descriptor = None
    for klass in uma::BreakdownElement.__mro__:
        if "checklist" in klass.__dict__:
            descriptor = klass.__dict__["checklist"]
            break
    assert isinstance(descriptor, property)

def test_uma::breakdownelement_has_prefix():
    assert hasattr(uma::BreakdownElement, "prefix")
    descriptor = None
    for klass in uma::BreakdownElement.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)

def test_uma::breakdownelement_has_reusableAsset():
    assert hasattr(uma::BreakdownElement, "reusableAsset")
    descriptor = None
    for klass in uma::BreakdownElement.__mro__:
        if "reusableAsset" in klass.__dict__:
            descriptor = klass.__dict__["reusableAsset"]
            break
    assert isinstance(descriptor, property)

def test_uma::breakdownelement_has_supportingMaterial():
    assert hasattr(uma::BreakdownElement, "supportingMaterial")
    descriptor = None
    for klass in uma::BreakdownElement.__mro__:
        if "supportingMaterial" in klass.__dict__:
            descriptor = klass.__dict__["supportingMaterial"]
            break
    assert isinstance(descriptor, property)

def test_uma::breakdownelement_has_planningData():
    assert hasattr(uma::BreakdownElement, "planningData")
    descriptor = None
    for klass in uma::BreakdownElement.__mro__:
        if "planningData" in klass.__dict__:
            descriptor = klass.__dict__["planningData"]
            break
    assert isinstance(descriptor, property)



def test_breakdownelementdescription_is_not_abstract():
    assert not inspect.isabstract(BreakdownElementDescription)


def test_breakdownelementdescription_constructor_exists():
    assert callable(BreakdownElementDescription.__init__)


def test_breakdownelementdescription_constructor_args():
    sig = inspect.signature(BreakdownElementDescription.__init__)
    params = list(sig.parameters.keys())



def test_uma::descriptordescription_is_not_abstract():
    assert not inspect.isabstract(uma::DescriptorDescription)


def test_uma::descriptordescription_constructor_exists():
    assert callable(uma::DescriptorDescription.__init__)


def test_uma::descriptordescription_constructor_args():
    sig = inspect.signature(uma::DescriptorDescription.__init__)
    params = list(sig.parameters.keys())
    assert "refinedDescription" in params, "Missing parameter 'refinedDescription'"

def test_uma::descriptordescription_has_refinedDescription():
    assert hasattr(uma::DescriptorDescription, "refinedDescription")
    descriptor = None
    for klass in uma::DescriptorDescription.__mro__:
        if "refinedDescription" in klass.__dict__:
            descriptor = klass.__dict__["refinedDescription"]
            break
    assert isinstance(descriptor, property)



def test_uma::workproducttype_is_not_abstract():
    assert not inspect.isabstract(uma::WorkProductType)


def test_uma::workproducttype_constructor_exists():
    assert callable(uma::WorkProductType.__init__)


def test_uma::workproducttype_constructor_args():
    sig = inspect.signature(uma::WorkProductType.__init__)
    params = list(sig.parameters.keys())
    assert "workProduct" in params, "Missing parameter 'workProduct'"
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma::workproducttype_has_workProduct():
    assert hasattr(uma::WorkProductType, "workProduct")
    descriptor = None
    for klass in uma::WorkProductType.__mro__:
        if "workProduct" in klass.__dict__:
            descriptor = klass.__dict__["workProduct"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproducttype_has_group2():
    assert hasattr(uma::WorkProductType, "group2")
    descriptor = None
    for klass in uma::WorkProductType.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma::workproduct_is_not_abstract():
    assert not inspect.isabstract(uma::WorkProduct)


def test_uma::workproduct_constructor_exists():
    assert callable(uma::WorkProduct.__init__)


def test_uma::workproduct_constructor_args():
    sig = inspect.signature(uma::WorkProduct.__init__)
    params = list(sig.parameters.keys())
    assert "estimate" in params, "Missing parameter 'estimate'"
    assert "estimationConsiderations" in params, "Missing parameter 'estimationConsiderations'"
    assert "toolMentor" in params, "Missing parameter 'toolMentor'"
    assert "template" in params, "Missing parameter 'template'"
    assert "report" in params, "Missing parameter 'report'"
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma::workproduct_has_estimate():
    assert hasattr(uma::WorkProduct, "estimate")
    descriptor = None
    for klass in uma::WorkProduct.__mro__:
        if "estimate" in klass.__dict__:
            descriptor = klass.__dict__["estimate"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproduct_has_estimationConsiderations():
    assert hasattr(uma::WorkProduct, "estimationConsiderations")
    descriptor = None
    for klass in uma::WorkProduct.__mro__:
        if "estimationConsiderations" in klass.__dict__:
            descriptor = klass.__dict__["estimationConsiderations"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproduct_has_toolMentor():
    assert hasattr(uma::WorkProduct, "toolMentor")
    descriptor = None
    for klass in uma::WorkProduct.__mro__:
        if "toolMentor" in klass.__dict__:
            descriptor = klass.__dict__["toolMentor"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproduct_has_template():
    assert hasattr(uma::WorkProduct, "template")
    descriptor = None
    for klass in uma::WorkProduct.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproduct_has_report():
    assert hasattr(uma::WorkProduct, "report")
    descriptor = None
    for klass in uma::WorkProduct.__mro__:
        if "report" in klass.__dict__:
            descriptor = klass.__dict__["report"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproduct_has_group2():
    assert hasattr(uma::WorkProduct, "group2")
    descriptor = None
    for klass in uma::WorkProduct.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma::workproductdescription_is_not_abstract():
    assert not inspect.isabstract(uma::WorkProductDescription)


def test_uma::workproductdescription_constructor_exists():
    assert callable(uma::WorkProductDescription.__init__)


def test_uma::workproductdescription_constructor_args():
    sig = inspect.signature(uma::WorkProductDescription.__init__)
    params = list(sig.parameters.keys())
    assert "reasonsForNotNeeding" in params, "Missing parameter 'reasonsForNotNeeding'"
    assert "impactOfNotHaving" in params, "Missing parameter 'impactOfNotHaving'"
    assert "purpose" in params, "Missing parameter 'purpose'"

def test_uma::workproductdescription_has_reasonsForNotNeeding():
    assert hasattr(uma::WorkProductDescription, "reasonsForNotNeeding")
    descriptor = None
    for klass in uma::WorkProductDescription.__mro__:
        if "reasonsForNotNeeding" in klass.__dict__:
            descriptor = klass.__dict__["reasonsForNotNeeding"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproductdescription_has_impactOfNotHaving():
    assert hasattr(uma::WorkProductDescription, "impactOfNotHaving")
    descriptor = None
    for klass in uma::WorkProductDescription.__mro__:
        if "impactOfNotHaving" in klass.__dict__:
            descriptor = klass.__dict__["impactOfNotHaving"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproductdescription_has_purpose():
    assert hasattr(uma::WorkProductDescription, "purpose")
    descriptor = None
    for klass in uma::WorkProductDescription.__mro__:
        if "purpose" in klass.__dict__:
            descriptor = klass.__dict__["purpose"]
            break
    assert isinstance(descriptor, property)



def test_uma::workorder_is_not_abstract():
    assert not inspect.isabstract(uma::WorkOrder)


def test_uma::workorder_constructor_exists():
    assert callable(uma::WorkOrder.__init__)


def test_uma::workorder_constructor_args():
    sig = inspect.signature(uma::WorkOrder.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "properties" in params, "Missing parameter 'properties'"
    assert "value" in params, "Missing parameter 'value'"
    assert "linkType" in params, "Missing parameter 'linkType'"

def test_uma::workorder_has_id():
    assert hasattr(uma::WorkOrder, "id")
    descriptor = None
    for klass in uma::WorkOrder.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_uma::workorder_has_properties():
    assert hasattr(uma::WorkOrder, "properties")
    descriptor = None
    for klass in uma::WorkOrder.__mro__:
        if "properties" in klass.__dict__:
            descriptor = klass.__dict__["properties"]
            break
    assert isinstance(descriptor, property)

def test_uma::workorder_has_value():
    assert hasattr(uma::WorkOrder, "value")
    descriptor = None
    for klass in uma::WorkOrder.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_uma::workorder_has_linkType():
    assert hasattr(uma::WorkOrder, "linkType")
    descriptor = None
    for klass in uma::WorkOrder.__mro__:
        if "linkType" in klass.__dict__:
            descriptor = klass.__dict__["linkType"]
            break
    assert isinstance(descriptor, property)



def test_uma::workbreakdownelement_is_not_abstract():
    assert not inspect.isabstract(uma::WorkBreakdownElement)


def test_uma::workbreakdownelement_constructor_exists():
    assert callable(uma::WorkBreakdownElement.__init__)


def test_uma::workbreakdownelement_constructor_args():
    sig = inspect.signature(uma::WorkBreakdownElement.__init__)
    params = list(sig.parameters.keys())
    assert "group2" in params, "Missing parameter 'group2'"
    assert "isEventDriven" in params, "Missing parameter 'isEventDriven'"
    assert "isRepeatable" in params, "Missing parameter 'isRepeatable'"
    assert "isOngoing" in params, "Missing parameter 'isOngoing'"

def test_uma::workbreakdownelement_has_group2():
    assert hasattr(uma::WorkBreakdownElement, "group2")
    descriptor = None
    for klass in uma::WorkBreakdownElement.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)

def test_uma::workbreakdownelement_has_isEventDriven():
    assert hasattr(uma::WorkBreakdownElement, "isEventDriven")
    descriptor = None
    for klass in uma::WorkBreakdownElement.__mro__:
        if "isEventDriven" in klass.__dict__:
            descriptor = klass.__dict__["isEventDriven"]
            break
    assert isinstance(descriptor, property)

def test_uma::workbreakdownelement_has_isRepeatable():
    assert hasattr(uma::WorkBreakdownElement, "isRepeatable")
    descriptor = None
    for klass in uma::WorkBreakdownElement.__mro__:
        if "isRepeatable" in klass.__dict__:
            descriptor = klass.__dict__["isRepeatable"]
            break
    assert isinstance(descriptor, property)

def test_uma::workbreakdownelement_has_isOngoing():
    assert hasattr(uma::WorkBreakdownElement, "isOngoing")
    descriptor = None
    for klass in uma::WorkBreakdownElement.__mro__:
        if "isOngoing" in klass.__dict__:
            descriptor = klass.__dict__["isOngoing"]
            break
    assert isinstance(descriptor, property)



def test_concept_is_not_abstract():
    assert not inspect.isabstract(Concept)


def test_concept_constructor_exists():
    assert callable(Concept.__init__)


def test_concept_constructor_args():
    sig = inspect.signature(Concept.__init__)
    params = list(sig.parameters.keys())



def test_uma::whitepaper_is_not_abstract():
    assert not inspect.isabstract(uma::Whitepaper)


def test_uma::whitepaper_constructor_exists():
    assert callable(uma::Whitepaper.__init__)


def test_uma::whitepaper_constructor_args():
    sig = inspect.signature(uma::Whitepaper.__init__)
    params = list(sig.parameters.keys())



def test_uma::workdefinition_is_not_abstract():
    assert not inspect.isabstract(uma::WorkDefinition)


def test_uma::workdefinition_constructor_exists():
    assert callable(uma::WorkDefinition.__init__)


def test_uma::workdefinition_constructor_args():
    sig = inspect.signature(uma::WorkDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "postcondition" in params, "Missing parameter 'postcondition'"

def test_uma::workdefinition_has_precondition():
    assert hasattr(uma::WorkDefinition, "precondition")
    descriptor = None
    for klass in uma::WorkDefinition.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_uma::workdefinition_has_postcondition():
    assert hasattr(uma::WorkDefinition, "postcondition")
    descriptor = None
    for klass in uma::WorkDefinition.__mro__:
        if "postcondition" in klass.__dict__:
            descriptor = klass.__dict__["postcondition"]
            break
    assert isinstance(descriptor, property)



def test_uma::termdefinition_is_not_abstract():
    assert not inspect.isabstract(uma::TermDefinition)


def test_uma::termdefinition_constructor_exists():
    assert callable(uma::TermDefinition.__init__)


def test_uma::termdefinition_constructor_args():
    sig = inspect.signature(uma::TermDefinition.__init__)
    params = list(sig.parameters.keys())



def test_uma::template_is_not_abstract():
    assert not inspect.isabstract(uma::Template)


def test_uma::template_constructor_exists():
    assert callable(uma::Template.__init__)


def test_uma::template_constructor_args():
    sig = inspect.signature(uma::Template.__init__)
    params = list(sig.parameters.keys())



def test_uma::teamprofile_is_not_abstract():
    assert not inspect.isabstract(uma::TeamProfile)


def test_uma::teamprofile_constructor_exists():
    assert callable(uma::TeamProfile.__init__)


def test_uma::teamprofile_constructor_args():
    sig = inspect.signature(uma::TeamProfile.__init__)
    params = list(sig.parameters.keys())
    assert "superTeam" in params, "Missing parameter 'superTeam'"
    assert "subTeam" in params, "Missing parameter 'subTeam'"
    assert "group2" in params, "Missing parameter 'group2'"
    assert "role" in params, "Missing parameter 'role'"

def test_uma::teamprofile_has_superTeam():
    assert hasattr(uma::TeamProfile, "superTeam")
    descriptor = None
    for klass in uma::TeamProfile.__mro__:
        if "superTeam" in klass.__dict__:
            descriptor = klass.__dict__["superTeam"]
            break
    assert isinstance(descriptor, property)

def test_uma::teamprofile_has_subTeam():
    assert hasattr(uma::TeamProfile, "subTeam")
    descriptor = None
    for klass in uma::TeamProfile.__mro__:
        if "subTeam" in klass.__dict__:
            descriptor = klass.__dict__["subTeam"]
            break
    assert isinstance(descriptor, property)

def test_uma::teamprofile_has_group2():
    assert hasattr(uma::TeamProfile, "group2")
    descriptor = None
    for klass in uma::TeamProfile.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)

def test_uma::teamprofile_has_role():
    assert hasattr(uma::TeamProfile, "role")
    descriptor = None
    for klass in uma::TeamProfile.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)



def test_uma::toolmentor_is_not_abstract():
    assert not inspect.isabstract(uma::ToolMentor)


def test_uma::toolmentor_constructor_exists():
    assert callable(uma::ToolMentor.__init__)


def test_uma::toolmentor_constructor_args():
    sig = inspect.signature(uma::ToolMentor.__init__)
    params = list(sig.parameters.keys())



def test_uma::tool_is_not_abstract():
    assert not inspect.isabstract(uma::Tool)


def test_uma::tool_constructor_exists():
    assert callable(uma::Tool.__init__)


def test_uma::tool_constructor_args():
    sig = inspect.signature(uma::Tool.__init__)
    params = list(sig.parameters.keys())
    assert "toolMentor" in params, "Missing parameter 'toolMentor'"
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma::tool_has_toolMentor():
    assert hasattr(uma::Tool, "toolMentor")
    descriptor = None
    for klass in uma::Tool.__mro__:
        if "toolMentor" in klass.__dict__:
            descriptor = klass.__dict__["toolMentor"]
            break
    assert isinstance(descriptor, property)

def test_uma::tool_has_group2():
    assert hasattr(uma::Tool, "group2")
    descriptor = None
    for klass in uma::Tool.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma::taskdescription_is_not_abstract():
    assert not inspect.isabstract(uma::TaskDescription)


def test_uma::taskdescription_constructor_exists():
    assert callable(uma::TaskDescription.__init__)


def test_uma::taskdescription_constructor_args():
    sig = inspect.signature(uma::TaskDescription.__init__)
    params = list(sig.parameters.keys())
    assert "purpose" in params, "Missing parameter 'purpose'"
    assert "alternatives" in params, "Missing parameter 'alternatives'"

def test_uma::taskdescription_has_purpose():
    assert hasattr(uma::TaskDescription, "purpose")
    descriptor = None
    for klass in uma::TaskDescription.__mro__:
        if "purpose" in klass.__dict__:
            descriptor = klass.__dict__["purpose"]
            break
    assert isinstance(descriptor, property)

def test_uma::taskdescription_has_alternatives():
    assert hasattr(uma::TaskDescription, "alternatives")
    descriptor = None
    for klass in uma::TaskDescription.__mro__:
        if "alternatives" in klass.__dict__:
            descriptor = klass.__dict__["alternatives"]
            break
    assert isinstance(descriptor, property)



def test_uma::task_is_not_abstract():
    assert not inspect.isabstract(uma::Task)


def test_uma::task_constructor_exists():
    assert callable(uma::Task.__init__)


def test_uma::task_constructor_args():
    sig = inspect.signature(uma::Task.__init__)
    params = list(sig.parameters.keys())
    assert "performedBy" in params, "Missing parameter 'performedBy'"
    assert "estimationConsiderations" in params, "Missing parameter 'estimationConsiderations'"
    assert "optionalInput" in params, "Missing parameter 'optionalInput'"
    assert "estimate" in params, "Missing parameter 'estimate'"
    assert "group2" in params, "Missing parameter 'group2'"
    assert "output" in params, "Missing parameter 'output'"
    assert "mandatoryInput" in params, "Missing parameter 'mandatoryInput'"
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "additionallyPerformedBy" in params, "Missing parameter 'additionallyPerformedBy'"
    assert "toolMentor" in params, "Missing parameter 'toolMentor'"
    assert "postcondition" in params, "Missing parameter 'postcondition'"

def test_uma::task_has_performedBy():
    assert hasattr(uma::Task, "performedBy")
    descriptor = None
    for klass in uma::Task.__mro__:
        if "performedBy" in klass.__dict__:
            descriptor = klass.__dict__["performedBy"]
            break
    assert isinstance(descriptor, property)

def test_uma::task_has_estimationConsiderations():
    assert hasattr(uma::Task, "estimationConsiderations")
    descriptor = None
    for klass in uma::Task.__mro__:
        if "estimationConsiderations" in klass.__dict__:
            descriptor = klass.__dict__["estimationConsiderations"]
            break
    assert isinstance(descriptor, property)

def test_uma::task_has_optionalInput():
    assert hasattr(uma::Task, "optionalInput")
    descriptor = None
    for klass in uma::Task.__mro__:
        if "optionalInput" in klass.__dict__:
            descriptor = klass.__dict__["optionalInput"]
            break
    assert isinstance(descriptor, property)

def test_uma::task_has_estimate():
    assert hasattr(uma::Task, "estimate")
    descriptor = None
    for klass in uma::Task.__mro__:
        if "estimate" in klass.__dict__:
            descriptor = klass.__dict__["estimate"]
            break
    assert isinstance(descriptor, property)

def test_uma::task_has_group2():
    assert hasattr(uma::Task, "group2")
    descriptor = None
    for klass in uma::Task.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)

def test_uma::task_has_output():
    assert hasattr(uma::Task, "output")
    descriptor = None
    for klass in uma::Task.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_uma::task_has_mandatoryInput():
    assert hasattr(uma::Task, "mandatoryInput")
    descriptor = None
    for klass in uma::Task.__mro__:
        if "mandatoryInput" in klass.__dict__:
            descriptor = klass.__dict__["mandatoryInput"]
            break
    assert isinstance(descriptor, property)

def test_uma::task_has_precondition():
    assert hasattr(uma::Task, "precondition")
    descriptor = None
    for klass in uma::Task.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_uma::task_has_additionallyPerformedBy():
    assert hasattr(uma::Task, "additionallyPerformedBy")
    descriptor = None
    for klass in uma::Task.__mro__:
        if "additionallyPerformedBy" in klass.__dict__:
            descriptor = klass.__dict__["additionallyPerformedBy"]
            break
    assert isinstance(descriptor, property)

def test_uma::task_has_toolMentor():
    assert hasattr(uma::Task, "toolMentor")
    descriptor = None
    for klass in uma::Task.__mro__:
        if "toolMentor" in klass.__dict__:
            descriptor = klass.__dict__["toolMentor"]
            break
    assert isinstance(descriptor, property)

def test_uma::task_has_postcondition():
    assert hasattr(uma::Task, "postcondition")
    descriptor = None
    for klass in uma::Task.__mro__:
        if "postcondition" in klass.__dict__:
            descriptor = klass.__dict__["postcondition"]
            break
    assert isinstance(descriptor, property)



def test_uma::supportingmaterial_is_not_abstract():
    assert not inspect.isabstract(uma::SupportingMaterial)


def test_uma::supportingmaterial_constructor_exists():
    assert callable(uma::SupportingMaterial.__init__)


def test_uma::supportingmaterial_constructor_args():
    sig = inspect.signature(uma::SupportingMaterial.__init__)
    params = list(sig.parameters.keys())



def test_uma::rolesetgrouping_is_not_abstract():
    assert not inspect.isabstract(uma::RoleSetGrouping)


def test_uma::rolesetgrouping_constructor_exists():
    assert callable(uma::RoleSetGrouping.__init__)


def test_uma::rolesetgrouping_constructor_args():
    sig = inspect.signature(uma::RoleSetGrouping.__init__)
    params = list(sig.parameters.keys())
    assert "roleSet" in params, "Missing parameter 'roleSet'"
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma::rolesetgrouping_has_roleSet():
    assert hasattr(uma::RoleSetGrouping, "roleSet")
    descriptor = None
    for klass in uma::RoleSetGrouping.__mro__:
        if "roleSet" in klass.__dict__:
            descriptor = klass.__dict__["roleSet"]
            break
    assert isinstance(descriptor, property)

def test_uma::rolesetgrouping_has_group2():
    assert hasattr(uma::RoleSetGrouping, "group2")
    descriptor = None
    for klass in uma::RoleSetGrouping.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_uma::roleset_is_not_abstract():
    assert not inspect.isabstract(uma::RoleSet)


def test_uma::roleset_constructor_exists():
    assert callable(uma::RoleSet.__init__)


def test_uma::roleset_constructor_args():
    sig = inspect.signature(uma::RoleSet.__init__)
    params = list(sig.parameters.keys())
    assert "role" in params, "Missing parameter 'role'"
    assert "group2" in params, "Missing parameter 'group2'"

def test_uma::roleset_has_role():
    assert hasattr(uma::RoleSet, "role")
    descriptor = None
    for klass in uma::RoleSet.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_uma::roleset_has_group2():
    assert hasattr(uma::RoleSet, "group2")
    descriptor = None
    for klass in uma::RoleSet.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)



def test_descriptor_is_not_abstract():
    assert not inspect.isabstract(Descriptor)


def test_descriptor_constructor_exists():
    assert callable(Descriptor.__init__)


def test_descriptor_constructor_args():
    sig = inspect.signature(Descriptor.__init__)
    params = list(sig.parameters.keys())



def test_uma::workproductdescriptor_is_not_abstract():
    assert not inspect.isabstract(uma::WorkProductDescriptor)


def test_uma::workproductdescriptor_constructor_exists():
    assert callable(uma::WorkProductDescriptor.__init__)


def test_uma::workproductdescriptor_constructor_args():
    sig = inspect.signature(uma::WorkProductDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "deliverableParts" in params, "Missing parameter 'deliverableParts'"
    assert "mandatoryInputTo" in params, "Missing parameter 'mandatoryInputTo'"
    assert "impactedBy" in params, "Missing parameter 'impactedBy'"
    assert "activityExitState" in params, "Missing parameter 'activityExitState'"
    assert "outputFrom" in params, "Missing parameter 'outputFrom'"
    assert "workProduct" in params, "Missing parameter 'workProduct'"
    assert "responsibleRole" in params, "Missing parameter 'responsibleRole'"
    assert "externalInputTo" in params, "Missing parameter 'externalInputTo'"
    assert "group2" in params, "Missing parameter 'group2'"
    assert "impacts" in params, "Missing parameter 'impacts'"
    assert "activityEntryState" in params, "Missing parameter 'activityEntryState'"
    assert "optionalInputTo" in params, "Missing parameter 'optionalInputTo'"

def test_uma::workproductdescriptor_has_deliverableParts():
    assert hasattr(uma::WorkProductDescriptor, "deliverableParts")
    descriptor = None
    for klass in uma::WorkProductDescriptor.__mro__:
        if "deliverableParts" in klass.__dict__:
            descriptor = klass.__dict__["deliverableParts"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproductdescriptor_has_mandatoryInputTo():
    assert hasattr(uma::WorkProductDescriptor, "mandatoryInputTo")
    descriptor = None
    for klass in uma::WorkProductDescriptor.__mro__:
        if "mandatoryInputTo" in klass.__dict__:
            descriptor = klass.__dict__["mandatoryInputTo"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproductdescriptor_has_impactedBy():
    assert hasattr(uma::WorkProductDescriptor, "impactedBy")
    descriptor = None
    for klass in uma::WorkProductDescriptor.__mro__:
        if "impactedBy" in klass.__dict__:
            descriptor = klass.__dict__["impactedBy"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproductdescriptor_has_activityExitState():
    assert hasattr(uma::WorkProductDescriptor, "activityExitState")
    descriptor = None
    for klass in uma::WorkProductDescriptor.__mro__:
        if "activityExitState" in klass.__dict__:
            descriptor = klass.__dict__["activityExitState"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproductdescriptor_has_outputFrom():
    assert hasattr(uma::WorkProductDescriptor, "outputFrom")
    descriptor = None
    for klass in uma::WorkProductDescriptor.__mro__:
        if "outputFrom" in klass.__dict__:
            descriptor = klass.__dict__["outputFrom"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproductdescriptor_has_workProduct():
    assert hasattr(uma::WorkProductDescriptor, "workProduct")
    descriptor = None
    for klass in uma::WorkProductDescriptor.__mro__:
        if "workProduct" in klass.__dict__:
            descriptor = klass.__dict__["workProduct"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproductdescriptor_has_responsibleRole():
    assert hasattr(uma::WorkProductDescriptor, "responsibleRole")
    descriptor = None
    for klass in uma::WorkProductDescriptor.__mro__:
        if "responsibleRole" in klass.__dict__:
            descriptor = klass.__dict__["responsibleRole"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproductdescriptor_has_externalInputTo():
    assert hasattr(uma::WorkProductDescriptor, "externalInputTo")
    descriptor = None
    for klass in uma::WorkProductDescriptor.__mro__:
        if "externalInputTo" in klass.__dict__:
            descriptor = klass.__dict__["externalInputTo"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproductdescriptor_has_group2():
    assert hasattr(uma::WorkProductDescriptor, "group2")
    descriptor = None
    for klass in uma::WorkProductDescriptor.__mro__:
        if "group2" in klass.__dict__:
            descriptor = klass.__dict__["group2"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproductdescriptor_has_impacts():
    assert hasattr(uma::WorkProductDescriptor, "impacts")
    descriptor = None
    for klass in uma::WorkProductDescriptor.__mro__:
        if "impacts" in klass.__dict__:
            descriptor = klass.__dict__["impacts"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproductdescriptor_has_activityEntryState():
    assert hasattr(uma::WorkProductDescriptor, "activityEntryState")
    descriptor = None
    for klass in uma::WorkProductDescriptor.__mro__:
        if "activityEntryState" in klass.__dict__:
            descriptor = klass.__dict__["activityEntryState"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproductdescriptor_has_optionalInputTo():
    assert hasattr(uma::WorkProductDescriptor, "optionalInputTo")
    descriptor = None
    for klass in uma::WorkProductDescriptor.__mro__:
        if "optionalInputTo" in klass.__dict__:
            descriptor = klass.__dict__["optionalInputTo"]
            break
    assert isinstance(descriptor, property)



def test_uma::roledescriptor_is_not_abstract():
    assert not inspect.isabstract(uma::RoleDescriptor)


def test_uma::roledescriptor_constructor_exists():
    assert callable(uma::RoleDescriptor.__init__)


def test_uma::roledescriptor_constructor_args():
    sig = inspect.signature(uma::RoleDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "responsibleFor" in params, "Missing parameter 'responsibleFor'"
    assert "role" in params, "Missing parameter 'role'"

def test_uma::roledescriptor_has_responsibleFor():
    assert hasattr(uma::RoleDescriptor, "responsibleFor")
    descriptor = None
    for klass in uma::RoleDescriptor.__mro__:
        if "responsibleFor" in klass.__dict__:
            descriptor = klass.__dict__["responsibleFor"]
            break
    assert isinstance(descriptor, property)

def test_uma::roledescriptor_has_role():
    assert hasattr(uma::RoleDescriptor, "role")
    descriptor = None
    for klass in uma::RoleDescriptor.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)



def test_uma::roadmap_is_not_abstract():
    assert not inspect.isabstract(uma::Roadmap)


def test_uma::roadmap_constructor_exists():
    assert callable(uma::Roadmap.__init__)


def test_uma::roadmap_constructor_args():
    sig = inspect.signature(uma::Roadmap.__init__)
    params = list(sig.parameters.keys())



def test_uma::reusableasset_is_not_abstract():
    assert not inspect.isabstract(uma::ReusableAsset)


def test_uma::reusableasset_constructor_exists():
    assert callable(uma::ReusableAsset.__init__)


def test_uma::reusableasset_constructor_args():
    sig = inspect.signature(uma::ReusableAsset.__init__)
    params = list(sig.parameters.keys())



def test_uma::report_is_not_abstract():
    assert not inspect.isabstract(uma::Report)


def test_uma::report_constructor_exists():
    assert callable(uma::Report.__init__)


def test_uma::report_constructor_args():
    sig = inspect.signature(uma::Report.__init__)
    params = list(sig.parameters.keys())



def test_uma::activitydescription_is_not_abstract():
    assert not inspect.isabstract(uma::ActivityDescription)


def test_uma::activitydescription_constructor_exists():
    assert callable(uma::ActivityDescription.__init__)


def test_uma::activitydescription_constructor_args():
    sig = inspect.signature(uma::ActivityDescription.__init__)
    params = list(sig.parameters.keys())
    assert "purpose" in params, "Missing parameter 'purpose'"
    assert "howToStaff" in params, "Missing parameter 'howToStaff'"
    assert "alternatives" in params, "Missing parameter 'alternatives'"

def test_uma::activitydescription_has_purpose():
    assert hasattr(uma::ActivityDescription, "purpose")
    descriptor = None
    for klass in uma::ActivityDescription.__mro__:
        if "purpose" in klass.__dict__:
            descriptor = klass.__dict__["purpose"]
            break
    assert isinstance(descriptor, property)

def test_uma::activitydescription_has_howToStaff():
    assert hasattr(uma::ActivityDescription, "howToStaff")
    descriptor = None
    for klass in uma::ActivityDescription.__mro__:
        if "howToStaff" in klass.__dict__:
            descriptor = klass.__dict__["howToStaff"]
            break
    assert isinstance(descriptor, property)

def test_uma::activitydescription_has_alternatives():
    assert hasattr(uma::ActivityDescription, "alternatives")
    descriptor = None
    for klass in uma::ActivityDescription.__mro__:
        if "alternatives" in klass.__dict__:
            descriptor = klass.__dict__["alternatives"]
            break
    assert isinstance(descriptor, property)

def test_variabilitytype_exists():
    # Check that the Enumeration exists
    assert VariabilityType is not None

def test_variabilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariabilityType]
    expected_literals = [
        "localContribution",
        "extends",
        "replaces",
        "contributes",
        "na",
        "extendsReplaces",
        "localReplacement",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VariabilityType"

def test_workordertype_exists():
    # Check that the Enumeration exists
    assert WorkOrderType is not None

def test_workordertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkOrderType]
    expected_literals = [
        "startToStart",
        "finishToFinish",
        "finishToStart",
        "startToFinish",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WorkOrderType"


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
ActivityDescription_strategy = st.builds(
    ActivityDescription,
)
uma::ProcessDescription_strategy = st.builds(
    uma::ProcessDescription,
    usageNotes=
        safe_text,
    scope=
        safe_text
)
ProcessPackage_strategy = st.builds(
    ProcessPackage,
)
uma::ProcessComponent_strategy = st.builds(
    uma::ProcessComponent,
    version=
        safe_text,
    copyright=
        safe_text,
    changeDescription=
        safe_text,
    authors=
        safe_text,
    changeDate=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uma::PackageableElement_strategy = st.builds(
    uma::PackageableElement,
)
Element_strategy = st.builds(
    Element,
)
uma::NamedElement_strategy = st.builds(
    uma::NamedElement,
    name=
        safe_text
)
Activity_strategy = st.builds(
    Activity,
)
uma::Phase_strategy = st.builds(
    uma::Phase,
)
uma::Process_strategy = st.builds(
    uma::Process,
    includesPattern=
        safe_text,
    validContext=
        safe_text,
    diagramURI=
        safe_text,
    defaultContext=
        safe_text
)
uma::Iteration_strategy = st.builds(
    uma::Iteration,
)
uma::EStringToStringMapEntry_strategy = st.builds(
    uma::EStringToStringMapEntry,
)
uma::Element_strategy = st.builds(
    uma::Element,
)
BreakdownElement_strategy = st.builds(
    BreakdownElement,
)
uma::ProcessComponentInterface_strategy = st.builds(
    uma::ProcessComponentInterface,
    group2=
        safe_text
)
uma::Descriptor_strategy = st.builds(
    uma::Descriptor,
    isSynchronizedWithSource=
        safe_text
)
uma::DocumentRoot_strategy = st.builds(
    uma::DocumentRoot,
    mixed=
        safe_text
)
ProcessDescription_strategy = st.builds(
    ProcessDescription,
)
uma::DeliveryProcessDescription_strategy = st.builds(
    uma::DeliveryProcessDescription,
    scale=
        safe_text,
    estimatingTechnique=
        safe_text,
    typeOfContract=
        safe_text,
    riskLevel=
        safe_text,
    projectCharacteristics=
        safe_text,
    projectMemberExpertise=
        safe_text
)
ContentCategory_strategy = st.builds(
    ContentCategory,
)
uma::DisciplineGrouping_strategy = st.builds(
    uma::DisciplineGrouping,
    discipline=
        safe_text,
    group2=
        safe_text
)
uma::Domain_strategy = st.builds(
    uma::Domain,
    workProduct=
        safe_text,
    group2=
        safe_text
)
uma::Discipline_strategy = st.builds(
    uma::Discipline,
    referenceWorkflow=
        safe_text,
    task=
        safe_text,
    group2=
        safe_text
)
uma::CustomCategory_strategy = st.builds(
    uma::CustomCategory,
    categorizedElement=
        safe_text,
    group2=
        safe_text,
    subCategory=
        safe_text
)
WorkBreakdownElement_strategy = st.builds(
    WorkBreakdownElement,
)
uma::TaskDescriptor_strategy = st.builds(
    uma::TaskDescriptor,
    performedPrimarilyBy=
        safe_text,
    assistedBy=
        safe_text,
    externalInput=
        safe_text,
    mandatoryInput=
        safe_text,
    group3=
        safe_text,
    additionallyPerformedBy=
        safe_text,
    optionalInput=
        safe_text,
    isSynchronizedWithSource=
        safe_text,
    task=
        safe_text,
    output=
        safe_text
)
uma::Milestone_strategy = st.builds(
    uma::Milestone,
    requiredResult=
        safe_text
)
uma::Activity_strategy = st.builds(
    uma::Activity,
    group3=
        safe_text,
    roadmap=
        safe_text,
    variabilityBasedOnElement=
        safe_text,
    postcondition=
        safe_text,
    variabilityType=
        safe_text,
    precondition=
        safe_text,
    isEnactable=
        safe_text
)
DescribableElement_strategy = st.builds(
    DescribableElement,
)
uma::ProcessElement_strategy = st.builds(
    uma::ProcessElement,
)
uma::ContentElement_strategy = st.builds(
    uma::ContentElement,
    variabilityBasedOnElement=
        safe_text,
    guideline=
        safe_text,
    concept=
        safe_text,
    supportingMaterial=
        safe_text,
    variabilityType=
        safe_text,
    checklist=
        safe_text,
    reusableAsset=
        safe_text,
    whitepaper=
        safe_text,
    group1=
        safe_text,
    example=
        safe_text
)
MethodUnit_strategy = st.builds(
    MethodUnit,
)
uma::MethodConfiguration_strategy = st.builds(
    uma::MethodConfiguration,
    methodPackageSelection=
        safe_text,
    baseConfiguration=
        safe_text,
    methodPluginSelection=
        safe_text,
    addedCategory=
        safe_text,
    processView=
        safe_text,
    subtractedCategory=
        safe_text,
    defaultView=
        safe_text
)
uma::MethodLibrary_strategy = st.builds(
    uma::MethodLibrary,
    tool=
        safe_text
)
uma::MethodPlugin_strategy = st.builds(
    uma::MethodPlugin,
    referencedMethodPlugin=
        safe_text,
    userChangeable=
        safe_text,
    supporting=
        safe_text
)
uma::ContentDescription_strategy = st.builds(
    uma::ContentDescription,
    mainDescription=
        safe_text,
    keyConsiderations=
        safe_text,
    externalId=
        safe_text
)
MethodPackage_strategy = st.builds(
    MethodPackage,
)
uma::ContentPackage_strategy = st.builds(
    uma::ContentPackage,
    group2=
        safe_text
)
uma::ProcessPackage_strategy = st.builds(
    uma::ProcessPackage,
    group2=
        safe_text
)
uma::ContentCategoryPackage_strategy = st.builds(
    uma::ContentCategoryPackage,
    group2=
        safe_text
)
RoleDescriptor_strategy = st.builds(
    RoleDescriptor,
)
uma::CompositeRole_strategy = st.builds(
    uma::CompositeRole,
    group2=
        safe_text
)
Guidance_strategy = st.builds(
    Guidance,
)
uma::Practice_strategy = st.builds(
    uma::Practice,
    activityReference=
        safe_text,
    group2=
        safe_text,
    contentReference=
        safe_text
)
uma::Example_strategy = st.builds(
    uma::Example,
)
uma::EstimatingMetric_strategy = st.builds(
    uma::EstimatingMetric,
)
uma::EstimationConsiderations_strategy = st.builds(
    uma::EstimationConsiderations,
)
uma::Estimate_strategy = st.builds(
    uma::Estimate,
    estimationConsiderations=
        safe_text,
    estimationMetric=
        safe_text,
    group2=
        safe_text
)
uma::Guideline_strategy = st.builds(
    uma::Guideline,
)
uma::Concept_strategy = st.builds(
    uma::Concept,
)
uma::Checklist_strategy = st.builds(
    uma::Checklist,
)
Process_strategy = st.builds(
    Process,
)
uma::ProcessPlanningTemplate_strategy = st.builds(
    uma::ProcessPlanningTemplate,
    group4=
        safe_text,
    baseProcess=
        safe_text
)
uma::DeliveryProcess_strategy = st.builds(
    uma::DeliveryProcess,
    educationMaterial=
        safe_text,
    communicationsMaterial=
        safe_text,
    group4=
        safe_text
)
uma::CapabilityPattern_strategy = st.builds(
    uma::CapabilityPattern,
)
ContentElement_strategy = st.builds(
    ContentElement,
)
uma::Role_strategy = st.builds(
    uma::Role,
    responsibleFor=
        safe_text,
    group2=
        safe_text
)
uma::Guidance_strategy = st.builds(
    uma::Guidance,
)
uma::Kind_strategy = st.builds(
    uma::Kind,
    applicableMetaClassInfo=
        safe_text
)
uma::ContentCategory_strategy = st.builds(
    uma::ContentCategory,
)
MethodElement_strategy = st.builds(
    MethodElement,
)
uma::MethodPackage_strategy = st.builds(
    uma::MethodPackage,
    global_=
        safe_text,
    group1=
        safe_text,
    reusedPackage=
        safe_text
)
uma::MethodUnit_strategy = st.builds(
    uma::MethodUnit,
    authors=
        safe_text,
    copyright=
        safe_text,
    changeDate=
        safe_text,
    version=
        safe_text,
    changeDescription=
        safe_text
)
uma::Section_strategy = st.builds(
    uma::Section,
    sectionName=
        safe_text,
    variabilityType=
        safe_text,
    predecessor=
        safe_text,
    variabilityBasedOnElement=
        safe_text,
    description=
        safe_text
)
uma::DescribableElement_strategy = st.builds(
    uma::DescribableElement,
    shapeicon=
        safe_text,
    isAbstract=
        safe_text,
    nodeicon=
        safe_text,
    fulfill=
        safe_text
)
uma::Constraint_strategy = st.builds(
    uma::Constraint,
    mainDescription=
        safe_text
)
ContentDescription_strategy = st.builds(
    ContentDescription,
)
uma::GuidanceDescription_strategy = st.builds(
    uma::GuidanceDescription,
    attachment=
        safe_text
)
uma::PracticeDescription_strategy = st.builds(
    uma::PracticeDescription,
    application=
        safe_text,
    goals=
        safe_text,
    background=
        safe_text,
    levelsOfAdoption=
        safe_text,
    problem=
        safe_text,
    additionalInfo=
        safe_text
)
uma::RoleDescription_strategy = st.builds(
    uma::RoleDescription,
    assignmentApproaches=
        safe_text,
    skills=
        safe_text,
    synonyms=
        safe_text
)
uma::BreakdownElementDescription_strategy = st.builds(
    uma::BreakdownElementDescription,
    usageGuidance=
        safe_text
)
WorkProductDescription_strategy = st.builds(
    WorkProductDescription,
)
uma::DeliverableDescription_strategy = st.builds(
    uma::DeliverableDescription,
    externalDescription=
        safe_text,
    packagingGuidance=
        safe_text
)
uma::ArtifactDescription_strategy = st.builds(
    uma::ArtifactDescription,
    notation=
        safe_text,
    representation=
        safe_text,
    representationOptions=
        safe_text,
    briefOutline=
        safe_text
)
WorkProduct_strategy = st.builds(
    WorkProduct,
)
uma::Outcome_strategy = st.builds(
    uma::Outcome,
)
uma::Deliverable_strategy = st.builds(
    uma::Deliverable,
    group3=
        safe_text,
    deliveredWorkProduct=
        safe_text
)
uma::Artifact_strategy = st.builds(
    uma::Artifact,
    group3=
        safe_text
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
uma::MethodElementProperty_strategy = st.builds(
    uma::MethodElementProperty,
    value=
        safe_text
)
uma::MethodElement_strategy = st.builds(
    uma::MethodElement,
    orderingGuide=
        safe_text,
    group=
        safe_text,
    presentationName=
        safe_text,
    id=
        safe_text,
    suppressed=
        safe_text,
    briefDescription=
        safe_text
)
uma::ApplicableMetaClassInfo_strategy = st.builds(
    uma::ApplicableMetaClassInfo,
    isPrimaryExtension=
        safe_text
)
ProcessElement_strategy = st.builds(
    ProcessElement,
)
uma::PlanningData_strategy = st.builds(
    uma::PlanningData,
    startDate=
        safe_text,
    rank=
        safe_text,
    finishDate=
        safe_text
)
uma::BreakdownElement_strategy = st.builds(
    uma::BreakdownElement,
    presentedBefore=
        safe_text,
    isPlanned=
        safe_text,
    concept=
        safe_text,
    example=
        safe_text,
    hasMultipleOccurrences=
        safe_text,
    group1=
        safe_text,
    isOptional=
        safe_text,
    superActivity=
        safe_text,
    guideline=
        safe_text,
    whitepaper=
        safe_text,
    presentedAfter=
        safe_text,
    checklist=
        safe_text,
    prefix=
        safe_text,
    reusableAsset=
        safe_text,
    supportingMaterial=
        safe_text,
    planningData=
        safe_text
)
BreakdownElementDescription_strategy = st.builds(
    BreakdownElementDescription,
)
uma::DescriptorDescription_strategy = st.builds(
    uma::DescriptorDescription,
    refinedDescription=
        safe_text
)
uma::WorkProductType_strategy = st.builds(
    uma::WorkProductType,
    workProduct=
        safe_text,
    group2=
        safe_text
)
uma::WorkProduct_strategy = st.builds(
    uma::WorkProduct,
    estimate=
        safe_text,
    estimationConsiderations=
        safe_text,
    toolMentor=
        safe_text,
    template=
        safe_text,
    report=
        safe_text,
    group2=
        safe_text
)
uma::WorkProductDescription_strategy = st.builds(
    uma::WorkProductDescription,
    reasonsForNotNeeding=
        safe_text,
    impactOfNotHaving=
        safe_text,
    purpose=
        safe_text
)
uma::WorkOrder_strategy = st.builds(
    uma::WorkOrder,
    id=
        safe_text,
    properties=
        safe_text,
    value=
        safe_text,
    linkType=
        safe_text
)
uma::WorkBreakdownElement_strategy = st.builds(
    uma::WorkBreakdownElement,
    group2=
        safe_text,
    isEventDriven=
        safe_text,
    isRepeatable=
        safe_text,
    isOngoing=
        safe_text
)
Concept_strategy = st.builds(
    Concept,
)
uma::Whitepaper_strategy = st.builds(
    uma::Whitepaper,
)
uma::WorkDefinition_strategy = st.builds(
    uma::WorkDefinition,
    precondition=
        safe_text,
    postcondition=
        safe_text
)
uma::TermDefinition_strategy = st.builds(
    uma::TermDefinition,
)
uma::Template_strategy = st.builds(
    uma::Template,
)
uma::TeamProfile_strategy = st.builds(
    uma::TeamProfile,
    superTeam=
        safe_text,
    subTeam=
        safe_text,
    group2=
        safe_text,
    role=
        safe_text
)
uma::ToolMentor_strategy = st.builds(
    uma::ToolMentor,
)
uma::Tool_strategy = st.builds(
    uma::Tool,
    toolMentor=
        safe_text,
    group2=
        safe_text
)
uma::TaskDescription_strategy = st.builds(
    uma::TaskDescription,
    purpose=
        safe_text,
    alternatives=
        safe_text
)
uma::Task_strategy = st.builds(
    uma::Task,
    performedBy=
        safe_text,
    estimationConsiderations=
        safe_text,
    optionalInput=
        safe_text,
    estimate=
        safe_text,
    group2=
        safe_text,
    output=
        safe_text,
    mandatoryInput=
        safe_text,
    precondition=
        safe_text,
    additionallyPerformedBy=
        safe_text,
    toolMentor=
        safe_text,
    postcondition=
        safe_text
)
uma::SupportingMaterial_strategy = st.builds(
    uma::SupportingMaterial,
)
uma::RoleSetGrouping_strategy = st.builds(
    uma::RoleSetGrouping,
    roleSet=
        safe_text,
    group2=
        safe_text
)
uma::RoleSet_strategy = st.builds(
    uma::RoleSet,
    role=
        safe_text,
    group2=
        safe_text
)
Descriptor_strategy = st.builds(
    Descriptor,
)
uma::WorkProductDescriptor_strategy = st.builds(
    uma::WorkProductDescriptor,
    deliverableParts=
        safe_text,
    mandatoryInputTo=
        safe_text,
    impactedBy=
        safe_text,
    activityExitState=
        safe_text,
    outputFrom=
        safe_text,
    workProduct=
        safe_text,
    responsibleRole=
        safe_text,
    externalInputTo=
        safe_text,
    group2=
        safe_text,
    impacts=
        safe_text,
    activityEntryState=
        safe_text,
    optionalInputTo=
        safe_text
)
uma::RoleDescriptor_strategy = st.builds(
    uma::RoleDescriptor,
    responsibleFor=
        safe_text,
    role=
        safe_text
)
uma::Roadmap_strategy = st.builds(
    uma::Roadmap,
)
uma::ReusableAsset_strategy = st.builds(
    uma::ReusableAsset,
)
uma::Report_strategy = st.builds(
    uma::Report,
)
uma::ActivityDescription_strategy = st.builds(
    uma::ActivityDescription,
    purpose=
        safe_text,
    howToStaff=
        safe_text,
    alternatives=
        safe_text
)

@given(instance=ActivityDescription_strategy)
@settings(max_examples=50)
def test_activitydescription_instantiation(instance):
    assert isinstance(instance, ActivityDescription)

@given(instance=uma::ProcessDescription_strategy)
@settings(max_examples=50)
def test_uma::processdescription_instantiation(instance):
    assert isinstance(instance, uma::ProcessDescription)

@given(instance=uma::ProcessDescription_strategy)
def test_uma::processdescription_usageNotes_type(instance):
    assert isinstance(instance.usageNotes, str)


@given(instance=uma::ProcessDescription_strategy)
def test_uma::processdescription_usageNotes_setter(instance):
    original = instance.usageNotes
    instance.usageNotes = original
    assert instance.usageNotes == original

@given(instance=uma::ProcessDescription_strategy)
def test_uma::processdescription_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=uma::ProcessDescription_strategy)
def test_uma::processdescription_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=ProcessPackage_strategy)
@settings(max_examples=50)
def test_processpackage_instantiation(instance):
    assert isinstance(instance, ProcessPackage)

@given(instance=uma::ProcessComponent_strategy)
@settings(max_examples=50)
def test_uma::processcomponent_instantiation(instance):
    assert isinstance(instance, uma::ProcessComponent)

@given(instance=uma::ProcessComponent_strategy)
def test_uma::processcomponent_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=uma::ProcessComponent_strategy)
def test_uma::processcomponent_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=uma::ProcessComponent_strategy)
def test_uma::processcomponent_copyright_type(instance):
    assert isinstance(instance.copyright, str)


@given(instance=uma::ProcessComponent_strategy)
def test_uma::processcomponent_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original

@given(instance=uma::ProcessComponent_strategy)
def test_uma::processcomponent_changeDescription_type(instance):
    assert isinstance(instance.changeDescription, str)


@given(instance=uma::ProcessComponent_strategy)
def test_uma::processcomponent_changeDescription_setter(instance):
    original = instance.changeDescription
    instance.changeDescription = original
    assert instance.changeDescription == original

@given(instance=uma::ProcessComponent_strategy)
def test_uma::processcomponent_authors_type(instance):
    assert isinstance(instance.authors, str)


@given(instance=uma::ProcessComponent_strategy)
def test_uma::processcomponent_authors_setter(instance):
    original = instance.authors
    instance.authors = original
    assert instance.authors == original

@given(instance=uma::ProcessComponent_strategy)
def test_uma::processcomponent_changeDate_type(instance):
    assert isinstance(instance.changeDate, str)


@given(instance=uma::ProcessComponent_strategy)
def test_uma::processcomponent_changeDate_setter(instance):
    original = instance.changeDate
    instance.changeDate = original
    assert instance.changeDate == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=uma::PackageableElement_strategy)
@settings(max_examples=50)
def test_uma::packageableelement_instantiation(instance):
    assert isinstance(instance, uma::PackageableElement)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=uma::NamedElement_strategy)
@settings(max_examples=50)
def test_uma::namedelement_instantiation(instance):
    assert isinstance(instance, uma::NamedElement)

@given(instance=uma::NamedElement_strategy)
def test_uma::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=uma::NamedElement_strategy)
def test_uma::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=uma::Phase_strategy)
@settings(max_examples=50)
def test_uma::phase_instantiation(instance):
    assert isinstance(instance, uma::Phase)

@given(instance=uma::Process_strategy)
@settings(max_examples=50)
def test_uma::process_instantiation(instance):
    assert isinstance(instance, uma::Process)

@given(instance=uma::Process_strategy)
def test_uma::process_includesPattern_type(instance):
    assert isinstance(instance.includesPattern, str)


@given(instance=uma::Process_strategy)
def test_uma::process_includesPattern_setter(instance):
    original = instance.includesPattern
    instance.includesPattern = original
    assert instance.includesPattern == original

@given(instance=uma::Process_strategy)
def test_uma::process_validContext_type(instance):
    assert isinstance(instance.validContext, str)


@given(instance=uma::Process_strategy)
def test_uma::process_validContext_setter(instance):
    original = instance.validContext
    instance.validContext = original
    assert instance.validContext == original

@given(instance=uma::Process_strategy)
def test_uma::process_diagramURI_type(instance):
    assert isinstance(instance.diagramURI, str)


@given(instance=uma::Process_strategy)
def test_uma::process_diagramURI_setter(instance):
    original = instance.diagramURI
    instance.diagramURI = original
    assert instance.diagramURI == original

@given(instance=uma::Process_strategy)
def test_uma::process_defaultContext_type(instance):
    assert isinstance(instance.defaultContext, str)


@given(instance=uma::Process_strategy)
def test_uma::process_defaultContext_setter(instance):
    original = instance.defaultContext
    instance.defaultContext = original
    assert instance.defaultContext == original

@given(instance=uma::Iteration_strategy)
@settings(max_examples=50)
def test_uma::iteration_instantiation(instance):
    assert isinstance(instance, uma::Iteration)

@given(instance=uma::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_uma::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, uma::EStringToStringMapEntry)

@given(instance=uma::Element_strategy)
@settings(max_examples=50)
def test_uma::element_instantiation(instance):
    assert isinstance(instance, uma::Element)

@given(instance=BreakdownElement_strategy)
@settings(max_examples=50)
def test_breakdownelement_instantiation(instance):
    assert isinstance(instance, BreakdownElement)

@given(instance=uma::ProcessComponentInterface_strategy)
@settings(max_examples=50)
def test_uma::processcomponentinterface_instantiation(instance):
    assert isinstance(instance, uma::ProcessComponentInterface)

@given(instance=uma::ProcessComponentInterface_strategy)
def test_uma::processcomponentinterface_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::ProcessComponentInterface_strategy)
def test_uma::processcomponentinterface_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma::Descriptor_strategy)
@settings(max_examples=50)
def test_uma::descriptor_instantiation(instance):
    assert isinstance(instance, uma::Descriptor)

@given(instance=uma::Descriptor_strategy)
def test_uma::descriptor_isSynchronizedWithSource_type(instance):
    assert isinstance(instance.isSynchronizedWithSource, str)


@given(instance=uma::Descriptor_strategy)
def test_uma::descriptor_isSynchronizedWithSource_setter(instance):
    original = instance.isSynchronizedWithSource
    instance.isSynchronizedWithSource = original
    assert instance.isSynchronizedWithSource == original

@given(instance=uma::DocumentRoot_strategy)
@settings(max_examples=50)
def test_uma::documentroot_instantiation(instance):
    assert isinstance(instance, uma::DocumentRoot)

@given(instance=uma::DocumentRoot_strategy)
def test_uma::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=uma::DocumentRoot_strategy)
def test_uma::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=ProcessDescription_strategy)
@settings(max_examples=50)
def test_processdescription_instantiation(instance):
    assert isinstance(instance, ProcessDescription)

@given(instance=uma::DeliveryProcessDescription_strategy)
@settings(max_examples=50)
def test_uma::deliveryprocessdescription_instantiation(instance):
    assert isinstance(instance, uma::DeliveryProcessDescription)

@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_scale_type(instance):
    assert isinstance(instance.scale, str)


@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_estimatingTechnique_type(instance):
    assert isinstance(instance.estimatingTechnique, str)


@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_estimatingTechnique_setter(instance):
    original = instance.estimatingTechnique
    instance.estimatingTechnique = original
    assert instance.estimatingTechnique == original

@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_typeOfContract_type(instance):
    assert isinstance(instance.typeOfContract, str)


@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_typeOfContract_setter(instance):
    original = instance.typeOfContract
    instance.typeOfContract = original
    assert instance.typeOfContract == original

@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_riskLevel_type(instance):
    assert isinstance(instance.riskLevel, str)


@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_riskLevel_setter(instance):
    original = instance.riskLevel
    instance.riskLevel = original
    assert instance.riskLevel == original

@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_projectCharacteristics_type(instance):
    assert isinstance(instance.projectCharacteristics, str)


@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_projectCharacteristics_setter(instance):
    original = instance.projectCharacteristics
    instance.projectCharacteristics = original
    assert instance.projectCharacteristics == original

@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_projectMemberExpertise_type(instance):
    assert isinstance(instance.projectMemberExpertise, str)


@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_projectMemberExpertise_setter(instance):
    original = instance.projectMemberExpertise
    instance.projectMemberExpertise = original
    assert instance.projectMemberExpertise == original

@given(instance=ContentCategory_strategy)
@settings(max_examples=50)
def test_contentcategory_instantiation(instance):
    assert isinstance(instance, ContentCategory)

@given(instance=uma::DisciplineGrouping_strategy)
@settings(max_examples=50)
def test_uma::disciplinegrouping_instantiation(instance):
    assert isinstance(instance, uma::DisciplineGrouping)

@given(instance=uma::DisciplineGrouping_strategy)
def test_uma::disciplinegrouping_discipline_type(instance):
    assert isinstance(instance.discipline, str)


@given(instance=uma::DisciplineGrouping_strategy)
def test_uma::disciplinegrouping_discipline_setter(instance):
    original = instance.discipline
    instance.discipline = original
    assert instance.discipline == original

@given(instance=uma::DisciplineGrouping_strategy)
def test_uma::disciplinegrouping_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::DisciplineGrouping_strategy)
def test_uma::disciplinegrouping_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma::Domain_strategy)
@settings(max_examples=50)
def test_uma::domain_instantiation(instance):
    assert isinstance(instance, uma::Domain)

@given(instance=uma::Domain_strategy)
def test_uma::domain_workProduct_type(instance):
    assert isinstance(instance.workProduct, str)


@given(instance=uma::Domain_strategy)
def test_uma::domain_workProduct_setter(instance):
    original = instance.workProduct
    instance.workProduct = original
    assert instance.workProduct == original

@given(instance=uma::Domain_strategy)
def test_uma::domain_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::Domain_strategy)
def test_uma::domain_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma::Discipline_strategy)
@settings(max_examples=50)
def test_uma::discipline_instantiation(instance):
    assert isinstance(instance, uma::Discipline)

@given(instance=uma::Discipline_strategy)
def test_uma::discipline_referenceWorkflow_type(instance):
    assert isinstance(instance.referenceWorkflow, str)


@given(instance=uma::Discipline_strategy)
def test_uma::discipline_referenceWorkflow_setter(instance):
    original = instance.referenceWorkflow
    instance.referenceWorkflow = original
    assert instance.referenceWorkflow == original

@given(instance=uma::Discipline_strategy)
def test_uma::discipline_task_type(instance):
    assert isinstance(instance.task, str)


@given(instance=uma::Discipline_strategy)
def test_uma::discipline_task_setter(instance):
    original = instance.task
    instance.task = original
    assert instance.task == original

@given(instance=uma::Discipline_strategy)
def test_uma::discipline_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::Discipline_strategy)
def test_uma::discipline_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma::CustomCategory_strategy)
@settings(max_examples=50)
def test_uma::customcategory_instantiation(instance):
    assert isinstance(instance, uma::CustomCategory)

@given(instance=uma::CustomCategory_strategy)
def test_uma::customcategory_categorizedElement_type(instance):
    assert isinstance(instance.categorizedElement, str)


@given(instance=uma::CustomCategory_strategy)
def test_uma::customcategory_categorizedElement_setter(instance):
    original = instance.categorizedElement
    instance.categorizedElement = original
    assert instance.categorizedElement == original

@given(instance=uma::CustomCategory_strategy)
def test_uma::customcategory_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::CustomCategory_strategy)
def test_uma::customcategory_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma::CustomCategory_strategy)
def test_uma::customcategory_subCategory_type(instance):
    assert isinstance(instance.subCategory, str)


@given(instance=uma::CustomCategory_strategy)
def test_uma::customcategory_subCategory_setter(instance):
    original = instance.subCategory
    instance.subCategory = original
    assert instance.subCategory == original

@given(instance=WorkBreakdownElement_strategy)
@settings(max_examples=50)
def test_workbreakdownelement_instantiation(instance):
    assert isinstance(instance, WorkBreakdownElement)

@given(instance=uma::TaskDescriptor_strategy)
@settings(max_examples=50)
def test_uma::taskdescriptor_instantiation(instance):
    assert isinstance(instance, uma::TaskDescriptor)

@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_performedPrimarilyBy_type(instance):
    assert isinstance(instance.performedPrimarilyBy, str)


@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_performedPrimarilyBy_setter(instance):
    original = instance.performedPrimarilyBy
    instance.performedPrimarilyBy = original
    assert instance.performedPrimarilyBy == original

@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_assistedBy_type(instance):
    assert isinstance(instance.assistedBy, str)


@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_assistedBy_setter(instance):
    original = instance.assistedBy
    instance.assistedBy = original
    assert instance.assistedBy == original

@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_externalInput_type(instance):
    assert isinstance(instance.externalInput, str)


@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_externalInput_setter(instance):
    original = instance.externalInput
    instance.externalInput = original
    assert instance.externalInput == original

@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_mandatoryInput_type(instance):
    assert isinstance(instance.mandatoryInput, str)


@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_mandatoryInput_setter(instance):
    original = instance.mandatoryInput
    instance.mandatoryInput = original
    assert instance.mandatoryInput == original

@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_additionallyPerformedBy_type(instance):
    assert isinstance(instance.additionallyPerformedBy, str)


@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_additionallyPerformedBy_setter(instance):
    original = instance.additionallyPerformedBy
    instance.additionallyPerformedBy = original
    assert instance.additionallyPerformedBy == original

@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_optionalInput_type(instance):
    assert isinstance(instance.optionalInput, str)


@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_optionalInput_setter(instance):
    original = instance.optionalInput
    instance.optionalInput = original
    assert instance.optionalInput == original

@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_isSynchronizedWithSource_type(instance):
    assert isinstance(instance.isSynchronizedWithSource, str)


@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_isSynchronizedWithSource_setter(instance):
    original = instance.isSynchronizedWithSource
    instance.isSynchronizedWithSource = original
    assert instance.isSynchronizedWithSource == original

@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_task_type(instance):
    assert isinstance(instance.task, str)


@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_task_setter(instance):
    original = instance.task
    instance.task = original
    assert instance.task == original

@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=uma::TaskDescriptor_strategy)
def test_uma::taskdescriptor_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=uma::Milestone_strategy)
@settings(max_examples=50)
def test_uma::milestone_instantiation(instance):
    assert isinstance(instance, uma::Milestone)

@given(instance=uma::Milestone_strategy)
def test_uma::milestone_requiredResult_type(instance):
    assert isinstance(instance.requiredResult, str)


@given(instance=uma::Milestone_strategy)
def test_uma::milestone_requiredResult_setter(instance):
    original = instance.requiredResult
    instance.requiredResult = original
    assert instance.requiredResult == original

@given(instance=uma::Activity_strategy)
@settings(max_examples=50)
def test_uma::activity_instantiation(instance):
    assert isinstance(instance, uma::Activity)

@given(instance=uma::Activity_strategy)
def test_uma::activity_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=uma::Activity_strategy)
def test_uma::activity_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=uma::Activity_strategy)
def test_uma::activity_roadmap_type(instance):
    assert isinstance(instance.roadmap, str)


@given(instance=uma::Activity_strategy)
def test_uma::activity_roadmap_setter(instance):
    original = instance.roadmap
    instance.roadmap = original
    assert instance.roadmap == original

@given(instance=uma::Activity_strategy)
def test_uma::activity_variabilityBasedOnElement_type(instance):
    assert isinstance(instance.variabilityBasedOnElement, str)


@given(instance=uma::Activity_strategy)
def test_uma::activity_variabilityBasedOnElement_setter(instance):
    original = instance.variabilityBasedOnElement
    instance.variabilityBasedOnElement = original
    assert instance.variabilityBasedOnElement == original

@given(instance=uma::Activity_strategy)
def test_uma::activity_postcondition_type(instance):
    assert isinstance(instance.postcondition, str)


@given(instance=uma::Activity_strategy)
def test_uma::activity_postcondition_setter(instance):
    original = instance.postcondition
    instance.postcondition = original
    assert instance.postcondition == original

@given(instance=uma::Activity_strategy)
def test_uma::activity_variabilityType_type(instance):
    assert isinstance(instance.variabilityType, str)


@given(instance=uma::Activity_strategy)
def test_uma::activity_variabilityType_setter(instance):
    original = instance.variabilityType
    instance.variabilityType = original
    assert instance.variabilityType == original

@given(instance=uma::Activity_strategy)
def test_uma::activity_precondition_type(instance):
    assert isinstance(instance.precondition, str)


@given(instance=uma::Activity_strategy)
def test_uma::activity_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original

@given(instance=uma::Activity_strategy)
def test_uma::activity_isEnactable_type(instance):
    assert isinstance(instance.isEnactable, str)


@given(instance=uma::Activity_strategy)
def test_uma::activity_isEnactable_setter(instance):
    original = instance.isEnactable
    instance.isEnactable = original
    assert instance.isEnactable == original

@given(instance=DescribableElement_strategy)
@settings(max_examples=50)
def test_describableelement_instantiation(instance):
    assert isinstance(instance, DescribableElement)

@given(instance=uma::ProcessElement_strategy)
@settings(max_examples=50)
def test_uma::processelement_instantiation(instance):
    assert isinstance(instance, uma::ProcessElement)

@given(instance=uma::ContentElement_strategy)
@settings(max_examples=50)
def test_uma::contentelement_instantiation(instance):
    assert isinstance(instance, uma::ContentElement)

@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_variabilityBasedOnElement_type(instance):
    assert isinstance(instance.variabilityBasedOnElement, str)


@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_variabilityBasedOnElement_setter(instance):
    original = instance.variabilityBasedOnElement
    instance.variabilityBasedOnElement = original
    assert instance.variabilityBasedOnElement == original

@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_guideline_type(instance):
    assert isinstance(instance.guideline, str)


@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_guideline_setter(instance):
    original = instance.guideline
    instance.guideline = original
    assert instance.guideline == original

@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_concept_type(instance):
    assert isinstance(instance.concept, str)


@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_concept_setter(instance):
    original = instance.concept
    instance.concept = original
    assert instance.concept == original

@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_supportingMaterial_type(instance):
    assert isinstance(instance.supportingMaterial, str)


@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_supportingMaterial_setter(instance):
    original = instance.supportingMaterial
    instance.supportingMaterial = original
    assert instance.supportingMaterial == original

@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_variabilityType_type(instance):
    assert isinstance(instance.variabilityType, str)


@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_variabilityType_setter(instance):
    original = instance.variabilityType
    instance.variabilityType = original
    assert instance.variabilityType == original

@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_checklist_type(instance):
    assert isinstance(instance.checklist, str)


@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_checklist_setter(instance):
    original = instance.checklist
    instance.checklist = original
    assert instance.checklist == original

@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_reusableAsset_type(instance):
    assert isinstance(instance.reusableAsset, str)


@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_reusableAsset_setter(instance):
    original = instance.reusableAsset
    instance.reusableAsset = original
    assert instance.reusableAsset == original

@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_whitepaper_type(instance):
    assert isinstance(instance.whitepaper, str)


@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_whitepaper_setter(instance):
    original = instance.whitepaper
    instance.whitepaper = original
    assert instance.whitepaper == original

@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_group1_type(instance):
    assert isinstance(instance.group1, str)


@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_group1_setter(instance):
    original = instance.group1
    instance.group1 = original
    assert instance.group1 == original

@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_example_type(instance):
    assert isinstance(instance.example, str)


@given(instance=uma::ContentElement_strategy)
def test_uma::contentelement_example_setter(instance):
    original = instance.example
    instance.example = original
    assert instance.example == original

@given(instance=MethodUnit_strategy)
@settings(max_examples=50)
def test_methodunit_instantiation(instance):
    assert isinstance(instance, MethodUnit)

@given(instance=uma::MethodConfiguration_strategy)
@settings(max_examples=50)
def test_uma::methodconfiguration_instantiation(instance):
    assert isinstance(instance, uma::MethodConfiguration)

@given(instance=uma::MethodConfiguration_strategy)
def test_uma::methodconfiguration_methodPackageSelection_type(instance):
    assert isinstance(instance.methodPackageSelection, str)


@given(instance=uma::MethodConfiguration_strategy)
def test_uma::methodconfiguration_methodPackageSelection_setter(instance):
    original = instance.methodPackageSelection
    instance.methodPackageSelection = original
    assert instance.methodPackageSelection == original

@given(instance=uma::MethodConfiguration_strategy)
def test_uma::methodconfiguration_baseConfiguration_type(instance):
    assert isinstance(instance.baseConfiguration, str)


@given(instance=uma::MethodConfiguration_strategy)
def test_uma::methodconfiguration_baseConfiguration_setter(instance):
    original = instance.baseConfiguration
    instance.baseConfiguration = original
    assert instance.baseConfiguration == original

@given(instance=uma::MethodConfiguration_strategy)
def test_uma::methodconfiguration_methodPluginSelection_type(instance):
    assert isinstance(instance.methodPluginSelection, str)


@given(instance=uma::MethodConfiguration_strategy)
def test_uma::methodconfiguration_methodPluginSelection_setter(instance):
    original = instance.methodPluginSelection
    instance.methodPluginSelection = original
    assert instance.methodPluginSelection == original

@given(instance=uma::MethodConfiguration_strategy)
def test_uma::methodconfiguration_addedCategory_type(instance):
    assert isinstance(instance.addedCategory, str)


@given(instance=uma::MethodConfiguration_strategy)
def test_uma::methodconfiguration_addedCategory_setter(instance):
    original = instance.addedCategory
    instance.addedCategory = original
    assert instance.addedCategory == original

@given(instance=uma::MethodConfiguration_strategy)
def test_uma::methodconfiguration_processView_type(instance):
    assert isinstance(instance.processView, str)


@given(instance=uma::MethodConfiguration_strategy)
def test_uma::methodconfiguration_processView_setter(instance):
    original = instance.processView
    instance.processView = original
    assert instance.processView == original

@given(instance=uma::MethodConfiguration_strategy)
def test_uma::methodconfiguration_subtractedCategory_type(instance):
    assert isinstance(instance.subtractedCategory, str)


@given(instance=uma::MethodConfiguration_strategy)
def test_uma::methodconfiguration_subtractedCategory_setter(instance):
    original = instance.subtractedCategory
    instance.subtractedCategory = original
    assert instance.subtractedCategory == original

@given(instance=uma::MethodConfiguration_strategy)
def test_uma::methodconfiguration_defaultView_type(instance):
    assert isinstance(instance.defaultView, str)


@given(instance=uma::MethodConfiguration_strategy)
def test_uma::methodconfiguration_defaultView_setter(instance):
    original = instance.defaultView
    instance.defaultView = original
    assert instance.defaultView == original

@given(instance=uma::MethodLibrary_strategy)
@settings(max_examples=50)
def test_uma::methodlibrary_instantiation(instance):
    assert isinstance(instance, uma::MethodLibrary)

@given(instance=uma::MethodLibrary_strategy)
def test_uma::methodlibrary_tool_type(instance):
    assert isinstance(instance.tool, str)


@given(instance=uma::MethodLibrary_strategy)
def test_uma::methodlibrary_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original

@given(instance=uma::MethodPlugin_strategy)
@settings(max_examples=50)
def test_uma::methodplugin_instantiation(instance):
    assert isinstance(instance, uma::MethodPlugin)

@given(instance=uma::MethodPlugin_strategy)
def test_uma::methodplugin_referencedMethodPlugin_type(instance):
    assert isinstance(instance.referencedMethodPlugin, str)


@given(instance=uma::MethodPlugin_strategy)
def test_uma::methodplugin_referencedMethodPlugin_setter(instance):
    original = instance.referencedMethodPlugin
    instance.referencedMethodPlugin = original
    assert instance.referencedMethodPlugin == original

@given(instance=uma::MethodPlugin_strategy)
def test_uma::methodplugin_userChangeable_type(instance):
    assert isinstance(instance.userChangeable, str)


@given(instance=uma::MethodPlugin_strategy)
def test_uma::methodplugin_userChangeable_setter(instance):
    original = instance.userChangeable
    instance.userChangeable = original
    assert instance.userChangeable == original

@given(instance=uma::MethodPlugin_strategy)
def test_uma::methodplugin_supporting_type(instance):
    assert isinstance(instance.supporting, str)


@given(instance=uma::MethodPlugin_strategy)
def test_uma::methodplugin_supporting_setter(instance):
    original = instance.supporting
    instance.supporting = original
    assert instance.supporting == original

@given(instance=uma::ContentDescription_strategy)
@settings(max_examples=50)
def test_uma::contentdescription_instantiation(instance):
    assert isinstance(instance, uma::ContentDescription)

@given(instance=uma::ContentDescription_strategy)
def test_uma::contentdescription_mainDescription_type(instance):
    assert isinstance(instance.mainDescription, str)


@given(instance=uma::ContentDescription_strategy)
def test_uma::contentdescription_mainDescription_setter(instance):
    original = instance.mainDescription
    instance.mainDescription = original
    assert instance.mainDescription == original

@given(instance=uma::ContentDescription_strategy)
def test_uma::contentdescription_keyConsiderations_type(instance):
    assert isinstance(instance.keyConsiderations, str)


@given(instance=uma::ContentDescription_strategy)
def test_uma::contentdescription_keyConsiderations_setter(instance):
    original = instance.keyConsiderations
    instance.keyConsiderations = original
    assert instance.keyConsiderations == original

@given(instance=uma::ContentDescription_strategy)
def test_uma::contentdescription_externalId_type(instance):
    assert isinstance(instance.externalId, str)


@given(instance=uma::ContentDescription_strategy)
def test_uma::contentdescription_externalId_setter(instance):
    original = instance.externalId
    instance.externalId = original
    assert instance.externalId == original

@given(instance=MethodPackage_strategy)
@settings(max_examples=50)
def test_methodpackage_instantiation(instance):
    assert isinstance(instance, MethodPackage)

@given(instance=uma::ContentPackage_strategy)
@settings(max_examples=50)
def test_uma::contentpackage_instantiation(instance):
    assert isinstance(instance, uma::ContentPackage)

@given(instance=uma::ContentPackage_strategy)
def test_uma::contentpackage_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::ContentPackage_strategy)
def test_uma::contentpackage_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma::ProcessPackage_strategy)
@settings(max_examples=50)
def test_uma::processpackage_instantiation(instance):
    assert isinstance(instance, uma::ProcessPackage)

@given(instance=uma::ProcessPackage_strategy)
def test_uma::processpackage_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::ProcessPackage_strategy)
def test_uma::processpackage_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma::ContentCategoryPackage_strategy)
@settings(max_examples=50)
def test_uma::contentcategorypackage_instantiation(instance):
    assert isinstance(instance, uma::ContentCategoryPackage)

@given(instance=uma::ContentCategoryPackage_strategy)
def test_uma::contentcategorypackage_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::ContentCategoryPackage_strategy)
def test_uma::contentcategorypackage_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=RoleDescriptor_strategy)
@settings(max_examples=50)
def test_roledescriptor_instantiation(instance):
    assert isinstance(instance, RoleDescriptor)

@given(instance=uma::CompositeRole_strategy)
@settings(max_examples=50)
def test_uma::compositerole_instantiation(instance):
    assert isinstance(instance, uma::CompositeRole)

@given(instance=uma::CompositeRole_strategy)
def test_uma::compositerole_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::CompositeRole_strategy)
def test_uma::compositerole_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=Guidance_strategy)
@settings(max_examples=50)
def test_guidance_instantiation(instance):
    assert isinstance(instance, Guidance)

@given(instance=uma::Practice_strategy)
@settings(max_examples=50)
def test_uma::practice_instantiation(instance):
    assert isinstance(instance, uma::Practice)

@given(instance=uma::Practice_strategy)
def test_uma::practice_activityReference_type(instance):
    assert isinstance(instance.activityReference, str)


@given(instance=uma::Practice_strategy)
def test_uma::practice_activityReference_setter(instance):
    original = instance.activityReference
    instance.activityReference = original
    assert instance.activityReference == original

@given(instance=uma::Practice_strategy)
def test_uma::practice_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::Practice_strategy)
def test_uma::practice_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma::Practice_strategy)
def test_uma::practice_contentReference_type(instance):
    assert isinstance(instance.contentReference, str)


@given(instance=uma::Practice_strategy)
def test_uma::practice_contentReference_setter(instance):
    original = instance.contentReference
    instance.contentReference = original
    assert instance.contentReference == original

@given(instance=uma::Example_strategy)
@settings(max_examples=50)
def test_uma::example_instantiation(instance):
    assert isinstance(instance, uma::Example)

@given(instance=uma::EstimatingMetric_strategy)
@settings(max_examples=50)
def test_uma::estimatingmetric_instantiation(instance):
    assert isinstance(instance, uma::EstimatingMetric)

@given(instance=uma::EstimationConsiderations_strategy)
@settings(max_examples=50)
def test_uma::estimationconsiderations_instantiation(instance):
    assert isinstance(instance, uma::EstimationConsiderations)

@given(instance=uma::Estimate_strategy)
@settings(max_examples=50)
def test_uma::estimate_instantiation(instance):
    assert isinstance(instance, uma::Estimate)

@given(instance=uma::Estimate_strategy)
def test_uma::estimate_estimationConsiderations_type(instance):
    assert isinstance(instance.estimationConsiderations, str)


@given(instance=uma::Estimate_strategy)
def test_uma::estimate_estimationConsiderations_setter(instance):
    original = instance.estimationConsiderations
    instance.estimationConsiderations = original
    assert instance.estimationConsiderations == original

@given(instance=uma::Estimate_strategy)
def test_uma::estimate_estimationMetric_type(instance):
    assert isinstance(instance.estimationMetric, str)


@given(instance=uma::Estimate_strategy)
def test_uma::estimate_estimationMetric_setter(instance):
    original = instance.estimationMetric
    instance.estimationMetric = original
    assert instance.estimationMetric == original

@given(instance=uma::Estimate_strategy)
def test_uma::estimate_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::Estimate_strategy)
def test_uma::estimate_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma::Guideline_strategy)
@settings(max_examples=50)
def test_uma::guideline_instantiation(instance):
    assert isinstance(instance, uma::Guideline)

@given(instance=uma::Concept_strategy)
@settings(max_examples=50)
def test_uma::concept_instantiation(instance):
    assert isinstance(instance, uma::Concept)

@given(instance=uma::Checklist_strategy)
@settings(max_examples=50)
def test_uma::checklist_instantiation(instance):
    assert isinstance(instance, uma::Checklist)

@given(instance=Process_strategy)
@settings(max_examples=50)
def test_process_instantiation(instance):
    assert isinstance(instance, Process)

@given(instance=uma::ProcessPlanningTemplate_strategy)
@settings(max_examples=50)
def test_uma::processplanningtemplate_instantiation(instance):
    assert isinstance(instance, uma::ProcessPlanningTemplate)

@given(instance=uma::ProcessPlanningTemplate_strategy)
def test_uma::processplanningtemplate_group4_type(instance):
    assert isinstance(instance.group4, str)


@given(instance=uma::ProcessPlanningTemplate_strategy)
def test_uma::processplanningtemplate_group4_setter(instance):
    original = instance.group4
    instance.group4 = original
    assert instance.group4 == original

@given(instance=uma::ProcessPlanningTemplate_strategy)
def test_uma::processplanningtemplate_baseProcess_type(instance):
    assert isinstance(instance.baseProcess, str)


@given(instance=uma::ProcessPlanningTemplate_strategy)
def test_uma::processplanningtemplate_baseProcess_setter(instance):
    original = instance.baseProcess
    instance.baseProcess = original
    assert instance.baseProcess == original

@given(instance=uma::DeliveryProcess_strategy)
@settings(max_examples=50)
def test_uma::deliveryprocess_instantiation(instance):
    assert isinstance(instance, uma::DeliveryProcess)

@given(instance=uma::DeliveryProcess_strategy)
def test_uma::deliveryprocess_educationMaterial_type(instance):
    assert isinstance(instance.educationMaterial, str)


@given(instance=uma::DeliveryProcess_strategy)
def test_uma::deliveryprocess_educationMaterial_setter(instance):
    original = instance.educationMaterial
    instance.educationMaterial = original
    assert instance.educationMaterial == original

@given(instance=uma::DeliveryProcess_strategy)
def test_uma::deliveryprocess_communicationsMaterial_type(instance):
    assert isinstance(instance.communicationsMaterial, str)


@given(instance=uma::DeliveryProcess_strategy)
def test_uma::deliveryprocess_communicationsMaterial_setter(instance):
    original = instance.communicationsMaterial
    instance.communicationsMaterial = original
    assert instance.communicationsMaterial == original

@given(instance=uma::DeliveryProcess_strategy)
def test_uma::deliveryprocess_group4_type(instance):
    assert isinstance(instance.group4, str)


@given(instance=uma::DeliveryProcess_strategy)
def test_uma::deliveryprocess_group4_setter(instance):
    original = instance.group4
    instance.group4 = original
    assert instance.group4 == original

@given(instance=uma::CapabilityPattern_strategy)
@settings(max_examples=50)
def test_uma::capabilitypattern_instantiation(instance):
    assert isinstance(instance, uma::CapabilityPattern)

@given(instance=ContentElement_strategy)
@settings(max_examples=50)
def test_contentelement_instantiation(instance):
    assert isinstance(instance, ContentElement)

@given(instance=uma::Role_strategy)
@settings(max_examples=50)
def test_uma::role_instantiation(instance):
    assert isinstance(instance, uma::Role)

@given(instance=uma::Role_strategy)
def test_uma::role_responsibleFor_type(instance):
    assert isinstance(instance.responsibleFor, str)


@given(instance=uma::Role_strategy)
def test_uma::role_responsibleFor_setter(instance):
    original = instance.responsibleFor
    instance.responsibleFor = original
    assert instance.responsibleFor == original

@given(instance=uma::Role_strategy)
def test_uma::role_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::Role_strategy)
def test_uma::role_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma::Guidance_strategy)
@settings(max_examples=50)
def test_uma::guidance_instantiation(instance):
    assert isinstance(instance, uma::Guidance)

@given(instance=uma::Kind_strategy)
@settings(max_examples=50)
def test_uma::kind_instantiation(instance):
    assert isinstance(instance, uma::Kind)

@given(instance=uma::Kind_strategy)
def test_uma::kind_applicableMetaClassInfo_type(instance):
    assert isinstance(instance.applicableMetaClassInfo, str)


@given(instance=uma::Kind_strategy)
def test_uma::kind_applicableMetaClassInfo_setter(instance):
    original = instance.applicableMetaClassInfo
    instance.applicableMetaClassInfo = original
    assert instance.applicableMetaClassInfo == original

@given(instance=uma::ContentCategory_strategy)
@settings(max_examples=50)
def test_uma::contentcategory_instantiation(instance):
    assert isinstance(instance, uma::ContentCategory)

@given(instance=MethodElement_strategy)
@settings(max_examples=50)
def test_methodelement_instantiation(instance):
    assert isinstance(instance, MethodElement)

@given(instance=uma::MethodPackage_strategy)
@settings(max_examples=50)
def test_uma::methodpackage_instantiation(instance):
    assert isinstance(instance, uma::MethodPackage)

@given(instance=uma::MethodPackage_strategy)
def test_uma::methodpackage_global__type(instance):
    assert isinstance(instance.global_, str)


@given(instance=uma::MethodPackage_strategy)
def test_uma::methodpackage_global__setter(instance):
    original = instance.global_
    instance.global_ = original
    assert instance.global_ == original

@given(instance=uma::MethodPackage_strategy)
def test_uma::methodpackage_group1_type(instance):
    assert isinstance(instance.group1, str)


@given(instance=uma::MethodPackage_strategy)
def test_uma::methodpackage_group1_setter(instance):
    original = instance.group1
    instance.group1 = original
    assert instance.group1 == original

@given(instance=uma::MethodPackage_strategy)
def test_uma::methodpackage_reusedPackage_type(instance):
    assert isinstance(instance.reusedPackage, str)


@given(instance=uma::MethodPackage_strategy)
def test_uma::methodpackage_reusedPackage_setter(instance):
    original = instance.reusedPackage
    instance.reusedPackage = original
    assert instance.reusedPackage == original

@given(instance=uma::MethodUnit_strategy)
@settings(max_examples=50)
def test_uma::methodunit_instantiation(instance):
    assert isinstance(instance, uma::MethodUnit)

@given(instance=uma::MethodUnit_strategy)
def test_uma::methodunit_authors_type(instance):
    assert isinstance(instance.authors, str)


@given(instance=uma::MethodUnit_strategy)
def test_uma::methodunit_authors_setter(instance):
    original = instance.authors
    instance.authors = original
    assert instance.authors == original

@given(instance=uma::MethodUnit_strategy)
def test_uma::methodunit_copyright_type(instance):
    assert isinstance(instance.copyright, str)


@given(instance=uma::MethodUnit_strategy)
def test_uma::methodunit_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original

@given(instance=uma::MethodUnit_strategy)
def test_uma::methodunit_changeDate_type(instance):
    assert isinstance(instance.changeDate, str)


@given(instance=uma::MethodUnit_strategy)
def test_uma::methodunit_changeDate_setter(instance):
    original = instance.changeDate
    instance.changeDate = original
    assert instance.changeDate == original

@given(instance=uma::MethodUnit_strategy)
def test_uma::methodunit_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=uma::MethodUnit_strategy)
def test_uma::methodunit_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=uma::MethodUnit_strategy)
def test_uma::methodunit_changeDescription_type(instance):
    assert isinstance(instance.changeDescription, str)


@given(instance=uma::MethodUnit_strategy)
def test_uma::methodunit_changeDescription_setter(instance):
    original = instance.changeDescription
    instance.changeDescription = original
    assert instance.changeDescription == original

@given(instance=uma::Section_strategy)
@settings(max_examples=50)
def test_uma::section_instantiation(instance):
    assert isinstance(instance, uma::Section)

@given(instance=uma::Section_strategy)
def test_uma::section_sectionName_type(instance):
    assert isinstance(instance.sectionName, str)


@given(instance=uma::Section_strategy)
def test_uma::section_sectionName_setter(instance):
    original = instance.sectionName
    instance.sectionName = original
    assert instance.sectionName == original

@given(instance=uma::Section_strategy)
def test_uma::section_variabilityType_type(instance):
    assert isinstance(instance.variabilityType, str)


@given(instance=uma::Section_strategy)
def test_uma::section_variabilityType_setter(instance):
    original = instance.variabilityType
    instance.variabilityType = original
    assert instance.variabilityType == original

@given(instance=uma::Section_strategy)
def test_uma::section_predecessor_type(instance):
    assert isinstance(instance.predecessor, str)


@given(instance=uma::Section_strategy)
def test_uma::section_predecessor_setter(instance):
    original = instance.predecessor
    instance.predecessor = original
    assert instance.predecessor == original

@given(instance=uma::Section_strategy)
def test_uma::section_variabilityBasedOnElement_type(instance):
    assert isinstance(instance.variabilityBasedOnElement, str)


@given(instance=uma::Section_strategy)
def test_uma::section_variabilityBasedOnElement_setter(instance):
    original = instance.variabilityBasedOnElement
    instance.variabilityBasedOnElement = original
    assert instance.variabilityBasedOnElement == original

@given(instance=uma::Section_strategy)
def test_uma::section_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=uma::Section_strategy)
def test_uma::section_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=uma::DescribableElement_strategy)
@settings(max_examples=50)
def test_uma::describableelement_instantiation(instance):
    assert isinstance(instance, uma::DescribableElement)

@given(instance=uma::DescribableElement_strategy)
def test_uma::describableelement_shapeicon_type(instance):
    assert isinstance(instance.shapeicon, str)


@given(instance=uma::DescribableElement_strategy)
def test_uma::describableelement_shapeicon_setter(instance):
    original = instance.shapeicon
    instance.shapeicon = original
    assert instance.shapeicon == original

@given(instance=uma::DescribableElement_strategy)
def test_uma::describableelement_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, str)


@given(instance=uma::DescribableElement_strategy)
def test_uma::describableelement_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=uma::DescribableElement_strategy)
def test_uma::describableelement_nodeicon_type(instance):
    assert isinstance(instance.nodeicon, str)


@given(instance=uma::DescribableElement_strategy)
def test_uma::describableelement_nodeicon_setter(instance):
    original = instance.nodeicon
    instance.nodeicon = original
    assert instance.nodeicon == original

@given(instance=uma::DescribableElement_strategy)
def test_uma::describableelement_fulfill_type(instance):
    assert isinstance(instance.fulfill, str)


@given(instance=uma::DescribableElement_strategy)
def test_uma::describableelement_fulfill_setter(instance):
    original = instance.fulfill
    instance.fulfill = original
    assert instance.fulfill == original

@given(instance=uma::Constraint_strategy)
@settings(max_examples=50)
def test_uma::constraint_instantiation(instance):
    assert isinstance(instance, uma::Constraint)

@given(instance=uma::Constraint_strategy)
def test_uma::constraint_mainDescription_type(instance):
    assert isinstance(instance.mainDescription, str)


@given(instance=uma::Constraint_strategy)
def test_uma::constraint_mainDescription_setter(instance):
    original = instance.mainDescription
    instance.mainDescription = original
    assert instance.mainDescription == original

@given(instance=ContentDescription_strategy)
@settings(max_examples=50)
def test_contentdescription_instantiation(instance):
    assert isinstance(instance, ContentDescription)

@given(instance=uma::GuidanceDescription_strategy)
@settings(max_examples=50)
def test_uma::guidancedescription_instantiation(instance):
    assert isinstance(instance, uma::GuidanceDescription)

@given(instance=uma::GuidanceDescription_strategy)
def test_uma::guidancedescription_attachment_type(instance):
    assert isinstance(instance.attachment, str)


@given(instance=uma::GuidanceDescription_strategy)
def test_uma::guidancedescription_attachment_setter(instance):
    original = instance.attachment
    instance.attachment = original
    assert instance.attachment == original

@given(instance=uma::PracticeDescription_strategy)
@settings(max_examples=50)
def test_uma::practicedescription_instantiation(instance):
    assert isinstance(instance, uma::PracticeDescription)

@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_application_type(instance):
    assert isinstance(instance.application, str)


@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_application_setter(instance):
    original = instance.application
    instance.application = original
    assert instance.application == original

@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_goals_type(instance):
    assert isinstance(instance.goals, str)


@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_goals_setter(instance):
    original = instance.goals
    instance.goals = original
    assert instance.goals == original

@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_background_type(instance):
    assert isinstance(instance.background, str)


@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original

@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_levelsOfAdoption_type(instance):
    assert isinstance(instance.levelsOfAdoption, str)


@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_levelsOfAdoption_setter(instance):
    original = instance.levelsOfAdoption
    instance.levelsOfAdoption = original
    assert instance.levelsOfAdoption == original

@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_problem_type(instance):
    assert isinstance(instance.problem, str)


@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_problem_setter(instance):
    original = instance.problem
    instance.problem = original
    assert instance.problem == original

@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_additionalInfo_type(instance):
    assert isinstance(instance.additionalInfo, str)


@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_additionalInfo_setter(instance):
    original = instance.additionalInfo
    instance.additionalInfo = original
    assert instance.additionalInfo == original

@given(instance=uma::RoleDescription_strategy)
@settings(max_examples=50)
def test_uma::roledescription_instantiation(instance):
    assert isinstance(instance, uma::RoleDescription)

@given(instance=uma::RoleDescription_strategy)
def test_uma::roledescription_assignmentApproaches_type(instance):
    assert isinstance(instance.assignmentApproaches, str)


@given(instance=uma::RoleDescription_strategy)
def test_uma::roledescription_assignmentApproaches_setter(instance):
    original = instance.assignmentApproaches
    instance.assignmentApproaches = original
    assert instance.assignmentApproaches == original

@given(instance=uma::RoleDescription_strategy)
def test_uma::roledescription_skills_type(instance):
    assert isinstance(instance.skills, str)


@given(instance=uma::RoleDescription_strategy)
def test_uma::roledescription_skills_setter(instance):
    original = instance.skills
    instance.skills = original
    assert instance.skills == original

@given(instance=uma::RoleDescription_strategy)
def test_uma::roledescription_synonyms_type(instance):
    assert isinstance(instance.synonyms, str)


@given(instance=uma::RoleDescription_strategy)
def test_uma::roledescription_synonyms_setter(instance):
    original = instance.synonyms
    instance.synonyms = original
    assert instance.synonyms == original

@given(instance=uma::BreakdownElementDescription_strategy)
@settings(max_examples=50)
def test_uma::breakdownelementdescription_instantiation(instance):
    assert isinstance(instance, uma::BreakdownElementDescription)

@given(instance=uma::BreakdownElementDescription_strategy)
def test_uma::breakdownelementdescription_usageGuidance_type(instance):
    assert isinstance(instance.usageGuidance, str)


@given(instance=uma::BreakdownElementDescription_strategy)
def test_uma::breakdownelementdescription_usageGuidance_setter(instance):
    original = instance.usageGuidance
    instance.usageGuidance = original
    assert instance.usageGuidance == original

@given(instance=WorkProductDescription_strategy)
@settings(max_examples=50)
def test_workproductdescription_instantiation(instance):
    assert isinstance(instance, WorkProductDescription)

@given(instance=uma::DeliverableDescription_strategy)
@settings(max_examples=50)
def test_uma::deliverabledescription_instantiation(instance):
    assert isinstance(instance, uma::DeliverableDescription)

@given(instance=uma::DeliverableDescription_strategy)
def test_uma::deliverabledescription_externalDescription_type(instance):
    assert isinstance(instance.externalDescription, str)


@given(instance=uma::DeliverableDescription_strategy)
def test_uma::deliverabledescription_externalDescription_setter(instance):
    original = instance.externalDescription
    instance.externalDescription = original
    assert instance.externalDescription == original

@given(instance=uma::DeliverableDescription_strategy)
def test_uma::deliverabledescription_packagingGuidance_type(instance):
    assert isinstance(instance.packagingGuidance, str)


@given(instance=uma::DeliverableDescription_strategy)
def test_uma::deliverabledescription_packagingGuidance_setter(instance):
    original = instance.packagingGuidance
    instance.packagingGuidance = original
    assert instance.packagingGuidance == original

@given(instance=uma::ArtifactDescription_strategy)
@settings(max_examples=50)
def test_uma::artifactdescription_instantiation(instance):
    assert isinstance(instance, uma::ArtifactDescription)

@given(instance=uma::ArtifactDescription_strategy)
def test_uma::artifactdescription_notation_type(instance):
    assert isinstance(instance.notation, str)


@given(instance=uma::ArtifactDescription_strategy)
def test_uma::artifactdescription_notation_setter(instance):
    original = instance.notation
    instance.notation = original
    assert instance.notation == original

@given(instance=uma::ArtifactDescription_strategy)
def test_uma::artifactdescription_representation_type(instance):
    assert isinstance(instance.representation, str)


@given(instance=uma::ArtifactDescription_strategy)
def test_uma::artifactdescription_representation_setter(instance):
    original = instance.representation
    instance.representation = original
    assert instance.representation == original

@given(instance=uma::ArtifactDescription_strategy)
def test_uma::artifactdescription_representationOptions_type(instance):
    assert isinstance(instance.representationOptions, str)


@given(instance=uma::ArtifactDescription_strategy)
def test_uma::artifactdescription_representationOptions_setter(instance):
    original = instance.representationOptions
    instance.representationOptions = original
    assert instance.representationOptions == original

@given(instance=uma::ArtifactDescription_strategy)
def test_uma::artifactdescription_briefOutline_type(instance):
    assert isinstance(instance.briefOutline, str)


@given(instance=uma::ArtifactDescription_strategy)
def test_uma::artifactdescription_briefOutline_setter(instance):
    original = instance.briefOutline
    instance.briefOutline = original
    assert instance.briefOutline == original

@given(instance=WorkProduct_strategy)
@settings(max_examples=50)
def test_workproduct_instantiation(instance):
    assert isinstance(instance, WorkProduct)

@given(instance=uma::Outcome_strategy)
@settings(max_examples=50)
def test_uma::outcome_instantiation(instance):
    assert isinstance(instance, uma::Outcome)

@given(instance=uma::Deliverable_strategy)
@settings(max_examples=50)
def test_uma::deliverable_instantiation(instance):
    assert isinstance(instance, uma::Deliverable)

@given(instance=uma::Deliverable_strategy)
def test_uma::deliverable_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=uma::Deliverable_strategy)
def test_uma::deliverable_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=uma::Deliverable_strategy)
def test_uma::deliverable_deliveredWorkProduct_type(instance):
    assert isinstance(instance.deliveredWorkProduct, str)


@given(instance=uma::Deliverable_strategy)
def test_uma::deliverable_deliveredWorkProduct_setter(instance):
    original = instance.deliveredWorkProduct
    instance.deliveredWorkProduct = original
    assert instance.deliveredWorkProduct == original

@given(instance=uma::Artifact_strategy)
@settings(max_examples=50)
def test_uma::artifact_instantiation(instance):
    assert isinstance(instance, uma::Artifact)

@given(instance=uma::Artifact_strategy)
def test_uma::artifact_group3_type(instance):
    assert isinstance(instance.group3, str)


@given(instance=uma::Artifact_strategy)
def test_uma::artifact_group3_setter(instance):
    original = instance.group3
    instance.group3 = original
    assert instance.group3 == original

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=uma::MethodElementProperty_strategy)
@settings(max_examples=50)
def test_uma::methodelementproperty_instantiation(instance):
    assert isinstance(instance, uma::MethodElementProperty)

@given(instance=uma::MethodElementProperty_strategy)
def test_uma::methodelementproperty_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=uma::MethodElementProperty_strategy)
def test_uma::methodelementproperty_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uma::MethodElement_strategy)
@settings(max_examples=50)
def test_uma::methodelement_instantiation(instance):
    assert isinstance(instance, uma::MethodElement)

@given(instance=uma::MethodElement_strategy)
def test_uma::methodelement_orderingGuide_type(instance):
    assert isinstance(instance.orderingGuide, str)


@given(instance=uma::MethodElement_strategy)
def test_uma::methodelement_orderingGuide_setter(instance):
    original = instance.orderingGuide
    instance.orderingGuide = original
    assert instance.orderingGuide == original

@given(instance=uma::MethodElement_strategy)
def test_uma::methodelement_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=uma::MethodElement_strategy)
def test_uma::methodelement_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=uma::MethodElement_strategy)
def test_uma::methodelement_presentationName_type(instance):
    assert isinstance(instance.presentationName, str)


@given(instance=uma::MethodElement_strategy)
def test_uma::methodelement_presentationName_setter(instance):
    original = instance.presentationName
    instance.presentationName = original
    assert instance.presentationName == original

@given(instance=uma::MethodElement_strategy)
def test_uma::methodelement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=uma::MethodElement_strategy)
def test_uma::methodelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=uma::MethodElement_strategy)
def test_uma::methodelement_suppressed_type(instance):
    assert isinstance(instance.suppressed, str)


@given(instance=uma::MethodElement_strategy)
def test_uma::methodelement_suppressed_setter(instance):
    original = instance.suppressed
    instance.suppressed = original
    assert instance.suppressed == original

@given(instance=uma::MethodElement_strategy)
def test_uma::methodelement_briefDescription_type(instance):
    assert isinstance(instance.briefDescription, str)


@given(instance=uma::MethodElement_strategy)
def test_uma::methodelement_briefDescription_setter(instance):
    original = instance.briefDescription
    instance.briefDescription = original
    assert instance.briefDescription == original

@given(instance=uma::ApplicableMetaClassInfo_strategy)
@settings(max_examples=50)
def test_uma::applicablemetaclassinfo_instantiation(instance):
    assert isinstance(instance, uma::ApplicableMetaClassInfo)

@given(instance=uma::ApplicableMetaClassInfo_strategy)
def test_uma::applicablemetaclassinfo_isPrimaryExtension_type(instance):
    assert isinstance(instance.isPrimaryExtension, str)


@given(instance=uma::ApplicableMetaClassInfo_strategy)
def test_uma::applicablemetaclassinfo_isPrimaryExtension_setter(instance):
    original = instance.isPrimaryExtension
    instance.isPrimaryExtension = original
    assert instance.isPrimaryExtension == original

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

@given(instance=uma::PlanningData_strategy)
@settings(max_examples=50)
def test_uma::planningdata_instantiation(instance):
    assert isinstance(instance, uma::PlanningData)

@given(instance=uma::PlanningData_strategy)
def test_uma::planningdata_startDate_type(instance):
    assert isinstance(instance.startDate, str)


@given(instance=uma::PlanningData_strategy)
def test_uma::planningdata_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original

@given(instance=uma::PlanningData_strategy)
def test_uma::planningdata_rank_type(instance):
    assert isinstance(instance.rank, str)


@given(instance=uma::PlanningData_strategy)
def test_uma::planningdata_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=uma::PlanningData_strategy)
def test_uma::planningdata_finishDate_type(instance):
    assert isinstance(instance.finishDate, str)


@given(instance=uma::PlanningData_strategy)
def test_uma::planningdata_finishDate_setter(instance):
    original = instance.finishDate
    instance.finishDate = original
    assert instance.finishDate == original

@given(instance=uma::BreakdownElement_strategy)
@settings(max_examples=50)
def test_uma::breakdownelement_instantiation(instance):
    assert isinstance(instance, uma::BreakdownElement)

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_presentedBefore_type(instance):
    assert isinstance(instance.presentedBefore, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_presentedBefore_setter(instance):
    original = instance.presentedBefore
    instance.presentedBefore = original
    assert instance.presentedBefore == original

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_isPlanned_type(instance):
    assert isinstance(instance.isPlanned, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_isPlanned_setter(instance):
    original = instance.isPlanned
    instance.isPlanned = original
    assert instance.isPlanned == original

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_concept_type(instance):
    assert isinstance(instance.concept, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_concept_setter(instance):
    original = instance.concept
    instance.concept = original
    assert instance.concept == original

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_example_type(instance):
    assert isinstance(instance.example, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_example_setter(instance):
    original = instance.example
    instance.example = original
    assert instance.example == original

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_hasMultipleOccurrences_type(instance):
    assert isinstance(instance.hasMultipleOccurrences, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_hasMultipleOccurrences_setter(instance):
    original = instance.hasMultipleOccurrences
    instance.hasMultipleOccurrences = original
    assert instance.hasMultipleOccurrences == original

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_group1_type(instance):
    assert isinstance(instance.group1, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_group1_setter(instance):
    original = instance.group1
    instance.group1 = original
    assert instance.group1 == original

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_isOptional_type(instance):
    assert isinstance(instance.isOptional, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_superActivity_type(instance):
    assert isinstance(instance.superActivity, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_superActivity_setter(instance):
    original = instance.superActivity
    instance.superActivity = original
    assert instance.superActivity == original

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_guideline_type(instance):
    assert isinstance(instance.guideline, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_guideline_setter(instance):
    original = instance.guideline
    instance.guideline = original
    assert instance.guideline == original

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_whitepaper_type(instance):
    assert isinstance(instance.whitepaper, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_whitepaper_setter(instance):
    original = instance.whitepaper
    instance.whitepaper = original
    assert instance.whitepaper == original

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_presentedAfter_type(instance):
    assert isinstance(instance.presentedAfter, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_presentedAfter_setter(instance):
    original = instance.presentedAfter
    instance.presentedAfter = original
    assert instance.presentedAfter == original

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_checklist_type(instance):
    assert isinstance(instance.checklist, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_checklist_setter(instance):
    original = instance.checklist
    instance.checklist = original
    assert instance.checklist == original

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_prefix_type(instance):
    assert isinstance(instance.prefix, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_reusableAsset_type(instance):
    assert isinstance(instance.reusableAsset, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_reusableAsset_setter(instance):
    original = instance.reusableAsset
    instance.reusableAsset = original
    assert instance.reusableAsset == original

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_supportingMaterial_type(instance):
    assert isinstance(instance.supportingMaterial, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_supportingMaterial_setter(instance):
    original = instance.supportingMaterial
    instance.supportingMaterial = original
    assert instance.supportingMaterial == original

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_planningData_type(instance):
    assert isinstance(instance.planningData, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_planningData_setter(instance):
    original = instance.planningData
    instance.planningData = original
    assert instance.planningData == original

@given(instance=BreakdownElementDescription_strategy)
@settings(max_examples=50)
def test_breakdownelementdescription_instantiation(instance):
    assert isinstance(instance, BreakdownElementDescription)

@given(instance=uma::DescriptorDescription_strategy)
@settings(max_examples=50)
def test_uma::descriptordescription_instantiation(instance):
    assert isinstance(instance, uma::DescriptorDescription)

@given(instance=uma::DescriptorDescription_strategy)
def test_uma::descriptordescription_refinedDescription_type(instance):
    assert isinstance(instance.refinedDescription, str)


@given(instance=uma::DescriptorDescription_strategy)
def test_uma::descriptordescription_refinedDescription_setter(instance):
    original = instance.refinedDescription
    instance.refinedDescription = original
    assert instance.refinedDescription == original

@given(instance=uma::WorkProductType_strategy)
@settings(max_examples=50)
def test_uma::workproducttype_instantiation(instance):
    assert isinstance(instance, uma::WorkProductType)

@given(instance=uma::WorkProductType_strategy)
def test_uma::workproducttype_workProduct_type(instance):
    assert isinstance(instance.workProduct, str)


@given(instance=uma::WorkProductType_strategy)
def test_uma::workproducttype_workProduct_setter(instance):
    original = instance.workProduct
    instance.workProduct = original
    assert instance.workProduct == original

@given(instance=uma::WorkProductType_strategy)
def test_uma::workproducttype_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::WorkProductType_strategy)
def test_uma::workproducttype_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma::WorkProduct_strategy)
@settings(max_examples=50)
def test_uma::workproduct_instantiation(instance):
    assert isinstance(instance, uma::WorkProduct)

@given(instance=uma::WorkProduct_strategy)
def test_uma::workproduct_estimate_type(instance):
    assert isinstance(instance.estimate, str)


@given(instance=uma::WorkProduct_strategy)
def test_uma::workproduct_estimate_setter(instance):
    original = instance.estimate
    instance.estimate = original
    assert instance.estimate == original

@given(instance=uma::WorkProduct_strategy)
def test_uma::workproduct_estimationConsiderations_type(instance):
    assert isinstance(instance.estimationConsiderations, str)


@given(instance=uma::WorkProduct_strategy)
def test_uma::workproduct_estimationConsiderations_setter(instance):
    original = instance.estimationConsiderations
    instance.estimationConsiderations = original
    assert instance.estimationConsiderations == original

@given(instance=uma::WorkProduct_strategy)
def test_uma::workproduct_toolMentor_type(instance):
    assert isinstance(instance.toolMentor, str)


@given(instance=uma::WorkProduct_strategy)
def test_uma::workproduct_toolMentor_setter(instance):
    original = instance.toolMentor
    instance.toolMentor = original
    assert instance.toolMentor == original

@given(instance=uma::WorkProduct_strategy)
def test_uma::workproduct_template_type(instance):
    assert isinstance(instance.template, str)


@given(instance=uma::WorkProduct_strategy)
def test_uma::workproduct_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=uma::WorkProduct_strategy)
def test_uma::workproduct_report_type(instance):
    assert isinstance(instance.report, str)


@given(instance=uma::WorkProduct_strategy)
def test_uma::workproduct_report_setter(instance):
    original = instance.report
    instance.report = original
    assert instance.report == original

@given(instance=uma::WorkProduct_strategy)
def test_uma::workproduct_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::WorkProduct_strategy)
def test_uma::workproduct_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma::WorkProductDescription_strategy)
@settings(max_examples=50)
def test_uma::workproductdescription_instantiation(instance):
    assert isinstance(instance, uma::WorkProductDescription)

@given(instance=uma::WorkProductDescription_strategy)
def test_uma::workproductdescription_reasonsForNotNeeding_type(instance):
    assert isinstance(instance.reasonsForNotNeeding, str)


@given(instance=uma::WorkProductDescription_strategy)
def test_uma::workproductdescription_reasonsForNotNeeding_setter(instance):
    original = instance.reasonsForNotNeeding
    instance.reasonsForNotNeeding = original
    assert instance.reasonsForNotNeeding == original

@given(instance=uma::WorkProductDescription_strategy)
def test_uma::workproductdescription_impactOfNotHaving_type(instance):
    assert isinstance(instance.impactOfNotHaving, str)


@given(instance=uma::WorkProductDescription_strategy)
def test_uma::workproductdescription_impactOfNotHaving_setter(instance):
    original = instance.impactOfNotHaving
    instance.impactOfNotHaving = original
    assert instance.impactOfNotHaving == original

@given(instance=uma::WorkProductDescription_strategy)
def test_uma::workproductdescription_purpose_type(instance):
    assert isinstance(instance.purpose, str)


@given(instance=uma::WorkProductDescription_strategy)
def test_uma::workproductdescription_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original

@given(instance=uma::WorkOrder_strategy)
@settings(max_examples=50)
def test_uma::workorder_instantiation(instance):
    assert isinstance(instance, uma::WorkOrder)

@given(instance=uma::WorkOrder_strategy)
def test_uma::workorder_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=uma::WorkOrder_strategy)
def test_uma::workorder_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=uma::WorkOrder_strategy)
def test_uma::workorder_properties_type(instance):
    assert isinstance(instance.properties, str)


@given(instance=uma::WorkOrder_strategy)
def test_uma::workorder_properties_setter(instance):
    original = instance.properties
    instance.properties = original
    assert instance.properties == original

@given(instance=uma::WorkOrder_strategy)
def test_uma::workorder_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=uma::WorkOrder_strategy)
def test_uma::workorder_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uma::WorkOrder_strategy)
def test_uma::workorder_linkType_type(instance):
    assert isinstance(instance.linkType, str)


@given(instance=uma::WorkOrder_strategy)
def test_uma::workorder_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original

@given(instance=uma::WorkBreakdownElement_strategy)
@settings(max_examples=50)
def test_uma::workbreakdownelement_instantiation(instance):
    assert isinstance(instance, uma::WorkBreakdownElement)

@given(instance=uma::WorkBreakdownElement_strategy)
def test_uma::workbreakdownelement_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::WorkBreakdownElement_strategy)
def test_uma::workbreakdownelement_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma::WorkBreakdownElement_strategy)
def test_uma::workbreakdownelement_isEventDriven_type(instance):
    assert isinstance(instance.isEventDriven, str)


@given(instance=uma::WorkBreakdownElement_strategy)
def test_uma::workbreakdownelement_isEventDriven_setter(instance):
    original = instance.isEventDriven
    instance.isEventDriven = original
    assert instance.isEventDriven == original

@given(instance=uma::WorkBreakdownElement_strategy)
def test_uma::workbreakdownelement_isRepeatable_type(instance):
    assert isinstance(instance.isRepeatable, str)


@given(instance=uma::WorkBreakdownElement_strategy)
def test_uma::workbreakdownelement_isRepeatable_setter(instance):
    original = instance.isRepeatable
    instance.isRepeatable = original
    assert instance.isRepeatable == original

@given(instance=uma::WorkBreakdownElement_strategy)
def test_uma::workbreakdownelement_isOngoing_type(instance):
    assert isinstance(instance.isOngoing, str)


@given(instance=uma::WorkBreakdownElement_strategy)
def test_uma::workbreakdownelement_isOngoing_setter(instance):
    original = instance.isOngoing
    instance.isOngoing = original
    assert instance.isOngoing == original

@given(instance=Concept_strategy)
@settings(max_examples=50)
def test_concept_instantiation(instance):
    assert isinstance(instance, Concept)

@given(instance=uma::Whitepaper_strategy)
@settings(max_examples=50)
def test_uma::whitepaper_instantiation(instance):
    assert isinstance(instance, uma::Whitepaper)

@given(instance=uma::WorkDefinition_strategy)
@settings(max_examples=50)
def test_uma::workdefinition_instantiation(instance):
    assert isinstance(instance, uma::WorkDefinition)

@given(instance=uma::WorkDefinition_strategy)
def test_uma::workdefinition_precondition_type(instance):
    assert isinstance(instance.precondition, str)


@given(instance=uma::WorkDefinition_strategy)
def test_uma::workdefinition_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original

@given(instance=uma::WorkDefinition_strategy)
def test_uma::workdefinition_postcondition_type(instance):
    assert isinstance(instance.postcondition, str)


@given(instance=uma::WorkDefinition_strategy)
def test_uma::workdefinition_postcondition_setter(instance):
    original = instance.postcondition
    instance.postcondition = original
    assert instance.postcondition == original

@given(instance=uma::TermDefinition_strategy)
@settings(max_examples=50)
def test_uma::termdefinition_instantiation(instance):
    assert isinstance(instance, uma::TermDefinition)

@given(instance=uma::Template_strategy)
@settings(max_examples=50)
def test_uma::template_instantiation(instance):
    assert isinstance(instance, uma::Template)

@given(instance=uma::TeamProfile_strategy)
@settings(max_examples=50)
def test_uma::teamprofile_instantiation(instance):
    assert isinstance(instance, uma::TeamProfile)

@given(instance=uma::TeamProfile_strategy)
def test_uma::teamprofile_superTeam_type(instance):
    assert isinstance(instance.superTeam, str)


@given(instance=uma::TeamProfile_strategy)
def test_uma::teamprofile_superTeam_setter(instance):
    original = instance.superTeam
    instance.superTeam = original
    assert instance.superTeam == original

@given(instance=uma::TeamProfile_strategy)
def test_uma::teamprofile_subTeam_type(instance):
    assert isinstance(instance.subTeam, str)


@given(instance=uma::TeamProfile_strategy)
def test_uma::teamprofile_subTeam_setter(instance):
    original = instance.subTeam
    instance.subTeam = original
    assert instance.subTeam == original

@given(instance=uma::TeamProfile_strategy)
def test_uma::teamprofile_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::TeamProfile_strategy)
def test_uma::teamprofile_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma::TeamProfile_strategy)
def test_uma::teamprofile_role_type(instance):
    assert isinstance(instance.role, str)


@given(instance=uma::TeamProfile_strategy)
def test_uma::teamprofile_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=uma::ToolMentor_strategy)
@settings(max_examples=50)
def test_uma::toolmentor_instantiation(instance):
    assert isinstance(instance, uma::ToolMentor)

@given(instance=uma::Tool_strategy)
@settings(max_examples=50)
def test_uma::tool_instantiation(instance):
    assert isinstance(instance, uma::Tool)

@given(instance=uma::Tool_strategy)
def test_uma::tool_toolMentor_type(instance):
    assert isinstance(instance.toolMentor, str)


@given(instance=uma::Tool_strategy)
def test_uma::tool_toolMentor_setter(instance):
    original = instance.toolMentor
    instance.toolMentor = original
    assert instance.toolMentor == original

@given(instance=uma::Tool_strategy)
def test_uma::tool_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::Tool_strategy)
def test_uma::tool_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma::TaskDescription_strategy)
@settings(max_examples=50)
def test_uma::taskdescription_instantiation(instance):
    assert isinstance(instance, uma::TaskDescription)

@given(instance=uma::TaskDescription_strategy)
def test_uma::taskdescription_purpose_type(instance):
    assert isinstance(instance.purpose, str)


@given(instance=uma::TaskDescription_strategy)
def test_uma::taskdescription_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original

@given(instance=uma::TaskDescription_strategy)
def test_uma::taskdescription_alternatives_type(instance):
    assert isinstance(instance.alternatives, str)


@given(instance=uma::TaskDescription_strategy)
def test_uma::taskdescription_alternatives_setter(instance):
    original = instance.alternatives
    instance.alternatives = original
    assert instance.alternatives == original

@given(instance=uma::Task_strategy)
@settings(max_examples=50)
def test_uma::task_instantiation(instance):
    assert isinstance(instance, uma::Task)

@given(instance=uma::Task_strategy)
def test_uma::task_performedBy_type(instance):
    assert isinstance(instance.performedBy, str)


@given(instance=uma::Task_strategy)
def test_uma::task_performedBy_setter(instance):
    original = instance.performedBy
    instance.performedBy = original
    assert instance.performedBy == original

@given(instance=uma::Task_strategy)
def test_uma::task_estimationConsiderations_type(instance):
    assert isinstance(instance.estimationConsiderations, str)


@given(instance=uma::Task_strategy)
def test_uma::task_estimationConsiderations_setter(instance):
    original = instance.estimationConsiderations
    instance.estimationConsiderations = original
    assert instance.estimationConsiderations == original

@given(instance=uma::Task_strategy)
def test_uma::task_optionalInput_type(instance):
    assert isinstance(instance.optionalInput, str)


@given(instance=uma::Task_strategy)
def test_uma::task_optionalInput_setter(instance):
    original = instance.optionalInput
    instance.optionalInput = original
    assert instance.optionalInput == original

@given(instance=uma::Task_strategy)
def test_uma::task_estimate_type(instance):
    assert isinstance(instance.estimate, str)


@given(instance=uma::Task_strategy)
def test_uma::task_estimate_setter(instance):
    original = instance.estimate
    instance.estimate = original
    assert instance.estimate == original

@given(instance=uma::Task_strategy)
def test_uma::task_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::Task_strategy)
def test_uma::task_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma::Task_strategy)
def test_uma::task_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=uma::Task_strategy)
def test_uma::task_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=uma::Task_strategy)
def test_uma::task_mandatoryInput_type(instance):
    assert isinstance(instance.mandatoryInput, str)


@given(instance=uma::Task_strategy)
def test_uma::task_mandatoryInput_setter(instance):
    original = instance.mandatoryInput
    instance.mandatoryInput = original
    assert instance.mandatoryInput == original

@given(instance=uma::Task_strategy)
def test_uma::task_precondition_type(instance):
    assert isinstance(instance.precondition, str)


@given(instance=uma::Task_strategy)
def test_uma::task_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original

@given(instance=uma::Task_strategy)
def test_uma::task_additionallyPerformedBy_type(instance):
    assert isinstance(instance.additionallyPerformedBy, str)


@given(instance=uma::Task_strategy)
def test_uma::task_additionallyPerformedBy_setter(instance):
    original = instance.additionallyPerformedBy
    instance.additionallyPerformedBy = original
    assert instance.additionallyPerformedBy == original

@given(instance=uma::Task_strategy)
def test_uma::task_toolMentor_type(instance):
    assert isinstance(instance.toolMentor, str)


@given(instance=uma::Task_strategy)
def test_uma::task_toolMentor_setter(instance):
    original = instance.toolMentor
    instance.toolMentor = original
    assert instance.toolMentor == original

@given(instance=uma::Task_strategy)
def test_uma::task_postcondition_type(instance):
    assert isinstance(instance.postcondition, str)


@given(instance=uma::Task_strategy)
def test_uma::task_postcondition_setter(instance):
    original = instance.postcondition
    instance.postcondition = original
    assert instance.postcondition == original

@given(instance=uma::SupportingMaterial_strategy)
@settings(max_examples=50)
def test_uma::supportingmaterial_instantiation(instance):
    assert isinstance(instance, uma::SupportingMaterial)

@given(instance=uma::RoleSetGrouping_strategy)
@settings(max_examples=50)
def test_uma::rolesetgrouping_instantiation(instance):
    assert isinstance(instance, uma::RoleSetGrouping)

@given(instance=uma::RoleSetGrouping_strategy)
def test_uma::rolesetgrouping_roleSet_type(instance):
    assert isinstance(instance.roleSet, str)


@given(instance=uma::RoleSetGrouping_strategy)
def test_uma::rolesetgrouping_roleSet_setter(instance):
    original = instance.roleSet
    instance.roleSet = original
    assert instance.roleSet == original

@given(instance=uma::RoleSetGrouping_strategy)
def test_uma::rolesetgrouping_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::RoleSetGrouping_strategy)
def test_uma::rolesetgrouping_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma::RoleSet_strategy)
@settings(max_examples=50)
def test_uma::roleset_instantiation(instance):
    assert isinstance(instance, uma::RoleSet)

@given(instance=uma::RoleSet_strategy)
def test_uma::roleset_role_type(instance):
    assert isinstance(instance.role, str)


@given(instance=uma::RoleSet_strategy)
def test_uma::roleset_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=uma::RoleSet_strategy)
def test_uma::roleset_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::RoleSet_strategy)
def test_uma::roleset_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=Descriptor_strategy)
@settings(max_examples=50)
def test_descriptor_instantiation(instance):
    assert isinstance(instance, Descriptor)

@given(instance=uma::WorkProductDescriptor_strategy)
@settings(max_examples=50)
def test_uma::workproductdescriptor_instantiation(instance):
    assert isinstance(instance, uma::WorkProductDescriptor)

@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_deliverableParts_type(instance):
    assert isinstance(instance.deliverableParts, str)


@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_deliverableParts_setter(instance):
    original = instance.deliverableParts
    instance.deliverableParts = original
    assert instance.deliverableParts == original

@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_mandatoryInputTo_type(instance):
    assert isinstance(instance.mandatoryInputTo, str)


@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_mandatoryInputTo_setter(instance):
    original = instance.mandatoryInputTo
    instance.mandatoryInputTo = original
    assert instance.mandatoryInputTo == original

@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_impactedBy_type(instance):
    assert isinstance(instance.impactedBy, str)


@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_impactedBy_setter(instance):
    original = instance.impactedBy
    instance.impactedBy = original
    assert instance.impactedBy == original

@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_activityExitState_type(instance):
    assert isinstance(instance.activityExitState, str)


@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_activityExitState_setter(instance):
    original = instance.activityExitState
    instance.activityExitState = original
    assert instance.activityExitState == original

@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_outputFrom_type(instance):
    assert isinstance(instance.outputFrom, str)


@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_outputFrom_setter(instance):
    original = instance.outputFrom
    instance.outputFrom = original
    assert instance.outputFrom == original

@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_workProduct_type(instance):
    assert isinstance(instance.workProduct, str)


@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_workProduct_setter(instance):
    original = instance.workProduct
    instance.workProduct = original
    assert instance.workProduct == original

@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_responsibleRole_type(instance):
    assert isinstance(instance.responsibleRole, str)


@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_responsibleRole_setter(instance):
    original = instance.responsibleRole
    instance.responsibleRole = original
    assert instance.responsibleRole == original

@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_externalInputTo_type(instance):
    assert isinstance(instance.externalInputTo, str)


@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_externalInputTo_setter(instance):
    original = instance.externalInputTo
    instance.externalInputTo = original
    assert instance.externalInputTo == original

@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_group2_type(instance):
    assert isinstance(instance.group2, str)


@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_group2_setter(instance):
    original = instance.group2
    instance.group2 = original
    assert instance.group2 == original

@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_impacts_type(instance):
    assert isinstance(instance.impacts, str)


@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_impacts_setter(instance):
    original = instance.impacts
    instance.impacts = original
    assert instance.impacts == original

@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_activityEntryState_type(instance):
    assert isinstance(instance.activityEntryState, str)


@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_activityEntryState_setter(instance):
    original = instance.activityEntryState
    instance.activityEntryState = original
    assert instance.activityEntryState == original

@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_optionalInputTo_type(instance):
    assert isinstance(instance.optionalInputTo, str)


@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_optionalInputTo_setter(instance):
    original = instance.optionalInputTo
    instance.optionalInputTo = original
    assert instance.optionalInputTo == original

@given(instance=uma::RoleDescriptor_strategy)
@settings(max_examples=50)
def test_uma::roledescriptor_instantiation(instance):
    assert isinstance(instance, uma::RoleDescriptor)

@given(instance=uma::RoleDescriptor_strategy)
def test_uma::roledescriptor_responsibleFor_type(instance):
    assert isinstance(instance.responsibleFor, str)


@given(instance=uma::RoleDescriptor_strategy)
def test_uma::roledescriptor_responsibleFor_setter(instance):
    original = instance.responsibleFor
    instance.responsibleFor = original
    assert instance.responsibleFor == original

@given(instance=uma::RoleDescriptor_strategy)
def test_uma::roledescriptor_role_type(instance):
    assert isinstance(instance.role, str)


@given(instance=uma::RoleDescriptor_strategy)
def test_uma::roledescriptor_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=uma::Roadmap_strategy)
@settings(max_examples=50)
def test_uma::roadmap_instantiation(instance):
    assert isinstance(instance, uma::Roadmap)

@given(instance=uma::ReusableAsset_strategy)
@settings(max_examples=50)
def test_uma::reusableasset_instantiation(instance):
    assert isinstance(instance, uma::ReusableAsset)

@given(instance=uma::Report_strategy)
@settings(max_examples=50)
def test_uma::report_instantiation(instance):
    assert isinstance(instance, uma::Report)

@given(instance=uma::ActivityDescription_strategy)
@settings(max_examples=50)
def test_uma::activitydescription_instantiation(instance):
    assert isinstance(instance, uma::ActivityDescription)

@given(instance=uma::ActivityDescription_strategy)
def test_uma::activitydescription_purpose_type(instance):
    assert isinstance(instance.purpose, str)


@given(instance=uma::ActivityDescription_strategy)
def test_uma::activitydescription_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original

@given(instance=uma::ActivityDescription_strategy)
def test_uma::activitydescription_howToStaff_type(instance):
    assert isinstance(instance.howToStaff, str)


@given(instance=uma::ActivityDescription_strategy)
def test_uma::activitydescription_howToStaff_setter(instance):
    original = instance.howToStaff
    instance.howToStaff = original
    assert instance.howToStaff == original

@given(instance=uma::ActivityDescription_strategy)
def test_uma::activitydescription_alternatives_type(instance):
    assert isinstance(instance.alternatives, str)


@given(instance=uma::ActivityDescription_strategy)
def test_uma::activitydescription_alternatives_setter(instance):
    original = instance.alternatives
    instance.alternatives = original
    assert instance.alternatives == original

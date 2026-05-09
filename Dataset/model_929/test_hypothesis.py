import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    MethodConfiguration,
    uma::ProcessFamily,
    Process,
    uma::DeliveryProcess,
    ProcessPackage,
    uma::ProcessPlanningTemplate,
    uma::CapabilityPattern,
    ContentCategory,
    uma::Discipline,
    uma::CustomCategory,
    uma::RoleSetGrouping,
    uma::Tool,
    uma::DisciplineGrouping,
    uma::WorkProductType,
    uma::Domain,
    uma::RoleSet,
    uma::Transition,
    uma::Vertex,
    uma::Region,
    Vertex,
    uma::PseudoState,
    uma::State,
    Concept,
    uma::Whitepaper,
    Guidance,
    uma::Practice,
    uma::TermDefinition,
    ActivityDescription,
    uma::ProcessDescription,
    ProcessDescription,
    uma::DeliveryProcessDescription,
    BreakdownElementDescription,
    uma::DescriptorDescription,
    uma::ActivityDescription,
    RoleDescriptor,
    uma::CompositeRole,
    ProcessElement,
    uma::WorkOrder,
    Descriptor,
    uma::WorkProductDescriptor,
    uma::ProcessComponentDescriptor,
    uma::RoleDescriptor,
    Activity,
    uma::Process,
    uma::Phase,
    uma::Iteration,
    uma::PlanningData,
    BreakdownElement,
    uma::TeamProfile,
    uma::ProcessComponentInterface,
    uma::Descriptor,
    uma::WorkBreakdownElement,
    uma::Roadmap,
    uma::BreakdownElement,
    WorkBreakdownElement,
    uma::TaskDescriptor,
    uma::Milestone,
    uma::Dimension,
    GraphicPrimitive,
    uma::Ellipse,
    uma::Polyline,
    LeafElement,
    uma::GraphicPrimitive,
    uma::Image,
    uma::TextElement,
    SemanticModelBridge,
    uma::UMASemanticModelBridge,
    uma::CoreSemanticModelBridge,
    uma::SimpleSemanticModelElement,
    GraphNode,
    DiagramElement,
    uma::LeafElement,
    uma::GraphElement,
    GraphElement,
    uma::GraphEdge,
    uma::GraphNode,
    uma::Diagram,
    uma::Property,
    uma::Reference,
    uma::SemanticModelBridge,
    uma::GraphConnector,
    uma::DiagramLink,
    ContentDescription,
    uma::BreakdownElementDescription,
    uma::WorkProductDescription,
    WorkProductDescription,
    uma::ArtifactDescription,
    uma::Point,
    uma::PracticeDescription,
    uma::GuidanceDescription,
    uma::TaskDescription,
    uma::RoleDescription,
    uma::DeliverableDescription,
    MethodPackage,
    uma::ProcessPackage,
    uma::ContentPackage,
    Package,
    WorkProduct,
    uma::Outcome,
    uma::Deliverable,
    uma::Artifact,
    Section,
    MethodUnit,
    uma::MethodConfiguration,
    uma::MethodLibrary,
    uma::ProcessComponent,
    uma::MethodPlugin,
    WorkDefinition,
    uma::StateMachine,
    uma::Step,
    uma::EstimationConsiderations,
    uma::ToolMentor,
    uma::Template,
    uma::Report,
    ContentElement,
    uma::ContentCategory,
    uma::Task,
    uma::Guidance,
    uma::WorkProduct,
    uma::Role,
    uma::ContentDescription,
    Classifier,
    uma::ReusableAsset,
    uma::Example,
    uma::Guideline,
    uma::Checklist,
    uma::Concept,
    uma::SupportingMaterial,
    VariabilityElement,
    uma::Section,
    uma::Activity,
    DescribableElement,
    uma::ProcessElement,
    uma::ContentElement,
    MethodElement,
    uma::DescribableElement,
    uma::WorkDefinition,
    uma::MethodUnit,
    uma::VariabilityElement,
    uma::MethodPackage,
    uma::DiagramElement,
    uma::Constraint,
    Namespace,
    NamedElement,
    uma::Namespace,
    uma::PackageableElement,
    Element,
    uma::NamedElement,
    uma::Element,
    PackageableElement,
    uma::MethodElement,
    uma::Package,
    uma::Type,
    Type,
    uma::Classifier,
    WorkOrderType,
    PseudoStateKind,
    VariabilityType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_methodconfiguration_is_not_abstract():
    assert not inspect.isabstract(MethodConfiguration)


def test_methodconfiguration_constructor_exists():
    assert callable(MethodConfiguration.__init__)


def test_methodconfiguration_constructor_args():
    sig = inspect.signature(MethodConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_uma::processfamily_is_not_abstract():
    assert not inspect.isabstract(uma::ProcessFamily)


def test_uma::processfamily_constructor_exists():
    assert callable(uma::ProcessFamily.__init__)


def test_uma::processfamily_constructor_args():
    sig = inspect.signature(uma::ProcessFamily.__init__)
    params = list(sig.parameters.keys())



def test_process_is_not_abstract():
    assert not inspect.isabstract(Process)


def test_process_constructor_exists():
    assert callable(Process.__init__)


def test_process_constructor_args():
    sig = inspect.signature(Process.__init__)
    params = list(sig.parameters.keys())



def test_uma::deliveryprocess_is_not_abstract():
    assert not inspect.isabstract(uma::DeliveryProcess)


def test_uma::deliveryprocess_constructor_exists():
    assert callable(uma::DeliveryProcess.__init__)


def test_uma::deliveryprocess_constructor_args():
    sig = inspect.signature(uma::DeliveryProcess.__init__)
    params = list(sig.parameters.keys())



def test_processpackage_is_not_abstract():
    assert not inspect.isabstract(ProcessPackage)


def test_processpackage_constructor_exists():
    assert callable(ProcessPackage.__init__)


def test_processpackage_constructor_args():
    sig = inspect.signature(ProcessPackage.__init__)
    params = list(sig.parameters.keys())



def test_uma::processplanningtemplate_is_not_abstract():
    assert not inspect.isabstract(uma::ProcessPlanningTemplate)


def test_uma::processplanningtemplate_constructor_exists():
    assert callable(uma::ProcessPlanningTemplate.__init__)


def test_uma::processplanningtemplate_constructor_args():
    sig = inspect.signature(uma::ProcessPlanningTemplate.__init__)
    params = list(sig.parameters.keys())



def test_uma::capabilitypattern_is_not_abstract():
    assert not inspect.isabstract(uma::CapabilityPattern)


def test_uma::capabilitypattern_constructor_exists():
    assert callable(uma::CapabilityPattern.__init__)


def test_uma::capabilitypattern_constructor_args():
    sig = inspect.signature(uma::CapabilityPattern.__init__)
    params = list(sig.parameters.keys())



def test_contentcategory_is_not_abstract():
    assert not inspect.isabstract(ContentCategory)


def test_contentcategory_constructor_exists():
    assert callable(ContentCategory.__init__)


def test_contentcategory_constructor_args():
    sig = inspect.signature(ContentCategory.__init__)
    params = list(sig.parameters.keys())



def test_uma::discipline_is_not_abstract():
    assert not inspect.isabstract(uma::Discipline)


def test_uma::discipline_constructor_exists():
    assert callable(uma::Discipline.__init__)


def test_uma::discipline_constructor_args():
    sig = inspect.signature(uma::Discipline.__init__)
    params = list(sig.parameters.keys())



def test_uma::customcategory_is_not_abstract():
    assert not inspect.isabstract(uma::CustomCategory)


def test_uma::customcategory_constructor_exists():
    assert callable(uma::CustomCategory.__init__)


def test_uma::customcategory_constructor_args():
    sig = inspect.signature(uma::CustomCategory.__init__)
    params = list(sig.parameters.keys())



def test_uma::rolesetgrouping_is_not_abstract():
    assert not inspect.isabstract(uma::RoleSetGrouping)


def test_uma::rolesetgrouping_constructor_exists():
    assert callable(uma::RoleSetGrouping.__init__)


def test_uma::rolesetgrouping_constructor_args():
    sig = inspect.signature(uma::RoleSetGrouping.__init__)
    params = list(sig.parameters.keys())



def test_uma::tool_is_not_abstract():
    assert not inspect.isabstract(uma::Tool)


def test_uma::tool_constructor_exists():
    assert callable(uma::Tool.__init__)


def test_uma::tool_constructor_args():
    sig = inspect.signature(uma::Tool.__init__)
    params = list(sig.parameters.keys())



def test_uma::disciplinegrouping_is_not_abstract():
    assert not inspect.isabstract(uma::DisciplineGrouping)


def test_uma::disciplinegrouping_constructor_exists():
    assert callable(uma::DisciplineGrouping.__init__)


def test_uma::disciplinegrouping_constructor_args():
    sig = inspect.signature(uma::DisciplineGrouping.__init__)
    params = list(sig.parameters.keys())



def test_uma::workproducttype_is_not_abstract():
    assert not inspect.isabstract(uma::WorkProductType)


def test_uma::workproducttype_constructor_exists():
    assert callable(uma::WorkProductType.__init__)


def test_uma::workproducttype_constructor_args():
    sig = inspect.signature(uma::WorkProductType.__init__)
    params = list(sig.parameters.keys())



def test_uma::domain_is_not_abstract():
    assert not inspect.isabstract(uma::Domain)


def test_uma::domain_constructor_exists():
    assert callable(uma::Domain.__init__)


def test_uma::domain_constructor_args():
    sig = inspect.signature(uma::Domain.__init__)
    params = list(sig.parameters.keys())



def test_uma::roleset_is_not_abstract():
    assert not inspect.isabstract(uma::RoleSet)


def test_uma::roleset_constructor_exists():
    assert callable(uma::RoleSet.__init__)


def test_uma::roleset_constructor_args():
    sig = inspect.signature(uma::RoleSet.__init__)
    params = list(sig.parameters.keys())



def test_uma::transition_is_not_abstract():
    assert not inspect.isabstract(uma::Transition)


def test_uma::transition_constructor_exists():
    assert callable(uma::Transition.__init__)


def test_uma::transition_constructor_args():
    sig = inspect.signature(uma::Transition.__init__)
    params = list(sig.parameters.keys())



def test_uma::vertex_is_not_abstract():
    assert not inspect.isabstract(uma::Vertex)


def test_uma::vertex_constructor_exists():
    assert callable(uma::Vertex.__init__)


def test_uma::vertex_constructor_args():
    sig = inspect.signature(uma::Vertex.__init__)
    params = list(sig.parameters.keys())



def test_uma::region_is_not_abstract():
    assert not inspect.isabstract(uma::Region)


def test_uma::region_constructor_exists():
    assert callable(uma::Region.__init__)


def test_uma::region_constructor_args():
    sig = inspect.signature(uma::Region.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_uma::pseudostate_is_not_abstract():
    assert not inspect.isabstract(uma::PseudoState)


def test_uma::pseudostate_constructor_exists():
    assert callable(uma::PseudoState.__init__)


def test_uma::pseudostate_constructor_args():
    sig = inspect.signature(uma::PseudoState.__init__)
    params = list(sig.parameters.keys())



def test_uma::state_is_not_abstract():
    assert not inspect.isabstract(uma::State)


def test_uma::state_constructor_exists():
    assert callable(uma::State.__init__)


def test_uma::state_constructor_args():
    sig = inspect.signature(uma::State.__init__)
    params = list(sig.parameters.keys())



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



def test_uma::termdefinition_is_not_abstract():
    assert not inspect.isabstract(uma::TermDefinition)


def test_uma::termdefinition_constructor_exists():
    assert callable(uma::TermDefinition.__init__)


def test_uma::termdefinition_constructor_args():
    sig = inspect.signature(uma::TermDefinition.__init__)
    params = list(sig.parameters.keys())



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
    assert "scope" in params, "Missing parameter 'scope'"
    assert "usageNotes" in params, "Missing parameter 'usageNotes'"
    assert "externalId" in params, "Missing parameter 'externalId'"

def test_uma::processdescription_has_scope():
    assert hasattr(uma::ProcessDescription, "scope")
    descriptor = None
    for klass in uma::ProcessDescription.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_uma::processdescription_has_usageNotes():
    assert hasattr(uma::ProcessDescription, "usageNotes")
    descriptor = None
    for klass in uma::ProcessDescription.__mro__:
        if "usageNotes" in klass.__dict__:
            descriptor = klass.__dict__["usageNotes"]
            break
    assert isinstance(descriptor, property)

def test_uma::processdescription_has_externalId():
    assert hasattr(uma::ProcessDescription, "externalId")
    descriptor = None
    for klass in uma::ProcessDescription.__mro__:
        if "externalId" in klass.__dict__:
            descriptor = klass.__dict__["externalId"]
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
    assert "projectMemberExpertise" in params, "Missing parameter 'projectMemberExpertise'"
    assert "riskLevel" in params, "Missing parameter 'riskLevel'"
    assert "projectCharacteristics" in params, "Missing parameter 'projectCharacteristics'"
    assert "typeOfContract" in params, "Missing parameter 'typeOfContract'"
    assert "estimatingTechnique" in params, "Missing parameter 'estimatingTechnique'"
    assert "scale" in params, "Missing parameter 'scale'"

def test_uma::deliveryprocessdescription_has_projectMemberExpertise():
    assert hasattr(uma::DeliveryProcessDescription, "projectMemberExpertise")
    descriptor = None
    for klass in uma::DeliveryProcessDescription.__mro__:
        if "projectMemberExpertise" in klass.__dict__:
            descriptor = klass.__dict__["projectMemberExpertise"]
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

def test_uma::deliveryprocessdescription_has_typeOfContract():
    assert hasattr(uma::DeliveryProcessDescription, "typeOfContract")
    descriptor = None
    for klass in uma::DeliveryProcessDescription.__mro__:
        if "typeOfContract" in klass.__dict__:
            descriptor = klass.__dict__["typeOfContract"]
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

def test_uma::deliveryprocessdescription_has_scale():
    assert hasattr(uma::DeliveryProcessDescription, "scale")
    descriptor = None
    for klass in uma::DeliveryProcessDescription.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
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



def test_uma::activitydescription_is_not_abstract():
    assert not inspect.isabstract(uma::ActivityDescription)


def test_uma::activitydescription_constructor_exists():
    assert callable(uma::ActivityDescription.__init__)


def test_uma::activitydescription_constructor_args():
    sig = inspect.signature(uma::ActivityDescription.__init__)
    params = list(sig.parameters.keys())
    assert "purpose" in params, "Missing parameter 'purpose'"
    assert "alternatives" in params, "Missing parameter 'alternatives'"
    assert "howtoStaff" in params, "Missing parameter 'howtoStaff'"

def test_uma::activitydescription_has_purpose():
    assert hasattr(uma::ActivityDescription, "purpose")
    descriptor = None
    for klass in uma::ActivityDescription.__mro__:
        if "purpose" in klass.__dict__:
            descriptor = klass.__dict__["purpose"]
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

def test_uma::activitydescription_has_howtoStaff():
    assert hasattr(uma::ActivityDescription, "howtoStaff")
    descriptor = None
    for klass in uma::ActivityDescription.__mro__:
        if "howtoStaff" in klass.__dict__:
            descriptor = klass.__dict__["howtoStaff"]
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



def test_processelement_is_not_abstract():
    assert not inspect.isabstract(ProcessElement)


def test_processelement_constructor_exists():
    assert callable(ProcessElement.__init__)


def test_processelement_constructor_args():
    sig = inspect.signature(ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::workorder_is_not_abstract():
    assert not inspect.isabstract(uma::WorkOrder)


def test_uma::workorder_constructor_exists():
    assert callable(uma::WorkOrder.__init__)


def test_uma::workorder_constructor_args():
    sig = inspect.signature(uma::WorkOrder.__init__)
    params = list(sig.parameters.keys())
    assert "linkType" in params, "Missing parameter 'linkType'"

def test_uma::workorder_has_linkType():
    assert hasattr(uma::WorkOrder, "linkType")
    descriptor = None
    for klass in uma::WorkOrder.__mro__:
        if "linkType" in klass.__dict__:
            descriptor = klass.__dict__["linkType"]
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
    assert "activityEntryState" in params, "Missing parameter 'activityEntryState'"
    assert "activityExitState" in params, "Missing parameter 'activityExitState'"

def test_uma::workproductdescriptor_has_activityEntryState():
    assert hasattr(uma::WorkProductDescriptor, "activityEntryState")
    descriptor = None
    for klass in uma::WorkProductDescriptor.__mro__:
        if "activityEntryState" in klass.__dict__:
            descriptor = klass.__dict__["activityEntryState"]
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



def test_uma::processcomponentdescriptor_is_not_abstract():
    assert not inspect.isabstract(uma::ProcessComponentDescriptor)


def test_uma::processcomponentdescriptor_constructor_exists():
    assert callable(uma::ProcessComponentDescriptor.__init__)


def test_uma::processcomponentdescriptor_constructor_args():
    sig = inspect.signature(uma::ProcessComponentDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_uma::roledescriptor_is_not_abstract():
    assert not inspect.isabstract(uma::RoleDescriptor)


def test_uma::roledescriptor_constructor_exists():
    assert callable(uma::RoleDescriptor.__init__)


def test_uma::roledescriptor_constructor_args():
    sig = inspect.signature(uma::RoleDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_activity_is_not_abstract():
    assert not inspect.isabstract(Activity)


def test_activity_constructor_exists():
    assert callable(Activity.__init__)


def test_activity_constructor_args():
    sig = inspect.signature(Activity.__init__)
    params = list(sig.parameters.keys())



def test_uma::process_is_not_abstract():
    assert not inspect.isabstract(uma::Process)


def test_uma::process_constructor_exists():
    assert callable(uma::Process.__init__)


def test_uma::process_constructor_args():
    sig = inspect.signature(uma::Process.__init__)
    params = list(sig.parameters.keys())



def test_uma::phase_is_not_abstract():
    assert not inspect.isabstract(uma::Phase)


def test_uma::phase_constructor_exists():
    assert callable(uma::Phase.__init__)


def test_uma::phase_constructor_args():
    sig = inspect.signature(uma::Phase.__init__)
    params = list(sig.parameters.keys())



def test_uma::iteration_is_not_abstract():
    assert not inspect.isabstract(uma::Iteration)


def test_uma::iteration_constructor_exists():
    assert callable(uma::Iteration.__init__)


def test_uma::iteration_constructor_args():
    sig = inspect.signature(uma::Iteration.__init__)
    params = list(sig.parameters.keys())



def test_uma::planningdata_is_not_abstract():
    assert not inspect.isabstract(uma::PlanningData)


def test_uma::planningdata_constructor_exists():
    assert callable(uma::PlanningData.__init__)


def test_uma::planningdata_constructor_args():
    sig = inspect.signature(uma::PlanningData.__init__)
    params = list(sig.parameters.keys())
    assert "rank" in params, "Missing parameter 'rank'"
    assert "finishDate" in params, "Missing parameter 'finishDate'"
    assert "startDate" in params, "Missing parameter 'startDate'"

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

def test_uma::planningdata_has_startDate():
    assert hasattr(uma::PlanningData, "startDate")
    descriptor = None
    for klass in uma::PlanningData.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)



def test_breakdownelement_is_not_abstract():
    assert not inspect.isabstract(BreakdownElement)


def test_breakdownelement_constructor_exists():
    assert callable(BreakdownElement.__init__)


def test_breakdownelement_constructor_args():
    sig = inspect.signature(BreakdownElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::teamprofile_is_not_abstract():
    assert not inspect.isabstract(uma::TeamProfile)


def test_uma::teamprofile_constructor_exists():
    assert callable(uma::TeamProfile.__init__)


def test_uma::teamprofile_constructor_args():
    sig = inspect.signature(uma::TeamProfile.__init__)
    params = list(sig.parameters.keys())



def test_uma::processcomponentinterface_is_not_abstract():
    assert not inspect.isabstract(uma::ProcessComponentInterface)


def test_uma::processcomponentinterface_constructor_exists():
    assert callable(uma::ProcessComponentInterface.__init__)


def test_uma::processcomponentinterface_constructor_args():
    sig = inspect.signature(uma::ProcessComponentInterface.__init__)
    params = list(sig.parameters.keys())



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



def test_uma::workbreakdownelement_is_not_abstract():
    assert not inspect.isabstract(uma::WorkBreakdownElement)


def test_uma::workbreakdownelement_constructor_exists():
    assert callable(uma::WorkBreakdownElement.__init__)


def test_uma::workbreakdownelement_constructor_args():
    sig = inspect.signature(uma::WorkBreakdownElement.__init__)
    params = list(sig.parameters.keys())
    assert "isEventDriven" in params, "Missing parameter 'isEventDriven'"
    assert "isRepeatable" in params, "Missing parameter 'isRepeatable'"
    assert "isOngoing" in params, "Missing parameter 'isOngoing'"

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



def test_uma::roadmap_is_not_abstract():
    assert not inspect.isabstract(uma::Roadmap)


def test_uma::roadmap_constructor_exists():
    assert callable(uma::Roadmap.__init__)


def test_uma::roadmap_constructor_args():
    sig = inspect.signature(uma::Roadmap.__init__)
    params = list(sig.parameters.keys())



def test_uma::breakdownelement_is_not_abstract():
    assert not inspect.isabstract(uma::BreakdownElement)


def test_uma::breakdownelement_constructor_exists():
    assert callable(uma::BreakdownElement.__init__)


def test_uma::breakdownelement_constructor_args():
    sig = inspect.signature(uma::BreakdownElement.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"
    assert "isOptional" in params, "Missing parameter 'isOptional'"
    assert "isPlanned" in params, "Missing parameter 'isPlanned'"
    assert "hasMultipleOccurrences" in params, "Missing parameter 'hasMultipleOccurrences'"

def test_uma::breakdownelement_has_prefix():
    assert hasattr(uma::BreakdownElement, "prefix")
    descriptor = None
    for klass in uma::BreakdownElement.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
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

def test_uma::breakdownelement_has_isPlanned():
    assert hasattr(uma::BreakdownElement, "isPlanned")
    descriptor = None
    for klass in uma::BreakdownElement.__mro__:
        if "isPlanned" in klass.__dict__:
            descriptor = klass.__dict__["isPlanned"]
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



def test_uma::milestone_is_not_abstract():
    assert not inspect.isabstract(uma::Milestone)


def test_uma::milestone_constructor_exists():
    assert callable(uma::Milestone.__init__)


def test_uma::milestone_constructor_args():
    sig = inspect.signature(uma::Milestone.__init__)
    params = list(sig.parameters.keys())



def test_uma::dimension_is_not_abstract():
    assert not inspect.isabstract(uma::Dimension)


def test_uma::dimension_constructor_exists():
    assert callable(uma::Dimension.__init__)


def test_uma::dimension_constructor_args():
    sig = inspect.signature(uma::Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_uma::dimension_has_width():
    assert hasattr(uma::Dimension, "width")
    descriptor = None
    for klass in uma::Dimension.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_uma::dimension_has_height():
    assert hasattr(uma::Dimension, "height")
    descriptor = None
    for klass in uma::Dimension.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_graphicprimitive_is_not_abstract():
    assert not inspect.isabstract(GraphicPrimitive)


def test_graphicprimitive_constructor_exists():
    assert callable(GraphicPrimitive.__init__)


def test_graphicprimitive_constructor_args():
    sig = inspect.signature(GraphicPrimitive.__init__)
    params = list(sig.parameters.keys())



def test_uma::ellipse_is_not_abstract():
    assert not inspect.isabstract(uma::Ellipse)


def test_uma::ellipse_constructor_exists():
    assert callable(uma::Ellipse.__init__)


def test_uma::ellipse_constructor_args():
    sig = inspect.signature(uma::Ellipse.__init__)
    params = list(sig.parameters.keys())
    assert "endAngle" in params, "Missing parameter 'endAngle'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "radiusX" in params, "Missing parameter 'radiusX'"
    assert "radiusY" in params, "Missing parameter 'radiusY'"
    assert "startAngle" in params, "Missing parameter 'startAngle'"

def test_uma::ellipse_has_endAngle():
    assert hasattr(uma::Ellipse, "endAngle")
    descriptor = None
    for klass in uma::Ellipse.__mro__:
        if "endAngle" in klass.__dict__:
            descriptor = klass.__dict__["endAngle"]
            break
    assert isinstance(descriptor, property)

def test_uma::ellipse_has_rotation():
    assert hasattr(uma::Ellipse, "rotation")
    descriptor = None
    for klass in uma::Ellipse.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_uma::ellipse_has_radiusX():
    assert hasattr(uma::Ellipse, "radiusX")
    descriptor = None
    for klass in uma::Ellipse.__mro__:
        if "radiusX" in klass.__dict__:
            descriptor = klass.__dict__["radiusX"]
            break
    assert isinstance(descriptor, property)

def test_uma::ellipse_has_radiusY():
    assert hasattr(uma::Ellipse, "radiusY")
    descriptor = None
    for klass in uma::Ellipse.__mro__:
        if "radiusY" in klass.__dict__:
            descriptor = klass.__dict__["radiusY"]
            break
    assert isinstance(descriptor, property)

def test_uma::ellipse_has_startAngle():
    assert hasattr(uma::Ellipse, "startAngle")
    descriptor = None
    for klass in uma::Ellipse.__mro__:
        if "startAngle" in klass.__dict__:
            descriptor = klass.__dict__["startAngle"]
            break
    assert isinstance(descriptor, property)



def test_uma::polyline_is_not_abstract():
    assert not inspect.isabstract(uma::Polyline)


def test_uma::polyline_constructor_exists():
    assert callable(uma::Polyline.__init__)


def test_uma::polyline_constructor_args():
    sig = inspect.signature(uma::Polyline.__init__)
    params = list(sig.parameters.keys())
    assert "closed" in params, "Missing parameter 'closed'"

def test_uma::polyline_has_closed():
    assert hasattr(uma::Polyline, "closed")
    descriptor = None
    for klass in uma::Polyline.__mro__:
        if "closed" in klass.__dict__:
            descriptor = klass.__dict__["closed"]
            break
    assert isinstance(descriptor, property)



def test_leafelement_is_not_abstract():
    assert not inspect.isabstract(LeafElement)


def test_leafelement_constructor_exists():
    assert callable(LeafElement.__init__)


def test_leafelement_constructor_args():
    sig = inspect.signature(LeafElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::graphicprimitive_is_not_abstract():
    assert not inspect.isabstract(uma::GraphicPrimitive)


def test_uma::graphicprimitive_constructor_exists():
    assert callable(uma::GraphicPrimitive.__init__)


def test_uma::graphicprimitive_constructor_args():
    sig = inspect.signature(uma::GraphicPrimitive.__init__)
    params = list(sig.parameters.keys())



def test_uma::image_is_not_abstract():
    assert not inspect.isabstract(uma::Image)


def test_uma::image_constructor_exists():
    assert callable(uma::Image.__init__)


def test_uma::image_constructor_args():
    sig = inspect.signature(uma::Image.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"
    assert "mimeType" in params, "Missing parameter 'mimeType'"

def test_uma::image_has_uri():
    assert hasattr(uma::Image, "uri")
    descriptor = None
    for klass in uma::Image.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)

def test_uma::image_has_mimeType():
    assert hasattr(uma::Image, "mimeType")
    descriptor = None
    for klass in uma::Image.__mro__:
        if "mimeType" in klass.__dict__:
            descriptor = klass.__dict__["mimeType"]
            break
    assert isinstance(descriptor, property)



def test_uma::textelement_is_not_abstract():
    assert not inspect.isabstract(uma::TextElement)


def test_uma::textelement_constructor_exists():
    assert callable(uma::TextElement.__init__)


def test_uma::textelement_constructor_args():
    sig = inspect.signature(uma::TextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_uma::textelement_has_text():
    assert hasattr(uma::TextElement, "text")
    descriptor = None
    for klass in uma::TextElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_semanticmodelbridge_is_not_abstract():
    assert not inspect.isabstract(SemanticModelBridge)


def test_semanticmodelbridge_constructor_exists():
    assert callable(SemanticModelBridge.__init__)


def test_semanticmodelbridge_constructor_args():
    sig = inspect.signature(SemanticModelBridge.__init__)
    params = list(sig.parameters.keys())



def test_uma::umasemanticmodelbridge_is_not_abstract():
    assert not inspect.isabstract(uma::UMASemanticModelBridge)


def test_uma::umasemanticmodelbridge_constructor_exists():
    assert callable(uma::UMASemanticModelBridge.__init__)


def test_uma::umasemanticmodelbridge_constructor_args():
    sig = inspect.signature(uma::UMASemanticModelBridge.__init__)
    params = list(sig.parameters.keys())



def test_uma::coresemanticmodelbridge_is_not_abstract():
    assert not inspect.isabstract(uma::CoreSemanticModelBridge)


def test_uma::coresemanticmodelbridge_constructor_exists():
    assert callable(uma::CoreSemanticModelBridge.__init__)


def test_uma::coresemanticmodelbridge_constructor_args():
    sig = inspect.signature(uma::CoreSemanticModelBridge.__init__)
    params = list(sig.parameters.keys())



def test_uma::simplesemanticmodelelement_is_not_abstract():
    assert not inspect.isabstract(uma::SimpleSemanticModelElement)


def test_uma::simplesemanticmodelelement_constructor_exists():
    assert callable(uma::SimpleSemanticModelElement.__init__)


def test_uma::simplesemanticmodelelement_constructor_args():
    sig = inspect.signature(uma::SimpleSemanticModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "typeInfo" in params, "Missing parameter 'typeInfo'"

def test_uma::simplesemanticmodelelement_has_typeInfo():
    assert hasattr(uma::SimpleSemanticModelElement, "typeInfo")
    descriptor = None
    for klass in uma::SimpleSemanticModelElement.__mro__:
        if "typeInfo" in klass.__dict__:
            descriptor = klass.__dict__["typeInfo"]
            break
    assert isinstance(descriptor, property)



def test_graphnode_is_not_abstract():
    assert not inspect.isabstract(GraphNode)


def test_graphnode_constructor_exists():
    assert callable(GraphNode.__init__)


def test_graphnode_constructor_args():
    sig = inspect.signature(GraphNode.__init__)
    params = list(sig.parameters.keys())



def test_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::leafelement_is_not_abstract():
    assert not inspect.isabstract(uma::LeafElement)


def test_uma::leafelement_constructor_exists():
    assert callable(uma::LeafElement.__init__)


def test_uma::leafelement_constructor_args():
    sig = inspect.signature(uma::LeafElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::graphelement_is_not_abstract():
    assert not inspect.isabstract(uma::GraphElement)


def test_uma::graphelement_constructor_exists():
    assert callable(uma::GraphElement.__init__)


def test_uma::graphelement_constructor_args():
    sig = inspect.signature(uma::GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_graphelement_is_not_abstract():
    assert not inspect.isabstract(GraphElement)


def test_graphelement_constructor_exists():
    assert callable(GraphElement.__init__)


def test_graphelement_constructor_args():
    sig = inspect.signature(GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::graphedge_is_not_abstract():
    assert not inspect.isabstract(uma::GraphEdge)


def test_uma::graphedge_constructor_exists():
    assert callable(uma::GraphEdge.__init__)


def test_uma::graphedge_constructor_args():
    sig = inspect.signature(uma::GraphEdge.__init__)
    params = list(sig.parameters.keys())



def test_uma::graphnode_is_not_abstract():
    assert not inspect.isabstract(uma::GraphNode)


def test_uma::graphnode_constructor_exists():
    assert callable(uma::GraphNode.__init__)


def test_uma::graphnode_constructor_args():
    sig = inspect.signature(uma::GraphNode.__init__)
    params = list(sig.parameters.keys())



def test_uma::diagram_is_not_abstract():
    assert not inspect.isabstract(uma::Diagram)


def test_uma::diagram_constructor_exists():
    assert callable(uma::Diagram.__init__)


def test_uma::diagram_constructor_args():
    sig = inspect.signature(uma::Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "zoom" in params, "Missing parameter 'zoom'"

def test_uma::diagram_has_zoom():
    assert hasattr(uma::Diagram, "zoom")
    descriptor = None
    for klass in uma::Diagram.__mro__:
        if "zoom" in klass.__dict__:
            descriptor = klass.__dict__["zoom"]
            break
    assert isinstance(descriptor, property)



def test_uma::property_is_not_abstract():
    assert not inspect.isabstract(uma::Property)


def test_uma::property_constructor_exists():
    assert callable(uma::Property.__init__)


def test_uma::property_constructor_args():
    sig = inspect.signature(uma::Property.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_uma::property_has_value():
    assert hasattr(uma::Property, "value")
    descriptor = None
    for klass in uma::Property.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_uma::property_has_key():
    assert hasattr(uma::Property, "key")
    descriptor = None
    for klass in uma::Property.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_uma::reference_is_not_abstract():
    assert not inspect.isabstract(uma::Reference)


def test_uma::reference_constructor_exists():
    assert callable(uma::Reference.__init__)


def test_uma::reference_constructor_args():
    sig = inspect.signature(uma::Reference.__init__)
    params = list(sig.parameters.keys())
    assert "isIndividualRepresentation" in params, "Missing parameter 'isIndividualRepresentation'"

def test_uma::reference_has_isIndividualRepresentation():
    assert hasattr(uma::Reference, "isIndividualRepresentation")
    descriptor = None
    for klass in uma::Reference.__mro__:
        if "isIndividualRepresentation" in klass.__dict__:
            descriptor = klass.__dict__["isIndividualRepresentation"]
            break
    assert isinstance(descriptor, property)



def test_uma::semanticmodelbridge_is_not_abstract():
    assert not inspect.isabstract(uma::SemanticModelBridge)


def test_uma::semanticmodelbridge_constructor_exists():
    assert callable(uma::SemanticModelBridge.__init__)


def test_uma::semanticmodelbridge_constructor_args():
    sig = inspect.signature(uma::SemanticModelBridge.__init__)
    params = list(sig.parameters.keys())
    assert "presentation" in params, "Missing parameter 'presentation'"

def test_uma::semanticmodelbridge_has_presentation():
    assert hasattr(uma::SemanticModelBridge, "presentation")
    descriptor = None
    for klass in uma::SemanticModelBridge.__mro__:
        if "presentation" in klass.__dict__:
            descriptor = klass.__dict__["presentation"]
            break
    assert isinstance(descriptor, property)



def test_uma::graphconnector_is_not_abstract():
    assert not inspect.isabstract(uma::GraphConnector)


def test_uma::graphconnector_constructor_exists():
    assert callable(uma::GraphConnector.__init__)


def test_uma::graphconnector_constructor_args():
    sig = inspect.signature(uma::GraphConnector.__init__)
    params = list(sig.parameters.keys())



def test_uma::diagramlink_is_not_abstract():
    assert not inspect.isabstract(uma::DiagramLink)


def test_uma::diagramlink_constructor_exists():
    assert callable(uma::DiagramLink.__init__)


def test_uma::diagramlink_constructor_args():
    sig = inspect.signature(uma::DiagramLink.__init__)
    params = list(sig.parameters.keys())
    assert "zoom" in params, "Missing parameter 'zoom'"

def test_uma::diagramlink_has_zoom():
    assert hasattr(uma::DiagramLink, "zoom")
    descriptor = None
    for klass in uma::DiagramLink.__mro__:
        if "zoom" in klass.__dict__:
            descriptor = klass.__dict__["zoom"]
            break
    assert isinstance(descriptor, property)



def test_contentdescription_is_not_abstract():
    assert not inspect.isabstract(ContentDescription)


def test_contentdescription_constructor_exists():
    assert callable(ContentDescription.__init__)


def test_contentdescription_constructor_args():
    sig = inspect.signature(ContentDescription.__init__)
    params = list(sig.parameters.keys())



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



def test_uma::workproductdescription_is_not_abstract():
    assert not inspect.isabstract(uma::WorkProductDescription)


def test_uma::workproductdescription_constructor_exists():
    assert callable(uma::WorkProductDescription.__init__)


def test_uma::workproductdescription_constructor_args():
    sig = inspect.signature(uma::WorkProductDescription.__init__)
    params = list(sig.parameters.keys())
    assert "impactOfNotHaving" in params, "Missing parameter 'impactOfNotHaving'"
    assert "reasonsForNotNeeding" in params, "Missing parameter 'reasonsForNotNeeding'"
    assert "externalId" in params, "Missing parameter 'externalId'"
    assert "purpose" in params, "Missing parameter 'purpose'"

def test_uma::workproductdescription_has_impactOfNotHaving():
    assert hasattr(uma::WorkProductDescription, "impactOfNotHaving")
    descriptor = None
    for klass in uma::WorkProductDescription.__mro__:
        if "impactOfNotHaving" in klass.__dict__:
            descriptor = klass.__dict__["impactOfNotHaving"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproductdescription_has_reasonsForNotNeeding():
    assert hasattr(uma::WorkProductDescription, "reasonsForNotNeeding")
    descriptor = None
    for klass in uma::WorkProductDescription.__mro__:
        if "reasonsForNotNeeding" in klass.__dict__:
            descriptor = klass.__dict__["reasonsForNotNeeding"]
            break
    assert isinstance(descriptor, property)

def test_uma::workproductdescription_has_externalId():
    assert hasattr(uma::WorkProductDescription, "externalId")
    descriptor = None
    for klass in uma::WorkProductDescription.__mro__:
        if "externalId" in klass.__dict__:
            descriptor = klass.__dict__["externalId"]
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



def test_workproductdescription_is_not_abstract():
    assert not inspect.isabstract(WorkProductDescription)


def test_workproductdescription_constructor_exists():
    assert callable(WorkProductDescription.__init__)


def test_workproductdescription_constructor_args():
    sig = inspect.signature(WorkProductDescription.__init__)
    params = list(sig.parameters.keys())



def test_uma::artifactdescription_is_not_abstract():
    assert not inspect.isabstract(uma::ArtifactDescription)


def test_uma::artifactdescription_constructor_exists():
    assert callable(uma::ArtifactDescription.__init__)


def test_uma::artifactdescription_constructor_args():
    sig = inspect.signature(uma::ArtifactDescription.__init__)
    params = list(sig.parameters.keys())
    assert "briefOutline" in params, "Missing parameter 'briefOutline'"
    assert "representationOptions" in params, "Missing parameter 'representationOptions'"

def test_uma::artifactdescription_has_briefOutline():
    assert hasattr(uma::ArtifactDescription, "briefOutline")
    descriptor = None
    for klass in uma::ArtifactDescription.__mro__:
        if "briefOutline" in klass.__dict__:
            descriptor = klass.__dict__["briefOutline"]
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



def test_uma::point_is_not_abstract():
    assert not inspect.isabstract(uma::Point)


def test_uma::point_constructor_exists():
    assert callable(uma::Point.__init__)


def test_uma::point_constructor_args():
    sig = inspect.signature(uma::Point.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_uma::point_has_x():
    assert hasattr(uma::Point, "x")
    descriptor = None
    for klass in uma::Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_uma::point_has_y():
    assert hasattr(uma::Point, "y")
    descriptor = None
    for klass in uma::Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_uma::practicedescription_is_not_abstract():
    assert not inspect.isabstract(uma::PracticeDescription)


def test_uma::practicedescription_constructor_exists():
    assert callable(uma::PracticeDescription.__init__)


def test_uma::practicedescription_constructor_args():
    sig = inspect.signature(uma::PracticeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "levelsOfAdoption" in params, "Missing parameter 'levelsOfAdoption'"
    assert "additionalInfo" in params, "Missing parameter 'additionalInfo'"
    assert "goals" in params, "Missing parameter 'goals'"
    assert "background" in params, "Missing parameter 'background'"
    assert "problem" in params, "Missing parameter 'problem'"
    assert "application" in params, "Missing parameter 'application'"

def test_uma::practicedescription_has_levelsOfAdoption():
    assert hasattr(uma::PracticeDescription, "levelsOfAdoption")
    descriptor = None
    for klass in uma::PracticeDescription.__mro__:
        if "levelsOfAdoption" in klass.__dict__:
            descriptor = klass.__dict__["levelsOfAdoption"]
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

def test_uma::practicedescription_has_problem():
    assert hasattr(uma::PracticeDescription, "problem")
    descriptor = None
    for klass in uma::PracticeDescription.__mro__:
        if "problem" in klass.__dict__:
            descriptor = klass.__dict__["problem"]
            break
    assert isinstance(descriptor, property)

def test_uma::practicedescription_has_application():
    assert hasattr(uma::PracticeDescription, "application")
    descriptor = None
    for klass in uma::PracticeDescription.__mro__:
        if "application" in klass.__dict__:
            descriptor = klass.__dict__["application"]
            break
    assert isinstance(descriptor, property)



def test_uma::guidancedescription_is_not_abstract():
    assert not inspect.isabstract(uma::GuidanceDescription)


def test_uma::guidancedescription_constructor_exists():
    assert callable(uma::GuidanceDescription.__init__)


def test_uma::guidancedescription_constructor_args():
    sig = inspect.signature(uma::GuidanceDescription.__init__)
    params = list(sig.parameters.keys())
    assert "attachments" in params, "Missing parameter 'attachments'"

def test_uma::guidancedescription_has_attachments():
    assert hasattr(uma::GuidanceDescription, "attachments")
    descriptor = None
    for klass in uma::GuidanceDescription.__mro__:
        if "attachments" in klass.__dict__:
            descriptor = klass.__dict__["attachments"]
            break
    assert isinstance(descriptor, property)



def test_uma::taskdescription_is_not_abstract():
    assert not inspect.isabstract(uma::TaskDescription)


def test_uma::taskdescription_constructor_exists():
    assert callable(uma::TaskDescription.__init__)


def test_uma::taskdescription_constructor_args():
    sig = inspect.signature(uma::TaskDescription.__init__)
    params = list(sig.parameters.keys())
    assert "alternatives" in params, "Missing parameter 'alternatives'"
    assert "purpose" in params, "Missing parameter 'purpose'"

def test_uma::taskdescription_has_alternatives():
    assert hasattr(uma::TaskDescription, "alternatives")
    descriptor = None
    for klass in uma::TaskDescription.__mro__:
        if "alternatives" in klass.__dict__:
            descriptor = klass.__dict__["alternatives"]
            break
    assert isinstance(descriptor, property)

def test_uma::taskdescription_has_purpose():
    assert hasattr(uma::TaskDescription, "purpose")
    descriptor = None
    for klass in uma::TaskDescription.__mro__:
        if "purpose" in klass.__dict__:
            descriptor = klass.__dict__["purpose"]
            break
    assert isinstance(descriptor, property)



def test_uma::roledescription_is_not_abstract():
    assert not inspect.isabstract(uma::RoleDescription)


def test_uma::roledescription_constructor_exists():
    assert callable(uma::RoleDescription.__init__)


def test_uma::roledescription_constructor_args():
    sig = inspect.signature(uma::RoleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "synonyms" in params, "Missing parameter 'synonyms'"
    assert "assignmentApproaches" in params, "Missing parameter 'assignmentApproaches'"
    assert "skills" in params, "Missing parameter 'skills'"

def test_uma::roledescription_has_synonyms():
    assert hasattr(uma::RoleDescription, "synonyms")
    descriptor = None
    for klass in uma::RoleDescription.__mro__:
        if "synonyms" in klass.__dict__:
            descriptor = klass.__dict__["synonyms"]
            break
    assert isinstance(descriptor, property)

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



def test_methodpackage_is_not_abstract():
    assert not inspect.isabstract(MethodPackage)


def test_methodpackage_constructor_exists():
    assert callable(MethodPackage.__init__)


def test_methodpackage_constructor_args():
    sig = inspect.signature(MethodPackage.__init__)
    params = list(sig.parameters.keys())



def test_uma::processpackage_is_not_abstract():
    assert not inspect.isabstract(uma::ProcessPackage)


def test_uma::processpackage_constructor_exists():
    assert callable(uma::ProcessPackage.__init__)


def test_uma::processpackage_constructor_args():
    sig = inspect.signature(uma::ProcessPackage.__init__)
    params = list(sig.parameters.keys())



def test_uma::contentpackage_is_not_abstract():
    assert not inspect.isabstract(uma::ContentPackage)


def test_uma::contentpackage_constructor_exists():
    assert callable(uma::ContentPackage.__init__)


def test_uma::contentpackage_constructor_args():
    sig = inspect.signature(uma::ContentPackage.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



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



def test_uma::artifact_is_not_abstract():
    assert not inspect.isabstract(uma::Artifact)


def test_uma::artifact_constructor_exists():
    assert callable(uma::Artifact.__init__)


def test_uma::artifact_constructor_args():
    sig = inspect.signature(uma::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_section_constructor_exists():
    assert callable(Section.__init__)


def test_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



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



def test_uma::methodlibrary_is_not_abstract():
    assert not inspect.isabstract(uma::MethodLibrary)


def test_uma::methodlibrary_constructor_exists():
    assert callable(uma::MethodLibrary.__init__)


def test_uma::methodlibrary_constructor_args():
    sig = inspect.signature(uma::MethodLibrary.__init__)
    params = list(sig.parameters.keys())



def test_uma::processcomponent_is_not_abstract():
    assert not inspect.isabstract(uma::ProcessComponent)


def test_uma::processcomponent_constructor_exists():
    assert callable(uma::ProcessComponent.__init__)


def test_uma::processcomponent_constructor_args():
    sig = inspect.signature(uma::ProcessComponent.__init__)
    params = list(sig.parameters.keys())



def test_uma::methodplugin_is_not_abstract():
    assert not inspect.isabstract(uma::MethodPlugin)


def test_uma::methodplugin_constructor_exists():
    assert callable(uma::MethodPlugin.__init__)


def test_uma::methodplugin_constructor_args():
    sig = inspect.signature(uma::MethodPlugin.__init__)
    params = list(sig.parameters.keys())
    assert "userChangeable" in params, "Missing parameter 'userChangeable'"

def test_uma::methodplugin_has_userChangeable():
    assert hasattr(uma::MethodPlugin, "userChangeable")
    descriptor = None
    for klass in uma::MethodPlugin.__mro__:
        if "userChangeable" in klass.__dict__:
            descriptor = klass.__dict__["userChangeable"]
            break
    assert isinstance(descriptor, property)



def test_workdefinition_is_not_abstract():
    assert not inspect.isabstract(WorkDefinition)


def test_workdefinition_constructor_exists():
    assert callable(WorkDefinition.__init__)


def test_workdefinition_constructor_args():
    sig = inspect.signature(WorkDefinition.__init__)
    params = list(sig.parameters.keys())



def test_uma::statemachine_is_not_abstract():
    assert not inspect.isabstract(uma::StateMachine)


def test_uma::statemachine_constructor_exists():
    assert callable(uma::StateMachine.__init__)


def test_uma::statemachine_constructor_args():
    sig = inspect.signature(uma::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uma::step_is_not_abstract():
    assert not inspect.isabstract(uma::Step)


def test_uma::step_constructor_exists():
    assert callable(uma::Step.__init__)


def test_uma::step_constructor_args():
    sig = inspect.signature(uma::Step.__init__)
    params = list(sig.parameters.keys())



def test_uma::estimationconsiderations_is_not_abstract():
    assert not inspect.isabstract(uma::EstimationConsiderations)


def test_uma::estimationconsiderations_constructor_exists():
    assert callable(uma::EstimationConsiderations.__init__)


def test_uma::estimationconsiderations_constructor_args():
    sig = inspect.signature(uma::EstimationConsiderations.__init__)
    params = list(sig.parameters.keys())



def test_uma::toolmentor_is_not_abstract():
    assert not inspect.isabstract(uma::ToolMentor)


def test_uma::toolmentor_constructor_exists():
    assert callable(uma::ToolMentor.__init__)


def test_uma::toolmentor_constructor_args():
    sig = inspect.signature(uma::ToolMentor.__init__)
    params = list(sig.parameters.keys())



def test_uma::template_is_not_abstract():
    assert not inspect.isabstract(uma::Template)


def test_uma::template_constructor_exists():
    assert callable(uma::Template.__init__)


def test_uma::template_constructor_args():
    sig = inspect.signature(uma::Template.__init__)
    params = list(sig.parameters.keys())



def test_uma::report_is_not_abstract():
    assert not inspect.isabstract(uma::Report)


def test_uma::report_constructor_exists():
    assert callable(uma::Report.__init__)


def test_uma::report_constructor_args():
    sig = inspect.signature(uma::Report.__init__)
    params = list(sig.parameters.keys())



def test_contentelement_is_not_abstract():
    assert not inspect.isabstract(ContentElement)


def test_contentelement_constructor_exists():
    assert callable(ContentElement.__init__)


def test_contentelement_constructor_args():
    sig = inspect.signature(ContentElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::contentcategory_is_not_abstract():
    assert not inspect.isabstract(uma::ContentCategory)


def test_uma::contentcategory_constructor_exists():
    assert callable(uma::ContentCategory.__init__)


def test_uma::contentcategory_constructor_args():
    sig = inspect.signature(uma::ContentCategory.__init__)
    params = list(sig.parameters.keys())



def test_uma::task_is_not_abstract():
    assert not inspect.isabstract(uma::Task)


def test_uma::task_constructor_exists():
    assert callable(uma::Task.__init__)


def test_uma::task_constructor_args():
    sig = inspect.signature(uma::Task.__init__)
    params = list(sig.parameters.keys())



def test_uma::guidance_is_not_abstract():
    assert not inspect.isabstract(uma::Guidance)


def test_uma::guidance_constructor_exists():
    assert callable(uma::Guidance.__init__)


def test_uma::guidance_constructor_args():
    sig = inspect.signature(uma::Guidance.__init__)
    params = list(sig.parameters.keys())



def test_uma::workproduct_is_not_abstract():
    assert not inspect.isabstract(uma::WorkProduct)


def test_uma::workproduct_constructor_exists():
    assert callable(uma::WorkProduct.__init__)


def test_uma::workproduct_constructor_args():
    sig = inspect.signature(uma::WorkProduct.__init__)
    params = list(sig.parameters.keys())



def test_uma::role_is_not_abstract():
    assert not inspect.isabstract(uma::Role)


def test_uma::role_constructor_exists():
    assert callable(uma::Role.__init__)


def test_uma::role_constructor_args():
    sig = inspect.signature(uma::Role.__init__)
    params = list(sig.parameters.keys())



def test_uma::contentdescription_is_not_abstract():
    assert not inspect.isabstract(uma::ContentDescription)


def test_uma::contentdescription_constructor_exists():
    assert callable(uma::ContentDescription.__init__)


def test_uma::contentdescription_constructor_args():
    sig = inspect.signature(uma::ContentDescription.__init__)
    params = list(sig.parameters.keys())
    assert "mainDescription" in params, "Missing parameter 'mainDescription'"
    assert "keyConsiderations" in params, "Missing parameter 'keyConsiderations'"

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



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uma::reusableasset_is_not_abstract():
    assert not inspect.isabstract(uma::ReusableAsset)


def test_uma::reusableasset_constructor_exists():
    assert callable(uma::ReusableAsset.__init__)


def test_uma::reusableasset_constructor_args():
    sig = inspect.signature(uma::ReusableAsset.__init__)
    params = list(sig.parameters.keys())



def test_uma::example_is_not_abstract():
    assert not inspect.isabstract(uma::Example)


def test_uma::example_constructor_exists():
    assert callable(uma::Example.__init__)


def test_uma::example_constructor_args():
    sig = inspect.signature(uma::Example.__init__)
    params = list(sig.parameters.keys())



def test_uma::guideline_is_not_abstract():
    assert not inspect.isabstract(uma::Guideline)


def test_uma::guideline_constructor_exists():
    assert callable(uma::Guideline.__init__)


def test_uma::guideline_constructor_args():
    sig = inspect.signature(uma::Guideline.__init__)
    params = list(sig.parameters.keys())



def test_uma::checklist_is_not_abstract():
    assert not inspect.isabstract(uma::Checklist)


def test_uma::checklist_constructor_exists():
    assert callable(uma::Checklist.__init__)


def test_uma::checklist_constructor_args():
    sig = inspect.signature(uma::Checklist.__init__)
    params = list(sig.parameters.keys())



def test_uma::concept_is_not_abstract():
    assert not inspect.isabstract(uma::Concept)


def test_uma::concept_constructor_exists():
    assert callable(uma::Concept.__init__)


def test_uma::concept_constructor_args():
    sig = inspect.signature(uma::Concept.__init__)
    params = list(sig.parameters.keys())



def test_uma::supportingmaterial_is_not_abstract():
    assert not inspect.isabstract(uma::SupportingMaterial)


def test_uma::supportingmaterial_constructor_exists():
    assert callable(uma::SupportingMaterial.__init__)


def test_uma::supportingmaterial_constructor_args():
    sig = inspect.signature(uma::SupportingMaterial.__init__)
    params = list(sig.parameters.keys())



def test_variabilityelement_is_not_abstract():
    assert not inspect.isabstract(VariabilityElement)


def test_variabilityelement_constructor_exists():
    assert callable(VariabilityElement.__init__)


def test_variabilityelement_constructor_args():
    sig = inspect.signature(VariabilityElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::section_is_not_abstract():
    assert not inspect.isabstract(uma::Section)


def test_uma::section_constructor_exists():
    assert callable(uma::Section.__init__)


def test_uma::section_constructor_args():
    sig = inspect.signature(uma::Section.__init__)
    params = list(sig.parameters.keys())
    assert "sectionDescription" in params, "Missing parameter 'sectionDescription'"
    assert "sectionName" in params, "Missing parameter 'sectionName'"

def test_uma::section_has_sectionDescription():
    assert hasattr(uma::Section, "sectionDescription")
    descriptor = None
    for klass in uma::Section.__mro__:
        if "sectionDescription" in klass.__dict__:
            descriptor = klass.__dict__["sectionDescription"]
            break
    assert isinstance(descriptor, property)

def test_uma::section_has_sectionName():
    assert hasattr(uma::Section, "sectionName")
    descriptor = None
    for klass in uma::Section.__mro__:
        if "sectionName" in klass.__dict__:
            descriptor = klass.__dict__["sectionName"]
            break
    assert isinstance(descriptor, property)



def test_uma::activity_is_not_abstract():
    assert not inspect.isabstract(uma::Activity)


def test_uma::activity_constructor_exists():
    assert callable(uma::Activity.__init__)


def test_uma::activity_constructor_args():
    sig = inspect.signature(uma::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "isEnactable" in params, "Missing parameter 'isEnactable'"

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



def test_methodelement_is_not_abstract():
    assert not inspect.isabstract(MethodElement)


def test_methodelement_constructor_exists():
    assert callable(MethodElement.__init__)


def test_methodelement_constructor_args():
    sig = inspect.signature(MethodElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::describableelement_is_not_abstract():
    assert not inspect.isabstract(uma::DescribableElement)


def test_uma::describableelement_constructor_exists():
    assert callable(uma::DescribableElement.__init__)


def test_uma::describableelement_constructor_args():
    sig = inspect.signature(uma::DescribableElement.__init__)
    params = list(sig.parameters.keys())
    assert "shapeicon" in params, "Missing parameter 'shapeicon'"
    assert "presentationName" in params, "Missing parameter 'presentationName'"
    assert "nodeicon" in params, "Missing parameter 'nodeicon'"

def test_uma::describableelement_has_shapeicon():
    assert hasattr(uma::DescribableElement, "shapeicon")
    descriptor = None
    for klass in uma::DescribableElement.__mro__:
        if "shapeicon" in klass.__dict__:
            descriptor = klass.__dict__["shapeicon"]
            break
    assert isinstance(descriptor, property)

def test_uma::describableelement_has_presentationName():
    assert hasattr(uma::DescribableElement, "presentationName")
    descriptor = None
    for klass in uma::DescribableElement.__mro__:
        if "presentationName" in klass.__dict__:
            descriptor = klass.__dict__["presentationName"]
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



def test_uma::workdefinition_is_not_abstract():
    assert not inspect.isabstract(uma::WorkDefinition)


def test_uma::workdefinition_constructor_exists():
    assert callable(uma::WorkDefinition.__init__)


def test_uma::workdefinition_constructor_args():
    sig = inspect.signature(uma::WorkDefinition.__init__)
    params = list(sig.parameters.keys())



def test_uma::methodunit_is_not_abstract():
    assert not inspect.isabstract(uma::MethodUnit)


def test_uma::methodunit_constructor_exists():
    assert callable(uma::MethodUnit.__init__)


def test_uma::methodunit_constructor_args():
    sig = inspect.signature(uma::MethodUnit.__init__)
    params = list(sig.parameters.keys())
    assert "changeDescription" in params, "Missing parameter 'changeDescription'"
    assert "changeDate" in params, "Missing parameter 'changeDate'"
    assert "version" in params, "Missing parameter 'version'"
    assert "authors" in params, "Missing parameter 'authors'"

def test_uma::methodunit_has_changeDescription():
    assert hasattr(uma::MethodUnit, "changeDescription")
    descriptor = None
    for klass in uma::MethodUnit.__mro__:
        if "changeDescription" in klass.__dict__:
            descriptor = klass.__dict__["changeDescription"]
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

def test_uma::methodunit_has_authors():
    assert hasattr(uma::MethodUnit, "authors")
    descriptor = None
    for klass in uma::MethodUnit.__mro__:
        if "authors" in klass.__dict__:
            descriptor = klass.__dict__["authors"]
            break
    assert isinstance(descriptor, property)



def test_uma::variabilityelement_is_not_abstract():
    assert not inspect.isabstract(uma::VariabilityElement)


def test_uma::variabilityelement_constructor_exists():
    assert callable(uma::VariabilityElement.__init__)


def test_uma::variabilityelement_constructor_args():
    sig = inspect.signature(uma::VariabilityElement.__init__)
    params = list(sig.parameters.keys())
    assert "variabilityType" in params, "Missing parameter 'variabilityType'"

def test_uma::variabilityelement_has_variabilityType():
    assert hasattr(uma::VariabilityElement, "variabilityType")
    descriptor = None
    for klass in uma::VariabilityElement.__mro__:
        if "variabilityType" in klass.__dict__:
            descriptor = klass.__dict__["variabilityType"]
            break
    assert isinstance(descriptor, property)



def test_uma::methodpackage_is_not_abstract():
    assert not inspect.isabstract(uma::MethodPackage)


def test_uma::methodpackage_constructor_exists():
    assert callable(uma::MethodPackage.__init__)


def test_uma::methodpackage_constructor_args():
    sig = inspect.signature(uma::MethodPackage.__init__)
    params = list(sig.parameters.keys())
    assert "global_" in params, "Missing parameter 'global_'"

def test_uma::methodpackage_has_global_():
    assert hasattr(uma::MethodPackage, "global_")
    descriptor = None
    for klass in uma::MethodPackage.__mro__:
        if "global_" in klass.__dict__:
            descriptor = klass.__dict__["global_"]
            break
    assert isinstance(descriptor, property)



def test_uma::diagramelement_is_not_abstract():
    assert not inspect.isabstract(uma::DiagramElement)


def test_uma::diagramelement_constructor_exists():
    assert callable(uma::DiagramElement.__init__)


def test_uma::diagramelement_constructor_args():
    sig = inspect.signature(uma::DiagramElement.__init__)
    params = list(sig.parameters.keys())
    assert "isVisible" in params, "Missing parameter 'isVisible'"

def test_uma::diagramelement_has_isVisible():
    assert hasattr(uma::DiagramElement, "isVisible")
    descriptor = None
    for klass in uma::DiagramElement.__mro__:
        if "isVisible" in klass.__dict__:
            descriptor = klass.__dict__["isVisible"]
            break
    assert isinstance(descriptor, property)



def test_uma::constraint_is_not_abstract():
    assert not inspect.isabstract(uma::Constraint)


def test_uma::constraint_constructor_exists():
    assert callable(uma::Constraint.__init__)


def test_uma::constraint_constructor_args():
    sig = inspect.signature(uma::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_uma::constraint_has_body():
    assert hasattr(uma::Constraint, "body")
    descriptor = None
    for klass in uma::Constraint.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::namespace_is_not_abstract():
    assert not inspect.isabstract(uma::Namespace)


def test_uma::namespace_constructor_exists():
    assert callable(uma::Namespace.__init__)


def test_uma::namespace_constructor_args():
    sig = inspect.signature(uma::Namespace.__init__)
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



def test_uma::element_is_not_abstract():
    assert not inspect.isabstract(uma::Element)


def test_uma::element_constructor_exists():
    assert callable(uma::Element.__init__)


def test_uma::element_constructor_args():
    sig = inspect.signature(uma::Element.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::methodelement_is_not_abstract():
    assert not inspect.isabstract(uma::MethodElement)


def test_uma::methodelement_constructor_exists():
    assert callable(uma::MethodElement.__init__)


def test_uma::methodelement_constructor_args():
    sig = inspect.signature(uma::MethodElement.__init__)
    params = list(sig.parameters.keys())
    assert "orderingGuide" in params, "Missing parameter 'orderingGuide'"
    assert "briefDescription" in params, "Missing parameter 'briefDescription'"
    assert "guid" in params, "Missing parameter 'guid'"
    assert "suppressed" in params, "Missing parameter 'suppressed'"

def test_uma::methodelement_has_orderingGuide():
    assert hasattr(uma::MethodElement, "orderingGuide")
    descriptor = None
    for klass in uma::MethodElement.__mro__:
        if "orderingGuide" in klass.__dict__:
            descriptor = klass.__dict__["orderingGuide"]
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

def test_uma::methodelement_has_guid():
    assert hasattr(uma::MethodElement, "guid")
    descriptor = None
    for klass in uma::MethodElement.__mro__:
        if "guid" in klass.__dict__:
            descriptor = klass.__dict__["guid"]
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



def test_uma::package_is_not_abstract():
    assert not inspect.isabstract(uma::Package)


def test_uma::package_constructor_exists():
    assert callable(uma::Package.__init__)


def test_uma::package_constructor_args():
    sig = inspect.signature(uma::Package.__init__)
    params = list(sig.parameters.keys())



def test_uma::type_is_not_abstract():
    assert not inspect.isabstract(uma::Type)


def test_uma::type_constructor_exists():
    assert callable(uma::Type.__init__)


def test_uma::type_constructor_args():
    sig = inspect.signature(uma::Type.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_uma::classifier_is_not_abstract():
    assert not inspect.isabstract(uma::Classifier)


def test_uma::classifier_constructor_exists():
    assert callable(uma::Classifier.__init__)


def test_uma::classifier_constructor_args():
    sig = inspect.signature(uma::Classifier.__init__)
    params = list(sig.parameters.keys())

def test_workordertype_exists():
    # Check that the Enumeration exists
    assert WorkOrderType is not None

def test_workordertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkOrderType]
    expected_literals = [
        "finishToFinish",
        "startToStart",
        "finishToStart",
        "startToFinish",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WorkOrderType"

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudoStateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudoStateKind]
    expected_literals = [
        "junction",
        "terminate",
        "entryPoint",
        "fork",
        "exitPoint",
        "choice",
        "join",
        "initial",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudoStateKind"

def test_variabilitytype_exists():
    # Check that the Enumeration exists
    assert VariabilityType is not None

def test_variabilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariabilityType]
    expected_literals = [
        "replaces",
        "na",
        "localReplacement",
        "contributes",
        "localContribution",
        "extends",
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
MethodConfiguration_strategy = st.builds(
    MethodConfiguration,
)
uma::ProcessFamily_strategy = st.builds(
    uma::ProcessFamily,
)
Process_strategy = st.builds(
    Process,
)
uma::DeliveryProcess_strategy = st.builds(
    uma::DeliveryProcess,
)
ProcessPackage_strategy = st.builds(
    ProcessPackage,
)
uma::ProcessPlanningTemplate_strategy = st.builds(
    uma::ProcessPlanningTemplate,
)
uma::CapabilityPattern_strategy = st.builds(
    uma::CapabilityPattern,
)
ContentCategory_strategy = st.builds(
    ContentCategory,
)
uma::Discipline_strategy = st.builds(
    uma::Discipline,
)
uma::CustomCategory_strategy = st.builds(
    uma::CustomCategory,
)
uma::RoleSetGrouping_strategy = st.builds(
    uma::RoleSetGrouping,
)
uma::Tool_strategy = st.builds(
    uma::Tool,
)
uma::DisciplineGrouping_strategy = st.builds(
    uma::DisciplineGrouping,
)
uma::WorkProductType_strategy = st.builds(
    uma::WorkProductType,
)
uma::Domain_strategy = st.builds(
    uma::Domain,
)
uma::RoleSet_strategy = st.builds(
    uma::RoleSet,
)
uma::Transition_strategy = st.builds(
    uma::Transition,
)
uma::Vertex_strategy = st.builds(
    uma::Vertex,
)
uma::Region_strategy = st.builds(
    uma::Region,
)
Vertex_strategy = st.builds(
    Vertex,
)
uma::PseudoState_strategy = st.builds(
    uma::PseudoState,
)
uma::State_strategy = st.builds(
    uma::State,
)
Concept_strategy = st.builds(
    Concept,
)
uma::Whitepaper_strategy = st.builds(
    uma::Whitepaper,
)
Guidance_strategy = st.builds(
    Guidance,
)
uma::Practice_strategy = st.builds(
    uma::Practice,
)
uma::TermDefinition_strategy = st.builds(
    uma::TermDefinition,
)
ActivityDescription_strategy = st.builds(
    ActivityDescription,
)
uma::ProcessDescription_strategy = st.builds(
    uma::ProcessDescription,
    scope=
        safe_text,
    usageNotes=
        safe_text,
    externalId=
        safe_text
)
ProcessDescription_strategy = st.builds(
    ProcessDescription,
)
uma::DeliveryProcessDescription_strategy = st.builds(
    uma::DeliveryProcessDescription,
    projectMemberExpertise=
        safe_text,
    riskLevel=
        safe_text,
    projectCharacteristics=
        safe_text,
    typeOfContract=
        safe_text,
    estimatingTechnique=
        safe_text,
    scale=
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
uma::ActivityDescription_strategy = st.builds(
    uma::ActivityDescription,
    purpose=
        safe_text,
    alternatives=
        safe_text,
    howtoStaff=
        safe_text
)
RoleDescriptor_strategy = st.builds(
    RoleDescriptor,
)
uma::CompositeRole_strategy = st.builds(
    uma::CompositeRole,
)
ProcessElement_strategy = st.builds(
    ProcessElement,
)
uma::WorkOrder_strategy = st.builds(
    uma::WorkOrder,
    linkType=
        safe_text
)
Descriptor_strategy = st.builds(
    Descriptor,
)
uma::WorkProductDescriptor_strategy = st.builds(
    uma::WorkProductDescriptor,
    activityEntryState=
        safe_text,
    activityExitState=
        safe_text
)
uma::ProcessComponentDescriptor_strategy = st.builds(
    uma::ProcessComponentDescriptor,
)
uma::RoleDescriptor_strategy = st.builds(
    uma::RoleDescriptor,
)
Activity_strategy = st.builds(
    Activity,
)
uma::Process_strategy = st.builds(
    uma::Process,
)
uma::Phase_strategy = st.builds(
    uma::Phase,
)
uma::Iteration_strategy = st.builds(
    uma::Iteration,
)
uma::PlanningData_strategy = st.builds(
    uma::PlanningData,
    rank=
        safe_text,
    finishDate=
        safe_text,
    startDate=
        safe_text
)
BreakdownElement_strategy = st.builds(
    BreakdownElement,
)
uma::TeamProfile_strategy = st.builds(
    uma::TeamProfile,
)
uma::ProcessComponentInterface_strategy = st.builds(
    uma::ProcessComponentInterface,
)
uma::Descriptor_strategy = st.builds(
    uma::Descriptor,
    isSynchronizedWithSource=
        safe_text
)
uma::WorkBreakdownElement_strategy = st.builds(
    uma::WorkBreakdownElement,
    isEventDriven=
        safe_text,
    isRepeatable=
        safe_text,
    isOngoing=
        safe_text
)
uma::Roadmap_strategy = st.builds(
    uma::Roadmap,
)
uma::BreakdownElement_strategy = st.builds(
    uma::BreakdownElement,
    prefix=
        safe_text,
    isOptional=
        safe_text,
    isPlanned=
        safe_text,
    hasMultipleOccurrences=
        safe_text
)
WorkBreakdownElement_strategy = st.builds(
    WorkBreakdownElement,
)
uma::TaskDescriptor_strategy = st.builds(
    uma::TaskDescriptor,
)
uma::Milestone_strategy = st.builds(
    uma::Milestone,
)
uma::Dimension_strategy = st.builds(
    uma::Dimension,
    width=
        safe_text,
    height=
        safe_text
)
GraphicPrimitive_strategy = st.builds(
    GraphicPrimitive,
)
uma::Ellipse_strategy = st.builds(
    uma::Ellipse,
    endAngle=
        safe_text,
    rotation=
        safe_text,
    radiusX=
        safe_text,
    radiusY=
        safe_text,
    startAngle=
        safe_text
)
uma::Polyline_strategy = st.builds(
    uma::Polyline,
    closed=
        safe_text
)
LeafElement_strategy = st.builds(
    LeafElement,
)
uma::GraphicPrimitive_strategy = st.builds(
    uma::GraphicPrimitive,
)
uma::Image_strategy = st.builds(
    uma::Image,
    uri=
        safe_text,
    mimeType=
        safe_text
)
uma::TextElement_strategy = st.builds(
    uma::TextElement,
    text=
        safe_text
)
SemanticModelBridge_strategy = st.builds(
    SemanticModelBridge,
)
uma::UMASemanticModelBridge_strategy = st.builds(
    uma::UMASemanticModelBridge,
)
uma::CoreSemanticModelBridge_strategy = st.builds(
    uma::CoreSemanticModelBridge,
)
uma::SimpleSemanticModelElement_strategy = st.builds(
    uma::SimpleSemanticModelElement,
    typeInfo=
        safe_text
)
GraphNode_strategy = st.builds(
    GraphNode,
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
uma::LeafElement_strategy = st.builds(
    uma::LeafElement,
)
uma::GraphElement_strategy = st.builds(
    uma::GraphElement,
)
GraphElement_strategy = st.builds(
    GraphElement,
)
uma::GraphEdge_strategy = st.builds(
    uma::GraphEdge,
)
uma::GraphNode_strategy = st.builds(
    uma::GraphNode,
)
uma::Diagram_strategy = st.builds(
    uma::Diagram,
    zoom=
        safe_text
)
uma::Property_strategy = st.builds(
    uma::Property,
    value=
        safe_text,
    key=
        safe_text
)
uma::Reference_strategy = st.builds(
    uma::Reference,
    isIndividualRepresentation=
        safe_text
)
uma::SemanticModelBridge_strategy = st.builds(
    uma::SemanticModelBridge,
    presentation=
        safe_text
)
uma::GraphConnector_strategy = st.builds(
    uma::GraphConnector,
)
uma::DiagramLink_strategy = st.builds(
    uma::DiagramLink,
    zoom=
        safe_text
)
ContentDescription_strategy = st.builds(
    ContentDescription,
)
uma::BreakdownElementDescription_strategy = st.builds(
    uma::BreakdownElementDescription,
    usageGuidance=
        safe_text
)
uma::WorkProductDescription_strategy = st.builds(
    uma::WorkProductDescription,
    impactOfNotHaving=
        safe_text,
    reasonsForNotNeeding=
        safe_text,
    externalId=
        safe_text,
    purpose=
        safe_text
)
WorkProductDescription_strategy = st.builds(
    WorkProductDescription,
)
uma::ArtifactDescription_strategy = st.builds(
    uma::ArtifactDescription,
    briefOutline=
        safe_text,
    representationOptions=
        safe_text
)
uma::Point_strategy = st.builds(
    uma::Point,
    x=
        safe_text,
    y=
        safe_text
)
uma::PracticeDescription_strategy = st.builds(
    uma::PracticeDescription,
    levelsOfAdoption=
        safe_text,
    additionalInfo=
        safe_text,
    goals=
        safe_text,
    background=
        safe_text,
    problem=
        safe_text,
    application=
        safe_text
)
uma::GuidanceDescription_strategy = st.builds(
    uma::GuidanceDescription,
    attachments=
        safe_text
)
uma::TaskDescription_strategy = st.builds(
    uma::TaskDescription,
    alternatives=
        safe_text,
    purpose=
        safe_text
)
uma::RoleDescription_strategy = st.builds(
    uma::RoleDescription,
    synonyms=
        safe_text,
    assignmentApproaches=
        safe_text,
    skills=
        safe_text
)
uma::DeliverableDescription_strategy = st.builds(
    uma::DeliverableDescription,
    externalDescription=
        safe_text,
    packagingGuidance=
        safe_text
)
MethodPackage_strategy = st.builds(
    MethodPackage,
)
uma::ProcessPackage_strategy = st.builds(
    uma::ProcessPackage,
)
uma::ContentPackage_strategy = st.builds(
    uma::ContentPackage,
)
Package_strategy = st.builds(
    Package,
)
WorkProduct_strategy = st.builds(
    WorkProduct,
)
uma::Outcome_strategy = st.builds(
    uma::Outcome,
)
uma::Deliverable_strategy = st.builds(
    uma::Deliverable,
)
uma::Artifact_strategy = st.builds(
    uma::Artifact,
)
Section_strategy = st.builds(
    Section,
)
MethodUnit_strategy = st.builds(
    MethodUnit,
)
uma::MethodConfiguration_strategy = st.builds(
    uma::MethodConfiguration,
)
uma::MethodLibrary_strategy = st.builds(
    uma::MethodLibrary,
)
uma::ProcessComponent_strategy = st.builds(
    uma::ProcessComponent,
)
uma::MethodPlugin_strategy = st.builds(
    uma::MethodPlugin,
    userChangeable=
        safe_text
)
WorkDefinition_strategy = st.builds(
    WorkDefinition,
)
uma::StateMachine_strategy = st.builds(
    uma::StateMachine,
)
uma::Step_strategy = st.builds(
    uma::Step,
)
uma::EstimationConsiderations_strategy = st.builds(
    uma::EstimationConsiderations,
)
uma::ToolMentor_strategy = st.builds(
    uma::ToolMentor,
)
uma::Template_strategy = st.builds(
    uma::Template,
)
uma::Report_strategy = st.builds(
    uma::Report,
)
ContentElement_strategy = st.builds(
    ContentElement,
)
uma::ContentCategory_strategy = st.builds(
    uma::ContentCategory,
)
uma::Task_strategy = st.builds(
    uma::Task,
)
uma::Guidance_strategy = st.builds(
    uma::Guidance,
)
uma::WorkProduct_strategy = st.builds(
    uma::WorkProduct,
)
uma::Role_strategy = st.builds(
    uma::Role,
)
uma::ContentDescription_strategy = st.builds(
    uma::ContentDescription,
    mainDescription=
        safe_text,
    keyConsiderations=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
uma::ReusableAsset_strategy = st.builds(
    uma::ReusableAsset,
)
uma::Example_strategy = st.builds(
    uma::Example,
)
uma::Guideline_strategy = st.builds(
    uma::Guideline,
)
uma::Checklist_strategy = st.builds(
    uma::Checklist,
)
uma::Concept_strategy = st.builds(
    uma::Concept,
)
uma::SupportingMaterial_strategy = st.builds(
    uma::SupportingMaterial,
)
VariabilityElement_strategy = st.builds(
    VariabilityElement,
)
uma::Section_strategy = st.builds(
    uma::Section,
    sectionDescription=
        safe_text,
    sectionName=
        safe_text
)
uma::Activity_strategy = st.builds(
    uma::Activity,
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
)
MethodElement_strategy = st.builds(
    MethodElement,
)
uma::DescribableElement_strategy = st.builds(
    uma::DescribableElement,
    shapeicon=
        safe_text,
    presentationName=
        safe_text,
    nodeicon=
        safe_text
)
uma::WorkDefinition_strategy = st.builds(
    uma::WorkDefinition,
)
uma::MethodUnit_strategy = st.builds(
    uma::MethodUnit,
    changeDescription=
        safe_text,
    changeDate=
        safe_text,
    version=
        safe_text,
    authors=
        safe_text
)
uma::VariabilityElement_strategy = st.builds(
    uma::VariabilityElement,
    variabilityType=
        safe_text
)
uma::MethodPackage_strategy = st.builds(
    uma::MethodPackage,
    global_=
        safe_text
)
uma::DiagramElement_strategy = st.builds(
    uma::DiagramElement,
    isVisible=
        safe_text
)
uma::Constraint_strategy = st.builds(
    uma::Constraint,
    body=
        safe_text
)
Namespace_strategy = st.builds(
    Namespace,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
uma::Namespace_strategy = st.builds(
    uma::Namespace,
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
uma::Element_strategy = st.builds(
    uma::Element,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
uma::MethodElement_strategy = st.builds(
    uma::MethodElement,
    orderingGuide=
        safe_text,
    briefDescription=
        safe_text,
    guid=
        safe_text,
    suppressed=
        safe_text
)
uma::Package_strategy = st.builds(
    uma::Package,
)
uma::Type_strategy = st.builds(
    uma::Type,
)
Type_strategy = st.builds(
    Type,
)
uma::Classifier_strategy = st.builds(
    uma::Classifier,
)

@given(instance=MethodConfiguration_strategy)
@settings(max_examples=50)
def test_methodconfiguration_instantiation(instance):
    assert isinstance(instance, MethodConfiguration)

@given(instance=uma::ProcessFamily_strategy)
@settings(max_examples=50)
def test_uma::processfamily_instantiation(instance):
    assert isinstance(instance, uma::ProcessFamily)

@given(instance=Process_strategy)
@settings(max_examples=50)
def test_process_instantiation(instance):
    assert isinstance(instance, Process)

@given(instance=uma::DeliveryProcess_strategy)
@settings(max_examples=50)
def test_uma::deliveryprocess_instantiation(instance):
    assert isinstance(instance, uma::DeliveryProcess)

@given(instance=ProcessPackage_strategy)
@settings(max_examples=50)
def test_processpackage_instantiation(instance):
    assert isinstance(instance, ProcessPackage)

@given(instance=uma::ProcessPlanningTemplate_strategy)
@settings(max_examples=50)
def test_uma::processplanningtemplate_instantiation(instance):
    assert isinstance(instance, uma::ProcessPlanningTemplate)

@given(instance=uma::CapabilityPattern_strategy)
@settings(max_examples=50)
def test_uma::capabilitypattern_instantiation(instance):
    assert isinstance(instance, uma::CapabilityPattern)

@given(instance=ContentCategory_strategy)
@settings(max_examples=50)
def test_contentcategory_instantiation(instance):
    assert isinstance(instance, ContentCategory)

@given(instance=uma::Discipline_strategy)
@settings(max_examples=50)
def test_uma::discipline_instantiation(instance):
    assert isinstance(instance, uma::Discipline)

@given(instance=uma::CustomCategory_strategy)
@settings(max_examples=50)
def test_uma::customcategory_instantiation(instance):
    assert isinstance(instance, uma::CustomCategory)

@given(instance=uma::RoleSetGrouping_strategy)
@settings(max_examples=50)
def test_uma::rolesetgrouping_instantiation(instance):
    assert isinstance(instance, uma::RoleSetGrouping)

@given(instance=uma::Tool_strategy)
@settings(max_examples=50)
def test_uma::tool_instantiation(instance):
    assert isinstance(instance, uma::Tool)

@given(instance=uma::DisciplineGrouping_strategy)
@settings(max_examples=50)
def test_uma::disciplinegrouping_instantiation(instance):
    assert isinstance(instance, uma::DisciplineGrouping)

@given(instance=uma::WorkProductType_strategy)
@settings(max_examples=50)
def test_uma::workproducttype_instantiation(instance):
    assert isinstance(instance, uma::WorkProductType)

@given(instance=uma::Domain_strategy)
@settings(max_examples=50)
def test_uma::domain_instantiation(instance):
    assert isinstance(instance, uma::Domain)

@given(instance=uma::RoleSet_strategy)
@settings(max_examples=50)
def test_uma::roleset_instantiation(instance):
    assert isinstance(instance, uma::RoleSet)

@given(instance=uma::Transition_strategy)
@settings(max_examples=50)
def test_uma::transition_instantiation(instance):
    assert isinstance(instance, uma::Transition)

@given(instance=uma::Vertex_strategy)
@settings(max_examples=50)
def test_uma::vertex_instantiation(instance):
    assert isinstance(instance, uma::Vertex)

@given(instance=uma::Region_strategy)
@settings(max_examples=50)
def test_uma::region_instantiation(instance):
    assert isinstance(instance, uma::Region)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=uma::PseudoState_strategy)
@settings(max_examples=50)
def test_uma::pseudostate_instantiation(instance):
    assert isinstance(instance, uma::PseudoState)

@given(instance=uma::State_strategy)
@settings(max_examples=50)
def test_uma::state_instantiation(instance):
    assert isinstance(instance, uma::State)

@given(instance=Concept_strategy)
@settings(max_examples=50)
def test_concept_instantiation(instance):
    assert isinstance(instance, Concept)

@given(instance=uma::Whitepaper_strategy)
@settings(max_examples=50)
def test_uma::whitepaper_instantiation(instance):
    assert isinstance(instance, uma::Whitepaper)

@given(instance=Guidance_strategy)
@settings(max_examples=50)
def test_guidance_instantiation(instance):
    assert isinstance(instance, Guidance)

@given(instance=uma::Practice_strategy)
@settings(max_examples=50)
def test_uma::practice_instantiation(instance):
    assert isinstance(instance, uma::Practice)

@given(instance=uma::TermDefinition_strategy)
@settings(max_examples=50)
def test_uma::termdefinition_instantiation(instance):
    assert isinstance(instance, uma::TermDefinition)

@given(instance=ActivityDescription_strategy)
@settings(max_examples=50)
def test_activitydescription_instantiation(instance):
    assert isinstance(instance, ActivityDescription)

@given(instance=uma::ProcessDescription_strategy)
@settings(max_examples=50)
def test_uma::processdescription_instantiation(instance):
    assert isinstance(instance, uma::ProcessDescription)

@given(instance=uma::ProcessDescription_strategy)
def test_uma::processdescription_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=uma::ProcessDescription_strategy)
def test_uma::processdescription_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=uma::ProcessDescription_strategy)
def test_uma::processdescription_usageNotes_type(instance):
    assert isinstance(instance.usageNotes, str)


@given(instance=uma::ProcessDescription_strategy)
def test_uma::processdescription_usageNotes_setter(instance):
    original = instance.usageNotes
    instance.usageNotes = original
    assert instance.usageNotes == original

@given(instance=uma::ProcessDescription_strategy)
def test_uma::processdescription_externalId_type(instance):
    assert isinstance(instance.externalId, str)


@given(instance=uma::ProcessDescription_strategy)
def test_uma::processdescription_externalId_setter(instance):
    original = instance.externalId
    instance.externalId = original
    assert instance.externalId == original

@given(instance=ProcessDescription_strategy)
@settings(max_examples=50)
def test_processdescription_instantiation(instance):
    assert isinstance(instance, ProcessDescription)

@given(instance=uma::DeliveryProcessDescription_strategy)
@settings(max_examples=50)
def test_uma::deliveryprocessdescription_instantiation(instance):
    assert isinstance(instance, uma::DeliveryProcessDescription)

@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_projectMemberExpertise_type(instance):
    assert isinstance(instance.projectMemberExpertise, str)


@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_projectMemberExpertise_setter(instance):
    original = instance.projectMemberExpertise
    instance.projectMemberExpertise = original
    assert instance.projectMemberExpertise == original

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
def test_uma::deliveryprocessdescription_typeOfContract_type(instance):
    assert isinstance(instance.typeOfContract, str)


@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_typeOfContract_setter(instance):
    original = instance.typeOfContract
    instance.typeOfContract = original
    assert instance.typeOfContract == original

@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_estimatingTechnique_type(instance):
    assert isinstance(instance.estimatingTechnique, str)


@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_estimatingTechnique_setter(instance):
    original = instance.estimatingTechnique
    instance.estimatingTechnique = original
    assert instance.estimatingTechnique == original

@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_scale_type(instance):
    assert isinstance(instance.scale, str)


@given(instance=uma::DeliveryProcessDescription_strategy)
def test_uma::deliveryprocessdescription_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

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
def test_uma::activitydescription_alternatives_type(instance):
    assert isinstance(instance.alternatives, str)


@given(instance=uma::ActivityDescription_strategy)
def test_uma::activitydescription_alternatives_setter(instance):
    original = instance.alternatives
    instance.alternatives = original
    assert instance.alternatives == original

@given(instance=uma::ActivityDescription_strategy)
def test_uma::activitydescription_howtoStaff_type(instance):
    assert isinstance(instance.howtoStaff, str)


@given(instance=uma::ActivityDescription_strategy)
def test_uma::activitydescription_howtoStaff_setter(instance):
    original = instance.howtoStaff
    instance.howtoStaff = original
    assert instance.howtoStaff == original

@given(instance=RoleDescriptor_strategy)
@settings(max_examples=50)
def test_roledescriptor_instantiation(instance):
    assert isinstance(instance, RoleDescriptor)

@given(instance=uma::CompositeRole_strategy)
@settings(max_examples=50)
def test_uma::compositerole_instantiation(instance):
    assert isinstance(instance, uma::CompositeRole)

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

@given(instance=uma::WorkOrder_strategy)
@settings(max_examples=50)
def test_uma::workorder_instantiation(instance):
    assert isinstance(instance, uma::WorkOrder)

@given(instance=uma::WorkOrder_strategy)
def test_uma::workorder_linkType_type(instance):
    assert isinstance(instance.linkType, str)


@given(instance=uma::WorkOrder_strategy)
def test_uma::workorder_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original

@given(instance=Descriptor_strategy)
@settings(max_examples=50)
def test_descriptor_instantiation(instance):
    assert isinstance(instance, Descriptor)

@given(instance=uma::WorkProductDescriptor_strategy)
@settings(max_examples=50)
def test_uma::workproductdescriptor_instantiation(instance):
    assert isinstance(instance, uma::WorkProductDescriptor)

@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_activityEntryState_type(instance):
    assert isinstance(instance.activityEntryState, str)


@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_activityEntryState_setter(instance):
    original = instance.activityEntryState
    instance.activityEntryState = original
    assert instance.activityEntryState == original

@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_activityExitState_type(instance):
    assert isinstance(instance.activityExitState, str)


@given(instance=uma::WorkProductDescriptor_strategy)
def test_uma::workproductdescriptor_activityExitState_setter(instance):
    original = instance.activityExitState
    instance.activityExitState = original
    assert instance.activityExitState == original

@given(instance=uma::ProcessComponentDescriptor_strategy)
@settings(max_examples=50)
def test_uma::processcomponentdescriptor_instantiation(instance):
    assert isinstance(instance, uma::ProcessComponentDescriptor)

@given(instance=uma::RoleDescriptor_strategy)
@settings(max_examples=50)
def test_uma::roledescriptor_instantiation(instance):
    assert isinstance(instance, uma::RoleDescriptor)

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=uma::Process_strategy)
@settings(max_examples=50)
def test_uma::process_instantiation(instance):
    assert isinstance(instance, uma::Process)

@given(instance=uma::Phase_strategy)
@settings(max_examples=50)
def test_uma::phase_instantiation(instance):
    assert isinstance(instance, uma::Phase)

@given(instance=uma::Iteration_strategy)
@settings(max_examples=50)
def test_uma::iteration_instantiation(instance):
    assert isinstance(instance, uma::Iteration)

@given(instance=uma::PlanningData_strategy)
@settings(max_examples=50)
def test_uma::planningdata_instantiation(instance):
    assert isinstance(instance, uma::PlanningData)

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

@given(instance=uma::PlanningData_strategy)
def test_uma::planningdata_startDate_type(instance):
    assert isinstance(instance.startDate, str)


@given(instance=uma::PlanningData_strategy)
def test_uma::planningdata_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original

@given(instance=BreakdownElement_strategy)
@settings(max_examples=50)
def test_breakdownelement_instantiation(instance):
    assert isinstance(instance, BreakdownElement)

@given(instance=uma::TeamProfile_strategy)
@settings(max_examples=50)
def test_uma::teamprofile_instantiation(instance):
    assert isinstance(instance, uma::TeamProfile)

@given(instance=uma::ProcessComponentInterface_strategy)
@settings(max_examples=50)
def test_uma::processcomponentinterface_instantiation(instance):
    assert isinstance(instance, uma::ProcessComponentInterface)

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

@given(instance=uma::WorkBreakdownElement_strategy)
@settings(max_examples=50)
def test_uma::workbreakdownelement_instantiation(instance):
    assert isinstance(instance, uma::WorkBreakdownElement)

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

@given(instance=uma::Roadmap_strategy)
@settings(max_examples=50)
def test_uma::roadmap_instantiation(instance):
    assert isinstance(instance, uma::Roadmap)

@given(instance=uma::BreakdownElement_strategy)
@settings(max_examples=50)
def test_uma::breakdownelement_instantiation(instance):
    assert isinstance(instance, uma::BreakdownElement)

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_prefix_type(instance):
    assert isinstance(instance.prefix, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_isOptional_type(instance):
    assert isinstance(instance.isOptional, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_isPlanned_type(instance):
    assert isinstance(instance.isPlanned, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_isPlanned_setter(instance):
    original = instance.isPlanned
    instance.isPlanned = original
    assert instance.isPlanned == original

@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_hasMultipleOccurrences_type(instance):
    assert isinstance(instance.hasMultipleOccurrences, str)


@given(instance=uma::BreakdownElement_strategy)
def test_uma::breakdownelement_hasMultipleOccurrences_setter(instance):
    original = instance.hasMultipleOccurrences
    instance.hasMultipleOccurrences = original
    assert instance.hasMultipleOccurrences == original

@given(instance=WorkBreakdownElement_strategy)
@settings(max_examples=50)
def test_workbreakdownelement_instantiation(instance):
    assert isinstance(instance, WorkBreakdownElement)

@given(instance=uma::TaskDescriptor_strategy)
@settings(max_examples=50)
def test_uma::taskdescriptor_instantiation(instance):
    assert isinstance(instance, uma::TaskDescriptor)

@given(instance=uma::Milestone_strategy)
@settings(max_examples=50)
def test_uma::milestone_instantiation(instance):
    assert isinstance(instance, uma::Milestone)

@given(instance=uma::Dimension_strategy)
@settings(max_examples=50)
def test_uma::dimension_instantiation(instance):
    assert isinstance(instance, uma::Dimension)

@given(instance=uma::Dimension_strategy)
def test_uma::dimension_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=uma::Dimension_strategy)
def test_uma::dimension_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=uma::Dimension_strategy)
def test_uma::dimension_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=uma::Dimension_strategy)
def test_uma::dimension_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=GraphicPrimitive_strategy)
@settings(max_examples=50)
def test_graphicprimitive_instantiation(instance):
    assert isinstance(instance, GraphicPrimitive)

@given(instance=uma::Ellipse_strategy)
@settings(max_examples=50)
def test_uma::ellipse_instantiation(instance):
    assert isinstance(instance, uma::Ellipse)

@given(instance=uma::Ellipse_strategy)
def test_uma::ellipse_endAngle_type(instance):
    assert isinstance(instance.endAngle, str)


@given(instance=uma::Ellipse_strategy)
def test_uma::ellipse_endAngle_setter(instance):
    original = instance.endAngle
    instance.endAngle = original
    assert instance.endAngle == original

@given(instance=uma::Ellipse_strategy)
def test_uma::ellipse_rotation_type(instance):
    assert isinstance(instance.rotation, str)


@given(instance=uma::Ellipse_strategy)
def test_uma::ellipse_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original

@given(instance=uma::Ellipse_strategy)
def test_uma::ellipse_radiusX_type(instance):
    assert isinstance(instance.radiusX, str)


@given(instance=uma::Ellipse_strategy)
def test_uma::ellipse_radiusX_setter(instance):
    original = instance.radiusX
    instance.radiusX = original
    assert instance.radiusX == original

@given(instance=uma::Ellipse_strategy)
def test_uma::ellipse_radiusY_type(instance):
    assert isinstance(instance.radiusY, str)


@given(instance=uma::Ellipse_strategy)
def test_uma::ellipse_radiusY_setter(instance):
    original = instance.radiusY
    instance.radiusY = original
    assert instance.radiusY == original

@given(instance=uma::Ellipse_strategy)
def test_uma::ellipse_startAngle_type(instance):
    assert isinstance(instance.startAngle, str)


@given(instance=uma::Ellipse_strategy)
def test_uma::ellipse_startAngle_setter(instance):
    original = instance.startAngle
    instance.startAngle = original
    assert instance.startAngle == original

@given(instance=uma::Polyline_strategy)
@settings(max_examples=50)
def test_uma::polyline_instantiation(instance):
    assert isinstance(instance, uma::Polyline)

@given(instance=uma::Polyline_strategy)
def test_uma::polyline_closed_type(instance):
    assert isinstance(instance.closed, str)


@given(instance=uma::Polyline_strategy)
def test_uma::polyline_closed_setter(instance):
    original = instance.closed
    instance.closed = original
    assert instance.closed == original

@given(instance=LeafElement_strategy)
@settings(max_examples=50)
def test_leafelement_instantiation(instance):
    assert isinstance(instance, LeafElement)

@given(instance=uma::GraphicPrimitive_strategy)
@settings(max_examples=50)
def test_uma::graphicprimitive_instantiation(instance):
    assert isinstance(instance, uma::GraphicPrimitive)

@given(instance=uma::Image_strategy)
@settings(max_examples=50)
def test_uma::image_instantiation(instance):
    assert isinstance(instance, uma::Image)

@given(instance=uma::Image_strategy)
def test_uma::image_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=uma::Image_strategy)
def test_uma::image_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=uma::Image_strategy)
def test_uma::image_mimeType_type(instance):
    assert isinstance(instance.mimeType, str)


@given(instance=uma::Image_strategy)
def test_uma::image_mimeType_setter(instance):
    original = instance.mimeType
    instance.mimeType = original
    assert instance.mimeType == original

@given(instance=uma::TextElement_strategy)
@settings(max_examples=50)
def test_uma::textelement_instantiation(instance):
    assert isinstance(instance, uma::TextElement)

@given(instance=uma::TextElement_strategy)
def test_uma::textelement_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=uma::TextElement_strategy)
def test_uma::textelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=SemanticModelBridge_strategy)
@settings(max_examples=50)
def test_semanticmodelbridge_instantiation(instance):
    assert isinstance(instance, SemanticModelBridge)

@given(instance=uma::UMASemanticModelBridge_strategy)
@settings(max_examples=50)
def test_uma::umasemanticmodelbridge_instantiation(instance):
    assert isinstance(instance, uma::UMASemanticModelBridge)

@given(instance=uma::CoreSemanticModelBridge_strategy)
@settings(max_examples=50)
def test_uma::coresemanticmodelbridge_instantiation(instance):
    assert isinstance(instance, uma::CoreSemanticModelBridge)

@given(instance=uma::SimpleSemanticModelElement_strategy)
@settings(max_examples=50)
def test_uma::simplesemanticmodelelement_instantiation(instance):
    assert isinstance(instance, uma::SimpleSemanticModelElement)

@given(instance=uma::SimpleSemanticModelElement_strategy)
def test_uma::simplesemanticmodelelement_typeInfo_type(instance):
    assert isinstance(instance.typeInfo, str)


@given(instance=uma::SimpleSemanticModelElement_strategy)
def test_uma::simplesemanticmodelelement_typeInfo_setter(instance):
    original = instance.typeInfo
    instance.typeInfo = original
    assert instance.typeInfo == original

@given(instance=GraphNode_strategy)
@settings(max_examples=50)
def test_graphnode_instantiation(instance):
    assert isinstance(instance, GraphNode)

@given(instance=DiagramElement_strategy)
@settings(max_examples=50)
def test_diagramelement_instantiation(instance):
    assert isinstance(instance, DiagramElement)

@given(instance=uma::LeafElement_strategy)
@settings(max_examples=50)
def test_uma::leafelement_instantiation(instance):
    assert isinstance(instance, uma::LeafElement)

@given(instance=uma::GraphElement_strategy)
@settings(max_examples=50)
def test_uma::graphelement_instantiation(instance):
    assert isinstance(instance, uma::GraphElement)

@given(instance=GraphElement_strategy)
@settings(max_examples=50)
def test_graphelement_instantiation(instance):
    assert isinstance(instance, GraphElement)

@given(instance=uma::GraphEdge_strategy)
@settings(max_examples=50)
def test_uma::graphedge_instantiation(instance):
    assert isinstance(instance, uma::GraphEdge)

@given(instance=uma::GraphNode_strategy)
@settings(max_examples=50)
def test_uma::graphnode_instantiation(instance):
    assert isinstance(instance, uma::GraphNode)

@given(instance=uma::Diagram_strategy)
@settings(max_examples=50)
def test_uma::diagram_instantiation(instance):
    assert isinstance(instance, uma::Diagram)

@given(instance=uma::Diagram_strategy)
def test_uma::diagram_zoom_type(instance):
    assert isinstance(instance.zoom, str)


@given(instance=uma::Diagram_strategy)
def test_uma::diagram_zoom_setter(instance):
    original = instance.zoom
    instance.zoom = original
    assert instance.zoom == original

@given(instance=uma::Property_strategy)
@settings(max_examples=50)
def test_uma::property_instantiation(instance):
    assert isinstance(instance, uma::Property)

@given(instance=uma::Property_strategy)
def test_uma::property_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=uma::Property_strategy)
def test_uma::property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uma::Property_strategy)
def test_uma::property_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=uma::Property_strategy)
def test_uma::property_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=uma::Reference_strategy)
@settings(max_examples=50)
def test_uma::reference_instantiation(instance):
    assert isinstance(instance, uma::Reference)

@given(instance=uma::Reference_strategy)
def test_uma::reference_isIndividualRepresentation_type(instance):
    assert isinstance(instance.isIndividualRepresentation, str)


@given(instance=uma::Reference_strategy)
def test_uma::reference_isIndividualRepresentation_setter(instance):
    original = instance.isIndividualRepresentation
    instance.isIndividualRepresentation = original
    assert instance.isIndividualRepresentation == original

@given(instance=uma::SemanticModelBridge_strategy)
@settings(max_examples=50)
def test_uma::semanticmodelbridge_instantiation(instance):
    assert isinstance(instance, uma::SemanticModelBridge)

@given(instance=uma::SemanticModelBridge_strategy)
def test_uma::semanticmodelbridge_presentation_type(instance):
    assert isinstance(instance.presentation, str)


@given(instance=uma::SemanticModelBridge_strategy)
def test_uma::semanticmodelbridge_presentation_setter(instance):
    original = instance.presentation
    instance.presentation = original
    assert instance.presentation == original

@given(instance=uma::GraphConnector_strategy)
@settings(max_examples=50)
def test_uma::graphconnector_instantiation(instance):
    assert isinstance(instance, uma::GraphConnector)

@given(instance=uma::DiagramLink_strategy)
@settings(max_examples=50)
def test_uma::diagramlink_instantiation(instance):
    assert isinstance(instance, uma::DiagramLink)

@given(instance=uma::DiagramLink_strategy)
def test_uma::diagramlink_zoom_type(instance):
    assert isinstance(instance.zoom, str)


@given(instance=uma::DiagramLink_strategy)
def test_uma::diagramlink_zoom_setter(instance):
    original = instance.zoom
    instance.zoom = original
    assert instance.zoom == original

@given(instance=ContentDescription_strategy)
@settings(max_examples=50)
def test_contentdescription_instantiation(instance):
    assert isinstance(instance, ContentDescription)

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

@given(instance=uma::WorkProductDescription_strategy)
@settings(max_examples=50)
def test_uma::workproductdescription_instantiation(instance):
    assert isinstance(instance, uma::WorkProductDescription)

@given(instance=uma::WorkProductDescription_strategy)
def test_uma::workproductdescription_impactOfNotHaving_type(instance):
    assert isinstance(instance.impactOfNotHaving, str)


@given(instance=uma::WorkProductDescription_strategy)
def test_uma::workproductdescription_impactOfNotHaving_setter(instance):
    original = instance.impactOfNotHaving
    instance.impactOfNotHaving = original
    assert instance.impactOfNotHaving == original

@given(instance=uma::WorkProductDescription_strategy)
def test_uma::workproductdescription_reasonsForNotNeeding_type(instance):
    assert isinstance(instance.reasonsForNotNeeding, str)


@given(instance=uma::WorkProductDescription_strategy)
def test_uma::workproductdescription_reasonsForNotNeeding_setter(instance):
    original = instance.reasonsForNotNeeding
    instance.reasonsForNotNeeding = original
    assert instance.reasonsForNotNeeding == original

@given(instance=uma::WorkProductDescription_strategy)
def test_uma::workproductdescription_externalId_type(instance):
    assert isinstance(instance.externalId, str)


@given(instance=uma::WorkProductDescription_strategy)
def test_uma::workproductdescription_externalId_setter(instance):
    original = instance.externalId
    instance.externalId = original
    assert instance.externalId == original

@given(instance=uma::WorkProductDescription_strategy)
def test_uma::workproductdescription_purpose_type(instance):
    assert isinstance(instance.purpose, str)


@given(instance=uma::WorkProductDescription_strategy)
def test_uma::workproductdescription_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original

@given(instance=WorkProductDescription_strategy)
@settings(max_examples=50)
def test_workproductdescription_instantiation(instance):
    assert isinstance(instance, WorkProductDescription)

@given(instance=uma::ArtifactDescription_strategy)
@settings(max_examples=50)
def test_uma::artifactdescription_instantiation(instance):
    assert isinstance(instance, uma::ArtifactDescription)

@given(instance=uma::ArtifactDescription_strategy)
def test_uma::artifactdescription_briefOutline_type(instance):
    assert isinstance(instance.briefOutline, str)


@given(instance=uma::ArtifactDescription_strategy)
def test_uma::artifactdescription_briefOutline_setter(instance):
    original = instance.briefOutline
    instance.briefOutline = original
    assert instance.briefOutline == original

@given(instance=uma::ArtifactDescription_strategy)
def test_uma::artifactdescription_representationOptions_type(instance):
    assert isinstance(instance.representationOptions, str)


@given(instance=uma::ArtifactDescription_strategy)
def test_uma::artifactdescription_representationOptions_setter(instance):
    original = instance.representationOptions
    instance.representationOptions = original
    assert instance.representationOptions == original

@given(instance=uma::Point_strategy)
@settings(max_examples=50)
def test_uma::point_instantiation(instance):
    assert isinstance(instance, uma::Point)

@given(instance=uma::Point_strategy)
def test_uma::point_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=uma::Point_strategy)
def test_uma::point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=uma::Point_strategy)
def test_uma::point_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=uma::Point_strategy)
def test_uma::point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=uma::PracticeDescription_strategy)
@settings(max_examples=50)
def test_uma::practicedescription_instantiation(instance):
    assert isinstance(instance, uma::PracticeDescription)

@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_levelsOfAdoption_type(instance):
    assert isinstance(instance.levelsOfAdoption, str)


@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_levelsOfAdoption_setter(instance):
    original = instance.levelsOfAdoption
    instance.levelsOfAdoption = original
    assert instance.levelsOfAdoption == original

@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_additionalInfo_type(instance):
    assert isinstance(instance.additionalInfo, str)


@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_additionalInfo_setter(instance):
    original = instance.additionalInfo
    instance.additionalInfo = original
    assert instance.additionalInfo == original

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
def test_uma::practicedescription_problem_type(instance):
    assert isinstance(instance.problem, str)


@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_problem_setter(instance):
    original = instance.problem
    instance.problem = original
    assert instance.problem == original

@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_application_type(instance):
    assert isinstance(instance.application, str)


@given(instance=uma::PracticeDescription_strategy)
def test_uma::practicedescription_application_setter(instance):
    original = instance.application
    instance.application = original
    assert instance.application == original

@given(instance=uma::GuidanceDescription_strategy)
@settings(max_examples=50)
def test_uma::guidancedescription_instantiation(instance):
    assert isinstance(instance, uma::GuidanceDescription)

@given(instance=uma::GuidanceDescription_strategy)
def test_uma::guidancedescription_attachments_type(instance):
    assert isinstance(instance.attachments, str)


@given(instance=uma::GuidanceDescription_strategy)
def test_uma::guidancedescription_attachments_setter(instance):
    original = instance.attachments
    instance.attachments = original
    assert instance.attachments == original

@given(instance=uma::TaskDescription_strategy)
@settings(max_examples=50)
def test_uma::taskdescription_instantiation(instance):
    assert isinstance(instance, uma::TaskDescription)

@given(instance=uma::TaskDescription_strategy)
def test_uma::taskdescription_alternatives_type(instance):
    assert isinstance(instance.alternatives, str)


@given(instance=uma::TaskDescription_strategy)
def test_uma::taskdescription_alternatives_setter(instance):
    original = instance.alternatives
    instance.alternatives = original
    assert instance.alternatives == original

@given(instance=uma::TaskDescription_strategy)
def test_uma::taskdescription_purpose_type(instance):
    assert isinstance(instance.purpose, str)


@given(instance=uma::TaskDescription_strategy)
def test_uma::taskdescription_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original

@given(instance=uma::RoleDescription_strategy)
@settings(max_examples=50)
def test_uma::roledescription_instantiation(instance):
    assert isinstance(instance, uma::RoleDescription)

@given(instance=uma::RoleDescription_strategy)
def test_uma::roledescription_synonyms_type(instance):
    assert isinstance(instance.synonyms, str)


@given(instance=uma::RoleDescription_strategy)
def test_uma::roledescription_synonyms_setter(instance):
    original = instance.synonyms
    instance.synonyms = original
    assert instance.synonyms == original

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

@given(instance=MethodPackage_strategy)
@settings(max_examples=50)
def test_methodpackage_instantiation(instance):
    assert isinstance(instance, MethodPackage)

@given(instance=uma::ProcessPackage_strategy)
@settings(max_examples=50)
def test_uma::processpackage_instantiation(instance):
    assert isinstance(instance, uma::ProcessPackage)

@given(instance=uma::ContentPackage_strategy)
@settings(max_examples=50)
def test_uma::contentpackage_instantiation(instance):
    assert isinstance(instance, uma::ContentPackage)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

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

@given(instance=uma::Artifact_strategy)
@settings(max_examples=50)
def test_uma::artifact_instantiation(instance):
    assert isinstance(instance, uma::Artifact)

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=MethodUnit_strategy)
@settings(max_examples=50)
def test_methodunit_instantiation(instance):
    assert isinstance(instance, MethodUnit)

@given(instance=uma::MethodConfiguration_strategy)
@settings(max_examples=50)
def test_uma::methodconfiguration_instantiation(instance):
    assert isinstance(instance, uma::MethodConfiguration)

@given(instance=uma::MethodLibrary_strategy)
@settings(max_examples=50)
def test_uma::methodlibrary_instantiation(instance):
    assert isinstance(instance, uma::MethodLibrary)

@given(instance=uma::ProcessComponent_strategy)
@settings(max_examples=50)
def test_uma::processcomponent_instantiation(instance):
    assert isinstance(instance, uma::ProcessComponent)

@given(instance=uma::MethodPlugin_strategy)
@settings(max_examples=50)
def test_uma::methodplugin_instantiation(instance):
    assert isinstance(instance, uma::MethodPlugin)

@given(instance=uma::MethodPlugin_strategy)
def test_uma::methodplugin_userChangeable_type(instance):
    assert isinstance(instance.userChangeable, str)


@given(instance=uma::MethodPlugin_strategy)
def test_uma::methodplugin_userChangeable_setter(instance):
    original = instance.userChangeable
    instance.userChangeable = original
    assert instance.userChangeable == original

@given(instance=WorkDefinition_strategy)
@settings(max_examples=50)
def test_workdefinition_instantiation(instance):
    assert isinstance(instance, WorkDefinition)

@given(instance=uma::StateMachine_strategy)
@settings(max_examples=50)
def test_uma::statemachine_instantiation(instance):
    assert isinstance(instance, uma::StateMachine)

@given(instance=uma::Step_strategy)
@settings(max_examples=50)
def test_uma::step_instantiation(instance):
    assert isinstance(instance, uma::Step)

@given(instance=uma::EstimationConsiderations_strategy)
@settings(max_examples=50)
def test_uma::estimationconsiderations_instantiation(instance):
    assert isinstance(instance, uma::EstimationConsiderations)

@given(instance=uma::ToolMentor_strategy)
@settings(max_examples=50)
def test_uma::toolmentor_instantiation(instance):
    assert isinstance(instance, uma::ToolMentor)

@given(instance=uma::Template_strategy)
@settings(max_examples=50)
def test_uma::template_instantiation(instance):
    assert isinstance(instance, uma::Template)

@given(instance=uma::Report_strategy)
@settings(max_examples=50)
def test_uma::report_instantiation(instance):
    assert isinstance(instance, uma::Report)

@given(instance=ContentElement_strategy)
@settings(max_examples=50)
def test_contentelement_instantiation(instance):
    assert isinstance(instance, ContentElement)

@given(instance=uma::ContentCategory_strategy)
@settings(max_examples=50)
def test_uma::contentcategory_instantiation(instance):
    assert isinstance(instance, uma::ContentCategory)

@given(instance=uma::Task_strategy)
@settings(max_examples=50)
def test_uma::task_instantiation(instance):
    assert isinstance(instance, uma::Task)

@given(instance=uma::Guidance_strategy)
@settings(max_examples=50)
def test_uma::guidance_instantiation(instance):
    assert isinstance(instance, uma::Guidance)

@given(instance=uma::WorkProduct_strategy)
@settings(max_examples=50)
def test_uma::workproduct_instantiation(instance):
    assert isinstance(instance, uma::WorkProduct)

@given(instance=uma::Role_strategy)
@settings(max_examples=50)
def test_uma::role_instantiation(instance):
    assert isinstance(instance, uma::Role)

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

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=uma::ReusableAsset_strategy)
@settings(max_examples=50)
def test_uma::reusableasset_instantiation(instance):
    assert isinstance(instance, uma::ReusableAsset)

@given(instance=uma::Example_strategy)
@settings(max_examples=50)
def test_uma::example_instantiation(instance):
    assert isinstance(instance, uma::Example)

@given(instance=uma::Guideline_strategy)
@settings(max_examples=50)
def test_uma::guideline_instantiation(instance):
    assert isinstance(instance, uma::Guideline)

@given(instance=uma::Checklist_strategy)
@settings(max_examples=50)
def test_uma::checklist_instantiation(instance):
    assert isinstance(instance, uma::Checklist)

@given(instance=uma::Concept_strategy)
@settings(max_examples=50)
def test_uma::concept_instantiation(instance):
    assert isinstance(instance, uma::Concept)

@given(instance=uma::SupportingMaterial_strategy)
@settings(max_examples=50)
def test_uma::supportingmaterial_instantiation(instance):
    assert isinstance(instance, uma::SupportingMaterial)

@given(instance=VariabilityElement_strategy)
@settings(max_examples=50)
def test_variabilityelement_instantiation(instance):
    assert isinstance(instance, VariabilityElement)

@given(instance=uma::Section_strategy)
@settings(max_examples=50)
def test_uma::section_instantiation(instance):
    assert isinstance(instance, uma::Section)

@given(instance=uma::Section_strategy)
def test_uma::section_sectionDescription_type(instance):
    assert isinstance(instance.sectionDescription, str)


@given(instance=uma::Section_strategy)
def test_uma::section_sectionDescription_setter(instance):
    original = instance.sectionDescription
    instance.sectionDescription = original
    assert instance.sectionDescription == original

@given(instance=uma::Section_strategy)
def test_uma::section_sectionName_type(instance):
    assert isinstance(instance.sectionName, str)


@given(instance=uma::Section_strategy)
def test_uma::section_sectionName_setter(instance):
    original = instance.sectionName
    instance.sectionName = original
    assert instance.sectionName == original

@given(instance=uma::Activity_strategy)
@settings(max_examples=50)
def test_uma::activity_instantiation(instance):
    assert isinstance(instance, uma::Activity)

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

@given(instance=MethodElement_strategy)
@settings(max_examples=50)
def test_methodelement_instantiation(instance):
    assert isinstance(instance, MethodElement)

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
def test_uma::describableelement_presentationName_type(instance):
    assert isinstance(instance.presentationName, str)


@given(instance=uma::DescribableElement_strategy)
def test_uma::describableelement_presentationName_setter(instance):
    original = instance.presentationName
    instance.presentationName = original
    assert instance.presentationName == original

@given(instance=uma::DescribableElement_strategy)
def test_uma::describableelement_nodeicon_type(instance):
    assert isinstance(instance.nodeicon, str)


@given(instance=uma::DescribableElement_strategy)
def test_uma::describableelement_nodeicon_setter(instance):
    original = instance.nodeicon
    instance.nodeicon = original
    assert instance.nodeicon == original

@given(instance=uma::WorkDefinition_strategy)
@settings(max_examples=50)
def test_uma::workdefinition_instantiation(instance):
    assert isinstance(instance, uma::WorkDefinition)

@given(instance=uma::MethodUnit_strategy)
@settings(max_examples=50)
def test_uma::methodunit_instantiation(instance):
    assert isinstance(instance, uma::MethodUnit)

@given(instance=uma::MethodUnit_strategy)
def test_uma::methodunit_changeDescription_type(instance):
    assert isinstance(instance.changeDescription, str)


@given(instance=uma::MethodUnit_strategy)
def test_uma::methodunit_changeDescription_setter(instance):
    original = instance.changeDescription
    instance.changeDescription = original
    assert instance.changeDescription == original

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
def test_uma::methodunit_authors_type(instance):
    assert isinstance(instance.authors, str)


@given(instance=uma::MethodUnit_strategy)
def test_uma::methodunit_authors_setter(instance):
    original = instance.authors
    instance.authors = original
    assert instance.authors == original

@given(instance=uma::VariabilityElement_strategy)
@settings(max_examples=50)
def test_uma::variabilityelement_instantiation(instance):
    assert isinstance(instance, uma::VariabilityElement)

@given(instance=uma::VariabilityElement_strategy)
def test_uma::variabilityelement_variabilityType_type(instance):
    assert isinstance(instance.variabilityType, str)


@given(instance=uma::VariabilityElement_strategy)
def test_uma::variabilityelement_variabilityType_setter(instance):
    original = instance.variabilityType
    instance.variabilityType = original
    assert instance.variabilityType == original

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

@given(instance=uma::DiagramElement_strategy)
@settings(max_examples=50)
def test_uma::diagramelement_instantiation(instance):
    assert isinstance(instance, uma::DiagramElement)

@given(instance=uma::DiagramElement_strategy)
def test_uma::diagramelement_isVisible_type(instance):
    assert isinstance(instance.isVisible, str)


@given(instance=uma::DiagramElement_strategy)
def test_uma::diagramelement_isVisible_setter(instance):
    original = instance.isVisible
    instance.isVisible = original
    assert instance.isVisible == original

@given(instance=uma::Constraint_strategy)
@settings(max_examples=50)
def test_uma::constraint_instantiation(instance):
    assert isinstance(instance, uma::Constraint)

@given(instance=uma::Constraint_strategy)
def test_uma::constraint_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=uma::Constraint_strategy)
def test_uma::constraint_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=uma::Namespace_strategy)
@settings(max_examples=50)
def test_uma::namespace_instantiation(instance):
    assert isinstance(instance, uma::Namespace)

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

@given(instance=uma::Element_strategy)
@settings(max_examples=50)
def test_uma::element_instantiation(instance):
    assert isinstance(instance, uma::Element)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

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
def test_uma::methodelement_briefDescription_type(instance):
    assert isinstance(instance.briefDescription, str)


@given(instance=uma::MethodElement_strategy)
def test_uma::methodelement_briefDescription_setter(instance):
    original = instance.briefDescription
    instance.briefDescription = original
    assert instance.briefDescription == original

@given(instance=uma::MethodElement_strategy)
def test_uma::methodelement_guid_type(instance):
    assert isinstance(instance.guid, str)


@given(instance=uma::MethodElement_strategy)
def test_uma::methodelement_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original

@given(instance=uma::MethodElement_strategy)
def test_uma::methodelement_suppressed_type(instance):
    assert isinstance(instance.suppressed, str)


@given(instance=uma::MethodElement_strategy)
def test_uma::methodelement_suppressed_setter(instance):
    original = instance.suppressed
    instance.suppressed = original
    assert instance.suppressed == original

@given(instance=uma::Package_strategy)
@settings(max_examples=50)
def test_uma::package_instantiation(instance):
    assert isinstance(instance, uma::Package)

@given(instance=uma::Type_strategy)
@settings(max_examples=50)
def test_uma::type_instantiation(instance):
    assert isinstance(instance, uma::Type)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=uma::Classifier_strategy)
@settings(max_examples=50)
def test_uma::classifier_instantiation(instance):
    assert isinstance(instance, uma::Classifier)

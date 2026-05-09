import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    uma::spem::RoleDefinition,
    Node,
    spem::activity::EndNode,
    spem::activity::DecisionNode,
    spem::activity::ForkNode,
    spem::activity::JoinNode,
    spem::activity::StartNode,
    activity::spem::BreakdownElement,
    Edge,
    uma::spem::MethodContentElement,
    uma::spem::Activity,
    Practice,
    uma::spem::WorkProductDefinition,
    Concept,
    spem::uma::Whitepaper,
    SupportingMaterial,
    uma::spem::WorkProductPortConnector,
    CapabilityPattern,
    Activity,
    spem::uma::Phase,
    spem::uma::Iteration,
    spem::uma::Process,
    uma::spem::MethodPlugin,
    uma::spem::MethodLibrary,
    uma::spem::WorkProductUse,
    uma::spem::MethodConfiguration,
    spem::uma::Root,
    Category,
    spem::uma::Domain,
    spem::uma::DisciplineGrouping,
    spem::uma::CustomCategory,
    MethodContentPackage,
    spem::uma::WorkProductKindPackage,
    spem::uma::TaskDefinitionPackage,
    spem::uma::QualificationPackage,
    spem::uma::ToolDefinitionPackage,
    spem::uma::GuidancePackage,
    spem::uma::RoleDefinitionPackage,
    spem::uma::DomainPackage,
    spem::uma::WorkProductDefinitionPackage,
    spem::uma::RoleSetPackage,
    spem::uma::ConfigurationPackage,
    spem::uma::DisciplinePackage,
    spem::uma::CategoryPackage,
    Guidance,
    spem::uma::Example,
    spem::uma::Concept,
    spem::uma::EstimatingConsideration,
    spem::uma::Template,
    spem::uma::TermDefinition,
    spem::uma::Guideline,
    spem::uma::Roadmap,
    spem::uma::ToolMentor,
    spem::uma::ReusableAsset,
    spem::uma::Report,
    spem::uma::Practice,
    spem::uma::SupportingMaterial,
    spem::uma::Checklist,
    uma::spem::TaskDefinition,
    Process,
    spem::uma::ProcessPlanningTemplate,
    spem::uma::DeliveryProcess,
    spem::uma::CapabilityPattern,
    spem::uma::Discipline,
    Artifact,
    WorkProductUse,
    spem::uma::Deliverable,
    spem::uma::Outcome,
    spem::uma::Artifact,
    MethodLibraryPackageableElement,
    spem::MethodPluginPackageableElement,
    spem::MethodLibraryPackageableElement,
    spem::MethodLibrary,
    spem::MethodPlugin,
    ProcessPackage,
    spem::uma::CapabilityPatternPackage,
    spem::uma::ProcessComponentPackage,
    spem::uma::DeliveryProcessPackage,
    spem::ProcessComponent,
    spem::VariabilityElement,
    RoleUse,
    spem::CompositeRole,
    Kind,
    MethodPluginPackageableElement,
    spem::ProcessPackageableElement,
    spem::MethodContentPackageableElement,
    MethodContentPackageableElement,
    spem::MethodContentPackage,
    MethodContentElement,
    spem::Default::ResponsibilityAssignment,
    spem::MethodContentKind,
    spem::WorkProductDefinition,
    spem::uma::RoleSet,
    spem::Default::TaskDefinitionPerformer,
    spem::WorkProductDefinitionRelationship,
    spem::uma::WorkProductKind,
    spem::ToolDefinition,
    spem::Category,
    spem::Guidance,
    ProcessPackageableElement,
    spem::ProcessPackage,
    DescribableElement,
    spem::Metric,
    spem::ProcessElement,
    WorkDefinitionParameter,
    spem::Default::TaskDefinitionParameter,
    VariabilityElement,
    spem::MethodContentElement,
    WorkBreakdownElement,
    spem::Milestone,
    WorkDefinition,
    spem::TaskDefinition,
    spem::Step,
    spem::Activity,
    spem::Qualification,
    spem::RoleDefinition,
    MethodContentUse,
    spem::WorkProductUse,
    spem::ProcessComponentUse,
    spem::TaskUse,
    spem::RoleUse,
    WorkDefinitionPerformer,
    spem::MethodConfiguration,
    spem::WorkDefinitionParameter,
    BreakdownElement,
    spem::WorkProductUseRelationship,
    spem::activity::Edge,
    spem::ProcessPerformer,
    spem::WorkSequence,
    spem::TeamProfile,
    spem::MethodContentUse,
    spem::ProcessResponsibilityAssignment,
    spem::ProcessParameter,
    spem::activity::Node,
    spem::WorkBreakdownElement,
    ProcessElement,
    spem::WorkProductPort,
    spem::WorkProductPortConnector,
    spem::PlanningData,
    spem::ProcessKind,
    spem::BreakdownElement,
    spem::WorkDefinition,
    spem::WorkDefinitionPerformer,
    ExtensibleElement,
    spem::DescribableElement,
    spem::Kind,
    spem::ExtensibleElement,
    ParameterDirectionKind,
    WorkSequenceKind,
    OptionalityKind,
    ContractKind,
    ActivityUseKind,
    RiskLevel,
    ExpertiseLevel,
    WorkProductRelationshipKind,
    EstimatingTechnique,
    VariabilityType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uma::spem::roledefinition_is_not_abstract():
    assert not inspect.isabstract(uma::spem::RoleDefinition)


def test_uma::spem::roledefinition_constructor_exists():
    assert callable(uma::spem::RoleDefinition.__init__)


def test_uma::spem::roledefinition_constructor_args():
    sig = inspect.signature(uma::spem::RoleDefinition.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_spem::activity::endnode_is_not_abstract():
    assert not inspect.isabstract(spem::activity::EndNode)


def test_spem::activity::endnode_constructor_exists():
    assert callable(spem::activity::EndNode.__init__)


def test_spem::activity::endnode_constructor_args():
    sig = inspect.signature(spem::activity::EndNode.__init__)
    params = list(sig.parameters.keys())



def test_spem::activity::decisionnode_is_not_abstract():
    assert not inspect.isabstract(spem::activity::DecisionNode)


def test_spem::activity::decisionnode_constructor_exists():
    assert callable(spem::activity::DecisionNode.__init__)


def test_spem::activity::decisionnode_constructor_args():
    sig = inspect.signature(spem::activity::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_spem::activity::forknode_is_not_abstract():
    assert not inspect.isabstract(spem::activity::ForkNode)


def test_spem::activity::forknode_constructor_exists():
    assert callable(spem::activity::ForkNode.__init__)


def test_spem::activity::forknode_constructor_args():
    sig = inspect.signature(spem::activity::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_spem::activity::joinnode_is_not_abstract():
    assert not inspect.isabstract(spem::activity::JoinNode)


def test_spem::activity::joinnode_constructor_exists():
    assert callable(spem::activity::JoinNode.__init__)


def test_spem::activity::joinnode_constructor_args():
    sig = inspect.signature(spem::activity::JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_spem::activity::startnode_is_not_abstract():
    assert not inspect.isabstract(spem::activity::StartNode)


def test_spem::activity::startnode_constructor_exists():
    assert callable(spem::activity::StartNode.__init__)


def test_spem::activity::startnode_constructor_args():
    sig = inspect.signature(spem::activity::StartNode.__init__)
    params = list(sig.parameters.keys())



def test_activity::spem::breakdownelement_is_not_abstract():
    assert not inspect.isabstract(activity::spem::BreakdownElement)


def test_activity::spem::breakdownelement_constructor_exists():
    assert callable(activity::spem::BreakdownElement.__init__)


def test_activity::spem::breakdownelement_constructor_args():
    sig = inspect.signature(activity::spem::BreakdownElement.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_uma::spem::methodcontentelement_is_not_abstract():
    assert not inspect.isabstract(uma::spem::MethodContentElement)


def test_uma::spem::methodcontentelement_constructor_exists():
    assert callable(uma::spem::MethodContentElement.__init__)


def test_uma::spem::methodcontentelement_constructor_args():
    sig = inspect.signature(uma::spem::MethodContentElement.__init__)
    params = list(sig.parameters.keys())



def test_uma::spem::activity_is_not_abstract():
    assert not inspect.isabstract(uma::spem::Activity)


def test_uma::spem::activity_constructor_exists():
    assert callable(uma::spem::Activity.__init__)


def test_uma::spem::activity_constructor_args():
    sig = inspect.signature(uma::spem::Activity.__init__)
    params = list(sig.parameters.keys())



def test_practice_is_not_abstract():
    assert not inspect.isabstract(Practice)


def test_practice_constructor_exists():
    assert callable(Practice.__init__)


def test_practice_constructor_args():
    sig = inspect.signature(Practice.__init__)
    params = list(sig.parameters.keys())



def test_uma::spem::workproductdefinition_is_not_abstract():
    assert not inspect.isabstract(uma::spem::WorkProductDefinition)


def test_uma::spem::workproductdefinition_constructor_exists():
    assert callable(uma::spem::WorkProductDefinition.__init__)


def test_uma::spem::workproductdefinition_constructor_args():
    sig = inspect.signature(uma::spem::WorkProductDefinition.__init__)
    params = list(sig.parameters.keys())



def test_concept_is_not_abstract():
    assert not inspect.isabstract(Concept)


def test_concept_constructor_exists():
    assert callable(Concept.__init__)


def test_concept_constructor_args():
    sig = inspect.signature(Concept.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::whitepaper_is_not_abstract():
    assert not inspect.isabstract(spem::uma::Whitepaper)


def test_spem::uma::whitepaper_constructor_exists():
    assert callable(spem::uma::Whitepaper.__init__)


def test_spem::uma::whitepaper_constructor_args():
    sig = inspect.signature(spem::uma::Whitepaper.__init__)
    params = list(sig.parameters.keys())



def test_supportingmaterial_is_not_abstract():
    assert not inspect.isabstract(SupportingMaterial)


def test_supportingmaterial_constructor_exists():
    assert callable(SupportingMaterial.__init__)


def test_supportingmaterial_constructor_args():
    sig = inspect.signature(SupportingMaterial.__init__)
    params = list(sig.parameters.keys())



def test_uma::spem::workproductportconnector_is_not_abstract():
    assert not inspect.isabstract(uma::spem::WorkProductPortConnector)


def test_uma::spem::workproductportconnector_constructor_exists():
    assert callable(uma::spem::WorkProductPortConnector.__init__)


def test_uma::spem::workproductportconnector_constructor_args():
    sig = inspect.signature(uma::spem::WorkProductPortConnector.__init__)
    params = list(sig.parameters.keys())



def test_capabilitypattern_is_not_abstract():
    assert not inspect.isabstract(CapabilityPattern)


def test_capabilitypattern_constructor_exists():
    assert callable(CapabilityPattern.__init__)


def test_capabilitypattern_constructor_args():
    sig = inspect.signature(CapabilityPattern.__init__)
    params = list(sig.parameters.keys())



def test_activity_is_not_abstract():
    assert not inspect.isabstract(Activity)


def test_activity_constructor_exists():
    assert callable(Activity.__init__)


def test_activity_constructor_args():
    sig = inspect.signature(Activity.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::phase_is_not_abstract():
    assert not inspect.isabstract(spem::uma::Phase)


def test_spem::uma::phase_constructor_exists():
    assert callable(spem::uma::Phase.__init__)


def test_spem::uma::phase_constructor_args():
    sig = inspect.signature(spem::uma::Phase.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::iteration_is_not_abstract():
    assert not inspect.isabstract(spem::uma::Iteration)


def test_spem::uma::iteration_constructor_exists():
    assert callable(spem::uma::Iteration.__init__)


def test_spem::uma::iteration_constructor_args():
    sig = inspect.signature(spem::uma::Iteration.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::process_is_not_abstract():
    assert not inspect.isabstract(spem::uma::Process)


def test_spem::uma::process_constructor_exists():
    assert callable(spem::uma::Process.__init__)


def test_spem::uma::process_constructor_args():
    sig = inspect.signature(spem::uma::Process.__init__)
    params = list(sig.parameters.keys())
    assert "usageNote" in params, "Missing parameter 'usageNote'"
    assert "scope" in params, "Missing parameter 'scope'"

def test_spem::uma::process_has_usageNote():
    assert hasattr(spem::uma::Process, "usageNote")
    descriptor = None
    for klass in spem::uma::Process.__mro__:
        if "usageNote" in klass.__dict__:
            descriptor = klass.__dict__["usageNote"]
            break
    assert isinstance(descriptor, property)

def test_spem::uma::process_has_scope():
    assert hasattr(spem::uma::Process, "scope")
    descriptor = None
    for klass in spem::uma::Process.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_uma::spem::methodplugin_is_not_abstract():
    assert not inspect.isabstract(uma::spem::MethodPlugin)


def test_uma::spem::methodplugin_constructor_exists():
    assert callable(uma::spem::MethodPlugin.__init__)


def test_uma::spem::methodplugin_constructor_args():
    sig = inspect.signature(uma::spem::MethodPlugin.__init__)
    params = list(sig.parameters.keys())



def test_uma::spem::methodlibrary_is_not_abstract():
    assert not inspect.isabstract(uma::spem::MethodLibrary)


def test_uma::spem::methodlibrary_constructor_exists():
    assert callable(uma::spem::MethodLibrary.__init__)


def test_uma::spem::methodlibrary_constructor_args():
    sig = inspect.signature(uma::spem::MethodLibrary.__init__)
    params = list(sig.parameters.keys())



def test_uma::spem::workproductuse_is_not_abstract():
    assert not inspect.isabstract(uma::spem::WorkProductUse)


def test_uma::spem::workproductuse_constructor_exists():
    assert callable(uma::spem::WorkProductUse.__init__)


def test_uma::spem::workproductuse_constructor_args():
    sig = inspect.signature(uma::spem::WorkProductUse.__init__)
    params = list(sig.parameters.keys())



def test_uma::spem::methodconfiguration_is_not_abstract():
    assert not inspect.isabstract(uma::spem::MethodConfiguration)


def test_uma::spem::methodconfiguration_constructor_exists():
    assert callable(uma::spem::MethodConfiguration.__init__)


def test_uma::spem::methodconfiguration_constructor_args():
    sig = inspect.signature(uma::spem::MethodConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::root_is_not_abstract():
    assert not inspect.isabstract(spem::uma::Root)


def test_spem::uma::root_constructor_exists():
    assert callable(spem::uma::Root.__init__)


def test_spem::uma::root_constructor_args():
    sig = inspect.signature(spem::uma::Root.__init__)
    params = list(sig.parameters.keys())



def test_category_is_not_abstract():
    assert not inspect.isabstract(Category)


def test_category_constructor_exists():
    assert callable(Category.__init__)


def test_category_constructor_args():
    sig = inspect.signature(Category.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::domain_is_not_abstract():
    assert not inspect.isabstract(spem::uma::Domain)


def test_spem::uma::domain_constructor_exists():
    assert callable(spem::uma::Domain.__init__)


def test_spem::uma::domain_constructor_args():
    sig = inspect.signature(spem::uma::Domain.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::disciplinegrouping_is_not_abstract():
    assert not inspect.isabstract(spem::uma::DisciplineGrouping)


def test_spem::uma::disciplinegrouping_constructor_exists():
    assert callable(spem::uma::DisciplineGrouping.__init__)


def test_spem::uma::disciplinegrouping_constructor_args():
    sig = inspect.signature(spem::uma::DisciplineGrouping.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::customcategory_is_not_abstract():
    assert not inspect.isabstract(spem::uma::CustomCategory)


def test_spem::uma::customcategory_constructor_exists():
    assert callable(spem::uma::CustomCategory.__init__)


def test_spem::uma::customcategory_constructor_args():
    sig = inspect.signature(spem::uma::CustomCategory.__init__)
    params = list(sig.parameters.keys())



def test_methodcontentpackage_is_not_abstract():
    assert not inspect.isabstract(MethodContentPackage)


def test_methodcontentpackage_constructor_exists():
    assert callable(MethodContentPackage.__init__)


def test_methodcontentpackage_constructor_args():
    sig = inspect.signature(MethodContentPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::workproductkindpackage_is_not_abstract():
    assert not inspect.isabstract(spem::uma::WorkProductKindPackage)


def test_spem::uma::workproductkindpackage_constructor_exists():
    assert callable(spem::uma::WorkProductKindPackage.__init__)


def test_spem::uma::workproductkindpackage_constructor_args():
    sig = inspect.signature(spem::uma::WorkProductKindPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::taskdefinitionpackage_is_not_abstract():
    assert not inspect.isabstract(spem::uma::TaskDefinitionPackage)


def test_spem::uma::taskdefinitionpackage_constructor_exists():
    assert callable(spem::uma::TaskDefinitionPackage.__init__)


def test_spem::uma::taskdefinitionpackage_constructor_args():
    sig = inspect.signature(spem::uma::TaskDefinitionPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::qualificationpackage_is_not_abstract():
    assert not inspect.isabstract(spem::uma::QualificationPackage)


def test_spem::uma::qualificationpackage_constructor_exists():
    assert callable(spem::uma::QualificationPackage.__init__)


def test_spem::uma::qualificationpackage_constructor_args():
    sig = inspect.signature(spem::uma::QualificationPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::tooldefinitionpackage_is_not_abstract():
    assert not inspect.isabstract(spem::uma::ToolDefinitionPackage)


def test_spem::uma::tooldefinitionpackage_constructor_exists():
    assert callable(spem::uma::ToolDefinitionPackage.__init__)


def test_spem::uma::tooldefinitionpackage_constructor_args():
    sig = inspect.signature(spem::uma::ToolDefinitionPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::guidancepackage_is_not_abstract():
    assert not inspect.isabstract(spem::uma::GuidancePackage)


def test_spem::uma::guidancepackage_constructor_exists():
    assert callable(spem::uma::GuidancePackage.__init__)


def test_spem::uma::guidancepackage_constructor_args():
    sig = inspect.signature(spem::uma::GuidancePackage.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::roledefinitionpackage_is_not_abstract():
    assert not inspect.isabstract(spem::uma::RoleDefinitionPackage)


def test_spem::uma::roledefinitionpackage_constructor_exists():
    assert callable(spem::uma::RoleDefinitionPackage.__init__)


def test_spem::uma::roledefinitionpackage_constructor_args():
    sig = inspect.signature(spem::uma::RoleDefinitionPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::domainpackage_is_not_abstract():
    assert not inspect.isabstract(spem::uma::DomainPackage)


def test_spem::uma::domainpackage_constructor_exists():
    assert callable(spem::uma::DomainPackage.__init__)


def test_spem::uma::domainpackage_constructor_args():
    sig = inspect.signature(spem::uma::DomainPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::workproductdefinitionpackage_is_not_abstract():
    assert not inspect.isabstract(spem::uma::WorkProductDefinitionPackage)


def test_spem::uma::workproductdefinitionpackage_constructor_exists():
    assert callable(spem::uma::WorkProductDefinitionPackage.__init__)


def test_spem::uma::workproductdefinitionpackage_constructor_args():
    sig = inspect.signature(spem::uma::WorkProductDefinitionPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::rolesetpackage_is_not_abstract():
    assert not inspect.isabstract(spem::uma::RoleSetPackage)


def test_spem::uma::rolesetpackage_constructor_exists():
    assert callable(spem::uma::RoleSetPackage.__init__)


def test_spem::uma::rolesetpackage_constructor_args():
    sig = inspect.signature(spem::uma::RoleSetPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::configurationpackage_is_not_abstract():
    assert not inspect.isabstract(spem::uma::ConfigurationPackage)


def test_spem::uma::configurationpackage_constructor_exists():
    assert callable(spem::uma::ConfigurationPackage.__init__)


def test_spem::uma::configurationpackage_constructor_args():
    sig = inspect.signature(spem::uma::ConfigurationPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::disciplinepackage_is_not_abstract():
    assert not inspect.isabstract(spem::uma::DisciplinePackage)


def test_spem::uma::disciplinepackage_constructor_exists():
    assert callable(spem::uma::DisciplinePackage.__init__)


def test_spem::uma::disciplinepackage_constructor_args():
    sig = inspect.signature(spem::uma::DisciplinePackage.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::categorypackage_is_not_abstract():
    assert not inspect.isabstract(spem::uma::CategoryPackage)


def test_spem::uma::categorypackage_constructor_exists():
    assert callable(spem::uma::CategoryPackage.__init__)


def test_spem::uma::categorypackage_constructor_args():
    sig = inspect.signature(spem::uma::CategoryPackage.__init__)
    params = list(sig.parameters.keys())



def test_guidance_is_not_abstract():
    assert not inspect.isabstract(Guidance)


def test_guidance_constructor_exists():
    assert callable(Guidance.__init__)


def test_guidance_constructor_args():
    sig = inspect.signature(Guidance.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::example_is_not_abstract():
    assert not inspect.isabstract(spem::uma::Example)


def test_spem::uma::example_constructor_exists():
    assert callable(spem::uma::Example.__init__)


def test_spem::uma::example_constructor_args():
    sig = inspect.signature(spem::uma::Example.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::concept_is_not_abstract():
    assert not inspect.isabstract(spem::uma::Concept)


def test_spem::uma::concept_constructor_exists():
    assert callable(spem::uma::Concept.__init__)


def test_spem::uma::concept_constructor_args():
    sig = inspect.signature(spem::uma::Concept.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::estimatingconsideration_is_not_abstract():
    assert not inspect.isabstract(spem::uma::EstimatingConsideration)


def test_spem::uma::estimatingconsideration_constructor_exists():
    assert callable(spem::uma::EstimatingConsideration.__init__)


def test_spem::uma::estimatingconsideration_constructor_args():
    sig = inspect.signature(spem::uma::EstimatingConsideration.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::template_is_not_abstract():
    assert not inspect.isabstract(spem::uma::Template)


def test_spem::uma::template_constructor_exists():
    assert callable(spem::uma::Template.__init__)


def test_spem::uma::template_constructor_args():
    sig = inspect.signature(spem::uma::Template.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::termdefinition_is_not_abstract():
    assert not inspect.isabstract(spem::uma::TermDefinition)


def test_spem::uma::termdefinition_constructor_exists():
    assert callable(spem::uma::TermDefinition.__init__)


def test_spem::uma::termdefinition_constructor_args():
    sig = inspect.signature(spem::uma::TermDefinition.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::guideline_is_not_abstract():
    assert not inspect.isabstract(spem::uma::Guideline)


def test_spem::uma::guideline_constructor_exists():
    assert callable(spem::uma::Guideline.__init__)


def test_spem::uma::guideline_constructor_args():
    sig = inspect.signature(spem::uma::Guideline.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::roadmap_is_not_abstract():
    assert not inspect.isabstract(spem::uma::Roadmap)


def test_spem::uma::roadmap_constructor_exists():
    assert callable(spem::uma::Roadmap.__init__)


def test_spem::uma::roadmap_constructor_args():
    sig = inspect.signature(spem::uma::Roadmap.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::toolmentor_is_not_abstract():
    assert not inspect.isabstract(spem::uma::ToolMentor)


def test_spem::uma::toolmentor_constructor_exists():
    assert callable(spem::uma::ToolMentor.__init__)


def test_spem::uma::toolmentor_constructor_args():
    sig = inspect.signature(spem::uma::ToolMentor.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::reusableasset_is_not_abstract():
    assert not inspect.isabstract(spem::uma::ReusableAsset)


def test_spem::uma::reusableasset_constructor_exists():
    assert callable(spem::uma::ReusableAsset.__init__)


def test_spem::uma::reusableasset_constructor_args():
    sig = inspect.signature(spem::uma::ReusableAsset.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::report_is_not_abstract():
    assert not inspect.isabstract(spem::uma::Report)


def test_spem::uma::report_constructor_exists():
    assert callable(spem::uma::Report.__init__)


def test_spem::uma::report_constructor_args():
    sig = inspect.signature(spem::uma::Report.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::practice_is_not_abstract():
    assert not inspect.isabstract(spem::uma::Practice)


def test_spem::uma::practice_constructor_exists():
    assert callable(spem::uma::Practice.__init__)


def test_spem::uma::practice_constructor_args():
    sig = inspect.signature(spem::uma::Practice.__init__)
    params = list(sig.parameters.keys())
    assert "problem" in params, "Missing parameter 'problem'"
    assert "background" in params, "Missing parameter 'background'"
    assert "goal" in params, "Missing parameter 'goal'"
    assert "levelOfAdoption" in params, "Missing parameter 'levelOfAdoption'"
    assert "application" in params, "Missing parameter 'application'"
    assert "additionalInfo" in params, "Missing parameter 'additionalInfo'"

def test_spem::uma::practice_has_problem():
    assert hasattr(spem::uma::Practice, "problem")
    descriptor = None
    for klass in spem::uma::Practice.__mro__:
        if "problem" in klass.__dict__:
            descriptor = klass.__dict__["problem"]
            break
    assert isinstance(descriptor, property)

def test_spem::uma::practice_has_background():
    assert hasattr(spem::uma::Practice, "background")
    descriptor = None
    for klass in spem::uma::Practice.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_spem::uma::practice_has_goal():
    assert hasattr(spem::uma::Practice, "goal")
    descriptor = None
    for klass in spem::uma::Practice.__mro__:
        if "goal" in klass.__dict__:
            descriptor = klass.__dict__["goal"]
            break
    assert isinstance(descriptor, property)

def test_spem::uma::practice_has_levelOfAdoption():
    assert hasattr(spem::uma::Practice, "levelOfAdoption")
    descriptor = None
    for klass in spem::uma::Practice.__mro__:
        if "levelOfAdoption" in klass.__dict__:
            descriptor = klass.__dict__["levelOfAdoption"]
            break
    assert isinstance(descriptor, property)

def test_spem::uma::practice_has_application():
    assert hasattr(spem::uma::Practice, "application")
    descriptor = None
    for klass in spem::uma::Practice.__mro__:
        if "application" in klass.__dict__:
            descriptor = klass.__dict__["application"]
            break
    assert isinstance(descriptor, property)

def test_spem::uma::practice_has_additionalInfo():
    assert hasattr(spem::uma::Practice, "additionalInfo")
    descriptor = None
    for klass in spem::uma::Practice.__mro__:
        if "additionalInfo" in klass.__dict__:
            descriptor = klass.__dict__["additionalInfo"]
            break
    assert isinstance(descriptor, property)



def test_spem::uma::supportingmaterial_is_not_abstract():
    assert not inspect.isabstract(spem::uma::SupportingMaterial)


def test_spem::uma::supportingmaterial_constructor_exists():
    assert callable(spem::uma::SupportingMaterial.__init__)


def test_spem::uma::supportingmaterial_constructor_args():
    sig = inspect.signature(spem::uma::SupportingMaterial.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::checklist_is_not_abstract():
    assert not inspect.isabstract(spem::uma::Checklist)


def test_spem::uma::checklist_constructor_exists():
    assert callable(spem::uma::Checklist.__init__)


def test_spem::uma::checklist_constructor_args():
    sig = inspect.signature(spem::uma::Checklist.__init__)
    params = list(sig.parameters.keys())



def test_uma::spem::taskdefinition_is_not_abstract():
    assert not inspect.isabstract(uma::spem::TaskDefinition)


def test_uma::spem::taskdefinition_constructor_exists():
    assert callable(uma::spem::TaskDefinition.__init__)


def test_uma::spem::taskdefinition_constructor_args():
    sig = inspect.signature(uma::spem::TaskDefinition.__init__)
    params = list(sig.parameters.keys())



def test_process_is_not_abstract():
    assert not inspect.isabstract(Process)


def test_process_constructor_exists():
    assert callable(Process.__init__)


def test_process_constructor_args():
    sig = inspect.signature(Process.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::processplanningtemplate_is_not_abstract():
    assert not inspect.isabstract(spem::uma::ProcessPlanningTemplate)


def test_spem::uma::processplanningtemplate_constructor_exists():
    assert callable(spem::uma::ProcessPlanningTemplate.__init__)


def test_spem::uma::processplanningtemplate_constructor_args():
    sig = inspect.signature(spem::uma::ProcessPlanningTemplate.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::deliveryprocess_is_not_abstract():
    assert not inspect.isabstract(spem::uma::DeliveryProcess)


def test_spem::uma::deliveryprocess_constructor_exists():
    assert callable(spem::uma::DeliveryProcess.__init__)


def test_spem::uma::deliveryprocess_constructor_args():
    sig = inspect.signature(spem::uma::DeliveryProcess.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"
    assert "estimatingTechnique" in params, "Missing parameter 'estimatingTechnique'"
    assert "typeOfContract" in params, "Missing parameter 'typeOfContract'"
    assert "projectMemberExpertise" in params, "Missing parameter 'projectMemberExpertise'"
    assert "riskLevel" in params, "Missing parameter 'riskLevel'"
    assert "projectCharacteristics" in params, "Missing parameter 'projectCharacteristics'"

def test_spem::uma::deliveryprocess_has_scale():
    assert hasattr(spem::uma::DeliveryProcess, "scale")
    descriptor = None
    for klass in spem::uma::DeliveryProcess.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_spem::uma::deliveryprocess_has_estimatingTechnique():
    assert hasattr(spem::uma::DeliveryProcess, "estimatingTechnique")
    descriptor = None
    for klass in spem::uma::DeliveryProcess.__mro__:
        if "estimatingTechnique" in klass.__dict__:
            descriptor = klass.__dict__["estimatingTechnique"]
            break
    assert isinstance(descriptor, property)

def test_spem::uma::deliveryprocess_has_typeOfContract():
    assert hasattr(spem::uma::DeliveryProcess, "typeOfContract")
    descriptor = None
    for klass in spem::uma::DeliveryProcess.__mro__:
        if "typeOfContract" in klass.__dict__:
            descriptor = klass.__dict__["typeOfContract"]
            break
    assert isinstance(descriptor, property)

def test_spem::uma::deliveryprocess_has_projectMemberExpertise():
    assert hasattr(spem::uma::DeliveryProcess, "projectMemberExpertise")
    descriptor = None
    for klass in spem::uma::DeliveryProcess.__mro__:
        if "projectMemberExpertise" in klass.__dict__:
            descriptor = klass.__dict__["projectMemberExpertise"]
            break
    assert isinstance(descriptor, property)

def test_spem::uma::deliveryprocess_has_riskLevel():
    assert hasattr(spem::uma::DeliveryProcess, "riskLevel")
    descriptor = None
    for klass in spem::uma::DeliveryProcess.__mro__:
        if "riskLevel" in klass.__dict__:
            descriptor = klass.__dict__["riskLevel"]
            break
    assert isinstance(descriptor, property)

def test_spem::uma::deliveryprocess_has_projectCharacteristics():
    assert hasattr(spem::uma::DeliveryProcess, "projectCharacteristics")
    descriptor = None
    for klass in spem::uma::DeliveryProcess.__mro__:
        if "projectCharacteristics" in klass.__dict__:
            descriptor = klass.__dict__["projectCharacteristics"]
            break
    assert isinstance(descriptor, property)



def test_spem::uma::capabilitypattern_is_not_abstract():
    assert not inspect.isabstract(spem::uma::CapabilityPattern)


def test_spem::uma::capabilitypattern_constructor_exists():
    assert callable(spem::uma::CapabilityPattern.__init__)


def test_spem::uma::capabilitypattern_constructor_args():
    sig = inspect.signature(spem::uma::CapabilityPattern.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::discipline_is_not_abstract():
    assert not inspect.isabstract(spem::uma::Discipline)


def test_spem::uma::discipline_constructor_exists():
    assert callable(spem::uma::Discipline.__init__)


def test_spem::uma::discipline_constructor_args():
    sig = inspect.signature(spem::uma::Discipline.__init__)
    params = list(sig.parameters.keys())



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_workproductuse_is_not_abstract():
    assert not inspect.isabstract(WorkProductUse)


def test_workproductuse_constructor_exists():
    assert callable(WorkProductUse.__init__)


def test_workproductuse_constructor_args():
    sig = inspect.signature(WorkProductUse.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::deliverable_is_not_abstract():
    assert not inspect.isabstract(spem::uma::Deliverable)


def test_spem::uma::deliverable_constructor_exists():
    assert callable(spem::uma::Deliverable.__init__)


def test_spem::uma::deliverable_constructor_args():
    sig = inspect.signature(spem::uma::Deliverable.__init__)
    params = list(sig.parameters.keys())
    assert "externalDescription" in params, "Missing parameter 'externalDescription'"
    assert "packagingGuidance" in params, "Missing parameter 'packagingGuidance'"

def test_spem::uma::deliverable_has_externalDescription():
    assert hasattr(spem::uma::Deliverable, "externalDescription")
    descriptor = None
    for klass in spem::uma::Deliverable.__mro__:
        if "externalDescription" in klass.__dict__:
            descriptor = klass.__dict__["externalDescription"]
            break
    assert isinstance(descriptor, property)

def test_spem::uma::deliverable_has_packagingGuidance():
    assert hasattr(spem::uma::Deliverable, "packagingGuidance")
    descriptor = None
    for klass in spem::uma::Deliverable.__mro__:
        if "packagingGuidance" in klass.__dict__:
            descriptor = klass.__dict__["packagingGuidance"]
            break
    assert isinstance(descriptor, property)



def test_spem::uma::outcome_is_not_abstract():
    assert not inspect.isabstract(spem::uma::Outcome)


def test_spem::uma::outcome_constructor_exists():
    assert callable(spem::uma::Outcome.__init__)


def test_spem::uma::outcome_constructor_args():
    sig = inspect.signature(spem::uma::Outcome.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::artifact_is_not_abstract():
    assert not inspect.isabstract(spem::uma::Artifact)


def test_spem::uma::artifact_constructor_exists():
    assert callable(spem::uma::Artifact.__init__)


def test_spem::uma::artifact_constructor_args():
    sig = inspect.signature(spem::uma::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_methodlibrarypackageableelement_is_not_abstract():
    assert not inspect.isabstract(MethodLibraryPackageableElement)


def test_methodlibrarypackageableelement_constructor_exists():
    assert callable(MethodLibraryPackageableElement.__init__)


def test_methodlibrarypackageableelement_constructor_args():
    sig = inspect.signature(MethodLibraryPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_spem::methodpluginpackageableelement_is_not_abstract():
    assert not inspect.isabstract(spem::MethodPluginPackageableElement)


def test_spem::methodpluginpackageableelement_constructor_exists():
    assert callable(spem::MethodPluginPackageableElement.__init__)


def test_spem::methodpluginpackageableelement_constructor_args():
    sig = inspect.signature(spem::MethodPluginPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_spem::methodlibrarypackageableelement_is_not_abstract():
    assert not inspect.isabstract(spem::MethodLibraryPackageableElement)


def test_spem::methodlibrarypackageableelement_constructor_exists():
    assert callable(spem::MethodLibraryPackageableElement.__init__)


def test_spem::methodlibrarypackageableelement_constructor_args():
    sig = inspect.signature(spem::MethodLibraryPackageableElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spem::methodlibrarypackageableelement_has_name():
    assert hasattr(spem::MethodLibraryPackageableElement, "name")
    descriptor = None
    for klass in spem::MethodLibraryPackageableElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spem::methodlibrary_is_not_abstract():
    assert not inspect.isabstract(spem::MethodLibrary)


def test_spem::methodlibrary_constructor_exists():
    assert callable(spem::MethodLibrary.__init__)


def test_spem::methodlibrary_constructor_args():
    sig = inspect.signature(spem::MethodLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spem::methodlibrary_has_name():
    assert hasattr(spem::MethodLibrary, "name")
    descriptor = None
    for klass in spem::MethodLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spem::methodplugin_is_not_abstract():
    assert not inspect.isabstract(spem::MethodPlugin)


def test_spem::methodplugin_constructor_exists():
    assert callable(spem::MethodPlugin.__init__)


def test_spem::methodplugin_constructor_args():
    sig = inspect.signature(spem::MethodPlugin.__init__)
    params = list(sig.parameters.keys())



def test_processpackage_is_not_abstract():
    assert not inspect.isabstract(ProcessPackage)


def test_processpackage_constructor_exists():
    assert callable(ProcessPackage.__init__)


def test_processpackage_constructor_args():
    sig = inspect.signature(ProcessPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::capabilitypatternpackage_is_not_abstract():
    assert not inspect.isabstract(spem::uma::CapabilityPatternPackage)


def test_spem::uma::capabilitypatternpackage_constructor_exists():
    assert callable(spem::uma::CapabilityPatternPackage.__init__)


def test_spem::uma::capabilitypatternpackage_constructor_args():
    sig = inspect.signature(spem::uma::CapabilityPatternPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::processcomponentpackage_is_not_abstract():
    assert not inspect.isabstract(spem::uma::ProcessComponentPackage)


def test_spem::uma::processcomponentpackage_constructor_exists():
    assert callable(spem::uma::ProcessComponentPackage.__init__)


def test_spem::uma::processcomponentpackage_constructor_args():
    sig = inspect.signature(spem::uma::ProcessComponentPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::deliveryprocesspackage_is_not_abstract():
    assert not inspect.isabstract(spem::uma::DeliveryProcessPackage)


def test_spem::uma::deliveryprocesspackage_constructor_exists():
    assert callable(spem::uma::DeliveryProcessPackage.__init__)


def test_spem::uma::deliveryprocesspackage_constructor_args():
    sig = inspect.signature(spem::uma::DeliveryProcessPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem::processcomponent_is_not_abstract():
    assert not inspect.isabstract(spem::ProcessComponent)


def test_spem::processcomponent_constructor_exists():
    assert callable(spem::ProcessComponent.__init__)


def test_spem::processcomponent_constructor_args():
    sig = inspect.signature(spem::ProcessComponent.__init__)
    params = list(sig.parameters.keys())



def test_spem::variabilityelement_is_not_abstract():
    assert not inspect.isabstract(spem::VariabilityElement)


def test_spem::variabilityelement_constructor_exists():
    assert callable(spem::VariabilityElement.__init__)


def test_spem::variabilityelement_constructor_args():
    sig = inspect.signature(spem::VariabilityElement.__init__)
    params = list(sig.parameters.keys())
    assert "variabilityType" in params, "Missing parameter 'variabilityType'"

def test_spem::variabilityelement_has_variabilityType():
    assert hasattr(spem::VariabilityElement, "variabilityType")
    descriptor = None
    for klass in spem::VariabilityElement.__mro__:
        if "variabilityType" in klass.__dict__:
            descriptor = klass.__dict__["variabilityType"]
            break
    assert isinstance(descriptor, property)



def test_roleuse_is_not_abstract():
    assert not inspect.isabstract(RoleUse)


def test_roleuse_constructor_exists():
    assert callable(RoleUse.__init__)


def test_roleuse_constructor_args():
    sig = inspect.signature(RoleUse.__init__)
    params = list(sig.parameters.keys())



def test_spem::compositerole_is_not_abstract():
    assert not inspect.isabstract(spem::CompositeRole)


def test_spem::compositerole_constructor_exists():
    assert callable(spem::CompositeRole.__init__)


def test_spem::compositerole_constructor_args():
    sig = inspect.signature(spem::CompositeRole.__init__)
    params = list(sig.parameters.keys())



def test_kind_is_not_abstract():
    assert not inspect.isabstract(Kind)


def test_kind_constructor_exists():
    assert callable(Kind.__init__)


def test_kind_constructor_args():
    sig = inspect.signature(Kind.__init__)
    params = list(sig.parameters.keys())



def test_methodpluginpackageableelement_is_not_abstract():
    assert not inspect.isabstract(MethodPluginPackageableElement)


def test_methodpluginpackageableelement_constructor_exists():
    assert callable(MethodPluginPackageableElement.__init__)


def test_methodpluginpackageableelement_constructor_args():
    sig = inspect.signature(MethodPluginPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_spem::processpackageableelement_is_not_abstract():
    assert not inspect.isabstract(spem::ProcessPackageableElement)


def test_spem::processpackageableelement_constructor_exists():
    assert callable(spem::ProcessPackageableElement.__init__)


def test_spem::processpackageableelement_constructor_args():
    sig = inspect.signature(spem::ProcessPackageableElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spem::processpackageableelement_has_name():
    assert hasattr(spem::ProcessPackageableElement, "name")
    descriptor = None
    for klass in spem::ProcessPackageableElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spem::methodcontentpackageableelement_is_not_abstract():
    assert not inspect.isabstract(spem::MethodContentPackageableElement)


def test_spem::methodcontentpackageableelement_constructor_exists():
    assert callable(spem::MethodContentPackageableElement.__init__)


def test_spem::methodcontentpackageableelement_constructor_args():
    sig = inspect.signature(spem::MethodContentPackageableElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spem::methodcontentpackageableelement_has_name():
    assert hasattr(spem::MethodContentPackageableElement, "name")
    descriptor = None
    for klass in spem::MethodContentPackageableElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_methodcontentpackageableelement_is_not_abstract():
    assert not inspect.isabstract(MethodContentPackageableElement)


def test_methodcontentpackageableelement_constructor_exists():
    assert callable(MethodContentPackageableElement.__init__)


def test_methodcontentpackageableelement_constructor_args():
    sig = inspect.signature(MethodContentPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_spem::methodcontentpackage_is_not_abstract():
    assert not inspect.isabstract(spem::MethodContentPackage)


def test_spem::methodcontentpackage_constructor_exists():
    assert callable(spem::MethodContentPackage.__init__)


def test_spem::methodcontentpackage_constructor_args():
    sig = inspect.signature(spem::MethodContentPackage.__init__)
    params = list(sig.parameters.keys())



def test_methodcontentelement_is_not_abstract():
    assert not inspect.isabstract(MethodContentElement)


def test_methodcontentelement_constructor_exists():
    assert callable(MethodContentElement.__init__)


def test_methodcontentelement_constructor_args():
    sig = inspect.signature(MethodContentElement.__init__)
    params = list(sig.parameters.keys())



def test_spem::default::responsibilityassignment_is_not_abstract():
    assert not inspect.isabstract(spem::Default::ResponsibilityAssignment)


def test_spem::default::responsibilityassignment_constructor_exists():
    assert callable(spem::Default::ResponsibilityAssignment.__init__)


def test_spem::default::responsibilityassignment_constructor_args():
    sig = inspect.signature(spem::Default::ResponsibilityAssignment.__init__)
    params = list(sig.parameters.keys())



def test_spem::methodcontentkind_is_not_abstract():
    assert not inspect.isabstract(spem::MethodContentKind)


def test_spem::methodcontentkind_constructor_exists():
    assert callable(spem::MethodContentKind.__init__)


def test_spem::methodcontentkind_constructor_args():
    sig = inspect.signature(spem::MethodContentKind.__init__)
    params = list(sig.parameters.keys())



def test_spem::workproductdefinition_is_not_abstract():
    assert not inspect.isabstract(spem::WorkProductDefinition)


def test_spem::workproductdefinition_constructor_exists():
    assert callable(spem::WorkProductDefinition.__init__)


def test_spem::workproductdefinition_constructor_args():
    sig = inspect.signature(spem::WorkProductDefinition.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::roleset_is_not_abstract():
    assert not inspect.isabstract(spem::uma::RoleSet)


def test_spem::uma::roleset_constructor_exists():
    assert callable(spem::uma::RoleSet.__init__)


def test_spem::uma::roleset_constructor_args():
    sig = inspect.signature(spem::uma::RoleSet.__init__)
    params = list(sig.parameters.keys())



def test_spem::default::taskdefinitionperformer_is_not_abstract():
    assert not inspect.isabstract(spem::Default::TaskDefinitionPerformer)


def test_spem::default::taskdefinitionperformer_constructor_exists():
    assert callable(spem::Default::TaskDefinitionPerformer.__init__)


def test_spem::default::taskdefinitionperformer_constructor_args():
    sig = inspect.signature(spem::Default::TaskDefinitionPerformer.__init__)
    params = list(sig.parameters.keys())



def test_spem::workproductdefinitionrelationship_is_not_abstract():
    assert not inspect.isabstract(spem::WorkProductDefinitionRelationship)


def test_spem::workproductdefinitionrelationship_constructor_exists():
    assert callable(spem::WorkProductDefinitionRelationship.__init__)


def test_spem::workproductdefinitionrelationship_constructor_args():
    sig = inspect.signature(spem::WorkProductDefinitionRelationship.__init__)
    params = list(sig.parameters.keys())



def test_spem::uma::workproductkind_is_not_abstract():
    assert not inspect.isabstract(spem::uma::WorkProductKind)


def test_spem::uma::workproductkind_constructor_exists():
    assert callable(spem::uma::WorkProductKind.__init__)


def test_spem::uma::workproductkind_constructor_args():
    sig = inspect.signature(spem::uma::WorkProductKind.__init__)
    params = list(sig.parameters.keys())



def test_spem::tooldefinition_is_not_abstract():
    assert not inspect.isabstract(spem::ToolDefinition)


def test_spem::tooldefinition_constructor_exists():
    assert callable(spem::ToolDefinition.__init__)


def test_spem::tooldefinition_constructor_args():
    sig = inspect.signature(spem::ToolDefinition.__init__)
    params = list(sig.parameters.keys())



def test_spem::category_is_not_abstract():
    assert not inspect.isabstract(spem::Category)


def test_spem::category_constructor_exists():
    assert callable(spem::Category.__init__)


def test_spem::category_constructor_args():
    sig = inspect.signature(spem::Category.__init__)
    params = list(sig.parameters.keys())



def test_spem::guidance_is_not_abstract():
    assert not inspect.isabstract(spem::Guidance)


def test_spem::guidance_constructor_exists():
    assert callable(spem::Guidance.__init__)


def test_spem::guidance_constructor_args():
    sig = inspect.signature(spem::Guidance.__init__)
    params = list(sig.parameters.keys())



def test_processpackageableelement_is_not_abstract():
    assert not inspect.isabstract(ProcessPackageableElement)


def test_processpackageableelement_constructor_exists():
    assert callable(ProcessPackageableElement.__init__)


def test_processpackageableelement_constructor_args():
    sig = inspect.signature(ProcessPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_spem::processpackage_is_not_abstract():
    assert not inspect.isabstract(spem::ProcessPackage)


def test_spem::processpackage_constructor_exists():
    assert callable(spem::ProcessPackage.__init__)


def test_spem::processpackage_constructor_args():
    sig = inspect.signature(spem::ProcessPackage.__init__)
    params = list(sig.parameters.keys())



def test_describableelement_is_not_abstract():
    assert not inspect.isabstract(DescribableElement)


def test_describableelement_constructor_exists():
    assert callable(DescribableElement.__init__)


def test_describableelement_constructor_args():
    sig = inspect.signature(DescribableElement.__init__)
    params = list(sig.parameters.keys())



def test_spem::metric_is_not_abstract():
    assert not inspect.isabstract(spem::Metric)


def test_spem::metric_constructor_exists():
    assert callable(spem::Metric.__init__)


def test_spem::metric_constructor_args():
    sig = inspect.signature(spem::Metric.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_spem::metric_has_expression():
    assert hasattr(spem::Metric, "expression")
    descriptor = None
    for klass in spem::Metric.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_spem::processelement_is_not_abstract():
    assert not inspect.isabstract(spem::ProcessElement)


def test_spem::processelement_constructor_exists():
    assert callable(spem::ProcessElement.__init__)


def test_spem::processelement_constructor_args():
    sig = inspect.signature(spem::ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_workdefinitionparameter_is_not_abstract():
    assert not inspect.isabstract(WorkDefinitionParameter)


def test_workdefinitionparameter_constructor_exists():
    assert callable(WorkDefinitionParameter.__init__)


def test_workdefinitionparameter_constructor_args():
    sig = inspect.signature(WorkDefinitionParameter.__init__)
    params = list(sig.parameters.keys())



def test_spem::default::taskdefinitionparameter_is_not_abstract():
    assert not inspect.isabstract(spem::Default::TaskDefinitionParameter)


def test_spem::default::taskdefinitionparameter_constructor_exists():
    assert callable(spem::Default::TaskDefinitionParameter.__init__)


def test_spem::default::taskdefinitionparameter_constructor_args():
    sig = inspect.signature(spem::Default::TaskDefinitionParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "optionality" in params, "Missing parameter 'optionality'"

def test_spem::default::taskdefinitionparameter_has_name():
    assert hasattr(spem::Default::TaskDefinitionParameter, "name")
    descriptor = None
    for klass in spem::Default::TaskDefinitionParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_spem::default::taskdefinitionparameter_has_optionality():
    assert hasattr(spem::Default::TaskDefinitionParameter, "optionality")
    descriptor = None
    for klass in spem::Default::TaskDefinitionParameter.__mro__:
        if "optionality" in klass.__dict__:
            descriptor = klass.__dict__["optionality"]
            break
    assert isinstance(descriptor, property)



def test_variabilityelement_is_not_abstract():
    assert not inspect.isabstract(VariabilityElement)


def test_variabilityelement_constructor_exists():
    assert callable(VariabilityElement.__init__)


def test_variabilityelement_constructor_args():
    sig = inspect.signature(VariabilityElement.__init__)
    params = list(sig.parameters.keys())



def test_spem::methodcontentelement_is_not_abstract():
    assert not inspect.isabstract(spem::MethodContentElement)


def test_spem::methodcontentelement_constructor_exists():
    assert callable(spem::MethodContentElement.__init__)


def test_spem::methodcontentelement_constructor_args():
    sig = inspect.signature(spem::MethodContentElement.__init__)
    params = list(sig.parameters.keys())



def test_workbreakdownelement_is_not_abstract():
    assert not inspect.isabstract(WorkBreakdownElement)


def test_workbreakdownelement_constructor_exists():
    assert callable(WorkBreakdownElement.__init__)


def test_workbreakdownelement_constructor_args():
    sig = inspect.signature(WorkBreakdownElement.__init__)
    params = list(sig.parameters.keys())



def test_spem::milestone_is_not_abstract():
    assert not inspect.isabstract(spem::Milestone)


def test_spem::milestone_constructor_exists():
    assert callable(spem::Milestone.__init__)


def test_spem::milestone_constructor_args():
    sig = inspect.signature(spem::Milestone.__init__)
    params = list(sig.parameters.keys())



def test_workdefinition_is_not_abstract():
    assert not inspect.isabstract(WorkDefinition)


def test_workdefinition_constructor_exists():
    assert callable(WorkDefinition.__init__)


def test_workdefinition_constructor_args():
    sig = inspect.signature(WorkDefinition.__init__)
    params = list(sig.parameters.keys())



def test_spem::taskdefinition_is_not_abstract():
    assert not inspect.isabstract(spem::TaskDefinition)


def test_spem::taskdefinition_constructor_exists():
    assert callable(spem::TaskDefinition.__init__)


def test_spem::taskdefinition_constructor_args():
    sig = inspect.signature(spem::TaskDefinition.__init__)
    params = list(sig.parameters.keys())



def test_spem::step_is_not_abstract():
    assert not inspect.isabstract(spem::Step)


def test_spem::step_constructor_exists():
    assert callable(spem::Step.__init__)


def test_spem::step_constructor_args():
    sig = inspect.signature(spem::Step.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spem::step_has_name():
    assert hasattr(spem::Step, "name")
    descriptor = None
    for klass in spem::Step.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spem::activity_is_not_abstract():
    assert not inspect.isabstract(spem::Activity)


def test_spem::activity_constructor_exists():
    assert callable(spem::Activity.__init__)


def test_spem::activity_constructor_args():
    sig = inspect.signature(spem::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "useKind" in params, "Missing parameter 'useKind'"
    assert "isEnactable" in params, "Missing parameter 'isEnactable'"

def test_spem::activity_has_useKind():
    assert hasattr(spem::Activity, "useKind")
    descriptor = None
    for klass in spem::Activity.__mro__:
        if "useKind" in klass.__dict__:
            descriptor = klass.__dict__["useKind"]
            break
    assert isinstance(descriptor, property)

def test_spem::activity_has_isEnactable():
    assert hasattr(spem::Activity, "isEnactable")
    descriptor = None
    for klass in spem::Activity.__mro__:
        if "isEnactable" in klass.__dict__:
            descriptor = klass.__dict__["isEnactable"]
            break
    assert isinstance(descriptor, property)



def test_spem::qualification_is_not_abstract():
    assert not inspect.isabstract(spem::Qualification)


def test_spem::qualification_constructor_exists():
    assert callable(spem::Qualification.__init__)


def test_spem::qualification_constructor_args():
    sig = inspect.signature(spem::Qualification.__init__)
    params = list(sig.parameters.keys())



def test_spem::roledefinition_is_not_abstract():
    assert not inspect.isabstract(spem::RoleDefinition)


def test_spem::roledefinition_constructor_exists():
    assert callable(spem::RoleDefinition.__init__)


def test_spem::roledefinition_constructor_args():
    sig = inspect.signature(spem::RoleDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "synonym" in params, "Missing parameter 'synonym'"

def test_spem::roledefinition_has_synonym():
    assert hasattr(spem::RoleDefinition, "synonym")
    descriptor = None
    for klass in spem::RoleDefinition.__mro__:
        if "synonym" in klass.__dict__:
            descriptor = klass.__dict__["synonym"]
            break
    assert isinstance(descriptor, property)



def test_methodcontentuse_is_not_abstract():
    assert not inspect.isabstract(MethodContentUse)


def test_methodcontentuse_constructor_exists():
    assert callable(MethodContentUse.__init__)


def test_methodcontentuse_constructor_args():
    sig = inspect.signature(MethodContentUse.__init__)
    params = list(sig.parameters.keys())



def test_spem::workproductuse_is_not_abstract():
    assert not inspect.isabstract(spem::WorkProductUse)


def test_spem::workproductuse_constructor_exists():
    assert callable(spem::WorkProductUse.__init__)


def test_spem::workproductuse_constructor_args():
    sig = inspect.signature(spem::WorkProductUse.__init__)
    params = list(sig.parameters.keys())



def test_spem::processcomponentuse_is_not_abstract():
    assert not inspect.isabstract(spem::ProcessComponentUse)


def test_spem::processcomponentuse_constructor_exists():
    assert callable(spem::ProcessComponentUse.__init__)


def test_spem::processcomponentuse_constructor_args():
    sig = inspect.signature(spem::ProcessComponentUse.__init__)
    params = list(sig.parameters.keys())



def test_spem::taskuse_is_not_abstract():
    assert not inspect.isabstract(spem::TaskUse)


def test_spem::taskuse_constructor_exists():
    assert callable(spem::TaskUse.__init__)


def test_spem::taskuse_constructor_args():
    sig = inspect.signature(spem::TaskUse.__init__)
    params = list(sig.parameters.keys())
    assert "preCondition" in params, "Missing parameter 'preCondition'"
    assert "postCondition" in params, "Missing parameter 'postCondition'"

def test_spem::taskuse_has_preCondition():
    assert hasattr(spem::TaskUse, "preCondition")
    descriptor = None
    for klass in spem::TaskUse.__mro__:
        if "preCondition" in klass.__dict__:
            descriptor = klass.__dict__["preCondition"]
            break
    assert isinstance(descriptor, property)

def test_spem::taskuse_has_postCondition():
    assert hasattr(spem::TaskUse, "postCondition")
    descriptor = None
    for klass in spem::TaskUse.__mro__:
        if "postCondition" in klass.__dict__:
            descriptor = klass.__dict__["postCondition"]
            break
    assert isinstance(descriptor, property)



def test_spem::roleuse_is_not_abstract():
    assert not inspect.isabstract(spem::RoleUse)


def test_spem::roleuse_constructor_exists():
    assert callable(spem::RoleUse.__init__)


def test_spem::roleuse_constructor_args():
    sig = inspect.signature(spem::RoleUse.__init__)
    params = list(sig.parameters.keys())



def test_workdefinitionperformer_is_not_abstract():
    assert not inspect.isabstract(WorkDefinitionPerformer)


def test_workdefinitionperformer_constructor_exists():
    assert callable(WorkDefinitionPerformer.__init__)


def test_workdefinitionperformer_constructor_args():
    sig = inspect.signature(WorkDefinitionPerformer.__init__)
    params = list(sig.parameters.keys())



def test_spem::methodconfiguration_is_not_abstract():
    assert not inspect.isabstract(spem::MethodConfiguration)


def test_spem::methodconfiguration_constructor_exists():
    assert callable(spem::MethodConfiguration.__init__)


def test_spem::methodconfiguration_constructor_args():
    sig = inspect.signature(spem::MethodConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_spem::workdefinitionparameter_is_not_abstract():
    assert not inspect.isabstract(spem::WorkDefinitionParameter)


def test_spem::workdefinitionparameter_constructor_exists():
    assert callable(spem::WorkDefinitionParameter.__init__)


def test_spem::workdefinitionparameter_constructor_args():
    sig = inspect.signature(spem::WorkDefinitionParameter.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_spem::workdefinitionparameter_has_direction():
    assert hasattr(spem::WorkDefinitionParameter, "direction")
    descriptor = None
    for klass in spem::WorkDefinitionParameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_breakdownelement_is_not_abstract():
    assert not inspect.isabstract(BreakdownElement)


def test_breakdownelement_constructor_exists():
    assert callable(BreakdownElement.__init__)


def test_breakdownelement_constructor_args():
    sig = inspect.signature(BreakdownElement.__init__)
    params = list(sig.parameters.keys())



def test_spem::workproductuserelationship_is_not_abstract():
    assert not inspect.isabstract(spem::WorkProductUseRelationship)


def test_spem::workproductuserelationship_constructor_exists():
    assert callable(spem::WorkProductUseRelationship.__init__)


def test_spem::workproductuserelationship_constructor_args():
    sig = inspect.signature(spem::WorkProductUseRelationship.__init__)
    params = list(sig.parameters.keys())
    assert "relationshipKind" in params, "Missing parameter 'relationshipKind'"

def test_spem::workproductuserelationship_has_relationshipKind():
    assert hasattr(spem::WorkProductUseRelationship, "relationshipKind")
    descriptor = None
    for klass in spem::WorkProductUseRelationship.__mro__:
        if "relationshipKind" in klass.__dict__:
            descriptor = klass.__dict__["relationshipKind"]
            break
    assert isinstance(descriptor, property)



def test_spem::activity::edge_is_not_abstract():
    assert not inspect.isabstract(spem::activity::Edge)


def test_spem::activity::edge_constructor_exists():
    assert callable(spem::activity::Edge.__init__)


def test_spem::activity::edge_constructor_args():
    sig = inspect.signature(spem::activity::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"

def test_spem::activity::edge_has_guard():
    assert hasattr(spem::activity::Edge, "guard")
    descriptor = None
    for klass in spem::activity::Edge.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)



def test_spem::processperformer_is_not_abstract():
    assert not inspect.isabstract(spem::ProcessPerformer)


def test_spem::processperformer_constructor_exists():
    assert callable(spem::ProcessPerformer.__init__)


def test_spem::processperformer_constructor_args():
    sig = inspect.signature(spem::ProcessPerformer.__init__)
    params = list(sig.parameters.keys())



def test_spem::worksequence_is_not_abstract():
    assert not inspect.isabstract(spem::WorkSequence)


def test_spem::worksequence_constructor_exists():
    assert callable(spem::WorkSequence.__init__)


def test_spem::worksequence_constructor_args():
    sig = inspect.signature(spem::WorkSequence.__init__)
    params = list(sig.parameters.keys())
    assert "linkKind" in params, "Missing parameter 'linkKind'"

def test_spem::worksequence_has_linkKind():
    assert hasattr(spem::WorkSequence, "linkKind")
    descriptor = None
    for klass in spem::WorkSequence.__mro__:
        if "linkKind" in klass.__dict__:
            descriptor = klass.__dict__["linkKind"]
            break
    assert isinstance(descriptor, property)



def test_spem::teamprofile_is_not_abstract():
    assert not inspect.isabstract(spem::TeamProfile)


def test_spem::teamprofile_constructor_exists():
    assert callable(spem::TeamProfile.__init__)


def test_spem::teamprofile_constructor_args():
    sig = inspect.signature(spem::TeamProfile.__init__)
    params = list(sig.parameters.keys())



def test_spem::methodcontentuse_is_not_abstract():
    assert not inspect.isabstract(spem::MethodContentUse)


def test_spem::methodcontentuse_constructor_exists():
    assert callable(spem::MethodContentUse.__init__)


def test_spem::methodcontentuse_constructor_args():
    sig = inspect.signature(spem::MethodContentUse.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronizedWithSource" in params, "Missing parameter 'isSynchronizedWithSource'"

def test_spem::methodcontentuse_has_isSynchronizedWithSource():
    assert hasattr(spem::MethodContentUse, "isSynchronizedWithSource")
    descriptor = None
    for klass in spem::MethodContentUse.__mro__:
        if "isSynchronizedWithSource" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronizedWithSource"]
            break
    assert isinstance(descriptor, property)



def test_spem::processresponsibilityassignment_is_not_abstract():
    assert not inspect.isabstract(spem::ProcessResponsibilityAssignment)


def test_spem::processresponsibilityassignment_constructor_exists():
    assert callable(spem::ProcessResponsibilityAssignment.__init__)


def test_spem::processresponsibilityassignment_constructor_args():
    sig = inspect.signature(spem::ProcessResponsibilityAssignment.__init__)
    params = list(sig.parameters.keys())



def test_spem::processparameter_is_not_abstract():
    assert not inspect.isabstract(spem::ProcessParameter)


def test_spem::processparameter_constructor_exists():
    assert callable(spem::ProcessParameter.__init__)


def test_spem::processparameter_constructor_args():
    sig = inspect.signature(spem::ProcessParameter.__init__)
    params = list(sig.parameters.keys())
    assert "optionality" in params, "Missing parameter 'optionality'"

def test_spem::processparameter_has_optionality():
    assert hasattr(spem::ProcessParameter, "optionality")
    descriptor = None
    for klass in spem::ProcessParameter.__mro__:
        if "optionality" in klass.__dict__:
            descriptor = klass.__dict__["optionality"]
            break
    assert isinstance(descriptor, property)



def test_spem::activity::node_is_not_abstract():
    assert not inspect.isabstract(spem::activity::Node)


def test_spem::activity::node_constructor_exists():
    assert callable(spem::activity::Node.__init__)


def test_spem::activity::node_constructor_args():
    sig = inspect.signature(spem::activity::Node.__init__)
    params = list(sig.parameters.keys())



def test_spem::workbreakdownelement_is_not_abstract():
    assert not inspect.isabstract(spem::WorkBreakdownElement)


def test_spem::workbreakdownelement_constructor_exists():
    assert callable(spem::WorkBreakdownElement.__init__)


def test_spem::workbreakdownelement_constructor_args():
    sig = inspect.signature(spem::WorkBreakdownElement.__init__)
    params = list(sig.parameters.keys())
    assert "isEventDriven" in params, "Missing parameter 'isEventDriven'"
    assert "isOngoing" in params, "Missing parameter 'isOngoing'"
    assert "isRepeatable" in params, "Missing parameter 'isRepeatable'"

def test_spem::workbreakdownelement_has_isEventDriven():
    assert hasattr(spem::WorkBreakdownElement, "isEventDriven")
    descriptor = None
    for klass in spem::WorkBreakdownElement.__mro__:
        if "isEventDriven" in klass.__dict__:
            descriptor = klass.__dict__["isEventDriven"]
            break
    assert isinstance(descriptor, property)

def test_spem::workbreakdownelement_has_isOngoing():
    assert hasattr(spem::WorkBreakdownElement, "isOngoing")
    descriptor = None
    for klass in spem::WorkBreakdownElement.__mro__:
        if "isOngoing" in klass.__dict__:
            descriptor = klass.__dict__["isOngoing"]
            break
    assert isinstance(descriptor, property)

def test_spem::workbreakdownelement_has_isRepeatable():
    assert hasattr(spem::WorkBreakdownElement, "isRepeatable")
    descriptor = None
    for klass in spem::WorkBreakdownElement.__mro__:
        if "isRepeatable" in klass.__dict__:
            descriptor = klass.__dict__["isRepeatable"]
            break
    assert isinstance(descriptor, property)



def test_processelement_is_not_abstract():
    assert not inspect.isabstract(ProcessElement)


def test_processelement_constructor_exists():
    assert callable(ProcessElement.__init__)


def test_processelement_constructor_args():
    sig = inspect.signature(ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_spem::workproductport_is_not_abstract():
    assert not inspect.isabstract(spem::WorkProductPort)


def test_spem::workproductport_constructor_exists():
    assert callable(spem::WorkProductPort.__init__)


def test_spem::workproductport_constructor_args():
    sig = inspect.signature(spem::WorkProductPort.__init__)
    params = list(sig.parameters.keys())
    assert "isOptional" in params, "Missing parameter 'isOptional'"
    assert "portKind" in params, "Missing parameter 'portKind'"

def test_spem::workproductport_has_isOptional():
    assert hasattr(spem::WorkProductPort, "isOptional")
    descriptor = None
    for klass in spem::WorkProductPort.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)

def test_spem::workproductport_has_portKind():
    assert hasattr(spem::WorkProductPort, "portKind")
    descriptor = None
    for klass in spem::WorkProductPort.__mro__:
        if "portKind" in klass.__dict__:
            descriptor = klass.__dict__["portKind"]
            break
    assert isinstance(descriptor, property)



def test_spem::workproductportconnector_is_not_abstract():
    assert not inspect.isabstract(spem::WorkProductPortConnector)


def test_spem::workproductportconnector_constructor_exists():
    assert callable(spem::WorkProductPortConnector.__init__)


def test_spem::workproductportconnector_constructor_args():
    sig = inspect.signature(spem::WorkProductPortConnector.__init__)
    params = list(sig.parameters.keys())



def test_spem::planningdata_is_not_abstract():
    assert not inspect.isabstract(spem::PlanningData)


def test_spem::planningdata_constructor_exists():
    assert callable(spem::PlanningData.__init__)


def test_spem::planningdata_constructor_args():
    sig = inspect.signature(spem::PlanningData.__init__)
    params = list(sig.parameters.keys())
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "finishDate" in params, "Missing parameter 'finishDate'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "rank" in params, "Missing parameter 'rank'"

def test_spem::planningdata_has_startDate():
    assert hasattr(spem::PlanningData, "startDate")
    descriptor = None
    for klass in spem::PlanningData.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_spem::planningdata_has_finishDate():
    assert hasattr(spem::PlanningData, "finishDate")
    descriptor = None
    for klass in spem::PlanningData.__mro__:
        if "finishDate" in klass.__dict__:
            descriptor = klass.__dict__["finishDate"]
            break
    assert isinstance(descriptor, property)

def test_spem::planningdata_has_duration():
    assert hasattr(spem::PlanningData, "duration")
    descriptor = None
    for klass in spem::PlanningData.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_spem::planningdata_has_rank():
    assert hasattr(spem::PlanningData, "rank")
    descriptor = None
    for klass in spem::PlanningData.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)



def test_spem::processkind_is_not_abstract():
    assert not inspect.isabstract(spem::ProcessKind)


def test_spem::processkind_constructor_exists():
    assert callable(spem::ProcessKind.__init__)


def test_spem::processkind_constructor_args():
    sig = inspect.signature(spem::ProcessKind.__init__)
    params = list(sig.parameters.keys())



def test_spem::breakdownelement_is_not_abstract():
    assert not inspect.isabstract(spem::BreakdownElement)


def test_spem::breakdownelement_constructor_exists():
    assert callable(spem::BreakdownElement.__init__)


def test_spem::breakdownelement_constructor_args():
    sig = inspect.signature(spem::BreakdownElement.__init__)
    params = list(sig.parameters.keys())
    assert "isPlanned" in params, "Missing parameter 'isPlanned'"
    assert "isOptional" in params, "Missing parameter 'isOptional'"
    assert "hasMultipleOccurrences" in params, "Missing parameter 'hasMultipleOccurrences'"

def test_spem::breakdownelement_has_isPlanned():
    assert hasattr(spem::BreakdownElement, "isPlanned")
    descriptor = None
    for klass in spem::BreakdownElement.__mro__:
        if "isPlanned" in klass.__dict__:
            descriptor = klass.__dict__["isPlanned"]
            break
    assert isinstance(descriptor, property)

def test_spem::breakdownelement_has_isOptional():
    assert hasattr(spem::BreakdownElement, "isOptional")
    descriptor = None
    for klass in spem::BreakdownElement.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)

def test_spem::breakdownelement_has_hasMultipleOccurrences():
    assert hasattr(spem::BreakdownElement, "hasMultipleOccurrences")
    descriptor = None
    for klass in spem::BreakdownElement.__mro__:
        if "hasMultipleOccurrences" in klass.__dict__:
            descriptor = klass.__dict__["hasMultipleOccurrences"]
            break
    assert isinstance(descriptor, property)



def test_spem::workdefinition_is_not_abstract():
    assert not inspect.isabstract(spem::WorkDefinition)


def test_spem::workdefinition_constructor_exists():
    assert callable(spem::WorkDefinition.__init__)


def test_spem::workdefinition_constructor_args():
    sig = inspect.signature(spem::WorkDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "preCondition" in params, "Missing parameter 'preCondition'"
    assert "postCondition" in params, "Missing parameter 'postCondition'"

def test_spem::workdefinition_has_preCondition():
    assert hasattr(spem::WorkDefinition, "preCondition")
    descriptor = None
    for klass in spem::WorkDefinition.__mro__:
        if "preCondition" in klass.__dict__:
            descriptor = klass.__dict__["preCondition"]
            break
    assert isinstance(descriptor, property)

def test_spem::workdefinition_has_postCondition():
    assert hasattr(spem::WorkDefinition, "postCondition")
    descriptor = None
    for klass in spem::WorkDefinition.__mro__:
        if "postCondition" in klass.__dict__:
            descriptor = klass.__dict__["postCondition"]
            break
    assert isinstance(descriptor, property)



def test_spem::workdefinitionperformer_is_not_abstract():
    assert not inspect.isabstract(spem::WorkDefinitionPerformer)


def test_spem::workdefinitionperformer_constructor_exists():
    assert callable(spem::WorkDefinitionPerformer.__init__)


def test_spem::workdefinitionperformer_constructor_args():
    sig = inspect.signature(spem::WorkDefinitionPerformer.__init__)
    params = list(sig.parameters.keys())



def test_extensibleelement_is_not_abstract():
    assert not inspect.isabstract(ExtensibleElement)


def test_extensibleelement_constructor_exists():
    assert callable(ExtensibleElement.__init__)


def test_extensibleelement_constructor_args():
    sig = inspect.signature(ExtensibleElement.__init__)
    params = list(sig.parameters.keys())



def test_spem::describableelement_is_not_abstract():
    assert not inspect.isabstract(spem::DescribableElement)


def test_spem::describableelement_constructor_exists():
    assert callable(spem::DescribableElement.__init__)


def test_spem::describableelement_constructor_args():
    sig = inspect.signature(spem::DescribableElement.__init__)
    params = list(sig.parameters.keys())
    assert "briefDescription" in params, "Missing parameter 'briefDescription'"
    assert "purpose" in params, "Missing parameter 'purpose'"
    assert "mainDescription" in params, "Missing parameter 'mainDescription'"
    assert "author" in params, "Missing parameter 'author'"
    assert "changeDate" in params, "Missing parameter 'changeDate'"
    assert "presentationName" in params, "Missing parameter 'presentationName'"
    assert "version" in params, "Missing parameter 'version'"
    assert "changeDescription" in params, "Missing parameter 'changeDescription'"
    assert "copyright" in params, "Missing parameter 'copyright'"

def test_spem::describableelement_has_briefDescription():
    assert hasattr(spem::DescribableElement, "briefDescription")
    descriptor = None
    for klass in spem::DescribableElement.__mro__:
        if "briefDescription" in klass.__dict__:
            descriptor = klass.__dict__["briefDescription"]
            break
    assert isinstance(descriptor, property)

def test_spem::describableelement_has_purpose():
    assert hasattr(spem::DescribableElement, "purpose")
    descriptor = None
    for klass in spem::DescribableElement.__mro__:
        if "purpose" in klass.__dict__:
            descriptor = klass.__dict__["purpose"]
            break
    assert isinstance(descriptor, property)

def test_spem::describableelement_has_mainDescription():
    assert hasattr(spem::DescribableElement, "mainDescription")
    descriptor = None
    for klass in spem::DescribableElement.__mro__:
        if "mainDescription" in klass.__dict__:
            descriptor = klass.__dict__["mainDescription"]
            break
    assert isinstance(descriptor, property)

def test_spem::describableelement_has_author():
    assert hasattr(spem::DescribableElement, "author")
    descriptor = None
    for klass in spem::DescribableElement.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_spem::describableelement_has_changeDate():
    assert hasattr(spem::DescribableElement, "changeDate")
    descriptor = None
    for klass in spem::DescribableElement.__mro__:
        if "changeDate" in klass.__dict__:
            descriptor = klass.__dict__["changeDate"]
            break
    assert isinstance(descriptor, property)

def test_spem::describableelement_has_presentationName():
    assert hasattr(spem::DescribableElement, "presentationName")
    descriptor = None
    for klass in spem::DescribableElement.__mro__:
        if "presentationName" in klass.__dict__:
            descriptor = klass.__dict__["presentationName"]
            break
    assert isinstance(descriptor, property)

def test_spem::describableelement_has_version():
    assert hasattr(spem::DescribableElement, "version")
    descriptor = None
    for klass in spem::DescribableElement.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_spem::describableelement_has_changeDescription():
    assert hasattr(spem::DescribableElement, "changeDescription")
    descriptor = None
    for klass in spem::DescribableElement.__mro__:
        if "changeDescription" in klass.__dict__:
            descriptor = klass.__dict__["changeDescription"]
            break
    assert isinstance(descriptor, property)

def test_spem::describableelement_has_copyright():
    assert hasattr(spem::DescribableElement, "copyright")
    descriptor = None
    for klass in spem::DescribableElement.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)



def test_spem::kind_is_not_abstract():
    assert not inspect.isabstract(spem::Kind)


def test_spem::kind_constructor_exists():
    assert callable(spem::Kind.__init__)


def test_spem::kind_constructor_args():
    sig = inspect.signature(spem::Kind.__init__)
    params = list(sig.parameters.keys())



def test_spem::extensibleelement_is_not_abstract():
    assert not inspect.isabstract(spem::ExtensibleElement)


def test_spem::extensibleelement_constructor_exists():
    assert callable(spem::ExtensibleElement.__init__)


def test_spem::extensibleelement_constructor_args():
    sig = inspect.signature(spem::ExtensibleElement.__init__)
    params = list(sig.parameters.keys())

def test_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "in_",
        "inout",
        "out",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirectionKind"

def test_worksequencekind_exists():
    # Check that the Enumeration exists
    assert WorkSequenceKind is not None

def test_worksequencekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkSequenceKind]
    expected_literals = [
        "startToStart",
        "startToFinish",
        "finishToStart",
        "finishToFinish",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WorkSequenceKind"

def test_optionalitykind_exists():
    # Check that the Enumeration exists
    assert OptionalityKind is not None

def test_optionalitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OptionalityKind]
    expected_literals = [
        "optional",
        "mandatory",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OptionalityKind"

def test_contractkind_exists():
    # Check that the Enumeration exists
    assert ContractKind is not None

def test_contractkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractKind]
    expected_literals = [
        "IMPLIED",
        "EXPRESS",
        "OTHER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractKind"

def test_activityusekind_exists():
    # Check that the Enumeration exists
    assert ActivityUseKind is not None

def test_activityusekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActivityUseKind]
    expected_literals = [
        "extension",
        "localContribution",
        "na",
        "localReplacement",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActivityUseKind"

def test_risklevel_exists():
    # Check that the Enumeration exists
    assert RiskLevel is not None

def test_risklevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RiskLevel]
    expected_literals = [
        "HIGH",
        "LOW",
        "MID",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RiskLevel"

def test_expertiselevel_exists():
    # Check that the Enumeration exists
    assert ExpertiseLevel is not None

def test_expertiselevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExpertiseLevel]
    expected_literals = [
        "MID",
        "LOW",
        "LEVEL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExpertiseLevel"

def test_workproductrelationshipkind_exists():
    # Check that the Enumeration exists
    assert WorkProductRelationshipKind is not None

def test_workproductrelationshipkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkProductRelationshipKind]
    expected_literals = [
        "impactedBy",
        "composition",
        "aggregation",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WorkProductRelationshipKind"

def test_estimatingtechnique_exists():
    # Check that the Enumeration exists
    assert EstimatingTechnique is not None

def test_estimatingtechnique_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EstimatingTechnique]
    expected_literals = [
        "SKILLS",
        "DEFECTS",
        "TIME",
        "COST",
        "OTHER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EstimatingTechnique"

def test_variabilitytype_exists():
    # Check that the Enumeration exists
    assert VariabilityType is not None

def test_variabilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariabilityType]
    expected_literals = [
        "extends",
        "replaces",
        "na",
        "contributes",
        "extends_replaces",
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
uma::spem::RoleDefinition_strategy = st.builds(
    uma::spem::RoleDefinition,
)
Node_strategy = st.builds(
    Node,
)
spem::activity::EndNode_strategy = st.builds(
    spem::activity::EndNode,
)
spem::activity::DecisionNode_strategy = st.builds(
    spem::activity::DecisionNode,
)
spem::activity::ForkNode_strategy = st.builds(
    spem::activity::ForkNode,
)
spem::activity::JoinNode_strategy = st.builds(
    spem::activity::JoinNode,
)
spem::activity::StartNode_strategy = st.builds(
    spem::activity::StartNode,
)
activity::spem::BreakdownElement_strategy = st.builds(
    activity::spem::BreakdownElement,
)
Edge_strategy = st.builds(
    Edge,
)
uma::spem::MethodContentElement_strategy = st.builds(
    uma::spem::MethodContentElement,
)
uma::spem::Activity_strategy = st.builds(
    uma::spem::Activity,
)
Practice_strategy = st.builds(
    Practice,
)
uma::spem::WorkProductDefinition_strategy = st.builds(
    uma::spem::WorkProductDefinition,
)
Concept_strategy = st.builds(
    Concept,
)
spem::uma::Whitepaper_strategy = st.builds(
    spem::uma::Whitepaper,
)
SupportingMaterial_strategy = st.builds(
    SupportingMaterial,
)
uma::spem::WorkProductPortConnector_strategy = st.builds(
    uma::spem::WorkProductPortConnector,
)
CapabilityPattern_strategy = st.builds(
    CapabilityPattern,
)
Activity_strategy = st.builds(
    Activity,
)
spem::uma::Phase_strategy = st.builds(
    spem::uma::Phase,
)
spem::uma::Iteration_strategy = st.builds(
    spem::uma::Iteration,
)
spem::uma::Process_strategy = st.builds(
    spem::uma::Process,
    usageNote=
        safe_text,
    scope=
        safe_text
)
uma::spem::MethodPlugin_strategy = st.builds(
    uma::spem::MethodPlugin,
)
uma::spem::MethodLibrary_strategy = st.builds(
    uma::spem::MethodLibrary,
)
uma::spem::WorkProductUse_strategy = st.builds(
    uma::spem::WorkProductUse,
)
uma::spem::MethodConfiguration_strategy = st.builds(
    uma::spem::MethodConfiguration,
)
spem::uma::Root_strategy = st.builds(
    spem::uma::Root,
)
Category_strategy = st.builds(
    Category,
)
spem::uma::Domain_strategy = st.builds(
    spem::uma::Domain,
)
spem::uma::DisciplineGrouping_strategy = st.builds(
    spem::uma::DisciplineGrouping,
)
spem::uma::CustomCategory_strategy = st.builds(
    spem::uma::CustomCategory,
)
MethodContentPackage_strategy = st.builds(
    MethodContentPackage,
)
spem::uma::WorkProductKindPackage_strategy = st.builds(
    spem::uma::WorkProductKindPackage,
)
spem::uma::TaskDefinitionPackage_strategy = st.builds(
    spem::uma::TaskDefinitionPackage,
)
spem::uma::QualificationPackage_strategy = st.builds(
    spem::uma::QualificationPackage,
)
spem::uma::ToolDefinitionPackage_strategy = st.builds(
    spem::uma::ToolDefinitionPackage,
)
spem::uma::GuidancePackage_strategy = st.builds(
    spem::uma::GuidancePackage,
)
spem::uma::RoleDefinitionPackage_strategy = st.builds(
    spem::uma::RoleDefinitionPackage,
)
spem::uma::DomainPackage_strategy = st.builds(
    spem::uma::DomainPackage,
)
spem::uma::WorkProductDefinitionPackage_strategy = st.builds(
    spem::uma::WorkProductDefinitionPackage,
)
spem::uma::RoleSetPackage_strategy = st.builds(
    spem::uma::RoleSetPackage,
)
spem::uma::ConfigurationPackage_strategy = st.builds(
    spem::uma::ConfigurationPackage,
)
spem::uma::DisciplinePackage_strategy = st.builds(
    spem::uma::DisciplinePackage,
)
spem::uma::CategoryPackage_strategy = st.builds(
    spem::uma::CategoryPackage,
)
Guidance_strategy = st.builds(
    Guidance,
)
spem::uma::Example_strategy = st.builds(
    spem::uma::Example,
)
spem::uma::Concept_strategy = st.builds(
    spem::uma::Concept,
)
spem::uma::EstimatingConsideration_strategy = st.builds(
    spem::uma::EstimatingConsideration,
)
spem::uma::Template_strategy = st.builds(
    spem::uma::Template,
)
spem::uma::TermDefinition_strategy = st.builds(
    spem::uma::TermDefinition,
)
spem::uma::Guideline_strategy = st.builds(
    spem::uma::Guideline,
)
spem::uma::Roadmap_strategy = st.builds(
    spem::uma::Roadmap,
)
spem::uma::ToolMentor_strategy = st.builds(
    spem::uma::ToolMentor,
)
spem::uma::ReusableAsset_strategy = st.builds(
    spem::uma::ReusableAsset,
)
spem::uma::Report_strategy = st.builds(
    spem::uma::Report,
)
spem::uma::Practice_strategy = st.builds(
    spem::uma::Practice,
    problem=
        safe_text,
    background=
        safe_text,
    goal=
        safe_text,
    levelOfAdoption=
        safe_text,
    application=
        safe_text,
    additionalInfo=
        safe_text
)
spem::uma::SupportingMaterial_strategy = st.builds(
    spem::uma::SupportingMaterial,
)
spem::uma::Checklist_strategy = st.builds(
    spem::uma::Checklist,
)
uma::spem::TaskDefinition_strategy = st.builds(
    uma::spem::TaskDefinition,
)
Process_strategy = st.builds(
    Process,
)
spem::uma::ProcessPlanningTemplate_strategy = st.builds(
    spem::uma::ProcessPlanningTemplate,
)
spem::uma::DeliveryProcess_strategy = st.builds(
    spem::uma::DeliveryProcess,
    scale=
        safe_text,
    estimatingTechnique=
        safe_text,
    typeOfContract=
        safe_text,
    projectMemberExpertise=
        safe_text,
    riskLevel=
        safe_text,
    projectCharacteristics=
        safe_text
)
spem::uma::CapabilityPattern_strategy = st.builds(
    spem::uma::CapabilityPattern,
)
spem::uma::Discipline_strategy = st.builds(
    spem::uma::Discipline,
)
Artifact_strategy = st.builds(
    Artifact,
)
WorkProductUse_strategy = st.builds(
    WorkProductUse,
)
spem::uma::Deliverable_strategy = st.builds(
    spem::uma::Deliverable,
    externalDescription=
        safe_text,
    packagingGuidance=
        safe_text
)
spem::uma::Outcome_strategy = st.builds(
    spem::uma::Outcome,
)
spem::uma::Artifact_strategy = st.builds(
    spem::uma::Artifact,
)
MethodLibraryPackageableElement_strategy = st.builds(
    MethodLibraryPackageableElement,
)
spem::MethodPluginPackageableElement_strategy = st.builds(
    spem::MethodPluginPackageableElement,
)
spem::MethodLibraryPackageableElement_strategy = st.builds(
    spem::MethodLibraryPackageableElement,
    name=
        safe_text
)
spem::MethodLibrary_strategy = st.builds(
    spem::MethodLibrary,
    name=
        safe_text
)
spem::MethodPlugin_strategy = st.builds(
    spem::MethodPlugin,
)
ProcessPackage_strategy = st.builds(
    ProcessPackage,
)
spem::uma::CapabilityPatternPackage_strategy = st.builds(
    spem::uma::CapabilityPatternPackage,
)
spem::uma::ProcessComponentPackage_strategy = st.builds(
    spem::uma::ProcessComponentPackage,
)
spem::uma::DeliveryProcessPackage_strategy = st.builds(
    spem::uma::DeliveryProcessPackage,
)
spem::ProcessComponent_strategy = st.builds(
    spem::ProcessComponent,
)
spem::VariabilityElement_strategy = st.builds(
    spem::VariabilityElement,
    variabilityType=
        safe_text
)
RoleUse_strategy = st.builds(
    RoleUse,
)
spem::CompositeRole_strategy = st.builds(
    spem::CompositeRole,
)
Kind_strategy = st.builds(
    Kind,
)
MethodPluginPackageableElement_strategy = st.builds(
    MethodPluginPackageableElement,
)
spem::ProcessPackageableElement_strategy = st.builds(
    spem::ProcessPackageableElement,
    name=
        safe_text
)
spem::MethodContentPackageableElement_strategy = st.builds(
    spem::MethodContentPackageableElement,
    name=
        safe_text
)
MethodContentPackageableElement_strategy = st.builds(
    MethodContentPackageableElement,
)
spem::MethodContentPackage_strategy = st.builds(
    spem::MethodContentPackage,
)
MethodContentElement_strategy = st.builds(
    MethodContentElement,
)
spem::Default::ResponsibilityAssignment_strategy = st.builds(
    spem::Default::ResponsibilityAssignment,
)
spem::MethodContentKind_strategy = st.builds(
    spem::MethodContentKind,
)
spem::WorkProductDefinition_strategy = st.builds(
    spem::WorkProductDefinition,
)
spem::uma::RoleSet_strategy = st.builds(
    spem::uma::RoleSet,
)
spem::Default::TaskDefinitionPerformer_strategy = st.builds(
    spem::Default::TaskDefinitionPerformer,
)
spem::WorkProductDefinitionRelationship_strategy = st.builds(
    spem::WorkProductDefinitionRelationship,
)
spem::uma::WorkProductKind_strategy = st.builds(
    spem::uma::WorkProductKind,
)
spem::ToolDefinition_strategy = st.builds(
    spem::ToolDefinition,
)
spem::Category_strategy = st.builds(
    spem::Category,
)
spem::Guidance_strategy = st.builds(
    spem::Guidance,
)
ProcessPackageableElement_strategy = st.builds(
    ProcessPackageableElement,
)
spem::ProcessPackage_strategy = st.builds(
    spem::ProcessPackage,
)
DescribableElement_strategy = st.builds(
    DescribableElement,
)
spem::Metric_strategy = st.builds(
    spem::Metric,
    expression=
        safe_text
)
spem::ProcessElement_strategy = st.builds(
    spem::ProcessElement,
)
WorkDefinitionParameter_strategy = st.builds(
    WorkDefinitionParameter,
)
spem::Default::TaskDefinitionParameter_strategy = st.builds(
    spem::Default::TaskDefinitionParameter,
    name=
        safe_text,
    optionality=
        safe_text
)
VariabilityElement_strategy = st.builds(
    VariabilityElement,
)
spem::MethodContentElement_strategy = st.builds(
    spem::MethodContentElement,
)
WorkBreakdownElement_strategy = st.builds(
    WorkBreakdownElement,
)
spem::Milestone_strategy = st.builds(
    spem::Milestone,
)
WorkDefinition_strategy = st.builds(
    WorkDefinition,
)
spem::TaskDefinition_strategy = st.builds(
    spem::TaskDefinition,
)
spem::Step_strategy = st.builds(
    spem::Step,
    name=
        safe_text
)
spem::Activity_strategy = st.builds(
    spem::Activity,
    useKind=
        safe_text,
    isEnactable=
        st.booleans()
)
spem::Qualification_strategy = st.builds(
    spem::Qualification,
)
spem::RoleDefinition_strategy = st.builds(
    spem::RoleDefinition,
    synonym=
        safe_text
)
MethodContentUse_strategy = st.builds(
    MethodContentUse,
)
spem::WorkProductUse_strategy = st.builds(
    spem::WorkProductUse,
)
spem::ProcessComponentUse_strategy = st.builds(
    spem::ProcessComponentUse,
)
spem::TaskUse_strategy = st.builds(
    spem::TaskUse,
    preCondition=
        safe_text,
    postCondition=
        safe_text
)
spem::RoleUse_strategy = st.builds(
    spem::RoleUse,
)
WorkDefinitionPerformer_strategy = st.builds(
    WorkDefinitionPerformer,
)
spem::MethodConfiguration_strategy = st.builds(
    spem::MethodConfiguration,
)
spem::WorkDefinitionParameter_strategy = st.builds(
    spem::WorkDefinitionParameter,
    direction=
        safe_text
)
BreakdownElement_strategy = st.builds(
    BreakdownElement,
)
spem::WorkProductUseRelationship_strategy = st.builds(
    spem::WorkProductUseRelationship,
    relationshipKind=
        safe_text
)
spem::activity::Edge_strategy = st.builds(
    spem::activity::Edge,
    guard=
        safe_text
)
spem::ProcessPerformer_strategy = st.builds(
    spem::ProcessPerformer,
)
spem::WorkSequence_strategy = st.builds(
    spem::WorkSequence,
    linkKind=
        safe_text
)
spem::TeamProfile_strategy = st.builds(
    spem::TeamProfile,
)
spem::MethodContentUse_strategy = st.builds(
    spem::MethodContentUse,
    isSynchronizedWithSource=
        st.booleans()
)
spem::ProcessResponsibilityAssignment_strategy = st.builds(
    spem::ProcessResponsibilityAssignment,
)
spem::ProcessParameter_strategy = st.builds(
    spem::ProcessParameter,
    optionality=
        safe_text
)
spem::activity::Node_strategy = st.builds(
    spem::activity::Node,
)
spem::WorkBreakdownElement_strategy = st.builds(
    spem::WorkBreakdownElement,
    isEventDriven=
        st.booleans(),
    isOngoing=
        st.booleans(),
    isRepeatable=
        st.booleans()
)
ProcessElement_strategy = st.builds(
    ProcessElement,
)
spem::WorkProductPort_strategy = st.builds(
    spem::WorkProductPort,
    isOptional=
        st.booleans(),
    portKind=
        safe_text
)
spem::WorkProductPortConnector_strategy = st.builds(
    spem::WorkProductPortConnector,
)
spem::PlanningData_strategy = st.builds(
    spem::PlanningData,
    startDate=
        st.dates(),
    finishDate=
        st.dates(),
    duration=
        safe_text,
    rank=
        st.integers()
)
spem::ProcessKind_strategy = st.builds(
    spem::ProcessKind,
)
spem::BreakdownElement_strategy = st.builds(
    spem::BreakdownElement,
    isPlanned=
        st.booleans(),
    isOptional=
        st.booleans(),
    hasMultipleOccurrences=
        st.booleans()
)
spem::WorkDefinition_strategy = st.builds(
    spem::WorkDefinition,
    preCondition=
        safe_text,
    postCondition=
        safe_text
)
spem::WorkDefinitionPerformer_strategy = st.builds(
    spem::WorkDefinitionPerformer,
)
ExtensibleElement_strategy = st.builds(
    ExtensibleElement,
)
spem::DescribableElement_strategy = st.builds(
    spem::DescribableElement,
    briefDescription=
        safe_text,
    purpose=
        safe_text,
    mainDescription=
        safe_text,
    author=
        safe_text,
    changeDate=
        st.dates(),
    presentationName=
        safe_text,
    version=
        safe_text,
    changeDescription=
        safe_text,
    copyright=
        safe_text
)
spem::Kind_strategy = st.builds(
    spem::Kind,
)
spem::ExtensibleElement_strategy = st.builds(
    spem::ExtensibleElement,
)

@given(instance=uma::spem::RoleDefinition_strategy)
@settings(max_examples=50)
def test_uma::spem::roledefinition_instantiation(instance):
    assert isinstance(instance, uma::spem::RoleDefinition)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=spem::activity::EndNode_strategy)
@settings(max_examples=50)
def test_spem::activity::endnode_instantiation(instance):
    assert isinstance(instance, spem::activity::EndNode)

@given(instance=spem::activity::DecisionNode_strategy)
@settings(max_examples=50)
def test_spem::activity::decisionnode_instantiation(instance):
    assert isinstance(instance, spem::activity::DecisionNode)

@given(instance=spem::activity::ForkNode_strategy)
@settings(max_examples=50)
def test_spem::activity::forknode_instantiation(instance):
    assert isinstance(instance, spem::activity::ForkNode)

@given(instance=spem::activity::JoinNode_strategy)
@settings(max_examples=50)
def test_spem::activity::joinnode_instantiation(instance):
    assert isinstance(instance, spem::activity::JoinNode)

@given(instance=spem::activity::StartNode_strategy)
@settings(max_examples=50)
def test_spem::activity::startnode_instantiation(instance):
    assert isinstance(instance, spem::activity::StartNode)

@given(instance=activity::spem::BreakdownElement_strategy)
@settings(max_examples=50)
def test_activity::spem::breakdownelement_instantiation(instance):
    assert isinstance(instance, activity::spem::BreakdownElement)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=uma::spem::MethodContentElement_strategy)
@settings(max_examples=50)
def test_uma::spem::methodcontentelement_instantiation(instance):
    assert isinstance(instance, uma::spem::MethodContentElement)

@given(instance=uma::spem::Activity_strategy)
@settings(max_examples=50)
def test_uma::spem::activity_instantiation(instance):
    assert isinstance(instance, uma::spem::Activity)

@given(instance=Practice_strategy)
@settings(max_examples=50)
def test_practice_instantiation(instance):
    assert isinstance(instance, Practice)

@given(instance=uma::spem::WorkProductDefinition_strategy)
@settings(max_examples=50)
def test_uma::spem::workproductdefinition_instantiation(instance):
    assert isinstance(instance, uma::spem::WorkProductDefinition)

@given(instance=Concept_strategy)
@settings(max_examples=50)
def test_concept_instantiation(instance):
    assert isinstance(instance, Concept)

@given(instance=spem::uma::Whitepaper_strategy)
@settings(max_examples=50)
def test_spem::uma::whitepaper_instantiation(instance):
    assert isinstance(instance, spem::uma::Whitepaper)

@given(instance=SupportingMaterial_strategy)
@settings(max_examples=50)
def test_supportingmaterial_instantiation(instance):
    assert isinstance(instance, SupportingMaterial)

@given(instance=uma::spem::WorkProductPortConnector_strategy)
@settings(max_examples=50)
def test_uma::spem::workproductportconnector_instantiation(instance):
    assert isinstance(instance, uma::spem::WorkProductPortConnector)

@given(instance=CapabilityPattern_strategy)
@settings(max_examples=50)
def test_capabilitypattern_instantiation(instance):
    assert isinstance(instance, CapabilityPattern)

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=spem::uma::Phase_strategy)
@settings(max_examples=50)
def test_spem::uma::phase_instantiation(instance):
    assert isinstance(instance, spem::uma::Phase)

@given(instance=spem::uma::Iteration_strategy)
@settings(max_examples=50)
def test_spem::uma::iteration_instantiation(instance):
    assert isinstance(instance, spem::uma::Iteration)

@given(instance=spem::uma::Process_strategy)
@settings(max_examples=50)
def test_spem::uma::process_instantiation(instance):
    assert isinstance(instance, spem::uma::Process)

@given(instance=spem::uma::Process_strategy)
def test_spem::uma::process_usageNote_type(instance):
    assert isinstance(instance.usageNote, str)


@given(instance=spem::uma::Process_strategy)
def test_spem::uma::process_usageNote_setter(instance):
    original = instance.usageNote
    instance.usageNote = original
    assert instance.usageNote == original

@given(instance=spem::uma::Process_strategy)
def test_spem::uma::process_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=spem::uma::Process_strategy)
def test_spem::uma::process_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=uma::spem::MethodPlugin_strategy)
@settings(max_examples=50)
def test_uma::spem::methodplugin_instantiation(instance):
    assert isinstance(instance, uma::spem::MethodPlugin)

@given(instance=uma::spem::MethodLibrary_strategy)
@settings(max_examples=50)
def test_uma::spem::methodlibrary_instantiation(instance):
    assert isinstance(instance, uma::spem::MethodLibrary)

@given(instance=uma::spem::WorkProductUse_strategy)
@settings(max_examples=50)
def test_uma::spem::workproductuse_instantiation(instance):
    assert isinstance(instance, uma::spem::WorkProductUse)

@given(instance=uma::spem::MethodConfiguration_strategy)
@settings(max_examples=50)
def test_uma::spem::methodconfiguration_instantiation(instance):
    assert isinstance(instance, uma::spem::MethodConfiguration)

@given(instance=spem::uma::Root_strategy)
@settings(max_examples=50)
def test_spem::uma::root_instantiation(instance):
    assert isinstance(instance, spem::uma::Root)

@given(instance=Category_strategy)
@settings(max_examples=50)
def test_category_instantiation(instance):
    assert isinstance(instance, Category)

@given(instance=spem::uma::Domain_strategy)
@settings(max_examples=50)
def test_spem::uma::domain_instantiation(instance):
    assert isinstance(instance, spem::uma::Domain)

@given(instance=spem::uma::DisciplineGrouping_strategy)
@settings(max_examples=50)
def test_spem::uma::disciplinegrouping_instantiation(instance):
    assert isinstance(instance, spem::uma::DisciplineGrouping)

@given(instance=spem::uma::CustomCategory_strategy)
@settings(max_examples=50)
def test_spem::uma::customcategory_instantiation(instance):
    assert isinstance(instance, spem::uma::CustomCategory)

@given(instance=MethodContentPackage_strategy)
@settings(max_examples=50)
def test_methodcontentpackage_instantiation(instance):
    assert isinstance(instance, MethodContentPackage)

@given(instance=spem::uma::WorkProductKindPackage_strategy)
@settings(max_examples=50)
def test_spem::uma::workproductkindpackage_instantiation(instance):
    assert isinstance(instance, spem::uma::WorkProductKindPackage)

@given(instance=spem::uma::TaskDefinitionPackage_strategy)
@settings(max_examples=50)
def test_spem::uma::taskdefinitionpackage_instantiation(instance):
    assert isinstance(instance, spem::uma::TaskDefinitionPackage)

@given(instance=spem::uma::QualificationPackage_strategy)
@settings(max_examples=50)
def test_spem::uma::qualificationpackage_instantiation(instance):
    assert isinstance(instance, spem::uma::QualificationPackage)

@given(instance=spem::uma::ToolDefinitionPackage_strategy)
@settings(max_examples=50)
def test_spem::uma::tooldefinitionpackage_instantiation(instance):
    assert isinstance(instance, spem::uma::ToolDefinitionPackage)

@given(instance=spem::uma::GuidancePackage_strategy)
@settings(max_examples=50)
def test_spem::uma::guidancepackage_instantiation(instance):
    assert isinstance(instance, spem::uma::GuidancePackage)

@given(instance=spem::uma::RoleDefinitionPackage_strategy)
@settings(max_examples=50)
def test_spem::uma::roledefinitionpackage_instantiation(instance):
    assert isinstance(instance, spem::uma::RoleDefinitionPackage)

@given(instance=spem::uma::DomainPackage_strategy)
@settings(max_examples=50)
def test_spem::uma::domainpackage_instantiation(instance):
    assert isinstance(instance, spem::uma::DomainPackage)

@given(instance=spem::uma::WorkProductDefinitionPackage_strategy)
@settings(max_examples=50)
def test_spem::uma::workproductdefinitionpackage_instantiation(instance):
    assert isinstance(instance, spem::uma::WorkProductDefinitionPackage)

@given(instance=spem::uma::RoleSetPackage_strategy)
@settings(max_examples=50)
def test_spem::uma::rolesetpackage_instantiation(instance):
    assert isinstance(instance, spem::uma::RoleSetPackage)

@given(instance=spem::uma::ConfigurationPackage_strategy)
@settings(max_examples=50)
def test_spem::uma::configurationpackage_instantiation(instance):
    assert isinstance(instance, spem::uma::ConfigurationPackage)

@given(instance=spem::uma::DisciplinePackage_strategy)
@settings(max_examples=50)
def test_spem::uma::disciplinepackage_instantiation(instance):
    assert isinstance(instance, spem::uma::DisciplinePackage)

@given(instance=spem::uma::CategoryPackage_strategy)
@settings(max_examples=50)
def test_spem::uma::categorypackage_instantiation(instance):
    assert isinstance(instance, spem::uma::CategoryPackage)

@given(instance=Guidance_strategy)
@settings(max_examples=50)
def test_guidance_instantiation(instance):
    assert isinstance(instance, Guidance)

@given(instance=spem::uma::Example_strategy)
@settings(max_examples=50)
def test_spem::uma::example_instantiation(instance):
    assert isinstance(instance, spem::uma::Example)

@given(instance=spem::uma::Concept_strategy)
@settings(max_examples=50)
def test_spem::uma::concept_instantiation(instance):
    assert isinstance(instance, spem::uma::Concept)

@given(instance=spem::uma::EstimatingConsideration_strategy)
@settings(max_examples=50)
def test_spem::uma::estimatingconsideration_instantiation(instance):
    assert isinstance(instance, spem::uma::EstimatingConsideration)

@given(instance=spem::uma::Template_strategy)
@settings(max_examples=50)
def test_spem::uma::template_instantiation(instance):
    assert isinstance(instance, spem::uma::Template)

@given(instance=spem::uma::TermDefinition_strategy)
@settings(max_examples=50)
def test_spem::uma::termdefinition_instantiation(instance):
    assert isinstance(instance, spem::uma::TermDefinition)

@given(instance=spem::uma::Guideline_strategy)
@settings(max_examples=50)
def test_spem::uma::guideline_instantiation(instance):
    assert isinstance(instance, spem::uma::Guideline)

@given(instance=spem::uma::Roadmap_strategy)
@settings(max_examples=50)
def test_spem::uma::roadmap_instantiation(instance):
    assert isinstance(instance, spem::uma::Roadmap)

@given(instance=spem::uma::ToolMentor_strategy)
@settings(max_examples=50)
def test_spem::uma::toolmentor_instantiation(instance):
    assert isinstance(instance, spem::uma::ToolMentor)

@given(instance=spem::uma::ReusableAsset_strategy)
@settings(max_examples=50)
def test_spem::uma::reusableasset_instantiation(instance):
    assert isinstance(instance, spem::uma::ReusableAsset)

@given(instance=spem::uma::Report_strategy)
@settings(max_examples=50)
def test_spem::uma::report_instantiation(instance):
    assert isinstance(instance, spem::uma::Report)

@given(instance=spem::uma::Practice_strategy)
@settings(max_examples=50)
def test_spem::uma::practice_instantiation(instance):
    assert isinstance(instance, spem::uma::Practice)

@given(instance=spem::uma::Practice_strategy)
def test_spem::uma::practice_problem_type(instance):
    assert isinstance(instance.problem, str)


@given(instance=spem::uma::Practice_strategy)
def test_spem::uma::practice_problem_setter(instance):
    original = instance.problem
    instance.problem = original
    assert instance.problem == original

@given(instance=spem::uma::Practice_strategy)
def test_spem::uma::practice_background_type(instance):
    assert isinstance(instance.background, str)


@given(instance=spem::uma::Practice_strategy)
def test_spem::uma::practice_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original

@given(instance=spem::uma::Practice_strategy)
def test_spem::uma::practice_goal_type(instance):
    assert isinstance(instance.goal, str)


@given(instance=spem::uma::Practice_strategy)
def test_spem::uma::practice_goal_setter(instance):
    original = instance.goal
    instance.goal = original
    assert instance.goal == original

@given(instance=spem::uma::Practice_strategy)
def test_spem::uma::practice_levelOfAdoption_type(instance):
    assert isinstance(instance.levelOfAdoption, str)


@given(instance=spem::uma::Practice_strategy)
def test_spem::uma::practice_levelOfAdoption_setter(instance):
    original = instance.levelOfAdoption
    instance.levelOfAdoption = original
    assert instance.levelOfAdoption == original

@given(instance=spem::uma::Practice_strategy)
def test_spem::uma::practice_application_type(instance):
    assert isinstance(instance.application, str)


@given(instance=spem::uma::Practice_strategy)
def test_spem::uma::practice_application_setter(instance):
    original = instance.application
    instance.application = original
    assert instance.application == original

@given(instance=spem::uma::Practice_strategy)
def test_spem::uma::practice_additionalInfo_type(instance):
    assert isinstance(instance.additionalInfo, str)


@given(instance=spem::uma::Practice_strategy)
def test_spem::uma::practice_additionalInfo_setter(instance):
    original = instance.additionalInfo
    instance.additionalInfo = original
    assert instance.additionalInfo == original

@given(instance=spem::uma::SupportingMaterial_strategy)
@settings(max_examples=50)
def test_spem::uma::supportingmaterial_instantiation(instance):
    assert isinstance(instance, spem::uma::SupportingMaterial)

@given(instance=spem::uma::Checklist_strategy)
@settings(max_examples=50)
def test_spem::uma::checklist_instantiation(instance):
    assert isinstance(instance, spem::uma::Checklist)

@given(instance=uma::spem::TaskDefinition_strategy)
@settings(max_examples=50)
def test_uma::spem::taskdefinition_instantiation(instance):
    assert isinstance(instance, uma::spem::TaskDefinition)

@given(instance=Process_strategy)
@settings(max_examples=50)
def test_process_instantiation(instance):
    assert isinstance(instance, Process)

@given(instance=spem::uma::ProcessPlanningTemplate_strategy)
@settings(max_examples=50)
def test_spem::uma::processplanningtemplate_instantiation(instance):
    assert isinstance(instance, spem::uma::ProcessPlanningTemplate)

@given(instance=spem::uma::DeliveryProcess_strategy)
@settings(max_examples=50)
def test_spem::uma::deliveryprocess_instantiation(instance):
    assert isinstance(instance, spem::uma::DeliveryProcess)

@given(instance=spem::uma::DeliveryProcess_strategy)
def test_spem::uma::deliveryprocess_scale_type(instance):
    assert isinstance(instance.scale, str)


@given(instance=spem::uma::DeliveryProcess_strategy)
def test_spem::uma::deliveryprocess_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=spem::uma::DeliveryProcess_strategy)
def test_spem::uma::deliveryprocess_estimatingTechnique_type(instance):
    assert isinstance(instance.estimatingTechnique, str)


@given(instance=spem::uma::DeliveryProcess_strategy)
def test_spem::uma::deliveryprocess_estimatingTechnique_setter(instance):
    original = instance.estimatingTechnique
    instance.estimatingTechnique = original
    assert instance.estimatingTechnique == original

@given(instance=spem::uma::DeliveryProcess_strategy)
def test_spem::uma::deliveryprocess_typeOfContract_type(instance):
    assert isinstance(instance.typeOfContract, str)


@given(instance=spem::uma::DeliveryProcess_strategy)
def test_spem::uma::deliveryprocess_typeOfContract_setter(instance):
    original = instance.typeOfContract
    instance.typeOfContract = original
    assert instance.typeOfContract == original

@given(instance=spem::uma::DeliveryProcess_strategy)
def test_spem::uma::deliveryprocess_projectMemberExpertise_type(instance):
    assert isinstance(instance.projectMemberExpertise, str)


@given(instance=spem::uma::DeliveryProcess_strategy)
def test_spem::uma::deliveryprocess_projectMemberExpertise_setter(instance):
    original = instance.projectMemberExpertise
    instance.projectMemberExpertise = original
    assert instance.projectMemberExpertise == original

@given(instance=spem::uma::DeliveryProcess_strategy)
def test_spem::uma::deliveryprocess_riskLevel_type(instance):
    assert isinstance(instance.riskLevel, str)


@given(instance=spem::uma::DeliveryProcess_strategy)
def test_spem::uma::deliveryprocess_riskLevel_setter(instance):
    original = instance.riskLevel
    instance.riskLevel = original
    assert instance.riskLevel == original

@given(instance=spem::uma::DeliveryProcess_strategy)
def test_spem::uma::deliveryprocess_projectCharacteristics_type(instance):
    assert isinstance(instance.projectCharacteristics, str)


@given(instance=spem::uma::DeliveryProcess_strategy)
def test_spem::uma::deliveryprocess_projectCharacteristics_setter(instance):
    original = instance.projectCharacteristics
    instance.projectCharacteristics = original
    assert instance.projectCharacteristics == original

@given(instance=spem::uma::CapabilityPattern_strategy)
@settings(max_examples=50)
def test_spem::uma::capabilitypattern_instantiation(instance):
    assert isinstance(instance, spem::uma::CapabilityPattern)

@given(instance=spem::uma::Discipline_strategy)
@settings(max_examples=50)
def test_spem::uma::discipline_instantiation(instance):
    assert isinstance(instance, spem::uma::Discipline)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=WorkProductUse_strategy)
@settings(max_examples=50)
def test_workproductuse_instantiation(instance):
    assert isinstance(instance, WorkProductUse)

@given(instance=spem::uma::Deliverable_strategy)
@settings(max_examples=50)
def test_spem::uma::deliverable_instantiation(instance):
    assert isinstance(instance, spem::uma::Deliverable)

@given(instance=spem::uma::Deliverable_strategy)
def test_spem::uma::deliverable_externalDescription_type(instance):
    assert isinstance(instance.externalDescription, str)


@given(instance=spem::uma::Deliverable_strategy)
def test_spem::uma::deliverable_externalDescription_setter(instance):
    original = instance.externalDescription
    instance.externalDescription = original
    assert instance.externalDescription == original

@given(instance=spem::uma::Deliverable_strategy)
def test_spem::uma::deliverable_packagingGuidance_type(instance):
    assert isinstance(instance.packagingGuidance, str)


@given(instance=spem::uma::Deliverable_strategy)
def test_spem::uma::deliverable_packagingGuidance_setter(instance):
    original = instance.packagingGuidance
    instance.packagingGuidance = original
    assert instance.packagingGuidance == original

@given(instance=spem::uma::Outcome_strategy)
@settings(max_examples=50)
def test_spem::uma::outcome_instantiation(instance):
    assert isinstance(instance, spem::uma::Outcome)

@given(instance=spem::uma::Artifact_strategy)
@settings(max_examples=50)
def test_spem::uma::artifact_instantiation(instance):
    assert isinstance(instance, spem::uma::Artifact)

@given(instance=MethodLibraryPackageableElement_strategy)
@settings(max_examples=50)
def test_methodlibrarypackageableelement_instantiation(instance):
    assert isinstance(instance, MethodLibraryPackageableElement)

@given(instance=spem::MethodPluginPackageableElement_strategy)
@settings(max_examples=50)
def test_spem::methodpluginpackageableelement_instantiation(instance):
    assert isinstance(instance, spem::MethodPluginPackageableElement)

@given(instance=spem::MethodLibraryPackageableElement_strategy)
@settings(max_examples=50)
def test_spem::methodlibrarypackageableelement_instantiation(instance):
    assert isinstance(instance, spem::MethodLibraryPackageableElement)

@given(instance=spem::MethodLibraryPackageableElement_strategy)
def test_spem::methodlibrarypackageableelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=spem::MethodLibraryPackageableElement_strategy)
def test_spem::methodlibrarypackageableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=spem::MethodLibrary_strategy)
@settings(max_examples=50)
def test_spem::methodlibrary_instantiation(instance):
    assert isinstance(instance, spem::MethodLibrary)

@given(instance=spem::MethodLibrary_strategy)
def test_spem::methodlibrary_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=spem::MethodLibrary_strategy)
def test_spem::methodlibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=spem::MethodPlugin_strategy)
@settings(max_examples=50)
def test_spem::methodplugin_instantiation(instance):
    assert isinstance(instance, spem::MethodPlugin)

@given(instance=ProcessPackage_strategy)
@settings(max_examples=50)
def test_processpackage_instantiation(instance):
    assert isinstance(instance, ProcessPackage)

@given(instance=spem::uma::CapabilityPatternPackage_strategy)
@settings(max_examples=50)
def test_spem::uma::capabilitypatternpackage_instantiation(instance):
    assert isinstance(instance, spem::uma::CapabilityPatternPackage)

@given(instance=spem::uma::ProcessComponentPackage_strategy)
@settings(max_examples=50)
def test_spem::uma::processcomponentpackage_instantiation(instance):
    assert isinstance(instance, spem::uma::ProcessComponentPackage)

@given(instance=spem::uma::DeliveryProcessPackage_strategy)
@settings(max_examples=50)
def test_spem::uma::deliveryprocesspackage_instantiation(instance):
    assert isinstance(instance, spem::uma::DeliveryProcessPackage)

@given(instance=spem::ProcessComponent_strategy)
@settings(max_examples=50)
def test_spem::processcomponent_instantiation(instance):
    assert isinstance(instance, spem::ProcessComponent)

@given(instance=spem::VariabilityElement_strategy)
@settings(max_examples=50)
def test_spem::variabilityelement_instantiation(instance):
    assert isinstance(instance, spem::VariabilityElement)

@given(instance=spem::VariabilityElement_strategy)
def test_spem::variabilityelement_variabilityType_type(instance):
    assert isinstance(instance.variabilityType, str)


@given(instance=spem::VariabilityElement_strategy)
def test_spem::variabilityelement_variabilityType_setter(instance):
    original = instance.variabilityType
    instance.variabilityType = original
    assert instance.variabilityType == original

@given(instance=RoleUse_strategy)
@settings(max_examples=50)
def test_roleuse_instantiation(instance):
    assert isinstance(instance, RoleUse)

@given(instance=spem::CompositeRole_strategy)
@settings(max_examples=50)
def test_spem::compositerole_instantiation(instance):
    assert isinstance(instance, spem::CompositeRole)

@given(instance=Kind_strategy)
@settings(max_examples=50)
def test_kind_instantiation(instance):
    assert isinstance(instance, Kind)

@given(instance=MethodPluginPackageableElement_strategy)
@settings(max_examples=50)
def test_methodpluginpackageableelement_instantiation(instance):
    assert isinstance(instance, MethodPluginPackageableElement)

@given(instance=spem::ProcessPackageableElement_strategy)
@settings(max_examples=50)
def test_spem::processpackageableelement_instantiation(instance):
    assert isinstance(instance, spem::ProcessPackageableElement)

@given(instance=spem::ProcessPackageableElement_strategy)
def test_spem::processpackageableelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=spem::ProcessPackageableElement_strategy)
def test_spem::processpackageableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=spem::MethodContentPackageableElement_strategy)
@settings(max_examples=50)
def test_spem::methodcontentpackageableelement_instantiation(instance):
    assert isinstance(instance, spem::MethodContentPackageableElement)

@given(instance=spem::MethodContentPackageableElement_strategy)
def test_spem::methodcontentpackageableelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=spem::MethodContentPackageableElement_strategy)
def test_spem::methodcontentpackageableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MethodContentPackageableElement_strategy)
@settings(max_examples=50)
def test_methodcontentpackageableelement_instantiation(instance):
    assert isinstance(instance, MethodContentPackageableElement)

@given(instance=spem::MethodContentPackage_strategy)
@settings(max_examples=50)
def test_spem::methodcontentpackage_instantiation(instance):
    assert isinstance(instance, spem::MethodContentPackage)

@given(instance=MethodContentElement_strategy)
@settings(max_examples=50)
def test_methodcontentelement_instantiation(instance):
    assert isinstance(instance, MethodContentElement)

@given(instance=spem::Default::ResponsibilityAssignment_strategy)
@settings(max_examples=50)
def test_spem::default::responsibilityassignment_instantiation(instance):
    assert isinstance(instance, spem::Default::ResponsibilityAssignment)

@given(instance=spem::MethodContentKind_strategy)
@settings(max_examples=50)
def test_spem::methodcontentkind_instantiation(instance):
    assert isinstance(instance, spem::MethodContentKind)

@given(instance=spem::WorkProductDefinition_strategy)
@settings(max_examples=50)
def test_spem::workproductdefinition_instantiation(instance):
    assert isinstance(instance, spem::WorkProductDefinition)

@given(instance=spem::uma::RoleSet_strategy)
@settings(max_examples=50)
def test_spem::uma::roleset_instantiation(instance):
    assert isinstance(instance, spem::uma::RoleSet)

@given(instance=spem::Default::TaskDefinitionPerformer_strategy)
@settings(max_examples=50)
def test_spem::default::taskdefinitionperformer_instantiation(instance):
    assert isinstance(instance, spem::Default::TaskDefinitionPerformer)

@given(instance=spem::WorkProductDefinitionRelationship_strategy)
@settings(max_examples=50)
def test_spem::workproductdefinitionrelationship_instantiation(instance):
    assert isinstance(instance, spem::WorkProductDefinitionRelationship)

@given(instance=spem::uma::WorkProductKind_strategy)
@settings(max_examples=50)
def test_spem::uma::workproductkind_instantiation(instance):
    assert isinstance(instance, spem::uma::WorkProductKind)

@given(instance=spem::ToolDefinition_strategy)
@settings(max_examples=50)
def test_spem::tooldefinition_instantiation(instance):
    assert isinstance(instance, spem::ToolDefinition)

@given(instance=spem::Category_strategy)
@settings(max_examples=50)
def test_spem::category_instantiation(instance):
    assert isinstance(instance, spem::Category)

@given(instance=spem::Guidance_strategy)
@settings(max_examples=50)
def test_spem::guidance_instantiation(instance):
    assert isinstance(instance, spem::Guidance)

@given(instance=ProcessPackageableElement_strategy)
@settings(max_examples=50)
def test_processpackageableelement_instantiation(instance):
    assert isinstance(instance, ProcessPackageableElement)

@given(instance=spem::ProcessPackage_strategy)
@settings(max_examples=50)
def test_spem::processpackage_instantiation(instance):
    assert isinstance(instance, spem::ProcessPackage)

@given(instance=DescribableElement_strategy)
@settings(max_examples=50)
def test_describableelement_instantiation(instance):
    assert isinstance(instance, DescribableElement)

@given(instance=spem::Metric_strategy)
@settings(max_examples=50)
def test_spem::metric_instantiation(instance):
    assert isinstance(instance, spem::Metric)

@given(instance=spem::Metric_strategy)
def test_spem::metric_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=spem::Metric_strategy)
def test_spem::metric_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=spem::ProcessElement_strategy)
@settings(max_examples=50)
def test_spem::processelement_instantiation(instance):
    assert isinstance(instance, spem::ProcessElement)

@given(instance=WorkDefinitionParameter_strategy)
@settings(max_examples=50)
def test_workdefinitionparameter_instantiation(instance):
    assert isinstance(instance, WorkDefinitionParameter)

@given(instance=spem::Default::TaskDefinitionParameter_strategy)
@settings(max_examples=50)
def test_spem::default::taskdefinitionparameter_instantiation(instance):
    assert isinstance(instance, spem::Default::TaskDefinitionParameter)

@given(instance=spem::Default::TaskDefinitionParameter_strategy)
def test_spem::default::taskdefinitionparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=spem::Default::TaskDefinitionParameter_strategy)
def test_spem::default::taskdefinitionparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=spem::Default::TaskDefinitionParameter_strategy)
def test_spem::default::taskdefinitionparameter_optionality_type(instance):
    assert isinstance(instance.optionality, str)


@given(instance=spem::Default::TaskDefinitionParameter_strategy)
def test_spem::default::taskdefinitionparameter_optionality_setter(instance):
    original = instance.optionality
    instance.optionality = original
    assert instance.optionality == original

@given(instance=VariabilityElement_strategy)
@settings(max_examples=50)
def test_variabilityelement_instantiation(instance):
    assert isinstance(instance, VariabilityElement)

@given(instance=spem::MethodContentElement_strategy)
@settings(max_examples=50)
def test_spem::methodcontentelement_instantiation(instance):
    assert isinstance(instance, spem::MethodContentElement)

@given(instance=WorkBreakdownElement_strategy)
@settings(max_examples=50)
def test_workbreakdownelement_instantiation(instance):
    assert isinstance(instance, WorkBreakdownElement)

@given(instance=spem::Milestone_strategy)
@settings(max_examples=50)
def test_spem::milestone_instantiation(instance):
    assert isinstance(instance, spem::Milestone)

@given(instance=WorkDefinition_strategy)
@settings(max_examples=50)
def test_workdefinition_instantiation(instance):
    assert isinstance(instance, WorkDefinition)

@given(instance=spem::TaskDefinition_strategy)
@settings(max_examples=50)
def test_spem::taskdefinition_instantiation(instance):
    assert isinstance(instance, spem::TaskDefinition)

@given(instance=spem::Step_strategy)
@settings(max_examples=50)
def test_spem::step_instantiation(instance):
    assert isinstance(instance, spem::Step)

@given(instance=spem::Step_strategy)
def test_spem::step_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=spem::Step_strategy)
def test_spem::step_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=spem::Activity_strategy)
@settings(max_examples=50)
def test_spem::activity_instantiation(instance):
    assert isinstance(instance, spem::Activity)

@given(instance=spem::Activity_strategy)
def test_spem::activity_useKind_type(instance):
    assert isinstance(instance.useKind, str)


@given(instance=spem::Activity_strategy)
def test_spem::activity_useKind_setter(instance):
    original = instance.useKind
    instance.useKind = original
    assert instance.useKind == original

@given(instance=spem::Activity_strategy)
def test_spem::activity_isEnactable_type(instance):
    assert isinstance(instance.isEnactable, bool)


@given(instance=spem::Activity_strategy)
def test_spem::activity_isEnactable_setter(instance):
    original = instance.isEnactable
    instance.isEnactable = original
    assert instance.isEnactable == original

@given(instance=spem::Qualification_strategy)
@settings(max_examples=50)
def test_spem::qualification_instantiation(instance):
    assert isinstance(instance, spem::Qualification)

@given(instance=spem::RoleDefinition_strategy)
@settings(max_examples=50)
def test_spem::roledefinition_instantiation(instance):
    assert isinstance(instance, spem::RoleDefinition)

@given(instance=spem::RoleDefinition_strategy)
def test_spem::roledefinition_synonym_type(instance):
    assert isinstance(instance.synonym, str)


@given(instance=spem::RoleDefinition_strategy)
def test_spem::roledefinition_synonym_setter(instance):
    original = instance.synonym
    instance.synonym = original
    assert instance.synonym == original

@given(instance=MethodContentUse_strategy)
@settings(max_examples=50)
def test_methodcontentuse_instantiation(instance):
    assert isinstance(instance, MethodContentUse)

@given(instance=spem::WorkProductUse_strategy)
@settings(max_examples=50)
def test_spem::workproductuse_instantiation(instance):
    assert isinstance(instance, spem::WorkProductUse)

@given(instance=spem::ProcessComponentUse_strategy)
@settings(max_examples=50)
def test_spem::processcomponentuse_instantiation(instance):
    assert isinstance(instance, spem::ProcessComponentUse)

@given(instance=spem::TaskUse_strategy)
@settings(max_examples=50)
def test_spem::taskuse_instantiation(instance):
    assert isinstance(instance, spem::TaskUse)

@given(instance=spem::TaskUse_strategy)
def test_spem::taskuse_preCondition_type(instance):
    assert isinstance(instance.preCondition, str)


@given(instance=spem::TaskUse_strategy)
def test_spem::taskuse_preCondition_setter(instance):
    original = instance.preCondition
    instance.preCondition = original
    assert instance.preCondition == original

@given(instance=spem::TaskUse_strategy)
def test_spem::taskuse_postCondition_type(instance):
    assert isinstance(instance.postCondition, str)


@given(instance=spem::TaskUse_strategy)
def test_spem::taskuse_postCondition_setter(instance):
    original = instance.postCondition
    instance.postCondition = original
    assert instance.postCondition == original

@given(instance=spem::RoleUse_strategy)
@settings(max_examples=50)
def test_spem::roleuse_instantiation(instance):
    assert isinstance(instance, spem::RoleUse)

@given(instance=WorkDefinitionPerformer_strategy)
@settings(max_examples=50)
def test_workdefinitionperformer_instantiation(instance):
    assert isinstance(instance, WorkDefinitionPerformer)

@given(instance=spem::MethodConfiguration_strategy)
@settings(max_examples=50)
def test_spem::methodconfiguration_instantiation(instance):
    assert isinstance(instance, spem::MethodConfiguration)

@given(instance=spem::WorkDefinitionParameter_strategy)
@settings(max_examples=50)
def test_spem::workdefinitionparameter_instantiation(instance):
    assert isinstance(instance, spem::WorkDefinitionParameter)

@given(instance=spem::WorkDefinitionParameter_strategy)
def test_spem::workdefinitionparameter_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=spem::WorkDefinitionParameter_strategy)
def test_spem::workdefinitionparameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=BreakdownElement_strategy)
@settings(max_examples=50)
def test_breakdownelement_instantiation(instance):
    assert isinstance(instance, BreakdownElement)

@given(instance=spem::WorkProductUseRelationship_strategy)
@settings(max_examples=50)
def test_spem::workproductuserelationship_instantiation(instance):
    assert isinstance(instance, spem::WorkProductUseRelationship)

@given(instance=spem::WorkProductUseRelationship_strategy)
def test_spem::workproductuserelationship_relationshipKind_type(instance):
    assert isinstance(instance.relationshipKind, str)


@given(instance=spem::WorkProductUseRelationship_strategy)
def test_spem::workproductuserelationship_relationshipKind_setter(instance):
    original = instance.relationshipKind
    instance.relationshipKind = original
    assert instance.relationshipKind == original

@given(instance=spem::activity::Edge_strategy)
@settings(max_examples=50)
def test_spem::activity::edge_instantiation(instance):
    assert isinstance(instance, spem::activity::Edge)

@given(instance=spem::activity::Edge_strategy)
def test_spem::activity::edge_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=spem::activity::Edge_strategy)
def test_spem::activity::edge_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=spem::ProcessPerformer_strategy)
@settings(max_examples=50)
def test_spem::processperformer_instantiation(instance):
    assert isinstance(instance, spem::ProcessPerformer)

@given(instance=spem::WorkSequence_strategy)
@settings(max_examples=50)
def test_spem::worksequence_instantiation(instance):
    assert isinstance(instance, spem::WorkSequence)

@given(instance=spem::WorkSequence_strategy)
def test_spem::worksequence_linkKind_type(instance):
    assert isinstance(instance.linkKind, str)


@given(instance=spem::WorkSequence_strategy)
def test_spem::worksequence_linkKind_setter(instance):
    original = instance.linkKind
    instance.linkKind = original
    assert instance.linkKind == original

@given(instance=spem::TeamProfile_strategy)
@settings(max_examples=50)
def test_spem::teamprofile_instantiation(instance):
    assert isinstance(instance, spem::TeamProfile)

@given(instance=spem::MethodContentUse_strategy)
@settings(max_examples=50)
def test_spem::methodcontentuse_instantiation(instance):
    assert isinstance(instance, spem::MethodContentUse)

@given(instance=spem::MethodContentUse_strategy)
def test_spem::methodcontentuse_isSynchronizedWithSource_type(instance):
    assert isinstance(instance.isSynchronizedWithSource, bool)


@given(instance=spem::MethodContentUse_strategy)
def test_spem::methodcontentuse_isSynchronizedWithSource_setter(instance):
    original = instance.isSynchronizedWithSource
    instance.isSynchronizedWithSource = original
    assert instance.isSynchronizedWithSource == original

@given(instance=spem::ProcessResponsibilityAssignment_strategy)
@settings(max_examples=50)
def test_spem::processresponsibilityassignment_instantiation(instance):
    assert isinstance(instance, spem::ProcessResponsibilityAssignment)

@given(instance=spem::ProcessParameter_strategy)
@settings(max_examples=50)
def test_spem::processparameter_instantiation(instance):
    assert isinstance(instance, spem::ProcessParameter)

@given(instance=spem::ProcessParameter_strategy)
def test_spem::processparameter_optionality_type(instance):
    assert isinstance(instance.optionality, str)


@given(instance=spem::ProcessParameter_strategy)
def test_spem::processparameter_optionality_setter(instance):
    original = instance.optionality
    instance.optionality = original
    assert instance.optionality == original

@given(instance=spem::activity::Node_strategy)
@settings(max_examples=50)
def test_spem::activity::node_instantiation(instance):
    assert isinstance(instance, spem::activity::Node)

@given(instance=spem::WorkBreakdownElement_strategy)
@settings(max_examples=50)
def test_spem::workbreakdownelement_instantiation(instance):
    assert isinstance(instance, spem::WorkBreakdownElement)

@given(instance=spem::WorkBreakdownElement_strategy)
def test_spem::workbreakdownelement_isEventDriven_type(instance):
    assert isinstance(instance.isEventDriven, bool)


@given(instance=spem::WorkBreakdownElement_strategy)
def test_spem::workbreakdownelement_isEventDriven_setter(instance):
    original = instance.isEventDriven
    instance.isEventDriven = original
    assert instance.isEventDriven == original

@given(instance=spem::WorkBreakdownElement_strategy)
def test_spem::workbreakdownelement_isOngoing_type(instance):
    assert isinstance(instance.isOngoing, bool)


@given(instance=spem::WorkBreakdownElement_strategy)
def test_spem::workbreakdownelement_isOngoing_setter(instance):
    original = instance.isOngoing
    instance.isOngoing = original
    assert instance.isOngoing == original

@given(instance=spem::WorkBreakdownElement_strategy)
def test_spem::workbreakdownelement_isRepeatable_type(instance):
    assert isinstance(instance.isRepeatable, bool)


@given(instance=spem::WorkBreakdownElement_strategy)
def test_spem::workbreakdownelement_isRepeatable_setter(instance):
    original = instance.isRepeatable
    instance.isRepeatable = original
    assert instance.isRepeatable == original

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

@given(instance=spem::WorkProductPort_strategy)
@settings(max_examples=50)
def test_spem::workproductport_instantiation(instance):
    assert isinstance(instance, spem::WorkProductPort)

@given(instance=spem::WorkProductPort_strategy)
def test_spem::workproductport_isOptional_type(instance):
    assert isinstance(instance.isOptional, bool)


@given(instance=spem::WorkProductPort_strategy)
def test_spem::workproductport_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=spem::WorkProductPort_strategy)
def test_spem::workproductport_portKind_type(instance):
    assert isinstance(instance.portKind, str)


@given(instance=spem::WorkProductPort_strategy)
def test_spem::workproductport_portKind_setter(instance):
    original = instance.portKind
    instance.portKind = original
    assert instance.portKind == original

@given(instance=spem::WorkProductPortConnector_strategy)
@settings(max_examples=50)
def test_spem::workproductportconnector_instantiation(instance):
    assert isinstance(instance, spem::WorkProductPortConnector)

@given(instance=spem::PlanningData_strategy)
@settings(max_examples=50)
def test_spem::planningdata_instantiation(instance):
    assert isinstance(instance, spem::PlanningData)

@given(instance=spem::PlanningData_strategy)
def test_spem::planningdata_startDate_type(instance):
    assert isinstance(instance.startDate, date)


@given(instance=spem::PlanningData_strategy)
def test_spem::planningdata_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original

@given(instance=spem::PlanningData_strategy)
def test_spem::planningdata_finishDate_type(instance):
    assert isinstance(instance.finishDate, date)


@given(instance=spem::PlanningData_strategy)
def test_spem::planningdata_finishDate_setter(instance):
    original = instance.finishDate
    instance.finishDate = original
    assert instance.finishDate == original

@given(instance=spem::PlanningData_strategy)
def test_spem::planningdata_duration_type(instance):
    assert isinstance(instance.duration, str)


@given(instance=spem::PlanningData_strategy)
def test_spem::planningdata_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=spem::PlanningData_strategy)
def test_spem::planningdata_rank_type(instance):
    assert isinstance(instance.rank, int)


@given(instance=spem::PlanningData_strategy)
def test_spem::planningdata_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=spem::ProcessKind_strategy)
@settings(max_examples=50)
def test_spem::processkind_instantiation(instance):
    assert isinstance(instance, spem::ProcessKind)

@given(instance=spem::BreakdownElement_strategy)
@settings(max_examples=50)
def test_spem::breakdownelement_instantiation(instance):
    assert isinstance(instance, spem::BreakdownElement)

@given(instance=spem::BreakdownElement_strategy)
def test_spem::breakdownelement_isPlanned_type(instance):
    assert isinstance(instance.isPlanned, bool)


@given(instance=spem::BreakdownElement_strategy)
def test_spem::breakdownelement_isPlanned_setter(instance):
    original = instance.isPlanned
    instance.isPlanned = original
    assert instance.isPlanned == original

@given(instance=spem::BreakdownElement_strategy)
def test_spem::breakdownelement_isOptional_type(instance):
    assert isinstance(instance.isOptional, bool)


@given(instance=spem::BreakdownElement_strategy)
def test_spem::breakdownelement_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=spem::BreakdownElement_strategy)
def test_spem::breakdownelement_hasMultipleOccurrences_type(instance):
    assert isinstance(instance.hasMultipleOccurrences, bool)


@given(instance=spem::BreakdownElement_strategy)
def test_spem::breakdownelement_hasMultipleOccurrences_setter(instance):
    original = instance.hasMultipleOccurrences
    instance.hasMultipleOccurrences = original
    assert instance.hasMultipleOccurrences == original

@given(instance=spem::WorkDefinition_strategy)
@settings(max_examples=50)
def test_spem::workdefinition_instantiation(instance):
    assert isinstance(instance, spem::WorkDefinition)

@given(instance=spem::WorkDefinition_strategy)
def test_spem::workdefinition_preCondition_type(instance):
    assert isinstance(instance.preCondition, str)


@given(instance=spem::WorkDefinition_strategy)
def test_spem::workdefinition_preCondition_setter(instance):
    original = instance.preCondition
    instance.preCondition = original
    assert instance.preCondition == original

@given(instance=spem::WorkDefinition_strategy)
def test_spem::workdefinition_postCondition_type(instance):
    assert isinstance(instance.postCondition, str)


@given(instance=spem::WorkDefinition_strategy)
def test_spem::workdefinition_postCondition_setter(instance):
    original = instance.postCondition
    instance.postCondition = original
    assert instance.postCondition == original

@given(instance=spem::WorkDefinitionPerformer_strategy)
@settings(max_examples=50)
def test_spem::workdefinitionperformer_instantiation(instance):
    assert isinstance(instance, spem::WorkDefinitionPerformer)

@given(instance=ExtensibleElement_strategy)
@settings(max_examples=50)
def test_extensibleelement_instantiation(instance):
    assert isinstance(instance, ExtensibleElement)

@given(instance=spem::DescribableElement_strategy)
@settings(max_examples=50)
def test_spem::describableelement_instantiation(instance):
    assert isinstance(instance, spem::DescribableElement)

@given(instance=spem::DescribableElement_strategy)
def test_spem::describableelement_briefDescription_type(instance):
    assert isinstance(instance.briefDescription, str)


@given(instance=spem::DescribableElement_strategy)
def test_spem::describableelement_briefDescription_setter(instance):
    original = instance.briefDescription
    instance.briefDescription = original
    assert instance.briefDescription == original

@given(instance=spem::DescribableElement_strategy)
def test_spem::describableelement_purpose_type(instance):
    assert isinstance(instance.purpose, str)


@given(instance=spem::DescribableElement_strategy)
def test_spem::describableelement_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original

@given(instance=spem::DescribableElement_strategy)
def test_spem::describableelement_mainDescription_type(instance):
    assert isinstance(instance.mainDescription, str)


@given(instance=spem::DescribableElement_strategy)
def test_spem::describableelement_mainDescription_setter(instance):
    original = instance.mainDescription
    instance.mainDescription = original
    assert instance.mainDescription == original

@given(instance=spem::DescribableElement_strategy)
def test_spem::describableelement_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=spem::DescribableElement_strategy)
def test_spem::describableelement_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=spem::DescribableElement_strategy)
def test_spem::describableelement_changeDate_type(instance):
    assert isinstance(instance.changeDate, date)


@given(instance=spem::DescribableElement_strategy)
def test_spem::describableelement_changeDate_setter(instance):
    original = instance.changeDate
    instance.changeDate = original
    assert instance.changeDate == original

@given(instance=spem::DescribableElement_strategy)
def test_spem::describableelement_presentationName_type(instance):
    assert isinstance(instance.presentationName, str)


@given(instance=spem::DescribableElement_strategy)
def test_spem::describableelement_presentationName_setter(instance):
    original = instance.presentationName
    instance.presentationName = original
    assert instance.presentationName == original

@given(instance=spem::DescribableElement_strategy)
def test_spem::describableelement_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=spem::DescribableElement_strategy)
def test_spem::describableelement_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=spem::DescribableElement_strategy)
def test_spem::describableelement_changeDescription_type(instance):
    assert isinstance(instance.changeDescription, str)


@given(instance=spem::DescribableElement_strategy)
def test_spem::describableelement_changeDescription_setter(instance):
    original = instance.changeDescription
    instance.changeDescription = original
    assert instance.changeDescription == original

@given(instance=spem::DescribableElement_strategy)
def test_spem::describableelement_copyright_type(instance):
    assert isinstance(instance.copyright, str)


@given(instance=spem::DescribableElement_strategy)
def test_spem::describableelement_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original

@given(instance=spem::Kind_strategy)
@settings(max_examples=50)
def test_spem::kind_instantiation(instance):
    assert isinstance(instance, spem::Kind)

@given(instance=spem::ExtensibleElement_strategy)
@settings(max_examples=50)
def test_spem::extensibleelement_instantiation(instance):
    assert isinstance(instance, spem::ExtensibleElement)

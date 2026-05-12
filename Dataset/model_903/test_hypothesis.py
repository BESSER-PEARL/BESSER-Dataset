import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    spem_activity_EndNode,
    spem_activity_JoinNode,
    spem_activity_ForkNode,
    spem_activity_DecisionNode,
    spem_activity_StartNode,
    activity_spem_BreakdownElement,
    Edge,
    uma_spem_MethodContentElement,
    uma_spem_Activity,
    Practice,
    uma_spem_WorkProductDefinition,
    Concept,
    spem_uma_Whitepaper,
    uma_spem_RoleDefinition,
    SupportingMaterial,
    uma_spem_WorkProductPortConnector,
    CapabilityPattern,
    Activity,
    spem_uma_Iteration,
    spem_uma_Phase,
    spem_uma_Process,
    uma_spem_MethodPlugin,
    uma_spem_MethodLibrary,
    uma_spem_WorkProductUse,
    uma_spem_MethodConfiguration,
    spem_uma_Root,
    Category,
    spem_uma_Domain,
    spem_uma_DisciplineGrouping,
    spem_uma_CustomCategory,
    MethodContentPackage,
    spem_uma_GuidancePackage,
    spem_uma_RoleSetPackage,
    spem_uma_ConfigurationPackage,
    spem_uma_DisciplinePackage,
    spem_uma_RoleDefinitionPackage,
    spem_uma_ToolDefinitionPackage,
    spem_uma_WorkProductKindPackage,
    spem_uma_DomainPackage,
    spem_uma_WorkProductDefinitionPackage,
    spem_uma_QualificationPackage,
    spem_uma_TaskDefinitionPackage,
    spem_uma_CategoryPackage,
    Guidance,
    spem_uma_EstimatingConsideration,
    spem_uma_Template,
    spem_uma_Practice,
    spem_uma_TermDefinition,
    spem_uma_Guideline,
    spem_uma_Roadmap,
    spem_uma_Example,
    spem_uma_SupportingMaterial,
    spem_uma_ToolMentor,
    spem_uma_Concept,
    spem_uma_ReusableAsset,
    spem_uma_Report,
    spem_uma_Checklist,
    uma_spem_TaskDefinition,
    Process,
    spem_uma_ProcessPlanningTemplate,
    spem_uma_DeliveryProcess,
    spem_uma_CapabilityPattern,
    spem_uma_Discipline,
    Artifact,
    WorkProductUse,
    spem_uma_Outcome,
    spem_uma_Deliverable,
    spem_uma_Artifact,
    MethodLibraryPackageableElement,
    spem_MethodPluginPackageableElement,
    spem_MethodLibraryPackageableElement,
    spem_MethodLibrary,
    spem_MethodPlugin,
    ProcessPackage,
    spem_uma_DeliveryProcessPackage,
    spem_uma_ProcessComponentPackage,
    spem_uma_CapabilityPatternPackage,
    spem_ProcessComponent,
    spem_VariabilityElement,
    RoleUse,
    spem_CompositeRole,
    Kind,
    MethodPluginPackageableElement,
    spem_ProcessPackageableElement,
    spem_MethodContentPackageableElement,
    MethodContentPackageableElement,
    spem_MethodContentPackage,
    MethodContentElement,
    spem_Default_ResponsibilityAssignment,
    spem_uma_RoleSet,
    spem_Default_TaskDefinitionPerformer,
    spem_MethodContentKind,
    spem_ToolDefinition,
    spem_WorkProductDefinition,
    spem_uma_WorkProductKind,
    spem_WorkProductDefinitionRelationship,
    spem_Category,
    spem_Guidance,
    ProcessPackageableElement,
    spem_ProcessPackage,
    DescribableElement,
    spem_Metric,
    spem_ProcessElement,
    WorkDefinitionParameter,
    spem_Default_TaskDefinitionParameter,
    VariabilityElement,
    spem_MethodContentElement,
    WorkBreakdownElement,
    spem_Milestone,
    WorkDefinition,
    spem_TaskDefinition,
    spem_Step,
    spem_Activity,
    spem_Qualification,
    spem_RoleDefinition,
    MethodContentUse,
    spem_ProcessComponentUse,
    spem_WorkProductUse,
    spem_TaskUse,
    spem_RoleUse,
    WorkDefinitionPerformer,
    spem_MethodConfiguration,
    spem_WorkDefinitionParameter,
    BreakdownElement,
    spem_ProcessPerformer,
    spem_ProcessResponsibilityAssignment,
    spem_MethodContentUse,
    spem_activity_Edge,
    spem_TeamProfile,
    spem_activity_Node,
    spem_ProcessParameter,
    spem_WorkProductUseRelationship,
    spem_WorkSequence,
    spem_WorkBreakdownElement,
    ProcessElement,
    spem_WorkProductPortConnector,
    spem_PlanningData,
    spem_WorkProductPort,
    spem_ProcessKind,
    spem_BreakdownElement,
    spem_WorkDefinition,
    spem_WorkDefinitionPerformer,
    ExtensibleElement,
    spem_DescribableElement,
    spem_Kind,
    spem_ExtensibleElement,
    ContractKind,
    RiskLevel,
    EstimatingTechnique,
    ParameterDirectionKind,
    VariabilityType,
    ExpertiseLevel,
    WorkSequenceKind,
    WorkProductRelationshipKind,
    ActivityUseKind,
    OptionalityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_spem_activity_endnode_is_not_abstract():
    assert not inspect.isabstract(spem_activity_EndNode)


def test_spem_activity_endnode_constructor_exists():
    assert callable(spem_activity_EndNode.__init__)


def test_spem_activity_endnode_constructor_args():
    sig = inspect.signature(spem_activity_EndNode.__init__)
    params = list(sig.parameters.keys())



def test_spem_activity_joinnode_is_not_abstract():
    assert not inspect.isabstract(spem_activity_JoinNode)


def test_spem_activity_joinnode_constructor_exists():
    assert callable(spem_activity_JoinNode.__init__)


def test_spem_activity_joinnode_constructor_args():
    sig = inspect.signature(spem_activity_JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_spem_activity_forknode_is_not_abstract():
    assert not inspect.isabstract(spem_activity_ForkNode)


def test_spem_activity_forknode_constructor_exists():
    assert callable(spem_activity_ForkNode.__init__)


def test_spem_activity_forknode_constructor_args():
    sig = inspect.signature(spem_activity_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_spem_activity_decisionnode_is_not_abstract():
    assert not inspect.isabstract(spem_activity_DecisionNode)


def test_spem_activity_decisionnode_constructor_exists():
    assert callable(spem_activity_DecisionNode.__init__)


def test_spem_activity_decisionnode_constructor_args():
    sig = inspect.signature(spem_activity_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_spem_activity_startnode_is_not_abstract():
    assert not inspect.isabstract(spem_activity_StartNode)


def test_spem_activity_startnode_constructor_exists():
    assert callable(spem_activity_StartNode.__init__)


def test_spem_activity_startnode_constructor_args():
    sig = inspect.signature(spem_activity_StartNode.__init__)
    params = list(sig.parameters.keys())



def test_activity_spem_breakdownelement_is_not_abstract():
    assert not inspect.isabstract(activity_spem_BreakdownElement)


def test_activity_spem_breakdownelement_constructor_exists():
    assert callable(activity_spem_BreakdownElement.__init__)


def test_activity_spem_breakdownelement_constructor_args():
    sig = inspect.signature(activity_spem_BreakdownElement.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_uma_spem_methodcontentelement_is_not_abstract():
    assert not inspect.isabstract(uma_spem_MethodContentElement)


def test_uma_spem_methodcontentelement_constructor_exists():
    assert callable(uma_spem_MethodContentElement.__init__)


def test_uma_spem_methodcontentelement_constructor_args():
    sig = inspect.signature(uma_spem_MethodContentElement.__init__)
    params = list(sig.parameters.keys())



def test_uma_spem_activity_is_not_abstract():
    assert not inspect.isabstract(uma_spem_Activity)


def test_uma_spem_activity_constructor_exists():
    assert callable(uma_spem_Activity.__init__)


def test_uma_spem_activity_constructor_args():
    sig = inspect.signature(uma_spem_Activity.__init__)
    params = list(sig.parameters.keys())



def test_practice_is_not_abstract():
    assert not inspect.isabstract(Practice)


def test_practice_constructor_exists():
    assert callable(Practice.__init__)


def test_practice_constructor_args():
    sig = inspect.signature(Practice.__init__)
    params = list(sig.parameters.keys())



def test_uma_spem_workproductdefinition_is_not_abstract():
    assert not inspect.isabstract(uma_spem_WorkProductDefinition)


def test_uma_spem_workproductdefinition_constructor_exists():
    assert callable(uma_spem_WorkProductDefinition.__init__)


def test_uma_spem_workproductdefinition_constructor_args():
    sig = inspect.signature(uma_spem_WorkProductDefinition.__init__)
    params = list(sig.parameters.keys())



def test_concept_is_not_abstract():
    assert not inspect.isabstract(Concept)


def test_concept_constructor_exists():
    assert callable(Concept.__init__)


def test_concept_constructor_args():
    sig = inspect.signature(Concept.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_whitepaper_is_not_abstract():
    assert not inspect.isabstract(spem_uma_Whitepaper)


def test_spem_uma_whitepaper_constructor_exists():
    assert callable(spem_uma_Whitepaper.__init__)


def test_spem_uma_whitepaper_constructor_args():
    sig = inspect.signature(spem_uma_Whitepaper.__init__)
    params = list(sig.parameters.keys())



def test_uma_spem_roledefinition_is_not_abstract():
    assert not inspect.isabstract(uma_spem_RoleDefinition)


def test_uma_spem_roledefinition_constructor_exists():
    assert callable(uma_spem_RoleDefinition.__init__)


def test_uma_spem_roledefinition_constructor_args():
    sig = inspect.signature(uma_spem_RoleDefinition.__init__)
    params = list(sig.parameters.keys())



def test_supportingmaterial_is_not_abstract():
    assert not inspect.isabstract(SupportingMaterial)


def test_supportingmaterial_constructor_exists():
    assert callable(SupportingMaterial.__init__)


def test_supportingmaterial_constructor_args():
    sig = inspect.signature(SupportingMaterial.__init__)
    params = list(sig.parameters.keys())



def test_uma_spem_workproductportconnector_is_not_abstract():
    assert not inspect.isabstract(uma_spem_WorkProductPortConnector)


def test_uma_spem_workproductportconnector_constructor_exists():
    assert callable(uma_spem_WorkProductPortConnector.__init__)


def test_uma_spem_workproductportconnector_constructor_args():
    sig = inspect.signature(uma_spem_WorkProductPortConnector.__init__)
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



def test_spem_uma_iteration_is_not_abstract():
    assert not inspect.isabstract(spem_uma_Iteration)


def test_spem_uma_iteration_constructor_exists():
    assert callable(spem_uma_Iteration.__init__)


def test_spem_uma_iteration_constructor_args():
    sig = inspect.signature(spem_uma_Iteration.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_phase_is_not_abstract():
    assert not inspect.isabstract(spem_uma_Phase)


def test_spem_uma_phase_constructor_exists():
    assert callable(spem_uma_Phase.__init__)


def test_spem_uma_phase_constructor_args():
    sig = inspect.signature(spem_uma_Phase.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_process_is_not_abstract():
    assert not inspect.isabstract(spem_uma_Process)


def test_spem_uma_process_constructor_exists():
    assert callable(spem_uma_Process.__init__)


def test_spem_uma_process_constructor_args():
    sig = inspect.signature(spem_uma_Process.__init__)
    params = list(sig.parameters.keys())
    assert "usageNote" in params, "Missing parameter 'usageNote'"
    assert "scope" in params, "Missing parameter 'scope'"

def test_spem_uma_process_has_usageNote():
    assert hasattr(spem_uma_Process, "usageNote")
    descriptor = None
    for klass in spem_uma_Process.__mro__:
        if "usageNote" in klass.__dict__:
            descriptor = klass.__dict__["usageNote"]
            break
    assert isinstance(descriptor, property)

def test_spem_uma_process_has_scope():
    assert hasattr(spem_uma_Process, "scope")
    descriptor = None
    for klass in spem_uma_Process.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_uma_spem_methodplugin_is_not_abstract():
    assert not inspect.isabstract(uma_spem_MethodPlugin)


def test_uma_spem_methodplugin_constructor_exists():
    assert callable(uma_spem_MethodPlugin.__init__)


def test_uma_spem_methodplugin_constructor_args():
    sig = inspect.signature(uma_spem_MethodPlugin.__init__)
    params = list(sig.parameters.keys())



def test_uma_spem_methodlibrary_is_not_abstract():
    assert not inspect.isabstract(uma_spem_MethodLibrary)


def test_uma_spem_methodlibrary_constructor_exists():
    assert callable(uma_spem_MethodLibrary.__init__)


def test_uma_spem_methodlibrary_constructor_args():
    sig = inspect.signature(uma_spem_MethodLibrary.__init__)
    params = list(sig.parameters.keys())



def test_uma_spem_workproductuse_is_not_abstract():
    assert not inspect.isabstract(uma_spem_WorkProductUse)


def test_uma_spem_workproductuse_constructor_exists():
    assert callable(uma_spem_WorkProductUse.__init__)


def test_uma_spem_workproductuse_constructor_args():
    sig = inspect.signature(uma_spem_WorkProductUse.__init__)
    params = list(sig.parameters.keys())



def test_uma_spem_methodconfiguration_is_not_abstract():
    assert not inspect.isabstract(uma_spem_MethodConfiguration)


def test_uma_spem_methodconfiguration_constructor_exists():
    assert callable(uma_spem_MethodConfiguration.__init__)


def test_uma_spem_methodconfiguration_constructor_args():
    sig = inspect.signature(uma_spem_MethodConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_root_is_not_abstract():
    assert not inspect.isabstract(spem_uma_Root)


def test_spem_uma_root_constructor_exists():
    assert callable(spem_uma_Root.__init__)


def test_spem_uma_root_constructor_args():
    sig = inspect.signature(spem_uma_Root.__init__)
    params = list(sig.parameters.keys())



def test_category_is_not_abstract():
    assert not inspect.isabstract(Category)


def test_category_constructor_exists():
    assert callable(Category.__init__)


def test_category_constructor_args():
    sig = inspect.signature(Category.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_domain_is_not_abstract():
    assert not inspect.isabstract(spem_uma_Domain)


def test_spem_uma_domain_constructor_exists():
    assert callable(spem_uma_Domain.__init__)


def test_spem_uma_domain_constructor_args():
    sig = inspect.signature(spem_uma_Domain.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_disciplinegrouping_is_not_abstract():
    assert not inspect.isabstract(spem_uma_DisciplineGrouping)


def test_spem_uma_disciplinegrouping_constructor_exists():
    assert callable(spem_uma_DisciplineGrouping.__init__)


def test_spem_uma_disciplinegrouping_constructor_args():
    sig = inspect.signature(spem_uma_DisciplineGrouping.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_customcategory_is_not_abstract():
    assert not inspect.isabstract(spem_uma_CustomCategory)


def test_spem_uma_customcategory_constructor_exists():
    assert callable(spem_uma_CustomCategory.__init__)


def test_spem_uma_customcategory_constructor_args():
    sig = inspect.signature(spem_uma_CustomCategory.__init__)
    params = list(sig.parameters.keys())



def test_methodcontentpackage_is_not_abstract():
    assert not inspect.isabstract(MethodContentPackage)


def test_methodcontentpackage_constructor_exists():
    assert callable(MethodContentPackage.__init__)


def test_methodcontentpackage_constructor_args():
    sig = inspect.signature(MethodContentPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_guidancepackage_is_not_abstract():
    assert not inspect.isabstract(spem_uma_GuidancePackage)


def test_spem_uma_guidancepackage_constructor_exists():
    assert callable(spem_uma_GuidancePackage.__init__)


def test_spem_uma_guidancepackage_constructor_args():
    sig = inspect.signature(spem_uma_GuidancePackage.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_rolesetpackage_is_not_abstract():
    assert not inspect.isabstract(spem_uma_RoleSetPackage)


def test_spem_uma_rolesetpackage_constructor_exists():
    assert callable(spem_uma_RoleSetPackage.__init__)


def test_spem_uma_rolesetpackage_constructor_args():
    sig = inspect.signature(spem_uma_RoleSetPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_configurationpackage_is_not_abstract():
    assert not inspect.isabstract(spem_uma_ConfigurationPackage)


def test_spem_uma_configurationpackage_constructor_exists():
    assert callable(spem_uma_ConfigurationPackage.__init__)


def test_spem_uma_configurationpackage_constructor_args():
    sig = inspect.signature(spem_uma_ConfigurationPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_disciplinepackage_is_not_abstract():
    assert not inspect.isabstract(spem_uma_DisciplinePackage)


def test_spem_uma_disciplinepackage_constructor_exists():
    assert callable(spem_uma_DisciplinePackage.__init__)


def test_spem_uma_disciplinepackage_constructor_args():
    sig = inspect.signature(spem_uma_DisciplinePackage.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_roledefinitionpackage_is_not_abstract():
    assert not inspect.isabstract(spem_uma_RoleDefinitionPackage)


def test_spem_uma_roledefinitionpackage_constructor_exists():
    assert callable(spem_uma_RoleDefinitionPackage.__init__)


def test_spem_uma_roledefinitionpackage_constructor_args():
    sig = inspect.signature(spem_uma_RoleDefinitionPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_tooldefinitionpackage_is_not_abstract():
    assert not inspect.isabstract(spem_uma_ToolDefinitionPackage)


def test_spem_uma_tooldefinitionpackage_constructor_exists():
    assert callable(spem_uma_ToolDefinitionPackage.__init__)


def test_spem_uma_tooldefinitionpackage_constructor_args():
    sig = inspect.signature(spem_uma_ToolDefinitionPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_workproductkindpackage_is_not_abstract():
    assert not inspect.isabstract(spem_uma_WorkProductKindPackage)


def test_spem_uma_workproductkindpackage_constructor_exists():
    assert callable(spem_uma_WorkProductKindPackage.__init__)


def test_spem_uma_workproductkindpackage_constructor_args():
    sig = inspect.signature(spem_uma_WorkProductKindPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_domainpackage_is_not_abstract():
    assert not inspect.isabstract(spem_uma_DomainPackage)


def test_spem_uma_domainpackage_constructor_exists():
    assert callable(spem_uma_DomainPackage.__init__)


def test_spem_uma_domainpackage_constructor_args():
    sig = inspect.signature(spem_uma_DomainPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_workproductdefinitionpackage_is_not_abstract():
    assert not inspect.isabstract(spem_uma_WorkProductDefinitionPackage)


def test_spem_uma_workproductdefinitionpackage_constructor_exists():
    assert callable(spem_uma_WorkProductDefinitionPackage.__init__)


def test_spem_uma_workproductdefinitionpackage_constructor_args():
    sig = inspect.signature(spem_uma_WorkProductDefinitionPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_qualificationpackage_is_not_abstract():
    assert not inspect.isabstract(spem_uma_QualificationPackage)


def test_spem_uma_qualificationpackage_constructor_exists():
    assert callable(spem_uma_QualificationPackage.__init__)


def test_spem_uma_qualificationpackage_constructor_args():
    sig = inspect.signature(spem_uma_QualificationPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_taskdefinitionpackage_is_not_abstract():
    assert not inspect.isabstract(spem_uma_TaskDefinitionPackage)


def test_spem_uma_taskdefinitionpackage_constructor_exists():
    assert callable(spem_uma_TaskDefinitionPackage.__init__)


def test_spem_uma_taskdefinitionpackage_constructor_args():
    sig = inspect.signature(spem_uma_TaskDefinitionPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_categorypackage_is_not_abstract():
    assert not inspect.isabstract(spem_uma_CategoryPackage)


def test_spem_uma_categorypackage_constructor_exists():
    assert callable(spem_uma_CategoryPackage.__init__)


def test_spem_uma_categorypackage_constructor_args():
    sig = inspect.signature(spem_uma_CategoryPackage.__init__)
    params = list(sig.parameters.keys())



def test_guidance_is_not_abstract():
    assert not inspect.isabstract(Guidance)


def test_guidance_constructor_exists():
    assert callable(Guidance.__init__)


def test_guidance_constructor_args():
    sig = inspect.signature(Guidance.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_estimatingconsideration_is_not_abstract():
    assert not inspect.isabstract(spem_uma_EstimatingConsideration)


def test_spem_uma_estimatingconsideration_constructor_exists():
    assert callable(spem_uma_EstimatingConsideration.__init__)


def test_spem_uma_estimatingconsideration_constructor_args():
    sig = inspect.signature(spem_uma_EstimatingConsideration.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_template_is_not_abstract():
    assert not inspect.isabstract(spem_uma_Template)


def test_spem_uma_template_constructor_exists():
    assert callable(spem_uma_Template.__init__)


def test_spem_uma_template_constructor_args():
    sig = inspect.signature(spem_uma_Template.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_practice_is_not_abstract():
    assert not inspect.isabstract(spem_uma_Practice)


def test_spem_uma_practice_constructor_exists():
    assert callable(spem_uma_Practice.__init__)


def test_spem_uma_practice_constructor_args():
    sig = inspect.signature(spem_uma_Practice.__init__)
    params = list(sig.parameters.keys())
    assert "levelOfAdoption" in params, "Missing parameter 'levelOfAdoption'"
    assert "background" in params, "Missing parameter 'background'"
    assert "additionalInfo" in params, "Missing parameter 'additionalInfo'"
    assert "goal" in params, "Missing parameter 'goal'"
    assert "problem" in params, "Missing parameter 'problem'"
    assert "application" in params, "Missing parameter 'application'"

def test_spem_uma_practice_has_levelOfAdoption():
    assert hasattr(spem_uma_Practice, "levelOfAdoption")
    descriptor = None
    for klass in spem_uma_Practice.__mro__:
        if "levelOfAdoption" in klass.__dict__:
            descriptor = klass.__dict__["levelOfAdoption"]
            break
    assert isinstance(descriptor, property)

def test_spem_uma_practice_has_background():
    assert hasattr(spem_uma_Practice, "background")
    descriptor = None
    for klass in spem_uma_Practice.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_spem_uma_practice_has_additionalInfo():
    assert hasattr(spem_uma_Practice, "additionalInfo")
    descriptor = None
    for klass in spem_uma_Practice.__mro__:
        if "additionalInfo" in klass.__dict__:
            descriptor = klass.__dict__["additionalInfo"]
            break
    assert isinstance(descriptor, property)

def test_spem_uma_practice_has_goal():
    assert hasattr(spem_uma_Practice, "goal")
    descriptor = None
    for klass in spem_uma_Practice.__mro__:
        if "goal" in klass.__dict__:
            descriptor = klass.__dict__["goal"]
            break
    assert isinstance(descriptor, property)

def test_spem_uma_practice_has_problem():
    assert hasattr(spem_uma_Practice, "problem")
    descriptor = None
    for klass in spem_uma_Practice.__mro__:
        if "problem" in klass.__dict__:
            descriptor = klass.__dict__["problem"]
            break
    assert isinstance(descriptor, property)

def test_spem_uma_practice_has_application():
    assert hasattr(spem_uma_Practice, "application")
    descriptor = None
    for klass in spem_uma_Practice.__mro__:
        if "application" in klass.__dict__:
            descriptor = klass.__dict__["application"]
            break
    assert isinstance(descriptor, property)



def test_spem_uma_termdefinition_is_not_abstract():
    assert not inspect.isabstract(spem_uma_TermDefinition)


def test_spem_uma_termdefinition_constructor_exists():
    assert callable(spem_uma_TermDefinition.__init__)


def test_spem_uma_termdefinition_constructor_args():
    sig = inspect.signature(spem_uma_TermDefinition.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_guideline_is_not_abstract():
    assert not inspect.isabstract(spem_uma_Guideline)


def test_spem_uma_guideline_constructor_exists():
    assert callable(spem_uma_Guideline.__init__)


def test_spem_uma_guideline_constructor_args():
    sig = inspect.signature(spem_uma_Guideline.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_roadmap_is_not_abstract():
    assert not inspect.isabstract(spem_uma_Roadmap)


def test_spem_uma_roadmap_constructor_exists():
    assert callable(spem_uma_Roadmap.__init__)


def test_spem_uma_roadmap_constructor_args():
    sig = inspect.signature(spem_uma_Roadmap.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_example_is_not_abstract():
    assert not inspect.isabstract(spem_uma_Example)


def test_spem_uma_example_constructor_exists():
    assert callable(spem_uma_Example.__init__)


def test_spem_uma_example_constructor_args():
    sig = inspect.signature(spem_uma_Example.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_supportingmaterial_is_not_abstract():
    assert not inspect.isabstract(spem_uma_SupportingMaterial)


def test_spem_uma_supportingmaterial_constructor_exists():
    assert callable(spem_uma_SupportingMaterial.__init__)


def test_spem_uma_supportingmaterial_constructor_args():
    sig = inspect.signature(spem_uma_SupportingMaterial.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_toolmentor_is_not_abstract():
    assert not inspect.isabstract(spem_uma_ToolMentor)


def test_spem_uma_toolmentor_constructor_exists():
    assert callable(spem_uma_ToolMentor.__init__)


def test_spem_uma_toolmentor_constructor_args():
    sig = inspect.signature(spem_uma_ToolMentor.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_concept_is_not_abstract():
    assert not inspect.isabstract(spem_uma_Concept)


def test_spem_uma_concept_constructor_exists():
    assert callable(spem_uma_Concept.__init__)


def test_spem_uma_concept_constructor_args():
    sig = inspect.signature(spem_uma_Concept.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_reusableasset_is_not_abstract():
    assert not inspect.isabstract(spem_uma_ReusableAsset)


def test_spem_uma_reusableasset_constructor_exists():
    assert callable(spem_uma_ReusableAsset.__init__)


def test_spem_uma_reusableasset_constructor_args():
    sig = inspect.signature(spem_uma_ReusableAsset.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_report_is_not_abstract():
    assert not inspect.isabstract(spem_uma_Report)


def test_spem_uma_report_constructor_exists():
    assert callable(spem_uma_Report.__init__)


def test_spem_uma_report_constructor_args():
    sig = inspect.signature(spem_uma_Report.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_checklist_is_not_abstract():
    assert not inspect.isabstract(spem_uma_Checklist)


def test_spem_uma_checklist_constructor_exists():
    assert callable(spem_uma_Checklist.__init__)


def test_spem_uma_checklist_constructor_args():
    sig = inspect.signature(spem_uma_Checklist.__init__)
    params = list(sig.parameters.keys())



def test_uma_spem_taskdefinition_is_not_abstract():
    assert not inspect.isabstract(uma_spem_TaskDefinition)


def test_uma_spem_taskdefinition_constructor_exists():
    assert callable(uma_spem_TaskDefinition.__init__)


def test_uma_spem_taskdefinition_constructor_args():
    sig = inspect.signature(uma_spem_TaskDefinition.__init__)
    params = list(sig.parameters.keys())



def test_process_is_not_abstract():
    assert not inspect.isabstract(Process)


def test_process_constructor_exists():
    assert callable(Process.__init__)


def test_process_constructor_args():
    sig = inspect.signature(Process.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_processplanningtemplate_is_not_abstract():
    assert not inspect.isabstract(spem_uma_ProcessPlanningTemplate)


def test_spem_uma_processplanningtemplate_constructor_exists():
    assert callable(spem_uma_ProcessPlanningTemplate.__init__)


def test_spem_uma_processplanningtemplate_constructor_args():
    sig = inspect.signature(spem_uma_ProcessPlanningTemplate.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_deliveryprocess_is_not_abstract():
    assert not inspect.isabstract(spem_uma_DeliveryProcess)


def test_spem_uma_deliveryprocess_constructor_exists():
    assert callable(spem_uma_DeliveryProcess.__init__)


def test_spem_uma_deliveryprocess_constructor_args():
    sig = inspect.signature(spem_uma_DeliveryProcess.__init__)
    params = list(sig.parameters.keys())
    assert "scale" in params, "Missing parameter 'scale'"
    assert "projectCharacteristics" in params, "Missing parameter 'projectCharacteristics'"
    assert "typeOfContract" in params, "Missing parameter 'typeOfContract'"
    assert "riskLevel" in params, "Missing parameter 'riskLevel'"
    assert "projectMemberExpertise" in params, "Missing parameter 'projectMemberExpertise'"
    assert "estimatingTechnique" in params, "Missing parameter 'estimatingTechnique'"

def test_spem_uma_deliveryprocess_has_scale():
    assert hasattr(spem_uma_DeliveryProcess, "scale")
    descriptor = None
    for klass in spem_uma_DeliveryProcess.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_spem_uma_deliveryprocess_has_projectCharacteristics():
    assert hasattr(spem_uma_DeliveryProcess, "projectCharacteristics")
    descriptor = None
    for klass in spem_uma_DeliveryProcess.__mro__:
        if "projectCharacteristics" in klass.__dict__:
            descriptor = klass.__dict__["projectCharacteristics"]
            break
    assert isinstance(descriptor, property)

def test_spem_uma_deliveryprocess_has_typeOfContract():
    assert hasattr(spem_uma_DeliveryProcess, "typeOfContract")
    descriptor = None
    for klass in spem_uma_DeliveryProcess.__mro__:
        if "typeOfContract" in klass.__dict__:
            descriptor = klass.__dict__["typeOfContract"]
            break
    assert isinstance(descriptor, property)

def test_spem_uma_deliveryprocess_has_riskLevel():
    assert hasattr(spem_uma_DeliveryProcess, "riskLevel")
    descriptor = None
    for klass in spem_uma_DeliveryProcess.__mro__:
        if "riskLevel" in klass.__dict__:
            descriptor = klass.__dict__["riskLevel"]
            break
    assert isinstance(descriptor, property)

def test_spem_uma_deliveryprocess_has_projectMemberExpertise():
    assert hasattr(spem_uma_DeliveryProcess, "projectMemberExpertise")
    descriptor = None
    for klass in spem_uma_DeliveryProcess.__mro__:
        if "projectMemberExpertise" in klass.__dict__:
            descriptor = klass.__dict__["projectMemberExpertise"]
            break
    assert isinstance(descriptor, property)

def test_spem_uma_deliveryprocess_has_estimatingTechnique():
    assert hasattr(spem_uma_DeliveryProcess, "estimatingTechnique")
    descriptor = None
    for klass in spem_uma_DeliveryProcess.__mro__:
        if "estimatingTechnique" in klass.__dict__:
            descriptor = klass.__dict__["estimatingTechnique"]
            break
    assert isinstance(descriptor, property)



def test_spem_uma_capabilitypattern_is_not_abstract():
    assert not inspect.isabstract(spem_uma_CapabilityPattern)


def test_spem_uma_capabilitypattern_constructor_exists():
    assert callable(spem_uma_CapabilityPattern.__init__)


def test_spem_uma_capabilitypattern_constructor_args():
    sig = inspect.signature(spem_uma_CapabilityPattern.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_discipline_is_not_abstract():
    assert not inspect.isabstract(spem_uma_Discipline)


def test_spem_uma_discipline_constructor_exists():
    assert callable(spem_uma_Discipline.__init__)


def test_spem_uma_discipline_constructor_args():
    sig = inspect.signature(spem_uma_Discipline.__init__)
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



def test_spem_uma_outcome_is_not_abstract():
    assert not inspect.isabstract(spem_uma_Outcome)


def test_spem_uma_outcome_constructor_exists():
    assert callable(spem_uma_Outcome.__init__)


def test_spem_uma_outcome_constructor_args():
    sig = inspect.signature(spem_uma_Outcome.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_deliverable_is_not_abstract():
    assert not inspect.isabstract(spem_uma_Deliverable)


def test_spem_uma_deliverable_constructor_exists():
    assert callable(spem_uma_Deliverable.__init__)


def test_spem_uma_deliverable_constructor_args():
    sig = inspect.signature(spem_uma_Deliverable.__init__)
    params = list(sig.parameters.keys())
    assert "packagingGuidance" in params, "Missing parameter 'packagingGuidance'"
    assert "externalDescription" in params, "Missing parameter 'externalDescription'"

def test_spem_uma_deliverable_has_packagingGuidance():
    assert hasattr(spem_uma_Deliverable, "packagingGuidance")
    descriptor = None
    for klass in spem_uma_Deliverable.__mro__:
        if "packagingGuidance" in klass.__dict__:
            descriptor = klass.__dict__["packagingGuidance"]
            break
    assert isinstance(descriptor, property)

def test_spem_uma_deliverable_has_externalDescription():
    assert hasattr(spem_uma_Deliverable, "externalDescription")
    descriptor = None
    for klass in spem_uma_Deliverable.__mro__:
        if "externalDescription" in klass.__dict__:
            descriptor = klass.__dict__["externalDescription"]
            break
    assert isinstance(descriptor, property)



def test_spem_uma_artifact_is_not_abstract():
    assert not inspect.isabstract(spem_uma_Artifact)


def test_spem_uma_artifact_constructor_exists():
    assert callable(spem_uma_Artifact.__init__)


def test_spem_uma_artifact_constructor_args():
    sig = inspect.signature(spem_uma_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_methodlibrarypackageableelement_is_not_abstract():
    assert not inspect.isabstract(MethodLibraryPackageableElement)


def test_methodlibrarypackageableelement_constructor_exists():
    assert callable(MethodLibraryPackageableElement.__init__)


def test_methodlibrarypackageableelement_constructor_args():
    sig = inspect.signature(MethodLibraryPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_spem_methodpluginpackageableelement_is_not_abstract():
    assert not inspect.isabstract(spem_MethodPluginPackageableElement)


def test_spem_methodpluginpackageableelement_constructor_exists():
    assert callable(spem_MethodPluginPackageableElement.__init__)


def test_spem_methodpluginpackageableelement_constructor_args():
    sig = inspect.signature(spem_MethodPluginPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_spem_methodlibrarypackageableelement_is_not_abstract():
    assert not inspect.isabstract(spem_MethodLibraryPackageableElement)


def test_spem_methodlibrarypackageableelement_constructor_exists():
    assert callable(spem_MethodLibraryPackageableElement.__init__)


def test_spem_methodlibrarypackageableelement_constructor_args():
    sig = inspect.signature(spem_MethodLibraryPackageableElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spem_methodlibrarypackageableelement_has_name():
    assert hasattr(spem_MethodLibraryPackageableElement, "name")
    descriptor = None
    for klass in spem_MethodLibraryPackageableElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spem_methodlibrary_is_not_abstract():
    assert not inspect.isabstract(spem_MethodLibrary)


def test_spem_methodlibrary_constructor_exists():
    assert callable(spem_MethodLibrary.__init__)


def test_spem_methodlibrary_constructor_args():
    sig = inspect.signature(spem_MethodLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spem_methodlibrary_has_name():
    assert hasattr(spem_MethodLibrary, "name")
    descriptor = None
    for klass in spem_MethodLibrary.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spem_methodplugin_is_not_abstract():
    assert not inspect.isabstract(spem_MethodPlugin)


def test_spem_methodplugin_constructor_exists():
    assert callable(spem_MethodPlugin.__init__)


def test_spem_methodplugin_constructor_args():
    sig = inspect.signature(spem_MethodPlugin.__init__)
    params = list(sig.parameters.keys())



def test_processpackage_is_not_abstract():
    assert not inspect.isabstract(ProcessPackage)


def test_processpackage_constructor_exists():
    assert callable(ProcessPackage.__init__)


def test_processpackage_constructor_args():
    sig = inspect.signature(ProcessPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_deliveryprocesspackage_is_not_abstract():
    assert not inspect.isabstract(spem_uma_DeliveryProcessPackage)


def test_spem_uma_deliveryprocesspackage_constructor_exists():
    assert callable(spem_uma_DeliveryProcessPackage.__init__)


def test_spem_uma_deliveryprocesspackage_constructor_args():
    sig = inspect.signature(spem_uma_DeliveryProcessPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_processcomponentpackage_is_not_abstract():
    assert not inspect.isabstract(spem_uma_ProcessComponentPackage)


def test_spem_uma_processcomponentpackage_constructor_exists():
    assert callable(spem_uma_ProcessComponentPackage.__init__)


def test_spem_uma_processcomponentpackage_constructor_args():
    sig = inspect.signature(spem_uma_ProcessComponentPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_capabilitypatternpackage_is_not_abstract():
    assert not inspect.isabstract(spem_uma_CapabilityPatternPackage)


def test_spem_uma_capabilitypatternpackage_constructor_exists():
    assert callable(spem_uma_CapabilityPatternPackage.__init__)


def test_spem_uma_capabilitypatternpackage_constructor_args():
    sig = inspect.signature(spem_uma_CapabilityPatternPackage.__init__)
    params = list(sig.parameters.keys())



def test_spem_processcomponent_is_not_abstract():
    assert not inspect.isabstract(spem_ProcessComponent)


def test_spem_processcomponent_constructor_exists():
    assert callable(spem_ProcessComponent.__init__)


def test_spem_processcomponent_constructor_args():
    sig = inspect.signature(spem_ProcessComponent.__init__)
    params = list(sig.parameters.keys())



def test_spem_variabilityelement_is_not_abstract():
    assert not inspect.isabstract(spem_VariabilityElement)


def test_spem_variabilityelement_constructor_exists():
    assert callable(spem_VariabilityElement.__init__)


def test_spem_variabilityelement_constructor_args():
    sig = inspect.signature(spem_VariabilityElement.__init__)
    params = list(sig.parameters.keys())
    assert "variabilityType" in params, "Missing parameter 'variabilityType'"

def test_spem_variabilityelement_has_variabilityType():
    assert hasattr(spem_VariabilityElement, "variabilityType")
    descriptor = None
    for klass in spem_VariabilityElement.__mro__:
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



def test_spem_compositerole_is_not_abstract():
    assert not inspect.isabstract(spem_CompositeRole)


def test_spem_compositerole_constructor_exists():
    assert callable(spem_CompositeRole.__init__)


def test_spem_compositerole_constructor_args():
    sig = inspect.signature(spem_CompositeRole.__init__)
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



def test_spem_processpackageableelement_is_not_abstract():
    assert not inspect.isabstract(spem_ProcessPackageableElement)


def test_spem_processpackageableelement_constructor_exists():
    assert callable(spem_ProcessPackageableElement.__init__)


def test_spem_processpackageableelement_constructor_args():
    sig = inspect.signature(spem_ProcessPackageableElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spem_processpackageableelement_has_name():
    assert hasattr(spem_ProcessPackageableElement, "name")
    descriptor = None
    for klass in spem_ProcessPackageableElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spem_methodcontentpackageableelement_is_not_abstract():
    assert not inspect.isabstract(spem_MethodContentPackageableElement)


def test_spem_methodcontentpackageableelement_constructor_exists():
    assert callable(spem_MethodContentPackageableElement.__init__)


def test_spem_methodcontentpackageableelement_constructor_args():
    sig = inspect.signature(spem_MethodContentPackageableElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spem_methodcontentpackageableelement_has_name():
    assert hasattr(spem_MethodContentPackageableElement, "name")
    descriptor = None
    for klass in spem_MethodContentPackageableElement.__mro__:
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



def test_spem_methodcontentpackage_is_not_abstract():
    assert not inspect.isabstract(spem_MethodContentPackage)


def test_spem_methodcontentpackage_constructor_exists():
    assert callable(spem_MethodContentPackage.__init__)


def test_spem_methodcontentpackage_constructor_args():
    sig = inspect.signature(spem_MethodContentPackage.__init__)
    params = list(sig.parameters.keys())



def test_methodcontentelement_is_not_abstract():
    assert not inspect.isabstract(MethodContentElement)


def test_methodcontentelement_constructor_exists():
    assert callable(MethodContentElement.__init__)


def test_methodcontentelement_constructor_args():
    sig = inspect.signature(MethodContentElement.__init__)
    params = list(sig.parameters.keys())



def test_spem_default_responsibilityassignment_is_not_abstract():
    assert not inspect.isabstract(spem_Default_ResponsibilityAssignment)


def test_spem_default_responsibilityassignment_constructor_exists():
    assert callable(spem_Default_ResponsibilityAssignment.__init__)


def test_spem_default_responsibilityassignment_constructor_args():
    sig = inspect.signature(spem_Default_ResponsibilityAssignment.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_roleset_is_not_abstract():
    assert not inspect.isabstract(spem_uma_RoleSet)


def test_spem_uma_roleset_constructor_exists():
    assert callable(spem_uma_RoleSet.__init__)


def test_spem_uma_roleset_constructor_args():
    sig = inspect.signature(spem_uma_RoleSet.__init__)
    params = list(sig.parameters.keys())



def test_spem_default_taskdefinitionperformer_is_not_abstract():
    assert not inspect.isabstract(spem_Default_TaskDefinitionPerformer)


def test_spem_default_taskdefinitionperformer_constructor_exists():
    assert callable(spem_Default_TaskDefinitionPerformer.__init__)


def test_spem_default_taskdefinitionperformer_constructor_args():
    sig = inspect.signature(spem_Default_TaskDefinitionPerformer.__init__)
    params = list(sig.parameters.keys())



def test_spem_methodcontentkind_is_not_abstract():
    assert not inspect.isabstract(spem_MethodContentKind)


def test_spem_methodcontentkind_constructor_exists():
    assert callable(spem_MethodContentKind.__init__)


def test_spem_methodcontentkind_constructor_args():
    sig = inspect.signature(spem_MethodContentKind.__init__)
    params = list(sig.parameters.keys())



def test_spem_tooldefinition_is_not_abstract():
    assert not inspect.isabstract(spem_ToolDefinition)


def test_spem_tooldefinition_constructor_exists():
    assert callable(spem_ToolDefinition.__init__)


def test_spem_tooldefinition_constructor_args():
    sig = inspect.signature(spem_ToolDefinition.__init__)
    params = list(sig.parameters.keys())



def test_spem_workproductdefinition_is_not_abstract():
    assert not inspect.isabstract(spem_WorkProductDefinition)


def test_spem_workproductdefinition_constructor_exists():
    assert callable(spem_WorkProductDefinition.__init__)


def test_spem_workproductdefinition_constructor_args():
    sig = inspect.signature(spem_WorkProductDefinition.__init__)
    params = list(sig.parameters.keys())



def test_spem_uma_workproductkind_is_not_abstract():
    assert not inspect.isabstract(spem_uma_WorkProductKind)


def test_spem_uma_workproductkind_constructor_exists():
    assert callable(spem_uma_WorkProductKind.__init__)


def test_spem_uma_workproductkind_constructor_args():
    sig = inspect.signature(spem_uma_WorkProductKind.__init__)
    params = list(sig.parameters.keys())



def test_spem_workproductdefinitionrelationship_is_not_abstract():
    assert not inspect.isabstract(spem_WorkProductDefinitionRelationship)


def test_spem_workproductdefinitionrelationship_constructor_exists():
    assert callable(spem_WorkProductDefinitionRelationship.__init__)


def test_spem_workproductdefinitionrelationship_constructor_args():
    sig = inspect.signature(spem_WorkProductDefinitionRelationship.__init__)
    params = list(sig.parameters.keys())



def test_spem_category_is_not_abstract():
    assert not inspect.isabstract(spem_Category)


def test_spem_category_constructor_exists():
    assert callable(spem_Category.__init__)


def test_spem_category_constructor_args():
    sig = inspect.signature(spem_Category.__init__)
    params = list(sig.parameters.keys())



def test_spem_guidance_is_not_abstract():
    assert not inspect.isabstract(spem_Guidance)


def test_spem_guidance_constructor_exists():
    assert callable(spem_Guidance.__init__)


def test_spem_guidance_constructor_args():
    sig = inspect.signature(spem_Guidance.__init__)
    params = list(sig.parameters.keys())



def test_processpackageableelement_is_not_abstract():
    assert not inspect.isabstract(ProcessPackageableElement)


def test_processpackageableelement_constructor_exists():
    assert callable(ProcessPackageableElement.__init__)


def test_processpackageableelement_constructor_args():
    sig = inspect.signature(ProcessPackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_spem_processpackage_is_not_abstract():
    assert not inspect.isabstract(spem_ProcessPackage)


def test_spem_processpackage_constructor_exists():
    assert callable(spem_ProcessPackage.__init__)


def test_spem_processpackage_constructor_args():
    sig = inspect.signature(spem_ProcessPackage.__init__)
    params = list(sig.parameters.keys())



def test_describableelement_is_not_abstract():
    assert not inspect.isabstract(DescribableElement)


def test_describableelement_constructor_exists():
    assert callable(DescribableElement.__init__)


def test_describableelement_constructor_args():
    sig = inspect.signature(DescribableElement.__init__)
    params = list(sig.parameters.keys())



def test_spem_metric_is_not_abstract():
    assert not inspect.isabstract(spem_Metric)


def test_spem_metric_constructor_exists():
    assert callable(spem_Metric.__init__)


def test_spem_metric_constructor_args():
    sig = inspect.signature(spem_Metric.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_spem_metric_has_expression():
    assert hasattr(spem_Metric, "expression")
    descriptor = None
    for klass in spem_Metric.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_spem_processelement_is_not_abstract():
    assert not inspect.isabstract(spem_ProcessElement)


def test_spem_processelement_constructor_exists():
    assert callable(spem_ProcessElement.__init__)


def test_spem_processelement_constructor_args():
    sig = inspect.signature(spem_ProcessElement.__init__)
    params = list(sig.parameters.keys())



def test_workdefinitionparameter_is_not_abstract():
    assert not inspect.isabstract(WorkDefinitionParameter)


def test_workdefinitionparameter_constructor_exists():
    assert callable(WorkDefinitionParameter.__init__)


def test_workdefinitionparameter_constructor_args():
    sig = inspect.signature(WorkDefinitionParameter.__init__)
    params = list(sig.parameters.keys())



def test_spem_default_taskdefinitionparameter_is_not_abstract():
    assert not inspect.isabstract(spem_Default_TaskDefinitionParameter)


def test_spem_default_taskdefinitionparameter_constructor_exists():
    assert callable(spem_Default_TaskDefinitionParameter.__init__)


def test_spem_default_taskdefinitionparameter_constructor_args():
    sig = inspect.signature(spem_Default_TaskDefinitionParameter.__init__)
    params = list(sig.parameters.keys())
    assert "optionality" in params, "Missing parameter 'optionality'"
    assert "name" in params, "Missing parameter 'name'"

def test_spem_default_taskdefinitionparameter_has_optionality():
    assert hasattr(spem_Default_TaskDefinitionParameter, "optionality")
    descriptor = None
    for klass in spem_Default_TaskDefinitionParameter.__mro__:
        if "optionality" in klass.__dict__:
            descriptor = klass.__dict__["optionality"]
            break
    assert isinstance(descriptor, property)

def test_spem_default_taskdefinitionparameter_has_name():
    assert hasattr(spem_Default_TaskDefinitionParameter, "name")
    descriptor = None
    for klass in spem_Default_TaskDefinitionParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_variabilityelement_is_not_abstract():
    assert not inspect.isabstract(VariabilityElement)


def test_variabilityelement_constructor_exists():
    assert callable(VariabilityElement.__init__)


def test_variabilityelement_constructor_args():
    sig = inspect.signature(VariabilityElement.__init__)
    params = list(sig.parameters.keys())



def test_spem_methodcontentelement_is_not_abstract():
    assert not inspect.isabstract(spem_MethodContentElement)


def test_spem_methodcontentelement_constructor_exists():
    assert callable(spem_MethodContentElement.__init__)


def test_spem_methodcontentelement_constructor_args():
    sig = inspect.signature(spem_MethodContentElement.__init__)
    params = list(sig.parameters.keys())



def test_workbreakdownelement_is_not_abstract():
    assert not inspect.isabstract(WorkBreakdownElement)


def test_workbreakdownelement_constructor_exists():
    assert callable(WorkBreakdownElement.__init__)


def test_workbreakdownelement_constructor_args():
    sig = inspect.signature(WorkBreakdownElement.__init__)
    params = list(sig.parameters.keys())



def test_spem_milestone_is_not_abstract():
    assert not inspect.isabstract(spem_Milestone)


def test_spem_milestone_constructor_exists():
    assert callable(spem_Milestone.__init__)


def test_spem_milestone_constructor_args():
    sig = inspect.signature(spem_Milestone.__init__)
    params = list(sig.parameters.keys())



def test_workdefinition_is_not_abstract():
    assert not inspect.isabstract(WorkDefinition)


def test_workdefinition_constructor_exists():
    assert callable(WorkDefinition.__init__)


def test_workdefinition_constructor_args():
    sig = inspect.signature(WorkDefinition.__init__)
    params = list(sig.parameters.keys())



def test_spem_taskdefinition_is_not_abstract():
    assert not inspect.isabstract(spem_TaskDefinition)


def test_spem_taskdefinition_constructor_exists():
    assert callable(spem_TaskDefinition.__init__)


def test_spem_taskdefinition_constructor_args():
    sig = inspect.signature(spem_TaskDefinition.__init__)
    params = list(sig.parameters.keys())



def test_spem_step_is_not_abstract():
    assert not inspect.isabstract(spem_Step)


def test_spem_step_constructor_exists():
    assert callable(spem_Step.__init__)


def test_spem_step_constructor_args():
    sig = inspect.signature(spem_Step.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_spem_step_has_name():
    assert hasattr(spem_Step, "name")
    descriptor = None
    for klass in spem_Step.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_spem_activity_is_not_abstract():
    assert not inspect.isabstract(spem_Activity)


def test_spem_activity_constructor_exists():
    assert callable(spem_Activity.__init__)


def test_spem_activity_constructor_args():
    sig = inspect.signature(spem_Activity.__init__)
    params = list(sig.parameters.keys())
    assert "useKind" in params, "Missing parameter 'useKind'"
    assert "isEnactable" in params, "Missing parameter 'isEnactable'"

def test_spem_activity_has_useKind():
    assert hasattr(spem_Activity, "useKind")
    descriptor = None
    for klass in spem_Activity.__mro__:
        if "useKind" in klass.__dict__:
            descriptor = klass.__dict__["useKind"]
            break
    assert isinstance(descriptor, property)

def test_spem_activity_has_isEnactable():
    assert hasattr(spem_Activity, "isEnactable")
    descriptor = None
    for klass in spem_Activity.__mro__:
        if "isEnactable" in klass.__dict__:
            descriptor = klass.__dict__["isEnactable"]
            break
    assert isinstance(descriptor, property)



def test_spem_qualification_is_not_abstract():
    assert not inspect.isabstract(spem_Qualification)


def test_spem_qualification_constructor_exists():
    assert callable(spem_Qualification.__init__)


def test_spem_qualification_constructor_args():
    sig = inspect.signature(spem_Qualification.__init__)
    params = list(sig.parameters.keys())



def test_spem_roledefinition_is_not_abstract():
    assert not inspect.isabstract(spem_RoleDefinition)


def test_spem_roledefinition_constructor_exists():
    assert callable(spem_RoleDefinition.__init__)


def test_spem_roledefinition_constructor_args():
    sig = inspect.signature(spem_RoleDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "synonym" in params, "Missing parameter 'synonym'"

def test_spem_roledefinition_has_synonym():
    assert hasattr(spem_RoleDefinition, "synonym")
    descriptor = None
    for klass in spem_RoleDefinition.__mro__:
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



def test_spem_processcomponentuse_is_not_abstract():
    assert not inspect.isabstract(spem_ProcessComponentUse)


def test_spem_processcomponentuse_constructor_exists():
    assert callable(spem_ProcessComponentUse.__init__)


def test_spem_processcomponentuse_constructor_args():
    sig = inspect.signature(spem_ProcessComponentUse.__init__)
    params = list(sig.parameters.keys())



def test_spem_workproductuse_is_not_abstract():
    assert not inspect.isabstract(spem_WorkProductUse)


def test_spem_workproductuse_constructor_exists():
    assert callable(spem_WorkProductUse.__init__)


def test_spem_workproductuse_constructor_args():
    sig = inspect.signature(spem_WorkProductUse.__init__)
    params = list(sig.parameters.keys())



def test_spem_taskuse_is_not_abstract():
    assert not inspect.isabstract(spem_TaskUse)


def test_spem_taskuse_constructor_exists():
    assert callable(spem_TaskUse.__init__)


def test_spem_taskuse_constructor_args():
    sig = inspect.signature(spem_TaskUse.__init__)
    params = list(sig.parameters.keys())
    assert "preCondition" in params, "Missing parameter 'preCondition'"
    assert "postCondition" in params, "Missing parameter 'postCondition'"

def test_spem_taskuse_has_preCondition():
    assert hasattr(spem_TaskUse, "preCondition")
    descriptor = None
    for klass in spem_TaskUse.__mro__:
        if "preCondition" in klass.__dict__:
            descriptor = klass.__dict__["preCondition"]
            break
    assert isinstance(descriptor, property)

def test_spem_taskuse_has_postCondition():
    assert hasattr(spem_TaskUse, "postCondition")
    descriptor = None
    for klass in spem_TaskUse.__mro__:
        if "postCondition" in klass.__dict__:
            descriptor = klass.__dict__["postCondition"]
            break
    assert isinstance(descriptor, property)



def test_spem_roleuse_is_not_abstract():
    assert not inspect.isabstract(spem_RoleUse)


def test_spem_roleuse_constructor_exists():
    assert callable(spem_RoleUse.__init__)


def test_spem_roleuse_constructor_args():
    sig = inspect.signature(spem_RoleUse.__init__)
    params = list(sig.parameters.keys())



def test_workdefinitionperformer_is_not_abstract():
    assert not inspect.isabstract(WorkDefinitionPerformer)


def test_workdefinitionperformer_constructor_exists():
    assert callable(WorkDefinitionPerformer.__init__)


def test_workdefinitionperformer_constructor_args():
    sig = inspect.signature(WorkDefinitionPerformer.__init__)
    params = list(sig.parameters.keys())



def test_spem_methodconfiguration_is_not_abstract():
    assert not inspect.isabstract(spem_MethodConfiguration)


def test_spem_methodconfiguration_constructor_exists():
    assert callable(spem_MethodConfiguration.__init__)


def test_spem_methodconfiguration_constructor_args():
    sig = inspect.signature(spem_MethodConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_spem_workdefinitionparameter_is_not_abstract():
    assert not inspect.isabstract(spem_WorkDefinitionParameter)


def test_spem_workdefinitionparameter_constructor_exists():
    assert callable(spem_WorkDefinitionParameter.__init__)


def test_spem_workdefinitionparameter_constructor_args():
    sig = inspect.signature(spem_WorkDefinitionParameter.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_spem_workdefinitionparameter_has_direction():
    assert hasattr(spem_WorkDefinitionParameter, "direction")
    descriptor = None
    for klass in spem_WorkDefinitionParameter.__mro__:
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



def test_spem_processperformer_is_not_abstract():
    assert not inspect.isabstract(spem_ProcessPerformer)


def test_spem_processperformer_constructor_exists():
    assert callable(spem_ProcessPerformer.__init__)


def test_spem_processperformer_constructor_args():
    sig = inspect.signature(spem_ProcessPerformer.__init__)
    params = list(sig.parameters.keys())



def test_spem_processresponsibilityassignment_is_not_abstract():
    assert not inspect.isabstract(spem_ProcessResponsibilityAssignment)


def test_spem_processresponsibilityassignment_constructor_exists():
    assert callable(spem_ProcessResponsibilityAssignment.__init__)


def test_spem_processresponsibilityassignment_constructor_args():
    sig = inspect.signature(spem_ProcessResponsibilityAssignment.__init__)
    params = list(sig.parameters.keys())



def test_spem_methodcontentuse_is_not_abstract():
    assert not inspect.isabstract(spem_MethodContentUse)


def test_spem_methodcontentuse_constructor_exists():
    assert callable(spem_MethodContentUse.__init__)


def test_spem_methodcontentuse_constructor_args():
    sig = inspect.signature(spem_MethodContentUse.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronizedWithSource" in params, "Missing parameter 'isSynchronizedWithSource'"

def test_spem_methodcontentuse_has_isSynchronizedWithSource():
    assert hasattr(spem_MethodContentUse, "isSynchronizedWithSource")
    descriptor = None
    for klass in spem_MethodContentUse.__mro__:
        if "isSynchronizedWithSource" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronizedWithSource"]
            break
    assert isinstance(descriptor, property)



def test_spem_activity_edge_is_not_abstract():
    assert not inspect.isabstract(spem_activity_Edge)


def test_spem_activity_edge_constructor_exists():
    assert callable(spem_activity_Edge.__init__)


def test_spem_activity_edge_constructor_args():
    sig = inspect.signature(spem_activity_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"

def test_spem_activity_edge_has_guard():
    assert hasattr(spem_activity_Edge, "guard")
    descriptor = None
    for klass in spem_activity_Edge.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)



def test_spem_teamprofile_is_not_abstract():
    assert not inspect.isabstract(spem_TeamProfile)


def test_spem_teamprofile_constructor_exists():
    assert callable(spem_TeamProfile.__init__)


def test_spem_teamprofile_constructor_args():
    sig = inspect.signature(spem_TeamProfile.__init__)
    params = list(sig.parameters.keys())



def test_spem_activity_node_is_not_abstract():
    assert not inspect.isabstract(spem_activity_Node)


def test_spem_activity_node_constructor_exists():
    assert callable(spem_activity_Node.__init__)


def test_spem_activity_node_constructor_args():
    sig = inspect.signature(spem_activity_Node.__init__)
    params = list(sig.parameters.keys())



def test_spem_processparameter_is_not_abstract():
    assert not inspect.isabstract(spem_ProcessParameter)


def test_spem_processparameter_constructor_exists():
    assert callable(spem_ProcessParameter.__init__)


def test_spem_processparameter_constructor_args():
    sig = inspect.signature(spem_ProcessParameter.__init__)
    params = list(sig.parameters.keys())
    assert "optionality" in params, "Missing parameter 'optionality'"

def test_spem_processparameter_has_optionality():
    assert hasattr(spem_ProcessParameter, "optionality")
    descriptor = None
    for klass in spem_ProcessParameter.__mro__:
        if "optionality" in klass.__dict__:
            descriptor = klass.__dict__["optionality"]
            break
    assert isinstance(descriptor, property)



def test_spem_workproductuserelationship_is_not_abstract():
    assert not inspect.isabstract(spem_WorkProductUseRelationship)


def test_spem_workproductuserelationship_constructor_exists():
    assert callable(spem_WorkProductUseRelationship.__init__)


def test_spem_workproductuserelationship_constructor_args():
    sig = inspect.signature(spem_WorkProductUseRelationship.__init__)
    params = list(sig.parameters.keys())
    assert "relationshipKind" in params, "Missing parameter 'relationshipKind'"

def test_spem_workproductuserelationship_has_relationshipKind():
    assert hasattr(spem_WorkProductUseRelationship, "relationshipKind")
    descriptor = None
    for klass in spem_WorkProductUseRelationship.__mro__:
        if "relationshipKind" in klass.__dict__:
            descriptor = klass.__dict__["relationshipKind"]
            break
    assert isinstance(descriptor, property)



def test_spem_worksequence_is_not_abstract():
    assert not inspect.isabstract(spem_WorkSequence)


def test_spem_worksequence_constructor_exists():
    assert callable(spem_WorkSequence.__init__)


def test_spem_worksequence_constructor_args():
    sig = inspect.signature(spem_WorkSequence.__init__)
    params = list(sig.parameters.keys())
    assert "linkKind" in params, "Missing parameter 'linkKind'"

def test_spem_worksequence_has_linkKind():
    assert hasattr(spem_WorkSequence, "linkKind")
    descriptor = None
    for klass in spem_WorkSequence.__mro__:
        if "linkKind" in klass.__dict__:
            descriptor = klass.__dict__["linkKind"]
            break
    assert isinstance(descriptor, property)



def test_spem_workbreakdownelement_is_not_abstract():
    assert not inspect.isabstract(spem_WorkBreakdownElement)


def test_spem_workbreakdownelement_constructor_exists():
    assert callable(spem_WorkBreakdownElement.__init__)


def test_spem_workbreakdownelement_constructor_args():
    sig = inspect.signature(spem_WorkBreakdownElement.__init__)
    params = list(sig.parameters.keys())
    assert "isEventDriven" in params, "Missing parameter 'isEventDriven'"
    assert "isOngoing" in params, "Missing parameter 'isOngoing'"
    assert "isRepeatable" in params, "Missing parameter 'isRepeatable'"

def test_spem_workbreakdownelement_has_isEventDriven():
    assert hasattr(spem_WorkBreakdownElement, "isEventDriven")
    descriptor = None
    for klass in spem_WorkBreakdownElement.__mro__:
        if "isEventDriven" in klass.__dict__:
            descriptor = klass.__dict__["isEventDriven"]
            break
    assert isinstance(descriptor, property)

def test_spem_workbreakdownelement_has_isOngoing():
    assert hasattr(spem_WorkBreakdownElement, "isOngoing")
    descriptor = None
    for klass in spem_WorkBreakdownElement.__mro__:
        if "isOngoing" in klass.__dict__:
            descriptor = klass.__dict__["isOngoing"]
            break
    assert isinstance(descriptor, property)

def test_spem_workbreakdownelement_has_isRepeatable():
    assert hasattr(spem_WorkBreakdownElement, "isRepeatable")
    descriptor = None
    for klass in spem_WorkBreakdownElement.__mro__:
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



def test_spem_workproductportconnector_is_not_abstract():
    assert not inspect.isabstract(spem_WorkProductPortConnector)


def test_spem_workproductportconnector_constructor_exists():
    assert callable(spem_WorkProductPortConnector.__init__)


def test_spem_workproductportconnector_constructor_args():
    sig = inspect.signature(spem_WorkProductPortConnector.__init__)
    params = list(sig.parameters.keys())



def test_spem_planningdata_is_not_abstract():
    assert not inspect.isabstract(spem_PlanningData)


def test_spem_planningdata_constructor_exists():
    assert callable(spem_PlanningData.__init__)


def test_spem_planningdata_constructor_args():
    sig = inspect.signature(spem_PlanningData.__init__)
    params = list(sig.parameters.keys())
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "duration" in params, "Missing parameter 'duration'"
    assert "rank" in params, "Missing parameter 'rank'"
    assert "finishDate" in params, "Missing parameter 'finishDate'"

def test_spem_planningdata_has_startDate():
    assert hasattr(spem_PlanningData, "startDate")
    descriptor = None
    for klass in spem_PlanningData.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_spem_planningdata_has_duration():
    assert hasattr(spem_PlanningData, "duration")
    descriptor = None
    for klass in spem_PlanningData.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_spem_planningdata_has_rank():
    assert hasattr(spem_PlanningData, "rank")
    descriptor = None
    for klass in spem_PlanningData.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)

def test_spem_planningdata_has_finishDate():
    assert hasattr(spem_PlanningData, "finishDate")
    descriptor = None
    for klass in spem_PlanningData.__mro__:
        if "finishDate" in klass.__dict__:
            descriptor = klass.__dict__["finishDate"]
            break
    assert isinstance(descriptor, property)



def test_spem_workproductport_is_not_abstract():
    assert not inspect.isabstract(spem_WorkProductPort)


def test_spem_workproductport_constructor_exists():
    assert callable(spem_WorkProductPort.__init__)


def test_spem_workproductport_constructor_args():
    sig = inspect.signature(spem_WorkProductPort.__init__)
    params = list(sig.parameters.keys())
    assert "portKind" in params, "Missing parameter 'portKind'"
    assert "isOptional" in params, "Missing parameter 'isOptional'"

def test_spem_workproductport_has_portKind():
    assert hasattr(spem_WorkProductPort, "portKind")
    descriptor = None
    for klass in spem_WorkProductPort.__mro__:
        if "portKind" in klass.__dict__:
            descriptor = klass.__dict__["portKind"]
            break
    assert isinstance(descriptor, property)

def test_spem_workproductport_has_isOptional():
    assert hasattr(spem_WorkProductPort, "isOptional")
    descriptor = None
    for klass in spem_WorkProductPort.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)



def test_spem_processkind_is_not_abstract():
    assert not inspect.isabstract(spem_ProcessKind)


def test_spem_processkind_constructor_exists():
    assert callable(spem_ProcessKind.__init__)


def test_spem_processkind_constructor_args():
    sig = inspect.signature(spem_ProcessKind.__init__)
    params = list(sig.parameters.keys())



def test_spem_breakdownelement_is_not_abstract():
    assert not inspect.isabstract(spem_BreakdownElement)


def test_spem_breakdownelement_constructor_exists():
    assert callable(spem_BreakdownElement.__init__)


def test_spem_breakdownelement_constructor_args():
    sig = inspect.signature(spem_BreakdownElement.__init__)
    params = list(sig.parameters.keys())
    assert "hasMultipleOccurrences" in params, "Missing parameter 'hasMultipleOccurrences'"
    assert "isPlanned" in params, "Missing parameter 'isPlanned'"
    assert "isOptional" in params, "Missing parameter 'isOptional'"

def test_spem_breakdownelement_has_hasMultipleOccurrences():
    assert hasattr(spem_BreakdownElement, "hasMultipleOccurrences")
    descriptor = None
    for klass in spem_BreakdownElement.__mro__:
        if "hasMultipleOccurrences" in klass.__dict__:
            descriptor = klass.__dict__["hasMultipleOccurrences"]
            break
    assert isinstance(descriptor, property)

def test_spem_breakdownelement_has_isPlanned():
    assert hasattr(spem_BreakdownElement, "isPlanned")
    descriptor = None
    for klass in spem_BreakdownElement.__mro__:
        if "isPlanned" in klass.__dict__:
            descriptor = klass.__dict__["isPlanned"]
            break
    assert isinstance(descriptor, property)

def test_spem_breakdownelement_has_isOptional():
    assert hasattr(spem_BreakdownElement, "isOptional")
    descriptor = None
    for klass in spem_BreakdownElement.__mro__:
        if "isOptional" in klass.__dict__:
            descriptor = klass.__dict__["isOptional"]
            break
    assert isinstance(descriptor, property)



def test_spem_workdefinition_is_not_abstract():
    assert not inspect.isabstract(spem_WorkDefinition)


def test_spem_workdefinition_constructor_exists():
    assert callable(spem_WorkDefinition.__init__)


def test_spem_workdefinition_constructor_args():
    sig = inspect.signature(spem_WorkDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "postCondition" in params, "Missing parameter 'postCondition'"
    assert "preCondition" in params, "Missing parameter 'preCondition'"

def test_spem_workdefinition_has_postCondition():
    assert hasattr(spem_WorkDefinition, "postCondition")
    descriptor = None
    for klass in spem_WorkDefinition.__mro__:
        if "postCondition" in klass.__dict__:
            descriptor = klass.__dict__["postCondition"]
            break
    assert isinstance(descriptor, property)

def test_spem_workdefinition_has_preCondition():
    assert hasattr(spem_WorkDefinition, "preCondition")
    descriptor = None
    for klass in spem_WorkDefinition.__mro__:
        if "preCondition" in klass.__dict__:
            descriptor = klass.__dict__["preCondition"]
            break
    assert isinstance(descriptor, property)



def test_spem_workdefinitionperformer_is_not_abstract():
    assert not inspect.isabstract(spem_WorkDefinitionPerformer)


def test_spem_workdefinitionperformer_constructor_exists():
    assert callable(spem_WorkDefinitionPerformer.__init__)


def test_spem_workdefinitionperformer_constructor_args():
    sig = inspect.signature(spem_WorkDefinitionPerformer.__init__)
    params = list(sig.parameters.keys())



def test_extensibleelement_is_not_abstract():
    assert not inspect.isabstract(ExtensibleElement)


def test_extensibleelement_constructor_exists():
    assert callable(ExtensibleElement.__init__)


def test_extensibleelement_constructor_args():
    sig = inspect.signature(ExtensibleElement.__init__)
    params = list(sig.parameters.keys())



def test_spem_describableelement_is_not_abstract():
    assert not inspect.isabstract(spem_DescribableElement)


def test_spem_describableelement_constructor_exists():
    assert callable(spem_DescribableElement.__init__)


def test_spem_describableelement_constructor_args():
    sig = inspect.signature(spem_DescribableElement.__init__)
    params = list(sig.parameters.keys())
    assert "briefDescription" in params, "Missing parameter 'briefDescription'"
    assert "version" in params, "Missing parameter 'version'"
    assert "purpose" in params, "Missing parameter 'purpose'"
    assert "mainDescription" in params, "Missing parameter 'mainDescription'"
    assert "copyright" in params, "Missing parameter 'copyright'"
    assert "author" in params, "Missing parameter 'author'"
    assert "changeDate" in params, "Missing parameter 'changeDate'"
    assert "changeDescription" in params, "Missing parameter 'changeDescription'"
    assert "presentationName" in params, "Missing parameter 'presentationName'"

def test_spem_describableelement_has_briefDescription():
    assert hasattr(spem_DescribableElement, "briefDescription")
    descriptor = None
    for klass in spem_DescribableElement.__mro__:
        if "briefDescription" in klass.__dict__:
            descriptor = klass.__dict__["briefDescription"]
            break
    assert isinstance(descriptor, property)

def test_spem_describableelement_has_version():
    assert hasattr(spem_DescribableElement, "version")
    descriptor = None
    for klass in spem_DescribableElement.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_spem_describableelement_has_purpose():
    assert hasattr(spem_DescribableElement, "purpose")
    descriptor = None
    for klass in spem_DescribableElement.__mro__:
        if "purpose" in klass.__dict__:
            descriptor = klass.__dict__["purpose"]
            break
    assert isinstance(descriptor, property)

def test_spem_describableelement_has_mainDescription():
    assert hasattr(spem_DescribableElement, "mainDescription")
    descriptor = None
    for klass in spem_DescribableElement.__mro__:
        if "mainDescription" in klass.__dict__:
            descriptor = klass.__dict__["mainDescription"]
            break
    assert isinstance(descriptor, property)

def test_spem_describableelement_has_copyright():
    assert hasattr(spem_DescribableElement, "copyright")
    descriptor = None
    for klass in spem_DescribableElement.__mro__:
        if "copyright" in klass.__dict__:
            descriptor = klass.__dict__["copyright"]
            break
    assert isinstance(descriptor, property)

def test_spem_describableelement_has_author():
    assert hasattr(spem_DescribableElement, "author")
    descriptor = None
    for klass in spem_DescribableElement.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_spem_describableelement_has_changeDate():
    assert hasattr(spem_DescribableElement, "changeDate")
    descriptor = None
    for klass in spem_DescribableElement.__mro__:
        if "changeDate" in klass.__dict__:
            descriptor = klass.__dict__["changeDate"]
            break
    assert isinstance(descriptor, property)

def test_spem_describableelement_has_changeDescription():
    assert hasattr(spem_DescribableElement, "changeDescription")
    descriptor = None
    for klass in spem_DescribableElement.__mro__:
        if "changeDescription" in klass.__dict__:
            descriptor = klass.__dict__["changeDescription"]
            break
    assert isinstance(descriptor, property)

def test_spem_describableelement_has_presentationName():
    assert hasattr(spem_DescribableElement, "presentationName")
    descriptor = None
    for klass in spem_DescribableElement.__mro__:
        if "presentationName" in klass.__dict__:
            descriptor = klass.__dict__["presentationName"]
            break
    assert isinstance(descriptor, property)



def test_spem_kind_is_not_abstract():
    assert not inspect.isabstract(spem_Kind)


def test_spem_kind_constructor_exists():
    assert callable(spem_Kind.__init__)


def test_spem_kind_constructor_args():
    sig = inspect.signature(spem_Kind.__init__)
    params = list(sig.parameters.keys())



def test_spem_extensibleelement_is_not_abstract():
    assert not inspect.isabstract(spem_ExtensibleElement)


def test_spem_extensibleelement_constructor_exists():
    assert callable(spem_ExtensibleElement.__init__)


def test_spem_extensibleelement_constructor_args():
    sig = inspect.signature(spem_ExtensibleElement.__init__)
    params = list(sig.parameters.keys())

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

def test_risklevel_exists():
    # Check that the Enumeration exists
    assert RiskLevel is not None

def test_risklevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RiskLevel]
    expected_literals = [
        "HIGH",
        "MID",
        "LOW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RiskLevel"

def test_estimatingtechnique_exists():
    # Check that the Enumeration exists
    assert EstimatingTechnique is not None

def test_estimatingtechnique_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EstimatingTechnique]
    expected_literals = [
        "DEFECTS",
        "OTHER",
        "TIME",
        "SKILLS",
        "COST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EstimatingTechnique"

def test_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "inout",
        "out",
        "in_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirectionKind"

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

def test_expertiselevel_exists():
    # Check that the Enumeration exists
    assert ExpertiseLevel is not None

def test_expertiselevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExpertiseLevel]
    expected_literals = [
        "MID",
        "LEVEL",
        "LOW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExpertiseLevel"

def test_worksequencekind_exists():
    # Check that the Enumeration exists
    assert WorkSequenceKind is not None

def test_worksequencekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WorkSequenceKind]
    expected_literals = [
        "startToFinish",
        "startToStart",
        "finishToStart",
        "finishToFinish",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WorkSequenceKind"

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

def test_activityusekind_exists():
    # Check that the Enumeration exists
    assert ActivityUseKind is not None

def test_activityusekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActivityUseKind]
    expected_literals = [
        "localContribution",
        "localReplacement",
        "extension",
        "na",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActivityUseKind"

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
Node_strategy = st.builds(
    Node,
)
spem_activity_EndNode_strategy = st.builds(
    spem_activity_EndNode,
)
spem_activity_JoinNode_strategy = st.builds(
    spem_activity_JoinNode,
)
spem_activity_ForkNode_strategy = st.builds(
    spem_activity_ForkNode,
)
spem_activity_DecisionNode_strategy = st.builds(
    spem_activity_DecisionNode,
)
spem_activity_StartNode_strategy = st.builds(
    spem_activity_StartNode,
)
activity_spem_BreakdownElement_strategy = st.builds(
    activity_spem_BreakdownElement,
)
Edge_strategy = st.builds(
    Edge,
)
uma_spem_MethodContentElement_strategy = st.builds(
    uma_spem_MethodContentElement,
)
uma_spem_Activity_strategy = st.builds(
    uma_spem_Activity,
)
Practice_strategy = st.builds(
    Practice,
)
uma_spem_WorkProductDefinition_strategy = st.builds(
    uma_spem_WorkProductDefinition,
)
Concept_strategy = st.builds(
    Concept,
)
spem_uma_Whitepaper_strategy = st.builds(
    spem_uma_Whitepaper,
)
uma_spem_RoleDefinition_strategy = st.builds(
    uma_spem_RoleDefinition,
)
SupportingMaterial_strategy = st.builds(
    SupportingMaterial,
)
uma_spem_WorkProductPortConnector_strategy = st.builds(
    uma_spem_WorkProductPortConnector,
)
CapabilityPattern_strategy = st.builds(
    CapabilityPattern,
)
Activity_strategy = st.builds(
    Activity,
)
spem_uma_Iteration_strategy = st.builds(
    spem_uma_Iteration,
)
spem_uma_Phase_strategy = st.builds(
    spem_uma_Phase,
)
spem_uma_Process_strategy = st.builds(
    spem_uma_Process,
    usageNote=
        safe_text,
    scope=
        safe_text
)
uma_spem_MethodPlugin_strategy = st.builds(
    uma_spem_MethodPlugin,
)
uma_spem_MethodLibrary_strategy = st.builds(
    uma_spem_MethodLibrary,
)
uma_spem_WorkProductUse_strategy = st.builds(
    uma_spem_WorkProductUse,
)
uma_spem_MethodConfiguration_strategy = st.builds(
    uma_spem_MethodConfiguration,
)
spem_uma_Root_strategy = st.builds(
    spem_uma_Root,
)
Category_strategy = st.builds(
    Category,
)
spem_uma_Domain_strategy = st.builds(
    spem_uma_Domain,
)
spem_uma_DisciplineGrouping_strategy = st.builds(
    spem_uma_DisciplineGrouping,
)
spem_uma_CustomCategory_strategy = st.builds(
    spem_uma_CustomCategory,
)
MethodContentPackage_strategy = st.builds(
    MethodContentPackage,
)
spem_uma_GuidancePackage_strategy = st.builds(
    spem_uma_GuidancePackage,
)
spem_uma_RoleSetPackage_strategy = st.builds(
    spem_uma_RoleSetPackage,
)
spem_uma_ConfigurationPackage_strategy = st.builds(
    spem_uma_ConfigurationPackage,
)
spem_uma_DisciplinePackage_strategy = st.builds(
    spem_uma_DisciplinePackage,
)
spem_uma_RoleDefinitionPackage_strategy = st.builds(
    spem_uma_RoleDefinitionPackage,
)
spem_uma_ToolDefinitionPackage_strategy = st.builds(
    spem_uma_ToolDefinitionPackage,
)
spem_uma_WorkProductKindPackage_strategy = st.builds(
    spem_uma_WorkProductKindPackage,
)
spem_uma_DomainPackage_strategy = st.builds(
    spem_uma_DomainPackage,
)
spem_uma_WorkProductDefinitionPackage_strategy = st.builds(
    spem_uma_WorkProductDefinitionPackage,
)
spem_uma_QualificationPackage_strategy = st.builds(
    spem_uma_QualificationPackage,
)
spem_uma_TaskDefinitionPackage_strategy = st.builds(
    spem_uma_TaskDefinitionPackage,
)
spem_uma_CategoryPackage_strategy = st.builds(
    spem_uma_CategoryPackage,
)
Guidance_strategy = st.builds(
    Guidance,
)
spem_uma_EstimatingConsideration_strategy = st.builds(
    spem_uma_EstimatingConsideration,
)
spem_uma_Template_strategy = st.builds(
    spem_uma_Template,
)
spem_uma_Practice_strategy = st.builds(
    spem_uma_Practice,
    levelOfAdoption=
        safe_text,
    background=
        safe_text,
    additionalInfo=
        safe_text,
    goal=
        safe_text,
    problem=
        safe_text,
    application=
        safe_text
)
spem_uma_TermDefinition_strategy = st.builds(
    spem_uma_TermDefinition,
)
spem_uma_Guideline_strategy = st.builds(
    spem_uma_Guideline,
)
spem_uma_Roadmap_strategy = st.builds(
    spem_uma_Roadmap,
)
spem_uma_Example_strategy = st.builds(
    spem_uma_Example,
)
spem_uma_SupportingMaterial_strategy = st.builds(
    spem_uma_SupportingMaterial,
)
spem_uma_ToolMentor_strategy = st.builds(
    spem_uma_ToolMentor,
)
spem_uma_Concept_strategy = st.builds(
    spem_uma_Concept,
)
spem_uma_ReusableAsset_strategy = st.builds(
    spem_uma_ReusableAsset,
)
spem_uma_Report_strategy = st.builds(
    spem_uma_Report,
)
spem_uma_Checklist_strategy = st.builds(
    spem_uma_Checklist,
)
uma_spem_TaskDefinition_strategy = st.builds(
    uma_spem_TaskDefinition,
)
Process_strategy = st.builds(
    Process,
)
spem_uma_ProcessPlanningTemplate_strategy = st.builds(
    spem_uma_ProcessPlanningTemplate,
)
spem_uma_DeliveryProcess_strategy = st.builds(
    spem_uma_DeliveryProcess,
    scale=
        safe_text,
    projectCharacteristics=
        safe_text,
    typeOfContract=
        safe_text,
    riskLevel=
        safe_text,
    projectMemberExpertise=
        safe_text,
    estimatingTechnique=
        safe_text
)
spem_uma_CapabilityPattern_strategy = st.builds(
    spem_uma_CapabilityPattern,
)
spem_uma_Discipline_strategy = st.builds(
    spem_uma_Discipline,
)
Artifact_strategy = st.builds(
    Artifact,
)
WorkProductUse_strategy = st.builds(
    WorkProductUse,
)
spem_uma_Outcome_strategy = st.builds(
    spem_uma_Outcome,
)
spem_uma_Deliverable_strategy = st.builds(
    spem_uma_Deliverable,
    packagingGuidance=
        safe_text,
    externalDescription=
        safe_text
)
spem_uma_Artifact_strategy = st.builds(
    spem_uma_Artifact,
)
MethodLibraryPackageableElement_strategy = st.builds(
    MethodLibraryPackageableElement,
)
spem_MethodPluginPackageableElement_strategy = st.builds(
    spem_MethodPluginPackageableElement,
)
spem_MethodLibraryPackageableElement_strategy = st.builds(
    spem_MethodLibraryPackageableElement,
    name=
        safe_text
)
spem_MethodLibrary_strategy = st.builds(
    spem_MethodLibrary,
    name=
        safe_text
)
spem_MethodPlugin_strategy = st.builds(
    spem_MethodPlugin,
)
ProcessPackage_strategy = st.builds(
    ProcessPackage,
)
spem_uma_DeliveryProcessPackage_strategy = st.builds(
    spem_uma_DeliveryProcessPackage,
)
spem_uma_ProcessComponentPackage_strategy = st.builds(
    spem_uma_ProcessComponentPackage,
)
spem_uma_CapabilityPatternPackage_strategy = st.builds(
    spem_uma_CapabilityPatternPackage,
)
spem_ProcessComponent_strategy = st.builds(
    spem_ProcessComponent,
)
spem_VariabilityElement_strategy = st.builds(
    spem_VariabilityElement,
    variabilityType=
        safe_text
)
RoleUse_strategy = st.builds(
    RoleUse,
)
spem_CompositeRole_strategy = st.builds(
    spem_CompositeRole,
)
Kind_strategy = st.builds(
    Kind,
)
MethodPluginPackageableElement_strategy = st.builds(
    MethodPluginPackageableElement,
)
spem_ProcessPackageableElement_strategy = st.builds(
    spem_ProcessPackageableElement,
    name=
        safe_text
)
spem_MethodContentPackageableElement_strategy = st.builds(
    spem_MethodContentPackageableElement,
    name=
        safe_text
)
MethodContentPackageableElement_strategy = st.builds(
    MethodContentPackageableElement,
)
spem_MethodContentPackage_strategy = st.builds(
    spem_MethodContentPackage,
)
MethodContentElement_strategy = st.builds(
    MethodContentElement,
)
spem_Default_ResponsibilityAssignment_strategy = st.builds(
    spem_Default_ResponsibilityAssignment,
)
spem_uma_RoleSet_strategy = st.builds(
    spem_uma_RoleSet,
)
spem_Default_TaskDefinitionPerformer_strategy = st.builds(
    spem_Default_TaskDefinitionPerformer,
)
spem_MethodContentKind_strategy = st.builds(
    spem_MethodContentKind,
)
spem_ToolDefinition_strategy = st.builds(
    spem_ToolDefinition,
)
spem_WorkProductDefinition_strategy = st.builds(
    spem_WorkProductDefinition,
)
spem_uma_WorkProductKind_strategy = st.builds(
    spem_uma_WorkProductKind,
)
spem_WorkProductDefinitionRelationship_strategy = st.builds(
    spem_WorkProductDefinitionRelationship,
)
spem_Category_strategy = st.builds(
    spem_Category,
)
spem_Guidance_strategy = st.builds(
    spem_Guidance,
)
ProcessPackageableElement_strategy = st.builds(
    ProcessPackageableElement,
)
spem_ProcessPackage_strategy = st.builds(
    spem_ProcessPackage,
)
DescribableElement_strategy = st.builds(
    DescribableElement,
)
spem_Metric_strategy = st.builds(
    spem_Metric,
    expression=
        safe_text
)
spem_ProcessElement_strategy = st.builds(
    spem_ProcessElement,
)
WorkDefinitionParameter_strategy = st.builds(
    WorkDefinitionParameter,
)
spem_Default_TaskDefinitionParameter_strategy = st.builds(
    spem_Default_TaskDefinitionParameter,
    optionality=
        safe_text,
    name=
        safe_text
)
VariabilityElement_strategy = st.builds(
    VariabilityElement,
)
spem_MethodContentElement_strategy = st.builds(
    spem_MethodContentElement,
)
WorkBreakdownElement_strategy = st.builds(
    WorkBreakdownElement,
)
spem_Milestone_strategy = st.builds(
    spem_Milestone,
)
WorkDefinition_strategy = st.builds(
    WorkDefinition,
)
spem_TaskDefinition_strategy = st.builds(
    spem_TaskDefinition,
)
spem_Step_strategy = st.builds(
    spem_Step,
    name=
        safe_text
)
spem_Activity_strategy = st.builds(
    spem_Activity,
    useKind=
        safe_text,
    isEnactable=
        st.booleans()
)
spem_Qualification_strategy = st.builds(
    spem_Qualification,
)
spem_RoleDefinition_strategy = st.builds(
    spem_RoleDefinition,
    synonym=
        safe_text
)
MethodContentUse_strategy = st.builds(
    MethodContentUse,
)
spem_ProcessComponentUse_strategy = st.builds(
    spem_ProcessComponentUse,
)
spem_WorkProductUse_strategy = st.builds(
    spem_WorkProductUse,
)
spem_TaskUse_strategy = st.builds(
    spem_TaskUse,
    preCondition=
        safe_text,
    postCondition=
        safe_text
)
spem_RoleUse_strategy = st.builds(
    spem_RoleUse,
)
WorkDefinitionPerformer_strategy = st.builds(
    WorkDefinitionPerformer,
)
spem_MethodConfiguration_strategy = st.builds(
    spem_MethodConfiguration,
)
spem_WorkDefinitionParameter_strategy = st.builds(
    spem_WorkDefinitionParameter,
    direction=
        safe_text
)
BreakdownElement_strategy = st.builds(
    BreakdownElement,
)
spem_ProcessPerformer_strategy = st.builds(
    spem_ProcessPerformer,
)
spem_ProcessResponsibilityAssignment_strategy = st.builds(
    spem_ProcessResponsibilityAssignment,
)
spem_MethodContentUse_strategy = st.builds(
    spem_MethodContentUse,
    isSynchronizedWithSource=
        st.booleans()
)
spem_activity_Edge_strategy = st.builds(
    spem_activity_Edge,
    guard=
        safe_text
)
spem_TeamProfile_strategy = st.builds(
    spem_TeamProfile,
)
spem_activity_Node_strategy = st.builds(
    spem_activity_Node,
)
spem_ProcessParameter_strategy = st.builds(
    spem_ProcessParameter,
    optionality=
        safe_text
)
spem_WorkProductUseRelationship_strategy = st.builds(
    spem_WorkProductUseRelationship,
    relationshipKind=
        safe_text
)
spem_WorkSequence_strategy = st.builds(
    spem_WorkSequence,
    linkKind=
        safe_text
)
spem_WorkBreakdownElement_strategy = st.builds(
    spem_WorkBreakdownElement,
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
spem_WorkProductPortConnector_strategy = st.builds(
    spem_WorkProductPortConnector,
)
spem_PlanningData_strategy = st.builds(
    spem_PlanningData,
    startDate=
        st.dates(),
    duration=
        safe_text,
    rank=
        st.integers(),
    finishDate=
        st.dates()
)
spem_WorkProductPort_strategy = st.builds(
    spem_WorkProductPort,
    portKind=
        safe_text,
    isOptional=
        st.booleans()
)
spem_ProcessKind_strategy = st.builds(
    spem_ProcessKind,
)
spem_BreakdownElement_strategy = st.builds(
    spem_BreakdownElement,
    hasMultipleOccurrences=
        st.booleans(),
    isPlanned=
        st.booleans(),
    isOptional=
        st.booleans()
)
spem_WorkDefinition_strategy = st.builds(
    spem_WorkDefinition,
    postCondition=
        safe_text,
    preCondition=
        safe_text
)
spem_WorkDefinitionPerformer_strategy = st.builds(
    spem_WorkDefinitionPerformer,
)
ExtensibleElement_strategy = st.builds(
    ExtensibleElement,
)
spem_DescribableElement_strategy = st.builds(
    spem_DescribableElement,
    briefDescription=
        safe_text,
    version=
        safe_text,
    purpose=
        safe_text,
    mainDescription=
        safe_text,
    copyright=
        safe_text,
    author=
        safe_text,
    changeDate=
        st.dates(),
    changeDescription=
        safe_text,
    presentationName=
        safe_text
)
spem_Kind_strategy = st.builds(
    spem_Kind,
)
spem_ExtensibleElement_strategy = st.builds(
    spem_ExtensibleElement,
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=spem_activity_EndNode_strategy)
@settings(max_examples=50)
def test_spem_activity_endnode_instantiation(instance):
    assert isinstance(instance, spem_activity_EndNode)

@given(instance=spem_activity_JoinNode_strategy)
@settings(max_examples=50)
def test_spem_activity_joinnode_instantiation(instance):
    assert isinstance(instance, spem_activity_JoinNode)

@given(instance=spem_activity_ForkNode_strategy)
@settings(max_examples=50)
def test_spem_activity_forknode_instantiation(instance):
    assert isinstance(instance, spem_activity_ForkNode)

@given(instance=spem_activity_DecisionNode_strategy)
@settings(max_examples=50)
def test_spem_activity_decisionnode_instantiation(instance):
    assert isinstance(instance, spem_activity_DecisionNode)

@given(instance=spem_activity_StartNode_strategy)
@settings(max_examples=50)
def test_spem_activity_startnode_instantiation(instance):
    assert isinstance(instance, spem_activity_StartNode)

@given(instance=activity_spem_BreakdownElement_strategy)
@settings(max_examples=50)
def test_activity_spem_breakdownelement_instantiation(instance):
    assert isinstance(instance, activity_spem_BreakdownElement)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=uma_spem_MethodContentElement_strategy)
@settings(max_examples=50)
def test_uma_spem_methodcontentelement_instantiation(instance):
    assert isinstance(instance, uma_spem_MethodContentElement)

@given(instance=uma_spem_Activity_strategy)
@settings(max_examples=50)
def test_uma_spem_activity_instantiation(instance):
    assert isinstance(instance, uma_spem_Activity)

@given(instance=Practice_strategy)
@settings(max_examples=50)
def test_practice_instantiation(instance):
    assert isinstance(instance, Practice)

@given(instance=uma_spem_WorkProductDefinition_strategy)
@settings(max_examples=50)
def test_uma_spem_workproductdefinition_instantiation(instance):
    assert isinstance(instance, uma_spem_WorkProductDefinition)

@given(instance=Concept_strategy)
@settings(max_examples=50)
def test_concept_instantiation(instance):
    assert isinstance(instance, Concept)

@given(instance=spem_uma_Whitepaper_strategy)
@settings(max_examples=50)
def test_spem_uma_whitepaper_instantiation(instance):
    assert isinstance(instance, spem_uma_Whitepaper)

@given(instance=uma_spem_RoleDefinition_strategy)
@settings(max_examples=50)
def test_uma_spem_roledefinition_instantiation(instance):
    assert isinstance(instance, uma_spem_RoleDefinition)

@given(instance=SupportingMaterial_strategy)
@settings(max_examples=50)
def test_supportingmaterial_instantiation(instance):
    assert isinstance(instance, SupportingMaterial)

@given(instance=uma_spem_WorkProductPortConnector_strategy)
@settings(max_examples=50)
def test_uma_spem_workproductportconnector_instantiation(instance):
    assert isinstance(instance, uma_spem_WorkProductPortConnector)

@given(instance=CapabilityPattern_strategy)
@settings(max_examples=50)
def test_capabilitypattern_instantiation(instance):
    assert isinstance(instance, CapabilityPattern)

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=spem_uma_Iteration_strategy)
@settings(max_examples=50)
def test_spem_uma_iteration_instantiation(instance):
    assert isinstance(instance, spem_uma_Iteration)

@given(instance=spem_uma_Phase_strategy)
@settings(max_examples=50)
def test_spem_uma_phase_instantiation(instance):
    assert isinstance(instance, spem_uma_Phase)

@given(instance=spem_uma_Process_strategy)
@settings(max_examples=50)
def test_spem_uma_process_instantiation(instance):
    assert isinstance(instance, spem_uma_Process)



@given(instance=spem_uma_Process_strategy)
def test_spem_uma_process_usageNote_setter(instance):
    original = instance.usageNote
    instance.usageNote = original
    assert instance.usageNote == original



@given(instance=spem_uma_Process_strategy)
def test_spem_uma_process_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=uma_spem_MethodPlugin_strategy)
@settings(max_examples=50)
def test_uma_spem_methodplugin_instantiation(instance):
    assert isinstance(instance, uma_spem_MethodPlugin)

@given(instance=uma_spem_MethodLibrary_strategy)
@settings(max_examples=50)
def test_uma_spem_methodlibrary_instantiation(instance):
    assert isinstance(instance, uma_spem_MethodLibrary)

@given(instance=uma_spem_WorkProductUse_strategy)
@settings(max_examples=50)
def test_uma_spem_workproductuse_instantiation(instance):
    assert isinstance(instance, uma_spem_WorkProductUse)

@given(instance=uma_spem_MethodConfiguration_strategy)
@settings(max_examples=50)
def test_uma_spem_methodconfiguration_instantiation(instance):
    assert isinstance(instance, uma_spem_MethodConfiguration)

@given(instance=spem_uma_Root_strategy)
@settings(max_examples=50)
def test_spem_uma_root_instantiation(instance):
    assert isinstance(instance, spem_uma_Root)

@given(instance=Category_strategy)
@settings(max_examples=50)
def test_category_instantiation(instance):
    assert isinstance(instance, Category)

@given(instance=spem_uma_Domain_strategy)
@settings(max_examples=50)
def test_spem_uma_domain_instantiation(instance):
    assert isinstance(instance, spem_uma_Domain)

@given(instance=spem_uma_DisciplineGrouping_strategy)
@settings(max_examples=50)
def test_spem_uma_disciplinegrouping_instantiation(instance):
    assert isinstance(instance, spem_uma_DisciplineGrouping)

@given(instance=spem_uma_CustomCategory_strategy)
@settings(max_examples=50)
def test_spem_uma_customcategory_instantiation(instance):
    assert isinstance(instance, spem_uma_CustomCategory)

@given(instance=MethodContentPackage_strategy)
@settings(max_examples=50)
def test_methodcontentpackage_instantiation(instance):
    assert isinstance(instance, MethodContentPackage)

@given(instance=spem_uma_GuidancePackage_strategy)
@settings(max_examples=50)
def test_spem_uma_guidancepackage_instantiation(instance):
    assert isinstance(instance, spem_uma_GuidancePackage)

@given(instance=spem_uma_RoleSetPackage_strategy)
@settings(max_examples=50)
def test_spem_uma_rolesetpackage_instantiation(instance):
    assert isinstance(instance, spem_uma_RoleSetPackage)

@given(instance=spem_uma_ConfigurationPackage_strategy)
@settings(max_examples=50)
def test_spem_uma_configurationpackage_instantiation(instance):
    assert isinstance(instance, spem_uma_ConfigurationPackage)

@given(instance=spem_uma_DisciplinePackage_strategy)
@settings(max_examples=50)
def test_spem_uma_disciplinepackage_instantiation(instance):
    assert isinstance(instance, spem_uma_DisciplinePackage)

@given(instance=spem_uma_RoleDefinitionPackage_strategy)
@settings(max_examples=50)
def test_spem_uma_roledefinitionpackage_instantiation(instance):
    assert isinstance(instance, spem_uma_RoleDefinitionPackage)

@given(instance=spem_uma_ToolDefinitionPackage_strategy)
@settings(max_examples=50)
def test_spem_uma_tooldefinitionpackage_instantiation(instance):
    assert isinstance(instance, spem_uma_ToolDefinitionPackage)

@given(instance=spem_uma_WorkProductKindPackage_strategy)
@settings(max_examples=50)
def test_spem_uma_workproductkindpackage_instantiation(instance):
    assert isinstance(instance, spem_uma_WorkProductKindPackage)

@given(instance=spem_uma_DomainPackage_strategy)
@settings(max_examples=50)
def test_spem_uma_domainpackage_instantiation(instance):
    assert isinstance(instance, spem_uma_DomainPackage)

@given(instance=spem_uma_WorkProductDefinitionPackage_strategy)
@settings(max_examples=50)
def test_spem_uma_workproductdefinitionpackage_instantiation(instance):
    assert isinstance(instance, spem_uma_WorkProductDefinitionPackage)

@given(instance=spem_uma_QualificationPackage_strategy)
@settings(max_examples=50)
def test_spem_uma_qualificationpackage_instantiation(instance):
    assert isinstance(instance, spem_uma_QualificationPackage)

@given(instance=spem_uma_TaskDefinitionPackage_strategy)
@settings(max_examples=50)
def test_spem_uma_taskdefinitionpackage_instantiation(instance):
    assert isinstance(instance, spem_uma_TaskDefinitionPackage)

@given(instance=spem_uma_CategoryPackage_strategy)
@settings(max_examples=50)
def test_spem_uma_categorypackage_instantiation(instance):
    assert isinstance(instance, spem_uma_CategoryPackage)

@given(instance=Guidance_strategy)
@settings(max_examples=50)
def test_guidance_instantiation(instance):
    assert isinstance(instance, Guidance)

@given(instance=spem_uma_EstimatingConsideration_strategy)
@settings(max_examples=50)
def test_spem_uma_estimatingconsideration_instantiation(instance):
    assert isinstance(instance, spem_uma_EstimatingConsideration)

@given(instance=spem_uma_Template_strategy)
@settings(max_examples=50)
def test_spem_uma_template_instantiation(instance):
    assert isinstance(instance, spem_uma_Template)

@given(instance=spem_uma_Practice_strategy)
@settings(max_examples=50)
def test_spem_uma_practice_instantiation(instance):
    assert isinstance(instance, spem_uma_Practice)



@given(instance=spem_uma_Practice_strategy)
def test_spem_uma_practice_levelOfAdoption_setter(instance):
    original = instance.levelOfAdoption
    instance.levelOfAdoption = original
    assert instance.levelOfAdoption == original



@given(instance=spem_uma_Practice_strategy)
def test_spem_uma_practice_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original



@given(instance=spem_uma_Practice_strategy)
def test_spem_uma_practice_additionalInfo_setter(instance):
    original = instance.additionalInfo
    instance.additionalInfo = original
    assert instance.additionalInfo == original



@given(instance=spem_uma_Practice_strategy)
def test_spem_uma_practice_goal_setter(instance):
    original = instance.goal
    instance.goal = original
    assert instance.goal == original



@given(instance=spem_uma_Practice_strategy)
def test_spem_uma_practice_problem_setter(instance):
    original = instance.problem
    instance.problem = original
    assert instance.problem == original



@given(instance=spem_uma_Practice_strategy)
def test_spem_uma_practice_application_setter(instance):
    original = instance.application
    instance.application = original
    assert instance.application == original

@given(instance=spem_uma_TermDefinition_strategy)
@settings(max_examples=50)
def test_spem_uma_termdefinition_instantiation(instance):
    assert isinstance(instance, spem_uma_TermDefinition)

@given(instance=spem_uma_Guideline_strategy)
@settings(max_examples=50)
def test_spem_uma_guideline_instantiation(instance):
    assert isinstance(instance, spem_uma_Guideline)

@given(instance=spem_uma_Roadmap_strategy)
@settings(max_examples=50)
def test_spem_uma_roadmap_instantiation(instance):
    assert isinstance(instance, spem_uma_Roadmap)

@given(instance=spem_uma_Example_strategy)
@settings(max_examples=50)
def test_spem_uma_example_instantiation(instance):
    assert isinstance(instance, spem_uma_Example)

@given(instance=spem_uma_SupportingMaterial_strategy)
@settings(max_examples=50)
def test_spem_uma_supportingmaterial_instantiation(instance):
    assert isinstance(instance, spem_uma_SupportingMaterial)

@given(instance=spem_uma_ToolMentor_strategy)
@settings(max_examples=50)
def test_spem_uma_toolmentor_instantiation(instance):
    assert isinstance(instance, spem_uma_ToolMentor)

@given(instance=spem_uma_Concept_strategy)
@settings(max_examples=50)
def test_spem_uma_concept_instantiation(instance):
    assert isinstance(instance, spem_uma_Concept)

@given(instance=spem_uma_ReusableAsset_strategy)
@settings(max_examples=50)
def test_spem_uma_reusableasset_instantiation(instance):
    assert isinstance(instance, spem_uma_ReusableAsset)

@given(instance=spem_uma_Report_strategy)
@settings(max_examples=50)
def test_spem_uma_report_instantiation(instance):
    assert isinstance(instance, spem_uma_Report)

@given(instance=spem_uma_Checklist_strategy)
@settings(max_examples=50)
def test_spem_uma_checklist_instantiation(instance):
    assert isinstance(instance, spem_uma_Checklist)

@given(instance=uma_spem_TaskDefinition_strategy)
@settings(max_examples=50)
def test_uma_spem_taskdefinition_instantiation(instance):
    assert isinstance(instance, uma_spem_TaskDefinition)

@given(instance=Process_strategy)
@settings(max_examples=50)
def test_process_instantiation(instance):
    assert isinstance(instance, Process)

@given(instance=spem_uma_ProcessPlanningTemplate_strategy)
@settings(max_examples=50)
def test_spem_uma_processplanningtemplate_instantiation(instance):
    assert isinstance(instance, spem_uma_ProcessPlanningTemplate)

@given(instance=spem_uma_DeliveryProcess_strategy)
@settings(max_examples=50)
def test_spem_uma_deliveryprocess_instantiation(instance):
    assert isinstance(instance, spem_uma_DeliveryProcess)



@given(instance=spem_uma_DeliveryProcess_strategy)
def test_spem_uma_deliveryprocess_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=spem_uma_DeliveryProcess_strategy)
def test_spem_uma_deliveryprocess_projectCharacteristics_setter(instance):
    original = instance.projectCharacteristics
    instance.projectCharacteristics = original
    assert instance.projectCharacteristics == original



@given(instance=spem_uma_DeliveryProcess_strategy)
def test_spem_uma_deliveryprocess_typeOfContract_setter(instance):
    original = instance.typeOfContract
    instance.typeOfContract = original
    assert instance.typeOfContract == original



@given(instance=spem_uma_DeliveryProcess_strategy)
def test_spem_uma_deliveryprocess_riskLevel_setter(instance):
    original = instance.riskLevel
    instance.riskLevel = original
    assert instance.riskLevel == original



@given(instance=spem_uma_DeliveryProcess_strategy)
def test_spem_uma_deliveryprocess_projectMemberExpertise_setter(instance):
    original = instance.projectMemberExpertise
    instance.projectMemberExpertise = original
    assert instance.projectMemberExpertise == original



@given(instance=spem_uma_DeliveryProcess_strategy)
def test_spem_uma_deliveryprocess_estimatingTechnique_setter(instance):
    original = instance.estimatingTechnique
    instance.estimatingTechnique = original
    assert instance.estimatingTechnique == original

@given(instance=spem_uma_CapabilityPattern_strategy)
@settings(max_examples=50)
def test_spem_uma_capabilitypattern_instantiation(instance):
    assert isinstance(instance, spem_uma_CapabilityPattern)

@given(instance=spem_uma_Discipline_strategy)
@settings(max_examples=50)
def test_spem_uma_discipline_instantiation(instance):
    assert isinstance(instance, spem_uma_Discipline)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=WorkProductUse_strategy)
@settings(max_examples=50)
def test_workproductuse_instantiation(instance):
    assert isinstance(instance, WorkProductUse)

@given(instance=spem_uma_Outcome_strategy)
@settings(max_examples=50)
def test_spem_uma_outcome_instantiation(instance):
    assert isinstance(instance, spem_uma_Outcome)

@given(instance=spem_uma_Deliverable_strategy)
@settings(max_examples=50)
def test_spem_uma_deliverable_instantiation(instance):
    assert isinstance(instance, spem_uma_Deliverable)



@given(instance=spem_uma_Deliverable_strategy)
def test_spem_uma_deliverable_packagingGuidance_setter(instance):
    original = instance.packagingGuidance
    instance.packagingGuidance = original
    assert instance.packagingGuidance == original



@given(instance=spem_uma_Deliverable_strategy)
def test_spem_uma_deliverable_externalDescription_setter(instance):
    original = instance.externalDescription
    instance.externalDescription = original
    assert instance.externalDescription == original

@given(instance=spem_uma_Artifact_strategy)
@settings(max_examples=50)
def test_spem_uma_artifact_instantiation(instance):
    assert isinstance(instance, spem_uma_Artifact)

@given(instance=MethodLibraryPackageableElement_strategy)
@settings(max_examples=50)
def test_methodlibrarypackageableelement_instantiation(instance):
    assert isinstance(instance, MethodLibraryPackageableElement)

@given(instance=spem_MethodPluginPackageableElement_strategy)
@settings(max_examples=50)
def test_spem_methodpluginpackageableelement_instantiation(instance):
    assert isinstance(instance, spem_MethodPluginPackageableElement)

@given(instance=spem_MethodLibraryPackageableElement_strategy)
@settings(max_examples=50)
def test_spem_methodlibrarypackageableelement_instantiation(instance):
    assert isinstance(instance, spem_MethodLibraryPackageableElement)



@given(instance=spem_MethodLibraryPackageableElement_strategy)
def test_spem_methodlibrarypackageableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=spem_MethodLibrary_strategy)
@settings(max_examples=50)
def test_spem_methodlibrary_instantiation(instance):
    assert isinstance(instance, spem_MethodLibrary)



@given(instance=spem_MethodLibrary_strategy)
def test_spem_methodlibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=spem_MethodPlugin_strategy)
@settings(max_examples=50)
def test_spem_methodplugin_instantiation(instance):
    assert isinstance(instance, spem_MethodPlugin)

@given(instance=ProcessPackage_strategy)
@settings(max_examples=50)
def test_processpackage_instantiation(instance):
    assert isinstance(instance, ProcessPackage)

@given(instance=spem_uma_DeliveryProcessPackage_strategy)
@settings(max_examples=50)
def test_spem_uma_deliveryprocesspackage_instantiation(instance):
    assert isinstance(instance, spem_uma_DeliveryProcessPackage)

@given(instance=spem_uma_ProcessComponentPackage_strategy)
@settings(max_examples=50)
def test_spem_uma_processcomponentpackage_instantiation(instance):
    assert isinstance(instance, spem_uma_ProcessComponentPackage)

@given(instance=spem_uma_CapabilityPatternPackage_strategy)
@settings(max_examples=50)
def test_spem_uma_capabilitypatternpackage_instantiation(instance):
    assert isinstance(instance, spem_uma_CapabilityPatternPackage)

@given(instance=spem_ProcessComponent_strategy)
@settings(max_examples=50)
def test_spem_processcomponent_instantiation(instance):
    assert isinstance(instance, spem_ProcessComponent)

@given(instance=spem_VariabilityElement_strategy)
@settings(max_examples=50)
def test_spem_variabilityelement_instantiation(instance):
    assert isinstance(instance, spem_VariabilityElement)



@given(instance=spem_VariabilityElement_strategy)
def test_spem_variabilityelement_variabilityType_setter(instance):
    original = instance.variabilityType
    instance.variabilityType = original
    assert instance.variabilityType == original

@given(instance=RoleUse_strategy)
@settings(max_examples=50)
def test_roleuse_instantiation(instance):
    assert isinstance(instance, RoleUse)

@given(instance=spem_CompositeRole_strategy)
@settings(max_examples=50)
def test_spem_compositerole_instantiation(instance):
    assert isinstance(instance, spem_CompositeRole)

@given(instance=Kind_strategy)
@settings(max_examples=50)
def test_kind_instantiation(instance):
    assert isinstance(instance, Kind)

@given(instance=MethodPluginPackageableElement_strategy)
@settings(max_examples=50)
def test_methodpluginpackageableelement_instantiation(instance):
    assert isinstance(instance, MethodPluginPackageableElement)

@given(instance=spem_ProcessPackageableElement_strategy)
@settings(max_examples=50)
def test_spem_processpackageableelement_instantiation(instance):
    assert isinstance(instance, spem_ProcessPackageableElement)



@given(instance=spem_ProcessPackageableElement_strategy)
def test_spem_processpackageableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=spem_MethodContentPackageableElement_strategy)
@settings(max_examples=50)
def test_spem_methodcontentpackageableelement_instantiation(instance):
    assert isinstance(instance, spem_MethodContentPackageableElement)



@given(instance=spem_MethodContentPackageableElement_strategy)
def test_spem_methodcontentpackageableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MethodContentPackageableElement_strategy)
@settings(max_examples=50)
def test_methodcontentpackageableelement_instantiation(instance):
    assert isinstance(instance, MethodContentPackageableElement)

@given(instance=spem_MethodContentPackage_strategy)
@settings(max_examples=50)
def test_spem_methodcontentpackage_instantiation(instance):
    assert isinstance(instance, spem_MethodContentPackage)

@given(instance=MethodContentElement_strategy)
@settings(max_examples=50)
def test_methodcontentelement_instantiation(instance):
    assert isinstance(instance, MethodContentElement)

@given(instance=spem_Default_ResponsibilityAssignment_strategy)
@settings(max_examples=50)
def test_spem_default_responsibilityassignment_instantiation(instance):
    assert isinstance(instance, spem_Default_ResponsibilityAssignment)

@given(instance=spem_uma_RoleSet_strategy)
@settings(max_examples=50)
def test_spem_uma_roleset_instantiation(instance):
    assert isinstance(instance, spem_uma_RoleSet)

@given(instance=spem_Default_TaskDefinitionPerformer_strategy)
@settings(max_examples=50)
def test_spem_default_taskdefinitionperformer_instantiation(instance):
    assert isinstance(instance, spem_Default_TaskDefinitionPerformer)

@given(instance=spem_MethodContentKind_strategy)
@settings(max_examples=50)
def test_spem_methodcontentkind_instantiation(instance):
    assert isinstance(instance, spem_MethodContentKind)

@given(instance=spem_ToolDefinition_strategy)
@settings(max_examples=50)
def test_spem_tooldefinition_instantiation(instance):
    assert isinstance(instance, spem_ToolDefinition)

@given(instance=spem_WorkProductDefinition_strategy)
@settings(max_examples=50)
def test_spem_workproductdefinition_instantiation(instance):
    assert isinstance(instance, spem_WorkProductDefinition)

@given(instance=spem_uma_WorkProductKind_strategy)
@settings(max_examples=50)
def test_spem_uma_workproductkind_instantiation(instance):
    assert isinstance(instance, spem_uma_WorkProductKind)

@given(instance=spem_WorkProductDefinitionRelationship_strategy)
@settings(max_examples=50)
def test_spem_workproductdefinitionrelationship_instantiation(instance):
    assert isinstance(instance, spem_WorkProductDefinitionRelationship)

@given(instance=spem_Category_strategy)
@settings(max_examples=50)
def test_spem_category_instantiation(instance):
    assert isinstance(instance, spem_Category)

@given(instance=spem_Guidance_strategy)
@settings(max_examples=50)
def test_spem_guidance_instantiation(instance):
    assert isinstance(instance, spem_Guidance)

@given(instance=ProcessPackageableElement_strategy)
@settings(max_examples=50)
def test_processpackageableelement_instantiation(instance):
    assert isinstance(instance, ProcessPackageableElement)

@given(instance=spem_ProcessPackage_strategy)
@settings(max_examples=50)
def test_spem_processpackage_instantiation(instance):
    assert isinstance(instance, spem_ProcessPackage)

@given(instance=DescribableElement_strategy)
@settings(max_examples=50)
def test_describableelement_instantiation(instance):
    assert isinstance(instance, DescribableElement)

@given(instance=spem_Metric_strategy)
@settings(max_examples=50)
def test_spem_metric_instantiation(instance):
    assert isinstance(instance, spem_Metric)



@given(instance=spem_Metric_strategy)
def test_spem_metric_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=spem_ProcessElement_strategy)
@settings(max_examples=50)
def test_spem_processelement_instantiation(instance):
    assert isinstance(instance, spem_ProcessElement)

@given(instance=WorkDefinitionParameter_strategy)
@settings(max_examples=50)
def test_workdefinitionparameter_instantiation(instance):
    assert isinstance(instance, WorkDefinitionParameter)

@given(instance=spem_Default_TaskDefinitionParameter_strategy)
@settings(max_examples=50)
def test_spem_default_taskdefinitionparameter_instantiation(instance):
    assert isinstance(instance, spem_Default_TaskDefinitionParameter)



@given(instance=spem_Default_TaskDefinitionParameter_strategy)
def test_spem_default_taskdefinitionparameter_optionality_setter(instance):
    original = instance.optionality
    instance.optionality = original
    assert instance.optionality == original



@given(instance=spem_Default_TaskDefinitionParameter_strategy)
def test_spem_default_taskdefinitionparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=VariabilityElement_strategy)
@settings(max_examples=50)
def test_variabilityelement_instantiation(instance):
    assert isinstance(instance, VariabilityElement)

@given(instance=spem_MethodContentElement_strategy)
@settings(max_examples=50)
def test_spem_methodcontentelement_instantiation(instance):
    assert isinstance(instance, spem_MethodContentElement)

@given(instance=WorkBreakdownElement_strategy)
@settings(max_examples=50)
def test_workbreakdownelement_instantiation(instance):
    assert isinstance(instance, WorkBreakdownElement)

@given(instance=spem_Milestone_strategy)
@settings(max_examples=50)
def test_spem_milestone_instantiation(instance):
    assert isinstance(instance, spem_Milestone)

@given(instance=WorkDefinition_strategy)
@settings(max_examples=50)
def test_workdefinition_instantiation(instance):
    assert isinstance(instance, WorkDefinition)

@given(instance=spem_TaskDefinition_strategy)
@settings(max_examples=50)
def test_spem_taskdefinition_instantiation(instance):
    assert isinstance(instance, spem_TaskDefinition)

@given(instance=spem_Step_strategy)
@settings(max_examples=50)
def test_spem_step_instantiation(instance):
    assert isinstance(instance, spem_Step)



@given(instance=spem_Step_strategy)
def test_spem_step_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=spem_Activity_strategy)
@settings(max_examples=50)
def test_spem_activity_instantiation(instance):
    assert isinstance(instance, spem_Activity)



@given(instance=spem_Activity_strategy)
def test_spem_activity_useKind_setter(instance):
    original = instance.useKind
    instance.useKind = original
    assert instance.useKind == original



@given(instance=spem_Activity_strategy)
def test_spem_activity_isEnactable_setter(instance):
    original = instance.isEnactable
    instance.isEnactable = original
    assert instance.isEnactable == original

@given(instance=spem_Qualification_strategy)
@settings(max_examples=50)
def test_spem_qualification_instantiation(instance):
    assert isinstance(instance, spem_Qualification)

@given(instance=spem_RoleDefinition_strategy)
@settings(max_examples=50)
def test_spem_roledefinition_instantiation(instance):
    assert isinstance(instance, spem_RoleDefinition)



@given(instance=spem_RoleDefinition_strategy)
def test_spem_roledefinition_synonym_setter(instance):
    original = instance.synonym
    instance.synonym = original
    assert instance.synonym == original

@given(instance=MethodContentUse_strategy)
@settings(max_examples=50)
def test_methodcontentuse_instantiation(instance):
    assert isinstance(instance, MethodContentUse)

@given(instance=spem_ProcessComponentUse_strategy)
@settings(max_examples=50)
def test_spem_processcomponentuse_instantiation(instance):
    assert isinstance(instance, spem_ProcessComponentUse)

@given(instance=spem_WorkProductUse_strategy)
@settings(max_examples=50)
def test_spem_workproductuse_instantiation(instance):
    assert isinstance(instance, spem_WorkProductUse)

@given(instance=spem_TaskUse_strategy)
@settings(max_examples=50)
def test_spem_taskuse_instantiation(instance):
    assert isinstance(instance, spem_TaskUse)



@given(instance=spem_TaskUse_strategy)
def test_spem_taskuse_preCondition_setter(instance):
    original = instance.preCondition
    instance.preCondition = original
    assert instance.preCondition == original



@given(instance=spem_TaskUse_strategy)
def test_spem_taskuse_postCondition_setter(instance):
    original = instance.postCondition
    instance.postCondition = original
    assert instance.postCondition == original

@given(instance=spem_RoleUse_strategy)
@settings(max_examples=50)
def test_spem_roleuse_instantiation(instance):
    assert isinstance(instance, spem_RoleUse)

@given(instance=WorkDefinitionPerformer_strategy)
@settings(max_examples=50)
def test_workdefinitionperformer_instantiation(instance):
    assert isinstance(instance, WorkDefinitionPerformer)

@given(instance=spem_MethodConfiguration_strategy)
@settings(max_examples=50)
def test_spem_methodconfiguration_instantiation(instance):
    assert isinstance(instance, spem_MethodConfiguration)

@given(instance=spem_WorkDefinitionParameter_strategy)
@settings(max_examples=50)
def test_spem_workdefinitionparameter_instantiation(instance):
    assert isinstance(instance, spem_WorkDefinitionParameter)



@given(instance=spem_WorkDefinitionParameter_strategy)
def test_spem_workdefinitionparameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=BreakdownElement_strategy)
@settings(max_examples=50)
def test_breakdownelement_instantiation(instance):
    assert isinstance(instance, BreakdownElement)

@given(instance=spem_ProcessPerformer_strategy)
@settings(max_examples=50)
def test_spem_processperformer_instantiation(instance):
    assert isinstance(instance, spem_ProcessPerformer)

@given(instance=spem_ProcessResponsibilityAssignment_strategy)
@settings(max_examples=50)
def test_spem_processresponsibilityassignment_instantiation(instance):
    assert isinstance(instance, spem_ProcessResponsibilityAssignment)

@given(instance=spem_MethodContentUse_strategy)
@settings(max_examples=50)
def test_spem_methodcontentuse_instantiation(instance):
    assert isinstance(instance, spem_MethodContentUse)



@given(instance=spem_MethodContentUse_strategy)
def test_spem_methodcontentuse_isSynchronizedWithSource_setter(instance):
    original = instance.isSynchronizedWithSource
    instance.isSynchronizedWithSource = original
    assert instance.isSynchronizedWithSource == original

@given(instance=spem_activity_Edge_strategy)
@settings(max_examples=50)
def test_spem_activity_edge_instantiation(instance):
    assert isinstance(instance, spem_activity_Edge)



@given(instance=spem_activity_Edge_strategy)
def test_spem_activity_edge_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=spem_TeamProfile_strategy)
@settings(max_examples=50)
def test_spem_teamprofile_instantiation(instance):
    assert isinstance(instance, spem_TeamProfile)

@given(instance=spem_activity_Node_strategy)
@settings(max_examples=50)
def test_spem_activity_node_instantiation(instance):
    assert isinstance(instance, spem_activity_Node)

@given(instance=spem_ProcessParameter_strategy)
@settings(max_examples=50)
def test_spem_processparameter_instantiation(instance):
    assert isinstance(instance, spem_ProcessParameter)



@given(instance=spem_ProcessParameter_strategy)
def test_spem_processparameter_optionality_setter(instance):
    original = instance.optionality
    instance.optionality = original
    assert instance.optionality == original

@given(instance=spem_WorkProductUseRelationship_strategy)
@settings(max_examples=50)
def test_spem_workproductuserelationship_instantiation(instance):
    assert isinstance(instance, spem_WorkProductUseRelationship)



@given(instance=spem_WorkProductUseRelationship_strategy)
def test_spem_workproductuserelationship_relationshipKind_setter(instance):
    original = instance.relationshipKind
    instance.relationshipKind = original
    assert instance.relationshipKind == original

@given(instance=spem_WorkSequence_strategy)
@settings(max_examples=50)
def test_spem_worksequence_instantiation(instance):
    assert isinstance(instance, spem_WorkSequence)



@given(instance=spem_WorkSequence_strategy)
def test_spem_worksequence_linkKind_setter(instance):
    original = instance.linkKind
    instance.linkKind = original
    assert instance.linkKind == original

@given(instance=spem_WorkBreakdownElement_strategy)
@settings(max_examples=50)
def test_spem_workbreakdownelement_instantiation(instance):
    assert isinstance(instance, spem_WorkBreakdownElement)



@given(instance=spem_WorkBreakdownElement_strategy)
def test_spem_workbreakdownelement_isEventDriven_setter(instance):
    original = instance.isEventDriven
    instance.isEventDriven = original
    assert instance.isEventDriven == original



@given(instance=spem_WorkBreakdownElement_strategy)
def test_spem_workbreakdownelement_isOngoing_setter(instance):
    original = instance.isOngoing
    instance.isOngoing = original
    assert instance.isOngoing == original



@given(instance=spem_WorkBreakdownElement_strategy)
def test_spem_workbreakdownelement_isRepeatable_setter(instance):
    original = instance.isRepeatable
    instance.isRepeatable = original
    assert instance.isRepeatable == original

@given(instance=ProcessElement_strategy)
@settings(max_examples=50)
def test_processelement_instantiation(instance):
    assert isinstance(instance, ProcessElement)

@given(instance=spem_WorkProductPortConnector_strategy)
@settings(max_examples=50)
def test_spem_workproductportconnector_instantiation(instance):
    assert isinstance(instance, spem_WorkProductPortConnector)

@given(instance=spem_PlanningData_strategy)
@settings(max_examples=50)
def test_spem_planningdata_instantiation(instance):
    assert isinstance(instance, spem_PlanningData)



@given(instance=spem_PlanningData_strategy)
def test_spem_planningdata_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original



@given(instance=spem_PlanningData_strategy)
def test_spem_planningdata_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=spem_PlanningData_strategy)
def test_spem_planningdata_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original



@given(instance=spem_PlanningData_strategy)
def test_spem_planningdata_finishDate_setter(instance):
    original = instance.finishDate
    instance.finishDate = original
    assert instance.finishDate == original

@given(instance=spem_WorkProductPort_strategy)
@settings(max_examples=50)
def test_spem_workproductport_instantiation(instance):
    assert isinstance(instance, spem_WorkProductPort)



@given(instance=spem_WorkProductPort_strategy)
def test_spem_workproductport_portKind_setter(instance):
    original = instance.portKind
    instance.portKind = original
    assert instance.portKind == original



@given(instance=spem_WorkProductPort_strategy)
def test_spem_workproductport_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=spem_ProcessKind_strategy)
@settings(max_examples=50)
def test_spem_processkind_instantiation(instance):
    assert isinstance(instance, spem_ProcessKind)

@given(instance=spem_BreakdownElement_strategy)
@settings(max_examples=50)
def test_spem_breakdownelement_instantiation(instance):
    assert isinstance(instance, spem_BreakdownElement)



@given(instance=spem_BreakdownElement_strategy)
def test_spem_breakdownelement_hasMultipleOccurrences_setter(instance):
    original = instance.hasMultipleOccurrences
    instance.hasMultipleOccurrences = original
    assert instance.hasMultipleOccurrences == original



@given(instance=spem_BreakdownElement_strategy)
def test_spem_breakdownelement_isPlanned_setter(instance):
    original = instance.isPlanned
    instance.isPlanned = original
    assert instance.isPlanned == original



@given(instance=spem_BreakdownElement_strategy)
def test_spem_breakdownelement_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=spem_WorkDefinition_strategy)
@settings(max_examples=50)
def test_spem_workdefinition_instantiation(instance):
    assert isinstance(instance, spem_WorkDefinition)



@given(instance=spem_WorkDefinition_strategy)
def test_spem_workdefinition_postCondition_setter(instance):
    original = instance.postCondition
    instance.postCondition = original
    assert instance.postCondition == original



@given(instance=spem_WorkDefinition_strategy)
def test_spem_workdefinition_preCondition_setter(instance):
    original = instance.preCondition
    instance.preCondition = original
    assert instance.preCondition == original

@given(instance=spem_WorkDefinitionPerformer_strategy)
@settings(max_examples=50)
def test_spem_workdefinitionperformer_instantiation(instance):
    assert isinstance(instance, spem_WorkDefinitionPerformer)

@given(instance=ExtensibleElement_strategy)
@settings(max_examples=50)
def test_extensibleelement_instantiation(instance):
    assert isinstance(instance, ExtensibleElement)

@given(instance=spem_DescribableElement_strategy)
@settings(max_examples=50)
def test_spem_describableelement_instantiation(instance):
    assert isinstance(instance, spem_DescribableElement)



@given(instance=spem_DescribableElement_strategy)
def test_spem_describableelement_briefDescription_setter(instance):
    original = instance.briefDescription
    instance.briefDescription = original
    assert instance.briefDescription == original



@given(instance=spem_DescribableElement_strategy)
def test_spem_describableelement_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=spem_DescribableElement_strategy)
def test_spem_describableelement_purpose_setter(instance):
    original = instance.purpose
    instance.purpose = original
    assert instance.purpose == original



@given(instance=spem_DescribableElement_strategy)
def test_spem_describableelement_mainDescription_setter(instance):
    original = instance.mainDescription
    instance.mainDescription = original
    assert instance.mainDescription == original



@given(instance=spem_DescribableElement_strategy)
def test_spem_describableelement_copyright_setter(instance):
    original = instance.copyright
    instance.copyright = original
    assert instance.copyright == original



@given(instance=spem_DescribableElement_strategy)
def test_spem_describableelement_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=spem_DescribableElement_strategy)
def test_spem_describableelement_changeDate_setter(instance):
    original = instance.changeDate
    instance.changeDate = original
    assert instance.changeDate == original



@given(instance=spem_DescribableElement_strategy)
def test_spem_describableelement_changeDescription_setter(instance):
    original = instance.changeDescription
    instance.changeDescription = original
    assert instance.changeDescription == original



@given(instance=spem_DescribableElement_strategy)
def test_spem_describableelement_presentationName_setter(instance):
    original = instance.presentationName
    instance.presentationName = original
    assert instance.presentationName == original

@given(instance=spem_Kind_strategy)
@settings(max_examples=50)
def test_spem_kind_instantiation(instance):
    assert isinstance(instance, spem_Kind)

@given(instance=spem_ExtensibleElement_strategy)
@settings(max_examples=50)
def test_spem_extensibleelement_instantiation(instance):
    assert isinstance(instance, spem_ExtensibleElement)

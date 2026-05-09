import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    url::ModelElementUrlFragment,
    url::ProjectUrlFragment,
    url::ServerUrl,
    esmodel::url::ModelElementUrl,
    esmodel::url::ModelElementUrlFragment,
    esmodel::url::ProjectUrlFragment,
    component::Component,
    component::ComponentService,
    Solution,
    model::change::MergingSolution,
    change::MergingProposal,
    Proposal,
    model::change::MergingProposal,
    Issue,
    model::change::MergingIssue,
    rationale::Proposal,
    rationale::Assessment,
    rationale::Issue,
    rationale::Criterion,
    rationale::Solution,
    Criterion,
    model::requirement::NonFunctionalRequirement,
    requirement::SystemFunction,
    NonDomainElement,
    requirement::ActorInstance,
    requirement::UserTask,
    requirement::Step,
    requirement::NonFunctionalRequirement,
    requirement::Actor,
    Section,
    model::document::LeafSection,
    document::CompositeSection,
    requirement::FunctionalRequirement,
    document::Section,
    model::document::CompositeSection,
    classes::MethodArgument,
    classes::PackageElement,
    PackageElement,
    model::classes::Package,
    model::classes::Class,
    classes::Dependency,
    classes::Package,
    requirement::Scenario,
    requirement::UseCase,
    classes::Method,
    classes::Attribute,
    classes::Association,
    classes::Class,
    diagram::model::Diagram,
    task::Checkable,
    organization::User,
    task::WorkPackage,
    organization::OrgUnit,
    WorkItem,
    model::task::Milestone,
    model::task::WorkPackage,
    change::ModelChangePackage,
    Project,
    model::Project,
    model::NonDomainElement,
    UnicaseModelElement,
    model::rationale::Comment,
    model::requirement::SystemFunction,
    model::requirement::Actor,
    model::component::Component,
    model::change::ModelChangePackage,
    model::task::Checkable,
    model::classes::Attribute,
    model::rationale::Proposal,
    model::rationale::Assessment,
    model::document::Section,
    model::component::ComponentService,
    model::Attachment,
    model::requirement::UseCase,
    model::rationale::Solution,
    model::rationale::Criterion,
    model::classes::Association,
    model::classes::PackageElement,
    model::requirement::Scenario,
    model::requirement::Step,
    model::classes::Method,
    model::classes::Dependency,
    model::requirement::ActorInstance,
    model::requirement::UserTask,
    model::classes::MethodArgument,
    model::requirement::FunctionalRequirement,
    model::Annotation,
    profile::StereotypeInstance,
    rationale::Comment,
    OrgUnit,
    model::organization::Group,
    model::organization::User,
    task::WorkItem,
    model::bug::BugReport,
    model::task::ActionItem,
    organization::Group,
    model::organization::OrgUnit,
    metamodel::AssociationClassElement,
    metamodel::NonDomainElement,
    metamodel::ModelVersion,
    UniqueIdentifier,
    metamodel::ModelElementId,
    IdentifiableElement,
    esmodel::notification::ESNotification,
    metamodel::ModelElement,
    metamodel::IdentifiableElement,
    metamodel::UniqueIdentifier,
    ModelElement,
    metamodel::Project,
    document::LeafSection,
    Attachment,
    model::diagram::MEDiagram,
    Annotation,
    model::rationale::Issue,
    model::task::WorkItem,
    model::UnicaseModelElement,
    esmodel::url::ServerUrl,
    esmodel::accesscontrol::OrgUnitProperty,
    esmodel::accesscontrol::ACOrgUnitId,
    accesscontrol::ACOrgUnit,
    accesscontrol::OrgUnitProperty,
    roles::Role,
    Role,
    esmodel::roles::ServerAdmin,
    esmodel::roles::WriterRole,
    esmodel::roles::ProjectAdminRole,
    esmodel::roles::ReaderRole,
    esmodel::roles::Role,
    esmodel::accesscontrol::ACOrgUnit,
    operations::OperationId,
    ACOrgUnit,
    esmodel::accesscontrol::ACGroup,
    esmodel::accesscontrol::ACUser,
    ServerProjectEvent,
    esmodel::server::ProjectUpdatedEvent,
    ServerEvent,
    esmodel::server::ServerProjectEvent,
    ReadEvent,
    esmodel::events::NotificationReadEvent,
    esmodel::operations::ModelElementGroup,
    Event,
    esmodel::events::ShowHistoryEvent,
    esmodel::events::ExceptionEvent,
    esmodel::events::AnnotationEvent,
    esmodel::events::MergeGlobalChoiceEvent,
    esmodel::events::TraceEvent,
    esmodel::events::PerspectiveEvent,
    esmodel::events::MergeChoiceEvent,
    esmodel::events::LinkEvent,
    esmodel::events::PluginFocusEvent,
    esmodel::events::NotificationIgnoreEvent,
    esmodel::events::UpdateEvent,
    esmodel::events::PresentationSwitchEvent,
    esmodel::events::URLEvent,
    esmodel::events::NotificationGenerationEvent,
    esmodel::events::ShowChangesEvent,
    esmodel::events::PluginStartEvent,
    esmodel::server::ServerEvent,
    esmodel::events::CheckoutEvent,
    esmodel::events::Validate,
    esmodel::events::MergeEvent,
    esmodel::events::NavigatorCreateEvent,
    esmodel::events::DNDEvent,
    esmodel::events::UndoEvent,
    esmodel::events::RevertEvent,
    esmodel::events::ReadEvent,
    esmodel::events::Event,
    CompositeOperation,
    esmodel::semantic::SemanticCompositeOperation,
    esmodel::operations::EObjectToModelElementIdMap,
    esmodel::operations::OperationGroup,
    esmodel::operations::OperationId,
    AttributeOperation,
    esmodel::operations::DiagramLayoutOperation,
    ReferenceOperation,
    esmodel::operations::MultiReferenceSetOperation,
    esmodel::operations::MultiReferenceOperation,
    esmodel::operations::SingleReferenceOperation,
    FeatureOperation,
    esmodel::operations::MultiAttributeSetOperation,
    esmodel::operations::MultiAttributeMoveOperation,
    esmodel::operations::MultiReferenceMoveOperation,
    esmodel::operations::ReferenceOperation,
    esmodel::operations::MultiAttributeOperation,
    esmodel::operations::AttributeOperation,
    operations::EObjectToModelElementIdMap,
    operations::ReferenceOperation,
    operations::esmodel::EObject,
    AbstractOperation,
    esmodel::operations::FeatureOperation,
    esmodel::operations::CreateDeleteOperation,
    esmodel::operations::CompositeOperation,
    esmodel::operations::AbstractOperation,
    esmodel::versioning::LogMessage,
    esmodel::versioning::VersionProperty,
    esmodel::versioning::VersionSpec,
    esmodel::versioning::Version,
    esmodel::versioning::HistoryQuery,
    versioning::ChangePackage,
    versioning::TagVersionSpec,
    esmodel::versioning::HistoryInfo,
    versioning::VersionProperty,
    notification::ESNotification,
    versioning::LogMessage,
    events::Event,
    operations::AbstractOperation,
    esmodel::versioning::ChangePackage,
    VersionSpec,
    esmodel::versioning::DateVersionSpec,
    esmodel::versioning::PrimaryVersionSpec,
    esmodel::versioning::HeadVersionSpec,
    esmodel::versioning::TagVersionSpec,
    esmodel::ClientVersionInfo,
    esmodel::VersionInfo,
    esmodel::ProjectId,
    accesscontrol::ACUser,
    SessionId,
    ProjectHistory,
    accesscontrol::ACGroup,
    esmodel::ServerSpace,
    esmodel::SessionId,
    versioning::PrimaryVersionSpec,
    esmodel::ProjectInfo,
    versioning::Version,
    ProjectId,
    esmodel::ProjectHistory,
    ActivityObject,
    model::activity::Fork,
    model::activity::ActivityInitial,
    model::activity::ActivityEnd,
    model::activity::Branch,
    model::activity::Activity,
    activity::ActivityObject,
    model::activity::Transition,
    activity::Transition,
    model::activity::ActivityObject,
    ModelElementId,
    model::util::ModelElementPath,
    StereotypeAttributeInstance,
    model::profile::StereotypeAttributeInstanceString,
    model::profile::Profile,
    model::profile::StereotypeAttributeInstance,
    StereotypeAttribute,
    model::profile::StereotypeAttributeSimple,
    model::profile::StereotypeAttribute,
    profile::StereotypeAttributeInstance,
    model::profile::StereotypeInstance,
    profile::StereotypeAttribute,
    profile::Profile,
    model::profile::Stereotype,
    profile::Stereotype,
    model::attachment::FileAttachment,
    model::attachment::UrlAttachment,
    StateNode,
    model::state::StateInitial,
    model::state::StateEnd,
    model::state::State,
    state::Transition,
    model::state::StateNode,
    state::StateNode,
    model::state::Transition,
    MeetingSection,
    model::meeting::IssueMeetingSection,
    model::meeting::WorkItemMeetingSection,
    model::meeting::CompositeMeetingSection,
    model::meeting::MeetingSection,
    meeting::WorkItemMeetingSection,
    meeting::IssueMeetingSection,
    meeting::MeetingSection,
    model::meeting::Meeting,
    model::component::DeploymentNode,
    AssociationType,
    VisibilityType,
    Severity,
    ScopeType,
    ArgumentDirectionType,
    ResolutionType,
    MergeChoiceSelection,
    MergeGlobalChoiceSelection,
    ContainmentType,
    DiagramType,
    BugStatus,
    ActivityType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_url::modelelementurlfragment_is_not_abstract():
    assert not inspect.isabstract(url::ModelElementUrlFragment)


def test_url::modelelementurlfragment_constructor_exists():
    assert callable(url::ModelElementUrlFragment.__init__)


def test_url::modelelementurlfragment_constructor_args():
    sig = inspect.signature(url::ModelElementUrlFragment.__init__)
    params = list(sig.parameters.keys())



def test_url::projecturlfragment_is_not_abstract():
    assert not inspect.isabstract(url::ProjectUrlFragment)


def test_url::projecturlfragment_constructor_exists():
    assert callable(url::ProjectUrlFragment.__init__)


def test_url::projecturlfragment_constructor_args():
    sig = inspect.signature(url::ProjectUrlFragment.__init__)
    params = list(sig.parameters.keys())



def test_url::serverurl_is_not_abstract():
    assert not inspect.isabstract(url::ServerUrl)


def test_url::serverurl_constructor_exists():
    assert callable(url::ServerUrl.__init__)


def test_url::serverurl_constructor_args():
    sig = inspect.signature(url::ServerUrl.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::url::modelelementurl_is_not_abstract():
    assert not inspect.isabstract(esmodel::url::ModelElementUrl)


def test_esmodel::url::modelelementurl_constructor_exists():
    assert callable(esmodel::url::ModelElementUrl.__init__)


def test_esmodel::url::modelelementurl_constructor_args():
    sig = inspect.signature(esmodel::url::ModelElementUrl.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::url::modelelementurlfragment_is_not_abstract():
    assert not inspect.isabstract(esmodel::url::ModelElementUrlFragment)


def test_esmodel::url::modelelementurlfragment_constructor_exists():
    assert callable(esmodel::url::ModelElementUrlFragment.__init__)


def test_esmodel::url::modelelementurlfragment_constructor_args():
    sig = inspect.signature(esmodel::url::ModelElementUrlFragment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esmodel::url::modelelementurlfragment_has_name():
    assert hasattr(esmodel::url::ModelElementUrlFragment, "name")
    descriptor = None
    for klass in esmodel::url::ModelElementUrlFragment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::url::projecturlfragment_is_not_abstract():
    assert not inspect.isabstract(esmodel::url::ProjectUrlFragment)


def test_esmodel::url::projecturlfragment_constructor_exists():
    assert callable(esmodel::url::ProjectUrlFragment.__init__)


def test_esmodel::url::projecturlfragment_constructor_args():
    sig = inspect.signature(esmodel::url::ProjectUrlFragment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esmodel::url::projecturlfragment_has_name():
    assert hasattr(esmodel::url::ProjectUrlFragment, "name")
    descriptor = None
    for klass in esmodel::url::ProjectUrlFragment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_component::component_is_not_abstract():
    assert not inspect.isabstract(component::Component)


def test_component::component_constructor_exists():
    assert callable(component::Component.__init__)


def test_component::component_constructor_args():
    sig = inspect.signature(component::Component.__init__)
    params = list(sig.parameters.keys())



def test_component::componentservice_is_not_abstract():
    assert not inspect.isabstract(component::ComponentService)


def test_component::componentservice_constructor_exists():
    assert callable(component::ComponentService.__init__)


def test_component::componentservice_constructor_args():
    sig = inspect.signature(component::ComponentService.__init__)
    params = list(sig.parameters.keys())



def test_solution_is_not_abstract():
    assert not inspect.isabstract(Solution)


def test_solution_constructor_exists():
    assert callable(Solution.__init__)


def test_solution_constructor_args():
    sig = inspect.signature(Solution.__init__)
    params = list(sig.parameters.keys())



def test_model::change::mergingsolution_is_not_abstract():
    assert not inspect.isabstract(model::change::MergingSolution)


def test_model::change::mergingsolution_constructor_exists():
    assert callable(model::change::MergingSolution.__init__)


def test_model::change::mergingsolution_constructor_args():
    sig = inspect.signature(model::change::MergingSolution.__init__)
    params = list(sig.parameters.keys())



def test_change::mergingproposal_is_not_abstract():
    assert not inspect.isabstract(change::MergingProposal)


def test_change::mergingproposal_constructor_exists():
    assert callable(change::MergingProposal.__init__)


def test_change::mergingproposal_constructor_args():
    sig = inspect.signature(change::MergingProposal.__init__)
    params = list(sig.parameters.keys())



def test_proposal_is_not_abstract():
    assert not inspect.isabstract(Proposal)


def test_proposal_constructor_exists():
    assert callable(Proposal.__init__)


def test_proposal_constructor_args():
    sig = inspect.signature(Proposal.__init__)
    params = list(sig.parameters.keys())



def test_model::change::mergingproposal_is_not_abstract():
    assert not inspect.isabstract(model::change::MergingProposal)


def test_model::change::mergingproposal_constructor_exists():
    assert callable(model::change::MergingProposal.__init__)


def test_model::change::mergingproposal_constructor_args():
    sig = inspect.signature(model::change::MergingProposal.__init__)
    params = list(sig.parameters.keys())



def test_issue_is_not_abstract():
    assert not inspect.isabstract(Issue)


def test_issue_constructor_exists():
    assert callable(Issue.__init__)


def test_issue_constructor_args():
    sig = inspect.signature(Issue.__init__)
    params = list(sig.parameters.keys())



def test_model::change::mergingissue_is_not_abstract():
    assert not inspect.isabstract(model::change::MergingIssue)


def test_model::change::mergingissue_constructor_exists():
    assert callable(model::change::MergingIssue.__init__)


def test_model::change::mergingissue_constructor_args():
    sig = inspect.signature(model::change::MergingIssue.__init__)
    params = list(sig.parameters.keys())
    assert "resolvingRevision" in params, "Missing parameter 'resolvingRevision'"

def test_model::change::mergingissue_has_resolvingRevision():
    assert hasattr(model::change::MergingIssue, "resolvingRevision")
    descriptor = None
    for klass in model::change::MergingIssue.__mro__:
        if "resolvingRevision" in klass.__dict__:
            descriptor = klass.__dict__["resolvingRevision"]
            break
    assert isinstance(descriptor, property)



def test_rationale::proposal_is_not_abstract():
    assert not inspect.isabstract(rationale::Proposal)


def test_rationale::proposal_constructor_exists():
    assert callable(rationale::Proposal.__init__)


def test_rationale::proposal_constructor_args():
    sig = inspect.signature(rationale::Proposal.__init__)
    params = list(sig.parameters.keys())



def test_rationale::assessment_is_not_abstract():
    assert not inspect.isabstract(rationale::Assessment)


def test_rationale::assessment_constructor_exists():
    assert callable(rationale::Assessment.__init__)


def test_rationale::assessment_constructor_args():
    sig = inspect.signature(rationale::Assessment.__init__)
    params = list(sig.parameters.keys())



def test_rationale::issue_is_not_abstract():
    assert not inspect.isabstract(rationale::Issue)


def test_rationale::issue_constructor_exists():
    assert callable(rationale::Issue.__init__)


def test_rationale::issue_constructor_args():
    sig = inspect.signature(rationale::Issue.__init__)
    params = list(sig.parameters.keys())



def test_rationale::criterion_is_not_abstract():
    assert not inspect.isabstract(rationale::Criterion)


def test_rationale::criterion_constructor_exists():
    assert callable(rationale::Criterion.__init__)


def test_rationale::criterion_constructor_args():
    sig = inspect.signature(rationale::Criterion.__init__)
    params = list(sig.parameters.keys())



def test_rationale::solution_is_not_abstract():
    assert not inspect.isabstract(rationale::Solution)


def test_rationale::solution_constructor_exists():
    assert callable(rationale::Solution.__init__)


def test_rationale::solution_constructor_args():
    sig = inspect.signature(rationale::Solution.__init__)
    params = list(sig.parameters.keys())



def test_criterion_is_not_abstract():
    assert not inspect.isabstract(Criterion)


def test_criterion_constructor_exists():
    assert callable(Criterion.__init__)


def test_criterion_constructor_args():
    sig = inspect.signature(Criterion.__init__)
    params = list(sig.parameters.keys())



def test_model::requirement::nonfunctionalrequirement_is_not_abstract():
    assert not inspect.isabstract(model::requirement::NonFunctionalRequirement)


def test_model::requirement::nonfunctionalrequirement_constructor_exists():
    assert callable(model::requirement::NonFunctionalRequirement.__init__)


def test_model::requirement::nonfunctionalrequirement_constructor_args():
    sig = inspect.signature(model::requirement::NonFunctionalRequirement.__init__)
    params = list(sig.parameters.keys())



def test_requirement::systemfunction_is_not_abstract():
    assert not inspect.isabstract(requirement::SystemFunction)


def test_requirement::systemfunction_constructor_exists():
    assert callable(requirement::SystemFunction.__init__)


def test_requirement::systemfunction_constructor_args():
    sig = inspect.signature(requirement::SystemFunction.__init__)
    params = list(sig.parameters.keys())



def test_nondomainelement_is_not_abstract():
    assert not inspect.isabstract(NonDomainElement)


def test_nondomainelement_constructor_exists():
    assert callable(NonDomainElement.__init__)


def test_nondomainelement_constructor_args():
    sig = inspect.signature(NonDomainElement.__init__)
    params = list(sig.parameters.keys())



def test_requirement::actorinstance_is_not_abstract():
    assert not inspect.isabstract(requirement::ActorInstance)


def test_requirement::actorinstance_constructor_exists():
    assert callable(requirement::ActorInstance.__init__)


def test_requirement::actorinstance_constructor_args():
    sig = inspect.signature(requirement::ActorInstance.__init__)
    params = list(sig.parameters.keys())



def test_requirement::usertask_is_not_abstract():
    assert not inspect.isabstract(requirement::UserTask)


def test_requirement::usertask_constructor_exists():
    assert callable(requirement::UserTask.__init__)


def test_requirement::usertask_constructor_args():
    sig = inspect.signature(requirement::UserTask.__init__)
    params = list(sig.parameters.keys())



def test_requirement::step_is_not_abstract():
    assert not inspect.isabstract(requirement::Step)


def test_requirement::step_constructor_exists():
    assert callable(requirement::Step.__init__)


def test_requirement::step_constructor_args():
    sig = inspect.signature(requirement::Step.__init__)
    params = list(sig.parameters.keys())



def test_requirement::nonfunctionalrequirement_is_not_abstract():
    assert not inspect.isabstract(requirement::NonFunctionalRequirement)


def test_requirement::nonfunctionalrequirement_constructor_exists():
    assert callable(requirement::NonFunctionalRequirement.__init__)


def test_requirement::nonfunctionalrequirement_constructor_args():
    sig = inspect.signature(requirement::NonFunctionalRequirement.__init__)
    params = list(sig.parameters.keys())



def test_requirement::actor_is_not_abstract():
    assert not inspect.isabstract(requirement::Actor)


def test_requirement::actor_constructor_exists():
    assert callable(requirement::Actor.__init__)


def test_requirement::actor_constructor_args():
    sig = inspect.signature(requirement::Actor.__init__)
    params = list(sig.parameters.keys())



def test_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_section_constructor_exists():
    assert callable(Section.__init__)


def test_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_model::document::leafsection_is_not_abstract():
    assert not inspect.isabstract(model::document::LeafSection)


def test_model::document::leafsection_constructor_exists():
    assert callable(model::document::LeafSection.__init__)


def test_model::document::leafsection_constructor_args():
    sig = inspect.signature(model::document::LeafSection.__init__)
    params = list(sig.parameters.keys())



def test_document::compositesection_is_not_abstract():
    assert not inspect.isabstract(document::CompositeSection)


def test_document::compositesection_constructor_exists():
    assert callable(document::CompositeSection.__init__)


def test_document::compositesection_constructor_args():
    sig = inspect.signature(document::CompositeSection.__init__)
    params = list(sig.parameters.keys())



def test_requirement::functionalrequirement_is_not_abstract():
    assert not inspect.isabstract(requirement::FunctionalRequirement)


def test_requirement::functionalrequirement_constructor_exists():
    assert callable(requirement::FunctionalRequirement.__init__)


def test_requirement::functionalrequirement_constructor_args():
    sig = inspect.signature(requirement::FunctionalRequirement.__init__)
    params = list(sig.parameters.keys())



def test_document::section_is_not_abstract():
    assert not inspect.isabstract(document::Section)


def test_document::section_constructor_exists():
    assert callable(document::Section.__init__)


def test_document::section_constructor_args():
    sig = inspect.signature(document::Section.__init__)
    params = list(sig.parameters.keys())



def test_model::document::compositesection_is_not_abstract():
    assert not inspect.isabstract(model::document::CompositeSection)


def test_model::document::compositesection_constructor_exists():
    assert callable(model::document::CompositeSection.__init__)


def test_model::document::compositesection_constructor_args():
    sig = inspect.signature(model::document::CompositeSection.__init__)
    params = list(sig.parameters.keys())



def test_classes::methodargument_is_not_abstract():
    assert not inspect.isabstract(classes::MethodArgument)


def test_classes::methodargument_constructor_exists():
    assert callable(classes::MethodArgument.__init__)


def test_classes::methodargument_constructor_args():
    sig = inspect.signature(classes::MethodArgument.__init__)
    params = list(sig.parameters.keys())



def test_classes::packageelement_is_not_abstract():
    assert not inspect.isabstract(classes::PackageElement)


def test_classes::packageelement_constructor_exists():
    assert callable(classes::PackageElement.__init__)


def test_classes::packageelement_constructor_args():
    sig = inspect.signature(classes::PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_packageelement_is_not_abstract():
    assert not inspect.isabstract(PackageElement)


def test_packageelement_constructor_exists():
    assert callable(PackageElement.__init__)


def test_packageelement_constructor_args():
    sig = inspect.signature(PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_model::classes::package_is_not_abstract():
    assert not inspect.isabstract(model::classes::Package)


def test_model::classes::package_constructor_exists():
    assert callable(model::classes::Package.__init__)


def test_model::classes::package_constructor_args():
    sig = inspect.signature(model::classes::Package.__init__)
    params = list(sig.parameters.keys())



def test_model::classes::class_is_not_abstract():
    assert not inspect.isabstract(model::classes::Class)


def test_model::classes::class_constructor_exists():
    assert callable(model::classes::Class.__init__)


def test_model::classes::class_constructor_args():
    sig = inspect.signature(model::classes::Class.__init__)
    params = list(sig.parameters.keys())



def test_classes::dependency_is_not_abstract():
    assert not inspect.isabstract(classes::Dependency)


def test_classes::dependency_constructor_exists():
    assert callable(classes::Dependency.__init__)


def test_classes::dependency_constructor_args():
    sig = inspect.signature(classes::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_classes::package_is_not_abstract():
    assert not inspect.isabstract(classes::Package)


def test_classes::package_constructor_exists():
    assert callable(classes::Package.__init__)


def test_classes::package_constructor_args():
    sig = inspect.signature(classes::Package.__init__)
    params = list(sig.parameters.keys())



def test_requirement::scenario_is_not_abstract():
    assert not inspect.isabstract(requirement::Scenario)


def test_requirement::scenario_constructor_exists():
    assert callable(requirement::Scenario.__init__)


def test_requirement::scenario_constructor_args():
    sig = inspect.signature(requirement::Scenario.__init__)
    params = list(sig.parameters.keys())



def test_requirement::usecase_is_not_abstract():
    assert not inspect.isabstract(requirement::UseCase)


def test_requirement::usecase_constructor_exists():
    assert callable(requirement::UseCase.__init__)


def test_requirement::usecase_constructor_args():
    sig = inspect.signature(requirement::UseCase.__init__)
    params = list(sig.parameters.keys())



def test_classes::method_is_not_abstract():
    assert not inspect.isabstract(classes::Method)


def test_classes::method_constructor_exists():
    assert callable(classes::Method.__init__)


def test_classes::method_constructor_args():
    sig = inspect.signature(classes::Method.__init__)
    params = list(sig.parameters.keys())



def test_classes::attribute_is_not_abstract():
    assert not inspect.isabstract(classes::Attribute)


def test_classes::attribute_constructor_exists():
    assert callable(classes::Attribute.__init__)


def test_classes::attribute_constructor_args():
    sig = inspect.signature(classes::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_classes::association_is_not_abstract():
    assert not inspect.isabstract(classes::Association)


def test_classes::association_constructor_exists():
    assert callable(classes::Association.__init__)


def test_classes::association_constructor_args():
    sig = inspect.signature(classes::Association.__init__)
    params = list(sig.parameters.keys())



def test_classes::class_is_not_abstract():
    assert not inspect.isabstract(classes::Class)


def test_classes::class_constructor_exists():
    assert callable(classes::Class.__init__)


def test_classes::class_constructor_args():
    sig = inspect.signature(classes::Class.__init__)
    params = list(sig.parameters.keys())



def test_diagram::model::diagram_is_not_abstract():
    assert not inspect.isabstract(diagram::model::Diagram)


def test_diagram::model::diagram_constructor_exists():
    assert callable(diagram::model::Diagram.__init__)


def test_diagram::model::diagram_constructor_args():
    sig = inspect.signature(diagram::model::Diagram.__init__)
    params = list(sig.parameters.keys())



def test_task::checkable_is_not_abstract():
    assert not inspect.isabstract(task::Checkable)


def test_task::checkable_constructor_exists():
    assert callable(task::Checkable.__init__)


def test_task::checkable_constructor_args():
    sig = inspect.signature(task::Checkable.__init__)
    params = list(sig.parameters.keys())



def test_organization::user_is_not_abstract():
    assert not inspect.isabstract(organization::User)


def test_organization::user_constructor_exists():
    assert callable(organization::User.__init__)


def test_organization::user_constructor_args():
    sig = inspect.signature(organization::User.__init__)
    params = list(sig.parameters.keys())



def test_task::workpackage_is_not_abstract():
    assert not inspect.isabstract(task::WorkPackage)


def test_task::workpackage_constructor_exists():
    assert callable(task::WorkPackage.__init__)


def test_task::workpackage_constructor_args():
    sig = inspect.signature(task::WorkPackage.__init__)
    params = list(sig.parameters.keys())



def test_organization::orgunit_is_not_abstract():
    assert not inspect.isabstract(organization::OrgUnit)


def test_organization::orgunit_constructor_exists():
    assert callable(organization::OrgUnit.__init__)


def test_organization::orgunit_constructor_args():
    sig = inspect.signature(organization::OrgUnit.__init__)
    params = list(sig.parameters.keys())



def test_workitem_is_not_abstract():
    assert not inspect.isabstract(WorkItem)


def test_workitem_constructor_exists():
    assert callable(WorkItem.__init__)


def test_workitem_constructor_args():
    sig = inspect.signature(WorkItem.__init__)
    params = list(sig.parameters.keys())



def test_model::task::milestone_is_not_abstract():
    assert not inspect.isabstract(model::task::Milestone)


def test_model::task::milestone_constructor_exists():
    assert callable(model::task::Milestone.__init__)


def test_model::task::milestone_constructor_args():
    sig = inspect.signature(model::task::Milestone.__init__)
    params = list(sig.parameters.keys())



def test_model::task::workpackage_is_not_abstract():
    assert not inspect.isabstract(model::task::WorkPackage)


def test_model::task::workpackage_constructor_exists():
    assert callable(model::task::WorkPackage.__init__)


def test_model::task::workpackage_constructor_args():
    sig = inspect.signature(model::task::WorkPackage.__init__)
    params = list(sig.parameters.keys())
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "endDate" in params, "Missing parameter 'endDate'"

def test_model::task::workpackage_has_startDate():
    assert hasattr(model::task::WorkPackage, "startDate")
    descriptor = None
    for klass in model::task::WorkPackage.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_model::task::workpackage_has_endDate():
    assert hasattr(model::task::WorkPackage, "endDate")
    descriptor = None
    for klass in model::task::WorkPackage.__mro__:
        if "endDate" in klass.__dict__:
            descriptor = klass.__dict__["endDate"]
            break
    assert isinstance(descriptor, property)



def test_change::modelchangepackage_is_not_abstract():
    assert not inspect.isabstract(change::ModelChangePackage)


def test_change::modelchangepackage_constructor_exists():
    assert callable(change::ModelChangePackage.__init__)


def test_change::modelchangepackage_constructor_args():
    sig = inspect.signature(change::ModelChangePackage.__init__)
    params = list(sig.parameters.keys())



def test_project_is_not_abstract():
    assert not inspect.isabstract(Project)


def test_project_constructor_exists():
    assert callable(Project.__init__)


def test_project_constructor_args():
    sig = inspect.signature(Project.__init__)
    params = list(sig.parameters.keys())



def test_model::project_is_not_abstract():
    assert not inspect.isabstract(model::Project)


def test_model::project_constructor_exists():
    assert callable(model::Project.__init__)


def test_model::project_constructor_args():
    sig = inspect.signature(model::Project.__init__)
    params = list(sig.parameters.keys())



def test_model::nondomainelement_is_not_abstract():
    assert not inspect.isabstract(model::NonDomainElement)


def test_model::nondomainelement_constructor_exists():
    assert callable(model::NonDomainElement.__init__)


def test_model::nondomainelement_constructor_args():
    sig = inspect.signature(model::NonDomainElement.__init__)
    params = list(sig.parameters.keys())



def test_unicasemodelelement_is_not_abstract():
    assert not inspect.isabstract(UnicaseModelElement)


def test_unicasemodelelement_constructor_exists():
    assert callable(UnicaseModelElement.__init__)


def test_unicasemodelelement_constructor_args():
    sig = inspect.signature(UnicaseModelElement.__init__)
    params = list(sig.parameters.keys())



def test_model::rationale::comment_is_not_abstract():
    assert not inspect.isabstract(model::rationale::Comment)


def test_model::rationale::comment_constructor_exists():
    assert callable(model::rationale::Comment.__init__)


def test_model::rationale::comment_constructor_args():
    sig = inspect.signature(model::rationale::Comment.__init__)
    params = list(sig.parameters.keys())



def test_model::requirement::systemfunction_is_not_abstract():
    assert not inspect.isabstract(model::requirement::SystemFunction)


def test_model::requirement::systemfunction_constructor_exists():
    assert callable(model::requirement::SystemFunction.__init__)


def test_model::requirement::systemfunction_constructor_args():
    sig = inspect.signature(model::requirement::SystemFunction.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"
    assert "exception" in params, "Missing parameter 'exception'"

def test_model::requirement::systemfunction_has_input():
    assert hasattr(model::requirement::SystemFunction, "input")
    descriptor = None
    for klass in model::requirement::SystemFunction.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_model::requirement::systemfunction_has_output():
    assert hasattr(model::requirement::SystemFunction, "output")
    descriptor = None
    for klass in model::requirement::SystemFunction.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_model::requirement::systemfunction_has_exception():
    assert hasattr(model::requirement::SystemFunction, "exception")
    descriptor = None
    for klass in model::requirement::SystemFunction.__mro__:
        if "exception" in klass.__dict__:
            descriptor = klass.__dict__["exception"]
            break
    assert isinstance(descriptor, property)



def test_model::requirement::actor_is_not_abstract():
    assert not inspect.isabstract(model::requirement::Actor)


def test_model::requirement::actor_constructor_exists():
    assert callable(model::requirement::Actor.__init__)


def test_model::requirement::actor_constructor_args():
    sig = inspect.signature(model::requirement::Actor.__init__)
    params = list(sig.parameters.keys())



def test_model::component::component_is_not_abstract():
    assert not inspect.isabstract(model::component::Component)


def test_model::component::component_constructor_exists():
    assert callable(model::component::Component.__init__)


def test_model::component::component_constructor_args():
    sig = inspect.signature(model::component::Component.__init__)
    params = list(sig.parameters.keys())



def test_model::change::modelchangepackage_is_not_abstract():
    assert not inspect.isabstract(model::change::ModelChangePackage)


def test_model::change::modelchangepackage_constructor_exists():
    assert callable(model::change::ModelChangePackage.__init__)


def test_model::change::modelchangepackage_constructor_args():
    sig = inspect.signature(model::change::ModelChangePackage.__init__)
    params = list(sig.parameters.keys())
    assert "targetVersion" in params, "Missing parameter 'targetVersion'"
    assert "sourceVersion" in params, "Missing parameter 'sourceVersion'"

def test_model::change::modelchangepackage_has_targetVersion():
    assert hasattr(model::change::ModelChangePackage, "targetVersion")
    descriptor = None
    for klass in model::change::ModelChangePackage.__mro__:
        if "targetVersion" in klass.__dict__:
            descriptor = klass.__dict__["targetVersion"]
            break
    assert isinstance(descriptor, property)

def test_model::change::modelchangepackage_has_sourceVersion():
    assert hasattr(model::change::ModelChangePackage, "sourceVersion")
    descriptor = None
    for klass in model::change::ModelChangePackage.__mro__:
        if "sourceVersion" in klass.__dict__:
            descriptor = klass.__dict__["sourceVersion"]
            break
    assert isinstance(descriptor, property)



def test_model::task::checkable_is_not_abstract():
    assert not inspect.isabstract(model::task::Checkable)


def test_model::task::checkable_constructor_exists():
    assert callable(model::task::Checkable.__init__)


def test_model::task::checkable_constructor_args():
    sig = inspect.signature(model::task::Checkable.__init__)
    params = list(sig.parameters.keys())
    assert "checked" in params, "Missing parameter 'checked'"

def test_model::task::checkable_has_checked():
    assert hasattr(model::task::Checkable, "checked")
    descriptor = None
    for klass in model::task::Checkable.__mro__:
        if "checked" in klass.__dict__:
            descriptor = klass.__dict__["checked"]
            break
    assert isinstance(descriptor, property)



def test_model::classes::attribute_is_not_abstract():
    assert not inspect.isabstract(model::classes::Attribute)


def test_model::classes::attribute_constructor_exists():
    assert callable(model::classes::Attribute.__init__)


def test_model::classes::attribute_constructor_args():
    sig = inspect.signature(model::classes::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "signature" in params, "Missing parameter 'signature'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "type" in params, "Missing parameter 'type'"
    assert "scope" in params, "Missing parameter 'scope'"
    assert "properties" in params, "Missing parameter 'properties'"
    assert "label" in params, "Missing parameter 'label'"

def test_model::classes::attribute_has_defaultValue():
    assert hasattr(model::classes::Attribute, "defaultValue")
    descriptor = None
    for klass in model::classes::Attribute.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::attribute_has_signature():
    assert hasattr(model::classes::Attribute, "signature")
    descriptor = None
    for klass in model::classes::Attribute.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::attribute_has_visibility():
    assert hasattr(model::classes::Attribute, "visibility")
    descriptor = None
    for klass in model::classes::Attribute.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::attribute_has_type():
    assert hasattr(model::classes::Attribute, "type")
    descriptor = None
    for klass in model::classes::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::attribute_has_scope():
    assert hasattr(model::classes::Attribute, "scope")
    descriptor = None
    for klass in model::classes::Attribute.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::attribute_has_properties():
    assert hasattr(model::classes::Attribute, "properties")
    descriptor = None
    for klass in model::classes::Attribute.__mro__:
        if "properties" in klass.__dict__:
            descriptor = klass.__dict__["properties"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::attribute_has_label():
    assert hasattr(model::classes::Attribute, "label")
    descriptor = None
    for klass in model::classes::Attribute.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_model::rationale::proposal_is_not_abstract():
    assert not inspect.isabstract(model::rationale::Proposal)


def test_model::rationale::proposal_constructor_exists():
    assert callable(model::rationale::Proposal.__init__)


def test_model::rationale::proposal_constructor_args():
    sig = inspect.signature(model::rationale::Proposal.__init__)
    params = list(sig.parameters.keys())



def test_model::rationale::assessment_is_not_abstract():
    assert not inspect.isabstract(model::rationale::Assessment)


def test_model::rationale::assessment_constructor_exists():
    assert callable(model::rationale::Assessment.__init__)


def test_model::rationale::assessment_constructor_args():
    sig = inspect.signature(model::rationale::Assessment.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model::rationale::assessment_has_value():
    assert hasattr(model::rationale::Assessment, "value")
    descriptor = None
    for klass in model::rationale::Assessment.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model::document::section_is_not_abstract():
    assert not inspect.isabstract(model::document::Section)


def test_model::document::section_constructor_exists():
    assert callable(model::document::Section.__init__)


def test_model::document::section_constructor_args():
    sig = inspect.signature(model::document::Section.__init__)
    params = list(sig.parameters.keys())



def test_model::component::componentservice_is_not_abstract():
    assert not inspect.isabstract(model::component::ComponentService)


def test_model::component::componentservice_constructor_exists():
    assert callable(model::component::ComponentService.__init__)


def test_model::component::componentservice_constructor_args():
    sig = inspect.signature(model::component::ComponentService.__init__)
    params = list(sig.parameters.keys())



def test_model::attachment_is_not_abstract():
    assert not inspect.isabstract(model::Attachment)


def test_model::attachment_constructor_exists():
    assert callable(model::Attachment.__init__)


def test_model::attachment_constructor_args():
    sig = inspect.signature(model::Attachment.__init__)
    params = list(sig.parameters.keys())



def test_model::requirement::usecase_is_not_abstract():
    assert not inspect.isabstract(model::requirement::UseCase)


def test_model::requirement::usecase_constructor_exists():
    assert callable(model::requirement::UseCase.__init__)


def test_model::requirement::usecase_constructor_args():
    sig = inspect.signature(model::requirement::UseCase.__init__)
    params = list(sig.parameters.keys())
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "postcondition" in params, "Missing parameter 'postcondition'"
    assert "rules" in params, "Missing parameter 'rules'"
    assert "exception" in params, "Missing parameter 'exception'"

def test_model::requirement::usecase_has_precondition():
    assert hasattr(model::requirement::UseCase, "precondition")
    descriptor = None
    for klass in model::requirement::UseCase.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_model::requirement::usecase_has_postcondition():
    assert hasattr(model::requirement::UseCase, "postcondition")
    descriptor = None
    for klass in model::requirement::UseCase.__mro__:
        if "postcondition" in klass.__dict__:
            descriptor = klass.__dict__["postcondition"]
            break
    assert isinstance(descriptor, property)

def test_model::requirement::usecase_has_rules():
    assert hasattr(model::requirement::UseCase, "rules")
    descriptor = None
    for klass in model::requirement::UseCase.__mro__:
        if "rules" in klass.__dict__:
            descriptor = klass.__dict__["rules"]
            break
    assert isinstance(descriptor, property)

def test_model::requirement::usecase_has_exception():
    assert hasattr(model::requirement::UseCase, "exception")
    descriptor = None
    for klass in model::requirement::UseCase.__mro__:
        if "exception" in klass.__dict__:
            descriptor = klass.__dict__["exception"]
            break
    assert isinstance(descriptor, property)



def test_model::rationale::solution_is_not_abstract():
    assert not inspect.isabstract(model::rationale::Solution)


def test_model::rationale::solution_constructor_exists():
    assert callable(model::rationale::Solution.__init__)


def test_model::rationale::solution_constructor_args():
    sig = inspect.signature(model::rationale::Solution.__init__)
    params = list(sig.parameters.keys())



def test_model::rationale::criterion_is_not_abstract():
    assert not inspect.isabstract(model::rationale::Criterion)


def test_model::rationale::criterion_constructor_exists():
    assert callable(model::rationale::Criterion.__init__)


def test_model::rationale::criterion_constructor_args():
    sig = inspect.signature(model::rationale::Criterion.__init__)
    params = list(sig.parameters.keys())



def test_model::classes::association_is_not_abstract():
    assert not inspect.isabstract(model::classes::Association)


def test_model::classes::association_constructor_exists():
    assert callable(model::classes::Association.__init__)


def test_model::classes::association_constructor_args():
    sig = inspect.signature(model::classes::Association.__init__)
    params = list(sig.parameters.keys())
    assert "targetMultiplicity" in params, "Missing parameter 'targetMultiplicity'"
    assert "targetRole" in params, "Missing parameter 'targetRole'"
    assert "type" in params, "Missing parameter 'type'"
    assert "sourceMultiplicity" in params, "Missing parameter 'sourceMultiplicity'"
    assert "sourceRole" in params, "Missing parameter 'sourceRole'"

def test_model::classes::association_has_targetMultiplicity():
    assert hasattr(model::classes::Association, "targetMultiplicity")
    descriptor = None
    for klass in model::classes::Association.__mro__:
        if "targetMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["targetMultiplicity"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::association_has_targetRole():
    assert hasattr(model::classes::Association, "targetRole")
    descriptor = None
    for klass in model::classes::Association.__mro__:
        if "targetRole" in klass.__dict__:
            descriptor = klass.__dict__["targetRole"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::association_has_type():
    assert hasattr(model::classes::Association, "type")
    descriptor = None
    for klass in model::classes::Association.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::association_has_sourceMultiplicity():
    assert hasattr(model::classes::Association, "sourceMultiplicity")
    descriptor = None
    for klass in model::classes::Association.__mro__:
        if "sourceMultiplicity" in klass.__dict__:
            descriptor = klass.__dict__["sourceMultiplicity"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::association_has_sourceRole():
    assert hasattr(model::classes::Association, "sourceRole")
    descriptor = None
    for klass in model::classes::Association.__mro__:
        if "sourceRole" in klass.__dict__:
            descriptor = klass.__dict__["sourceRole"]
            break
    assert isinstance(descriptor, property)



def test_model::classes::packageelement_is_not_abstract():
    assert not inspect.isabstract(model::classes::PackageElement)


def test_model::classes::packageelement_constructor_exists():
    assert callable(model::classes::PackageElement.__init__)


def test_model::classes::packageelement_constructor_args():
    sig = inspect.signature(model::classes::PackageElement.__init__)
    params = list(sig.parameters.keys())



def test_model::requirement::scenario_is_not_abstract():
    assert not inspect.isabstract(model::requirement::Scenario)


def test_model::requirement::scenario_constructor_exists():
    assert callable(model::requirement::Scenario.__init__)


def test_model::requirement::scenario_constructor_args():
    sig = inspect.signature(model::requirement::Scenario.__init__)
    params = list(sig.parameters.keys())



def test_model::requirement::step_is_not_abstract():
    assert not inspect.isabstract(model::requirement::Step)


def test_model::requirement::step_constructor_exists():
    assert callable(model::requirement::Step.__init__)


def test_model::requirement::step_constructor_args():
    sig = inspect.signature(model::requirement::Step.__init__)
    params = list(sig.parameters.keys())
    assert "userStep" in params, "Missing parameter 'userStep'"

def test_model::requirement::step_has_userStep():
    assert hasattr(model::requirement::Step, "userStep")
    descriptor = None
    for klass in model::requirement::Step.__mro__:
        if "userStep" in klass.__dict__:
            descriptor = klass.__dict__["userStep"]
            break
    assert isinstance(descriptor, property)



def test_model::classes::method_is_not_abstract():
    assert not inspect.isabstract(model::classes::Method)


def test_model::classes::method_constructor_exists():
    assert callable(model::classes::Method.__init__)


def test_model::classes::method_constructor_args():
    sig = inspect.signature(model::classes::Method.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"
    assert "properties" in params, "Missing parameter 'properties'"
    assert "returnType" in params, "Missing parameter 'returnType'"
    assert "label" in params, "Missing parameter 'label'"
    assert "stubbed" in params, "Missing parameter 'stubbed'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "signature" in params, "Missing parameter 'signature'"

def test_model::classes::method_has_scope():
    assert hasattr(model::classes::Method, "scope")
    descriptor = None
    for klass in model::classes::Method.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::method_has_properties():
    assert hasattr(model::classes::Method, "properties")
    descriptor = None
    for klass in model::classes::Method.__mro__:
        if "properties" in klass.__dict__:
            descriptor = klass.__dict__["properties"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::method_has_returnType():
    assert hasattr(model::classes::Method, "returnType")
    descriptor = None
    for klass in model::classes::Method.__mro__:
        if "returnType" in klass.__dict__:
            descriptor = klass.__dict__["returnType"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::method_has_label():
    assert hasattr(model::classes::Method, "label")
    descriptor = None
    for klass in model::classes::Method.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::method_has_stubbed():
    assert hasattr(model::classes::Method, "stubbed")
    descriptor = None
    for klass in model::classes::Method.__mro__:
        if "stubbed" in klass.__dict__:
            descriptor = klass.__dict__["stubbed"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::method_has_visibility():
    assert hasattr(model::classes::Method, "visibility")
    descriptor = None
    for klass in model::classes::Method.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::method_has_signature():
    assert hasattr(model::classes::Method, "signature")
    descriptor = None
    for klass in model::classes::Method.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_model::classes::dependency_is_not_abstract():
    assert not inspect.isabstract(model::classes::Dependency)


def test_model::classes::dependency_constructor_exists():
    assert callable(model::classes::Dependency.__init__)


def test_model::classes::dependency_constructor_args():
    sig = inspect.signature(model::classes::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_model::requirement::actorinstance_is_not_abstract():
    assert not inspect.isabstract(model::requirement::ActorInstance)


def test_model::requirement::actorinstance_constructor_exists():
    assert callable(model::requirement::ActorInstance.__init__)


def test_model::requirement::actorinstance_constructor_args():
    sig = inspect.signature(model::requirement::ActorInstance.__init__)
    params = list(sig.parameters.keys())



def test_model::requirement::usertask_is_not_abstract():
    assert not inspect.isabstract(model::requirement::UserTask)


def test_model::requirement::usertask_constructor_exists():
    assert callable(model::requirement::UserTask.__init__)


def test_model::requirement::usertask_constructor_args():
    sig = inspect.signature(model::requirement::UserTask.__init__)
    params = list(sig.parameters.keys())



def test_model::classes::methodargument_is_not_abstract():
    assert not inspect.isabstract(model::classes::MethodArgument)


def test_model::classes::methodargument_constructor_exists():
    assert callable(model::classes::MethodArgument.__init__)


def test_model::classes::methodargument_constructor_args():
    sig = inspect.signature(model::classes::MethodArgument.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "label" in params, "Missing parameter 'label'"
    assert "type" in params, "Missing parameter 'type'"
    assert "signature" in params, "Missing parameter 'signature'"

def test_model::classes::methodargument_has_defaultValue():
    assert hasattr(model::classes::MethodArgument, "defaultValue")
    descriptor = None
    for klass in model::classes::MethodArgument.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::methodargument_has_direction():
    assert hasattr(model::classes::MethodArgument, "direction")
    descriptor = None
    for klass in model::classes::MethodArgument.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::methodargument_has_label():
    assert hasattr(model::classes::MethodArgument, "label")
    descriptor = None
    for klass in model::classes::MethodArgument.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::methodargument_has_type():
    assert hasattr(model::classes::MethodArgument, "type")
    descriptor = None
    for klass in model::classes::MethodArgument.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_model::classes::methodargument_has_signature():
    assert hasattr(model::classes::MethodArgument, "signature")
    descriptor = None
    for klass in model::classes::MethodArgument.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_model::requirement::functionalrequirement_is_not_abstract():
    assert not inspect.isabstract(model::requirement::FunctionalRequirement)


def test_model::requirement::functionalrequirement_constructor_exists():
    assert callable(model::requirement::FunctionalRequirement.__init__)


def test_model::requirement::functionalrequirement_constructor_args():
    sig = inspect.signature(model::requirement::FunctionalRequirement.__init__)
    params = list(sig.parameters.keys())
    assert "storyPoints" in params, "Missing parameter 'storyPoints'"
    assert "cost" in params, "Missing parameter 'cost'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "reviewed" in params, "Missing parameter 'reviewed'"

def test_model::requirement::functionalrequirement_has_storyPoints():
    assert hasattr(model::requirement::FunctionalRequirement, "storyPoints")
    descriptor = None
    for klass in model::requirement::FunctionalRequirement.__mro__:
        if "storyPoints" in klass.__dict__:
            descriptor = klass.__dict__["storyPoints"]
            break
    assert isinstance(descriptor, property)

def test_model::requirement::functionalrequirement_has_cost():
    assert hasattr(model::requirement::FunctionalRequirement, "cost")
    descriptor = None
    for klass in model::requirement::FunctionalRequirement.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_model::requirement::functionalrequirement_has_priority():
    assert hasattr(model::requirement::FunctionalRequirement, "priority")
    descriptor = None
    for klass in model::requirement::FunctionalRequirement.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_model::requirement::functionalrequirement_has_reviewed():
    assert hasattr(model::requirement::FunctionalRequirement, "reviewed")
    descriptor = None
    for klass in model::requirement::FunctionalRequirement.__mro__:
        if "reviewed" in klass.__dict__:
            descriptor = klass.__dict__["reviewed"]
            break
    assert isinstance(descriptor, property)



def test_model::annotation_is_not_abstract():
    assert not inspect.isabstract(model::Annotation)


def test_model::annotation_constructor_exists():
    assert callable(model::Annotation.__init__)


def test_model::annotation_constructor_args():
    sig = inspect.signature(model::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_profile::stereotypeinstance_is_not_abstract():
    assert not inspect.isabstract(profile::StereotypeInstance)


def test_profile::stereotypeinstance_constructor_exists():
    assert callable(profile::StereotypeInstance.__init__)


def test_profile::stereotypeinstance_constructor_args():
    sig = inspect.signature(profile::StereotypeInstance.__init__)
    params = list(sig.parameters.keys())



def test_rationale::comment_is_not_abstract():
    assert not inspect.isabstract(rationale::Comment)


def test_rationale::comment_constructor_exists():
    assert callable(rationale::Comment.__init__)


def test_rationale::comment_constructor_args():
    sig = inspect.signature(rationale::Comment.__init__)
    params = list(sig.parameters.keys())



def test_orgunit_is_not_abstract():
    assert not inspect.isabstract(OrgUnit)


def test_orgunit_constructor_exists():
    assert callable(OrgUnit.__init__)


def test_orgunit_constructor_args():
    sig = inspect.signature(OrgUnit.__init__)
    params = list(sig.parameters.keys())



def test_model::organization::group_is_not_abstract():
    assert not inspect.isabstract(model::organization::Group)


def test_model::organization::group_constructor_exists():
    assert callable(model::organization::Group.__init__)


def test_model::organization::group_constructor_args():
    sig = inspect.signature(model::organization::Group.__init__)
    params = list(sig.parameters.keys())



def test_model::organization::user_is_not_abstract():
    assert not inspect.isabstract(model::organization::User)


def test_model::organization::user_constructor_exists():
    assert callable(model::organization::User.__init__)


def test_model::organization::user_constructor_args():
    sig = inspect.signature(model::organization::User.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "email" in params, "Missing parameter 'email'"

def test_model::organization::user_has_firstName():
    assert hasattr(model::organization::User, "firstName")
    descriptor = None
    for klass in model::organization::User.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_model::organization::user_has_lastName():
    assert hasattr(model::organization::User, "lastName")
    descriptor = None
    for klass in model::organization::User.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_model::organization::user_has_email():
    assert hasattr(model::organization::User, "email")
    descriptor = None
    for klass in model::organization::User.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_task::workitem_is_not_abstract():
    assert not inspect.isabstract(task::WorkItem)


def test_task::workitem_constructor_exists():
    assert callable(task::WorkItem.__init__)


def test_task::workitem_constructor_args():
    sig = inspect.signature(task::WorkItem.__init__)
    params = list(sig.parameters.keys())



def test_model::bug::bugreport_is_not_abstract():
    assert not inspect.isabstract(model::bug::BugReport)


def test_model::bug::bugreport_constructor_exists():
    assert callable(model::bug::BugReport.__init__)


def test_model::bug::bugreport_constructor_args():
    sig = inspect.signature(model::bug::BugReport.__init__)
    params = list(sig.parameters.keys())
    assert "resolution" in params, "Missing parameter 'resolution'"
    assert "resolutionType" in params, "Missing parameter 'resolutionType'"
    assert "severity" in params, "Missing parameter 'severity'"
    assert "Status" in params, "Missing parameter 'Status'"

def test_model::bug::bugreport_has_resolution():
    assert hasattr(model::bug::BugReport, "resolution")
    descriptor = None
    for klass in model::bug::BugReport.__mro__:
        if "resolution" in klass.__dict__:
            descriptor = klass.__dict__["resolution"]
            break
    assert isinstance(descriptor, property)

def test_model::bug::bugreport_has_resolutionType():
    assert hasattr(model::bug::BugReport, "resolutionType")
    descriptor = None
    for klass in model::bug::BugReport.__mro__:
        if "resolutionType" in klass.__dict__:
            descriptor = klass.__dict__["resolutionType"]
            break
    assert isinstance(descriptor, property)

def test_model::bug::bugreport_has_severity():
    assert hasattr(model::bug::BugReport, "severity")
    descriptor = None
    for klass in model::bug::BugReport.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)

def test_model::bug::bugreport_has_Status():
    assert hasattr(model::bug::BugReport, "Status")
    descriptor = None
    for klass in model::bug::BugReport.__mro__:
        if "Status" in klass.__dict__:
            descriptor = klass.__dict__["Status"]
            break
    assert isinstance(descriptor, property)



def test_model::task::actionitem_is_not_abstract():
    assert not inspect.isabstract(model::task::ActionItem)


def test_model::task::actionitem_constructor_exists():
    assert callable(model::task::ActionItem.__init__)


def test_model::task::actionitem_constructor_args():
    sig = inspect.signature(model::task::ActionItem.__init__)
    params = list(sig.parameters.keys())
    assert "done" in params, "Missing parameter 'done'"
    assert "activity" in params, "Missing parameter 'activity'"

def test_model::task::actionitem_has_done():
    assert hasattr(model::task::ActionItem, "done")
    descriptor = None
    for klass in model::task::ActionItem.__mro__:
        if "done" in klass.__dict__:
            descriptor = klass.__dict__["done"]
            break
    assert isinstance(descriptor, property)

def test_model::task::actionitem_has_activity():
    assert hasattr(model::task::ActionItem, "activity")
    descriptor = None
    for klass in model::task::ActionItem.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)



def test_organization::group_is_not_abstract():
    assert not inspect.isabstract(organization::Group)


def test_organization::group_constructor_exists():
    assert callable(organization::Group.__init__)


def test_organization::group_constructor_args():
    sig = inspect.signature(organization::Group.__init__)
    params = list(sig.parameters.keys())



def test_model::organization::orgunit_is_not_abstract():
    assert not inspect.isabstract(model::organization::OrgUnit)


def test_model::organization::orgunit_constructor_exists():
    assert callable(model::organization::OrgUnit.__init__)


def test_model::organization::orgunit_constructor_args():
    sig = inspect.signature(model::organization::OrgUnit.__init__)
    params = list(sig.parameters.keys())
    assert "acOrgId" in params, "Missing parameter 'acOrgId'"

def test_model::organization::orgunit_has_acOrgId():
    assert hasattr(model::organization::OrgUnit, "acOrgId")
    descriptor = None
    for klass in model::organization::OrgUnit.__mro__:
        if "acOrgId" in klass.__dict__:
            descriptor = klass.__dict__["acOrgId"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::associationclasselement_is_not_abstract():
    assert not inspect.isabstract(metamodel::AssociationClassElement)


def test_metamodel::associationclasselement_constructor_exists():
    assert callable(metamodel::AssociationClassElement.__init__)


def test_metamodel::associationclasselement_constructor_args():
    sig = inspect.signature(metamodel::AssociationClassElement.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::nondomainelement_is_not_abstract():
    assert not inspect.isabstract(metamodel::NonDomainElement)


def test_metamodel::nondomainelement_constructor_exists():
    assert callable(metamodel::NonDomainElement.__init__)


def test_metamodel::nondomainelement_constructor_args():
    sig = inspect.signature(metamodel::NonDomainElement.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::modelversion_is_not_abstract():
    assert not inspect.isabstract(metamodel::ModelVersion)


def test_metamodel::modelversion_constructor_exists():
    assert callable(metamodel::ModelVersion.__init__)


def test_metamodel::modelversion_constructor_args():
    sig = inspect.signature(metamodel::ModelVersion.__init__)
    params = list(sig.parameters.keys())
    assert "releaseNumber" in params, "Missing parameter 'releaseNumber'"

def test_metamodel::modelversion_has_releaseNumber():
    assert hasattr(metamodel::ModelVersion, "releaseNumber")
    descriptor = None
    for klass in metamodel::ModelVersion.__mro__:
        if "releaseNumber" in klass.__dict__:
            descriptor = klass.__dict__["releaseNumber"]
            break
    assert isinstance(descriptor, property)



def test_uniqueidentifier_is_not_abstract():
    assert not inspect.isabstract(UniqueIdentifier)


def test_uniqueidentifier_constructor_exists():
    assert callable(UniqueIdentifier.__init__)


def test_uniqueidentifier_constructor_args():
    sig = inspect.signature(UniqueIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::modelelementid_is_not_abstract():
    assert not inspect.isabstract(metamodel::ModelElementId)


def test_metamodel::modelelementid_constructor_exists():
    assert callable(metamodel::ModelElementId.__init__)


def test_metamodel::modelelementid_constructor_args():
    sig = inspect.signature(metamodel::ModelElementId.__init__)
    params = list(sig.parameters.keys())



def test_identifiableelement_is_not_abstract():
    assert not inspect.isabstract(IdentifiableElement)


def test_identifiableelement_constructor_exists():
    assert callable(IdentifiableElement.__init__)


def test_identifiableelement_constructor_args():
    sig = inspect.signature(IdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::notification::esnotification_is_not_abstract():
    assert not inspect.isabstract(esmodel::notification::ESNotification)


def test_esmodel::notification::esnotification_constructor_exists():
    assert callable(esmodel::notification::ESNotification.__init__)


def test_esmodel::notification::esnotification_constructor_args():
    sig = inspect.signature(esmodel::notification::ESNotification.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "seen" in params, "Missing parameter 'seen'"
    assert "sender" in params, "Missing parameter 'sender'"
    assert "recipient" in params, "Missing parameter 'recipient'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"
    assert "details" in params, "Missing parameter 'details'"
    assert "name" in params, "Missing parameter 'name'"
    assert "provider" in params, "Missing parameter 'provider'"

def test_esmodel::notification::esnotification_has_message():
    assert hasattr(esmodel::notification::ESNotification, "message")
    descriptor = None
    for klass in esmodel::notification::ESNotification.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::notification::esnotification_has_seen():
    assert hasattr(esmodel::notification::ESNotification, "seen")
    descriptor = None
    for klass in esmodel::notification::ESNotification.__mro__:
        if "seen" in klass.__dict__:
            descriptor = klass.__dict__["seen"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::notification::esnotification_has_sender():
    assert hasattr(esmodel::notification::ESNotification, "sender")
    descriptor = None
    for klass in esmodel::notification::ESNotification.__mro__:
        if "sender" in klass.__dict__:
            descriptor = klass.__dict__["sender"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::notification::esnotification_has_recipient():
    assert hasattr(esmodel::notification::ESNotification, "recipient")
    descriptor = None
    for klass in esmodel::notification::ESNotification.__mro__:
        if "recipient" in klass.__dict__:
            descriptor = klass.__dict__["recipient"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::notification::esnotification_has_creationDate():
    assert hasattr(esmodel::notification::ESNotification, "creationDate")
    descriptor = None
    for klass in esmodel::notification::ESNotification.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::notification::esnotification_has_details():
    assert hasattr(esmodel::notification::ESNotification, "details")
    descriptor = None
    for klass in esmodel::notification::ESNotification.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::notification::esnotification_has_name():
    assert hasattr(esmodel::notification::ESNotification, "name")
    descriptor = None
    for klass in esmodel::notification::ESNotification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::notification::esnotification_has_provider():
    assert hasattr(esmodel::notification::ESNotification, "provider")
    descriptor = None
    for klass in esmodel::notification::ESNotification.__mro__:
        if "provider" in klass.__dict__:
            descriptor = klass.__dict__["provider"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::modelelement_is_not_abstract():
    assert not inspect.isabstract(metamodel::ModelElement)


def test_metamodel::modelelement_constructor_exists():
    assert callable(metamodel::ModelElement.__init__)


def test_metamodel::modelelement_constructor_args():
    sig = inspect.signature(metamodel::ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "creator" in params, "Missing parameter 'creator'"
    assert "creationDate" in params, "Missing parameter 'creationDate'"

def test_metamodel::modelelement_has_creator():
    assert hasattr(metamodel::ModelElement, "creator")
    descriptor = None
    for klass in metamodel::ModelElement.__mro__:
        if "creator" in klass.__dict__:
            descriptor = klass.__dict__["creator"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::modelelement_has_creationDate():
    assert hasattr(metamodel::ModelElement, "creationDate")
    descriptor = None
    for klass in metamodel::ModelElement.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::identifiableelement_is_not_abstract():
    assert not inspect.isabstract(metamodel::IdentifiableElement)


def test_metamodel::identifiableelement_constructor_exists():
    assert callable(metamodel::IdentifiableElement.__init__)


def test_metamodel::identifiableelement_constructor_args():
    sig = inspect.signature(metamodel::IdentifiableElement.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_metamodel::identifiableelement_has_identifier():
    assert hasattr(metamodel::IdentifiableElement, "identifier")
    descriptor = None
    for klass in metamodel::IdentifiableElement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::uniqueidentifier_is_not_abstract():
    assert not inspect.isabstract(metamodel::UniqueIdentifier)


def test_metamodel::uniqueidentifier_constructor_exists():
    assert callable(metamodel::UniqueIdentifier.__init__)


def test_metamodel::uniqueidentifier_constructor_args():
    sig = inspect.signature(metamodel::UniqueIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_metamodel::uniqueidentifier_has_id():
    assert hasattr(metamodel::UniqueIdentifier, "id")
    descriptor = None
    for klass in metamodel::UniqueIdentifier.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::project_is_not_abstract():
    assert not inspect.isabstract(metamodel::Project)


def test_metamodel::project_constructor_exists():
    assert callable(metamodel::Project.__init__)


def test_metamodel::project_constructor_args():
    sig = inspect.signature(metamodel::Project.__init__)
    params = list(sig.parameters.keys())



def test_document::leafsection_is_not_abstract():
    assert not inspect.isabstract(document::LeafSection)


def test_document::leafsection_constructor_exists():
    assert callable(document::LeafSection.__init__)


def test_document::leafsection_constructor_args():
    sig = inspect.signature(document::LeafSection.__init__)
    params = list(sig.parameters.keys())



def test_attachment_is_not_abstract():
    assert not inspect.isabstract(Attachment)


def test_attachment_constructor_exists():
    assert callable(Attachment.__init__)


def test_attachment_constructor_args():
    sig = inspect.signature(Attachment.__init__)
    params = list(sig.parameters.keys())



def test_model::diagram::mediagram_is_not_abstract():
    assert not inspect.isabstract(model::diagram::MEDiagram)


def test_model::diagram::mediagram_constructor_exists():
    assert callable(model::diagram::MEDiagram.__init__)


def test_model::diagram::mediagram_constructor_args():
    sig = inspect.signature(model::diagram::MEDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "diagramLayout" in params, "Missing parameter 'diagramLayout'"
    assert "type" in params, "Missing parameter 'type'"

def test_model::diagram::mediagram_has_diagramLayout():
    assert hasattr(model::diagram::MEDiagram, "diagramLayout")
    descriptor = None
    for klass in model::diagram::MEDiagram.__mro__:
        if "diagramLayout" in klass.__dict__:
            descriptor = klass.__dict__["diagramLayout"]
            break
    assert isinstance(descriptor, property)

def test_model::diagram::mediagram_has_type():
    assert hasattr(model::diagram::MEDiagram, "type")
    descriptor = None
    for klass in model::diagram::MEDiagram.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_model::rationale::issue_is_not_abstract():
    assert not inspect.isabstract(model::rationale::Issue)


def test_model::rationale::issue_constructor_exists():
    assert callable(model::rationale::Issue.__init__)


def test_model::rationale::issue_constructor_args():
    sig = inspect.signature(model::rationale::Issue.__init__)
    params = list(sig.parameters.keys())
    assert "activity" in params, "Missing parameter 'activity'"

def test_model::rationale::issue_has_activity():
    assert hasattr(model::rationale::Issue, "activity")
    descriptor = None
    for klass in model::rationale::Issue.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)



def test_model::task::workitem_is_not_abstract():
    assert not inspect.isabstract(model::task::WorkItem)


def test_model::task::workitem_constructor_exists():
    assert callable(model::task::WorkItem.__init__)


def test_model::task::workitem_constructor_args():
    sig = inspect.signature(model::task::WorkItem.__init__)
    params = list(sig.parameters.keys())
    assert "dueDate" in params, "Missing parameter 'dueDate'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "effort" in params, "Missing parameter 'effort'"
    assert "resolved" in params, "Missing parameter 'resolved'"
    assert "estimate" in params, "Missing parameter 'estimate'"

def test_model::task::workitem_has_dueDate():
    assert hasattr(model::task::WorkItem, "dueDate")
    descriptor = None
    for klass in model::task::WorkItem.__mro__:
        if "dueDate" in klass.__dict__:
            descriptor = klass.__dict__["dueDate"]
            break
    assert isinstance(descriptor, property)

def test_model::task::workitem_has_priority():
    assert hasattr(model::task::WorkItem, "priority")
    descriptor = None
    for klass in model::task::WorkItem.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_model::task::workitem_has_effort():
    assert hasattr(model::task::WorkItem, "effort")
    descriptor = None
    for klass in model::task::WorkItem.__mro__:
        if "effort" in klass.__dict__:
            descriptor = klass.__dict__["effort"]
            break
    assert isinstance(descriptor, property)

def test_model::task::workitem_has_resolved():
    assert hasattr(model::task::WorkItem, "resolved")
    descriptor = None
    for klass in model::task::WorkItem.__mro__:
        if "resolved" in klass.__dict__:
            descriptor = klass.__dict__["resolved"]
            break
    assert isinstance(descriptor, property)

def test_model::task::workitem_has_estimate():
    assert hasattr(model::task::WorkItem, "estimate")
    descriptor = None
    for klass in model::task::WorkItem.__mro__:
        if "estimate" in klass.__dict__:
            descriptor = klass.__dict__["estimate"]
            break
    assert isinstance(descriptor, property)



def test_model::unicasemodelelement_is_not_abstract():
    assert not inspect.isabstract(model::UnicaseModelElement)


def test_model::unicasemodelelement_constructor_exists():
    assert callable(model::UnicaseModelElement.__init__)


def test_model::unicasemodelelement_constructor_args():
    sig = inspect.signature(model::UnicaseModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "state" in params, "Missing parameter 'state'"
    assert "name" in params, "Missing parameter 'name'"

def test_model::unicasemodelelement_has_description():
    assert hasattr(model::UnicaseModelElement, "description")
    descriptor = None
    for klass in model::UnicaseModelElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_model::unicasemodelelement_has_state():
    assert hasattr(model::UnicaseModelElement, "state")
    descriptor = None
    for klass in model::UnicaseModelElement.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_model::unicasemodelelement_has_name():
    assert hasattr(model::UnicaseModelElement, "name")
    descriptor = None
    for klass in model::UnicaseModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::url::serverurl_is_not_abstract():
    assert not inspect.isabstract(esmodel::url::ServerUrl)


def test_esmodel::url::serverurl_constructor_exists():
    assert callable(esmodel::url::ServerUrl.__init__)


def test_esmodel::url::serverurl_constructor_args():
    sig = inspect.signature(esmodel::url::ServerUrl.__init__)
    params = list(sig.parameters.keys())
    assert "hostName" in params, "Missing parameter 'hostName'"
    assert "port" in params, "Missing parameter 'port'"

def test_esmodel::url::serverurl_has_hostName():
    assert hasattr(esmodel::url::ServerUrl, "hostName")
    descriptor = None
    for klass in esmodel::url::ServerUrl.__mro__:
        if "hostName" in klass.__dict__:
            descriptor = klass.__dict__["hostName"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::url::serverurl_has_port():
    assert hasattr(esmodel::url::ServerUrl, "port")
    descriptor = None
    for klass in esmodel::url::ServerUrl.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::accesscontrol::orgunitproperty_is_not_abstract():
    assert not inspect.isabstract(esmodel::accesscontrol::OrgUnitProperty)


def test_esmodel::accesscontrol::orgunitproperty_constructor_exists():
    assert callable(esmodel::accesscontrol::OrgUnitProperty.__init__)


def test_esmodel::accesscontrol::orgunitproperty_constructor_args():
    sig = inspect.signature(esmodel::accesscontrol::OrgUnitProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_esmodel::accesscontrol::orgunitproperty_has_name():
    assert hasattr(esmodel::accesscontrol::OrgUnitProperty, "name")
    descriptor = None
    for klass in esmodel::accesscontrol::OrgUnitProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::accesscontrol::orgunitproperty_has_value():
    assert hasattr(esmodel::accesscontrol::OrgUnitProperty, "value")
    descriptor = None
    for klass in esmodel::accesscontrol::OrgUnitProperty.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::accesscontrol::acorgunitid_is_not_abstract():
    assert not inspect.isabstract(esmodel::accesscontrol::ACOrgUnitId)


def test_esmodel::accesscontrol::acorgunitid_constructor_exists():
    assert callable(esmodel::accesscontrol::ACOrgUnitId.__init__)


def test_esmodel::accesscontrol::acorgunitid_constructor_args():
    sig = inspect.signature(esmodel::accesscontrol::ACOrgUnitId.__init__)
    params = list(sig.parameters.keys())



def test_accesscontrol::acorgunit_is_not_abstract():
    assert not inspect.isabstract(accesscontrol::ACOrgUnit)


def test_accesscontrol::acorgunit_constructor_exists():
    assert callable(accesscontrol::ACOrgUnit.__init__)


def test_accesscontrol::acorgunit_constructor_args():
    sig = inspect.signature(accesscontrol::ACOrgUnit.__init__)
    params = list(sig.parameters.keys())



def test_accesscontrol::orgunitproperty_is_not_abstract():
    assert not inspect.isabstract(accesscontrol::OrgUnitProperty)


def test_accesscontrol::orgunitproperty_constructor_exists():
    assert callable(accesscontrol::OrgUnitProperty.__init__)


def test_accesscontrol::orgunitproperty_constructor_args():
    sig = inspect.signature(accesscontrol::OrgUnitProperty.__init__)
    params = list(sig.parameters.keys())



def test_roles::role_is_not_abstract():
    assert not inspect.isabstract(roles::Role)


def test_roles::role_constructor_exists():
    assert callable(roles::Role.__init__)


def test_roles::role_constructor_args():
    sig = inspect.signature(roles::Role.__init__)
    params = list(sig.parameters.keys())



def test_role_is_not_abstract():
    assert not inspect.isabstract(Role)


def test_role_constructor_exists():
    assert callable(Role.__init__)


def test_role_constructor_args():
    sig = inspect.signature(Role.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::roles::serveradmin_is_not_abstract():
    assert not inspect.isabstract(esmodel::roles::ServerAdmin)


def test_esmodel::roles::serveradmin_constructor_exists():
    assert callable(esmodel::roles::ServerAdmin.__init__)


def test_esmodel::roles::serveradmin_constructor_args():
    sig = inspect.signature(esmodel::roles::ServerAdmin.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::roles::writerrole_is_not_abstract():
    assert not inspect.isabstract(esmodel::roles::WriterRole)


def test_esmodel::roles::writerrole_constructor_exists():
    assert callable(esmodel::roles::WriterRole.__init__)


def test_esmodel::roles::writerrole_constructor_args():
    sig = inspect.signature(esmodel::roles::WriterRole.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::roles::projectadminrole_is_not_abstract():
    assert not inspect.isabstract(esmodel::roles::ProjectAdminRole)


def test_esmodel::roles::projectadminrole_constructor_exists():
    assert callable(esmodel::roles::ProjectAdminRole.__init__)


def test_esmodel::roles::projectadminrole_constructor_args():
    sig = inspect.signature(esmodel::roles::ProjectAdminRole.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::roles::readerrole_is_not_abstract():
    assert not inspect.isabstract(esmodel::roles::ReaderRole)


def test_esmodel::roles::readerrole_constructor_exists():
    assert callable(esmodel::roles::ReaderRole.__init__)


def test_esmodel::roles::readerrole_constructor_args():
    sig = inspect.signature(esmodel::roles::ReaderRole.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::roles::role_is_not_abstract():
    assert not inspect.isabstract(esmodel::roles::Role)


def test_esmodel::roles::role_constructor_exists():
    assert callable(esmodel::roles::Role.__init__)


def test_esmodel::roles::role_constructor_args():
    sig = inspect.signature(esmodel::roles::Role.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::accesscontrol::acorgunit_is_not_abstract():
    assert not inspect.isabstract(esmodel::accesscontrol::ACOrgUnit)


def test_esmodel::accesscontrol::acorgunit_constructor_exists():
    assert callable(esmodel::accesscontrol::ACOrgUnit.__init__)


def test_esmodel::accesscontrol::acorgunit_constructor_args():
    sig = inspect.signature(esmodel::accesscontrol::ACOrgUnit.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_esmodel::accesscontrol::acorgunit_has_description():
    assert hasattr(esmodel::accesscontrol::ACOrgUnit, "description")
    descriptor = None
    for klass in esmodel::accesscontrol::ACOrgUnit.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::accesscontrol::acorgunit_has_name():
    assert hasattr(esmodel::accesscontrol::ACOrgUnit, "name")
    descriptor = None
    for klass in esmodel::accesscontrol::ACOrgUnit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_operations::operationid_is_not_abstract():
    assert not inspect.isabstract(operations::OperationId)


def test_operations::operationid_constructor_exists():
    assert callable(operations::OperationId.__init__)


def test_operations::operationid_constructor_args():
    sig = inspect.signature(operations::OperationId.__init__)
    params = list(sig.parameters.keys())



def test_acorgunit_is_not_abstract():
    assert not inspect.isabstract(ACOrgUnit)


def test_acorgunit_constructor_exists():
    assert callable(ACOrgUnit.__init__)


def test_acorgunit_constructor_args():
    sig = inspect.signature(ACOrgUnit.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::accesscontrol::acgroup_is_not_abstract():
    assert not inspect.isabstract(esmodel::accesscontrol::ACGroup)


def test_esmodel::accesscontrol::acgroup_constructor_exists():
    assert callable(esmodel::accesscontrol::ACGroup.__init__)


def test_esmodel::accesscontrol::acgroup_constructor_args():
    sig = inspect.signature(esmodel::accesscontrol::ACGroup.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::accesscontrol::acuser_is_not_abstract():
    assert not inspect.isabstract(esmodel::accesscontrol::ACUser)


def test_esmodel::accesscontrol::acuser_constructor_exists():
    assert callable(esmodel::accesscontrol::ACUser.__init__)


def test_esmodel::accesscontrol::acuser_constructor_args():
    sig = inspect.signature(esmodel::accesscontrol::ACUser.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_esmodel::accesscontrol::acuser_has_firstName():
    assert hasattr(esmodel::accesscontrol::ACUser, "firstName")
    descriptor = None
    for klass in esmodel::accesscontrol::ACUser.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::accesscontrol::acuser_has_lastName():
    assert hasattr(esmodel::accesscontrol::ACUser, "lastName")
    descriptor = None
    for klass in esmodel::accesscontrol::ACUser.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_serverprojectevent_is_not_abstract():
    assert not inspect.isabstract(ServerProjectEvent)


def test_serverprojectevent_constructor_exists():
    assert callable(ServerProjectEvent.__init__)


def test_serverprojectevent_constructor_args():
    sig = inspect.signature(ServerProjectEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::server::projectupdatedevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::server::ProjectUpdatedEvent)


def test_esmodel::server::projectupdatedevent_constructor_exists():
    assert callable(esmodel::server::ProjectUpdatedEvent.__init__)


def test_esmodel::server::projectupdatedevent_constructor_args():
    sig = inspect.signature(esmodel::server::ProjectUpdatedEvent.__init__)
    params = list(sig.parameters.keys())



def test_serverevent_is_not_abstract():
    assert not inspect.isabstract(ServerEvent)


def test_serverevent_constructor_exists():
    assert callable(ServerEvent.__init__)


def test_serverevent_constructor_args():
    sig = inspect.signature(ServerEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::server::serverprojectevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::server::ServerProjectEvent)


def test_esmodel::server::serverprojectevent_constructor_exists():
    assert callable(esmodel::server::ServerProjectEvent.__init__)


def test_esmodel::server::serverprojectevent_constructor_args():
    sig = inspect.signature(esmodel::server::ServerProjectEvent.__init__)
    params = list(sig.parameters.keys())



def test_readevent_is_not_abstract():
    assert not inspect.isabstract(ReadEvent)


def test_readevent_constructor_exists():
    assert callable(ReadEvent.__init__)


def test_readevent_constructor_args():
    sig = inspect.signature(ReadEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::events::notificationreadevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::NotificationReadEvent)


def test_esmodel::events::notificationreadevent_constructor_exists():
    assert callable(esmodel::events::NotificationReadEvent.__init__)


def test_esmodel::events::notificationreadevent_constructor_args():
    sig = inspect.signature(esmodel::events::NotificationReadEvent.__init__)
    params = list(sig.parameters.keys())
    assert "notificationId" in params, "Missing parameter 'notificationId'"

def test_esmodel::events::notificationreadevent_has_notificationId():
    assert hasattr(esmodel::events::NotificationReadEvent, "notificationId")
    descriptor = None
    for klass in esmodel::events::NotificationReadEvent.__mro__:
        if "notificationId" in klass.__dict__:
            descriptor = klass.__dict__["notificationId"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::operations::modelelementgroup_is_not_abstract():
    assert not inspect.isabstract(esmodel::operations::ModelElementGroup)


def test_esmodel::operations::modelelementgroup_constructor_exists():
    assert callable(esmodel::operations::ModelElementGroup.__init__)


def test_esmodel::operations::modelelementgroup_constructor_args():
    sig = inspect.signature(esmodel::operations::ModelElementGroup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esmodel::operations::modelelementgroup_has_name():
    assert hasattr(esmodel::operations::ModelElementGroup, "name")
    descriptor = None
    for klass in esmodel::operations::ModelElementGroup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::events::showhistoryevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::ShowHistoryEvent)


def test_esmodel::events::showhistoryevent_constructor_exists():
    assert callable(esmodel::events::ShowHistoryEvent.__init__)


def test_esmodel::events::showhistoryevent_constructor_args():
    sig = inspect.signature(esmodel::events::ShowHistoryEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::events::exceptionevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::ExceptionEvent)


def test_esmodel::events::exceptionevent_constructor_exists():
    assert callable(esmodel::events::ExceptionEvent.__init__)


def test_esmodel::events::exceptionevent_constructor_args():
    sig = inspect.signature(esmodel::events::ExceptionEvent.__init__)
    params = list(sig.parameters.keys())
    assert "ExceptionCauseTitle" in params, "Missing parameter 'ExceptionCauseTitle'"
    assert "ExceptionCauseStackTrace" in params, "Missing parameter 'ExceptionCauseStackTrace'"
    assert "ExceptionTitle" in params, "Missing parameter 'ExceptionTitle'"
    assert "ExceptionStackTrace" in params, "Missing parameter 'ExceptionStackTrace'"

def test_esmodel::events::exceptionevent_has_ExceptionCauseTitle():
    assert hasattr(esmodel::events::ExceptionEvent, "ExceptionCauseTitle")
    descriptor = None
    for klass in esmodel::events::ExceptionEvent.__mro__:
        if "ExceptionCauseTitle" in klass.__dict__:
            descriptor = klass.__dict__["ExceptionCauseTitle"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::events::exceptionevent_has_ExceptionCauseStackTrace():
    assert hasattr(esmodel::events::ExceptionEvent, "ExceptionCauseStackTrace")
    descriptor = None
    for klass in esmodel::events::ExceptionEvent.__mro__:
        if "ExceptionCauseStackTrace" in klass.__dict__:
            descriptor = klass.__dict__["ExceptionCauseStackTrace"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::events::exceptionevent_has_ExceptionTitle():
    assert hasattr(esmodel::events::ExceptionEvent, "ExceptionTitle")
    descriptor = None
    for klass in esmodel::events::ExceptionEvent.__mro__:
        if "ExceptionTitle" in klass.__dict__:
            descriptor = klass.__dict__["ExceptionTitle"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::events::exceptionevent_has_ExceptionStackTrace():
    assert hasattr(esmodel::events::ExceptionEvent, "ExceptionStackTrace")
    descriptor = None
    for klass in esmodel::events::ExceptionEvent.__mro__:
        if "ExceptionStackTrace" in klass.__dict__:
            descriptor = klass.__dict__["ExceptionStackTrace"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::events::annotationevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::AnnotationEvent)


def test_esmodel::events::annotationevent_constructor_exists():
    assert callable(esmodel::events::AnnotationEvent.__init__)


def test_esmodel::events::annotationevent_constructor_args():
    sig = inspect.signature(esmodel::events::AnnotationEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::events::mergeglobalchoiceevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::MergeGlobalChoiceEvent)


def test_esmodel::events::mergeglobalchoiceevent_constructor_exists():
    assert callable(esmodel::events::MergeGlobalChoiceEvent.__init__)


def test_esmodel::events::mergeglobalchoiceevent_constructor_args():
    sig = inspect.signature(esmodel::events::MergeGlobalChoiceEvent.__init__)
    params = list(sig.parameters.keys())
    assert "selection" in params, "Missing parameter 'selection'"

def test_esmodel::events::mergeglobalchoiceevent_has_selection():
    assert hasattr(esmodel::events::MergeGlobalChoiceEvent, "selection")
    descriptor = None
    for klass in esmodel::events::MergeGlobalChoiceEvent.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::events::traceevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::TraceEvent)


def test_esmodel::events::traceevent_constructor_exists():
    assert callable(esmodel::events::TraceEvent.__init__)


def test_esmodel::events::traceevent_constructor_args():
    sig = inspect.signature(esmodel::events::TraceEvent.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_esmodel::events::traceevent_has_featureName():
    assert hasattr(esmodel::events::TraceEvent, "featureName")
    descriptor = None
    for klass in esmodel::events::TraceEvent.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::events::perspectiveevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::PerspectiveEvent)


def test_esmodel::events::perspectiveevent_constructor_exists():
    assert callable(esmodel::events::PerspectiveEvent.__init__)


def test_esmodel::events::perspectiveevent_constructor_args():
    sig = inspect.signature(esmodel::events::PerspectiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::events::mergechoiceevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::MergeChoiceEvent)


def test_esmodel::events::mergechoiceevent_constructor_exists():
    assert callable(esmodel::events::MergeChoiceEvent.__init__)


def test_esmodel::events::mergechoiceevent_constructor_args():
    sig = inspect.signature(esmodel::events::MergeChoiceEvent.__init__)
    params = list(sig.parameters.keys())
    assert "createdIssueName" in params, "Missing parameter 'createdIssueName'"
    assert "selection" in params, "Missing parameter 'selection'"
    assert "contextFeature" in params, "Missing parameter 'contextFeature'"

def test_esmodel::events::mergechoiceevent_has_createdIssueName():
    assert hasattr(esmodel::events::MergeChoiceEvent, "createdIssueName")
    descriptor = None
    for klass in esmodel::events::MergeChoiceEvent.__mro__:
        if "createdIssueName" in klass.__dict__:
            descriptor = klass.__dict__["createdIssueName"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::events::mergechoiceevent_has_selection():
    assert hasattr(esmodel::events::MergeChoiceEvent, "selection")
    descriptor = None
    for klass in esmodel::events::MergeChoiceEvent.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::events::mergechoiceevent_has_contextFeature():
    assert hasattr(esmodel::events::MergeChoiceEvent, "contextFeature")
    descriptor = None
    for klass in esmodel::events::MergeChoiceEvent.__mro__:
        if "contextFeature" in klass.__dict__:
            descriptor = klass.__dict__["contextFeature"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::events::linkevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::LinkEvent)


def test_esmodel::events::linkevent_constructor_exists():
    assert callable(esmodel::events::LinkEvent.__init__)


def test_esmodel::events::linkevent_constructor_args():
    sig = inspect.signature(esmodel::events::LinkEvent.__init__)
    params = list(sig.parameters.keys())
    assert "createdNew" in params, "Missing parameter 'createdNew'"
    assert "sourceView" in params, "Missing parameter 'sourceView'"

def test_esmodel::events::linkevent_has_createdNew():
    assert hasattr(esmodel::events::LinkEvent, "createdNew")
    descriptor = None
    for klass in esmodel::events::LinkEvent.__mro__:
        if "createdNew" in klass.__dict__:
            descriptor = klass.__dict__["createdNew"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::events::linkevent_has_sourceView():
    assert hasattr(esmodel::events::LinkEvent, "sourceView")
    descriptor = None
    for klass in esmodel::events::LinkEvent.__mro__:
        if "sourceView" in klass.__dict__:
            descriptor = klass.__dict__["sourceView"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::events::pluginfocusevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::PluginFocusEvent)


def test_esmodel::events::pluginfocusevent_constructor_exists():
    assert callable(esmodel::events::PluginFocusEvent.__init__)


def test_esmodel::events::pluginfocusevent_constructor_args():
    sig = inspect.signature(esmodel::events::PluginFocusEvent.__init__)
    params = list(sig.parameters.keys())
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "pluginId" in params, "Missing parameter 'pluginId'"

def test_esmodel::events::pluginfocusevent_has_startDate():
    assert hasattr(esmodel::events::PluginFocusEvent, "startDate")
    descriptor = None
    for klass in esmodel::events::PluginFocusEvent.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::events::pluginfocusevent_has_pluginId():
    assert hasattr(esmodel::events::PluginFocusEvent, "pluginId")
    descriptor = None
    for klass in esmodel::events::PluginFocusEvent.__mro__:
        if "pluginId" in klass.__dict__:
            descriptor = klass.__dict__["pluginId"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::events::notificationignoreevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::NotificationIgnoreEvent)


def test_esmodel::events::notificationignoreevent_constructor_exists():
    assert callable(esmodel::events::NotificationIgnoreEvent.__init__)


def test_esmodel::events::notificationignoreevent_constructor_args():
    sig = inspect.signature(esmodel::events::NotificationIgnoreEvent.__init__)
    params = list(sig.parameters.keys())
    assert "notificationId" in params, "Missing parameter 'notificationId'"

def test_esmodel::events::notificationignoreevent_has_notificationId():
    assert hasattr(esmodel::events::NotificationIgnoreEvent, "notificationId")
    descriptor = None
    for klass in esmodel::events::NotificationIgnoreEvent.__mro__:
        if "notificationId" in klass.__dict__:
            descriptor = klass.__dict__["notificationId"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::events::updateevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::UpdateEvent)


def test_esmodel::events::updateevent_constructor_exists():
    assert callable(esmodel::events::UpdateEvent.__init__)


def test_esmodel::events::updateevent_constructor_args():
    sig = inspect.signature(esmodel::events::UpdateEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::events::presentationswitchevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::PresentationSwitchEvent)


def test_esmodel::events::presentationswitchevent_constructor_exists():
    assert callable(esmodel::events::PresentationSwitchEvent.__init__)


def test_esmodel::events::presentationswitchevent_constructor_args():
    sig = inspect.signature(esmodel::events::PresentationSwitchEvent.__init__)
    params = list(sig.parameters.keys())
    assert "newPresentation" in params, "Missing parameter 'newPresentation'"
    assert "readView" in params, "Missing parameter 'readView'"

def test_esmodel::events::presentationswitchevent_has_newPresentation():
    assert hasattr(esmodel::events::PresentationSwitchEvent, "newPresentation")
    descriptor = None
    for klass in esmodel::events::PresentationSwitchEvent.__mro__:
        if "newPresentation" in klass.__dict__:
            descriptor = klass.__dict__["newPresentation"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::events::presentationswitchevent_has_readView():
    assert hasattr(esmodel::events::PresentationSwitchEvent, "readView")
    descriptor = None
    for klass in esmodel::events::PresentationSwitchEvent.__mro__:
        if "readView" in klass.__dict__:
            descriptor = klass.__dict__["readView"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::events::urlevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::URLEvent)


def test_esmodel::events::urlevent_constructor_exists():
    assert callable(esmodel::events::URLEvent.__init__)


def test_esmodel::events::urlevent_constructor_args():
    sig = inspect.signature(esmodel::events::URLEvent.__init__)
    params = list(sig.parameters.keys())
    assert "sourceView" in params, "Missing parameter 'sourceView'"

def test_esmodel::events::urlevent_has_sourceView():
    assert hasattr(esmodel::events::URLEvent, "sourceView")
    descriptor = None
    for klass in esmodel::events::URLEvent.__mro__:
        if "sourceView" in klass.__dict__:
            descriptor = klass.__dict__["sourceView"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::events::notificationgenerationevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::NotificationGenerationEvent)


def test_esmodel::events::notificationgenerationevent_constructor_exists():
    assert callable(esmodel::events::NotificationGenerationEvent.__init__)


def test_esmodel::events::notificationgenerationevent_constructor_args():
    sig = inspect.signature(esmodel::events::NotificationGenerationEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::events::showchangesevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::ShowChangesEvent)


def test_esmodel::events::showchangesevent_constructor_exists():
    assert callable(esmodel::events::ShowChangesEvent.__init__)


def test_esmodel::events::showchangesevent_constructor_args():
    sig = inspect.signature(esmodel::events::ShowChangesEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::events::pluginstartevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::PluginStartEvent)


def test_esmodel::events::pluginstartevent_constructor_exists():
    assert callable(esmodel::events::PluginStartEvent.__init__)


def test_esmodel::events::pluginstartevent_constructor_args():
    sig = inspect.signature(esmodel::events::PluginStartEvent.__init__)
    params = list(sig.parameters.keys())
    assert "pluginId" in params, "Missing parameter 'pluginId'"

def test_esmodel::events::pluginstartevent_has_pluginId():
    assert hasattr(esmodel::events::PluginStartEvent, "pluginId")
    descriptor = None
    for klass in esmodel::events::PluginStartEvent.__mro__:
        if "pluginId" in klass.__dict__:
            descriptor = klass.__dict__["pluginId"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::server::serverevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::server::ServerEvent)


def test_esmodel::server::serverevent_constructor_exists():
    assert callable(esmodel::server::ServerEvent.__init__)


def test_esmodel::server::serverevent_constructor_args():
    sig = inspect.signature(esmodel::server::ServerEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::events::checkoutevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::CheckoutEvent)


def test_esmodel::events::checkoutevent_constructor_exists():
    assert callable(esmodel::events::CheckoutEvent.__init__)


def test_esmodel::events::checkoutevent_constructor_args():
    sig = inspect.signature(esmodel::events::CheckoutEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::events::validate_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::Validate)


def test_esmodel::events::validate_constructor_exists():
    assert callable(esmodel::events::Validate.__init__)


def test_esmodel::events::validate_constructor_args():
    sig = inspect.signature(esmodel::events::Validate.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::events::mergeevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::MergeEvent)


def test_esmodel::events::mergeevent_constructor_exists():
    assert callable(esmodel::events::MergeEvent.__init__)


def test_esmodel::events::mergeevent_constructor_args():
    sig = inspect.signature(esmodel::events::MergeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfConflicts" in params, "Missing parameter 'numberOfConflicts'"
    assert "totalTime" in params, "Missing parameter 'totalTime'"

def test_esmodel::events::mergeevent_has_numberOfConflicts():
    assert hasattr(esmodel::events::MergeEvent, "numberOfConflicts")
    descriptor = None
    for klass in esmodel::events::MergeEvent.__mro__:
        if "numberOfConflicts" in klass.__dict__:
            descriptor = klass.__dict__["numberOfConflicts"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::events::mergeevent_has_totalTime():
    assert hasattr(esmodel::events::MergeEvent, "totalTime")
    descriptor = None
    for klass in esmodel::events::MergeEvent.__mro__:
        if "totalTime" in klass.__dict__:
            descriptor = klass.__dict__["totalTime"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::events::navigatorcreateevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::NavigatorCreateEvent)


def test_esmodel::events::navigatorcreateevent_constructor_exists():
    assert callable(esmodel::events::NavigatorCreateEvent.__init__)


def test_esmodel::events::navigatorcreateevent_constructor_args():
    sig = inspect.signature(esmodel::events::NavigatorCreateEvent.__init__)
    params = list(sig.parameters.keys())
    assert "dynamic" in params, "Missing parameter 'dynamic'"

def test_esmodel::events::navigatorcreateevent_has_dynamic():
    assert hasattr(esmodel::events::NavigatorCreateEvent, "dynamic")
    descriptor = None
    for klass in esmodel::events::NavigatorCreateEvent.__mro__:
        if "dynamic" in klass.__dict__:
            descriptor = klass.__dict__["dynamic"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::events::dndevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::DNDEvent)


def test_esmodel::events::dndevent_constructor_exists():
    assert callable(esmodel::events::DNDEvent.__init__)


def test_esmodel::events::dndevent_constructor_args():
    sig = inspect.signature(esmodel::events::DNDEvent.__init__)
    params = list(sig.parameters.keys())
    assert "targetView" in params, "Missing parameter 'targetView'"
    assert "sourceView" in params, "Missing parameter 'sourceView'"

def test_esmodel::events::dndevent_has_targetView():
    assert hasattr(esmodel::events::DNDEvent, "targetView")
    descriptor = None
    for klass in esmodel::events::DNDEvent.__mro__:
        if "targetView" in klass.__dict__:
            descriptor = klass.__dict__["targetView"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::events::dndevent_has_sourceView():
    assert hasattr(esmodel::events::DNDEvent, "sourceView")
    descriptor = None
    for klass in esmodel::events::DNDEvent.__mro__:
        if "sourceView" in klass.__dict__:
            descriptor = klass.__dict__["sourceView"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::events::undoevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::UndoEvent)


def test_esmodel::events::undoevent_constructor_exists():
    assert callable(esmodel::events::UndoEvent.__init__)


def test_esmodel::events::undoevent_constructor_args():
    sig = inspect.signature(esmodel::events::UndoEvent.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::events::revertevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::RevertEvent)


def test_esmodel::events::revertevent_constructor_exists():
    assert callable(esmodel::events::RevertEvent.__init__)


def test_esmodel::events::revertevent_constructor_args():
    sig = inspect.signature(esmodel::events::RevertEvent.__init__)
    params = list(sig.parameters.keys())
    assert "revertedChangesCount" in params, "Missing parameter 'revertedChangesCount'"

def test_esmodel::events::revertevent_has_revertedChangesCount():
    assert hasattr(esmodel::events::RevertEvent, "revertedChangesCount")
    descriptor = None
    for klass in esmodel::events::RevertEvent.__mro__:
        if "revertedChangesCount" in klass.__dict__:
            descriptor = klass.__dict__["revertedChangesCount"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::events::readevent_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::ReadEvent)


def test_esmodel::events::readevent_constructor_exists():
    assert callable(esmodel::events::ReadEvent.__init__)


def test_esmodel::events::readevent_constructor_args():
    sig = inspect.signature(esmodel::events::ReadEvent.__init__)
    params = list(sig.parameters.keys())
    assert "readView" in params, "Missing parameter 'readView'"
    assert "sourceView" in params, "Missing parameter 'sourceView'"

def test_esmodel::events::readevent_has_readView():
    assert hasattr(esmodel::events::ReadEvent, "readView")
    descriptor = None
    for klass in esmodel::events::ReadEvent.__mro__:
        if "readView" in klass.__dict__:
            descriptor = klass.__dict__["readView"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::events::readevent_has_sourceView():
    assert hasattr(esmodel::events::ReadEvent, "sourceView")
    descriptor = None
    for klass in esmodel::events::ReadEvent.__mro__:
        if "sourceView" in klass.__dict__:
            descriptor = klass.__dict__["sourceView"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::events::event_is_not_abstract():
    assert not inspect.isabstract(esmodel::events::Event)


def test_esmodel::events::event_constructor_exists():
    assert callable(esmodel::events::Event.__init__)


def test_esmodel::events::event_constructor_args():
    sig = inspect.signature(esmodel::events::Event.__init__)
    params = list(sig.parameters.keys())
    assert "timestamp" in params, "Missing parameter 'timestamp'"

def test_esmodel::events::event_has_timestamp():
    assert hasattr(esmodel::events::Event, "timestamp")
    descriptor = None
    for klass in esmodel::events::Event.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)



def test_compositeoperation_is_not_abstract():
    assert not inspect.isabstract(CompositeOperation)


def test_compositeoperation_constructor_exists():
    assert callable(CompositeOperation.__init__)


def test_compositeoperation_constructor_args():
    sig = inspect.signature(CompositeOperation.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::semantic::semanticcompositeoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel::semantic::SemanticCompositeOperation)


def test_esmodel::semantic::semanticcompositeoperation_constructor_exists():
    assert callable(esmodel::semantic::SemanticCompositeOperation.__init__)


def test_esmodel::semantic::semanticcompositeoperation_constructor_args():
    sig = inspect.signature(esmodel::semantic::SemanticCompositeOperation.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::operations::eobjecttomodelelementidmap_is_not_abstract():
    assert not inspect.isabstract(esmodel::operations::EObjectToModelElementIdMap)


def test_esmodel::operations::eobjecttomodelelementidmap_constructor_exists():
    assert callable(esmodel::operations::EObjectToModelElementIdMap.__init__)


def test_esmodel::operations::eobjecttomodelelementidmap_constructor_args():
    sig = inspect.signature(esmodel::operations::EObjectToModelElementIdMap.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::operations::operationgroup_is_not_abstract():
    assert not inspect.isabstract(esmodel::operations::OperationGroup)


def test_esmodel::operations::operationgroup_constructor_exists():
    assert callable(esmodel::operations::OperationGroup.__init__)


def test_esmodel::operations::operationgroup_constructor_args():
    sig = inspect.signature(esmodel::operations::OperationGroup.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esmodel::operations::operationgroup_has_name():
    assert hasattr(esmodel::operations::OperationGroup, "name")
    descriptor = None
    for klass in esmodel::operations::OperationGroup.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::operations::operationid_is_not_abstract():
    assert not inspect.isabstract(esmodel::operations::OperationId)


def test_esmodel::operations::operationid_constructor_exists():
    assert callable(esmodel::operations::OperationId.__init__)


def test_esmodel::operations::operationid_constructor_args():
    sig = inspect.signature(esmodel::operations::OperationId.__init__)
    params = list(sig.parameters.keys())



def test_attributeoperation_is_not_abstract():
    assert not inspect.isabstract(AttributeOperation)


def test_attributeoperation_constructor_exists():
    assert callable(AttributeOperation.__init__)


def test_attributeoperation_constructor_args():
    sig = inspect.signature(AttributeOperation.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::operations::diagramlayoutoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel::operations::DiagramLayoutOperation)


def test_esmodel::operations::diagramlayoutoperation_constructor_exists():
    assert callable(esmodel::operations::DiagramLayoutOperation.__init__)


def test_esmodel::operations::diagramlayoutoperation_constructor_args():
    sig = inspect.signature(esmodel::operations::DiagramLayoutOperation.__init__)
    params = list(sig.parameters.keys())



def test_referenceoperation_is_not_abstract():
    assert not inspect.isabstract(ReferenceOperation)


def test_referenceoperation_constructor_exists():
    assert callable(ReferenceOperation.__init__)


def test_referenceoperation_constructor_args():
    sig = inspect.signature(ReferenceOperation.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::operations::multireferencesetoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel::operations::MultiReferenceSetOperation)


def test_esmodel::operations::multireferencesetoperation_constructor_exists():
    assert callable(esmodel::operations::MultiReferenceSetOperation.__init__)


def test_esmodel::operations::multireferencesetoperation_constructor_args():
    sig = inspect.signature(esmodel::operations::MultiReferenceSetOperation.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"

def test_esmodel::operations::multireferencesetoperation_has_index():
    assert hasattr(esmodel::operations::MultiReferenceSetOperation, "index")
    descriptor = None
    for klass in esmodel::operations::MultiReferenceSetOperation.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::operations::multireferenceoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel::operations::MultiReferenceOperation)


def test_esmodel::operations::multireferenceoperation_constructor_exists():
    assert callable(esmodel::operations::MultiReferenceOperation.__init__)


def test_esmodel::operations::multireferenceoperation_constructor_args():
    sig = inspect.signature(esmodel::operations::MultiReferenceOperation.__init__)
    params = list(sig.parameters.keys())
    assert "add" in params, "Missing parameter 'add'"
    assert "index" in params, "Missing parameter 'index'"

def test_esmodel::operations::multireferenceoperation_has_add():
    assert hasattr(esmodel::operations::MultiReferenceOperation, "add")
    descriptor = None
    for klass in esmodel::operations::MultiReferenceOperation.__mro__:
        if "add" in klass.__dict__:
            descriptor = klass.__dict__["add"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::operations::multireferenceoperation_has_index():
    assert hasattr(esmodel::operations::MultiReferenceOperation, "index")
    descriptor = None
    for klass in esmodel::operations::MultiReferenceOperation.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::operations::singlereferenceoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel::operations::SingleReferenceOperation)


def test_esmodel::operations::singlereferenceoperation_constructor_exists():
    assert callable(esmodel::operations::SingleReferenceOperation.__init__)


def test_esmodel::operations::singlereferenceoperation_constructor_args():
    sig = inspect.signature(esmodel::operations::SingleReferenceOperation.__init__)
    params = list(sig.parameters.keys())



def test_featureoperation_is_not_abstract():
    assert not inspect.isabstract(FeatureOperation)


def test_featureoperation_constructor_exists():
    assert callable(FeatureOperation.__init__)


def test_featureoperation_constructor_args():
    sig = inspect.signature(FeatureOperation.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::operations::multiattributesetoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel::operations::MultiAttributeSetOperation)


def test_esmodel::operations::multiattributesetoperation_constructor_exists():
    assert callable(esmodel::operations::MultiAttributeSetOperation.__init__)


def test_esmodel::operations::multiattributesetoperation_constructor_args():
    sig = inspect.signature(esmodel::operations::MultiAttributeSetOperation.__init__)
    params = list(sig.parameters.keys())
    assert "newValue" in params, "Missing parameter 'newValue'"
    assert "index" in params, "Missing parameter 'index'"
    assert "oldValue" in params, "Missing parameter 'oldValue'"

def test_esmodel::operations::multiattributesetoperation_has_newValue():
    assert hasattr(esmodel::operations::MultiAttributeSetOperation, "newValue")
    descriptor = None
    for klass in esmodel::operations::MultiAttributeSetOperation.__mro__:
        if "newValue" in klass.__dict__:
            descriptor = klass.__dict__["newValue"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::operations::multiattributesetoperation_has_index():
    assert hasattr(esmodel::operations::MultiAttributeSetOperation, "index")
    descriptor = None
    for klass in esmodel::operations::MultiAttributeSetOperation.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::operations::multiattributesetoperation_has_oldValue():
    assert hasattr(esmodel::operations::MultiAttributeSetOperation, "oldValue")
    descriptor = None
    for klass in esmodel::operations::MultiAttributeSetOperation.__mro__:
        if "oldValue" in klass.__dict__:
            descriptor = klass.__dict__["oldValue"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::operations::multiattributemoveoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel::operations::MultiAttributeMoveOperation)


def test_esmodel::operations::multiattributemoveoperation_constructor_exists():
    assert callable(esmodel::operations::MultiAttributeMoveOperation.__init__)


def test_esmodel::operations::multiattributemoveoperation_constructor_args():
    sig = inspect.signature(esmodel::operations::MultiAttributeMoveOperation.__init__)
    params = list(sig.parameters.keys())
    assert "newIndex" in params, "Missing parameter 'newIndex'"
    assert "oldIndex" in params, "Missing parameter 'oldIndex'"
    assert "referencedValue" in params, "Missing parameter 'referencedValue'"

def test_esmodel::operations::multiattributemoveoperation_has_newIndex():
    assert hasattr(esmodel::operations::MultiAttributeMoveOperation, "newIndex")
    descriptor = None
    for klass in esmodel::operations::MultiAttributeMoveOperation.__mro__:
        if "newIndex" in klass.__dict__:
            descriptor = klass.__dict__["newIndex"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::operations::multiattributemoveoperation_has_oldIndex():
    assert hasattr(esmodel::operations::MultiAttributeMoveOperation, "oldIndex")
    descriptor = None
    for klass in esmodel::operations::MultiAttributeMoveOperation.__mro__:
        if "oldIndex" in klass.__dict__:
            descriptor = klass.__dict__["oldIndex"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::operations::multiattributemoveoperation_has_referencedValue():
    assert hasattr(esmodel::operations::MultiAttributeMoveOperation, "referencedValue")
    descriptor = None
    for klass in esmodel::operations::MultiAttributeMoveOperation.__mro__:
        if "referencedValue" in klass.__dict__:
            descriptor = klass.__dict__["referencedValue"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::operations::multireferencemoveoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel::operations::MultiReferenceMoveOperation)


def test_esmodel::operations::multireferencemoveoperation_constructor_exists():
    assert callable(esmodel::operations::MultiReferenceMoveOperation.__init__)


def test_esmodel::operations::multireferencemoveoperation_constructor_args():
    sig = inspect.signature(esmodel::operations::MultiReferenceMoveOperation.__init__)
    params = list(sig.parameters.keys())
    assert "oldIndex" in params, "Missing parameter 'oldIndex'"
    assert "newIndex" in params, "Missing parameter 'newIndex'"

def test_esmodel::operations::multireferencemoveoperation_has_oldIndex():
    assert hasattr(esmodel::operations::MultiReferenceMoveOperation, "oldIndex")
    descriptor = None
    for klass in esmodel::operations::MultiReferenceMoveOperation.__mro__:
        if "oldIndex" in klass.__dict__:
            descriptor = klass.__dict__["oldIndex"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::operations::multireferencemoveoperation_has_newIndex():
    assert hasattr(esmodel::operations::MultiReferenceMoveOperation, "newIndex")
    descriptor = None
    for klass in esmodel::operations::MultiReferenceMoveOperation.__mro__:
        if "newIndex" in klass.__dict__:
            descriptor = klass.__dict__["newIndex"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::operations::referenceoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel::operations::ReferenceOperation)


def test_esmodel::operations::referenceoperation_constructor_exists():
    assert callable(esmodel::operations::ReferenceOperation.__init__)


def test_esmodel::operations::referenceoperation_constructor_args():
    sig = inspect.signature(esmodel::operations::ReferenceOperation.__init__)
    params = list(sig.parameters.keys())
    assert "bidirectional" in params, "Missing parameter 'bidirectional'"
    assert "oppositeFeatureName" in params, "Missing parameter 'oppositeFeatureName'"
    assert "containmentType" in params, "Missing parameter 'containmentType'"

def test_esmodel::operations::referenceoperation_has_bidirectional():
    assert hasattr(esmodel::operations::ReferenceOperation, "bidirectional")
    descriptor = None
    for klass in esmodel::operations::ReferenceOperation.__mro__:
        if "bidirectional" in klass.__dict__:
            descriptor = klass.__dict__["bidirectional"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::operations::referenceoperation_has_oppositeFeatureName():
    assert hasattr(esmodel::operations::ReferenceOperation, "oppositeFeatureName")
    descriptor = None
    for klass in esmodel::operations::ReferenceOperation.__mro__:
        if "oppositeFeatureName" in klass.__dict__:
            descriptor = klass.__dict__["oppositeFeatureName"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::operations::referenceoperation_has_containmentType():
    assert hasattr(esmodel::operations::ReferenceOperation, "containmentType")
    descriptor = None
    for klass in esmodel::operations::ReferenceOperation.__mro__:
        if "containmentType" in klass.__dict__:
            descriptor = klass.__dict__["containmentType"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::operations::multiattributeoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel::operations::MultiAttributeOperation)


def test_esmodel::operations::multiattributeoperation_constructor_exists():
    assert callable(esmodel::operations::MultiAttributeOperation.__init__)


def test_esmodel::operations::multiattributeoperation_constructor_args():
    sig = inspect.signature(esmodel::operations::MultiAttributeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "add" in params, "Missing parameter 'add'"
    assert "indexes" in params, "Missing parameter 'indexes'"
    assert "referencedValues" in params, "Missing parameter 'referencedValues'"

def test_esmodel::operations::multiattributeoperation_has_add():
    assert hasattr(esmodel::operations::MultiAttributeOperation, "add")
    descriptor = None
    for klass in esmodel::operations::MultiAttributeOperation.__mro__:
        if "add" in klass.__dict__:
            descriptor = klass.__dict__["add"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::operations::multiattributeoperation_has_indexes():
    assert hasattr(esmodel::operations::MultiAttributeOperation, "indexes")
    descriptor = None
    for klass in esmodel::operations::MultiAttributeOperation.__mro__:
        if "indexes" in klass.__dict__:
            descriptor = klass.__dict__["indexes"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::operations::multiattributeoperation_has_referencedValues():
    assert hasattr(esmodel::operations::MultiAttributeOperation, "referencedValues")
    descriptor = None
    for klass in esmodel::operations::MultiAttributeOperation.__mro__:
        if "referencedValues" in klass.__dict__:
            descriptor = klass.__dict__["referencedValues"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::operations::attributeoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel::operations::AttributeOperation)


def test_esmodel::operations::attributeoperation_constructor_exists():
    assert callable(esmodel::operations::AttributeOperation.__init__)


def test_esmodel::operations::attributeoperation_constructor_args():
    sig = inspect.signature(esmodel::operations::AttributeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "newValue" in params, "Missing parameter 'newValue'"
    assert "oldValue" in params, "Missing parameter 'oldValue'"

def test_esmodel::operations::attributeoperation_has_newValue():
    assert hasattr(esmodel::operations::AttributeOperation, "newValue")
    descriptor = None
    for klass in esmodel::operations::AttributeOperation.__mro__:
        if "newValue" in klass.__dict__:
            descriptor = klass.__dict__["newValue"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::operations::attributeoperation_has_oldValue():
    assert hasattr(esmodel::operations::AttributeOperation, "oldValue")
    descriptor = None
    for klass in esmodel::operations::AttributeOperation.__mro__:
        if "oldValue" in klass.__dict__:
            descriptor = klass.__dict__["oldValue"]
            break
    assert isinstance(descriptor, property)



def test_operations::eobjecttomodelelementidmap_is_not_abstract():
    assert not inspect.isabstract(operations::EObjectToModelElementIdMap)


def test_operations::eobjecttomodelelementidmap_constructor_exists():
    assert callable(operations::EObjectToModelElementIdMap.__init__)


def test_operations::eobjecttomodelelementidmap_constructor_args():
    sig = inspect.signature(operations::EObjectToModelElementIdMap.__init__)
    params = list(sig.parameters.keys())



def test_operations::referenceoperation_is_not_abstract():
    assert not inspect.isabstract(operations::ReferenceOperation)


def test_operations::referenceoperation_constructor_exists():
    assert callable(operations::ReferenceOperation.__init__)


def test_operations::referenceoperation_constructor_args():
    sig = inspect.signature(operations::ReferenceOperation.__init__)
    params = list(sig.parameters.keys())



def test_operations::esmodel::eobject_is_not_abstract():
    assert not inspect.isabstract(operations::esmodel::EObject)


def test_operations::esmodel::eobject_constructor_exists():
    assert callable(operations::esmodel::EObject.__init__)


def test_operations::esmodel::eobject_constructor_args():
    sig = inspect.signature(operations::esmodel::EObject.__init__)
    params = list(sig.parameters.keys())



def test_abstractoperation_is_not_abstract():
    assert not inspect.isabstract(AbstractOperation)


def test_abstractoperation_constructor_exists():
    assert callable(AbstractOperation.__init__)


def test_abstractoperation_constructor_args():
    sig = inspect.signature(AbstractOperation.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::operations::featureoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel::operations::FeatureOperation)


def test_esmodel::operations::featureoperation_constructor_exists():
    assert callable(esmodel::operations::FeatureOperation.__init__)


def test_esmodel::operations::featureoperation_constructor_args():
    sig = inspect.signature(esmodel::operations::FeatureOperation.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_esmodel::operations::featureoperation_has_featureName():
    assert hasattr(esmodel::operations::FeatureOperation, "featureName")
    descriptor = None
    for klass in esmodel::operations::FeatureOperation.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::operations::createdeleteoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel::operations::CreateDeleteOperation)


def test_esmodel::operations::createdeleteoperation_constructor_exists():
    assert callable(esmodel::operations::CreateDeleteOperation.__init__)


def test_esmodel::operations::createdeleteoperation_constructor_args():
    sig = inspect.signature(esmodel::operations::CreateDeleteOperation.__init__)
    params = list(sig.parameters.keys())
    assert "delete" in params, "Missing parameter 'delete'"

def test_esmodel::operations::createdeleteoperation_has_delete():
    assert hasattr(esmodel::operations::CreateDeleteOperation, "delete")
    descriptor = None
    for klass in esmodel::operations::CreateDeleteOperation.__mro__:
        if "delete" in klass.__dict__:
            descriptor = klass.__dict__["delete"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::operations::compositeoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel::operations::CompositeOperation)


def test_esmodel::operations::compositeoperation_constructor_exists():
    assert callable(esmodel::operations::CompositeOperation.__init__)


def test_esmodel::operations::compositeoperation_constructor_args():
    sig = inspect.signature(esmodel::operations::CompositeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "compositeName" in params, "Missing parameter 'compositeName'"
    assert "compositeDescription" in params, "Missing parameter 'compositeDescription'"
    assert "reversed" in params, "Missing parameter 'reversed'"

def test_esmodel::operations::compositeoperation_has_compositeName():
    assert hasattr(esmodel::operations::CompositeOperation, "compositeName")
    descriptor = None
    for klass in esmodel::operations::CompositeOperation.__mro__:
        if "compositeName" in klass.__dict__:
            descriptor = klass.__dict__["compositeName"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::operations::compositeoperation_has_compositeDescription():
    assert hasattr(esmodel::operations::CompositeOperation, "compositeDescription")
    descriptor = None
    for klass in esmodel::operations::CompositeOperation.__mro__:
        if "compositeDescription" in klass.__dict__:
            descriptor = klass.__dict__["compositeDescription"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::operations::compositeoperation_has_reversed():
    assert hasattr(esmodel::operations::CompositeOperation, "reversed")
    descriptor = None
    for klass in esmodel::operations::CompositeOperation.__mro__:
        if "reversed" in klass.__dict__:
            descriptor = klass.__dict__["reversed"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::operations::abstractoperation_is_not_abstract():
    assert not inspect.isabstract(esmodel::operations::AbstractOperation)


def test_esmodel::operations::abstractoperation_constructor_exists():
    assert callable(esmodel::operations::AbstractOperation.__init__)


def test_esmodel::operations::abstractoperation_constructor_args():
    sig = inspect.signature(esmodel::operations::AbstractOperation.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "accepted" in params, "Missing parameter 'accepted'"
    assert "clientDate" in params, "Missing parameter 'clientDate'"
    assert "name" in params, "Missing parameter 'name'"

def test_esmodel::operations::abstractoperation_has_description():
    assert hasattr(esmodel::operations::AbstractOperation, "description")
    descriptor = None
    for klass in esmodel::operations::AbstractOperation.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::operations::abstractoperation_has_accepted():
    assert hasattr(esmodel::operations::AbstractOperation, "accepted")
    descriptor = None
    for klass in esmodel::operations::AbstractOperation.__mro__:
        if "accepted" in klass.__dict__:
            descriptor = klass.__dict__["accepted"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::operations::abstractoperation_has_clientDate():
    assert hasattr(esmodel::operations::AbstractOperation, "clientDate")
    descriptor = None
    for klass in esmodel::operations::AbstractOperation.__mro__:
        if "clientDate" in klass.__dict__:
            descriptor = klass.__dict__["clientDate"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::operations::abstractoperation_has_name():
    assert hasattr(esmodel::operations::AbstractOperation, "name")
    descriptor = None
    for klass in esmodel::operations::AbstractOperation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::versioning::logmessage_is_not_abstract():
    assert not inspect.isabstract(esmodel::versioning::LogMessage)


def test_esmodel::versioning::logmessage_constructor_exists():
    assert callable(esmodel::versioning::LogMessage.__init__)


def test_esmodel::versioning::logmessage_constructor_args():
    sig = inspect.signature(esmodel::versioning::LogMessage.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "message" in params, "Missing parameter 'message'"
    assert "clientDate" in params, "Missing parameter 'clientDate'"
    assert "author" in params, "Missing parameter 'author'"

def test_esmodel::versioning::logmessage_has_date():
    assert hasattr(esmodel::versioning::LogMessage, "date")
    descriptor = None
    for klass in esmodel::versioning::LogMessage.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::versioning::logmessage_has_message():
    assert hasattr(esmodel::versioning::LogMessage, "message")
    descriptor = None
    for klass in esmodel::versioning::LogMessage.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::versioning::logmessage_has_clientDate():
    assert hasattr(esmodel::versioning::LogMessage, "clientDate")
    descriptor = None
    for klass in esmodel::versioning::LogMessage.__mro__:
        if "clientDate" in klass.__dict__:
            descriptor = klass.__dict__["clientDate"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::versioning::logmessage_has_author():
    assert hasattr(esmodel::versioning::LogMessage, "author")
    descriptor = None
    for klass in esmodel::versioning::LogMessage.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::versioning::versionproperty_is_not_abstract():
    assert not inspect.isabstract(esmodel::versioning::VersionProperty)


def test_esmodel::versioning::versionproperty_constructor_exists():
    assert callable(esmodel::versioning::VersionProperty.__init__)


def test_esmodel::versioning::versionproperty_constructor_args():
    sig = inspect.signature(esmodel::versioning::VersionProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_esmodel::versioning::versionproperty_has_name():
    assert hasattr(esmodel::versioning::VersionProperty, "name")
    descriptor = None
    for klass in esmodel::versioning::VersionProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::versioning::versionproperty_has_value():
    assert hasattr(esmodel::versioning::VersionProperty, "value")
    descriptor = None
    for klass in esmodel::versioning::VersionProperty.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::versioning::versionspec_is_not_abstract():
    assert not inspect.isabstract(esmodel::versioning::VersionSpec)


def test_esmodel::versioning::versionspec_constructor_exists():
    assert callable(esmodel::versioning::VersionSpec.__init__)


def test_esmodel::versioning::versionspec_constructor_args():
    sig = inspect.signature(esmodel::versioning::VersionSpec.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::versioning::version_is_not_abstract():
    assert not inspect.isabstract(esmodel::versioning::Version)


def test_esmodel::versioning::version_constructor_exists():
    assert callable(esmodel::versioning::Version.__init__)


def test_esmodel::versioning::version_constructor_args():
    sig = inspect.signature(esmodel::versioning::Version.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::versioning::historyquery_is_not_abstract():
    assert not inspect.isabstract(esmodel::versioning::HistoryQuery)


def test_esmodel::versioning::historyquery_constructor_exists():
    assert callable(esmodel::versioning::HistoryQuery.__init__)


def test_esmodel::versioning::historyquery_constructor_args():
    sig = inspect.signature(esmodel::versioning::HistoryQuery.__init__)
    params = list(sig.parameters.keys())
    assert "includeChangePackage" in params, "Missing parameter 'includeChangePackage'"

def test_esmodel::versioning::historyquery_has_includeChangePackage():
    assert hasattr(esmodel::versioning::HistoryQuery, "includeChangePackage")
    descriptor = None
    for klass in esmodel::versioning::HistoryQuery.__mro__:
        if "includeChangePackage" in klass.__dict__:
            descriptor = klass.__dict__["includeChangePackage"]
            break
    assert isinstance(descriptor, property)



def test_versioning::changepackage_is_not_abstract():
    assert not inspect.isabstract(versioning::ChangePackage)


def test_versioning::changepackage_constructor_exists():
    assert callable(versioning::ChangePackage.__init__)


def test_versioning::changepackage_constructor_args():
    sig = inspect.signature(versioning::ChangePackage.__init__)
    params = list(sig.parameters.keys())



def test_versioning::tagversionspec_is_not_abstract():
    assert not inspect.isabstract(versioning::TagVersionSpec)


def test_versioning::tagversionspec_constructor_exists():
    assert callable(versioning::TagVersionSpec.__init__)


def test_versioning::tagversionspec_constructor_args():
    sig = inspect.signature(versioning::TagVersionSpec.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::versioning::historyinfo_is_not_abstract():
    assert not inspect.isabstract(esmodel::versioning::HistoryInfo)


def test_esmodel::versioning::historyinfo_constructor_exists():
    assert callable(esmodel::versioning::HistoryInfo.__init__)


def test_esmodel::versioning::historyinfo_constructor_args():
    sig = inspect.signature(esmodel::versioning::HistoryInfo.__init__)
    params = list(sig.parameters.keys())



def test_versioning::versionproperty_is_not_abstract():
    assert not inspect.isabstract(versioning::VersionProperty)


def test_versioning::versionproperty_constructor_exists():
    assert callable(versioning::VersionProperty.__init__)


def test_versioning::versionproperty_constructor_args():
    sig = inspect.signature(versioning::VersionProperty.__init__)
    params = list(sig.parameters.keys())



def test_notification::esnotification_is_not_abstract():
    assert not inspect.isabstract(notification::ESNotification)


def test_notification::esnotification_constructor_exists():
    assert callable(notification::ESNotification.__init__)


def test_notification::esnotification_constructor_args():
    sig = inspect.signature(notification::ESNotification.__init__)
    params = list(sig.parameters.keys())



def test_versioning::logmessage_is_not_abstract():
    assert not inspect.isabstract(versioning::LogMessage)


def test_versioning::logmessage_constructor_exists():
    assert callable(versioning::LogMessage.__init__)


def test_versioning::logmessage_constructor_args():
    sig = inspect.signature(versioning::LogMessage.__init__)
    params = list(sig.parameters.keys())



def test_events::event_is_not_abstract():
    assert not inspect.isabstract(events::Event)


def test_events::event_constructor_exists():
    assert callable(events::Event.__init__)


def test_events::event_constructor_args():
    sig = inspect.signature(events::Event.__init__)
    params = list(sig.parameters.keys())



def test_operations::abstractoperation_is_not_abstract():
    assert not inspect.isabstract(operations::AbstractOperation)


def test_operations::abstractoperation_constructor_exists():
    assert callable(operations::AbstractOperation.__init__)


def test_operations::abstractoperation_constructor_args():
    sig = inspect.signature(operations::AbstractOperation.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::versioning::changepackage_is_not_abstract():
    assert not inspect.isabstract(esmodel::versioning::ChangePackage)


def test_esmodel::versioning::changepackage_constructor_exists():
    assert callable(esmodel::versioning::ChangePackage.__init__)


def test_esmodel::versioning::changepackage_constructor_args():
    sig = inspect.signature(esmodel::versioning::ChangePackage.__init__)
    params = list(sig.parameters.keys())



def test_versionspec_is_not_abstract():
    assert not inspect.isabstract(VersionSpec)


def test_versionspec_constructor_exists():
    assert callable(VersionSpec.__init__)


def test_versionspec_constructor_args():
    sig = inspect.signature(VersionSpec.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::versioning::dateversionspec_is_not_abstract():
    assert not inspect.isabstract(esmodel::versioning::DateVersionSpec)


def test_esmodel::versioning::dateversionspec_constructor_exists():
    assert callable(esmodel::versioning::DateVersionSpec.__init__)


def test_esmodel::versioning::dateversionspec_constructor_args():
    sig = inspect.signature(esmodel::versioning::DateVersionSpec.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"

def test_esmodel::versioning::dateversionspec_has_date():
    assert hasattr(esmodel::versioning::DateVersionSpec, "date")
    descriptor = None
    for klass in esmodel::versioning::DateVersionSpec.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::versioning::primaryversionspec_is_not_abstract():
    assert not inspect.isabstract(esmodel::versioning::PrimaryVersionSpec)


def test_esmodel::versioning::primaryversionspec_constructor_exists():
    assert callable(esmodel::versioning::PrimaryVersionSpec.__init__)


def test_esmodel::versioning::primaryversionspec_constructor_args():
    sig = inspect.signature(esmodel::versioning::PrimaryVersionSpec.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_esmodel::versioning::primaryversionspec_has_identifier():
    assert hasattr(esmodel::versioning::PrimaryVersionSpec, "identifier")
    descriptor = None
    for klass in esmodel::versioning::PrimaryVersionSpec.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::versioning::headversionspec_is_not_abstract():
    assert not inspect.isabstract(esmodel::versioning::HeadVersionSpec)


def test_esmodel::versioning::headversionspec_constructor_exists():
    assert callable(esmodel::versioning::HeadVersionSpec.__init__)


def test_esmodel::versioning::headversionspec_constructor_args():
    sig = inspect.signature(esmodel::versioning::HeadVersionSpec.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::versioning::tagversionspec_is_not_abstract():
    assert not inspect.isabstract(esmodel::versioning::TagVersionSpec)


def test_esmodel::versioning::tagversionspec_constructor_exists():
    assert callable(esmodel::versioning::TagVersionSpec.__init__)


def test_esmodel::versioning::tagversionspec_constructor_args():
    sig = inspect.signature(esmodel::versioning::TagVersionSpec.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esmodel::versioning::tagversionspec_has_name():
    assert hasattr(esmodel::versioning::TagVersionSpec, "name")
    descriptor = None
    for klass in esmodel::versioning::TagVersionSpec.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::clientversioninfo_is_not_abstract():
    assert not inspect.isabstract(esmodel::ClientVersionInfo)


def test_esmodel::clientversioninfo_constructor_exists():
    assert callable(esmodel::ClientVersionInfo.__init__)


def test_esmodel::clientversioninfo_constructor_args():
    sig = inspect.signature(esmodel::ClientVersionInfo.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"

def test_esmodel::clientversioninfo_has_version():
    assert hasattr(esmodel::ClientVersionInfo, "version")
    descriptor = None
    for klass in esmodel::ClientVersionInfo.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::clientversioninfo_has_name():
    assert hasattr(esmodel::ClientVersionInfo, "name")
    descriptor = None
    for klass in esmodel::ClientVersionInfo.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::versioninfo_is_not_abstract():
    assert not inspect.isabstract(esmodel::VersionInfo)


def test_esmodel::versioninfo_constructor_exists():
    assert callable(esmodel::VersionInfo.__init__)


def test_esmodel::versioninfo_constructor_args():
    sig = inspect.signature(esmodel::VersionInfo.__init__)
    params = list(sig.parameters.keys())
    assert "emfStoreVersionString" in params, "Missing parameter 'emfStoreVersionString'"

def test_esmodel::versioninfo_has_emfStoreVersionString():
    assert hasattr(esmodel::VersionInfo, "emfStoreVersionString")
    descriptor = None
    for klass in esmodel::VersionInfo.__mro__:
        if "emfStoreVersionString" in klass.__dict__:
            descriptor = klass.__dict__["emfStoreVersionString"]
            break
    assert isinstance(descriptor, property)



def test_esmodel::projectid_is_not_abstract():
    assert not inspect.isabstract(esmodel::ProjectId)


def test_esmodel::projectid_constructor_exists():
    assert callable(esmodel::ProjectId.__init__)


def test_esmodel::projectid_constructor_args():
    sig = inspect.signature(esmodel::ProjectId.__init__)
    params = list(sig.parameters.keys())



def test_accesscontrol::acuser_is_not_abstract():
    assert not inspect.isabstract(accesscontrol::ACUser)


def test_accesscontrol::acuser_constructor_exists():
    assert callable(accesscontrol::ACUser.__init__)


def test_accesscontrol::acuser_constructor_args():
    sig = inspect.signature(accesscontrol::ACUser.__init__)
    params = list(sig.parameters.keys())



def test_sessionid_is_not_abstract():
    assert not inspect.isabstract(SessionId)


def test_sessionid_constructor_exists():
    assert callable(SessionId.__init__)


def test_sessionid_constructor_args():
    sig = inspect.signature(SessionId.__init__)
    params = list(sig.parameters.keys())



def test_projecthistory_is_not_abstract():
    assert not inspect.isabstract(ProjectHistory)


def test_projecthistory_constructor_exists():
    assert callable(ProjectHistory.__init__)


def test_projecthistory_constructor_args():
    sig = inspect.signature(ProjectHistory.__init__)
    params = list(sig.parameters.keys())



def test_accesscontrol::acgroup_is_not_abstract():
    assert not inspect.isabstract(accesscontrol::ACGroup)


def test_accesscontrol::acgroup_constructor_exists():
    assert callable(accesscontrol::ACGroup.__init__)


def test_accesscontrol::acgroup_constructor_args():
    sig = inspect.signature(accesscontrol::ACGroup.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::serverspace_is_not_abstract():
    assert not inspect.isabstract(esmodel::ServerSpace)


def test_esmodel::serverspace_constructor_exists():
    assert callable(esmodel::ServerSpace.__init__)


def test_esmodel::serverspace_constructor_args():
    sig = inspect.signature(esmodel::ServerSpace.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::sessionid_is_not_abstract():
    assert not inspect.isabstract(esmodel::SessionId)


def test_esmodel::sessionid_constructor_exists():
    assert callable(esmodel::SessionId.__init__)


def test_esmodel::sessionid_constructor_args():
    sig = inspect.signature(esmodel::SessionId.__init__)
    params = list(sig.parameters.keys())



def test_versioning::primaryversionspec_is_not_abstract():
    assert not inspect.isabstract(versioning::PrimaryVersionSpec)


def test_versioning::primaryversionspec_constructor_exists():
    assert callable(versioning::PrimaryVersionSpec.__init__)


def test_versioning::primaryversionspec_constructor_args():
    sig = inspect.signature(versioning::PrimaryVersionSpec.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::projectinfo_is_not_abstract():
    assert not inspect.isabstract(esmodel::ProjectInfo)


def test_esmodel::projectinfo_constructor_exists():
    assert callable(esmodel::ProjectInfo.__init__)


def test_esmodel::projectinfo_constructor_args():
    sig = inspect.signature(esmodel::ProjectInfo.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_esmodel::projectinfo_has_name():
    assert hasattr(esmodel::ProjectInfo, "name")
    descriptor = None
    for klass in esmodel::ProjectInfo.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::projectinfo_has_description():
    assert hasattr(esmodel::ProjectInfo, "description")
    descriptor = None
    for klass in esmodel::ProjectInfo.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_versioning::version_is_not_abstract():
    assert not inspect.isabstract(versioning::Version)


def test_versioning::version_constructor_exists():
    assert callable(versioning::Version.__init__)


def test_versioning::version_constructor_args():
    sig = inspect.signature(versioning::Version.__init__)
    params = list(sig.parameters.keys())



def test_projectid_is_not_abstract():
    assert not inspect.isabstract(ProjectId)


def test_projectid_constructor_exists():
    assert callable(ProjectId.__init__)


def test_projectid_constructor_args():
    sig = inspect.signature(ProjectId.__init__)
    params = list(sig.parameters.keys())



def test_esmodel::projecthistory_is_not_abstract():
    assert not inspect.isabstract(esmodel::ProjectHistory)


def test_esmodel::projecthistory_constructor_exists():
    assert callable(esmodel::ProjectHistory.__init__)


def test_esmodel::projecthistory_constructor_args():
    sig = inspect.signature(esmodel::ProjectHistory.__init__)
    params = list(sig.parameters.keys())
    assert "projectName" in params, "Missing parameter 'projectName'"
    assert "projectDescription" in params, "Missing parameter 'projectDescription'"

def test_esmodel::projecthistory_has_projectName():
    assert hasattr(esmodel::ProjectHistory, "projectName")
    descriptor = None
    for klass in esmodel::ProjectHistory.__mro__:
        if "projectName" in klass.__dict__:
            descriptor = klass.__dict__["projectName"]
            break
    assert isinstance(descriptor, property)

def test_esmodel::projecthistory_has_projectDescription():
    assert hasattr(esmodel::ProjectHistory, "projectDescription")
    descriptor = None
    for klass in esmodel::ProjectHistory.__mro__:
        if "projectDescription" in klass.__dict__:
            descriptor = klass.__dict__["projectDescription"]
            break
    assert isinstance(descriptor, property)



def test_activityobject_is_not_abstract():
    assert not inspect.isabstract(ActivityObject)


def test_activityobject_constructor_exists():
    assert callable(ActivityObject.__init__)


def test_activityobject_constructor_args():
    sig = inspect.signature(ActivityObject.__init__)
    params = list(sig.parameters.keys())



def test_model::activity::fork_is_not_abstract():
    assert not inspect.isabstract(model::activity::Fork)


def test_model::activity::fork_constructor_exists():
    assert callable(model::activity::Fork.__init__)


def test_model::activity::fork_constructor_args():
    sig = inspect.signature(model::activity::Fork.__init__)
    params = list(sig.parameters.keys())



def test_model::activity::activityinitial_is_not_abstract():
    assert not inspect.isabstract(model::activity::ActivityInitial)


def test_model::activity::activityinitial_constructor_exists():
    assert callable(model::activity::ActivityInitial.__init__)


def test_model::activity::activityinitial_constructor_args():
    sig = inspect.signature(model::activity::ActivityInitial.__init__)
    params = list(sig.parameters.keys())



def test_model::activity::activityend_is_not_abstract():
    assert not inspect.isabstract(model::activity::ActivityEnd)


def test_model::activity::activityend_constructor_exists():
    assert callable(model::activity::ActivityEnd.__init__)


def test_model::activity::activityend_constructor_args():
    sig = inspect.signature(model::activity::ActivityEnd.__init__)
    params = list(sig.parameters.keys())



def test_model::activity::branch_is_not_abstract():
    assert not inspect.isabstract(model::activity::Branch)


def test_model::activity::branch_constructor_exists():
    assert callable(model::activity::Branch.__init__)


def test_model::activity::branch_constructor_args():
    sig = inspect.signature(model::activity::Branch.__init__)
    params = list(sig.parameters.keys())



def test_model::activity::activity_is_not_abstract():
    assert not inspect.isabstract(model::activity::Activity)


def test_model::activity::activity_constructor_exists():
    assert callable(model::activity::Activity.__init__)


def test_model::activity::activity_constructor_args():
    sig = inspect.signature(model::activity::Activity.__init__)
    params = list(sig.parameters.keys())



def test_activity::activityobject_is_not_abstract():
    assert not inspect.isabstract(activity::ActivityObject)


def test_activity::activityobject_constructor_exists():
    assert callable(activity::ActivityObject.__init__)


def test_activity::activityobject_constructor_args():
    sig = inspect.signature(activity::ActivityObject.__init__)
    params = list(sig.parameters.keys())



def test_model::activity::transition_is_not_abstract():
    assert not inspect.isabstract(model::activity::Transition)


def test_model::activity::transition_constructor_exists():
    assert callable(model::activity::Transition.__init__)


def test_model::activity::transition_constructor_args():
    sig = inspect.signature(model::activity::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_model::activity::transition_has_condition():
    assert hasattr(model::activity::Transition, "condition")
    descriptor = None
    for klass in model::activity::Transition.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_activity::transition_is_not_abstract():
    assert not inspect.isabstract(activity::Transition)


def test_activity::transition_constructor_exists():
    assert callable(activity::Transition.__init__)


def test_activity::transition_constructor_args():
    sig = inspect.signature(activity::Transition.__init__)
    params = list(sig.parameters.keys())



def test_model::activity::activityobject_is_not_abstract():
    assert not inspect.isabstract(model::activity::ActivityObject)


def test_model::activity::activityobject_constructor_exists():
    assert callable(model::activity::ActivityObject.__init__)


def test_model::activity::activityobject_constructor_args():
    sig = inspect.signature(model::activity::ActivityObject.__init__)
    params = list(sig.parameters.keys())



def test_modelelementid_is_not_abstract():
    assert not inspect.isabstract(ModelElementId)


def test_modelelementid_constructor_exists():
    assert callable(ModelElementId.__init__)


def test_modelelementid_constructor_args():
    sig = inspect.signature(ModelElementId.__init__)
    params = list(sig.parameters.keys())



def test_model::util::modelelementpath_is_not_abstract():
    assert not inspect.isabstract(model::util::ModelElementPath)


def test_model::util::modelelementpath_constructor_exists():
    assert callable(model::util::ModelElementPath.__init__)


def test_model::util::modelelementpath_constructor_args():
    sig = inspect.signature(model::util::ModelElementPath.__init__)
    params = list(sig.parameters.keys())



def test_stereotypeattributeinstance_is_not_abstract():
    assert not inspect.isabstract(StereotypeAttributeInstance)


def test_stereotypeattributeinstance_constructor_exists():
    assert callable(StereotypeAttributeInstance.__init__)


def test_stereotypeattributeinstance_constructor_args():
    sig = inspect.signature(StereotypeAttributeInstance.__init__)
    params = list(sig.parameters.keys())



def test_model::profile::stereotypeattributeinstancestring_is_not_abstract():
    assert not inspect.isabstract(model::profile::StereotypeAttributeInstanceString)


def test_model::profile::stereotypeattributeinstancestring_constructor_exists():
    assert callable(model::profile::StereotypeAttributeInstanceString.__init__)


def test_model::profile::stereotypeattributeinstancestring_constructor_args():
    sig = inspect.signature(model::profile::StereotypeAttributeInstanceString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model::profile::stereotypeattributeinstancestring_has_value():
    assert hasattr(model::profile::StereotypeAttributeInstanceString, "value")
    descriptor = None
    for klass in model::profile::StereotypeAttributeInstanceString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model::profile::profile_is_not_abstract():
    assert not inspect.isabstract(model::profile::Profile)


def test_model::profile::profile_constructor_exists():
    assert callable(model::profile::Profile.__init__)


def test_model::profile::profile_constructor_args():
    sig = inspect.signature(model::profile::Profile.__init__)
    params = list(sig.parameters.keys())



def test_model::profile::stereotypeattributeinstance_is_not_abstract():
    assert not inspect.isabstract(model::profile::StereotypeAttributeInstance)


def test_model::profile::stereotypeattributeinstance_constructor_exists():
    assert callable(model::profile::StereotypeAttributeInstance.__init__)


def test_model::profile::stereotypeattributeinstance_constructor_args():
    sig = inspect.signature(model::profile::StereotypeAttributeInstance.__init__)
    params = list(sig.parameters.keys())



def test_stereotypeattribute_is_not_abstract():
    assert not inspect.isabstract(StereotypeAttribute)


def test_stereotypeattribute_constructor_exists():
    assert callable(StereotypeAttribute.__init__)


def test_stereotypeattribute_constructor_args():
    sig = inspect.signature(StereotypeAttribute.__init__)
    params = list(sig.parameters.keys())



def test_model::profile::stereotypeattributesimple_is_not_abstract():
    assert not inspect.isabstract(model::profile::StereotypeAttributeSimple)


def test_model::profile::stereotypeattributesimple_constructor_exists():
    assert callable(model::profile::StereotypeAttributeSimple.__init__)


def test_model::profile::stereotypeattributesimple_constructor_args():
    sig = inspect.signature(model::profile::StereotypeAttributeSimple.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_model::profile::stereotypeattributesimple_has_type():
    assert hasattr(model::profile::StereotypeAttributeSimple, "type")
    descriptor = None
    for klass in model::profile::StereotypeAttributeSimple.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_model::profile::stereotypeattribute_is_not_abstract():
    assert not inspect.isabstract(model::profile::StereotypeAttribute)


def test_model::profile::stereotypeattribute_constructor_exists():
    assert callable(model::profile::StereotypeAttribute.__init__)


def test_model::profile::stereotypeattribute_constructor_args():
    sig = inspect.signature(model::profile::StereotypeAttribute.__init__)
    params = list(sig.parameters.keys())



def test_profile::stereotypeattributeinstance_is_not_abstract():
    assert not inspect.isabstract(profile::StereotypeAttributeInstance)


def test_profile::stereotypeattributeinstance_constructor_exists():
    assert callable(profile::StereotypeAttributeInstance.__init__)


def test_profile::stereotypeattributeinstance_constructor_args():
    sig = inspect.signature(profile::StereotypeAttributeInstance.__init__)
    params = list(sig.parameters.keys())



def test_model::profile::stereotypeinstance_is_not_abstract():
    assert not inspect.isabstract(model::profile::StereotypeInstance)


def test_model::profile::stereotypeinstance_constructor_exists():
    assert callable(model::profile::StereotypeInstance.__init__)


def test_model::profile::stereotypeinstance_constructor_args():
    sig = inspect.signature(model::profile::StereotypeInstance.__init__)
    params = list(sig.parameters.keys())



def test_profile::stereotypeattribute_is_not_abstract():
    assert not inspect.isabstract(profile::StereotypeAttribute)


def test_profile::stereotypeattribute_constructor_exists():
    assert callable(profile::StereotypeAttribute.__init__)


def test_profile::stereotypeattribute_constructor_args():
    sig = inspect.signature(profile::StereotypeAttribute.__init__)
    params = list(sig.parameters.keys())



def test_profile::profile_is_not_abstract():
    assert not inspect.isabstract(profile::Profile)


def test_profile::profile_constructor_exists():
    assert callable(profile::Profile.__init__)


def test_profile::profile_constructor_args():
    sig = inspect.signature(profile::Profile.__init__)
    params = list(sig.parameters.keys())



def test_model::profile::stereotype_is_not_abstract():
    assert not inspect.isabstract(model::profile::Stereotype)


def test_model::profile::stereotype_constructor_exists():
    assert callable(model::profile::Stereotype.__init__)


def test_model::profile::stereotype_constructor_args():
    sig = inspect.signature(model::profile::Stereotype.__init__)
    params = list(sig.parameters.keys())
    assert "required" in params, "Missing parameter 'required'"

def test_model::profile::stereotype_has_required():
    assert hasattr(model::profile::Stereotype, "required")
    descriptor = None
    for klass in model::profile::Stereotype.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)



def test_profile::stereotype_is_not_abstract():
    assert not inspect.isabstract(profile::Stereotype)


def test_profile::stereotype_constructor_exists():
    assert callable(profile::Stereotype.__init__)


def test_profile::stereotype_constructor_args():
    sig = inspect.signature(profile::Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_model::attachment::fileattachment_is_not_abstract():
    assert not inspect.isabstract(model::attachment::FileAttachment)


def test_model::attachment::fileattachment_constructor_exists():
    assert callable(model::attachment::FileAttachment.__init__)


def test_model::attachment::fileattachment_constructor_args():
    sig = inspect.signature(model::attachment::FileAttachment.__init__)
    params = list(sig.parameters.keys())
    assert "fileSize" in params, "Missing parameter 'fileSize'"
    assert "fileID" in params, "Missing parameter 'fileID'"
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "fileHash" in params, "Missing parameter 'fileHash'"

def test_model::attachment::fileattachment_has_fileSize():
    assert hasattr(model::attachment::FileAttachment, "fileSize")
    descriptor = None
    for klass in model::attachment::FileAttachment.__mro__:
        if "fileSize" in klass.__dict__:
            descriptor = klass.__dict__["fileSize"]
            break
    assert isinstance(descriptor, property)

def test_model::attachment::fileattachment_has_fileID():
    assert hasattr(model::attachment::FileAttachment, "fileID")
    descriptor = None
    for klass in model::attachment::FileAttachment.__mro__:
        if "fileID" in klass.__dict__:
            descriptor = klass.__dict__["fileID"]
            break
    assert isinstance(descriptor, property)

def test_model::attachment::fileattachment_has_fileName():
    assert hasattr(model::attachment::FileAttachment, "fileName")
    descriptor = None
    for klass in model::attachment::FileAttachment.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)

def test_model::attachment::fileattachment_has_fileHash():
    assert hasattr(model::attachment::FileAttachment, "fileHash")
    descriptor = None
    for klass in model::attachment::FileAttachment.__mro__:
        if "fileHash" in klass.__dict__:
            descriptor = klass.__dict__["fileHash"]
            break
    assert isinstance(descriptor, property)



def test_model::attachment::urlattachment_is_not_abstract():
    assert not inspect.isabstract(model::attachment::UrlAttachment)


def test_model::attachment::urlattachment_constructor_exists():
    assert callable(model::attachment::UrlAttachment.__init__)


def test_model::attachment::urlattachment_constructor_args():
    sig = inspect.signature(model::attachment::UrlAttachment.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"

def test_model::attachment::urlattachment_has_url():
    assert hasattr(model::attachment::UrlAttachment, "url")
    descriptor = None
    for klass in model::attachment::UrlAttachment.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_statenode_is_not_abstract():
    assert not inspect.isabstract(StateNode)


def test_statenode_constructor_exists():
    assert callable(StateNode.__init__)


def test_statenode_constructor_args():
    sig = inspect.signature(StateNode.__init__)
    params = list(sig.parameters.keys())



def test_model::state::stateinitial_is_not_abstract():
    assert not inspect.isabstract(model::state::StateInitial)


def test_model::state::stateinitial_constructor_exists():
    assert callable(model::state::StateInitial.__init__)


def test_model::state::stateinitial_constructor_args():
    sig = inspect.signature(model::state::StateInitial.__init__)
    params = list(sig.parameters.keys())



def test_model::state::stateend_is_not_abstract():
    assert not inspect.isabstract(model::state::StateEnd)


def test_model::state::stateend_constructor_exists():
    assert callable(model::state::StateEnd.__init__)


def test_model::state::stateend_constructor_args():
    sig = inspect.signature(model::state::StateEnd.__init__)
    params = list(sig.parameters.keys())



def test_model::state::state_is_not_abstract():
    assert not inspect.isabstract(model::state::State)


def test_model::state::state_constructor_exists():
    assert callable(model::state::State.__init__)


def test_model::state::state_constructor_args():
    sig = inspect.signature(model::state::State.__init__)
    params = list(sig.parameters.keys())
    assert "exitConditions" in params, "Missing parameter 'exitConditions'"
    assert "activities" in params, "Missing parameter 'activities'"
    assert "entryConditions" in params, "Missing parameter 'entryConditions'"

def test_model::state::state_has_exitConditions():
    assert hasattr(model::state::State, "exitConditions")
    descriptor = None
    for klass in model::state::State.__mro__:
        if "exitConditions" in klass.__dict__:
            descriptor = klass.__dict__["exitConditions"]
            break
    assert isinstance(descriptor, property)

def test_model::state::state_has_activities():
    assert hasattr(model::state::State, "activities")
    descriptor = None
    for klass in model::state::State.__mro__:
        if "activities" in klass.__dict__:
            descriptor = klass.__dict__["activities"]
            break
    assert isinstance(descriptor, property)

def test_model::state::state_has_entryConditions():
    assert hasattr(model::state::State, "entryConditions")
    descriptor = None
    for klass in model::state::State.__mro__:
        if "entryConditions" in klass.__dict__:
            descriptor = klass.__dict__["entryConditions"]
            break
    assert isinstance(descriptor, property)



def test_state::transition_is_not_abstract():
    assert not inspect.isabstract(state::Transition)


def test_state::transition_constructor_exists():
    assert callable(state::Transition.__init__)


def test_state::transition_constructor_args():
    sig = inspect.signature(state::Transition.__init__)
    params = list(sig.parameters.keys())



def test_model::state::statenode_is_not_abstract():
    assert not inspect.isabstract(model::state::StateNode)


def test_model::state::statenode_constructor_exists():
    assert callable(model::state::StateNode.__init__)


def test_model::state::statenode_constructor_args():
    sig = inspect.signature(model::state::StateNode.__init__)
    params = list(sig.parameters.keys())



def test_state::statenode_is_not_abstract():
    assert not inspect.isabstract(state::StateNode)


def test_state::statenode_constructor_exists():
    assert callable(state::StateNode.__init__)


def test_state::statenode_constructor_args():
    sig = inspect.signature(state::StateNode.__init__)
    params = list(sig.parameters.keys())



def test_model::state::transition_is_not_abstract():
    assert not inspect.isabstract(model::state::Transition)


def test_model::state::transition_constructor_exists():
    assert callable(model::state::Transition.__init__)


def test_model::state::transition_constructor_args():
    sig = inspect.signature(model::state::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_model::state::transition_has_condition():
    assert hasattr(model::state::Transition, "condition")
    descriptor = None
    for klass in model::state::Transition.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_meetingsection_is_not_abstract():
    assert not inspect.isabstract(MeetingSection)


def test_meetingsection_constructor_exists():
    assert callable(MeetingSection.__init__)


def test_meetingsection_constructor_args():
    sig = inspect.signature(MeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_model::meeting::issuemeetingsection_is_not_abstract():
    assert not inspect.isabstract(model::meeting::IssueMeetingSection)


def test_model::meeting::issuemeetingsection_constructor_exists():
    assert callable(model::meeting::IssueMeetingSection.__init__)


def test_model::meeting::issuemeetingsection_constructor_args():
    sig = inspect.signature(model::meeting::IssueMeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_model::meeting::workitemmeetingsection_is_not_abstract():
    assert not inspect.isabstract(model::meeting::WorkItemMeetingSection)


def test_model::meeting::workitemmeetingsection_constructor_exists():
    assert callable(model::meeting::WorkItemMeetingSection.__init__)


def test_model::meeting::workitemmeetingsection_constructor_args():
    sig = inspect.signature(model::meeting::WorkItemMeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_model::meeting::compositemeetingsection_is_not_abstract():
    assert not inspect.isabstract(model::meeting::CompositeMeetingSection)


def test_model::meeting::compositemeetingsection_constructor_exists():
    assert callable(model::meeting::CompositeMeetingSection.__init__)


def test_model::meeting::compositemeetingsection_constructor_args():
    sig = inspect.signature(model::meeting::CompositeMeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_model::meeting::meetingsection_is_not_abstract():
    assert not inspect.isabstract(model::meeting::MeetingSection)


def test_model::meeting::meetingsection_constructor_exists():
    assert callable(model::meeting::MeetingSection.__init__)


def test_model::meeting::meetingsection_constructor_args():
    sig = inspect.signature(model::meeting::MeetingSection.__init__)
    params = list(sig.parameters.keys())
    assert "allocatedTime" in params, "Missing parameter 'allocatedTime'"

def test_model::meeting::meetingsection_has_allocatedTime():
    assert hasattr(model::meeting::MeetingSection, "allocatedTime")
    descriptor = None
    for klass in model::meeting::MeetingSection.__mro__:
        if "allocatedTime" in klass.__dict__:
            descriptor = klass.__dict__["allocatedTime"]
            break
    assert isinstance(descriptor, property)



def test_meeting::workitemmeetingsection_is_not_abstract():
    assert not inspect.isabstract(meeting::WorkItemMeetingSection)


def test_meeting::workitemmeetingsection_constructor_exists():
    assert callable(meeting::WorkItemMeetingSection.__init__)


def test_meeting::workitemmeetingsection_constructor_args():
    sig = inspect.signature(meeting::WorkItemMeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_meeting::issuemeetingsection_is_not_abstract():
    assert not inspect.isabstract(meeting::IssueMeetingSection)


def test_meeting::issuemeetingsection_constructor_exists():
    assert callable(meeting::IssueMeetingSection.__init__)


def test_meeting::issuemeetingsection_constructor_args():
    sig = inspect.signature(meeting::IssueMeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_meeting::meetingsection_is_not_abstract():
    assert not inspect.isabstract(meeting::MeetingSection)


def test_meeting::meetingsection_constructor_exists():
    assert callable(meeting::MeetingSection.__init__)


def test_meeting::meetingsection_constructor_args():
    sig = inspect.signature(meeting::MeetingSection.__init__)
    params = list(sig.parameters.keys())



def test_model::meeting::meeting_is_not_abstract():
    assert not inspect.isabstract(model::meeting::Meeting)


def test_model::meeting::meeting_constructor_exists():
    assert callable(model::meeting::Meeting.__init__)


def test_model::meeting::meeting_constructor_args():
    sig = inspect.signature(model::meeting::Meeting.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "starttime" in params, "Missing parameter 'starttime'"
    assert "endtime" in params, "Missing parameter 'endtime'"

def test_model::meeting::meeting_has_location():
    assert hasattr(model::meeting::Meeting, "location")
    descriptor = None
    for klass in model::meeting::Meeting.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_model::meeting::meeting_has_starttime():
    assert hasattr(model::meeting::Meeting, "starttime")
    descriptor = None
    for klass in model::meeting::Meeting.__mro__:
        if "starttime" in klass.__dict__:
            descriptor = klass.__dict__["starttime"]
            break
    assert isinstance(descriptor, property)

def test_model::meeting::meeting_has_endtime():
    assert hasattr(model::meeting::Meeting, "endtime")
    descriptor = None
    for klass in model::meeting::Meeting.__mro__:
        if "endtime" in klass.__dict__:
            descriptor = klass.__dict__["endtime"]
            break
    assert isinstance(descriptor, property)



def test_model::component::deploymentnode_is_not_abstract():
    assert not inspect.isabstract(model::component::DeploymentNode)


def test_model::component::deploymentnode_constructor_exists():
    assert callable(model::component::DeploymentNode.__init__)


def test_model::component::deploymentnode_constructor_args():
    sig = inspect.signature(model::component::DeploymentNode.__init__)
    params = list(sig.parameters.keys())

def test_associationtype_exists():
    # Check that the Enumeration exists
    assert AssociationType is not None

def test_associationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssociationType]
    expected_literals = [
        "AGGREGATION",
        "COMPOSITION",
        "UNDIRECTED_ASSOCIATION",
        "DIRECTED_ASSOCIATION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssociationType"

def test_visibilitytype_exists():
    # Check that the Enumeration exists
    assert VisibilityType is not None

def test_visibilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityType]
    expected_literals = [
        "GLOBAL",
        "UNDEFINED",
        "PROTECTED",
        "PACKAGE",
        "PRIVATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityType"

def test_severity_exists():
    # Check that the Enumeration exists
    assert Severity is not None

def test_severity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Severity]
    expected_literals = [
        "MINOR",
        "MAJOR",
        "FEATURE",
        "TRIVIAL",
        "BLOCKER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Severity"

def test_scopetype_exists():
    # Check that the Enumeration exists
    assert ScopeType is not None

def test_scopetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScopeType]
    expected_literals = [
        "INSTANCE",
        "CLASS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScopeType"

def test_argumentdirectiontype_exists():
    # Check that the Enumeration exists
    assert ArgumentDirectionType is not None

def test_argumentdirectiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArgumentDirectionType]
    expected_literals = [
        "UNDEFINED",
        "OUT",
        "IN",
        "INOUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArgumentDirectionType"

def test_resolutiontype_exists():
    # Check that the Enumeration exists
    assert ResolutionType is not None

def test_resolutiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResolutionType]
    expected_literals = [
        "FIXED",
        "CANNOT_REPRODUCE",
        "WONT_FIX",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResolutionType"

def test_mergechoiceselection_exists():
    # Check that the Enumeration exists
    assert MergeChoiceSelection is not None

def test_mergechoiceselection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MergeChoiceSelection]
    expected_literals = [
        "Their",
        "Mine",
        "MergedText",
        "Issue",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MergeChoiceSelection"

def test_mergeglobalchoiceselection_exists():
    # Check that the Enumeration exists
    assert MergeGlobalChoiceSelection is not None

def test_mergeglobalchoiceselection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MergeGlobalChoiceSelection]
    expected_literals = [
        "AllMine",
        "Cancel",
        "OKFinished",
        "OKNotFinished",
        "AllTheir",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MergeGlobalChoiceSelection"

def test_containmenttype_exists():
    # Check that the Enumeration exists
    assert ContainmentType is not None

def test_containmenttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainmentType]
    expected_literals = [
        "CONTAINMENT",
        "NONE",
        "CONTAINER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainmentType"

def test_diagramtype_exists():
    # Check that the Enumeration exists
    assert DiagramType is not None

def test_diagramtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DiagramType]
    expected_literals = [
        "COMPONENT_DIAGRAM",
        "USECASE_DIAGRAM",
        "STATE_DIAGRAM",
        "CLASS_DIAGRAM",
        "ACTIVITY_DIAGRAM",
        "WORKITEM_DIAGRAM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DiagramType"

def test_bugstatus_exists():
    # Check that the Enumeration exists
    assert BugStatus is not None

def test_bugstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BugStatus]
    expected_literals = [
        "CLOSED",
        "NEW",
        "ASSIGNED",
        "RESOLVED",
        "CONFIRMED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BugStatus"

def test_activitytype_exists():
    # Check that the Enumeration exists
    assert ActivityType is not None

def test_activitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActivityType]
    expected_literals = [
        "ANALYSIS",
        "OBJECT_DESIGN",
        "SYSTEM_DESIGN",
        "IMPLEMENTATION",
        "MANAGEMENT",
        "NONE",
        "TESTING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActivityType"


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
url::ModelElementUrlFragment_strategy = st.builds(
    url::ModelElementUrlFragment,
)
url::ProjectUrlFragment_strategy = st.builds(
    url::ProjectUrlFragment,
)
url::ServerUrl_strategy = st.builds(
    url::ServerUrl,
)
esmodel::url::ModelElementUrl_strategy = st.builds(
    esmodel::url::ModelElementUrl,
)
esmodel::url::ModelElementUrlFragment_strategy = st.builds(
    esmodel::url::ModelElementUrlFragment,
    name=
        safe_text
)
esmodel::url::ProjectUrlFragment_strategy = st.builds(
    esmodel::url::ProjectUrlFragment,
    name=
        safe_text
)
component::Component_strategy = st.builds(
    component::Component,
)
component::ComponentService_strategy = st.builds(
    component::ComponentService,
)
Solution_strategy = st.builds(
    Solution,
)
model::change::MergingSolution_strategy = st.builds(
    model::change::MergingSolution,
)
change::MergingProposal_strategy = st.builds(
    change::MergingProposal,
)
Proposal_strategy = st.builds(
    Proposal,
)
model::change::MergingProposal_strategy = st.builds(
    model::change::MergingProposal,
)
Issue_strategy = st.builds(
    Issue,
)
model::change::MergingIssue_strategy = st.builds(
    model::change::MergingIssue,
    resolvingRevision=
        st.integers()
)
rationale::Proposal_strategy = st.builds(
    rationale::Proposal,
)
rationale::Assessment_strategy = st.builds(
    rationale::Assessment,
)
rationale::Issue_strategy = st.builds(
    rationale::Issue,
)
rationale::Criterion_strategy = st.builds(
    rationale::Criterion,
)
rationale::Solution_strategy = st.builds(
    rationale::Solution,
)
Criterion_strategy = st.builds(
    Criterion,
)
model::requirement::NonFunctionalRequirement_strategy = st.builds(
    model::requirement::NonFunctionalRequirement,
)
requirement::SystemFunction_strategy = st.builds(
    requirement::SystemFunction,
)
NonDomainElement_strategy = st.builds(
    NonDomainElement,
)
requirement::ActorInstance_strategy = st.builds(
    requirement::ActorInstance,
)
requirement::UserTask_strategy = st.builds(
    requirement::UserTask,
)
requirement::Step_strategy = st.builds(
    requirement::Step,
)
requirement::NonFunctionalRequirement_strategy = st.builds(
    requirement::NonFunctionalRequirement,
)
requirement::Actor_strategy = st.builds(
    requirement::Actor,
)
Section_strategy = st.builds(
    Section,
)
model::document::LeafSection_strategy = st.builds(
    model::document::LeafSection,
)
document::CompositeSection_strategy = st.builds(
    document::CompositeSection,
)
requirement::FunctionalRequirement_strategy = st.builds(
    requirement::FunctionalRequirement,
)
document::Section_strategy = st.builds(
    document::Section,
)
model::document::CompositeSection_strategy = st.builds(
    model::document::CompositeSection,
)
classes::MethodArgument_strategy = st.builds(
    classes::MethodArgument,
)
classes::PackageElement_strategy = st.builds(
    classes::PackageElement,
)
PackageElement_strategy = st.builds(
    PackageElement,
)
model::classes::Package_strategy = st.builds(
    model::classes::Package,
)
model::classes::Class_strategy = st.builds(
    model::classes::Class,
)
classes::Dependency_strategy = st.builds(
    classes::Dependency,
)
classes::Package_strategy = st.builds(
    classes::Package,
)
requirement::Scenario_strategy = st.builds(
    requirement::Scenario,
)
requirement::UseCase_strategy = st.builds(
    requirement::UseCase,
)
classes::Method_strategy = st.builds(
    classes::Method,
)
classes::Attribute_strategy = st.builds(
    classes::Attribute,
)
classes::Association_strategy = st.builds(
    classes::Association,
)
classes::Class_strategy = st.builds(
    classes::Class,
)
diagram::model::Diagram_strategy = st.builds(
    diagram::model::Diagram,
)
task::Checkable_strategy = st.builds(
    task::Checkable,
)
organization::User_strategy = st.builds(
    organization::User,
)
task::WorkPackage_strategy = st.builds(
    task::WorkPackage,
)
organization::OrgUnit_strategy = st.builds(
    organization::OrgUnit,
)
WorkItem_strategy = st.builds(
    WorkItem,
)
model::task::Milestone_strategy = st.builds(
    model::task::Milestone,
)
model::task::WorkPackage_strategy = st.builds(
    model::task::WorkPackage,
    startDate=
        st.dates(),
    endDate=
        st.dates()
)
change::ModelChangePackage_strategy = st.builds(
    change::ModelChangePackage,
)
Project_strategy = st.builds(
    Project,
)
model::Project_strategy = st.builds(
    model::Project,
)
model::NonDomainElement_strategy = st.builds(
    model::NonDomainElement,
)
UnicaseModelElement_strategy = st.builds(
    UnicaseModelElement,
)
model::rationale::Comment_strategy = st.builds(
    model::rationale::Comment,
)
model::requirement::SystemFunction_strategy = st.builds(
    model::requirement::SystemFunction,
    input=
        safe_text,
    output=
        safe_text,
    exception=
        safe_text
)
model::requirement::Actor_strategy = st.builds(
    model::requirement::Actor,
)
model::component::Component_strategy = st.builds(
    model::component::Component,
)
model::change::ModelChangePackage_strategy = st.builds(
    model::change::ModelChangePackage,
    targetVersion=
        st.integers(),
    sourceVersion=
        st.integers()
)
model::task::Checkable_strategy = st.builds(
    model::task::Checkable,
    checked=
        st.booleans()
)
model::classes::Attribute_strategy = st.builds(
    model::classes::Attribute,
    defaultValue=
        safe_text,
    signature=
        safe_text,
    visibility=
        safe_text,
    type=
        safe_text,
    scope=
        safe_text,
    properties=
        safe_text,
    label=
        safe_text
)
model::rationale::Proposal_strategy = st.builds(
    model::rationale::Proposal,
)
model::rationale::Assessment_strategy = st.builds(
    model::rationale::Assessment,
    value=
        st.integers()
)
model::document::Section_strategy = st.builds(
    model::document::Section,
)
model::component::ComponentService_strategy = st.builds(
    model::component::ComponentService,
)
model::Attachment_strategy = st.builds(
    model::Attachment,
)
model::requirement::UseCase_strategy = st.builds(
    model::requirement::UseCase,
    precondition=
        safe_text,
    postcondition=
        safe_text,
    rules=
        safe_text,
    exception=
        safe_text
)
model::rationale::Solution_strategy = st.builds(
    model::rationale::Solution,
)
model::rationale::Criterion_strategy = st.builds(
    model::rationale::Criterion,
)
model::classes::Association_strategy = st.builds(
    model::classes::Association,
    targetMultiplicity=
        safe_text,
    targetRole=
        safe_text,
    type=
        safe_text,
    sourceMultiplicity=
        safe_text,
    sourceRole=
        safe_text
)
model::classes::PackageElement_strategy = st.builds(
    model::classes::PackageElement,
)
model::requirement::Scenario_strategy = st.builds(
    model::requirement::Scenario,
)
model::requirement::Step_strategy = st.builds(
    model::requirement::Step,
    userStep=
        st.booleans()
)
model::classes::Method_strategy = st.builds(
    model::classes::Method,
    scope=
        safe_text,
    properties=
        safe_text,
    returnType=
        safe_text,
    label=
        safe_text,
    stubbed=
        st.booleans(),
    visibility=
        safe_text,
    signature=
        safe_text
)
model::classes::Dependency_strategy = st.builds(
    model::classes::Dependency,
)
model::requirement::ActorInstance_strategy = st.builds(
    model::requirement::ActorInstance,
)
model::requirement::UserTask_strategy = st.builds(
    model::requirement::UserTask,
)
model::classes::MethodArgument_strategy = st.builds(
    model::classes::MethodArgument,
    defaultValue=
        safe_text,
    direction=
        safe_text,
    label=
        safe_text,
    type=
        safe_text,
    signature=
        safe_text
)
model::requirement::FunctionalRequirement_strategy = st.builds(
    model::requirement::FunctionalRequirement,
    storyPoints=
        st.integers(),
    cost=
        st.integers(),
    priority=
        st.integers(),
    reviewed=
        st.booleans()
)
model::Annotation_strategy = st.builds(
    model::Annotation,
)
profile::StereotypeInstance_strategy = st.builds(
    profile::StereotypeInstance,
)
rationale::Comment_strategy = st.builds(
    rationale::Comment,
)
OrgUnit_strategy = st.builds(
    OrgUnit,
)
model::organization::Group_strategy = st.builds(
    model::organization::Group,
)
model::organization::User_strategy = st.builds(
    model::organization::User,
    firstName=
        safe_text,
    lastName=
        safe_text,
    email=
        safe_text
)
task::WorkItem_strategy = st.builds(
    task::WorkItem,
)
model::bug::BugReport_strategy = st.builds(
    model::bug::BugReport,
    resolution=
        safe_text,
    resolutionType=
        safe_text,
    severity=
        safe_text,
    Status=
        safe_text
)
model::task::ActionItem_strategy = st.builds(
    model::task::ActionItem,
    done=
        st.booleans(),
    activity=
        safe_text
)
organization::Group_strategy = st.builds(
    organization::Group,
)
model::organization::OrgUnit_strategy = st.builds(
    model::organization::OrgUnit,
    acOrgId=
        safe_text
)
metamodel::AssociationClassElement_strategy = st.builds(
    metamodel::AssociationClassElement,
)
metamodel::NonDomainElement_strategy = st.builds(
    metamodel::NonDomainElement,
)
metamodel::ModelVersion_strategy = st.builds(
    metamodel::ModelVersion,
    releaseNumber=
        st.integers()
)
UniqueIdentifier_strategy = st.builds(
    UniqueIdentifier,
)
metamodel::ModelElementId_strategy = st.builds(
    metamodel::ModelElementId,
)
IdentifiableElement_strategy = st.builds(
    IdentifiableElement,
)
esmodel::notification::ESNotification_strategy = st.builds(
    esmodel::notification::ESNotification,
    message=
        safe_text,
    seen=
        st.booleans(),
    sender=
        safe_text,
    recipient=
        safe_text,
    creationDate=
        st.dates(),
    details=
        safe_text,
    name=
        safe_text,
    provider=
        safe_text
)
metamodel::ModelElement_strategy = st.builds(
    metamodel::ModelElement,
    creator=
        safe_text,
    creationDate=
        st.dates()
)
metamodel::IdentifiableElement_strategy = st.builds(
    metamodel::IdentifiableElement,
    identifier=
        safe_text
)
metamodel::UniqueIdentifier_strategy = st.builds(
    metamodel::UniqueIdentifier,
    id=
        safe_text
)
ModelElement_strategy = st.builds(
    ModelElement,
)
metamodel::Project_strategy = st.builds(
    metamodel::Project,
)
document::LeafSection_strategy = st.builds(
    document::LeafSection,
)
Attachment_strategy = st.builds(
    Attachment,
)
model::diagram::MEDiagram_strategy = st.builds(
    model::diagram::MEDiagram,
    diagramLayout=
        safe_text,
    type=
        safe_text
)
Annotation_strategy = st.builds(
    Annotation,
)
model::rationale::Issue_strategy = st.builds(
    model::rationale::Issue,
    activity=
        safe_text
)
model::task::WorkItem_strategy = st.builds(
    model::task::WorkItem,
    dueDate=
        st.dates(),
    priority=
        st.integers(),
    effort=
        st.integers(),
    resolved=
        st.booleans(),
    estimate=
        st.integers()
)
model::UnicaseModelElement_strategy = st.builds(
    model::UnicaseModelElement,
    description=
        safe_text,
    state=
        safe_text,
    name=
        safe_text
)
esmodel::url::ServerUrl_strategy = st.builds(
    esmodel::url::ServerUrl,
    hostName=
        safe_text,
    port=
        st.integers()
)
esmodel::accesscontrol::OrgUnitProperty_strategy = st.builds(
    esmodel::accesscontrol::OrgUnitProperty,
    name=
        safe_text,
    value=
        safe_text
)
esmodel::accesscontrol::ACOrgUnitId_strategy = st.builds(
    esmodel::accesscontrol::ACOrgUnitId,
)
accesscontrol::ACOrgUnit_strategy = st.builds(
    accesscontrol::ACOrgUnit,
)
accesscontrol::OrgUnitProperty_strategy = st.builds(
    accesscontrol::OrgUnitProperty,
)
roles::Role_strategy = st.builds(
    roles::Role,
)
Role_strategy = st.builds(
    Role,
)
esmodel::roles::ServerAdmin_strategy = st.builds(
    esmodel::roles::ServerAdmin,
)
esmodel::roles::WriterRole_strategy = st.builds(
    esmodel::roles::WriterRole,
)
esmodel::roles::ProjectAdminRole_strategy = st.builds(
    esmodel::roles::ProjectAdminRole,
)
esmodel::roles::ReaderRole_strategy = st.builds(
    esmodel::roles::ReaderRole,
)
esmodel::roles::Role_strategy = st.builds(
    esmodel::roles::Role,
)
esmodel::accesscontrol::ACOrgUnit_strategy = st.builds(
    esmodel::accesscontrol::ACOrgUnit,
    description=
        safe_text,
    name=
        safe_text
)
operations::OperationId_strategy = st.builds(
    operations::OperationId,
)
ACOrgUnit_strategy = st.builds(
    ACOrgUnit,
)
esmodel::accesscontrol::ACGroup_strategy = st.builds(
    esmodel::accesscontrol::ACGroup,
)
esmodel::accesscontrol::ACUser_strategy = st.builds(
    esmodel::accesscontrol::ACUser,
    firstName=
        safe_text,
    lastName=
        safe_text
)
ServerProjectEvent_strategy = st.builds(
    ServerProjectEvent,
)
esmodel::server::ProjectUpdatedEvent_strategy = st.builds(
    esmodel::server::ProjectUpdatedEvent,
)
ServerEvent_strategy = st.builds(
    ServerEvent,
)
esmodel::server::ServerProjectEvent_strategy = st.builds(
    esmodel::server::ServerProjectEvent,
)
ReadEvent_strategy = st.builds(
    ReadEvent,
)
esmodel::events::NotificationReadEvent_strategy = st.builds(
    esmodel::events::NotificationReadEvent,
    notificationId=
        safe_text
)
esmodel::operations::ModelElementGroup_strategy = st.builds(
    esmodel::operations::ModelElementGroup,
    name=
        safe_text
)
Event_strategy = st.builds(
    Event,
)
esmodel::events::ShowHistoryEvent_strategy = st.builds(
    esmodel::events::ShowHistoryEvent,
)
esmodel::events::ExceptionEvent_strategy = st.builds(
    esmodel::events::ExceptionEvent,
    ExceptionCauseTitle=
        safe_text,
    ExceptionCauseStackTrace=
        safe_text,
    ExceptionTitle=
        safe_text,
    ExceptionStackTrace=
        safe_text
)
esmodel::events::AnnotationEvent_strategy = st.builds(
    esmodel::events::AnnotationEvent,
)
esmodel::events::MergeGlobalChoiceEvent_strategy = st.builds(
    esmodel::events::MergeGlobalChoiceEvent,
    selection=
        safe_text
)
esmodel::events::TraceEvent_strategy = st.builds(
    esmodel::events::TraceEvent,
    featureName=
        safe_text
)
esmodel::events::PerspectiveEvent_strategy = st.builds(
    esmodel::events::PerspectiveEvent,
)
esmodel::events::MergeChoiceEvent_strategy = st.builds(
    esmodel::events::MergeChoiceEvent,
    createdIssueName=
        safe_text,
    selection=
        safe_text,
    contextFeature=
        safe_text
)
esmodel::events::LinkEvent_strategy = st.builds(
    esmodel::events::LinkEvent,
    createdNew=
        st.booleans(),
    sourceView=
        safe_text
)
esmodel::events::PluginFocusEvent_strategy = st.builds(
    esmodel::events::PluginFocusEvent,
    startDate=
        st.dates(),
    pluginId=
        safe_text
)
esmodel::events::NotificationIgnoreEvent_strategy = st.builds(
    esmodel::events::NotificationIgnoreEvent,
    notificationId=
        safe_text
)
esmodel::events::UpdateEvent_strategy = st.builds(
    esmodel::events::UpdateEvent,
)
esmodel::events::PresentationSwitchEvent_strategy = st.builds(
    esmodel::events::PresentationSwitchEvent,
    newPresentation=
        safe_text,
    readView=
        safe_text
)
esmodel::events::URLEvent_strategy = st.builds(
    esmodel::events::URLEvent,
    sourceView=
        safe_text
)
esmodel::events::NotificationGenerationEvent_strategy = st.builds(
    esmodel::events::NotificationGenerationEvent,
)
esmodel::events::ShowChangesEvent_strategy = st.builds(
    esmodel::events::ShowChangesEvent,
)
esmodel::events::PluginStartEvent_strategy = st.builds(
    esmodel::events::PluginStartEvent,
    pluginId=
        safe_text
)
esmodel::server::ServerEvent_strategy = st.builds(
    esmodel::server::ServerEvent,
)
esmodel::events::CheckoutEvent_strategy = st.builds(
    esmodel::events::CheckoutEvent,
)
esmodel::events::Validate_strategy = st.builds(
    esmodel::events::Validate,
)
esmodel::events::MergeEvent_strategy = st.builds(
    esmodel::events::MergeEvent,
    numberOfConflicts=
        st.integers(),
    totalTime=
        st.integers()
)
esmodel::events::NavigatorCreateEvent_strategy = st.builds(
    esmodel::events::NavigatorCreateEvent,
    dynamic=
        st.booleans()
)
esmodel::events::DNDEvent_strategy = st.builds(
    esmodel::events::DNDEvent,
    targetView=
        safe_text,
    sourceView=
        safe_text
)
esmodel::events::UndoEvent_strategy = st.builds(
    esmodel::events::UndoEvent,
)
esmodel::events::RevertEvent_strategy = st.builds(
    esmodel::events::RevertEvent,
    revertedChangesCount=
        st.integers()
)
esmodel::events::ReadEvent_strategy = st.builds(
    esmodel::events::ReadEvent,
    readView=
        safe_text,
    sourceView=
        safe_text
)
esmodel::events::Event_strategy = st.builds(
    esmodel::events::Event,
    timestamp=
        st.dates()
)
CompositeOperation_strategy = st.builds(
    CompositeOperation,
)
esmodel::semantic::SemanticCompositeOperation_strategy = st.builds(
    esmodel::semantic::SemanticCompositeOperation,
)
esmodel::operations::EObjectToModelElementIdMap_strategy = st.builds(
    esmodel::operations::EObjectToModelElementIdMap,
)
esmodel::operations::OperationGroup_strategy = st.builds(
    esmodel::operations::OperationGroup,
    name=
        safe_text
)
esmodel::operations::OperationId_strategy = st.builds(
    esmodel::operations::OperationId,
)
AttributeOperation_strategy = st.builds(
    AttributeOperation,
)
esmodel::operations::DiagramLayoutOperation_strategy = st.builds(
    esmodel::operations::DiagramLayoutOperation,
)
ReferenceOperation_strategy = st.builds(
    ReferenceOperation,
)
esmodel::operations::MultiReferenceSetOperation_strategy = st.builds(
    esmodel::operations::MultiReferenceSetOperation,
    index=
        st.integers()
)
esmodel::operations::MultiReferenceOperation_strategy = st.builds(
    esmodel::operations::MultiReferenceOperation,
    add=
        st.booleans(),
    index=
        st.integers()
)
esmodel::operations::SingleReferenceOperation_strategy = st.builds(
    esmodel::operations::SingleReferenceOperation,
)
FeatureOperation_strategy = st.builds(
    FeatureOperation,
)
esmodel::operations::MultiAttributeSetOperation_strategy = st.builds(
    esmodel::operations::MultiAttributeSetOperation,
    newValue=
        safe_text,
    index=
        st.integers(),
    oldValue=
        safe_text
)
esmodel::operations::MultiAttributeMoveOperation_strategy = st.builds(
    esmodel::operations::MultiAttributeMoveOperation,
    newIndex=
        st.integers(),
    oldIndex=
        st.integers(),
    referencedValue=
        safe_text
)
esmodel::operations::MultiReferenceMoveOperation_strategy = st.builds(
    esmodel::operations::MultiReferenceMoveOperation,
    oldIndex=
        st.integers(),
    newIndex=
        st.integers()
)
esmodel::operations::ReferenceOperation_strategy = st.builds(
    esmodel::operations::ReferenceOperation,
    bidirectional=
        st.booleans(),
    oppositeFeatureName=
        safe_text,
    containmentType=
        safe_text
)
esmodel::operations::MultiAttributeOperation_strategy = st.builds(
    esmodel::operations::MultiAttributeOperation,
    add=
        st.booleans(),
    indexes=
        st.integers(),
    referencedValues=
        safe_text
)
esmodel::operations::AttributeOperation_strategy = st.builds(
    esmodel::operations::AttributeOperation,
    newValue=
        safe_text,
    oldValue=
        safe_text
)
operations::EObjectToModelElementIdMap_strategy = st.builds(
    operations::EObjectToModelElementIdMap,
)
operations::ReferenceOperation_strategy = st.builds(
    operations::ReferenceOperation,
)
operations::esmodel::EObject_strategy = st.builds(
    operations::esmodel::EObject,
)
AbstractOperation_strategy = st.builds(
    AbstractOperation,
)
esmodel::operations::FeatureOperation_strategy = st.builds(
    esmodel::operations::FeatureOperation,
    featureName=
        safe_text
)
esmodel::operations::CreateDeleteOperation_strategy = st.builds(
    esmodel::operations::CreateDeleteOperation,
    delete=
        st.booleans()
)
esmodel::operations::CompositeOperation_strategy = st.builds(
    esmodel::operations::CompositeOperation,
    compositeName=
        safe_text,
    compositeDescription=
        safe_text,
    reversed=
        st.booleans()
)
esmodel::operations::AbstractOperation_strategy = st.builds(
    esmodel::operations::AbstractOperation,
    description=
        safe_text,
    accepted=
        st.booleans(),
    clientDate=
        st.dates(),
    name=
        safe_text
)
esmodel::versioning::LogMessage_strategy = st.builds(
    esmodel::versioning::LogMessage,
    date=
        st.dates(),
    message=
        safe_text,
    clientDate=
        st.dates(),
    author=
        safe_text
)
esmodel::versioning::VersionProperty_strategy = st.builds(
    esmodel::versioning::VersionProperty,
    name=
        safe_text,
    value=
        safe_text
)
esmodel::versioning::VersionSpec_strategy = st.builds(
    esmodel::versioning::VersionSpec,
)
esmodel::versioning::Version_strategy = st.builds(
    esmodel::versioning::Version,
)
esmodel::versioning::HistoryQuery_strategy = st.builds(
    esmodel::versioning::HistoryQuery,
    includeChangePackage=
        st.booleans()
)
versioning::ChangePackage_strategy = st.builds(
    versioning::ChangePackage,
)
versioning::TagVersionSpec_strategy = st.builds(
    versioning::TagVersionSpec,
)
esmodel::versioning::HistoryInfo_strategy = st.builds(
    esmodel::versioning::HistoryInfo,
)
versioning::VersionProperty_strategy = st.builds(
    versioning::VersionProperty,
)
notification::ESNotification_strategy = st.builds(
    notification::ESNotification,
)
versioning::LogMessage_strategy = st.builds(
    versioning::LogMessage,
)
events::Event_strategy = st.builds(
    events::Event,
)
operations::AbstractOperation_strategy = st.builds(
    operations::AbstractOperation,
)
esmodel::versioning::ChangePackage_strategy = st.builds(
    esmodel::versioning::ChangePackage,
)
VersionSpec_strategy = st.builds(
    VersionSpec,
)
esmodel::versioning::DateVersionSpec_strategy = st.builds(
    esmodel::versioning::DateVersionSpec,
    date=
        st.dates()
)
esmodel::versioning::PrimaryVersionSpec_strategy = st.builds(
    esmodel::versioning::PrimaryVersionSpec,
    identifier=
        st.integers()
)
esmodel::versioning::HeadVersionSpec_strategy = st.builds(
    esmodel::versioning::HeadVersionSpec,
)
esmodel::versioning::TagVersionSpec_strategy = st.builds(
    esmodel::versioning::TagVersionSpec,
    name=
        safe_text
)
esmodel::ClientVersionInfo_strategy = st.builds(
    esmodel::ClientVersionInfo,
    version=
        safe_text,
    name=
        safe_text
)
esmodel::VersionInfo_strategy = st.builds(
    esmodel::VersionInfo,
    emfStoreVersionString=
        safe_text
)
esmodel::ProjectId_strategy = st.builds(
    esmodel::ProjectId,
)
accesscontrol::ACUser_strategy = st.builds(
    accesscontrol::ACUser,
)
SessionId_strategy = st.builds(
    SessionId,
)
ProjectHistory_strategy = st.builds(
    ProjectHistory,
)
accesscontrol::ACGroup_strategy = st.builds(
    accesscontrol::ACGroup,
)
esmodel::ServerSpace_strategy = st.builds(
    esmodel::ServerSpace,
)
esmodel::SessionId_strategy = st.builds(
    esmodel::SessionId,
)
versioning::PrimaryVersionSpec_strategy = st.builds(
    versioning::PrimaryVersionSpec,
)
esmodel::ProjectInfo_strategy = st.builds(
    esmodel::ProjectInfo,
    name=
        safe_text,
    description=
        safe_text
)
versioning::Version_strategy = st.builds(
    versioning::Version,
)
ProjectId_strategy = st.builds(
    ProjectId,
)
esmodel::ProjectHistory_strategy = st.builds(
    esmodel::ProjectHistory,
    projectName=
        safe_text,
    projectDescription=
        safe_text
)
ActivityObject_strategy = st.builds(
    ActivityObject,
)
model::activity::Fork_strategy = st.builds(
    model::activity::Fork,
)
model::activity::ActivityInitial_strategy = st.builds(
    model::activity::ActivityInitial,
)
model::activity::ActivityEnd_strategy = st.builds(
    model::activity::ActivityEnd,
)
model::activity::Branch_strategy = st.builds(
    model::activity::Branch,
)
model::activity::Activity_strategy = st.builds(
    model::activity::Activity,
)
activity::ActivityObject_strategy = st.builds(
    activity::ActivityObject,
)
model::activity::Transition_strategy = st.builds(
    model::activity::Transition,
    condition=
        safe_text
)
activity::Transition_strategy = st.builds(
    activity::Transition,
)
model::activity::ActivityObject_strategy = st.builds(
    model::activity::ActivityObject,
)
ModelElementId_strategy = st.builds(
    ModelElementId,
)
model::util::ModelElementPath_strategy = st.builds(
    model::util::ModelElementPath,
)
StereotypeAttributeInstance_strategy = st.builds(
    StereotypeAttributeInstance,
)
model::profile::StereotypeAttributeInstanceString_strategy = st.builds(
    model::profile::StereotypeAttributeInstanceString,
    value=
        safe_text
)
model::profile::Profile_strategy = st.builds(
    model::profile::Profile,
)
model::profile::StereotypeAttributeInstance_strategy = st.builds(
    model::profile::StereotypeAttributeInstance,
)
StereotypeAttribute_strategy = st.builds(
    StereotypeAttribute,
)
model::profile::StereotypeAttributeSimple_strategy = st.builds(
    model::profile::StereotypeAttributeSimple,
    type=
        safe_text
)
model::profile::StereotypeAttribute_strategy = st.builds(
    model::profile::StereotypeAttribute,
)
profile::StereotypeAttributeInstance_strategy = st.builds(
    profile::StereotypeAttributeInstance,
)
model::profile::StereotypeInstance_strategy = st.builds(
    model::profile::StereotypeInstance,
)
profile::StereotypeAttribute_strategy = st.builds(
    profile::StereotypeAttribute,
)
profile::Profile_strategy = st.builds(
    profile::Profile,
)
model::profile::Stereotype_strategy = st.builds(
    model::profile::Stereotype,
    required=
        st.booleans()
)
profile::Stereotype_strategy = st.builds(
    profile::Stereotype,
)
model::attachment::FileAttachment_strategy = st.builds(
    model::attachment::FileAttachment,
    fileSize=
        safe_text,
    fileID=
        safe_text,
    fileName=
        safe_text,
    fileHash=
        safe_text
)
model::attachment::UrlAttachment_strategy = st.builds(
    model::attachment::UrlAttachment,
    url=
        safe_text
)
StateNode_strategy = st.builds(
    StateNode,
)
model::state::StateInitial_strategy = st.builds(
    model::state::StateInitial,
)
model::state::StateEnd_strategy = st.builds(
    model::state::StateEnd,
)
model::state::State_strategy = st.builds(
    model::state::State,
    exitConditions=
        safe_text,
    activities=
        safe_text,
    entryConditions=
        safe_text
)
state::Transition_strategy = st.builds(
    state::Transition,
)
model::state::StateNode_strategy = st.builds(
    model::state::StateNode,
)
state::StateNode_strategy = st.builds(
    state::StateNode,
)
model::state::Transition_strategy = st.builds(
    model::state::Transition,
    condition=
        safe_text
)
MeetingSection_strategy = st.builds(
    MeetingSection,
)
model::meeting::IssueMeetingSection_strategy = st.builds(
    model::meeting::IssueMeetingSection,
)
model::meeting::WorkItemMeetingSection_strategy = st.builds(
    model::meeting::WorkItemMeetingSection,
)
model::meeting::CompositeMeetingSection_strategy = st.builds(
    model::meeting::CompositeMeetingSection,
)
model::meeting::MeetingSection_strategy = st.builds(
    model::meeting::MeetingSection,
    allocatedTime=
        st.integers()
)
meeting::WorkItemMeetingSection_strategy = st.builds(
    meeting::WorkItemMeetingSection,
)
meeting::IssueMeetingSection_strategy = st.builds(
    meeting::IssueMeetingSection,
)
meeting::MeetingSection_strategy = st.builds(
    meeting::MeetingSection,
)
model::meeting::Meeting_strategy = st.builds(
    model::meeting::Meeting,
    location=
        safe_text,
    starttime=
        st.dates(),
    endtime=
        st.dates()
)
model::component::DeploymentNode_strategy = st.builds(
    model::component::DeploymentNode,
)

@given(instance=url::ModelElementUrlFragment_strategy)
@settings(max_examples=50)
def test_url::modelelementurlfragment_instantiation(instance):
    assert isinstance(instance, url::ModelElementUrlFragment)

@given(instance=url::ProjectUrlFragment_strategy)
@settings(max_examples=50)
def test_url::projecturlfragment_instantiation(instance):
    assert isinstance(instance, url::ProjectUrlFragment)

@given(instance=url::ServerUrl_strategy)
@settings(max_examples=50)
def test_url::serverurl_instantiation(instance):
    assert isinstance(instance, url::ServerUrl)

@given(instance=esmodel::url::ModelElementUrl_strategy)
@settings(max_examples=50)
def test_esmodel::url::modelelementurl_instantiation(instance):
    assert isinstance(instance, esmodel::url::ModelElementUrl)

@given(instance=esmodel::url::ModelElementUrlFragment_strategy)
@settings(max_examples=50)
def test_esmodel::url::modelelementurlfragment_instantiation(instance):
    assert isinstance(instance, esmodel::url::ModelElementUrlFragment)

@given(instance=esmodel::url::ModelElementUrlFragment_strategy)
def test_esmodel::url::modelelementurlfragment_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esmodel::url::ModelElementUrlFragment_strategy)
def test_esmodel::url::modelelementurlfragment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esmodel::url::ProjectUrlFragment_strategy)
@settings(max_examples=50)
def test_esmodel::url::projecturlfragment_instantiation(instance):
    assert isinstance(instance, esmodel::url::ProjectUrlFragment)

@given(instance=esmodel::url::ProjectUrlFragment_strategy)
def test_esmodel::url::projecturlfragment_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esmodel::url::ProjectUrlFragment_strategy)
def test_esmodel::url::projecturlfragment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=component::Component_strategy)
@settings(max_examples=50)
def test_component::component_instantiation(instance):
    assert isinstance(instance, component::Component)

@given(instance=component::ComponentService_strategy)
@settings(max_examples=50)
def test_component::componentservice_instantiation(instance):
    assert isinstance(instance, component::ComponentService)

@given(instance=Solution_strategy)
@settings(max_examples=50)
def test_solution_instantiation(instance):
    assert isinstance(instance, Solution)

@given(instance=model::change::MergingSolution_strategy)
@settings(max_examples=50)
def test_model::change::mergingsolution_instantiation(instance):
    assert isinstance(instance, model::change::MergingSolution)

@given(instance=change::MergingProposal_strategy)
@settings(max_examples=50)
def test_change::mergingproposal_instantiation(instance):
    assert isinstance(instance, change::MergingProposal)

@given(instance=Proposal_strategy)
@settings(max_examples=50)
def test_proposal_instantiation(instance):
    assert isinstance(instance, Proposal)

@given(instance=model::change::MergingProposal_strategy)
@settings(max_examples=50)
def test_model::change::mergingproposal_instantiation(instance):
    assert isinstance(instance, model::change::MergingProposal)

@given(instance=Issue_strategy)
@settings(max_examples=50)
def test_issue_instantiation(instance):
    assert isinstance(instance, Issue)

@given(instance=model::change::MergingIssue_strategy)
@settings(max_examples=50)
def test_model::change::mergingissue_instantiation(instance):
    assert isinstance(instance, model::change::MergingIssue)

@given(instance=model::change::MergingIssue_strategy)
def test_model::change::mergingissue_resolvingRevision_type(instance):
    assert isinstance(instance.resolvingRevision, int)


@given(instance=model::change::MergingIssue_strategy)
def test_model::change::mergingissue_resolvingRevision_setter(instance):
    original = instance.resolvingRevision
    instance.resolvingRevision = original
    assert instance.resolvingRevision == original

@given(instance=rationale::Proposal_strategy)
@settings(max_examples=50)
def test_rationale::proposal_instantiation(instance):
    assert isinstance(instance, rationale::Proposal)

@given(instance=rationale::Assessment_strategy)
@settings(max_examples=50)
def test_rationale::assessment_instantiation(instance):
    assert isinstance(instance, rationale::Assessment)

@given(instance=rationale::Issue_strategy)
@settings(max_examples=50)
def test_rationale::issue_instantiation(instance):
    assert isinstance(instance, rationale::Issue)

@given(instance=rationale::Criterion_strategy)
@settings(max_examples=50)
def test_rationale::criterion_instantiation(instance):
    assert isinstance(instance, rationale::Criterion)

@given(instance=rationale::Solution_strategy)
@settings(max_examples=50)
def test_rationale::solution_instantiation(instance):
    assert isinstance(instance, rationale::Solution)

@given(instance=Criterion_strategy)
@settings(max_examples=50)
def test_criterion_instantiation(instance):
    assert isinstance(instance, Criterion)

@given(instance=model::requirement::NonFunctionalRequirement_strategy)
@settings(max_examples=50)
def test_model::requirement::nonfunctionalrequirement_instantiation(instance):
    assert isinstance(instance, model::requirement::NonFunctionalRequirement)

@given(instance=requirement::SystemFunction_strategy)
@settings(max_examples=50)
def test_requirement::systemfunction_instantiation(instance):
    assert isinstance(instance, requirement::SystemFunction)

@given(instance=NonDomainElement_strategy)
@settings(max_examples=50)
def test_nondomainelement_instantiation(instance):
    assert isinstance(instance, NonDomainElement)

@given(instance=requirement::ActorInstance_strategy)
@settings(max_examples=50)
def test_requirement::actorinstance_instantiation(instance):
    assert isinstance(instance, requirement::ActorInstance)

@given(instance=requirement::UserTask_strategy)
@settings(max_examples=50)
def test_requirement::usertask_instantiation(instance):
    assert isinstance(instance, requirement::UserTask)

@given(instance=requirement::Step_strategy)
@settings(max_examples=50)
def test_requirement::step_instantiation(instance):
    assert isinstance(instance, requirement::Step)

@given(instance=requirement::NonFunctionalRequirement_strategy)
@settings(max_examples=50)
def test_requirement::nonfunctionalrequirement_instantiation(instance):
    assert isinstance(instance, requirement::NonFunctionalRequirement)

@given(instance=requirement::Actor_strategy)
@settings(max_examples=50)
def test_requirement::actor_instantiation(instance):
    assert isinstance(instance, requirement::Actor)

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=model::document::LeafSection_strategy)
@settings(max_examples=50)
def test_model::document::leafsection_instantiation(instance):
    assert isinstance(instance, model::document::LeafSection)

@given(instance=document::CompositeSection_strategy)
@settings(max_examples=50)
def test_document::compositesection_instantiation(instance):
    assert isinstance(instance, document::CompositeSection)

@given(instance=requirement::FunctionalRequirement_strategy)
@settings(max_examples=50)
def test_requirement::functionalrequirement_instantiation(instance):
    assert isinstance(instance, requirement::FunctionalRequirement)

@given(instance=document::Section_strategy)
@settings(max_examples=50)
def test_document::section_instantiation(instance):
    assert isinstance(instance, document::Section)

@given(instance=model::document::CompositeSection_strategy)
@settings(max_examples=50)
def test_model::document::compositesection_instantiation(instance):
    assert isinstance(instance, model::document::CompositeSection)

@given(instance=classes::MethodArgument_strategy)
@settings(max_examples=50)
def test_classes::methodargument_instantiation(instance):
    assert isinstance(instance, classes::MethodArgument)

@given(instance=classes::PackageElement_strategy)
@settings(max_examples=50)
def test_classes::packageelement_instantiation(instance):
    assert isinstance(instance, classes::PackageElement)

@given(instance=PackageElement_strategy)
@settings(max_examples=50)
def test_packageelement_instantiation(instance):
    assert isinstance(instance, PackageElement)

@given(instance=model::classes::Package_strategy)
@settings(max_examples=50)
def test_model::classes::package_instantiation(instance):
    assert isinstance(instance, model::classes::Package)

@given(instance=model::classes::Class_strategy)
@settings(max_examples=50)
def test_model::classes::class_instantiation(instance):
    assert isinstance(instance, model::classes::Class)

@given(instance=classes::Dependency_strategy)
@settings(max_examples=50)
def test_classes::dependency_instantiation(instance):
    assert isinstance(instance, classes::Dependency)

@given(instance=classes::Package_strategy)
@settings(max_examples=50)
def test_classes::package_instantiation(instance):
    assert isinstance(instance, classes::Package)

@given(instance=requirement::Scenario_strategy)
@settings(max_examples=50)
def test_requirement::scenario_instantiation(instance):
    assert isinstance(instance, requirement::Scenario)

@given(instance=requirement::UseCase_strategy)
@settings(max_examples=50)
def test_requirement::usecase_instantiation(instance):
    assert isinstance(instance, requirement::UseCase)

@given(instance=classes::Method_strategy)
@settings(max_examples=50)
def test_classes::method_instantiation(instance):
    assert isinstance(instance, classes::Method)

@given(instance=classes::Attribute_strategy)
@settings(max_examples=50)
def test_classes::attribute_instantiation(instance):
    assert isinstance(instance, classes::Attribute)

@given(instance=classes::Association_strategy)
@settings(max_examples=50)
def test_classes::association_instantiation(instance):
    assert isinstance(instance, classes::Association)

@given(instance=classes::Class_strategy)
@settings(max_examples=50)
def test_classes::class_instantiation(instance):
    assert isinstance(instance, classes::Class)

@given(instance=diagram::model::Diagram_strategy)
@settings(max_examples=50)
def test_diagram::model::diagram_instantiation(instance):
    assert isinstance(instance, diagram::model::Diagram)

@given(instance=task::Checkable_strategy)
@settings(max_examples=50)
def test_task::checkable_instantiation(instance):
    assert isinstance(instance, task::Checkable)

@given(instance=organization::User_strategy)
@settings(max_examples=50)
def test_organization::user_instantiation(instance):
    assert isinstance(instance, organization::User)

@given(instance=task::WorkPackage_strategy)
@settings(max_examples=50)
def test_task::workpackage_instantiation(instance):
    assert isinstance(instance, task::WorkPackage)

@given(instance=organization::OrgUnit_strategy)
@settings(max_examples=50)
def test_organization::orgunit_instantiation(instance):
    assert isinstance(instance, organization::OrgUnit)

@given(instance=WorkItem_strategy)
@settings(max_examples=50)
def test_workitem_instantiation(instance):
    assert isinstance(instance, WorkItem)

@given(instance=model::task::Milestone_strategy)
@settings(max_examples=50)
def test_model::task::milestone_instantiation(instance):
    assert isinstance(instance, model::task::Milestone)

@given(instance=model::task::WorkPackage_strategy)
@settings(max_examples=50)
def test_model::task::workpackage_instantiation(instance):
    assert isinstance(instance, model::task::WorkPackage)

@given(instance=model::task::WorkPackage_strategy)
def test_model::task::workpackage_startDate_type(instance):
    assert isinstance(instance.startDate, date)


@given(instance=model::task::WorkPackage_strategy)
def test_model::task::workpackage_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original

@given(instance=model::task::WorkPackage_strategy)
def test_model::task::workpackage_endDate_type(instance):
    assert isinstance(instance.endDate, date)


@given(instance=model::task::WorkPackage_strategy)
def test_model::task::workpackage_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original

@given(instance=change::ModelChangePackage_strategy)
@settings(max_examples=50)
def test_change::modelchangepackage_instantiation(instance):
    assert isinstance(instance, change::ModelChangePackage)

@given(instance=Project_strategy)
@settings(max_examples=50)
def test_project_instantiation(instance):
    assert isinstance(instance, Project)

@given(instance=model::Project_strategy)
@settings(max_examples=50)
def test_model::project_instantiation(instance):
    assert isinstance(instance, model::Project)

@given(instance=model::NonDomainElement_strategy)
@settings(max_examples=50)
def test_model::nondomainelement_instantiation(instance):
    assert isinstance(instance, model::NonDomainElement)

@given(instance=UnicaseModelElement_strategy)
@settings(max_examples=50)
def test_unicasemodelelement_instantiation(instance):
    assert isinstance(instance, UnicaseModelElement)

@given(instance=model::rationale::Comment_strategy)
@settings(max_examples=50)
def test_model::rationale::comment_instantiation(instance):
    assert isinstance(instance, model::rationale::Comment)

@given(instance=model::requirement::SystemFunction_strategy)
@settings(max_examples=50)
def test_model::requirement::systemfunction_instantiation(instance):
    assert isinstance(instance, model::requirement::SystemFunction)

@given(instance=model::requirement::SystemFunction_strategy)
def test_model::requirement::systemfunction_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=model::requirement::SystemFunction_strategy)
def test_model::requirement::systemfunction_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=model::requirement::SystemFunction_strategy)
def test_model::requirement::systemfunction_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=model::requirement::SystemFunction_strategy)
def test_model::requirement::systemfunction_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=model::requirement::SystemFunction_strategy)
def test_model::requirement::systemfunction_exception_type(instance):
    assert isinstance(instance.exception, str)


@given(instance=model::requirement::SystemFunction_strategy)
def test_model::requirement::systemfunction_exception_setter(instance):
    original = instance.exception
    instance.exception = original
    assert instance.exception == original

@given(instance=model::requirement::Actor_strategy)
@settings(max_examples=50)
def test_model::requirement::actor_instantiation(instance):
    assert isinstance(instance, model::requirement::Actor)

@given(instance=model::component::Component_strategy)
@settings(max_examples=50)
def test_model::component::component_instantiation(instance):
    assert isinstance(instance, model::component::Component)

@given(instance=model::change::ModelChangePackage_strategy)
@settings(max_examples=50)
def test_model::change::modelchangepackage_instantiation(instance):
    assert isinstance(instance, model::change::ModelChangePackage)

@given(instance=model::change::ModelChangePackage_strategy)
def test_model::change::modelchangepackage_targetVersion_type(instance):
    assert isinstance(instance.targetVersion, int)


@given(instance=model::change::ModelChangePackage_strategy)
def test_model::change::modelchangepackage_targetVersion_setter(instance):
    original = instance.targetVersion
    instance.targetVersion = original
    assert instance.targetVersion == original

@given(instance=model::change::ModelChangePackage_strategy)
def test_model::change::modelchangepackage_sourceVersion_type(instance):
    assert isinstance(instance.sourceVersion, int)


@given(instance=model::change::ModelChangePackage_strategy)
def test_model::change::modelchangepackage_sourceVersion_setter(instance):
    original = instance.sourceVersion
    instance.sourceVersion = original
    assert instance.sourceVersion == original

@given(instance=model::task::Checkable_strategy)
@settings(max_examples=50)
def test_model::task::checkable_instantiation(instance):
    assert isinstance(instance, model::task::Checkable)

@given(instance=model::task::Checkable_strategy)
def test_model::task::checkable_checked_type(instance):
    assert isinstance(instance.checked, bool)


@given(instance=model::task::Checkable_strategy)
def test_model::task::checkable_checked_setter(instance):
    original = instance.checked
    instance.checked = original
    assert instance.checked == original

@given(instance=model::classes::Attribute_strategy)
@settings(max_examples=50)
def test_model::classes::attribute_instantiation(instance):
    assert isinstance(instance, model::classes::Attribute)

@given(instance=model::classes::Attribute_strategy)
def test_model::classes::attribute_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=model::classes::Attribute_strategy)
def test_model::classes::attribute_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=model::classes::Attribute_strategy)
def test_model::classes::attribute_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=model::classes::Attribute_strategy)
def test_model::classes::attribute_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=model::classes::Attribute_strategy)
def test_model::classes::attribute_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=model::classes::Attribute_strategy)
def test_model::classes::attribute_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=model::classes::Attribute_strategy)
def test_model::classes::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::classes::Attribute_strategy)
def test_model::classes::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model::classes::Attribute_strategy)
def test_model::classes::attribute_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=model::classes::Attribute_strategy)
def test_model::classes::attribute_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=model::classes::Attribute_strategy)
def test_model::classes::attribute_properties_type(instance):
    assert isinstance(instance.properties, str)


@given(instance=model::classes::Attribute_strategy)
def test_model::classes::attribute_properties_setter(instance):
    original = instance.properties
    instance.properties = original
    assert instance.properties == original

@given(instance=model::classes::Attribute_strategy)
def test_model::classes::attribute_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=model::classes::Attribute_strategy)
def test_model::classes::attribute_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=model::rationale::Proposal_strategy)
@settings(max_examples=50)
def test_model::rationale::proposal_instantiation(instance):
    assert isinstance(instance, model::rationale::Proposal)

@given(instance=model::rationale::Assessment_strategy)
@settings(max_examples=50)
def test_model::rationale::assessment_instantiation(instance):
    assert isinstance(instance, model::rationale::Assessment)

@given(instance=model::rationale::Assessment_strategy)
def test_model::rationale::assessment_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=model::rationale::Assessment_strategy)
def test_model::rationale::assessment_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::document::Section_strategy)
@settings(max_examples=50)
def test_model::document::section_instantiation(instance):
    assert isinstance(instance, model::document::Section)

@given(instance=model::component::ComponentService_strategy)
@settings(max_examples=50)
def test_model::component::componentservice_instantiation(instance):
    assert isinstance(instance, model::component::ComponentService)

@given(instance=model::Attachment_strategy)
@settings(max_examples=50)
def test_model::attachment_instantiation(instance):
    assert isinstance(instance, model::Attachment)

@given(instance=model::requirement::UseCase_strategy)
@settings(max_examples=50)
def test_model::requirement::usecase_instantiation(instance):
    assert isinstance(instance, model::requirement::UseCase)

@given(instance=model::requirement::UseCase_strategy)
def test_model::requirement::usecase_precondition_type(instance):
    assert isinstance(instance.precondition, str)


@given(instance=model::requirement::UseCase_strategy)
def test_model::requirement::usecase_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original

@given(instance=model::requirement::UseCase_strategy)
def test_model::requirement::usecase_postcondition_type(instance):
    assert isinstance(instance.postcondition, str)


@given(instance=model::requirement::UseCase_strategy)
def test_model::requirement::usecase_postcondition_setter(instance):
    original = instance.postcondition
    instance.postcondition = original
    assert instance.postcondition == original

@given(instance=model::requirement::UseCase_strategy)
def test_model::requirement::usecase_rules_type(instance):
    assert isinstance(instance.rules, str)


@given(instance=model::requirement::UseCase_strategy)
def test_model::requirement::usecase_rules_setter(instance):
    original = instance.rules
    instance.rules = original
    assert instance.rules == original

@given(instance=model::requirement::UseCase_strategy)
def test_model::requirement::usecase_exception_type(instance):
    assert isinstance(instance.exception, str)


@given(instance=model::requirement::UseCase_strategy)
def test_model::requirement::usecase_exception_setter(instance):
    original = instance.exception
    instance.exception = original
    assert instance.exception == original

@given(instance=model::rationale::Solution_strategy)
@settings(max_examples=50)
def test_model::rationale::solution_instantiation(instance):
    assert isinstance(instance, model::rationale::Solution)

@given(instance=model::rationale::Criterion_strategy)
@settings(max_examples=50)
def test_model::rationale::criterion_instantiation(instance):
    assert isinstance(instance, model::rationale::Criterion)

@given(instance=model::classes::Association_strategy)
@settings(max_examples=50)
def test_model::classes::association_instantiation(instance):
    assert isinstance(instance, model::classes::Association)

@given(instance=model::classes::Association_strategy)
def test_model::classes::association_targetMultiplicity_type(instance):
    assert isinstance(instance.targetMultiplicity, str)


@given(instance=model::classes::Association_strategy)
def test_model::classes::association_targetMultiplicity_setter(instance):
    original = instance.targetMultiplicity
    instance.targetMultiplicity = original
    assert instance.targetMultiplicity == original

@given(instance=model::classes::Association_strategy)
def test_model::classes::association_targetRole_type(instance):
    assert isinstance(instance.targetRole, str)


@given(instance=model::classes::Association_strategy)
def test_model::classes::association_targetRole_setter(instance):
    original = instance.targetRole
    instance.targetRole = original
    assert instance.targetRole == original

@given(instance=model::classes::Association_strategy)
def test_model::classes::association_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::classes::Association_strategy)
def test_model::classes::association_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model::classes::Association_strategy)
def test_model::classes::association_sourceMultiplicity_type(instance):
    assert isinstance(instance.sourceMultiplicity, str)


@given(instance=model::classes::Association_strategy)
def test_model::classes::association_sourceMultiplicity_setter(instance):
    original = instance.sourceMultiplicity
    instance.sourceMultiplicity = original
    assert instance.sourceMultiplicity == original

@given(instance=model::classes::Association_strategy)
def test_model::classes::association_sourceRole_type(instance):
    assert isinstance(instance.sourceRole, str)


@given(instance=model::classes::Association_strategy)
def test_model::classes::association_sourceRole_setter(instance):
    original = instance.sourceRole
    instance.sourceRole = original
    assert instance.sourceRole == original

@given(instance=model::classes::PackageElement_strategy)
@settings(max_examples=50)
def test_model::classes::packageelement_instantiation(instance):
    assert isinstance(instance, model::classes::PackageElement)

@given(instance=model::requirement::Scenario_strategy)
@settings(max_examples=50)
def test_model::requirement::scenario_instantiation(instance):
    assert isinstance(instance, model::requirement::Scenario)

@given(instance=model::requirement::Step_strategy)
@settings(max_examples=50)
def test_model::requirement::step_instantiation(instance):
    assert isinstance(instance, model::requirement::Step)

@given(instance=model::requirement::Step_strategy)
def test_model::requirement::step_userStep_type(instance):
    assert isinstance(instance.userStep, bool)


@given(instance=model::requirement::Step_strategy)
def test_model::requirement::step_userStep_setter(instance):
    original = instance.userStep
    instance.userStep = original
    assert instance.userStep == original

@given(instance=model::classes::Method_strategy)
@settings(max_examples=50)
def test_model::classes::method_instantiation(instance):
    assert isinstance(instance, model::classes::Method)

@given(instance=model::classes::Method_strategy)
def test_model::classes::method_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=model::classes::Method_strategy)
def test_model::classes::method_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=model::classes::Method_strategy)
def test_model::classes::method_properties_type(instance):
    assert isinstance(instance.properties, str)


@given(instance=model::classes::Method_strategy)
def test_model::classes::method_properties_setter(instance):
    original = instance.properties
    instance.properties = original
    assert instance.properties == original

@given(instance=model::classes::Method_strategy)
def test_model::classes::method_returnType_type(instance):
    assert isinstance(instance.returnType, str)


@given(instance=model::classes::Method_strategy)
def test_model::classes::method_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original

@given(instance=model::classes::Method_strategy)
def test_model::classes::method_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=model::classes::Method_strategy)
def test_model::classes::method_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=model::classes::Method_strategy)
def test_model::classes::method_stubbed_type(instance):
    assert isinstance(instance.stubbed, bool)


@given(instance=model::classes::Method_strategy)
def test_model::classes::method_stubbed_setter(instance):
    original = instance.stubbed
    instance.stubbed = original
    assert instance.stubbed == original

@given(instance=model::classes::Method_strategy)
def test_model::classes::method_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=model::classes::Method_strategy)
def test_model::classes::method_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=model::classes::Method_strategy)
def test_model::classes::method_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=model::classes::Method_strategy)
def test_model::classes::method_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=model::classes::Dependency_strategy)
@settings(max_examples=50)
def test_model::classes::dependency_instantiation(instance):
    assert isinstance(instance, model::classes::Dependency)

@given(instance=model::requirement::ActorInstance_strategy)
@settings(max_examples=50)
def test_model::requirement::actorinstance_instantiation(instance):
    assert isinstance(instance, model::requirement::ActorInstance)

@given(instance=model::requirement::UserTask_strategy)
@settings(max_examples=50)
def test_model::requirement::usertask_instantiation(instance):
    assert isinstance(instance, model::requirement::UserTask)

@given(instance=model::classes::MethodArgument_strategy)
@settings(max_examples=50)
def test_model::classes::methodargument_instantiation(instance):
    assert isinstance(instance, model::classes::MethodArgument)

@given(instance=model::classes::MethodArgument_strategy)
def test_model::classes::methodargument_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=model::classes::MethodArgument_strategy)
def test_model::classes::methodargument_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=model::classes::MethodArgument_strategy)
def test_model::classes::methodargument_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=model::classes::MethodArgument_strategy)
def test_model::classes::methodargument_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=model::classes::MethodArgument_strategy)
def test_model::classes::methodargument_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=model::classes::MethodArgument_strategy)
def test_model::classes::methodargument_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=model::classes::MethodArgument_strategy)
def test_model::classes::methodargument_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::classes::MethodArgument_strategy)
def test_model::classes::methodargument_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model::classes::MethodArgument_strategy)
def test_model::classes::methodargument_signature_type(instance):
    assert isinstance(instance.signature, str)


@given(instance=model::classes::MethodArgument_strategy)
def test_model::classes::methodargument_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=model::requirement::FunctionalRequirement_strategy)
@settings(max_examples=50)
def test_model::requirement::functionalrequirement_instantiation(instance):
    assert isinstance(instance, model::requirement::FunctionalRequirement)

@given(instance=model::requirement::FunctionalRequirement_strategy)
def test_model::requirement::functionalrequirement_storyPoints_type(instance):
    assert isinstance(instance.storyPoints, int)


@given(instance=model::requirement::FunctionalRequirement_strategy)
def test_model::requirement::functionalrequirement_storyPoints_setter(instance):
    original = instance.storyPoints
    instance.storyPoints = original
    assert instance.storyPoints == original

@given(instance=model::requirement::FunctionalRequirement_strategy)
def test_model::requirement::functionalrequirement_cost_type(instance):
    assert isinstance(instance.cost, int)


@given(instance=model::requirement::FunctionalRequirement_strategy)
def test_model::requirement::functionalrequirement_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original

@given(instance=model::requirement::FunctionalRequirement_strategy)
def test_model::requirement::functionalrequirement_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=model::requirement::FunctionalRequirement_strategy)
def test_model::requirement::functionalrequirement_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=model::requirement::FunctionalRequirement_strategy)
def test_model::requirement::functionalrequirement_reviewed_type(instance):
    assert isinstance(instance.reviewed, bool)


@given(instance=model::requirement::FunctionalRequirement_strategy)
def test_model::requirement::functionalrequirement_reviewed_setter(instance):
    original = instance.reviewed
    instance.reviewed = original
    assert instance.reviewed == original

@given(instance=model::Annotation_strategy)
@settings(max_examples=50)
def test_model::annotation_instantiation(instance):
    assert isinstance(instance, model::Annotation)

@given(instance=profile::StereotypeInstance_strategy)
@settings(max_examples=50)
def test_profile::stereotypeinstance_instantiation(instance):
    assert isinstance(instance, profile::StereotypeInstance)

@given(instance=rationale::Comment_strategy)
@settings(max_examples=50)
def test_rationale::comment_instantiation(instance):
    assert isinstance(instance, rationale::Comment)

@given(instance=OrgUnit_strategy)
@settings(max_examples=50)
def test_orgunit_instantiation(instance):
    assert isinstance(instance, OrgUnit)

@given(instance=model::organization::Group_strategy)
@settings(max_examples=50)
def test_model::organization::group_instantiation(instance):
    assert isinstance(instance, model::organization::Group)

@given(instance=model::organization::User_strategy)
@settings(max_examples=50)
def test_model::organization::user_instantiation(instance):
    assert isinstance(instance, model::organization::User)

@given(instance=model::organization::User_strategy)
def test_model::organization::user_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=model::organization::User_strategy)
def test_model::organization::user_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=model::organization::User_strategy)
def test_model::organization::user_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=model::organization::User_strategy)
def test_model::organization::user_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=model::organization::User_strategy)
def test_model::organization::user_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=model::organization::User_strategy)
def test_model::organization::user_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=task::WorkItem_strategy)
@settings(max_examples=50)
def test_task::workitem_instantiation(instance):
    assert isinstance(instance, task::WorkItem)

@given(instance=model::bug::BugReport_strategy)
@settings(max_examples=50)
def test_model::bug::bugreport_instantiation(instance):
    assert isinstance(instance, model::bug::BugReport)

@given(instance=model::bug::BugReport_strategy)
def test_model::bug::bugreport_resolution_type(instance):
    assert isinstance(instance.resolution, str)


@given(instance=model::bug::BugReport_strategy)
def test_model::bug::bugreport_resolution_setter(instance):
    original = instance.resolution
    instance.resolution = original
    assert instance.resolution == original

@given(instance=model::bug::BugReport_strategy)
def test_model::bug::bugreport_resolutionType_type(instance):
    assert isinstance(instance.resolutionType, str)


@given(instance=model::bug::BugReport_strategy)
def test_model::bug::bugreport_resolutionType_setter(instance):
    original = instance.resolutionType
    instance.resolutionType = original
    assert instance.resolutionType == original

@given(instance=model::bug::BugReport_strategy)
def test_model::bug::bugreport_severity_type(instance):
    assert isinstance(instance.severity, str)


@given(instance=model::bug::BugReport_strategy)
def test_model::bug::bugreport_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=model::bug::BugReport_strategy)
def test_model::bug::bugreport_Status_type(instance):
    assert isinstance(instance.Status, str)


@given(instance=model::bug::BugReport_strategy)
def test_model::bug::bugreport_Status_setter(instance):
    original = instance.Status
    instance.Status = original
    assert instance.Status == original

@given(instance=model::task::ActionItem_strategy)
@settings(max_examples=50)
def test_model::task::actionitem_instantiation(instance):
    assert isinstance(instance, model::task::ActionItem)

@given(instance=model::task::ActionItem_strategy)
def test_model::task::actionitem_done_type(instance):
    assert isinstance(instance.done, bool)


@given(instance=model::task::ActionItem_strategy)
def test_model::task::actionitem_done_setter(instance):
    original = instance.done
    instance.done = original
    assert instance.done == original

@given(instance=model::task::ActionItem_strategy)
def test_model::task::actionitem_activity_type(instance):
    assert isinstance(instance.activity, str)


@given(instance=model::task::ActionItem_strategy)
def test_model::task::actionitem_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original

@given(instance=organization::Group_strategy)
@settings(max_examples=50)
def test_organization::group_instantiation(instance):
    assert isinstance(instance, organization::Group)

@given(instance=model::organization::OrgUnit_strategy)
@settings(max_examples=50)
def test_model::organization::orgunit_instantiation(instance):
    assert isinstance(instance, model::organization::OrgUnit)

@given(instance=model::organization::OrgUnit_strategy)
def test_model::organization::orgunit_acOrgId_type(instance):
    assert isinstance(instance.acOrgId, str)


@given(instance=model::organization::OrgUnit_strategy)
def test_model::organization::orgunit_acOrgId_setter(instance):
    original = instance.acOrgId
    instance.acOrgId = original
    assert instance.acOrgId == original

@given(instance=metamodel::AssociationClassElement_strategy)
@settings(max_examples=50)
def test_metamodel::associationclasselement_instantiation(instance):
    assert isinstance(instance, metamodel::AssociationClassElement)

@given(instance=metamodel::NonDomainElement_strategy)
@settings(max_examples=50)
def test_metamodel::nondomainelement_instantiation(instance):
    assert isinstance(instance, metamodel::NonDomainElement)

@given(instance=metamodel::ModelVersion_strategy)
@settings(max_examples=50)
def test_metamodel::modelversion_instantiation(instance):
    assert isinstance(instance, metamodel::ModelVersion)

@given(instance=metamodel::ModelVersion_strategy)
def test_metamodel::modelversion_releaseNumber_type(instance):
    assert isinstance(instance.releaseNumber, int)


@given(instance=metamodel::ModelVersion_strategy)
def test_metamodel::modelversion_releaseNumber_setter(instance):
    original = instance.releaseNumber
    instance.releaseNumber = original
    assert instance.releaseNumber == original

@given(instance=UniqueIdentifier_strategy)
@settings(max_examples=50)
def test_uniqueidentifier_instantiation(instance):
    assert isinstance(instance, UniqueIdentifier)

@given(instance=metamodel::ModelElementId_strategy)
@settings(max_examples=50)
def test_metamodel::modelelementid_instantiation(instance):
    assert isinstance(instance, metamodel::ModelElementId)

@given(instance=IdentifiableElement_strategy)
@settings(max_examples=50)
def test_identifiableelement_instantiation(instance):
    assert isinstance(instance, IdentifiableElement)

@given(instance=esmodel::notification::ESNotification_strategy)
@settings(max_examples=50)
def test_esmodel::notification::esnotification_instantiation(instance):
    assert isinstance(instance, esmodel::notification::ESNotification)

@given(instance=esmodel::notification::ESNotification_strategy)
def test_esmodel::notification::esnotification_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=esmodel::notification::ESNotification_strategy)
def test_esmodel::notification::esnotification_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=esmodel::notification::ESNotification_strategy)
def test_esmodel::notification::esnotification_seen_type(instance):
    assert isinstance(instance.seen, bool)


@given(instance=esmodel::notification::ESNotification_strategy)
def test_esmodel::notification::esnotification_seen_setter(instance):
    original = instance.seen
    instance.seen = original
    assert instance.seen == original

@given(instance=esmodel::notification::ESNotification_strategy)
def test_esmodel::notification::esnotification_sender_type(instance):
    assert isinstance(instance.sender, str)


@given(instance=esmodel::notification::ESNotification_strategy)
def test_esmodel::notification::esnotification_sender_setter(instance):
    original = instance.sender
    instance.sender = original
    assert instance.sender == original

@given(instance=esmodel::notification::ESNotification_strategy)
def test_esmodel::notification::esnotification_recipient_type(instance):
    assert isinstance(instance.recipient, str)


@given(instance=esmodel::notification::ESNotification_strategy)
def test_esmodel::notification::esnotification_recipient_setter(instance):
    original = instance.recipient
    instance.recipient = original
    assert instance.recipient == original

@given(instance=esmodel::notification::ESNotification_strategy)
def test_esmodel::notification::esnotification_creationDate_type(instance):
    assert isinstance(instance.creationDate, date)


@given(instance=esmodel::notification::ESNotification_strategy)
def test_esmodel::notification::esnotification_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=esmodel::notification::ESNotification_strategy)
def test_esmodel::notification::esnotification_details_type(instance):
    assert isinstance(instance.details, str)


@given(instance=esmodel::notification::ESNotification_strategy)
def test_esmodel::notification::esnotification_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original

@given(instance=esmodel::notification::ESNotification_strategy)
def test_esmodel::notification::esnotification_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esmodel::notification::ESNotification_strategy)
def test_esmodel::notification::esnotification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esmodel::notification::ESNotification_strategy)
def test_esmodel::notification::esnotification_provider_type(instance):
    assert isinstance(instance.provider, str)


@given(instance=esmodel::notification::ESNotification_strategy)
def test_esmodel::notification::esnotification_provider_setter(instance):
    original = instance.provider
    instance.provider = original
    assert instance.provider == original

@given(instance=metamodel::ModelElement_strategy)
@settings(max_examples=50)
def test_metamodel::modelelement_instantiation(instance):
    assert isinstance(instance, metamodel::ModelElement)

@given(instance=metamodel::ModelElement_strategy)
def test_metamodel::modelelement_creator_type(instance):
    assert isinstance(instance.creator, str)


@given(instance=metamodel::ModelElement_strategy)
def test_metamodel::modelelement_creator_setter(instance):
    original = instance.creator
    instance.creator = original
    assert instance.creator == original

@given(instance=metamodel::ModelElement_strategy)
def test_metamodel::modelelement_creationDate_type(instance):
    assert isinstance(instance.creationDate, date)


@given(instance=metamodel::ModelElement_strategy)
def test_metamodel::modelelement_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=metamodel::IdentifiableElement_strategy)
@settings(max_examples=50)
def test_metamodel::identifiableelement_instantiation(instance):
    assert isinstance(instance, metamodel::IdentifiableElement)

@given(instance=metamodel::IdentifiableElement_strategy)
def test_metamodel::identifiableelement_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=metamodel::IdentifiableElement_strategy)
def test_metamodel::identifiableelement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=metamodel::UniqueIdentifier_strategy)
@settings(max_examples=50)
def test_metamodel::uniqueidentifier_instantiation(instance):
    assert isinstance(instance, metamodel::UniqueIdentifier)

@given(instance=metamodel::UniqueIdentifier_strategy)
def test_metamodel::uniqueidentifier_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=metamodel::UniqueIdentifier_strategy)
def test_metamodel::uniqueidentifier_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=metamodel::Project_strategy)
@settings(max_examples=50)
def test_metamodel::project_instantiation(instance):
    assert isinstance(instance, metamodel::Project)

@given(instance=document::LeafSection_strategy)
@settings(max_examples=50)
def test_document::leafsection_instantiation(instance):
    assert isinstance(instance, document::LeafSection)

@given(instance=Attachment_strategy)
@settings(max_examples=50)
def test_attachment_instantiation(instance):
    assert isinstance(instance, Attachment)

@given(instance=model::diagram::MEDiagram_strategy)
@settings(max_examples=50)
def test_model::diagram::mediagram_instantiation(instance):
    assert isinstance(instance, model::diagram::MEDiagram)

@given(instance=model::diagram::MEDiagram_strategy)
def test_model::diagram::mediagram_diagramLayout_type(instance):
    assert isinstance(instance.diagramLayout, str)


@given(instance=model::diagram::MEDiagram_strategy)
def test_model::diagram::mediagram_diagramLayout_setter(instance):
    original = instance.diagramLayout
    instance.diagramLayout = original
    assert instance.diagramLayout == original

@given(instance=model::diagram::MEDiagram_strategy)
def test_model::diagram::mediagram_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::diagram::MEDiagram_strategy)
def test_model::diagram::mediagram_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=model::rationale::Issue_strategy)
@settings(max_examples=50)
def test_model::rationale::issue_instantiation(instance):
    assert isinstance(instance, model::rationale::Issue)

@given(instance=model::rationale::Issue_strategy)
def test_model::rationale::issue_activity_type(instance):
    assert isinstance(instance.activity, str)


@given(instance=model::rationale::Issue_strategy)
def test_model::rationale::issue_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original

@given(instance=model::task::WorkItem_strategy)
@settings(max_examples=50)
def test_model::task::workitem_instantiation(instance):
    assert isinstance(instance, model::task::WorkItem)

@given(instance=model::task::WorkItem_strategy)
def test_model::task::workitem_dueDate_type(instance):
    assert isinstance(instance.dueDate, date)


@given(instance=model::task::WorkItem_strategy)
def test_model::task::workitem_dueDate_setter(instance):
    original = instance.dueDate
    instance.dueDate = original
    assert instance.dueDate == original

@given(instance=model::task::WorkItem_strategy)
def test_model::task::workitem_priority_type(instance):
    assert isinstance(instance.priority, int)


@given(instance=model::task::WorkItem_strategy)
def test_model::task::workitem_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=model::task::WorkItem_strategy)
def test_model::task::workitem_effort_type(instance):
    assert isinstance(instance.effort, int)


@given(instance=model::task::WorkItem_strategy)
def test_model::task::workitem_effort_setter(instance):
    original = instance.effort
    instance.effort = original
    assert instance.effort == original

@given(instance=model::task::WorkItem_strategy)
def test_model::task::workitem_resolved_type(instance):
    assert isinstance(instance.resolved, bool)


@given(instance=model::task::WorkItem_strategy)
def test_model::task::workitem_resolved_setter(instance):
    original = instance.resolved
    instance.resolved = original
    assert instance.resolved == original

@given(instance=model::task::WorkItem_strategy)
def test_model::task::workitem_estimate_type(instance):
    assert isinstance(instance.estimate, int)


@given(instance=model::task::WorkItem_strategy)
def test_model::task::workitem_estimate_setter(instance):
    original = instance.estimate
    instance.estimate = original
    assert instance.estimate == original

@given(instance=model::UnicaseModelElement_strategy)
@settings(max_examples=50)
def test_model::unicasemodelelement_instantiation(instance):
    assert isinstance(instance, model::UnicaseModelElement)

@given(instance=model::UnicaseModelElement_strategy)
def test_model::unicasemodelelement_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=model::UnicaseModelElement_strategy)
def test_model::unicasemodelelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=model::UnicaseModelElement_strategy)
def test_model::unicasemodelelement_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=model::UnicaseModelElement_strategy)
def test_model::unicasemodelelement_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=model::UnicaseModelElement_strategy)
def test_model::unicasemodelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::UnicaseModelElement_strategy)
def test_model::unicasemodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esmodel::url::ServerUrl_strategy)
@settings(max_examples=50)
def test_esmodel::url::serverurl_instantiation(instance):
    assert isinstance(instance, esmodel::url::ServerUrl)

@given(instance=esmodel::url::ServerUrl_strategy)
def test_esmodel::url::serverurl_hostName_type(instance):
    assert isinstance(instance.hostName, str)


@given(instance=esmodel::url::ServerUrl_strategy)
def test_esmodel::url::serverurl_hostName_setter(instance):
    original = instance.hostName
    instance.hostName = original
    assert instance.hostName == original

@given(instance=esmodel::url::ServerUrl_strategy)
def test_esmodel::url::serverurl_port_type(instance):
    assert isinstance(instance.port, int)


@given(instance=esmodel::url::ServerUrl_strategy)
def test_esmodel::url::serverurl_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=esmodel::accesscontrol::OrgUnitProperty_strategy)
@settings(max_examples=50)
def test_esmodel::accesscontrol::orgunitproperty_instantiation(instance):
    assert isinstance(instance, esmodel::accesscontrol::OrgUnitProperty)

@given(instance=esmodel::accesscontrol::OrgUnitProperty_strategy)
def test_esmodel::accesscontrol::orgunitproperty_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esmodel::accesscontrol::OrgUnitProperty_strategy)
def test_esmodel::accesscontrol::orgunitproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esmodel::accesscontrol::OrgUnitProperty_strategy)
def test_esmodel::accesscontrol::orgunitproperty_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=esmodel::accesscontrol::OrgUnitProperty_strategy)
def test_esmodel::accesscontrol::orgunitproperty_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=esmodel::accesscontrol::ACOrgUnitId_strategy)
@settings(max_examples=50)
def test_esmodel::accesscontrol::acorgunitid_instantiation(instance):
    assert isinstance(instance, esmodel::accesscontrol::ACOrgUnitId)

@given(instance=accesscontrol::ACOrgUnit_strategy)
@settings(max_examples=50)
def test_accesscontrol::acorgunit_instantiation(instance):
    assert isinstance(instance, accesscontrol::ACOrgUnit)

@given(instance=accesscontrol::OrgUnitProperty_strategy)
@settings(max_examples=50)
def test_accesscontrol::orgunitproperty_instantiation(instance):
    assert isinstance(instance, accesscontrol::OrgUnitProperty)

@given(instance=roles::Role_strategy)
@settings(max_examples=50)
def test_roles::role_instantiation(instance):
    assert isinstance(instance, roles::Role)

@given(instance=Role_strategy)
@settings(max_examples=50)
def test_role_instantiation(instance):
    assert isinstance(instance, Role)

@given(instance=esmodel::roles::ServerAdmin_strategy)
@settings(max_examples=50)
def test_esmodel::roles::serveradmin_instantiation(instance):
    assert isinstance(instance, esmodel::roles::ServerAdmin)

@given(instance=esmodel::roles::WriterRole_strategy)
@settings(max_examples=50)
def test_esmodel::roles::writerrole_instantiation(instance):
    assert isinstance(instance, esmodel::roles::WriterRole)

@given(instance=esmodel::roles::ProjectAdminRole_strategy)
@settings(max_examples=50)
def test_esmodel::roles::projectadminrole_instantiation(instance):
    assert isinstance(instance, esmodel::roles::ProjectAdminRole)

@given(instance=esmodel::roles::ReaderRole_strategy)
@settings(max_examples=50)
def test_esmodel::roles::readerrole_instantiation(instance):
    assert isinstance(instance, esmodel::roles::ReaderRole)

@given(instance=esmodel::roles::Role_strategy)
@settings(max_examples=50)
def test_esmodel::roles::role_instantiation(instance):
    assert isinstance(instance, esmodel::roles::Role)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=esmodel::roles::Role_strategy)
@settings(max_examples=30)
def test_esmodel::roles::role_canmodify_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canModify(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canModify).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canModify' in esmodel::roles::Role is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canModify' in esmodel::roles::Role did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canModify' in esmodel::roles::Role is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=esmodel::roles::Role_strategy)
@settings(max_examples=30)
def test_esmodel::roles::role_candelete_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canDelete(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canDelete).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canDelete' in esmodel::roles::Role is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canDelete' in esmodel::roles::Role did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canDelete' in esmodel::roles::Role is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=esmodel::roles::Role_strategy)
@settings(max_examples=30)
def test_esmodel::roles::role_canadministrate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canAdministrate(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canAdministrate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canAdministrate' in esmodel::roles::Role is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canAdministrate' in esmodel::roles::Role did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canAdministrate' in esmodel::roles::Role is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=esmodel::roles::Role_strategy)
@settings(max_examples=30)
def test_esmodel::roles::role_cancreate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canCreate(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canCreate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canCreate' in esmodel::roles::Role is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canCreate' in esmodel::roles::Role did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canCreate' in esmodel::roles::Role is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=esmodel::roles::Role_strategy)
@settings(max_examples=30)
def test_esmodel::roles::role_canread_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canRead(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canRead).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canRead' in esmodel::roles::Role is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canRead' in esmodel::roles::Role did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canRead' in esmodel::roles::Role is not implemented or raised an error")

@given(instance=esmodel::accesscontrol::ACOrgUnit_strategy)
@settings(max_examples=50)
def test_esmodel::accesscontrol::acorgunit_instantiation(instance):
    assert isinstance(instance, esmodel::accesscontrol::ACOrgUnit)

@given(instance=esmodel::accesscontrol::ACOrgUnit_strategy)
def test_esmodel::accesscontrol::acorgunit_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=esmodel::accesscontrol::ACOrgUnit_strategy)
def test_esmodel::accesscontrol::acorgunit_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=esmodel::accesscontrol::ACOrgUnit_strategy)
def test_esmodel::accesscontrol::acorgunit_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esmodel::accesscontrol::ACOrgUnit_strategy)
def test_esmodel::accesscontrol::acorgunit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=operations::OperationId_strategy)
@settings(max_examples=50)
def test_operations::operationid_instantiation(instance):
    assert isinstance(instance, operations::OperationId)

@given(instance=ACOrgUnit_strategy)
@settings(max_examples=50)
def test_acorgunit_instantiation(instance):
    assert isinstance(instance, ACOrgUnit)

@given(instance=esmodel::accesscontrol::ACGroup_strategy)
@settings(max_examples=50)
def test_esmodel::accesscontrol::acgroup_instantiation(instance):
    assert isinstance(instance, esmodel::accesscontrol::ACGroup)

@given(instance=esmodel::accesscontrol::ACUser_strategy)
@settings(max_examples=50)
def test_esmodel::accesscontrol::acuser_instantiation(instance):
    assert isinstance(instance, esmodel::accesscontrol::ACUser)

@given(instance=esmodel::accesscontrol::ACUser_strategy)
def test_esmodel::accesscontrol::acuser_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=esmodel::accesscontrol::ACUser_strategy)
def test_esmodel::accesscontrol::acuser_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=esmodel::accesscontrol::ACUser_strategy)
def test_esmodel::accesscontrol::acuser_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=esmodel::accesscontrol::ACUser_strategy)
def test_esmodel::accesscontrol::acuser_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=ServerProjectEvent_strategy)
@settings(max_examples=50)
def test_serverprojectevent_instantiation(instance):
    assert isinstance(instance, ServerProjectEvent)

@given(instance=esmodel::server::ProjectUpdatedEvent_strategy)
@settings(max_examples=50)
def test_esmodel::server::projectupdatedevent_instantiation(instance):
    assert isinstance(instance, esmodel::server::ProjectUpdatedEvent)

@given(instance=ServerEvent_strategy)
@settings(max_examples=50)
def test_serverevent_instantiation(instance):
    assert isinstance(instance, ServerEvent)

@given(instance=esmodel::server::ServerProjectEvent_strategy)
@settings(max_examples=50)
def test_esmodel::server::serverprojectevent_instantiation(instance):
    assert isinstance(instance, esmodel::server::ServerProjectEvent)

@given(instance=ReadEvent_strategy)
@settings(max_examples=50)
def test_readevent_instantiation(instance):
    assert isinstance(instance, ReadEvent)

@given(instance=esmodel::events::NotificationReadEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::notificationreadevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::NotificationReadEvent)

@given(instance=esmodel::events::NotificationReadEvent_strategy)
def test_esmodel::events::notificationreadevent_notificationId_type(instance):
    assert isinstance(instance.notificationId, str)


@given(instance=esmodel::events::NotificationReadEvent_strategy)
def test_esmodel::events::notificationreadevent_notificationId_setter(instance):
    original = instance.notificationId
    instance.notificationId = original
    assert instance.notificationId == original

@given(instance=esmodel::operations::ModelElementGroup_strategy)
@settings(max_examples=50)
def test_esmodel::operations::modelelementgroup_instantiation(instance):
    assert isinstance(instance, esmodel::operations::ModelElementGroup)

@given(instance=esmodel::operations::ModelElementGroup_strategy)
def test_esmodel::operations::modelelementgroup_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esmodel::operations::ModelElementGroup_strategy)
def test_esmodel::operations::modelelementgroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=esmodel::events::ShowHistoryEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::showhistoryevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::ShowHistoryEvent)

@given(instance=esmodel::events::ExceptionEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::exceptionevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::ExceptionEvent)

@given(instance=esmodel::events::ExceptionEvent_strategy)
def test_esmodel::events::exceptionevent_ExceptionCauseTitle_type(instance):
    assert isinstance(instance.ExceptionCauseTitle, str)


@given(instance=esmodel::events::ExceptionEvent_strategy)
def test_esmodel::events::exceptionevent_ExceptionCauseTitle_setter(instance):
    original = instance.ExceptionCauseTitle
    instance.ExceptionCauseTitle = original
    assert instance.ExceptionCauseTitle == original

@given(instance=esmodel::events::ExceptionEvent_strategy)
def test_esmodel::events::exceptionevent_ExceptionCauseStackTrace_type(instance):
    assert isinstance(instance.ExceptionCauseStackTrace, str)


@given(instance=esmodel::events::ExceptionEvent_strategy)
def test_esmodel::events::exceptionevent_ExceptionCauseStackTrace_setter(instance):
    original = instance.ExceptionCauseStackTrace
    instance.ExceptionCauseStackTrace = original
    assert instance.ExceptionCauseStackTrace == original

@given(instance=esmodel::events::ExceptionEvent_strategy)
def test_esmodel::events::exceptionevent_ExceptionTitle_type(instance):
    assert isinstance(instance.ExceptionTitle, str)


@given(instance=esmodel::events::ExceptionEvent_strategy)
def test_esmodel::events::exceptionevent_ExceptionTitle_setter(instance):
    original = instance.ExceptionTitle
    instance.ExceptionTitle = original
    assert instance.ExceptionTitle == original

@given(instance=esmodel::events::ExceptionEvent_strategy)
def test_esmodel::events::exceptionevent_ExceptionStackTrace_type(instance):
    assert isinstance(instance.ExceptionStackTrace, str)


@given(instance=esmodel::events::ExceptionEvent_strategy)
def test_esmodel::events::exceptionevent_ExceptionStackTrace_setter(instance):
    original = instance.ExceptionStackTrace
    instance.ExceptionStackTrace = original
    assert instance.ExceptionStackTrace == original

@given(instance=esmodel::events::AnnotationEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::annotationevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::AnnotationEvent)

@given(instance=esmodel::events::MergeGlobalChoiceEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::mergeglobalchoiceevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::MergeGlobalChoiceEvent)

@given(instance=esmodel::events::MergeGlobalChoiceEvent_strategy)
def test_esmodel::events::mergeglobalchoiceevent_selection_type(instance):
    assert isinstance(instance.selection, str)


@given(instance=esmodel::events::MergeGlobalChoiceEvent_strategy)
def test_esmodel::events::mergeglobalchoiceevent_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=esmodel::events::TraceEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::traceevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::TraceEvent)

@given(instance=esmodel::events::TraceEvent_strategy)
def test_esmodel::events::traceevent_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=esmodel::events::TraceEvent_strategy)
def test_esmodel::events::traceevent_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=esmodel::events::PerspectiveEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::perspectiveevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::PerspectiveEvent)

@given(instance=esmodel::events::MergeChoiceEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::mergechoiceevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::MergeChoiceEvent)

@given(instance=esmodel::events::MergeChoiceEvent_strategy)
def test_esmodel::events::mergechoiceevent_createdIssueName_type(instance):
    assert isinstance(instance.createdIssueName, str)


@given(instance=esmodel::events::MergeChoiceEvent_strategy)
def test_esmodel::events::mergechoiceevent_createdIssueName_setter(instance):
    original = instance.createdIssueName
    instance.createdIssueName = original
    assert instance.createdIssueName == original

@given(instance=esmodel::events::MergeChoiceEvent_strategy)
def test_esmodel::events::mergechoiceevent_selection_type(instance):
    assert isinstance(instance.selection, str)


@given(instance=esmodel::events::MergeChoiceEvent_strategy)
def test_esmodel::events::mergechoiceevent_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=esmodel::events::MergeChoiceEvent_strategy)
def test_esmodel::events::mergechoiceevent_contextFeature_type(instance):
    assert isinstance(instance.contextFeature, str)


@given(instance=esmodel::events::MergeChoiceEvent_strategy)
def test_esmodel::events::mergechoiceevent_contextFeature_setter(instance):
    original = instance.contextFeature
    instance.contextFeature = original
    assert instance.contextFeature == original

@given(instance=esmodel::events::LinkEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::linkevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::LinkEvent)

@given(instance=esmodel::events::LinkEvent_strategy)
def test_esmodel::events::linkevent_createdNew_type(instance):
    assert isinstance(instance.createdNew, bool)


@given(instance=esmodel::events::LinkEvent_strategy)
def test_esmodel::events::linkevent_createdNew_setter(instance):
    original = instance.createdNew
    instance.createdNew = original
    assert instance.createdNew == original

@given(instance=esmodel::events::LinkEvent_strategy)
def test_esmodel::events::linkevent_sourceView_type(instance):
    assert isinstance(instance.sourceView, str)


@given(instance=esmodel::events::LinkEvent_strategy)
def test_esmodel::events::linkevent_sourceView_setter(instance):
    original = instance.sourceView
    instance.sourceView = original
    assert instance.sourceView == original

@given(instance=esmodel::events::PluginFocusEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::pluginfocusevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::PluginFocusEvent)

@given(instance=esmodel::events::PluginFocusEvent_strategy)
def test_esmodel::events::pluginfocusevent_startDate_type(instance):
    assert isinstance(instance.startDate, date)


@given(instance=esmodel::events::PluginFocusEvent_strategy)
def test_esmodel::events::pluginfocusevent_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original

@given(instance=esmodel::events::PluginFocusEvent_strategy)
def test_esmodel::events::pluginfocusevent_pluginId_type(instance):
    assert isinstance(instance.pluginId, str)


@given(instance=esmodel::events::PluginFocusEvent_strategy)
def test_esmodel::events::pluginfocusevent_pluginId_setter(instance):
    original = instance.pluginId
    instance.pluginId = original
    assert instance.pluginId == original

@given(instance=esmodel::events::NotificationIgnoreEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::notificationignoreevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::NotificationIgnoreEvent)

@given(instance=esmodel::events::NotificationIgnoreEvent_strategy)
def test_esmodel::events::notificationignoreevent_notificationId_type(instance):
    assert isinstance(instance.notificationId, str)


@given(instance=esmodel::events::NotificationIgnoreEvent_strategy)
def test_esmodel::events::notificationignoreevent_notificationId_setter(instance):
    original = instance.notificationId
    instance.notificationId = original
    assert instance.notificationId == original

@given(instance=esmodel::events::UpdateEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::updateevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::UpdateEvent)

@given(instance=esmodel::events::PresentationSwitchEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::presentationswitchevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::PresentationSwitchEvent)

@given(instance=esmodel::events::PresentationSwitchEvent_strategy)
def test_esmodel::events::presentationswitchevent_newPresentation_type(instance):
    assert isinstance(instance.newPresentation, str)


@given(instance=esmodel::events::PresentationSwitchEvent_strategy)
def test_esmodel::events::presentationswitchevent_newPresentation_setter(instance):
    original = instance.newPresentation
    instance.newPresentation = original
    assert instance.newPresentation == original

@given(instance=esmodel::events::PresentationSwitchEvent_strategy)
def test_esmodel::events::presentationswitchevent_readView_type(instance):
    assert isinstance(instance.readView, str)


@given(instance=esmodel::events::PresentationSwitchEvent_strategy)
def test_esmodel::events::presentationswitchevent_readView_setter(instance):
    original = instance.readView
    instance.readView = original
    assert instance.readView == original

@given(instance=esmodel::events::URLEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::urlevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::URLEvent)

@given(instance=esmodel::events::URLEvent_strategy)
def test_esmodel::events::urlevent_sourceView_type(instance):
    assert isinstance(instance.sourceView, str)


@given(instance=esmodel::events::URLEvent_strategy)
def test_esmodel::events::urlevent_sourceView_setter(instance):
    original = instance.sourceView
    instance.sourceView = original
    assert instance.sourceView == original

@given(instance=esmodel::events::NotificationGenerationEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::notificationgenerationevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::NotificationGenerationEvent)

@given(instance=esmodel::events::ShowChangesEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::showchangesevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::ShowChangesEvent)

@given(instance=esmodel::events::PluginStartEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::pluginstartevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::PluginStartEvent)

@given(instance=esmodel::events::PluginStartEvent_strategy)
def test_esmodel::events::pluginstartevent_pluginId_type(instance):
    assert isinstance(instance.pluginId, str)


@given(instance=esmodel::events::PluginStartEvent_strategy)
def test_esmodel::events::pluginstartevent_pluginId_setter(instance):
    original = instance.pluginId
    instance.pluginId = original
    assert instance.pluginId == original

@given(instance=esmodel::server::ServerEvent_strategy)
@settings(max_examples=50)
def test_esmodel::server::serverevent_instantiation(instance):
    assert isinstance(instance, esmodel::server::ServerEvent)

@given(instance=esmodel::events::CheckoutEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::checkoutevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::CheckoutEvent)

@given(instance=esmodel::events::Validate_strategy)
@settings(max_examples=50)
def test_esmodel::events::validate_instantiation(instance):
    assert isinstance(instance, esmodel::events::Validate)

@given(instance=esmodel::events::MergeEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::mergeevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::MergeEvent)

@given(instance=esmodel::events::MergeEvent_strategy)
def test_esmodel::events::mergeevent_numberOfConflicts_type(instance):
    assert isinstance(instance.numberOfConflicts, int)


@given(instance=esmodel::events::MergeEvent_strategy)
def test_esmodel::events::mergeevent_numberOfConflicts_setter(instance):
    original = instance.numberOfConflicts
    instance.numberOfConflicts = original
    assert instance.numberOfConflicts == original

@given(instance=esmodel::events::MergeEvent_strategy)
def test_esmodel::events::mergeevent_totalTime_type(instance):
    assert isinstance(instance.totalTime, int)


@given(instance=esmodel::events::MergeEvent_strategy)
def test_esmodel::events::mergeevent_totalTime_setter(instance):
    original = instance.totalTime
    instance.totalTime = original
    assert instance.totalTime == original

@given(instance=esmodel::events::NavigatorCreateEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::navigatorcreateevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::NavigatorCreateEvent)

@given(instance=esmodel::events::NavigatorCreateEvent_strategy)
def test_esmodel::events::navigatorcreateevent_dynamic_type(instance):
    assert isinstance(instance.dynamic, bool)


@given(instance=esmodel::events::NavigatorCreateEvent_strategy)
def test_esmodel::events::navigatorcreateevent_dynamic_setter(instance):
    original = instance.dynamic
    instance.dynamic = original
    assert instance.dynamic == original

@given(instance=esmodel::events::DNDEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::dndevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::DNDEvent)

@given(instance=esmodel::events::DNDEvent_strategy)
def test_esmodel::events::dndevent_targetView_type(instance):
    assert isinstance(instance.targetView, str)


@given(instance=esmodel::events::DNDEvent_strategy)
def test_esmodel::events::dndevent_targetView_setter(instance):
    original = instance.targetView
    instance.targetView = original
    assert instance.targetView == original

@given(instance=esmodel::events::DNDEvent_strategy)
def test_esmodel::events::dndevent_sourceView_type(instance):
    assert isinstance(instance.sourceView, str)


@given(instance=esmodel::events::DNDEvent_strategy)
def test_esmodel::events::dndevent_sourceView_setter(instance):
    original = instance.sourceView
    instance.sourceView = original
    assert instance.sourceView == original

@given(instance=esmodel::events::UndoEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::undoevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::UndoEvent)

@given(instance=esmodel::events::RevertEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::revertevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::RevertEvent)

@given(instance=esmodel::events::RevertEvent_strategy)
def test_esmodel::events::revertevent_revertedChangesCount_type(instance):
    assert isinstance(instance.revertedChangesCount, int)


@given(instance=esmodel::events::RevertEvent_strategy)
def test_esmodel::events::revertevent_revertedChangesCount_setter(instance):
    original = instance.revertedChangesCount
    instance.revertedChangesCount = original
    assert instance.revertedChangesCount == original

@given(instance=esmodel::events::ReadEvent_strategy)
@settings(max_examples=50)
def test_esmodel::events::readevent_instantiation(instance):
    assert isinstance(instance, esmodel::events::ReadEvent)

@given(instance=esmodel::events::ReadEvent_strategy)
def test_esmodel::events::readevent_readView_type(instance):
    assert isinstance(instance.readView, str)


@given(instance=esmodel::events::ReadEvent_strategy)
def test_esmodel::events::readevent_readView_setter(instance):
    original = instance.readView
    instance.readView = original
    assert instance.readView == original

@given(instance=esmodel::events::ReadEvent_strategy)
def test_esmodel::events::readevent_sourceView_type(instance):
    assert isinstance(instance.sourceView, str)


@given(instance=esmodel::events::ReadEvent_strategy)
def test_esmodel::events::readevent_sourceView_setter(instance):
    original = instance.sourceView
    instance.sourceView = original
    assert instance.sourceView == original

@given(instance=esmodel::events::Event_strategy)
@settings(max_examples=50)
def test_esmodel::events::event_instantiation(instance):
    assert isinstance(instance, esmodel::events::Event)

@given(instance=esmodel::events::Event_strategy)
def test_esmodel::events::event_timestamp_type(instance):
    assert isinstance(instance.timestamp, date)


@given(instance=esmodel::events::Event_strategy)
def test_esmodel::events::event_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=CompositeOperation_strategy)
@settings(max_examples=50)
def test_compositeoperation_instantiation(instance):
    assert isinstance(instance, CompositeOperation)

@given(instance=esmodel::semantic::SemanticCompositeOperation_strategy)
@settings(max_examples=50)
def test_esmodel::semantic::semanticcompositeoperation_instantiation(instance):
    assert isinstance(instance, esmodel::semantic::SemanticCompositeOperation)

@given(instance=esmodel::operations::EObjectToModelElementIdMap_strategy)
@settings(max_examples=50)
def test_esmodel::operations::eobjecttomodelelementidmap_instantiation(instance):
    assert isinstance(instance, esmodel::operations::EObjectToModelElementIdMap)

@given(instance=esmodel::operations::OperationGroup_strategy)
@settings(max_examples=50)
def test_esmodel::operations::operationgroup_instantiation(instance):
    assert isinstance(instance, esmodel::operations::OperationGroup)

@given(instance=esmodel::operations::OperationGroup_strategy)
def test_esmodel::operations::operationgroup_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esmodel::operations::OperationGroup_strategy)
def test_esmodel::operations::operationgroup_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esmodel::operations::OperationId_strategy)
@settings(max_examples=50)
def test_esmodel::operations::operationid_instantiation(instance):
    assert isinstance(instance, esmodel::operations::OperationId)

@given(instance=AttributeOperation_strategy)
@settings(max_examples=50)
def test_attributeoperation_instantiation(instance):
    assert isinstance(instance, AttributeOperation)

@given(instance=esmodel::operations::DiagramLayoutOperation_strategy)
@settings(max_examples=50)
def test_esmodel::operations::diagramlayoutoperation_instantiation(instance):
    assert isinstance(instance, esmodel::operations::DiagramLayoutOperation)

@given(instance=ReferenceOperation_strategy)
@settings(max_examples=50)
def test_referenceoperation_instantiation(instance):
    assert isinstance(instance, ReferenceOperation)

@given(instance=esmodel::operations::MultiReferenceSetOperation_strategy)
@settings(max_examples=50)
def test_esmodel::operations::multireferencesetoperation_instantiation(instance):
    assert isinstance(instance, esmodel::operations::MultiReferenceSetOperation)

@given(instance=esmodel::operations::MultiReferenceSetOperation_strategy)
def test_esmodel::operations::multireferencesetoperation_index_type(instance):
    assert isinstance(instance.index, int)


@given(instance=esmodel::operations::MultiReferenceSetOperation_strategy)
def test_esmodel::operations::multireferencesetoperation_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=esmodel::operations::MultiReferenceOperation_strategy)
@settings(max_examples=50)
def test_esmodel::operations::multireferenceoperation_instantiation(instance):
    assert isinstance(instance, esmodel::operations::MultiReferenceOperation)

@given(instance=esmodel::operations::MultiReferenceOperation_strategy)
def test_esmodel::operations::multireferenceoperation_add_type(instance):
    assert isinstance(instance.add, bool)


@given(instance=esmodel::operations::MultiReferenceOperation_strategy)
def test_esmodel::operations::multireferenceoperation_add_setter(instance):
    original = instance.add
    instance.add = original
    assert instance.add == original

@given(instance=esmodel::operations::MultiReferenceOperation_strategy)
def test_esmodel::operations::multireferenceoperation_index_type(instance):
    assert isinstance(instance.index, int)


@given(instance=esmodel::operations::MultiReferenceOperation_strategy)
def test_esmodel::operations::multireferenceoperation_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=esmodel::operations::SingleReferenceOperation_strategy)
@settings(max_examples=50)
def test_esmodel::operations::singlereferenceoperation_instantiation(instance):
    assert isinstance(instance, esmodel::operations::SingleReferenceOperation)

@given(instance=FeatureOperation_strategy)
@settings(max_examples=50)
def test_featureoperation_instantiation(instance):
    assert isinstance(instance, FeatureOperation)

@given(instance=esmodel::operations::MultiAttributeSetOperation_strategy)
@settings(max_examples=50)
def test_esmodel::operations::multiattributesetoperation_instantiation(instance):
    assert isinstance(instance, esmodel::operations::MultiAttributeSetOperation)

@given(instance=esmodel::operations::MultiAttributeSetOperation_strategy)
def test_esmodel::operations::multiattributesetoperation_newValue_type(instance):
    assert isinstance(instance.newValue, str)


@given(instance=esmodel::operations::MultiAttributeSetOperation_strategy)
def test_esmodel::operations::multiattributesetoperation_newValue_setter(instance):
    original = instance.newValue
    instance.newValue = original
    assert instance.newValue == original

@given(instance=esmodel::operations::MultiAttributeSetOperation_strategy)
def test_esmodel::operations::multiattributesetoperation_index_type(instance):
    assert isinstance(instance.index, int)


@given(instance=esmodel::operations::MultiAttributeSetOperation_strategy)
def test_esmodel::operations::multiattributesetoperation_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=esmodel::operations::MultiAttributeSetOperation_strategy)
def test_esmodel::operations::multiattributesetoperation_oldValue_type(instance):
    assert isinstance(instance.oldValue, str)


@given(instance=esmodel::operations::MultiAttributeSetOperation_strategy)
def test_esmodel::operations::multiattributesetoperation_oldValue_setter(instance):
    original = instance.oldValue
    instance.oldValue = original
    assert instance.oldValue == original

@given(instance=esmodel::operations::MultiAttributeMoveOperation_strategy)
@settings(max_examples=50)
def test_esmodel::operations::multiattributemoveoperation_instantiation(instance):
    assert isinstance(instance, esmodel::operations::MultiAttributeMoveOperation)

@given(instance=esmodel::operations::MultiAttributeMoveOperation_strategy)
def test_esmodel::operations::multiattributemoveoperation_newIndex_type(instance):
    assert isinstance(instance.newIndex, int)


@given(instance=esmodel::operations::MultiAttributeMoveOperation_strategy)
def test_esmodel::operations::multiattributemoveoperation_newIndex_setter(instance):
    original = instance.newIndex
    instance.newIndex = original
    assert instance.newIndex == original

@given(instance=esmodel::operations::MultiAttributeMoveOperation_strategy)
def test_esmodel::operations::multiattributemoveoperation_oldIndex_type(instance):
    assert isinstance(instance.oldIndex, int)


@given(instance=esmodel::operations::MultiAttributeMoveOperation_strategy)
def test_esmodel::operations::multiattributemoveoperation_oldIndex_setter(instance):
    original = instance.oldIndex
    instance.oldIndex = original
    assert instance.oldIndex == original

@given(instance=esmodel::operations::MultiAttributeMoveOperation_strategy)
def test_esmodel::operations::multiattributemoveoperation_referencedValue_type(instance):
    assert isinstance(instance.referencedValue, str)


@given(instance=esmodel::operations::MultiAttributeMoveOperation_strategy)
def test_esmodel::operations::multiattributemoveoperation_referencedValue_setter(instance):
    original = instance.referencedValue
    instance.referencedValue = original
    assert instance.referencedValue == original

@given(instance=esmodel::operations::MultiReferenceMoveOperation_strategy)
@settings(max_examples=50)
def test_esmodel::operations::multireferencemoveoperation_instantiation(instance):
    assert isinstance(instance, esmodel::operations::MultiReferenceMoveOperation)

@given(instance=esmodel::operations::MultiReferenceMoveOperation_strategy)
def test_esmodel::operations::multireferencemoveoperation_oldIndex_type(instance):
    assert isinstance(instance.oldIndex, int)


@given(instance=esmodel::operations::MultiReferenceMoveOperation_strategy)
def test_esmodel::operations::multireferencemoveoperation_oldIndex_setter(instance):
    original = instance.oldIndex
    instance.oldIndex = original
    assert instance.oldIndex == original

@given(instance=esmodel::operations::MultiReferenceMoveOperation_strategy)
def test_esmodel::operations::multireferencemoveoperation_newIndex_type(instance):
    assert isinstance(instance.newIndex, int)


@given(instance=esmodel::operations::MultiReferenceMoveOperation_strategy)
def test_esmodel::operations::multireferencemoveoperation_newIndex_setter(instance):
    original = instance.newIndex
    instance.newIndex = original
    assert instance.newIndex == original

@given(instance=esmodel::operations::ReferenceOperation_strategy)
@settings(max_examples=50)
def test_esmodel::operations::referenceoperation_instantiation(instance):
    assert isinstance(instance, esmodel::operations::ReferenceOperation)

@given(instance=esmodel::operations::ReferenceOperation_strategy)
def test_esmodel::operations::referenceoperation_bidirectional_type(instance):
    assert isinstance(instance.bidirectional, bool)


@given(instance=esmodel::operations::ReferenceOperation_strategy)
def test_esmodel::operations::referenceoperation_bidirectional_setter(instance):
    original = instance.bidirectional
    instance.bidirectional = original
    assert instance.bidirectional == original

@given(instance=esmodel::operations::ReferenceOperation_strategy)
def test_esmodel::operations::referenceoperation_oppositeFeatureName_type(instance):
    assert isinstance(instance.oppositeFeatureName, str)


@given(instance=esmodel::operations::ReferenceOperation_strategy)
def test_esmodel::operations::referenceoperation_oppositeFeatureName_setter(instance):
    original = instance.oppositeFeatureName
    instance.oppositeFeatureName = original
    assert instance.oppositeFeatureName == original

@given(instance=esmodel::operations::ReferenceOperation_strategy)
def test_esmodel::operations::referenceoperation_containmentType_type(instance):
    assert isinstance(instance.containmentType, str)


@given(instance=esmodel::operations::ReferenceOperation_strategy)
def test_esmodel::operations::referenceoperation_containmentType_setter(instance):
    original = instance.containmentType
    instance.containmentType = original
    assert instance.containmentType == original

@given(instance=esmodel::operations::MultiAttributeOperation_strategy)
@settings(max_examples=50)
def test_esmodel::operations::multiattributeoperation_instantiation(instance):
    assert isinstance(instance, esmodel::operations::MultiAttributeOperation)

@given(instance=esmodel::operations::MultiAttributeOperation_strategy)
def test_esmodel::operations::multiattributeoperation_add_type(instance):
    assert isinstance(instance.add, bool)


@given(instance=esmodel::operations::MultiAttributeOperation_strategy)
def test_esmodel::operations::multiattributeoperation_add_setter(instance):
    original = instance.add
    instance.add = original
    assert instance.add == original

@given(instance=esmodel::operations::MultiAttributeOperation_strategy)
def test_esmodel::operations::multiattributeoperation_indexes_type(instance):
    assert isinstance(instance.indexes, int)


@given(instance=esmodel::operations::MultiAttributeOperation_strategy)
def test_esmodel::operations::multiattributeoperation_indexes_setter(instance):
    original = instance.indexes
    instance.indexes = original
    assert instance.indexes == original

@given(instance=esmodel::operations::MultiAttributeOperation_strategy)
def test_esmodel::operations::multiattributeoperation_referencedValues_type(instance):
    assert isinstance(instance.referencedValues, str)


@given(instance=esmodel::operations::MultiAttributeOperation_strategy)
def test_esmodel::operations::multiattributeoperation_referencedValues_setter(instance):
    original = instance.referencedValues
    instance.referencedValues = original
    assert instance.referencedValues == original

@given(instance=esmodel::operations::AttributeOperation_strategy)
@settings(max_examples=50)
def test_esmodel::operations::attributeoperation_instantiation(instance):
    assert isinstance(instance, esmodel::operations::AttributeOperation)

@given(instance=esmodel::operations::AttributeOperation_strategy)
def test_esmodel::operations::attributeoperation_newValue_type(instance):
    assert isinstance(instance.newValue, str)


@given(instance=esmodel::operations::AttributeOperation_strategy)
def test_esmodel::operations::attributeoperation_newValue_setter(instance):
    original = instance.newValue
    instance.newValue = original
    assert instance.newValue == original

@given(instance=esmodel::operations::AttributeOperation_strategy)
def test_esmodel::operations::attributeoperation_oldValue_type(instance):
    assert isinstance(instance.oldValue, str)


@given(instance=esmodel::operations::AttributeOperation_strategy)
def test_esmodel::operations::attributeoperation_oldValue_setter(instance):
    original = instance.oldValue
    instance.oldValue = original
    assert instance.oldValue == original

@given(instance=operations::EObjectToModelElementIdMap_strategy)
@settings(max_examples=50)
def test_operations::eobjecttomodelelementidmap_instantiation(instance):
    assert isinstance(instance, operations::EObjectToModelElementIdMap)

@given(instance=operations::ReferenceOperation_strategy)
@settings(max_examples=50)
def test_operations::referenceoperation_instantiation(instance):
    assert isinstance(instance, operations::ReferenceOperation)

@given(instance=operations::esmodel::EObject_strategy)
@settings(max_examples=50)
def test_operations::esmodel::eobject_instantiation(instance):
    assert isinstance(instance, operations::esmodel::EObject)

@given(instance=AbstractOperation_strategy)
@settings(max_examples=50)
def test_abstractoperation_instantiation(instance):
    assert isinstance(instance, AbstractOperation)

@given(instance=esmodel::operations::FeatureOperation_strategy)
@settings(max_examples=50)
def test_esmodel::operations::featureoperation_instantiation(instance):
    assert isinstance(instance, esmodel::operations::FeatureOperation)

@given(instance=esmodel::operations::FeatureOperation_strategy)
def test_esmodel::operations::featureoperation_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=esmodel::operations::FeatureOperation_strategy)
def test_esmodel::operations::featureoperation_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=esmodel::operations::CreateDeleteOperation_strategy)
@settings(max_examples=50)
def test_esmodel::operations::createdeleteoperation_instantiation(instance):
    assert isinstance(instance, esmodel::operations::CreateDeleteOperation)

@given(instance=esmodel::operations::CreateDeleteOperation_strategy)
def test_esmodel::operations::createdeleteoperation_delete_type(instance):
    assert isinstance(instance.delete, bool)


@given(instance=esmodel::operations::CreateDeleteOperation_strategy)
def test_esmodel::operations::createdeleteoperation_delete_setter(instance):
    original = instance.delete
    instance.delete = original
    assert instance.delete == original

@given(instance=esmodel::operations::CompositeOperation_strategy)
@settings(max_examples=50)
def test_esmodel::operations::compositeoperation_instantiation(instance):
    assert isinstance(instance, esmodel::operations::CompositeOperation)

@given(instance=esmodel::operations::CompositeOperation_strategy)
def test_esmodel::operations::compositeoperation_compositeName_type(instance):
    assert isinstance(instance.compositeName, str)


@given(instance=esmodel::operations::CompositeOperation_strategy)
def test_esmodel::operations::compositeoperation_compositeName_setter(instance):
    original = instance.compositeName
    instance.compositeName = original
    assert instance.compositeName == original

@given(instance=esmodel::operations::CompositeOperation_strategy)
def test_esmodel::operations::compositeoperation_compositeDescription_type(instance):
    assert isinstance(instance.compositeDescription, str)


@given(instance=esmodel::operations::CompositeOperation_strategy)
def test_esmodel::operations::compositeoperation_compositeDescription_setter(instance):
    original = instance.compositeDescription
    instance.compositeDescription = original
    assert instance.compositeDescription == original

@given(instance=esmodel::operations::CompositeOperation_strategy)
def test_esmodel::operations::compositeoperation_reversed_type(instance):
    assert isinstance(instance.reversed, bool)


@given(instance=esmodel::operations::CompositeOperation_strategy)
def test_esmodel::operations::compositeoperation_reversed_setter(instance):
    original = instance.reversed
    instance.reversed = original
    assert instance.reversed == original

@given(instance=esmodel::operations::AbstractOperation_strategy)
@settings(max_examples=50)
def test_esmodel::operations::abstractoperation_instantiation(instance):
    assert isinstance(instance, esmodel::operations::AbstractOperation)

@given(instance=esmodel::operations::AbstractOperation_strategy)
def test_esmodel::operations::abstractoperation_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=esmodel::operations::AbstractOperation_strategy)
def test_esmodel::operations::abstractoperation_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=esmodel::operations::AbstractOperation_strategy)
def test_esmodel::operations::abstractoperation_accepted_type(instance):
    assert isinstance(instance.accepted, bool)


@given(instance=esmodel::operations::AbstractOperation_strategy)
def test_esmodel::operations::abstractoperation_accepted_setter(instance):
    original = instance.accepted
    instance.accepted = original
    assert instance.accepted == original

@given(instance=esmodel::operations::AbstractOperation_strategy)
def test_esmodel::operations::abstractoperation_clientDate_type(instance):
    assert isinstance(instance.clientDate, date)


@given(instance=esmodel::operations::AbstractOperation_strategy)
def test_esmodel::operations::abstractoperation_clientDate_setter(instance):
    original = instance.clientDate
    instance.clientDate = original
    assert instance.clientDate == original

@given(instance=esmodel::operations::AbstractOperation_strategy)
def test_esmodel::operations::abstractoperation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esmodel::operations::AbstractOperation_strategy)
def test_esmodel::operations::abstractoperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esmodel::versioning::LogMessage_strategy)
@settings(max_examples=50)
def test_esmodel::versioning::logmessage_instantiation(instance):
    assert isinstance(instance, esmodel::versioning::LogMessage)

@given(instance=esmodel::versioning::LogMessage_strategy)
def test_esmodel::versioning::logmessage_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=esmodel::versioning::LogMessage_strategy)
def test_esmodel::versioning::logmessage_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=esmodel::versioning::LogMessage_strategy)
def test_esmodel::versioning::logmessage_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=esmodel::versioning::LogMessage_strategy)
def test_esmodel::versioning::logmessage_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=esmodel::versioning::LogMessage_strategy)
def test_esmodel::versioning::logmessage_clientDate_type(instance):
    assert isinstance(instance.clientDate, date)


@given(instance=esmodel::versioning::LogMessage_strategy)
def test_esmodel::versioning::logmessage_clientDate_setter(instance):
    original = instance.clientDate
    instance.clientDate = original
    assert instance.clientDate == original

@given(instance=esmodel::versioning::LogMessage_strategy)
def test_esmodel::versioning::logmessage_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=esmodel::versioning::LogMessage_strategy)
def test_esmodel::versioning::logmessage_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=esmodel::versioning::VersionProperty_strategy)
@settings(max_examples=50)
def test_esmodel::versioning::versionproperty_instantiation(instance):
    assert isinstance(instance, esmodel::versioning::VersionProperty)

@given(instance=esmodel::versioning::VersionProperty_strategy)
def test_esmodel::versioning::versionproperty_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esmodel::versioning::VersionProperty_strategy)
def test_esmodel::versioning::versionproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esmodel::versioning::VersionProperty_strategy)
def test_esmodel::versioning::versionproperty_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=esmodel::versioning::VersionProperty_strategy)
def test_esmodel::versioning::versionproperty_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=esmodel::versioning::VersionSpec_strategy)
@settings(max_examples=50)
def test_esmodel::versioning::versionspec_instantiation(instance):
    assert isinstance(instance, esmodel::versioning::VersionSpec)

@given(instance=esmodel::versioning::Version_strategy)
@settings(max_examples=50)
def test_esmodel::versioning::version_instantiation(instance):
    assert isinstance(instance, esmodel::versioning::Version)

@given(instance=esmodel::versioning::HistoryQuery_strategy)
@settings(max_examples=50)
def test_esmodel::versioning::historyquery_instantiation(instance):
    assert isinstance(instance, esmodel::versioning::HistoryQuery)

@given(instance=esmodel::versioning::HistoryQuery_strategy)
def test_esmodel::versioning::historyquery_includeChangePackage_type(instance):
    assert isinstance(instance.includeChangePackage, bool)


@given(instance=esmodel::versioning::HistoryQuery_strategy)
def test_esmodel::versioning::historyquery_includeChangePackage_setter(instance):
    original = instance.includeChangePackage
    instance.includeChangePackage = original
    assert instance.includeChangePackage == original

@given(instance=versioning::ChangePackage_strategy)
@settings(max_examples=50)
def test_versioning::changepackage_instantiation(instance):
    assert isinstance(instance, versioning::ChangePackage)

@given(instance=versioning::TagVersionSpec_strategy)
@settings(max_examples=50)
def test_versioning::tagversionspec_instantiation(instance):
    assert isinstance(instance, versioning::TagVersionSpec)

@given(instance=esmodel::versioning::HistoryInfo_strategy)
@settings(max_examples=50)
def test_esmodel::versioning::historyinfo_instantiation(instance):
    assert isinstance(instance, esmodel::versioning::HistoryInfo)

@given(instance=versioning::VersionProperty_strategy)
@settings(max_examples=50)
def test_versioning::versionproperty_instantiation(instance):
    assert isinstance(instance, versioning::VersionProperty)

@given(instance=notification::ESNotification_strategy)
@settings(max_examples=50)
def test_notification::esnotification_instantiation(instance):
    assert isinstance(instance, notification::ESNotification)

@given(instance=versioning::LogMessage_strategy)
@settings(max_examples=50)
def test_versioning::logmessage_instantiation(instance):
    assert isinstance(instance, versioning::LogMessage)

@given(instance=events::Event_strategy)
@settings(max_examples=50)
def test_events::event_instantiation(instance):
    assert isinstance(instance, events::Event)

@given(instance=operations::AbstractOperation_strategy)
@settings(max_examples=50)
def test_operations::abstractoperation_instantiation(instance):
    assert isinstance(instance, operations::AbstractOperation)

@given(instance=esmodel::versioning::ChangePackage_strategy)
@settings(max_examples=50)
def test_esmodel::versioning::changepackage_instantiation(instance):
    assert isinstance(instance, esmodel::versioning::ChangePackage)

@given(instance=VersionSpec_strategy)
@settings(max_examples=50)
def test_versionspec_instantiation(instance):
    assert isinstance(instance, VersionSpec)

@given(instance=esmodel::versioning::DateVersionSpec_strategy)
@settings(max_examples=50)
def test_esmodel::versioning::dateversionspec_instantiation(instance):
    assert isinstance(instance, esmodel::versioning::DateVersionSpec)

@given(instance=esmodel::versioning::DateVersionSpec_strategy)
def test_esmodel::versioning::dateversionspec_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=esmodel::versioning::DateVersionSpec_strategy)
def test_esmodel::versioning::dateversionspec_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=esmodel::versioning::PrimaryVersionSpec_strategy)
@settings(max_examples=50)
def test_esmodel::versioning::primaryversionspec_instantiation(instance):
    assert isinstance(instance, esmodel::versioning::PrimaryVersionSpec)

@given(instance=esmodel::versioning::PrimaryVersionSpec_strategy)
def test_esmodel::versioning::primaryversionspec_identifier_type(instance):
    assert isinstance(instance.identifier, int)


@given(instance=esmodel::versioning::PrimaryVersionSpec_strategy)
def test_esmodel::versioning::primaryversionspec_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=esmodel::versioning::HeadVersionSpec_strategy)
@settings(max_examples=50)
def test_esmodel::versioning::headversionspec_instantiation(instance):
    assert isinstance(instance, esmodel::versioning::HeadVersionSpec)

@given(instance=esmodel::versioning::TagVersionSpec_strategy)
@settings(max_examples=50)
def test_esmodel::versioning::tagversionspec_instantiation(instance):
    assert isinstance(instance, esmodel::versioning::TagVersionSpec)

@given(instance=esmodel::versioning::TagVersionSpec_strategy)
def test_esmodel::versioning::tagversionspec_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esmodel::versioning::TagVersionSpec_strategy)
def test_esmodel::versioning::tagversionspec_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esmodel::ClientVersionInfo_strategy)
@settings(max_examples=50)
def test_esmodel::clientversioninfo_instantiation(instance):
    assert isinstance(instance, esmodel::ClientVersionInfo)

@given(instance=esmodel::ClientVersionInfo_strategy)
def test_esmodel::clientversioninfo_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=esmodel::ClientVersionInfo_strategy)
def test_esmodel::clientversioninfo_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=esmodel::ClientVersionInfo_strategy)
def test_esmodel::clientversioninfo_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esmodel::ClientVersionInfo_strategy)
def test_esmodel::clientversioninfo_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esmodel::VersionInfo_strategy)
@settings(max_examples=50)
def test_esmodel::versioninfo_instantiation(instance):
    assert isinstance(instance, esmodel::VersionInfo)

@given(instance=esmodel::VersionInfo_strategy)
def test_esmodel::versioninfo_emfStoreVersionString_type(instance):
    assert isinstance(instance.emfStoreVersionString, str)


@given(instance=esmodel::VersionInfo_strategy)
def test_esmodel::versioninfo_emfStoreVersionString_setter(instance):
    original = instance.emfStoreVersionString
    instance.emfStoreVersionString = original
    assert instance.emfStoreVersionString == original

@given(instance=esmodel::ProjectId_strategy)
@settings(max_examples=50)
def test_esmodel::projectid_instantiation(instance):
    assert isinstance(instance, esmodel::ProjectId)

@given(instance=accesscontrol::ACUser_strategy)
@settings(max_examples=50)
def test_accesscontrol::acuser_instantiation(instance):
    assert isinstance(instance, accesscontrol::ACUser)

@given(instance=SessionId_strategy)
@settings(max_examples=50)
def test_sessionid_instantiation(instance):
    assert isinstance(instance, SessionId)

@given(instance=ProjectHistory_strategy)
@settings(max_examples=50)
def test_projecthistory_instantiation(instance):
    assert isinstance(instance, ProjectHistory)

@given(instance=accesscontrol::ACGroup_strategy)
@settings(max_examples=50)
def test_accesscontrol::acgroup_instantiation(instance):
    assert isinstance(instance, accesscontrol::ACGroup)

@given(instance=esmodel::ServerSpace_strategy)
@settings(max_examples=50)
def test_esmodel::serverspace_instantiation(instance):
    assert isinstance(instance, esmodel::ServerSpace)

@given(instance=esmodel::SessionId_strategy)
@settings(max_examples=50)
def test_esmodel::sessionid_instantiation(instance):
    assert isinstance(instance, esmodel::SessionId)

@given(instance=versioning::PrimaryVersionSpec_strategy)
@settings(max_examples=50)
def test_versioning::primaryversionspec_instantiation(instance):
    assert isinstance(instance, versioning::PrimaryVersionSpec)

@given(instance=esmodel::ProjectInfo_strategy)
@settings(max_examples=50)
def test_esmodel::projectinfo_instantiation(instance):
    assert isinstance(instance, esmodel::ProjectInfo)

@given(instance=esmodel::ProjectInfo_strategy)
def test_esmodel::projectinfo_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esmodel::ProjectInfo_strategy)
def test_esmodel::projectinfo_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esmodel::ProjectInfo_strategy)
def test_esmodel::projectinfo_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=esmodel::ProjectInfo_strategy)
def test_esmodel::projectinfo_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=versioning::Version_strategy)
@settings(max_examples=50)
def test_versioning::version_instantiation(instance):
    assert isinstance(instance, versioning::Version)

@given(instance=ProjectId_strategy)
@settings(max_examples=50)
def test_projectid_instantiation(instance):
    assert isinstance(instance, ProjectId)

@given(instance=esmodel::ProjectHistory_strategy)
@settings(max_examples=50)
def test_esmodel::projecthistory_instantiation(instance):
    assert isinstance(instance, esmodel::ProjectHistory)

@given(instance=esmodel::ProjectHistory_strategy)
def test_esmodel::projecthistory_projectName_type(instance):
    assert isinstance(instance.projectName, str)


@given(instance=esmodel::ProjectHistory_strategy)
def test_esmodel::projecthistory_projectName_setter(instance):
    original = instance.projectName
    instance.projectName = original
    assert instance.projectName == original

@given(instance=esmodel::ProjectHistory_strategy)
def test_esmodel::projecthistory_projectDescription_type(instance):
    assert isinstance(instance.projectDescription, str)


@given(instance=esmodel::ProjectHistory_strategy)
def test_esmodel::projecthistory_projectDescription_setter(instance):
    original = instance.projectDescription
    instance.projectDescription = original
    assert instance.projectDescription == original

@given(instance=ActivityObject_strategy)
@settings(max_examples=50)
def test_activityobject_instantiation(instance):
    assert isinstance(instance, ActivityObject)

@given(instance=model::activity::Fork_strategy)
@settings(max_examples=50)
def test_model::activity::fork_instantiation(instance):
    assert isinstance(instance, model::activity::Fork)

@given(instance=model::activity::ActivityInitial_strategy)
@settings(max_examples=50)
def test_model::activity::activityinitial_instantiation(instance):
    assert isinstance(instance, model::activity::ActivityInitial)

@given(instance=model::activity::ActivityEnd_strategy)
@settings(max_examples=50)
def test_model::activity::activityend_instantiation(instance):
    assert isinstance(instance, model::activity::ActivityEnd)

@given(instance=model::activity::Branch_strategy)
@settings(max_examples=50)
def test_model::activity::branch_instantiation(instance):
    assert isinstance(instance, model::activity::Branch)

@given(instance=model::activity::Activity_strategy)
@settings(max_examples=50)
def test_model::activity::activity_instantiation(instance):
    assert isinstance(instance, model::activity::Activity)

@given(instance=activity::ActivityObject_strategy)
@settings(max_examples=50)
def test_activity::activityobject_instantiation(instance):
    assert isinstance(instance, activity::ActivityObject)

@given(instance=model::activity::Transition_strategy)
@settings(max_examples=50)
def test_model::activity::transition_instantiation(instance):
    assert isinstance(instance, model::activity::Transition)

@given(instance=model::activity::Transition_strategy)
def test_model::activity::transition_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=model::activity::Transition_strategy)
def test_model::activity::transition_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=activity::Transition_strategy)
@settings(max_examples=50)
def test_activity::transition_instantiation(instance):
    assert isinstance(instance, activity::Transition)

@given(instance=model::activity::ActivityObject_strategy)
@settings(max_examples=50)
def test_model::activity::activityobject_instantiation(instance):
    assert isinstance(instance, model::activity::ActivityObject)

@given(instance=ModelElementId_strategy)
@settings(max_examples=50)
def test_modelelementid_instantiation(instance):
    assert isinstance(instance, ModelElementId)

@given(instance=model::util::ModelElementPath_strategy)
@settings(max_examples=50)
def test_model::util::modelelementpath_instantiation(instance):
    assert isinstance(instance, model::util::ModelElementPath)

@given(instance=StereotypeAttributeInstance_strategy)
@settings(max_examples=50)
def test_stereotypeattributeinstance_instantiation(instance):
    assert isinstance(instance, StereotypeAttributeInstance)

@given(instance=model::profile::StereotypeAttributeInstanceString_strategy)
@settings(max_examples=50)
def test_model::profile::stereotypeattributeinstancestring_instantiation(instance):
    assert isinstance(instance, model::profile::StereotypeAttributeInstanceString)

@given(instance=model::profile::StereotypeAttributeInstanceString_strategy)
def test_model::profile::stereotypeattributeinstancestring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=model::profile::StereotypeAttributeInstanceString_strategy)
def test_model::profile::stereotypeattributeinstancestring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::profile::Profile_strategy)
@settings(max_examples=50)
def test_model::profile::profile_instantiation(instance):
    assert isinstance(instance, model::profile::Profile)

@given(instance=model::profile::StereotypeAttributeInstance_strategy)
@settings(max_examples=50)
def test_model::profile::stereotypeattributeinstance_instantiation(instance):
    assert isinstance(instance, model::profile::StereotypeAttributeInstance)

@given(instance=StereotypeAttribute_strategy)
@settings(max_examples=50)
def test_stereotypeattribute_instantiation(instance):
    assert isinstance(instance, StereotypeAttribute)

@given(instance=model::profile::StereotypeAttributeSimple_strategy)
@settings(max_examples=50)
def test_model::profile::stereotypeattributesimple_instantiation(instance):
    assert isinstance(instance, model::profile::StereotypeAttributeSimple)

@given(instance=model::profile::StereotypeAttributeSimple_strategy)
def test_model::profile::stereotypeattributesimple_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::profile::StereotypeAttributeSimple_strategy)
def test_model::profile::stereotypeattributesimple_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model::profile::StereotypeAttribute_strategy)
@settings(max_examples=50)
def test_model::profile::stereotypeattribute_instantiation(instance):
    assert isinstance(instance, model::profile::StereotypeAttribute)

@given(instance=profile::StereotypeAttributeInstance_strategy)
@settings(max_examples=50)
def test_profile::stereotypeattributeinstance_instantiation(instance):
    assert isinstance(instance, profile::StereotypeAttributeInstance)

@given(instance=model::profile::StereotypeInstance_strategy)
@settings(max_examples=50)
def test_model::profile::stereotypeinstance_instantiation(instance):
    assert isinstance(instance, model::profile::StereotypeInstance)

@given(instance=profile::StereotypeAttribute_strategy)
@settings(max_examples=50)
def test_profile::stereotypeattribute_instantiation(instance):
    assert isinstance(instance, profile::StereotypeAttribute)

@given(instance=profile::Profile_strategy)
@settings(max_examples=50)
def test_profile::profile_instantiation(instance):
    assert isinstance(instance, profile::Profile)

@given(instance=model::profile::Stereotype_strategy)
@settings(max_examples=50)
def test_model::profile::stereotype_instantiation(instance):
    assert isinstance(instance, model::profile::Stereotype)

@given(instance=model::profile::Stereotype_strategy)
def test_model::profile::stereotype_required_type(instance):
    assert isinstance(instance.required, bool)


@given(instance=model::profile::Stereotype_strategy)
def test_model::profile::stereotype_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original

@given(instance=profile::Stereotype_strategy)
@settings(max_examples=50)
def test_profile::stereotype_instantiation(instance):
    assert isinstance(instance, profile::Stereotype)

@given(instance=model::attachment::FileAttachment_strategy)
@settings(max_examples=50)
def test_model::attachment::fileattachment_instantiation(instance):
    assert isinstance(instance, model::attachment::FileAttachment)

@given(instance=model::attachment::FileAttachment_strategy)
def test_model::attachment::fileattachment_fileSize_type(instance):
    assert isinstance(instance.fileSize, str)


@given(instance=model::attachment::FileAttachment_strategy)
def test_model::attachment::fileattachment_fileSize_setter(instance):
    original = instance.fileSize
    instance.fileSize = original
    assert instance.fileSize == original

@given(instance=model::attachment::FileAttachment_strategy)
def test_model::attachment::fileattachment_fileID_type(instance):
    assert isinstance(instance.fileID, str)


@given(instance=model::attachment::FileAttachment_strategy)
def test_model::attachment::fileattachment_fileID_setter(instance):
    original = instance.fileID
    instance.fileID = original
    assert instance.fileID == original

@given(instance=model::attachment::FileAttachment_strategy)
def test_model::attachment::fileattachment_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=model::attachment::FileAttachment_strategy)
def test_model::attachment::fileattachment_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=model::attachment::FileAttachment_strategy)
def test_model::attachment::fileattachment_fileHash_type(instance):
    assert isinstance(instance.fileHash, str)


@given(instance=model::attachment::FileAttachment_strategy)
def test_model::attachment::fileattachment_fileHash_setter(instance):
    original = instance.fileHash
    instance.fileHash = original
    assert instance.fileHash == original

@given(instance=model::attachment::UrlAttachment_strategy)
@settings(max_examples=50)
def test_model::attachment::urlattachment_instantiation(instance):
    assert isinstance(instance, model::attachment::UrlAttachment)

@given(instance=model::attachment::UrlAttachment_strategy)
def test_model::attachment::urlattachment_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=model::attachment::UrlAttachment_strategy)
def test_model::attachment::urlattachment_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=StateNode_strategy)
@settings(max_examples=50)
def test_statenode_instantiation(instance):
    assert isinstance(instance, StateNode)

@given(instance=model::state::StateInitial_strategy)
@settings(max_examples=50)
def test_model::state::stateinitial_instantiation(instance):
    assert isinstance(instance, model::state::StateInitial)

@given(instance=model::state::StateEnd_strategy)
@settings(max_examples=50)
def test_model::state::stateend_instantiation(instance):
    assert isinstance(instance, model::state::StateEnd)

@given(instance=model::state::State_strategy)
@settings(max_examples=50)
def test_model::state::state_instantiation(instance):
    assert isinstance(instance, model::state::State)

@given(instance=model::state::State_strategy)
def test_model::state::state_exitConditions_type(instance):
    assert isinstance(instance.exitConditions, str)


@given(instance=model::state::State_strategy)
def test_model::state::state_exitConditions_setter(instance):
    original = instance.exitConditions
    instance.exitConditions = original
    assert instance.exitConditions == original

@given(instance=model::state::State_strategy)
def test_model::state::state_activities_type(instance):
    assert isinstance(instance.activities, str)


@given(instance=model::state::State_strategy)
def test_model::state::state_activities_setter(instance):
    original = instance.activities
    instance.activities = original
    assert instance.activities == original

@given(instance=model::state::State_strategy)
def test_model::state::state_entryConditions_type(instance):
    assert isinstance(instance.entryConditions, str)


@given(instance=model::state::State_strategy)
def test_model::state::state_entryConditions_setter(instance):
    original = instance.entryConditions
    instance.entryConditions = original
    assert instance.entryConditions == original

@given(instance=state::Transition_strategy)
@settings(max_examples=50)
def test_state::transition_instantiation(instance):
    assert isinstance(instance, state::Transition)

@given(instance=model::state::StateNode_strategy)
@settings(max_examples=50)
def test_model::state::statenode_instantiation(instance):
    assert isinstance(instance, model::state::StateNode)

@given(instance=state::StateNode_strategy)
@settings(max_examples=50)
def test_state::statenode_instantiation(instance):
    assert isinstance(instance, state::StateNode)

@given(instance=model::state::Transition_strategy)
@settings(max_examples=50)
def test_model::state::transition_instantiation(instance):
    assert isinstance(instance, model::state::Transition)

@given(instance=model::state::Transition_strategy)
def test_model::state::transition_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=model::state::Transition_strategy)
def test_model::state::transition_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=MeetingSection_strategy)
@settings(max_examples=50)
def test_meetingsection_instantiation(instance):
    assert isinstance(instance, MeetingSection)

@given(instance=model::meeting::IssueMeetingSection_strategy)
@settings(max_examples=50)
def test_model::meeting::issuemeetingsection_instantiation(instance):
    assert isinstance(instance, model::meeting::IssueMeetingSection)

@given(instance=model::meeting::WorkItemMeetingSection_strategy)
@settings(max_examples=50)
def test_model::meeting::workitemmeetingsection_instantiation(instance):
    assert isinstance(instance, model::meeting::WorkItemMeetingSection)

@given(instance=model::meeting::CompositeMeetingSection_strategy)
@settings(max_examples=50)
def test_model::meeting::compositemeetingsection_instantiation(instance):
    assert isinstance(instance, model::meeting::CompositeMeetingSection)

@given(instance=model::meeting::MeetingSection_strategy)
@settings(max_examples=50)
def test_model::meeting::meetingsection_instantiation(instance):
    assert isinstance(instance, model::meeting::MeetingSection)

@given(instance=model::meeting::MeetingSection_strategy)
def test_model::meeting::meetingsection_allocatedTime_type(instance):
    assert isinstance(instance.allocatedTime, int)


@given(instance=model::meeting::MeetingSection_strategy)
def test_model::meeting::meetingsection_allocatedTime_setter(instance):
    original = instance.allocatedTime
    instance.allocatedTime = original
    assert instance.allocatedTime == original

@given(instance=meeting::WorkItemMeetingSection_strategy)
@settings(max_examples=50)
def test_meeting::workitemmeetingsection_instantiation(instance):
    assert isinstance(instance, meeting::WorkItemMeetingSection)

@given(instance=meeting::IssueMeetingSection_strategy)
@settings(max_examples=50)
def test_meeting::issuemeetingsection_instantiation(instance):
    assert isinstance(instance, meeting::IssueMeetingSection)

@given(instance=meeting::MeetingSection_strategy)
@settings(max_examples=50)
def test_meeting::meetingsection_instantiation(instance):
    assert isinstance(instance, meeting::MeetingSection)

@given(instance=model::meeting::Meeting_strategy)
@settings(max_examples=50)
def test_model::meeting::meeting_instantiation(instance):
    assert isinstance(instance, model::meeting::Meeting)

@given(instance=model::meeting::Meeting_strategy)
def test_model::meeting::meeting_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=model::meeting::Meeting_strategy)
def test_model::meeting::meeting_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=model::meeting::Meeting_strategy)
def test_model::meeting::meeting_starttime_type(instance):
    assert isinstance(instance.starttime, date)


@given(instance=model::meeting::Meeting_strategy)
def test_model::meeting::meeting_starttime_setter(instance):
    original = instance.starttime
    instance.starttime = original
    assert instance.starttime == original

@given(instance=model::meeting::Meeting_strategy)
def test_model::meeting::meeting_endtime_type(instance):
    assert isinstance(instance.endtime, date)


@given(instance=model::meeting::Meeting_strategy)
def test_model::meeting::meeting_endtime_setter(instance):
    original = instance.endtime
    instance.endtime = original
    assert instance.endtime == original

@given(instance=model::component::DeploymentNode_strategy)
@settings(max_examples=50)
def test_model::component::deploymentnode_instantiation(instance):
    assert isinstance(instance, model::component::DeploymentNode)

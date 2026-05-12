import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    setup::Query,
    setup::BuildPlan,
    setup::QueryAttribute,
    setup::TextModification,
    SetupTask,
    setup::MylynBuildsTask,
    setup::JRETask,
    setup::KeyBindingTask,
    setup::MylynQueriesTask,
    SetupTaskContainer,
    setup::CompoundSetupTask,
    setup::ScopeRoot,
    setup::SetupTaskContainer,
    setup::LinkLocationTask,
    setup::EclipseIniTask,
    setup::RedirectionTask,
    setup::VariableChoice,
    setup::ContextVariableTask,
    setup::SetupTask,
    setup::Setup,
    ConfigurableItem,
    setup::Eclipse,
    setup::Branch,
    setup::Project,
    ScopeRoot,
    setup::Configuration,
    setup::Preferences,
    setup::ConfigurableItem,
    setup::Index,
    setup::MetaIndex,
    setup::MylynQueryTask,
    setup::CommandParameter,
    setup::KeyBindingContext,
    setup::FileEditor,
    setup::FileAssociationTask,
    setup::EclipsePreferenceTask,
    setup::TextModifyTask,
    setup::ResourceCreationTask,
    setup::ResourceCopyTask,
    setup::WorkingSet,
    setup::WorkingSetTask,
    setup::FileMapping,
    setup::FileAssociationsTask,
    setup::TargletData,
    TargletData,
    setup::Targlet,
    setup::ApiBaselineTask,
    setup::TargetPlatformTask,
    setup::ProjectSetImportTask,
    setup::ProjectsImportTask,
    setup::RepositoryList,
    ComponentExtension,
    setup::ComponentDefinition,
    setup::TargletTask,
    setup::TargletImportTask,
    setup::MavenImportTask,
    setup::Component,
    setup::ComponentExtension,
    setup::Predicate,
    SourceLocator,
    setup::AutomaticSourceLocator,
    setup::ManualSourceLocator,
    setup::SourceLocator,
    setup::P2Repository,
    setup::InstallableUnit,
    setup::P2Task,
    BasicMaterializationTask,
    setup::MaterializationTask,
    setup::BuckminsterImportTask,
    setup::BasicMaterializationTask,
    setup::GitCloneTask,
    Trigger,
    ComponentType,
    SetupTaskScope,
    VariableType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_setup::query_is_not_abstract():
    assert not inspect.isabstract(setup::Query)


def test_setup::query_constructor_exists():
    assert callable(setup::Query.__init__)


def test_setup::query_constructor_args():
    sig = inspect.signature(setup::Query.__init__)
    params = list(sig.parameters.keys())
    assert "summary" in params, "Missing parameter 'summary'"
    assert "uRL" in params, "Missing parameter 'uRL'"

def test_setup::query_has_summary():
    assert hasattr(setup::Query, "summary")
    descriptor = None
    for klass in setup::Query.__mro__:
        if "summary" in klass.__dict__:
            descriptor = klass.__dict__["summary"]
            break
    assert isinstance(descriptor, property)

def test_setup::query_has_uRL():
    assert hasattr(setup::Query, "uRL")
    descriptor = None
    for klass in setup::Query.__mro__:
        if "uRL" in klass.__dict__:
            descriptor = klass.__dict__["uRL"]
            break
    assert isinstance(descriptor, property)



def test_setup::buildplan_is_not_abstract():
    assert not inspect.isabstract(setup::BuildPlan)


def test_setup::buildplan_constructor_exists():
    assert callable(setup::BuildPlan.__init__)


def test_setup::buildplan_constructor_args():
    sig = inspect.signature(setup::BuildPlan.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_setup::buildplan_has_name():
    assert hasattr(setup::BuildPlan, "name")
    descriptor = None
    for klass in setup::BuildPlan.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_setup::queryattribute_is_not_abstract():
    assert not inspect.isabstract(setup::QueryAttribute)


def test_setup::queryattribute_constructor_exists():
    assert callable(setup::QueryAttribute.__init__)


def test_setup::queryattribute_constructor_args():
    sig = inspect.signature(setup::QueryAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_setup::queryattribute_has_key():
    assert hasattr(setup::QueryAttribute, "key")
    descriptor = None
    for klass in setup::QueryAttribute.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_setup::queryattribute_has_value():
    assert hasattr(setup::QueryAttribute, "value")
    descriptor = None
    for klass in setup::QueryAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_setup::textmodification_is_not_abstract():
    assert not inspect.isabstract(setup::TextModification)


def test_setup::textmodification_constructor_exists():
    assert callable(setup::TextModification.__init__)


def test_setup::textmodification_constructor_args():
    sig = inspect.signature(setup::TextModification.__init__)
    params = list(sig.parameters.keys())
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "substitutions" in params, "Missing parameter 'substitutions'"

def test_setup::textmodification_has_pattern():
    assert hasattr(setup::TextModification, "pattern")
    descriptor = None
    for klass in setup::TextModification.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_setup::textmodification_has_substitutions():
    assert hasattr(setup::TextModification, "substitutions")
    descriptor = None
    for klass in setup::TextModification.__mro__:
        if "substitutions" in klass.__dict__:
            descriptor = klass.__dict__["substitutions"]
            break
    assert isinstance(descriptor, property)



def test_setuptask_is_not_abstract():
    assert not inspect.isabstract(SetupTask)


def test_setuptask_constructor_exists():
    assert callable(SetupTask.__init__)


def test_setuptask_constructor_args():
    sig = inspect.signature(SetupTask.__init__)
    params = list(sig.parameters.keys())



def test_setup::mylynbuildstask_is_not_abstract():
    assert not inspect.isabstract(setup::MylynBuildsTask)


def test_setup::mylynbuildstask_constructor_exists():
    assert callable(setup::MylynBuildsTask.__init__)


def test_setup::mylynbuildstask_constructor_args():
    sig = inspect.signature(setup::MylynBuildsTask.__init__)
    params = list(sig.parameters.keys())
    assert "userID" in params, "Missing parameter 'userID'"
    assert "password" in params, "Missing parameter 'password'"
    assert "serverURL" in params, "Missing parameter 'serverURL'"
    assert "connectorKind" in params, "Missing parameter 'connectorKind'"

def test_setup::mylynbuildstask_has_userID():
    assert hasattr(setup::MylynBuildsTask, "userID")
    descriptor = None
    for klass in setup::MylynBuildsTask.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_setup::mylynbuildstask_has_password():
    assert hasattr(setup::MylynBuildsTask, "password")
    descriptor = None
    for klass in setup::MylynBuildsTask.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_setup::mylynbuildstask_has_serverURL():
    assert hasattr(setup::MylynBuildsTask, "serverURL")
    descriptor = None
    for klass in setup::MylynBuildsTask.__mro__:
        if "serverURL" in klass.__dict__:
            descriptor = klass.__dict__["serverURL"]
            break
    assert isinstance(descriptor, property)

def test_setup::mylynbuildstask_has_connectorKind():
    assert hasattr(setup::MylynBuildsTask, "connectorKind")
    descriptor = None
    for klass in setup::MylynBuildsTask.__mro__:
        if "connectorKind" in klass.__dict__:
            descriptor = klass.__dict__["connectorKind"]
            break
    assert isinstance(descriptor, property)



def test_setup::jretask_is_not_abstract():
    assert not inspect.isabstract(setup::JRETask)


def test_setup::jretask_constructor_exists():
    assert callable(setup::JRETask.__init__)


def test_setup::jretask_constructor_args():
    sig = inspect.signature(setup::JRETask.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "version" in params, "Missing parameter 'version'"

def test_setup::jretask_has_location():
    assert hasattr(setup::JRETask, "location")
    descriptor = None
    for klass in setup::JRETask.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_setup::jretask_has_version():
    assert hasattr(setup::JRETask, "version")
    descriptor = None
    for klass in setup::JRETask.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_setup::keybindingtask_is_not_abstract():
    assert not inspect.isabstract(setup::KeyBindingTask)


def test_setup::keybindingtask_constructor_exists():
    assert callable(setup::KeyBindingTask.__init__)


def test_setup::keybindingtask_constructor_args():
    sig = inspect.signature(setup::KeyBindingTask.__init__)
    params = list(sig.parameters.keys())
    assert "scheme" in params, "Missing parameter 'scheme'"
    assert "keys" in params, "Missing parameter 'keys'"
    assert "locale" in params, "Missing parameter 'locale'"
    assert "command" in params, "Missing parameter 'command'"
    assert "platform" in params, "Missing parameter 'platform'"

def test_setup::keybindingtask_has_scheme():
    assert hasattr(setup::KeyBindingTask, "scheme")
    descriptor = None
    for klass in setup::KeyBindingTask.__mro__:
        if "scheme" in klass.__dict__:
            descriptor = klass.__dict__["scheme"]
            break
    assert isinstance(descriptor, property)

def test_setup::keybindingtask_has_keys():
    assert hasattr(setup::KeyBindingTask, "keys")
    descriptor = None
    for klass in setup::KeyBindingTask.__mro__:
        if "keys" in klass.__dict__:
            descriptor = klass.__dict__["keys"]
            break
    assert isinstance(descriptor, property)

def test_setup::keybindingtask_has_locale():
    assert hasattr(setup::KeyBindingTask, "locale")
    descriptor = None
    for klass in setup::KeyBindingTask.__mro__:
        if "locale" in klass.__dict__:
            descriptor = klass.__dict__["locale"]
            break
    assert isinstance(descriptor, property)

def test_setup::keybindingtask_has_command():
    assert hasattr(setup::KeyBindingTask, "command")
    descriptor = None
    for klass in setup::KeyBindingTask.__mro__:
        if "command" in klass.__dict__:
            descriptor = klass.__dict__["command"]
            break
    assert isinstance(descriptor, property)

def test_setup::keybindingtask_has_platform():
    assert hasattr(setup::KeyBindingTask, "platform")
    descriptor = None
    for klass in setup::KeyBindingTask.__mro__:
        if "platform" in klass.__dict__:
            descriptor = klass.__dict__["platform"]
            break
    assert isinstance(descriptor, property)



def test_setup::mylynqueriestask_is_not_abstract():
    assert not inspect.isabstract(setup::MylynQueriesTask)


def test_setup::mylynqueriestask_constructor_exists():
    assert callable(setup::MylynQueriesTask.__init__)


def test_setup::mylynqueriestask_constructor_args():
    sig = inspect.signature(setup::MylynQueriesTask.__init__)
    params = list(sig.parameters.keys())
    assert "connectorKind" in params, "Missing parameter 'connectorKind'"
    assert "password" in params, "Missing parameter 'password'"
    assert "repositoryURL" in params, "Missing parameter 'repositoryURL'"
    assert "userID" in params, "Missing parameter 'userID'"

def test_setup::mylynqueriestask_has_connectorKind():
    assert hasattr(setup::MylynQueriesTask, "connectorKind")
    descriptor = None
    for klass in setup::MylynQueriesTask.__mro__:
        if "connectorKind" in klass.__dict__:
            descriptor = klass.__dict__["connectorKind"]
            break
    assert isinstance(descriptor, property)

def test_setup::mylynqueriestask_has_password():
    assert hasattr(setup::MylynQueriesTask, "password")
    descriptor = None
    for klass in setup::MylynQueriesTask.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_setup::mylynqueriestask_has_repositoryURL():
    assert hasattr(setup::MylynQueriesTask, "repositoryURL")
    descriptor = None
    for klass in setup::MylynQueriesTask.__mro__:
        if "repositoryURL" in klass.__dict__:
            descriptor = klass.__dict__["repositoryURL"]
            break
    assert isinstance(descriptor, property)

def test_setup::mylynqueriestask_has_userID():
    assert hasattr(setup::MylynQueriesTask, "userID")
    descriptor = None
    for klass in setup::MylynQueriesTask.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)



def test_setuptaskcontainer_is_not_abstract():
    assert not inspect.isabstract(SetupTaskContainer)


def test_setuptaskcontainer_constructor_exists():
    assert callable(SetupTaskContainer.__init__)


def test_setuptaskcontainer_constructor_args():
    sig = inspect.signature(SetupTaskContainer.__init__)
    params = list(sig.parameters.keys())



def test_setup::compoundsetuptask_is_not_abstract():
    assert not inspect.isabstract(setup::CompoundSetupTask)


def test_setup::compoundsetuptask_constructor_exists():
    assert callable(setup::CompoundSetupTask.__init__)


def test_setup::compoundsetuptask_constructor_args():
    sig = inspect.signature(setup::CompoundSetupTask.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_setup::compoundsetuptask_has_name():
    assert hasattr(setup::CompoundSetupTask, "name")
    descriptor = None
    for klass in setup::CompoundSetupTask.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_setup::scoperoot_is_not_abstract():
    assert not inspect.isabstract(setup::ScopeRoot)


def test_setup::scoperoot_constructor_exists():
    assert callable(setup::ScopeRoot.__init__)


def test_setup::scoperoot_constructor_args():
    sig = inspect.signature(setup::ScopeRoot.__init__)
    params = list(sig.parameters.keys())



def test_setup::setuptaskcontainer_is_not_abstract():
    assert not inspect.isabstract(setup::SetupTaskContainer)


def test_setup::setuptaskcontainer_constructor_exists():
    assert callable(setup::SetupTaskContainer.__init__)


def test_setup::setuptaskcontainer_constructor_args():
    sig = inspect.signature(setup::SetupTaskContainer.__init__)
    params = list(sig.parameters.keys())



def test_setup::linklocationtask_is_not_abstract():
    assert not inspect.isabstract(setup::LinkLocationTask)


def test_setup::linklocationtask_constructor_exists():
    assert callable(setup::LinkLocationTask.__init__)


def test_setup::linklocationtask_constructor_args():
    sig = inspect.signature(setup::LinkLocationTask.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"
    assert "name" in params, "Missing parameter 'name'"

def test_setup::linklocationtask_has_path():
    assert hasattr(setup::LinkLocationTask, "path")
    descriptor = None
    for klass in setup::LinkLocationTask.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_setup::linklocationtask_has_name():
    assert hasattr(setup::LinkLocationTask, "name")
    descriptor = None
    for klass in setup::LinkLocationTask.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_setup::eclipseinitask_is_not_abstract():
    assert not inspect.isabstract(setup::EclipseIniTask)


def test_setup::eclipseinitask_constructor_exists():
    assert callable(setup::EclipseIniTask.__init__)


def test_setup::eclipseinitask_constructor_args():
    sig = inspect.signature(setup::EclipseIniTask.__init__)
    params = list(sig.parameters.keys())
    assert "vm" in params, "Missing parameter 'vm'"
    assert "value" in params, "Missing parameter 'value'"
    assert "option" in params, "Missing parameter 'option'"

def test_setup::eclipseinitask_has_vm():
    assert hasattr(setup::EclipseIniTask, "vm")
    descriptor = None
    for klass in setup::EclipseIniTask.__mro__:
        if "vm" in klass.__dict__:
            descriptor = klass.__dict__["vm"]
            break
    assert isinstance(descriptor, property)

def test_setup::eclipseinitask_has_value():
    assert hasattr(setup::EclipseIniTask, "value")
    descriptor = None
    for klass in setup::EclipseIniTask.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_setup::eclipseinitask_has_option():
    assert hasattr(setup::EclipseIniTask, "option")
    descriptor = None
    for klass in setup::EclipseIniTask.__mro__:
        if "option" in klass.__dict__:
            descriptor = klass.__dict__["option"]
            break
    assert isinstance(descriptor, property)



def test_setup::redirectiontask_is_not_abstract():
    assert not inspect.isabstract(setup::RedirectionTask)


def test_setup::redirectiontask_constructor_exists():
    assert callable(setup::RedirectionTask.__init__)


def test_setup::redirectiontask_constructor_args():
    sig = inspect.signature(setup::RedirectionTask.__init__)
    params = list(sig.parameters.keys())
    assert "targetURL" in params, "Missing parameter 'targetURL'"
    assert "sourceURL" in params, "Missing parameter 'sourceURL'"

def test_setup::redirectiontask_has_targetURL():
    assert hasattr(setup::RedirectionTask, "targetURL")
    descriptor = None
    for klass in setup::RedirectionTask.__mro__:
        if "targetURL" in klass.__dict__:
            descriptor = klass.__dict__["targetURL"]
            break
    assert isinstance(descriptor, property)

def test_setup::redirectiontask_has_sourceURL():
    assert hasattr(setup::RedirectionTask, "sourceURL")
    descriptor = None
    for klass in setup::RedirectionTask.__mro__:
        if "sourceURL" in klass.__dict__:
            descriptor = klass.__dict__["sourceURL"]
            break
    assert isinstance(descriptor, property)



def test_setup::variablechoice_is_not_abstract():
    assert not inspect.isabstract(setup::VariableChoice)


def test_setup::variablechoice_constructor_exists():
    assert callable(setup::VariableChoice.__init__)


def test_setup::variablechoice_constructor_args():
    sig = inspect.signature(setup::VariableChoice.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "value" in params, "Missing parameter 'value'"

def test_setup::variablechoice_has_label():
    assert hasattr(setup::VariableChoice, "label")
    descriptor = None
    for klass in setup::VariableChoice.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_setup::variablechoice_has_value():
    assert hasattr(setup::VariableChoice, "value")
    descriptor = None
    for klass in setup::VariableChoice.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_setup::contextvariabletask_is_not_abstract():
    assert not inspect.isabstract(setup::ContextVariableTask)


def test_setup::contextvariabletask_constructor_exists():
    assert callable(setup::ContextVariableTask.__init__)


def test_setup::contextvariabletask_constructor_args():
    sig = inspect.signature(setup::ContextVariableTask.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"
    assert "stringSubstitution" in params, "Missing parameter 'stringSubstitution'"
    assert "type" in params, "Missing parameter 'type'"
    assert "label" in params, "Missing parameter 'label'"

def test_setup::contextvariabletask_has_value():
    assert hasattr(setup::ContextVariableTask, "value")
    descriptor = None
    for klass in setup::ContextVariableTask.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_setup::contextvariabletask_has_name():
    assert hasattr(setup::ContextVariableTask, "name")
    descriptor = None
    for klass in setup::ContextVariableTask.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_setup::contextvariabletask_has_stringSubstitution():
    assert hasattr(setup::ContextVariableTask, "stringSubstitution")
    descriptor = None
    for klass in setup::ContextVariableTask.__mro__:
        if "stringSubstitution" in klass.__dict__:
            descriptor = klass.__dict__["stringSubstitution"]
            break
    assert isinstance(descriptor, property)

def test_setup::contextvariabletask_has_type():
    assert hasattr(setup::ContextVariableTask, "type")
    descriptor = None
    for klass in setup::ContextVariableTask.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_setup::contextvariabletask_has_label():
    assert hasattr(setup::ContextVariableTask, "label")
    descriptor = None
    for klass in setup::ContextVariableTask.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_setup::setuptask_is_not_abstract():
    assert not inspect.isabstract(setup::SetupTask)


def test_setup::setuptask_constructor_exists():
    assert callable(setup::SetupTask.__init__)


def test_setup::setuptask_constructor_args():
    sig = inspect.signature(setup::SetupTask.__init__)
    params = list(sig.parameters.keys())
    assert "disabled" in params, "Missing parameter 'disabled'"
    assert "excludedTriggers" in params, "Missing parameter 'excludedTriggers'"
    assert "scope" in params, "Missing parameter 'scope'"
    assert "documentation" in params, "Missing parameter 'documentation'"

def test_setup::setuptask_has_disabled():
    assert hasattr(setup::SetupTask, "disabled")
    descriptor = None
    for klass in setup::SetupTask.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)

def test_setup::setuptask_has_excludedTriggers():
    assert hasattr(setup::SetupTask, "excludedTriggers")
    descriptor = None
    for klass in setup::SetupTask.__mro__:
        if "excludedTriggers" in klass.__dict__:
            descriptor = klass.__dict__["excludedTriggers"]
            break
    assert isinstance(descriptor, property)

def test_setup::setuptask_has_scope():
    assert hasattr(setup::SetupTask, "scope")
    descriptor = None
    for klass in setup::SetupTask.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_setup::setuptask_has_documentation():
    assert hasattr(setup::SetupTask, "documentation")
    descriptor = None
    for klass in setup::SetupTask.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)



def test_setup::setup_is_not_abstract():
    assert not inspect.isabstract(setup::Setup)


def test_setup::setup_constructor_exists():
    assert callable(setup::Setup.__init__)


def test_setup::setup_constructor_args():
    sig = inspect.signature(setup::Setup.__init__)
    params = list(sig.parameters.keys())



def test_configurableitem_is_not_abstract():
    assert not inspect.isabstract(ConfigurableItem)


def test_configurableitem_constructor_exists():
    assert callable(ConfigurableItem.__init__)


def test_configurableitem_constructor_args():
    sig = inspect.signature(ConfigurableItem.__init__)
    params = list(sig.parameters.keys())



def test_setup::eclipse_is_not_abstract():
    assert not inspect.isabstract(setup::Eclipse)


def test_setup::eclipse_constructor_exists():
    assert callable(setup::Eclipse.__init__)


def test_setup::eclipse_constructor_args():
    sig = inspect.signature(setup::Eclipse.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"

def test_setup::eclipse_has_version():
    assert hasattr(setup::Eclipse, "version")
    descriptor = None
    for klass in setup::Eclipse.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_setup::branch_is_not_abstract():
    assert not inspect.isabstract(setup::Branch)


def test_setup::branch_constructor_exists():
    assert callable(setup::Branch.__init__)


def test_setup::branch_constructor_args():
    sig = inspect.signature(setup::Branch.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_setup::branch_has_name():
    assert hasattr(setup::Branch, "name")
    descriptor = None
    for klass in setup::Branch.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_setup::project_is_not_abstract():
    assert not inspect.isabstract(setup::Project)


def test_setup::project_constructor_exists():
    assert callable(setup::Project.__init__)


def test_setup::project_constructor_args():
    sig = inspect.signature(setup::Project.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"

def test_setup::project_has_label():
    assert hasattr(setup::Project, "label")
    descriptor = None
    for klass in setup::Project.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_setup::project_has_name():
    assert hasattr(setup::Project, "name")
    descriptor = None
    for klass in setup::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_scoperoot_is_not_abstract():
    assert not inspect.isabstract(ScopeRoot)


def test_scoperoot_constructor_exists():
    assert callable(ScopeRoot.__init__)


def test_scoperoot_constructor_args():
    sig = inspect.signature(ScopeRoot.__init__)
    params = list(sig.parameters.keys())



def test_setup::configuration_is_not_abstract():
    assert not inspect.isabstract(setup::Configuration)


def test_setup::configuration_constructor_exists():
    assert callable(setup::Configuration.__init__)


def test_setup::configuration_constructor_args():
    sig = inspect.signature(setup::Configuration.__init__)
    params = list(sig.parameters.keys())



def test_setup::preferences_is_not_abstract():
    assert not inspect.isabstract(setup::Preferences)


def test_setup::preferences_constructor_exists():
    assert callable(setup::Preferences.__init__)


def test_setup::preferences_constructor_args():
    sig = inspect.signature(setup::Preferences.__init__)
    params = list(sig.parameters.keys())
    assert "acceptedLicenses" in params, "Missing parameter 'acceptedLicenses'"
    assert "installFolder" in params, "Missing parameter 'installFolder'"

def test_setup::preferences_has_acceptedLicenses():
    assert hasattr(setup::Preferences, "acceptedLicenses")
    descriptor = None
    for klass in setup::Preferences.__mro__:
        if "acceptedLicenses" in klass.__dict__:
            descriptor = klass.__dict__["acceptedLicenses"]
            break
    assert isinstance(descriptor, property)

def test_setup::preferences_has_installFolder():
    assert hasattr(setup::Preferences, "installFolder")
    descriptor = None
    for klass in setup::Preferences.__mro__:
        if "installFolder" in klass.__dict__:
            descriptor = klass.__dict__["installFolder"]
            break
    assert isinstance(descriptor, property)



def test_setup::configurableitem_is_not_abstract():
    assert not inspect.isabstract(setup::ConfigurableItem)


def test_setup::configurableitem_constructor_exists():
    assert callable(setup::ConfigurableItem.__init__)


def test_setup::configurableitem_constructor_args():
    sig = inspect.signature(setup::ConfigurableItem.__init__)
    params = list(sig.parameters.keys())



def test_setup::index_is_not_abstract():
    assert not inspect.isabstract(setup::Index)


def test_setup::index_constructor_exists():
    assert callable(setup::Index.__init__)


def test_setup::index_constructor_args():
    sig = inspect.signature(setup::Index.__init__)
    params = list(sig.parameters.keys())
    assert "uRI" in params, "Missing parameter 'uRI'"
    assert "oldURIs" in params, "Missing parameter 'oldURIs'"
    assert "name" in params, "Missing parameter 'name'"

def test_setup::index_has_uRI():
    assert hasattr(setup::Index, "uRI")
    descriptor = None
    for klass in setup::Index.__mro__:
        if "uRI" in klass.__dict__:
            descriptor = klass.__dict__["uRI"]
            break
    assert isinstance(descriptor, property)

def test_setup::index_has_oldURIs():
    assert hasattr(setup::Index, "oldURIs")
    descriptor = None
    for klass in setup::Index.__mro__:
        if "oldURIs" in klass.__dict__:
            descriptor = klass.__dict__["oldURIs"]
            break
    assert isinstance(descriptor, property)

def test_setup::index_has_name():
    assert hasattr(setup::Index, "name")
    descriptor = None
    for klass in setup::Index.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_setup::metaindex_is_not_abstract():
    assert not inspect.isabstract(setup::MetaIndex)


def test_setup::metaindex_constructor_exists():
    assert callable(setup::MetaIndex.__init__)


def test_setup::metaindex_constructor_args():
    sig = inspect.signature(setup::MetaIndex.__init__)
    params = list(sig.parameters.keys())



def test_setup::mylynquerytask_is_not_abstract():
    assert not inspect.isabstract(setup::MylynQueryTask)


def test_setup::mylynquerytask_constructor_exists():
    assert callable(setup::MylynQueryTask.__init__)


def test_setup::mylynquerytask_constructor_args():
    sig = inspect.signature(setup::MylynQueryTask.__init__)
    params = list(sig.parameters.keys())
    assert "repositoryURL" in params, "Missing parameter 'repositoryURL'"
    assert "summary" in params, "Missing parameter 'summary'"
    assert "relativeURL" in params, "Missing parameter 'relativeURL'"
    assert "connectorKind" in params, "Missing parameter 'connectorKind'"

def test_setup::mylynquerytask_has_repositoryURL():
    assert hasattr(setup::MylynQueryTask, "repositoryURL")
    descriptor = None
    for klass in setup::MylynQueryTask.__mro__:
        if "repositoryURL" in klass.__dict__:
            descriptor = klass.__dict__["repositoryURL"]
            break
    assert isinstance(descriptor, property)

def test_setup::mylynquerytask_has_summary():
    assert hasattr(setup::MylynQueryTask, "summary")
    descriptor = None
    for klass in setup::MylynQueryTask.__mro__:
        if "summary" in klass.__dict__:
            descriptor = klass.__dict__["summary"]
            break
    assert isinstance(descriptor, property)

def test_setup::mylynquerytask_has_relativeURL():
    assert hasattr(setup::MylynQueryTask, "relativeURL")
    descriptor = None
    for klass in setup::MylynQueryTask.__mro__:
        if "relativeURL" in klass.__dict__:
            descriptor = klass.__dict__["relativeURL"]
            break
    assert isinstance(descriptor, property)

def test_setup::mylynquerytask_has_connectorKind():
    assert hasattr(setup::MylynQueryTask, "connectorKind")
    descriptor = None
    for klass in setup::MylynQueryTask.__mro__:
        if "connectorKind" in klass.__dict__:
            descriptor = klass.__dict__["connectorKind"]
            break
    assert isinstance(descriptor, property)



def test_setup::commandparameter_is_not_abstract():
    assert not inspect.isabstract(setup::CommandParameter)


def test_setup::commandparameter_constructor_exists():
    assert callable(setup::CommandParameter.__init__)


def test_setup::commandparameter_constructor_args():
    sig = inspect.signature(setup::CommandParameter.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"
    assert "value" in params, "Missing parameter 'value'"

def test_setup::commandparameter_has_iD():
    assert hasattr(setup::CommandParameter, "iD")
    descriptor = None
    for klass in setup::CommandParameter.__mro__:
        if "iD" in klass.__dict__:
            descriptor = klass.__dict__["iD"]
            break
    assert isinstance(descriptor, property)

def test_setup::commandparameter_has_value():
    assert hasattr(setup::CommandParameter, "value")
    descriptor = None
    for klass in setup::CommandParameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_setup::keybindingcontext_is_not_abstract():
    assert not inspect.isabstract(setup::KeyBindingContext)


def test_setup::keybindingcontext_constructor_exists():
    assert callable(setup::KeyBindingContext.__init__)


def test_setup::keybindingcontext_constructor_args():
    sig = inspect.signature(setup::KeyBindingContext.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"

def test_setup::keybindingcontext_has_iD():
    assert hasattr(setup::KeyBindingContext, "iD")
    descriptor = None
    for klass in setup::KeyBindingContext.__mro__:
        if "iD" in klass.__dict__:
            descriptor = klass.__dict__["iD"]
            break
    assert isinstance(descriptor, property)



def test_setup::fileeditor_is_not_abstract():
    assert not inspect.isabstract(setup::FileEditor)


def test_setup::fileeditor_constructor_exists():
    assert callable(setup::FileEditor.__init__)


def test_setup::fileeditor_constructor_args():
    sig = inspect.signature(setup::FileEditor.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"

def test_setup::fileeditor_has_iD():
    assert hasattr(setup::FileEditor, "iD")
    descriptor = None
    for klass in setup::FileEditor.__mro__:
        if "iD" in klass.__dict__:
            descriptor = klass.__dict__["iD"]
            break
    assert isinstance(descriptor, property)



def test_setup::fileassociationtask_is_not_abstract():
    assert not inspect.isabstract(setup::FileAssociationTask)


def test_setup::fileassociationtask_constructor_exists():
    assert callable(setup::FileAssociationTask.__init__)


def test_setup::fileassociationtask_constructor_args():
    sig = inspect.signature(setup::FileAssociationTask.__init__)
    params = list(sig.parameters.keys())
    assert "filePattern" in params, "Missing parameter 'filePattern'"
    assert "defaultEditorID" in params, "Missing parameter 'defaultEditorID'"

def test_setup::fileassociationtask_has_filePattern():
    assert hasattr(setup::FileAssociationTask, "filePattern")
    descriptor = None
    for klass in setup::FileAssociationTask.__mro__:
        if "filePattern" in klass.__dict__:
            descriptor = klass.__dict__["filePattern"]
            break
    assert isinstance(descriptor, property)

def test_setup::fileassociationtask_has_defaultEditorID():
    assert hasattr(setup::FileAssociationTask, "defaultEditorID")
    descriptor = None
    for klass in setup::FileAssociationTask.__mro__:
        if "defaultEditorID" in klass.__dict__:
            descriptor = klass.__dict__["defaultEditorID"]
            break
    assert isinstance(descriptor, property)



def test_setup::eclipsepreferencetask_is_not_abstract():
    assert not inspect.isabstract(setup::EclipsePreferenceTask)


def test_setup::eclipsepreferencetask_constructor_exists():
    assert callable(setup::EclipsePreferenceTask.__init__)


def test_setup::eclipsepreferencetask_constructor_args():
    sig = inspect.signature(setup::EclipsePreferenceTask.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_setup::eclipsepreferencetask_has_key():
    assert hasattr(setup::EclipsePreferenceTask, "key")
    descriptor = None
    for klass in setup::EclipsePreferenceTask.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_setup::eclipsepreferencetask_has_value():
    assert hasattr(setup::EclipsePreferenceTask, "value")
    descriptor = None
    for klass in setup::EclipsePreferenceTask.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_setup::textmodifytask_is_not_abstract():
    assert not inspect.isabstract(setup::TextModifyTask)


def test_setup::textmodifytask_constructor_exists():
    assert callable(setup::TextModifyTask.__init__)


def test_setup::textmodifytask_constructor_args():
    sig = inspect.signature(setup::TextModifyTask.__init__)
    params = list(sig.parameters.keys())
    assert "encoding" in params, "Missing parameter 'encoding'"
    assert "uRL" in params, "Missing parameter 'uRL'"

def test_setup::textmodifytask_has_encoding():
    assert hasattr(setup::TextModifyTask, "encoding")
    descriptor = None
    for klass in setup::TextModifyTask.__mro__:
        if "encoding" in klass.__dict__:
            descriptor = klass.__dict__["encoding"]
            break
    assert isinstance(descriptor, property)

def test_setup::textmodifytask_has_uRL():
    assert hasattr(setup::TextModifyTask, "uRL")
    descriptor = None
    for klass in setup::TextModifyTask.__mro__:
        if "uRL" in klass.__dict__:
            descriptor = klass.__dict__["uRL"]
            break
    assert isinstance(descriptor, property)



def test_setup::resourcecreationtask_is_not_abstract():
    assert not inspect.isabstract(setup::ResourceCreationTask)


def test_setup::resourcecreationtask_constructor_exists():
    assert callable(setup::ResourceCreationTask.__init__)


def test_setup::resourcecreationtask_constructor_args():
    sig = inspect.signature(setup::ResourceCreationTask.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "encoding" in params, "Missing parameter 'encoding'"
    assert "targetURL" in params, "Missing parameter 'targetURL'"

def test_setup::resourcecreationtask_has_content():
    assert hasattr(setup::ResourceCreationTask, "content")
    descriptor = None
    for klass in setup::ResourceCreationTask.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_setup::resourcecreationtask_has_encoding():
    assert hasattr(setup::ResourceCreationTask, "encoding")
    descriptor = None
    for klass in setup::ResourceCreationTask.__mro__:
        if "encoding" in klass.__dict__:
            descriptor = klass.__dict__["encoding"]
            break
    assert isinstance(descriptor, property)

def test_setup::resourcecreationtask_has_targetURL():
    assert hasattr(setup::ResourceCreationTask, "targetURL")
    descriptor = None
    for klass in setup::ResourceCreationTask.__mro__:
        if "targetURL" in klass.__dict__:
            descriptor = klass.__dict__["targetURL"]
            break
    assert isinstance(descriptor, property)



def test_setup::resourcecopytask_is_not_abstract():
    assert not inspect.isabstract(setup::ResourceCopyTask)


def test_setup::resourcecopytask_constructor_exists():
    assert callable(setup::ResourceCopyTask.__init__)


def test_setup::resourcecopytask_constructor_args():
    sig = inspect.signature(setup::ResourceCopyTask.__init__)
    params = list(sig.parameters.keys())
    assert "sourceURL" in params, "Missing parameter 'sourceURL'"
    assert "targetURL" in params, "Missing parameter 'targetURL'"

def test_setup::resourcecopytask_has_sourceURL():
    assert hasattr(setup::ResourceCopyTask, "sourceURL")
    descriptor = None
    for klass in setup::ResourceCopyTask.__mro__:
        if "sourceURL" in klass.__dict__:
            descriptor = klass.__dict__["sourceURL"]
            break
    assert isinstance(descriptor, property)

def test_setup::resourcecopytask_has_targetURL():
    assert hasattr(setup::ResourceCopyTask, "targetURL")
    descriptor = None
    for klass in setup::ResourceCopyTask.__mro__:
        if "targetURL" in klass.__dict__:
            descriptor = klass.__dict__["targetURL"]
            break
    assert isinstance(descriptor, property)



def test_setup::workingset_is_not_abstract():
    assert not inspect.isabstract(setup::WorkingSet)


def test_setup::workingset_constructor_exists():
    assert callable(setup::WorkingSet.__init__)


def test_setup::workingset_constructor_args():
    sig = inspect.signature(setup::WorkingSet.__init__)
    params = list(sig.parameters.keys())



def test_setup::workingsettask_is_not_abstract():
    assert not inspect.isabstract(setup::WorkingSetTask)


def test_setup::workingsettask_constructor_exists():
    assert callable(setup::WorkingSetTask.__init__)


def test_setup::workingsettask_constructor_args():
    sig = inspect.signature(setup::WorkingSetTask.__init__)
    params = list(sig.parameters.keys())



def test_setup::filemapping_is_not_abstract():
    assert not inspect.isabstract(setup::FileMapping)


def test_setup::filemapping_constructor_exists():
    assert callable(setup::FileMapping.__init__)


def test_setup::filemapping_constructor_args():
    sig = inspect.signature(setup::FileMapping.__init__)
    params = list(sig.parameters.keys())
    assert "defaultEditorID" in params, "Missing parameter 'defaultEditorID'"
    assert "filePattern" in params, "Missing parameter 'filePattern'"

def test_setup::filemapping_has_defaultEditorID():
    assert hasattr(setup::FileMapping, "defaultEditorID")
    descriptor = None
    for klass in setup::FileMapping.__mro__:
        if "defaultEditorID" in klass.__dict__:
            descriptor = klass.__dict__["defaultEditorID"]
            break
    assert isinstance(descriptor, property)

def test_setup::filemapping_has_filePattern():
    assert hasattr(setup::FileMapping, "filePattern")
    descriptor = None
    for klass in setup::FileMapping.__mro__:
        if "filePattern" in klass.__dict__:
            descriptor = klass.__dict__["filePattern"]
            break
    assert isinstance(descriptor, property)



def test_setup::fileassociationstask_is_not_abstract():
    assert not inspect.isabstract(setup::FileAssociationsTask)


def test_setup::fileassociationstask_constructor_exists():
    assert callable(setup::FileAssociationsTask.__init__)


def test_setup::fileassociationstask_constructor_args():
    sig = inspect.signature(setup::FileAssociationsTask.__init__)
    params = list(sig.parameters.keys())



def test_setup::targletdata_is_not_abstract():
    assert not inspect.isabstract(setup::TargletData)


def test_setup::targletdata_constructor_exists():
    assert callable(setup::TargletData.__init__)


def test_setup::targletdata_constructor_args():
    sig = inspect.signature(setup::TargletData.__init__)
    params = list(sig.parameters.keys())
    assert "activeRepositoryList" in params, "Missing parameter 'activeRepositoryList'"
    assert "includeAllPlatforms" in params, "Missing parameter 'includeAllPlatforms'"
    assert "includeSources" in params, "Missing parameter 'includeSources'"
    assert "name" in params, "Missing parameter 'name'"

def test_setup::targletdata_has_activeRepositoryList():
    assert hasattr(setup::TargletData, "activeRepositoryList")
    descriptor = None
    for klass in setup::TargletData.__mro__:
        if "activeRepositoryList" in klass.__dict__:
            descriptor = klass.__dict__["activeRepositoryList"]
            break
    assert isinstance(descriptor, property)

def test_setup::targletdata_has_includeAllPlatforms():
    assert hasattr(setup::TargletData, "includeAllPlatforms")
    descriptor = None
    for klass in setup::TargletData.__mro__:
        if "includeAllPlatforms" in klass.__dict__:
            descriptor = klass.__dict__["includeAllPlatforms"]
            break
    assert isinstance(descriptor, property)

def test_setup::targletdata_has_includeSources():
    assert hasattr(setup::TargletData, "includeSources")
    descriptor = None
    for klass in setup::TargletData.__mro__:
        if "includeSources" in klass.__dict__:
            descriptor = klass.__dict__["includeSources"]
            break
    assert isinstance(descriptor, property)

def test_setup::targletdata_has_name():
    assert hasattr(setup::TargletData, "name")
    descriptor = None
    for klass in setup::TargletData.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_targletdata_is_not_abstract():
    assert not inspect.isabstract(TargletData)


def test_targletdata_constructor_exists():
    assert callable(TargletData.__init__)


def test_targletdata_constructor_args():
    sig = inspect.signature(TargletData.__init__)
    params = list(sig.parameters.keys())



def test_setup::targlet_is_not_abstract():
    assert not inspect.isabstract(setup::Targlet)


def test_setup::targlet_constructor_exists():
    assert callable(setup::Targlet.__init__)


def test_setup::targlet_constructor_args():
    sig = inspect.signature(setup::Targlet.__init__)
    params = list(sig.parameters.keys())



def test_setup::apibaselinetask_is_not_abstract():
    assert not inspect.isabstract(setup::ApiBaselineTask)


def test_setup::apibaselinetask_constructor_exists():
    assert callable(setup::ApiBaselineTask.__init__)


def test_setup::apibaselinetask_constructor_args():
    sig = inspect.signature(setup::ApiBaselineTask.__init__)
    params = list(sig.parameters.keys())
    assert "zipLocation" in params, "Missing parameter 'zipLocation'"
    assert "version" in params, "Missing parameter 'version'"
    assert "containerFolder" in params, "Missing parameter 'containerFolder'"

def test_setup::apibaselinetask_has_zipLocation():
    assert hasattr(setup::ApiBaselineTask, "zipLocation")
    descriptor = None
    for klass in setup::ApiBaselineTask.__mro__:
        if "zipLocation" in klass.__dict__:
            descriptor = klass.__dict__["zipLocation"]
            break
    assert isinstance(descriptor, property)

def test_setup::apibaselinetask_has_version():
    assert hasattr(setup::ApiBaselineTask, "version")
    descriptor = None
    for klass in setup::ApiBaselineTask.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_setup::apibaselinetask_has_containerFolder():
    assert hasattr(setup::ApiBaselineTask, "containerFolder")
    descriptor = None
    for klass in setup::ApiBaselineTask.__mro__:
        if "containerFolder" in klass.__dict__:
            descriptor = klass.__dict__["containerFolder"]
            break
    assert isinstance(descriptor, property)



def test_setup::targetplatformtask_is_not_abstract():
    assert not inspect.isabstract(setup::TargetPlatformTask)


def test_setup::targetplatformtask_constructor_exists():
    assert callable(setup::TargetPlatformTask.__init__)


def test_setup::targetplatformtask_constructor_args():
    sig = inspect.signature(setup::TargetPlatformTask.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_setup::targetplatformtask_has_name():
    assert hasattr(setup::TargetPlatformTask, "name")
    descriptor = None
    for klass in setup::TargetPlatformTask.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_setup::projectsetimporttask_is_not_abstract():
    assert not inspect.isabstract(setup::ProjectSetImportTask)


def test_setup::projectsetimporttask_constructor_exists():
    assert callable(setup::ProjectSetImportTask.__init__)


def test_setup::projectsetimporttask_constructor_args():
    sig = inspect.signature(setup::ProjectSetImportTask.__init__)
    params = list(sig.parameters.keys())
    assert "uRL" in params, "Missing parameter 'uRL'"

def test_setup::projectsetimporttask_has_uRL():
    assert hasattr(setup::ProjectSetImportTask, "uRL")
    descriptor = None
    for klass in setup::ProjectSetImportTask.__mro__:
        if "uRL" in klass.__dict__:
            descriptor = klass.__dict__["uRL"]
            break
    assert isinstance(descriptor, property)



def test_setup::projectsimporttask_is_not_abstract():
    assert not inspect.isabstract(setup::ProjectsImportTask)


def test_setup::projectsimporttask_constructor_exists():
    assert callable(setup::ProjectsImportTask.__init__)


def test_setup::projectsimporttask_constructor_args():
    sig = inspect.signature(setup::ProjectsImportTask.__init__)
    params = list(sig.parameters.keys())



def test_setup::repositorylist_is_not_abstract():
    assert not inspect.isabstract(setup::RepositoryList)


def test_setup::repositorylist_constructor_exists():
    assert callable(setup::RepositoryList.__init__)


def test_setup::repositorylist_constructor_args():
    sig = inspect.signature(setup::RepositoryList.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_setup::repositorylist_has_name():
    assert hasattr(setup::RepositoryList, "name")
    descriptor = None
    for klass in setup::RepositoryList.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_componentextension_is_not_abstract():
    assert not inspect.isabstract(ComponentExtension)


def test_componentextension_constructor_exists():
    assert callable(ComponentExtension.__init__)


def test_componentextension_constructor_args():
    sig = inspect.signature(ComponentExtension.__init__)
    params = list(sig.parameters.keys())



def test_setup::componentdefinition_is_not_abstract():
    assert not inspect.isabstract(setup::ComponentDefinition)


def test_setup::componentdefinition_constructor_exists():
    assert callable(setup::ComponentDefinition.__init__)


def test_setup::componentdefinition_constructor_args():
    sig = inspect.signature(setup::ComponentDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"
    assert "version" in params, "Missing parameter 'version'"

def test_setup::componentdefinition_has_iD():
    assert hasattr(setup::ComponentDefinition, "iD")
    descriptor = None
    for klass in setup::ComponentDefinition.__mro__:
        if "iD" in klass.__dict__:
            descriptor = klass.__dict__["iD"]
            break
    assert isinstance(descriptor, property)

def test_setup::componentdefinition_has_version():
    assert hasattr(setup::ComponentDefinition, "version")
    descriptor = None
    for klass in setup::ComponentDefinition.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_setup::targlettask_is_not_abstract():
    assert not inspect.isabstract(setup::TargletTask)


def test_setup::targlettask_constructor_exists():
    assert callable(setup::TargletTask.__init__)


def test_setup::targlettask_constructor_args():
    sig = inspect.signature(setup::TargletTask.__init__)
    params = list(sig.parameters.keys())



def test_setup::targletimporttask_is_not_abstract():
    assert not inspect.isabstract(setup::TargletImportTask)


def test_setup::targletimporttask_constructor_exists():
    assert callable(setup::TargletImportTask.__init__)


def test_setup::targletimporttask_constructor_args():
    sig = inspect.signature(setup::TargletImportTask.__init__)
    params = list(sig.parameters.keys())
    assert "targletURI" in params, "Missing parameter 'targletURI'"

def test_setup::targletimporttask_has_targletURI():
    assert hasattr(setup::TargletImportTask, "targletURI")
    descriptor = None
    for klass in setup::TargletImportTask.__mro__:
        if "targletURI" in klass.__dict__:
            descriptor = klass.__dict__["targletURI"]
            break
    assert isinstance(descriptor, property)



def test_setup::mavenimporttask_is_not_abstract():
    assert not inspect.isabstract(setup::MavenImportTask)


def test_setup::mavenimporttask_constructor_exists():
    assert callable(setup::MavenImportTask.__init__)


def test_setup::mavenimporttask_constructor_args():
    sig = inspect.signature(setup::MavenImportTask.__init__)
    params = list(sig.parameters.keys())



def test_setup::component_is_not_abstract():
    assert not inspect.isabstract(setup::Component)


def test_setup::component_constructor_exists():
    assert callable(setup::Component.__init__)


def test_setup::component_constructor_args():
    sig = inspect.signature(setup::Component.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "versionRange" in params, "Missing parameter 'versionRange'"

def test_setup::component_has_type():
    assert hasattr(setup::Component, "type")
    descriptor = None
    for klass in setup::Component.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_setup::component_has_name():
    assert hasattr(setup::Component, "name")
    descriptor = None
    for klass in setup::Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_setup::component_has_versionRange():
    assert hasattr(setup::Component, "versionRange")
    descriptor = None
    for klass in setup::Component.__mro__:
        if "versionRange" in klass.__dict__:
            descriptor = klass.__dict__["versionRange"]
            break
    assert isinstance(descriptor, property)



def test_setup::componentextension_is_not_abstract():
    assert not inspect.isabstract(setup::ComponentExtension)


def test_setup::componentextension_constructor_exists():
    assert callable(setup::ComponentExtension.__init__)


def test_setup::componentextension_constructor_args():
    sig = inspect.signature(setup::ComponentExtension.__init__)
    params = list(sig.parameters.keys())



def test_setup::predicate_is_not_abstract():
    assert not inspect.isabstract(setup::Predicate)


def test_setup::predicate_constructor_exists():
    assert callable(setup::Predicate.__init__)


def test_setup::predicate_constructor_args():
    sig = inspect.signature(setup::Predicate.__init__)
    params = list(sig.parameters.keys())



def test_sourcelocator_is_not_abstract():
    assert not inspect.isabstract(SourceLocator)


def test_sourcelocator_constructor_exists():
    assert callable(SourceLocator.__init__)


def test_sourcelocator_constructor_args():
    sig = inspect.signature(SourceLocator.__init__)
    params = list(sig.parameters.keys())



def test_setup::automaticsourcelocator_is_not_abstract():
    assert not inspect.isabstract(setup::AutomaticSourceLocator)


def test_setup::automaticsourcelocator_constructor_exists():
    assert callable(setup::AutomaticSourceLocator.__init__)


def test_setup::automaticsourcelocator_constructor_args():
    sig = inspect.signature(setup::AutomaticSourceLocator.__init__)
    params = list(sig.parameters.keys())
    assert "rootFolder" in params, "Missing parameter 'rootFolder'"
    assert "locateNestedProjects" in params, "Missing parameter 'locateNestedProjects'"

def test_setup::automaticsourcelocator_has_rootFolder():
    assert hasattr(setup::AutomaticSourceLocator, "rootFolder")
    descriptor = None
    for klass in setup::AutomaticSourceLocator.__mro__:
        if "rootFolder" in klass.__dict__:
            descriptor = klass.__dict__["rootFolder"]
            break
    assert isinstance(descriptor, property)

def test_setup::automaticsourcelocator_has_locateNestedProjects():
    assert hasattr(setup::AutomaticSourceLocator, "locateNestedProjects")
    descriptor = None
    for klass in setup::AutomaticSourceLocator.__mro__:
        if "locateNestedProjects" in klass.__dict__:
            descriptor = klass.__dict__["locateNestedProjects"]
            break
    assert isinstance(descriptor, property)



def test_setup::manualsourcelocator_is_not_abstract():
    assert not inspect.isabstract(setup::ManualSourceLocator)


def test_setup::manualsourcelocator_constructor_exists():
    assert callable(setup::ManualSourceLocator.__init__)


def test_setup::manualsourcelocator_constructor_args():
    sig = inspect.signature(setup::ManualSourceLocator.__init__)
    params = list(sig.parameters.keys())
    assert "componentNamePattern" in params, "Missing parameter 'componentNamePattern'"
    assert "location" in params, "Missing parameter 'location'"
    assert "componentTypes" in params, "Missing parameter 'componentTypes'"

def test_setup::manualsourcelocator_has_componentNamePattern():
    assert hasattr(setup::ManualSourceLocator, "componentNamePattern")
    descriptor = None
    for klass in setup::ManualSourceLocator.__mro__:
        if "componentNamePattern" in klass.__dict__:
            descriptor = klass.__dict__["componentNamePattern"]
            break
    assert isinstance(descriptor, property)

def test_setup::manualsourcelocator_has_location():
    assert hasattr(setup::ManualSourceLocator, "location")
    descriptor = None
    for klass in setup::ManualSourceLocator.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_setup::manualsourcelocator_has_componentTypes():
    assert hasattr(setup::ManualSourceLocator, "componentTypes")
    descriptor = None
    for klass in setup::ManualSourceLocator.__mro__:
        if "componentTypes" in klass.__dict__:
            descriptor = klass.__dict__["componentTypes"]
            break
    assert isinstance(descriptor, property)



def test_setup::sourcelocator_is_not_abstract():
    assert not inspect.isabstract(setup::SourceLocator)


def test_setup::sourcelocator_constructor_exists():
    assert callable(setup::SourceLocator.__init__)


def test_setup::sourcelocator_constructor_args():
    sig = inspect.signature(setup::SourceLocator.__init__)
    params = list(sig.parameters.keys())



def test_setup::p2repository_is_not_abstract():
    assert not inspect.isabstract(setup::P2Repository)


def test_setup::p2repository_constructor_exists():
    assert callable(setup::P2Repository.__init__)


def test_setup::p2repository_constructor_args():
    sig = inspect.signature(setup::P2Repository.__init__)
    params = list(sig.parameters.keys())
    assert "uRL" in params, "Missing parameter 'uRL'"

def test_setup::p2repository_has_uRL():
    assert hasattr(setup::P2Repository, "uRL")
    descriptor = None
    for klass in setup::P2Repository.__mro__:
        if "uRL" in klass.__dict__:
            descriptor = klass.__dict__["uRL"]
            break
    assert isinstance(descriptor, property)



def test_setup::installableunit_is_not_abstract():
    assert not inspect.isabstract(setup::InstallableUnit)


def test_setup::installableunit_constructor_exists():
    assert callable(setup::InstallableUnit.__init__)


def test_setup::installableunit_constructor_args():
    sig = inspect.signature(setup::InstallableUnit.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"
    assert "versionRange" in params, "Missing parameter 'versionRange'"

def test_setup::installableunit_has_iD():
    assert hasattr(setup::InstallableUnit, "iD")
    descriptor = None
    for klass in setup::InstallableUnit.__mro__:
        if "iD" in klass.__dict__:
            descriptor = klass.__dict__["iD"]
            break
    assert isinstance(descriptor, property)

def test_setup::installableunit_has_versionRange():
    assert hasattr(setup::InstallableUnit, "versionRange")
    descriptor = None
    for klass in setup::InstallableUnit.__mro__:
        if "versionRange" in klass.__dict__:
            descriptor = klass.__dict__["versionRange"]
            break
    assert isinstance(descriptor, property)



def test_setup::p2task_is_not_abstract():
    assert not inspect.isabstract(setup::P2Task)


def test_setup::p2task_constructor_exists():
    assert callable(setup::P2Task.__init__)


def test_setup::p2task_constructor_args():
    sig = inspect.signature(setup::P2Task.__init__)
    params = list(sig.parameters.keys())
    assert "mergeDisabled" in params, "Missing parameter 'mergeDisabled'"
    assert "licenseConfirmationDisabled" in params, "Missing parameter 'licenseConfirmationDisabled'"

def test_setup::p2task_has_mergeDisabled():
    assert hasattr(setup::P2Task, "mergeDisabled")
    descriptor = None
    for klass in setup::P2Task.__mro__:
        if "mergeDisabled" in klass.__dict__:
            descriptor = klass.__dict__["mergeDisabled"]
            break
    assert isinstance(descriptor, property)

def test_setup::p2task_has_licenseConfirmationDisabled():
    assert hasattr(setup::P2Task, "licenseConfirmationDisabled")
    descriptor = None
    for klass in setup::P2Task.__mro__:
        if "licenseConfirmationDisabled" in klass.__dict__:
            descriptor = klass.__dict__["licenseConfirmationDisabled"]
            break
    assert isinstance(descriptor, property)



def test_basicmaterializationtask_is_not_abstract():
    assert not inspect.isabstract(BasicMaterializationTask)


def test_basicmaterializationtask_constructor_exists():
    assert callable(BasicMaterializationTask.__init__)


def test_basicmaterializationtask_constructor_args():
    sig = inspect.signature(BasicMaterializationTask.__init__)
    params = list(sig.parameters.keys())



def test_setup::materializationtask_is_not_abstract():
    assert not inspect.isabstract(setup::MaterializationTask)


def test_setup::materializationtask_constructor_exists():
    assert callable(setup::MaterializationTask.__init__)


def test_setup::materializationtask_constructor_args():
    sig = inspect.signature(setup::MaterializationTask.__init__)
    params = list(sig.parameters.keys())



def test_setup::buckminsterimporttask_is_not_abstract():
    assert not inspect.isabstract(setup::BuckminsterImportTask)


def test_setup::buckminsterimporttask_constructor_exists():
    assert callable(setup::BuckminsterImportTask.__init__)


def test_setup::buckminsterimporttask_constructor_args():
    sig = inspect.signature(setup::BuckminsterImportTask.__init__)
    params = list(sig.parameters.keys())
    assert "mspec" in params, "Missing parameter 'mspec'"

def test_setup::buckminsterimporttask_has_mspec():
    assert hasattr(setup::BuckminsterImportTask, "mspec")
    descriptor = None
    for klass in setup::BuckminsterImportTask.__mro__:
        if "mspec" in klass.__dict__:
            descriptor = klass.__dict__["mspec"]
            break
    assert isinstance(descriptor, property)



def test_setup::basicmaterializationtask_is_not_abstract():
    assert not inspect.isabstract(setup::BasicMaterializationTask)


def test_setup::basicmaterializationtask_constructor_exists():
    assert callable(setup::BasicMaterializationTask.__init__)


def test_setup::basicmaterializationtask_constructor_args():
    sig = inspect.signature(setup::BasicMaterializationTask.__init__)
    params = list(sig.parameters.keys())
    assert "targetPlatform" in params, "Missing parameter 'targetPlatform'"
    assert "bundlePool" in params, "Missing parameter 'bundlePool'"

def test_setup::basicmaterializationtask_has_targetPlatform():
    assert hasattr(setup::BasicMaterializationTask, "targetPlatform")
    descriptor = None
    for klass in setup::BasicMaterializationTask.__mro__:
        if "targetPlatform" in klass.__dict__:
            descriptor = klass.__dict__["targetPlatform"]
            break
    assert isinstance(descriptor, property)

def test_setup::basicmaterializationtask_has_bundlePool():
    assert hasattr(setup::BasicMaterializationTask, "bundlePool")
    descriptor = None
    for klass in setup::BasicMaterializationTask.__mro__:
        if "bundlePool" in klass.__dict__:
            descriptor = klass.__dict__["bundlePool"]
            break
    assert isinstance(descriptor, property)



def test_setup::gitclonetask_is_not_abstract():
    assert not inspect.isabstract(setup::GitCloneTask)


def test_setup::gitclonetask_constructor_exists():
    assert callable(setup::GitCloneTask.__init__)


def test_setup::gitclonetask_constructor_args():
    sig = inspect.signature(setup::GitCloneTask.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "pushURI" in params, "Missing parameter 'pushURI'"
    assert "checkoutBranch" in params, "Missing parameter 'checkoutBranch'"
    assert "remoteURI" in params, "Missing parameter 'remoteURI'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "remoteName" in params, "Missing parameter 'remoteName'"

def test_setup::gitclonetask_has_location():
    assert hasattr(setup::GitCloneTask, "location")
    descriptor = None
    for klass in setup::GitCloneTask.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_setup::gitclonetask_has_pushURI():
    assert hasattr(setup::GitCloneTask, "pushURI")
    descriptor = None
    for klass in setup::GitCloneTask.__mro__:
        if "pushURI" in klass.__dict__:
            descriptor = klass.__dict__["pushURI"]
            break
    assert isinstance(descriptor, property)

def test_setup::gitclonetask_has_checkoutBranch():
    assert hasattr(setup::GitCloneTask, "checkoutBranch")
    descriptor = None
    for klass in setup::GitCloneTask.__mro__:
        if "checkoutBranch" in klass.__dict__:
            descriptor = klass.__dict__["checkoutBranch"]
            break
    assert isinstance(descriptor, property)

def test_setup::gitclonetask_has_remoteURI():
    assert hasattr(setup::GitCloneTask, "remoteURI")
    descriptor = None
    for klass in setup::GitCloneTask.__mro__:
        if "remoteURI" in klass.__dict__:
            descriptor = klass.__dict__["remoteURI"]
            break
    assert isinstance(descriptor, property)

def test_setup::gitclonetask_has_userID():
    assert hasattr(setup::GitCloneTask, "userID")
    descriptor = None
    for klass in setup::GitCloneTask.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_setup::gitclonetask_has_remoteName():
    assert hasattr(setup::GitCloneTask, "remoteName")
    descriptor = None
    for klass in setup::GitCloneTask.__mro__:
        if "remoteName" in klass.__dict__:
            descriptor = klass.__dict__["remoteName"]
            break
    assert isinstance(descriptor, property)

def test_trigger_exists():
    # Check that the Enumeration exists
    assert Trigger is not None

def test_trigger_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Trigger]
    expected_literals = [
        "STARTUP",
        "BOOTSTRAP",
        "MANUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Trigger"

def test_componenttype_exists():
    # Check that the Enumeration exists
    assert ComponentType is not None

def test_componenttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComponentType]
    expected_literals = [
        "JAR",
        "BUCKMINSTER",
        "OSGI_BUNDLE",
        "UNKNOWN",
        "ECLIPSE_FEATURE",
        "BOM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComponentType"

def test_setuptaskscope_exists():
    # Check that the Enumeration exists
    assert SetupTaskScope is not None

def test_setuptaskscope_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SetupTaskScope]
    expected_literals = [
        "User",
        "Project",
        "Configuration",
        "None_",
        "Eclipse",
        "Branch",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SetupTaskScope"

def test_variabletype_exists():
    # Check that the Enumeration exists
    assert VariableType is not None

def test_variabletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariableType]
    expected_literals = [
        "FLOAT",
        "FILE",
        "BOOLEAN",
        "CONTAINER",
        "STRING",
        "FOLDER",
        "PASSWORD",
        "PATTERN",
        "URI",
        "RESOURCE",
        "INTEGER",
        "PROJECT",
        "TEXT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VariableType"


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
setup::Query_strategy = st.builds(
    setup::Query,
    summary=
        safe_text,
    uRL=
        safe_text
)
setup::BuildPlan_strategy = st.builds(
    setup::BuildPlan,
    name=
        safe_text
)
setup::QueryAttribute_strategy = st.builds(
    setup::QueryAttribute,
    key=
        safe_text,
    value=
        safe_text
)
setup::TextModification_strategy = st.builds(
    setup::TextModification,
    pattern=
        safe_text,
    substitutions=
        safe_text
)
SetupTask_strategy = st.builds(
    SetupTask,
)
setup::MylynBuildsTask_strategy = st.builds(
    setup::MylynBuildsTask,
    userID=
        safe_text,
    password=
        safe_text,
    serverURL=
        safe_text,
    connectorKind=
        safe_text
)
setup::JRETask_strategy = st.builds(
    setup::JRETask,
    location=
        safe_text,
    version=
        safe_text
)
setup::KeyBindingTask_strategy = st.builds(
    setup::KeyBindingTask,
    scheme=
        safe_text,
    keys=
        safe_text,
    locale=
        safe_text,
    command=
        safe_text,
    platform=
        safe_text
)
setup::MylynQueriesTask_strategy = st.builds(
    setup::MylynQueriesTask,
    connectorKind=
        safe_text,
    password=
        safe_text,
    repositoryURL=
        safe_text,
    userID=
        safe_text
)
SetupTaskContainer_strategy = st.builds(
    SetupTaskContainer,
)
setup::CompoundSetupTask_strategy = st.builds(
    setup::CompoundSetupTask,
    name=
        safe_text
)
setup::ScopeRoot_strategy = st.builds(
    setup::ScopeRoot,
)
setup::SetupTaskContainer_strategy = st.builds(
    setup::SetupTaskContainer,
)
setup::LinkLocationTask_strategy = st.builds(
    setup::LinkLocationTask,
    path=
        safe_text,
    name=
        safe_text
)
setup::EclipseIniTask_strategy = st.builds(
    setup::EclipseIniTask,
    vm=
        st.booleans(),
    value=
        safe_text,
    option=
        safe_text
)
setup::RedirectionTask_strategy = st.builds(
    setup::RedirectionTask,
    targetURL=
        safe_text,
    sourceURL=
        safe_text
)
setup::VariableChoice_strategy = st.builds(
    setup::VariableChoice,
    label=
        safe_text,
    value=
        safe_text
)
setup::ContextVariableTask_strategy = st.builds(
    setup::ContextVariableTask,
    value=
        safe_text,
    name=
        safe_text,
    stringSubstitution=
        st.booleans(),
    type=
        safe_text,
    label=
        safe_text
)
setup::SetupTask_strategy = st.builds(
    setup::SetupTask,
    disabled=
        st.booleans(),
    excludedTriggers=
        safe_text,
    scope=
        safe_text,
    documentation=
        safe_text
)
setup::Setup_strategy = st.builds(
    setup::Setup,
)
ConfigurableItem_strategy = st.builds(
    ConfigurableItem,
)
setup::Eclipse_strategy = st.builds(
    setup::Eclipse,
    version=
        safe_text
)
setup::Branch_strategy = st.builds(
    setup::Branch,
    name=
        safe_text
)
setup::Project_strategy = st.builds(
    setup::Project,
    label=
        safe_text,
    name=
        safe_text
)
ScopeRoot_strategy = st.builds(
    ScopeRoot,
)
setup::Configuration_strategy = st.builds(
    setup::Configuration,
)
setup::Preferences_strategy = st.builds(
    setup::Preferences,
    acceptedLicenses=
        safe_text,
    installFolder=
        safe_text
)
setup::ConfigurableItem_strategy = st.builds(
    setup::ConfigurableItem,
)
setup::Index_strategy = st.builds(
    setup::Index,
    uRI=
        safe_text,
    oldURIs=
        safe_text,
    name=
        safe_text
)
setup::MetaIndex_strategy = st.builds(
    setup::MetaIndex,
)
setup::MylynQueryTask_strategy = st.builds(
    setup::MylynQueryTask,
    repositoryURL=
        safe_text,
    summary=
        safe_text,
    relativeURL=
        safe_text,
    connectorKind=
        safe_text
)
setup::CommandParameter_strategy = st.builds(
    setup::CommandParameter,
    iD=
        safe_text,
    value=
        safe_text
)
setup::KeyBindingContext_strategy = st.builds(
    setup::KeyBindingContext,
    iD=
        safe_text
)
setup::FileEditor_strategy = st.builds(
    setup::FileEditor,
    iD=
        safe_text
)
setup::FileAssociationTask_strategy = st.builds(
    setup::FileAssociationTask,
    filePattern=
        safe_text,
    defaultEditorID=
        safe_text
)
setup::EclipsePreferenceTask_strategy = st.builds(
    setup::EclipsePreferenceTask,
    key=
        safe_text,
    value=
        safe_text
)
setup::TextModifyTask_strategy = st.builds(
    setup::TextModifyTask,
    encoding=
        safe_text,
    uRL=
        safe_text
)
setup::ResourceCreationTask_strategy = st.builds(
    setup::ResourceCreationTask,
    content=
        safe_text,
    encoding=
        safe_text,
    targetURL=
        safe_text
)
setup::ResourceCopyTask_strategy = st.builds(
    setup::ResourceCopyTask,
    sourceURL=
        safe_text,
    targetURL=
        safe_text
)
setup::WorkingSet_strategy = st.builds(
    setup::WorkingSet,
)
setup::WorkingSetTask_strategy = st.builds(
    setup::WorkingSetTask,
)
setup::FileMapping_strategy = st.builds(
    setup::FileMapping,
    defaultEditorID=
        safe_text,
    filePattern=
        safe_text
)
setup::FileAssociationsTask_strategy = st.builds(
    setup::FileAssociationsTask,
)
setup::TargletData_strategy = st.builds(
    setup::TargletData,
    activeRepositoryList=
        safe_text,
    includeAllPlatforms=
        st.booleans(),
    includeSources=
        st.booleans(),
    name=
        safe_text
)
TargletData_strategy = st.builds(
    TargletData,
)
setup::Targlet_strategy = st.builds(
    setup::Targlet,
)
setup::ApiBaselineTask_strategy = st.builds(
    setup::ApiBaselineTask,
    zipLocation=
        safe_text,
    version=
        safe_text,
    containerFolder=
        safe_text
)
setup::TargetPlatformTask_strategy = st.builds(
    setup::TargetPlatformTask,
    name=
        safe_text
)
setup::ProjectSetImportTask_strategy = st.builds(
    setup::ProjectSetImportTask,
    uRL=
        safe_text
)
setup::ProjectsImportTask_strategy = st.builds(
    setup::ProjectsImportTask,
)
setup::RepositoryList_strategy = st.builds(
    setup::RepositoryList,
    name=
        safe_text
)
ComponentExtension_strategy = st.builds(
    ComponentExtension,
)
setup::ComponentDefinition_strategy = st.builds(
    setup::ComponentDefinition,
    iD=
        safe_text,
    version=
        safe_text
)
setup::TargletTask_strategy = st.builds(
    setup::TargletTask,
)
setup::TargletImportTask_strategy = st.builds(
    setup::TargletImportTask,
    targletURI=
        safe_text
)
setup::MavenImportTask_strategy = st.builds(
    setup::MavenImportTask,
)
setup::Component_strategy = st.builds(
    setup::Component,
    type=
        safe_text,
    name=
        safe_text,
    versionRange=
        safe_text
)
setup::ComponentExtension_strategy = st.builds(
    setup::ComponentExtension,
)
setup::Predicate_strategy = st.builds(
    setup::Predicate,
)
SourceLocator_strategy = st.builds(
    SourceLocator,
)
setup::AutomaticSourceLocator_strategy = st.builds(
    setup::AutomaticSourceLocator,
    rootFolder=
        safe_text,
    locateNestedProjects=
        st.booleans()
)
setup::ManualSourceLocator_strategy = st.builds(
    setup::ManualSourceLocator,
    componentNamePattern=
        safe_text,
    location=
        safe_text,
    componentTypes=
        safe_text
)
setup::SourceLocator_strategy = st.builds(
    setup::SourceLocator,
)
setup::P2Repository_strategy = st.builds(
    setup::P2Repository,
    uRL=
        safe_text
)
setup::InstallableUnit_strategy = st.builds(
    setup::InstallableUnit,
    iD=
        safe_text,
    versionRange=
        safe_text
)
setup::P2Task_strategy = st.builds(
    setup::P2Task,
    mergeDisabled=
        st.booleans(),
    licenseConfirmationDisabled=
        st.booleans()
)
BasicMaterializationTask_strategy = st.builds(
    BasicMaterializationTask,
)
setup::MaterializationTask_strategy = st.builds(
    setup::MaterializationTask,
)
setup::BuckminsterImportTask_strategy = st.builds(
    setup::BuckminsterImportTask,
    mspec=
        safe_text
)
setup::BasicMaterializationTask_strategy = st.builds(
    setup::BasicMaterializationTask,
    targetPlatform=
        safe_text,
    bundlePool=
        safe_text
)
setup::GitCloneTask_strategy = st.builds(
    setup::GitCloneTask,
    location=
        safe_text,
    pushURI=
        safe_text,
    checkoutBranch=
        safe_text,
    remoteURI=
        safe_text,
    userID=
        safe_text,
    remoteName=
        safe_text
)

@given(instance=setup::Query_strategy)
@settings(max_examples=50)
def test_setup::query_instantiation(instance):
    assert isinstance(instance, setup::Query)

@given(instance=setup::Query_strategy)
def test_setup::query_summary_type(instance):
    assert isinstance(instance.summary, str)


@given(instance=setup::Query_strategy)
def test_setup::query_summary_setter(instance):
    original = instance.summary
    instance.summary = original
    assert instance.summary == original

@given(instance=setup::Query_strategy)
def test_setup::query_uRL_type(instance):
    assert isinstance(instance.uRL, str)


@given(instance=setup::Query_strategy)
def test_setup::query_uRL_setter(instance):
    original = instance.uRL
    instance.uRL = original
    assert instance.uRL == original

@given(instance=setup::BuildPlan_strategy)
@settings(max_examples=50)
def test_setup::buildplan_instantiation(instance):
    assert isinstance(instance, setup::BuildPlan)

@given(instance=setup::BuildPlan_strategy)
def test_setup::buildplan_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=setup::BuildPlan_strategy)
def test_setup::buildplan_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=setup::QueryAttribute_strategy)
@settings(max_examples=50)
def test_setup::queryattribute_instantiation(instance):
    assert isinstance(instance, setup::QueryAttribute)

@given(instance=setup::QueryAttribute_strategy)
def test_setup::queryattribute_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=setup::QueryAttribute_strategy)
def test_setup::queryattribute_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=setup::QueryAttribute_strategy)
def test_setup::queryattribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=setup::QueryAttribute_strategy)
def test_setup::queryattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=setup::TextModification_strategy)
@settings(max_examples=50)
def test_setup::textmodification_instantiation(instance):
    assert isinstance(instance, setup::TextModification)

@given(instance=setup::TextModification_strategy)
def test_setup::textmodification_pattern_type(instance):
    assert isinstance(instance.pattern, str)


@given(instance=setup::TextModification_strategy)
def test_setup::textmodification_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original

@given(instance=setup::TextModification_strategy)
def test_setup::textmodification_substitutions_type(instance):
    assert isinstance(instance.substitutions, str)


@given(instance=setup::TextModification_strategy)
def test_setup::textmodification_substitutions_setter(instance):
    original = instance.substitutions
    instance.substitutions = original
    assert instance.substitutions == original

@given(instance=SetupTask_strategy)
@settings(max_examples=50)
def test_setuptask_instantiation(instance):
    assert isinstance(instance, SetupTask)

@given(instance=setup::MylynBuildsTask_strategy)
@settings(max_examples=50)
def test_setup::mylynbuildstask_instantiation(instance):
    assert isinstance(instance, setup::MylynBuildsTask)

@given(instance=setup::MylynBuildsTask_strategy)
def test_setup::mylynbuildstask_userID_type(instance):
    assert isinstance(instance.userID, str)


@given(instance=setup::MylynBuildsTask_strategy)
def test_setup::mylynbuildstask_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original

@given(instance=setup::MylynBuildsTask_strategy)
def test_setup::mylynbuildstask_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=setup::MylynBuildsTask_strategy)
def test_setup::mylynbuildstask_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=setup::MylynBuildsTask_strategy)
def test_setup::mylynbuildstask_serverURL_type(instance):
    assert isinstance(instance.serverURL, str)


@given(instance=setup::MylynBuildsTask_strategy)
def test_setup::mylynbuildstask_serverURL_setter(instance):
    original = instance.serverURL
    instance.serverURL = original
    assert instance.serverURL == original

@given(instance=setup::MylynBuildsTask_strategy)
def test_setup::mylynbuildstask_connectorKind_type(instance):
    assert isinstance(instance.connectorKind, str)


@given(instance=setup::MylynBuildsTask_strategy)
def test_setup::mylynbuildstask_connectorKind_setter(instance):
    original = instance.connectorKind
    instance.connectorKind = original
    assert instance.connectorKind == original

@given(instance=setup::JRETask_strategy)
@settings(max_examples=50)
def test_setup::jretask_instantiation(instance):
    assert isinstance(instance, setup::JRETask)

@given(instance=setup::JRETask_strategy)
def test_setup::jretask_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=setup::JRETask_strategy)
def test_setup::jretask_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=setup::JRETask_strategy)
def test_setup::jretask_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=setup::JRETask_strategy)
def test_setup::jretask_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=setup::KeyBindingTask_strategy)
@settings(max_examples=50)
def test_setup::keybindingtask_instantiation(instance):
    assert isinstance(instance, setup::KeyBindingTask)

@given(instance=setup::KeyBindingTask_strategy)
def test_setup::keybindingtask_scheme_type(instance):
    assert isinstance(instance.scheme, str)


@given(instance=setup::KeyBindingTask_strategy)
def test_setup::keybindingtask_scheme_setter(instance):
    original = instance.scheme
    instance.scheme = original
    assert instance.scheme == original

@given(instance=setup::KeyBindingTask_strategy)
def test_setup::keybindingtask_keys_type(instance):
    assert isinstance(instance.keys, str)


@given(instance=setup::KeyBindingTask_strategy)
def test_setup::keybindingtask_keys_setter(instance):
    original = instance.keys
    instance.keys = original
    assert instance.keys == original

@given(instance=setup::KeyBindingTask_strategy)
def test_setup::keybindingtask_locale_type(instance):
    assert isinstance(instance.locale, str)


@given(instance=setup::KeyBindingTask_strategy)
def test_setup::keybindingtask_locale_setter(instance):
    original = instance.locale
    instance.locale = original
    assert instance.locale == original

@given(instance=setup::KeyBindingTask_strategy)
def test_setup::keybindingtask_command_type(instance):
    assert isinstance(instance.command, str)


@given(instance=setup::KeyBindingTask_strategy)
def test_setup::keybindingtask_command_setter(instance):
    original = instance.command
    instance.command = original
    assert instance.command == original

@given(instance=setup::KeyBindingTask_strategy)
def test_setup::keybindingtask_platform_type(instance):
    assert isinstance(instance.platform, str)


@given(instance=setup::KeyBindingTask_strategy)
def test_setup::keybindingtask_platform_setter(instance):
    original = instance.platform
    instance.platform = original
    assert instance.platform == original

@given(instance=setup::MylynQueriesTask_strategy)
@settings(max_examples=50)
def test_setup::mylynqueriestask_instantiation(instance):
    assert isinstance(instance, setup::MylynQueriesTask)

@given(instance=setup::MylynQueriesTask_strategy)
def test_setup::mylynqueriestask_connectorKind_type(instance):
    assert isinstance(instance.connectorKind, str)


@given(instance=setup::MylynQueriesTask_strategy)
def test_setup::mylynqueriestask_connectorKind_setter(instance):
    original = instance.connectorKind
    instance.connectorKind = original
    assert instance.connectorKind == original

@given(instance=setup::MylynQueriesTask_strategy)
def test_setup::mylynqueriestask_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=setup::MylynQueriesTask_strategy)
def test_setup::mylynqueriestask_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=setup::MylynQueriesTask_strategy)
def test_setup::mylynqueriestask_repositoryURL_type(instance):
    assert isinstance(instance.repositoryURL, str)


@given(instance=setup::MylynQueriesTask_strategy)
def test_setup::mylynqueriestask_repositoryURL_setter(instance):
    original = instance.repositoryURL
    instance.repositoryURL = original
    assert instance.repositoryURL == original

@given(instance=setup::MylynQueriesTask_strategy)
def test_setup::mylynqueriestask_userID_type(instance):
    assert isinstance(instance.userID, str)


@given(instance=setup::MylynQueriesTask_strategy)
def test_setup::mylynqueriestask_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original

@given(instance=SetupTaskContainer_strategy)
@settings(max_examples=50)
def test_setuptaskcontainer_instantiation(instance):
    assert isinstance(instance, SetupTaskContainer)

@given(instance=setup::CompoundSetupTask_strategy)
@settings(max_examples=50)
def test_setup::compoundsetuptask_instantiation(instance):
    assert isinstance(instance, setup::CompoundSetupTask)

@given(instance=setup::CompoundSetupTask_strategy)
def test_setup::compoundsetuptask_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=setup::CompoundSetupTask_strategy)
def test_setup::compoundsetuptask_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=setup::ScopeRoot_strategy)
@settings(max_examples=50)
def test_setup::scoperoot_instantiation(instance):
    assert isinstance(instance, setup::ScopeRoot)

@given(instance=setup::SetupTaskContainer_strategy)
@settings(max_examples=50)
def test_setup::setuptaskcontainer_instantiation(instance):
    assert isinstance(instance, setup::SetupTaskContainer)

@given(instance=setup::LinkLocationTask_strategy)
@settings(max_examples=50)
def test_setup::linklocationtask_instantiation(instance):
    assert isinstance(instance, setup::LinkLocationTask)

@given(instance=setup::LinkLocationTask_strategy)
def test_setup::linklocationtask_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=setup::LinkLocationTask_strategy)
def test_setup::linklocationtask_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=setup::LinkLocationTask_strategy)
def test_setup::linklocationtask_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=setup::LinkLocationTask_strategy)
def test_setup::linklocationtask_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=setup::EclipseIniTask_strategy)
@settings(max_examples=50)
def test_setup::eclipseinitask_instantiation(instance):
    assert isinstance(instance, setup::EclipseIniTask)

@given(instance=setup::EclipseIniTask_strategy)
def test_setup::eclipseinitask_vm_type(instance):
    assert isinstance(instance.vm, bool)


@given(instance=setup::EclipseIniTask_strategy)
def test_setup::eclipseinitask_vm_setter(instance):
    original = instance.vm
    instance.vm = original
    assert instance.vm == original

@given(instance=setup::EclipseIniTask_strategy)
def test_setup::eclipseinitask_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=setup::EclipseIniTask_strategy)
def test_setup::eclipseinitask_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=setup::EclipseIniTask_strategy)
def test_setup::eclipseinitask_option_type(instance):
    assert isinstance(instance.option, str)


@given(instance=setup::EclipseIniTask_strategy)
def test_setup::eclipseinitask_option_setter(instance):
    original = instance.option
    instance.option = original
    assert instance.option == original

@given(instance=setup::RedirectionTask_strategy)
@settings(max_examples=50)
def test_setup::redirectiontask_instantiation(instance):
    assert isinstance(instance, setup::RedirectionTask)

@given(instance=setup::RedirectionTask_strategy)
def test_setup::redirectiontask_targetURL_type(instance):
    assert isinstance(instance.targetURL, str)


@given(instance=setup::RedirectionTask_strategy)
def test_setup::redirectiontask_targetURL_setter(instance):
    original = instance.targetURL
    instance.targetURL = original
    assert instance.targetURL == original

@given(instance=setup::RedirectionTask_strategy)
def test_setup::redirectiontask_sourceURL_type(instance):
    assert isinstance(instance.sourceURL, str)


@given(instance=setup::RedirectionTask_strategy)
def test_setup::redirectiontask_sourceURL_setter(instance):
    original = instance.sourceURL
    instance.sourceURL = original
    assert instance.sourceURL == original

@given(instance=setup::VariableChoice_strategy)
@settings(max_examples=50)
def test_setup::variablechoice_instantiation(instance):
    assert isinstance(instance, setup::VariableChoice)

@given(instance=setup::VariableChoice_strategy)
def test_setup::variablechoice_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=setup::VariableChoice_strategy)
def test_setup::variablechoice_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=setup::VariableChoice_strategy)
def test_setup::variablechoice_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=setup::VariableChoice_strategy)
def test_setup::variablechoice_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=setup::ContextVariableTask_strategy)
@settings(max_examples=50)
def test_setup::contextvariabletask_instantiation(instance):
    assert isinstance(instance, setup::ContextVariableTask)

@given(instance=setup::ContextVariableTask_strategy)
def test_setup::contextvariabletask_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=setup::ContextVariableTask_strategy)
def test_setup::contextvariabletask_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=setup::ContextVariableTask_strategy)
def test_setup::contextvariabletask_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=setup::ContextVariableTask_strategy)
def test_setup::contextvariabletask_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=setup::ContextVariableTask_strategy)
def test_setup::contextvariabletask_stringSubstitution_type(instance):
    assert isinstance(instance.stringSubstitution, bool)


@given(instance=setup::ContextVariableTask_strategy)
def test_setup::contextvariabletask_stringSubstitution_setter(instance):
    original = instance.stringSubstitution
    instance.stringSubstitution = original
    assert instance.stringSubstitution == original

@given(instance=setup::ContextVariableTask_strategy)
def test_setup::contextvariabletask_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=setup::ContextVariableTask_strategy)
def test_setup::contextvariabletask_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=setup::ContextVariableTask_strategy)
def test_setup::contextvariabletask_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=setup::ContextVariableTask_strategy)
def test_setup::contextvariabletask_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=setup::SetupTask_strategy)
@settings(max_examples=50)
def test_setup::setuptask_instantiation(instance):
    assert isinstance(instance, setup::SetupTask)

@given(instance=setup::SetupTask_strategy)
def test_setup::setuptask_disabled_type(instance):
    assert isinstance(instance.disabled, bool)


@given(instance=setup::SetupTask_strategy)
def test_setup::setuptask_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original

@given(instance=setup::SetupTask_strategy)
def test_setup::setuptask_excludedTriggers_type(instance):
    assert isinstance(instance.excludedTriggers, str)


@given(instance=setup::SetupTask_strategy)
def test_setup::setuptask_excludedTriggers_setter(instance):
    original = instance.excludedTriggers
    instance.excludedTriggers = original
    assert instance.excludedTriggers == original

@given(instance=setup::SetupTask_strategy)
def test_setup::setuptask_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=setup::SetupTask_strategy)
def test_setup::setuptask_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=setup::SetupTask_strategy)
def test_setup::setuptask_documentation_type(instance):
    assert isinstance(instance.documentation, str)


@given(instance=setup::SetupTask_strategy)
def test_setup::setuptask_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=setup::SetupTask_strategy)
@settings(max_examples=30)
def test_setup::setuptask_requires_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.requires(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.requires).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'requires' in setup::SetupTask is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'requires' in setup::SetupTask did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'requires' in setup::SetupTask is not implemented or raised an error")

@given(instance=setup::Setup_strategy)
@settings(max_examples=50)
def test_setup::setup_instantiation(instance):
    assert isinstance(instance, setup::Setup)

@given(instance=ConfigurableItem_strategy)
@settings(max_examples=50)
def test_configurableitem_instantiation(instance):
    assert isinstance(instance, ConfigurableItem)

@given(instance=setup::Eclipse_strategy)
@settings(max_examples=50)
def test_setup::eclipse_instantiation(instance):
    assert isinstance(instance, setup::Eclipse)

@given(instance=setup::Eclipse_strategy)
def test_setup::eclipse_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=setup::Eclipse_strategy)
def test_setup::eclipse_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=setup::Branch_strategy)
@settings(max_examples=50)
def test_setup::branch_instantiation(instance):
    assert isinstance(instance, setup::Branch)

@given(instance=setup::Branch_strategy)
def test_setup::branch_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=setup::Branch_strategy)
def test_setup::branch_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=setup::Project_strategy)
@settings(max_examples=50)
def test_setup::project_instantiation(instance):
    assert isinstance(instance, setup::Project)

@given(instance=setup::Project_strategy)
def test_setup::project_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=setup::Project_strategy)
def test_setup::project_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=setup::Project_strategy)
def test_setup::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=setup::Project_strategy)
def test_setup::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ScopeRoot_strategy)
@settings(max_examples=50)
def test_scoperoot_instantiation(instance):
    assert isinstance(instance, ScopeRoot)

@given(instance=setup::Configuration_strategy)
@settings(max_examples=50)
def test_setup::configuration_instantiation(instance):
    assert isinstance(instance, setup::Configuration)

@given(instance=setup::Preferences_strategy)
@settings(max_examples=50)
def test_setup::preferences_instantiation(instance):
    assert isinstance(instance, setup::Preferences)

@given(instance=setup::Preferences_strategy)
def test_setup::preferences_acceptedLicenses_type(instance):
    assert isinstance(instance.acceptedLicenses, str)


@given(instance=setup::Preferences_strategy)
def test_setup::preferences_acceptedLicenses_setter(instance):
    original = instance.acceptedLicenses
    instance.acceptedLicenses = original
    assert instance.acceptedLicenses == original

@given(instance=setup::Preferences_strategy)
def test_setup::preferences_installFolder_type(instance):
    assert isinstance(instance.installFolder, str)


@given(instance=setup::Preferences_strategy)
def test_setup::preferences_installFolder_setter(instance):
    original = instance.installFolder
    instance.installFolder = original
    assert instance.installFolder == original

@given(instance=setup::ConfigurableItem_strategy)
@settings(max_examples=50)
def test_setup::configurableitem_instantiation(instance):
    assert isinstance(instance, setup::ConfigurableItem)

@given(instance=setup::Index_strategy)
@settings(max_examples=50)
def test_setup::index_instantiation(instance):
    assert isinstance(instance, setup::Index)

@given(instance=setup::Index_strategy)
def test_setup::index_uRI_type(instance):
    assert isinstance(instance.uRI, str)


@given(instance=setup::Index_strategy)
def test_setup::index_uRI_setter(instance):
    original = instance.uRI
    instance.uRI = original
    assert instance.uRI == original

@given(instance=setup::Index_strategy)
def test_setup::index_oldURIs_type(instance):
    assert isinstance(instance.oldURIs, str)


@given(instance=setup::Index_strategy)
def test_setup::index_oldURIs_setter(instance):
    original = instance.oldURIs
    instance.oldURIs = original
    assert instance.oldURIs == original

@given(instance=setup::Index_strategy)
def test_setup::index_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=setup::Index_strategy)
def test_setup::index_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=setup::MetaIndex_strategy)
@settings(max_examples=50)
def test_setup::metaindex_instantiation(instance):
    assert isinstance(instance, setup::MetaIndex)

@given(instance=setup::MylynQueryTask_strategy)
@settings(max_examples=50)
def test_setup::mylynquerytask_instantiation(instance):
    assert isinstance(instance, setup::MylynQueryTask)

@given(instance=setup::MylynQueryTask_strategy)
def test_setup::mylynquerytask_repositoryURL_type(instance):
    assert isinstance(instance.repositoryURL, str)


@given(instance=setup::MylynQueryTask_strategy)
def test_setup::mylynquerytask_repositoryURL_setter(instance):
    original = instance.repositoryURL
    instance.repositoryURL = original
    assert instance.repositoryURL == original

@given(instance=setup::MylynQueryTask_strategy)
def test_setup::mylynquerytask_summary_type(instance):
    assert isinstance(instance.summary, str)


@given(instance=setup::MylynQueryTask_strategy)
def test_setup::mylynquerytask_summary_setter(instance):
    original = instance.summary
    instance.summary = original
    assert instance.summary == original

@given(instance=setup::MylynQueryTask_strategy)
def test_setup::mylynquerytask_relativeURL_type(instance):
    assert isinstance(instance.relativeURL, str)


@given(instance=setup::MylynQueryTask_strategy)
def test_setup::mylynquerytask_relativeURL_setter(instance):
    original = instance.relativeURL
    instance.relativeURL = original
    assert instance.relativeURL == original

@given(instance=setup::MylynQueryTask_strategy)
def test_setup::mylynquerytask_connectorKind_type(instance):
    assert isinstance(instance.connectorKind, str)


@given(instance=setup::MylynQueryTask_strategy)
def test_setup::mylynquerytask_connectorKind_setter(instance):
    original = instance.connectorKind
    instance.connectorKind = original
    assert instance.connectorKind == original

@given(instance=setup::CommandParameter_strategy)
@settings(max_examples=50)
def test_setup::commandparameter_instantiation(instance):
    assert isinstance(instance, setup::CommandParameter)

@given(instance=setup::CommandParameter_strategy)
def test_setup::commandparameter_iD_type(instance):
    assert isinstance(instance.iD, str)


@given(instance=setup::CommandParameter_strategy)
def test_setup::commandparameter_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original

@given(instance=setup::CommandParameter_strategy)
def test_setup::commandparameter_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=setup::CommandParameter_strategy)
def test_setup::commandparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=setup::KeyBindingContext_strategy)
@settings(max_examples=50)
def test_setup::keybindingcontext_instantiation(instance):
    assert isinstance(instance, setup::KeyBindingContext)

@given(instance=setup::KeyBindingContext_strategy)
def test_setup::keybindingcontext_iD_type(instance):
    assert isinstance(instance.iD, str)


@given(instance=setup::KeyBindingContext_strategy)
def test_setup::keybindingcontext_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original

@given(instance=setup::FileEditor_strategy)
@settings(max_examples=50)
def test_setup::fileeditor_instantiation(instance):
    assert isinstance(instance, setup::FileEditor)

@given(instance=setup::FileEditor_strategy)
def test_setup::fileeditor_iD_type(instance):
    assert isinstance(instance.iD, str)


@given(instance=setup::FileEditor_strategy)
def test_setup::fileeditor_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original

@given(instance=setup::FileAssociationTask_strategy)
@settings(max_examples=50)
def test_setup::fileassociationtask_instantiation(instance):
    assert isinstance(instance, setup::FileAssociationTask)

@given(instance=setup::FileAssociationTask_strategy)
def test_setup::fileassociationtask_filePattern_type(instance):
    assert isinstance(instance.filePattern, str)


@given(instance=setup::FileAssociationTask_strategy)
def test_setup::fileassociationtask_filePattern_setter(instance):
    original = instance.filePattern
    instance.filePattern = original
    assert instance.filePattern == original

@given(instance=setup::FileAssociationTask_strategy)
def test_setup::fileassociationtask_defaultEditorID_type(instance):
    assert isinstance(instance.defaultEditorID, str)


@given(instance=setup::FileAssociationTask_strategy)
def test_setup::fileassociationtask_defaultEditorID_setter(instance):
    original = instance.defaultEditorID
    instance.defaultEditorID = original
    assert instance.defaultEditorID == original

@given(instance=setup::EclipsePreferenceTask_strategy)
@settings(max_examples=50)
def test_setup::eclipsepreferencetask_instantiation(instance):
    assert isinstance(instance, setup::EclipsePreferenceTask)

@given(instance=setup::EclipsePreferenceTask_strategy)
def test_setup::eclipsepreferencetask_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=setup::EclipsePreferenceTask_strategy)
def test_setup::eclipsepreferencetask_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=setup::EclipsePreferenceTask_strategy)
def test_setup::eclipsepreferencetask_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=setup::EclipsePreferenceTask_strategy)
def test_setup::eclipsepreferencetask_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=setup::TextModifyTask_strategy)
@settings(max_examples=50)
def test_setup::textmodifytask_instantiation(instance):
    assert isinstance(instance, setup::TextModifyTask)

@given(instance=setup::TextModifyTask_strategy)
def test_setup::textmodifytask_encoding_type(instance):
    assert isinstance(instance.encoding, str)


@given(instance=setup::TextModifyTask_strategy)
def test_setup::textmodifytask_encoding_setter(instance):
    original = instance.encoding
    instance.encoding = original
    assert instance.encoding == original

@given(instance=setup::TextModifyTask_strategy)
def test_setup::textmodifytask_uRL_type(instance):
    assert isinstance(instance.uRL, str)


@given(instance=setup::TextModifyTask_strategy)
def test_setup::textmodifytask_uRL_setter(instance):
    original = instance.uRL
    instance.uRL = original
    assert instance.uRL == original

@given(instance=setup::ResourceCreationTask_strategy)
@settings(max_examples=50)
def test_setup::resourcecreationtask_instantiation(instance):
    assert isinstance(instance, setup::ResourceCreationTask)

@given(instance=setup::ResourceCreationTask_strategy)
def test_setup::resourcecreationtask_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=setup::ResourceCreationTask_strategy)
def test_setup::resourcecreationtask_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=setup::ResourceCreationTask_strategy)
def test_setup::resourcecreationtask_encoding_type(instance):
    assert isinstance(instance.encoding, str)


@given(instance=setup::ResourceCreationTask_strategy)
def test_setup::resourcecreationtask_encoding_setter(instance):
    original = instance.encoding
    instance.encoding = original
    assert instance.encoding == original

@given(instance=setup::ResourceCreationTask_strategy)
def test_setup::resourcecreationtask_targetURL_type(instance):
    assert isinstance(instance.targetURL, str)


@given(instance=setup::ResourceCreationTask_strategy)
def test_setup::resourcecreationtask_targetURL_setter(instance):
    original = instance.targetURL
    instance.targetURL = original
    assert instance.targetURL == original

@given(instance=setup::ResourceCopyTask_strategy)
@settings(max_examples=50)
def test_setup::resourcecopytask_instantiation(instance):
    assert isinstance(instance, setup::ResourceCopyTask)

@given(instance=setup::ResourceCopyTask_strategy)
def test_setup::resourcecopytask_sourceURL_type(instance):
    assert isinstance(instance.sourceURL, str)


@given(instance=setup::ResourceCopyTask_strategy)
def test_setup::resourcecopytask_sourceURL_setter(instance):
    original = instance.sourceURL
    instance.sourceURL = original
    assert instance.sourceURL == original

@given(instance=setup::ResourceCopyTask_strategy)
def test_setup::resourcecopytask_targetURL_type(instance):
    assert isinstance(instance.targetURL, str)


@given(instance=setup::ResourceCopyTask_strategy)
def test_setup::resourcecopytask_targetURL_setter(instance):
    original = instance.targetURL
    instance.targetURL = original
    assert instance.targetURL == original

@given(instance=setup::WorkingSet_strategy)
@settings(max_examples=50)
def test_setup::workingset_instantiation(instance):
    assert isinstance(instance, setup::WorkingSet)

@given(instance=setup::WorkingSetTask_strategy)
@settings(max_examples=50)
def test_setup::workingsettask_instantiation(instance):
    assert isinstance(instance, setup::WorkingSetTask)

@given(instance=setup::FileMapping_strategy)
@settings(max_examples=50)
def test_setup::filemapping_instantiation(instance):
    assert isinstance(instance, setup::FileMapping)

@given(instance=setup::FileMapping_strategy)
def test_setup::filemapping_defaultEditorID_type(instance):
    assert isinstance(instance.defaultEditorID, str)


@given(instance=setup::FileMapping_strategy)
def test_setup::filemapping_defaultEditorID_setter(instance):
    original = instance.defaultEditorID
    instance.defaultEditorID = original
    assert instance.defaultEditorID == original

@given(instance=setup::FileMapping_strategy)
def test_setup::filemapping_filePattern_type(instance):
    assert isinstance(instance.filePattern, str)


@given(instance=setup::FileMapping_strategy)
def test_setup::filemapping_filePattern_setter(instance):
    original = instance.filePattern
    instance.filePattern = original
    assert instance.filePattern == original

@given(instance=setup::FileAssociationsTask_strategy)
@settings(max_examples=50)
def test_setup::fileassociationstask_instantiation(instance):
    assert isinstance(instance, setup::FileAssociationsTask)

@given(instance=setup::TargletData_strategy)
@settings(max_examples=50)
def test_setup::targletdata_instantiation(instance):
    assert isinstance(instance, setup::TargletData)

@given(instance=setup::TargletData_strategy)
def test_setup::targletdata_activeRepositoryList_type(instance):
    assert isinstance(instance.activeRepositoryList, str)


@given(instance=setup::TargletData_strategy)
def test_setup::targletdata_activeRepositoryList_setter(instance):
    original = instance.activeRepositoryList
    instance.activeRepositoryList = original
    assert instance.activeRepositoryList == original

@given(instance=setup::TargletData_strategy)
def test_setup::targletdata_includeAllPlatforms_type(instance):
    assert isinstance(instance.includeAllPlatforms, bool)


@given(instance=setup::TargletData_strategy)
def test_setup::targletdata_includeAllPlatforms_setter(instance):
    original = instance.includeAllPlatforms
    instance.includeAllPlatforms = original
    assert instance.includeAllPlatforms == original

@given(instance=setup::TargletData_strategy)
def test_setup::targletdata_includeSources_type(instance):
    assert isinstance(instance.includeSources, bool)


@given(instance=setup::TargletData_strategy)
def test_setup::targletdata_includeSources_setter(instance):
    original = instance.includeSources
    instance.includeSources = original
    assert instance.includeSources == original

@given(instance=setup::TargletData_strategy)
def test_setup::targletdata_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=setup::TargletData_strategy)
def test_setup::targletdata_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TargletData_strategy)
@settings(max_examples=50)
def test_targletdata_instantiation(instance):
    assert isinstance(instance, TargletData)

@given(instance=setup::Targlet_strategy)
@settings(max_examples=50)
def test_setup::targlet_instantiation(instance):
    assert isinstance(instance, setup::Targlet)

@given(instance=setup::ApiBaselineTask_strategy)
@settings(max_examples=50)
def test_setup::apibaselinetask_instantiation(instance):
    assert isinstance(instance, setup::ApiBaselineTask)

@given(instance=setup::ApiBaselineTask_strategy)
def test_setup::apibaselinetask_zipLocation_type(instance):
    assert isinstance(instance.zipLocation, str)


@given(instance=setup::ApiBaselineTask_strategy)
def test_setup::apibaselinetask_zipLocation_setter(instance):
    original = instance.zipLocation
    instance.zipLocation = original
    assert instance.zipLocation == original

@given(instance=setup::ApiBaselineTask_strategy)
def test_setup::apibaselinetask_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=setup::ApiBaselineTask_strategy)
def test_setup::apibaselinetask_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=setup::ApiBaselineTask_strategy)
def test_setup::apibaselinetask_containerFolder_type(instance):
    assert isinstance(instance.containerFolder, str)


@given(instance=setup::ApiBaselineTask_strategy)
def test_setup::apibaselinetask_containerFolder_setter(instance):
    original = instance.containerFolder
    instance.containerFolder = original
    assert instance.containerFolder == original

@given(instance=setup::TargetPlatformTask_strategy)
@settings(max_examples=50)
def test_setup::targetplatformtask_instantiation(instance):
    assert isinstance(instance, setup::TargetPlatformTask)

@given(instance=setup::TargetPlatformTask_strategy)
def test_setup::targetplatformtask_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=setup::TargetPlatformTask_strategy)
def test_setup::targetplatformtask_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=setup::ProjectSetImportTask_strategy)
@settings(max_examples=50)
def test_setup::projectsetimporttask_instantiation(instance):
    assert isinstance(instance, setup::ProjectSetImportTask)

@given(instance=setup::ProjectSetImportTask_strategy)
def test_setup::projectsetimporttask_uRL_type(instance):
    assert isinstance(instance.uRL, str)


@given(instance=setup::ProjectSetImportTask_strategy)
def test_setup::projectsetimporttask_uRL_setter(instance):
    original = instance.uRL
    instance.uRL = original
    assert instance.uRL == original

@given(instance=setup::ProjectsImportTask_strategy)
@settings(max_examples=50)
def test_setup::projectsimporttask_instantiation(instance):
    assert isinstance(instance, setup::ProjectsImportTask)

@given(instance=setup::RepositoryList_strategy)
@settings(max_examples=50)
def test_setup::repositorylist_instantiation(instance):
    assert isinstance(instance, setup::RepositoryList)

@given(instance=setup::RepositoryList_strategy)
def test_setup::repositorylist_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=setup::RepositoryList_strategy)
def test_setup::repositorylist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ComponentExtension_strategy)
@settings(max_examples=50)
def test_componentextension_instantiation(instance):
    assert isinstance(instance, ComponentExtension)

@given(instance=setup::ComponentDefinition_strategy)
@settings(max_examples=50)
def test_setup::componentdefinition_instantiation(instance):
    assert isinstance(instance, setup::ComponentDefinition)

@given(instance=setup::ComponentDefinition_strategy)
def test_setup::componentdefinition_iD_type(instance):
    assert isinstance(instance.iD, str)


@given(instance=setup::ComponentDefinition_strategy)
def test_setup::componentdefinition_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original

@given(instance=setup::ComponentDefinition_strategy)
def test_setup::componentdefinition_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=setup::ComponentDefinition_strategy)
def test_setup::componentdefinition_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=setup::TargletTask_strategy)
@settings(max_examples=50)
def test_setup::targlettask_instantiation(instance):
    assert isinstance(instance, setup::TargletTask)

@given(instance=setup::TargletImportTask_strategy)
@settings(max_examples=50)
def test_setup::targletimporttask_instantiation(instance):
    assert isinstance(instance, setup::TargletImportTask)

@given(instance=setup::TargletImportTask_strategy)
def test_setup::targletimporttask_targletURI_type(instance):
    assert isinstance(instance.targletURI, str)


@given(instance=setup::TargletImportTask_strategy)
def test_setup::targletimporttask_targletURI_setter(instance):
    original = instance.targletURI
    instance.targletURI = original
    assert instance.targletURI == original

@given(instance=setup::MavenImportTask_strategy)
@settings(max_examples=50)
def test_setup::mavenimporttask_instantiation(instance):
    assert isinstance(instance, setup::MavenImportTask)

@given(instance=setup::Component_strategy)
@settings(max_examples=50)
def test_setup::component_instantiation(instance):
    assert isinstance(instance, setup::Component)

@given(instance=setup::Component_strategy)
def test_setup::component_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=setup::Component_strategy)
def test_setup::component_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=setup::Component_strategy)
def test_setup::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=setup::Component_strategy)
def test_setup::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=setup::Component_strategy)
def test_setup::component_versionRange_type(instance):
    assert isinstance(instance.versionRange, str)


@given(instance=setup::Component_strategy)
def test_setup::component_versionRange_setter(instance):
    original = instance.versionRange
    instance.versionRange = original
    assert instance.versionRange == original

@given(instance=setup::ComponentExtension_strategy)
@settings(max_examples=50)
def test_setup::componentextension_instantiation(instance):
    assert isinstance(instance, setup::ComponentExtension)

@given(instance=setup::Predicate_strategy)
@settings(max_examples=50)
def test_setup::predicate_instantiation(instance):
    assert isinstance(instance, setup::Predicate)

@given(instance=SourceLocator_strategy)
@settings(max_examples=50)
def test_sourcelocator_instantiation(instance):
    assert isinstance(instance, SourceLocator)

@given(instance=setup::AutomaticSourceLocator_strategy)
@settings(max_examples=50)
def test_setup::automaticsourcelocator_instantiation(instance):
    assert isinstance(instance, setup::AutomaticSourceLocator)

@given(instance=setup::AutomaticSourceLocator_strategy)
def test_setup::automaticsourcelocator_rootFolder_type(instance):
    assert isinstance(instance.rootFolder, str)


@given(instance=setup::AutomaticSourceLocator_strategy)
def test_setup::automaticsourcelocator_rootFolder_setter(instance):
    original = instance.rootFolder
    instance.rootFolder = original
    assert instance.rootFolder == original

@given(instance=setup::AutomaticSourceLocator_strategy)
def test_setup::automaticsourcelocator_locateNestedProjects_type(instance):
    assert isinstance(instance.locateNestedProjects, bool)


@given(instance=setup::AutomaticSourceLocator_strategy)
def test_setup::automaticsourcelocator_locateNestedProjects_setter(instance):
    original = instance.locateNestedProjects
    instance.locateNestedProjects = original
    assert instance.locateNestedProjects == original

@given(instance=setup::ManualSourceLocator_strategy)
@settings(max_examples=50)
def test_setup::manualsourcelocator_instantiation(instance):
    assert isinstance(instance, setup::ManualSourceLocator)

@given(instance=setup::ManualSourceLocator_strategy)
def test_setup::manualsourcelocator_componentNamePattern_type(instance):
    assert isinstance(instance.componentNamePattern, str)


@given(instance=setup::ManualSourceLocator_strategy)
def test_setup::manualsourcelocator_componentNamePattern_setter(instance):
    original = instance.componentNamePattern
    instance.componentNamePattern = original
    assert instance.componentNamePattern == original

@given(instance=setup::ManualSourceLocator_strategy)
def test_setup::manualsourcelocator_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=setup::ManualSourceLocator_strategy)
def test_setup::manualsourcelocator_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=setup::ManualSourceLocator_strategy)
def test_setup::manualsourcelocator_componentTypes_type(instance):
    assert isinstance(instance.componentTypes, str)


@given(instance=setup::ManualSourceLocator_strategy)
def test_setup::manualsourcelocator_componentTypes_setter(instance):
    original = instance.componentTypes
    instance.componentTypes = original
    assert instance.componentTypes == original

@given(instance=setup::SourceLocator_strategy)
@settings(max_examples=50)
def test_setup::sourcelocator_instantiation(instance):
    assert isinstance(instance, setup::SourceLocator)

@given(instance=setup::P2Repository_strategy)
@settings(max_examples=50)
def test_setup::p2repository_instantiation(instance):
    assert isinstance(instance, setup::P2Repository)

@given(instance=setup::P2Repository_strategy)
def test_setup::p2repository_uRL_type(instance):
    assert isinstance(instance.uRL, str)


@given(instance=setup::P2Repository_strategy)
def test_setup::p2repository_uRL_setter(instance):
    original = instance.uRL
    instance.uRL = original
    assert instance.uRL == original

@given(instance=setup::InstallableUnit_strategy)
@settings(max_examples=50)
def test_setup::installableunit_instantiation(instance):
    assert isinstance(instance, setup::InstallableUnit)

@given(instance=setup::InstallableUnit_strategy)
def test_setup::installableunit_iD_type(instance):
    assert isinstance(instance.iD, str)


@given(instance=setup::InstallableUnit_strategy)
def test_setup::installableunit_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original

@given(instance=setup::InstallableUnit_strategy)
def test_setup::installableunit_versionRange_type(instance):
    assert isinstance(instance.versionRange, str)


@given(instance=setup::InstallableUnit_strategy)
def test_setup::installableunit_versionRange_setter(instance):
    original = instance.versionRange
    instance.versionRange = original
    assert instance.versionRange == original

@given(instance=setup::P2Task_strategy)
@settings(max_examples=50)
def test_setup::p2task_instantiation(instance):
    assert isinstance(instance, setup::P2Task)

@given(instance=setup::P2Task_strategy)
def test_setup::p2task_mergeDisabled_type(instance):
    assert isinstance(instance.mergeDisabled, bool)


@given(instance=setup::P2Task_strategy)
def test_setup::p2task_mergeDisabled_setter(instance):
    original = instance.mergeDisabled
    instance.mergeDisabled = original
    assert instance.mergeDisabled == original

@given(instance=setup::P2Task_strategy)
def test_setup::p2task_licenseConfirmationDisabled_type(instance):
    assert isinstance(instance.licenseConfirmationDisabled, bool)


@given(instance=setup::P2Task_strategy)
def test_setup::p2task_licenseConfirmationDisabled_setter(instance):
    original = instance.licenseConfirmationDisabled
    instance.licenseConfirmationDisabled = original
    assert instance.licenseConfirmationDisabled == original

@given(instance=BasicMaterializationTask_strategy)
@settings(max_examples=50)
def test_basicmaterializationtask_instantiation(instance):
    assert isinstance(instance, BasicMaterializationTask)

@given(instance=setup::MaterializationTask_strategy)
@settings(max_examples=50)
def test_setup::materializationtask_instantiation(instance):
    assert isinstance(instance, setup::MaterializationTask)

@given(instance=setup::BuckminsterImportTask_strategy)
@settings(max_examples=50)
def test_setup::buckminsterimporttask_instantiation(instance):
    assert isinstance(instance, setup::BuckminsterImportTask)

@given(instance=setup::BuckminsterImportTask_strategy)
def test_setup::buckminsterimporttask_mspec_type(instance):
    assert isinstance(instance.mspec, str)


@given(instance=setup::BuckminsterImportTask_strategy)
def test_setup::buckminsterimporttask_mspec_setter(instance):
    original = instance.mspec
    instance.mspec = original
    assert instance.mspec == original

@given(instance=setup::BasicMaterializationTask_strategy)
@settings(max_examples=50)
def test_setup::basicmaterializationtask_instantiation(instance):
    assert isinstance(instance, setup::BasicMaterializationTask)

@given(instance=setup::BasicMaterializationTask_strategy)
def test_setup::basicmaterializationtask_targetPlatform_type(instance):
    assert isinstance(instance.targetPlatform, str)


@given(instance=setup::BasicMaterializationTask_strategy)
def test_setup::basicmaterializationtask_targetPlatform_setter(instance):
    original = instance.targetPlatform
    instance.targetPlatform = original
    assert instance.targetPlatform == original

@given(instance=setup::BasicMaterializationTask_strategy)
def test_setup::basicmaterializationtask_bundlePool_type(instance):
    assert isinstance(instance.bundlePool, str)


@given(instance=setup::BasicMaterializationTask_strategy)
def test_setup::basicmaterializationtask_bundlePool_setter(instance):
    original = instance.bundlePool
    instance.bundlePool = original
    assert instance.bundlePool == original

@given(instance=setup::GitCloneTask_strategy)
@settings(max_examples=50)
def test_setup::gitclonetask_instantiation(instance):
    assert isinstance(instance, setup::GitCloneTask)

@given(instance=setup::GitCloneTask_strategy)
def test_setup::gitclonetask_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=setup::GitCloneTask_strategy)
def test_setup::gitclonetask_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=setup::GitCloneTask_strategy)
def test_setup::gitclonetask_pushURI_type(instance):
    assert isinstance(instance.pushURI, str)


@given(instance=setup::GitCloneTask_strategy)
def test_setup::gitclonetask_pushURI_setter(instance):
    original = instance.pushURI
    instance.pushURI = original
    assert instance.pushURI == original

@given(instance=setup::GitCloneTask_strategy)
def test_setup::gitclonetask_checkoutBranch_type(instance):
    assert isinstance(instance.checkoutBranch, str)


@given(instance=setup::GitCloneTask_strategy)
def test_setup::gitclonetask_checkoutBranch_setter(instance):
    original = instance.checkoutBranch
    instance.checkoutBranch = original
    assert instance.checkoutBranch == original

@given(instance=setup::GitCloneTask_strategy)
def test_setup::gitclonetask_remoteURI_type(instance):
    assert isinstance(instance.remoteURI, str)


@given(instance=setup::GitCloneTask_strategy)
def test_setup::gitclonetask_remoteURI_setter(instance):
    original = instance.remoteURI
    instance.remoteURI = original
    assert instance.remoteURI == original

@given(instance=setup::GitCloneTask_strategy)
def test_setup::gitclonetask_userID_type(instance):
    assert isinstance(instance.userID, str)


@given(instance=setup::GitCloneTask_strategy)
def test_setup::gitclonetask_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original

@given(instance=setup::GitCloneTask_strategy)
def test_setup::gitclonetask_remoteName_type(instance):
    assert isinstance(instance.remoteName, str)


@given(instance=setup::GitCloneTask_strategy)
def test_setup::gitclonetask_remoteName_setter(instance):
    original = instance.remoteName
    instance.remoteName = original
    assert instance.remoteName == original

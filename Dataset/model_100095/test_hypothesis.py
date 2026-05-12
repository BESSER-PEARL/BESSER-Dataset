import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    setup_Query,
    setup_BuildPlan,
    setup_QueryAttribute,
    setup_TextModification,
    setup_CommandParameter,
    setup_KeyBindingContext,
    setup_FileEditor,
    setup_WorkingSet,
    setup_FileMapping,
    setup_TargletData,
    TargletData,
    setup_Targlet,
    setup_RepositoryList,
    ComponentExtension,
    setup_ComponentDefinition,
    setup_Component,
    setup_ComponentExtension,
    setup_Predicate,
    SourceLocator,
    setup_AutomaticSourceLocator,
    setup_ManualSourceLocator,
    setup_SourceLocator,
    setup_P2Repository,
    setup_InstallableUnit,
    BasicMaterializationTask,
    setup_MaterializationTask,
    setup_BuckminsterImportTask,
    SetupTask,
    setup_ProjectSetImportTask,
    setup_EclipsePreferenceTask,
    setup_TargletImportTask,
    setup_JRETask,
    setup_TextModifyTask,
    setup_ProjectsImportTask,
    setup_MylynQueryTask,
    setup_FileAssociationTask,
    setup_ResourceCopyTask,
    setup_KeyBindingTask,
    setup_MylynBuildsTask,
    setup_ResourceCreationTask,
    setup_GitCloneTask,
    setup_BasicMaterializationTask,
    setup_FileAssociationsTask,
    setup_WorkingSetTask,
    setup_ApiBaselineTask,
    setup_TargetPlatformTask,
    setup_MylynQueriesTask,
    setup_TargletTask,
    setup_MavenImportTask,
    setup_P2Task,
    SetupTaskContainer,
    setup_CompoundSetupTask,
    setup_ScopeRoot,
    setup_SetupTaskContainer,
    setup_LinkLocationTask,
    setup_EclipseIniTask,
    setup_RedirectionTask,
    setup_VariableChoice,
    setup_ContextVariableTask,
    setup_SetupTask,
    setup_Setup,
    ConfigurableItem,
    setup_Eclipse,
    setup_Branch,
    setup_Project,
    ScopeRoot,
    setup_ConfigurableItem,
    setup_Preferences,
    setup_Configuration,
    setup_Index,
    setup_MetaIndex,
    VariableType,
    Trigger,
    SetupTaskScope,
    ComponentType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_setup_query_is_not_abstract():
    assert not inspect.isabstract(setup_Query)


def test_setup_query_constructor_exists():
    assert callable(setup_Query.__init__)


def test_setup_query_constructor_args():
    sig = inspect.signature(setup_Query.__init__)
    params = list(sig.parameters.keys())
    assert "uRL" in params, "Missing parameter 'uRL'"
    assert "summary" in params, "Missing parameter 'summary'"

def test_setup_query_has_uRL():
    assert hasattr(setup_Query, "uRL")
    descriptor = None
    for klass in setup_Query.__mro__:
        if "uRL" in klass.__dict__:
            descriptor = klass.__dict__["uRL"]
            break
    assert isinstance(descriptor, property)

def test_setup_query_has_summary():
    assert hasattr(setup_Query, "summary")
    descriptor = None
    for klass in setup_Query.__mro__:
        if "summary" in klass.__dict__:
            descriptor = klass.__dict__["summary"]
            break
    assert isinstance(descriptor, property)



def test_setup_buildplan_is_not_abstract():
    assert not inspect.isabstract(setup_BuildPlan)


def test_setup_buildplan_constructor_exists():
    assert callable(setup_BuildPlan.__init__)


def test_setup_buildplan_constructor_args():
    sig = inspect.signature(setup_BuildPlan.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_setup_buildplan_has_name():
    assert hasattr(setup_BuildPlan, "name")
    descriptor = None
    for klass in setup_BuildPlan.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_setup_queryattribute_is_not_abstract():
    assert not inspect.isabstract(setup_QueryAttribute)


def test_setup_queryattribute_constructor_exists():
    assert callable(setup_QueryAttribute.__init__)


def test_setup_queryattribute_constructor_args():
    sig = inspect.signature(setup_QueryAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_setup_queryattribute_has_value():
    assert hasattr(setup_QueryAttribute, "value")
    descriptor = None
    for klass in setup_QueryAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_setup_queryattribute_has_key():
    assert hasattr(setup_QueryAttribute, "key")
    descriptor = None
    for klass in setup_QueryAttribute.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_setup_textmodification_is_not_abstract():
    assert not inspect.isabstract(setup_TextModification)


def test_setup_textmodification_constructor_exists():
    assert callable(setup_TextModification.__init__)


def test_setup_textmodification_constructor_args():
    sig = inspect.signature(setup_TextModification.__init__)
    params = list(sig.parameters.keys())
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "substitutions" in params, "Missing parameter 'substitutions'"

def test_setup_textmodification_has_pattern():
    assert hasattr(setup_TextModification, "pattern")
    descriptor = None
    for klass in setup_TextModification.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_setup_textmodification_has_substitutions():
    assert hasattr(setup_TextModification, "substitutions")
    descriptor = None
    for klass in setup_TextModification.__mro__:
        if "substitutions" in klass.__dict__:
            descriptor = klass.__dict__["substitutions"]
            break
    assert isinstance(descriptor, property)



def test_setup_commandparameter_is_not_abstract():
    assert not inspect.isabstract(setup_CommandParameter)


def test_setup_commandparameter_constructor_exists():
    assert callable(setup_CommandParameter.__init__)


def test_setup_commandparameter_constructor_args():
    sig = inspect.signature(setup_CommandParameter.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"
    assert "value" in params, "Missing parameter 'value'"

def test_setup_commandparameter_has_iD():
    assert hasattr(setup_CommandParameter, "iD")
    descriptor = None
    for klass in setup_CommandParameter.__mro__:
        if "iD" in klass.__dict__:
            descriptor = klass.__dict__["iD"]
            break
    assert isinstance(descriptor, property)

def test_setup_commandparameter_has_value():
    assert hasattr(setup_CommandParameter, "value")
    descriptor = None
    for klass in setup_CommandParameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_setup_keybindingcontext_is_not_abstract():
    assert not inspect.isabstract(setup_KeyBindingContext)


def test_setup_keybindingcontext_constructor_exists():
    assert callable(setup_KeyBindingContext.__init__)


def test_setup_keybindingcontext_constructor_args():
    sig = inspect.signature(setup_KeyBindingContext.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"

def test_setup_keybindingcontext_has_iD():
    assert hasattr(setup_KeyBindingContext, "iD")
    descriptor = None
    for klass in setup_KeyBindingContext.__mro__:
        if "iD" in klass.__dict__:
            descriptor = klass.__dict__["iD"]
            break
    assert isinstance(descriptor, property)



def test_setup_fileeditor_is_not_abstract():
    assert not inspect.isabstract(setup_FileEditor)


def test_setup_fileeditor_constructor_exists():
    assert callable(setup_FileEditor.__init__)


def test_setup_fileeditor_constructor_args():
    sig = inspect.signature(setup_FileEditor.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"

def test_setup_fileeditor_has_iD():
    assert hasattr(setup_FileEditor, "iD")
    descriptor = None
    for klass in setup_FileEditor.__mro__:
        if "iD" in klass.__dict__:
            descriptor = klass.__dict__["iD"]
            break
    assert isinstance(descriptor, property)



def test_setup_workingset_is_not_abstract():
    assert not inspect.isabstract(setup_WorkingSet)


def test_setup_workingset_constructor_exists():
    assert callable(setup_WorkingSet.__init__)


def test_setup_workingset_constructor_args():
    sig = inspect.signature(setup_WorkingSet.__init__)
    params = list(sig.parameters.keys())



def test_setup_filemapping_is_not_abstract():
    assert not inspect.isabstract(setup_FileMapping)


def test_setup_filemapping_constructor_exists():
    assert callable(setup_FileMapping.__init__)


def test_setup_filemapping_constructor_args():
    sig = inspect.signature(setup_FileMapping.__init__)
    params = list(sig.parameters.keys())
    assert "filePattern" in params, "Missing parameter 'filePattern'"
    assert "defaultEditorID" in params, "Missing parameter 'defaultEditorID'"

def test_setup_filemapping_has_filePattern():
    assert hasattr(setup_FileMapping, "filePattern")
    descriptor = None
    for klass in setup_FileMapping.__mro__:
        if "filePattern" in klass.__dict__:
            descriptor = klass.__dict__["filePattern"]
            break
    assert isinstance(descriptor, property)

def test_setup_filemapping_has_defaultEditorID():
    assert hasattr(setup_FileMapping, "defaultEditorID")
    descriptor = None
    for klass in setup_FileMapping.__mro__:
        if "defaultEditorID" in klass.__dict__:
            descriptor = klass.__dict__["defaultEditorID"]
            break
    assert isinstance(descriptor, property)



def test_setup_targletdata_is_not_abstract():
    assert not inspect.isabstract(setup_TargletData)


def test_setup_targletdata_constructor_exists():
    assert callable(setup_TargletData.__init__)


def test_setup_targletdata_constructor_args():
    sig = inspect.signature(setup_TargletData.__init__)
    params = list(sig.parameters.keys())
    assert "includeAllPlatforms" in params, "Missing parameter 'includeAllPlatforms'"
    assert "activeRepositoryList" in params, "Missing parameter 'activeRepositoryList'"
    assert "includeSources" in params, "Missing parameter 'includeSources'"
    assert "name" in params, "Missing parameter 'name'"

def test_setup_targletdata_has_includeAllPlatforms():
    assert hasattr(setup_TargletData, "includeAllPlatforms")
    descriptor = None
    for klass in setup_TargletData.__mro__:
        if "includeAllPlatforms" in klass.__dict__:
            descriptor = klass.__dict__["includeAllPlatforms"]
            break
    assert isinstance(descriptor, property)

def test_setup_targletdata_has_activeRepositoryList():
    assert hasattr(setup_TargletData, "activeRepositoryList")
    descriptor = None
    for klass in setup_TargletData.__mro__:
        if "activeRepositoryList" in klass.__dict__:
            descriptor = klass.__dict__["activeRepositoryList"]
            break
    assert isinstance(descriptor, property)

def test_setup_targletdata_has_includeSources():
    assert hasattr(setup_TargletData, "includeSources")
    descriptor = None
    for klass in setup_TargletData.__mro__:
        if "includeSources" in klass.__dict__:
            descriptor = klass.__dict__["includeSources"]
            break
    assert isinstance(descriptor, property)

def test_setup_targletdata_has_name():
    assert hasattr(setup_TargletData, "name")
    descriptor = None
    for klass in setup_TargletData.__mro__:
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



def test_setup_targlet_is_not_abstract():
    assert not inspect.isabstract(setup_Targlet)


def test_setup_targlet_constructor_exists():
    assert callable(setup_Targlet.__init__)


def test_setup_targlet_constructor_args():
    sig = inspect.signature(setup_Targlet.__init__)
    params = list(sig.parameters.keys())



def test_setup_repositorylist_is_not_abstract():
    assert not inspect.isabstract(setup_RepositoryList)


def test_setup_repositorylist_constructor_exists():
    assert callable(setup_RepositoryList.__init__)


def test_setup_repositorylist_constructor_args():
    sig = inspect.signature(setup_RepositoryList.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_setup_repositorylist_has_name():
    assert hasattr(setup_RepositoryList, "name")
    descriptor = None
    for klass in setup_RepositoryList.__mro__:
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



def test_setup_componentdefinition_is_not_abstract():
    assert not inspect.isabstract(setup_ComponentDefinition)


def test_setup_componentdefinition_constructor_exists():
    assert callable(setup_ComponentDefinition.__init__)


def test_setup_componentdefinition_constructor_args():
    sig = inspect.signature(setup_ComponentDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "iD" in params, "Missing parameter 'iD'"

def test_setup_componentdefinition_has_version():
    assert hasattr(setup_ComponentDefinition, "version")
    descriptor = None
    for klass in setup_ComponentDefinition.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_setup_componentdefinition_has_iD():
    assert hasattr(setup_ComponentDefinition, "iD")
    descriptor = None
    for klass in setup_ComponentDefinition.__mro__:
        if "iD" in klass.__dict__:
            descriptor = klass.__dict__["iD"]
            break
    assert isinstance(descriptor, property)



def test_setup_component_is_not_abstract():
    assert not inspect.isabstract(setup_Component)


def test_setup_component_constructor_exists():
    assert callable(setup_Component.__init__)


def test_setup_component_constructor_args():
    sig = inspect.signature(setup_Component.__init__)
    params = list(sig.parameters.keys())
    assert "versionRange" in params, "Missing parameter 'versionRange'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_setup_component_has_versionRange():
    assert hasattr(setup_Component, "versionRange")
    descriptor = None
    for klass in setup_Component.__mro__:
        if "versionRange" in klass.__dict__:
            descriptor = klass.__dict__["versionRange"]
            break
    assert isinstance(descriptor, property)

def test_setup_component_has_type():
    assert hasattr(setup_Component, "type")
    descriptor = None
    for klass in setup_Component.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_setup_component_has_name():
    assert hasattr(setup_Component, "name")
    descriptor = None
    for klass in setup_Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_setup_componentextension_is_not_abstract():
    assert not inspect.isabstract(setup_ComponentExtension)


def test_setup_componentextension_constructor_exists():
    assert callable(setup_ComponentExtension.__init__)


def test_setup_componentextension_constructor_args():
    sig = inspect.signature(setup_ComponentExtension.__init__)
    params = list(sig.parameters.keys())



def test_setup_predicate_is_not_abstract():
    assert not inspect.isabstract(setup_Predicate)


def test_setup_predicate_constructor_exists():
    assert callable(setup_Predicate.__init__)


def test_setup_predicate_constructor_args():
    sig = inspect.signature(setup_Predicate.__init__)
    params = list(sig.parameters.keys())



def test_sourcelocator_is_not_abstract():
    assert not inspect.isabstract(SourceLocator)


def test_sourcelocator_constructor_exists():
    assert callable(SourceLocator.__init__)


def test_sourcelocator_constructor_args():
    sig = inspect.signature(SourceLocator.__init__)
    params = list(sig.parameters.keys())



def test_setup_automaticsourcelocator_is_not_abstract():
    assert not inspect.isabstract(setup_AutomaticSourceLocator)


def test_setup_automaticsourcelocator_constructor_exists():
    assert callable(setup_AutomaticSourceLocator.__init__)


def test_setup_automaticsourcelocator_constructor_args():
    sig = inspect.signature(setup_AutomaticSourceLocator.__init__)
    params = list(sig.parameters.keys())
    assert "locateNestedProjects" in params, "Missing parameter 'locateNestedProjects'"
    assert "rootFolder" in params, "Missing parameter 'rootFolder'"

def test_setup_automaticsourcelocator_has_locateNestedProjects():
    assert hasattr(setup_AutomaticSourceLocator, "locateNestedProjects")
    descriptor = None
    for klass in setup_AutomaticSourceLocator.__mro__:
        if "locateNestedProjects" in klass.__dict__:
            descriptor = klass.__dict__["locateNestedProjects"]
            break
    assert isinstance(descriptor, property)

def test_setup_automaticsourcelocator_has_rootFolder():
    assert hasattr(setup_AutomaticSourceLocator, "rootFolder")
    descriptor = None
    for klass in setup_AutomaticSourceLocator.__mro__:
        if "rootFolder" in klass.__dict__:
            descriptor = klass.__dict__["rootFolder"]
            break
    assert isinstance(descriptor, property)



def test_setup_manualsourcelocator_is_not_abstract():
    assert not inspect.isabstract(setup_ManualSourceLocator)


def test_setup_manualsourcelocator_constructor_exists():
    assert callable(setup_ManualSourceLocator.__init__)


def test_setup_manualsourcelocator_constructor_args():
    sig = inspect.signature(setup_ManualSourceLocator.__init__)
    params = list(sig.parameters.keys())
    assert "componentTypes" in params, "Missing parameter 'componentTypes'"
    assert "location" in params, "Missing parameter 'location'"
    assert "componentNamePattern" in params, "Missing parameter 'componentNamePattern'"

def test_setup_manualsourcelocator_has_componentTypes():
    assert hasattr(setup_ManualSourceLocator, "componentTypes")
    descriptor = None
    for klass in setup_ManualSourceLocator.__mro__:
        if "componentTypes" in klass.__dict__:
            descriptor = klass.__dict__["componentTypes"]
            break
    assert isinstance(descriptor, property)

def test_setup_manualsourcelocator_has_location():
    assert hasattr(setup_ManualSourceLocator, "location")
    descriptor = None
    for klass in setup_ManualSourceLocator.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_setup_manualsourcelocator_has_componentNamePattern():
    assert hasattr(setup_ManualSourceLocator, "componentNamePattern")
    descriptor = None
    for klass in setup_ManualSourceLocator.__mro__:
        if "componentNamePattern" in klass.__dict__:
            descriptor = klass.__dict__["componentNamePattern"]
            break
    assert isinstance(descriptor, property)



def test_setup_sourcelocator_is_not_abstract():
    assert not inspect.isabstract(setup_SourceLocator)


def test_setup_sourcelocator_constructor_exists():
    assert callable(setup_SourceLocator.__init__)


def test_setup_sourcelocator_constructor_args():
    sig = inspect.signature(setup_SourceLocator.__init__)
    params = list(sig.parameters.keys())



def test_setup_p2repository_is_not_abstract():
    assert not inspect.isabstract(setup_P2Repository)


def test_setup_p2repository_constructor_exists():
    assert callable(setup_P2Repository.__init__)


def test_setup_p2repository_constructor_args():
    sig = inspect.signature(setup_P2Repository.__init__)
    params = list(sig.parameters.keys())
    assert "uRL" in params, "Missing parameter 'uRL'"

def test_setup_p2repository_has_uRL():
    assert hasattr(setup_P2Repository, "uRL")
    descriptor = None
    for klass in setup_P2Repository.__mro__:
        if "uRL" in klass.__dict__:
            descriptor = klass.__dict__["uRL"]
            break
    assert isinstance(descriptor, property)



def test_setup_installableunit_is_not_abstract():
    assert not inspect.isabstract(setup_InstallableUnit)


def test_setup_installableunit_constructor_exists():
    assert callable(setup_InstallableUnit.__init__)


def test_setup_installableunit_constructor_args():
    sig = inspect.signature(setup_InstallableUnit.__init__)
    params = list(sig.parameters.keys())
    assert "versionRange" in params, "Missing parameter 'versionRange'"
    assert "iD" in params, "Missing parameter 'iD'"

def test_setup_installableunit_has_versionRange():
    assert hasattr(setup_InstallableUnit, "versionRange")
    descriptor = None
    for klass in setup_InstallableUnit.__mro__:
        if "versionRange" in klass.__dict__:
            descriptor = klass.__dict__["versionRange"]
            break
    assert isinstance(descriptor, property)

def test_setup_installableunit_has_iD():
    assert hasattr(setup_InstallableUnit, "iD")
    descriptor = None
    for klass in setup_InstallableUnit.__mro__:
        if "iD" in klass.__dict__:
            descriptor = klass.__dict__["iD"]
            break
    assert isinstance(descriptor, property)



def test_basicmaterializationtask_is_not_abstract():
    assert not inspect.isabstract(BasicMaterializationTask)


def test_basicmaterializationtask_constructor_exists():
    assert callable(BasicMaterializationTask.__init__)


def test_basicmaterializationtask_constructor_args():
    sig = inspect.signature(BasicMaterializationTask.__init__)
    params = list(sig.parameters.keys())



def test_setup_materializationtask_is_not_abstract():
    assert not inspect.isabstract(setup_MaterializationTask)


def test_setup_materializationtask_constructor_exists():
    assert callable(setup_MaterializationTask.__init__)


def test_setup_materializationtask_constructor_args():
    sig = inspect.signature(setup_MaterializationTask.__init__)
    params = list(sig.parameters.keys())



def test_setup_buckminsterimporttask_is_not_abstract():
    assert not inspect.isabstract(setup_BuckminsterImportTask)


def test_setup_buckminsterimporttask_constructor_exists():
    assert callable(setup_BuckminsterImportTask.__init__)


def test_setup_buckminsterimporttask_constructor_args():
    sig = inspect.signature(setup_BuckminsterImportTask.__init__)
    params = list(sig.parameters.keys())
    assert "mspec" in params, "Missing parameter 'mspec'"

def test_setup_buckminsterimporttask_has_mspec():
    assert hasattr(setup_BuckminsterImportTask, "mspec")
    descriptor = None
    for klass in setup_BuckminsterImportTask.__mro__:
        if "mspec" in klass.__dict__:
            descriptor = klass.__dict__["mspec"]
            break
    assert isinstance(descriptor, property)



def test_setuptask_is_not_abstract():
    assert not inspect.isabstract(SetupTask)


def test_setuptask_constructor_exists():
    assert callable(SetupTask.__init__)


def test_setuptask_constructor_args():
    sig = inspect.signature(SetupTask.__init__)
    params = list(sig.parameters.keys())



def test_setup_projectsetimporttask_is_not_abstract():
    assert not inspect.isabstract(setup_ProjectSetImportTask)


def test_setup_projectsetimporttask_constructor_exists():
    assert callable(setup_ProjectSetImportTask.__init__)


def test_setup_projectsetimporttask_constructor_args():
    sig = inspect.signature(setup_ProjectSetImportTask.__init__)
    params = list(sig.parameters.keys())
    assert "uRL" in params, "Missing parameter 'uRL'"

def test_setup_projectsetimporttask_has_uRL():
    assert hasattr(setup_ProjectSetImportTask, "uRL")
    descriptor = None
    for klass in setup_ProjectSetImportTask.__mro__:
        if "uRL" in klass.__dict__:
            descriptor = klass.__dict__["uRL"]
            break
    assert isinstance(descriptor, property)



def test_setup_eclipsepreferencetask_is_not_abstract():
    assert not inspect.isabstract(setup_EclipsePreferenceTask)


def test_setup_eclipsepreferencetask_constructor_exists():
    assert callable(setup_EclipsePreferenceTask.__init__)


def test_setup_eclipsepreferencetask_constructor_args():
    sig = inspect.signature(setup_EclipsePreferenceTask.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_setup_eclipsepreferencetask_has_key():
    assert hasattr(setup_EclipsePreferenceTask, "key")
    descriptor = None
    for klass in setup_EclipsePreferenceTask.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_setup_eclipsepreferencetask_has_value():
    assert hasattr(setup_EclipsePreferenceTask, "value")
    descriptor = None
    for klass in setup_EclipsePreferenceTask.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_setup_targletimporttask_is_not_abstract():
    assert not inspect.isabstract(setup_TargletImportTask)


def test_setup_targletimporttask_constructor_exists():
    assert callable(setup_TargletImportTask.__init__)


def test_setup_targletimporttask_constructor_args():
    sig = inspect.signature(setup_TargletImportTask.__init__)
    params = list(sig.parameters.keys())
    assert "targletURI" in params, "Missing parameter 'targletURI'"

def test_setup_targletimporttask_has_targletURI():
    assert hasattr(setup_TargletImportTask, "targletURI")
    descriptor = None
    for klass in setup_TargletImportTask.__mro__:
        if "targletURI" in klass.__dict__:
            descriptor = klass.__dict__["targletURI"]
            break
    assert isinstance(descriptor, property)



def test_setup_jretask_is_not_abstract():
    assert not inspect.isabstract(setup_JRETask)


def test_setup_jretask_constructor_exists():
    assert callable(setup_JRETask.__init__)


def test_setup_jretask_constructor_args():
    sig = inspect.signature(setup_JRETask.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "version" in params, "Missing parameter 'version'"

def test_setup_jretask_has_location():
    assert hasattr(setup_JRETask, "location")
    descriptor = None
    for klass in setup_JRETask.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_setup_jretask_has_version():
    assert hasattr(setup_JRETask, "version")
    descriptor = None
    for klass in setup_JRETask.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_setup_textmodifytask_is_not_abstract():
    assert not inspect.isabstract(setup_TextModifyTask)


def test_setup_textmodifytask_constructor_exists():
    assert callable(setup_TextModifyTask.__init__)


def test_setup_textmodifytask_constructor_args():
    sig = inspect.signature(setup_TextModifyTask.__init__)
    params = list(sig.parameters.keys())
    assert "uRL" in params, "Missing parameter 'uRL'"
    assert "encoding" in params, "Missing parameter 'encoding'"

def test_setup_textmodifytask_has_uRL():
    assert hasattr(setup_TextModifyTask, "uRL")
    descriptor = None
    for klass in setup_TextModifyTask.__mro__:
        if "uRL" in klass.__dict__:
            descriptor = klass.__dict__["uRL"]
            break
    assert isinstance(descriptor, property)

def test_setup_textmodifytask_has_encoding():
    assert hasattr(setup_TextModifyTask, "encoding")
    descriptor = None
    for klass in setup_TextModifyTask.__mro__:
        if "encoding" in klass.__dict__:
            descriptor = klass.__dict__["encoding"]
            break
    assert isinstance(descriptor, property)



def test_setup_projectsimporttask_is_not_abstract():
    assert not inspect.isabstract(setup_ProjectsImportTask)


def test_setup_projectsimporttask_constructor_exists():
    assert callable(setup_ProjectsImportTask.__init__)


def test_setup_projectsimporttask_constructor_args():
    sig = inspect.signature(setup_ProjectsImportTask.__init__)
    params = list(sig.parameters.keys())



def test_setup_mylynquerytask_is_not_abstract():
    assert not inspect.isabstract(setup_MylynQueryTask)


def test_setup_mylynquerytask_constructor_exists():
    assert callable(setup_MylynQueryTask.__init__)


def test_setup_mylynquerytask_constructor_args():
    sig = inspect.signature(setup_MylynQueryTask.__init__)
    params = list(sig.parameters.keys())
    assert "summary" in params, "Missing parameter 'summary'"
    assert "repositoryURL" in params, "Missing parameter 'repositoryURL'"
    assert "connectorKind" in params, "Missing parameter 'connectorKind'"
    assert "relativeURL" in params, "Missing parameter 'relativeURL'"

def test_setup_mylynquerytask_has_summary():
    assert hasattr(setup_MylynQueryTask, "summary")
    descriptor = None
    for klass in setup_MylynQueryTask.__mro__:
        if "summary" in klass.__dict__:
            descriptor = klass.__dict__["summary"]
            break
    assert isinstance(descriptor, property)

def test_setup_mylynquerytask_has_repositoryURL():
    assert hasattr(setup_MylynQueryTask, "repositoryURL")
    descriptor = None
    for klass in setup_MylynQueryTask.__mro__:
        if "repositoryURL" in klass.__dict__:
            descriptor = klass.__dict__["repositoryURL"]
            break
    assert isinstance(descriptor, property)

def test_setup_mylynquerytask_has_connectorKind():
    assert hasattr(setup_MylynQueryTask, "connectorKind")
    descriptor = None
    for klass in setup_MylynQueryTask.__mro__:
        if "connectorKind" in klass.__dict__:
            descriptor = klass.__dict__["connectorKind"]
            break
    assert isinstance(descriptor, property)

def test_setup_mylynquerytask_has_relativeURL():
    assert hasattr(setup_MylynQueryTask, "relativeURL")
    descriptor = None
    for klass in setup_MylynQueryTask.__mro__:
        if "relativeURL" in klass.__dict__:
            descriptor = klass.__dict__["relativeURL"]
            break
    assert isinstance(descriptor, property)



def test_setup_fileassociationtask_is_not_abstract():
    assert not inspect.isabstract(setup_FileAssociationTask)


def test_setup_fileassociationtask_constructor_exists():
    assert callable(setup_FileAssociationTask.__init__)


def test_setup_fileassociationtask_constructor_args():
    sig = inspect.signature(setup_FileAssociationTask.__init__)
    params = list(sig.parameters.keys())
    assert "filePattern" in params, "Missing parameter 'filePattern'"
    assert "defaultEditorID" in params, "Missing parameter 'defaultEditorID'"

def test_setup_fileassociationtask_has_filePattern():
    assert hasattr(setup_FileAssociationTask, "filePattern")
    descriptor = None
    for klass in setup_FileAssociationTask.__mro__:
        if "filePattern" in klass.__dict__:
            descriptor = klass.__dict__["filePattern"]
            break
    assert isinstance(descriptor, property)

def test_setup_fileassociationtask_has_defaultEditorID():
    assert hasattr(setup_FileAssociationTask, "defaultEditorID")
    descriptor = None
    for klass in setup_FileAssociationTask.__mro__:
        if "defaultEditorID" in klass.__dict__:
            descriptor = klass.__dict__["defaultEditorID"]
            break
    assert isinstance(descriptor, property)



def test_setup_resourcecopytask_is_not_abstract():
    assert not inspect.isabstract(setup_ResourceCopyTask)


def test_setup_resourcecopytask_constructor_exists():
    assert callable(setup_ResourceCopyTask.__init__)


def test_setup_resourcecopytask_constructor_args():
    sig = inspect.signature(setup_ResourceCopyTask.__init__)
    params = list(sig.parameters.keys())
    assert "targetURL" in params, "Missing parameter 'targetURL'"
    assert "sourceURL" in params, "Missing parameter 'sourceURL'"

def test_setup_resourcecopytask_has_targetURL():
    assert hasattr(setup_ResourceCopyTask, "targetURL")
    descriptor = None
    for klass in setup_ResourceCopyTask.__mro__:
        if "targetURL" in klass.__dict__:
            descriptor = klass.__dict__["targetURL"]
            break
    assert isinstance(descriptor, property)

def test_setup_resourcecopytask_has_sourceURL():
    assert hasattr(setup_ResourceCopyTask, "sourceURL")
    descriptor = None
    for klass in setup_ResourceCopyTask.__mro__:
        if "sourceURL" in klass.__dict__:
            descriptor = klass.__dict__["sourceURL"]
            break
    assert isinstance(descriptor, property)



def test_setup_keybindingtask_is_not_abstract():
    assert not inspect.isabstract(setup_KeyBindingTask)


def test_setup_keybindingtask_constructor_exists():
    assert callable(setup_KeyBindingTask.__init__)


def test_setup_keybindingtask_constructor_args():
    sig = inspect.signature(setup_KeyBindingTask.__init__)
    params = list(sig.parameters.keys())
    assert "command" in params, "Missing parameter 'command'"
    assert "keys" in params, "Missing parameter 'keys'"
    assert "platform" in params, "Missing parameter 'platform'"
    assert "locale" in params, "Missing parameter 'locale'"
    assert "scheme" in params, "Missing parameter 'scheme'"

def test_setup_keybindingtask_has_command():
    assert hasattr(setup_KeyBindingTask, "command")
    descriptor = None
    for klass in setup_KeyBindingTask.__mro__:
        if "command" in klass.__dict__:
            descriptor = klass.__dict__["command"]
            break
    assert isinstance(descriptor, property)

def test_setup_keybindingtask_has_keys():
    assert hasattr(setup_KeyBindingTask, "keys")
    descriptor = None
    for klass in setup_KeyBindingTask.__mro__:
        if "keys" in klass.__dict__:
            descriptor = klass.__dict__["keys"]
            break
    assert isinstance(descriptor, property)

def test_setup_keybindingtask_has_platform():
    assert hasattr(setup_KeyBindingTask, "platform")
    descriptor = None
    for klass in setup_KeyBindingTask.__mro__:
        if "platform" in klass.__dict__:
            descriptor = klass.__dict__["platform"]
            break
    assert isinstance(descriptor, property)

def test_setup_keybindingtask_has_locale():
    assert hasattr(setup_KeyBindingTask, "locale")
    descriptor = None
    for klass in setup_KeyBindingTask.__mro__:
        if "locale" in klass.__dict__:
            descriptor = klass.__dict__["locale"]
            break
    assert isinstance(descriptor, property)

def test_setup_keybindingtask_has_scheme():
    assert hasattr(setup_KeyBindingTask, "scheme")
    descriptor = None
    for klass in setup_KeyBindingTask.__mro__:
        if "scheme" in klass.__dict__:
            descriptor = klass.__dict__["scheme"]
            break
    assert isinstance(descriptor, property)



def test_setup_mylynbuildstask_is_not_abstract():
    assert not inspect.isabstract(setup_MylynBuildsTask)


def test_setup_mylynbuildstask_constructor_exists():
    assert callable(setup_MylynBuildsTask.__init__)


def test_setup_mylynbuildstask_constructor_args():
    sig = inspect.signature(setup_MylynBuildsTask.__init__)
    params = list(sig.parameters.keys())
    assert "serverURL" in params, "Missing parameter 'serverURL'"
    assert "password" in params, "Missing parameter 'password'"
    assert "connectorKind" in params, "Missing parameter 'connectorKind'"
    assert "userID" in params, "Missing parameter 'userID'"

def test_setup_mylynbuildstask_has_serverURL():
    assert hasattr(setup_MylynBuildsTask, "serverURL")
    descriptor = None
    for klass in setup_MylynBuildsTask.__mro__:
        if "serverURL" in klass.__dict__:
            descriptor = klass.__dict__["serverURL"]
            break
    assert isinstance(descriptor, property)

def test_setup_mylynbuildstask_has_password():
    assert hasattr(setup_MylynBuildsTask, "password")
    descriptor = None
    for klass in setup_MylynBuildsTask.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_setup_mylynbuildstask_has_connectorKind():
    assert hasattr(setup_MylynBuildsTask, "connectorKind")
    descriptor = None
    for klass in setup_MylynBuildsTask.__mro__:
        if "connectorKind" in klass.__dict__:
            descriptor = klass.__dict__["connectorKind"]
            break
    assert isinstance(descriptor, property)

def test_setup_mylynbuildstask_has_userID():
    assert hasattr(setup_MylynBuildsTask, "userID")
    descriptor = None
    for klass in setup_MylynBuildsTask.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)



def test_setup_resourcecreationtask_is_not_abstract():
    assert not inspect.isabstract(setup_ResourceCreationTask)


def test_setup_resourcecreationtask_constructor_exists():
    assert callable(setup_ResourceCreationTask.__init__)


def test_setup_resourcecreationtask_constructor_args():
    sig = inspect.signature(setup_ResourceCreationTask.__init__)
    params = list(sig.parameters.keys())
    assert "encoding" in params, "Missing parameter 'encoding'"
    assert "content" in params, "Missing parameter 'content'"
    assert "targetURL" in params, "Missing parameter 'targetURL'"

def test_setup_resourcecreationtask_has_encoding():
    assert hasattr(setup_ResourceCreationTask, "encoding")
    descriptor = None
    for klass in setup_ResourceCreationTask.__mro__:
        if "encoding" in klass.__dict__:
            descriptor = klass.__dict__["encoding"]
            break
    assert isinstance(descriptor, property)

def test_setup_resourcecreationtask_has_content():
    assert hasattr(setup_ResourceCreationTask, "content")
    descriptor = None
    for klass in setup_ResourceCreationTask.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_setup_resourcecreationtask_has_targetURL():
    assert hasattr(setup_ResourceCreationTask, "targetURL")
    descriptor = None
    for klass in setup_ResourceCreationTask.__mro__:
        if "targetURL" in klass.__dict__:
            descriptor = klass.__dict__["targetURL"]
            break
    assert isinstance(descriptor, property)



def test_setup_gitclonetask_is_not_abstract():
    assert not inspect.isabstract(setup_GitCloneTask)


def test_setup_gitclonetask_constructor_exists():
    assert callable(setup_GitCloneTask.__init__)


def test_setup_gitclonetask_constructor_args():
    sig = inspect.signature(setup_GitCloneTask.__init__)
    params = list(sig.parameters.keys())
    assert "pushURI" in params, "Missing parameter 'pushURI'"
    assert "location" in params, "Missing parameter 'location'"
    assert "userID" in params, "Missing parameter 'userID'"
    assert "remoteName" in params, "Missing parameter 'remoteName'"
    assert "checkoutBranch" in params, "Missing parameter 'checkoutBranch'"
    assert "remoteURI" in params, "Missing parameter 'remoteURI'"

def test_setup_gitclonetask_has_pushURI():
    assert hasattr(setup_GitCloneTask, "pushURI")
    descriptor = None
    for klass in setup_GitCloneTask.__mro__:
        if "pushURI" in klass.__dict__:
            descriptor = klass.__dict__["pushURI"]
            break
    assert isinstance(descriptor, property)

def test_setup_gitclonetask_has_location():
    assert hasattr(setup_GitCloneTask, "location")
    descriptor = None
    for klass in setup_GitCloneTask.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_setup_gitclonetask_has_userID():
    assert hasattr(setup_GitCloneTask, "userID")
    descriptor = None
    for klass in setup_GitCloneTask.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)

def test_setup_gitclonetask_has_remoteName():
    assert hasattr(setup_GitCloneTask, "remoteName")
    descriptor = None
    for klass in setup_GitCloneTask.__mro__:
        if "remoteName" in klass.__dict__:
            descriptor = klass.__dict__["remoteName"]
            break
    assert isinstance(descriptor, property)

def test_setup_gitclonetask_has_checkoutBranch():
    assert hasattr(setup_GitCloneTask, "checkoutBranch")
    descriptor = None
    for klass in setup_GitCloneTask.__mro__:
        if "checkoutBranch" in klass.__dict__:
            descriptor = klass.__dict__["checkoutBranch"]
            break
    assert isinstance(descriptor, property)

def test_setup_gitclonetask_has_remoteURI():
    assert hasattr(setup_GitCloneTask, "remoteURI")
    descriptor = None
    for klass in setup_GitCloneTask.__mro__:
        if "remoteURI" in klass.__dict__:
            descriptor = klass.__dict__["remoteURI"]
            break
    assert isinstance(descriptor, property)



def test_setup_basicmaterializationtask_is_not_abstract():
    assert not inspect.isabstract(setup_BasicMaterializationTask)


def test_setup_basicmaterializationtask_constructor_exists():
    assert callable(setup_BasicMaterializationTask.__init__)


def test_setup_basicmaterializationtask_constructor_args():
    sig = inspect.signature(setup_BasicMaterializationTask.__init__)
    params = list(sig.parameters.keys())
    assert "bundlePool" in params, "Missing parameter 'bundlePool'"
    assert "targetPlatform" in params, "Missing parameter 'targetPlatform'"

def test_setup_basicmaterializationtask_has_bundlePool():
    assert hasattr(setup_BasicMaterializationTask, "bundlePool")
    descriptor = None
    for klass in setup_BasicMaterializationTask.__mro__:
        if "bundlePool" in klass.__dict__:
            descriptor = klass.__dict__["bundlePool"]
            break
    assert isinstance(descriptor, property)

def test_setup_basicmaterializationtask_has_targetPlatform():
    assert hasattr(setup_BasicMaterializationTask, "targetPlatform")
    descriptor = None
    for klass in setup_BasicMaterializationTask.__mro__:
        if "targetPlatform" in klass.__dict__:
            descriptor = klass.__dict__["targetPlatform"]
            break
    assert isinstance(descriptor, property)



def test_setup_fileassociationstask_is_not_abstract():
    assert not inspect.isabstract(setup_FileAssociationsTask)


def test_setup_fileassociationstask_constructor_exists():
    assert callable(setup_FileAssociationsTask.__init__)


def test_setup_fileassociationstask_constructor_args():
    sig = inspect.signature(setup_FileAssociationsTask.__init__)
    params = list(sig.parameters.keys())



def test_setup_workingsettask_is_not_abstract():
    assert not inspect.isabstract(setup_WorkingSetTask)


def test_setup_workingsettask_constructor_exists():
    assert callable(setup_WorkingSetTask.__init__)


def test_setup_workingsettask_constructor_args():
    sig = inspect.signature(setup_WorkingSetTask.__init__)
    params = list(sig.parameters.keys())



def test_setup_apibaselinetask_is_not_abstract():
    assert not inspect.isabstract(setup_ApiBaselineTask)


def test_setup_apibaselinetask_constructor_exists():
    assert callable(setup_ApiBaselineTask.__init__)


def test_setup_apibaselinetask_constructor_args():
    sig = inspect.signature(setup_ApiBaselineTask.__init__)
    params = list(sig.parameters.keys())
    assert "containerFolder" in params, "Missing parameter 'containerFolder'"
    assert "zipLocation" in params, "Missing parameter 'zipLocation'"
    assert "version" in params, "Missing parameter 'version'"

def test_setup_apibaselinetask_has_containerFolder():
    assert hasattr(setup_ApiBaselineTask, "containerFolder")
    descriptor = None
    for klass in setup_ApiBaselineTask.__mro__:
        if "containerFolder" in klass.__dict__:
            descriptor = klass.__dict__["containerFolder"]
            break
    assert isinstance(descriptor, property)

def test_setup_apibaselinetask_has_zipLocation():
    assert hasattr(setup_ApiBaselineTask, "zipLocation")
    descriptor = None
    for klass in setup_ApiBaselineTask.__mro__:
        if "zipLocation" in klass.__dict__:
            descriptor = klass.__dict__["zipLocation"]
            break
    assert isinstance(descriptor, property)

def test_setup_apibaselinetask_has_version():
    assert hasattr(setup_ApiBaselineTask, "version")
    descriptor = None
    for klass in setup_ApiBaselineTask.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_setup_targetplatformtask_is_not_abstract():
    assert not inspect.isabstract(setup_TargetPlatformTask)


def test_setup_targetplatformtask_constructor_exists():
    assert callable(setup_TargetPlatformTask.__init__)


def test_setup_targetplatformtask_constructor_args():
    sig = inspect.signature(setup_TargetPlatformTask.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_setup_targetplatformtask_has_name():
    assert hasattr(setup_TargetPlatformTask, "name")
    descriptor = None
    for klass in setup_TargetPlatformTask.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_setup_mylynqueriestask_is_not_abstract():
    assert not inspect.isabstract(setup_MylynQueriesTask)


def test_setup_mylynqueriestask_constructor_exists():
    assert callable(setup_MylynQueriesTask.__init__)


def test_setup_mylynqueriestask_constructor_args():
    sig = inspect.signature(setup_MylynQueriesTask.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "repositoryURL" in params, "Missing parameter 'repositoryURL'"
    assert "connectorKind" in params, "Missing parameter 'connectorKind'"
    assert "userID" in params, "Missing parameter 'userID'"

def test_setup_mylynqueriestask_has_password():
    assert hasattr(setup_MylynQueriesTask, "password")
    descriptor = None
    for klass in setup_MylynQueriesTask.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_setup_mylynqueriestask_has_repositoryURL():
    assert hasattr(setup_MylynQueriesTask, "repositoryURL")
    descriptor = None
    for klass in setup_MylynQueriesTask.__mro__:
        if "repositoryURL" in klass.__dict__:
            descriptor = klass.__dict__["repositoryURL"]
            break
    assert isinstance(descriptor, property)

def test_setup_mylynqueriestask_has_connectorKind():
    assert hasattr(setup_MylynQueriesTask, "connectorKind")
    descriptor = None
    for klass in setup_MylynQueriesTask.__mro__:
        if "connectorKind" in klass.__dict__:
            descriptor = klass.__dict__["connectorKind"]
            break
    assert isinstance(descriptor, property)

def test_setup_mylynqueriestask_has_userID():
    assert hasattr(setup_MylynQueriesTask, "userID")
    descriptor = None
    for klass in setup_MylynQueriesTask.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
            break
    assert isinstance(descriptor, property)



def test_setup_targlettask_is_not_abstract():
    assert not inspect.isabstract(setup_TargletTask)


def test_setup_targlettask_constructor_exists():
    assert callable(setup_TargletTask.__init__)


def test_setup_targlettask_constructor_args():
    sig = inspect.signature(setup_TargletTask.__init__)
    params = list(sig.parameters.keys())



def test_setup_mavenimporttask_is_not_abstract():
    assert not inspect.isabstract(setup_MavenImportTask)


def test_setup_mavenimporttask_constructor_exists():
    assert callable(setup_MavenImportTask.__init__)


def test_setup_mavenimporttask_constructor_args():
    sig = inspect.signature(setup_MavenImportTask.__init__)
    params = list(sig.parameters.keys())



def test_setup_p2task_is_not_abstract():
    assert not inspect.isabstract(setup_P2Task)


def test_setup_p2task_constructor_exists():
    assert callable(setup_P2Task.__init__)


def test_setup_p2task_constructor_args():
    sig = inspect.signature(setup_P2Task.__init__)
    params = list(sig.parameters.keys())
    assert "licenseConfirmationDisabled" in params, "Missing parameter 'licenseConfirmationDisabled'"
    assert "mergeDisabled" in params, "Missing parameter 'mergeDisabled'"

def test_setup_p2task_has_licenseConfirmationDisabled():
    assert hasattr(setup_P2Task, "licenseConfirmationDisabled")
    descriptor = None
    for klass in setup_P2Task.__mro__:
        if "licenseConfirmationDisabled" in klass.__dict__:
            descriptor = klass.__dict__["licenseConfirmationDisabled"]
            break
    assert isinstance(descriptor, property)

def test_setup_p2task_has_mergeDisabled():
    assert hasattr(setup_P2Task, "mergeDisabled")
    descriptor = None
    for klass in setup_P2Task.__mro__:
        if "mergeDisabled" in klass.__dict__:
            descriptor = klass.__dict__["mergeDisabled"]
            break
    assert isinstance(descriptor, property)



def test_setuptaskcontainer_is_not_abstract():
    assert not inspect.isabstract(SetupTaskContainer)


def test_setuptaskcontainer_constructor_exists():
    assert callable(SetupTaskContainer.__init__)


def test_setuptaskcontainer_constructor_args():
    sig = inspect.signature(SetupTaskContainer.__init__)
    params = list(sig.parameters.keys())



def test_setup_compoundsetuptask_is_not_abstract():
    assert not inspect.isabstract(setup_CompoundSetupTask)


def test_setup_compoundsetuptask_constructor_exists():
    assert callable(setup_CompoundSetupTask.__init__)


def test_setup_compoundsetuptask_constructor_args():
    sig = inspect.signature(setup_CompoundSetupTask.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_setup_compoundsetuptask_has_name():
    assert hasattr(setup_CompoundSetupTask, "name")
    descriptor = None
    for klass in setup_CompoundSetupTask.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_setup_scoperoot_is_not_abstract():
    assert not inspect.isabstract(setup_ScopeRoot)


def test_setup_scoperoot_constructor_exists():
    assert callable(setup_ScopeRoot.__init__)


def test_setup_scoperoot_constructor_args():
    sig = inspect.signature(setup_ScopeRoot.__init__)
    params = list(sig.parameters.keys())



def test_setup_setuptaskcontainer_is_not_abstract():
    assert not inspect.isabstract(setup_SetupTaskContainer)


def test_setup_setuptaskcontainer_constructor_exists():
    assert callable(setup_SetupTaskContainer.__init__)


def test_setup_setuptaskcontainer_constructor_args():
    sig = inspect.signature(setup_SetupTaskContainer.__init__)
    params = list(sig.parameters.keys())



def test_setup_linklocationtask_is_not_abstract():
    assert not inspect.isabstract(setup_LinkLocationTask)


def test_setup_linklocationtask_constructor_exists():
    assert callable(setup_LinkLocationTask.__init__)


def test_setup_linklocationtask_constructor_args():
    sig = inspect.signature(setup_LinkLocationTask.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"
    assert "name" in params, "Missing parameter 'name'"

def test_setup_linklocationtask_has_path():
    assert hasattr(setup_LinkLocationTask, "path")
    descriptor = None
    for klass in setup_LinkLocationTask.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_setup_linklocationtask_has_name():
    assert hasattr(setup_LinkLocationTask, "name")
    descriptor = None
    for klass in setup_LinkLocationTask.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_setup_eclipseinitask_is_not_abstract():
    assert not inspect.isabstract(setup_EclipseIniTask)


def test_setup_eclipseinitask_constructor_exists():
    assert callable(setup_EclipseIniTask.__init__)


def test_setup_eclipseinitask_constructor_args():
    sig = inspect.signature(setup_EclipseIniTask.__init__)
    params = list(sig.parameters.keys())
    assert "option" in params, "Missing parameter 'option'"
    assert "vm" in params, "Missing parameter 'vm'"
    assert "value" in params, "Missing parameter 'value'"

def test_setup_eclipseinitask_has_option():
    assert hasattr(setup_EclipseIniTask, "option")
    descriptor = None
    for klass in setup_EclipseIniTask.__mro__:
        if "option" in klass.__dict__:
            descriptor = klass.__dict__["option"]
            break
    assert isinstance(descriptor, property)

def test_setup_eclipseinitask_has_vm():
    assert hasattr(setup_EclipseIniTask, "vm")
    descriptor = None
    for klass in setup_EclipseIniTask.__mro__:
        if "vm" in klass.__dict__:
            descriptor = klass.__dict__["vm"]
            break
    assert isinstance(descriptor, property)

def test_setup_eclipseinitask_has_value():
    assert hasattr(setup_EclipseIniTask, "value")
    descriptor = None
    for klass in setup_EclipseIniTask.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_setup_redirectiontask_is_not_abstract():
    assert not inspect.isabstract(setup_RedirectionTask)


def test_setup_redirectiontask_constructor_exists():
    assert callable(setup_RedirectionTask.__init__)


def test_setup_redirectiontask_constructor_args():
    sig = inspect.signature(setup_RedirectionTask.__init__)
    params = list(sig.parameters.keys())
    assert "targetURL" in params, "Missing parameter 'targetURL'"
    assert "sourceURL" in params, "Missing parameter 'sourceURL'"

def test_setup_redirectiontask_has_targetURL():
    assert hasattr(setup_RedirectionTask, "targetURL")
    descriptor = None
    for klass in setup_RedirectionTask.__mro__:
        if "targetURL" in klass.__dict__:
            descriptor = klass.__dict__["targetURL"]
            break
    assert isinstance(descriptor, property)

def test_setup_redirectiontask_has_sourceURL():
    assert hasattr(setup_RedirectionTask, "sourceURL")
    descriptor = None
    for klass in setup_RedirectionTask.__mro__:
        if "sourceURL" in klass.__dict__:
            descriptor = klass.__dict__["sourceURL"]
            break
    assert isinstance(descriptor, property)



def test_setup_variablechoice_is_not_abstract():
    assert not inspect.isabstract(setup_VariableChoice)


def test_setup_variablechoice_constructor_exists():
    assert callable(setup_VariableChoice.__init__)


def test_setup_variablechoice_constructor_args():
    sig = inspect.signature(setup_VariableChoice.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "value" in params, "Missing parameter 'value'"

def test_setup_variablechoice_has_label():
    assert hasattr(setup_VariableChoice, "label")
    descriptor = None
    for klass in setup_VariableChoice.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_setup_variablechoice_has_value():
    assert hasattr(setup_VariableChoice, "value")
    descriptor = None
    for klass in setup_VariableChoice.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_setup_contextvariabletask_is_not_abstract():
    assert not inspect.isabstract(setup_ContextVariableTask)


def test_setup_contextvariabletask_constructor_exists():
    assert callable(setup_ContextVariableTask.__init__)


def test_setup_contextvariabletask_constructor_args():
    sig = inspect.signature(setup_ContextVariableTask.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "stringSubstitution" in params, "Missing parameter 'stringSubstitution'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_setup_contextvariabletask_has_label():
    assert hasattr(setup_ContextVariableTask, "label")
    descriptor = None
    for klass in setup_ContextVariableTask.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_setup_contextvariabletask_has_stringSubstitution():
    assert hasattr(setup_ContextVariableTask, "stringSubstitution")
    descriptor = None
    for klass in setup_ContextVariableTask.__mro__:
        if "stringSubstitution" in klass.__dict__:
            descriptor = klass.__dict__["stringSubstitution"]
            break
    assert isinstance(descriptor, property)

def test_setup_contextvariabletask_has_type():
    assert hasattr(setup_ContextVariableTask, "type")
    descriptor = None
    for klass in setup_ContextVariableTask.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_setup_contextvariabletask_has_name():
    assert hasattr(setup_ContextVariableTask, "name")
    descriptor = None
    for klass in setup_ContextVariableTask.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_setup_contextvariabletask_has_value():
    assert hasattr(setup_ContextVariableTask, "value")
    descriptor = None
    for klass in setup_ContextVariableTask.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_setup_setuptask_is_not_abstract():
    assert not inspect.isabstract(setup_SetupTask)


def test_setup_setuptask_constructor_exists():
    assert callable(setup_SetupTask.__init__)


def test_setup_setuptask_constructor_args():
    sig = inspect.signature(setup_SetupTask.__init__)
    params = list(sig.parameters.keys())
    assert "excludedTriggers" in params, "Missing parameter 'excludedTriggers'"
    assert "disabled" in params, "Missing parameter 'disabled'"
    assert "documentation" in params, "Missing parameter 'documentation'"
    assert "scope" in params, "Missing parameter 'scope'"

def test_setup_setuptask_has_excludedTriggers():
    assert hasattr(setup_SetupTask, "excludedTriggers")
    descriptor = None
    for klass in setup_SetupTask.__mro__:
        if "excludedTriggers" in klass.__dict__:
            descriptor = klass.__dict__["excludedTriggers"]
            break
    assert isinstance(descriptor, property)

def test_setup_setuptask_has_disabled():
    assert hasattr(setup_SetupTask, "disabled")
    descriptor = None
    for klass in setup_SetupTask.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)

def test_setup_setuptask_has_documentation():
    assert hasattr(setup_SetupTask, "documentation")
    descriptor = None
    for klass in setup_SetupTask.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)

def test_setup_setuptask_has_scope():
    assert hasattr(setup_SetupTask, "scope")
    descriptor = None
    for klass in setup_SetupTask.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_setup_setup_is_not_abstract():
    assert not inspect.isabstract(setup_Setup)


def test_setup_setup_constructor_exists():
    assert callable(setup_Setup.__init__)


def test_setup_setup_constructor_args():
    sig = inspect.signature(setup_Setup.__init__)
    params = list(sig.parameters.keys())



def test_configurableitem_is_not_abstract():
    assert not inspect.isabstract(ConfigurableItem)


def test_configurableitem_constructor_exists():
    assert callable(ConfigurableItem.__init__)


def test_configurableitem_constructor_args():
    sig = inspect.signature(ConfigurableItem.__init__)
    params = list(sig.parameters.keys())



def test_setup_eclipse_is_not_abstract():
    assert not inspect.isabstract(setup_Eclipse)


def test_setup_eclipse_constructor_exists():
    assert callable(setup_Eclipse.__init__)


def test_setup_eclipse_constructor_args():
    sig = inspect.signature(setup_Eclipse.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"

def test_setup_eclipse_has_version():
    assert hasattr(setup_Eclipse, "version")
    descriptor = None
    for klass in setup_Eclipse.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_setup_branch_is_not_abstract():
    assert not inspect.isabstract(setup_Branch)


def test_setup_branch_constructor_exists():
    assert callable(setup_Branch.__init__)


def test_setup_branch_constructor_args():
    sig = inspect.signature(setup_Branch.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_setup_branch_has_name():
    assert hasattr(setup_Branch, "name")
    descriptor = None
    for klass in setup_Branch.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_setup_project_is_not_abstract():
    assert not inspect.isabstract(setup_Project)


def test_setup_project_constructor_exists():
    assert callable(setup_Project.__init__)


def test_setup_project_constructor_args():
    sig = inspect.signature(setup_Project.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"

def test_setup_project_has_label():
    assert hasattr(setup_Project, "label")
    descriptor = None
    for klass in setup_Project.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_setup_project_has_name():
    assert hasattr(setup_Project, "name")
    descriptor = None
    for klass in setup_Project.__mro__:
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



def test_setup_configurableitem_is_not_abstract():
    assert not inspect.isabstract(setup_ConfigurableItem)


def test_setup_configurableitem_constructor_exists():
    assert callable(setup_ConfigurableItem.__init__)


def test_setup_configurableitem_constructor_args():
    sig = inspect.signature(setup_ConfigurableItem.__init__)
    params = list(sig.parameters.keys())



def test_setup_preferences_is_not_abstract():
    assert not inspect.isabstract(setup_Preferences)


def test_setup_preferences_constructor_exists():
    assert callable(setup_Preferences.__init__)


def test_setup_preferences_constructor_args():
    sig = inspect.signature(setup_Preferences.__init__)
    params = list(sig.parameters.keys())
    assert "acceptedLicenses" in params, "Missing parameter 'acceptedLicenses'"
    assert "installFolder" in params, "Missing parameter 'installFolder'"

def test_setup_preferences_has_acceptedLicenses():
    assert hasattr(setup_Preferences, "acceptedLicenses")
    descriptor = None
    for klass in setup_Preferences.__mro__:
        if "acceptedLicenses" in klass.__dict__:
            descriptor = klass.__dict__["acceptedLicenses"]
            break
    assert isinstance(descriptor, property)

def test_setup_preferences_has_installFolder():
    assert hasattr(setup_Preferences, "installFolder")
    descriptor = None
    for klass in setup_Preferences.__mro__:
        if "installFolder" in klass.__dict__:
            descriptor = klass.__dict__["installFolder"]
            break
    assert isinstance(descriptor, property)



def test_setup_configuration_is_not_abstract():
    assert not inspect.isabstract(setup_Configuration)


def test_setup_configuration_constructor_exists():
    assert callable(setup_Configuration.__init__)


def test_setup_configuration_constructor_args():
    sig = inspect.signature(setup_Configuration.__init__)
    params = list(sig.parameters.keys())



def test_setup_index_is_not_abstract():
    assert not inspect.isabstract(setup_Index)


def test_setup_index_constructor_exists():
    assert callable(setup_Index.__init__)


def test_setup_index_constructor_args():
    sig = inspect.signature(setup_Index.__init__)
    params = list(sig.parameters.keys())
    assert "uRI" in params, "Missing parameter 'uRI'"
    assert "name" in params, "Missing parameter 'name'"
    assert "oldURIs" in params, "Missing parameter 'oldURIs'"

def test_setup_index_has_uRI():
    assert hasattr(setup_Index, "uRI")
    descriptor = None
    for klass in setup_Index.__mro__:
        if "uRI" in klass.__dict__:
            descriptor = klass.__dict__["uRI"]
            break
    assert isinstance(descriptor, property)

def test_setup_index_has_name():
    assert hasattr(setup_Index, "name")
    descriptor = None
    for klass in setup_Index.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_setup_index_has_oldURIs():
    assert hasattr(setup_Index, "oldURIs")
    descriptor = None
    for klass in setup_Index.__mro__:
        if "oldURIs" in klass.__dict__:
            descriptor = klass.__dict__["oldURIs"]
            break
    assert isinstance(descriptor, property)



def test_setup_metaindex_is_not_abstract():
    assert not inspect.isabstract(setup_MetaIndex)


def test_setup_metaindex_constructor_exists():
    assert callable(setup_MetaIndex.__init__)


def test_setup_metaindex_constructor_args():
    sig = inspect.signature(setup_MetaIndex.__init__)
    params = list(sig.parameters.keys())

def test_variabletype_exists():
    # Check that the Enumeration exists
    assert VariableType is not None

def test_variabletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariableType]
    expected_literals = [
        "FLOAT",
        "URI",
        "FILE",
        "TEXT",
        "PATTERN",
        "FOLDER",
        "BOOLEAN",
        "INTEGER",
        "PROJECT",
        "RESOURCE",
        "CONTAINER",
        "PASSWORD",
        "STRING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VariableType"

def test_trigger_exists():
    # Check that the Enumeration exists
    assert Trigger is not None

def test_trigger_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Trigger]
    expected_literals = [
        "BOOTSTRAP",
        "STARTUP",
        "MANUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Trigger"

def test_setuptaskscope_exists():
    # Check that the Enumeration exists
    assert SetupTaskScope is not None

def test_setuptaskscope_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SetupTaskScope]
    expected_literals = [
        "Configuration",
        "Branch",
        "None_",
        "Project",
        "User",
        "Eclipse",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SetupTaskScope"

def test_componenttype_exists():
    # Check that the Enumeration exists
    assert ComponentType is not None

def test_componenttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComponentType]
    expected_literals = [
        "BUCKMINSTER",
        "OSGI_BUNDLE",
        "JAR",
        "UNKNOWN",
        "ECLIPSE_FEATURE",
        "BOM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComponentType"


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
setup_Query_strategy = st.builds(
    setup_Query,
    uRL=
        safe_text,
    summary=
        safe_text
)
setup_BuildPlan_strategy = st.builds(
    setup_BuildPlan,
    name=
        safe_text
)
setup_QueryAttribute_strategy = st.builds(
    setup_QueryAttribute,
    value=
        safe_text,
    key=
        safe_text
)
setup_TextModification_strategy = st.builds(
    setup_TextModification,
    pattern=
        safe_text,
    substitutions=
        safe_text
)
setup_CommandParameter_strategy = st.builds(
    setup_CommandParameter,
    iD=
        safe_text,
    value=
        safe_text
)
setup_KeyBindingContext_strategy = st.builds(
    setup_KeyBindingContext,
    iD=
        safe_text
)
setup_FileEditor_strategy = st.builds(
    setup_FileEditor,
    iD=
        safe_text
)
setup_WorkingSet_strategy = st.builds(
    setup_WorkingSet,
)
setup_FileMapping_strategy = st.builds(
    setup_FileMapping,
    filePattern=
        safe_text,
    defaultEditorID=
        safe_text
)
setup_TargletData_strategy = st.builds(
    setup_TargletData,
    includeAllPlatforms=
        st.booleans(),
    activeRepositoryList=
        safe_text,
    includeSources=
        st.booleans(),
    name=
        safe_text
)
TargletData_strategy = st.builds(
    TargletData,
)
setup_Targlet_strategy = st.builds(
    setup_Targlet,
)
setup_RepositoryList_strategy = st.builds(
    setup_RepositoryList,
    name=
        safe_text
)
ComponentExtension_strategy = st.builds(
    ComponentExtension,
)
setup_ComponentDefinition_strategy = st.builds(
    setup_ComponentDefinition,
    version=
        safe_text,
    iD=
        safe_text
)
setup_Component_strategy = st.builds(
    setup_Component,
    versionRange=
        safe_text,
    type=
        safe_text,
    name=
        safe_text
)
setup_ComponentExtension_strategy = st.builds(
    setup_ComponentExtension,
)
setup_Predicate_strategy = st.builds(
    setup_Predicate,
)
SourceLocator_strategy = st.builds(
    SourceLocator,
)
setup_AutomaticSourceLocator_strategy = st.builds(
    setup_AutomaticSourceLocator,
    locateNestedProjects=
        st.booleans(),
    rootFolder=
        safe_text
)
setup_ManualSourceLocator_strategy = st.builds(
    setup_ManualSourceLocator,
    componentTypes=
        safe_text,
    location=
        safe_text,
    componentNamePattern=
        safe_text
)
setup_SourceLocator_strategy = st.builds(
    setup_SourceLocator,
)
setup_P2Repository_strategy = st.builds(
    setup_P2Repository,
    uRL=
        safe_text
)
setup_InstallableUnit_strategy = st.builds(
    setup_InstallableUnit,
    versionRange=
        safe_text,
    iD=
        safe_text
)
BasicMaterializationTask_strategy = st.builds(
    BasicMaterializationTask,
)
setup_MaterializationTask_strategy = st.builds(
    setup_MaterializationTask,
)
setup_BuckminsterImportTask_strategy = st.builds(
    setup_BuckminsterImportTask,
    mspec=
        safe_text
)
SetupTask_strategy = st.builds(
    SetupTask,
)
setup_ProjectSetImportTask_strategy = st.builds(
    setup_ProjectSetImportTask,
    uRL=
        safe_text
)
setup_EclipsePreferenceTask_strategy = st.builds(
    setup_EclipsePreferenceTask,
    key=
        safe_text,
    value=
        safe_text
)
setup_TargletImportTask_strategy = st.builds(
    setup_TargletImportTask,
    targletURI=
        safe_text
)
setup_JRETask_strategy = st.builds(
    setup_JRETask,
    location=
        safe_text,
    version=
        safe_text
)
setup_TextModifyTask_strategy = st.builds(
    setup_TextModifyTask,
    uRL=
        safe_text,
    encoding=
        safe_text
)
setup_ProjectsImportTask_strategy = st.builds(
    setup_ProjectsImportTask,
)
setup_MylynQueryTask_strategy = st.builds(
    setup_MylynQueryTask,
    summary=
        safe_text,
    repositoryURL=
        safe_text,
    connectorKind=
        safe_text,
    relativeURL=
        safe_text
)
setup_FileAssociationTask_strategy = st.builds(
    setup_FileAssociationTask,
    filePattern=
        safe_text,
    defaultEditorID=
        safe_text
)
setup_ResourceCopyTask_strategy = st.builds(
    setup_ResourceCopyTask,
    targetURL=
        safe_text,
    sourceURL=
        safe_text
)
setup_KeyBindingTask_strategy = st.builds(
    setup_KeyBindingTask,
    command=
        safe_text,
    keys=
        safe_text,
    platform=
        safe_text,
    locale=
        safe_text,
    scheme=
        safe_text
)
setup_MylynBuildsTask_strategy = st.builds(
    setup_MylynBuildsTask,
    serverURL=
        safe_text,
    password=
        safe_text,
    connectorKind=
        safe_text,
    userID=
        safe_text
)
setup_ResourceCreationTask_strategy = st.builds(
    setup_ResourceCreationTask,
    encoding=
        safe_text,
    content=
        safe_text,
    targetURL=
        safe_text
)
setup_GitCloneTask_strategy = st.builds(
    setup_GitCloneTask,
    pushURI=
        safe_text,
    location=
        safe_text,
    userID=
        safe_text,
    remoteName=
        safe_text,
    checkoutBranch=
        safe_text,
    remoteURI=
        safe_text
)
setup_BasicMaterializationTask_strategy = st.builds(
    setup_BasicMaterializationTask,
    bundlePool=
        safe_text,
    targetPlatform=
        safe_text
)
setup_FileAssociationsTask_strategy = st.builds(
    setup_FileAssociationsTask,
)
setup_WorkingSetTask_strategy = st.builds(
    setup_WorkingSetTask,
)
setup_ApiBaselineTask_strategy = st.builds(
    setup_ApiBaselineTask,
    containerFolder=
        safe_text,
    zipLocation=
        safe_text,
    version=
        safe_text
)
setup_TargetPlatformTask_strategy = st.builds(
    setup_TargetPlatformTask,
    name=
        safe_text
)
setup_MylynQueriesTask_strategy = st.builds(
    setup_MylynQueriesTask,
    password=
        safe_text,
    repositoryURL=
        safe_text,
    connectorKind=
        safe_text,
    userID=
        safe_text
)
setup_TargletTask_strategy = st.builds(
    setup_TargletTask,
)
setup_MavenImportTask_strategy = st.builds(
    setup_MavenImportTask,
)
setup_P2Task_strategy = st.builds(
    setup_P2Task,
    licenseConfirmationDisabled=
        st.booleans(),
    mergeDisabled=
        st.booleans()
)
SetupTaskContainer_strategy = st.builds(
    SetupTaskContainer,
)
setup_CompoundSetupTask_strategy = st.builds(
    setup_CompoundSetupTask,
    name=
        safe_text
)
setup_ScopeRoot_strategy = st.builds(
    setup_ScopeRoot,
)
setup_SetupTaskContainer_strategy = st.builds(
    setup_SetupTaskContainer,
)
setup_LinkLocationTask_strategy = st.builds(
    setup_LinkLocationTask,
    path=
        safe_text,
    name=
        safe_text
)
setup_EclipseIniTask_strategy = st.builds(
    setup_EclipseIniTask,
    option=
        safe_text,
    vm=
        st.booleans(),
    value=
        safe_text
)
setup_RedirectionTask_strategy = st.builds(
    setup_RedirectionTask,
    targetURL=
        safe_text,
    sourceURL=
        safe_text
)
setup_VariableChoice_strategy = st.builds(
    setup_VariableChoice,
    label=
        safe_text,
    value=
        safe_text
)
setup_ContextVariableTask_strategy = st.builds(
    setup_ContextVariableTask,
    label=
        safe_text,
    stringSubstitution=
        st.booleans(),
    type=
        safe_text,
    name=
        safe_text,
    value=
        safe_text
)
setup_SetupTask_strategy = st.builds(
    setup_SetupTask,
    excludedTriggers=
        safe_text,
    disabled=
        st.booleans(),
    documentation=
        safe_text,
    scope=
        safe_text
)
setup_Setup_strategy = st.builds(
    setup_Setup,
)
ConfigurableItem_strategy = st.builds(
    ConfigurableItem,
)
setup_Eclipse_strategy = st.builds(
    setup_Eclipse,
    version=
        safe_text
)
setup_Branch_strategy = st.builds(
    setup_Branch,
    name=
        safe_text
)
setup_Project_strategy = st.builds(
    setup_Project,
    label=
        safe_text,
    name=
        safe_text
)
ScopeRoot_strategy = st.builds(
    ScopeRoot,
)
setup_ConfigurableItem_strategy = st.builds(
    setup_ConfigurableItem,
)
setup_Preferences_strategy = st.builds(
    setup_Preferences,
    acceptedLicenses=
        safe_text,
    installFolder=
        safe_text
)
setup_Configuration_strategy = st.builds(
    setup_Configuration,
)
setup_Index_strategy = st.builds(
    setup_Index,
    uRI=
        safe_text,
    name=
        safe_text,
    oldURIs=
        safe_text
)
setup_MetaIndex_strategy = st.builds(
    setup_MetaIndex,
)

@given(instance=setup_Query_strategy)
@settings(max_examples=50)
def test_setup_query_instantiation(instance):
    assert isinstance(instance, setup_Query)



@given(instance=setup_Query_strategy)
def test_setup_query_uRL_setter(instance):
    original = instance.uRL
    instance.uRL = original
    assert instance.uRL == original



@given(instance=setup_Query_strategy)
def test_setup_query_summary_setter(instance):
    original = instance.summary
    instance.summary = original
    assert instance.summary == original

@given(instance=setup_BuildPlan_strategy)
@settings(max_examples=50)
def test_setup_buildplan_instantiation(instance):
    assert isinstance(instance, setup_BuildPlan)



@given(instance=setup_BuildPlan_strategy)
def test_setup_buildplan_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=setup_QueryAttribute_strategy)
@settings(max_examples=50)
def test_setup_queryattribute_instantiation(instance):
    assert isinstance(instance, setup_QueryAttribute)



@given(instance=setup_QueryAttribute_strategy)
def test_setup_queryattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=setup_QueryAttribute_strategy)
def test_setup_queryattribute_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=setup_TextModification_strategy)
@settings(max_examples=50)
def test_setup_textmodification_instantiation(instance):
    assert isinstance(instance, setup_TextModification)



@given(instance=setup_TextModification_strategy)
def test_setup_textmodification_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original



@given(instance=setup_TextModification_strategy)
def test_setup_textmodification_substitutions_setter(instance):
    original = instance.substitutions
    instance.substitutions = original
    assert instance.substitutions == original

@given(instance=setup_CommandParameter_strategy)
@settings(max_examples=50)
def test_setup_commandparameter_instantiation(instance):
    assert isinstance(instance, setup_CommandParameter)



@given(instance=setup_CommandParameter_strategy)
def test_setup_commandparameter_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original



@given(instance=setup_CommandParameter_strategy)
def test_setup_commandparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=setup_KeyBindingContext_strategy)
@settings(max_examples=50)
def test_setup_keybindingcontext_instantiation(instance):
    assert isinstance(instance, setup_KeyBindingContext)



@given(instance=setup_KeyBindingContext_strategy)
def test_setup_keybindingcontext_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original

@given(instance=setup_FileEditor_strategy)
@settings(max_examples=50)
def test_setup_fileeditor_instantiation(instance):
    assert isinstance(instance, setup_FileEditor)



@given(instance=setup_FileEditor_strategy)
def test_setup_fileeditor_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original

@given(instance=setup_WorkingSet_strategy)
@settings(max_examples=50)
def test_setup_workingset_instantiation(instance):
    assert isinstance(instance, setup_WorkingSet)

@given(instance=setup_FileMapping_strategy)
@settings(max_examples=50)
def test_setup_filemapping_instantiation(instance):
    assert isinstance(instance, setup_FileMapping)



@given(instance=setup_FileMapping_strategy)
def test_setup_filemapping_filePattern_setter(instance):
    original = instance.filePattern
    instance.filePattern = original
    assert instance.filePattern == original



@given(instance=setup_FileMapping_strategy)
def test_setup_filemapping_defaultEditorID_setter(instance):
    original = instance.defaultEditorID
    instance.defaultEditorID = original
    assert instance.defaultEditorID == original

@given(instance=setup_TargletData_strategy)
@settings(max_examples=50)
def test_setup_targletdata_instantiation(instance):
    assert isinstance(instance, setup_TargletData)



@given(instance=setup_TargletData_strategy)
def test_setup_targletdata_includeAllPlatforms_setter(instance):
    original = instance.includeAllPlatforms
    instance.includeAllPlatforms = original
    assert instance.includeAllPlatforms == original



@given(instance=setup_TargletData_strategy)
def test_setup_targletdata_activeRepositoryList_setter(instance):
    original = instance.activeRepositoryList
    instance.activeRepositoryList = original
    assert instance.activeRepositoryList == original



@given(instance=setup_TargletData_strategy)
def test_setup_targletdata_includeSources_setter(instance):
    original = instance.includeSources
    instance.includeSources = original
    assert instance.includeSources == original



@given(instance=setup_TargletData_strategy)
def test_setup_targletdata_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TargletData_strategy)
@settings(max_examples=50)
def test_targletdata_instantiation(instance):
    assert isinstance(instance, TargletData)

@given(instance=setup_Targlet_strategy)
@settings(max_examples=50)
def test_setup_targlet_instantiation(instance):
    assert isinstance(instance, setup_Targlet)

@given(instance=setup_RepositoryList_strategy)
@settings(max_examples=50)
def test_setup_repositorylist_instantiation(instance):
    assert isinstance(instance, setup_RepositoryList)



@given(instance=setup_RepositoryList_strategy)
def test_setup_repositorylist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ComponentExtension_strategy)
@settings(max_examples=50)
def test_componentextension_instantiation(instance):
    assert isinstance(instance, ComponentExtension)

@given(instance=setup_ComponentDefinition_strategy)
@settings(max_examples=50)
def test_setup_componentdefinition_instantiation(instance):
    assert isinstance(instance, setup_ComponentDefinition)



@given(instance=setup_ComponentDefinition_strategy)
def test_setup_componentdefinition_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=setup_ComponentDefinition_strategy)
def test_setup_componentdefinition_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original

@given(instance=setup_Component_strategy)
@settings(max_examples=50)
def test_setup_component_instantiation(instance):
    assert isinstance(instance, setup_Component)



@given(instance=setup_Component_strategy)
def test_setup_component_versionRange_setter(instance):
    original = instance.versionRange
    instance.versionRange = original
    assert instance.versionRange == original



@given(instance=setup_Component_strategy)
def test_setup_component_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=setup_Component_strategy)
def test_setup_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=setup_ComponentExtension_strategy)
@settings(max_examples=50)
def test_setup_componentextension_instantiation(instance):
    assert isinstance(instance, setup_ComponentExtension)

@given(instance=setup_Predicate_strategy)
@settings(max_examples=50)
def test_setup_predicate_instantiation(instance):
    assert isinstance(instance, setup_Predicate)

@given(instance=SourceLocator_strategy)
@settings(max_examples=50)
def test_sourcelocator_instantiation(instance):
    assert isinstance(instance, SourceLocator)

@given(instance=setup_AutomaticSourceLocator_strategy)
@settings(max_examples=50)
def test_setup_automaticsourcelocator_instantiation(instance):
    assert isinstance(instance, setup_AutomaticSourceLocator)



@given(instance=setup_AutomaticSourceLocator_strategy)
def test_setup_automaticsourcelocator_locateNestedProjects_setter(instance):
    original = instance.locateNestedProjects
    instance.locateNestedProjects = original
    assert instance.locateNestedProjects == original



@given(instance=setup_AutomaticSourceLocator_strategy)
def test_setup_automaticsourcelocator_rootFolder_setter(instance):
    original = instance.rootFolder
    instance.rootFolder = original
    assert instance.rootFolder == original

@given(instance=setup_ManualSourceLocator_strategy)
@settings(max_examples=50)
def test_setup_manualsourcelocator_instantiation(instance):
    assert isinstance(instance, setup_ManualSourceLocator)



@given(instance=setup_ManualSourceLocator_strategy)
def test_setup_manualsourcelocator_componentTypes_setter(instance):
    original = instance.componentTypes
    instance.componentTypes = original
    assert instance.componentTypes == original



@given(instance=setup_ManualSourceLocator_strategy)
def test_setup_manualsourcelocator_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=setup_ManualSourceLocator_strategy)
def test_setup_manualsourcelocator_componentNamePattern_setter(instance):
    original = instance.componentNamePattern
    instance.componentNamePattern = original
    assert instance.componentNamePattern == original

@given(instance=setup_SourceLocator_strategy)
@settings(max_examples=50)
def test_setup_sourcelocator_instantiation(instance):
    assert isinstance(instance, setup_SourceLocator)

@given(instance=setup_P2Repository_strategy)
@settings(max_examples=50)
def test_setup_p2repository_instantiation(instance):
    assert isinstance(instance, setup_P2Repository)



@given(instance=setup_P2Repository_strategy)
def test_setup_p2repository_uRL_setter(instance):
    original = instance.uRL
    instance.uRL = original
    assert instance.uRL == original

@given(instance=setup_InstallableUnit_strategy)
@settings(max_examples=50)
def test_setup_installableunit_instantiation(instance):
    assert isinstance(instance, setup_InstallableUnit)



@given(instance=setup_InstallableUnit_strategy)
def test_setup_installableunit_versionRange_setter(instance):
    original = instance.versionRange
    instance.versionRange = original
    assert instance.versionRange == original



@given(instance=setup_InstallableUnit_strategy)
def test_setup_installableunit_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original

@given(instance=BasicMaterializationTask_strategy)
@settings(max_examples=50)
def test_basicmaterializationtask_instantiation(instance):
    assert isinstance(instance, BasicMaterializationTask)

@given(instance=setup_MaterializationTask_strategy)
@settings(max_examples=50)
def test_setup_materializationtask_instantiation(instance):
    assert isinstance(instance, setup_MaterializationTask)

@given(instance=setup_BuckminsterImportTask_strategy)
@settings(max_examples=50)
def test_setup_buckminsterimporttask_instantiation(instance):
    assert isinstance(instance, setup_BuckminsterImportTask)



@given(instance=setup_BuckminsterImportTask_strategy)
def test_setup_buckminsterimporttask_mspec_setter(instance):
    original = instance.mspec
    instance.mspec = original
    assert instance.mspec == original

@given(instance=SetupTask_strategy)
@settings(max_examples=50)
def test_setuptask_instantiation(instance):
    assert isinstance(instance, SetupTask)

@given(instance=setup_ProjectSetImportTask_strategy)
@settings(max_examples=50)
def test_setup_projectsetimporttask_instantiation(instance):
    assert isinstance(instance, setup_ProjectSetImportTask)



@given(instance=setup_ProjectSetImportTask_strategy)
def test_setup_projectsetimporttask_uRL_setter(instance):
    original = instance.uRL
    instance.uRL = original
    assert instance.uRL == original

@given(instance=setup_EclipsePreferenceTask_strategy)
@settings(max_examples=50)
def test_setup_eclipsepreferencetask_instantiation(instance):
    assert isinstance(instance, setup_EclipsePreferenceTask)



@given(instance=setup_EclipsePreferenceTask_strategy)
def test_setup_eclipsepreferencetask_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=setup_EclipsePreferenceTask_strategy)
def test_setup_eclipsepreferencetask_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=setup_TargletImportTask_strategy)
@settings(max_examples=50)
def test_setup_targletimporttask_instantiation(instance):
    assert isinstance(instance, setup_TargletImportTask)



@given(instance=setup_TargletImportTask_strategy)
def test_setup_targletimporttask_targletURI_setter(instance):
    original = instance.targletURI
    instance.targletURI = original
    assert instance.targletURI == original

@given(instance=setup_JRETask_strategy)
@settings(max_examples=50)
def test_setup_jretask_instantiation(instance):
    assert isinstance(instance, setup_JRETask)



@given(instance=setup_JRETask_strategy)
def test_setup_jretask_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=setup_JRETask_strategy)
def test_setup_jretask_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=setup_TextModifyTask_strategy)
@settings(max_examples=50)
def test_setup_textmodifytask_instantiation(instance):
    assert isinstance(instance, setup_TextModifyTask)



@given(instance=setup_TextModifyTask_strategy)
def test_setup_textmodifytask_uRL_setter(instance):
    original = instance.uRL
    instance.uRL = original
    assert instance.uRL == original



@given(instance=setup_TextModifyTask_strategy)
def test_setup_textmodifytask_encoding_setter(instance):
    original = instance.encoding
    instance.encoding = original
    assert instance.encoding == original

@given(instance=setup_ProjectsImportTask_strategy)
@settings(max_examples=50)
def test_setup_projectsimporttask_instantiation(instance):
    assert isinstance(instance, setup_ProjectsImportTask)

@given(instance=setup_MylynQueryTask_strategy)
@settings(max_examples=50)
def test_setup_mylynquerytask_instantiation(instance):
    assert isinstance(instance, setup_MylynQueryTask)



@given(instance=setup_MylynQueryTask_strategy)
def test_setup_mylynquerytask_summary_setter(instance):
    original = instance.summary
    instance.summary = original
    assert instance.summary == original



@given(instance=setup_MylynQueryTask_strategy)
def test_setup_mylynquerytask_repositoryURL_setter(instance):
    original = instance.repositoryURL
    instance.repositoryURL = original
    assert instance.repositoryURL == original



@given(instance=setup_MylynQueryTask_strategy)
def test_setup_mylynquerytask_connectorKind_setter(instance):
    original = instance.connectorKind
    instance.connectorKind = original
    assert instance.connectorKind == original



@given(instance=setup_MylynQueryTask_strategy)
def test_setup_mylynquerytask_relativeURL_setter(instance):
    original = instance.relativeURL
    instance.relativeURL = original
    assert instance.relativeURL == original

@given(instance=setup_FileAssociationTask_strategy)
@settings(max_examples=50)
def test_setup_fileassociationtask_instantiation(instance):
    assert isinstance(instance, setup_FileAssociationTask)



@given(instance=setup_FileAssociationTask_strategy)
def test_setup_fileassociationtask_filePattern_setter(instance):
    original = instance.filePattern
    instance.filePattern = original
    assert instance.filePattern == original



@given(instance=setup_FileAssociationTask_strategy)
def test_setup_fileassociationtask_defaultEditorID_setter(instance):
    original = instance.defaultEditorID
    instance.defaultEditorID = original
    assert instance.defaultEditorID == original

@given(instance=setup_ResourceCopyTask_strategy)
@settings(max_examples=50)
def test_setup_resourcecopytask_instantiation(instance):
    assert isinstance(instance, setup_ResourceCopyTask)



@given(instance=setup_ResourceCopyTask_strategy)
def test_setup_resourcecopytask_targetURL_setter(instance):
    original = instance.targetURL
    instance.targetURL = original
    assert instance.targetURL == original



@given(instance=setup_ResourceCopyTask_strategy)
def test_setup_resourcecopytask_sourceURL_setter(instance):
    original = instance.sourceURL
    instance.sourceURL = original
    assert instance.sourceURL == original

@given(instance=setup_KeyBindingTask_strategy)
@settings(max_examples=50)
def test_setup_keybindingtask_instantiation(instance):
    assert isinstance(instance, setup_KeyBindingTask)



@given(instance=setup_KeyBindingTask_strategy)
def test_setup_keybindingtask_command_setter(instance):
    original = instance.command
    instance.command = original
    assert instance.command == original



@given(instance=setup_KeyBindingTask_strategy)
def test_setup_keybindingtask_keys_setter(instance):
    original = instance.keys
    instance.keys = original
    assert instance.keys == original



@given(instance=setup_KeyBindingTask_strategy)
def test_setup_keybindingtask_platform_setter(instance):
    original = instance.platform
    instance.platform = original
    assert instance.platform == original



@given(instance=setup_KeyBindingTask_strategy)
def test_setup_keybindingtask_locale_setter(instance):
    original = instance.locale
    instance.locale = original
    assert instance.locale == original



@given(instance=setup_KeyBindingTask_strategy)
def test_setup_keybindingtask_scheme_setter(instance):
    original = instance.scheme
    instance.scheme = original
    assert instance.scheme == original

@given(instance=setup_MylynBuildsTask_strategy)
@settings(max_examples=50)
def test_setup_mylynbuildstask_instantiation(instance):
    assert isinstance(instance, setup_MylynBuildsTask)



@given(instance=setup_MylynBuildsTask_strategy)
def test_setup_mylynbuildstask_serverURL_setter(instance):
    original = instance.serverURL
    instance.serverURL = original
    assert instance.serverURL == original



@given(instance=setup_MylynBuildsTask_strategy)
def test_setup_mylynbuildstask_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=setup_MylynBuildsTask_strategy)
def test_setup_mylynbuildstask_connectorKind_setter(instance):
    original = instance.connectorKind
    instance.connectorKind = original
    assert instance.connectorKind == original



@given(instance=setup_MylynBuildsTask_strategy)
def test_setup_mylynbuildstask_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original

@given(instance=setup_ResourceCreationTask_strategy)
@settings(max_examples=50)
def test_setup_resourcecreationtask_instantiation(instance):
    assert isinstance(instance, setup_ResourceCreationTask)



@given(instance=setup_ResourceCreationTask_strategy)
def test_setup_resourcecreationtask_encoding_setter(instance):
    original = instance.encoding
    instance.encoding = original
    assert instance.encoding == original



@given(instance=setup_ResourceCreationTask_strategy)
def test_setup_resourcecreationtask_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=setup_ResourceCreationTask_strategy)
def test_setup_resourcecreationtask_targetURL_setter(instance):
    original = instance.targetURL
    instance.targetURL = original
    assert instance.targetURL == original

@given(instance=setup_GitCloneTask_strategy)
@settings(max_examples=50)
def test_setup_gitclonetask_instantiation(instance):
    assert isinstance(instance, setup_GitCloneTask)



@given(instance=setup_GitCloneTask_strategy)
def test_setup_gitclonetask_pushURI_setter(instance):
    original = instance.pushURI
    instance.pushURI = original
    assert instance.pushURI == original



@given(instance=setup_GitCloneTask_strategy)
def test_setup_gitclonetask_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=setup_GitCloneTask_strategy)
def test_setup_gitclonetask_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=setup_GitCloneTask_strategy)
def test_setup_gitclonetask_remoteName_setter(instance):
    original = instance.remoteName
    instance.remoteName = original
    assert instance.remoteName == original



@given(instance=setup_GitCloneTask_strategy)
def test_setup_gitclonetask_checkoutBranch_setter(instance):
    original = instance.checkoutBranch
    instance.checkoutBranch = original
    assert instance.checkoutBranch == original



@given(instance=setup_GitCloneTask_strategy)
def test_setup_gitclonetask_remoteURI_setter(instance):
    original = instance.remoteURI
    instance.remoteURI = original
    assert instance.remoteURI == original

@given(instance=setup_BasicMaterializationTask_strategy)
@settings(max_examples=50)
def test_setup_basicmaterializationtask_instantiation(instance):
    assert isinstance(instance, setup_BasicMaterializationTask)



@given(instance=setup_BasicMaterializationTask_strategy)
def test_setup_basicmaterializationtask_bundlePool_setter(instance):
    original = instance.bundlePool
    instance.bundlePool = original
    assert instance.bundlePool == original



@given(instance=setup_BasicMaterializationTask_strategy)
def test_setup_basicmaterializationtask_targetPlatform_setter(instance):
    original = instance.targetPlatform
    instance.targetPlatform = original
    assert instance.targetPlatform == original

@given(instance=setup_FileAssociationsTask_strategy)
@settings(max_examples=50)
def test_setup_fileassociationstask_instantiation(instance):
    assert isinstance(instance, setup_FileAssociationsTask)

@given(instance=setup_WorkingSetTask_strategy)
@settings(max_examples=50)
def test_setup_workingsettask_instantiation(instance):
    assert isinstance(instance, setup_WorkingSetTask)

@given(instance=setup_ApiBaselineTask_strategy)
@settings(max_examples=50)
def test_setup_apibaselinetask_instantiation(instance):
    assert isinstance(instance, setup_ApiBaselineTask)



@given(instance=setup_ApiBaselineTask_strategy)
def test_setup_apibaselinetask_containerFolder_setter(instance):
    original = instance.containerFolder
    instance.containerFolder = original
    assert instance.containerFolder == original



@given(instance=setup_ApiBaselineTask_strategy)
def test_setup_apibaselinetask_zipLocation_setter(instance):
    original = instance.zipLocation
    instance.zipLocation = original
    assert instance.zipLocation == original



@given(instance=setup_ApiBaselineTask_strategy)
def test_setup_apibaselinetask_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=setup_TargetPlatformTask_strategy)
@settings(max_examples=50)
def test_setup_targetplatformtask_instantiation(instance):
    assert isinstance(instance, setup_TargetPlatformTask)



@given(instance=setup_TargetPlatformTask_strategy)
def test_setup_targetplatformtask_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=setup_MylynQueriesTask_strategy)
@settings(max_examples=50)
def test_setup_mylynqueriestask_instantiation(instance):
    assert isinstance(instance, setup_MylynQueriesTask)



@given(instance=setup_MylynQueriesTask_strategy)
def test_setup_mylynqueriestask_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=setup_MylynQueriesTask_strategy)
def test_setup_mylynqueriestask_repositoryURL_setter(instance):
    original = instance.repositoryURL
    instance.repositoryURL = original
    assert instance.repositoryURL == original



@given(instance=setup_MylynQueriesTask_strategy)
def test_setup_mylynqueriestask_connectorKind_setter(instance):
    original = instance.connectorKind
    instance.connectorKind = original
    assert instance.connectorKind == original



@given(instance=setup_MylynQueriesTask_strategy)
def test_setup_mylynqueriestask_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original

@given(instance=setup_TargletTask_strategy)
@settings(max_examples=50)
def test_setup_targlettask_instantiation(instance):
    assert isinstance(instance, setup_TargletTask)

@given(instance=setup_MavenImportTask_strategy)
@settings(max_examples=50)
def test_setup_mavenimporttask_instantiation(instance):
    assert isinstance(instance, setup_MavenImportTask)

@given(instance=setup_P2Task_strategy)
@settings(max_examples=50)
def test_setup_p2task_instantiation(instance):
    assert isinstance(instance, setup_P2Task)



@given(instance=setup_P2Task_strategy)
def test_setup_p2task_licenseConfirmationDisabled_setter(instance):
    original = instance.licenseConfirmationDisabled
    instance.licenseConfirmationDisabled = original
    assert instance.licenseConfirmationDisabled == original



@given(instance=setup_P2Task_strategy)
def test_setup_p2task_mergeDisabled_setter(instance):
    original = instance.mergeDisabled
    instance.mergeDisabled = original
    assert instance.mergeDisabled == original

@given(instance=SetupTaskContainer_strategy)
@settings(max_examples=50)
def test_setuptaskcontainer_instantiation(instance):
    assert isinstance(instance, SetupTaskContainer)

@given(instance=setup_CompoundSetupTask_strategy)
@settings(max_examples=50)
def test_setup_compoundsetuptask_instantiation(instance):
    assert isinstance(instance, setup_CompoundSetupTask)



@given(instance=setup_CompoundSetupTask_strategy)
def test_setup_compoundsetuptask_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=setup_ScopeRoot_strategy)
@settings(max_examples=50)
def test_setup_scoperoot_instantiation(instance):
    assert isinstance(instance, setup_ScopeRoot)

@given(instance=setup_SetupTaskContainer_strategy)
@settings(max_examples=50)
def test_setup_setuptaskcontainer_instantiation(instance):
    assert isinstance(instance, setup_SetupTaskContainer)

@given(instance=setup_LinkLocationTask_strategy)
@settings(max_examples=50)
def test_setup_linklocationtask_instantiation(instance):
    assert isinstance(instance, setup_LinkLocationTask)



@given(instance=setup_LinkLocationTask_strategy)
def test_setup_linklocationtask_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original



@given(instance=setup_LinkLocationTask_strategy)
def test_setup_linklocationtask_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=setup_EclipseIniTask_strategy)
@settings(max_examples=50)
def test_setup_eclipseinitask_instantiation(instance):
    assert isinstance(instance, setup_EclipseIniTask)



@given(instance=setup_EclipseIniTask_strategy)
def test_setup_eclipseinitask_option_setter(instance):
    original = instance.option
    instance.option = original
    assert instance.option == original



@given(instance=setup_EclipseIniTask_strategy)
def test_setup_eclipseinitask_vm_setter(instance):
    original = instance.vm
    instance.vm = original
    assert instance.vm == original



@given(instance=setup_EclipseIniTask_strategy)
def test_setup_eclipseinitask_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=setup_RedirectionTask_strategy)
@settings(max_examples=50)
def test_setup_redirectiontask_instantiation(instance):
    assert isinstance(instance, setup_RedirectionTask)



@given(instance=setup_RedirectionTask_strategy)
def test_setup_redirectiontask_targetURL_setter(instance):
    original = instance.targetURL
    instance.targetURL = original
    assert instance.targetURL == original



@given(instance=setup_RedirectionTask_strategy)
def test_setup_redirectiontask_sourceURL_setter(instance):
    original = instance.sourceURL
    instance.sourceURL = original
    assert instance.sourceURL == original

@given(instance=setup_VariableChoice_strategy)
@settings(max_examples=50)
def test_setup_variablechoice_instantiation(instance):
    assert isinstance(instance, setup_VariableChoice)



@given(instance=setup_VariableChoice_strategy)
def test_setup_variablechoice_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=setup_VariableChoice_strategy)
def test_setup_variablechoice_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=setup_ContextVariableTask_strategy)
@settings(max_examples=50)
def test_setup_contextvariabletask_instantiation(instance):
    assert isinstance(instance, setup_ContextVariableTask)



@given(instance=setup_ContextVariableTask_strategy)
def test_setup_contextvariabletask_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=setup_ContextVariableTask_strategy)
def test_setup_contextvariabletask_stringSubstitution_setter(instance):
    original = instance.stringSubstitution
    instance.stringSubstitution = original
    assert instance.stringSubstitution == original



@given(instance=setup_ContextVariableTask_strategy)
def test_setup_contextvariabletask_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=setup_ContextVariableTask_strategy)
def test_setup_contextvariabletask_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=setup_ContextVariableTask_strategy)
def test_setup_contextvariabletask_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=setup_SetupTask_strategy)
@settings(max_examples=50)
def test_setup_setuptask_instantiation(instance):
    assert isinstance(instance, setup_SetupTask)



@given(instance=setup_SetupTask_strategy)
def test_setup_setuptask_excludedTriggers_setter(instance):
    original = instance.excludedTriggers
    instance.excludedTriggers = original
    assert instance.excludedTriggers == original



@given(instance=setup_SetupTask_strategy)
def test_setup_setuptask_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original



@given(instance=setup_SetupTask_strategy)
def test_setup_setuptask_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original



@given(instance=setup_SetupTask_strategy)
def test_setup_setuptask_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=setup_SetupTask_strategy)
@settings(max_examples=30)
def test_setup_setuptask_requires_changes_state(instance):
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
        assert has_statements, f"Function 'requires' in setup_SetupTask is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'requires' in setup_SetupTask did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'requires' in setup_SetupTask is not implemented or raised an error")

@given(instance=setup_Setup_strategy)
@settings(max_examples=50)
def test_setup_setup_instantiation(instance):
    assert isinstance(instance, setup_Setup)

@given(instance=ConfigurableItem_strategy)
@settings(max_examples=50)
def test_configurableitem_instantiation(instance):
    assert isinstance(instance, ConfigurableItem)

@given(instance=setup_Eclipse_strategy)
@settings(max_examples=50)
def test_setup_eclipse_instantiation(instance):
    assert isinstance(instance, setup_Eclipse)



@given(instance=setup_Eclipse_strategy)
def test_setup_eclipse_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=setup_Branch_strategy)
@settings(max_examples=50)
def test_setup_branch_instantiation(instance):
    assert isinstance(instance, setup_Branch)



@given(instance=setup_Branch_strategy)
def test_setup_branch_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=setup_Project_strategy)
@settings(max_examples=50)
def test_setup_project_instantiation(instance):
    assert isinstance(instance, setup_Project)



@given(instance=setup_Project_strategy)
def test_setup_project_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=setup_Project_strategy)
def test_setup_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ScopeRoot_strategy)
@settings(max_examples=50)
def test_scoperoot_instantiation(instance):
    assert isinstance(instance, ScopeRoot)

@given(instance=setup_ConfigurableItem_strategy)
@settings(max_examples=50)
def test_setup_configurableitem_instantiation(instance):
    assert isinstance(instance, setup_ConfigurableItem)

@given(instance=setup_Preferences_strategy)
@settings(max_examples=50)
def test_setup_preferences_instantiation(instance):
    assert isinstance(instance, setup_Preferences)



@given(instance=setup_Preferences_strategy)
def test_setup_preferences_acceptedLicenses_setter(instance):
    original = instance.acceptedLicenses
    instance.acceptedLicenses = original
    assert instance.acceptedLicenses == original



@given(instance=setup_Preferences_strategy)
def test_setup_preferences_installFolder_setter(instance):
    original = instance.installFolder
    instance.installFolder = original
    assert instance.installFolder == original

@given(instance=setup_Configuration_strategy)
@settings(max_examples=50)
def test_setup_configuration_instantiation(instance):
    assert isinstance(instance, setup_Configuration)

@given(instance=setup_Index_strategy)
@settings(max_examples=50)
def test_setup_index_instantiation(instance):
    assert isinstance(instance, setup_Index)



@given(instance=setup_Index_strategy)
def test_setup_index_uRI_setter(instance):
    original = instance.uRI
    instance.uRI = original
    assert instance.uRI == original



@given(instance=setup_Index_strategy)
def test_setup_index_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=setup_Index_strategy)
def test_setup_index_oldURIs_setter(instance):
    original = instance.oldURIs
    instance.oldURIs = original
    assert instance.oldURIs == original

@given(instance=setup_MetaIndex_strategy)
@settings(max_examples=50)
def test_setup_metaindex_instantiation(instance):
    assert isinstance(instance, setup_MetaIndex)

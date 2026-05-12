####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
SetupTaskScope: Enumeration = Enumeration(
    name="SetupTaskScope",
    literals={
            EnumerationLiteral(name="None_"),
			EnumerationLiteral(name="Eclipse"),
			EnumerationLiteral(name="Project"),
			EnumerationLiteral(name="Branch"),
			EnumerationLiteral(name="User"),
			EnumerationLiteral(name="Configuration")
    }
)

VariableType: Enumeration = Enumeration(
    name="VariableType",
    literals={
            EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="TEXT"),
			EnumerationLiteral(name="PASSWORD"),
			EnumerationLiteral(name="PATTERN"),
			EnumerationLiteral(name="URI"),
			EnumerationLiteral(name="FILE"),
			EnumerationLiteral(name="FOLDER"),
			EnumerationLiteral(name="RESOURCE"),
			EnumerationLiteral(name="CONTAINER"),
			EnumerationLiteral(name="PROJECT"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="FLOAT")
    }
)

Trigger: Enumeration = Enumeration(
    name="Trigger",
    literals={
            EnumerationLiteral(name="BOOTSTRAP"),
			EnumerationLiteral(name="STARTUP"),
			EnumerationLiteral(name="MANUAL")
    }
)

ComponentType: Enumeration = Enumeration(
    name="ComponentType",
    literals={
            EnumerationLiteral(name="OSGI_BUNDLE"),
			EnumerationLiteral(name="BUCKMINSTER"),
			EnumerationLiteral(name="JAR"),
			EnumerationLiteral(name="BOM"),
			EnumerationLiteral(name="UNKNOWN"),
			EnumerationLiteral(name="ECLIPSE_FEATURE")
    }
)

# Classes
setup_MetaIndex = Class(name="setup_MetaIndex")
setup_Index = Class(name="setup_Index")
ScopeRoot = Class(name="ScopeRoot")
setup_Project = Class(name="setup_Project")
setup_ConfigurableItem = Class(name="setup_ConfigurableItem", is_abstract=True)
setup_Branch = Class(name="setup_Branch")
setup_Eclipse = Class(name="setup_Eclipse")
ConfigurableItem = Class(name="ConfigurableItem")
setup_Configuration = Class(name="setup_Configuration")
setup_Setup = Class(name="setup_Setup")
setup_SetupTask = Class(name="setup_SetupTask", is_abstract=True)
setup_Preferences = Class(name="setup_Preferences")
setup_ContextVariableTask = Class(name="setup_ContextVariableTask")
setup_VariableChoice = Class(name="setup_VariableChoice")
setup_RedirectionTask = Class(name="setup_RedirectionTask")
setup_EclipseIniTask = Class(name="setup_EclipseIniTask")
setup_LinkLocationTask = Class(name="setup_LinkLocationTask")
setup_SetupTaskContainer = Class(name="setup_SetupTaskContainer", is_abstract=True)
setup_ScopeRoot = Class(name="setup_ScopeRoot", is_abstract=True)
SetupTaskContainer = Class(name="SetupTaskContainer")
setup_CompoundSetupTask = Class(name="setup_CompoundSetupTask")
SetupTask = Class(name="SetupTask")
setup_GitCloneTask = Class(name="setup_GitCloneTask")
setup_BasicMaterializationTask = Class(name="setup_BasicMaterializationTask", is_abstract=True)
setup_BuckminsterImportTask = Class(name="setup_BuckminsterImportTask")
BasicMaterializationTask = Class(name="BasicMaterializationTask")
setup_P2Task = Class(name="setup_P2Task")
setup_InstallableUnit = Class(name="setup_InstallableUnit")
setup_P2Repository = Class(name="setup_P2Repository")
setup_SourceLocator = Class(name="setup_SourceLocator", is_abstract=True)
setup_ManualSourceLocator = Class(name="setup_ManualSourceLocator")
SourceLocator = Class(name="SourceLocator")
setup_AutomaticSourceLocator = Class(name="setup_AutomaticSourceLocator")
setup_Predicate = Class(name="setup_Predicate")
setup_ComponentExtension = Class(name="setup_ComponentExtension")
setup_MaterializationTask = Class(name="setup_MaterializationTask")
setup_Component = Class(name="setup_Component")
setup_MavenImportTask = Class(name="setup_MavenImportTask")
setup_TargletImportTask = Class(name="setup_TargletImportTask")
setup_TargletTask = Class(name="setup_TargletTask")
setup_ComponentDefinition = Class(name="setup_ComponentDefinition")
ComponentExtension = Class(name="ComponentExtension")
setup_RepositoryList = Class(name="setup_RepositoryList")
setup_ProjectsImportTask = Class(name="setup_ProjectsImportTask")
setup_ProjectSetImportTask = Class(name="setup_ProjectSetImportTask")
setup_TargetPlatformTask = Class(name="setup_TargetPlatformTask")
setup_ApiBaselineTask = Class(name="setup_ApiBaselineTask")
TargletData = Class(name="TargletData")
setup_Targlet = Class(name="setup_Targlet")
setup_TargletData = Class(name="setup_TargletData", is_abstract=True)
setup_FileAssociationsTask = Class(name="setup_FileAssociationsTask")
setup_FileMapping = Class(name="setup_FileMapping")
setup_WorkingSetTask = Class(name="setup_WorkingSetTask")
setup_WorkingSet = Class(name="setup_WorkingSet")
setup_ResourceCopyTask = Class(name="setup_ResourceCopyTask")
setup_ResourceCreationTask = Class(name="setup_ResourceCreationTask")
setup_TextModifyTask = Class(name="setup_TextModifyTask")
setup_EclipsePreferenceTask = Class(name="setup_EclipsePreferenceTask")
setup_FileAssociationTask = Class(name="setup_FileAssociationTask")
setup_FileEditor = Class(name="setup_FileEditor")
setup_KeyBindingContext = Class(name="setup_KeyBindingContext")
setup_CommandParameter = Class(name="setup_CommandParameter")
setup_MylynQueryTask = Class(name="setup_MylynQueryTask")
setup_MylynQueriesTask = Class(name="setup_MylynQueriesTask")
setup_TextModification = Class(name="setup_TextModification")
setup_KeyBindingTask = Class(name="setup_KeyBindingTask")
setup_QueryAttribute = Class(name="setup_QueryAttribute")
setup_MylynBuildsTask = Class(name="setup_MylynBuildsTask")
setup_BuildPlan = Class(name="setup_BuildPlan")
setup_JRETask = Class(name="setup_JRETask")
setup_Query = Class(name="setup_Query")

# setup_MetaIndex class attributes and methods

# setup_Index class attributes and methods
setup_Index_name: Property = Property(name="name", type=StringType)
setup_Index_uRI: Property = Property(name="uRI", type=StringType)
setup_Index_oldURIs: Property = Property(name="oldURIs", type=StringType)
setup_Index.attributes={setup_Index_oldURIs, setup_Index_uRI, setup_Index_name}

# ScopeRoot class attributes and methods

# setup_Project class attributes and methods
setup_Project_name: Property = Property(name="name", type=StringType)
setup_Project_label: Property = Property(name="label", type=StringType)
setup_Project.attributes={setup_Project_label, setup_Project_name}

# setup_ConfigurableItem class attributes and methods

# setup_Branch class attributes and methods
setup_Branch_name: Property = Property(name="name", type=StringType)
setup_Branch.attributes={setup_Branch_name}

# setup_Eclipse class attributes and methods
setup_Eclipse_version: Property = Property(name="version", type=StringType)
setup_Eclipse.attributes={setup_Eclipse_version}

# ConfigurableItem class attributes and methods

# setup_Configuration class attributes and methods

# setup_Setup class attributes and methods
setup_Setup_m_getSetupTasks: Method = Method(name="getSetupTasks", parameters={Parameter(name='setup_preferences', type=StringType), Parameter(name='setup_filterRestrictions', type=StringType), Parameter(name='setup_trigger', type=StringType)}, type=StringType)
setup_Setup.methods={setup_Setup_m_getSetupTasks}

# setup_SetupTask class attributes and methods
setup_SetupTask_disabled: Property = Property(name="disabled", type=BooleanType)
setup_SetupTask_scope: Property = Property(name="scope", type=StringType)
setup_SetupTask_excludedTriggers: Property = Property(name="excludedTriggers", type=StringType)
setup_SetupTask_documentation: Property = Property(name="documentation", type=StringType)
setup_SetupTask_m_getScopeRoot: Method = Method(name="getScopeRoot", parameters={}, type=ScopeRoot)
setup_SetupTask_m_requires: Method = Method(name="requires", parameters={Parameter(name='setup_setupTask', type=StringType)}, type=BooleanType)
setup_SetupTask_m_getValidTriggers: Method = Method(name="getValidTriggers", parameters={}, type=StringType)
setup_SetupTask_m_getTriggers: Method = Method(name="getTriggers", parameters={}, type=StringType)
setup_SetupTask.attributes={setup_SetupTask_disabled, setup_SetupTask_scope, setup_SetupTask_excludedTriggers, setup_SetupTask_documentation}
setup_SetupTask.methods={setup_SetupTask_m_getTriggers, setup_SetupTask_m_requires, setup_SetupTask_m_getValidTriggers, setup_SetupTask_m_getScopeRoot}

# setup_Preferences class attributes and methods
setup_Preferences_installFolder: Property = Property(name="installFolder", type=StringType)
setup_Preferences_acceptedLicenses: Property = Property(name="acceptedLicenses", type=StringType)
setup_Preferences.attributes={setup_Preferences_acceptedLicenses, setup_Preferences_installFolder}

# setup_ContextVariableTask class attributes and methods
setup_ContextVariableTask_type: Property = Property(name="type", type=StringType)
setup_ContextVariableTask_name: Property = Property(name="name", type=StringType)
setup_ContextVariableTask_value: Property = Property(name="value", type=StringType)
setup_ContextVariableTask_stringSubstitution: Property = Property(name="stringSubstitution", type=BooleanType)
setup_ContextVariableTask_label: Property = Property(name="label", type=StringType)
setup_ContextVariableTask.attributes={setup_ContextVariableTask_stringSubstitution, setup_ContextVariableTask_name, setup_ContextVariableTask_label, setup_ContextVariableTask_value, setup_ContextVariableTask_type}

# setup_VariableChoice class attributes and methods
setup_VariableChoice_value: Property = Property(name="value", type=StringType)
setup_VariableChoice_label: Property = Property(name="label", type=StringType)
setup_VariableChoice.attributes={setup_VariableChoice_label, setup_VariableChoice_value}

# setup_RedirectionTask class attributes and methods
setup_RedirectionTask_sourceURL: Property = Property(name="sourceURL", type=StringType)
setup_RedirectionTask_targetURL: Property = Property(name="targetURL", type=StringType)
setup_RedirectionTask.attributes={setup_RedirectionTask_sourceURL, setup_RedirectionTask_targetURL}

# setup_EclipseIniTask class attributes and methods
setup_EclipseIniTask_option: Property = Property(name="option", type=StringType)
setup_EclipseIniTask_value: Property = Property(name="value", type=StringType)
setup_EclipseIniTask_vm: Property = Property(name="vm", type=BooleanType)
setup_EclipseIniTask.attributes={setup_EclipseIniTask_vm, setup_EclipseIniTask_option, setup_EclipseIniTask_value}

# setup_LinkLocationTask class attributes and methods
setup_LinkLocationTask_path: Property = Property(name="path", type=StringType)
setup_LinkLocationTask_name: Property = Property(name="name", type=StringType)
setup_LinkLocationTask.attributes={setup_LinkLocationTask_name, setup_LinkLocationTask_path}

# setup_SetupTaskContainer class attributes and methods

# setup_ScopeRoot class attributes and methods
setup_ScopeRoot_m_getScope: Method = Method(name="getScope", parameters={}, type=StringType)
setup_ScopeRoot_m_getParentScopeRoot: Method = Method(name="getParentScopeRoot", parameters={}, type=ScopeRoot)
setup_ScopeRoot.methods={setup_ScopeRoot_m_getScope, setup_ScopeRoot_m_getParentScopeRoot}

# SetupTaskContainer class attributes and methods

# setup_CompoundSetupTask class attributes and methods
setup_CompoundSetupTask_name: Property = Property(name="name", type=StringType)
setup_CompoundSetupTask.attributes={setup_CompoundSetupTask_name}

# SetupTask class attributes and methods

# setup_GitCloneTask class attributes and methods
setup_GitCloneTask_location: Property = Property(name="location", type=StringType)
setup_GitCloneTask_remoteName: Property = Property(name="remoteName", type=StringType)
setup_GitCloneTask_remoteURI: Property = Property(name="remoteURI", type=StringType)
setup_GitCloneTask_pushURI: Property = Property(name="pushURI", type=StringType)
setup_GitCloneTask_userID: Property = Property(name="userID", type=StringType)
setup_GitCloneTask_checkoutBranch: Property = Property(name="checkoutBranch", type=StringType)
setup_GitCloneTask.attributes={setup_GitCloneTask_userID, setup_GitCloneTask_pushURI, setup_GitCloneTask_checkoutBranch, setup_GitCloneTask_location, setup_GitCloneTask_remoteURI, setup_GitCloneTask_remoteName}

# setup_BasicMaterializationTask class attributes and methods
setup_BasicMaterializationTask_targetPlatform: Property = Property(name="targetPlatform", type=StringType)
setup_BasicMaterializationTask_bundlePool: Property = Property(name="bundlePool", type=StringType)
setup_BasicMaterializationTask.attributes={setup_BasicMaterializationTask_targetPlatform, setup_BasicMaterializationTask_bundlePool}

# setup_BuckminsterImportTask class attributes and methods
setup_BuckminsterImportTask_mspec: Property = Property(name="mspec", type=StringType)
setup_BuckminsterImportTask.attributes={setup_BuckminsterImportTask_mspec}

# BasicMaterializationTask class attributes and methods

# setup_P2Task class attributes and methods
setup_P2Task_mergeDisabled: Property = Property(name="mergeDisabled", type=BooleanType)
setup_P2Task_licenseConfirmationDisabled: Property = Property(name="licenseConfirmationDisabled", type=BooleanType)
setup_P2Task.attributes={setup_P2Task_mergeDisabled, setup_P2Task_licenseConfirmationDisabled}

# setup_InstallableUnit class attributes and methods
setup_InstallableUnit_iD: Property = Property(name="iD", type=StringType)
setup_InstallableUnit_versionRange: Property = Property(name="versionRange", type=StringType)
setup_InstallableUnit.attributes={setup_InstallableUnit_iD, setup_InstallableUnit_versionRange}

# setup_P2Repository class attributes and methods
setup_P2Repository_uRL: Property = Property(name="uRL", type=StringType)
setup_P2Repository.attributes={setup_P2Repository_uRL}

# setup_SourceLocator class attributes and methods

# setup_ManualSourceLocator class attributes and methods
setup_ManualSourceLocator_location: Property = Property(name="location", type=StringType)
setup_ManualSourceLocator_componentNamePattern: Property = Property(name="componentNamePattern", type=StringType)
setup_ManualSourceLocator_componentTypes: Property = Property(name="componentTypes", type=StringType)
setup_ManualSourceLocator.attributes={setup_ManualSourceLocator_componentTypes, setup_ManualSourceLocator_componentNamePattern, setup_ManualSourceLocator_location}

# SourceLocator class attributes and methods

# setup_AutomaticSourceLocator class attributes and methods
setup_AutomaticSourceLocator_rootFolder: Property = Property(name="rootFolder", type=StringType)
setup_AutomaticSourceLocator_locateNestedProjects: Property = Property(name="locateNestedProjects", type=BooleanType)
setup_AutomaticSourceLocator.attributes={setup_AutomaticSourceLocator_locateNestedProjects, setup_AutomaticSourceLocator_rootFolder}

# setup_Predicate class attributes and methods

# setup_ComponentExtension class attributes and methods

# setup_MaterializationTask class attributes and methods

# setup_Component class attributes and methods
setup_Component_name: Property = Property(name="name", type=StringType)
setup_Component_type: Property = Property(name="type", type=StringType)
setup_Component_versionRange: Property = Property(name="versionRange", type=StringType)
setup_Component.attributes={setup_Component_name, setup_Component_type, setup_Component_versionRange}

# setup_MavenImportTask class attributes and methods

# setup_TargletImportTask class attributes and methods
setup_TargletImportTask_targletURI: Property = Property(name="targletURI", type=StringType)
setup_TargletImportTask.attributes={setup_TargletImportTask_targletURI}

# setup_TargletTask class attributes and methods

# setup_ComponentDefinition class attributes and methods
setup_ComponentDefinition_version: Property = Property(name="version", type=StringType)
setup_ComponentDefinition_iD: Property = Property(name="iD", type=StringType)
setup_ComponentDefinition.attributes={setup_ComponentDefinition_iD, setup_ComponentDefinition_version}

# ComponentExtension class attributes and methods

# setup_RepositoryList class attributes and methods
setup_RepositoryList_name: Property = Property(name="name", type=StringType)
setup_RepositoryList.attributes={setup_RepositoryList_name}

# setup_ProjectsImportTask class attributes and methods

# setup_ProjectSetImportTask class attributes and methods
setup_ProjectSetImportTask_uRL: Property = Property(name="uRL", type=StringType)
setup_ProjectSetImportTask.attributes={setup_ProjectSetImportTask_uRL}

# setup_TargetPlatformTask class attributes and methods
setup_TargetPlatformTask_name: Property = Property(name="name", type=StringType)
setup_TargetPlatformTask.attributes={setup_TargetPlatformTask_name}

# setup_ApiBaselineTask class attributes and methods
setup_ApiBaselineTask_version: Property = Property(name="version", type=StringType)
setup_ApiBaselineTask_containerFolder: Property = Property(name="containerFolder", type=StringType)
setup_ApiBaselineTask_zipLocation: Property = Property(name="zipLocation", type=StringType)
setup_ApiBaselineTask.attributes={setup_ApiBaselineTask_version, setup_ApiBaselineTask_containerFolder, setup_ApiBaselineTask_zipLocation}

# TargletData class attributes and methods

# setup_Targlet class attributes and methods

# setup_TargletData class attributes and methods
setup_TargletData_activeRepositoryList: Property = Property(name="activeRepositoryList", type=StringType)
setup_TargletData_includeSources: Property = Property(name="includeSources", type=BooleanType)
setup_TargletData_includeAllPlatforms: Property = Property(name="includeAllPlatforms", type=BooleanType)
setup_TargletData_name: Property = Property(name="name", type=StringType)
setup_TargletData.attributes={setup_TargletData_includeSources, setup_TargletData_includeAllPlatforms, setup_TargletData_name, setup_TargletData_activeRepositoryList}

# setup_FileAssociationsTask class attributes and methods

# setup_FileMapping class attributes and methods
setup_FileMapping_filePattern: Property = Property(name="filePattern", type=StringType)
setup_FileMapping_defaultEditorID: Property = Property(name="defaultEditorID", type=StringType)
setup_FileMapping.attributes={setup_FileMapping_filePattern, setup_FileMapping_defaultEditorID}

# setup_WorkingSetTask class attributes and methods

# setup_WorkingSet class attributes and methods

# setup_ResourceCopyTask class attributes and methods
setup_ResourceCopyTask_sourceURL: Property = Property(name="sourceURL", type=StringType)
setup_ResourceCopyTask_targetURL: Property = Property(name="targetURL", type=StringType)
setup_ResourceCopyTask.attributes={setup_ResourceCopyTask_targetURL, setup_ResourceCopyTask_sourceURL}

# setup_ResourceCreationTask class attributes and methods
setup_ResourceCreationTask_content: Property = Property(name="content", type=StringType)
setup_ResourceCreationTask_targetURL: Property = Property(name="targetURL", type=StringType)
setup_ResourceCreationTask_encoding: Property = Property(name="encoding", type=StringType)
setup_ResourceCreationTask.attributes={setup_ResourceCreationTask_encoding, setup_ResourceCreationTask_targetURL, setup_ResourceCreationTask_content}

# setup_TextModifyTask class attributes and methods
setup_TextModifyTask_uRL: Property = Property(name="uRL", type=StringType)
setup_TextModifyTask_encoding: Property = Property(name="encoding", type=StringType)
setup_TextModifyTask.attributes={setup_TextModifyTask_uRL, setup_TextModifyTask_encoding}

# setup_EclipsePreferenceTask class attributes and methods
setup_EclipsePreferenceTask_key: Property = Property(name="key", type=StringType)
setup_EclipsePreferenceTask_value: Property = Property(name="value", type=StringType)
setup_EclipsePreferenceTask.attributes={setup_EclipsePreferenceTask_key, setup_EclipsePreferenceTask_value}

# setup_FileAssociationTask class attributes and methods
setup_FileAssociationTask_filePattern: Property = Property(name="filePattern", type=StringType)
setup_FileAssociationTask_defaultEditorID: Property = Property(name="defaultEditorID", type=StringType)
setup_FileAssociationTask.attributes={setup_FileAssociationTask_filePattern, setup_FileAssociationTask_defaultEditorID}

# setup_FileEditor class attributes and methods
setup_FileEditor_iD: Property = Property(name="iD", type=StringType)
setup_FileEditor.attributes={setup_FileEditor_iD}

# setup_KeyBindingContext class attributes and methods
setup_KeyBindingContext_iD: Property = Property(name="iD", type=StringType)
setup_KeyBindingContext.attributes={setup_KeyBindingContext_iD}

# setup_CommandParameter class attributes and methods
setup_CommandParameter_iD: Property = Property(name="iD", type=StringType)
setup_CommandParameter_value: Property = Property(name="value", type=StringType)
setup_CommandParameter.attributes={setup_CommandParameter_iD, setup_CommandParameter_value}

# setup_MylynQueryTask class attributes and methods
setup_MylynQueryTask_connectorKind: Property = Property(name="connectorKind", type=StringType)
setup_MylynQueryTask_summary: Property = Property(name="summary", type=StringType)
setup_MylynQueryTask_repositoryURL: Property = Property(name="repositoryURL", type=StringType)
setup_MylynQueryTask_relativeURL: Property = Property(name="relativeURL", type=StringType)
setup_MylynQueryTask.attributes={setup_MylynQueryTask_relativeURL, setup_MylynQueryTask_repositoryURL, setup_MylynQueryTask_summary, setup_MylynQueryTask_connectorKind}

# setup_MylynQueriesTask class attributes and methods
setup_MylynQueriesTask_connectorKind: Property = Property(name="connectorKind", type=StringType)
setup_MylynQueriesTask_repositoryURL: Property = Property(name="repositoryURL", type=StringType)
setup_MylynQueriesTask_userID: Property = Property(name="userID", type=StringType)
setup_MylynQueriesTask_password: Property = Property(name="password", type=StringType)
setup_MylynQueriesTask.attributes={setup_MylynQueriesTask_userID, setup_MylynQueriesTask_connectorKind, setup_MylynQueriesTask_repositoryURL, setup_MylynQueriesTask_password}

# setup_TextModification class attributes and methods
setup_TextModification_pattern: Property = Property(name="pattern", type=StringType)
setup_TextModification_substitutions: Property = Property(name="substitutions", type=StringType)
setup_TextModification.attributes={setup_TextModification_pattern, setup_TextModification_substitutions}

# setup_KeyBindingTask class attributes and methods
setup_KeyBindingTask_platform: Property = Property(name="platform", type=StringType)
setup_KeyBindingTask_locale: Property = Property(name="locale", type=StringType)
setup_KeyBindingTask_keys: Property = Property(name="keys", type=StringType)
setup_KeyBindingTask_command: Property = Property(name="command", type=StringType)
setup_KeyBindingTask_scheme: Property = Property(name="scheme", type=StringType)
setup_KeyBindingTask.attributes={setup_KeyBindingTask_keys, setup_KeyBindingTask_locale, setup_KeyBindingTask_command, setup_KeyBindingTask_scheme, setup_KeyBindingTask_platform}

# setup_QueryAttribute class attributes and methods
setup_QueryAttribute_key: Property = Property(name="key", type=StringType)
setup_QueryAttribute_value: Property = Property(name="value", type=StringType)
setup_QueryAttribute.attributes={setup_QueryAttribute_key, setup_QueryAttribute_value}

# setup_MylynBuildsTask class attributes and methods
setup_MylynBuildsTask_connectorKind: Property = Property(name="connectorKind", type=StringType)
setup_MylynBuildsTask_serverURL: Property = Property(name="serverURL", type=StringType)
setup_MylynBuildsTask_userID: Property = Property(name="userID", type=StringType)
setup_MylynBuildsTask_password: Property = Property(name="password", type=StringType)
setup_MylynBuildsTask.attributes={setup_MylynBuildsTask_connectorKind, setup_MylynBuildsTask_userID, setup_MylynBuildsTask_serverURL, setup_MylynBuildsTask_password}

# setup_BuildPlan class attributes and methods
setup_BuildPlan_name: Property = Property(name="name", type=StringType)
setup_BuildPlan.attributes={setup_BuildPlan_name}

# setup_JRETask class attributes and methods
setup_JRETask_version: Property = Property(name="version", type=StringType)
setup_JRETask_location: Property = Property(name="location", type=StringType)
setup_JRETask.attributes={setup_JRETask_location, setup_JRETask_version}

# setup_Query class attributes and methods
setup_Query_summary: Property = Property(name="summary", type=StringType)
setup_Query_uRL: Property = Property(name="uRL", type=StringType)
setup_Query.attributes={setup_Query_uRL, setup_Query_summary}

# Relationships
indexes0: BinaryAssociation = BinaryAssociation(
    name="indexes0",
    ends={
        Property(name="setup_Index", type=setup_MetaIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_MetaIndex", type=setup_Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eclipseVersions2: BinaryAssociation = BinaryAssociation(
    name="eclipseVersions2",
    ends={
        Property(name="Eclipse", type=setup_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="configuration", type=setup_Eclipse, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
projects3: BinaryAssociation = BinaryAssociation(
    name="projects3",
    ends={
        Property(name="Project", type=setup_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="configuration4", type=setup_Project, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
configuration5: BinaryAssociation = BinaryAssociation(
    name="configuration5",
    ends={
        Property(name="Configuration6", type=setup_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="projects", type=setup_Configuration, multiplicity=Multiplicity(0, 1))
    }
)
branches7: BinaryAssociation = BinaryAssociation(
    name="branches7",
    ends={
        Property(name="Branch", type=setup_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="project", type=setup_Branch, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
restrictions8: BinaryAssociation = BinaryAssociation(
    name="restrictions8",
    ends={
        Property(name="setup_Eclipse", type=setup_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_Project", type=setup_Eclipse, multiplicity=Multiplicity(0, 9999))
    }
)
configuration1: BinaryAssociation = BinaryAssociation(
    name="configuration1",
    ends={
        Property(name="Configuration", type=setup_Eclipse, multiplicity=Multiplicity(1, 1)),
        Property(name="eclipseVersions", type=setup_Configuration, multiplicity=Multiplicity(0, 1))
    }
)
branch13: BinaryAssociation = BinaryAssociation(
    name="branch13",
    ends={
        Property(name="setup_Branch14", type=setup_Setup, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_Setup", type=setup_Branch, multiplicity=Multiplicity(1, 1))
    }
)
eclipseVersion15: BinaryAssociation = BinaryAssociation(
    name="eclipseVersion15",
    ends={
        Property(name="setup_Eclipse17", type=setup_Setup, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_Setup16", type=setup_Eclipse, multiplicity=Multiplicity(1, 1))
    }
)
requirements19: BinaryAssociation = BinaryAssociation(
    name="requirements19",
    ends={
        Property(name="setup_SetupTask", type=setup_SetupTask, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_SetupTask18", type=setup_SetupTask, multiplicity=Multiplicity(0, 9999))
    }
)
restrictions20: BinaryAssociation = BinaryAssociation(
    name="restrictions20",
    ends={
        Property(name="setup_ConfigurableItem", type=setup_SetupTask, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_SetupTask21", type=setup_ConfigurableItem, multiplicity=Multiplicity(0, 9999))
    }
)
project9: BinaryAssociation = BinaryAssociation(
    name="project9",
    ends={
        Property(name="Project10", type=setup_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branches", type=setup_Project, multiplicity=Multiplicity(0, 1))
    }
)
restrictions11: BinaryAssociation = BinaryAssociation(
    name="restrictions11",
    ends={
        Property(name="setup_Eclipse12", type=setup_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_Branch", type=setup_Eclipse, multiplicity=Multiplicity(0, 9999))
    }
)
choices24: BinaryAssociation = BinaryAssociation(
    name="choices24",
    ends={
        Property(name="setup_VariableChoice", type=setup_ContextVariableTask, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_ContextVariableTask", type=setup_VariableChoice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
setupTasks22: BinaryAssociation = BinaryAssociation(
    name="setupTasks22",
    ends={
        Property(name="setup_SetupTask23", type=setup_SetupTaskContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_SetupTaskContainer", type=setup_SetupTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
installableUnits25: BinaryAssociation = BinaryAssociation(
    name="installableUnits25",
    ends={
        Property(name="setup_InstallableUnit", type=setup_P2Task, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_P2Task", type=setup_InstallableUnit, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
p2Repositories26: BinaryAssociation = BinaryAssociation(
    name="p2Repositories26",
    ends={
        Property(name="setup_P2Repository", type=setup_P2Task, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_P2Task27", type=setup_P2Repository, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sourceLocators29: BinaryAssociation = BinaryAssociation(
    name="sourceLocators29",
    ends={
        Property(name="setup_SourceLocator", type=setup_MaterializationTask, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_MaterializationTask30", type=setup_SourceLocator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
p2Repositories31: BinaryAssociation = BinaryAssociation(
    name="p2Repositories31",
    ends={
        Property(name="setup_P2Repository33", type=setup_MaterializationTask, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_MaterializationTask32", type=setup_P2Repository, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predicates34: BinaryAssociation = BinaryAssociation(
    name="predicates34",
    ends={
        Property(name="setup_Predicate", type=setup_AutomaticSourceLocator, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_AutomaticSourceLocator", type=setup_Predicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencies35: BinaryAssociation = BinaryAssociation(
    name="dependencies35",
    ends={
        Property(name="setup_InstallableUnit36", type=setup_ComponentExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_ComponentExtension", type=setup_InstallableUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootComponents28: BinaryAssociation = BinaryAssociation(
    name="rootComponents28",
    ends={
        Property(name="setup_Component", type=setup_MaterializationTask, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_MaterializationTask", type=setup_Component, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sourceLocators37: BinaryAssociation = BinaryAssociation(
    name="sourceLocators37",
    ends={
        Property(name="setup_AutomaticSourceLocator38", type=setup_MavenImportTask, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_MavenImportTask", type=setup_AutomaticSourceLocator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sourceLocators41: BinaryAssociation = BinaryAssociation(
    name="sourceLocators41",
    ends={
        Property(name="setup_TargletData42", type=setup_AutomaticSourceLocator, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="setup_AutomaticSourceLocator43", type=setup_TargletData, multiplicity=Multiplicity(1, 1))
    }
)
repositoryLists44: BinaryAssociation = BinaryAssociation(
    name="repositoryLists44",
    ends={
        Property(name="setup_RepositoryList", type=setup_TargletData, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_TargletData45", type=setup_RepositoryList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activeP2Repositories46: BinaryAssociation = BinaryAssociation(
    name="activeP2Repositories46",
    ends={
        Property(name="setup_P2Repository48", type=setup_TargletData, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_TargletData47", type=setup_P2Repository, multiplicity=Multiplicity(0, 9999))
    }
)
p2Repositories49: BinaryAssociation = BinaryAssociation(
    name="p2Repositories49",
    ends={
        Property(name="setup_P2Repository51", type=setup_RepositoryList, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_RepositoryList50", type=setup_P2Repository, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceLocators52: BinaryAssociation = BinaryAssociation(
    name="sourceLocators52",
    ends={
        Property(name="setup_AutomaticSourceLocator53", type=setup_ProjectsImportTask, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_ProjectsImportTask", type=setup_AutomaticSourceLocator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
roots39: BinaryAssociation = BinaryAssociation(
    name="roots39",
    ends={
        Property(name="setup_InstallableUnit40", type=setup_TargletData, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_TargletData", type=setup_InstallableUnit, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
editors54: BinaryAssociation = BinaryAssociation(
    name="editors54",
    ends={
        Property(name="setup_FileAssociationTask", type=setup_FileEditor, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="setup_FileEditor", type=setup_FileAssociationTask, multiplicity=Multiplicity(1, 1))
    }
)
mappings55: BinaryAssociation = BinaryAssociation(
    name="mappings55",
    ends={
        Property(name="setup_FileMapping", type=setup_FileAssociationsTask, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_FileAssociationsTask", type=setup_FileMapping, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
editors56: BinaryAssociation = BinaryAssociation(
    name="editors56",
    ends={
        Property(name="setup_FileEditor58", type=setup_FileMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_FileMapping57", type=setup_FileEditor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
workingSets59: BinaryAssociation = BinaryAssociation(
    name="workingSets59",
    ends={
        Property(name="setup_WorkingSet", type=setup_WorkingSetTask, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_WorkingSetTask", type=setup_WorkingSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contexts61: BinaryAssociation = BinaryAssociation(
    name="contexts61",
    ends={
        Property(name="setup_KeyBindingContext", type=setup_KeyBindingTask, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_KeyBindingTask", type=setup_KeyBindingContext, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
commandParameters62: BinaryAssociation = BinaryAssociation(
    name="commandParameters62",
    ends={
        Property(name="setup_CommandParameter", type=setup_KeyBindingTask, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_KeyBindingTask63", type=setup_CommandParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifications60: BinaryAssociation = BinaryAssociation(
    name="modifications60",
    ends={
        Property(name="setup_TextModification", type=setup_TextModifyTask, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_TextModifyTask", type=setup_TextModification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task65: BinaryAssociation = BinaryAssociation(
    name="task65",
    ends={
        Property(name="MylynQueriesTask", type=setup_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="queries", type=setup_MylynQueriesTask, multiplicity=Multiplicity(0, 1))
    }
)
attributes66: BinaryAssociation = BinaryAssociation(
    name="attributes66",
    ends={
        Property(name="setup_QueryAttribute", type=setup_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_Query", type=setup_QueryAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
buildPlans67: BinaryAssociation = BinaryAssociation(
    name="buildPlans67",
    ends={
        Property(name="setup_BuildPlan", type=setup_MylynBuildsTask, multiplicity=Multiplicity(1, 1)),
        Property(name="setup_MylynBuildsTask", type=setup_BuildPlan, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
queries64: BinaryAssociation = BinaryAssociation(
    name="queries64",
    ends={
        Property(name="Query", type=setup_MylynQueriesTask, multiplicity=Multiplicity(1, 1)),
        Property(name="task", type=setup_Query, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_setup_Configuration_ScopeRoot = Generalization(general=ScopeRoot, specific=setup_Configuration)
gen_setup_ConfigurableItem_ScopeRoot = Generalization(general=ScopeRoot, specific=setup_ConfigurableItem)
gen_setup_Project_ConfigurableItem = Generalization(general=ConfigurableItem, specific=setup_Project)
gen_setup_Eclipse_ConfigurableItem = Generalization(general=ConfigurableItem, specific=setup_Eclipse)
gen_setup_Preferences_ScopeRoot = Generalization(general=ScopeRoot, specific=setup_Preferences)
gen_setup_Branch_ConfigurableItem = Generalization(general=ConfigurableItem, specific=setup_Branch)
gen_setup_CompoundSetupTask_SetupTaskContainer = Generalization(general=SetupTaskContainer, specific=setup_CompoundSetupTask)
gen_setup_ContextVariableTask_SetupTask = Generalization(general=SetupTask, specific=setup_ContextVariableTask)
gen_setup_RedirectionTask_SetupTask = Generalization(general=SetupTask, specific=setup_RedirectionTask)
gen_setup_EclipseIniTask_SetupTask = Generalization(general=SetupTask, specific=setup_EclipseIniTask)
gen_setup_LinkLocationTask_SetupTask = Generalization(general=SetupTask, specific=setup_LinkLocationTask)
gen_setup_ScopeRoot_SetupTaskContainer = Generalization(general=SetupTaskContainer, specific=setup_ScopeRoot)
gen_setup_CompoundSetupTask_SetupTask = Generalization(general=SetupTask, specific=setup_CompoundSetupTask)
gen_setup_GitCloneTask_SetupTask = Generalization(general=SetupTask, specific=setup_GitCloneTask)
gen_setup_BasicMaterializationTask_SetupTask = Generalization(general=SetupTask, specific=setup_BasicMaterializationTask)
gen_setup_BuckminsterImportTask_BasicMaterializationTask = Generalization(general=BasicMaterializationTask, specific=setup_BuckminsterImportTask)
gen_setup_P2Task_SetupTask = Generalization(general=SetupTask, specific=setup_P2Task)
gen_setup_ManualSourceLocator_SourceLocator = Generalization(general=SourceLocator, specific=setup_ManualSourceLocator)
gen_setup_AutomaticSourceLocator_SourceLocator = Generalization(general=SourceLocator, specific=setup_AutomaticSourceLocator)
gen_setup_MaterializationTask_BasicMaterializationTask = Generalization(general=BasicMaterializationTask, specific=setup_MaterializationTask)
gen_setup_MavenImportTask_SetupTask = Generalization(general=SetupTask, specific=setup_MavenImportTask)
gen_setup_TargletImportTask_SetupTask = Generalization(general=SetupTask, specific=setup_TargletImportTask)
gen_setup_TargletTask_SetupTask = Generalization(general=SetupTask, specific=setup_TargletTask)
gen_setup_ComponentDefinition_ComponentExtension = Generalization(general=ComponentExtension, specific=setup_ComponentDefinition)
gen_setup_ProjectsImportTask_SetupTask = Generalization(general=SetupTask, specific=setup_ProjectsImportTask)
gen_setup_ProjectSetImportTask_SetupTask = Generalization(general=SetupTask, specific=setup_ProjectSetImportTask)
gen_setup_TargetPlatformTask_SetupTask = Generalization(general=SetupTask, specific=setup_TargetPlatformTask)
gen_setup_ApiBaselineTask_SetupTask = Generalization(general=SetupTask, specific=setup_ApiBaselineTask)
gen_setup_TargletTask_TargletData = Generalization(general=TargletData, specific=setup_TargletTask)
gen_setup_Targlet_TargletData = Generalization(general=TargletData, specific=setup_Targlet)
gen_setup_FileAssociationsTask_SetupTask = Generalization(general=SetupTask, specific=setup_FileAssociationsTask)
gen_setup_WorkingSetTask_SetupTask = Generalization(general=SetupTask, specific=setup_WorkingSetTask)
gen_setup_ResourceCopyTask_SetupTask = Generalization(general=SetupTask, specific=setup_ResourceCopyTask)
gen_setup_ResourceCreationTask_SetupTask = Generalization(general=SetupTask, specific=setup_ResourceCreationTask)
gen_setup_TextModifyTask_SetupTask = Generalization(general=SetupTask, specific=setup_TextModifyTask)
gen_setup_EclipsePreferenceTask_SetupTask = Generalization(general=SetupTask, specific=setup_EclipsePreferenceTask)
gen_setup_FileAssociationTask_SetupTask = Generalization(general=SetupTask, specific=setup_FileAssociationTask)
gen_setup_MylynQueryTask_SetupTask = Generalization(general=SetupTask, specific=setup_MylynQueryTask)
gen_setup_MylynQueriesTask_SetupTask = Generalization(general=SetupTask, specific=setup_MylynQueriesTask)
gen_setup_KeyBindingTask_SetupTask = Generalization(general=SetupTask, specific=setup_KeyBindingTask)
gen_setup_MylynBuildsTask_SetupTask = Generalization(general=SetupTask, specific=setup_MylynBuildsTask)
gen_setup_JRETask_SetupTask = Generalization(general=SetupTask, specific=setup_JRETask)

# Domain Model
domain_model = DomainModel(
    name="setup",
    types={setup_MetaIndex, setup_Index, ScopeRoot, setup_Project, setup_ConfigurableItem, setup_Branch, setup_Eclipse, ConfigurableItem, setup_Configuration, setup_Setup, setup_SetupTask, setup_Preferences, setup_ContextVariableTask, setup_VariableChoice, setup_RedirectionTask, setup_EclipseIniTask, setup_LinkLocationTask, setup_SetupTaskContainer, setup_ScopeRoot, SetupTaskContainer, setup_CompoundSetupTask, SetupTask, setup_GitCloneTask, setup_BasicMaterializationTask, setup_BuckminsterImportTask, BasicMaterializationTask, setup_P2Task, setup_InstallableUnit, setup_P2Repository, setup_SourceLocator, setup_ManualSourceLocator, SourceLocator, setup_AutomaticSourceLocator, setup_Predicate, setup_ComponentExtension, setup_MaterializationTask, setup_Component, setup_MavenImportTask, setup_TargletImportTask, setup_TargletTask, setup_ComponentDefinition, ComponentExtension, setup_RepositoryList, setup_ProjectsImportTask, setup_ProjectSetImportTask, setup_TargetPlatformTask, setup_ApiBaselineTask, TargletData, setup_Targlet, setup_TargletData, setup_FileAssociationsTask, setup_FileMapping, setup_WorkingSetTask, setup_WorkingSet, setup_ResourceCopyTask, setup_ResourceCreationTask, setup_TextModifyTask, setup_EclipsePreferenceTask, setup_FileAssociationTask, setup_FileEditor, setup_KeyBindingContext, setup_CommandParameter, setup_MylynQueryTask, setup_MylynQueriesTask, setup_TextModification, setup_KeyBindingTask, setup_QueryAttribute, setup_MylynBuildsTask, setup_BuildPlan, setup_JRETask, setup_Query, SetupTaskScope, VariableType, Trigger, ComponentType},
    associations={indexes0, eclipseVersions2, projects3, configuration5, branches7, restrictions8, configuration1, branch13, eclipseVersion15, requirements19, restrictions20, project9, restrictions11, choices24, setupTasks22, installableUnits25, p2Repositories26, sourceLocators29, p2Repositories31, predicates34, dependencies35, rootComponents28, sourceLocators37, sourceLocators41, repositoryLists44, activeP2Repositories46, p2Repositories49, sourceLocators52, roots39, editors54, mappings55, editors56, workingSets59, contexts61, commandParameters62, modifications60, task65, attributes66, buildPlans67, queries64},
    generalizations={gen_setup_Configuration_ScopeRoot, gen_setup_ConfigurableItem_ScopeRoot, gen_setup_Project_ConfigurableItem, gen_setup_Eclipse_ConfigurableItem, gen_setup_Preferences_ScopeRoot, gen_setup_Branch_ConfigurableItem, gen_setup_CompoundSetupTask_SetupTaskContainer, gen_setup_ContextVariableTask_SetupTask, gen_setup_RedirectionTask_SetupTask, gen_setup_EclipseIniTask_SetupTask, gen_setup_LinkLocationTask_SetupTask, gen_setup_ScopeRoot_SetupTaskContainer, gen_setup_CompoundSetupTask_SetupTask, gen_setup_GitCloneTask_SetupTask, gen_setup_BasicMaterializationTask_SetupTask, gen_setup_BuckminsterImportTask_BasicMaterializationTask, gen_setup_P2Task_SetupTask, gen_setup_ManualSourceLocator_SourceLocator, gen_setup_AutomaticSourceLocator_SourceLocator, gen_setup_MaterializationTask_BasicMaterializationTask, gen_setup_MavenImportTask_SetupTask, gen_setup_TargletImportTask_SetupTask, gen_setup_TargletTask_SetupTask, gen_setup_ComponentDefinition_ComponentExtension, gen_setup_ProjectsImportTask_SetupTask, gen_setup_ProjectSetImportTask_SetupTask, gen_setup_TargetPlatformTask_SetupTask, gen_setup_ApiBaselineTask_SetupTask, gen_setup_TargletTask_TargletData, gen_setup_Targlet_TargletData, gen_setup_FileAssociationsTask_SetupTask, gen_setup_WorkingSetTask_SetupTask, gen_setup_ResourceCopyTask_SetupTask, gen_setup_ResourceCreationTask_SetupTask, gen_setup_TextModifyTask_SetupTask, gen_setup_EclipsePreferenceTask_SetupTask, gen_setup_FileAssociationTask_SetupTask, gen_setup_MylynQueryTask_SetupTask, gen_setup_MylynQueriesTask_SetupTask, gen_setup_KeyBindingTask_SetupTask, gen_setup_MylynBuildsTask_SetupTask, gen_setup_JRETask_SetupTask},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
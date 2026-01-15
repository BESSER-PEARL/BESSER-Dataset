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

# Classes
p2_Copyright = Class(name="p2::Copyright")
ICopyright = Class(name="ICopyright")
p2_IAdaptable = Class(name="p2::IAdaptable", is_abstract=True)
p2_ArtifactKey = Class(name="p2::ArtifactKey")
IArtifactKey = Class(name="IArtifactKey")
p2_ArtifactDescriptor = Class(name="p2::ArtifactDescriptor")
IArtifactDescriptor = Class(name="IArtifactDescriptor")
p2_Property = Class(name="p2::Property")
p2_IProcessingStepDescriptor = Class(name="p2::IProcessingStepDescriptor", is_abstract=True)
p2_ArtifactRepository = Class(name="p2::ArtifactRepository")
p2_ArtifactsByKey = Class(name="p2::ArtifactsByKey")
p2_IArtifactKey = Class(name="p2::IArtifactKey", is_abstract=True)
p2_IArtifactDescriptor = Class(name="p2::IArtifactDescriptor", is_abstract=True)
p2_Comparable = Class(name="p2::Comparable", is_abstract=True)
p2_IArtifactRepository = Class(name="p2::IArtifactRepository", is_abstract=True)
p2_ICopyright = Class(name="p2::ICopyright", is_abstract=True)
p2_IInstallableUnitFragment = Class(name="p2::IInstallableUnitFragment", is_abstract=True)
p2_ILicense = Class(name="p2::ILicense", is_abstract=True)
p2_IRequirement = Class(name="p2::IRequirement", is_abstract=True)
p2_IFileArtifactRepository = Class(name="p2::IFileArtifactRepository", is_abstract=True)
IArtifactRepository = Class(name="IArtifactRepository")
p2_IInstallableUnit = Class(name="p2::IInstallableUnit", is_abstract=True)
p2_InstallableUnit = Class(name="p2::InstallableUnit")
p2_InstallableUnitFragment = Class(name="p2::InstallableUnitFragment")
InstallableUnit = Class(name="InstallableUnit")
IInstallableUnitFragment = Class(name="IInstallableUnitFragment")
p2_IProvidedCapability = Class(name="p2::IProvidedCapability", is_abstract=True)
p2_ITouchpointData = Class(name="p2::ITouchpointData", is_abstract=True)
p2_ITouchpointType = Class(name="p2::ITouchpointType", is_abstract=True)
p2_IUpdateDescriptor = Class(name="p2::IUpdateDescriptor", is_abstract=True)
IInstallableUnit = Class(name="IInstallableUnit")
p2_IInstallableUnitPatch = Class(name="p2::IInstallableUnitPatch", is_abstract=True)
p2_IRequirementChange = Class(name="p2::IRequirementChange", is_abstract=True)
p2_IQueryable = Class(name="p2::IQueryable", is_abstract=True)
p2_InstallableUnitPatch = Class(name="p2::InstallableUnitPatch")
IInstallableUnitPatch = Class(name="IInstallableUnitPatch")
p2_IRepository = Class(name="p2::IRepository", is_abstract=True)
p2_InstructionMap = Class(name="p2::InstructionMap")
p2_ITouchpointInstruction = Class(name="p2::ITouchpointInstruction", is_abstract=True)
p2_IMetadataRepository = Class(name="p2::IMetadataRepository", is_abstract=True)
p2_IRequiredCapability = Class(name="p2::IRequiredCapability", is_abstract=True)
IRequirement = Class(name="IRequirement")
p2_IRepositoryReference = Class(name="p2::IRepositoryReference", is_abstract=True)
p2_IVersionedId = Class(name="p2::IVersionedId", is_abstract=True)
p2_License = Class(name="p2::License")
ILicense = Class(name="ILicense")
p2_MappingRule = Class(name="p2::MappingRule")
p2_MetadataRepository = Class(name="p2::MetadataRepository")
p2_RequiredCapability = Class(name="p2::RequiredCapability")
Requirement = Class(name="Requirement")
IRequiredCapability = Class(name="IRequiredCapability")
p2_Requirement = Class(name="p2::Requirement")
p2_RequirementChange = Class(name="p2::RequirementChange")
IRequirementChange = Class(name="IRequirementChange")
p2_SimpleArtifactRepository = Class(name="p2::SimpleArtifactRepository")
ArtifactRepository = Class(name="ArtifactRepository")
IFileArtifactRepository = Class(name="IFileArtifactRepository")
p2_SimpleArtifactDescriptor = Class(name="p2::SimpleArtifactDescriptor")
ArtifactDescriptor = Class(name="ArtifactDescriptor")
p2_ProcessingStepDescriptor = Class(name="p2::ProcessingStepDescriptor")
IProcessingStepDescriptor = Class(name="IProcessingStepDescriptor")
p2_ProvidedCapability = Class(name="p2::ProvidedCapability")
IProvidedCapability = Class(name="IProvidedCapability")
p2_Repository = Class(name="p2::Repository", is_abstract=True)
p2_RepositoryReference = Class(name="p2::RepositoryReference")
IRepositoryReference = Class(name="IRepositoryReference")
p2_TouchpointData = Class(name="p2::TouchpointData")
ITouchpointData = Class(name="ITouchpointData")
p2_TouchpointInstruction = Class(name="p2::TouchpointInstruction")
ITouchpointInstruction = Class(name="ITouchpointInstruction")
p2_TouchpointType = Class(name="p2::TouchpointType")
ITouchpointType = Class(name="ITouchpointType")
p2_UpdateDescriptor = Class(name="p2::UpdateDescriptor")
IUpdateDescriptor = Class(name="IUpdateDescriptor")

# p2_Copyright class attributes and methods

# ICopyright class attributes and methods

# p2_IAdaptable class attributes and methods
p2_IAdaptable_m_getAdapter: Method = Method(name="getAdapter", parameters={Parameter(name='adapter')}, type=StringType)
p2_IAdaptable.methods={p2_IAdaptable_m_getAdapter}

# p2_ArtifactKey class attributes and methods

# IArtifactKey class attributes and methods

# p2_ArtifactDescriptor class attributes and methods

# IArtifactDescriptor class attributes and methods

# p2_Property class attributes and methods
p2_Property_key: Property = Property(name="key", type=StringType)
p2_Property_value: Property = Property(name="value", type=StringType)
p2_Property.attributes={p2_Property_value, p2_Property_key}

# p2_IProcessingStepDescriptor class attributes and methods
p2_IProcessingStepDescriptor_processorId: Property = Property(name="processorId", type=StringType)
p2_IProcessingStepDescriptor_data: Property = Property(name="data", type=StringType)
p2_IProcessingStepDescriptor_required: Property = Property(name="required", type=BooleanType)
p2_IProcessingStepDescriptor.attributes={p2_IProcessingStepDescriptor_data, p2_IProcessingStepDescriptor_required, p2_IProcessingStepDescriptor_processorId}

# p2_ArtifactRepository class attributes and methods

# p2_ArtifactsByKey class attributes and methods

# p2_IArtifactKey class attributes and methods
p2_IArtifactKey_classifier: Property = Property(name="classifier", type=StringType)
p2_IArtifactKey_id: Property = Property(name="id", type=StringType)
p2_IArtifactKey_version: Property = Property(name="version", type=StringType)
p2_IArtifactKey_m_toExternalForm: Method = Method(name="toExternalForm", parameters={}, type=StringType)
p2_IArtifactKey.attributes={p2_IArtifactKey_id, p2_IArtifactKey_classifier, p2_IArtifactKey_version}
p2_IArtifactKey.methods={p2_IArtifactKey_m_toExternalForm}

# p2_IArtifactDescriptor class attributes and methods
p2_IArtifactDescriptor_m_getProperties: Method = Method(name="getProperties", parameters={})
p2_IArtifactDescriptor_m_getProperty: Method = Method(name="getProperty", parameters={Parameter(name='key')}, type=StringType)
p2_IArtifactDescriptor_m_getProcessingSteps: Method = Method(name="getProcessingSteps", parameters={}, type=StringType)
p2_IArtifactDescriptor_m_getRepository: Method = Method(name="getRepository", parameters={}, type=StringType)
p2_IArtifactDescriptor.methods={p2_IArtifactDescriptor_m_getProcessingSteps, p2_IArtifactDescriptor_m_getProperties, p2_IArtifactDescriptor_m_getRepository, p2_IArtifactDescriptor_m_getProperty}

# p2_Comparable class attributes and methods
p2_Comparable_m_compareTo: Method = Method(name="compareTo", parameters={Parameter(name='o')}, type=IntegerType)
p2_Comparable.methods={p2_Comparable_m_compareTo}

# p2_IArtifactRepository class attributes and methods
p2_IArtifactRepository_m_addDescriptors: Method = Method(name="addDescriptors", parameters={Parameter(name='monitor'), Parameter(name='descriptors')})
p2_IArtifactRepository_m_contains: Method = Method(name="contains", parameters={Parameter(name='descriptor')}, type=BooleanType)
p2_IArtifactRepository_m_contains: Method = Method(name="contains", parameters={Parameter(name='key')}, type=BooleanType)
p2_IArtifactRepository_m_getArtifact: Method = Method(name="getArtifact", parameters={Parameter(name='monitor'), Parameter(name='destination'), Parameter(name='descriptor')}, type=StringType)
p2_IArtifactRepository_m_createArtifactDescriptor: Method = Method(name="createArtifactDescriptor", parameters={Parameter(name='key')}, type=IArtifactDescriptor)
p2_IArtifactRepository_m_createArtifactKey: Method = Method(name="createArtifactKey", parameters={Parameter(name='version'), Parameter(name='id'), Parameter(name='classifier')}, type=IArtifactKey)
p2_IArtifactRepository_m_addDescriptor: Method = Method(name="addDescriptor", parameters={Parameter(name='descriptor')})
p2_IArtifactRepository_m_addDescriptor: Method = Method(name="addDescriptor", parameters={Parameter(name='descriptor'), Parameter(name='monitor')})
p2_IArtifactRepository_m_addDescriptors: Method = Method(name="addDescriptors", parameters={Parameter(name='descriptors')})
p2_IArtifactRepository_m_removeDescriptors: Method = Method(name="removeDescriptors", parameters={Parameter(name='keys')})
p2_IArtifactRepository_m_removeDescriptors: Method = Method(name="removeDescriptors", parameters={Parameter(name='keys'), Parameter(name='monitor')})
p2_IArtifactRepository_m_executeBatch: Method = Method(name="executeBatch", parameters={Parameter(name='monitor'), Parameter(name='runnable')}, type=StringType)
p2_IArtifactRepository_m_getRawArtifact: Method = Method(name="getRawArtifact", parameters={Parameter(name='monitor'), Parameter(name='descriptor'), Parameter(name='destination')}, type=StringType)
p2_IArtifactRepository_m_getArtifactDescriptors: Method = Method(name="getArtifactDescriptors", parameters={Parameter(name='key')}, type=StringType)
p2_IArtifactRepository_m_getArtifacts: Method = Method(name="getArtifacts", parameters={Parameter(name='requests'), Parameter(name='monitor')}, type=StringType)
p2_IArtifactRepository_m_getOutputStream: Method = Method(name="getOutputStream", parameters={Parameter(name='descriptor')}, type=StringType)
p2_IArtifactRepository_m_descriptorQueryable: Method = Method(name="descriptorQueryable", parameters={})
p2_IArtifactRepository_m_removeAll: Method = Method(name="removeAll", parameters={})
p2_IArtifactRepository_m_removeAll: Method = Method(name="removeAll", parameters={Parameter(name='monitor')})
p2_IArtifactRepository_m_removeDescriptor: Method = Method(name="removeDescriptor", parameters={Parameter(name='descriptor')})
p2_IArtifactRepository_m_removeDescriptor: Method = Method(name="removeDescriptor", parameters={Parameter(name='monitor'), Parameter(name='descriptor')})
p2_IArtifactRepository_m_removeDescriptor: Method = Method(name="removeDescriptor", parameters={Parameter(name='key')})
p2_IArtifactRepository_m_removeDescriptor: Method = Method(name="removeDescriptor", parameters={Parameter(name='monitor'), Parameter(name='key')})
p2_IArtifactRepository_m_removeDescriptors: Method = Method(name="removeDescriptors", parameters={Parameter(name='descriptors')})
p2_IArtifactRepository_m_removeDescriptors: Method = Method(name="removeDescriptors", parameters={Parameter(name='monitor'), Parameter(name='descriptors')})
p2_IArtifactRepository.methods={p2_IArtifactRepository_m_descriptorQueryable, p2_IArtifactRepository_m_addDescriptor, p2_IArtifactRepository_m_contains, p2_IArtifactRepository_m_getArtifactDescriptors, p2_IArtifactRepository_m_removeAll, p2_IArtifactRepository_m_createArtifactKey, p2_IArtifactRepository_m_removeDescriptor, p2_IArtifactRepository_m_getArtifact, p2_IArtifactRepository_m_executeBatch, p2_IArtifactRepository_m_removeAll, p2_IArtifactRepository_m_getArtifacts, p2_IArtifactRepository_m_addDescriptors, p2_IArtifactRepository_m_removeDescriptors, p2_IArtifactRepository_m_removeDescriptor, p2_IArtifactRepository_m_removeDescriptors, p2_IArtifactRepository_m_removeDescriptor, p2_IArtifactRepository_m_createArtifactDescriptor, p2_IArtifactRepository_m_addDescriptors, p2_IArtifactRepository_m_removeDescriptor, p2_IArtifactRepository_m_getOutputStream, p2_IArtifactRepository_m_getRawArtifact, p2_IArtifactRepository_m_removeDescriptors, p2_IArtifactRepository_m_removeDescriptors, p2_IArtifactRepository_m_addDescriptor, p2_IArtifactRepository_m_contains}

# p2_ICopyright class attributes and methods
p2_ICopyright_location: Property = Property(name="location", type=StringType)
p2_ICopyright_body: Property = Property(name="body", type=StringType)
p2_ICopyright.attributes={p2_ICopyright_body, p2_ICopyright_location}

# p2_IInstallableUnitFragment class attributes and methods

# p2_ILicense class attributes and methods
p2_ILicense_location: Property = Property(name="location", type=StringType)
p2_ILicense_body: Property = Property(name="body", type=StringType)
p2_ILicense_UUID: Property = Property(name="UUID", type=StringType)
p2_ILicense.attributes={p2_ILicense_body, p2_ILicense_location, p2_ILicense_UUID}

# p2_IRequirement class attributes and methods
p2_IRequirement_filter: Property = Property(name="filter", type=StringType)
p2_IRequirement_max: Property = Property(name="max", type=StringType)
p2_IRequirement_min: Property = Property(name="min", type=StringType)
p2_IRequirement_matches: Property = Property(name="matches", type=StringType)
p2_IRequirement_greedy: Property = Property(name="greedy", type=BooleanType)
p2_IRequirement_description: Property = Property(name="description", type=StringType)
p2_IRequirement_m_isMatch: Method = Method(name="isMatch", parameters={Parameter(name='installableUnit')}, type=BooleanType)
p2_IRequirement.attributes={p2_IRequirement_filter, p2_IRequirement_min, p2_IRequirement_description, p2_IRequirement_matches, p2_IRequirement_max, p2_IRequirement_greedy}
p2_IRequirement.methods={p2_IRequirement_m_isMatch}

# p2_IFileArtifactRepository class attributes and methods
p2_IFileArtifactRepository_m_getArtifactFile: Method = Method(name="getArtifactFile", parameters={Parameter(name='key')}, type=StringType)
p2_IFileArtifactRepository_m_getArtifactFile: Method = Method(name="getArtifactFile", parameters={Parameter(name='descriptor')}, type=StringType)
p2_IFileArtifactRepository.methods={p2_IFileArtifactRepository_m_getArtifactFile, p2_IFileArtifactRepository_m_getArtifactFile}

# IArtifactRepository class attributes and methods

# p2_IInstallableUnit class attributes and methods
p2_IInstallableUnit_filter: Property = Property(name="filter", type=StringType)
p2_IInstallableUnit_resolved: Property = Property(name="resolved", type=BooleanType)
p2_IInstallableUnit_singleton: Property = Property(name="singleton", type=BooleanType)
p2_IInstallableUnit_m_unresolved: Method = Method(name="unresolved", parameters={}, type=StringType)
p2_IInstallableUnit_m_getCopyright: Method = Method(name="getCopyright", parameters={Parameter(name='locale')}, type=ICopyright)
p2_IInstallableUnit_m_getLicenses: Method = Method(name="getLicenses", parameters={Parameter(name='locale')}, type=StringType)
p2_IInstallableUnit_m_getProperties: Method = Method(name="getProperties", parameters={})
p2_IInstallableUnit_m_getProperty: Method = Method(name="getProperty", parameters={Parameter(name='key')}, type=StringType)
p2_IInstallableUnit_m_getProperty: Method = Method(name="getProperty", parameters={Parameter(name='key'), Parameter(name='locale')}, type=StringType)
p2_IInstallableUnit_m_satisfies: Method = Method(name="satisfies", parameters={Parameter(name='candidate')}, type=BooleanType)
p2_IInstallableUnit.attributes={p2_IInstallableUnit_filter, p2_IInstallableUnit_resolved, p2_IInstallableUnit_singleton}
p2_IInstallableUnit.methods={p2_IInstallableUnit_m_unresolved, p2_IInstallableUnit_m_getProperties, p2_IInstallableUnit_m_getLicenses, p2_IInstallableUnit_m_satisfies, p2_IInstallableUnit_m_getCopyright, p2_IInstallableUnit_m_getProperty, p2_IInstallableUnit_m_getProperty}

# p2_InstallableUnit class attributes and methods

# p2_InstallableUnitFragment class attributes and methods

# InstallableUnit class attributes and methods

# IInstallableUnitFragment class attributes and methods

# p2_IProvidedCapability class attributes and methods
p2_IProvidedCapability_name: Property = Property(name="name", type=StringType)
p2_IProvidedCapability_namespace: Property = Property(name="namespace", type=StringType)
p2_IProvidedCapability_version: Property = Property(name="version", type=StringType)
p2_IProvidedCapability.attributes={p2_IProvidedCapability_version, p2_IProvidedCapability_namespace, p2_IProvidedCapability_name}

# p2_ITouchpointData class attributes and methods
p2_ITouchpointData_m_getInstructions: Method = Method(name="getInstructions", parameters={})
p2_ITouchpointData_m_getInstruction: Method = Method(name="getInstruction", parameters={Parameter(name='key')}, type=StringType)
p2_ITouchpointData.methods={p2_ITouchpointData_m_getInstruction, p2_ITouchpointData_m_getInstructions}

# p2_ITouchpointType class attributes and methods
p2_ITouchpointType_id: Property = Property(name="id", type=StringType)
p2_ITouchpointType_version: Property = Property(name="version", type=StringType)
p2_ITouchpointType.attributes={p2_ITouchpointType_version, p2_ITouchpointType_id}

# p2_IUpdateDescriptor class attributes and methods
p2_IUpdateDescriptor_description: Property = Property(name="description", type=StringType)
p2_IUpdateDescriptor_severity: Property = Property(name="severity", type=IntegerType)
p2_IUpdateDescriptor_location: Property = Property(name="location", type=StringType)
p2_IUpdateDescriptor_m_isUpdateOf: Method = Method(name="isUpdateOf", parameters={Parameter(name='installableUnit')}, type=BooleanType)
p2_IUpdateDescriptor_m_getIUsBeingUpdated: Method = Method(name="getIUsBeingUpdated", parameters={})
p2_IUpdateDescriptor.attributes={p2_IUpdateDescriptor_location, p2_IUpdateDescriptor_severity, p2_IUpdateDescriptor_description}
p2_IUpdateDescriptor.methods={p2_IUpdateDescriptor_m_getIUsBeingUpdated, p2_IUpdateDescriptor_m_isUpdateOf}

# IInstallableUnit class attributes and methods

# p2_IInstallableUnitPatch class attributes and methods

# p2_IRequirementChange class attributes and methods
p2_IRequirementChange_m_applyOn: Method = Method(name="applyOn", parameters={}, type=StringType)
p2_IRequirementChange_m_newValue: Method = Method(name="newValue", parameters={}, type=StringType)
p2_IRequirementChange_m_matches: Method = Method(name="matches", parameters={Parameter(name='toMatch')}, type=BooleanType)
p2_IRequirementChange.methods={p2_IRequirementChange_m_matches, p2_IRequirementChange_m_applyOn, p2_IRequirementChange_m_newValue}

# p2_IQueryable class attributes and methods
p2_IQueryable_m_query: Method = Method(name="query", parameters={Parameter(name='progress'), Parameter(name='query')})
p2_IQueryable.methods={p2_IQueryable_m_query}

# p2_InstallableUnitPatch class attributes and methods
p2_InstallableUnitPatch_m_getApplicabilityScope: Method = Method(name="getApplicabilityScope", parameters={}, type=StringType)
p2_InstallableUnitPatch.methods={p2_InstallableUnitPatch_m_getApplicabilityScope}

# IInstallableUnitPatch class attributes and methods

# p2_IRepository class attributes and methods
p2_IRepository_location: Property = Property(name="location", type=StringType)
p2_IRepository_name: Property = Property(name="name", type=StringType)
p2_IRepository_type: Property = Property(name="type", type=StringType)
p2_IRepository_version: Property = Property(name="version", type=StringType)
p2_IRepository_description: Property = Property(name="description", type=StringType)
p2_IRepository_provider: Property = Property(name="provider", type=StringType)
p2_IRepository_modifiable: Property = Property(name="modifiable", type=BooleanType)
p2_IRepository_provisioningAgent: Property = Property(name="provisioningAgent", type=StringType)
p2_IRepository_m_getProperty: Method = Method(name="getProperty", parameters={Parameter(name='key')}, type=StringType)
p2_IRepository_m_getProperties: Method = Method(name="getProperties", parameters={})
p2_IRepository_m_setProperty: Method = Method(name="setProperty", parameters={Parameter(name='key'), Parameter(name='value')}, type=StringType)
p2_IRepository_m_setProperty: Method = Method(name="setProperty", parameters={Parameter(name='key'), Parameter(name='monitor'), Parameter(name='value')}, type=StringType)
p2_IRepository.attributes={p2_IRepository_location, p2_IRepository_provider, p2_IRepository_name, p2_IRepository_description, p2_IRepository_provisioningAgent, p2_IRepository_version, p2_IRepository_type, p2_IRepository_modifiable}
p2_IRepository.methods={p2_IRepository_m_getProperties, p2_IRepository_m_getProperty, p2_IRepository_m_setProperty, p2_IRepository_m_setProperty}

# p2_InstructionMap class attributes and methods
p2_InstructionMap_key: Property = Property(name="key", type=StringType)
p2_InstructionMap.attributes={p2_InstructionMap_key}

# p2_ITouchpointInstruction class attributes and methods
p2_ITouchpointInstruction_body: Property = Property(name="body", type=StringType)
p2_ITouchpointInstruction_importAttribute: Property = Property(name="importAttribute", type=StringType)
p2_ITouchpointInstruction.attributes={p2_ITouchpointInstruction_body, p2_ITouchpointInstruction_importAttribute}

# p2_IMetadataRepository class attributes and methods
p2_IMetadataRepository_m_addInstallableUnits: Method = Method(name="addInstallableUnits", parameters={Parameter(name='installableUnits')})
p2_IMetadataRepository_m_addReferences: Method = Method(name="addReferences", parameters={Parameter(name='references')})
p2_IMetadataRepository_m_removeAll: Method = Method(name="removeAll", parameters={})
p2_IMetadataRepository_m_removeInstallableUnits: Method = Method(name="removeInstallableUnits", parameters={Parameter(name='installableUnits')}, type=BooleanType)
p2_IMetadataRepository_m_executeBatch: Method = Method(name="executeBatch", parameters={Parameter(name='runnable'), Parameter(name='monitor')}, type=StringType)
p2_IMetadataRepository_m_compress: Method = Method(name="compress", parameters={Parameter(name='iuPool')})
p2_IMetadataRepository.methods={p2_IMetadataRepository_m_addInstallableUnits, p2_IMetadataRepository_m_removeInstallableUnits, p2_IMetadataRepository_m_executeBatch, p2_IMetadataRepository_m_addReferences, p2_IMetadataRepository_m_compress, p2_IMetadataRepository_m_removeAll}

# p2_IRequiredCapability class attributes and methods
p2_IRequiredCapability_name: Property = Property(name="name", type=StringType)
p2_IRequiredCapability_namespace: Property = Property(name="namespace", type=StringType)
p2_IRequiredCapability_range: Property = Property(name="range", type=StringType)
p2_IRequiredCapability.attributes={p2_IRequiredCapability_range, p2_IRequiredCapability_namespace, p2_IRequiredCapability_name}

# IRequirement class attributes and methods

# p2_IRepositoryReference class attributes and methods
p2_IRepositoryReference_location: Property = Property(name="location", type=StringType)
p2_IRepositoryReference_type: Property = Property(name="type", type=IntegerType)
p2_IRepositoryReference_options: Property = Property(name="options", type=IntegerType)
p2_IRepositoryReference_nickname: Property = Property(name="nickname", type=StringType)
p2_IRepositoryReference.attributes={p2_IRepositoryReference_type, p2_IRepositoryReference_location, p2_IRepositoryReference_options, p2_IRepositoryReference_nickname}

# p2_IVersionedId class attributes and methods
p2_IVersionedId_id: Property = Property(name="id", type=StringType)
p2_IVersionedId_version: Property = Property(name="version", type=StringType)
p2_IVersionedId.attributes={p2_IVersionedId_id, p2_IVersionedId_version}

# p2_License class attributes and methods

# ILicense class attributes and methods

# p2_MappingRule class attributes and methods
p2_MappingRule_filter: Property = Property(name="filter", type=StringType)
p2_MappingRule_output: Property = Property(name="output", type=StringType)
p2_MappingRule.attributes={p2_MappingRule_filter, p2_MappingRule_output}

# p2_MetadataRepository class attributes and methods

# p2_RequiredCapability class attributes and methods

# Requirement class attributes and methods

# IRequiredCapability class attributes and methods

# p2_Requirement class attributes and methods

# p2_RequirementChange class attributes and methods

# IRequirementChange class attributes and methods

# p2_SimpleArtifactRepository class attributes and methods

# ArtifactRepository class attributes and methods

# IFileArtifactRepository class attributes and methods

# p2_SimpleArtifactDescriptor class attributes and methods
p2_SimpleArtifactDescriptor_m_getRepositoryProperties: Method = Method(name="getRepositoryProperties", parameters={})
p2_SimpleArtifactDescriptor_m_getRepositoryProperty: Method = Method(name="getRepositoryProperty", parameters={Parameter(name='key')}, type=StringType)
p2_SimpleArtifactDescriptor.methods={p2_SimpleArtifactDescriptor_m_getRepositoryProperty, p2_SimpleArtifactDescriptor_m_getRepositoryProperties}

# ArtifactDescriptor class attributes and methods

# p2_ProcessingStepDescriptor class attributes and methods

# IProcessingStepDescriptor class attributes and methods

# p2_ProvidedCapability class attributes and methods

# IProvidedCapability class attributes and methods

# p2_Repository class attributes and methods

# p2_RepositoryReference class attributes and methods

# IRepositoryReference class attributes and methods

# p2_TouchpointData class attributes and methods

# ITouchpointData class attributes and methods

# p2_TouchpointInstruction class attributes and methods

# ITouchpointInstruction class attributes and methods

# p2_TouchpointType class attributes and methods

# ITouchpointType class attributes and methods

# p2_UpdateDescriptor class attributes and methods

# IUpdateDescriptor class attributes and methods

# Relationships
propertyMap0: BinaryAssociation = BinaryAssociation(
    name="propertyMap0",
    ends={
        Property(name="p2_Property", type=p2_ArtifactDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_ArtifactDescriptor", type=p2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processingStepList1: BinaryAssociation = BinaryAssociation(
    name="processingStepList1",
    ends={
        Property(name="p2_IProcessingStepDescriptor", type=p2_ArtifactDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_ArtifactDescriptor2", type=p2_IProcessingStepDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifactMap3: BinaryAssociation = BinaryAssociation(
    name="artifactMap3",
    ends={
        Property(name="p2_ArtifactsByKey", type=p2_ArtifactRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_ArtifactRepository", type=p2_ArtifactsByKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key4: BinaryAssociation = BinaryAssociation(
    name="key4",
    ends={
        Property(name="p2_IArtifactKey", type=p2_ArtifactsByKey, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_ArtifactsByKey5", type=p2_IArtifactKey, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value6: BinaryAssociation = BinaryAssociation(
    name="value6",
    ends={
        Property(name="p2_IArtifactDescriptor", type=p2_ArtifactsByKey, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_ArtifactsByKey7", type=p2_IArtifactDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifactKey8: BinaryAssociation = BinaryAssociation(
    name="artifactKey8",
    ends={
        Property(name="p2_IArtifactKey10", type=p2_IArtifactDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_IArtifactDescriptor9", type=p2_IArtifactKey, multiplicity=Multiplicity(1, 1))
    }
)
copyright13: BinaryAssociation = BinaryAssociation(
    name="copyright13",
    ends={
        Property(name="p2_ICopyright", type=p2_IInstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_IInstallableUnit14", type=p2_ICopyright, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragments15: BinaryAssociation = BinaryAssociation(
    name="fragments15",
    ends={
        Property(name="p2_IInstallableUnitFragment", type=p2_IInstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_IInstallableUnit16", type=p2_IInstallableUnitFragment, multiplicity=Multiplicity(0, 9999))
    }
)
licenses17: BinaryAssociation = BinaryAssociation(
    name="licenses17",
    ends={
        Property(name="p2_ILicense", type=p2_IInstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_IInstallableUnit18", type=p2_ILicense, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metaRequirements19: BinaryAssociation = BinaryAssociation(
    name="metaRequirements19",
    ends={
        Property(name="p2_IRequirement", type=p2_IInstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_IInstallableUnit20", type=p2_IRequirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artifacts11: BinaryAssociation = BinaryAssociation(
    name="artifacts11",
    ends={
        Property(name="p2_IArtifactKey12", type=p2_IInstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_IInstallableUnit", type=p2_IArtifactKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
appliesTo36: BinaryAssociation = BinaryAssociation(
    name="appliesTo36",
    ends={
        Property(name="p2_IRequirement38", type=p2_IInstallableUnitPatch, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_IInstallableUnitPatch37", type=p2_IRequirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertyMap39: BinaryAssociation = BinaryAssociation(
    name="propertyMap39",
    ends={
        Property(name="p2_Property40", type=p2_InstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_InstallableUnit", type=p2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedCapabilities21: BinaryAssociation = BinaryAssociation(
    name="providedCapabilities21",
    ends={
        Property(name="p2_IProvidedCapability", type=p2_IInstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_IInstallableUnit22", type=p2_IProvidedCapability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
host41: BinaryAssociation = BinaryAssociation(
    name="host41",
    ends={
        Property(name="p2_IRequirement42", type=p2_InstallableUnitFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_InstallableUnitFragment", type=p2_IRequirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requirements23: BinaryAssociation = BinaryAssociation(
    name="requirements23",
    ends={
        Property(name="p2_IRequirement25", type=p2_IInstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_IInstallableUnit24", type=p2_IRequirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
touchpointData26: BinaryAssociation = BinaryAssociation(
    name="touchpointData26",
    ends={
        Property(name="p2_ITouchpointData", type=p2_IInstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_IInstallableUnit27", type=p2_ITouchpointData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
touchpointType28: BinaryAssociation = BinaryAssociation(
    name="touchpointType28",
    ends={
        Property(name="p2_ITouchpointType", type=p2_IInstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_IInstallableUnit29", type=p2_ITouchpointType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updateDescriptor30: BinaryAssociation = BinaryAssociation(
    name="updateDescriptor30",
    ends={
        Property(name="p2_IUpdateDescriptor", type=p2_IInstallableUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_IInstallableUnit31", type=p2_IUpdateDescriptor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requirementsChange32: BinaryAssociation = BinaryAssociation(
    name="requirementsChange32",
    ends={
        Property(name="p2_IRequirementChange", type=p2_IInstallableUnitPatch, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_IInstallableUnitPatch", type=p2_IRequirementChange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lifeCycle33: BinaryAssociation = BinaryAssociation(
    name="lifeCycle33",
    ends={
        Property(name="p2_IRequirement35", type=p2_IInstallableUnitPatch, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_IInstallableUnitPatch34", type=p2_IRequirement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value43: BinaryAssociation = BinaryAssociation(
    name="value43",
    ends={
        Property(name="p2_ITouchpointInstruction", type=p2_InstructionMap, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_InstructionMap", type=p2_ITouchpointInstruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
applyOn44: BinaryAssociation = BinaryAssociation(
    name="applyOn44",
    ends={
        Property(name="p2_IRequiredCapability", type=p2_IRequirementChange, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_IRequirementChange45", type=p2_IRequiredCapability, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newValue46: BinaryAssociation = BinaryAssociation(
    name="newValue46",
    ends={
        Property(name="p2_IRequiredCapability48", type=p2_IRequirementChange, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_IRequirementChange47", type=p2_IRequiredCapability, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rules55: BinaryAssociation = BinaryAssociation(
    name="rules55",
    ends={
        Property(name="p2_MappingRule", type=p2_SimpleArtifactRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_SimpleArtifactRepository", type=p2_MappingRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
installableUnits49: BinaryAssociation = BinaryAssociation(
    name="installableUnits49",
    ends={
        Property(name="p2_IInstallableUnit50", type=p2_MetadataRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_MetadataRepository", type=p2_IInstallableUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references51: BinaryAssociation = BinaryAssociation(
    name="references51",
    ends={
        Property(name="p2_IRepositoryReference", type=p2_MetadataRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_MetadataRepository52", type=p2_IRepositoryReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertyMap53: BinaryAssociation = BinaryAssociation(
    name="propertyMap53",
    ends={
        Property(name="p2_Property54", type=p2_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_Repository", type=p2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repositoryPropertyMap56: BinaryAssociation = BinaryAssociation(
    name="repositoryPropertyMap56",
    ends={
        Property(name="p2_Property57", type=p2_SimpleArtifactDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_SimpleArtifactDescriptor", type=p2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructionMap58: BinaryAssociation = BinaryAssociation(
    name="instructionMap58",
    ends={
        Property(name="p2_InstructionMap59", type=p2_TouchpointData, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_TouchpointData", type=p2_InstructionMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_p2_Copyright_ICopyright = Generalization(general=ICopyright, specific=p2_Copyright)
gen_p2_ArtifactKey_IArtifactKey = Generalization(general=IArtifactKey, specific=p2_ArtifactKey)
gen_p2_ArtifactDescriptor_IArtifactDescriptor = Generalization(general=IArtifactDescriptor, specific=p2_ArtifactDescriptor)
gen_p2_IFileArtifactRepository_IArtifactRepository = Generalization(general=IArtifactRepository, specific=p2_IFileArtifactRepository)
gen_p2_InstallableUnit_IInstallableUnit = Generalization(general=IInstallableUnit, specific=p2_InstallableUnit)
gen_p2_InstallableUnitFragment_InstallableUnit = Generalization(general=InstallableUnit, specific=p2_InstallableUnitFragment)
gen_p2_InstallableUnitFragment_IInstallableUnitFragment = Generalization(general=IInstallableUnitFragment, specific=p2_InstallableUnitFragment)
gen_p2_IInstallableUnitFragment_IInstallableUnit = Generalization(general=IInstallableUnit, specific=p2_IInstallableUnitFragment)
gen_p2_IInstallableUnitPatch_IInstallableUnit = Generalization(general=IInstallableUnit, specific=p2_IInstallableUnitPatch)
gen_p2_InstallableUnitPatch_InstallableUnit = Generalization(general=InstallableUnit, specific=p2_InstallableUnitPatch)
gen_p2_InstallableUnitPatch_IInstallableUnitPatch = Generalization(general=IInstallableUnitPatch, specific=p2_InstallableUnitPatch)
gen_p2_IRequiredCapability_IRequirement = Generalization(general=IRequirement, specific=p2_IRequiredCapability)
gen_p2_License_ILicense = Generalization(general=ILicense, specific=p2_License)
gen_p2_RequiredCapability_Requirement = Generalization(general=Requirement, specific=p2_RequiredCapability)
gen_p2_RequiredCapability_IRequiredCapability = Generalization(general=IRequiredCapability, specific=p2_RequiredCapability)
gen_p2_Requirement_IRequirement = Generalization(general=IRequirement, specific=p2_Requirement)
gen_p2_RequirementChange_IRequirementChange = Generalization(general=IRequirementChange, specific=p2_RequirementChange)
gen_p2_SimpleArtifactRepository_ArtifactRepository = Generalization(general=ArtifactRepository, specific=p2_SimpleArtifactRepository)
gen_p2_SimpleArtifactRepository_IFileArtifactRepository = Generalization(general=IFileArtifactRepository, specific=p2_SimpleArtifactRepository)
gen_p2_SimpleArtifactDescriptor_ArtifactDescriptor = Generalization(general=ArtifactDescriptor, specific=p2_SimpleArtifactDescriptor)
gen_p2_ProcessingStepDescriptor_IProcessingStepDescriptor = Generalization(general=IProcessingStepDescriptor, specific=p2_ProcessingStepDescriptor)
gen_p2_ProvidedCapability_IProvidedCapability = Generalization(general=IProvidedCapability, specific=p2_ProvidedCapability)
gen_p2_RepositoryReference_IRepositoryReference = Generalization(general=IRepositoryReference, specific=p2_RepositoryReference)
gen_p2_TouchpointData_ITouchpointData = Generalization(general=ITouchpointData, specific=p2_TouchpointData)
gen_p2_TouchpointInstruction_ITouchpointInstruction = Generalization(general=ITouchpointInstruction, specific=p2_TouchpointInstruction)
gen_p2_TouchpointType_ITouchpointType = Generalization(general=ITouchpointType, specific=p2_TouchpointType)
gen_p2_UpdateDescriptor_IUpdateDescriptor = Generalization(general=IUpdateDescriptor, specific=p2_UpdateDescriptor)

# Domain Model
domain_model = DomainModel(
    name="p2",
    types={p2_Copyright, ICopyright, p2_IAdaptable, p2_ArtifactKey, IArtifactKey, p2_ArtifactDescriptor, IArtifactDescriptor, p2_Property, p2_IProcessingStepDescriptor, p2_ArtifactRepository, p2_ArtifactsByKey, p2_IArtifactKey, p2_IArtifactDescriptor, p2_Comparable, p2_IArtifactRepository, p2_ICopyright, p2_IInstallableUnitFragment, p2_ILicense, p2_IRequirement, p2_IFileArtifactRepository, IArtifactRepository, p2_IInstallableUnit, p2_InstallableUnit, p2_InstallableUnitFragment, InstallableUnit, IInstallableUnitFragment, p2_IProvidedCapability, p2_ITouchpointData, p2_ITouchpointType, p2_IUpdateDescriptor, IInstallableUnit, p2_IInstallableUnitPatch, p2_IRequirementChange, p2_IQueryable, p2_InstallableUnitPatch, IInstallableUnitPatch, p2_IRepository, p2_InstructionMap, p2_ITouchpointInstruction, p2_IMetadataRepository, p2_IRequiredCapability, IRequirement, p2_IRepositoryReference, p2_IVersionedId, p2_License, ILicense, p2_MappingRule, p2_MetadataRepository, p2_RequiredCapability, Requirement, IRequiredCapability, p2_Requirement, p2_RequirementChange, IRequirementChange, p2_SimpleArtifactRepository, ArtifactRepository, IFileArtifactRepository, p2_SimpleArtifactDescriptor, ArtifactDescriptor, p2_ProcessingStepDescriptor, IProcessingStepDescriptor, p2_ProvidedCapability, IProvidedCapability, p2_Repository, p2_RepositoryReference, IRepositoryReference, p2_TouchpointData, ITouchpointData, p2_TouchpointInstruction, ITouchpointInstruction, p2_TouchpointType, ITouchpointType, p2_UpdateDescriptor, IUpdateDescriptor},
    associations={propertyMap0, processingStepList1, artifactMap3, key4, value6, artifactKey8, copyright13, fragments15, licenses17, metaRequirements19, artifacts11, appliesTo36, propertyMap39, providedCapabilities21, host41, requirements23, touchpointData26, touchpointType28, updateDescriptor30, requirementsChange32, lifeCycle33, value43, applyOn44, newValue46, rules55, installableUnits49, references51, propertyMap53, repositoryPropertyMap56, instructionMap58},
    generalizations={gen_p2_Copyright_ICopyright, gen_p2_ArtifactKey_IArtifactKey, gen_p2_ArtifactDescriptor_IArtifactDescriptor, gen_p2_IFileArtifactRepository_IArtifactRepository, gen_p2_InstallableUnit_IInstallableUnit, gen_p2_InstallableUnitFragment_InstallableUnit, gen_p2_InstallableUnitFragment_IInstallableUnitFragment, gen_p2_IInstallableUnitFragment_IInstallableUnit, gen_p2_IInstallableUnitPatch_IInstallableUnit, gen_p2_InstallableUnitPatch_InstallableUnit, gen_p2_InstallableUnitPatch_IInstallableUnitPatch, gen_p2_IRequiredCapability_IRequirement, gen_p2_License_ILicense, gen_p2_RequiredCapability_Requirement, gen_p2_RequiredCapability_IRequiredCapability, gen_p2_Requirement_IRequirement, gen_p2_RequirementChange_IRequirementChange, gen_p2_SimpleArtifactRepository_ArtifactRepository, gen_p2_SimpleArtifactRepository_IFileArtifactRepository, gen_p2_SimpleArtifactDescriptor_ArtifactDescriptor, gen_p2_ProcessingStepDescriptor_IProcessingStepDescriptor, gen_p2_ProvidedCapability_IProvidedCapability, gen_p2_RepositoryReference_IRepositoryReference, gen_p2_TouchpointData_ITouchpointData, gen_p2_TouchpointInstruction_ITouchpointInstruction, gen_p2_TouchpointType_ITouchpointType, gen_p2_UpdateDescriptor_IUpdateDescriptor},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
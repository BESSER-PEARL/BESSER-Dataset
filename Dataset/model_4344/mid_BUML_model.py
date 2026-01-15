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
MIDLevel: Enumeration = Enumeration(
    name="MIDLevel",
    literals={
            EnumerationLiteral(name="INSTANCES"),
			EnumerationLiteral(name="TYPES"),
			EnumerationLiteral(name="WORKFLOWS")
    }
)

ModelOrigin: Enumeration = Enumeration(
    name="ModelOrigin",
    literals={
            EnumerationLiteral(name="IMPORTED"),
			EnumerationLiteral(name="CREATED")
    }
)

# Classes
mid_MID = Class(name="mid::MID")
Operator = Class(name="Operator")
mid_EStringToExtendibleElementMap = Class(name="mid::EStringToExtendibleElementMap")
mid_ExtendibleElement = Class(name="mid::ExtendibleElement", is_abstract=True)
mid_Model = Class(name="mid::Model")
Editor = Class(name="Editor")
mid_ExtendibleElementConstraint = Class(name="mid::ExtendibleElementConstraint")
GenericElement = Class(name="GenericElement")
mid_ExtendibleElementEndpoint = Class(name="mid::ExtendibleElementEndpoint", is_abstract=True)
ExtendibleElement = Class(name="ExtendibleElement")
mid_ModelElement = Class(name="mid::ModelElement")
ConversionOperator = Class(name="ConversionOperator")
mid_ModelEndpoint = Class(name="mid::ModelEndpoint")
ExtendibleElementEndpoint = Class(name="ExtendibleElementEndpoint")
mid_EMFInfo = Class(name="mid::EMFInfo")
mid_GenericElement = Class(name="mid::GenericElement", is_abstract=True)
mid_relationship_ModelRel = Class(name="mid::relationship::ModelRel")
Model = Class(name="Model")
ModelEndpointReference = Class(name="ModelEndpointReference")
MappingReference = Class(name="MappingReference")
mid_relationship_BinaryModelRel = Class(name="mid::relationship::BinaryModelRel")
ModelRel = Class(name="ModelRel")
relationship_mid_ModelEndpoint = Class(name="relationship::mid::ModelEndpoint")
Mapping = Class(name="Mapping")
ExtendibleElementReference = Class(name="ExtendibleElementReference")
mid_relationship_ExtendibleElementEndpointReference = Class(name="mid::relationship::ExtendibleElementEndpointReference", is_abstract=True)
relationship_mid_Model = Class(name="relationship::mid::Model")
mid_relationship_ExtendibleElementReference = Class(name="mid::relationship::ExtendibleElementReference", is_abstract=True)
relationship_mid_ExtendibleElement = Class(name="relationship::mid::ExtendibleElement")
ModelElementEndpointReference = Class(name="ModelElementEndpointReference")
mid_relationship_Mapping = Class(name="mid::relationship::Mapping")
mid_relationship_ModelEndpointReference = Class(name="mid::relationship::ModelEndpointReference")
ExtendibleElementEndpointReference = Class(name="ExtendibleElementEndpointReference")
ModelElementReference = Class(name="ModelElementReference")
mid_relationship_ModelElementReference = Class(name="mid::relationship::ModelElementReference")
mid_relationship_BinaryMapping = Class(name="mid::relationship::BinaryMapping")
mid_relationship_ModelElementEndpoint = Class(name="mid::relationship::ModelElementEndpoint")
ModelElementEndpoint = Class(name="ModelElementEndpoint")
mid_relationship_MappingReference = Class(name="mid::relationship::MappingReference")
mid_editor_Editor = Class(name="mid::editor::Editor")
mid_relationship_BinaryMappingReference = Class(name="mid::relationship::BinaryMappingReference")
mid_relationship_ModelElementEndpointReference = Class(name="mid::relationship::ModelElementEndpointReference")
mid_editor_Diagram = Class(name="mid::editor::Diagram")
mid_operator_Operator = Class(name="mid::operator::Operator")
mid_operator_WorkflowOperator = Class(name="mid::operator::WorkflowOperator")
operator_mid_ModelEndpoint = Class(name="operator::mid::ModelEndpoint")
GenericEndpoint = Class(name="GenericEndpoint")
mid_operator_ConversionOperator = Class(name="mid::operator::ConversionOperator")
mid_operator_RandomOperator = Class(name="mid::operator::RandomOperator")
mid_operator_OperatorGeneric = Class(name="mid::operator::OperatorGeneric")
operator_mid_GenericElement = Class(name="operator::mid::GenericElement")
mid_operator_GenericEndpoint = Class(name="mid::operator::GenericEndpoint")
mid_operator_OperatorInput = Class(name="mid::operator::OperatorInput")
operator_mid_Model = Class(name="operator::mid::Model")
mid_operator_OperatorConstraint = Class(name="mid::operator::OperatorConstraint")
ExtendibleElementConstraint = Class(name="ExtendibleElementConstraint")
OperatorConstraintRule = Class(name="OperatorConstraintRule")
mid_operator_OperatorConstraintRule = Class(name="mid::operator::OperatorConstraintRule")
OperatorConstraintParameter = Class(name="OperatorConstraintParameter")
mid_operator_OperatorConstraintParameter = Class(name="mid::operator::OperatorConstraintParameter")

# mid_MID class attributes and methods
mid_MID_level: Property = Property(name="level", type=StringType)
mid_MID_m_isTypesLevel: Method = Method(name="isTypesLevel", parameters={}, type=BooleanType)
mid_MID_m_isInstancesLevel: Method = Method(name="isInstancesLevel", parameters={}, type=BooleanType)
mid_MID_m_isWorkflowsLevel: Method = Method(name="isWorkflowsLevel", parameters={}, type=BooleanType)
mid_MID_m_getExtendibleElement: Method = Method(name="getExtendibleElement", parameters={Parameter(name='uri')})
mid_MID_m_getModelRels: Method = Method(name="getModelRels", parameters={}, type=StringType)
mid_MID.attributes={mid_MID_level}
mid_MID.methods={mid_MID_m_getExtendibleElement, mid_MID_m_isWorkflowsLevel, mid_MID_m_getModelRels, mid_MID_m_isInstancesLevel, mid_MID_m_isTypesLevel}

# Operator class attributes and methods

# mid_EStringToExtendibleElementMap class attributes and methods
mid_EStringToExtendibleElementMap_key: Property = Property(name="key", type=StringType)
mid_EStringToExtendibleElementMap.attributes={mid_EStringToExtendibleElementMap_key}

# mid_ExtendibleElement class attributes and methods
mid_ExtendibleElement_uri: Property = Property(name="uri", type=StringType)
mid_ExtendibleElement_name: Property = Property(name="name", type=StringType)
mid_ExtendibleElement_level: Property = Property(name="level", type=StringType)
mid_ExtendibleElement_metatypeUri: Property = Property(name="metatypeUri", type=StringType)
mid_ExtendibleElement_dynamic: Property = Property(name="dynamic", type=BooleanType)
mid_ExtendibleElement_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_ExtendibleElement_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_ExtendibleElement_m_isLevel: Method = Method(name="isLevel", parameters={Parameter(name='midLevel')}, type=BooleanType)
mid_ExtendibleElement_m_validateInstanceType: Method = Method(name="validateInstanceType", parameters={Parameter(name='type')}, type=BooleanType)
mid_ExtendibleElement_m_validateInstance: Method = Method(name="validateInstance", parameters={}, type=BooleanType)
mid_ExtendibleElement_m_validateInstanceInEditor: Method = Method(name="validateInstanceInEditor", parameters={Parameter(name='context')}, type=StringType)
mid_ExtendibleElement_m_isWorkflowsLevel: Method = Method(name="isWorkflowsLevel", parameters={}, type=BooleanType)
mid_ExtendibleElement_m_updateWorkflowInstanceId: Method = Method(name="updateWorkflowInstanceId", parameters={Parameter(name='newInstanceId')})
mid_ExtendibleElement_m_toMIDCustomPrintLabel: Method = Method(name="toMIDCustomPrintLabel", parameters={}, type=StringType)
mid_ExtendibleElement_m_toMIDCustomEditLabel: Method = Method(name="toMIDCustomEditLabel", parameters={}, type=StringType)
mid_ExtendibleElement_m_updateMIDCustomLabel: Method = Method(name="updateMIDCustomLabel", parameters={Parameter(name='newLabel')})
mid_ExtendibleElement_m_isTypesLevel: Method = Method(name="isTypesLevel", parameters={}, type=BooleanType)
mid_ExtendibleElement_m_createSubtypeUri: Method = Method(name="createSubtypeUri", parameters={Parameter(name='newTypeFragmentUri'), Parameter(name='newTypeName')}, type=StringType)
mid_ExtendibleElement_m_addTypeConstraint: Method = Method(name="addTypeConstraint", parameters={Parameter(name='implementation'), Parameter(name='language')})
mid_ExtendibleElement_m_isInstancesLevel: Method = Method(name="isInstancesLevel", parameters={}, type=BooleanType)
mid_ExtendibleElement_m_getRuntimeTypes: Method = Method(name="getRuntimeTypes", parameters={})
mid_ExtendibleElement.attributes={mid_ExtendibleElement_level, mid_ExtendibleElement_metatypeUri, mid_ExtendibleElement_dynamic, mid_ExtendibleElement_uri, mid_ExtendibleElement_name}
mid_ExtendibleElement.methods={mid_ExtendibleElement_m_toMIDCustomEditLabel, mid_ExtendibleElement_m_toMIDCustomPrintLabel, mid_ExtendibleElement_m_validateInstanceType, mid_ExtendibleElement_m_isInstancesLevel, mid_ExtendibleElement_m_isLevel, mid_ExtendibleElement_m_getRuntimeTypes, mid_ExtendibleElement_m_getMIDContainer, mid_ExtendibleElement_m_getMetatype, mid_ExtendibleElement_m_updateMIDCustomLabel, mid_ExtendibleElement_m_validateInstance, mid_ExtendibleElement_m_updateWorkflowInstanceId, mid_ExtendibleElement_m_validateInstanceInEditor, mid_ExtendibleElement_m_isWorkflowsLevel, mid_ExtendibleElement_m_addTypeConstraint, mid_ExtendibleElement_m_createSubtypeUri, mid_ExtendibleElement_m_isTypesLevel}

# mid_Model class attributes and methods
mid_Model_origin: Property = Property(name="origin", type=StringType)
mid_Model_fileExtension: Property = Property(name="fileExtension", type=StringType)
mid_Model_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_Model_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=StringType)
mid_Model_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_Model_m_createSubtype: Method = Method(name="createSubtype", parameters={Parameter(name='isMetamodelExtension'), Parameter(name='newModelTypeName')}, type=StringType)
mid_Model_m_deleteType: Method = Method(name="deleteType", parameters={})
mid_Model_m_importInstanceAndEditor: Method = Method(name="importInstanceAndEditor", parameters={Parameter(name='modelUri'), Parameter(name='instanceMID')}, type=StringType)
mid_Model_m_copyInstance: Method = Method(name="copyInstance", parameters={Parameter(name='origModel'), Parameter(name='instanceMID'), Parameter(name='newModelName')}, type=StringType)
mid_Model_m_copyInstanceAndEditor: Method = Method(name="copyInstanceAndEditor", parameters={Parameter(name='copyDiagram'), Parameter(name='instanceMID'), Parameter(name='origModel'), Parameter(name='newModelName')}, type=StringType)
mid_Model_m_deleteInstance: Method = Method(name="deleteInstance", parameters={})
mid_Model_m_deleteInstanceAndFile: Method = Method(name="deleteInstanceAndFile", parameters={})
mid_Model_m_getEMFInstanceRoot: Method = Method(name="getEMFInstanceRoot", parameters={}, type=StringType)
mid_Model_m_openInstance: Method = Method(name="openInstance", parameters={})
mid_Model_m_createWorkflowInstance: Method = Method(name="createWorkflowInstance", parameters={Parameter(name='workflowMID'), Parameter(name='newModelId')}, type=StringType)
mid_Model_m_deleteWorkflowInstance: Method = Method(name="deleteWorkflowInstance", parameters={})
mid_Model_m_getEMFTypeRoot: Method = Method(name="getEMFTypeRoot", parameters={}, type=StringType)
mid_Model_m_openType: Method = Method(name="openType", parameters={})
mid_Model_m_createInstance: Method = Method(name="createInstance", parameters={Parameter(name='newModelUri'), Parameter(name='instanceMID')}, type=StringType)
mid_Model_m_createInstanceEditor: Method = Method(name="createInstanceEditor", parameters={}, type=StringType)
mid_Model_m_createInstanceAndEditor: Method = Method(name="createInstanceAndEditor", parameters={Parameter(name='newModelUri'), Parameter(name='instanceMID')}, type=StringType)
mid_Model_m_importInstance: Method = Method(name="importInstance", parameters={Parameter(name='modelUri'), Parameter(name='instanceMID')}, type=StringType)
mid_Model.attributes={mid_Model_origin, mid_Model_fileExtension}
mid_Model.methods={mid_Model_m_copyInstanceAndEditor, mid_Model_m_createWorkflowInstance, mid_Model_m_createInstanceAndEditor, mid_Model_m_getMIDContainer, mid_Model_m_deleteType, mid_Model_m_createInstanceEditor, mid_Model_m_importInstanceAndEditor, mid_Model_m_getEMFInstanceRoot, mid_Model_m_getEMFTypeRoot, mid_Model_m_getMetatype, mid_Model_m_importInstance, mid_Model_m_deleteInstanceAndFile, mid_Model_m_openType, mid_Model_m_createSubtype, mid_Model_m_getSupertype, mid_Model_m_createInstance, mid_Model_m_deleteInstance, mid_Model_m_copyInstance, mid_Model_m_openInstance, mid_Model_m_deleteWorkflowInstance}

# Editor class attributes and methods

# mid_ExtendibleElementConstraint class attributes and methods
mid_ExtendibleElementConstraint_implementation: Property = Property(name="implementation", type=StringType)
mid_ExtendibleElementConstraint_language: Property = Property(name="language", type=StringType)
mid_ExtendibleElementConstraint.attributes={mid_ExtendibleElementConstraint_language, mid_ExtendibleElementConstraint_implementation}

# GenericElement class attributes and methods

# mid_ExtendibleElementEndpoint class attributes and methods
mid_ExtendibleElementEndpoint_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
mid_ExtendibleElementEndpoint_upperBound: Property = Property(name="upperBound", type=IntegerType)
mid_ExtendibleElementEndpoint_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_ExtendibleElementEndpoint_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=StringType)
mid_ExtendibleElementEndpoint_m_getTargetUri: Method = Method(name="getTargetUri", parameters={}, type=StringType)
mid_ExtendibleElementEndpoint.attributes={mid_ExtendibleElementEndpoint_upperBound, mid_ExtendibleElementEndpoint_lowerBound}
mid_ExtendibleElementEndpoint.methods={mid_ExtendibleElementEndpoint_m_getTargetUri, mid_ExtendibleElementEndpoint_m_getMetatype, mid_ExtendibleElementEndpoint_m_getSupertype}

# ExtendibleElement class attributes and methods

# mid_ModelElement class attributes and methods
mid_ModelElement_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_ModelElement_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=StringType)
mid_ModelElement_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_ModelElement_m_createTypeReference: Method = Method(name="createTypeReference", parameters={Parameter(name='isModifiable'), Parameter(name='modelElemTypeRef'), Parameter(name='containerModelTypeEndpointRef')}, type=StringType)
mid_ModelElement_m_createSubtypeAndReference: Method = Method(name="createSubtypeAndReference", parameters={Parameter(name='eInfo'), Parameter(name='modelElemTypeRef'), Parameter(name='newModelElemTypeName'), Parameter(name='containerModelTypeEndpointRef'), Parameter(name='newModelElemTypeUri')}, type=StringType)
mid_ModelElement_m_deleteType: Method = Method(name="deleteType", parameters={})
mid_ModelElement_m_getEMFTypeObject: Method = Method(name="getEMFTypeObject", parameters={}, type=StringType)
mid_ModelElement_m_createInstanceReference: Method = Method(name="createInstanceReference", parameters={Parameter(name='containerModelEndpointRef')}, type=StringType)
mid_ModelElement_m_createInstanceAndReference: Method = Method(name="createInstanceAndReference", parameters={Parameter(name='newModelElemUri'), Parameter(name='containerModelEndpointRef'), Parameter(name='newModelElemName'), Parameter(name='eInfo')}, type=StringType)
mid_ModelElement_m_deleteInstance: Method = Method(name="deleteInstance", parameters={})
mid_ModelElement_m_getEMFInstanceObject: Method = Method(name="getEMFInstanceObject", parameters={}, type=StringType)
mid_ModelElement.methods={mid_ModelElement_m_createInstanceAndReference, mid_ModelElement_m_createSubtypeAndReference, mid_ModelElement_m_createTypeReference, mid_ModelElement_m_deleteInstance, mid_ModelElement_m_deleteType, mid_ModelElement_m_createInstanceReference, mid_ModelElement_m_getEMFInstanceObject, mid_ModelElement_m_getMetatype, mid_ModelElement_m_getMIDContainer, mid_ModelElement_m_getEMFTypeObject, mid_ModelElement_m_getSupertype}

# ConversionOperator class attributes and methods

# mid_ModelEndpoint class attributes and methods
mid_ModelEndpoint_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_ModelEndpoint_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=StringType)
mid_ModelEndpoint_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_ModelEndpoint_m_createWorkflowInstance: Method = Method(name="createWorkflowInstance", parameters={Parameter(name='targetModel'), Parameter(name='containerFeatureName'), Parameter(name='containerOperator')}, type=StringType)
mid_ModelEndpoint_m_replaceWorkflowInstance: Method = Method(name="replaceWorkflowInstance", parameters={Parameter(name='oldModelEndpoint'), Parameter(name='targetModel')})
mid_ModelEndpoint_m_deleteWorkflowInstance: Method = Method(name="deleteWorkflowInstance", parameters={})
mid_ModelEndpoint_m_getTarget: Method = Method(name="getTarget", parameters={}, type=StringType)
mid_ModelEndpoint_m_createTypeReference: Method = Method(name="createTypeReference", parameters={Parameter(name='isModifiable'), Parameter(name='containerModelRelType')}, type=StringType)
mid_ModelEndpoint_m_createSubtype: Method = Method(name="createSubtype", parameters={Parameter(name='isBinarySrc'), Parameter(name='containerModelRelType'), Parameter(name='newModelTypeEndpointName'), Parameter(name='targetModelType')}, type=StringType)
mid_ModelEndpoint_m_replaceSubtype: Method = Method(name="replaceSubtype", parameters={Parameter(name='targetModelType'), Parameter(name='newModelTypeEndpointName'), Parameter(name='oldModelTypeEndpoint')})
mid_ModelEndpoint_m_deleteType: Method = Method(name="deleteType", parameters={Parameter(name='isFullDelete')})
mid_ModelEndpoint_m_createInstanceReference: Method = Method(name="createInstanceReference", parameters={Parameter(name='containerModelRel')}, type=StringType)
mid_ModelEndpoint_m_createInstance: Method = Method(name="createInstance", parameters={Parameter(name='containerModelRel'), Parameter(name='targetModel')}, type=StringType)
mid_ModelEndpoint_m_createInstance: Method = Method(name="createInstance", parameters={Parameter(name='targetModel'), Parameter(name='containerOperator'), Parameter(name='containerFeatureName')}, type=StringType)
mid_ModelEndpoint_m_replaceInstance: Method = Method(name="replaceInstance", parameters={Parameter(name='oldModelEndpoint'), Parameter(name='targetModel')})
mid_ModelEndpoint_m_deleteInstance: Method = Method(name="deleteInstance", parameters={Parameter(name='isFullDelete')})
mid_ModelEndpoint_m_createWorkflowInstance: Method = Method(name="createWorkflowInstance", parameters={Parameter(name='containerModelRel'), Parameter(name='targetModel')}, type=StringType)
mid_ModelEndpoint.methods={mid_ModelEndpoint_m_createInstance, mid_ModelEndpoint_m_createWorkflowInstance, mid_ModelEndpoint_m_getMetatype, mid_ModelEndpoint_m_createInstanceReference, mid_ModelEndpoint_m_createSubtype, mid_ModelEndpoint_m_getSupertype, mid_ModelEndpoint_m_replaceWorkflowInstance, mid_ModelEndpoint_m_deleteWorkflowInstance, mid_ModelEndpoint_m_createWorkflowInstance, mid_ModelEndpoint_m_deleteInstance, mid_ModelEndpoint_m_createTypeReference, mid_ModelEndpoint_m_getTarget, mid_ModelEndpoint_m_createInstance, mid_ModelEndpoint_m_deleteType, mid_ModelEndpoint_m_replaceSubtype, mid_ModelEndpoint_m_getMIDContainer, mid_ModelEndpoint_m_replaceInstance}

# ExtendibleElementEndpoint class attributes and methods

# mid_EMFInfo class attributes and methods
mid_EMFInfo_className: Property = Property(name="className", type=StringType)
mid_EMFInfo_featureName: Property = Property(name="featureName", type=StringType)
mid_EMFInfo_attribute: Property = Property(name="attribute", type=BooleanType)
mid_EMFInfo_relatedClassName: Property = Property(name="relatedClassName", type=StringType)
mid_EMFInfo_m_toTypeString: Method = Method(name="toTypeString", parameters={}, type=StringType)
mid_EMFInfo_m_toInstanceString: Method = Method(name="toInstanceString", parameters={}, type=StringType)
mid_EMFInfo.attributes={mid_EMFInfo_relatedClassName, mid_EMFInfo_featureName, mid_EMFInfo_attribute, mid_EMFInfo_className}
mid_EMFInfo.methods={mid_EMFInfo_m_toInstanceString, mid_EMFInfo_m_toTypeString}

# mid_GenericElement class attributes and methods
mid_GenericElement_abstract: Property = Property(name="abstract", type=BooleanType)
mid_GenericElement.attributes={mid_GenericElement_abstract}

# mid_relationship_ModelRel class attributes and methods
mid_relationship_ModelRel_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_relationship_ModelRel_m_createBinarySubtype: Method = Method(name="createBinarySubtype", parameters={Parameter(name='isMetamodelExtension'), Parameter(name='newModelRelTypeName')}, type=StringType)
mid_relationship_ModelRel_m_copySubtype: Method = Method(name="copySubtype", parameters={Parameter(name='origModelRelType')}, type=StringType)
mid_relationship_ModelRel_m_getOutlineResourceTypes: Method = Method(name="getOutlineResourceTypes", parameters={}, type=StringType)
mid_relationship_ModelRel_m_createInstanceAndEndpoints: Method = Method(name="createInstanceAndEndpoints", parameters={Parameter(name='endpointModels'), Parameter(name='instanceMID'), Parameter(name='newModelRelUri')}, type=StringType)
mid_relationship_ModelRel_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_relationship_ModelRel_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=Model)
mid_relationship_ModelRel_m_createBinaryInstance: Method = Method(name="createBinaryInstance", parameters={Parameter(name='instanceMID'), Parameter(name='newModelRelUri')}, type=StringType)
mid_relationship_ModelRel_m_createBinaryInstanceAndEndpoints: Method = Method(name="createBinaryInstanceAndEndpoints", parameters={Parameter(name='instanceMID'), Parameter(name='endpointSourceModel'), Parameter(name='endpointTargetModel'), Parameter(name='newModelRelUri')}, type=StringType)
mid_relationship_ModelRel_m_getOutlineResourceInstances: Method = Method(name="getOutlineResourceInstances", parameters={}, type=StringType)
mid_relationship_ModelRel_m_createWorkflowInstanceAndEndpoints: Method = Method(name="createWorkflowInstanceAndEndpoints", parameters={Parameter(name='workflowMID'), Parameter(name='endpointModels'), Parameter(name='newModelRelId')}, type=StringType)
mid_relationship_ModelRel_m_createWorkflowBinaryInstance: Method = Method(name="createWorkflowBinaryInstance", parameters={Parameter(name='workflowMID'), Parameter(name='newModelRelId')}, type=StringType)
mid_relationship_ModelRel_m_createWorkflowBinaryInstanceAndEndpoints: Method = Method(name="createWorkflowBinaryInstanceAndEndpoints", parameters={Parameter(name='endpointTargetModel'), Parameter(name='workflowMID'), Parameter(name='newModelRelId'), Parameter(name='endpointSourceModel')}, type=StringType)
mid_relationship_ModelRel.methods={mid_relationship_ModelRel_m_getSupertype, mid_relationship_ModelRel_m_getMetatype, mid_relationship_ModelRel_m_createBinaryInstanceAndEndpoints, mid_relationship_ModelRel_m_createWorkflowInstanceAndEndpoints, mid_relationship_ModelRel_m_createWorkflowBinaryInstance, mid_relationship_ModelRel_m_getMIDContainer, mid_relationship_ModelRel_m_createWorkflowBinaryInstanceAndEndpoints, mid_relationship_ModelRel_m_createInstanceAndEndpoints, mid_relationship_ModelRel_m_getOutlineResourceInstances, mid_relationship_ModelRel_m_createBinarySubtype, mid_relationship_ModelRel_m_createBinaryInstance, mid_relationship_ModelRel_m_copySubtype, mid_relationship_ModelRel_m_getOutlineResourceTypes}

# Model class attributes and methods

# ModelEndpointReference class attributes and methods

# MappingReference class attributes and methods

# mid_relationship_BinaryModelRel class attributes and methods
mid_relationship_BinaryModelRel_m_addModelType: Method = Method(name="addModelType", parameters={Parameter(name='isBinarySrc'), Parameter(name='modelType')})
mid_relationship_BinaryModelRel.methods={mid_relationship_BinaryModelRel_m_addModelType}

# ModelRel class attributes and methods

# relationship_mid_ModelEndpoint class attributes and methods

# Mapping class attributes and methods

# ExtendibleElementReference class attributes and methods

# mid_relationship_ExtendibleElementEndpointReference class attributes and methods
mid_relationship_ExtendibleElementEndpointReference_m_getObject: Method = Method(name="getObject", parameters={}, type=ExtendibleElementEndpoint)
mid_relationship_ExtendibleElementEndpointReference_m_getSupertypeRef: Method = Method(name="getSupertypeRef", parameters={}, type=StringType)
mid_relationship_ExtendibleElementEndpointReference_m_getTargetUri: Method = Method(name="getTargetUri", parameters={}, type=StringType)
mid_relationship_ExtendibleElementEndpointReference.methods={mid_relationship_ExtendibleElementEndpointReference_m_getSupertypeRef, mid_relationship_ExtendibleElementEndpointReference_m_getTargetUri, mid_relationship_ExtendibleElementEndpointReference_m_getObject}

# relationship_mid_Model class attributes and methods

# mid_relationship_ExtendibleElementReference class attributes and methods
mid_relationship_ExtendibleElementReference_modifiable: Property = Property(name="modifiable", type=BooleanType)
mid_relationship_ExtendibleElementReference_m_getUri: Method = Method(name="getUri", parameters={}, type=StringType)
mid_relationship_ExtendibleElementReference_m_getObject: Method = Method(name="getObject", parameters={}, type=ExtendibleElement)
mid_relationship_ExtendibleElementReference_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_relationship_ExtendibleElementReference_m_isTypesLevel: Method = Method(name="isTypesLevel", parameters={}, type=BooleanType)
mid_relationship_ExtendibleElementReference_m_isInstancesLevel: Method = Method(name="isInstancesLevel", parameters={}, type=BooleanType)
mid_relationship_ExtendibleElementReference_m_isWorkflowsLevel: Method = Method(name="isWorkflowsLevel", parameters={}, type=BooleanType)
mid_relationship_ExtendibleElementReference.attributes={mid_relationship_ExtendibleElementReference_modifiable}
mid_relationship_ExtendibleElementReference.methods={mid_relationship_ExtendibleElementReference_m_getUri, mid_relationship_ExtendibleElementReference_m_getMIDContainer, mid_relationship_ExtendibleElementReference_m_isTypesLevel, mid_relationship_ExtendibleElementReference_m_getObject, mid_relationship_ExtendibleElementReference_m_isWorkflowsLevel, mid_relationship_ExtendibleElementReference_m_isInstancesLevel}

# relationship_mid_ExtendibleElement class attributes and methods

# ModelElementEndpointReference class attributes and methods

# mid_relationship_Mapping class attributes and methods
mid_relationship_Mapping_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_relationship_Mapping_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=StringType)
mid_relationship_Mapping_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_relationship_Mapping_m_createTypeReference: Method = Method(name="createTypeReference", parameters={Parameter(name='isModifiable'), Parameter(name='mappingTypeRef'), Parameter(name='containerModelRelType')}, type=StringType)
mid_relationship_Mapping_m_createSubtypeAndReference: Method = Method(name="createSubtypeAndReference", parameters={Parameter(name='newMappingTypeName'), Parameter(name='mappingTypeRef'), Parameter(name='isBinary'), Parameter(name='containerModelRelType')}, type=StringType)
mid_relationship_Mapping_m_deleteType: Method = Method(name="deleteType", parameters={})
mid_relationship_Mapping_m_createInstanceReference: Method = Method(name="createInstanceReference", parameters={Parameter(name='containerModelRel')}, type=StringType)
mid_relationship_Mapping_m_createInstanceAndReference: Method = Method(name="createInstanceAndReference", parameters={Parameter(name='isBinary'), Parameter(name='containerModelRel')}, type=StringType)
mid_relationship_Mapping_m_createInstanceAndReferenceAndEndpointsAndReferences: Method = Method(name="createInstanceAndReferenceAndEndpointsAndReferences", parameters={Parameter(name='isBinary'), Parameter(name='targetModelElemRefs')}, type=StringType)
mid_relationship_Mapping_m_deleteInstance: Method = Method(name="deleteInstance", parameters={})
mid_relationship_Mapping.methods={mid_relationship_Mapping_m_getMetatype, mid_relationship_Mapping_m_getSupertype, mid_relationship_Mapping_m_getMIDContainer, mid_relationship_Mapping_m_createInstanceAndReferenceAndEndpointsAndReferences, mid_relationship_Mapping_m_createTypeReference, mid_relationship_Mapping_m_createInstanceAndReference, mid_relationship_Mapping_m_createSubtypeAndReference, mid_relationship_Mapping_m_deleteType, mid_relationship_Mapping_m_createInstanceReference, mid_relationship_Mapping_m_deleteInstance}

# mid_relationship_ModelEndpointReference class attributes and methods
mid_relationship_ModelEndpointReference_m_getObject: Method = Method(name="getObject", parameters={}, type=StringType)
mid_relationship_ModelEndpointReference_m_getSupertypeRef: Method = Method(name="getSupertypeRef", parameters={}, type=StringType)
mid_relationship_ModelEndpointReference_m_acceptModelElementType: Method = Method(name="acceptModelElementType", parameters={Parameter(name='metamodelObj')}, type=BooleanType)
mid_relationship_ModelEndpointReference_m_deleteTypeReference: Method = Method(name="deleteTypeReference", parameters={Parameter(name='isFullDelete')})
mid_relationship_ModelEndpointReference_m_acceptModelElementInstance: Method = Method(name="acceptModelElementInstance", parameters={Parameter(name='modelObj')}, type=StringType)
mid_relationship_ModelEndpointReference_m_createModelElementInstanceAndReference: Method = Method(name="createModelElementInstanceAndReference", parameters={Parameter(name='modelObj'), Parameter(name='newModelElemName')}, type=StringType)
mid_relationship_ModelEndpointReference.methods={mid_relationship_ModelEndpointReference_m_getSupertypeRef, mid_relationship_ModelEndpointReference_m_createModelElementInstanceAndReference, mid_relationship_ModelEndpointReference_m_getObject, mid_relationship_ModelEndpointReference_m_acceptModelElementType, mid_relationship_ModelEndpointReference_m_acceptModelElementInstance, mid_relationship_ModelEndpointReference_m_deleteTypeReference}

# ExtendibleElementEndpointReference class attributes and methods

# ModelElementReference class attributes and methods

# mid_relationship_ModelElementReference class attributes and methods
mid_relationship_ModelElementReference_m_getSupertypeRef: Method = Method(name="getSupertypeRef", parameters={}, type=StringType)
mid_relationship_ModelElementReference_m_deleteTypeReference: Method = Method(name="deleteTypeReference", parameters={})
mid_relationship_ModelElementReference_m_deleteInstanceReference: Method = Method(name="deleteInstanceReference", parameters={})
mid_relationship_ModelElementReference_m_getObject: Method = Method(name="getObject", parameters={}, type=StringType)
mid_relationship_ModelElementReference.methods={mid_relationship_ModelElementReference_m_deleteTypeReference, mid_relationship_ModelElementReference_m_getObject, mid_relationship_ModelElementReference_m_deleteInstanceReference, mid_relationship_ModelElementReference_m_getSupertypeRef}

# mid_relationship_BinaryMapping class attributes and methods

# mid_relationship_ModelElementEndpoint class attributes and methods
mid_relationship_ModelElementEndpoint_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_relationship_ModelElementEndpoint_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=StringType)
mid_relationship_ModelElementEndpoint_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_relationship_ModelElementEndpoint_m_getTarget: Method = Method(name="getTarget", parameters={}, type=StringType)
mid_relationship_ModelElementEndpoint_m_createTypeReference: Method = Method(name="createTypeReference", parameters={Parameter(name='containerMappingTypeRef'), Parameter(name='isModifiable'), Parameter(name='targetModelElemTypeRef'), Parameter(name='modelElemTypeEndpointRef'), Parameter(name='isBinarySrc')}, type=StringType)
mid_relationship_ModelElementEndpoint_m_createSubtypeAndReference: Method = Method(name="createSubtypeAndReference", parameters={Parameter(name='containerMappingTypeRef'), Parameter(name='isBinarySrc'), Parameter(name='targetModelElemTypeRef'), Parameter(name='newModelElemTypeEndpointName')}, type=StringType)
mid_relationship_ModelElementEndpoint_m_replaceSubtypeAndReference: Method = Method(name="replaceSubtypeAndReference", parameters={Parameter(name='oldModelElemTypeEndpointRef'), Parameter(name='newModelElemTypeEndpointName'), Parameter(name='targetModelElemTypeRef')})
mid_relationship_ModelElementEndpoint_m_deleteType: Method = Method(name="deleteType", parameters={Parameter(name='isFullDelete')})
mid_relationship_ModelElementEndpoint_m_createInstanceReference: Method = Method(name="createInstanceReference", parameters={Parameter(name='containerMappingRef'), Parameter(name='targetModelElemRef')}, type=StringType)
mid_relationship_ModelElementEndpoint_m_createInstanceAndReference: Method = Method(name="createInstanceAndReference", parameters={Parameter(name='targetModelElemRef'), Parameter(name='containerMappingRef')}, type=StringType)
mid_relationship_ModelElementEndpoint_m_replaceInstanceAndReference: Method = Method(name="replaceInstanceAndReference", parameters={Parameter(name='targetModelElemRef'), Parameter(name='oldModelElemEndpointRef')})
mid_relationship_ModelElementEndpoint.methods={mid_relationship_ModelElementEndpoint_m_getSupertype, mid_relationship_ModelElementEndpoint_m_createSubtypeAndReference, mid_relationship_ModelElementEndpoint_m_replaceSubtypeAndReference, mid_relationship_ModelElementEndpoint_m_getMetatype, mid_relationship_ModelElementEndpoint_m_createInstanceReference, mid_relationship_ModelElementEndpoint_m_getTarget, mid_relationship_ModelElementEndpoint_m_createInstanceAndReference, mid_relationship_ModelElementEndpoint_m_deleteType, mid_relationship_ModelElementEndpoint_m_getMIDContainer, mid_relationship_ModelElementEndpoint_m_createTypeReference, mid_relationship_ModelElementEndpoint_m_replaceInstanceAndReference}

# ModelElementEndpoint class attributes and methods

# mid_relationship_MappingReference class attributes and methods
mid_relationship_MappingReference_m_getObject: Method = Method(name="getObject", parameters={}, type=StringType)
mid_relationship_MappingReference_m_getSupertypeRef: Method = Method(name="getSupertypeRef", parameters={}, type=StringType)
mid_relationship_MappingReference_m_deleteTypeReference: Method = Method(name="deleteTypeReference", parameters={})
mid_relationship_MappingReference_m_deleteTypeAndReference: Method = Method(name="deleteTypeAndReference", parameters={})
mid_relationship_MappingReference_m_deleteInstanceReference: Method = Method(name="deleteInstanceReference", parameters={})
mid_relationship_MappingReference_m_deleteInstanceAndReference: Method = Method(name="deleteInstanceAndReference", parameters={})
mid_relationship_MappingReference.methods={mid_relationship_MappingReference_m_deleteInstanceReference, mid_relationship_MappingReference_m_deleteInstanceAndReference, mid_relationship_MappingReference_m_deleteTypeReference, mid_relationship_MappingReference_m_getSupertypeRef, mid_relationship_MappingReference_m_getObject, mid_relationship_MappingReference_m_deleteTypeAndReference}

# mid_editor_Editor class attributes and methods
mid_editor_Editor_modelUri: Property = Property(name="modelUri", type=StringType)
mid_editor_Editor_id: Property = Property(name="id", type=StringType)
mid_editor_Editor_wizardId: Property = Property(name="wizardId", type=StringType)
mid_editor_Editor_fileExtensions: Property = Property(name="fileExtensions", type=StringType)
mid_editor_Editor_wizardDialogClass: Property = Property(name="wizardDialogClass", type=StringType)
mid_editor_Editor_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_editor_Editor_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=StringType)
mid_editor_Editor_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_editor_Editor_m_createSubtype: Method = Method(name="createSubtype", parameters={Parameter(name='modelTypeUri'), Parameter(name='newEditorTypeName'), Parameter(name='newEditorTypeFragmentUri'), Parameter(name='wizardDialogClassName'), Parameter(name='editorId'), Parameter(name='wizardId')}, type=StringType)
mid_editor_Editor_m_deleteType: Method = Method(name="deleteType", parameters={})
mid_editor_Editor_m_createInstance: Method = Method(name="createInstance", parameters={Parameter(name='instanceMID'), Parameter(name='modelUri')}, type=StringType)
mid_editor_Editor_m_invokeInstanceWizard: Method = Method(name="invokeInstanceWizard", parameters={Parameter(name='initialSelection')}, type=StringType)
mid_editor_Editor_m_deleteInstance: Method = Method(name="deleteInstance", parameters={})
mid_editor_Editor.attributes={mid_editor_Editor_modelUri, mid_editor_Editor_wizardDialogClass, mid_editor_Editor_wizardId, mid_editor_Editor_fileExtensions, mid_editor_Editor_id}
mid_editor_Editor.methods={mid_editor_Editor_m_deleteInstance, mid_editor_Editor_m_getMIDContainer, mid_editor_Editor_m_createSubtype, mid_editor_Editor_m_createInstance, mid_editor_Editor_m_invokeInstanceWizard, mid_editor_Editor_m_getSupertype, mid_editor_Editor_m_deleteType, mid_editor_Editor_m_getMetatype}

# mid_relationship_BinaryMappingReference class attributes and methods
mid_relationship_BinaryMappingReference_m_getObject: Method = Method(name="getObject", parameters={}, type=StringType)
mid_relationship_BinaryMappingReference_m_addModelElementTypeReference: Method = Method(name="addModelElementTypeReference", parameters={Parameter(name='isBinarySrc'), Parameter(name='modelElemTypeRef')})
mid_relationship_BinaryMappingReference.methods={mid_relationship_BinaryMappingReference_m_addModelElementTypeReference, mid_relationship_BinaryMappingReference_m_getObject}

# mid_relationship_ModelElementEndpointReference class attributes and methods
mid_relationship_ModelElementEndpointReference_m_deleteInstanceAndReference: Method = Method(name="deleteInstanceAndReference", parameters={Parameter(name='isFullDelete')})
mid_relationship_ModelElementEndpointReference_m_getObject: Method = Method(name="getObject", parameters={}, type=StringType)
mid_relationship_ModelElementEndpointReference_m_getSupertypeRef: Method = Method(name="getSupertypeRef", parameters={}, type=StringType)
mid_relationship_ModelElementEndpointReference_m_deleteTypeReference: Method = Method(name="deleteTypeReference", parameters={Parameter(name='isFullDelete')})
mid_relationship_ModelElementEndpointReference_m_deleteTypeAndReference: Method = Method(name="deleteTypeAndReference", parameters={Parameter(name='isFullDelete')})
mid_relationship_ModelElementEndpointReference.methods={mid_relationship_ModelElementEndpointReference_m_deleteInstanceAndReference, mid_relationship_ModelElementEndpointReference_m_deleteTypeReference, mid_relationship_ModelElementEndpointReference_m_getObject, mid_relationship_ModelElementEndpointReference_m_deleteTypeAndReference, mid_relationship_ModelElementEndpointReference_m_getSupertypeRef}

# mid_editor_Diagram class attributes and methods
mid_editor_Diagram_m_createSubtype: Method = Method(name="createSubtype", parameters={Parameter(name='wizardId'), Parameter(name='wizardDialogClassName'), Parameter(name='newEditorTypeFragmentUri'), Parameter(name='editorId'), Parameter(name='modelTypeUri'), Parameter(name='newEditorTypeName')}, type=StringType)
mid_editor_Diagram_m_createInstance: Method = Method(name="createInstance", parameters={Parameter(name='instanceMID'), Parameter(name='modelUri')}, type=StringType)
mid_editor_Diagram_m_invokeInstanceWizard: Method = Method(name="invokeInstanceWizard", parameters={Parameter(name='initialSelection')}, type=StringType)
mid_editor_Diagram.methods={mid_editor_Diagram_m_createSubtype, mid_editor_Diagram_m_invokeInstanceWizard, mid_editor_Diagram_m_createInstance}

# mid_operator_Operator class attributes and methods
mid_operator_Operator_inputSubdir: Property = Property(name="inputSubdir", type=StringType)
mid_operator_Operator_updateMID: Property = Property(name="updateMID", type=BooleanType)
mid_operator_Operator_executionTime: Property = Property(name="executionTime", type=StringType)
mid_operator_Operator_commutative: Property = Property(name="commutative", type=BooleanType)
mid_operator_Operator_m_getOutputModels: Method = Method(name="getOutputModels", parameters={}, type=Model)
mid_operator_Operator_m_createInstance: Method = Method(name="createInstance", parameters={Parameter(name='instanceMID')}, type=StringType)
mid_operator_Operator_m_deleteInstance: Method = Method(name="deleteInstance", parameters={})
mid_operator_Operator_m_selectAllowedGenerics: Method = Method(name="selectAllowedGenerics", parameters={Parameter(name='inputs')}, type=StringType)
mid_operator_Operator_m_isAllowedGeneric: Method = Method(name="isAllowedGeneric", parameters={Parameter(name='inputs'), Parameter(name='genericTypeEndpoint'), Parameter(name='genericType')}, type=BooleanType)
mid_operator_Operator_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_operator_Operator_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=StringType)
mid_operator_Operator_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_operator_Operator_m_createSubtype: Method = Method(name="createSubtype", parameters={Parameter(name='implementationUri'), Parameter(name='newOperatorTypeName')}, type=StringType)
mid_operator_Operator_m_deleteType: Method = Method(name="deleteType", parameters={})
mid_operator_Operator_m_openType: Method = Method(name="openType", parameters={})
mid_operator_Operator_m_findAllowedInputs: Method = Method(name="findAllowedInputs", parameters={Parameter(name='inputMIDs')})
mid_operator_Operator_m_findFirstAllowedInput: Method = Method(name="findFirstAllowedInput", parameters={Parameter(name='inputMIDs')}, type=StringType)
mid_operator_Operator_m_checkAllowedInputs: Method = Method(name="checkAllowedInputs", parameters={Parameter(name='inputModels')}, type=StringType)
mid_operator_Operator_m_getOutputsByName: Method = Method(name="getOutputsByName", parameters={})
mid_operator_Operator_m_openInstance: Method = Method(name="openInstance", parameters={})
mid_operator_Operator_m_createWorkflowInstance: Method = Method(name="createWorkflowInstance", parameters={Parameter(name='workflowMID')}, type=StringType)
mid_operator_Operator_m_deleteWorkflowInstance: Method = Method(name="deleteWorkflowInstance", parameters={})
mid_operator_Operator_m_startWorkflowInstance: Method = Method(name="startWorkflowInstance", parameters={Parameter(name='inputs'), Parameter(name='generics'), Parameter(name='workflowMID')}, type=StringType)
mid_operator_Operator_m_openWorkflowInstance: Method = Method(name="openWorkflowInstance", parameters={})
mid_operator_Operator_m_getInputProperties: Method = Method(name="getInputProperties", parameters={}, type=StringType)
mid_operator_Operator_m_readInputProperties: Method = Method(name="readInputProperties", parameters={Parameter(name='inputProperties')})
mid_operator_Operator_m_run: Method = Method(name="run", parameters={Parameter(name='genericsByName'), Parameter(name='inputsByName'), Parameter(name='outputMIDsByName')})
mid_operator_Operator_m_startInstance: Method = Method(name="startInstance", parameters={Parameter(name='instanceMID'), Parameter(name='generics'), Parameter(name='inputProperties'), Parameter(name='inputs'), Parameter(name='outputMIDsByName')}, type=StringType)
mid_operator_Operator.attributes={mid_operator_Operator_updateMID, mid_operator_Operator_inputSubdir, mid_operator_Operator_executionTime, mid_operator_Operator_commutative}
mid_operator_Operator.methods={mid_operator_Operator_m_selectAllowedGenerics, mid_operator_Operator_m_openInstance, mid_operator_Operator_m_getMIDContainer, mid_operator_Operator_m_getMetatype, mid_operator_Operator_m_checkAllowedInputs, mid_operator_Operator_m_findAllowedInputs, mid_operator_Operator_m_createWorkflowInstance, mid_operator_Operator_m_deleteInstance, mid_operator_Operator_m_deleteWorkflowInstance, mid_operator_Operator_m_getOutputsByName, mid_operator_Operator_m_openType, mid_operator_Operator_m_startInstance, mid_operator_Operator_m_run, mid_operator_Operator_m_getInputProperties, mid_operator_Operator_m_getSupertype, mid_operator_Operator_m_isAllowedGeneric, mid_operator_Operator_m_openWorkflowInstance, mid_operator_Operator_m_readInputProperties, mid_operator_Operator_m_startWorkflowInstance, mid_operator_Operator_m_findFirstAllowedInput, mid_operator_Operator_m_createSubtype, mid_operator_Operator_m_getOutputModels, mid_operator_Operator_m_createInstance, mid_operator_Operator_m_deleteType}

# mid_operator_WorkflowOperator class attributes and methods
mid_operator_WorkflowOperator_midUri: Property = Property(name="midUri", type=StringType)
mid_operator_WorkflowOperator_m_getWorkflowMID: Method = Method(name="getWorkflowMID", parameters={}, type=StringType)
mid_operator_WorkflowOperator_m_getInstanceMID: Method = Method(name="getInstanceMID", parameters={}, type=StringType)
mid_operator_WorkflowOperator.attributes={mid_operator_WorkflowOperator_midUri}
mid_operator_WorkflowOperator.methods={mid_operator_WorkflowOperator_m_getInstanceMID, mid_operator_WorkflowOperator_m_getWorkflowMID}

# operator_mid_ModelEndpoint class attributes and methods

# GenericEndpoint class attributes and methods

# mid_operator_ConversionOperator class attributes and methods
mid_operator_ConversionOperator_m_deleteType: Method = Method(name="deleteType", parameters={})
mid_operator_ConversionOperator_m_cleanup: Method = Method(name="cleanup", parameters={})
mid_operator_ConversionOperator.methods={mid_operator_ConversionOperator_m_cleanup, mid_operator_ConversionOperator_m_deleteType}

# mid_operator_RandomOperator class attributes and methods
mid_operator_RandomOperator_state: Property = Property(name="state", type=StringType)
mid_operator_RandomOperator.attributes={mid_operator_RandomOperator_state}

# mid_operator_OperatorGeneric class attributes and methods

# operator_mid_GenericElement class attributes and methods

# mid_operator_GenericEndpoint class attributes and methods
mid_operator_GenericEndpoint_metatargetUri: Property = Property(name="metatargetUri", type=StringType)
mid_operator_GenericEndpoint_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=StringType)
mid_operator_GenericEndpoint_m_getTarget: Method = Method(name="getTarget", parameters={}, type=GenericElement)
mid_operator_GenericEndpoint_m_setTarget: Method = Method(name="setTarget", parameters={Parameter(name='newTarget')})
mid_operator_GenericEndpoint_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_operator_GenericEndpoint_m_createInstance: Method = Method(name="createInstance", parameters={Parameter(name='targetGeneric'), Parameter(name='containerOperator')}, type=StringType)
mid_operator_GenericEndpoint_m_createWorkflowInstance: Method = Method(name="createWorkflowInstance", parameters={Parameter(name='containerOperator'), Parameter(name='targetGeneric')}, type=StringType)
mid_operator_GenericEndpoint.attributes={mid_operator_GenericEndpoint_metatargetUri}
mid_operator_GenericEndpoint.methods={mid_operator_GenericEndpoint_m_createWorkflowInstance, mid_operator_GenericEndpoint_m_getMetatype, mid_operator_GenericEndpoint_m_createInstance, mid_operator_GenericEndpoint_m_setTarget, mid_operator_GenericEndpoint_m_getTarget, mid_operator_GenericEndpoint_m_getSupertype}

# mid_operator_OperatorInput class attributes and methods

# operator_mid_Model class attributes and methods

# mid_operator_OperatorConstraint class attributes and methods

# ExtendibleElementConstraint class attributes and methods

# OperatorConstraintRule class attributes and methods

# mid_operator_OperatorConstraintRule class attributes and methods

# OperatorConstraintParameter class attributes and methods

# mid_operator_OperatorConstraintParameter class attributes and methods
mid_operator_OperatorConstraintParameter_endpointIndex: Property = Property(name="endpointIndex", type=IntegerType)
mid_operator_OperatorConstraintParameter.attributes={mid_operator_OperatorConstraintParameter_endpointIndex}

# Relationships
operators3: BinaryAssociation = BinaryAssociation(
    name="operators3",
    ends={
        Property(name="Operator", type=mid_MID, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_MID4", type=Operator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendibleTable5: BinaryAssociation = BinaryAssociation(
    name="extendibleTable5",
    ends={
        Property(name="mid_EStringToExtendibleElementMap", type=mid_MID, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_MID6", type=mid_EStringToExtendibleElementMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value7: BinaryAssociation = BinaryAssociation(
    name="value7",
    ends={
        Property(name="mid_ExtendibleElement", type=mid_EStringToExtendibleElementMap, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_EStringToExtendibleElementMap8", type=mid_ExtendibleElement, multiplicity=Multiplicity(1, 1))
    }
)
models0: BinaryAssociation = BinaryAssociation(
    name="models0",
    ends={
        Property(name="mid_Model", type=mid_MID, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_MID", type=mid_Model, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
editors1: BinaryAssociation = BinaryAssociation(
    name="editors1",
    ends={
        Property(name="Editor", type=mid_MID, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_MID2", type=Editor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supertype10: BinaryAssociation = BinaryAssociation(
    name="supertype10",
    ends={
        Property(name="mid_ExtendibleElement11", type=mid_ExtendibleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_ExtendibleElement9", type=mid_ExtendibleElement, multiplicity=Multiplicity(0, 1))
    }
)
constraint12: BinaryAssociation = BinaryAssociation(
    name="constraint12",
    ends={
        Property(name="mid_ExtendibleElementConstraint", type=mid_ExtendibleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_ExtendibleElement13", type=mid_ExtendibleElementConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="mid_ExtendibleElement15", type=mid_ExtendibleElementEndpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_ExtendibleElementEndpoint", type=mid_ExtendibleElement, multiplicity=Multiplicity(1, 1))
    }
)
editors16: BinaryAssociation = BinaryAssociation(
    name="editors16",
    ends={
        Property(name="Editor18", type=mid_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_Model17", type=Editor, multiplicity=Multiplicity(0, 9999))
    }
)
modelElems19: BinaryAssociation = BinaryAssociation(
    name="modelElems19",
    ends={
        Property(name="mid_ModelElement", type=mid_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_Model20", type=mid_ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversionOperators21: BinaryAssociation = BinaryAssociation(
    name="conversionOperators21",
    ends={
        Property(name="ConversionOperator", type=mid_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_Model22", type=ConversionOperator, multiplicity=Multiplicity(0, 9999))
    }
)
eInfo23: BinaryAssociation = BinaryAssociation(
    name="eInfo23",
    ends={
        Property(name="mid_EMFInfo", type=mid_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_ModelElement24", type=mid_EMFInfo, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modelEndpointRefs28: BinaryAssociation = BinaryAssociation(
    name="modelEndpointRefs28",
    ends={
        Property(name="ModelEndpointReference", type=mid_relationship_ModelRel, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_ModelRel29", type=ModelEndpointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappingRefs30: BinaryAssociation = BinaryAssociation(
    name="mappingRefs30",
    ends={
        Property(name="MappingReference", type=mid_relationship_ModelRel, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_ModelRel31", type=MappingReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelEndpoints25: BinaryAssociation = BinaryAssociation(
    name="modelEndpoints25",
    ends={
        Property(name="relationship_mid_ModelEndpoint", type=mid_relationship_ModelRel, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_ModelRel", type=relationship_mid_ModelEndpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappings26: BinaryAssociation = BinaryAssociation(
    name="mappings26",
    ends={
        Property(name="Mapping", type=mid_relationship_ModelRel, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_ModelRel27", type=Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supertypeRef40: BinaryAssociation = BinaryAssociation(
    name="supertypeRef40",
    ends={
        Property(name="ExtendibleElementReference", type=mid_relationship_ExtendibleElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_ExtendibleElementReference41", type=ExtendibleElementReference, multiplicity=Multiplicity(0, 1))
    }
)
sourceModel32: BinaryAssociation = BinaryAssociation(
    name="sourceModel32",
    ends={
        Property(name="relationship_mid_Model", type=mid_relationship_BinaryModelRel, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_BinaryModelRel", type=relationship_mid_Model, multiplicity=Multiplicity(1, 1))
    }
)
targetModel33: BinaryAssociation = BinaryAssociation(
    name="targetModel33",
    ends={
        Property(name="relationship_mid_Model35", type=mid_relationship_BinaryModelRel, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_BinaryModelRel34", type=relationship_mid_Model, multiplicity=Multiplicity(1, 1))
    }
)
referencedObject36: BinaryAssociation = BinaryAssociation(
    name="referencedObject36",
    ends={
        Property(name="relationship_mid_ExtendibleElement", type=mid_relationship_ExtendibleElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_ExtendibleElementReference", type=relationship_mid_ExtendibleElement, multiplicity=Multiplicity(0, 1))
    }
)
containedObject37: BinaryAssociation = BinaryAssociation(
    name="containedObject37",
    ends={
        Property(name="relationship_mid_ExtendibleElement39", type=mid_relationship_ExtendibleElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_ExtendibleElementReference38", type=relationship_mid_ExtendibleElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElemEndpointRefs43: BinaryAssociation = BinaryAssociation(
    name="modelElemEndpointRefs43",
    ends={
        Property(name="relationship", type=mid_relationship_ModelElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelElementEndpointReference", type=ModelElementEndpointReference, multiplicity=Multiplicity(0, 9999))
    }
)
modelElemRefs42: BinaryAssociation = BinaryAssociation(
    name="modelElemRefs42",
    ends={
        Property(name="ModelElementReference", type=mid_relationship_ModelEndpointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_ModelEndpointReference", type=ModelElementReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelElemEndpointRefs45: BinaryAssociation = BinaryAssociation(
    name="modelElemEndpointRefs45",
    ends={
        Property(name="ModelElementEndpointReference47", type=mid_relationship_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_Mapping46", type=ModelElementEndpointReference, multiplicity=Multiplicity(0, 9999))
    }
)
modelElemEndpoints44: BinaryAssociation = BinaryAssociation(
    name="modelElemEndpoints44",
    ends={
        Property(name="ModelElementEndpoint", type=mid_relationship_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_Mapping", type=ModelElementEndpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelElemRef55: BinaryAssociation = BinaryAssociation(
    name="modelElemRef55",
    ends={
        Property(name="relationship57", type=mid_relationship_ModelElementEndpointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ModelElementReference56", type=ModelElementReference, multiplicity=Multiplicity(1, 1))
    }
)
modelElemEndpointRefs48: BinaryAssociation = BinaryAssociation(
    name="modelElemEndpointRefs48",
    ends={
        Property(name="ModelElementEndpointReference49", type=mid_relationship_MappingReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_MappingReference", type=ModelElementEndpointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceModelElemRef50: BinaryAssociation = BinaryAssociation(
    name="sourceModelElemRef50",
    ends={
        Property(name="ModelElementReference51", type=mid_relationship_BinaryMappingReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_BinaryMappingReference", type=ModelElementReference, multiplicity=Multiplicity(1, 1))
    }
)
targetModelElemRef52: BinaryAssociation = BinaryAssociation(
    name="targetModelElemRef52",
    ends={
        Property(name="ModelElementReference54", type=mid_relationship_BinaryMappingReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_BinaryMappingReference53", type=ModelElementReference, multiplicity=Multiplicity(1, 1))
    }
)
inputs58: BinaryAssociation = BinaryAssociation(
    name="inputs58",
    ends={
        Property(name="operator_mid_ModelEndpoint", type=mid_operator_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_Operator", type=operator_mid_ModelEndpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs59: BinaryAssociation = BinaryAssociation(
    name="outputs59",
    ends={
        Property(name="operator_mid_ModelEndpoint61", type=mid_operator_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_Operator60", type=operator_mid_ModelEndpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generics62: BinaryAssociation = BinaryAssociation(
    name="generics62",
    ends={
        Property(name="GenericEndpoint", type=mid_operator_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_Operator63", type=GenericEndpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
previousOperator64: BinaryAssociation = BinaryAssociation(
    name="previousOperator64",
    ends={
        Property(name="Operator66", type=mid_operator_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_Operator65", type=Operator, multiplicity=Multiplicity(0, 1))
    }
)
modelTypeEndpoint71: BinaryAssociation = BinaryAssociation(
    name="modelTypeEndpoint71",
    ends={
        Property(name="operator_mid_ModelEndpoint73", type=mid_operator_OperatorInput, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_OperatorInput72", type=operator_mid_ModelEndpoint, multiplicity=Multiplicity(1, 1))
    }
)
generic74: BinaryAssociation = BinaryAssociation(
    name="generic74",
    ends={
        Property(name="operator_mid_GenericElement", type=mid_operator_OperatorGeneric, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_OperatorGeneric", type=operator_mid_GenericElement, multiplicity=Multiplicity(1, 1))
    }
)
genericSuperTypeEndpoint75: BinaryAssociation = BinaryAssociation(
    name="genericSuperTypeEndpoint75",
    ends={
        Property(name="GenericEndpoint77", type=mid_operator_OperatorGeneric, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_OperatorGeneric76", type=GenericEndpoint, multiplicity=Multiplicity(1, 1))
    }
)
model67: BinaryAssociation = BinaryAssociation(
    name="model67",
    ends={
        Property(name="operator_mid_Model", type=mid_operator_OperatorInput, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_OperatorInput", type=operator_mid_Model, multiplicity=Multiplicity(1, 1))
    }
)
conversions68: BinaryAssociation = BinaryAssociation(
    name="conversions68",
    ends={
        Property(name="ConversionOperator70", type=mid_operator_OperatorInput, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_OperatorInput69", type=ConversionOperator, multiplicity=Multiplicity(0, 9999))
    }
)
rules78: BinaryAssociation = BinaryAssociation(
    name="rules78",
    ends={
        Property(name="OperatorConstraintRule", type=mid_operator_OperatorConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_OperatorConstraint", type=OperatorConstraintRule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outputModelRel79: BinaryAssociation = BinaryAssociation(
    name="outputModelRel79",
    ends={
        Property(name="OperatorConstraintParameter", type=mid_operator_OperatorConstraintRule, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_OperatorConstraintRule", type=OperatorConstraintParameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
endpointModels80: BinaryAssociation = BinaryAssociation(
    name="endpointModels80",
    ends={
        Property(name="OperatorConstraintParameter82", type=mid_operator_OperatorConstraintRule, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_OperatorConstraintRule81", type=OperatorConstraintParameter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parameterRef83: BinaryAssociation = BinaryAssociation(
    name="parameterRef83",
    ends={
        Property(name="ModelEndpointReference84", type=mid_operator_OperatorConstraintParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_OperatorConstraintParameter", type=ModelEndpointReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_mid_Model_GenericElement = Generalization(general=GenericElement, specific=mid_Model)
gen_mid_ExtendibleElementEndpoint_ExtendibleElement = Generalization(general=ExtendibleElement, specific=mid_ExtendibleElementEndpoint)
gen_mid_ModelElement_ExtendibleElement = Generalization(general=ExtendibleElement, specific=mid_ModelElement)
gen_mid_ModelEndpoint_ExtendibleElementEndpoint = Generalization(general=ExtendibleElementEndpoint, specific=mid_ModelEndpoint)
gen_mid_GenericElement_ExtendibleElement = Generalization(general=ExtendibleElement, specific=mid_GenericElement)
gen_mid_relationship_ModelRel_Model = Generalization(general=Model, specific=mid_relationship_ModelRel)
gen_mid_relationship_BinaryModelRel_ModelRel = Generalization(general=ModelRel, specific=mid_relationship_BinaryModelRel)
gen_mid_relationship_ExtendibleElementEndpointReference_ExtendibleElementReference = Generalization(general=ExtendibleElementReference, specific=mid_relationship_ExtendibleElementEndpointReference)
gen_mid_relationship_Mapping_ExtendibleElement = Generalization(general=ExtendibleElement, specific=mid_relationship_Mapping)
gen_mid_relationship_ModelEndpointReference_ExtendibleElementEndpointReference = Generalization(general=ExtendibleElementEndpointReference, specific=mid_relationship_ModelEndpointReference)
gen_mid_relationship_ModelElementReference_ExtendibleElementReference = Generalization(general=ExtendibleElementReference, specific=mid_relationship_ModelElementReference)
gen_mid_relationship_BinaryMapping_Mapping = Generalization(general=Mapping, specific=mid_relationship_BinaryMapping)
gen_mid_relationship_ModelElementEndpoint_ExtendibleElementEndpoint = Generalization(general=ExtendibleElementEndpoint, specific=mid_relationship_ModelElementEndpoint)
gen_mid_relationship_MappingReference_ExtendibleElementReference = Generalization(general=ExtendibleElementReference, specific=mid_relationship_MappingReference)
gen_mid_editor_Editor_ExtendibleElement = Generalization(general=ExtendibleElement, specific=mid_editor_Editor)
gen_mid_relationship_BinaryMappingReference_MappingReference = Generalization(general=MappingReference, specific=mid_relationship_BinaryMappingReference)
gen_mid_relationship_ModelElementEndpointReference_ExtendibleElementEndpointReference = Generalization(general=ExtendibleElementEndpointReference, specific=mid_relationship_ModelElementEndpointReference)
gen_mid_editor_Diagram_Editor = Generalization(general=Editor, specific=mid_editor_Diagram)
gen_mid_operator_Operator_GenericElement = Generalization(general=GenericElement, specific=mid_operator_Operator)
gen_mid_operator_WorkflowOperator_Operator = Generalization(general=Operator, specific=mid_operator_WorkflowOperator)
gen_mid_operator_ConversionOperator_Operator = Generalization(general=Operator, specific=mid_operator_ConversionOperator)
gen_mid_operator_RandomOperator_Operator = Generalization(general=Operator, specific=mid_operator_RandomOperator)
gen_mid_operator_GenericEndpoint_ExtendibleElementEndpoint = Generalization(general=ExtendibleElementEndpoint, specific=mid_operator_GenericEndpoint)
gen_mid_operator_OperatorConstraint_ExtendibleElementConstraint = Generalization(general=ExtendibleElementConstraint, specific=mid_operator_OperatorConstraint)

# Domain Model
domain_model = DomainModel(
    name="mid",
    types={mid_MID, Operator, mid_EStringToExtendibleElementMap, mid_ExtendibleElement, mid_Model, Editor, mid_ExtendibleElementConstraint, GenericElement, mid_ExtendibleElementEndpoint, ExtendibleElement, mid_ModelElement, ConversionOperator, mid_ModelEndpoint, ExtendibleElementEndpoint, mid_EMFInfo, mid_GenericElement, mid_relationship_ModelRel, Model, ModelEndpointReference, MappingReference, mid_relationship_BinaryModelRel, ModelRel, relationship_mid_ModelEndpoint, Mapping, ExtendibleElementReference, mid_relationship_ExtendibleElementEndpointReference, relationship_mid_Model, mid_relationship_ExtendibleElementReference, relationship_mid_ExtendibleElement, ModelElementEndpointReference, mid_relationship_Mapping, mid_relationship_ModelEndpointReference, ExtendibleElementEndpointReference, ModelElementReference, mid_relationship_ModelElementReference, mid_relationship_BinaryMapping, mid_relationship_ModelElementEndpoint, ModelElementEndpoint, mid_relationship_MappingReference, mid_editor_Editor, mid_relationship_BinaryMappingReference, mid_relationship_ModelElementEndpointReference, mid_editor_Diagram, mid_operator_Operator, mid_operator_WorkflowOperator, operator_mid_ModelEndpoint, GenericEndpoint, mid_operator_ConversionOperator, mid_operator_RandomOperator, mid_operator_OperatorGeneric, operator_mid_GenericElement, mid_operator_GenericEndpoint, mid_operator_OperatorInput, operator_mid_Model, mid_operator_OperatorConstraint, ExtendibleElementConstraint, OperatorConstraintRule, mid_operator_OperatorConstraintRule, OperatorConstraintParameter, mid_operator_OperatorConstraintParameter, MIDLevel, ModelOrigin},
    associations={operators3, extendibleTable5, value7, models0, editors1, supertype10, constraint12, target14, editors16, modelElems19, conversionOperators21, eInfo23, modelEndpointRefs28, mappingRefs30, modelEndpoints25, mappings26, supertypeRef40, sourceModel32, targetModel33, referencedObject36, containedObject37, modelElemEndpointRefs43, modelElemRefs42, modelElemEndpointRefs45, modelElemEndpoints44, modelElemRef55, modelElemEndpointRefs48, sourceModelElemRef50, targetModelElemRef52, inputs58, outputs59, generics62, previousOperator64, modelTypeEndpoint71, generic74, genericSuperTypeEndpoint75, model67, conversions68, rules78, outputModelRel79, endpointModels80, parameterRef83},
    generalizations={gen_mid_Model_GenericElement, gen_mid_ExtendibleElementEndpoint_ExtendibleElement, gen_mid_ModelElement_ExtendibleElement, gen_mid_ModelEndpoint_ExtendibleElementEndpoint, gen_mid_GenericElement_ExtendibleElement, gen_mid_relationship_ModelRel_Model, gen_mid_relationship_BinaryModelRel_ModelRel, gen_mid_relationship_ExtendibleElementEndpointReference_ExtendibleElementReference, gen_mid_relationship_Mapping_ExtendibleElement, gen_mid_relationship_ModelEndpointReference_ExtendibleElementEndpointReference, gen_mid_relationship_ModelElementReference_ExtendibleElementReference, gen_mid_relationship_BinaryMapping_Mapping, gen_mid_relationship_ModelElementEndpoint_ExtendibleElementEndpoint, gen_mid_relationship_MappingReference_ExtendibleElementReference, gen_mid_editor_Editor_ExtendibleElement, gen_mid_relationship_BinaryMappingReference_MappingReference, gen_mid_relationship_ModelElementEndpointReference_ExtendibleElementEndpointReference, gen_mid_editor_Diagram_Editor, gen_mid_operator_Operator_GenericElement, gen_mid_operator_WorkflowOperator_Operator, gen_mid_operator_ConversionOperator_Operator, gen_mid_operator_RandomOperator_Operator, gen_mid_operator_GenericEndpoint_ExtendibleElementEndpoint, gen_mid_operator_OperatorConstraint_ExtendibleElementConstraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
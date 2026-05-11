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
mid_Model = Class(name="mid_Model")
Editor = Class(name="Editor")
Operator = Class(name="Operator")
mid_EStringToExtendibleElementMap = Class(name="mid_EStringToExtendibleElementMap")
mid_MID = Class(name="mid_MID")
mid_ExtendibleElement = Class(name="mid_ExtendibleElement", is_abstract=True)
mid_ExtendibleElementEndpoint = Class(name="mid_ExtendibleElementEndpoint", is_abstract=True)
ExtendibleElement = Class(name="ExtendibleElement")
mid_ExtendibleElementConstraint = Class(name="mid_ExtendibleElementConstraint")
GenericElement = Class(name="GenericElement")
mid_ModelElement = Class(name="mid_ModelElement")
ConversionOperator = Class(name="ConversionOperator")
mid_EMFInfo = Class(name="mid_EMFInfo")
mid_ModelEndpoint = Class(name="mid_ModelEndpoint")
ExtendibleElementEndpoint = Class(name="ExtendibleElementEndpoint")
mid_GenericElement = Class(name="mid_GenericElement", is_abstract=True)
mid_relationship_ModelRel = Class(name="mid_relationship_ModelRel")
Model = Class(name="Model")
relationship_mid_ModelEndpoint = Class(name="relationship_mid_ModelEndpoint")
Mapping = Class(name="Mapping")
ModelEndpointReference = Class(name="ModelEndpointReference")
MappingReference = Class(name="MappingReference")
mid_relationship_BinaryModelRel = Class(name="mid_relationship_BinaryModelRel")
ModelRel = Class(name="ModelRel")
relationship_mid_Model = Class(name="relationship_mid_Model")
mid_relationship_ExtendibleElementReference = Class(name="mid_relationship_ExtendibleElementReference", is_abstract=True)
relationship_mid_ExtendibleElement = Class(name="relationship_mid_ExtendibleElement")
ExtendibleElementReference = Class(name="ExtendibleElementReference")
mid_relationship_ExtendibleElementEndpointReference = Class(name="mid_relationship_ExtendibleElementEndpointReference", is_abstract=True)
mid_relationship_ModelEndpointReference = Class(name="mid_relationship_ModelEndpointReference")
ExtendibleElementEndpointReference = Class(name="ExtendibleElementEndpointReference")
ModelElementReference = Class(name="ModelElementReference")
mid_relationship_ModelElementReference = Class(name="mid_relationship_ModelElementReference")
ModelElementEndpointReference = Class(name="ModelElementEndpointReference")
mid_relationship_Mapping = Class(name="mid_relationship_Mapping")
ModelElementEndpoint = Class(name="ModelElementEndpoint")
mid_relationship_BinaryMapping = Class(name="mid_relationship_BinaryMapping")
mid_relationship_ModelElementEndpoint = Class(name="mid_relationship_ModelElementEndpoint")
mid_relationship_BinaryMappingReference = Class(name="mid_relationship_BinaryMappingReference")
mid_relationship_MappingReference = Class(name="mid_relationship_MappingReference")
mid_editor_Editor = Class(name="mid_editor_Editor")
mid_relationship_ModelElementEndpointReference = Class(name="mid_relationship_ModelElementEndpointReference")
mid_editor_Diagram = Class(name="mid_editor_Diagram")
mid_operator_Operator = Class(name="mid_operator_Operator")
mid_operator_ConversionOperator = Class(name="mid_operator_ConversionOperator")
mid_operator_RandomOperator = Class(name="mid_operator_RandomOperator")
mid_operator_WorkflowOperator = Class(name="mid_operator_WorkflowOperator")
operator_mid_ModelEndpoint = Class(name="operator_mid_ModelEndpoint")
GenericEndpoint = Class(name="GenericEndpoint")
mid_operator_OperatorInput = Class(name="mid_operator_OperatorInput")
operator_mid_Model = Class(name="operator_mid_Model")
mid_operator_OperatorGeneric = Class(name="mid_operator_OperatorGeneric")
operator_mid_GenericElement = Class(name="operator_mid_GenericElement")
mid_operator_GenericEndpoint = Class(name="mid_operator_GenericEndpoint")
mid_operator_OperatorConstraint = Class(name="mid_operator_OperatorConstraint")
ExtendibleElementConstraint = Class(name="ExtendibleElementConstraint")
OperatorConstraintRule = Class(name="OperatorConstraintRule")
mid_operator_OperatorConstraintRule = Class(name="mid_operator_OperatorConstraintRule")
OperatorConstraintParameter = Class(name="OperatorConstraintParameter")
mid_operator_OperatorConstraintParameter = Class(name="mid_operator_OperatorConstraintParameter")

# mid_Model class attributes and methods
mid_Model_origin: Property = Property(name="origin", type=StringType)
mid_Model_fileExtension: Property = Property(name="fileExtension", type=StringType)
mid_Model_m_createInstance: Method = Method(name="createInstance", parameters={Parameter(name='mid_instanceMID', type=StringType), Parameter(name='mid_newModelUri', type=StringType)}, type=StringType)
mid_Model_m_createInstanceEditor: Method = Method(name="createInstanceEditor", parameters={}, type=StringType)
mid_Model_m_createInstanceAndEditor: Method = Method(name="createInstanceAndEditor", parameters={Parameter(name='mid_newModelUri', type=StringType), Parameter(name='mid_instanceMID', type=StringType)}, type=StringType)
mid_Model_m_importInstance: Method = Method(name="importInstance", parameters={Parameter(name='mid_modelUri', type=StringType), Parameter(name='mid_instanceMID', type=StringType)}, type=StringType)
mid_Model_m_importInstanceAndEditor: Method = Method(name="importInstanceAndEditor", parameters={Parameter(name='mid_instanceMID', type=StringType), Parameter(name='mid_modelUri', type=StringType)}, type=StringType)
mid_Model_m_copyInstance: Method = Method(name="copyInstance", parameters={Parameter(name='mid_instanceMID', type=StringType), Parameter(name='mid_newModelName', type=StringType), Parameter(name='mid_origModel', type=StringType)}, type=StringType)
mid_Model_m_copyInstanceAndEditor: Method = Method(name="copyInstanceAndEditor", parameters={Parameter(name='mid_origModel', type=StringType), Parameter(name='mid_instanceMID', type=StringType), Parameter(name='mid_newModelName', type=StringType), Parameter(name='mid_copyDiagram', type=StringType)}, type=StringType)
mid_Model_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_Model_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=StringType)
mid_Model_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_Model_m_createSubtype: Method = Method(name="createSubtype", parameters={Parameter(name='mid_isMetamodelExtension', type=StringType), Parameter(name='mid_newModelTypeName', type=StringType)}, type=StringType)
mid_Model_m_deleteType: Method = Method(name="deleteType", parameters={})
mid_Model_m_getEMFTypeRoot: Method = Method(name="getEMFTypeRoot", parameters={}, type=StringType)
mid_Model_m_openType: Method = Method(name="openType", parameters={})
mid_Model_m_deleteInstance: Method = Method(name="deleteInstance", parameters={})
mid_Model_m_deleteInstanceAndFile: Method = Method(name="deleteInstanceAndFile", parameters={})
mid_Model_m_getEMFInstanceRoot: Method = Method(name="getEMFInstanceRoot", parameters={}, type=StringType)
mid_Model_m_openInstance: Method = Method(name="openInstance", parameters={})
mid_Model_m_createWorkflowInstance: Method = Method(name="createWorkflowInstance", parameters={Parameter(name='mid_newModelId', type=StringType), Parameter(name='mid_workflowMID', type=StringType)}, type=StringType)
mid_Model_m_deleteWorkflowInstance: Method = Method(name="deleteWorkflowInstance", parameters={})
mid_Model.attributes={mid_Model_fileExtension, mid_Model_origin}
mid_Model.methods={mid_Model_m_createInstanceAndEditor, mid_Model_m_openInstance, mid_Model_m_createInstance, mid_Model_m_getEMFInstanceRoot, mid_Model_m_createWorkflowInstance, mid_Model_m_createInstanceEditor, mid_Model_m_getMIDContainer, mid_Model_m_deleteInstance, mid_Model_m_openType, mid_Model_m_copyInstance, mid_Model_m_createSubtype, mid_Model_m_copyInstanceAndEditor, mid_Model_m_getMetatype, mid_Model_m_deleteWorkflowInstance, mid_Model_m_getEMFTypeRoot, mid_Model_m_deleteInstanceAndFile, mid_Model_m_getSupertype, mid_Model_m_deleteType, mid_Model_m_importInstanceAndEditor, mid_Model_m_importInstance}

# Editor class attributes and methods

# Operator class attributes and methods

# mid_EStringToExtendibleElementMap class attributes and methods
mid_EStringToExtendibleElementMap_key: Property = Property(name="key", type=StringType)
mid_EStringToExtendibleElementMap.attributes={mid_EStringToExtendibleElementMap_key}

# mid_MID class attributes and methods
mid_MID_level: Property = Property(name="level", type=StringType)
mid_MID_m_getModelRels: Method = Method(name="getModelRels", parameters={}, type=StringType)
mid_MID_m_isTypesLevel: Method = Method(name="isTypesLevel", parameters={}, type=BooleanType)
mid_MID_m_isInstancesLevel: Method = Method(name="isInstancesLevel", parameters={}, type=BooleanType)
mid_MID_m_isWorkflowsLevel: Method = Method(name="isWorkflowsLevel", parameters={}, type=BooleanType)
mid_MID_m_getExtendibleElement: Method = Method(name="getExtendibleElement", parameters={Parameter(name='mid_uri', type=StringType)})
mid_MID.attributes={mid_MID_level}
mid_MID.methods={mid_MID_m_isTypesLevel, mid_MID_m_getModelRels, mid_MID_m_isInstancesLevel, mid_MID_m_isWorkflowsLevel, mid_MID_m_getExtendibleElement}

# mid_ExtendibleElement class attributes and methods
mid_ExtendibleElement_uri: Property = Property(name="uri", type=StringType)
mid_ExtendibleElement_name: Property = Property(name="name", type=StringType)
mid_ExtendibleElement_level: Property = Property(name="level", type=StringType)
mid_ExtendibleElement_metatypeUri: Property = Property(name="metatypeUri", type=StringType)
mid_ExtendibleElement_dynamic: Property = Property(name="dynamic", type=BooleanType)
mid_ExtendibleElement_m_createSubtypeUri: Method = Method(name="createSubtypeUri", parameters={Parameter(name='mid_newTypeFragmentUri', type=StringType), Parameter(name='mid_newTypeName', type=StringType)}, type=StringType)
mid_ExtendibleElement_m_addTypeConstraint: Method = Method(name="addTypeConstraint", parameters={Parameter(name='mid_language', type=StringType), Parameter(name='mid_implementation', type=StringType)})
mid_ExtendibleElement_m_isInstancesLevel: Method = Method(name="isInstancesLevel", parameters={}, type=BooleanType)
mid_ExtendibleElement_m_getRuntimeTypes: Method = Method(name="getRuntimeTypes", parameters={})
mid_ExtendibleElement_m_validateInstanceType: Method = Method(name="validateInstanceType", parameters={Parameter(name='mid_type', type=StringType)}, type=BooleanType)
mid_ExtendibleElement_m_validateInstance: Method = Method(name="validateInstance", parameters={}, type=BooleanType)
mid_ExtendibleElement_m_validateInstanceInEditor: Method = Method(name="validateInstanceInEditor", parameters={Parameter(name='mid_context', type=StringType)}, type=StringType)
mid_ExtendibleElement_m_isWorkflowsLevel: Method = Method(name="isWorkflowsLevel", parameters={}, type=BooleanType)
mid_ExtendibleElement_m_updateWorkflowInstanceId: Method = Method(name="updateWorkflowInstanceId", parameters={Parameter(name='mid_newInstanceId', type=StringType)})
mid_ExtendibleElement_m_toMIDCustomPrintLabel: Method = Method(name="toMIDCustomPrintLabel", parameters={}, type=StringType)
mid_ExtendibleElement_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_ExtendibleElement_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_ExtendibleElement_m_isLevel: Method = Method(name="isLevel", parameters={Parameter(name='mid_midLevel', type=StringType)}, type=BooleanType)
mid_ExtendibleElement_m_isTypesLevel: Method = Method(name="isTypesLevel", parameters={}, type=BooleanType)
mid_ExtendibleElement_m_toMIDCustomEditLabel: Method = Method(name="toMIDCustomEditLabel", parameters={}, type=StringType)
mid_ExtendibleElement_m_updateMIDCustomLabel: Method = Method(name="updateMIDCustomLabel", parameters={Parameter(name='mid_newLabel', type=StringType)})
mid_ExtendibleElement.attributes={mid_ExtendibleElement_name, mid_ExtendibleElement_level, mid_ExtendibleElement_dynamic, mid_ExtendibleElement_uri, mid_ExtendibleElement_metatypeUri}
mid_ExtendibleElement.methods={mid_ExtendibleElement_m_isTypesLevel, mid_ExtendibleElement_m_updateMIDCustomLabel, mid_ExtendibleElement_m_addTypeConstraint, mid_ExtendibleElement_m_getMetatype, mid_ExtendibleElement_m_validateInstanceInEditor, mid_ExtendibleElement_m_updateWorkflowInstanceId, mid_ExtendibleElement_m_toMIDCustomEditLabel, mid_ExtendibleElement_m_isLevel, mid_ExtendibleElement_m_getMIDContainer, mid_ExtendibleElement_m_validateInstance, mid_ExtendibleElement_m_createSubtypeUri, mid_ExtendibleElement_m_isInstancesLevel, mid_ExtendibleElement_m_getRuntimeTypes, mid_ExtendibleElement_m_toMIDCustomPrintLabel, mid_ExtendibleElement_m_validateInstanceType, mid_ExtendibleElement_m_isWorkflowsLevel}

# mid_ExtendibleElementEndpoint class attributes and methods
mid_ExtendibleElementEndpoint_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
mid_ExtendibleElementEndpoint_upperBound: Property = Property(name="upperBound", type=IntegerType)
mid_ExtendibleElementEndpoint_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_ExtendibleElementEndpoint_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=StringType)
mid_ExtendibleElementEndpoint_m_getTargetUri: Method = Method(name="getTargetUri", parameters={}, type=StringType)
mid_ExtendibleElementEndpoint.attributes={mid_ExtendibleElementEndpoint_lowerBound, mid_ExtendibleElementEndpoint_upperBound}
mid_ExtendibleElementEndpoint.methods={mid_ExtendibleElementEndpoint_m_getSupertype, mid_ExtendibleElementEndpoint_m_getTargetUri, mid_ExtendibleElementEndpoint_m_getMetatype}

# ExtendibleElement class attributes and methods

# mid_ExtendibleElementConstraint class attributes and methods
mid_ExtendibleElementConstraint_implementation: Property = Property(name="implementation", type=StringType)
mid_ExtendibleElementConstraint_language: Property = Property(name="language", type=StringType)
mid_ExtendibleElementConstraint.attributes={mid_ExtendibleElementConstraint_language, mid_ExtendibleElementConstraint_implementation}

# GenericElement class attributes and methods

# mid_ModelElement class attributes and methods
mid_ModelElement_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_ModelElement_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=StringType)
mid_ModelElement_m_deleteInstance: Method = Method(name="deleteInstance", parameters={})
mid_ModelElement_m_getEMFInstanceObject: Method = Method(name="getEMFInstanceObject", parameters={}, type=StringType)
mid_ModelElement_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_ModelElement_m_createTypeReference: Method = Method(name="createTypeReference", parameters={Parameter(name='mid_modelElemTypeRef', type=StringType), Parameter(name='mid_containerModelTypeEndpointRef', type=StringType), Parameter(name='mid_isModifiable', type=StringType)}, type=StringType)
mid_ModelElement_m_createSubtypeAndReference: Method = Method(name="createSubtypeAndReference", parameters={Parameter(name='mid_modelElemTypeRef', type=StringType), Parameter(name='mid_newModelElemTypeName', type=StringType), Parameter(name='mid_containerModelTypeEndpointRef', type=StringType), Parameter(name='mid_newModelElemTypeUri', type=StringType), Parameter(name='mid_eInfo', type=StringType)}, type=StringType)
mid_ModelElement_m_deleteType: Method = Method(name="deleteType", parameters={})
mid_ModelElement_m_getEMFTypeObject: Method = Method(name="getEMFTypeObject", parameters={}, type=StringType)
mid_ModelElement_m_createInstanceReference: Method = Method(name="createInstanceReference", parameters={Parameter(name='mid_containerModelEndpointRef', type=StringType)}, type=StringType)
mid_ModelElement_m_createInstanceAndReference: Method = Method(name="createInstanceAndReference", parameters={Parameter(name='mid_newModelElemName', type=StringType), Parameter(name='mid_newModelElemUri', type=StringType), Parameter(name='mid_containerModelEndpointRef', type=StringType), Parameter(name='mid_eInfo', type=StringType)}, type=StringType)
mid_ModelElement.methods={mid_ModelElement_m_createInstanceAndReference, mid_ModelElement_m_createSubtypeAndReference, mid_ModelElement_m_deleteType, mid_ModelElement_m_getEMFTypeObject, mid_ModelElement_m_createTypeReference, mid_ModelElement_m_deleteInstance, mid_ModelElement_m_getMIDContainer, mid_ModelElement_m_createInstanceReference, mid_ModelElement_m_getSupertype, mid_ModelElement_m_getMetatype, mid_ModelElement_m_getEMFInstanceObject}

# ConversionOperator class attributes and methods

# mid_EMFInfo class attributes and methods
mid_EMFInfo_className: Property = Property(name="className", type=StringType)
mid_EMFInfo_featureName: Property = Property(name="featureName", type=StringType)
mid_EMFInfo_attribute: Property = Property(name="attribute", type=BooleanType)
mid_EMFInfo_relatedClassName: Property = Property(name="relatedClassName", type=StringType)
mid_EMFInfo_m_toTypeString: Method = Method(name="toTypeString", parameters={}, type=StringType)
mid_EMFInfo_m_toInstanceString: Method = Method(name="toInstanceString", parameters={}, type=StringType)
mid_EMFInfo.attributes={mid_EMFInfo_relatedClassName, mid_EMFInfo_featureName, mid_EMFInfo_className, mid_EMFInfo_attribute}
mid_EMFInfo.methods={mid_EMFInfo_m_toTypeString, mid_EMFInfo_m_toInstanceString}

# mid_ModelEndpoint class attributes and methods
mid_ModelEndpoint_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_ModelEndpoint_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=StringType)
mid_ModelEndpoint_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_ModelEndpoint_m_getTarget: Method = Method(name="getTarget", parameters={}, type=StringType)
mid_ModelEndpoint_m_createTypeReference: Method = Method(name="createTypeReference", parameters={Parameter(name='mid_containerModelRelType', type=StringType), Parameter(name='mid_isModifiable', type=StringType)}, type=StringType)
mid_ModelEndpoint_m_createSubtype: Method = Method(name="createSubtype", parameters={Parameter(name='mid_targetModelType', type=StringType), Parameter(name='mid_containerModelRelType', type=StringType), Parameter(name='mid_newModelTypeEndpointName', type=StringType), Parameter(name='mid_isBinarySrc', type=StringType)}, type=StringType)
mid_ModelEndpoint_m_replaceSubtype: Method = Method(name="replaceSubtype", parameters={Parameter(name='mid_targetModelType', type=StringType), Parameter(name='mid_oldModelTypeEndpoint', type=StringType), Parameter(name='mid_newModelTypeEndpointName', type=StringType)})
mid_ModelEndpoint_m_deleteType: Method = Method(name="deleteType", parameters={Parameter(name='mid_isFullDelete', type=StringType)})
mid_ModelEndpoint_m_createInstanceReference: Method = Method(name="createInstanceReference", parameters={Parameter(name='mid_containerModelRel', type=StringType)}, type=StringType)
mid_ModelEndpoint_m_createInstance: Method = Method(name="createInstance", parameters={Parameter(name='mid_containerModelRel', type=StringType), Parameter(name='mid_targetModel', type=StringType)}, type=StringType)
mid_ModelEndpoint_m_replaceInstance: Method = Method(name="replaceInstance", parameters={Parameter(name='mid_targetModel', type=StringType), Parameter(name='mid_oldModelEndpoint', type=StringType)})
mid_ModelEndpoint_m_deleteInstance: Method = Method(name="deleteInstance", parameters={Parameter(name='mid_isFullDelete', type=StringType)})
mid_ModelEndpoint_m_createWorkflowInstance: Method = Method(name="createWorkflowInstance", parameters={Parameter(name='mid_containerModelRel', type=StringType), Parameter(name='mid_targetModel', type=StringType)}, type=StringType)
mid_ModelEndpoint_m_createWorkflowInstance: Method = Method(name="createWorkflowInstance", parameters={Parameter(name='mid_targetModel', type=StringType), Parameter(name='mid_containerOperator', type=StringType), Parameter(name='mid_containerFeatureName', type=StringType)}, type=StringType)
mid_ModelEndpoint_m_replaceWorkflowInstance: Method = Method(name="replaceWorkflowInstance", parameters={Parameter(name='mid_targetModel', type=StringType), Parameter(name='mid_oldModelEndpoint', type=StringType)})
mid_ModelEndpoint_m_deleteWorkflowInstance: Method = Method(name="deleteWorkflowInstance", parameters={})
mid_ModelEndpoint_m_createInstance: Method = Method(name="createInstance", parameters={Parameter(name='mid_containerFeatureName', type=StringType), Parameter(name='mid_targetModel', type=StringType), Parameter(name='mid_containerOperator', type=StringType)}, type=StringType)
mid_ModelEndpoint.methods={mid_ModelEndpoint_m_replaceInstance, mid_ModelEndpoint_m_createTypeReference, mid_ModelEndpoint_m_createWorkflowInstance, mid_ModelEndpoint_m_getTarget, mid_ModelEndpoint_m_deleteWorkflowInstance, mid_ModelEndpoint_m_deleteType, mid_ModelEndpoint_m_createSubtype, mid_ModelEndpoint_m_deleteInstance, mid_ModelEndpoint_m_createInstanceReference, mid_ModelEndpoint_m_getSupertype, mid_ModelEndpoint_m_createWorkflowInstance, mid_ModelEndpoint_m_createInstance, mid_ModelEndpoint_m_getMetatype, mid_ModelEndpoint_m_createInstance, mid_ModelEndpoint_m_replaceWorkflowInstance, mid_ModelEndpoint_m_getMIDContainer, mid_ModelEndpoint_m_replaceSubtype}

# ExtendibleElementEndpoint class attributes and methods

# mid_GenericElement class attributes and methods
mid_GenericElement_abstract: Property = Property(name="abstract", type=BooleanType)
mid_GenericElement.attributes={mid_GenericElement_abstract}

# mid_relationship_ModelRel class attributes and methods
mid_relationship_ModelRel_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_relationship_ModelRel_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=Model)
mid_relationship_ModelRel_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_relationship_ModelRel_m_createBinarySubtype: Method = Method(name="createBinarySubtype", parameters={Parameter(name='mid_isMetamodelExtension', type=StringType), Parameter(name='mid_newModelRelTypeName', type=StringType)}, type=StringType)
mid_relationship_ModelRel_m_copySubtype: Method = Method(name="copySubtype", parameters={Parameter(name='mid_origModelRelType', type=StringType)}, type=StringType)
mid_relationship_ModelRel_m_getOutlineResourceTypes: Method = Method(name="getOutlineResourceTypes", parameters={}, type=StringType)
mid_relationship_ModelRel_m_createInstanceAndEndpoints: Method = Method(name="createInstanceAndEndpoints", parameters={Parameter(name='mid_endpointModels', type=StringType), Parameter(name='mid_instanceMID', type=StringType), Parameter(name='mid_newModelRelUri', type=StringType)}, type=StringType)
mid_relationship_ModelRel_m_createBinaryInstance: Method = Method(name="createBinaryInstance", parameters={Parameter(name='mid_newModelRelUri', type=StringType), Parameter(name='mid_instanceMID', type=StringType)}, type=StringType)
mid_relationship_ModelRel_m_createBinaryInstanceAndEndpoints: Method = Method(name="createBinaryInstanceAndEndpoints", parameters={Parameter(name='mid_endpointSourceModel', type=StringType), Parameter(name='mid_newModelRelUri', type=StringType), Parameter(name='mid_instanceMID', type=StringType), Parameter(name='mid_endpointTargetModel', type=StringType)}, type=StringType)
mid_relationship_ModelRel_m_getOutlineResourceInstances: Method = Method(name="getOutlineResourceInstances", parameters={}, type=StringType)
mid_relationship_ModelRel_m_createWorkflowInstanceAndEndpoints: Method = Method(name="createWorkflowInstanceAndEndpoints", parameters={Parameter(name='mid_workflowMID', type=StringType), Parameter(name='mid_newModelRelId', type=StringType), Parameter(name='mid_endpointModels', type=StringType)}, type=StringType)
mid_relationship_ModelRel_m_createWorkflowBinaryInstance: Method = Method(name="createWorkflowBinaryInstance", parameters={Parameter(name='mid_workflowMID', type=StringType), Parameter(name='mid_newModelRelId', type=StringType)}, type=StringType)
mid_relationship_ModelRel_m_createWorkflowBinaryInstanceAndEndpoints: Method = Method(name="createWorkflowBinaryInstanceAndEndpoints", parameters={Parameter(name='mid_workflowMID', type=StringType), Parameter(name='mid_endpointSourceModel', type=StringType), Parameter(name='mid_newModelRelId', type=StringType), Parameter(name='mid_endpointTargetModel', type=StringType)}, type=StringType)
mid_relationship_ModelRel.methods={mid_relationship_ModelRel_m_getMIDContainer, mid_relationship_ModelRel_m_getOutlineResourceTypes, mid_relationship_ModelRel_m_createBinaryInstance, mid_relationship_ModelRel_m_createBinaryInstanceAndEndpoints, mid_relationship_ModelRel_m_createWorkflowBinaryInstance, mid_relationship_ModelRel_m_getOutlineResourceInstances, mid_relationship_ModelRel_m_copySubtype, mid_relationship_ModelRel_m_createInstanceAndEndpoints, mid_relationship_ModelRel_m_createWorkflowBinaryInstanceAndEndpoints, mid_relationship_ModelRel_m_getSupertype, mid_relationship_ModelRel_m_createBinarySubtype, mid_relationship_ModelRel_m_getMetatype, mid_relationship_ModelRel_m_createWorkflowInstanceAndEndpoints}

# Model class attributes and methods

# relationship_mid_ModelEndpoint class attributes and methods

# Mapping class attributes and methods

# ModelEndpointReference class attributes and methods

# MappingReference class attributes and methods

# mid_relationship_BinaryModelRel class attributes and methods
mid_relationship_BinaryModelRel_m_addModelType: Method = Method(name="addModelType", parameters={Parameter(name='mid_modelType', type=StringType), Parameter(name='mid_isBinarySrc', type=StringType)})
mid_relationship_BinaryModelRel.methods={mid_relationship_BinaryModelRel_m_addModelType}

# ModelRel class attributes and methods

# relationship_mid_Model class attributes and methods

# mid_relationship_ExtendibleElementReference class attributes and methods
mid_relationship_ExtendibleElementReference_modifiable: Property = Property(name="modifiable", type=BooleanType)
mid_relationship_ExtendibleElementReference_m_getUri: Method = Method(name="getUri", parameters={}, type=StringType)
mid_relationship_ExtendibleElementReference_m_getObject: Method = Method(name="getObject", parameters={}, type=ExtendibleElement)
mid_relationship_ExtendibleElementReference_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_relationship_ExtendibleElementReference_m_isTypesLevel: Method = Method(name="isTypesLevel", parameters={}, type=BooleanType)
mid_relationship_ExtendibleElementReference_m_isWorkflowsLevel: Method = Method(name="isWorkflowsLevel", parameters={}, type=BooleanType)
mid_relationship_ExtendibleElementReference_m_isInstancesLevel: Method = Method(name="isInstancesLevel", parameters={}, type=BooleanType)
mid_relationship_ExtendibleElementReference.attributes={mid_relationship_ExtendibleElementReference_modifiable}
mid_relationship_ExtendibleElementReference.methods={mid_relationship_ExtendibleElementReference_m_getObject, mid_relationship_ExtendibleElementReference_m_getMIDContainer, mid_relationship_ExtendibleElementReference_m_isInstancesLevel, mid_relationship_ExtendibleElementReference_m_isTypesLevel, mid_relationship_ExtendibleElementReference_m_isWorkflowsLevel, mid_relationship_ExtendibleElementReference_m_getUri}

# relationship_mid_ExtendibleElement class attributes and methods

# ExtendibleElementReference class attributes and methods

# mid_relationship_ExtendibleElementEndpointReference class attributes and methods
mid_relationship_ExtendibleElementEndpointReference_m_getObject: Method = Method(name="getObject", parameters={}, type=ExtendibleElementEndpoint)
mid_relationship_ExtendibleElementEndpointReference_m_getSupertypeRef: Method = Method(name="getSupertypeRef", parameters={}, type=StringType)
mid_relationship_ExtendibleElementEndpointReference_m_getTargetUri: Method = Method(name="getTargetUri", parameters={}, type=StringType)
mid_relationship_ExtendibleElementEndpointReference.methods={mid_relationship_ExtendibleElementEndpointReference_m_getObject, mid_relationship_ExtendibleElementEndpointReference_m_getSupertypeRef, mid_relationship_ExtendibleElementEndpointReference_m_getTargetUri}

# mid_relationship_ModelEndpointReference class attributes and methods
mid_relationship_ModelEndpointReference_m_getObject: Method = Method(name="getObject", parameters={}, type=StringType)
mid_relationship_ModelEndpointReference_m_getSupertypeRef: Method = Method(name="getSupertypeRef", parameters={}, type=StringType)
mid_relationship_ModelEndpointReference_m_acceptModelElementType: Method = Method(name="acceptModelElementType", parameters={Parameter(name='mid_metamodelObj', type=StringType)}, type=BooleanType)
mid_relationship_ModelEndpointReference_m_deleteTypeReference: Method = Method(name="deleteTypeReference", parameters={Parameter(name='mid_isFullDelete', type=StringType)})
mid_relationship_ModelEndpointReference_m_acceptModelElementInstance: Method = Method(name="acceptModelElementInstance", parameters={Parameter(name='mid_modelObj', type=StringType)}, type=StringType)
mid_relationship_ModelEndpointReference_m_createModelElementInstanceAndReference: Method = Method(name="createModelElementInstanceAndReference", parameters={Parameter(name='mid_newModelElemName', type=StringType), Parameter(name='mid_modelObj', type=StringType)}, type=StringType)
mid_relationship_ModelEndpointReference.methods={mid_relationship_ModelEndpointReference_m_getSupertypeRef, mid_relationship_ModelEndpointReference_m_acceptModelElementInstance, mid_relationship_ModelEndpointReference_m_acceptModelElementType, mid_relationship_ModelEndpointReference_m_getObject, mid_relationship_ModelEndpointReference_m_createModelElementInstanceAndReference, mid_relationship_ModelEndpointReference_m_deleteTypeReference}

# ExtendibleElementEndpointReference class attributes and methods

# ModelElementReference class attributes and methods

# mid_relationship_ModelElementReference class attributes and methods
mid_relationship_ModelElementReference_m_getObject: Method = Method(name="getObject", parameters={}, type=StringType)
mid_relationship_ModelElementReference_m_getSupertypeRef: Method = Method(name="getSupertypeRef", parameters={}, type=StringType)
mid_relationship_ModelElementReference_m_deleteTypeReference: Method = Method(name="deleteTypeReference", parameters={})
mid_relationship_ModelElementReference_m_deleteInstanceReference: Method = Method(name="deleteInstanceReference", parameters={})
mid_relationship_ModelElementReference.methods={mid_relationship_ModelElementReference_m_deleteInstanceReference, mid_relationship_ModelElementReference_m_getSupertypeRef, mid_relationship_ModelElementReference_m_getObject, mid_relationship_ModelElementReference_m_deleteTypeReference}

# ModelElementEndpointReference class attributes and methods

# mid_relationship_Mapping class attributes and methods
mid_relationship_Mapping_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_relationship_Mapping_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=StringType)
mid_relationship_Mapping_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_relationship_Mapping_m_createTypeReference: Method = Method(name="createTypeReference", parameters={Parameter(name='mid_mappingTypeRef', type=StringType), Parameter(name='mid_isModifiable', type=StringType), Parameter(name='mid_containerModelRelType', type=StringType)}, type=StringType)
mid_relationship_Mapping_m_createSubtypeAndReference: Method = Method(name="createSubtypeAndReference", parameters={Parameter(name='mid_mappingTypeRef', type=StringType), Parameter(name='mid_isBinary', type=StringType), Parameter(name='mid_newMappingTypeName', type=StringType), Parameter(name='mid_containerModelRelType', type=StringType)}, type=StringType)
mid_relationship_Mapping_m_deleteType: Method = Method(name="deleteType", parameters={})
mid_relationship_Mapping_m_createInstanceReference: Method = Method(name="createInstanceReference", parameters={Parameter(name='mid_containerModelRel', type=StringType)}, type=StringType)
mid_relationship_Mapping_m_createInstanceAndReference: Method = Method(name="createInstanceAndReference", parameters={Parameter(name='mid_isBinary', type=StringType), Parameter(name='mid_containerModelRel', type=StringType)}, type=StringType)
mid_relationship_Mapping_m_createInstanceAndReferenceAndEndpointsAndReferences: Method = Method(name="createInstanceAndReferenceAndEndpointsAndReferences", parameters={Parameter(name='mid_targetModelElemRefs', type=StringType), Parameter(name='mid_isBinary', type=StringType)}, type=StringType)
mid_relationship_Mapping_m_deleteInstance: Method = Method(name="deleteInstance", parameters={})
mid_relationship_Mapping.methods={mid_relationship_Mapping_m_createInstanceReference, mid_relationship_Mapping_m_createSubtypeAndReference, mid_relationship_Mapping_m_createInstanceAndReferenceAndEndpointsAndReferences, mid_relationship_Mapping_m_deleteInstance, mid_relationship_Mapping_m_getSupertype, mid_relationship_Mapping_m_deleteType, mid_relationship_Mapping_m_getMIDContainer, mid_relationship_Mapping_m_createTypeReference, mid_relationship_Mapping_m_getMetatype, mid_relationship_Mapping_m_createInstanceAndReference}

# ModelElementEndpoint class attributes and methods

# mid_relationship_BinaryMapping class attributes and methods

# mid_relationship_ModelElementEndpoint class attributes and methods
mid_relationship_ModelElementEndpoint_m_createSubtypeAndReference: Method = Method(name="createSubtypeAndReference", parameters={Parameter(name='mid_targetModelElemTypeRef', type=StringType), Parameter(name='mid_containerMappingTypeRef', type=StringType), Parameter(name='mid_newModelElemTypeEndpointName', type=StringType), Parameter(name='mid_isBinarySrc', type=StringType)}, type=StringType)
mid_relationship_ModelElementEndpoint_m_replaceSubtypeAndReference: Method = Method(name="replaceSubtypeAndReference", parameters={Parameter(name='mid_oldModelElemTypeEndpointRef', type=StringType), Parameter(name='mid_newModelElemTypeEndpointName', type=StringType), Parameter(name='mid_targetModelElemTypeRef', type=StringType)})
mid_relationship_ModelElementEndpoint_m_deleteType: Method = Method(name="deleteType", parameters={Parameter(name='mid_isFullDelete', type=StringType)})
mid_relationship_ModelElementEndpoint_m_createInstanceReference: Method = Method(name="createInstanceReference", parameters={Parameter(name='mid_containerMappingRef', type=StringType), Parameter(name='mid_targetModelElemRef', type=StringType)}, type=StringType)
mid_relationship_ModelElementEndpoint_m_createInstanceAndReference: Method = Method(name="createInstanceAndReference", parameters={Parameter(name='mid_targetModelElemRef', type=StringType), Parameter(name='mid_containerMappingRef', type=StringType)}, type=StringType)
mid_relationship_ModelElementEndpoint_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_relationship_ModelElementEndpoint_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=StringType)
mid_relationship_ModelElementEndpoint_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_relationship_ModelElementEndpoint_m_getTarget: Method = Method(name="getTarget", parameters={}, type=StringType)
mid_relationship_ModelElementEndpoint_m_createTypeReference: Method = Method(name="createTypeReference", parameters={Parameter(name='mid_modelElemTypeEndpointRef', type=StringType), Parameter(name='mid_isModifiable', type=StringType), Parameter(name='mid_isBinarySrc', type=StringType), Parameter(name='mid_containerMappingTypeRef', type=StringType), Parameter(name='mid_targetModelElemTypeRef', type=StringType)}, type=StringType)
mid_relationship_ModelElementEndpoint_m_replaceInstanceAndReference: Method = Method(name="replaceInstanceAndReference", parameters={Parameter(name='mid_targetModelElemRef', type=StringType), Parameter(name='mid_oldModelElemEndpointRef', type=StringType)})
mid_relationship_ModelElementEndpoint.methods={mid_relationship_ModelElementEndpoint_m_getTarget, mid_relationship_ModelElementEndpoint_m_createInstanceReference, mid_relationship_ModelElementEndpoint_m_replaceInstanceAndReference, mid_relationship_ModelElementEndpoint_m_replaceSubtypeAndReference, mid_relationship_ModelElementEndpoint_m_createInstanceAndReference, mid_relationship_ModelElementEndpoint_m_getSupertype, mid_relationship_ModelElementEndpoint_m_getMetatype, mid_relationship_ModelElementEndpoint_m_createSubtypeAndReference, mid_relationship_ModelElementEndpoint_m_deleteType, mid_relationship_ModelElementEndpoint_m_createTypeReference, mid_relationship_ModelElementEndpoint_m_getMIDContainer}

# mid_relationship_BinaryMappingReference class attributes and methods
mid_relationship_BinaryMappingReference_m_getObject: Method = Method(name="getObject", parameters={}, type=StringType)
mid_relationship_BinaryMappingReference_m_addModelElementTypeReference: Method = Method(name="addModelElementTypeReference", parameters={Parameter(name='mid_isBinarySrc', type=StringType), Parameter(name='mid_modelElemTypeRef', type=StringType)})
mid_relationship_BinaryMappingReference.methods={mid_relationship_BinaryMappingReference_m_getObject, mid_relationship_BinaryMappingReference_m_addModelElementTypeReference}

# mid_relationship_MappingReference class attributes and methods
mid_relationship_MappingReference_m_deleteInstanceAndReference: Method = Method(name="deleteInstanceAndReference", parameters={})
mid_relationship_MappingReference_m_getObject: Method = Method(name="getObject", parameters={}, type=StringType)
mid_relationship_MappingReference_m_getSupertypeRef: Method = Method(name="getSupertypeRef", parameters={}, type=StringType)
mid_relationship_MappingReference_m_deleteTypeReference: Method = Method(name="deleteTypeReference", parameters={})
mid_relationship_MappingReference_m_deleteTypeAndReference: Method = Method(name="deleteTypeAndReference", parameters={})
mid_relationship_MappingReference_m_deleteInstanceReference: Method = Method(name="deleteInstanceReference", parameters={})
mid_relationship_MappingReference.methods={mid_relationship_MappingReference_m_deleteInstanceAndReference, mid_relationship_MappingReference_m_deleteInstanceReference, mid_relationship_MappingReference_m_getSupertypeRef, mid_relationship_MappingReference_m_deleteTypeAndReference, mid_relationship_MappingReference_m_getObject, mid_relationship_MappingReference_m_deleteTypeReference}

# mid_editor_Editor class attributes and methods
mid_editor_Editor_modelUri: Property = Property(name="modelUri", type=StringType)
mid_editor_Editor_id: Property = Property(name="id", type=StringType)
mid_editor_Editor_wizardId: Property = Property(name="wizardId", type=StringType)
mid_editor_Editor_fileExtensions: Property = Property(name="fileExtensions", type=StringType)
mid_editor_Editor_wizardDialogClass: Property = Property(name="wizardDialogClass", type=StringType)
mid_editor_Editor_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_editor_Editor_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=StringType)
mid_editor_Editor_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_editor_Editor_m_createSubtype: Method = Method(name="createSubtype", parameters={Parameter(name='mid_newEditorTypeFragmentUri', type=StringType), Parameter(name='mid_modelTypeUri', type=StringType), Parameter(name='mid_editorId', type=StringType), Parameter(name='mid_wizardId', type=StringType), Parameter(name='mid_wizardDialogClassName', type=StringType), Parameter(name='mid_newEditorTypeName', type=StringType)}, type=StringType)
mid_editor_Editor_m_deleteType: Method = Method(name="deleteType", parameters={})
mid_editor_Editor_m_createInstance: Method = Method(name="createInstance", parameters={Parameter(name='mid_modelUri', type=StringType), Parameter(name='mid_instanceMID', type=StringType)}, type=StringType)
mid_editor_Editor_m_invokeInstanceWizard: Method = Method(name="invokeInstanceWizard", parameters={Parameter(name='mid_initialSelection', type=StringType)}, type=StringType)
mid_editor_Editor_m_deleteInstance: Method = Method(name="deleteInstance", parameters={})
mid_editor_Editor.attributes={mid_editor_Editor_id, mid_editor_Editor_modelUri, mid_editor_Editor_wizardId, mid_editor_Editor_wizardDialogClass, mid_editor_Editor_fileExtensions}
mid_editor_Editor.methods={mid_editor_Editor_m_deleteInstance, mid_editor_Editor_m_createSubtype, mid_editor_Editor_m_createInstance, mid_editor_Editor_m_deleteType, mid_editor_Editor_m_getMIDContainer, mid_editor_Editor_m_invokeInstanceWizard, mid_editor_Editor_m_getMetatype, mid_editor_Editor_m_getSupertype}

# mid_relationship_ModelElementEndpointReference class attributes and methods
mid_relationship_ModelElementEndpointReference_m_getObject: Method = Method(name="getObject", parameters={}, type=StringType)
mid_relationship_ModelElementEndpointReference_m_getSupertypeRef: Method = Method(name="getSupertypeRef", parameters={}, type=StringType)
mid_relationship_ModelElementEndpointReference_m_deleteTypeReference: Method = Method(name="deleteTypeReference", parameters={Parameter(name='mid_isFullDelete', type=StringType)})
mid_relationship_ModelElementEndpointReference_m_deleteTypeAndReference: Method = Method(name="deleteTypeAndReference", parameters={Parameter(name='mid_isFullDelete', type=StringType)})
mid_relationship_ModelElementEndpointReference_m_deleteInstanceAndReference: Method = Method(name="deleteInstanceAndReference", parameters={Parameter(name='mid_isFullDelete', type=StringType)})
mid_relationship_ModelElementEndpointReference.methods={mid_relationship_ModelElementEndpointReference_m_getObject, mid_relationship_ModelElementEndpointReference_m_deleteTypeAndReference, mid_relationship_ModelElementEndpointReference_m_deleteTypeReference, mid_relationship_ModelElementEndpointReference_m_getSupertypeRef, mid_relationship_ModelElementEndpointReference_m_deleteInstanceAndReference}

# mid_editor_Diagram class attributes and methods
mid_editor_Diagram_m_createSubtype: Method = Method(name="createSubtype", parameters={Parameter(name='mid_newEditorTypeFragmentUri', type=StringType), Parameter(name='mid_newEditorTypeName', type=StringType), Parameter(name='mid_editorId', type=StringType), Parameter(name='mid_modelTypeUri', type=StringType), Parameter(name='mid_wizardDialogClassName', type=StringType), Parameter(name='mid_wizardId', type=StringType)}, type=StringType)
mid_editor_Diagram_m_createInstance: Method = Method(name="createInstance", parameters={Parameter(name='mid_modelUri', type=StringType), Parameter(name='mid_instanceMID', type=StringType)}, type=StringType)
mid_editor_Diagram_m_invokeInstanceWizard: Method = Method(name="invokeInstanceWizard", parameters={Parameter(name='mid_initialSelection', type=StringType)}, type=StringType)
mid_editor_Diagram.methods={mid_editor_Diagram_m_createSubtype, mid_editor_Diagram_m_createInstance, mid_editor_Diagram_m_invokeInstanceWizard}

# mid_operator_Operator class attributes and methods
mid_operator_Operator_updateMID: Property = Property(name="updateMID", type=BooleanType)
mid_operator_Operator_executionTime: Property = Property(name="executionTime", type=StringType)
mid_operator_Operator_commutative: Property = Property(name="commutative", type=BooleanType)
mid_operator_Operator_inputSubdir: Property = Property(name="inputSubdir", type=StringType)
mid_operator_Operator_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_operator_Operator_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=StringType)
mid_operator_Operator_m_getMIDContainer: Method = Method(name="getMIDContainer", parameters={}, type=StringType)
mid_operator_Operator_m_createSubtype: Method = Method(name="createSubtype", parameters={Parameter(name='mid_implementationUri', type=StringType), Parameter(name='mid_newOperatorTypeName', type=StringType)}, type=StringType)
mid_operator_Operator_m_deleteType: Method = Method(name="deleteType", parameters={})
mid_operator_Operator_m_openType: Method = Method(name="openType", parameters={})
mid_operator_Operator_m_findAllowedInputs: Method = Method(name="findAllowedInputs", parameters={Parameter(name='mid_inputMIDs', type=StringType)})
mid_operator_Operator_m_getInputProperties: Method = Method(name="getInputProperties", parameters={}, type=StringType)
mid_operator_Operator_m_readInputProperties: Method = Method(name="readInputProperties", parameters={Parameter(name='mid_inputProperties', type=StringType)})
mid_operator_Operator_m_run: Method = Method(name="run", parameters={Parameter(name='mid_genericsByName', type=StringType), Parameter(name='mid_outputMIDsByName', type=StringType), Parameter(name='mid_inputsByName', type=StringType)})
mid_operator_Operator_m_startInstance: Method = Method(name="startInstance", parameters={Parameter(name='mid_instanceMID', type=StringType), Parameter(name='mid_outputMIDsByName', type=StringType), Parameter(name='mid_inputProperties', type=StringType), Parameter(name='mid_inputs', type=StringType), Parameter(name='mid_generics', type=StringType)}, type=StringType)
mid_operator_Operator_m_findFirstAllowedInput: Method = Method(name="findFirstAllowedInput", parameters={Parameter(name='mid_inputMIDs', type=StringType)}, type=StringType)
mid_operator_Operator_m_checkAllowedInputs: Method = Method(name="checkAllowedInputs", parameters={Parameter(name='mid_inputModels', type=StringType)}, type=StringType)
mid_operator_Operator_m_getOutputsByName: Method = Method(name="getOutputsByName", parameters={})
mid_operator_Operator_m_getOutputModels: Method = Method(name="getOutputModels", parameters={}, type=Model)
mid_operator_Operator_m_createInstance: Method = Method(name="createInstance", parameters={Parameter(name='mid_instanceMID', type=StringType)}, type=StringType)
mid_operator_Operator_m_deleteInstance: Method = Method(name="deleteInstance", parameters={})
mid_operator_Operator_m_selectAllowedGenerics: Method = Method(name="selectAllowedGenerics", parameters={Parameter(name='mid_inputs', type=StringType)}, type=StringType)
mid_operator_Operator_m_isAllowedGeneric: Method = Method(name="isAllowedGeneric", parameters={Parameter(name='mid_genericType', type=StringType), Parameter(name='mid_genericTypeEndpoint', type=StringType), Parameter(name='mid_inputs', type=StringType)}, type=BooleanType)
mid_operator_Operator_m_openInstance: Method = Method(name="openInstance", parameters={})
mid_operator_Operator_m_createWorkflowInstance: Method = Method(name="createWorkflowInstance", parameters={Parameter(name='mid_workflowMID', type=StringType)}, type=StringType)
mid_operator_Operator_m_deleteWorkflowInstance: Method = Method(name="deleteWorkflowInstance", parameters={})
mid_operator_Operator_m_startWorkflowInstance: Method = Method(name="startWorkflowInstance", parameters={Parameter(name='mid_inputs', type=StringType), Parameter(name='mid_generics', type=StringType), Parameter(name='mid_workflowMID', type=StringType)}, type=StringType)
mid_operator_Operator_m_openWorkflowInstance: Method = Method(name="openWorkflowInstance", parameters={})
mid_operator_Operator.attributes={mid_operator_Operator_commutative, mid_operator_Operator_inputSubdir, mid_operator_Operator_executionTime, mid_operator_Operator_updateMID}
mid_operator_Operator.methods={mid_operator_Operator_m_openWorkflowInstance, mid_operator_Operator_m_findFirstAllowedInput, mid_operator_Operator_m_createSubtype, mid_operator_Operator_m_createInstance, mid_operator_Operator_m_getMetatype, mid_operator_Operator_m_getMIDContainer, mid_operator_Operator_m_getSupertype, mid_operator_Operator_m_startWorkflowInstance, mid_operator_Operator_m_getOutputsByName, mid_operator_Operator_m_getInputProperties, mid_operator_Operator_m_findAllowedInputs, mid_operator_Operator_m_deleteInstance, mid_operator_Operator_m_startInstance, mid_operator_Operator_m_openType, mid_operator_Operator_m_readInputProperties, mid_operator_Operator_m_selectAllowedGenerics, mid_operator_Operator_m_deleteType, mid_operator_Operator_m_checkAllowedInputs, mid_operator_Operator_m_getOutputModels, mid_operator_Operator_m_isAllowedGeneric, mid_operator_Operator_m_run, mid_operator_Operator_m_openInstance, mid_operator_Operator_m_createWorkflowInstance, mid_operator_Operator_m_deleteWorkflowInstance}

# mid_operator_ConversionOperator class attributes and methods
mid_operator_ConversionOperator_m_deleteType: Method = Method(name="deleteType", parameters={})
mid_operator_ConversionOperator_m_cleanup: Method = Method(name="cleanup", parameters={})
mid_operator_ConversionOperator.methods={mid_operator_ConversionOperator_m_deleteType, mid_operator_ConversionOperator_m_cleanup}

# mid_operator_RandomOperator class attributes and methods
mid_operator_RandomOperator_state: Property = Property(name="state", type=StringType)
mid_operator_RandomOperator.attributes={mid_operator_RandomOperator_state}

# mid_operator_WorkflowOperator class attributes and methods
mid_operator_WorkflowOperator_midUri: Property = Property(name="midUri", type=StringType)
mid_operator_WorkflowOperator_m_getWorkflowMID: Method = Method(name="getWorkflowMID", parameters={}, type=StringType)
mid_operator_WorkflowOperator_m_getInstanceMID: Method = Method(name="getInstanceMID", parameters={}, type=StringType)
mid_operator_WorkflowOperator.attributes={mid_operator_WorkflowOperator_midUri}
mid_operator_WorkflowOperator.methods={mid_operator_WorkflowOperator_m_getInstanceMID, mid_operator_WorkflowOperator_m_getWorkflowMID}

# operator_mid_ModelEndpoint class attributes and methods

# GenericEndpoint class attributes and methods

# mid_operator_OperatorInput class attributes and methods

# operator_mid_Model class attributes and methods

# mid_operator_OperatorGeneric class attributes and methods

# operator_mid_GenericElement class attributes and methods

# mid_operator_GenericEndpoint class attributes and methods
mid_operator_GenericEndpoint_metatargetUri: Property = Property(name="metatargetUri", type=StringType)
mid_operator_GenericEndpoint_m_createWorkflowInstance: Method = Method(name="createWorkflowInstance", parameters={Parameter(name='mid_containerOperator', type=StringType), Parameter(name='mid_targetGeneric', type=StringType)}, type=StringType)
mid_operator_GenericEndpoint_m_getSupertype: Method = Method(name="getSupertype", parameters={}, type=StringType)
mid_operator_GenericEndpoint_m_getTarget: Method = Method(name="getTarget", parameters={}, type=GenericElement)
mid_operator_GenericEndpoint_m_setTarget: Method = Method(name="setTarget", parameters={Parameter(name='mid_newTarget', type=StringType)})
mid_operator_GenericEndpoint_m_getMetatype: Method = Method(name="getMetatype", parameters={}, type=StringType)
mid_operator_GenericEndpoint_m_createInstance: Method = Method(name="createInstance", parameters={Parameter(name='mid_targetGeneric', type=StringType), Parameter(name='mid_containerOperator', type=StringType)}, type=StringType)
mid_operator_GenericEndpoint.attributes={mid_operator_GenericEndpoint_metatargetUri}
mid_operator_GenericEndpoint.methods={mid_operator_GenericEndpoint_m_getTarget, mid_operator_GenericEndpoint_m_getSupertype, mid_operator_GenericEndpoint_m_getMetatype, mid_operator_GenericEndpoint_m_createInstance, mid_operator_GenericEndpoint_m_createWorkflowInstance, mid_operator_GenericEndpoint_m_setTarget}

# mid_operator_OperatorConstraint class attributes and methods

# ExtendibleElementConstraint class attributes and methods

# OperatorConstraintRule class attributes and methods

# mid_operator_OperatorConstraintRule class attributes and methods

# OperatorConstraintParameter class attributes and methods

# mid_operator_OperatorConstraintParameter class attributes and methods
mid_operator_OperatorConstraintParameter_endpointIndex: Property = Property(name="endpointIndex", type=IntegerType)
mid_operator_OperatorConstraintParameter.attributes={mid_operator_OperatorConstraintParameter_endpointIndex}

# Relationships
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
supertypeRef40: BinaryAssociation = BinaryAssociation(
    name="supertypeRef40",
    ends={
        Property(name="ExtendibleElementReference", type=mid_relationship_ExtendibleElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_ExtendibleElementReference41", type=ExtendibleElementReference, multiplicity=Multiplicity(0, 1))
    }
)
modelElemRefs42: BinaryAssociation = BinaryAssociation(
    name="modelElemRefs42",
    ends={
        Property(name="ModelElementReference", type=mid_relationship_ModelEndpointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_ModelEndpointReference", type=ModelElementReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelElemEndpointRefs43: BinaryAssociation = BinaryAssociation(
    name="modelElemEndpointRefs43",
    ends={
        Property(name="ModelElementEndpointReference", type=mid_relationship_ModelElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="modelElemRef", type=ModelElementEndpointReference, multiplicity=Multiplicity(0, 9999))
    }
)
modelElemEndpoints44: BinaryAssociation = BinaryAssociation(
    name="modelElemEndpoints44",
    ends={
        Property(name="ModelElementEndpoint", type=mid_relationship_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_Mapping", type=ModelElementEndpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelElemEndpointRefs45: BinaryAssociation = BinaryAssociation(
    name="modelElemEndpointRefs45",
    ends={
        Property(name="ModelElementEndpointReference47", type=mid_relationship_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_Mapping46", type=ModelElementEndpointReference, multiplicity=Multiplicity(0, 9999))
    }
)
modelElemEndpointRefs48: BinaryAssociation = BinaryAssociation(
    name="modelElemEndpointRefs48",
    ends={
        Property(name="ModelElementEndpointReference49", type=mid_relationship_MappingReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_relationship_MappingReference", type=ModelElementEndpointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelElemRef55: BinaryAssociation = BinaryAssociation(
    name="modelElemRef55",
    ends={
        Property(name="ModelElementReference56", type=mid_relationship_ModelElementEndpointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="modelElemEndpointRefs", type=ModelElementReference, multiplicity=Multiplicity(1, 1))
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
previousOperator63: BinaryAssociation = BinaryAssociation(
    name="previousOperator63",
    ends={
        Property(name="Operator65", type=mid_operator_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_Operator64", type=Operator, multiplicity=Multiplicity(0, 1))
    }
)
inputs57: BinaryAssociation = BinaryAssociation(
    name="inputs57",
    ends={
        Property(name="operator_mid_ModelEndpoint", type=mid_operator_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_Operator", type=operator_mid_ModelEndpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs58: BinaryAssociation = BinaryAssociation(
    name="outputs58",
    ends={
        Property(name="operator_mid_ModelEndpoint60", type=mid_operator_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_Operator59", type=operator_mid_ModelEndpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generics61: BinaryAssociation = BinaryAssociation(
    name="generics61",
    ends={
        Property(name="GenericEndpoint", type=mid_operator_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_Operator62", type=GenericEndpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model66: BinaryAssociation = BinaryAssociation(
    name="model66",
    ends={
        Property(name="operator_mid_Model", type=mid_operator_OperatorInput, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_OperatorInput", type=operator_mid_Model, multiplicity=Multiplicity(1, 1))
    }
)
conversions67: BinaryAssociation = BinaryAssociation(
    name="conversions67",
    ends={
        Property(name="ConversionOperator69", type=mid_operator_OperatorInput, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_OperatorInput68", type=ConversionOperator, multiplicity=Multiplicity(0, 9999))
    }
)
modelTypeEndpoint70: BinaryAssociation = BinaryAssociation(
    name="modelTypeEndpoint70",
    ends={
        Property(name="operator_mid_ModelEndpoint72", type=mid_operator_OperatorInput, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_OperatorInput71", type=operator_mid_ModelEndpoint, multiplicity=Multiplicity(1, 1))
    }
)
generic73: BinaryAssociation = BinaryAssociation(
    name="generic73",
    ends={
        Property(name="operator_mid_GenericElement", type=mid_operator_OperatorGeneric, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_OperatorGeneric", type=operator_mid_GenericElement, multiplicity=Multiplicity(1, 1))
    }
)
parameterRef82: BinaryAssociation = BinaryAssociation(
    name="parameterRef82",
    ends={
        Property(name="ModelEndpointReference83", type=mid_operator_OperatorConstraintParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_OperatorConstraintParameter", type=ModelEndpointReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
genericSuperTypeEndpoint74: BinaryAssociation = BinaryAssociation(
    name="genericSuperTypeEndpoint74",
    ends={
        Property(name="GenericEndpoint76", type=mid_operator_OperatorGeneric, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_OperatorGeneric75", type=GenericEndpoint, multiplicity=Multiplicity(1, 1))
    }
)
rules77: BinaryAssociation = BinaryAssociation(
    name="rules77",
    ends={
        Property(name="OperatorConstraintRule", type=mid_operator_OperatorConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_OperatorConstraint", type=OperatorConstraintRule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outputModelRel78: BinaryAssociation = BinaryAssociation(
    name="outputModelRel78",
    ends={
        Property(name="OperatorConstraintParameter", type=mid_operator_OperatorConstraintRule, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_OperatorConstraintRule", type=OperatorConstraintParameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
endpointModels79: BinaryAssociation = BinaryAssociation(
    name="endpointModels79",
    ends={
        Property(name="OperatorConstraintParameter81", type=mid_operator_OperatorConstraintRule, multiplicity=Multiplicity(1, 1)),
        Property(name="mid_operator_OperatorConstraintRule80", type=OperatorConstraintParameter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_mid_ExtendibleElementEndpoint_ExtendibleElement = Generalization(general=ExtendibleElement, specific=mid_ExtendibleElementEndpoint)
gen_mid_Model_GenericElement = Generalization(general=GenericElement, specific=mid_Model)
gen_mid_ModelElement_ExtendibleElement = Generalization(general=ExtendibleElement, specific=mid_ModelElement)
gen_mid_ModelEndpoint_ExtendibleElementEndpoint = Generalization(general=ExtendibleElementEndpoint, specific=mid_ModelEndpoint)
gen_mid_GenericElement_ExtendibleElement = Generalization(general=ExtendibleElement, specific=mid_GenericElement)
gen_mid_relationship_ModelRel_Model = Generalization(general=Model, specific=mid_relationship_ModelRel)
gen_mid_relationship_BinaryModelRel_ModelRel = Generalization(general=ModelRel, specific=mid_relationship_BinaryModelRel)
gen_mid_relationship_ExtendibleElementEndpointReference_ExtendibleElementReference = Generalization(general=ExtendibleElementReference, specific=mid_relationship_ExtendibleElementEndpointReference)
gen_mid_relationship_ModelEndpointReference_ExtendibleElementEndpointReference = Generalization(general=ExtendibleElementEndpointReference, specific=mid_relationship_ModelEndpointReference)
gen_mid_relationship_ModelElementReference_ExtendibleElementReference = Generalization(general=ExtendibleElementReference, specific=mid_relationship_ModelElementReference)
gen_mid_relationship_Mapping_ExtendibleElement = Generalization(general=ExtendibleElement, specific=mid_relationship_Mapping)
gen_mid_relationship_BinaryMapping_Mapping = Generalization(general=Mapping, specific=mid_relationship_BinaryMapping)
gen_mid_relationship_ModelElementEndpoint_ExtendibleElementEndpoint = Generalization(general=ExtendibleElementEndpoint, specific=mid_relationship_ModelElementEndpoint)
gen_mid_relationship_BinaryMappingReference_MappingReference = Generalization(general=MappingReference, specific=mid_relationship_BinaryMappingReference)
gen_mid_relationship_MappingReference_ExtendibleElementReference = Generalization(general=ExtendibleElementReference, specific=mid_relationship_MappingReference)
gen_mid_editor_Editor_ExtendibleElement = Generalization(general=ExtendibleElement, specific=mid_editor_Editor)
gen_mid_relationship_ModelElementEndpointReference_ExtendibleElementEndpointReference = Generalization(general=ExtendibleElementEndpointReference, specific=mid_relationship_ModelElementEndpointReference)
gen_mid_editor_Diagram_Editor = Generalization(general=Editor, specific=mid_editor_Diagram)
gen_mid_operator_Operator_GenericElement = Generalization(general=GenericElement, specific=mid_operator_Operator)
gen_mid_operator_ConversionOperator_Operator = Generalization(general=Operator, specific=mid_operator_ConversionOperator)
gen_mid_operator_RandomOperator_Operator = Generalization(general=Operator, specific=mid_operator_RandomOperator)
gen_mid_operator_WorkflowOperator_Operator = Generalization(general=Operator, specific=mid_operator_WorkflowOperator)
gen_mid_operator_GenericEndpoint_ExtendibleElementEndpoint = Generalization(general=ExtendibleElementEndpoint, specific=mid_operator_GenericEndpoint)
gen_mid_operator_OperatorConstraint_ExtendibleElementConstraint = Generalization(general=ExtendibleElementConstraint, specific=mid_operator_OperatorConstraint)

# Domain Model
domain_model = DomainModel(
    name="mid",
    types={mid_Model, Editor, Operator, mid_EStringToExtendibleElementMap, mid_MID, mid_ExtendibleElement, mid_ExtendibleElementEndpoint, ExtendibleElement, mid_ExtendibleElementConstraint, GenericElement, mid_ModelElement, ConversionOperator, mid_EMFInfo, mid_ModelEndpoint, ExtendibleElementEndpoint, mid_GenericElement, mid_relationship_ModelRel, Model, relationship_mid_ModelEndpoint, Mapping, ModelEndpointReference, MappingReference, mid_relationship_BinaryModelRel, ModelRel, relationship_mid_Model, mid_relationship_ExtendibleElementReference, relationship_mid_ExtendibleElement, ExtendibleElementReference, mid_relationship_ExtendibleElementEndpointReference, mid_relationship_ModelEndpointReference, ExtendibleElementEndpointReference, ModelElementReference, mid_relationship_ModelElementReference, ModelElementEndpointReference, mid_relationship_Mapping, ModelElementEndpoint, mid_relationship_BinaryMapping, mid_relationship_ModelElementEndpoint, mid_relationship_BinaryMappingReference, mid_relationship_MappingReference, mid_editor_Editor, mid_relationship_ModelElementEndpointReference, mid_editor_Diagram, mid_operator_Operator, mid_operator_ConversionOperator, mid_operator_RandomOperator, mid_operator_WorkflowOperator, operator_mid_ModelEndpoint, GenericEndpoint, mid_operator_OperatorInput, operator_mid_Model, mid_operator_OperatorGeneric, operator_mid_GenericElement, mid_operator_GenericEndpoint, mid_operator_OperatorConstraint, ExtendibleElementConstraint, OperatorConstraintRule, mid_operator_OperatorConstraintRule, OperatorConstraintParameter, mid_operator_OperatorConstraintParameter, MIDLevel, ModelOrigin},
    associations={models0, editors1, operators3, extendibleTable5, value7, supertype10, constraint12, target14, editors16, modelElems19, conversionOperators21, eInfo23, modelEndpoints25, mappings26, modelEndpointRefs28, mappingRefs30, sourceModel32, targetModel33, referencedObject36, containedObject37, supertypeRef40, modelElemRefs42, modelElemEndpointRefs43, modelElemEndpoints44, modelElemEndpointRefs45, modelElemEndpointRefs48, modelElemRef55, sourceModelElemRef50, targetModelElemRef52, previousOperator63, inputs57, outputs58, generics61, model66, conversions67, modelTypeEndpoint70, generic73, parameterRef82, genericSuperTypeEndpoint74, rules77, outputModelRel78, endpointModels79},
    generalizations={gen_mid_ExtendibleElementEndpoint_ExtendibleElement, gen_mid_Model_GenericElement, gen_mid_ModelElement_ExtendibleElement, gen_mid_ModelEndpoint_ExtendibleElementEndpoint, gen_mid_GenericElement_ExtendibleElement, gen_mid_relationship_ModelRel_Model, gen_mid_relationship_BinaryModelRel_ModelRel, gen_mid_relationship_ExtendibleElementEndpointReference_ExtendibleElementReference, gen_mid_relationship_ModelEndpointReference_ExtendibleElementEndpointReference, gen_mid_relationship_ModelElementReference_ExtendibleElementReference, gen_mid_relationship_Mapping_ExtendibleElement, gen_mid_relationship_BinaryMapping_Mapping, gen_mid_relationship_ModelElementEndpoint_ExtendibleElementEndpoint, gen_mid_relationship_BinaryMappingReference_MappingReference, gen_mid_relationship_MappingReference_ExtendibleElementReference, gen_mid_editor_Editor_ExtendibleElement, gen_mid_relationship_ModelElementEndpointReference_ExtendibleElementEndpointReference, gen_mid_editor_Diagram_Editor, gen_mid_operator_Operator_GenericElement, gen_mid_operator_ConversionOperator_Operator, gen_mid_operator_RandomOperator_Operator, gen_mid_operator_WorkflowOperator_Operator, gen_mid_operator_GenericEndpoint_ExtendibleElementEndpoint, gen_mid_operator_OperatorConstraint_ExtendibleElementConstraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
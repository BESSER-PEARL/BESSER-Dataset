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
ParameterType: Enumeration = Enumeration(
    name="ParameterType",
    literals={
            EnumerationLiteral(name="INPUT"),
			EnumerationLiteral(name="OUTPUT")
    }
)

NodeType: Enumeration = Enumeration(
    name="NodeType",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

ErrorCode: Enumeration = Enumeration(
    name="ErrorCode",
    literals={
            EnumerationLiteral(name="testgeneration"),
			EnumerationLiteral(name="trello"),
			EnumerationLiteral(name="nlp"),
			EnumerationLiteral(name="noSuchService"),
			EnumerationLiteral(name="methodNotAllowed"),
			EnumerationLiteral(name="inMaintenanceMode"),
			EnumerationLiteral(name="invalidData"),
			EnumerationLiteral(name="validator"),
			EnumerationLiteral(name="noAuthorization"),
			EnumerationLiteral(name="internalProblem"),
			EnumerationLiteral(name="userSession"),
			EnumerationLiteral(name="configuration"),
			EnumerationLiteral(name="persistency"),
			EnumerationLiteral(name="migration"),
			EnumerationLiteral(name="seralization"),
			EnumerationLiteral(name="restService"),
			EnumerationLiteral(name="scheduler"),
			EnumerationLiteral(name="hpProxy"),
			EnumerationLiteral(name="jira"),
			EnumerationLiteral(name="metrics"),
			EnumerationLiteral(name="search")
    }
)

OperationType: Enumeration = Enumeration(
    name="OperationType",
    literals={
            EnumerationLiteral(name="CREATE"),
			EnumerationLiteral(name="UPDATE"),
			EnumerationLiteral(name="DELETE")
    }
)

# Classes
model_base_ISpecmateModelObject = Class(name="model::base::ISpecmateModelObject", is_abstract=True)
base_IContainer = Class(name="base::IContainer")
base_ITracingElement = Class(name="base::ITracingElement")
model_base_Folder = Class(name="model::base::Folder")
ISpecmateModelObject = Class(name="ISpecmateModelObject")
model_base_IPositionable = Class(name="model::base::IPositionable", is_abstract=True)
model_base_IExternal = Class(name="model::base::IExternal")
model_base_INamed = Class(name="model::base::INamed", is_abstract=True)
model_base_IDescribed = Class(name="model::base::IDescribed", is_abstract=True)
model_base_IID = Class(name="model::base::IID", is_abstract=True)
model_base_IContentElement = Class(name="model::base::IContentElement", is_abstract=True)
base_IID = Class(name="base::IID")
base_INamed = Class(name="base::INamed")
base_IDescribed = Class(name="base::IDescribed")
base_IRecycled = Class(name="base::IRecycled")
model_base_IContainer = Class(name="model::base::IContainer", is_abstract=True)
IContentElement = Class(name="IContentElement")
model_requirements_CEGModel = Class(name="model::requirements::CEGModel")
model_base_ISpecmatePositionableModelObject = Class(name="model::base::ISpecmatePositionableModelObject", is_abstract=True)
model_base_IModelConnection = Class(name="model::base::IModelConnection")
IModelNode = Class(name="IModelNode")
model_base_IModelNode = Class(name="model::base::IModelNode")
ISpecmatePositionableModelObject = Class(name="ISpecmatePositionableModelObject")
IModelConnection = Class(name="IModelConnection")
model_base_ITracingElement = Class(name="model::base::ITracingElement")
ITracingElement = Class(name="ITracingElement")
model_base_IRecycled = Class(name="model::base::IRecycled", is_abstract=True)
model_requirements_Requirement = Class(name="model::requirements::Requirement")
base_ISpecmateModelObject = Class(name="base::ISpecmateModelObject")
base_IExternal = Class(name="base::IExternal")
model_testspecification_TestCase = Class(name="model::testspecification::TestCase")
base_IPositionable = Class(name="base::IPositionable")
model_testspecification_ParameterAssignment = Class(name="model::testspecification::ParameterAssignment")
TestParameter = Class(name="TestParameter")
model_testspecification_TestProcedure = Class(name="model::testspecification::TestProcedure")
model_requirements_CEGNode = Class(name="model::requirements::CEGNode")
model_requirements_CEGConnection = Class(name="model::requirements::CEGConnection")
model_testspecification_TestSpecification = Class(name="model::testspecification::TestSpecification")
IContainer = Class(name="IContainer")
model_testspecification_TestParameter = Class(name="model::testspecification::TestParameter")
ParameterAssignment = Class(name="ParameterAssignment")
model_processes_ProcessEnd = Class(name="model::processes::ProcessEnd")
model_history_History = Class(name="model::history::History")
HistoryEntry = Class(name="HistoryEntry")
model_history_HistoryEntry = Class(name="model::history::HistoryEntry")
model_testspecification_TestStep = Class(name="model::testspecification::TestStep")
base_IContentElement = Class(name="base::IContentElement")
model_processes_Process = Class(name="model::processes::Process")
model_processes_ProcessNode = Class(name="model::processes::ProcessNode", is_abstract=True)
model_processes_ProcessStep = Class(name="model::processes::ProcessStep")
ProcessNode = Class(name="ProcessNode")
model_processes_ProcessDecision = Class(name="model::processes::ProcessDecision")
model_processes_ProcessConnection = Class(name="model::processes::ProcessConnection")
model_processes_ProcessStart = Class(name="model::processes::ProcessStart")
model_batch_BatchOperation = Class(name="model::batch::BatchOperation")
Operation = Class(name="Operation")
model_batch_Operation = Class(name="model::batch::Operation")
Change = Class(name="Change")
model_history_Change = Class(name="model::history::Change")
model_administration_Status = Class(name="model::administration::Status")
model_administration_ProblemDetail = Class(name="model::administration::ProblemDetail")
model_export_Export = Class(name="model::export::Export")
INamed = Class(name="INamed")

# model_base_ISpecmateModelObject class attributes and methods

# base_IContainer class attributes and methods

# base_ITracingElement class attributes and methods

# model_base_Folder class attributes and methods
model_base_Folder_library: Property = Property(name="library", type=BooleanType)
model_base_Folder.attributes={model_base_Folder_library}

# ISpecmateModelObject class attributes and methods

# model_base_IPositionable class attributes and methods
model_base_IPositionable_position: Property = Property(name="position", type=IntegerType)
model_base_IPositionable.attributes={model_base_IPositionable_position}

# model_base_IExternal class attributes and methods
model_base_IExternal_extId: Property = Property(name="extId", type=StringType)
model_base_IExternal_extId2: Property = Property(name="extId2", type=StringType)
model_base_IExternal_source: Property = Property(name="source", type=StringType)
model_base_IExternal_live: Property = Property(name="live", type=BooleanType)
model_base_IExternal.attributes={model_base_IExternal_source, model_base_IExternal_live, model_base_IExternal_extId, model_base_IExternal_extId2}

# model_base_INamed class attributes and methods
model_base_INamed_name: Property = Property(name="name", type=StringType)
model_base_INamed.attributes={model_base_INamed_name}

# model_base_IDescribed class attributes and methods
model_base_IDescribed_description: Property = Property(name="description", type=StringType)
model_base_IDescribed.attributes={model_base_IDescribed_description}

# model_base_IID class attributes and methods
model_base_IID_id: Property = Property(name="id", type=StringType)
model_base_IID.attributes={model_base_IID_id}

# model_base_IContentElement class attributes and methods

# base_IID class attributes and methods

# base_INamed class attributes and methods

# base_IDescribed class attributes and methods

# base_IRecycled class attributes and methods

# model_base_IContainer class attributes and methods

# IContentElement class attributes and methods

# model_requirements_CEGModel class attributes and methods
model_requirements_CEGModel_modelRequirements: Property = Property(name="modelRequirements", type=StringType)
model_requirements_CEGModel.attributes={model_requirements_CEGModel_modelRequirements}

# model_base_ISpecmatePositionableModelObject class attributes and methods
model_base_ISpecmatePositionableModelObject_x: Property = Property(name="x", type=FloatType)
model_base_ISpecmatePositionableModelObject_y: Property = Property(name="y", type=FloatType)
model_base_ISpecmatePositionableModelObject_width: Property = Property(name="width", type=FloatType)
model_base_ISpecmatePositionableModelObject_height: Property = Property(name="height", type=FloatType)
model_base_ISpecmatePositionableModelObject.attributes={model_base_ISpecmatePositionableModelObject_height, model_base_ISpecmatePositionableModelObject_y, model_base_ISpecmatePositionableModelObject_x, model_base_ISpecmatePositionableModelObject_width}

# model_base_IModelConnection class attributes and methods

# IModelNode class attributes and methods

# model_base_IModelNode class attributes and methods

# ISpecmatePositionableModelObject class attributes and methods

# IModelConnection class attributes and methods

# model_base_ITracingElement class attributes and methods

# ITracingElement class attributes and methods

# model_base_IRecycled class attributes and methods
model_base_IRecycled_recycled: Property = Property(name="recycled", type=BooleanType)
model_base_IRecycled_hasRecycledChildren: Property = Property(name="hasRecycledChildren", type=BooleanType)
model_base_IRecycled.attributes={model_base_IRecycled_hasRecycledChildren, model_base_IRecycled_recycled}

# model_requirements_Requirement class attributes and methods
model_requirements_Requirement_implementingITTeam: Property = Property(name="implementingITTeam", type=StringType)
model_requirements_Requirement_plannedRelease: Property = Property(name="plannedRelease", type=StringType)
model_requirements_Requirement_status: Property = Property(name="status", type=StringType)
model_requirements_Requirement_isRegressionRequirement: Property = Property(name="isRegressionRequirement", type=BooleanType)
model_requirements_Requirement_platform: Property = Property(name="platform", type=StringType)
model_requirements_Requirement_numberOfTests: Property = Property(name="numberOfTests", type=IntegerType)
model_requirements_Requirement_tac: Property = Property(name="tac", type=StringType)
model_requirements_Requirement_implementingUnit: Property = Property(name="implementingUnit", type=StringType)
model_requirements_Requirement_implementingBOTeam: Property = Property(name="implementingBOTeam", type=StringType)
model_requirements_Requirement.attributes={model_requirements_Requirement_implementingBOTeam, model_requirements_Requirement_status, model_requirements_Requirement_implementingITTeam, model_requirements_Requirement_plannedRelease, model_requirements_Requirement_implementingUnit, model_requirements_Requirement_platform, model_requirements_Requirement_numberOfTests, model_requirements_Requirement_isRegressionRequirement, model_requirements_Requirement_tac}

# base_ISpecmateModelObject class attributes and methods

# base_IExternal class attributes and methods

# model_testspecification_TestCase class attributes and methods
model_testspecification_TestCase_consistent: Property = Property(name="consistent", type=BooleanType)
model_testspecification_TestCase.attributes={model_testspecification_TestCase_consistent}

# base_IPositionable class attributes and methods

# model_testspecification_ParameterAssignment class attributes and methods
model_testspecification_ParameterAssignment_value: Property = Property(name="value", type=StringType)
model_testspecification_ParameterAssignment_condition: Property = Property(name="condition", type=StringType)
model_testspecification_ParameterAssignment.attributes={model_testspecification_ParameterAssignment_value, model_testspecification_ParameterAssignment_condition}

# TestParameter class attributes and methods

# model_testspecification_TestProcedure class attributes and methods
model_testspecification_TestProcedure_isRegressionTest: Property = Property(name="isRegressionTest", type=BooleanType)
model_testspecification_TestProcedure.attributes={model_testspecification_TestProcedure_isRegressionTest}

# model_requirements_CEGNode class attributes and methods
model_requirements_CEGNode_type: Property = Property(name="type", type=StringType)
model_requirements_CEGNode_variable: Property = Property(name="variable", type=StringType)
model_requirements_CEGNode_condition: Property = Property(name="condition", type=StringType)
model_requirements_CEGNode.attributes={model_requirements_CEGNode_condition, model_requirements_CEGNode_type, model_requirements_CEGNode_variable}

# model_requirements_CEGConnection class attributes and methods
model_requirements_CEGConnection_negate: Property = Property(name="negate", type=BooleanType)
model_requirements_CEGConnection.attributes={model_requirements_CEGConnection_negate}

# model_testspecification_TestSpecification class attributes and methods

# IContainer class attributes and methods

# model_testspecification_TestParameter class attributes and methods
model_testspecification_TestParameter_type: Property = Property(name="type", type=StringType)
model_testspecification_TestParameter.attributes={model_testspecification_TestParameter_type}

# ParameterAssignment class attributes and methods

# model_processes_ProcessEnd class attributes and methods

# model_history_History class attributes and methods

# HistoryEntry class attributes and methods

# model_history_HistoryEntry class attributes and methods
model_history_HistoryEntry_timestamp: Property = Property(name="timestamp", type=StringType)
model_history_HistoryEntry_user: Property = Property(name="user", type=StringType)
model_history_HistoryEntry_deletedObjects: Property = Property(name="deletedObjects", type=StringType)
model_history_HistoryEntry_comment: Property = Property(name="comment", type=StringType)
model_history_HistoryEntry.attributes={model_history_HistoryEntry_user, model_history_HistoryEntry_timestamp, model_history_HistoryEntry_deletedObjects, model_history_HistoryEntry_comment}

# model_testspecification_TestStep class attributes and methods
model_testspecification_TestStep_expectedOutcome: Property = Property(name="expectedOutcome", type=StringType)
model_testspecification_TestStep.attributes={model_testspecification_TestStep_expectedOutcome}

# base_IContentElement class attributes and methods

# model_processes_Process class attributes and methods

# model_processes_ProcessNode class attributes and methods

# model_processes_ProcessStep class attributes and methods
model_processes_ProcessStep_expectedOutcome: Property = Property(name="expectedOutcome", type=StringType)
model_processes_ProcessStep.attributes={model_processes_ProcessStep_expectedOutcome}

# ProcessNode class attributes and methods

# model_processes_ProcessDecision class attributes and methods

# model_processes_ProcessConnection class attributes and methods
model_processes_ProcessConnection_condition: Property = Property(name="condition", type=StringType)
model_processes_ProcessConnection_labelX: Property = Property(name="labelX", type=FloatType)
model_processes_ProcessConnection_labelY: Property = Property(name="labelY", type=FloatType)
model_processes_ProcessConnection.attributes={model_processes_ProcessConnection_labelX, model_processes_ProcessConnection_condition, model_processes_ProcessConnection_labelY}

# model_processes_ProcessStart class attributes and methods

# model_batch_BatchOperation class attributes and methods

# Operation class attributes and methods

# model_batch_Operation class attributes and methods
model_batch_Operation_type: Property = Property(name="type", type=StringType)
model_batch_Operation.attributes={model_batch_Operation_type}

# Change class attributes and methods

# model_history_Change class attributes and methods
model_history_Change_objectName: Property = Property(name="objectName", type=StringType)
model_history_Change_objectType: Property = Property(name="objectType", type=StringType)
model_history_Change_oldValue: Property = Property(name="oldValue", type=StringType)
model_history_Change_newValue: Property = Property(name="newValue", type=StringType)
model_history_Change_feature: Property = Property(name="feature", type=StringType)
model_history_Change_isCreate: Property = Property(name="isCreate", type=BooleanType)
model_history_Change_isDelete: Property = Property(name="isDelete", type=BooleanType)
model_history_Change.attributes={model_history_Change_newValue, model_history_Change_feature, model_history_Change_oldValue, model_history_Change_objectName, model_history_Change_isCreate, model_history_Change_objectType, model_history_Change_isDelete}

# model_administration_Status class attributes and methods
model_administration_Status_value: Property = Property(name="value", type=StringType)
model_administration_Status.attributes={model_administration_Status_value}

# model_administration_ProblemDetail class attributes and methods
model_administration_ProblemDetail_ecode: Property = Property(name="ecode", type=StringType)
model_administration_ProblemDetail_status: Property = Property(name="status", type=IntegerType)
model_administration_ProblemDetail_detail: Property = Property(name="detail", type=StringType)
model_administration_ProblemDetail_instance: Property = Property(name="instance", type=StringType)
model_administration_ProblemDetail.attributes={model_administration_ProblemDetail_ecode, model_administration_ProblemDetail_instance, model_administration_ProblemDetail_status, model_administration_ProblemDetail_detail}

# model_export_Export class attributes and methods
model_export_Export_type: Property = Property(name="type", type=StringType)
model_export_Export_content: Property = Property(name="content", type=StringType)
model_export_Export.attributes={model_export_Export_type, model_export_Export_content}

# INamed class attributes and methods

# Relationships
contents0: BinaryAssociation = BinaryAssociation(
    name="contents0",
    ends={
        Property(name="IContentElement", type=model_base_IContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="model_base_IContainer", type=IContentElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source1: BinaryAssociation = BinaryAssociation(
    name="source1",
    ends={
        Property(name="base", type=model_base_IModelConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="IModelNode", type=IModelNode, multiplicity=Multiplicity(0, 1))
    }
)
target2: BinaryAssociation = BinaryAssociation(
    name="target2",
    ends={
        Property(name="base4", type=model_base_IModelConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="IModelNode3", type=IModelNode, multiplicity=Multiplicity(0, 1))
    }
)
outgoingConnections5: BinaryAssociation = BinaryAssociation(
    name="outgoingConnections5",
    ends={
        Property(name="base6", type=model_base_IModelNode, multiplicity=Multiplicity(1, 1)),
        Property(name="IModelConnection", type=IModelConnection, multiplicity=Multiplicity(0, 9999))
    }
)
incomingConnections7: BinaryAssociation = BinaryAssociation(
    name="incomingConnections7",
    ends={
        Property(name="base9", type=model_base_IModelNode, multiplicity=Multiplicity(1, 1)),
        Property(name="IModelConnection8", type=IModelConnection, multiplicity=Multiplicity(0, 9999))
    }
)
tracesTo10: BinaryAssociation = BinaryAssociation(
    name="tracesTo10",
    ends={
        Property(name="base11", type=model_base_ITracingElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ITracingElement", type=ITracingElement, multiplicity=Multiplicity(0, 9999))
    }
)
tracesFrom12: BinaryAssociation = BinaryAssociation(
    name="tracesFrom12",
    ends={
        Property(name="base14", type=model_base_ITracingElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ITracingElement13", type=ITracingElement, multiplicity=Multiplicity(0, 9999))
    }
)
parameter16: BinaryAssociation = BinaryAssociation(
    name="parameter16",
    ends={
        Property(name="testspecification17", type=model_testspecification_ParameterAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="TestParameter", type=TestParameter, multiplicity=Multiplicity(0, 1))
    }
)
assignments15: BinaryAssociation = BinaryAssociation(
    name="assignments15",
    ends={
        Property(name="testspecification", type=model_testspecification_TestParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ParameterAssignment", type=ParameterAssignment, multiplicity=Multiplicity(0, 9999))
    }
)
entries20: BinaryAssociation = BinaryAssociation(
    name="entries20",
    ends={
        Property(name="HistoryEntry", type=model_history_History, multiplicity=Multiplicity(1, 1)),
        Property(name="model_history_History", type=HistoryEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedTestParameters18: BinaryAssociation = BinaryAssociation(
    name="referencedTestParameters18",
    ends={
        Property(name="TestParameter19", type=model_testspecification_TestStep, multiplicity=Multiplicity(1, 1)),
        Property(name="model_testspecification_TestStep", type=TestParameter, multiplicity=Multiplicity(0, 9999))
    }
)
operations22: BinaryAssociation = BinaryAssociation(
    name="operations22",
    ends={
        Property(name="Operation", type=model_batch_BatchOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_batch_BatchOperation", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target23: BinaryAssociation = BinaryAssociation(
    name="target23",
    ends={
        Property(name="IContentElement24", type=model_batch_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_batch_Operation", type=IContentElement, multiplicity=Multiplicity(0, 1))
    }
)
value25: BinaryAssociation = BinaryAssociation(
    name="value25",
    ends={
        Property(name="IContentElement27", type=model_batch_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_batch_Operation26", type=IContentElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
changes21: BinaryAssociation = BinaryAssociation(
    name="changes21",
    ends={
        Property(name="Change", type=model_history_HistoryEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="model_history_HistoryEntry", type=Change, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_model_base_ISpecmateModelObject_base_IContainer = Generalization(general=base_IContainer, specific=model_base_ISpecmateModelObject)
gen_model_base_ISpecmateModelObject_base_ITracingElement = Generalization(general=base_ITracingElement, specific=model_base_ISpecmateModelObject)
gen_model_base_Folder_ISpecmateModelObject = Generalization(general=ISpecmateModelObject, specific=model_base_Folder)
gen_model_base_IContentElement_base_IID = Generalization(general=base_IID, specific=model_base_IContentElement)
gen_model_base_IContentElement_base_INamed = Generalization(general=base_INamed, specific=model_base_IContentElement)
gen_model_base_IContentElement_base_IDescribed = Generalization(general=base_IDescribed, specific=model_base_IContentElement)
gen_model_base_IContentElement_base_IRecycled = Generalization(general=base_IRecycled, specific=model_base_IContentElement)
gen_model_base_IContainer_IContentElement = Generalization(general=IContentElement, specific=model_base_IContainer)
gen_model_requirements_CEGModel_ISpecmateModelObject = Generalization(general=ISpecmateModelObject, specific=model_requirements_CEGModel)
gen_model_base_ISpecmatePositionableModelObject_ISpecmateModelObject = Generalization(general=ISpecmateModelObject, specific=model_base_ISpecmatePositionableModelObject)
gen_model_base_IModelConnection_ISpecmateModelObject = Generalization(general=ISpecmateModelObject, specific=model_base_IModelConnection)
gen_model_base_IModelNode_ISpecmatePositionableModelObject = Generalization(general=ISpecmatePositionableModelObject, specific=model_base_IModelNode)
gen_model_requirements_Requirement_base_ISpecmateModelObject = Generalization(general=base_ISpecmateModelObject, specific=model_requirements_Requirement)
gen_model_requirements_Requirement_base_IExternal = Generalization(general=base_IExternal, specific=model_requirements_Requirement)
gen_model_testspecification_TestCase_base_IContainer = Generalization(general=base_IContainer, specific=model_testspecification_TestCase)
gen_model_testspecification_TestCase_base_IPositionable = Generalization(general=base_IPositionable, specific=model_testspecification_TestCase)
gen_model_testspecification_ParameterAssignment_IContentElement = Generalization(general=IContentElement, specific=model_testspecification_ParameterAssignment)
gen_model_requirements_CEGNode_IModelNode = Generalization(general=IModelNode, specific=model_requirements_CEGNode)
gen_model_requirements_CEGConnection_IModelConnection = Generalization(general=IModelConnection, specific=model_requirements_CEGConnection)
gen_model_testspecification_TestSpecification_IContainer = Generalization(general=IContainer, specific=model_testspecification_TestSpecification)
gen_model_testspecification_TestParameter_IContentElement = Generalization(general=IContentElement, specific=model_testspecification_TestParameter)
gen_model_processes_ProcessEnd_ProcessNode = Generalization(general=ProcessNode, specific=model_processes_ProcessEnd)
gen_model_testspecification_TestProcedure_base_IContainer = Generalization(general=base_IContainer, specific=model_testspecification_TestProcedure)
gen_model_testspecification_TestProcedure_base_IExternal = Generalization(general=base_IExternal, specific=model_testspecification_TestProcedure)
gen_model_testspecification_TestStep_base_IContentElement = Generalization(general=base_IContentElement, specific=model_testspecification_TestStep)
gen_model_testspecification_TestStep_base_IPositionable = Generalization(general=base_IPositionable, specific=model_testspecification_TestStep)
gen_model_processes_Process_IContainer = Generalization(general=IContainer, specific=model_processes_Process)
gen_model_processes_ProcessNode_IModelNode = Generalization(general=IModelNode, specific=model_processes_ProcessNode)
gen_model_processes_ProcessStep_ProcessNode = Generalization(general=ProcessNode, specific=model_processes_ProcessStep)
gen_model_processes_ProcessDecision_ProcessNode = Generalization(general=ProcessNode, specific=model_processes_ProcessDecision)
gen_model_processes_ProcessConnection_IModelConnection = Generalization(general=IModelConnection, specific=model_processes_ProcessConnection)
gen_model_processes_ProcessStart_ProcessNode = Generalization(general=ProcessNode, specific=model_processes_ProcessStart)
gen_model_export_Export_INamed = Generalization(general=INamed, specific=model_export_Export)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_base_ISpecmateModelObject, base_IContainer, base_ITracingElement, model_base_Folder, ISpecmateModelObject, model_base_IPositionable, model_base_IExternal, model_base_INamed, model_base_IDescribed, model_base_IID, model_base_IContentElement, base_IID, base_INamed, base_IDescribed, base_IRecycled, model_base_IContainer, IContentElement, model_requirements_CEGModel, model_base_ISpecmatePositionableModelObject, model_base_IModelConnection, IModelNode, model_base_IModelNode, ISpecmatePositionableModelObject, IModelConnection, model_base_ITracingElement, ITracingElement, model_base_IRecycled, model_requirements_Requirement, base_ISpecmateModelObject, base_IExternal, model_testspecification_TestCase, base_IPositionable, model_testspecification_ParameterAssignment, TestParameter, model_testspecification_TestProcedure, model_requirements_CEGNode, model_requirements_CEGConnection, model_testspecification_TestSpecification, IContainer, model_testspecification_TestParameter, ParameterAssignment, model_processes_ProcessEnd, model_history_History, HistoryEntry, model_history_HistoryEntry, model_testspecification_TestStep, base_IContentElement, model_processes_Process, model_processes_ProcessNode, model_processes_ProcessStep, ProcessNode, model_processes_ProcessDecision, model_processes_ProcessConnection, model_processes_ProcessStart, model_batch_BatchOperation, Operation, model_batch_Operation, Change, model_history_Change, model_administration_Status, model_administration_ProblemDetail, model_export_Export, INamed, ParameterType, NodeType, ErrorCode, OperationType},
    associations={contents0, source1, target2, outgoingConnections5, incomingConnections7, tracesTo10, tracesFrom12, parameter16, assignments15, entries20, referencedTestParameters18, operations22, target23, value25, changes21},
    generalizations={gen_model_base_ISpecmateModelObject_base_IContainer, gen_model_base_ISpecmateModelObject_base_ITracingElement, gen_model_base_Folder_ISpecmateModelObject, gen_model_base_IContentElement_base_IID, gen_model_base_IContentElement_base_INamed, gen_model_base_IContentElement_base_IDescribed, gen_model_base_IContentElement_base_IRecycled, gen_model_base_IContainer_IContentElement, gen_model_requirements_CEGModel_ISpecmateModelObject, gen_model_base_ISpecmatePositionableModelObject_ISpecmateModelObject, gen_model_base_IModelConnection_ISpecmateModelObject, gen_model_base_IModelNode_ISpecmatePositionableModelObject, gen_model_requirements_Requirement_base_ISpecmateModelObject, gen_model_requirements_Requirement_base_IExternal, gen_model_testspecification_TestCase_base_IContainer, gen_model_testspecification_TestCase_base_IPositionable, gen_model_testspecification_ParameterAssignment_IContentElement, gen_model_requirements_CEGNode_IModelNode, gen_model_requirements_CEGConnection_IModelConnection, gen_model_testspecification_TestSpecification_IContainer, gen_model_testspecification_TestParameter_IContentElement, gen_model_processes_ProcessEnd_ProcessNode, gen_model_testspecification_TestProcedure_base_IContainer, gen_model_testspecification_TestProcedure_base_IExternal, gen_model_testspecification_TestStep_base_IContentElement, gen_model_testspecification_TestStep_base_IPositionable, gen_model_processes_Process_IContainer, gen_model_processes_ProcessNode_IModelNode, gen_model_processes_ProcessStep_ProcessNode, gen_model_processes_ProcessDecision_ProcessNode, gen_model_processes_ProcessConnection_IModelConnection, gen_model_processes_ProcessStart_ProcessNode, gen_model_export_Export_INamed},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
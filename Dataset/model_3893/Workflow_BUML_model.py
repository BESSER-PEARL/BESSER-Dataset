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
workflow_ActivityO = Class(name="workflow::ActivityO")
ActivityAspect = Class(name="ActivityAspect")
workflow_Agent = Class(name="workflow::Agent")
workflow_Case = Class(name="workflow::Case")
workflow_CaseAspect = Class(name="workflow::CaseAspect", is_abstract=True)
workflow_Activity = Class(name="workflow::Activity")
workflow_Process = Class(name="workflow::Process")
workflow_RuntimeCoreModel = Class(name="workflow::RuntimeCoreModel")
workflow_ActivityAspect = Class(name="workflow::ActivityAspect", is_abstract=True)
workflow_Task = Class(name="workflow::Task")
workflow_TaskO = Class(name="workflow::TaskO")
TaskAspect = Class(name="TaskAspect")
workflow_Role = Class(name="workflow::Role")
workflow_TaskC = Class(name="workflow::TaskC", is_abstract=True)
workflow_ActivityC = Class(name="workflow::ActivityC")
workflow_CaseC = Class(name="workflow::CaseC")
workflow_Control = Class(name="workflow::Control", is_abstract=True)
ProcessAspect = Class(name="ProcessAspect")
CaseAspect = Class(name="CaseAspect")
workflow_State = Class(name="workflow::State", is_abstract=True)
workflow_PetriNet = Class(name="workflow::PetriNet")
Control = Class(name="Control")
workflow_Arc = Class(name="workflow::Arc")
workflow_Place = Class(name="workflow::Place")
workflow_Transition = Class(name="workflow::Transition")
TaskC = Class(name="TaskC")
workflow_RuntimeInformation = Class(name="workflow::RuntimeInformation")
workflow_Token = Class(name="workflow::Token")
workflow_ModelRegistry = Class(name="workflow::ModelRegistry")
workflow_WorkflowEngine = Class(name="workflow::WorkflowEngine")
workflow_CoreModel = Class(name="workflow::CoreModel")
workflow_GlobalAspect = Class(name="workflow::GlobalAspect", is_abstract=True)
workflow_Information = Class(name="workflow::Information")
workflow_ProcessDocument = Class(name="workflow::ProcessDocument")
workflow_TaskI = Class(name="workflow::TaskI")
workflow_DocumentDescriptor = Class(name="workflow::DocumentDescriptor", is_abstract=True)
workflow_DocumentCondition = Class(name="workflow::DocumentCondition", is_abstract=True)
workflow_DocumentType = Class(name="workflow::DocumentType", is_abstract=True)
workflow_Marking = Class(name="workflow::Marking")
State = Class(name="State")
workflow_CaseI = Class(name="workflow::CaseI")
workflow_String2DocumentMap = Class(name="workflow::String2DocumentMap")
workflow_ModelAspect = Class(name="workflow::ModelAspect", is_abstract=True)
workflow_ProcessAspect = Class(name="workflow::ProcessAspect", is_abstract=True)
workflow_TaskAspect = Class(name="workflow::TaskAspect", is_abstract=True)
workflow_RuntimeModelAspect = Class(name="workflow::RuntimeModelAspect", is_abstract=True)
workflow_ActivityI = Class(name="workflow::ActivityI")
workflow_Document = Class(name="workflow::Document", is_abstract=True)
workflow_OrganisationAspect = Class(name="workflow::OrganisationAspect")
ModelAspect = Class(name="ModelAspect")
workflow_ControlAspect = Class(name="workflow::ControlAspect")
workflow_RuntimeGlobalAspect = Class(name="workflow::RuntimeGlobalAspect", is_abstract=True)
workflow_ProcessO = Class(name="workflow::ProcessO")
workflow_Expression = Class(name="workflow::Expression")
workflow_DefaultDocumentType = Class(name="workflow::DefaultDocumentType")
DocumentType = Class(name="DocumentType")
workflow_Field = Class(name="workflow::Field")
workflow_EnumField = Class(name="workflow::EnumField")
workflow_InformationAspect = Class(name="workflow::InformationAspect")
workflow_CaseO = Class(name="workflow::CaseO")
workflow_InformationRuntimeAspect = Class(name="workflow::InformationRuntimeAspect")
RuntimeModelAspect = Class(name="RuntimeModelAspect")
workflow_DefaultDocumentDescriptor = Class(name="workflow::DefaultDocumentDescriptor")
DocumentDescriptor = Class(name="DocumentDescriptor")
workflow_Atom = Class(name="workflow::Atom")
Expression = Class(name="Expression")
workflow_Operator = Class(name="workflow::Operator")
workflow_DocumentDescrAtom = Class(name="workflow::DocumentDescrAtom")
Atom = Class(name="Atom")
workflow_FieldAtom = Class(name="workflow::FieldAtom")
workflow_ConstantAtom = Class(name="workflow::ConstantAtom")
workflow_DotOperator = Class(name="workflow::DotOperator")
Operator = Class(name="Operator")
workflow_EqualToOperator = Class(name="workflow::EqualToOperator")
workflow_DefaultDocument = Class(name="workflow::DefaultDocument")
Document = Class(name="Document")
workflow_FieldValue = Class(name="workflow::FieldValue")
workflow_EnumFieldValue = Class(name="workflow::EnumFieldValue")
workflow_LessThanOperator = Class(name="workflow::LessThanOperator")
workflow_GreaterThanOperator = Class(name="workflow::GreaterThanOperator")
workflow_EnumFieldAtom = Class(name="workflow::EnumFieldAtom")
workflow_EnumLiteralAtom = Class(name="workflow::EnumLiteralAtom")
workflow_UnequalToOperator = Class(name="workflow::UnequalToOperator")
workflow_AgentContainer = Class(name="workflow::AgentContainer")
RuntimeGlobalAspect = Class(name="RuntimeGlobalAspect")
workflow_Organisation = Class(name="workflow::Organisation")
GlobalAspect = Class(name="GlobalAspect")
workflow_DocumentTypeContainer = Class(name="workflow::DocumentTypeContainer")
workflow_DefaultDocumentCondition = Class(name="workflow::DefaultDocumentCondition")
DocumentCondition = Class(name="DocumentCondition")
workflow_EnumLiteral = Class(name="workflow::EnumLiteral")
workflow_DocumentContainer = Class(name="workflow::DocumentContainer")

# workflow_ActivityO class attributes and methods

# ActivityAspect class attributes and methods

# workflow_Agent class attributes and methods
workflow_Agent_name: Property = Property(name="name", type=StringType)
workflow_Agent_username: Property = Property(name="username", type=StringType)
workflow_Agent_password: Property = Property(name="password", type=StringType)
workflow_Agent.attributes={workflow_Agent_username, workflow_Agent_name, workflow_Agent_password}

# workflow_Case class attributes and methods
workflow_Case_id: Property = Property(name="id", type=StringType)
workflow_Case_client: Property = Property(name="client", type=StringType)
workflow_Case_started: Property = Property(name="started", type=BooleanType)
workflow_Case_finished: Property = Property(name="finished", type=BooleanType)
workflow_Case.attributes={workflow_Case_client, workflow_Case_finished, workflow_Case_started, workflow_Case_id}

# workflow_CaseAspect class attributes and methods

# workflow_Activity class attributes and methods
workflow_Activity_started: Property = Property(name="started", type=BooleanType)
workflow_Activity_finished: Property = Property(name="finished", type=BooleanType)
workflow_Activity.attributes={workflow_Activity_started, workflow_Activity_finished}

# workflow_Process class attributes and methods
workflow_Process_name: Property = Property(name="name", type=StringType)
workflow_Process.attributes={workflow_Process_name}

# workflow_RuntimeCoreModel class attributes and methods

# workflow_ActivityAspect class attributes and methods

# workflow_Task class attributes and methods
workflow_Task_name: Property = Property(name="name", type=StringType)
workflow_Task.attributes={workflow_Task_name}

# workflow_TaskO class attributes and methods
workflow_TaskO_name: Property = Property(name="name", type=StringType)
workflow_TaskO.attributes={workflow_TaskO_name}

# TaskAspect class attributes and methods

# workflow_Role class attributes and methods
workflow_Role_name: Property = Property(name="name", type=StringType)
workflow_Role.attributes={workflow_Role_name}

# workflow_TaskC class attributes and methods
workflow_TaskC_name: Property = Property(name="name", type=StringType)
workflow_TaskC.attributes={workflow_TaskC_name}

# workflow_ActivityC class attributes and methods

# workflow_CaseC class attributes and methods

# workflow_Control class attributes and methods

# ProcessAspect class attributes and methods

# CaseAspect class attributes and methods

# workflow_State class attributes and methods

# workflow_PetriNet class attributes and methods

# Control class attributes and methods

# workflow_Arc class attributes and methods
workflow_Arc_name: Property = Property(name="name", type=StringType)
workflow_Arc.attributes={workflow_Arc_name}

# workflow_Place class attributes and methods
workflow_Place_name: Property = Property(name="name", type=StringType)
workflow_Place.attributes={workflow_Place_name}

# workflow_Transition class attributes and methods

# TaskC class attributes and methods

# workflow_RuntimeInformation class attributes and methods
workflow_RuntimeInformation_caseIdCount: Property = Property(name="caseIdCount", type=StringType)
workflow_RuntimeInformation.attributes={workflow_RuntimeInformation_caseIdCount}

# workflow_Token class attributes and methods

# workflow_ModelRegistry class attributes and methods

# workflow_WorkflowEngine class attributes and methods

# workflow_CoreModel class attributes and methods
workflow_CoreModel_name: Property = Property(name="name", type=StringType)
workflow_CoreModel.attributes={workflow_CoreModel_name}

# workflow_GlobalAspect class attributes and methods

# workflow_Information class attributes and methods

# workflow_ProcessDocument class attributes and methods
workflow_ProcessDocument_name: Property = Property(name="name", type=StringType)
workflow_ProcessDocument.attributes={workflow_ProcessDocument_name}

# workflow_TaskI class attributes and methods

# workflow_DocumentDescriptor class attributes and methods
workflow_DocumentDescriptor_name: Property = Property(name="name", type=StringType)
workflow_DocumentDescriptor.attributes={workflow_DocumentDescriptor_name}

# workflow_DocumentCondition class attributes and methods
workflow_DocumentCondition_name: Property = Property(name="name", type=StringType)
workflow_DocumentCondition.attributes={workflow_DocumentCondition_name}

# workflow_DocumentType class attributes and methods
workflow_DocumentType_name: Property = Property(name="name", type=StringType)
workflow_DocumentType.attributes={workflow_DocumentType_name}

# workflow_Marking class attributes and methods

# State class attributes and methods

# workflow_CaseI class attributes and methods

# workflow_String2DocumentMap class attributes and methods
workflow_String2DocumentMap_key: Property = Property(name="key", type=StringType)
workflow_String2DocumentMap.attributes={workflow_String2DocumentMap_key}

# workflow_ModelAspect class attributes and methods

# workflow_ProcessAspect class attributes and methods

# workflow_TaskAspect class attributes and methods

# workflow_RuntimeModelAspect class attributes and methods

# workflow_ActivityI class attributes and methods

# workflow_Document class attributes and methods
workflow_Document_name: Property = Property(name="name", type=StringType)
workflow_Document_id: Property = Property(name="id", type=StringType)
workflow_Document.attributes={workflow_Document_name, workflow_Document_id}

# workflow_OrganisationAspect class attributes and methods

# ModelAspect class attributes and methods

# workflow_ControlAspect class attributes and methods

# workflow_RuntimeGlobalAspect class attributes and methods

# workflow_ProcessO class attributes and methods

# workflow_Expression class attributes and methods

# workflow_DefaultDocumentType class attributes and methods

# DocumentType class attributes and methods

# workflow_Field class attributes and methods
workflow_Field_name: Property = Property(name="name", type=StringType)
workflow_Field.attributes={workflow_Field_name}

# workflow_EnumField class attributes and methods
workflow_EnumField_name: Property = Property(name="name", type=StringType)
workflow_EnumField.attributes={workflow_EnumField_name}

# workflow_InformationAspect class attributes and methods

# workflow_CaseO class attributes and methods

# workflow_InformationRuntimeAspect class attributes and methods

# RuntimeModelAspect class attributes and methods

# workflow_DefaultDocumentDescriptor class attributes and methods

# DocumentDescriptor class attributes and methods

# workflow_Atom class attributes and methods

# Expression class attributes and methods

# workflow_Operator class attributes and methods

# workflow_DocumentDescrAtom class attributes and methods

# Atom class attributes and methods

# workflow_FieldAtom class attributes and methods

# workflow_ConstantAtom class attributes and methods
workflow_ConstantAtom_value: Property = Property(name="value", type=StringType)
workflow_ConstantAtom.attributes={workflow_ConstantAtom_value}

# workflow_DotOperator class attributes and methods

# Operator class attributes and methods

# workflow_EqualToOperator class attributes and methods

# workflow_DefaultDocument class attributes and methods
workflow_DefaultDocument_placeholder: Property = Property(name="placeholder", type=BooleanType)
workflow_DefaultDocument.attributes={workflow_DefaultDocument_placeholder}

# Document class attributes and methods

# workflow_FieldValue class attributes and methods
workflow_FieldValue_value: Property = Property(name="value", type=StringType)
workflow_FieldValue.attributes={workflow_FieldValue_value}

# workflow_EnumFieldValue class attributes and methods

# workflow_LessThanOperator class attributes and methods

# workflow_GreaterThanOperator class attributes and methods

# workflow_EnumFieldAtom class attributes and methods

# workflow_EnumLiteralAtom class attributes and methods

# workflow_UnequalToOperator class attributes and methods

# workflow_AgentContainer class attributes and methods
workflow_AgentContainer_name: Property = Property(name="name", type=StringType)
workflow_AgentContainer.attributes={workflow_AgentContainer_name}

# RuntimeGlobalAspect class attributes and methods

# workflow_Organisation class attributes and methods
workflow_Organisation_name: Property = Property(name="name", type=StringType)
workflow_Organisation.attributes={workflow_Organisation_name}

# GlobalAspect class attributes and methods

# workflow_DocumentTypeContainer class attributes and methods
workflow_DocumentTypeContainer_name: Property = Property(name="name", type=StringType)
workflow_DocumentTypeContainer.attributes={workflow_DocumentTypeContainer_name}

# workflow_DefaultDocumentCondition class attributes and methods

# DocumentCondition class attributes and methods

# workflow_EnumLiteral class attributes and methods
workflow_EnumLiteral_name: Property = Property(name="name", type=StringType)
workflow_EnumLiteral.attributes={workflow_EnumLiteral_name}

# workflow_DocumentContainer class attributes and methods
workflow_DocumentContainer_name: Property = Property(name="name", type=StringType)
workflow_DocumentContainer.attributes={workflow_DocumentContainer_name}

# Relationships
requiredRoles0: BinaryAssociation = BinaryAssociation(
    name="requiredRoles0",
    ends={
        Property(name="workflow_TaskO", type=workflow_Role, multiplicity=Multiplicity(1, 9999)),
        Property(name="workflow_Role", type=workflow_TaskO, multiplicity=Multiplicity(1, 1))
    }
)
followsUpOn2: BinaryAssociation = BinaryAssociation(
    name="followsUpOn2",
    ends={
        Property(name="workflow_TaskO3", type=workflow_TaskO, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_TaskO1", type=workflow_TaskO, multiplicity=Multiplicity(1, 1))
    }
)
assignedTo4: BinaryAssociation = BinaryAssociation(
    name="assignedTo4",
    ends={
        Property(name="Agent", type=workflow_ActivityO, multiplicity=Multiplicity(1, 1)),
        Property(name="active", type=workflow_Agent, multiplicity=Multiplicity(0, 1))
    }
)
aspects5: BinaryAssociation = BinaryAssociation(
    name="aspects5",
    ends={
        Property(name="CaseAspect", type=workflow_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="core", type=workflow_CaseAspect, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activities6: BinaryAssociation = BinaryAssociation(
    name="activities6",
    ends={
        Property(name="workflow_Activity", type=workflow_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Case", type=workflow_Activity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process7: BinaryAssociation = BinaryAssociation(
    name="process7",
    ends={
        Property(name="workflow_Process", type=workflow_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Case8", type=workflow_Process, multiplicity=Multiplicity(1, 1))
    }
)
runtimeCoreModel9: BinaryAssociation = BinaryAssociation(
    name="runtimeCoreModel9",
    ends={
        Property(name="RuntimeCoreModel", type=workflow_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="cases", type=workflow_RuntimeCoreModel, multiplicity=Multiplicity(1, 1))
    }
)
aspects10: BinaryAssociation = BinaryAssociation(
    name="aspects10",
    ends={
        Property(name="ActivityAspect", type=workflow_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="core11", type=workflow_ActivityAspect, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task12: BinaryAssociation = BinaryAssociation(
    name="task12",
    ends={
        Property(name="workflow_Task", type=workflow_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Activity13", type=workflow_Task, multiplicity=Multiplicity(1, 1))
    }
)
EReference014: BinaryAssociation = BinaryAssociation(
    name="EReference014",
    ends={
        Property(name="workflow_ActivityAspect", type=workflow_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Activity15", type=workflow_ActivityAspect, multiplicity=Multiplicity(0, 1))
    }
)
takenRoles16: BinaryAssociation = BinaryAssociation(
    name="takenRoles16",
    ends={
        Property(name="workflow_Role17", type=workflow_Agent, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Agent", type=workflow_Role, multiplicity=Multiplicity(1, 9999))
    }
)
case22: BinaryAssociation = BinaryAssociation(
    name="case22",
    ends={
        Property(name="workflow_CaseC", type=workflow_ActivityC, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_ActivityC", type=workflow_CaseC, multiplicity=Multiplicity(1, 1))
    }
)
state23: BinaryAssociation = BinaryAssociation(
    name="state23",
    ends={
        Property(name="workflow_State", type=workflow_CaseC, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_CaseC24", type=workflow_State, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arcs25: BinaryAssociation = BinaryAssociation(
    name="arcs25",
    ends={
        Property(name="workflow_Arc", type=workflow_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_PetriNet", type=workflow_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
places26: BinaryAssociation = BinaryAssociation(
    name="places26",
    ends={
        Property(name="workflow_Place", type=workflow_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_PetriNet27", type=workflow_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
start28: BinaryAssociation = BinaryAssociation(
    name="start28",
    ends={
        Property(name="workflow_Place30", type=workflow_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_PetriNet29", type=workflow_Place, multiplicity=Multiplicity(1, 1))
    }
)
finish31: BinaryAssociation = BinaryAssociation(
    name="finish31",
    ends={
        Property(name="workflow_Place33", type=workflow_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_PetriNet32", type=workflow_Place, multiplicity=Multiplicity(1, 1))
    }
)
out34: BinaryAssociation = BinaryAssociation(
    name="out34",
    ends={
        Property(name="Arc", type=workflow_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceTransition", type=workflow_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
in35: BinaryAssociation = BinaryAssociation(
    name="in35",
    ends={
        Property(name="Arc36", type=workflow_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="targetTransition", type=workflow_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
sourcePlace37: BinaryAssociation = BinaryAssociation(
    name="sourcePlace37",
    ends={
        Property(name="Place", type=workflow_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=workflow_Place, multiplicity=Multiplicity(1, 1))
    }
)
targetPlace38: BinaryAssociation = BinaryAssociation(
    name="targetPlace38",
    ends={
        Property(name="Place39", type=workflow_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="in", type=workflow_Place, multiplicity=Multiplicity(1, 1))
    }
)
sourceTransition40: BinaryAssociation = BinaryAssociation(
    name="sourceTransition40",
    ends={
        Property(name="Transition", type=workflow_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="out41", type=workflow_Transition, multiplicity=Multiplicity(1, 1))
    }
)
active18: BinaryAssociation = BinaryAssociation(
    name="active18",
    ends={
        Property(name="ActivityO", type=workflow_Agent, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedTo", type=workflow_ActivityO, multiplicity=Multiplicity(0, 9999))
    }
)
mayTakeRoles19: BinaryAssociation = BinaryAssociation(
    name="mayTakeRoles19",
    ends={
        Property(name="workflow_Role21", type=workflow_Agent, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Agent20", type=workflow_Role, multiplicity=Multiplicity(1, 9999))
    }
)
tokens49: BinaryAssociation = BinaryAssociation(
    name="tokens49",
    ends={
        Property(name="workflow_Token", type=workflow_Marking, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Marking", type=workflow_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
petrinet50: BinaryAssociation = BinaryAssociation(
    name="petrinet50",
    ends={
        Property(name="workflow_PetriNet52", type=workflow_Marking, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Marking51", type=workflow_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
place53: BinaryAssociation = BinaryAssociation(
    name="place53",
    ends={
        Property(name="workflow_Place55", type=workflow_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Token54", type=workflow_Place, multiplicity=Multiplicity(1, 1))
    }
)
engine56: BinaryAssociation = BinaryAssociation(
    name="engine56",
    ends={
        Property(name="WorkflowEngine", type=workflow_ModelRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="modelRegistry", type=workflow_WorkflowEngine, multiplicity=Multiplicity(1, 1))
    }
)
coreModels57: BinaryAssociation = BinaryAssociation(
    name="coreModels57",
    ends={
        Property(name="CoreModel", type=workflow_ModelRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="modelRegistry58", type=workflow_CoreModel, multiplicity=Multiplicity(0, 9999))
    }
)
globalAspects59: BinaryAssociation = BinaryAssociation(
    name="globalAspects59",
    ends={
        Property(name="GlobalAspect", type=workflow_ModelRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="modelRegistry60", type=workflow_GlobalAspect, multiplicity=Multiplicity(0, 9999))
    }
)
processDocuments61: BinaryAssociation = BinaryAssociation(
    name="processDocuments61",
    ends={
        Property(name="workflow_ProcessDocument", type=workflow_Information, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Information", type=workflow_ProcessDocument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in62: BinaryAssociation = BinaryAssociation(
    name="in62",
    ends={
        Property(name="workflow_DocumentDescriptor", type=workflow_TaskI, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_TaskI", type=workflow_DocumentDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out63: BinaryAssociation = BinaryAssociation(
    name="out63",
    ends={
        Property(name="workflow_DocumentDescriptor65", type=workflow_TaskI, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_TaskI64", type=workflow_DocumentDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
start66: BinaryAssociation = BinaryAssociation(
    name="start66",
    ends={
        Property(name="workflow_DocumentCondition", type=workflow_TaskI, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_TaskI67", type=workflow_DocumentCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finish68: BinaryAssociation = BinaryAssociation(
    name="finish68",
    ends={
        Property(name="workflow_DocumentCondition70", type=workflow_TaskI, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_TaskI69", type=workflow_DocumentCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
documentType71: BinaryAssociation = BinaryAssociation(
    name="documentType71",
    ends={
        Property(name="workflow_DocumentType", type=workflow_DocumentDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_DocumentDescriptor72", type=workflow_DocumentType, multiplicity=Multiplicity(1, 1))
    }
)
processDocument73: BinaryAssociation = BinaryAssociation(
    name="processDocument73",
    ends={
        Property(name="workflow_ProcessDocument75", type=workflow_DocumentDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_DocumentDescriptor74", type=workflow_ProcessDocument, multiplicity=Multiplicity(1, 1))
    }
)
targetTransition42: BinaryAssociation = BinaryAssociation(
    name="targetTransition42",
    ends={
        Property(name="Transition44", type=workflow_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="in43", type=workflow_Transition, multiplicity=Multiplicity(1, 1))
    }
)
in45: BinaryAssociation = BinaryAssociation(
    name="in45",
    ends={
        Property(name="Arc46", type=workflow_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="targetPlace", type=workflow_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
out47: BinaryAssociation = BinaryAssociation(
    name="out47",
    ends={
        Property(name="Arc48", type=workflow_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="sourcePlace", type=workflow_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
caseDocuments83: BinaryAssociation = BinaryAssociation(
    name="caseDocuments83",
    ends={
        Property(name="workflow_String2DocumentMap", type=workflow_CaseI, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_CaseI", type=workflow_String2DocumentMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process84: BinaryAssociation = BinaryAssociation(
    name="process84",
    ends={
        Property(name="workflow_ProcessAspect", type=workflow_ModelAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_ModelAspect", type=workflow_ProcessAspect, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tasks85: BinaryAssociation = BinaryAssociation(
    name="tasks85",
    ends={
        Property(name="workflow_TaskAspect", type=workflow_ProcessAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_ProcessAspect86", type=workflow_TaskAspect, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
core87: BinaryAssociation = BinaryAssociation(
    name="core87",
    ends={
        Property(name="Process", type=workflow_ProcessAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="aspects", type=workflow_Process, multiplicity=Multiplicity(1, 1))
    }
)
core88: BinaryAssociation = BinaryAssociation(
    name="core88",
    ends={
        Property(name="Task", type=workflow_TaskAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="aspects89", type=workflow_Task, multiplicity=Multiplicity(1, 1))
    }
)
process90: BinaryAssociation = BinaryAssociation(
    name="process90",
    ends={
        Property(name="workflow_ProcessAspect91", type=workflow_CaseAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_CaseAspect", type=workflow_ProcessAspect, multiplicity=Multiplicity(0, 1))
    }
)
core92: BinaryAssociation = BinaryAssociation(
    name="core92",
    ends={
        Property(name="Case", type=workflow_CaseAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="aspects93", type=workflow_Case, multiplicity=Multiplicity(1, 1))
    }
)
task94: BinaryAssociation = BinaryAssociation(
    name="task94",
    ends={
        Property(name="workflow_TaskAspect96", type=workflow_ActivityAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_ActivityAspect95", type=workflow_TaskAspect, multiplicity=Multiplicity(1, 1))
    }
)
core97: BinaryAssociation = BinaryAssociation(
    name="core97",
    ends={
        Property(name="Activity", type=workflow_ActivityAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="aspects98", type=workflow_Activity, multiplicity=Multiplicity(1, 1))
    }
)
aspects99: BinaryAssociation = BinaryAssociation(
    name="aspects99",
    ends={
        Property(name="workflow_ModelAspect100", type=workflow_CoreModel, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_CoreModel", type=workflow_ModelAspect, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process101: BinaryAssociation = BinaryAssociation(
    name="process101",
    ends={
        Property(name="Process102", type=workflow_CoreModel, multiplicity=Multiplicity(1, 1)),
        Property(name="coreModel", type=workflow_Process, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelRegistry103: BinaryAssociation = BinaryAssociation(
    name="modelRegistry103",
    ends={
        Property(name="ModelRegistry", type=workflow_CoreModel, multiplicity=Multiplicity(1, 1)),
        Property(name="coreModels", type=workflow_ModelRegistry, multiplicity=Multiplicity(1, 1))
    }
)
in76: BinaryAssociation = BinaryAssociation(
    name="in76",
    ends={
        Property(name="workflow_Document", type=workflow_ActivityI, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_ActivityI", type=workflow_Document, multiplicity=Multiplicity(0, 9999))
    }
)
out77: BinaryAssociation = BinaryAssociation(
    name="out77",
    ends={
        Property(name="workflow_Document79", type=workflow_ActivityI, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_ActivityI78", type=workflow_Document, multiplicity=Multiplicity(0, 9999))
    }
)
DocumentType80: BinaryAssociation = BinaryAssociation(
    name="DocumentType80",
    ends={
        Property(name="workflow_DocumentType82", type=workflow_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Document81", type=workflow_DocumentType, multiplicity=Multiplicity(1, 1))
    }
)
aspects111: BinaryAssociation = BinaryAssociation(
    name="aspects111",
    ends={
        Property(name="TaskAspect", type=workflow_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="core112", type=workflow_TaskAspect, multiplicity=Multiplicity(0, 9999))
    }
)
aspects113: BinaryAssociation = BinaryAssociation(
    name="aspects113",
    ends={
        Property(name="workflow_RuntimeModelAspect", type=workflow_RuntimeCoreModel, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_RuntimeCoreModel", type=workflow_RuntimeModelAspect, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cases114: BinaryAssociation = BinaryAssociation(
    name="cases114",
    ends={
        Property(name="Case115", type=workflow_RuntimeCoreModel, multiplicity=Multiplicity(1, 1)),
        Property(name="runtimeCoreModel", type=workflow_Case, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coreModel116: BinaryAssociation = BinaryAssociation(
    name="coreModel116",
    ends={
        Property(name="workflow_CoreModel118", type=workflow_RuntimeCoreModel, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_RuntimeCoreModel117", type=workflow_CoreModel, multiplicity=Multiplicity(1, 1))
    }
)
modelRegistry119: BinaryAssociation = BinaryAssociation(
    name="modelRegistry119",
    ends={
        Property(name="ModelRegistry120", type=workflow_WorkflowEngine, multiplicity=Multiplicity(1, 1)),
        Property(name="engine", type=workflow_ModelRegistry, multiplicity=Multiplicity(1, 1))
    }
)
runtimeCoreModels121: BinaryAssociation = BinaryAssociation(
    name="runtimeCoreModels121",
    ends={
        Property(name="workflow_RuntimeCoreModel122", type=workflow_WorkflowEngine, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_WorkflowEngine", type=workflow_RuntimeCoreModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
runtimeGlobalAspects123: BinaryAssociation = BinaryAssociation(
    name="runtimeGlobalAspects123",
    ends={
        Property(name="RuntimeGlobalAspect", type=workflow_WorkflowEngine, multiplicity=Multiplicity(1, 1)),
        Property(name="engine124", type=workflow_RuntimeGlobalAspect, multiplicity=Multiplicity(0, 9999))
    }
)
involved125: BinaryAssociation = BinaryAssociation(
    name="involved125",
    ends={
        Property(name="workflow_Role126", type=workflow_ProcessO, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_ProcessO", type=workflow_Role, multiplicity=Multiplicity(0, 9999))
    }
)
fields127: BinaryAssociation = BinaryAssociation(
    name="fields127",
    ends={
        Property(name="workflow_Field", type=workflow_DefaultDocumentType, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_DefaultDocumentType", type=workflow_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumFields128: BinaryAssociation = BinaryAssociation(
    name="enumFields128",
    ends={
        Property(name="workflow_EnumField", type=workflow_DefaultDocumentType, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_DefaultDocumentType129", type=workflow_EnumField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tasks104: BinaryAssociation = BinaryAssociation(
    name="tasks104",
    ends={
        Property(name="workflow_Task106", type=workflow_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Process105", type=workflow_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coreModel107: BinaryAssociation = BinaryAssociation(
    name="coreModel107",
    ends={
        Property(name="CoreModel108", type=workflow_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="process", type=workflow_CoreModel, multiplicity=Multiplicity(1, 1))
    }
)
aspects109: BinaryAssociation = BinaryAssociation(
    name="aspects109",
    ends={
        Property(name="ProcessAspect", type=workflow_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="core110", type=workflow_ProcessAspect, multiplicity=Multiplicity(0, 9999))
    }
)
involved136: BinaryAssociation = BinaryAssociation(
    name="involved136",
    ends={
        Property(name="workflow_Agent137", type=workflow_CaseO, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_CaseO", type=workflow_Agent, multiplicity=Multiplicity(0, 9999))
    }
)
documentType138: BinaryAssociation = BinaryAssociation(
    name="documentType138",
    ends={
        Property(name="workflow_DocumentType140", type=workflow_ProcessDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_ProcessDocument139", type=workflow_DocumentType, multiplicity=Multiplicity(1, 1))
    }
)
value141: BinaryAssociation = BinaryAssociation(
    name="value141",
    ends={
        Property(name="workflow_Document143", type=workflow_String2DocumentMap, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_String2DocumentMap142", type=workflow_Document, multiplicity=Multiplicity(1, 1))
    }
)
operands144: BinaryAssociation = BinaryAssociation(
    name="operands144",
    ends={
        Property(name="workflow_Expression", type=workflow_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Operator", type=workflow_Expression, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
descriptor145: BinaryAssociation = BinaryAssociation(
    name="descriptor145",
    ends={
        Property(name="workflow_DocumentDescriptor146", type=workflow_DocumentDescrAtom, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_DocumentDescrAtom", type=workflow_DocumentDescriptor, multiplicity=Multiplicity(1, 1))
    }
)
field147: BinaryAssociation = BinaryAssociation(
    name="field147",
    ends={
        Property(name="workflow_Field148", type=workflow_FieldAtom, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_FieldAtom", type=workflow_Field, multiplicity=Multiplicity(1, 1))
    }
)
fieldValues130: BinaryAssociation = BinaryAssociation(
    name="fieldValues130",
    ends={
        Property(name="workflow_FieldValue", type=workflow_DefaultDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_DefaultDocument", type=workflow_FieldValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumFieldValues131: BinaryAssociation = BinaryAssociation(
    name="enumFieldValues131",
    ends={
        Property(name="workflow_EnumFieldValue", type=workflow_DefaultDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_DefaultDocument132", type=workflow_EnumFieldValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
field133: BinaryAssociation = BinaryAssociation(
    name="field133",
    ends={
        Property(name="workflow_Field135", type=workflow_FieldValue, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_FieldValue134", type=workflow_Field, multiplicity=Multiplicity(1, 1))
    }
)
enumField156: BinaryAssociation = BinaryAssociation(
    name="enumField156",
    ends={
        Property(name="workflow_EnumField158", type=workflow_EnumFieldValue, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_EnumFieldValue157", type=workflow_EnumField, multiplicity=Multiplicity(1, 1))
    }
)
enumValue159: BinaryAssociation = BinaryAssociation(
    name="enumValue159",
    ends={
        Property(name="workflow_EnumLiteral161", type=workflow_EnumFieldValue, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_EnumFieldValue160", type=workflow_EnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
enumField162: BinaryAssociation = BinaryAssociation(
    name="enumField162",
    ends={
        Property(name="workflow_EnumField163", type=workflow_EnumFieldAtom, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_EnumFieldAtom", type=workflow_EnumField, multiplicity=Multiplicity(1, 1))
    }
)
enumLiteral164: BinaryAssociation = BinaryAssociation(
    name="enumLiteral164",
    ends={
        Property(name="workflow_EnumLiteral165", type=workflow_EnumLiteralAtom, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_EnumLiteralAtom", type=workflow_EnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
agents166: BinaryAssociation = BinaryAssociation(
    name="agents166",
    ends={
        Property(name="workflow_Agent167", type=workflow_AgentContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_AgentContainer", type=workflow_Agent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roles168: BinaryAssociation = BinaryAssociation(
    name="roles168",
    ends={
        Property(name="workflow_Role169", type=workflow_Organisation, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Organisation", type=workflow_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelRegistry170: BinaryAssociation = BinaryAssociation(
    name="modelRegistry170",
    ends={
        Property(name="ModelRegistry171", type=workflow_GlobalAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="globalAspects", type=workflow_ModelRegistry, multiplicity=Multiplicity(1, 1))
    }
)
engine172: BinaryAssociation = BinaryAssociation(
    name="engine172",
    ends={
        Property(name="WorkflowEngine173", type=workflow_RuntimeGlobalAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="runtimeGlobalAspects", type=workflow_WorkflowEngine, multiplicity=Multiplicity(1, 1))
    }
)
expression149: BinaryAssociation = BinaryAssociation(
    name="expression149",
    ends={
        Property(name="workflow_Expression150", type=workflow_DefaultDocumentCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_DefaultDocumentCondition", type=workflow_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enumLiterals151: BinaryAssociation = BinaryAssociation(
    name="enumLiterals151",
    ends={
        Property(name="workflow_EnumLiteral", type=workflow_EnumField, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_EnumField152", type=workflow_EnumLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
defaultValue153: BinaryAssociation = BinaryAssociation(
    name="defaultValue153",
    ends={
        Property(name="workflow_EnumLiteral155", type=workflow_EnumField, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_EnumField154", type=workflow_EnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
documentTypes174: BinaryAssociation = BinaryAssociation(
    name="documentTypes174",
    ends={
        Property(name="workflow_DocumentType175", type=workflow_DocumentTypeContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_DocumentTypeContainer", type=workflow_DocumentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
documents176: BinaryAssociation = BinaryAssociation(
    name="documents176",
    ends={
        Property(name="workflow_Document177", type=workflow_DocumentContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_DocumentContainer", type=workflow_Document, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_workflow_ActivityO_ActivityAspect = Generalization(general=ActivityAspect, specific=workflow_ActivityO)
gen_workflow_TaskO_TaskAspect = Generalization(general=TaskAspect, specific=workflow_TaskO)
gen_workflow_TaskC_TaskAspect = Generalization(general=TaskAspect, specific=workflow_TaskC)
gen_workflow_ActivityC_ActivityAspect = Generalization(general=ActivityAspect, specific=workflow_ActivityC)
gen_workflow_Control_ProcessAspect = Generalization(general=ProcessAspect, specific=workflow_Control)
gen_workflow_CaseC_CaseAspect = Generalization(general=CaseAspect, specific=workflow_CaseC)
gen_workflow_PetriNet_Control = Generalization(general=Control, specific=workflow_PetriNet)
gen_workflow_Transition_TaskC = Generalization(general=TaskC, specific=workflow_Transition)
gen_workflow_Information_ProcessAspect = Generalization(general=ProcessAspect, specific=workflow_Information)
gen_workflow_TaskI_TaskAspect = Generalization(general=TaskAspect, specific=workflow_TaskI)
gen_workflow_Marking_State = Generalization(general=State, specific=workflow_Marking)
gen_workflow_CaseI_CaseAspect = Generalization(general=CaseAspect, specific=workflow_CaseI)
gen_workflow_ActivityI_ActivityAspect = Generalization(general=ActivityAspect, specific=workflow_ActivityI)
gen_workflow_OrganisationAspect_ModelAspect = Generalization(general=ModelAspect, specific=workflow_OrganisationAspect)
gen_workflow_ControlAspect_ModelAspect = Generalization(general=ModelAspect, specific=workflow_ControlAspect)
gen_workflow_ProcessO_ProcessAspect = Generalization(general=ProcessAspect, specific=workflow_ProcessO)
gen_workflow_DefaultDocumentType_DocumentType = Generalization(general=DocumentType, specific=workflow_DefaultDocumentType)
gen_workflow_InformationAspect_ModelAspect = Generalization(general=ModelAspect, specific=workflow_InformationAspect)
gen_workflow_CaseO_CaseAspect = Generalization(general=CaseAspect, specific=workflow_CaseO)
gen_workflow_InformationRuntimeAspect_RuntimeModelAspect = Generalization(general=RuntimeModelAspect, specific=workflow_InformationRuntimeAspect)
gen_workflow_DefaultDocumentDescriptor_DocumentDescriptor = Generalization(general=DocumentDescriptor, specific=workflow_DefaultDocumentDescriptor)
gen_workflow_Atom_Expression = Generalization(general=Expression, specific=workflow_Atom)
gen_workflow_Operator_Expression = Generalization(general=Expression, specific=workflow_Operator)
gen_workflow_DocumentDescrAtom_Atom = Generalization(general=Atom, specific=workflow_DocumentDescrAtom)
gen_workflow_FieldAtom_Atom = Generalization(general=Atom, specific=workflow_FieldAtom)
gen_workflow_ConstantAtom_Atom = Generalization(general=Atom, specific=workflow_ConstantAtom)
gen_workflow_DotOperator_Operator = Generalization(general=Operator, specific=workflow_DotOperator)
gen_workflow_EqualToOperator_Operator = Generalization(general=Operator, specific=workflow_EqualToOperator)
gen_workflow_DefaultDocument_Document = Generalization(general=Document, specific=workflow_DefaultDocument)
gen_workflow_LessThanOperator_Operator = Generalization(general=Operator, specific=workflow_LessThanOperator)
gen_workflow_GreaterThanOperator_Operator = Generalization(general=Operator, specific=workflow_GreaterThanOperator)
gen_workflow_EnumFieldAtom_Atom = Generalization(general=Atom, specific=workflow_EnumFieldAtom)
gen_workflow_EnumLiteralAtom_Atom = Generalization(general=Atom, specific=workflow_EnumLiteralAtom)
gen_workflow_UnequalToOperator_Operator = Generalization(general=Operator, specific=workflow_UnequalToOperator)
gen_workflow_AgentContainer_RuntimeGlobalAspect = Generalization(general=RuntimeGlobalAspect, specific=workflow_AgentContainer)
gen_workflow_Organisation_GlobalAspect = Generalization(general=GlobalAspect, specific=workflow_Organisation)
gen_workflow_DefaultDocumentCondition_DocumentCondition = Generalization(general=DocumentCondition, specific=workflow_DefaultDocumentCondition)
gen_workflow_DocumentTypeContainer_GlobalAspect = Generalization(general=GlobalAspect, specific=workflow_DocumentTypeContainer)
gen_workflow_DocumentContainer_RuntimeGlobalAspect = Generalization(general=RuntimeGlobalAspect, specific=workflow_DocumentContainer)

# Domain Model
domain_model = DomainModel(
    name="workflow",
    types={workflow_ActivityO, ActivityAspect, workflow_Agent, workflow_Case, workflow_CaseAspect, workflow_Activity, workflow_Process, workflow_RuntimeCoreModel, workflow_ActivityAspect, workflow_Task, workflow_TaskO, TaskAspect, workflow_Role, workflow_TaskC, workflow_ActivityC, workflow_CaseC, workflow_Control, ProcessAspect, CaseAspect, workflow_State, workflow_PetriNet, Control, workflow_Arc, workflow_Place, workflow_Transition, TaskC, workflow_RuntimeInformation, workflow_Token, workflow_ModelRegistry, workflow_WorkflowEngine, workflow_CoreModel, workflow_GlobalAspect, workflow_Information, workflow_ProcessDocument, workflow_TaskI, workflow_DocumentDescriptor, workflow_DocumentCondition, workflow_DocumentType, workflow_Marking, State, workflow_CaseI, workflow_String2DocumentMap, workflow_ModelAspect, workflow_ProcessAspect, workflow_TaskAspect, workflow_RuntimeModelAspect, workflow_ActivityI, workflow_Document, workflow_OrganisationAspect, ModelAspect, workflow_ControlAspect, workflow_RuntimeGlobalAspect, workflow_ProcessO, workflow_Expression, workflow_DefaultDocumentType, DocumentType, workflow_Field, workflow_EnumField, workflow_InformationAspect, workflow_CaseO, workflow_InformationRuntimeAspect, RuntimeModelAspect, workflow_DefaultDocumentDescriptor, DocumentDescriptor, workflow_Atom, Expression, workflow_Operator, workflow_DocumentDescrAtom, Atom, workflow_FieldAtom, workflow_ConstantAtom, workflow_DotOperator, Operator, workflow_EqualToOperator, workflow_DefaultDocument, Document, workflow_FieldValue, workflow_EnumFieldValue, workflow_LessThanOperator, workflow_GreaterThanOperator, workflow_EnumFieldAtom, workflow_EnumLiteralAtom, workflow_UnequalToOperator, workflow_AgentContainer, RuntimeGlobalAspect, workflow_Organisation, GlobalAspect, workflow_DocumentTypeContainer, workflow_DefaultDocumentCondition, DocumentCondition, workflow_EnumLiteral, workflow_DocumentContainer},
    associations={requiredRoles0, followsUpOn2, assignedTo4, aspects5, activities6, process7, runtimeCoreModel9, aspects10, task12, EReference014, takenRoles16, case22, state23, arcs25, places26, start28, finish31, out34, in35, sourcePlace37, targetPlace38, sourceTransition40, active18, mayTakeRoles19, tokens49, petrinet50, place53, engine56, coreModels57, globalAspects59, processDocuments61, in62, out63, start66, finish68, documentType71, processDocument73, targetTransition42, in45, out47, caseDocuments83, process84, tasks85, core87, core88, process90, core92, task94, core97, aspects99, process101, modelRegistry103, in76, out77, DocumentType80, aspects111, aspects113, cases114, coreModel116, modelRegistry119, runtimeCoreModels121, runtimeGlobalAspects123, involved125, fields127, enumFields128, tasks104, coreModel107, aspects109, involved136, documentType138, value141, operands144, descriptor145, field147, fieldValues130, enumFieldValues131, field133, enumField156, enumValue159, enumField162, enumLiteral164, agents166, roles168, modelRegistry170, engine172, expression149, enumLiterals151, defaultValue153, documentTypes174, documents176},
    generalizations={gen_workflow_ActivityO_ActivityAspect, gen_workflow_TaskO_TaskAspect, gen_workflow_TaskC_TaskAspect, gen_workflow_ActivityC_ActivityAspect, gen_workflow_Control_ProcessAspect, gen_workflow_CaseC_CaseAspect, gen_workflow_PetriNet_Control, gen_workflow_Transition_TaskC, gen_workflow_Information_ProcessAspect, gen_workflow_TaskI_TaskAspect, gen_workflow_Marking_State, gen_workflow_CaseI_CaseAspect, gen_workflow_ActivityI_ActivityAspect, gen_workflow_OrganisationAspect_ModelAspect, gen_workflow_ControlAspect_ModelAspect, gen_workflow_ProcessO_ProcessAspect, gen_workflow_DefaultDocumentType_DocumentType, gen_workflow_InformationAspect_ModelAspect, gen_workflow_CaseO_CaseAspect, gen_workflow_InformationRuntimeAspect_RuntimeModelAspect, gen_workflow_DefaultDocumentDescriptor_DocumentDescriptor, gen_workflow_Atom_Expression, gen_workflow_Operator_Expression, gen_workflow_DocumentDescrAtom_Atom, gen_workflow_FieldAtom_Atom, gen_workflow_ConstantAtom_Atom, gen_workflow_DotOperator_Operator, gen_workflow_EqualToOperator_Operator, gen_workflow_DefaultDocument_Document, gen_workflow_LessThanOperator_Operator, gen_workflow_GreaterThanOperator_Operator, gen_workflow_EnumFieldAtom_Atom, gen_workflow_EnumLiteralAtom_Atom, gen_workflow_UnequalToOperator_Operator, gen_workflow_AgentContainer_RuntimeGlobalAspect, gen_workflow_Organisation_GlobalAspect, gen_workflow_DefaultDocumentCondition_DocumentCondition, gen_workflow_DocumentTypeContainer_GlobalAspect, gen_workflow_DocumentContainer_RuntimeGlobalAspect},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
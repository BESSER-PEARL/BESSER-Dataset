from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class UserTask:

    pass
class Transaction:

    pass
class artifacts_TextAnnotation:

    pass
class events_TimerEventDefinition:

    pass
class events_ThrowEvent:

    pass
class events_TerminateEventDefinition:

    pass
class Task:

    pass
class SubProcess:

    pass
class SubConversation:

    pass
class choreographyactivities_SubChoreography:

    pass
class events_StartEvent:

    pass
class ServiceTask:

    pass
class StandardLoopCharacteristics:

    pass
class events_SignalEventDefinition:

    pass
class events_Signal:

    pass
class flows_SequenceFlow:

    pass
class SendTask:

    pass
class ScriptTask:

    pass
class bpmn2_EObject:

    pass
class ResourceParameterBinding:

    pass
class ResourceParameter:

    pass
class ResourceAssignmentExpression:

    pass
class Resource:

    pass
class Rendering:

    pass
class Relationship:

    pass
class ReceiveTask:

    pass
class Property:

    pass
class Process:

    pass
class PotentialOwner:

    pass
class PartnerRole:

    pass
class PartnerEntity:

    pass
class ParticipantMultiplicity:

    pass
class ParticipantAssociation:

    pass
class Participant:

    pass
class gateways_ParallelGateway:

    pass
class OutputSet:

    pass
class Operation:

    pass
class MultiInstanceLoopCharacteristics:

    pass
class Monitoring:

    pass
class MessageFlowAssociation:

    pass
class MessageFlow:

    pass
class MessageEventDefinition:

    pass
class Message:

    pass
class ManualTask:

    pass
class LoopCharacteristics:

    pass
class events_LinkEventDefinition:

    pass
class LaneSet:

    pass
class Lane:

    pass
class ItemDefinition:

    pass
class InputOutputSpecification:

    pass
class InputOutputBinding:

    pass
class events_IntermediateThrowEvent:

    pass
class events_IntermediateCatchEvent:

    pass
class Interface:

    pass
class InputSet:

    pass
class gateways_InclusiveGateway:

    pass
class Import:

    pass
class events_ImplicitThrowEvent:

    pass
class ResourceRole:

    pass
class Performer:

    pass
class HumanPerformer:

    pass
class artifacts_Group:

    pass
class GlobalUserTask:

    pass
class GlobalTask:

    pass
class GlobalScriptTask:

    pass
class GlobalManualTask:

    pass
class GlobalConversation:

    pass
class GlobalChoreographyTask:

    pass
class GlobalBusinessRuleTask:

    pass
class gateways_Gateway:

    pass
class FormalExpression:

    pass
class flows_FlowNode:

    pass
class extension_ExtensionAttributeValue:

    pass
class extension_Extension:

    pass
class Expression:

    pass
class gateways_ExclusiveGateway:

    pass
class gateways_EventBasedGateway:

    pass
class events_Event:

    pass
class events_EscalationEventDefinition:

    pass
class Escalation:

    pass
class events_ErrorEventDefinition:

    pass
class Error:

    pass
class EndPoint:

    pass
class events_EndEvent:

    pass
class Documentation:

    pass
class Definitions:

    pass
class DataStoreReference:

    pass
class DataStore:

    pass
class DataObject:

    pass
class DataState:

    pass
class DataOutputAssociation:

    pass
class DataOutput:

    pass
class DataObjectReference:

    pass
class correlations_CorrelationSubscription:

    pass
class DataInputAssociation:

    pass
class DataInput:

    pass
class DataAssociation:

    pass
class correlations_CorrelationKey:

    pass
class correlations_CorrelationPropertyRetrievalExpression:

    pass
class correlations_CorrelationPropertyBinding:

    pass
class correlations_CorrelationProperty:

    pass
class gateways_ComplexGateway:

    pass
class ConversationLink:

    pass
class ConversationAssociation:

    pass
class Conversation:

    pass
class events_ConditionalEventDefinition:

    pass
class ComplexBehaviorDefinition:

    pass
class events_CompensateEventDefinition:

    pass
class choreographyactivities_ChoreographyTask:

    pass
class choreographyactivities_ChoreographyActivity:

    pass
class Collaboration:

    pass
class Choreography:

    pass
class artifacts_CategoryValue:

    pass
class artifacts_Category:

    pass
class events_CatchEvent:

    pass
class RootElement:

    pass
class events_EventDefinition:

    pass
class events_CancelEventDefinition:

    pass
class ConversationNode:

    pass
class CallConversation:

    pass
class choreographyactivities_CallChoreography:

    pass
class CallActivity:

    pass
class CallableElement:

    pass
class BusinessRuleTask:

    pass
class events_BoundaryEvent:

    pass
class BaseElement:

    pass
class Auditing:

    pass
class artifacts_Association:

    pass
class Assignment:

    pass
class artifacts_Artifact:

    pass
class flows_FlowElement:

    pass
class AdHocSubProcess:

    pass
class Activity:

    pass
class bpmn2_EStringToStringMapEntry:

    pass
class bpmn2_DocumentRoot:

    def __init__(self, mixed: str, bpmn2_DocumentRoot: set["bpmn2_EStringToStringMapEntry"] = None, bpmn2_DocumentRoot2: set["bpmn2_EStringToStringMapEntry"] = None, bpmn2_DocumentRoot5: set["Activity"] = None, bpmn2_DocumentRoot7: set["AdHocSubProcess"] = None, bpmn2_DocumentRoot9: set["flows_FlowElement"] = None, bpmn2_DocumentRoot11: set["artifacts_Artifact"] = None, bpmn2_DocumentRoot13: set["Assignment"] = None, bpmn2_DocumentRoot15: set["artifacts_Association"] = None, bpmn2_DocumentRoot17: set["Auditing"] = None, bpmn2_DocumentRoot19: set["BaseElement"] = None, bpmn2_DocumentRoot21: set["BaseElement"] = None, bpmn2_DocumentRoot24: set["events_BoundaryEvent"] = None, bpmn2_DocumentRoot26: set["BusinessRuleTask"] = None, bpmn2_DocumentRoot28: set["CallableElement"] = None, bpmn2_DocumentRoot30: set["CallActivity"] = None, bpmn2_DocumentRoot32: set["choreographyactivities_CallChoreography"] = None, bpmn2_DocumentRoot34: set["CallConversation"] = None, bpmn2_DocumentRoot36: set["ConversationNode"] = None, bpmn2_DocumentRoot38: set["events_CancelEventDefinition"] = None, bpmn2_DocumentRoot40: set["events_EventDefinition"] = None, bpmn2_DocumentRoot42: set["RootElement"] = None, bpmn2_DocumentRoot46: set["artifacts_Category"] = None, bpmn2_DocumentRoot48: set["artifacts_CategoryValue"] = None, bpmn2_DocumentRoot50: set["Choreography"] = None, bpmn2_DocumentRoot44: set["events_CatchEvent"] = None, bpmn2_DocumentRoot54: set["choreographyactivities_ChoreographyActivity"] = None, bpmn2_DocumentRoot56: set["choreographyactivities_ChoreographyTask"] = None, bpmn2_DocumentRoot58: set["events_CompensateEventDefinition"] = None, bpmn2_DocumentRoot60: set["ComplexBehaviorDefinition"] = None, bpmn2_DocumentRoot52: set["Collaboration"] = None, bpmn2_DocumentRoot64: set["events_ConditionalEventDefinition"] = None, bpmn2_DocumentRoot66: set["Conversation"] = None, bpmn2_DocumentRoot68: set["ConversationAssociation"] = None, bpmn2_DocumentRoot70: set["ConversationLink"] = None, bpmn2_DocumentRoot62: set["gateways_ComplexGateway"] = None, bpmn2_DocumentRoot74: set["correlations_CorrelationProperty"] = None, bpmn2_DocumentRoot76: set["correlations_CorrelationPropertyBinding"] = None, bpmn2_DocumentRoot78: set["correlations_CorrelationPropertyRetrievalExpression"] = None, bpmn2_DocumentRoot72: set["correlations_CorrelationKey"] = None, bpmn2_DocumentRoot82: set["DataAssociation"] = None, bpmn2_DocumentRoot84: set["DataInput"] = None, bpmn2_DocumentRoot86: set["DataInputAssociation"] = None, bpmn2_DocumentRoot80: set["correlations_CorrelationSubscription"] = None, bpmn2_DocumentRoot90: set["DataObjectReference"] = None, bpmn2_DocumentRoot92: set["DataOutput"] = None, bpmn2_DocumentRoot94: set["DataOutputAssociation"] = None, bpmn2_DocumentRoot96: set["DataState"] = None, bpmn2_DocumentRoot98: set["DataStore"] = None, bpmn2_DocumentRoot88: set["DataObject"] = None, bpmn2_DocumentRoot100: set["DataStoreReference"] = None, bpmn2_DocumentRoot102: set["Definitions"] = None, bpmn2_DocumentRoot104: set["Documentation"] = None, bpmn2_DocumentRoot106: set["events_EndEvent"] = None, bpmn2_DocumentRoot108: set["EndPoint"] = None, bpmn2_DocumentRoot110: set["Error"] = None, bpmn2_DocumentRoot112: set["events_ErrorEventDefinition"] = None, bpmn2_DocumentRoot114: set["Escalation"] = None, bpmn2_DocumentRoot116: set["events_EscalationEventDefinition"] = None, bpmn2_DocumentRoot118: set["events_Event"] = None, bpmn2_DocumentRoot120: set["gateways_EventBasedGateway"] = None, bpmn2_DocumentRoot122: set["gateways_ExclusiveGateway"] = None, bpmn2_DocumentRoot124: set["Expression"] = None, bpmn2_DocumentRoot126: set["extension_Extension"] = None, bpmn2_DocumentRoot128: set["extension_ExtensionAttributeValue"] = None, bpmn2_DocumentRoot130: set["flows_FlowNode"] = None, bpmn2_DocumentRoot132: set["FormalExpression"] = None, bpmn2_DocumentRoot134: set["gateways_Gateway"] = None, bpmn2_DocumentRoot136: set["GlobalBusinessRuleTask"] = None, bpmn2_DocumentRoot138: set["GlobalChoreographyTask"] = None, bpmn2_DocumentRoot140: set["GlobalConversation"] = None, bpmn2_DocumentRoot142: set["GlobalManualTask"] = None, bpmn2_DocumentRoot144: set["GlobalScriptTask"] = None, bpmn2_DocumentRoot146: set["GlobalTask"] = None, bpmn2_DocumentRoot148: set["GlobalUserTask"] = None, bpmn2_DocumentRoot150: set["artifacts_Group"] = None, bpmn2_DocumentRoot152: set["HumanPerformer"] = None, bpmn2_DocumentRoot154: set["Performer"] = None, bpmn2_DocumentRoot156: set["ResourceRole"] = None, bpmn2_DocumentRoot158: set["events_ImplicitThrowEvent"] = None, bpmn2_DocumentRoot160: set["Import"] = None, bpmn2_DocumentRoot162: set["gateways_InclusiveGateway"] = None, bpmn2_DocumentRoot164: set["InputSet"] = None, bpmn2_DocumentRoot166: set["Interface"] = None, bpmn2_DocumentRoot168: set["events_IntermediateCatchEvent"] = None, bpmn2_DocumentRoot170: set["events_IntermediateThrowEvent"] = None, bpmn2_DocumentRoot172: set["InputOutputBinding"] = None, bpmn2_DocumentRoot174: set["InputOutputSpecification"] = None, bpmn2_DocumentRoot176: set["ItemDefinition"] = None, bpmn2_DocumentRoot178: set["Lane"] = None, bpmn2_DocumentRoot180: set["LaneSet"] = None, bpmn2_DocumentRoot182: set["events_LinkEventDefinition"] = None, bpmn2_DocumentRoot184: set["LoopCharacteristics"] = None, bpmn2_DocumentRoot186: set["ManualTask"] = None, bpmn2_DocumentRoot188: set["Message"] = None, bpmn2_DocumentRoot190: set["MessageEventDefinition"] = None, bpmn2_DocumentRoot192: set["MessageFlow"] = None, bpmn2_DocumentRoot194: set["MessageFlowAssociation"] = None, bpmn2_DocumentRoot196: set["Monitoring"] = None, bpmn2_DocumentRoot198: set["MultiInstanceLoopCharacteristics"] = None, bpmn2_DocumentRoot200: set["Operation"] = None, bpmn2_DocumentRoot202: set["OutputSet"] = None, bpmn2_DocumentRoot204: set["gateways_ParallelGateway"] = None, bpmn2_DocumentRoot206: set["Participant"] = None, bpmn2_DocumentRoot208: set["ParticipantAssociation"] = None, bpmn2_DocumentRoot210: set["ParticipantMultiplicity"] = None, bpmn2_DocumentRoot212: set["PartnerEntity"] = None, bpmn2_DocumentRoot214: set["PartnerRole"] = None, bpmn2_DocumentRoot216: set["PotentialOwner"] = None, bpmn2_DocumentRoot218: set["Process"] = None, bpmn2_DocumentRoot220: set["Property"] = None, bpmn2_DocumentRoot222: set["ReceiveTask"] = None, bpmn2_DocumentRoot224: set["Relationship"] = None, bpmn2_DocumentRoot226: set["Rendering"] = None, bpmn2_DocumentRoot228: set["Resource"] = None, bpmn2_DocumentRoot230: set["ResourceAssignmentExpression"] = None, bpmn2_DocumentRoot232: set["ResourceParameter"] = None, bpmn2_DocumentRoot234: set["ResourceParameterBinding"] = None, bpmn2_DocumentRoot236: set["bpmn2_EObject"] = None, bpmn2_DocumentRoot240: set["SendTask"] = None, bpmn2_DocumentRoot242: set["flows_SequenceFlow"] = None, bpmn2_DocumentRoot238: set["ScriptTask"] = None, bpmn2_DocumentRoot244: set["ServiceTask"] = None, bpmn2_DocumentRoot246: set["events_Signal"] = None, bpmn2_DocumentRoot248: set["events_SignalEventDefinition"] = None, bpmn2_DocumentRoot250: set["StandardLoopCharacteristics"] = None, bpmn2_DocumentRoot252: set["events_StartEvent"] = None, bpmn2_DocumentRoot254: set["choreographyactivities_SubChoreography"] = None, bpmn2_DocumentRoot256: set["SubConversation"] = None, bpmn2_DocumentRoot258: set["SubProcess"] = None, bpmn2_DocumentRoot260: set["Task"] = None, bpmn2_DocumentRoot262: set["events_TerminateEventDefinition"] = None, bpmn2_DocumentRoot264: set["bpmn2_EObject"] = None, bpmn2_DocumentRoot267: set["artifacts_TextAnnotation"] = None, bpmn2_DocumentRoot269: set["events_ThrowEvent"] = None, bpmn2_DocumentRoot271: set["events_TimerEventDefinition"] = None, bpmn2_DocumentRoot273: set["Transaction"] = None, bpmn2_DocumentRoot275: set["UserTask"] = None):
        self.mixed = mixed
        self.bpmn2_DocumentRoot = bpmn2_DocumentRoot if bpmn2_DocumentRoot is not None else set()
        self.bpmn2_DocumentRoot2 = bpmn2_DocumentRoot2 if bpmn2_DocumentRoot2 is not None else set()
        self.bpmn2_DocumentRoot5 = bpmn2_DocumentRoot5 if bpmn2_DocumentRoot5 is not None else set()
        self.bpmn2_DocumentRoot7 = bpmn2_DocumentRoot7 if bpmn2_DocumentRoot7 is not None else set()
        self.bpmn2_DocumentRoot9 = bpmn2_DocumentRoot9 if bpmn2_DocumentRoot9 is not None else set()
        self.bpmn2_DocumentRoot11 = bpmn2_DocumentRoot11 if bpmn2_DocumentRoot11 is not None else set()
        self.bpmn2_DocumentRoot13 = bpmn2_DocumentRoot13 if bpmn2_DocumentRoot13 is not None else set()
        self.bpmn2_DocumentRoot15 = bpmn2_DocumentRoot15 if bpmn2_DocumentRoot15 is not None else set()
        self.bpmn2_DocumentRoot17 = bpmn2_DocumentRoot17 if bpmn2_DocumentRoot17 is not None else set()
        self.bpmn2_DocumentRoot19 = bpmn2_DocumentRoot19 if bpmn2_DocumentRoot19 is not None else set()
        self.bpmn2_DocumentRoot21 = bpmn2_DocumentRoot21 if bpmn2_DocumentRoot21 is not None else set()
        self.bpmn2_DocumentRoot24 = bpmn2_DocumentRoot24 if bpmn2_DocumentRoot24 is not None else set()
        self.bpmn2_DocumentRoot26 = bpmn2_DocumentRoot26 if bpmn2_DocumentRoot26 is not None else set()
        self.bpmn2_DocumentRoot28 = bpmn2_DocumentRoot28 if bpmn2_DocumentRoot28 is not None else set()
        self.bpmn2_DocumentRoot30 = bpmn2_DocumentRoot30 if bpmn2_DocumentRoot30 is not None else set()
        self.bpmn2_DocumentRoot32 = bpmn2_DocumentRoot32 if bpmn2_DocumentRoot32 is not None else set()
        self.bpmn2_DocumentRoot34 = bpmn2_DocumentRoot34 if bpmn2_DocumentRoot34 is not None else set()
        self.bpmn2_DocumentRoot36 = bpmn2_DocumentRoot36 if bpmn2_DocumentRoot36 is not None else set()
        self.bpmn2_DocumentRoot38 = bpmn2_DocumentRoot38 if bpmn2_DocumentRoot38 is not None else set()
        self.bpmn2_DocumentRoot40 = bpmn2_DocumentRoot40 if bpmn2_DocumentRoot40 is not None else set()
        self.bpmn2_DocumentRoot42 = bpmn2_DocumentRoot42 if bpmn2_DocumentRoot42 is not None else set()
        self.bpmn2_DocumentRoot46 = bpmn2_DocumentRoot46 if bpmn2_DocumentRoot46 is not None else set()
        self.bpmn2_DocumentRoot48 = bpmn2_DocumentRoot48 if bpmn2_DocumentRoot48 is not None else set()
        self.bpmn2_DocumentRoot50 = bpmn2_DocumentRoot50 if bpmn2_DocumentRoot50 is not None else set()
        self.bpmn2_DocumentRoot44 = bpmn2_DocumentRoot44 if bpmn2_DocumentRoot44 is not None else set()
        self.bpmn2_DocumentRoot54 = bpmn2_DocumentRoot54 if bpmn2_DocumentRoot54 is not None else set()
        self.bpmn2_DocumentRoot56 = bpmn2_DocumentRoot56 if bpmn2_DocumentRoot56 is not None else set()
        self.bpmn2_DocumentRoot58 = bpmn2_DocumentRoot58 if bpmn2_DocumentRoot58 is not None else set()
        self.bpmn2_DocumentRoot60 = bpmn2_DocumentRoot60 if bpmn2_DocumentRoot60 is not None else set()
        self.bpmn2_DocumentRoot52 = bpmn2_DocumentRoot52 if bpmn2_DocumentRoot52 is not None else set()
        self.bpmn2_DocumentRoot64 = bpmn2_DocumentRoot64 if bpmn2_DocumentRoot64 is not None else set()
        self.bpmn2_DocumentRoot66 = bpmn2_DocumentRoot66 if bpmn2_DocumentRoot66 is not None else set()
        self.bpmn2_DocumentRoot68 = bpmn2_DocumentRoot68 if bpmn2_DocumentRoot68 is not None else set()
        self.bpmn2_DocumentRoot70 = bpmn2_DocumentRoot70 if bpmn2_DocumentRoot70 is not None else set()
        self.bpmn2_DocumentRoot62 = bpmn2_DocumentRoot62 if bpmn2_DocumentRoot62 is not None else set()
        self.bpmn2_DocumentRoot74 = bpmn2_DocumentRoot74 if bpmn2_DocumentRoot74 is not None else set()
        self.bpmn2_DocumentRoot76 = bpmn2_DocumentRoot76 if bpmn2_DocumentRoot76 is not None else set()
        self.bpmn2_DocumentRoot78 = bpmn2_DocumentRoot78 if bpmn2_DocumentRoot78 is not None else set()
        self.bpmn2_DocumentRoot72 = bpmn2_DocumentRoot72 if bpmn2_DocumentRoot72 is not None else set()
        self.bpmn2_DocumentRoot82 = bpmn2_DocumentRoot82 if bpmn2_DocumentRoot82 is not None else set()
        self.bpmn2_DocumentRoot84 = bpmn2_DocumentRoot84 if bpmn2_DocumentRoot84 is not None else set()
        self.bpmn2_DocumentRoot86 = bpmn2_DocumentRoot86 if bpmn2_DocumentRoot86 is not None else set()
        self.bpmn2_DocumentRoot80 = bpmn2_DocumentRoot80 if bpmn2_DocumentRoot80 is not None else set()
        self.bpmn2_DocumentRoot90 = bpmn2_DocumentRoot90 if bpmn2_DocumentRoot90 is not None else set()
        self.bpmn2_DocumentRoot92 = bpmn2_DocumentRoot92 if bpmn2_DocumentRoot92 is not None else set()
        self.bpmn2_DocumentRoot94 = bpmn2_DocumentRoot94 if bpmn2_DocumentRoot94 is not None else set()
        self.bpmn2_DocumentRoot96 = bpmn2_DocumentRoot96 if bpmn2_DocumentRoot96 is not None else set()
        self.bpmn2_DocumentRoot98 = bpmn2_DocumentRoot98 if bpmn2_DocumentRoot98 is not None else set()
        self.bpmn2_DocumentRoot88 = bpmn2_DocumentRoot88 if bpmn2_DocumentRoot88 is not None else set()
        self.bpmn2_DocumentRoot100 = bpmn2_DocumentRoot100 if bpmn2_DocumentRoot100 is not None else set()
        self.bpmn2_DocumentRoot102 = bpmn2_DocumentRoot102 if bpmn2_DocumentRoot102 is not None else set()
        self.bpmn2_DocumentRoot104 = bpmn2_DocumentRoot104 if bpmn2_DocumentRoot104 is not None else set()
        self.bpmn2_DocumentRoot106 = bpmn2_DocumentRoot106 if bpmn2_DocumentRoot106 is not None else set()
        self.bpmn2_DocumentRoot108 = bpmn2_DocumentRoot108 if bpmn2_DocumentRoot108 is not None else set()
        self.bpmn2_DocumentRoot110 = bpmn2_DocumentRoot110 if bpmn2_DocumentRoot110 is not None else set()
        self.bpmn2_DocumentRoot112 = bpmn2_DocumentRoot112 if bpmn2_DocumentRoot112 is not None else set()
        self.bpmn2_DocumentRoot114 = bpmn2_DocumentRoot114 if bpmn2_DocumentRoot114 is not None else set()
        self.bpmn2_DocumentRoot116 = bpmn2_DocumentRoot116 if bpmn2_DocumentRoot116 is not None else set()
        self.bpmn2_DocumentRoot118 = bpmn2_DocumentRoot118 if bpmn2_DocumentRoot118 is not None else set()
        self.bpmn2_DocumentRoot120 = bpmn2_DocumentRoot120 if bpmn2_DocumentRoot120 is not None else set()
        self.bpmn2_DocumentRoot122 = bpmn2_DocumentRoot122 if bpmn2_DocumentRoot122 is not None else set()
        self.bpmn2_DocumentRoot124 = bpmn2_DocumentRoot124 if bpmn2_DocumentRoot124 is not None else set()
        self.bpmn2_DocumentRoot126 = bpmn2_DocumentRoot126 if bpmn2_DocumentRoot126 is not None else set()
        self.bpmn2_DocumentRoot128 = bpmn2_DocumentRoot128 if bpmn2_DocumentRoot128 is not None else set()
        self.bpmn2_DocumentRoot130 = bpmn2_DocumentRoot130 if bpmn2_DocumentRoot130 is not None else set()
        self.bpmn2_DocumentRoot132 = bpmn2_DocumentRoot132 if bpmn2_DocumentRoot132 is not None else set()
        self.bpmn2_DocumentRoot134 = bpmn2_DocumentRoot134 if bpmn2_DocumentRoot134 is not None else set()
        self.bpmn2_DocumentRoot136 = bpmn2_DocumentRoot136 if bpmn2_DocumentRoot136 is not None else set()
        self.bpmn2_DocumentRoot138 = bpmn2_DocumentRoot138 if bpmn2_DocumentRoot138 is not None else set()
        self.bpmn2_DocumentRoot140 = bpmn2_DocumentRoot140 if bpmn2_DocumentRoot140 is not None else set()
        self.bpmn2_DocumentRoot142 = bpmn2_DocumentRoot142 if bpmn2_DocumentRoot142 is not None else set()
        self.bpmn2_DocumentRoot144 = bpmn2_DocumentRoot144 if bpmn2_DocumentRoot144 is not None else set()
        self.bpmn2_DocumentRoot146 = bpmn2_DocumentRoot146 if bpmn2_DocumentRoot146 is not None else set()
        self.bpmn2_DocumentRoot148 = bpmn2_DocumentRoot148 if bpmn2_DocumentRoot148 is not None else set()
        self.bpmn2_DocumentRoot150 = bpmn2_DocumentRoot150 if bpmn2_DocumentRoot150 is not None else set()
        self.bpmn2_DocumentRoot152 = bpmn2_DocumentRoot152 if bpmn2_DocumentRoot152 is not None else set()
        self.bpmn2_DocumentRoot154 = bpmn2_DocumentRoot154 if bpmn2_DocumentRoot154 is not None else set()
        self.bpmn2_DocumentRoot156 = bpmn2_DocumentRoot156 if bpmn2_DocumentRoot156 is not None else set()
        self.bpmn2_DocumentRoot158 = bpmn2_DocumentRoot158 if bpmn2_DocumentRoot158 is not None else set()
        self.bpmn2_DocumentRoot160 = bpmn2_DocumentRoot160 if bpmn2_DocumentRoot160 is not None else set()
        self.bpmn2_DocumentRoot162 = bpmn2_DocumentRoot162 if bpmn2_DocumentRoot162 is not None else set()
        self.bpmn2_DocumentRoot164 = bpmn2_DocumentRoot164 if bpmn2_DocumentRoot164 is not None else set()
        self.bpmn2_DocumentRoot166 = bpmn2_DocumentRoot166 if bpmn2_DocumentRoot166 is not None else set()
        self.bpmn2_DocumentRoot168 = bpmn2_DocumentRoot168 if bpmn2_DocumentRoot168 is not None else set()
        self.bpmn2_DocumentRoot170 = bpmn2_DocumentRoot170 if bpmn2_DocumentRoot170 is not None else set()
        self.bpmn2_DocumentRoot172 = bpmn2_DocumentRoot172 if bpmn2_DocumentRoot172 is not None else set()
        self.bpmn2_DocumentRoot174 = bpmn2_DocumentRoot174 if bpmn2_DocumentRoot174 is not None else set()
        self.bpmn2_DocumentRoot176 = bpmn2_DocumentRoot176 if bpmn2_DocumentRoot176 is not None else set()
        self.bpmn2_DocumentRoot178 = bpmn2_DocumentRoot178 if bpmn2_DocumentRoot178 is not None else set()
        self.bpmn2_DocumentRoot180 = bpmn2_DocumentRoot180 if bpmn2_DocumentRoot180 is not None else set()
        self.bpmn2_DocumentRoot182 = bpmn2_DocumentRoot182 if bpmn2_DocumentRoot182 is not None else set()
        self.bpmn2_DocumentRoot184 = bpmn2_DocumentRoot184 if bpmn2_DocumentRoot184 is not None else set()
        self.bpmn2_DocumentRoot186 = bpmn2_DocumentRoot186 if bpmn2_DocumentRoot186 is not None else set()
        self.bpmn2_DocumentRoot188 = bpmn2_DocumentRoot188 if bpmn2_DocumentRoot188 is not None else set()
        self.bpmn2_DocumentRoot190 = bpmn2_DocumentRoot190 if bpmn2_DocumentRoot190 is not None else set()
        self.bpmn2_DocumentRoot192 = bpmn2_DocumentRoot192 if bpmn2_DocumentRoot192 is not None else set()
        self.bpmn2_DocumentRoot194 = bpmn2_DocumentRoot194 if bpmn2_DocumentRoot194 is not None else set()
        self.bpmn2_DocumentRoot196 = bpmn2_DocumentRoot196 if bpmn2_DocumentRoot196 is not None else set()
        self.bpmn2_DocumentRoot198 = bpmn2_DocumentRoot198 if bpmn2_DocumentRoot198 is not None else set()
        self.bpmn2_DocumentRoot200 = bpmn2_DocumentRoot200 if bpmn2_DocumentRoot200 is not None else set()
        self.bpmn2_DocumentRoot202 = bpmn2_DocumentRoot202 if bpmn2_DocumentRoot202 is not None else set()
        self.bpmn2_DocumentRoot204 = bpmn2_DocumentRoot204 if bpmn2_DocumentRoot204 is not None else set()
        self.bpmn2_DocumentRoot206 = bpmn2_DocumentRoot206 if bpmn2_DocumentRoot206 is not None else set()
        self.bpmn2_DocumentRoot208 = bpmn2_DocumentRoot208 if bpmn2_DocumentRoot208 is not None else set()
        self.bpmn2_DocumentRoot210 = bpmn2_DocumentRoot210 if bpmn2_DocumentRoot210 is not None else set()
        self.bpmn2_DocumentRoot212 = bpmn2_DocumentRoot212 if bpmn2_DocumentRoot212 is not None else set()
        self.bpmn2_DocumentRoot214 = bpmn2_DocumentRoot214 if bpmn2_DocumentRoot214 is not None else set()
        self.bpmn2_DocumentRoot216 = bpmn2_DocumentRoot216 if bpmn2_DocumentRoot216 is not None else set()
        self.bpmn2_DocumentRoot218 = bpmn2_DocumentRoot218 if bpmn2_DocumentRoot218 is not None else set()
        self.bpmn2_DocumentRoot220 = bpmn2_DocumentRoot220 if bpmn2_DocumentRoot220 is not None else set()
        self.bpmn2_DocumentRoot222 = bpmn2_DocumentRoot222 if bpmn2_DocumentRoot222 is not None else set()
        self.bpmn2_DocumentRoot224 = bpmn2_DocumentRoot224 if bpmn2_DocumentRoot224 is not None else set()
        self.bpmn2_DocumentRoot226 = bpmn2_DocumentRoot226 if bpmn2_DocumentRoot226 is not None else set()
        self.bpmn2_DocumentRoot228 = bpmn2_DocumentRoot228 if bpmn2_DocumentRoot228 is not None else set()
        self.bpmn2_DocumentRoot230 = bpmn2_DocumentRoot230 if bpmn2_DocumentRoot230 is not None else set()
        self.bpmn2_DocumentRoot232 = bpmn2_DocumentRoot232 if bpmn2_DocumentRoot232 is not None else set()
        self.bpmn2_DocumentRoot234 = bpmn2_DocumentRoot234 if bpmn2_DocumentRoot234 is not None else set()
        self.bpmn2_DocumentRoot236 = bpmn2_DocumentRoot236 if bpmn2_DocumentRoot236 is not None else set()
        self.bpmn2_DocumentRoot240 = bpmn2_DocumentRoot240 if bpmn2_DocumentRoot240 is not None else set()
        self.bpmn2_DocumentRoot242 = bpmn2_DocumentRoot242 if bpmn2_DocumentRoot242 is not None else set()
        self.bpmn2_DocumentRoot238 = bpmn2_DocumentRoot238 if bpmn2_DocumentRoot238 is not None else set()
        self.bpmn2_DocumentRoot244 = bpmn2_DocumentRoot244 if bpmn2_DocumentRoot244 is not None else set()
        self.bpmn2_DocumentRoot246 = bpmn2_DocumentRoot246 if bpmn2_DocumentRoot246 is not None else set()
        self.bpmn2_DocumentRoot248 = bpmn2_DocumentRoot248 if bpmn2_DocumentRoot248 is not None else set()
        self.bpmn2_DocumentRoot250 = bpmn2_DocumentRoot250 if bpmn2_DocumentRoot250 is not None else set()
        self.bpmn2_DocumentRoot252 = bpmn2_DocumentRoot252 if bpmn2_DocumentRoot252 is not None else set()
        self.bpmn2_DocumentRoot254 = bpmn2_DocumentRoot254 if bpmn2_DocumentRoot254 is not None else set()
        self.bpmn2_DocumentRoot256 = bpmn2_DocumentRoot256 if bpmn2_DocumentRoot256 is not None else set()
        self.bpmn2_DocumentRoot258 = bpmn2_DocumentRoot258 if bpmn2_DocumentRoot258 is not None else set()
        self.bpmn2_DocumentRoot260 = bpmn2_DocumentRoot260 if bpmn2_DocumentRoot260 is not None else set()
        self.bpmn2_DocumentRoot262 = bpmn2_DocumentRoot262 if bpmn2_DocumentRoot262 is not None else set()
        self.bpmn2_DocumentRoot264 = bpmn2_DocumentRoot264 if bpmn2_DocumentRoot264 is not None else set()
        self.bpmn2_DocumentRoot267 = bpmn2_DocumentRoot267 if bpmn2_DocumentRoot267 is not None else set()
        self.bpmn2_DocumentRoot269 = bpmn2_DocumentRoot269 if bpmn2_DocumentRoot269 is not None else set()
        self.bpmn2_DocumentRoot271 = bpmn2_DocumentRoot271 if bpmn2_DocumentRoot271 is not None else set()
        self.bpmn2_DocumentRoot273 = bpmn2_DocumentRoot273 if bpmn2_DocumentRoot273 is not None else set()
        self.bpmn2_DocumentRoot275 = bpmn2_DocumentRoot275 if bpmn2_DocumentRoot275 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def bpmn2_DocumentRoot98(self):
        return self.__bpmn2_DocumentRoot98

    @bpmn2_DocumentRoot98.setter
    def bpmn2_DocumentRoot98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot98", None)
        self.__bpmn2_DocumentRoot98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataStore"):
                    opp_val = getattr(item, "DataStore", None)
                    
                    if opp_val == self:
                        setattr(item, "DataStore", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataStore"):
                    opp_val = getattr(item, "DataStore", None)
                    
                    setattr(item, "DataStore", self)
                    

    @property
    def bpmn2_DocumentRoot202(self):
        return self.__bpmn2_DocumentRoot202

    @bpmn2_DocumentRoot202.setter
    def bpmn2_DocumentRoot202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot202", None)
        self.__bpmn2_DocumentRoot202 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutputSet"):
                    opp_val = getattr(item, "OutputSet", None)
                    
                    if opp_val == self:
                        setattr(item, "OutputSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutputSet"):
                    opp_val = getattr(item, "OutputSet", None)
                    
                    setattr(item, "OutputSet", self)
                    

    @property
    def bpmn2_DocumentRoot254(self):
        return self.__bpmn2_DocumentRoot254

    @bpmn2_DocumentRoot254.setter
    def bpmn2_DocumentRoot254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot254", None)
        self.__bpmn2_DocumentRoot254 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "choreographyactivities_SubChoreography"):
                    opp_val = getattr(item, "choreographyactivities_SubChoreography", None)
                    
                    if opp_val == self:
                        setattr(item, "choreographyactivities_SubChoreography", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "choreographyactivities_SubChoreography"):
                    opp_val = getattr(item, "choreographyactivities_SubChoreography", None)
                    
                    setattr(item, "choreographyactivities_SubChoreography", self)
                    

    @property
    def bpmn2_DocumentRoot234(self):
        return self.__bpmn2_DocumentRoot234

    @bpmn2_DocumentRoot234.setter
    def bpmn2_DocumentRoot234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot234", None)
        self.__bpmn2_DocumentRoot234 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResourceParameterBinding"):
                    opp_val = getattr(item, "ResourceParameterBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "ResourceParameterBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResourceParameterBinding"):
                    opp_val = getattr(item, "ResourceParameterBinding", None)
                    
                    setattr(item, "ResourceParameterBinding", self)
                    

    @property
    def bpmn2_DocumentRoot196(self):
        return self.__bpmn2_DocumentRoot196

    @bpmn2_DocumentRoot196.setter
    def bpmn2_DocumentRoot196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot196", None)
        self.__bpmn2_DocumentRoot196 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Monitoring"):
                    opp_val = getattr(item, "Monitoring", None)
                    
                    if opp_val == self:
                        setattr(item, "Monitoring", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Monitoring"):
                    opp_val = getattr(item, "Monitoring", None)
                    
                    setattr(item, "Monitoring", self)
                    

    @property
    def bpmn2_DocumentRoot275(self):
        return self.__bpmn2_DocumentRoot275

    @bpmn2_DocumentRoot275.setter
    def bpmn2_DocumentRoot275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot275", None)
        self.__bpmn2_DocumentRoot275 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UserTask"):
                    opp_val = getattr(item, "UserTask", None)
                    
                    if opp_val == self:
                        setattr(item, "UserTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UserTask"):
                    opp_val = getattr(item, "UserTask", None)
                    
                    setattr(item, "UserTask", self)
                    

    @property
    def bpmn2_DocumentRoot267(self):
        return self.__bpmn2_DocumentRoot267

    @bpmn2_DocumentRoot267.setter
    def bpmn2_DocumentRoot267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot267", None)
        self.__bpmn2_DocumentRoot267 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "artifacts_TextAnnotation"):
                    opp_val = getattr(item, "artifacts_TextAnnotation", None)
                    
                    if opp_val == self:
                        setattr(item, "artifacts_TextAnnotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "artifacts_TextAnnotation"):
                    opp_val = getattr(item, "artifacts_TextAnnotation", None)
                    
                    setattr(item, "artifacts_TextAnnotation", self)
                    

    @property
    def bpmn2_DocumentRoot(self):
        return self.__bpmn2_DocumentRoot

    @bpmn2_DocumentRoot.setter
    def bpmn2_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot", None)
        self.__bpmn2_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_EStringToStringMapEntry"):
                    opp_val = getattr(item, "bpmn2_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_EStringToStringMapEntry"):
                    opp_val = getattr(item, "bpmn2_EStringToStringMapEntry", None)
                    
                    setattr(item, "bpmn2_EStringToStringMapEntry", self)
                    

    @property
    def bpmn2_DocumentRoot168(self):
        return self.__bpmn2_DocumentRoot168

    @bpmn2_DocumentRoot168.setter
    def bpmn2_DocumentRoot168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot168", None)
        self.__bpmn2_DocumentRoot168 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_IntermediateCatchEvent"):
                    opp_val = getattr(item, "events_IntermediateCatchEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "events_IntermediateCatchEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_IntermediateCatchEvent"):
                    opp_val = getattr(item, "events_IntermediateCatchEvent", None)
                    
                    setattr(item, "events_IntermediateCatchEvent", self)
                    

    @property
    def bpmn2_DocumentRoot176(self):
        return self.__bpmn2_DocumentRoot176

    @bpmn2_DocumentRoot176.setter
    def bpmn2_DocumentRoot176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot176", None)
        self.__bpmn2_DocumentRoot176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ItemDefinition"):
                    opp_val = getattr(item, "ItemDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "ItemDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ItemDefinition"):
                    opp_val = getattr(item, "ItemDefinition", None)
                    
                    setattr(item, "ItemDefinition", self)
                    

    @property
    def bpmn2_DocumentRoot170(self):
        return self.__bpmn2_DocumentRoot170

    @bpmn2_DocumentRoot170.setter
    def bpmn2_DocumentRoot170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot170", None)
        self.__bpmn2_DocumentRoot170 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_IntermediateThrowEvent"):
                    opp_val = getattr(item, "events_IntermediateThrowEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "events_IntermediateThrowEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_IntermediateThrowEvent"):
                    opp_val = getattr(item, "events_IntermediateThrowEvent", None)
                    
                    setattr(item, "events_IntermediateThrowEvent", self)
                    

    @property
    def bpmn2_DocumentRoot222(self):
        return self.__bpmn2_DocumentRoot222

    @bpmn2_DocumentRoot222.setter
    def bpmn2_DocumentRoot222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot222", None)
        self.__bpmn2_DocumentRoot222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ReceiveTask"):
                    opp_val = getattr(item, "ReceiveTask", None)
                    
                    if opp_val == self:
                        setattr(item, "ReceiveTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ReceiveTask"):
                    opp_val = getattr(item, "ReceiveTask", None)
                    
                    setattr(item, "ReceiveTask", self)
                    

    @property
    def bpmn2_DocumentRoot54(self):
        return self.__bpmn2_DocumentRoot54

    @bpmn2_DocumentRoot54.setter
    def bpmn2_DocumentRoot54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot54", None)
        self.__bpmn2_DocumentRoot54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "choreographyactivities_ChoreographyActivity"):
                    opp_val = getattr(item, "choreographyactivities_ChoreographyActivity", None)
                    
                    if opp_val == self:
                        setattr(item, "choreographyactivities_ChoreographyActivity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "choreographyactivities_ChoreographyActivity"):
                    opp_val = getattr(item, "choreographyactivities_ChoreographyActivity", None)
                    
                    setattr(item, "choreographyactivities_ChoreographyActivity", self)
                    

    @property
    def bpmn2_DocumentRoot92(self):
        return self.__bpmn2_DocumentRoot92

    @bpmn2_DocumentRoot92.setter
    def bpmn2_DocumentRoot92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot92", None)
        self.__bpmn2_DocumentRoot92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataOutput"):
                    opp_val = getattr(item, "DataOutput", None)
                    
                    if opp_val == self:
                        setattr(item, "DataOutput", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataOutput"):
                    opp_val = getattr(item, "DataOutput", None)
                    
                    setattr(item, "DataOutput", self)
                    

    @property
    def bpmn2_DocumentRoot240(self):
        return self.__bpmn2_DocumentRoot240

    @bpmn2_DocumentRoot240.setter
    def bpmn2_DocumentRoot240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot240", None)
        self.__bpmn2_DocumentRoot240 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SendTask"):
                    opp_val = getattr(item, "SendTask", None)
                    
                    if opp_val == self:
                        setattr(item, "SendTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SendTask"):
                    opp_val = getattr(item, "SendTask", None)
                    
                    setattr(item, "SendTask", self)
                    

    @property
    def bpmn2_DocumentRoot244(self):
        return self.__bpmn2_DocumentRoot244

    @bpmn2_DocumentRoot244.setter
    def bpmn2_DocumentRoot244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot244", None)
        self.__bpmn2_DocumentRoot244 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ServiceTask"):
                    opp_val = getattr(item, "ServiceTask", None)
                    
                    if opp_val == self:
                        setattr(item, "ServiceTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ServiceTask"):
                    opp_val = getattr(item, "ServiceTask", None)
                    
                    setattr(item, "ServiceTask", self)
                    

    @property
    def bpmn2_DocumentRoot88(self):
        return self.__bpmn2_DocumentRoot88

    @bpmn2_DocumentRoot88.setter
    def bpmn2_DocumentRoot88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot88", None)
        self.__bpmn2_DocumentRoot88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataObject"):
                    opp_val = getattr(item, "DataObject", None)
                    
                    if opp_val == self:
                        setattr(item, "DataObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataObject"):
                    opp_val = getattr(item, "DataObject", None)
                    
                    setattr(item, "DataObject", self)
                    

    @property
    def bpmn2_DocumentRoot112(self):
        return self.__bpmn2_DocumentRoot112

    @bpmn2_DocumentRoot112.setter
    def bpmn2_DocumentRoot112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot112", None)
        self.__bpmn2_DocumentRoot112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_ErrorEventDefinition"):
                    opp_val = getattr(item, "events_ErrorEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "events_ErrorEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_ErrorEventDefinition"):
                    opp_val = getattr(item, "events_ErrorEventDefinition", None)
                    
                    setattr(item, "events_ErrorEventDefinition", self)
                    

    @property
    def bpmn2_DocumentRoot262(self):
        return self.__bpmn2_DocumentRoot262

    @bpmn2_DocumentRoot262.setter
    def bpmn2_DocumentRoot262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot262", None)
        self.__bpmn2_DocumentRoot262 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_TerminateEventDefinition"):
                    opp_val = getattr(item, "events_TerminateEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "events_TerminateEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_TerminateEventDefinition"):
                    opp_val = getattr(item, "events_TerminateEventDefinition", None)
                    
                    setattr(item, "events_TerminateEventDefinition", self)
                    

    @property
    def bpmn2_DocumentRoot186(self):
        return self.__bpmn2_DocumentRoot186

    @bpmn2_DocumentRoot186.setter
    def bpmn2_DocumentRoot186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot186", None)
        self.__bpmn2_DocumentRoot186 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ManualTask"):
                    opp_val = getattr(item, "ManualTask", None)
                    
                    if opp_val == self:
                        setattr(item, "ManualTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ManualTask"):
                    opp_val = getattr(item, "ManualTask", None)
                    
                    setattr(item, "ManualTask", self)
                    

    @property
    def bpmn2_DocumentRoot216(self):
        return self.__bpmn2_DocumentRoot216

    @bpmn2_DocumentRoot216.setter
    def bpmn2_DocumentRoot216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot216", None)
        self.__bpmn2_DocumentRoot216 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PotentialOwner"):
                    opp_val = getattr(item, "PotentialOwner", None)
                    
                    if opp_val == self:
                        setattr(item, "PotentialOwner", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PotentialOwner"):
                    opp_val = getattr(item, "PotentialOwner", None)
                    
                    setattr(item, "PotentialOwner", self)
                    

    @property
    def bpmn2_DocumentRoot204(self):
        return self.__bpmn2_DocumentRoot204

    @bpmn2_DocumentRoot204.setter
    def bpmn2_DocumentRoot204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot204", None)
        self.__bpmn2_DocumentRoot204 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gateways_ParallelGateway"):
                    opp_val = getattr(item, "gateways_ParallelGateway", None)
                    
                    if opp_val == self:
                        setattr(item, "gateways_ParallelGateway", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gateways_ParallelGateway"):
                    opp_val = getattr(item, "gateways_ParallelGateway", None)
                    
                    setattr(item, "gateways_ParallelGateway", self)
                    

    @property
    def bpmn2_DocumentRoot158(self):
        return self.__bpmn2_DocumentRoot158

    @bpmn2_DocumentRoot158.setter
    def bpmn2_DocumentRoot158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot158", None)
        self.__bpmn2_DocumentRoot158 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_ImplicitThrowEvent"):
                    opp_val = getattr(item, "events_ImplicitThrowEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "events_ImplicitThrowEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_ImplicitThrowEvent"):
                    opp_val = getattr(item, "events_ImplicitThrowEvent", None)
                    
                    setattr(item, "events_ImplicitThrowEvent", self)
                    

    @property
    def bpmn2_DocumentRoot122(self):
        return self.__bpmn2_DocumentRoot122

    @bpmn2_DocumentRoot122.setter
    def bpmn2_DocumentRoot122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot122", None)
        self.__bpmn2_DocumentRoot122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gateways_ExclusiveGateway"):
                    opp_val = getattr(item, "gateways_ExclusiveGateway", None)
                    
                    if opp_val == self:
                        setattr(item, "gateways_ExclusiveGateway", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gateways_ExclusiveGateway"):
                    opp_val = getattr(item, "gateways_ExclusiveGateway", None)
                    
                    setattr(item, "gateways_ExclusiveGateway", self)
                    

    @property
    def bpmn2_DocumentRoot86(self):
        return self.__bpmn2_DocumentRoot86

    @bpmn2_DocumentRoot86.setter
    def bpmn2_DocumentRoot86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot86", None)
        self.__bpmn2_DocumentRoot86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataInputAssociation"):
                    opp_val = getattr(item, "DataInputAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "DataInputAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataInputAssociation"):
                    opp_val = getattr(item, "DataInputAssociation", None)
                    
                    setattr(item, "DataInputAssociation", self)
                    

    @property
    def bpmn2_DocumentRoot230(self):
        return self.__bpmn2_DocumentRoot230

    @bpmn2_DocumentRoot230.setter
    def bpmn2_DocumentRoot230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot230", None)
        self.__bpmn2_DocumentRoot230 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResourceAssignmentExpression"):
                    opp_val = getattr(item, "ResourceAssignmentExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "ResourceAssignmentExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResourceAssignmentExpression"):
                    opp_val = getattr(item, "ResourceAssignmentExpression", None)
                    
                    setattr(item, "ResourceAssignmentExpression", self)
                    

    @property
    def bpmn2_DocumentRoot269(self):
        return self.__bpmn2_DocumentRoot269

    @bpmn2_DocumentRoot269.setter
    def bpmn2_DocumentRoot269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot269", None)
        self.__bpmn2_DocumentRoot269 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_ThrowEvent"):
                    opp_val = getattr(item, "events_ThrowEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "events_ThrowEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_ThrowEvent"):
                    opp_val = getattr(item, "events_ThrowEvent", None)
                    
                    setattr(item, "events_ThrowEvent", self)
                    

    @property
    def bpmn2_DocumentRoot15(self):
        return self.__bpmn2_DocumentRoot15

    @bpmn2_DocumentRoot15.setter
    def bpmn2_DocumentRoot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot15", None)
        self.__bpmn2_DocumentRoot15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "artifacts_Association"):
                    opp_val = getattr(item, "artifacts_Association", None)
                    
                    if opp_val == self:
                        setattr(item, "artifacts_Association", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "artifacts_Association"):
                    opp_val = getattr(item, "artifacts_Association", None)
                    
                    setattr(item, "artifacts_Association", self)
                    

    @property
    def bpmn2_DocumentRoot32(self):
        return self.__bpmn2_DocumentRoot32

    @bpmn2_DocumentRoot32.setter
    def bpmn2_DocumentRoot32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot32", None)
        self.__bpmn2_DocumentRoot32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "choreographyactivities_CallChoreography"):
                    opp_val = getattr(item, "choreographyactivities_CallChoreography", None)
                    
                    if opp_val == self:
                        setattr(item, "choreographyactivities_CallChoreography", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "choreographyactivities_CallChoreography"):
                    opp_val = getattr(item, "choreographyactivities_CallChoreography", None)
                    
                    setattr(item, "choreographyactivities_CallChoreography", self)
                    

    @property
    def bpmn2_DocumentRoot184(self):
        return self.__bpmn2_DocumentRoot184

    @bpmn2_DocumentRoot184.setter
    def bpmn2_DocumentRoot184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot184", None)
        self.__bpmn2_DocumentRoot184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LoopCharacteristics"):
                    opp_val = getattr(item, "LoopCharacteristics", None)
                    
                    if opp_val == self:
                        setattr(item, "LoopCharacteristics", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LoopCharacteristics"):
                    opp_val = getattr(item, "LoopCharacteristics", None)
                    
                    setattr(item, "LoopCharacteristics", self)
                    

    @property
    def bpmn2_DocumentRoot264(self):
        return self.__bpmn2_DocumentRoot264

    @bpmn2_DocumentRoot264.setter
    def bpmn2_DocumentRoot264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot264", None)
        self.__bpmn2_DocumentRoot264 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_EObject265"):
                    opp_val = getattr(item, "bpmn2_EObject265", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_EObject265", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_EObject265"):
                    opp_val = getattr(item, "bpmn2_EObject265", None)
                    
                    setattr(item, "bpmn2_EObject265", self)
                    

    @property
    def bpmn2_DocumentRoot271(self):
        return self.__bpmn2_DocumentRoot271

    @bpmn2_DocumentRoot271.setter
    def bpmn2_DocumentRoot271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot271", None)
        self.__bpmn2_DocumentRoot271 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_TimerEventDefinition"):
                    opp_val = getattr(item, "events_TimerEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "events_TimerEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_TimerEventDefinition"):
                    opp_val = getattr(item, "events_TimerEventDefinition", None)
                    
                    setattr(item, "events_TimerEventDefinition", self)
                    

    @property
    def bpmn2_DocumentRoot106(self):
        return self.__bpmn2_DocumentRoot106

    @bpmn2_DocumentRoot106.setter
    def bpmn2_DocumentRoot106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot106", None)
        self.__bpmn2_DocumentRoot106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_EndEvent"):
                    opp_val = getattr(item, "events_EndEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "events_EndEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_EndEvent"):
                    opp_val = getattr(item, "events_EndEvent", None)
                    
                    setattr(item, "events_EndEvent", self)
                    

    @property
    def bpmn2_DocumentRoot162(self):
        return self.__bpmn2_DocumentRoot162

    @bpmn2_DocumentRoot162.setter
    def bpmn2_DocumentRoot162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot162", None)
        self.__bpmn2_DocumentRoot162 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gateways_InclusiveGateway"):
                    opp_val = getattr(item, "gateways_InclusiveGateway", None)
                    
                    if opp_val == self:
                        setattr(item, "gateways_InclusiveGateway", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gateways_InclusiveGateway"):
                    opp_val = getattr(item, "gateways_InclusiveGateway", None)
                    
                    setattr(item, "gateways_InclusiveGateway", self)
                    

    @property
    def bpmn2_DocumentRoot226(self):
        return self.__bpmn2_DocumentRoot226

    @bpmn2_DocumentRoot226.setter
    def bpmn2_DocumentRoot226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot226", None)
        self.__bpmn2_DocumentRoot226 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Rendering"):
                    opp_val = getattr(item, "Rendering", None)
                    
                    if opp_val == self:
                        setattr(item, "Rendering", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Rendering"):
                    opp_val = getattr(item, "Rendering", None)
                    
                    setattr(item, "Rendering", self)
                    

    @property
    def bpmn2_DocumentRoot128(self):
        return self.__bpmn2_DocumentRoot128

    @bpmn2_DocumentRoot128.setter
    def bpmn2_DocumentRoot128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot128", None)
        self.__bpmn2_DocumentRoot128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extension_ExtensionAttributeValue"):
                    opp_val = getattr(item, "extension_ExtensionAttributeValue", None)
                    
                    if opp_val == self:
                        setattr(item, "extension_ExtensionAttributeValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extension_ExtensionAttributeValue"):
                    opp_val = getattr(item, "extension_ExtensionAttributeValue", None)
                    
                    setattr(item, "extension_ExtensionAttributeValue", self)
                    

    @property
    def bpmn2_DocumentRoot258(self):
        return self.__bpmn2_DocumentRoot258

    @bpmn2_DocumentRoot258.setter
    def bpmn2_DocumentRoot258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot258", None)
        self.__bpmn2_DocumentRoot258 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SubProcess"):
                    opp_val = getattr(item, "SubProcess", None)
                    
                    if opp_val == self:
                        setattr(item, "SubProcess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SubProcess"):
                    opp_val = getattr(item, "SubProcess", None)
                    
                    setattr(item, "SubProcess", self)
                    

    @property
    def bpmn2_DocumentRoot132(self):
        return self.__bpmn2_DocumentRoot132

    @bpmn2_DocumentRoot132.setter
    def bpmn2_DocumentRoot132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot132", None)
        self.__bpmn2_DocumentRoot132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FormalExpression"):
                    opp_val = getattr(item, "FormalExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "FormalExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FormalExpression"):
                    opp_val = getattr(item, "FormalExpression", None)
                    
                    setattr(item, "FormalExpression", self)
                    

    @property
    def bpmn2_DocumentRoot164(self):
        return self.__bpmn2_DocumentRoot164

    @bpmn2_DocumentRoot164.setter
    def bpmn2_DocumentRoot164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot164", None)
        self.__bpmn2_DocumentRoot164 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputSet"):
                    opp_val = getattr(item, "InputSet", None)
                    
                    if opp_val == self:
                        setattr(item, "InputSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputSet"):
                    opp_val = getattr(item, "InputSet", None)
                    
                    setattr(item, "InputSet", self)
                    

    @property
    def bpmn2_DocumentRoot19(self):
        return self.__bpmn2_DocumentRoot19

    @bpmn2_DocumentRoot19.setter
    def bpmn2_DocumentRoot19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot19", None)
        self.__bpmn2_DocumentRoot19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BaseElement"):
                    opp_val = getattr(item, "BaseElement", None)
                    
                    if opp_val == self:
                        setattr(item, "BaseElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BaseElement"):
                    opp_val = getattr(item, "BaseElement", None)
                    
                    setattr(item, "BaseElement", self)
                    

    @property
    def bpmn2_DocumentRoot138(self):
        return self.__bpmn2_DocumentRoot138

    @bpmn2_DocumentRoot138.setter
    def bpmn2_DocumentRoot138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot138", None)
        self.__bpmn2_DocumentRoot138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalChoreographyTask"):
                    opp_val = getattr(item, "GlobalChoreographyTask", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalChoreographyTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalChoreographyTask"):
                    opp_val = getattr(item, "GlobalChoreographyTask", None)
                    
                    setattr(item, "GlobalChoreographyTask", self)
                    

    @property
    def bpmn2_DocumentRoot144(self):
        return self.__bpmn2_DocumentRoot144

    @bpmn2_DocumentRoot144.setter
    def bpmn2_DocumentRoot144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot144", None)
        self.__bpmn2_DocumentRoot144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalScriptTask"):
                    opp_val = getattr(item, "GlobalScriptTask", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalScriptTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalScriptTask"):
                    opp_val = getattr(item, "GlobalScriptTask", None)
                    
                    setattr(item, "GlobalScriptTask", self)
                    

    @property
    def bpmn2_DocumentRoot200(self):
        return self.__bpmn2_DocumentRoot200

    @bpmn2_DocumentRoot200.setter
    def bpmn2_DocumentRoot200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot200", None)
        self.__bpmn2_DocumentRoot200 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    setattr(item, "Operation", self)
                    

    @property
    def bpmn2_DocumentRoot188(self):
        return self.__bpmn2_DocumentRoot188

    @bpmn2_DocumentRoot188.setter
    def bpmn2_DocumentRoot188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot188", None)
        self.__bpmn2_DocumentRoot188 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Message"):
                    opp_val = getattr(item, "Message", None)
                    
                    if opp_val == self:
                        setattr(item, "Message", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Message"):
                    opp_val = getattr(item, "Message", None)
                    
                    setattr(item, "Message", self)
                    

    @property
    def bpmn2_DocumentRoot180(self):
        return self.__bpmn2_DocumentRoot180

    @bpmn2_DocumentRoot180.setter
    def bpmn2_DocumentRoot180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot180", None)
        self.__bpmn2_DocumentRoot180 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LaneSet"):
                    opp_val = getattr(item, "LaneSet", None)
                    
                    if opp_val == self:
                        setattr(item, "LaneSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LaneSet"):
                    opp_val = getattr(item, "LaneSet", None)
                    
                    setattr(item, "LaneSet", self)
                    

    @property
    def bpmn2_DocumentRoot9(self):
        return self.__bpmn2_DocumentRoot9

    @bpmn2_DocumentRoot9.setter
    def bpmn2_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot9", None)
        self.__bpmn2_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flows_FlowElement"):
                    opp_val = getattr(item, "flows_FlowElement", None)
                    
                    if opp_val == self:
                        setattr(item, "flows_FlowElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flows_FlowElement"):
                    opp_val = getattr(item, "flows_FlowElement", None)
                    
                    setattr(item, "flows_FlowElement", self)
                    

    @property
    def bpmn2_DocumentRoot62(self):
        return self.__bpmn2_DocumentRoot62

    @bpmn2_DocumentRoot62.setter
    def bpmn2_DocumentRoot62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot62", None)
        self.__bpmn2_DocumentRoot62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gateways_ComplexGateway"):
                    opp_val = getattr(item, "gateways_ComplexGateway", None)
                    
                    if opp_val == self:
                        setattr(item, "gateways_ComplexGateway", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gateways_ComplexGateway"):
                    opp_val = getattr(item, "gateways_ComplexGateway", None)
                    
                    setattr(item, "gateways_ComplexGateway", self)
                    

    @property
    def bpmn2_DocumentRoot96(self):
        return self.__bpmn2_DocumentRoot96

    @bpmn2_DocumentRoot96.setter
    def bpmn2_DocumentRoot96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot96", None)
        self.__bpmn2_DocumentRoot96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataState"):
                    opp_val = getattr(item, "DataState", None)
                    
                    if opp_val == self:
                        setattr(item, "DataState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataState"):
                    opp_val = getattr(item, "DataState", None)
                    
                    setattr(item, "DataState", self)
                    

    @property
    def bpmn2_DocumentRoot218(self):
        return self.__bpmn2_DocumentRoot218

    @bpmn2_DocumentRoot218.setter
    def bpmn2_DocumentRoot218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot218", None)
        self.__bpmn2_DocumentRoot218 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Process"):
                    opp_val = getattr(item, "Process", None)
                    
                    if opp_val == self:
                        setattr(item, "Process", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process"):
                    opp_val = getattr(item, "Process", None)
                    
                    setattr(item, "Process", self)
                    

    @property
    def bpmn2_DocumentRoot220(self):
        return self.__bpmn2_DocumentRoot220

    @bpmn2_DocumentRoot220.setter
    def bpmn2_DocumentRoot220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot220", None)
        self.__bpmn2_DocumentRoot220 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    if opp_val == self:
                        setattr(item, "Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    setattr(item, "Property", self)
                    

    @property
    def bpmn2_DocumentRoot78(self):
        return self.__bpmn2_DocumentRoot78

    @bpmn2_DocumentRoot78.setter
    def bpmn2_DocumentRoot78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot78", None)
        self.__bpmn2_DocumentRoot78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "correlations_CorrelationPropertyRetrievalExpression"):
                    opp_val = getattr(item, "correlations_CorrelationPropertyRetrievalExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "correlations_CorrelationPropertyRetrievalExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "correlations_CorrelationPropertyRetrievalExpression"):
                    opp_val = getattr(item, "correlations_CorrelationPropertyRetrievalExpression", None)
                    
                    setattr(item, "correlations_CorrelationPropertyRetrievalExpression", self)
                    

    @property
    def bpmn2_DocumentRoot160(self):
        return self.__bpmn2_DocumentRoot160

    @bpmn2_DocumentRoot160.setter
    def bpmn2_DocumentRoot160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot160", None)
        self.__bpmn2_DocumentRoot160 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Import"):
                    opp_val = getattr(item, "Import", None)
                    
                    if opp_val == self:
                        setattr(item, "Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Import"):
                    opp_val = getattr(item, "Import", None)
                    
                    setattr(item, "Import", self)
                    

    @property
    def bpmn2_DocumentRoot108(self):
        return self.__bpmn2_DocumentRoot108

    @bpmn2_DocumentRoot108.setter
    def bpmn2_DocumentRoot108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot108", None)
        self.__bpmn2_DocumentRoot108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EndPoint"):
                    opp_val = getattr(item, "EndPoint", None)
                    
                    if opp_val == self:
                        setattr(item, "EndPoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EndPoint"):
                    opp_val = getattr(item, "EndPoint", None)
                    
                    setattr(item, "EndPoint", self)
                    

    @property
    def bpmn2_DocumentRoot38(self):
        return self.__bpmn2_DocumentRoot38

    @bpmn2_DocumentRoot38.setter
    def bpmn2_DocumentRoot38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot38", None)
        self.__bpmn2_DocumentRoot38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_CancelEventDefinition"):
                    opp_val = getattr(item, "events_CancelEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "events_CancelEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_CancelEventDefinition"):
                    opp_val = getattr(item, "events_CancelEventDefinition", None)
                    
                    setattr(item, "events_CancelEventDefinition", self)
                    

    @property
    def bpmn2_DocumentRoot60(self):
        return self.__bpmn2_DocumentRoot60

    @bpmn2_DocumentRoot60.setter
    def bpmn2_DocumentRoot60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot60", None)
        self.__bpmn2_DocumentRoot60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ComplexBehaviorDefinition"):
                    opp_val = getattr(item, "ComplexBehaviorDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "ComplexBehaviorDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ComplexBehaviorDefinition"):
                    opp_val = getattr(item, "ComplexBehaviorDefinition", None)
                    
                    setattr(item, "ComplexBehaviorDefinition", self)
                    

    @property
    def bpmn2_DocumentRoot100(self):
        return self.__bpmn2_DocumentRoot100

    @bpmn2_DocumentRoot100.setter
    def bpmn2_DocumentRoot100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot100", None)
        self.__bpmn2_DocumentRoot100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataStoreReference"):
                    opp_val = getattr(item, "DataStoreReference", None)
                    
                    if opp_val == self:
                        setattr(item, "DataStoreReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataStoreReference"):
                    opp_val = getattr(item, "DataStoreReference", None)
                    
                    setattr(item, "DataStoreReference", self)
                    

    @property
    def bpmn2_DocumentRoot142(self):
        return self.__bpmn2_DocumentRoot142

    @bpmn2_DocumentRoot142.setter
    def bpmn2_DocumentRoot142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot142", None)
        self.__bpmn2_DocumentRoot142 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalManualTask"):
                    opp_val = getattr(item, "GlobalManualTask", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalManualTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalManualTask"):
                    opp_val = getattr(item, "GlobalManualTask", None)
                    
                    setattr(item, "GlobalManualTask", self)
                    

    @property
    def bpmn2_DocumentRoot46(self):
        return self.__bpmn2_DocumentRoot46

    @bpmn2_DocumentRoot46.setter
    def bpmn2_DocumentRoot46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot46", None)
        self.__bpmn2_DocumentRoot46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "artifacts_Category"):
                    opp_val = getattr(item, "artifacts_Category", None)
                    
                    if opp_val == self:
                        setattr(item, "artifacts_Category", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "artifacts_Category"):
                    opp_val = getattr(item, "artifacts_Category", None)
                    
                    setattr(item, "artifacts_Category", self)
                    

    @property
    def bpmn2_DocumentRoot94(self):
        return self.__bpmn2_DocumentRoot94

    @bpmn2_DocumentRoot94.setter
    def bpmn2_DocumentRoot94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot94", None)
        self.__bpmn2_DocumentRoot94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataOutputAssociation"):
                    opp_val = getattr(item, "DataOutputAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "DataOutputAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataOutputAssociation"):
                    opp_val = getattr(item, "DataOutputAssociation", None)
                    
                    setattr(item, "DataOutputAssociation", self)
                    

    @property
    def bpmn2_DocumentRoot206(self):
        return self.__bpmn2_DocumentRoot206

    @bpmn2_DocumentRoot206.setter
    def bpmn2_DocumentRoot206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot206", None)
        self.__bpmn2_DocumentRoot206 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Participant"):
                    opp_val = getattr(item, "Participant", None)
                    
                    if opp_val == self:
                        setattr(item, "Participant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Participant"):
                    opp_val = getattr(item, "Participant", None)
                    
                    setattr(item, "Participant", self)
                    

    @property
    def bpmn2_DocumentRoot148(self):
        return self.__bpmn2_DocumentRoot148

    @bpmn2_DocumentRoot148.setter
    def bpmn2_DocumentRoot148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot148", None)
        self.__bpmn2_DocumentRoot148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalUserTask"):
                    opp_val = getattr(item, "GlobalUserTask", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalUserTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalUserTask"):
                    opp_val = getattr(item, "GlobalUserTask", None)
                    
                    setattr(item, "GlobalUserTask", self)
                    

    @property
    def bpmn2_DocumentRoot192(self):
        return self.__bpmn2_DocumentRoot192

    @bpmn2_DocumentRoot192.setter
    def bpmn2_DocumentRoot192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot192", None)
        self.__bpmn2_DocumentRoot192 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageFlow"):
                    opp_val = getattr(item, "MessageFlow", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageFlow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageFlow"):
                    opp_val = getattr(item, "MessageFlow", None)
                    
                    setattr(item, "MessageFlow", self)
                    

    @property
    def bpmn2_DocumentRoot44(self):
        return self.__bpmn2_DocumentRoot44

    @bpmn2_DocumentRoot44.setter
    def bpmn2_DocumentRoot44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot44", None)
        self.__bpmn2_DocumentRoot44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_CatchEvent"):
                    opp_val = getattr(item, "events_CatchEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "events_CatchEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_CatchEvent"):
                    opp_val = getattr(item, "events_CatchEvent", None)
                    
                    setattr(item, "events_CatchEvent", self)
                    

    @property
    def bpmn2_DocumentRoot74(self):
        return self.__bpmn2_DocumentRoot74

    @bpmn2_DocumentRoot74.setter
    def bpmn2_DocumentRoot74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot74", None)
        self.__bpmn2_DocumentRoot74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "correlations_CorrelationProperty"):
                    opp_val = getattr(item, "correlations_CorrelationProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "correlations_CorrelationProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "correlations_CorrelationProperty"):
                    opp_val = getattr(item, "correlations_CorrelationProperty", None)
                    
                    setattr(item, "correlations_CorrelationProperty", self)
                    

    @property
    def bpmn2_DocumentRoot13(self):
        return self.__bpmn2_DocumentRoot13

    @bpmn2_DocumentRoot13.setter
    def bpmn2_DocumentRoot13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot13", None)
        self.__bpmn2_DocumentRoot13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Assignment"):
                    opp_val = getattr(item, "Assignment", None)
                    
                    if opp_val == self:
                        setattr(item, "Assignment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Assignment"):
                    opp_val = getattr(item, "Assignment", None)
                    
                    setattr(item, "Assignment", self)
                    

    @property
    def bpmn2_DocumentRoot166(self):
        return self.__bpmn2_DocumentRoot166

    @bpmn2_DocumentRoot166.setter
    def bpmn2_DocumentRoot166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot166", None)
        self.__bpmn2_DocumentRoot166 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interface"):
                    opp_val = getattr(item, "Interface", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface"):
                    opp_val = getattr(item, "Interface", None)
                    
                    setattr(item, "Interface", self)
                    

    @property
    def bpmn2_DocumentRoot104(self):
        return self.__bpmn2_DocumentRoot104

    @bpmn2_DocumentRoot104.setter
    def bpmn2_DocumentRoot104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot104", None)
        self.__bpmn2_DocumentRoot104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Documentation"):
                    opp_val = getattr(item, "Documentation", None)
                    
                    if opp_val == self:
                        setattr(item, "Documentation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Documentation"):
                    opp_val = getattr(item, "Documentation", None)
                    
                    setattr(item, "Documentation", self)
                    

    @property
    def bpmn2_DocumentRoot84(self):
        return self.__bpmn2_DocumentRoot84

    @bpmn2_DocumentRoot84.setter
    def bpmn2_DocumentRoot84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot84", None)
        self.__bpmn2_DocumentRoot84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataInput"):
                    opp_val = getattr(item, "DataInput", None)
                    
                    if opp_val == self:
                        setattr(item, "DataInput", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataInput"):
                    opp_val = getattr(item, "DataInput", None)
                    
                    setattr(item, "DataInput", self)
                    

    @property
    def bpmn2_DocumentRoot82(self):
        return self.__bpmn2_DocumentRoot82

    @bpmn2_DocumentRoot82.setter
    def bpmn2_DocumentRoot82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot82", None)
        self.__bpmn2_DocumentRoot82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataAssociation"):
                    opp_val = getattr(item, "DataAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "DataAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataAssociation"):
                    opp_val = getattr(item, "DataAssociation", None)
                    
                    setattr(item, "DataAssociation", self)
                    

    @property
    def bpmn2_DocumentRoot70(self):
        return self.__bpmn2_DocumentRoot70

    @bpmn2_DocumentRoot70.setter
    def bpmn2_DocumentRoot70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot70", None)
        self.__bpmn2_DocumentRoot70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConversationLink"):
                    opp_val = getattr(item, "ConversationLink", None)
                    
                    if opp_val == self:
                        setattr(item, "ConversationLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConversationLink"):
                    opp_val = getattr(item, "ConversationLink", None)
                    
                    setattr(item, "ConversationLink", self)
                    

    @property
    def bpmn2_DocumentRoot56(self):
        return self.__bpmn2_DocumentRoot56

    @bpmn2_DocumentRoot56.setter
    def bpmn2_DocumentRoot56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot56", None)
        self.__bpmn2_DocumentRoot56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "choreographyactivities_ChoreographyTask"):
                    opp_val = getattr(item, "choreographyactivities_ChoreographyTask", None)
                    
                    if opp_val == self:
                        setattr(item, "choreographyactivities_ChoreographyTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "choreographyactivities_ChoreographyTask"):
                    opp_val = getattr(item, "choreographyactivities_ChoreographyTask", None)
                    
                    setattr(item, "choreographyactivities_ChoreographyTask", self)
                    

    @property
    def bpmn2_DocumentRoot64(self):
        return self.__bpmn2_DocumentRoot64

    @bpmn2_DocumentRoot64.setter
    def bpmn2_DocumentRoot64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot64", None)
        self.__bpmn2_DocumentRoot64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_ConditionalEventDefinition"):
                    opp_val = getattr(item, "events_ConditionalEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "events_ConditionalEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_ConditionalEventDefinition"):
                    opp_val = getattr(item, "events_ConditionalEventDefinition", None)
                    
                    setattr(item, "events_ConditionalEventDefinition", self)
                    

    @property
    def bpmn2_DocumentRoot28(self):
        return self.__bpmn2_DocumentRoot28

    @bpmn2_DocumentRoot28.setter
    def bpmn2_DocumentRoot28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot28", None)
        self.__bpmn2_DocumentRoot28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CallableElement"):
                    opp_val = getattr(item, "CallableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "CallableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CallableElement"):
                    opp_val = getattr(item, "CallableElement", None)
                    
                    setattr(item, "CallableElement", self)
                    

    @property
    def bpmn2_DocumentRoot30(self):
        return self.__bpmn2_DocumentRoot30

    @bpmn2_DocumentRoot30.setter
    def bpmn2_DocumentRoot30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot30", None)
        self.__bpmn2_DocumentRoot30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CallActivity"):
                    opp_val = getattr(item, "CallActivity", None)
                    
                    if opp_val == self:
                        setattr(item, "CallActivity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CallActivity"):
                    opp_val = getattr(item, "CallActivity", None)
                    
                    setattr(item, "CallActivity", self)
                    

    @property
    def bpmn2_DocumentRoot34(self):
        return self.__bpmn2_DocumentRoot34

    @bpmn2_DocumentRoot34.setter
    def bpmn2_DocumentRoot34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot34", None)
        self.__bpmn2_DocumentRoot34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CallConversation"):
                    opp_val = getattr(item, "CallConversation", None)
                    
                    if opp_val == self:
                        setattr(item, "CallConversation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CallConversation"):
                    opp_val = getattr(item, "CallConversation", None)
                    
                    setattr(item, "CallConversation", self)
                    

    @property
    def bpmn2_DocumentRoot198(self):
        return self.__bpmn2_DocumentRoot198

    @bpmn2_DocumentRoot198.setter
    def bpmn2_DocumentRoot198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot198", None)
        self.__bpmn2_DocumentRoot198 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MultiInstanceLoopCharacteristics"):
                    opp_val = getattr(item, "MultiInstanceLoopCharacteristics", None)
                    
                    if opp_val == self:
                        setattr(item, "MultiInstanceLoopCharacteristics", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MultiInstanceLoopCharacteristics"):
                    opp_val = getattr(item, "MultiInstanceLoopCharacteristics", None)
                    
                    setattr(item, "MultiInstanceLoopCharacteristics", self)
                    

    @property
    def bpmn2_DocumentRoot172(self):
        return self.__bpmn2_DocumentRoot172

    @bpmn2_DocumentRoot172.setter
    def bpmn2_DocumentRoot172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot172", None)
        self.__bpmn2_DocumentRoot172 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputOutputBinding"):
                    opp_val = getattr(item, "InputOutputBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "InputOutputBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputOutputBinding"):
                    opp_val = getattr(item, "InputOutputBinding", None)
                    
                    setattr(item, "InputOutputBinding", self)
                    

    @property
    def bpmn2_DocumentRoot248(self):
        return self.__bpmn2_DocumentRoot248

    @bpmn2_DocumentRoot248.setter
    def bpmn2_DocumentRoot248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot248", None)
        self.__bpmn2_DocumentRoot248 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_SignalEventDefinition"):
                    opp_val = getattr(item, "events_SignalEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "events_SignalEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_SignalEventDefinition"):
                    opp_val = getattr(item, "events_SignalEventDefinition", None)
                    
                    setattr(item, "events_SignalEventDefinition", self)
                    

    @property
    def bpmn2_DocumentRoot124(self):
        return self.__bpmn2_DocumentRoot124

    @bpmn2_DocumentRoot124.setter
    def bpmn2_DocumentRoot124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot124", None)
        self.__bpmn2_DocumentRoot124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression"):
                    opp_val = getattr(item, "Expression", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression"):
                    opp_val = getattr(item, "Expression", None)
                    
                    setattr(item, "Expression", self)
                    

    @property
    def bpmn2_DocumentRoot118(self):
        return self.__bpmn2_DocumentRoot118

    @bpmn2_DocumentRoot118.setter
    def bpmn2_DocumentRoot118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot118", None)
        self.__bpmn2_DocumentRoot118 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_Event"):
                    opp_val = getattr(item, "events_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "events_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_Event"):
                    opp_val = getattr(item, "events_Event", None)
                    
                    setattr(item, "events_Event", self)
                    

    @property
    def bpmn2_DocumentRoot250(self):
        return self.__bpmn2_DocumentRoot250

    @bpmn2_DocumentRoot250.setter
    def bpmn2_DocumentRoot250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot250", None)
        self.__bpmn2_DocumentRoot250 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StandardLoopCharacteristics"):
                    opp_val = getattr(item, "StandardLoopCharacteristics", None)
                    
                    if opp_val == self:
                        setattr(item, "StandardLoopCharacteristics", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StandardLoopCharacteristics"):
                    opp_val = getattr(item, "StandardLoopCharacteristics", None)
                    
                    setattr(item, "StandardLoopCharacteristics", self)
                    

    @property
    def bpmn2_DocumentRoot238(self):
        return self.__bpmn2_DocumentRoot238

    @bpmn2_DocumentRoot238.setter
    def bpmn2_DocumentRoot238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot238", None)
        self.__bpmn2_DocumentRoot238 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ScriptTask"):
                    opp_val = getattr(item, "ScriptTask", None)
                    
                    if opp_val == self:
                        setattr(item, "ScriptTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ScriptTask"):
                    opp_val = getattr(item, "ScriptTask", None)
                    
                    setattr(item, "ScriptTask", self)
                    

    @property
    def bpmn2_DocumentRoot21(self):
        return self.__bpmn2_DocumentRoot21

    @bpmn2_DocumentRoot21.setter
    def bpmn2_DocumentRoot21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot21", None)
        self.__bpmn2_DocumentRoot21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BaseElement22"):
                    opp_val = getattr(item, "BaseElement22", None)
                    
                    if opp_val == self:
                        setattr(item, "BaseElement22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BaseElement22"):
                    opp_val = getattr(item, "BaseElement22", None)
                    
                    setattr(item, "BaseElement22", self)
                    

    @property
    def bpmn2_DocumentRoot214(self):
        return self.__bpmn2_DocumentRoot214

    @bpmn2_DocumentRoot214.setter
    def bpmn2_DocumentRoot214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot214", None)
        self.__bpmn2_DocumentRoot214 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PartnerRole"):
                    opp_val = getattr(item, "PartnerRole", None)
                    
                    if opp_val == self:
                        setattr(item, "PartnerRole", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PartnerRole"):
                    opp_val = getattr(item, "PartnerRole", None)
                    
                    setattr(item, "PartnerRole", self)
                    

    @property
    def bpmn2_DocumentRoot66(self):
        return self.__bpmn2_DocumentRoot66

    @bpmn2_DocumentRoot66.setter
    def bpmn2_DocumentRoot66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot66", None)
        self.__bpmn2_DocumentRoot66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Conversation"):
                    opp_val = getattr(item, "Conversation", None)
                    
                    if opp_val == self:
                        setattr(item, "Conversation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Conversation"):
                    opp_val = getattr(item, "Conversation", None)
                    
                    setattr(item, "Conversation", self)
                    

    @property
    def bpmn2_DocumentRoot17(self):
        return self.__bpmn2_DocumentRoot17

    @bpmn2_DocumentRoot17.setter
    def bpmn2_DocumentRoot17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot17", None)
        self.__bpmn2_DocumentRoot17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Auditing"):
                    opp_val = getattr(item, "Auditing", None)
                    
                    if opp_val == self:
                        setattr(item, "Auditing", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Auditing"):
                    opp_val = getattr(item, "Auditing", None)
                    
                    setattr(item, "Auditing", self)
                    

    @property
    def bpmn2_DocumentRoot42(self):
        return self.__bpmn2_DocumentRoot42

    @bpmn2_DocumentRoot42.setter
    def bpmn2_DocumentRoot42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot42", None)
        self.__bpmn2_DocumentRoot42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RootElement"):
                    opp_val = getattr(item, "RootElement", None)
                    
                    if opp_val == self:
                        setattr(item, "RootElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RootElement"):
                    opp_val = getattr(item, "RootElement", None)
                    
                    setattr(item, "RootElement", self)
                    

    @property
    def bpmn2_DocumentRoot190(self):
        return self.__bpmn2_DocumentRoot190

    @bpmn2_DocumentRoot190.setter
    def bpmn2_DocumentRoot190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot190", None)
        self.__bpmn2_DocumentRoot190 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageEventDefinition"):
                    opp_val = getattr(item, "MessageEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageEventDefinition"):
                    opp_val = getattr(item, "MessageEventDefinition", None)
                    
                    setattr(item, "MessageEventDefinition", self)
                    

    @property
    def bpmn2_DocumentRoot50(self):
        return self.__bpmn2_DocumentRoot50

    @bpmn2_DocumentRoot50.setter
    def bpmn2_DocumentRoot50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot50", None)
        self.__bpmn2_DocumentRoot50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Choreography"):
                    opp_val = getattr(item, "Choreography", None)
                    
                    if opp_val == self:
                        setattr(item, "Choreography", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Choreography"):
                    opp_val = getattr(item, "Choreography", None)
                    
                    setattr(item, "Choreography", self)
                    

    @property
    def bpmn2_DocumentRoot26(self):
        return self.__bpmn2_DocumentRoot26

    @bpmn2_DocumentRoot26.setter
    def bpmn2_DocumentRoot26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot26", None)
        self.__bpmn2_DocumentRoot26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusinessRuleTask"):
                    opp_val = getattr(item, "BusinessRuleTask", None)
                    
                    if opp_val == self:
                        setattr(item, "BusinessRuleTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusinessRuleTask"):
                    opp_val = getattr(item, "BusinessRuleTask", None)
                    
                    setattr(item, "BusinessRuleTask", self)
                    

    @property
    def bpmn2_DocumentRoot2(self):
        return self.__bpmn2_DocumentRoot2

    @bpmn2_DocumentRoot2.setter
    def bpmn2_DocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot2", None)
        self.__bpmn2_DocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "bpmn2_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "bpmn2_EStringToStringMapEntry3", None)
                    
                    setattr(item, "bpmn2_EStringToStringMapEntry3", self)
                    

    @property
    def bpmn2_DocumentRoot252(self):
        return self.__bpmn2_DocumentRoot252

    @bpmn2_DocumentRoot252.setter
    def bpmn2_DocumentRoot252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot252", None)
        self.__bpmn2_DocumentRoot252 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_StartEvent"):
                    opp_val = getattr(item, "events_StartEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "events_StartEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_StartEvent"):
                    opp_val = getattr(item, "events_StartEvent", None)
                    
                    setattr(item, "events_StartEvent", self)
                    

    @property
    def bpmn2_DocumentRoot72(self):
        return self.__bpmn2_DocumentRoot72

    @bpmn2_DocumentRoot72.setter
    def bpmn2_DocumentRoot72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot72", None)
        self.__bpmn2_DocumentRoot72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "correlations_CorrelationKey"):
                    opp_val = getattr(item, "correlations_CorrelationKey", None)
                    
                    if opp_val == self:
                        setattr(item, "correlations_CorrelationKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "correlations_CorrelationKey"):
                    opp_val = getattr(item, "correlations_CorrelationKey", None)
                    
                    setattr(item, "correlations_CorrelationKey", self)
                    

    @property
    def bpmn2_DocumentRoot260(self):
        return self.__bpmn2_DocumentRoot260

    @bpmn2_DocumentRoot260.setter
    def bpmn2_DocumentRoot260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot260", None)
        self.__bpmn2_DocumentRoot260 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Task"):
                    opp_val = getattr(item, "Task", None)
                    
                    if opp_val == self:
                        setattr(item, "Task", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Task"):
                    opp_val = getattr(item, "Task", None)
                    
                    setattr(item, "Task", self)
                    

    @property
    def bpmn2_DocumentRoot228(self):
        return self.__bpmn2_DocumentRoot228

    @bpmn2_DocumentRoot228.setter
    def bpmn2_DocumentRoot228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot228", None)
        self.__bpmn2_DocumentRoot228 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Resource"):
                    opp_val = getattr(item, "Resource", None)
                    
                    if opp_val == self:
                        setattr(item, "Resource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Resource"):
                    opp_val = getattr(item, "Resource", None)
                    
                    setattr(item, "Resource", self)
                    

    @property
    def bpmn2_DocumentRoot208(self):
        return self.__bpmn2_DocumentRoot208

    @bpmn2_DocumentRoot208.setter
    def bpmn2_DocumentRoot208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot208", None)
        self.__bpmn2_DocumentRoot208 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ParticipantAssociation"):
                    opp_val = getattr(item, "ParticipantAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "ParticipantAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ParticipantAssociation"):
                    opp_val = getattr(item, "ParticipantAssociation", None)
                    
                    setattr(item, "ParticipantAssociation", self)
                    

    @property
    def bpmn2_DocumentRoot210(self):
        return self.__bpmn2_DocumentRoot210

    @bpmn2_DocumentRoot210.setter
    def bpmn2_DocumentRoot210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot210", None)
        self.__bpmn2_DocumentRoot210 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ParticipantMultiplicity"):
                    opp_val = getattr(item, "ParticipantMultiplicity", None)
                    
                    if opp_val == self:
                        setattr(item, "ParticipantMultiplicity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ParticipantMultiplicity"):
                    opp_val = getattr(item, "ParticipantMultiplicity", None)
                    
                    setattr(item, "ParticipantMultiplicity", self)
                    

    @property
    def bpmn2_DocumentRoot48(self):
        return self.__bpmn2_DocumentRoot48

    @bpmn2_DocumentRoot48.setter
    def bpmn2_DocumentRoot48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot48", None)
        self.__bpmn2_DocumentRoot48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "artifacts_CategoryValue"):
                    opp_val = getattr(item, "artifacts_CategoryValue", None)
                    
                    if opp_val == self:
                        setattr(item, "artifacts_CategoryValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "artifacts_CategoryValue"):
                    opp_val = getattr(item, "artifacts_CategoryValue", None)
                    
                    setattr(item, "artifacts_CategoryValue", self)
                    

    @property
    def bpmn2_DocumentRoot11(self):
        return self.__bpmn2_DocumentRoot11

    @bpmn2_DocumentRoot11.setter
    def bpmn2_DocumentRoot11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot11", None)
        self.__bpmn2_DocumentRoot11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "artifacts_Artifact"):
                    opp_val = getattr(item, "artifacts_Artifact", None)
                    
                    if opp_val == self:
                        setattr(item, "artifacts_Artifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "artifacts_Artifact"):
                    opp_val = getattr(item, "artifacts_Artifact", None)
                    
                    setattr(item, "artifacts_Artifact", self)
                    

    @property
    def bpmn2_DocumentRoot156(self):
        return self.__bpmn2_DocumentRoot156

    @bpmn2_DocumentRoot156.setter
    def bpmn2_DocumentRoot156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot156", None)
        self.__bpmn2_DocumentRoot156 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResourceRole"):
                    opp_val = getattr(item, "ResourceRole", None)
                    
                    if opp_val == self:
                        setattr(item, "ResourceRole", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResourceRole"):
                    opp_val = getattr(item, "ResourceRole", None)
                    
                    setattr(item, "ResourceRole", self)
                    

    @property
    def bpmn2_DocumentRoot126(self):
        return self.__bpmn2_DocumentRoot126

    @bpmn2_DocumentRoot126.setter
    def bpmn2_DocumentRoot126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot126", None)
        self.__bpmn2_DocumentRoot126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extension_Extension"):
                    opp_val = getattr(item, "extension_Extension", None)
                    
                    if opp_val == self:
                        setattr(item, "extension_Extension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extension_Extension"):
                    opp_val = getattr(item, "extension_Extension", None)
                    
                    setattr(item, "extension_Extension", self)
                    

    @property
    def bpmn2_DocumentRoot116(self):
        return self.__bpmn2_DocumentRoot116

    @bpmn2_DocumentRoot116.setter
    def bpmn2_DocumentRoot116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot116", None)
        self.__bpmn2_DocumentRoot116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_EscalationEventDefinition"):
                    opp_val = getattr(item, "events_EscalationEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "events_EscalationEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_EscalationEventDefinition"):
                    opp_val = getattr(item, "events_EscalationEventDefinition", None)
                    
                    setattr(item, "events_EscalationEventDefinition", self)
                    

    @property
    def bpmn2_DocumentRoot5(self):
        return self.__bpmn2_DocumentRoot5

    @bpmn2_DocumentRoot5.setter
    def bpmn2_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot5", None)
        self.__bpmn2_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Activity"):
                    opp_val = getattr(item, "Activity", None)
                    
                    if opp_val == self:
                        setattr(item, "Activity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Activity"):
                    opp_val = getattr(item, "Activity", None)
                    
                    setattr(item, "Activity", self)
                    

    @property
    def bpmn2_DocumentRoot24(self):
        return self.__bpmn2_DocumentRoot24

    @bpmn2_DocumentRoot24.setter
    def bpmn2_DocumentRoot24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot24", None)
        self.__bpmn2_DocumentRoot24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_BoundaryEvent"):
                    opp_val = getattr(item, "events_BoundaryEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "events_BoundaryEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_BoundaryEvent"):
                    opp_val = getattr(item, "events_BoundaryEvent", None)
                    
                    setattr(item, "events_BoundaryEvent", self)
                    

    @property
    def bpmn2_DocumentRoot58(self):
        return self.__bpmn2_DocumentRoot58

    @bpmn2_DocumentRoot58.setter
    def bpmn2_DocumentRoot58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot58", None)
        self.__bpmn2_DocumentRoot58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_CompensateEventDefinition"):
                    opp_val = getattr(item, "events_CompensateEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "events_CompensateEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_CompensateEventDefinition"):
                    opp_val = getattr(item, "events_CompensateEventDefinition", None)
                    
                    setattr(item, "events_CompensateEventDefinition", self)
                    

    @property
    def bpmn2_DocumentRoot242(self):
        return self.__bpmn2_DocumentRoot242

    @bpmn2_DocumentRoot242.setter
    def bpmn2_DocumentRoot242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot242", None)
        self.__bpmn2_DocumentRoot242 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flows_SequenceFlow"):
                    opp_val = getattr(item, "flows_SequenceFlow", None)
                    
                    if opp_val == self:
                        setattr(item, "flows_SequenceFlow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flows_SequenceFlow"):
                    opp_val = getattr(item, "flows_SequenceFlow", None)
                    
                    setattr(item, "flows_SequenceFlow", self)
                    

    @property
    def bpmn2_DocumentRoot120(self):
        return self.__bpmn2_DocumentRoot120

    @bpmn2_DocumentRoot120.setter
    def bpmn2_DocumentRoot120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot120", None)
        self.__bpmn2_DocumentRoot120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gateways_EventBasedGateway"):
                    opp_val = getattr(item, "gateways_EventBasedGateway", None)
                    
                    if opp_val == self:
                        setattr(item, "gateways_EventBasedGateway", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gateways_EventBasedGateway"):
                    opp_val = getattr(item, "gateways_EventBasedGateway", None)
                    
                    setattr(item, "gateways_EventBasedGateway", self)
                    

    @property
    def bpmn2_DocumentRoot130(self):
        return self.__bpmn2_DocumentRoot130

    @bpmn2_DocumentRoot130.setter
    def bpmn2_DocumentRoot130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot130", None)
        self.__bpmn2_DocumentRoot130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flows_FlowNode"):
                    opp_val = getattr(item, "flows_FlowNode", None)
                    
                    if opp_val == self:
                        setattr(item, "flows_FlowNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flows_FlowNode"):
                    opp_val = getattr(item, "flows_FlowNode", None)
                    
                    setattr(item, "flows_FlowNode", self)
                    

    @property
    def bpmn2_DocumentRoot136(self):
        return self.__bpmn2_DocumentRoot136

    @bpmn2_DocumentRoot136.setter
    def bpmn2_DocumentRoot136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot136", None)
        self.__bpmn2_DocumentRoot136 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalBusinessRuleTask"):
                    opp_val = getattr(item, "GlobalBusinessRuleTask", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalBusinessRuleTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalBusinessRuleTask"):
                    opp_val = getattr(item, "GlobalBusinessRuleTask", None)
                    
                    setattr(item, "GlobalBusinessRuleTask", self)
                    

    @property
    def bpmn2_DocumentRoot134(self):
        return self.__bpmn2_DocumentRoot134

    @bpmn2_DocumentRoot134.setter
    def bpmn2_DocumentRoot134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot134", None)
        self.__bpmn2_DocumentRoot134 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gateways_Gateway"):
                    opp_val = getattr(item, "gateways_Gateway", None)
                    
                    if opp_val == self:
                        setattr(item, "gateways_Gateway", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gateways_Gateway"):
                    opp_val = getattr(item, "gateways_Gateway", None)
                    
                    setattr(item, "gateways_Gateway", self)
                    

    @property
    def bpmn2_DocumentRoot178(self):
        return self.__bpmn2_DocumentRoot178

    @bpmn2_DocumentRoot178.setter
    def bpmn2_DocumentRoot178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot178", None)
        self.__bpmn2_DocumentRoot178 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Lane"):
                    opp_val = getattr(item, "Lane", None)
                    
                    if opp_val == self:
                        setattr(item, "Lane", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Lane"):
                    opp_val = getattr(item, "Lane", None)
                    
                    setattr(item, "Lane", self)
                    

    @property
    def bpmn2_DocumentRoot174(self):
        return self.__bpmn2_DocumentRoot174

    @bpmn2_DocumentRoot174.setter
    def bpmn2_DocumentRoot174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot174", None)
        self.__bpmn2_DocumentRoot174 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InputOutputSpecification"):
                    opp_val = getattr(item, "InputOutputSpecification", None)
                    
                    if opp_val == self:
                        setattr(item, "InputOutputSpecification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InputOutputSpecification"):
                    opp_val = getattr(item, "InputOutputSpecification", None)
                    
                    setattr(item, "InputOutputSpecification", self)
                    

    @property
    def bpmn2_DocumentRoot90(self):
        return self.__bpmn2_DocumentRoot90

    @bpmn2_DocumentRoot90.setter
    def bpmn2_DocumentRoot90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot90", None)
        self.__bpmn2_DocumentRoot90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataObjectReference"):
                    opp_val = getattr(item, "DataObjectReference", None)
                    
                    if opp_val == self:
                        setattr(item, "DataObjectReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataObjectReference"):
                    opp_val = getattr(item, "DataObjectReference", None)
                    
                    setattr(item, "DataObjectReference", self)
                    

    @property
    def bpmn2_DocumentRoot36(self):
        return self.__bpmn2_DocumentRoot36

    @bpmn2_DocumentRoot36.setter
    def bpmn2_DocumentRoot36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot36", None)
        self.__bpmn2_DocumentRoot36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConversationNode"):
                    opp_val = getattr(item, "ConversationNode", None)
                    
                    if opp_val == self:
                        setattr(item, "ConversationNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConversationNode"):
                    opp_val = getattr(item, "ConversationNode", None)
                    
                    setattr(item, "ConversationNode", self)
                    

    @property
    def bpmn2_DocumentRoot236(self):
        return self.__bpmn2_DocumentRoot236

    @bpmn2_DocumentRoot236.setter
    def bpmn2_DocumentRoot236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot236", None)
        self.__bpmn2_DocumentRoot236 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bpmn2_EObject"):
                    opp_val = getattr(item, "bpmn2_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "bpmn2_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bpmn2_EObject"):
                    opp_val = getattr(item, "bpmn2_EObject", None)
                    
                    setattr(item, "bpmn2_EObject", self)
                    

    @property
    def bpmn2_DocumentRoot110(self):
        return self.__bpmn2_DocumentRoot110

    @bpmn2_DocumentRoot110.setter
    def bpmn2_DocumentRoot110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot110", None)
        self.__bpmn2_DocumentRoot110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Error"):
                    opp_val = getattr(item, "Error", None)
                    
                    if opp_val == self:
                        setattr(item, "Error", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Error"):
                    opp_val = getattr(item, "Error", None)
                    
                    setattr(item, "Error", self)
                    

    @property
    def bpmn2_DocumentRoot224(self):
        return self.__bpmn2_DocumentRoot224

    @bpmn2_DocumentRoot224.setter
    def bpmn2_DocumentRoot224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot224", None)
        self.__bpmn2_DocumentRoot224 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relationship"):
                    opp_val = getattr(item, "Relationship", None)
                    
                    if opp_val == self:
                        setattr(item, "Relationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relationship"):
                    opp_val = getattr(item, "Relationship", None)
                    
                    setattr(item, "Relationship", self)
                    

    @property
    def bpmn2_DocumentRoot68(self):
        return self.__bpmn2_DocumentRoot68

    @bpmn2_DocumentRoot68.setter
    def bpmn2_DocumentRoot68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot68", None)
        self.__bpmn2_DocumentRoot68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConversationAssociation"):
                    opp_val = getattr(item, "ConversationAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "ConversationAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConversationAssociation"):
                    opp_val = getattr(item, "ConversationAssociation", None)
                    
                    setattr(item, "ConversationAssociation", self)
                    

    @property
    def bpmn2_DocumentRoot146(self):
        return self.__bpmn2_DocumentRoot146

    @bpmn2_DocumentRoot146.setter
    def bpmn2_DocumentRoot146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot146", None)
        self.__bpmn2_DocumentRoot146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalTask"):
                    opp_val = getattr(item, "GlobalTask", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalTask"):
                    opp_val = getattr(item, "GlobalTask", None)
                    
                    setattr(item, "GlobalTask", self)
                    

    @property
    def bpmn2_DocumentRoot40(self):
        return self.__bpmn2_DocumentRoot40

    @bpmn2_DocumentRoot40.setter
    def bpmn2_DocumentRoot40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot40", None)
        self.__bpmn2_DocumentRoot40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_EventDefinition"):
                    opp_val = getattr(item, "events_EventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "events_EventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_EventDefinition"):
                    opp_val = getattr(item, "events_EventDefinition", None)
                    
                    setattr(item, "events_EventDefinition", self)
                    

    @property
    def bpmn2_DocumentRoot76(self):
        return self.__bpmn2_DocumentRoot76

    @bpmn2_DocumentRoot76.setter
    def bpmn2_DocumentRoot76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot76", None)
        self.__bpmn2_DocumentRoot76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "correlations_CorrelationPropertyBinding"):
                    opp_val = getattr(item, "correlations_CorrelationPropertyBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "correlations_CorrelationPropertyBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "correlations_CorrelationPropertyBinding"):
                    opp_val = getattr(item, "correlations_CorrelationPropertyBinding", None)
                    
                    setattr(item, "correlations_CorrelationPropertyBinding", self)
                    

    @property
    def bpmn2_DocumentRoot152(self):
        return self.__bpmn2_DocumentRoot152

    @bpmn2_DocumentRoot152.setter
    def bpmn2_DocumentRoot152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot152", None)
        self.__bpmn2_DocumentRoot152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HumanPerformer"):
                    opp_val = getattr(item, "HumanPerformer", None)
                    
                    if opp_val == self:
                        setattr(item, "HumanPerformer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HumanPerformer"):
                    opp_val = getattr(item, "HumanPerformer", None)
                    
                    setattr(item, "HumanPerformer", self)
                    

    @property
    def bpmn2_DocumentRoot194(self):
        return self.__bpmn2_DocumentRoot194

    @bpmn2_DocumentRoot194.setter
    def bpmn2_DocumentRoot194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot194", None)
        self.__bpmn2_DocumentRoot194 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessageFlowAssociation"):
                    opp_val = getattr(item, "MessageFlowAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "MessageFlowAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessageFlowAssociation"):
                    opp_val = getattr(item, "MessageFlowAssociation", None)
                    
                    setattr(item, "MessageFlowAssociation", self)
                    

    @property
    def bpmn2_DocumentRoot7(self):
        return self.__bpmn2_DocumentRoot7

    @bpmn2_DocumentRoot7.setter
    def bpmn2_DocumentRoot7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot7", None)
        self.__bpmn2_DocumentRoot7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AdHocSubProcess"):
                    opp_val = getattr(item, "AdHocSubProcess", None)
                    
                    if opp_val == self:
                        setattr(item, "AdHocSubProcess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AdHocSubProcess"):
                    opp_val = getattr(item, "AdHocSubProcess", None)
                    
                    setattr(item, "AdHocSubProcess", self)
                    

    @property
    def bpmn2_DocumentRoot52(self):
        return self.__bpmn2_DocumentRoot52

    @bpmn2_DocumentRoot52.setter
    def bpmn2_DocumentRoot52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot52", None)
        self.__bpmn2_DocumentRoot52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Collaboration"):
                    opp_val = getattr(item, "Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Collaboration"):
                    opp_val = getattr(item, "Collaboration", None)
                    
                    setattr(item, "Collaboration", self)
                    

    @property
    def bpmn2_DocumentRoot212(self):
        return self.__bpmn2_DocumentRoot212

    @bpmn2_DocumentRoot212.setter
    def bpmn2_DocumentRoot212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot212", None)
        self.__bpmn2_DocumentRoot212 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PartnerEntity"):
                    opp_val = getattr(item, "PartnerEntity", None)
                    
                    if opp_val == self:
                        setattr(item, "PartnerEntity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PartnerEntity"):
                    opp_val = getattr(item, "PartnerEntity", None)
                    
                    setattr(item, "PartnerEntity", self)
                    

    @property
    def bpmn2_DocumentRoot246(self):
        return self.__bpmn2_DocumentRoot246

    @bpmn2_DocumentRoot246.setter
    def bpmn2_DocumentRoot246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot246", None)
        self.__bpmn2_DocumentRoot246 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_Signal"):
                    opp_val = getattr(item, "events_Signal", None)
                    
                    if opp_val == self:
                        setattr(item, "events_Signal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_Signal"):
                    opp_val = getattr(item, "events_Signal", None)
                    
                    setattr(item, "events_Signal", self)
                    

    @property
    def bpmn2_DocumentRoot150(self):
        return self.__bpmn2_DocumentRoot150

    @bpmn2_DocumentRoot150.setter
    def bpmn2_DocumentRoot150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot150", None)
        self.__bpmn2_DocumentRoot150 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "artifacts_Group"):
                    opp_val = getattr(item, "artifacts_Group", None)
                    
                    if opp_val == self:
                        setattr(item, "artifacts_Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "artifacts_Group"):
                    opp_val = getattr(item, "artifacts_Group", None)
                    
                    setattr(item, "artifacts_Group", self)
                    

    @property
    def bpmn2_DocumentRoot114(self):
        return self.__bpmn2_DocumentRoot114

    @bpmn2_DocumentRoot114.setter
    def bpmn2_DocumentRoot114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot114", None)
        self.__bpmn2_DocumentRoot114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Escalation"):
                    opp_val = getattr(item, "Escalation", None)
                    
                    if opp_val == self:
                        setattr(item, "Escalation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Escalation"):
                    opp_val = getattr(item, "Escalation", None)
                    
                    setattr(item, "Escalation", self)
                    

    @property
    def bpmn2_DocumentRoot80(self):
        return self.__bpmn2_DocumentRoot80

    @bpmn2_DocumentRoot80.setter
    def bpmn2_DocumentRoot80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot80", None)
        self.__bpmn2_DocumentRoot80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "correlations_CorrelationSubscription"):
                    opp_val = getattr(item, "correlations_CorrelationSubscription", None)
                    
                    if opp_val == self:
                        setattr(item, "correlations_CorrelationSubscription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "correlations_CorrelationSubscription"):
                    opp_val = getattr(item, "correlations_CorrelationSubscription", None)
                    
                    setattr(item, "correlations_CorrelationSubscription", self)
                    

    @property
    def bpmn2_DocumentRoot154(self):
        return self.__bpmn2_DocumentRoot154

    @bpmn2_DocumentRoot154.setter
    def bpmn2_DocumentRoot154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot154", None)
        self.__bpmn2_DocumentRoot154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Performer"):
                    opp_val = getattr(item, "Performer", None)
                    
                    if opp_val == self:
                        setattr(item, "Performer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Performer"):
                    opp_val = getattr(item, "Performer", None)
                    
                    setattr(item, "Performer", self)
                    

    @property
    def bpmn2_DocumentRoot102(self):
        return self.__bpmn2_DocumentRoot102

    @bpmn2_DocumentRoot102.setter
    def bpmn2_DocumentRoot102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot102", None)
        self.__bpmn2_DocumentRoot102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Definitions"):
                    opp_val = getattr(item, "Definitions", None)
                    
                    if opp_val == self:
                        setattr(item, "Definitions", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Definitions"):
                    opp_val = getattr(item, "Definitions", None)
                    
                    setattr(item, "Definitions", self)
                    

    @property
    def bpmn2_DocumentRoot232(self):
        return self.__bpmn2_DocumentRoot232

    @bpmn2_DocumentRoot232.setter
    def bpmn2_DocumentRoot232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot232", None)
        self.__bpmn2_DocumentRoot232 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResourceParameter"):
                    opp_val = getattr(item, "ResourceParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "ResourceParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResourceParameter"):
                    opp_val = getattr(item, "ResourceParameter", None)
                    
                    setattr(item, "ResourceParameter", self)
                    

    @property
    def bpmn2_DocumentRoot273(self):
        return self.__bpmn2_DocumentRoot273

    @bpmn2_DocumentRoot273.setter
    def bpmn2_DocumentRoot273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot273", None)
        self.__bpmn2_DocumentRoot273 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transaction"):
                    opp_val = getattr(item, "Transaction", None)
                    
                    if opp_val == self:
                        setattr(item, "Transaction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transaction"):
                    opp_val = getattr(item, "Transaction", None)
                    
                    setattr(item, "Transaction", self)
                    

    @property
    def bpmn2_DocumentRoot256(self):
        return self.__bpmn2_DocumentRoot256

    @bpmn2_DocumentRoot256.setter
    def bpmn2_DocumentRoot256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot256", None)
        self.__bpmn2_DocumentRoot256 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SubConversation"):
                    opp_val = getattr(item, "SubConversation", None)
                    
                    if opp_val == self:
                        setattr(item, "SubConversation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SubConversation"):
                    opp_val = getattr(item, "SubConversation", None)
                    
                    setattr(item, "SubConversation", self)
                    

    @property
    def bpmn2_DocumentRoot182(self):
        return self.__bpmn2_DocumentRoot182

    @bpmn2_DocumentRoot182.setter
    def bpmn2_DocumentRoot182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot182", None)
        self.__bpmn2_DocumentRoot182 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_LinkEventDefinition"):
                    opp_val = getattr(item, "events_LinkEventDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "events_LinkEventDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_LinkEventDefinition"):
                    opp_val = getattr(item, "events_LinkEventDefinition", None)
                    
                    setattr(item, "events_LinkEventDefinition", self)
                    

    @property
    def bpmn2_DocumentRoot140(self):
        return self.__bpmn2_DocumentRoot140

    @bpmn2_DocumentRoot140.setter
    def bpmn2_DocumentRoot140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn2_DocumentRoot__bpmn2_DocumentRoot140", None)
        self.__bpmn2_DocumentRoot140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalConversation"):
                    opp_val = getattr(item, "GlobalConversation", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalConversation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalConversation"):
                    opp_val = getattr(item, "GlobalConversation", None)
                    
                    setattr(item, "GlobalConversation", self)
                    

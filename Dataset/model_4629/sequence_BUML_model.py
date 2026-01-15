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
sequence_SequenceDDiagram = Class(name="sequence::SequenceDDiagram")
DSemanticDiagram = Class(name="DSemanticDiagram")
EventEndsOrdering = Class(name="EventEndsOrdering")
sequence_description_BasicMessageMapping = Class(name="sequence::description::BasicMessageMapping")
MessageMapping = Class(name="MessageMapping")
sequence_description_ReturnMessageMapping = Class(name="sequence::description::ReturnMessageMapping")
sequence_description_CreationMessageMapping = Class(name="sequence::description::CreationMessageMapping")
sequence_description_DestructionMessageMapping = Class(name="sequence::description::DestructionMessageMapping")
sequence_description_MessageEndVariable = Class(name="sequence::description::MessageEndVariable")
AbstractVariable = Class(name="AbstractVariable")
InstanceRolesOrdering = Class(name="InstanceRolesOrdering")
sequence_description_SequenceDiagramDescription = Class(name="sequence::description::SequenceDiagramDescription")
DiagramDescription = Class(name="DiagramDescription")
sequence_description_InstanceRoleMapping = Class(name="sequence::description::InstanceRoleMapping")
NodeMapping = Class(name="NodeMapping")
sequence_description_EventMapping = Class(name="sequence::description::EventMapping", is_abstract=True)
sequence_description_DelimitedEventMapping = Class(name="sequence::description::DelimitedEventMapping", is_abstract=True)
EventMapping = Class(name="EventMapping")
sequence_description_ExecutionMapping = Class(name="sequence::description::ExecutionMapping")
description_NodeMapping = Class(name="description::NodeMapping")
description_DelimitedEventMapping = Class(name="description::DelimitedEventMapping")
sequence_description_StateMapping = Class(name="sequence::description::StateMapping")
sequence_description_EndOfLifeMapping = Class(name="sequence::description::EndOfLifeMapping")
sequence_description_MessageMapping = Class(name="sequence::description::MessageMapping", is_abstract=True)
description_EdgeMapping = Class(name="description::EdgeMapping")
description_EventMapping = Class(name="description::EventMapping")
tool_ElementVariable = Class(name="tool::ElementVariable")
sequence_tool_LifelineCreationTool = Class(name="sequence::tool::LifelineCreationTool")
tool_ContainerCreationDescription = Class(name="tool::ContainerCreationDescription")
sequence_tool_MessageCreationTool = Class(name="sequence::tool::MessageCreationTool")
tool_EdgeCreationDescription = Class(name="tool::EdgeCreationDescription")
tool_OrderedElementCreationTool = Class(name="tool::OrderedElementCreationTool")
sequence_tool_ExecutionCreationTool = Class(name="sequence::tool::ExecutionCreationTool")
sequence_tool_StateCreationTool = Class(name="sequence::tool::StateCreationTool")
sequence_description_CoveredLifelinesVariable = Class(name="sequence::description::CoveredLifelinesVariable")
sequence_description_FrameMapping = Class(name="sequence::description::FrameMapping", is_abstract=True)
description_ContainerMapping = Class(name="description::ContainerMapping")
sequence_description_InteractionUseMapping = Class(name="sequence::description::InteractionUseMapping")
FrameMapping = Class(name="FrameMapping")
sequence_description_CombinedFragmentMapping = Class(name="sequence::description::CombinedFragmentMapping")
sequence_description_OperandMapping = Class(name="sequence::description::OperandMapping")
sequence_description_ObservationPointMapping = Class(name="sequence::description::ObservationPointMapping")
sequence_tool_SequenceDiagramToolDescription = Class(name="sequence::tool::SequenceDiagramToolDescription")
sequence_tool_OrderedElementCreationTool = Class(name="sequence::tool::OrderedElementCreationTool", is_abstract=True)
MessageEndVariable = Class(name="MessageEndVariable")
sequence_tool_CoveringElementCreationTool = Class(name="sequence::tool::CoveringElementCreationTool", is_abstract=True)
CoveredLifelinesVariable = Class(name="CoveredLifelinesVariable")
sequence_tool_InstanceRoleCreationTool = Class(name="sequence::tool::InstanceRoleCreationTool")
tool_NodeCreationDescription = Class(name="tool::NodeCreationDescription")
tool_SequenceDiagramToolDescription = Class(name="tool::SequenceDiagramToolDescription")
sequence_ordering_EventEndsOrdering = Class(name="sequence::ordering::EventEndsOrdering")
ordering_sequence_SequenceDDiagram = Class(name="ordering::sequence::SequenceDDiagram")
sequence_tool_InteractionUseCreationTool = Class(name="sequence::tool::InteractionUseCreationTool")
EventEnd = Class(name="EventEnd")
tool_CoveringElementCreationTool = Class(name="tool::CoveringElementCreationTool")
sequence_tool_CombinedFragmentCreationTool = Class(name="sequence::tool::CombinedFragmentCreationTool")
sequence_tool_OperandCreationTool = Class(name="sequence::tool::OperandCreationTool")
sequence_tool_ObservationPointCreationTool = Class(name="sequence::tool::ObservationPointCreationTool")
sequence_tool_ReorderTool = Class(name="sequence::tool::ReorderTool")
tool_AbstractToolDescription = Class(name="tool::AbstractToolDescription")
tool_InitialOperation = Class(name="tool::InitialOperation")
sequence_tool_InstanceRoleReorderTool = Class(name="sequence::tool::InstanceRoleReorderTool")
InstanceRoleMapping = Class(name="InstanceRoleMapping")
sequence_template_TSequenceDiagram = Class(name="sequence::template::TSequenceDiagram")
description_RepresentationTemplate = Class(name="description::RepresentationTemplate")
template_TTransformer = Class(name="template::TTransformer")
TLifelineMapping = Class(name="TLifelineMapping")
TMessageMapping = Class(name="TMessageMapping")
sequence_template_TMessageExtremity = Class(name="sequence::template::TMessageExtremity", is_abstract=True)
sequence_ordering_EventEnd = Class(name="sequence::ordering::EventEnd", is_abstract=True)
ordering_sequence_EObject = Class(name="ordering::sequence::EObject")
sequence_ordering_SingleEventEnd = Class(name="sequence::ordering::SingleEventEnd")
sequence_ordering_CompoundEventEnd = Class(name="sequence::ordering::CompoundEventEnd")
SingleEventEnd = Class(name="SingleEventEnd")
sequence_ordering_InstanceRolesOrdering = Class(name="sequence::ordering::InstanceRolesOrdering")
sequence_template_TTransformer = Class(name="sequence::template::TTransformer")
template_sequence_EObject = Class(name="template::sequence::EObject")
sequence_template_TAbstractMapping = Class(name="sequence::template::TAbstractMapping")
TTransformer = Class(name="TTransformer")
sequence_template_TExecutionMapping = Class(name="sequence::template::TExecutionMapping")
sequence_template_TLifelineMapping = Class(name="sequence::template::TLifelineMapping")
template_TAbstractMapping = Class(name="template::TAbstractMapping")
template_TMessageExtremity = Class(name="template::TMessageExtremity")
TExecutionMapping = Class(name="TExecutionMapping")
style_NodeStyleDescription = Class(name="style::NodeStyleDescription")
TLifelineStyle = Class(name="TLifelineStyle")
TConditionalLifelineStyle = Class(name="TConditionalLifelineStyle")
sequence_template_TLifelineStyle = Class(name="sequence::template::TLifelineStyle")
ColorDescription = Class(name="ColorDescription")
sequence_template_TConditionalLifelineStyle = Class(name="sequence::template::TConditionalLifelineStyle")
TConditionalMessageStyle = Class(name="TConditionalMessageStyle")
sequence_template_TMessageStyle = Class(name="sequence::template::TMessageStyle")
TExecutionStyle = Class(name="TExecutionStyle")
TConditionalExecutionStyle = Class(name="TConditionalExecutionStyle")
sequence_template_TExecutionStyle = Class(name="sequence::template::TExecutionStyle")
sequence_template_TConditionalExecutionStyle = Class(name="sequence::template::TConditionalExecutionStyle")
sequence_template_TMessageMapping = Class(name="sequence::template::TMessageMapping", is_abstract=True)
TAbstractMapping = Class(name="TAbstractMapping")
TMessageStyle = Class(name="TMessageStyle")
sequence_template_TReturnMessageMapping = Class(name="sequence::template::TReturnMessageMapping")
TBasicMessageMapping = Class(name="TBasicMessageMapping")
sequence_template_TCreationMessageMapping = Class(name="sequence::template::TCreationMessageMapping")
sequence_template_TConditionalMessageStyle = Class(name="sequence::template::TConditionalMessageStyle")
sequence_template_TBasicMessageMapping = Class(name="sequence::template::TBasicMessageMapping")
TSourceTargetMessageMapping = Class(name="TSourceTargetMessageMapping")
TMessageExtremity = Class(name="TMessageExtremity")
sequence_template_TSourceTargetMessageMapping = Class(name="sequence::template::TSourceTargetMessageMapping", is_abstract=True)
sequence_template_TDestructionMessageMapping = Class(name="sequence::template::TDestructionMessageMapping")

# sequence_SequenceDDiagram class attributes and methods

# DSemanticDiagram class attributes and methods

# EventEndsOrdering class attributes and methods

# sequence_description_BasicMessageMapping class attributes and methods

# MessageMapping class attributes and methods

# sequence_description_ReturnMessageMapping class attributes and methods
sequence_description_ReturnMessageMapping_invocationMessageFinderExpression: Property = Property(name="invocationMessageFinderExpression", type=StringType)
sequence_description_ReturnMessageMapping.attributes={sequence_description_ReturnMessageMapping_invocationMessageFinderExpression}

# sequence_description_CreationMessageMapping class attributes and methods

# sequence_description_DestructionMessageMapping class attributes and methods

# sequence_description_MessageEndVariable class attributes and methods

# AbstractVariable class attributes and methods

# InstanceRolesOrdering class attributes and methods

# sequence_description_SequenceDiagramDescription class attributes and methods
sequence_description_SequenceDiagramDescription_endsOrdering: Property = Property(name="endsOrdering", type=StringType)
sequence_description_SequenceDiagramDescription_instanceRolesOrdering: Property = Property(name="instanceRolesOrdering", type=StringType)
sequence_description_SequenceDiagramDescription.attributes={sequence_description_SequenceDiagramDescription_instanceRolesOrdering, sequence_description_SequenceDiagramDescription_endsOrdering}

# DiagramDescription class attributes and methods

# sequence_description_InstanceRoleMapping class attributes and methods

# NodeMapping class attributes and methods

# sequence_description_EventMapping class attributes and methods

# sequence_description_DelimitedEventMapping class attributes and methods
sequence_description_DelimitedEventMapping_startingEndFinderExpression: Property = Property(name="startingEndFinderExpression", type=StringType)
sequence_description_DelimitedEventMapping_finishingEndFinderExpression: Property = Property(name="finishingEndFinderExpression", type=StringType)
sequence_description_DelimitedEventMapping.attributes={sequence_description_DelimitedEventMapping_finishingEndFinderExpression, sequence_description_DelimitedEventMapping_startingEndFinderExpression}

# EventMapping class attributes and methods

# sequence_description_ExecutionMapping class attributes and methods

# description_NodeMapping class attributes and methods

# description_DelimitedEventMapping class attributes and methods

# sequence_description_StateMapping class attributes and methods

# sequence_description_EndOfLifeMapping class attributes and methods

# sequence_description_MessageMapping class attributes and methods
sequence_description_MessageMapping_receivingEndFinderExpression: Property = Property(name="receivingEndFinderExpression", type=StringType)
sequence_description_MessageMapping_sendingEndFinderExpression: Property = Property(name="sendingEndFinderExpression", type=StringType)
sequence_description_MessageMapping.attributes={sequence_description_MessageMapping_receivingEndFinderExpression, sequence_description_MessageMapping_sendingEndFinderExpression}

# description_EdgeMapping class attributes and methods

# description_EventMapping class attributes and methods

# tool_ElementVariable class attributes and methods

# sequence_tool_LifelineCreationTool class attributes and methods

# tool_ContainerCreationDescription class attributes and methods

# sequence_tool_MessageCreationTool class attributes and methods

# tool_EdgeCreationDescription class attributes and methods

# tool_OrderedElementCreationTool class attributes and methods

# sequence_tool_ExecutionCreationTool class attributes and methods

# sequence_tool_StateCreationTool class attributes and methods

# sequence_description_CoveredLifelinesVariable class attributes and methods

# sequence_description_FrameMapping class attributes and methods
sequence_description_FrameMapping_coveredLifelinesExpression: Property = Property(name="coveredLifelinesExpression", type=StringType)
sequence_description_FrameMapping_centerLabelExpression: Property = Property(name="centerLabelExpression", type=StringType)
sequence_description_FrameMapping.attributes={sequence_description_FrameMapping_centerLabelExpression, sequence_description_FrameMapping_coveredLifelinesExpression}

# description_ContainerMapping class attributes and methods

# sequence_description_InteractionUseMapping class attributes and methods

# FrameMapping class attributes and methods

# sequence_description_CombinedFragmentMapping class attributes and methods

# sequence_description_OperandMapping class attributes and methods

# sequence_description_ObservationPointMapping class attributes and methods

# sequence_tool_SequenceDiagramToolDescription class attributes and methods

# sequence_tool_OrderedElementCreationTool class attributes and methods

# MessageEndVariable class attributes and methods

# sequence_tool_CoveringElementCreationTool class attributes and methods

# CoveredLifelinesVariable class attributes and methods

# sequence_tool_InstanceRoleCreationTool class attributes and methods

# tool_NodeCreationDescription class attributes and methods

# tool_SequenceDiagramToolDescription class attributes and methods

# sequence_ordering_EventEndsOrdering class attributes and methods

# ordering_sequence_SequenceDDiagram class attributes and methods

# sequence_tool_InteractionUseCreationTool class attributes and methods

# EventEnd class attributes and methods

# tool_CoveringElementCreationTool class attributes and methods

# sequence_tool_CombinedFragmentCreationTool class attributes and methods

# sequence_tool_OperandCreationTool class attributes and methods

# sequence_tool_ObservationPointCreationTool class attributes and methods

# sequence_tool_ReorderTool class attributes and methods

# tool_AbstractToolDescription class attributes and methods

# tool_InitialOperation class attributes and methods

# sequence_tool_InstanceRoleReorderTool class attributes and methods

# InstanceRoleMapping class attributes and methods

# sequence_template_TSequenceDiagram class attributes and methods
sequence_template_TSequenceDiagram_domainClass: Property = Property(name="domainClass", type=StringType)
sequence_template_TSequenceDiagram_endsOrdering: Property = Property(name="endsOrdering", type=StringType)
sequence_template_TSequenceDiagram.attributes={sequence_template_TSequenceDiagram_domainClass, sequence_template_TSequenceDiagram_endsOrdering}

# description_RepresentationTemplate class attributes and methods

# template_TTransformer class attributes and methods

# TLifelineMapping class attributes and methods

# TMessageMapping class attributes and methods

# sequence_template_TMessageExtremity class attributes and methods

# sequence_ordering_EventEnd class attributes and methods

# ordering_sequence_EObject class attributes and methods

# sequence_ordering_SingleEventEnd class attributes and methods
sequence_ordering_SingleEventEnd_start: Property = Property(name="start", type=BooleanType)
sequence_ordering_SingleEventEnd.attributes={sequence_ordering_SingleEventEnd_start}

# sequence_ordering_CompoundEventEnd class attributes and methods
sequence_ordering_CompoundEventEnd_m_getSemanticEvents: Method = Method(name="getSemanticEvents", parameters={}, type=StringType)
sequence_ordering_CompoundEventEnd.methods={sequence_ordering_CompoundEventEnd_m_getSemanticEvents}

# SingleEventEnd class attributes and methods

# sequence_ordering_InstanceRolesOrdering class attributes and methods

# sequence_template_TTransformer class attributes and methods

# template_sequence_EObject class attributes and methods

# sequence_template_TAbstractMapping class attributes and methods
sequence_template_TAbstractMapping_name: Property = Property(name="name", type=StringType)
sequence_template_TAbstractMapping_domainClass: Property = Property(name="domainClass", type=StringType)
sequence_template_TAbstractMapping_semanticCandidatesExpression: Property = Property(name="semanticCandidatesExpression", type=StringType)
sequence_template_TAbstractMapping.attributes={sequence_template_TAbstractMapping_domainClass, sequence_template_TAbstractMapping_semanticCandidatesExpression, sequence_template_TAbstractMapping_name}

# TTransformer class attributes and methods

# sequence_template_TExecutionMapping class attributes and methods
sequence_template_TExecutionMapping_startingEndFinderExpression: Property = Property(name="startingEndFinderExpression", type=StringType)
sequence_template_TExecutionMapping_finishingEndFinderExpression: Property = Property(name="finishingEndFinderExpression", type=StringType)
sequence_template_TExecutionMapping_recursive: Property = Property(name="recursive", type=BooleanType)
sequence_template_TExecutionMapping.attributes={sequence_template_TExecutionMapping_recursive, sequence_template_TExecutionMapping_startingEndFinderExpression, sequence_template_TExecutionMapping_finishingEndFinderExpression}

# sequence_template_TLifelineMapping class attributes and methods
sequence_template_TLifelineMapping_eolVisibleExpression: Property = Property(name="eolVisibleExpression", type=StringType)
sequence_template_TLifelineMapping.attributes={sequence_template_TLifelineMapping_eolVisibleExpression}

# template_TAbstractMapping class attributes and methods

# template_TMessageExtremity class attributes and methods

# TExecutionMapping class attributes and methods

# style_NodeStyleDescription class attributes and methods

# TLifelineStyle class attributes and methods

# TConditionalLifelineStyle class attributes and methods

# sequence_template_TLifelineStyle class attributes and methods
sequence_template_TLifelineStyle_lifelineWidthComputationExpression: Property = Property(name="lifelineWidthComputationExpression", type=StringType)
sequence_template_TLifelineStyle.attributes={sequence_template_TLifelineStyle_lifelineWidthComputationExpression}

# ColorDescription class attributes and methods

# sequence_template_TConditionalLifelineStyle class attributes and methods
sequence_template_TConditionalLifelineStyle_predicateExpression: Property = Property(name="predicateExpression", type=StringType)
sequence_template_TConditionalLifelineStyle.attributes={sequence_template_TConditionalLifelineStyle_predicateExpression}

# TConditionalMessageStyle class attributes and methods

# sequence_template_TMessageStyle class attributes and methods
sequence_template_TMessageStyle_lineStyle: Property = Property(name="lineStyle", type=StringType)
sequence_template_TMessageStyle_sourceArrow: Property = Property(name="sourceArrow", type=StringType)
sequence_template_TMessageStyle_targetArrow: Property = Property(name="targetArrow", type=StringType)
sequence_template_TMessageStyle_labelExpression: Property = Property(name="labelExpression", type=StringType)
sequence_template_TMessageStyle.attributes={sequence_template_TMessageStyle_labelExpression, sequence_template_TMessageStyle_targetArrow, sequence_template_TMessageStyle_lineStyle, sequence_template_TMessageStyle_sourceArrow}

# TExecutionStyle class attributes and methods

# TConditionalExecutionStyle class attributes and methods

# sequence_template_TExecutionStyle class attributes and methods
sequence_template_TExecutionStyle_borderSizeComputationExpression: Property = Property(name="borderSizeComputationExpression", type=StringType)
sequence_template_TExecutionStyle.attributes={sequence_template_TExecutionStyle_borderSizeComputationExpression}

# sequence_template_TConditionalExecutionStyle class attributes and methods
sequence_template_TConditionalExecutionStyle_predicateExpression: Property = Property(name="predicateExpression", type=StringType)
sequence_template_TConditionalExecutionStyle.attributes={sequence_template_TConditionalExecutionStyle_predicateExpression}

# sequence_template_TMessageMapping class attributes and methods
sequence_template_TMessageMapping_sendingEndFinderExpression: Property = Property(name="sendingEndFinderExpression", type=StringType)
sequence_template_TMessageMapping_receivingEndFinderExpression: Property = Property(name="receivingEndFinderExpression", type=StringType)
sequence_template_TMessageMapping.attributes={sequence_template_TMessageMapping_sendingEndFinderExpression, sequence_template_TMessageMapping_receivingEndFinderExpression}

# TAbstractMapping class attributes and methods

# TMessageStyle class attributes and methods

# sequence_template_TReturnMessageMapping class attributes and methods
sequence_template_TReturnMessageMapping_invocationMessageFinderExpression: Property = Property(name="invocationMessageFinderExpression", type=StringType)
sequence_template_TReturnMessageMapping.attributes={sequence_template_TReturnMessageMapping_invocationMessageFinderExpression}

# TBasicMessageMapping class attributes and methods

# sequence_template_TCreationMessageMapping class attributes and methods

# sequence_template_TConditionalMessageStyle class attributes and methods
sequence_template_TConditionalMessageStyle_predicateExpression: Property = Property(name="predicateExpression", type=StringType)
sequence_template_TConditionalMessageStyle.attributes={sequence_template_TConditionalMessageStyle_predicateExpression}

# sequence_template_TBasicMessageMapping class attributes and methods

# TSourceTargetMessageMapping class attributes and methods

# TMessageExtremity class attributes and methods

# sequence_template_TSourceTargetMessageMapping class attributes and methods
sequence_template_TSourceTargetMessageMapping_useDomainElement: Property = Property(name="useDomainElement", type=BooleanType)
sequence_template_TSourceTargetMessageMapping_sourceFinderExpression: Property = Property(name="sourceFinderExpression", type=StringType)
sequence_template_TSourceTargetMessageMapping_targetFinderExpression: Property = Property(name="targetFinderExpression", type=StringType)
sequence_template_TSourceTargetMessageMapping.attributes={sequence_template_TSourceTargetMessageMapping_sourceFinderExpression, sequence_template_TSourceTargetMessageMapping_targetFinderExpression, sequence_template_TSourceTargetMessageMapping_useDomainElement}

# sequence_template_TDestructionMessageMapping class attributes and methods

# Relationships
semanticOrdering0: BinaryAssociation = BinaryAssociation(
    name="semanticOrdering0",
    ends={
        Property(name="EventEndsOrdering", type=sequence_SequenceDDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_SequenceDDiagram", type=EventEndsOrdering, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
graphicalOrdering1: BinaryAssociation = BinaryAssociation(
    name="graphicalOrdering1",
    ends={
        Property(name="EventEndsOrdering3", type=sequence_SequenceDDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_SequenceDDiagram2", type=EventEndsOrdering, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instanceRoleSemanticOrdering4: BinaryAssociation = BinaryAssociation(
    name="instanceRoleSemanticOrdering4",
    ends={
        Property(name="InstanceRolesOrdering", type=sequence_SequenceDDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_SequenceDDiagram5", type=InstanceRolesOrdering, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
predecessor11: BinaryAssociation = BinaryAssociation(
    name="predecessor11",
    ends={
        Property(name="tool_ElementVariable", type=sequence_tool_InstanceRoleCreationTool, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_tool_InstanceRoleCreationTool", type=tool_ElementVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
startingEndPredecessor6: BinaryAssociation = BinaryAssociation(
    name="startingEndPredecessor6",
    ends={
        Property(name="MessageEndVariable", type=sequence_tool_OrderedElementCreationTool, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_tool_OrderedElementCreationTool", type=MessageEndVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finishingEndPredecessor7: BinaryAssociation = BinaryAssociation(
    name="finishingEndPredecessor7",
    ends={
        Property(name="MessageEndVariable9", type=sequence_tool_OrderedElementCreationTool, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_tool_OrderedElementCreationTool8", type=MessageEndVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
coveredLifelines10: BinaryAssociation = BinaryAssociation(
    name="coveredLifelines10",
    ends={
        Property(name="CoveredLifelinesVariable", type=sequence_tool_CoveringElementCreationTool, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_tool_CoveringElementCreationTool", type=CoveredLifelinesVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
predecessorBefore28: BinaryAssociation = BinaryAssociation(
    name="predecessorBefore28",
    ends={
        Property(name="tool_ElementVariable30", type=sequence_tool_InstanceRoleReorderTool, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_tool_InstanceRoleReorderTool29", type=tool_ElementVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
predecessorAfter31: BinaryAssociation = BinaryAssociation(
    name="predecessorAfter31",
    ends={
        Property(name="tool_ElementVariable33", type=sequence_tool_InstanceRoleReorderTool, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_tool_InstanceRoleReorderTool32", type=tool_ElementVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instanceRoleMoved34: BinaryAssociation = BinaryAssociation(
    name="instanceRoleMoved34",
    ends={
        Property(name="tool_InitialOperation36", type=sequence_tool_InstanceRoleReorderTool, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_tool_InstanceRoleReorderTool35", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sequenceDiagram37: BinaryAssociation = BinaryAssociation(
    name="sequenceDiagram37",
    ends={
        Property(name="ordering_sequence_SequenceDDiagram", type=sequence_ordering_EventEndsOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_ordering_EventEndsOrdering", type=ordering_sequence_SequenceDDiagram, multiplicity=Multiplicity(0, 1))
    }
)
mappings12: BinaryAssociation = BinaryAssociation(
    name="mappings12",
    ends={
        Property(name="EventMapping", type=sequence_tool_ReorderTool, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_tool_ReorderTool", type=EventMapping, multiplicity=Multiplicity(0, 9999))
    }
)
startingEndPredecessorBefore13: BinaryAssociation = BinaryAssociation(
    name="startingEndPredecessorBefore13",
    ends={
        Property(name="MessageEndVariable15", type=sequence_tool_ReorderTool, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_tool_ReorderTool14", type=MessageEndVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
startingEndPredecessorAfter16: BinaryAssociation = BinaryAssociation(
    name="startingEndPredecessorAfter16",
    ends={
        Property(name="MessageEndVariable18", type=sequence_tool_ReorderTool, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_tool_ReorderTool17", type=MessageEndVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finishingEndPredecessorBefore19: BinaryAssociation = BinaryAssociation(
    name="finishingEndPredecessorBefore19",
    ends={
        Property(name="MessageEndVariable21", type=sequence_tool_ReorderTool, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_tool_ReorderTool20", type=MessageEndVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finishingEndPredecessorAfter22: BinaryAssociation = BinaryAssociation(
    name="finishingEndPredecessorAfter22",
    ends={
        Property(name="MessageEndVariable24", type=sequence_tool_ReorderTool, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_tool_ReorderTool23", type=MessageEndVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
onEventMovedOperation25: BinaryAssociation = BinaryAssociation(
    name="onEventMovedOperation25",
    ends={
        Property(name="tool_InitialOperation", type=sequence_tool_ReorderTool, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_tool_ReorderTool26", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mappings27: BinaryAssociation = BinaryAssociation(
    name="mappings27",
    ends={
        Property(name="InstanceRoleMapping", type=sequence_tool_InstanceRoleReorderTool, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_tool_InstanceRoleReorderTool", type=InstanceRoleMapping, multiplicity=Multiplicity(0, 9999))
    }
)
lifelineMappings47: BinaryAssociation = BinaryAssociation(
    name="lifelineMappings47",
    ends={
        Property(name="TLifelineMapping", type=sequence_template_TSequenceDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TSequenceDiagram", type=TLifelineMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageMappings48: BinaryAssociation = BinaryAssociation(
    name="messageMappings48",
    ends={
        Property(name="TMessageMapping", type=sequence_template_TSequenceDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TSequenceDiagram49", type=TMessageMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventEnds38: BinaryAssociation = BinaryAssociation(
    name="eventEnds38",
    ends={
        Property(name="EventEnd", type=sequence_ordering_EventEndsOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_ordering_EventEndsOrdering39", type=EventEnd, multiplicity=Multiplicity(0, 9999))
    }
)
semanticEnd40: BinaryAssociation = BinaryAssociation(
    name="semanticEnd40",
    ends={
        Property(name="ordering_sequence_EObject", type=sequence_ordering_EventEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_ordering_EventEnd", type=ordering_sequence_EObject, multiplicity=Multiplicity(1, 1))
    }
)
semanticEvent41: BinaryAssociation = BinaryAssociation(
    name="semanticEvent41",
    ends={
        Property(name="ordering_sequence_EObject42", type=sequence_ordering_SingleEventEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_ordering_SingleEventEnd", type=ordering_sequence_EObject, multiplicity=Multiplicity(1, 1))
    }
)
eventEnds43: BinaryAssociation = BinaryAssociation(
    name="eventEnds43",
    ends={
        Property(name="SingleEventEnd", type=sequence_ordering_CompoundEventEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_ordering_CompoundEventEnd", type=SingleEventEnd, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
semanticInstanceRoles44: BinaryAssociation = BinaryAssociation(
    name="semanticInstanceRoles44",
    ends={
        Property(name="ordering_sequence_EObject45", type=sequence_ordering_InstanceRolesOrdering, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_ordering_InstanceRolesOrdering", type=ordering_sequence_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
outputs46: BinaryAssociation = BinaryAssociation(
    name="outputs46",
    ends={
        Property(name="template_sequence_EObject", type=sequence_template_TTransformer, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TTransformer", type=template_sequence_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
style61: BinaryAssociation = BinaryAssociation(
    name="style61",
    ends={
        Property(name="TLifelineStyle62", type=sequence_template_TConditionalLifelineStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TConditionalLifelineStyle", type=TLifelineStyle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
executionMappings63: BinaryAssociation = BinaryAssociation(
    name="executionMappings63",
    ends={
        Property(name="TExecutionMapping64", type=sequence_template_TExecutionMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TExecutionMapping", type=TExecutionMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executionMappings50: BinaryAssociation = BinaryAssociation(
    name="executionMappings50",
    ends={
        Property(name="TExecutionMapping", type=sequence_template_TLifelineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TLifelineMapping", type=TExecutionMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instanceRoleStyle51: BinaryAssociation = BinaryAssociation(
    name="instanceRoleStyle51",
    ends={
        Property(name="style_NodeStyleDescription", type=sequence_template_TLifelineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TLifelineMapping52", type=style_NodeStyleDescription, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lifelineStyle53: BinaryAssociation = BinaryAssociation(
    name="lifelineStyle53",
    ends={
        Property(name="TLifelineStyle", type=sequence_template_TLifelineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TLifelineMapping54", type=TLifelineStyle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
endOfLifeStyle55: BinaryAssociation = BinaryAssociation(
    name="endOfLifeStyle55",
    ends={
        Property(name="style_NodeStyleDescription57", type=sequence_template_TLifelineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TLifelineMapping56", type=style_NodeStyleDescription, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conditionalLifeLineStyles58: BinaryAssociation = BinaryAssociation(
    name="conditionalLifeLineStyles58",
    ends={
        Property(name="TConditionalLifelineStyle", type=sequence_template_TLifelineMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TLifelineMapping59", type=TConditionalLifelineStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lifelineColor60: BinaryAssociation = BinaryAssociation(
    name="lifelineColor60",
    ends={
        Property(name="ColorDescription", type=sequence_template_TLifelineStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TLifelineStyle", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
style76: BinaryAssociation = BinaryAssociation(
    name="style76",
    ends={
        Property(name="sequence_template_TMessageMapping", type=TMessageStyle, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="TMessageStyle", type=sequence_template_TMessageMapping, multiplicity=Multiplicity(1, 1))
    }
)
conditionalStyle77: BinaryAssociation = BinaryAssociation(
    name="conditionalStyle77",
    ends={
        Property(name="TConditionalMessageStyle", type=sequence_template_TMessageMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TMessageMapping78", type=TConditionalMessageStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strokeColor79: BinaryAssociation = BinaryAssociation(
    name="strokeColor79",
    ends={
        Property(name="ColorDescription80", type=sequence_template_TMessageStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TMessageStyle", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
style65: BinaryAssociation = BinaryAssociation(
    name="style65",
    ends={
        Property(name="TExecutionStyle", type=sequence_template_TExecutionMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TExecutionMapping66", type=TExecutionStyle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conditionalStyles67: BinaryAssociation = BinaryAssociation(
    name="conditionalStyles67",
    ends={
        Property(name="TConditionalExecutionStyle", type=sequence_template_TExecutionMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TExecutionMapping68", type=TConditionalExecutionStyle, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borderColor69: BinaryAssociation = BinaryAssociation(
    name="borderColor69",
    ends={
        Property(name="ColorDescription70", type=sequence_template_TExecutionStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TExecutionStyle", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
backgroundColor71: BinaryAssociation = BinaryAssociation(
    name="backgroundColor71",
    ends={
        Property(name="ColorDescription73", type=sequence_template_TExecutionStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TExecutionStyle72", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
style74: BinaryAssociation = BinaryAssociation(
    name="style74",
    ends={
        Property(name="TExecutionStyle75", type=sequence_template_TConditionalExecutionStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TConditionalExecutionStyle", type=TExecutionStyle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
invocationMapping86: BinaryAssociation = BinaryAssociation(
    name="invocationMapping86",
    ends={
        Property(name="TBasicMessageMapping", type=sequence_template_TReturnMessageMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TReturnMessageMapping", type=TBasicMessageMapping, multiplicity=Multiplicity(1, 1))
    }
)
target87: BinaryAssociation = BinaryAssociation(
    name="target87",
    ends={
        Property(name="TLifelineMapping88", type=sequence_template_TCreationMessageMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TCreationMessageMapping", type=TLifelineMapping, multiplicity=Multiplicity(1, 9999))
    }
)
style81: BinaryAssociation = BinaryAssociation(
    name="style81",
    ends={
        Property(name="TMessageStyle82", type=sequence_template_TConditionalMessageStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TConditionalMessageStyle", type=TMessageStyle, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target83: BinaryAssociation = BinaryAssociation(
    name="target83",
    ends={
        Property(name="TMessageExtremity", type=sequence_template_TBasicMessageMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TBasicMessageMapping", type=TMessageExtremity, multiplicity=Multiplicity(1, 9999))
    }
)
source84: BinaryAssociation = BinaryAssociation(
    name="source84",
    ends={
        Property(name="TMessageExtremity85", type=sequence_template_TSourceTargetMessageMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TSourceTargetMessageMapping", type=TMessageExtremity, multiplicity=Multiplicity(1, 9999))
    }
)
target89: BinaryAssociation = BinaryAssociation(
    name="target89",
    ends={
        Property(name="TLifelineMapping90", type=sequence_template_TDestructionMessageMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="sequence_template_TDestructionMessageMapping", type=TLifelineMapping, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_sequence_SequenceDDiagram_DSemanticDiagram = Generalization(general=DSemanticDiagram, specific=sequence_SequenceDDiagram)
gen_sequence_description_BasicMessageMapping_MessageMapping = Generalization(general=MessageMapping, specific=sequence_description_BasicMessageMapping)
gen_sequence_description_ReturnMessageMapping_MessageMapping = Generalization(general=MessageMapping, specific=sequence_description_ReturnMessageMapping)
gen_sequence_description_CreationMessageMapping_MessageMapping = Generalization(general=MessageMapping, specific=sequence_description_CreationMessageMapping)
gen_sequence_description_DestructionMessageMapping_MessageMapping = Generalization(general=MessageMapping, specific=sequence_description_DestructionMessageMapping)
gen_sequence_description_MessageEndVariable_AbstractVariable = Generalization(general=AbstractVariable, specific=sequence_description_MessageEndVariable)
gen_sequence_description_SequenceDiagramDescription_DiagramDescription = Generalization(general=DiagramDescription, specific=sequence_description_SequenceDiagramDescription)
gen_sequence_description_InstanceRoleMapping_NodeMapping = Generalization(general=NodeMapping, specific=sequence_description_InstanceRoleMapping)
gen_sequence_description_DelimitedEventMapping_EventMapping = Generalization(general=EventMapping, specific=sequence_description_DelimitedEventMapping)
gen_sequence_description_ExecutionMapping_description_NodeMapping = Generalization(general=description_NodeMapping, specific=sequence_description_ExecutionMapping)
gen_sequence_description_ExecutionMapping_description_DelimitedEventMapping = Generalization(general=description_DelimitedEventMapping, specific=sequence_description_ExecutionMapping)
gen_sequence_description_StateMapping_description_NodeMapping = Generalization(general=description_NodeMapping, specific=sequence_description_StateMapping)
gen_sequence_description_StateMapping_description_DelimitedEventMapping = Generalization(general=description_DelimitedEventMapping, specific=sequence_description_StateMapping)
gen_sequence_description_EndOfLifeMapping_NodeMapping = Generalization(general=NodeMapping, specific=sequence_description_EndOfLifeMapping)
gen_sequence_description_MessageMapping_description_EdgeMapping = Generalization(general=description_EdgeMapping, specific=sequence_description_MessageMapping)
gen_sequence_description_MessageMapping_description_EventMapping = Generalization(general=description_EventMapping, specific=sequence_description_MessageMapping)
gen_sequence_tool_LifelineCreationTool_tool_ContainerCreationDescription = Generalization(general=tool_ContainerCreationDescription, specific=sequence_tool_LifelineCreationTool)
gen_sequence_tool_LifelineCreationTool_tool_SequenceDiagramToolDescription = Generalization(general=tool_SequenceDiagramToolDescription, specific=sequence_tool_LifelineCreationTool)
gen_sequence_tool_MessageCreationTool_tool_SequenceDiagramToolDescription = Generalization(general=tool_SequenceDiagramToolDescription, specific=sequence_tool_MessageCreationTool)
gen_sequence_tool_MessageCreationTool_tool_EdgeCreationDescription = Generalization(general=tool_EdgeCreationDescription, specific=sequence_tool_MessageCreationTool)
gen_sequence_tool_MessageCreationTool_tool_OrderedElementCreationTool = Generalization(general=tool_OrderedElementCreationTool, specific=sequence_tool_MessageCreationTool)
gen_sequence_tool_ExecutionCreationTool_tool_NodeCreationDescription = Generalization(general=tool_NodeCreationDescription, specific=sequence_tool_ExecutionCreationTool)
gen_sequence_tool_ExecutionCreationTool_tool_SequenceDiagramToolDescription = Generalization(general=tool_SequenceDiagramToolDescription, specific=sequence_tool_ExecutionCreationTool)
gen_sequence_tool_ExecutionCreationTool_tool_OrderedElementCreationTool = Generalization(general=tool_OrderedElementCreationTool, specific=sequence_tool_ExecutionCreationTool)
gen_sequence_tool_StateCreationTool_tool_NodeCreationDescription = Generalization(general=tool_NodeCreationDescription, specific=sequence_tool_StateCreationTool)
gen_sequence_tool_StateCreationTool_tool_SequenceDiagramToolDescription = Generalization(general=tool_SequenceDiagramToolDescription, specific=sequence_tool_StateCreationTool)
gen_sequence_tool_StateCreationTool_tool_OrderedElementCreationTool = Generalization(general=tool_OrderedElementCreationTool, specific=sequence_tool_StateCreationTool)
gen_sequence_description_CoveredLifelinesVariable_AbstractVariable = Generalization(general=AbstractVariable, specific=sequence_description_CoveredLifelinesVariable)
gen_sequence_description_FrameMapping_description_ContainerMapping = Generalization(general=description_ContainerMapping, specific=sequence_description_FrameMapping)
gen_sequence_description_FrameMapping_description_DelimitedEventMapping = Generalization(general=description_DelimitedEventMapping, specific=sequence_description_FrameMapping)
gen_sequence_description_InteractionUseMapping_FrameMapping = Generalization(general=FrameMapping, specific=sequence_description_InteractionUseMapping)
gen_sequence_description_CombinedFragmentMapping_FrameMapping = Generalization(general=FrameMapping, specific=sequence_description_CombinedFragmentMapping)
gen_sequence_description_OperandMapping_description_ContainerMapping = Generalization(general=description_ContainerMapping, specific=sequence_description_OperandMapping)
gen_sequence_description_OperandMapping_description_DelimitedEventMapping = Generalization(general=description_DelimitedEventMapping, specific=sequence_description_OperandMapping)
gen_sequence_description_ObservationPointMapping_NodeMapping = Generalization(general=NodeMapping, specific=sequence_description_ObservationPointMapping)
gen_sequence_tool_InstanceRoleCreationTool_tool_NodeCreationDescription = Generalization(general=tool_NodeCreationDescription, specific=sequence_tool_InstanceRoleCreationTool)
gen_sequence_tool_InstanceRoleCreationTool_tool_SequenceDiagramToolDescription = Generalization(general=tool_SequenceDiagramToolDescription, specific=sequence_tool_InstanceRoleCreationTool)
gen_sequence_tool_InteractionUseCreationTool_tool_ContainerCreationDescription = Generalization(general=tool_ContainerCreationDescription, specific=sequence_tool_InteractionUseCreationTool)
gen_sequence_tool_InteractionUseCreationTool_tool_SequenceDiagramToolDescription = Generalization(general=tool_SequenceDiagramToolDescription, specific=sequence_tool_InteractionUseCreationTool)
gen_sequence_tool_InteractionUseCreationTool_tool_OrderedElementCreationTool = Generalization(general=tool_OrderedElementCreationTool, specific=sequence_tool_InteractionUseCreationTool)
gen_sequence_tool_InteractionUseCreationTool_tool_CoveringElementCreationTool = Generalization(general=tool_CoveringElementCreationTool, specific=sequence_tool_InteractionUseCreationTool)
gen_sequence_tool_CombinedFragmentCreationTool_tool_ContainerCreationDescription = Generalization(general=tool_ContainerCreationDescription, specific=sequence_tool_CombinedFragmentCreationTool)
gen_sequence_tool_CombinedFragmentCreationTool_tool_SequenceDiagramToolDescription = Generalization(general=tool_SequenceDiagramToolDescription, specific=sequence_tool_CombinedFragmentCreationTool)
gen_sequence_tool_CombinedFragmentCreationTool_tool_OrderedElementCreationTool = Generalization(general=tool_OrderedElementCreationTool, specific=sequence_tool_CombinedFragmentCreationTool)
gen_sequence_tool_CombinedFragmentCreationTool_tool_CoveringElementCreationTool = Generalization(general=tool_CoveringElementCreationTool, specific=sequence_tool_CombinedFragmentCreationTool)
gen_sequence_tool_OperandCreationTool_tool_ContainerCreationDescription = Generalization(general=tool_ContainerCreationDescription, specific=sequence_tool_OperandCreationTool)
gen_sequence_tool_OperandCreationTool_tool_SequenceDiagramToolDescription = Generalization(general=tool_SequenceDiagramToolDescription, specific=sequence_tool_OperandCreationTool)
gen_sequence_tool_OperandCreationTool_tool_OrderedElementCreationTool = Generalization(general=tool_OrderedElementCreationTool, specific=sequence_tool_OperandCreationTool)
gen_sequence_tool_ObservationPointCreationTool_tool_NodeCreationDescription = Generalization(general=tool_NodeCreationDescription, specific=sequence_tool_ObservationPointCreationTool)
gen_sequence_tool_ObservationPointCreationTool_tool_SequenceDiagramToolDescription = Generalization(general=tool_SequenceDiagramToolDescription, specific=sequence_tool_ObservationPointCreationTool)
gen_sequence_tool_ObservationPointCreationTool_tool_OrderedElementCreationTool = Generalization(general=tool_OrderedElementCreationTool, specific=sequence_tool_ObservationPointCreationTool)
gen_sequence_tool_ReorderTool_tool_AbstractToolDescription = Generalization(general=tool_AbstractToolDescription, specific=sequence_tool_ReorderTool)
gen_sequence_tool_ReorderTool_tool_SequenceDiagramToolDescription = Generalization(general=tool_SequenceDiagramToolDescription, specific=sequence_tool_ReorderTool)
gen_sequence_tool_InstanceRoleReorderTool_tool_AbstractToolDescription = Generalization(general=tool_AbstractToolDescription, specific=sequence_tool_InstanceRoleReorderTool)
gen_sequence_tool_InstanceRoleReorderTool_tool_SequenceDiagramToolDescription = Generalization(general=tool_SequenceDiagramToolDescription, specific=sequence_tool_InstanceRoleReorderTool)
gen_sequence_template_TSequenceDiagram_description_RepresentationTemplate = Generalization(general=description_RepresentationTemplate, specific=sequence_template_TSequenceDiagram)
gen_sequence_template_TSequenceDiagram_template_TTransformer = Generalization(general=template_TTransformer, specific=sequence_template_TSequenceDiagram)
gen_sequence_ordering_SingleEventEnd_EventEnd = Generalization(general=EventEnd, specific=sequence_ordering_SingleEventEnd)
gen_sequence_ordering_CompoundEventEnd_EventEnd = Generalization(general=EventEnd, specific=sequence_ordering_CompoundEventEnd)
gen_sequence_template_TAbstractMapping_TTransformer = Generalization(general=TTransformer, specific=sequence_template_TAbstractMapping)
gen_sequence_template_TExecutionMapping_template_TAbstractMapping = Generalization(general=template_TAbstractMapping, specific=sequence_template_TExecutionMapping)
gen_sequence_template_TExecutionMapping_template_TMessageExtremity = Generalization(general=template_TMessageExtremity, specific=sequence_template_TExecutionMapping)
gen_sequence_template_TLifelineMapping_template_TAbstractMapping = Generalization(general=template_TAbstractMapping, specific=sequence_template_TLifelineMapping)
gen_sequence_template_TLifelineMapping_template_TMessageExtremity = Generalization(general=template_TMessageExtremity, specific=sequence_template_TLifelineMapping)
gen_sequence_template_TLifelineStyle_TTransformer = Generalization(general=TTransformer, specific=sequence_template_TLifelineStyle)
gen_sequence_template_TConditionalLifelineStyle_TTransformer = Generalization(general=TTransformer, specific=sequence_template_TConditionalLifelineStyle)
gen_sequence_template_TMessageStyle_TTransformer = Generalization(general=TTransformer, specific=sequence_template_TMessageStyle)
gen_sequence_template_TExecutionStyle_TTransformer = Generalization(general=TTransformer, specific=sequence_template_TExecutionStyle)
gen_sequence_template_TConditionalExecutionStyle_TTransformer = Generalization(general=TTransformer, specific=sequence_template_TConditionalExecutionStyle)
gen_sequence_template_TMessageMapping_TAbstractMapping = Generalization(general=TAbstractMapping, specific=sequence_template_TMessageMapping)
gen_sequence_template_TReturnMessageMapping_TMessageMapping = Generalization(general=TMessageMapping, specific=sequence_template_TReturnMessageMapping)
gen_sequence_template_TCreationMessageMapping_TSourceTargetMessageMapping = Generalization(general=TSourceTargetMessageMapping, specific=sequence_template_TCreationMessageMapping)
gen_sequence_template_TConditionalMessageStyle_TTransformer = Generalization(general=TTransformer, specific=sequence_template_TConditionalMessageStyle)
gen_sequence_template_TBasicMessageMapping_TSourceTargetMessageMapping = Generalization(general=TSourceTargetMessageMapping, specific=sequence_template_TBasicMessageMapping)
gen_sequence_template_TSourceTargetMessageMapping_TMessageMapping = Generalization(general=TMessageMapping, specific=sequence_template_TSourceTargetMessageMapping)
gen_sequence_template_TDestructionMessageMapping_TSourceTargetMessageMapping = Generalization(general=TSourceTargetMessageMapping, specific=sequence_template_TDestructionMessageMapping)

# Domain Model
domain_model = DomainModel(
    name="sequence",
    types={sequence_SequenceDDiagram, DSemanticDiagram, EventEndsOrdering, sequence_description_BasicMessageMapping, MessageMapping, sequence_description_ReturnMessageMapping, sequence_description_CreationMessageMapping, sequence_description_DestructionMessageMapping, sequence_description_MessageEndVariable, AbstractVariable, InstanceRolesOrdering, sequence_description_SequenceDiagramDescription, DiagramDescription, sequence_description_InstanceRoleMapping, NodeMapping, sequence_description_EventMapping, sequence_description_DelimitedEventMapping, EventMapping, sequence_description_ExecutionMapping, description_NodeMapping, description_DelimitedEventMapping, sequence_description_StateMapping, sequence_description_EndOfLifeMapping, sequence_description_MessageMapping, description_EdgeMapping, description_EventMapping, tool_ElementVariable, sequence_tool_LifelineCreationTool, tool_ContainerCreationDescription, sequence_tool_MessageCreationTool, tool_EdgeCreationDescription, tool_OrderedElementCreationTool, sequence_tool_ExecutionCreationTool, sequence_tool_StateCreationTool, sequence_description_CoveredLifelinesVariable, sequence_description_FrameMapping, description_ContainerMapping, sequence_description_InteractionUseMapping, FrameMapping, sequence_description_CombinedFragmentMapping, sequence_description_OperandMapping, sequence_description_ObservationPointMapping, sequence_tool_SequenceDiagramToolDescription, sequence_tool_OrderedElementCreationTool, MessageEndVariable, sequence_tool_CoveringElementCreationTool, CoveredLifelinesVariable, sequence_tool_InstanceRoleCreationTool, tool_NodeCreationDescription, tool_SequenceDiagramToolDescription, sequence_ordering_EventEndsOrdering, ordering_sequence_SequenceDDiagram, sequence_tool_InteractionUseCreationTool, EventEnd, tool_CoveringElementCreationTool, sequence_tool_CombinedFragmentCreationTool, sequence_tool_OperandCreationTool, sequence_tool_ObservationPointCreationTool, sequence_tool_ReorderTool, tool_AbstractToolDescription, tool_InitialOperation, sequence_tool_InstanceRoleReorderTool, InstanceRoleMapping, sequence_template_TSequenceDiagram, description_RepresentationTemplate, template_TTransformer, TLifelineMapping, TMessageMapping, sequence_template_TMessageExtremity, sequence_ordering_EventEnd, ordering_sequence_EObject, sequence_ordering_SingleEventEnd, sequence_ordering_CompoundEventEnd, SingleEventEnd, sequence_ordering_InstanceRolesOrdering, sequence_template_TTransformer, template_sequence_EObject, sequence_template_TAbstractMapping, TTransformer, sequence_template_TExecutionMapping, sequence_template_TLifelineMapping, template_TAbstractMapping, template_TMessageExtremity, TExecutionMapping, style_NodeStyleDescription, TLifelineStyle, TConditionalLifelineStyle, sequence_template_TLifelineStyle, ColorDescription, sequence_template_TConditionalLifelineStyle, TConditionalMessageStyle, sequence_template_TMessageStyle, TExecutionStyle, TConditionalExecutionStyle, sequence_template_TExecutionStyle, sequence_template_TConditionalExecutionStyle, sequence_template_TMessageMapping, TAbstractMapping, TMessageStyle, sequence_template_TReturnMessageMapping, TBasicMessageMapping, sequence_template_TCreationMessageMapping, sequence_template_TConditionalMessageStyle, sequence_template_TBasicMessageMapping, TSourceTargetMessageMapping, TMessageExtremity, sequence_template_TSourceTargetMessageMapping, sequence_template_TDestructionMessageMapping},
    associations={semanticOrdering0, graphicalOrdering1, instanceRoleSemanticOrdering4, predecessor11, startingEndPredecessor6, finishingEndPredecessor7, coveredLifelines10, predecessorBefore28, predecessorAfter31, instanceRoleMoved34, sequenceDiagram37, mappings12, startingEndPredecessorBefore13, startingEndPredecessorAfter16, finishingEndPredecessorBefore19, finishingEndPredecessorAfter22, onEventMovedOperation25, mappings27, lifelineMappings47, messageMappings48, eventEnds38, semanticEnd40, semanticEvent41, eventEnds43, semanticInstanceRoles44, outputs46, style61, executionMappings63, executionMappings50, instanceRoleStyle51, lifelineStyle53, endOfLifeStyle55, conditionalLifeLineStyles58, lifelineColor60, style76, conditionalStyle77, strokeColor79, style65, conditionalStyles67, borderColor69, backgroundColor71, style74, invocationMapping86, target87, style81, target83, source84, target89},
    generalizations={gen_sequence_SequenceDDiagram_DSemanticDiagram, gen_sequence_description_BasicMessageMapping_MessageMapping, gen_sequence_description_ReturnMessageMapping_MessageMapping, gen_sequence_description_CreationMessageMapping_MessageMapping, gen_sequence_description_DestructionMessageMapping_MessageMapping, gen_sequence_description_MessageEndVariable_AbstractVariable, gen_sequence_description_SequenceDiagramDescription_DiagramDescription, gen_sequence_description_InstanceRoleMapping_NodeMapping, gen_sequence_description_DelimitedEventMapping_EventMapping, gen_sequence_description_ExecutionMapping_description_NodeMapping, gen_sequence_description_ExecutionMapping_description_DelimitedEventMapping, gen_sequence_description_StateMapping_description_NodeMapping, gen_sequence_description_StateMapping_description_DelimitedEventMapping, gen_sequence_description_EndOfLifeMapping_NodeMapping, gen_sequence_description_MessageMapping_description_EdgeMapping, gen_sequence_description_MessageMapping_description_EventMapping, gen_sequence_tool_LifelineCreationTool_tool_ContainerCreationDescription, gen_sequence_tool_LifelineCreationTool_tool_SequenceDiagramToolDescription, gen_sequence_tool_MessageCreationTool_tool_SequenceDiagramToolDescription, gen_sequence_tool_MessageCreationTool_tool_EdgeCreationDescription, gen_sequence_tool_MessageCreationTool_tool_OrderedElementCreationTool, gen_sequence_tool_ExecutionCreationTool_tool_NodeCreationDescription, gen_sequence_tool_ExecutionCreationTool_tool_SequenceDiagramToolDescription, gen_sequence_tool_ExecutionCreationTool_tool_OrderedElementCreationTool, gen_sequence_tool_StateCreationTool_tool_NodeCreationDescription, gen_sequence_tool_StateCreationTool_tool_SequenceDiagramToolDescription, gen_sequence_tool_StateCreationTool_tool_OrderedElementCreationTool, gen_sequence_description_CoveredLifelinesVariable_AbstractVariable, gen_sequence_description_FrameMapping_description_ContainerMapping, gen_sequence_description_FrameMapping_description_DelimitedEventMapping, gen_sequence_description_InteractionUseMapping_FrameMapping, gen_sequence_description_CombinedFragmentMapping_FrameMapping, gen_sequence_description_OperandMapping_description_ContainerMapping, gen_sequence_description_OperandMapping_description_DelimitedEventMapping, gen_sequence_description_ObservationPointMapping_NodeMapping, gen_sequence_tool_InstanceRoleCreationTool_tool_NodeCreationDescription, gen_sequence_tool_InstanceRoleCreationTool_tool_SequenceDiagramToolDescription, gen_sequence_tool_InteractionUseCreationTool_tool_ContainerCreationDescription, gen_sequence_tool_InteractionUseCreationTool_tool_SequenceDiagramToolDescription, gen_sequence_tool_InteractionUseCreationTool_tool_OrderedElementCreationTool, gen_sequence_tool_InteractionUseCreationTool_tool_CoveringElementCreationTool, gen_sequence_tool_CombinedFragmentCreationTool_tool_ContainerCreationDescription, gen_sequence_tool_CombinedFragmentCreationTool_tool_SequenceDiagramToolDescription, gen_sequence_tool_CombinedFragmentCreationTool_tool_OrderedElementCreationTool, gen_sequence_tool_CombinedFragmentCreationTool_tool_CoveringElementCreationTool, gen_sequence_tool_OperandCreationTool_tool_ContainerCreationDescription, gen_sequence_tool_OperandCreationTool_tool_SequenceDiagramToolDescription, gen_sequence_tool_OperandCreationTool_tool_OrderedElementCreationTool, gen_sequence_tool_ObservationPointCreationTool_tool_NodeCreationDescription, gen_sequence_tool_ObservationPointCreationTool_tool_SequenceDiagramToolDescription, gen_sequence_tool_ObservationPointCreationTool_tool_OrderedElementCreationTool, gen_sequence_tool_ReorderTool_tool_AbstractToolDescription, gen_sequence_tool_ReorderTool_tool_SequenceDiagramToolDescription, gen_sequence_tool_InstanceRoleReorderTool_tool_AbstractToolDescription, gen_sequence_tool_InstanceRoleReorderTool_tool_SequenceDiagramToolDescription, gen_sequence_template_TSequenceDiagram_description_RepresentationTemplate, gen_sequence_template_TSequenceDiagram_template_TTransformer, gen_sequence_ordering_SingleEventEnd_EventEnd, gen_sequence_ordering_CompoundEventEnd_EventEnd, gen_sequence_template_TAbstractMapping_TTransformer, gen_sequence_template_TExecutionMapping_template_TAbstractMapping, gen_sequence_template_TExecutionMapping_template_TMessageExtremity, gen_sequence_template_TLifelineMapping_template_TAbstractMapping, gen_sequence_template_TLifelineMapping_template_TMessageExtremity, gen_sequence_template_TLifelineStyle_TTransformer, gen_sequence_template_TConditionalLifelineStyle_TTransformer, gen_sequence_template_TMessageStyle_TTransformer, gen_sequence_template_TExecutionStyle_TTransformer, gen_sequence_template_TConditionalExecutionStyle_TTransformer, gen_sequence_template_TMessageMapping_TAbstractMapping, gen_sequence_template_TReturnMessageMapping_TMessageMapping, gen_sequence_template_TCreationMessageMapping_TSourceTargetMessageMapping, gen_sequence_template_TConditionalMessageStyle_TTransformer, gen_sequence_template_TBasicMessageMapping_TSourceTargetMessageMapping, gen_sequence_template_TSourceTargetMessageMapping_TMessageMapping, gen_sequence_template_TDestructionMessageMapping_TSourceTargetMessageMapping},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
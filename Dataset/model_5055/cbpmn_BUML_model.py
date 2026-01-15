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
ActivityType: Enumeration = Enumeration(
    name="ActivityType",
    literals={
            EnumerationLiteral(name="MANUAL"),
			EnumerationLiteral(name="RECEIVE"),
			EnumerationLiteral(name="SEND"),
			EnumerationLiteral(name="SERVICE"),
			EnumerationLiteral(name="USER"),
			EnumerationLiteral(name="BUSINESSRULE")
    }
)

EventType: Enumeration = Enumeration(
    name="EventType",
    literals={
            EnumerationLiteral(name="EEnumLiteral0")
    }
)

DecisionType: Enumeration = Enumeration(
    name="DecisionType",
    literals={
            EnumerationLiteral(name="EXCLUSIVE"),
			EnumerationLiteral(name="INCLUSIVE")
    }
)

DataObjectType: Enumeration = Enumeration(
    name="DataObjectType",
    literals={
            EnumerationLiteral(name="PHYSICAL"),
			EnumerationLiteral(name="INFORMATIONAL")
    }
)

FlowNodeInstanceStatus: Enumeration = Enumeration(
    name="FlowNodeInstanceStatus",
    literals={
            EnumerationLiteral(name="INIT"),
			EnumerationLiteral(name="STARTED"),
			EnumerationLiteral(name="INTERRUPTED"),
			EnumerationLiteral(name="SUCCESS"),
			EnumerationLiteral(name="FAILED")
    }
)

GatewayType: Enumeration = Enumeration(
    name="GatewayType",
    literals={
            EnumerationLiteral(name="SPLIT"),
			EnumerationLiteral(name="JOIN")
    }
)

# Classes
cbpmn_ProcessModel = Class(name="cbpmn::ProcessModel")
cbpmn_Branch = Class(name="cbpmn::Branch")
cbpmn_OCLConstraint = Class(name="cbpmn::OCLConstraint")
cbpmn_Activity = Class(name="cbpmn::Activity")
FlowNode = Class(name="FlowNode")
cbpmn_DataObjectReference = Class(name="cbpmn::DataObjectReference")
cbpmn_FlowNode = Class(name="cbpmn::FlowNode", is_abstract=True)
cbpmn_DecisionGateway = Class(name="cbpmn::DecisionGateway")
SplitGateway = Class(name="SplitGateway")
cbpmn_Event = Class(name="cbpmn::Event", is_abstract=True)
cbpmn_ParallelGateway = Class(name="cbpmn::ParallelGateway")
cbpmn_SplitGateway = Class(name="cbpmn::SplitGateway", is_abstract=True)
cbpmn_EClass = Class(name="cbpmn::EClass")
cbpmn_ProcessInstance = Class(name="cbpmn::ProcessInstance")
cbpmn_FlowNodeInstance = Class(name="cbpmn::FlowNodeInstance")
cbpmn_EObject = Class(name="cbpmn::EObject")
cbpmn_DataObject = Class(name="cbpmn::DataObject")
EObject = Class(name="EObject")
cbpmn_StartEvent = Class(name="cbpmn::StartEvent")
Event = Class(name="Event")
cbpmn_EndEvent = Class(name="cbpmn::EndEvent")
cbpmn_IntermediateEvent = Class(name="cbpmn::IntermediateEvent")

# cbpmn_ProcessModel class attributes and methods
cbpmn_ProcessModel_name: Property = Property(name="name", type=StringType)
cbpmn_ProcessModel_m_iterator: Method = Method(name="iterator", parameters={Parameter(name='iterator')}, type=StringType)
cbpmn_ProcessModel_m_iterator: Method = Method(name="iterator", parameters={Parameter(name='iterator'), Parameter(name='start')}, type=StringType)
cbpmn_ProcessModel_m_getRandomStartEvent: Method = Method(name="getRandomStartEvent", parameters={}, type=StringType)
cbpmn_ProcessModel.attributes={cbpmn_ProcessModel_name}
cbpmn_ProcessModel.methods={cbpmn_ProcessModel_m_iterator, cbpmn_ProcessModel_m_getRandomStartEvent, cbpmn_ProcessModel_m_iterator}

# cbpmn_Branch class attributes and methods
cbpmn_Branch_default: Property = Property(name="default", type=BooleanType)
cbpmn_Branch_m_getFirstNode: Method = Method(name="getFirstNode", parameters={}, type=FlowNode)
cbpmn_Branch_m_getLastNode: Method = Method(name="getLastNode", parameters={}, type=FlowNode)
cbpmn_Branch.attributes={cbpmn_Branch_default}
cbpmn_Branch.methods={cbpmn_Branch_m_getFirstNode, cbpmn_Branch_m_getLastNode}

# cbpmn_OCLConstraint class attributes and methods
cbpmn_OCLConstraint_constraintName: Property = Property(name="constraintName", type=StringType)
cbpmn_OCLConstraint_constraintStr: Property = Property(name="constraintStr", type=StringType)
cbpmn_OCLConstraint.attributes={cbpmn_OCLConstraint_constraintStr, cbpmn_OCLConstraint_constraintName}

# cbpmn_Activity class attributes and methods
cbpmn_Activity_type: Property = Property(name="type", type=StringType)
cbpmn_Activity.attributes={cbpmn_Activity_type}

# FlowNode class attributes and methods

# cbpmn_DataObjectReference class attributes and methods
cbpmn_DataObjectReference_name: Property = Property(name="name", type=StringType)
cbpmn_DataObjectReference_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
cbpmn_DataObjectReference_higherBound: Property = Property(name="higherBound", type=IntegerType)
cbpmn_DataObjectReference.attributes={cbpmn_DataObjectReference_higherBound, cbpmn_DataObjectReference_lowerBound, cbpmn_DataObjectReference_name}

# cbpmn_FlowNode class attributes and methods
cbpmn_FlowNode_name: Property = Property(name="name", type=StringType)
cbpmn_FlowNode.attributes={cbpmn_FlowNode_name}

# cbpmn_DecisionGateway class attributes and methods
cbpmn_DecisionGateway_type: Property = Property(name="type", type=StringType)
cbpmn_DecisionGateway_m_addBranchWithCondition: Method = Method(name="addBranchWithCondition", parameters={Parameter(name='default'), Parameter(name='condition'), Parameter(name='branch')})
cbpmn_DecisionGateway_m_getDefaultBranch: Method = Method(name="getDefaultBranch", parameters={}, type=StringType)
cbpmn_DecisionGateway_m_getRandomBranch: Method = Method(name="getRandomBranch", parameters={}, type=StringType)
cbpmn_DecisionGateway.attributes={cbpmn_DecisionGateway_type}
cbpmn_DecisionGateway.methods={cbpmn_DecisionGateway_m_getDefaultBranch, cbpmn_DecisionGateway_m_addBranchWithCondition, cbpmn_DecisionGateway_m_getRandomBranch}

# SplitGateway class attributes and methods

# cbpmn_Event class attributes and methods

# cbpmn_ParallelGateway class attributes and methods

# cbpmn_SplitGateway class attributes and methods

# cbpmn_EClass class attributes and methods

# cbpmn_ProcessInstance class attributes and methods
cbpmn_ProcessInstance_id: Property = Property(name="id", type=StringType)
cbpmn_ProcessInstance.attributes={cbpmn_ProcessInstance_id}

# cbpmn_FlowNodeInstance class attributes and methods
cbpmn_FlowNodeInstance_status: Property = Property(name="status", type=StringType)
cbpmn_FlowNodeInstance.attributes={cbpmn_FlowNodeInstance_status}

# cbpmn_EObject class attributes and methods

# cbpmn_DataObject class attributes and methods

# EObject class attributes and methods

# cbpmn_StartEvent class attributes and methods

# Event class attributes and methods

# cbpmn_EndEvent class attributes and methods

# cbpmn_IntermediateEvent class attributes and methods

# Relationships
mainBranch0: BinaryAssociation = BinaryAssociation(
    name="mainBranch0",
    ends={
        Property(name="cbpmn_Branch", type=cbpmn_ProcessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_ProcessModel", type=cbpmn_Branch, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
processInvariants1: BinaryAssociation = BinaryAssociation(
    name="processInvariants1",
    ends={
        Property(name="cbpmn_OCLConstraint", type=cbpmn_ProcessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_ProcessModel2", type=cbpmn_OCLConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preConditions3: BinaryAssociation = BinaryAssociation(
    name="preConditions3",
    ends={
        Property(name="cbpmn_OCLConstraint4", type=cbpmn_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_Activity", type=cbpmn_OCLConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postConditions5: BinaryAssociation = BinaryAssociation(
    name="postConditions5",
    ends={
        Property(name="cbpmn_OCLConstraint7", type=cbpmn_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_Activity6", type=cbpmn_OCLConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs8: BinaryAssociation = BinaryAssociation(
    name="outputs8",
    ends={
        Property(name="cbpmn_DataObjectReference", type=cbpmn_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_Activity9", type=cbpmn_DataObjectReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invariabilityClauses10: BinaryAssociation = BinaryAssociation(
    name="invariabilityClauses10",
    ends={
        Property(name="cbpmn_OCLConstraint12", type=cbpmn_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_Activity11", type=cbpmn_OCLConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes13: BinaryAssociation = BinaryAssociation(
    name="nodes13",
    ends={
        Property(name="FlowNode", type=cbpmn_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branch", type=cbpmn_FlowNode, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
branch17: BinaryAssociation = BinaryAssociation(
    name="branch17",
    ends={
        Property(name="Branch", type=cbpmn_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=cbpmn_Branch, multiplicity=Multiplicity(0, 1))
    }
)
next19: BinaryAssociation = BinaryAssociation(
    name="next19",
    ends={
        Property(name="FlowNode20", type=cbpmn_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="previous", type=cbpmn_FlowNode, multiplicity=Multiplicity(0, 1))
    }
)
previous22: BinaryAssociation = BinaryAssociation(
    name="previous22",
    ends={
        Property(name="FlowNode23", type=cbpmn_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="next", type=cbpmn_FlowNode, multiplicity=Multiplicity(0, 1))
    }
)
inputs24: BinaryAssociation = BinaryAssociation(
    name="inputs24",
    ends={
        Property(name="cbpmn_DataObjectReference25", type=cbpmn_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_FlowNode", type=cbpmn_DataObjectReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branch26: BinaryAssociation = BinaryAssociation(
    name="branch26",
    ends={
        Property(name="Branch27", type=cbpmn_OCLConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="entryConditions", type=cbpmn_Branch, multiplicity=Multiplicity(0, 1))
    }
)
trigger28: BinaryAssociation = BinaryAssociation(
    name="trigger28",
    ends={
        Property(name="cbpmn_OCLConstraint29", type=cbpmn_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_Event", type=cbpmn_OCLConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entryConditions14: BinaryAssociation = BinaryAssociation(
    name="entryConditions14",
    ends={
        Property(name="OCLConstraint", type=cbpmn_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branch15", type=cbpmn_OCLConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gateway16: BinaryAssociation = BinaryAssociation(
    name="gateway16",
    ends={
        Property(name="SplitGateway", type=cbpmn_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branches", type=cbpmn_SplitGateway, multiplicity=Multiplicity(0, 1))
    }
)
dataObjectClass32: BinaryAssociation = BinaryAssociation(
    name="dataObjectClass32",
    ends={
        Property(name="cbpmn_EClass", type=cbpmn_DataObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_DataObjectReference33", type=cbpmn_EClass, multiplicity=Multiplicity(1, 1))
    }
)
processModel34: BinaryAssociation = BinaryAssociation(
    name="processModel34",
    ends={
        Property(name="cbpmn_ProcessModel35", type=cbpmn_ProcessInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_ProcessInstance", type=cbpmn_ProcessModel, multiplicity=Multiplicity(1, 1))
    }
)
executedNodes36: BinaryAssociation = BinaryAssociation(
    name="executedNodes36",
    ends={
        Property(name="FlowNodeInstance", type=cbpmn_ProcessInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="processInstance", type=cbpmn_FlowNodeInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataObjects37: BinaryAssociation = BinaryAssociation(
    name="dataObjects37",
    ends={
        Property(name="cbpmn_EObject", type=cbpmn_ProcessInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_ProcessInstance38", type=cbpmn_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeDef39: BinaryAssociation = BinaryAssociation(
    name="nodeDef39",
    ends={
        Property(name="cbpmn_FlowNode40", type=cbpmn_FlowNodeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_FlowNodeInstance", type=cbpmn_FlowNode, multiplicity=Multiplicity(1, 1))
    }
)
inputs41: BinaryAssociation = BinaryAssociation(
    name="inputs41",
    ends={
        Property(name="cbpmn_EObject43", type=cbpmn_FlowNodeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_FlowNodeInstance42", type=cbpmn_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
outputs44: BinaryAssociation = BinaryAssociation(
    name="outputs44",
    ends={
        Property(name="cbpmn_EObject46", type=cbpmn_FlowNodeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_FlowNodeInstance45", type=cbpmn_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
processInstance47: BinaryAssociation = BinaryAssociation(
    name="processInstance47",
    ends={
        Property(name="ProcessInstance", type=cbpmn_FlowNodeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="executedNodes", type=cbpmn_ProcessInstance, multiplicity=Multiplicity(1, 1))
    }
)
type48: BinaryAssociation = BinaryAssociation(
    name="type48",
    ends={
        Property(name="cbpmn_EClass49", type=cbpmn_DataObject, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_DataObject", type=cbpmn_EClass, multiplicity=Multiplicity(1, 1))
    }
)
branches30: BinaryAssociation = BinaryAssociation(
    name="branches30",
    ends={
        Property(name="Branch31", type=cbpmn_SplitGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="gateway", type=cbpmn_Branch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_cbpmn_Activity_FlowNode = Generalization(general=FlowNode, specific=cbpmn_Activity)
gen_cbpmn_DecisionGateway_SplitGateway = Generalization(general=SplitGateway, specific=cbpmn_DecisionGateway)
gen_cbpmn_Event_FlowNode = Generalization(general=FlowNode, specific=cbpmn_Event)
gen_cbpmn_ParallelGateway_SplitGateway = Generalization(general=SplitGateway, specific=cbpmn_ParallelGateway)
gen_cbpmn_SplitGateway_FlowNode = Generalization(general=FlowNode, specific=cbpmn_SplitGateway)
gen_cbpmn_DataObject_EObject = Generalization(general=EObject, specific=cbpmn_DataObject)
gen_cbpmn_StartEvent_Event = Generalization(general=Event, specific=cbpmn_StartEvent)
gen_cbpmn_EndEvent_Event = Generalization(general=Event, specific=cbpmn_EndEvent)
gen_cbpmn_IntermediateEvent_Event = Generalization(general=Event, specific=cbpmn_IntermediateEvent)

# Domain Model
domain_model = DomainModel(
    name="cbpmn",
    types={cbpmn_ProcessModel, cbpmn_Branch, cbpmn_OCLConstraint, cbpmn_Activity, FlowNode, cbpmn_DataObjectReference, cbpmn_FlowNode, cbpmn_DecisionGateway, SplitGateway, cbpmn_Event, cbpmn_ParallelGateway, cbpmn_SplitGateway, cbpmn_EClass, cbpmn_ProcessInstance, cbpmn_FlowNodeInstance, cbpmn_EObject, cbpmn_DataObject, EObject, cbpmn_StartEvent, Event, cbpmn_EndEvent, cbpmn_IntermediateEvent, ActivityType, EventType, DecisionType, DataObjectType, FlowNodeInstanceStatus, GatewayType},
    associations={mainBranch0, processInvariants1, preConditions3, postConditions5, outputs8, invariabilityClauses10, nodes13, branch17, next19, previous22, inputs24, branch26, trigger28, entryConditions14, gateway16, dataObjectClass32, processModel34, executedNodes36, dataObjects37, nodeDef39, inputs41, outputs44, processInstance47, type48, branches30},
    generalizations={gen_cbpmn_Activity_FlowNode, gen_cbpmn_DecisionGateway_SplitGateway, gen_cbpmn_Event_FlowNode, gen_cbpmn_ParallelGateway_SplitGateway, gen_cbpmn_SplitGateway_FlowNode, gen_cbpmn_DataObject_EObject, gen_cbpmn_StartEvent_Event, gen_cbpmn_EndEvent_Event, gen_cbpmn_IntermediateEvent_Event},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
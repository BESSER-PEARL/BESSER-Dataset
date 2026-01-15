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

GatewayType: Enumeration = Enumeration(
    name="GatewayType",
    literals={
            EnumerationLiteral(name="JOIN"),
			EnumerationLiteral(name="SPLIT")
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

# Classes
cbpmn_ProcessModel = Class(name="cbpmn::ProcessModel")
cbpmn_Branch = Class(name="cbpmn::Branch")
cbpmn_OCLConstraint = Class(name="cbpmn::OCLConstraint")
cbpmn_Activity = Class(name="cbpmn::Activity")
FlowNode = Class(name="FlowNode")
cbpmn_DataObjectReference = Class(name="cbpmn::DataObjectReference")
cbpmn_DecisionCondition = Class(name="cbpmn::DecisionCondition")
cbpmn_FlowNode = Class(name="cbpmn::FlowNode", is_abstract=True)
cbpmn_DecisionGateway = Class(name="cbpmn::DecisionGateway")
SplitGateway = Class(name="SplitGateway")
OCLConstraint = Class(name="OCLConstraint")
cbpmn_Event = Class(name="cbpmn::Event")
cbpmn_ParallelGateway = Class(name="cbpmn::ParallelGateway")
cbpmn_SplitGateway = Class(name="cbpmn::SplitGateway", is_abstract=True)
cbpmn_EClass = Class(name="cbpmn::EClass")
cbpmn_ProcessInstance = Class(name="cbpmn::ProcessInstance")
cbpmn_FlowNodeInstance = Class(name="cbpmn::FlowNodeInstance")
cbpmn_EObject = Class(name="cbpmn::EObject")
cbpmn_DataObject = Class(name="cbpmn::DataObject")
EObject = Class(name="EObject")

# cbpmn_ProcessModel class attributes and methods
cbpmn_ProcessModel_name: Property = Property(name="name", type=StringType)
cbpmn_ProcessModel.attributes={cbpmn_ProcessModel_name}

# cbpmn_Branch class attributes and methods

# cbpmn_OCLConstraint class attributes and methods
cbpmn_OCLConstraint_constraintName: Property = Property(name="constraintName", type=StringType)
cbpmn_OCLConstraint_constraintStr: Property = Property(name="constraintStr", type=StringType)
cbpmn_OCLConstraint.attributes={cbpmn_OCLConstraint_constraintName, cbpmn_OCLConstraint_constraintStr}

# cbpmn_Activity class attributes and methods
cbpmn_Activity_type: Property = Property(name="type", type=StringType)
cbpmn_Activity.attributes={cbpmn_Activity_type}

# FlowNode class attributes and methods

# cbpmn_DataObjectReference class attributes and methods
cbpmn_DataObjectReference_name: Property = Property(name="name", type=StringType)
cbpmn_DataObjectReference_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
cbpmn_DataObjectReference_higherBound: Property = Property(name="higherBound", type=IntegerType)
cbpmn_DataObjectReference.attributes={cbpmn_DataObjectReference_lowerBound, cbpmn_DataObjectReference_higherBound, cbpmn_DataObjectReference_name}

# cbpmn_DecisionCondition class attributes and methods
cbpmn_DecisionCondition_isDefault: Property = Property(name="isDefault", type=BooleanType)
cbpmn_DecisionCondition.attributes={cbpmn_DecisionCondition_isDefault}

# cbpmn_FlowNode class attributes and methods
cbpmn_FlowNode_name: Property = Property(name="name", type=StringType)
cbpmn_FlowNode.attributes={cbpmn_FlowNode_name}

# cbpmn_DecisionGateway class attributes and methods
cbpmn_DecisionGateway_type: Property = Property(name="type", type=StringType)
cbpmn_DecisionGateway_m_addBranchWithCondition: Method = Method(name="addBranchWithCondition", parameters={Parameter(name='condition'), Parameter(name='default'), Parameter(name='branch')})
cbpmn_DecisionGateway.attributes={cbpmn_DecisionGateway_type}
cbpmn_DecisionGateway.methods={cbpmn_DecisionGateway_m_addBranchWithCondition}

# SplitGateway class attributes and methods

# OCLConstraint class attributes and methods

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
inputs8: BinaryAssociation = BinaryAssociation(
    name="inputs8",
    ends={
        Property(name="cbpmn_DataObjectReference", type=cbpmn_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_Activity9", type=cbpmn_DataObjectReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs10: BinaryAssociation = BinaryAssociation(
    name="outputs10",
    ends={
        Property(name="cbpmn_DataObjectReference12", type=cbpmn_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_Activity11", type=cbpmn_DataObjectReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invariabilityClauses13: BinaryAssociation = BinaryAssociation(
    name="invariabilityClauses13",
    ends={
        Property(name="cbpmn_OCLConstraint15", type=cbpmn_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_Activity14", type=cbpmn_OCLConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryConditions16: BinaryAssociation = BinaryAssociation(
    name="entryConditions16",
    ends={
        Property(name="cbpmn_DecisionCondition", type=cbpmn_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_Branch17", type=cbpmn_DecisionCondition, multiplicity=Multiplicity(0, 1))
    }
)
nodes18: BinaryAssociation = BinaryAssociation(
    name="nodes18",
    ends={
        Property(name="FlowNode", type=cbpmn_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="branch", type=cbpmn_FlowNode, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
conditions19: BinaryAssociation = BinaryAssociation(
    name="conditions19",
    ends={
        Property(name="cbpmn_DecisionCondition20", type=cbpmn_DecisionGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_DecisionGateway", type=cbpmn_DecisionCondition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
branch21: BinaryAssociation = BinaryAssociation(
    name="branch21",
    ends={
        Property(name="cbpmn_Branch23", type=cbpmn_DecisionCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_DecisionCondition22", type=cbpmn_Branch, multiplicity=Multiplicity(1, 1))
    }
)
branch24: BinaryAssociation = BinaryAssociation(
    name="branch24",
    ends={
        Property(name="Branch", type=cbpmn_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=cbpmn_Branch, multiplicity=Multiplicity(0, 1))
    }
)
next26: BinaryAssociation = BinaryAssociation(
    name="next26",
    ends={
        Property(name="FlowNode27", type=cbpmn_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="previous", type=cbpmn_FlowNode, multiplicity=Multiplicity(0, 1))
    }
)
previous29: BinaryAssociation = BinaryAssociation(
    name="previous29",
    ends={
        Property(name="FlowNode30", type=cbpmn_FlowNode, multiplicity=Multiplicity(1, 1)),
        Property(name="next", type=cbpmn_FlowNode, multiplicity=Multiplicity(0, 1))
    }
)
trigger31: BinaryAssociation = BinaryAssociation(
    name="trigger31",
    ends={
        Property(name="cbpmn_OCLConstraint32", type=cbpmn_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_Event", type=cbpmn_OCLConstraint, multiplicity=Multiplicity(0, 1))
    }
)
branches33: BinaryAssociation = BinaryAssociation(
    name="branches33",
    ends={
        Property(name="cbpmn_Branch34", type=cbpmn_SplitGateway, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_SplitGateway", type=cbpmn_Branch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataObjectClass35: BinaryAssociation = BinaryAssociation(
    name="dataObjectClass35",
    ends={
        Property(name="cbpmn_EClass", type=cbpmn_DataObjectReference, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_DataObjectReference36", type=cbpmn_EClass, multiplicity=Multiplicity(1, 1))
    }
)
processModel37: BinaryAssociation = BinaryAssociation(
    name="processModel37",
    ends={
        Property(name="cbpmn_ProcessModel38", type=cbpmn_ProcessInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_ProcessInstance", type=cbpmn_ProcessModel, multiplicity=Multiplicity(1, 1))
    }
)
executedNodes39: BinaryAssociation = BinaryAssociation(
    name="executedNodes39",
    ends={
        Property(name="FlowNodeInstance", type=cbpmn_ProcessInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="processInstance", type=cbpmn_FlowNodeInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataObjects40: BinaryAssociation = BinaryAssociation(
    name="dataObjects40",
    ends={
        Property(name="cbpmn_EObject", type=cbpmn_ProcessInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_ProcessInstance41", type=cbpmn_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeDef42: BinaryAssociation = BinaryAssociation(
    name="nodeDef42",
    ends={
        Property(name="cbpmn_FlowNode", type=cbpmn_FlowNodeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_FlowNodeInstance", type=cbpmn_FlowNode, multiplicity=Multiplicity(1, 1))
    }
)
inputs43: BinaryAssociation = BinaryAssociation(
    name="inputs43",
    ends={
        Property(name="cbpmn_EObject45", type=cbpmn_FlowNodeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_FlowNodeInstance44", type=cbpmn_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
outputs46: BinaryAssociation = BinaryAssociation(
    name="outputs46",
    ends={
        Property(name="cbpmn_EObject48", type=cbpmn_FlowNodeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_FlowNodeInstance47", type=cbpmn_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
processInstance49: BinaryAssociation = BinaryAssociation(
    name="processInstance49",
    ends={
        Property(name="ProcessInstance", type=cbpmn_FlowNodeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="executedNodes", type=cbpmn_ProcessInstance, multiplicity=Multiplicity(1, 1))
    }
)
type50: BinaryAssociation = BinaryAssociation(
    name="type50",
    ends={
        Property(name="cbpmn_EClass51", type=cbpmn_DataObject, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmn_DataObject", type=cbpmn_EClass, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_cbpmn_Activity_FlowNode = Generalization(general=FlowNode, specific=cbpmn_Activity)
gen_cbpmn_DecisionGateway_SplitGateway = Generalization(general=SplitGateway, specific=cbpmn_DecisionGateway)
gen_cbpmn_DecisionCondition_OCLConstraint = Generalization(general=OCLConstraint, specific=cbpmn_DecisionCondition)
gen_cbpmn_Event_FlowNode = Generalization(general=FlowNode, specific=cbpmn_Event)
gen_cbpmn_ParallelGateway_SplitGateway = Generalization(general=SplitGateway, specific=cbpmn_ParallelGateway)
gen_cbpmn_SplitGateway_FlowNode = Generalization(general=FlowNode, specific=cbpmn_SplitGateway)
gen_cbpmn_DataObject_EObject = Generalization(general=EObject, specific=cbpmn_DataObject)

# Domain Model
domain_model = DomainModel(
    name="cbpmn",
    types={cbpmn_ProcessModel, cbpmn_Branch, cbpmn_OCLConstraint, cbpmn_Activity, FlowNode, cbpmn_DataObjectReference, cbpmn_DecisionCondition, cbpmn_FlowNode, cbpmn_DecisionGateway, SplitGateway, OCLConstraint, cbpmn_Event, cbpmn_ParallelGateway, cbpmn_SplitGateway, cbpmn_EClass, cbpmn_ProcessInstance, cbpmn_FlowNodeInstance, cbpmn_EObject, cbpmn_DataObject, EObject, ActivityType, EventType, DecisionType, GatewayType, DataObjectType, FlowNodeInstanceStatus},
    associations={mainBranch0, processInvariants1, preConditions3, postConditions5, inputs8, outputs10, invariabilityClauses13, entryConditions16, nodes18, conditions19, branch21, branch24, next26, previous29, trigger31, branches33, dataObjectClass35, processModel37, executedNodes39, dataObjects40, nodeDef42, inputs43, outputs46, processInstance49, type50},
    generalizations={gen_cbpmn_Activity_FlowNode, gen_cbpmn_DecisionGateway_SplitGateway, gen_cbpmn_DecisionCondition_OCLConstraint, gen_cbpmn_Event_FlowNode, gen_cbpmn_ParallelGateway_SplitGateway, gen_cbpmn_SplitGateway_FlowNode, gen_cbpmn_DataObject_EObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
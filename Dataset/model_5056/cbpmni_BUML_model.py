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
FlowNodeStatusType: Enumeration = Enumeration(
    name="FlowNodeStatusType",
    literals={
            EnumerationLiteral(name="INACTIVE"),
			EnumerationLiteral(name="READY"),
			EnumerationLiteral(name="RUNNING"),
			EnumerationLiteral(name="COMPLETED"),
			EnumerationLiteral(name="ABORTED")
    }
)

# Classes
cbpmni_ProcessInst = Class(name="cbpmni::ProcessInst")
cbpmni_ProcessModel = Class(name="cbpmni::ProcessModel")
cbpmni_FlowNodeInst = Class(name="cbpmni::FlowNodeInst", is_abstract=True)
cbpmni_FlowNode = Class(name="cbpmni::FlowNode")
cbpmni_ActivityInst = Class(name="cbpmni::ActivityInst")
FlowNodeInst = Class(name="FlowNodeInst")
cbpmni_EObject = Class(name="cbpmni::EObject")
cbpmni_EventInst = Class(name="cbpmni::EventInst")
cbpmni_SplitInst = Class(name="cbpmni::SplitInst")
cbpmni_BranchInst = Class(name="cbpmni::BranchInst")
cbpmni_Branch = Class(name="cbpmni::Branch")
cbpmni_OCLConstraint = Class(name="cbpmni::OCLConstraint")
cbpmni_ConstraintInst = Class(name="cbpmni::ConstraintInst")

# cbpmni_ProcessInst class attributes and methods
cbpmni_ProcessInst_m_setupProcessInstance: Method = Method(name="setupProcessInstance", parameters={})
cbpmni_ProcessInst.methods={cbpmni_ProcessInst_m_setupProcessInstance}

# cbpmni_ProcessModel class attributes and methods

# cbpmni_FlowNodeInst class attributes and methods
cbpmni_FlowNodeInst_status: Property = Property(name="status", type=StringType)
cbpmni_FlowNodeInst_m_EOperation0: Method = Method(name="EOperation0", parameters={})
cbpmni_FlowNodeInst.attributes={cbpmni_FlowNodeInst_status}
cbpmni_FlowNodeInst.methods={cbpmni_FlowNodeInst_m_EOperation0}

# cbpmni_FlowNode class attributes and methods

# cbpmni_ActivityInst class attributes and methods

# FlowNodeInst class attributes and methods

# cbpmni_EObject class attributes and methods

# cbpmni_EventInst class attributes and methods

# cbpmni_SplitInst class attributes and methods

# cbpmni_BranchInst class attributes and methods

# cbpmni_Branch class attributes and methods

# cbpmni_OCLConstraint class attributes and methods

# cbpmni_ConstraintInst class attributes and methods

# Relationships
processDef0: BinaryAssociation = BinaryAssociation(
    name="processDef0",
    ends={
        Property(name="cbpmni_ProcessModel", type=cbpmni_ProcessInst, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmni_ProcessInst", type=cbpmni_ProcessModel, multiplicity=Multiplicity(0, 1))
    }
)
tokens1: BinaryAssociation = BinaryAssociation(
    name="tokens1",
    ends={
        Property(name="cbpmni_FlowNodeInst", type=cbpmni_ProcessInst, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmni_ProcessInst2", type=cbpmni_FlowNodeInst, multiplicity=Multiplicity(0, 9999))
    }
)
flowNodes3: BinaryAssociation = BinaryAssociation(
    name="flowNodes3",
    ends={
        Property(name="cbpmni_FlowNodeInst5", type=cbpmni_ProcessInst, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmni_ProcessInst4", type=cbpmni_FlowNodeInst, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeDef6: BinaryAssociation = BinaryAssociation(
    name="nodeDef6",
    ends={
        Property(name="cbpmni_FlowNode", type=cbpmni_FlowNodeInst, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmni_FlowNodeInst7", type=cbpmni_FlowNode, multiplicity=Multiplicity(0, 1))
    }
)
next9: BinaryAssociation = BinaryAssociation(
    name="next9",
    ends={
        Property(name="cbpmni_FlowNodeInst10", type=cbpmni_FlowNodeInst, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmni_FlowNodeInst8", type=cbpmni_FlowNodeInst, multiplicity=Multiplicity(0, 1))
    }
)
inputs15: BinaryAssociation = BinaryAssociation(
    name="inputs15",
    ends={
        Property(name="cbpmni_EObject", type=cbpmni_ActivityInst, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmni_ActivityInst16", type=cbpmni_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
outputs17: BinaryAssociation = BinaryAssociation(
    name="outputs17",
    ends={
        Property(name="cbpmni_EObject19", type=cbpmni_ActivityInst, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmni_ActivityInst18", type=cbpmni_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
branches20: BinaryAssociation = BinaryAssociation(
    name="branches20",
    ends={
        Property(name="cbpmni_BranchInst", type=cbpmni_SplitInst, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmni_SplitInst", type=cbpmni_BranchInst, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
branchDef21: BinaryAssociation = BinaryAssociation(
    name="branchDef21",
    ends={
        Property(name="cbpmni_Branch", type=cbpmni_BranchInst, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmni_BranchInst22", type=cbpmni_Branch, multiplicity=Multiplicity(0, 1))
    }
)
extension23: BinaryAssociation = BinaryAssociation(
    name="extension23",
    ends={
        Property(name="cbpmni_EObject25", type=cbpmni_ConstraintInst, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmni_ConstraintInst24", type=cbpmni_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
constraintDef26: BinaryAssociation = BinaryAssociation(
    name="constraintDef26",
    ends={
        Property(name="cbpmni_OCLConstraint", type=cbpmni_ConstraintInst, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmni_ConstraintInst27", type=cbpmni_OCLConstraint, multiplicity=Multiplicity(1, 1))
    }
)
preconditions11: BinaryAssociation = BinaryAssociation(
    name="preconditions11",
    ends={
        Property(name="cbpmni_ConstraintInst", type=cbpmni_ActivityInst, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmni_ActivityInst", type=cbpmni_ConstraintInst, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postconditions12: BinaryAssociation = BinaryAssociation(
    name="postconditions12",
    ends={
        Property(name="cbpmni_ConstraintInst14", type=cbpmni_ActivityInst, multiplicity=Multiplicity(1, 1)),
        Property(name="cbpmni_ActivityInst13", type=cbpmni_ConstraintInst, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_cbpmni_EventInst_FlowNodeInst = Generalization(general=FlowNodeInst, specific=cbpmni_EventInst)
gen_cbpmni_SplitInst_FlowNodeInst = Generalization(general=FlowNodeInst, specific=cbpmni_SplitInst)
gen_cbpmni_ActivityInst_FlowNodeInst = Generalization(general=FlowNodeInst, specific=cbpmni_ActivityInst)

# Domain Model
domain_model = DomainModel(
    name="cbpmni",
    types={cbpmni_ProcessInst, cbpmni_ProcessModel, cbpmni_FlowNodeInst, cbpmni_FlowNode, cbpmni_ActivityInst, FlowNodeInst, cbpmni_EObject, cbpmni_EventInst, cbpmni_SplitInst, cbpmni_BranchInst, cbpmni_Branch, cbpmni_OCLConstraint, cbpmni_ConstraintInst, FlowNodeStatusType},
    associations={processDef0, tokens1, flowNodes3, nodeDef6, next9, inputs15, outputs17, branches20, branchDef21, extension23, constraintDef26, preconditions11, postconditions12},
    generalizations={gen_cbpmni_EventInst_FlowNodeInst, gen_cbpmni_SplitInst_FlowNodeInst, gen_cbpmni_ActivityInst_FlowNodeInst},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
RoleType: Enumeration = Enumeration(
    name="RoleType",
    literals={
            EnumerationLiteral(name="Contributing"),
			EnumerationLiteral(name="Counteracting")
    }
)

Nature: Enumeration = Enumeration(
    name="Nature",
    literals={
            EnumerationLiteral(name="Attack"),
			EnumerationLiteral(name="Fault"),
			EnumerationLiteral(name="Hybrid")
    }
)

EdgeKind: Enumeration = Enumeration(
    name="EdgeKind",
    literals={
            EnumerationLiteral(name="DEPENDENCY"),
			EnumerationLiteral(name="TRIGGER")
    }
)

# Classes
UATMM_structure_AttackTree = Class(name="UATMM::structure::AttackTree")
UATMM_structure_Node = Class(name="UATMM::structure::Node")
UATMM_structure_Edge = Class(name="UATMM::structure::Edge")
UATMM_structure_TreeMetaData = Class(name="UATMM::structure::TreeMetaData")
UATMM_structure_Connector = Class(name="UATMM::structure::Connector")
UATMM_structure_FDEP = Class(name="UATMM::structure::FDEP")
UATMM_structure_AND = Class(name="UATMM::structure::AND")
Connector = Class(name="Connector")
UATMM_structure_OR = Class(name="UATMM::structure::OR")
UATMM_structure_XOR = Class(name="UATMM::structure::XOR")
UATMM_structure_PAND = Class(name="UATMM::structure::PAND")
UATMM_structure_TAND = Class(name="UATMM::structure::TAND")
UATMM_structure_KofN = Class(name="UATMM::structure::KofN")
UATMM_structure_Weighted = Class(name="UATMM::structure::Weighted")
UATMM_structure_SAND = Class(name="UATMM::structure::SAND")
UATMM_structure_SOR = Class(name="UATMM::structure::SOR")
UATMM_structure_Spare = Class(name="UATMM::structure::Spare")
UATMM_structure_RDEP = Class(name="UATMM::structure::RDEP")

# UATMM_structure_AttackTree class attributes and methods

# UATMM_structure_Node class attributes and methods
UATMM_structure_Node_id: Property = Property(name="id", type=StringType)
UATMM_structure_Node_label: Property = Property(name="label", type=StringType)
UATMM_structure_Node_nature: Property = Property(name="nature", type=StringType)
UATMM_structure_Node_role: Property = Property(name="role", type=StringType)
UATMM_structure_Node.attributes={UATMM_structure_Node_label, UATMM_structure_Node_id, UATMM_structure_Node_role, UATMM_structure_Node_nature}

# UATMM_structure_Edge class attributes and methods
UATMM_structure_Edge_edgeKind: Property = Property(name="edgeKind", type=StringType)
UATMM_structure_Edge.attributes={UATMM_structure_Edge_edgeKind}

# UATMM_structure_TreeMetaData class attributes and methods
UATMM_structure_TreeMetaData_Key: Property = Property(name="Key", type=StringType)
UATMM_structure_TreeMetaData_Value: Property = Property(name="Value", type=StringType)
UATMM_structure_TreeMetaData.attributes={UATMM_structure_TreeMetaData_Value, UATMM_structure_TreeMetaData_Key}

# UATMM_structure_Connector class attributes and methods

# UATMM_structure_FDEP class attributes and methods

# UATMM_structure_AND class attributes and methods

# Connector class attributes and methods

# UATMM_structure_OR class attributes and methods

# UATMM_structure_XOR class attributes and methods

# UATMM_structure_PAND class attributes and methods

# UATMM_structure_TAND class attributes and methods

# UATMM_structure_KofN class attributes and methods
UATMM_structure_KofN_Threshold: Property = Property(name="Threshold", type=IntegerType)
UATMM_structure_KofN.attributes={UATMM_structure_KofN_Threshold}

# UATMM_structure_Weighted class attributes and methods
UATMM_structure_Weighted_Treshold: Property = Property(name="Treshold", type=FloatType)
UATMM_structure_Weighted_Weights: Property = Property(name="Weights", type=FloatType)
UATMM_structure_Weighted.attributes={UATMM_structure_Weighted_Treshold, UATMM_structure_Weighted_Weights}

# UATMM_structure_SAND class attributes and methods

# UATMM_structure_SOR class attributes and methods

# UATMM_structure_Spare class attributes and methods

# UATMM_structure_RDEP class attributes and methods
UATMM_structure_RDEP_factor: Property = Property(name="factor", type=FloatType)
UATMM_structure_RDEP.attributes={UATMM_structure_RDEP_factor}

# Relationships
Edges4: BinaryAssociation = BinaryAssociation(
    name="Edges4",
    ends={
        Property(name="UATMM_structure_AttackTree5", type=UATMM_structure_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="UATMM_structure_Edge", type=UATMM_structure_AttackTree, multiplicity=Multiplicity(1, 1))
    }
)
Root0: BinaryAssociation = BinaryAssociation(
    name="Root0",
    ends={
        Property(name="UATMM_structure_Node", type=UATMM_structure_AttackTree, multiplicity=Multiplicity(1, 1)),
        Property(name="UATMM_structure_AttackTree", type=UATMM_structure_Node, multiplicity=Multiplicity(1, 1))
    }
)
Nodes1: BinaryAssociation = BinaryAssociation(
    name="Nodes1",
    ends={
        Property(name="UATMM_structure_Node3", type=UATMM_structure_AttackTree, multiplicity=Multiplicity(1, 1)),
        Property(name="UATMM_structure_AttackTree2", type=UATMM_structure_Node, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
metadata6: BinaryAssociation = BinaryAssociation(
    name="metadata6",
    ends={
        Property(name="UATMM_structure_TreeMetaData", type=UATMM_structure_AttackTree, multiplicity=Multiplicity(1, 1)),
        Property(name="UATMM_structure_AttackTree7", type=UATMM_structure_TreeMetaData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connector8: BinaryAssociation = BinaryAssociation(
    name="connector8",
    ends={
        Property(name="Connector", type=UATMM_structure_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="gate", type=UATMM_structure_Connector, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children10: BinaryAssociation = BinaryAssociation(
    name="children10",
    ends={
        Property(name="Node", type=UATMM_structure_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="parents", type=UATMM_structure_Node, multiplicity=Multiplicity(0, 9999))
    }
)
parents12: BinaryAssociation = BinaryAssociation(
    name="parents12",
    ends={
        Property(name="Node13", type=UATMM_structure_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=UATMM_structure_Node, multiplicity=Multiplicity(0, 9999))
    }
)
Target14: BinaryAssociation = BinaryAssociation(
    name="Target14",
    ends={
        Property(name="UATMM_structure_Node16", type=UATMM_structure_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="UATMM_structure_Edge15", type=UATMM_structure_Node, multiplicity=Multiplicity(1, 1))
    }
)
Source17: BinaryAssociation = BinaryAssociation(
    name="Source17",
    ends={
        Property(name="UATMM_structure_Node19", type=UATMM_structure_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="UATMM_structure_Edge18", type=UATMM_structure_Node, multiplicity=Multiplicity(1, 1))
    }
)
gate20: BinaryAssociation = BinaryAssociation(
    name="gate20",
    ends={
        Property(name="Node21", type=UATMM_structure_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="connector", type=UATMM_structure_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_UATMM_structure_SOR_Connector = Generalization(general=Connector, specific=UATMM_structure_SOR)
gen_UATMM_structure_FDEP_Connector = Generalization(general=Connector, specific=UATMM_structure_FDEP)
gen_UATMM_structure_AND_Connector = Generalization(general=Connector, specific=UATMM_structure_AND)
gen_UATMM_structure_OR_Connector = Generalization(general=Connector, specific=UATMM_structure_OR)
gen_UATMM_structure_XOR_Connector = Generalization(general=Connector, specific=UATMM_structure_XOR)
gen_UATMM_structure_PAND_Connector = Generalization(general=Connector, specific=UATMM_structure_PAND)
gen_UATMM_structure_TAND_Connector = Generalization(general=Connector, specific=UATMM_structure_TAND)
gen_UATMM_structure_KofN_Connector = Generalization(general=Connector, specific=UATMM_structure_KofN)
gen_UATMM_structure_Weighted_Connector = Generalization(general=Connector, specific=UATMM_structure_Weighted)
gen_UATMM_structure_SAND_Connector = Generalization(general=Connector, specific=UATMM_structure_SAND)
gen_UATMM_structure_Spare_Connector = Generalization(general=Connector, specific=UATMM_structure_Spare)
gen_UATMM_structure_RDEP_Connector = Generalization(general=Connector, specific=UATMM_structure_RDEP)

# Domain Model
domain_model = DomainModel(
    name="UATMM_structure",
    types={UATMM_structure_AttackTree, UATMM_structure_Node, UATMM_structure_Edge, UATMM_structure_TreeMetaData, UATMM_structure_Connector, UATMM_structure_FDEP, UATMM_structure_AND, Connector, UATMM_structure_OR, UATMM_structure_XOR, UATMM_structure_PAND, UATMM_structure_TAND, UATMM_structure_KofN, UATMM_structure_Weighted, UATMM_structure_SAND, UATMM_structure_SOR, UATMM_structure_Spare, UATMM_structure_RDEP, RoleType, Nature, EdgeKind},
    associations={Edges4, Root0, Nodes1, metadata6, connector8, children10, parents12, Target14, Source17, gate20},
    generalizations={gen_UATMM_structure_SOR_Connector, gen_UATMM_structure_FDEP_Connector, gen_UATMM_structure_AND_Connector, gen_UATMM_structure_OR_Connector, gen_UATMM_structure_XOR_Connector, gen_UATMM_structure_PAND_Connector, gen_UATMM_structure_TAND_Connector, gen_UATMM_structure_KofN_Connector, gen_UATMM_structure_Weighted_Connector, gen_UATMM_structure_SAND_Connector, gen_UATMM_structure_Spare_Connector, gen_UATMM_structure_RDEP_Connector},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
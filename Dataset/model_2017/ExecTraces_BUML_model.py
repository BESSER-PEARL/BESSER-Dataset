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
StateStatus: Enumeration = Enumeration(
    name="StateStatus",
    literals={
            EnumerationLiteral(name="new"),
			EnumerationLiteral(name="unSafeState"),
			EnumerationLiteral(name="Repeated")
    }
)

TransStatus: Enumeration = Enumeration(
    name="TransStatus",
    literals={
            EnumerationLiteral(name="normal"),
			EnumerationLiteral(name="error"),
			EnumerationLiteral(name="unsafeTrans"),
			EnumerationLiteral(name="redundantTrans")
    }
)

# Classes
execTraces_ExecTraces = Class(name="execTraces::ExecTraces")
execTraces_Node = Class(name="execTraces::Node")
execTraces_Variable = Class(name="execTraces::Variable")
execTraces_Literal = Class(name="execTraces::Literal")
execTraces_RealLiteral = Class(name="execTraces::RealLiteral")
Literal = Class(name="Literal")
execTraces_IntLiteral = Class(name="execTraces::IntLiteral")
execTraces_Edge = Class(name="execTraces::Edge")
execTraces_BoolLiteral = Class(name="execTraces::BoolLiteral")

# execTraces_ExecTraces class attributes and methods
execTraces_ExecTraces_ComponentName: Property = Property(name="ComponentName", type=StringType)
execTraces_ExecTraces.attributes={execTraces_ExecTraces_ComponentName}

# execTraces_Node class attributes and methods
execTraces_Node_name: Property = Property(name="name", type=StringType)
execTraces_Node_id: Property = Property(name="id", type=IntegerType)
execTraces_Node_level: Property = Property(name="level", type=IntegerType)
execTraces_Node_status: Property = Property(name="status", type=StringType)
execTraces_Node_constraints: Property = Property(name="constraints", type=StringType)
execTraces_Node.attributes={execTraces_Node_level, execTraces_Node_status, execTraces_Node_constraints, execTraces_Node_id, execTraces_Node_name}

# execTraces_Variable class attributes and methods
execTraces_Variable_name: Property = Property(name="name", type=StringType)
execTraces_Variable.attributes={execTraces_Variable_name}

# execTraces_Literal class attributes and methods

# execTraces_RealLiteral class attributes and methods
execTraces_RealLiteral_intPart: Property = Property(name="intPart", type=IntegerType)
execTraces_RealLiteral_decimalPart: Property = Property(name="decimalPart", type=IntegerType)
execTraces_RealLiteral.attributes={execTraces_RealLiteral_intPart, execTraces_RealLiteral_decimalPart}

# Literal class attributes and methods

# execTraces_IntLiteral class attributes and methods
execTraces_IntLiteral_int: Property = Property(name="int", type=IntegerType)
execTraces_IntLiteral.attributes={execTraces_IntLiteral_int}

# execTraces_Edge class attributes and methods
execTraces_Edge_guard: Property = Property(name="guard", type=StringType)
execTraces_Edge_trigger: Property = Property(name="trigger", type=StringType)
execTraces_Edge_actions: Property = Property(name="actions", type=StringType)
execTraces_Edge_status: Property = Property(name="status", type=StringType)
execTraces_Edge.attributes={execTraces_Edge_guard, execTraces_Edge_trigger, execTraces_Edge_actions, execTraces_Edge_status}

# execTraces_BoolLiteral class attributes and methods
execTraces_BoolLiteral_bool: Property = Property(name="bool", type=StringType)
execTraces_BoolLiteral.attributes={execTraces_BoolLiteral_bool}

# Relationships
Node0: BinaryAssociation = BinaryAssociation(
    name="Node0",
    ends={
        Property(name="execTraces_Node", type=execTraces_ExecTraces, multiplicity=Multiplicity(1, 1)),
        Property(name="execTraces_ExecTraces", type=execTraces_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
VarData9: BinaryAssociation = BinaryAssociation(
    name="VarData9",
    ends={
        Property(name="execTraces_Variable", type=execTraces_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="execTraces_Node10", type=execTraces_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingEdges11: BinaryAssociation = BinaryAssociation(
    name="outgoingEdges11",
    ends={
        Property(name="execTraces_Edge13", type=execTraces_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="execTraces_Node12", type=execTraces_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
incomingEdges14: BinaryAssociation = BinaryAssociation(
    name="incomingEdges14",
    ends={
        Property(name="execTraces_Edge16", type=execTraces_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="execTraces_Node15", type=execTraces_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
value17: BinaryAssociation = BinaryAssociation(
    name="value17",
    ends={
        Property(name="execTraces_Literal", type=execTraces_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="execTraces_Variable18", type=execTraces_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Edge1: BinaryAssociation = BinaryAssociation(
    name="Edge1",
    ends={
        Property(name="execTraces_Edge", type=execTraces_ExecTraces, multiplicity=Multiplicity(1, 1)),
        Property(name="execTraces_ExecTraces2", type=execTraces_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="execTraces_Node5", type=execTraces_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="execTraces_Edge4", type=execTraces_Node, multiplicity=Multiplicity(0, 1))
    }
)
destination6: BinaryAssociation = BinaryAssociation(
    name="destination6",
    ends={
        Property(name="execTraces_Node8", type=execTraces_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="execTraces_Edge7", type=execTraces_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_execTraces_RealLiteral_Literal = Generalization(general=Literal, specific=execTraces_RealLiteral)
gen_execTraces_IntLiteral_Literal = Generalization(general=Literal, specific=execTraces_IntLiteral)
gen_execTraces_BoolLiteral_Literal = Generalization(general=Literal, specific=execTraces_BoolLiteral)

# Domain Model
domain_model = DomainModel(
    name="execTraces",
    types={execTraces_ExecTraces, execTraces_Node, execTraces_Variable, execTraces_Literal, execTraces_RealLiteral, Literal, execTraces_IntLiteral, execTraces_Edge, execTraces_BoolLiteral, StateStatus, TransStatus},
    associations={Node0, VarData9, outgoingEdges11, incomingEdges14, value17, Edge1, source3, destination6},
    generalizations={gen_execTraces_RealLiteral_Literal, gen_execTraces_IntLiteral_Literal, gen_execTraces_BoolLiteral_Literal},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
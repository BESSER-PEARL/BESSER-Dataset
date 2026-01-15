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
ctrlflow101_Function = Class(name="ctrlflow101::Function")
SequenceNode = Class(name="SequenceNode")
ctrlflow101_Or = Class(name="ctrlflow101::Or")
ctrlflow101_Start = Class(name="ctrlflow101::Start")
ctrlflow101_Final = Class(name="ctrlflow101::Final")
ctrlflow101_Loop = Class(name="ctrlflow101::Loop")
ctrlflow101_Sequence = Class(name="ctrlflow101::Sequence", is_abstract=True)
ctrlflow101_Token = Class(name="ctrlflow101::Token")
ctrlflow101_SequenceNode = Class(name="ctrlflow101::SequenceNode", is_abstract=True)
ctrlflow101_And = Class(name="ctrlflow101::And")
Sequence = Class(name="Sequence")

# ctrlflow101_Function class attributes and methods

# SequenceNode class attributes and methods

# ctrlflow101_Or class attributes and methods

# ctrlflow101_Start class attributes and methods

# ctrlflow101_Final class attributes and methods

# ctrlflow101_Loop class attributes and methods

# ctrlflow101_Sequence class attributes and methods
ctrlflow101_Sequence_weight: Property = Property(name="weight", type=IntegerType)
ctrlflow101_Sequence.attributes={ctrlflow101_Sequence_weight}

# ctrlflow101_Token class attributes and methods

# ctrlflow101_SequenceNode class attributes and methods
ctrlflow101_SequenceNode_name: Property = Property(name="name", type=StringType)
ctrlflow101_SequenceNode_tMin: Property = Property(name="tMin", type=IntegerType)
ctrlflow101_SequenceNode_tMax: Property = Property(name="tMax", type=IntegerType)
ctrlflow101_SequenceNode.attributes={ctrlflow101_SequenceNode_tMax, ctrlflow101_SequenceNode_name, ctrlflow101_SequenceNode_tMin}

# ctrlflow101_And class attributes and methods

# Sequence class attributes and methods

# Relationships
decompositions1: BinaryAssociation = BinaryAssociation(
    name="decompositions1",
    ends={
        Property(name="ctrlflow101_Function", type=ctrlflow101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="ctrlflow101_Function0", type=ctrlflow101_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceNodes2: BinaryAssociation = BinaryAssociation(
    name="sequenceNodes2",
    ends={
        Property(name="ctrlflow101_Sequence", type=ctrlflow101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="ctrlflow101_Function3", type=ctrlflow101_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokens4: BinaryAssociation = BinaryAssociation(
    name="tokens4",
    ends={
        Property(name="ctrlflow101_Token", type=ctrlflow101_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="ctrlflow101_Function5", type=ctrlflow101_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controlFlowEdge7: BinaryAssociation = BinaryAssociation(
    name="controlFlowEdge7",
    ends={
        Property(name="ctrlflow101_SequenceNode", type=ctrlflow101_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ctrlflow101_SequenceNode6", type=ctrlflow101_SequenceNode, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ctrlflow101_Function_SequenceNode = Generalization(general=SequenceNode, specific=ctrlflow101_Function)
gen_ctrlflow101_And_Sequence = Generalization(general=Sequence, specific=ctrlflow101_And)
gen_ctrlflow101_Or_Sequence = Generalization(general=Sequence, specific=ctrlflow101_Or)
gen_ctrlflow101_Start_Sequence = Generalization(general=Sequence, specific=ctrlflow101_Start)
gen_ctrlflow101_Final_Sequence = Generalization(general=Sequence, specific=ctrlflow101_Final)
gen_ctrlflow101_Loop_Sequence = Generalization(general=Sequence, specific=ctrlflow101_Loop)
gen_ctrlflow101_Sequence_SequenceNode = Generalization(general=SequenceNode, specific=ctrlflow101_Sequence)

# Domain Model
domain_model = DomainModel(
    name="ctrlflow101",
    types={ctrlflow101_Function, SequenceNode, ctrlflow101_Or, ctrlflow101_Start, ctrlflow101_Final, ctrlflow101_Loop, ctrlflow101_Sequence, ctrlflow101_Token, ctrlflow101_SequenceNode, ctrlflow101_And, Sequence},
    associations={decompositions1, sequenceNodes2, tokens4, controlFlowEdge7},
    generalizations={gen_ctrlflow101_Function_SequenceNode, gen_ctrlflow101_And_Sequence, gen_ctrlflow101_Or_Sequence, gen_ctrlflow101_Start_Sequence, gen_ctrlflow101_Final_Sequence, gen_ctrlflow101_Loop_Sequence, gen_ctrlflow101_Sequence_SequenceNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
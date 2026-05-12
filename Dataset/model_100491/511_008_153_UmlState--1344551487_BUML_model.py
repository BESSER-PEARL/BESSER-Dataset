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
BehaviorKind: Enumeration = Enumeration(
    name="BehaviorKind",
    literals={
            EnumerationLiteral(name="ACTIVITY"),
			EnumerationLiteral(name="STATE_MACHINE"),
			EnumerationLiteral(name="OPAQUE_BEHAVIOR")
    }
)

# Classes
umlState_SubmachineRule = Class(name="umlState_SubmachineRule")
umlState_EntryRule = Class(name="umlState_EntryRule")
umlState_DoRule = Class(name="umlState_DoRule")
umlState_ExitRule = Class(name="umlState_ExitRule")
umlState_QualifiedName = Class(name="umlState_QualifiedName")
umlState_StateMachine = Class(name="umlState_StateMachine")
umlState_Namespace = Class(name="umlState_Namespace")
umlState_StateRule = Class(name="umlState_StateRule")

# umlState_SubmachineRule class attributes and methods

# umlState_EntryRule class attributes and methods
umlState_EntryRule_kind: Property = Property(name="kind", type=StringType)
umlState_EntryRule_behaviorName: Property = Property(name="behaviorName", type=StringType)
umlState_EntryRule.attributes={umlState_EntryRule_kind, umlState_EntryRule_behaviorName}

# umlState_DoRule class attributes and methods
umlState_DoRule_kind: Property = Property(name="kind", type=StringType)
umlState_DoRule_behaviorName: Property = Property(name="behaviorName", type=StringType)
umlState_DoRule.attributes={umlState_DoRule_behaviorName, umlState_DoRule_kind}

# umlState_ExitRule class attributes and methods
umlState_ExitRule_kind: Property = Property(name="kind", type=StringType)
umlState_ExitRule_behaviorName: Property = Property(name="behaviorName", type=StringType)
umlState_ExitRule.attributes={umlState_ExitRule_kind, umlState_ExitRule_behaviorName}

# umlState_QualifiedName class attributes and methods

# umlState_StateMachine class attributes and methods

# umlState_Namespace class attributes and methods

# umlState_StateRule class attributes and methods
umlState_StateRule_name: Property = Property(name="name", type=StringType)
umlState_StateRule.attributes={umlState_StateRule_name}

# Relationships
submachine0: BinaryAssociation = BinaryAssociation(
    name="submachine0",
    ends={
        Property(name="umlState_SubmachineRule", type=umlState_StateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="umlState_StateRule", type=umlState_SubmachineRule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry1: BinaryAssociation = BinaryAssociation(
    name="entry1",
    ends={
        Property(name="umlState_EntryRule", type=umlState_StateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="umlState_StateRule2", type=umlState_EntryRule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
do3: BinaryAssociation = BinaryAssociation(
    name="do3",
    ends={
        Property(name="umlState_DoRule", type=umlState_StateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="umlState_StateRule4", type=umlState_DoRule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit5: BinaryAssociation = BinaryAssociation(
    name="exit5",
    ends={
        Property(name="umlState_ExitRule", type=umlState_StateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="umlState_StateRule6", type=umlState_ExitRule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path7: BinaryAssociation = BinaryAssociation(
    name="path7",
    ends={
        Property(name="umlState_QualifiedName", type=umlState_SubmachineRule, multiplicity=Multiplicity(1, 1)),
        Property(name="umlState_SubmachineRule8", type=umlState_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
submachine9: BinaryAssociation = BinaryAssociation(
    name="submachine9",
    ends={
        Property(name="umlState_StateMachine", type=umlState_SubmachineRule, multiplicity=Multiplicity(1, 1)),
        Property(name="umlState_SubmachineRule10", type=umlState_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
path11: BinaryAssociation = BinaryAssociation(
    name="path11",
    ends={
        Property(name="umlState_Namespace", type=umlState_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="umlState_QualifiedName12", type=umlState_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
remaining14: BinaryAssociation = BinaryAssociation(
    name="remaining14",
    ends={
        Property(name="umlState_QualifiedName15", type=umlState_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="umlState_QualifiedName13", type=umlState_QualifiedName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="umlState",
    types={umlState_SubmachineRule, umlState_EntryRule, umlState_DoRule, umlState_ExitRule, umlState_QualifiedName, umlState_StateMachine, umlState_Namespace, umlState_StateRule, BehaviorKind},
    associations={submachine0, entry1, do3, exit5, path7, submachine9, path11, remaining14},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
StatemachineMetamodel_Statemachine = Class(name="StatemachineMetamodel::Statemachine")
StatemachineMetamodel_State = Class(name="StatemachineMetamodel::State")
StatemachineMetamodel_Transition = Class(name="StatemachineMetamodel::Transition")

# StatemachineMetamodel_Statemachine class attributes and methods

# StatemachineMetamodel_State class attributes and methods
StatemachineMetamodel_State_name: Property = Property(name="name", type=StringType)
StatemachineMetamodel_State.attributes={StatemachineMetamodel_State_name}

# StatemachineMetamodel_Transition class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="StatemachineMetamodel_State", type=StatemachineMetamodel_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StatemachineMetamodel_Statemachine", type=StatemachineMetamodel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetState1: BinaryAssociation = BinaryAssociation(
    name="targetState1",
    ends={
        Property(name="StatemachineMetamodel_State2", type=StatemachineMetamodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StatemachineMetamodel_Transition", type=StatemachineMetamodel_State, multiplicity=Multiplicity(0, 1))
    }
)
transitions3: BinaryAssociation = BinaryAssociation(
    name="transitions3",
    ends={
        Property(name="StatemachineMetamodel_Transition5", type=StatemachineMetamodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StatemachineMetamodel_State4", type=StatemachineMetamodel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="StatemachineMetamodel",
    types={StatemachineMetamodel_Statemachine, StatemachineMetamodel_State, StatemachineMetamodel_Transition},
    associations={states0, targetState1, transitions3},
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
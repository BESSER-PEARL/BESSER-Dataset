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
fsmtest_Model = Class(name="fsmtest::Model")
fsmtest_FsmDefinition = Class(name="fsmtest::FsmDefinition")
fsmtest_RandomTest = Class(name="fsmtest::RandomTest")
fsmtest_GuardDeclaration = Class(name="fsmtest::GuardDeclaration")
fsmtest_SignalDeclaration = Class(name="fsmtest::SignalDeclaration")
fsmtest_TransitionDeclaration = Class(name="fsmtest::TransitionDeclaration")
fsmtest_StateDeclaration = Class(name="fsmtest::StateDeclaration")
fsmtest_LoopsDeclaration = Class(name="fsmtest::LoopsDeclaration")
fsmtest_SeedDeclaration = Class(name="fsmtest::SeedDeclaration")
fsmtest_PreconditionDeclaration = Class(name="fsmtest::PreconditionDeclaration")
fsmtest_PostconditionDeclaration = Class(name="fsmtest::PostconditionDeclaration")
fsmtest_ConditionDeclaration = Class(name="fsmtest::ConditionDeclaration")

# fsmtest_Model class attributes and methods

# fsmtest_FsmDefinition class attributes and methods
fsmtest_FsmDefinition_name: Property = Property(name="name", type=StringType)
fsmtest_FsmDefinition.attributes={fsmtest_FsmDefinition_name}

# fsmtest_RandomTest class attributes and methods
fsmtest_RandomTest_name: Property = Property(name="name", type=StringType)
fsmtest_RandomTest.attributes={fsmtest_RandomTest_name}

# fsmtest_GuardDeclaration class attributes and methods

# fsmtest_SignalDeclaration class attributes and methods
fsmtest_SignalDeclaration_port: Property = Property(name="port", type=StringType)
fsmtest_SignalDeclaration_signame: Property = Property(name="signame", type=StringType)
fsmtest_SignalDeclaration_intVal: Property = Property(name="intVal", type=IntegerType)
fsmtest_SignalDeclaration_strVal: Property = Property(name="strVal", type=StringType)
fsmtest_SignalDeclaration.attributes={fsmtest_SignalDeclaration_port, fsmtest_SignalDeclaration_intVal, fsmtest_SignalDeclaration_signame, fsmtest_SignalDeclaration_strVal}

# fsmtest_TransitionDeclaration class attributes and methods
fsmtest_TransitionDeclaration_name: Property = Property(name="name", type=StringType)
fsmtest_TransitionDeclaration.attributes={fsmtest_TransitionDeclaration_name}

# fsmtest_StateDeclaration class attributes and methods
fsmtest_StateDeclaration_name: Property = Property(name="name", type=StringType)
fsmtest_StateDeclaration.attributes={fsmtest_StateDeclaration_name}

# fsmtest_LoopsDeclaration class attributes and methods
fsmtest_LoopsDeclaration_val: Property = Property(name="val", type=IntegerType)
fsmtest_LoopsDeclaration.attributes={fsmtest_LoopsDeclaration_val}

# fsmtest_SeedDeclaration class attributes and methods
fsmtest_SeedDeclaration_val: Property = Property(name="val", type=IntegerType)
fsmtest_SeedDeclaration.attributes={fsmtest_SeedDeclaration_val}

# fsmtest_PreconditionDeclaration class attributes and methods

# fsmtest_PostconditionDeclaration class attributes and methods

# fsmtest_ConditionDeclaration class attributes and methods

# Relationships
FsmDefinitions0: BinaryAssociation = BinaryAssociation(
    name="FsmDefinitions0",
    ends={
        Property(name="fsmtest_FsmDefinition", type=fsmtest_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmtest_Model", type=fsmtest_FsmDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal12: BinaryAssociation = BinaryAssociation(
    name="signal12",
    ends={
        Property(name="fsmtest_SignalDeclaration", type=fsmtest_GuardDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmtest_GuardDeclaration", type=fsmtest_SignalDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
destination13: BinaryAssociation = BinaryAssociation(
    name="destination13",
    ends={
        Property(name="fsmtest_StateDeclaration14", type=fsmtest_TransitionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmtest_TransitionDeclaration", type=fsmtest_StateDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
trigger15: BinaryAssociation = BinaryAssociation(
    name="trigger15",
    ends={
        Property(name="fsmtest_SignalDeclaration17", type=fsmtest_TransitionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmtest_TransitionDeclaration16", type=fsmtest_SignalDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
RandomTests1: BinaryAssociation = BinaryAssociation(
    name="RandomTests1",
    ends={
        Property(name="fsmtest_RandomTest", type=fsmtest_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmtest_Model2", type=fsmtest_RandomTest, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="fsmtest_StateDeclaration", type=fsmtest_FsmDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmtest_FsmDefinition4", type=fsmtest_StateDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fsm5: BinaryAssociation = BinaryAssociation(
    name="fsm5",
    ends={
        Property(name="fsmtest_FsmDefinition7", type=fsmtest_RandomTest, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmtest_RandomTest6", type=fsmtest_FsmDefinition, multiplicity=Multiplicity(0, 1))
    }
)
loopsDeclaration8: BinaryAssociation = BinaryAssociation(
    name="loopsDeclaration8",
    ends={
        Property(name="fsmtest_LoopsDeclaration", type=fsmtest_RandomTest, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmtest_RandomTest9", type=fsmtest_LoopsDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
seedDeclaration10: BinaryAssociation = BinaryAssociation(
    name="seedDeclaration10",
    ends={
        Property(name="fsmtest_SeedDeclaration", type=fsmtest_RandomTest, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmtest_RandomTest11", type=fsmtest_SeedDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signal30: BinaryAssociation = BinaryAssociation(
    name="signal30",
    ends={
        Property(name="fsmtest_SignalDeclaration32", type=fsmtest_PostconditionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmtest_PostconditionDeclaration31", type=fsmtest_SignalDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition33: BinaryAssociation = BinaryAssociation(
    name="condition33",
    ends={
        Property(name="fsmtest_ConditionDeclaration35", type=fsmtest_StateDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmtest_StateDeclaration34", type=fsmtest_ConditionDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions36: BinaryAssociation = BinaryAssociation(
    name="transitions36",
    ends={
        Property(name="fsmtest_TransitionDeclaration38", type=fsmtest_StateDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmtest_StateDeclaration37", type=fsmtest_TransitionDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triggers18: BinaryAssociation = BinaryAssociation(
    name="triggers18",
    ends={
        Property(name="fsmtest_GuardDeclaration20", type=fsmtest_TransitionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmtest_TransitionDeclaration19", type=fsmtest_GuardDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
precondition21: BinaryAssociation = BinaryAssociation(
    name="precondition21",
    ends={
        Property(name="fsmtest_PreconditionDeclaration", type=fsmtest_TransitionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmtest_TransitionDeclaration22", type=fsmtest_PreconditionDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postcondition23: BinaryAssociation = BinaryAssociation(
    name="postcondition23",
    ends={
        Property(name="fsmtest_PostconditionDeclaration", type=fsmtest_TransitionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmtest_TransitionDeclaration24", type=fsmtest_PostconditionDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal25: BinaryAssociation = BinaryAssociation(
    name="signal25",
    ends={
        Property(name="fsmtest_SignalDeclaration26", type=fsmtest_ConditionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmtest_ConditionDeclaration", type=fsmtest_SignalDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signal27: BinaryAssociation = BinaryAssociation(
    name="signal27",
    ends={
        Property(name="fsmtest_SignalDeclaration29", type=fsmtest_PreconditionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmtest_PreconditionDeclaration28", type=fsmtest_SignalDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsmtest",
    types={fsmtest_Model, fsmtest_FsmDefinition, fsmtest_RandomTest, fsmtest_GuardDeclaration, fsmtest_SignalDeclaration, fsmtest_TransitionDeclaration, fsmtest_StateDeclaration, fsmtest_LoopsDeclaration, fsmtest_SeedDeclaration, fsmtest_PreconditionDeclaration, fsmtest_PostconditionDeclaration, fsmtest_ConditionDeclaration},
    associations={FsmDefinitions0, signal12, destination13, trigger15, RandomTests1, states3, fsm5, loopsDeclaration8, seedDeclaration10, signal30, condition33, transitions36, triggers18, precondition21, postcondition23, signal25, signal27},
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
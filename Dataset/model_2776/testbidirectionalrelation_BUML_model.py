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
testbidirectionalrelation_ConceptA = Class(name="testbidirectionalrelation::ConceptA")
testbidirectionalrelation_ConceptB = Class(name="testbidirectionalrelation::ConceptB")
testbidirectionalrelation_ConceptC = Class(name="testbidirectionalrelation::ConceptC")
testbidirectionalrelation_ConceptD = Class(name="testbidirectionalrelation::ConceptD")
testbidirectionalrelation_ConceptE = Class(name="testbidirectionalrelation::ConceptE")
testbidirectionalrelation_ConceptF = Class(name="testbidirectionalrelation::ConceptF")
testbidirectionalrelation_ConceptG = Class(name="testbidirectionalrelation::ConceptG")

# testbidirectionalrelation_ConceptA class attributes and methods

# testbidirectionalrelation_ConceptB class attributes and methods

# testbidirectionalrelation_ConceptC class attributes and methods

# testbidirectionalrelation_ConceptD class attributes and methods

# testbidirectionalrelation_ConceptE class attributes and methods

# testbidirectionalrelation_ConceptF class attributes and methods

# testbidirectionalrelation_ConceptG class attributes and methods

# Relationships
conceptc11: BinaryAssociation = BinaryAssociation(
    name="conceptc11",
    ends={
        Property(name="12", type=testbidirectionalrelation_ConceptB, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=testbidirectionalrelation_ConceptC, multiplicity=Multiplicity(0, 1))
    }
)
conceptb13: BinaryAssociation = BinaryAssociation(
    name="conceptb13",
    ends={
        Property(name="15", type=testbidirectionalrelation_ConceptC, multiplicity=Multiplicity(1, 1)),
        Property(name="14", type=testbidirectionalrelation_ConceptB, multiplicity=Multiplicity(0, 1))
    }
)
concepte16: BinaryAssociation = BinaryAssociation(
    name="concepte16",
    ends={
        Property(name="18", type=testbidirectionalrelation_ConceptD, multiplicity=Multiplicity(1, 1)),
        Property(name="17", type=testbidirectionalrelation_ConceptE, multiplicity=Multiplicity(0, 1))
    }
)
conceptd19: BinaryAssociation = BinaryAssociation(
    name="conceptd19",
    ends={
        Property(name="21", type=testbidirectionalrelation_ConceptE, multiplicity=Multiplicity(1, 1)),
        Property(name="20", type=testbidirectionalrelation_ConceptD, multiplicity=Multiplicity(0, 9999))
    }
)
conceptb0: BinaryAssociation = BinaryAssociation(
    name="conceptb0",
    ends={
        Property(name="testbidirectionalrelation_ConceptB", type=testbidirectionalrelation_ConceptA, multiplicity=Multiplicity(1, 1)),
        Property(name="testbidirectionalrelation_ConceptA", type=testbidirectionalrelation_ConceptB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conceptc1: BinaryAssociation = BinaryAssociation(
    name="conceptc1",
    ends={
        Property(name="testbidirectionalrelation_ConceptC", type=testbidirectionalrelation_ConceptA, multiplicity=Multiplicity(1, 1)),
        Property(name="testbidirectionalrelation_ConceptA2", type=testbidirectionalrelation_ConceptC, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conceptd3: BinaryAssociation = BinaryAssociation(
    name="conceptd3",
    ends={
        Property(name="testbidirectionalrelation_ConceptD", type=testbidirectionalrelation_ConceptA, multiplicity=Multiplicity(1, 1)),
        Property(name="testbidirectionalrelation_ConceptA4", type=testbidirectionalrelation_ConceptD, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
concepte5: BinaryAssociation = BinaryAssociation(
    name="concepte5",
    ends={
        Property(name="testbidirectionalrelation_ConceptE", type=testbidirectionalrelation_ConceptA, multiplicity=Multiplicity(1, 1)),
        Property(name="testbidirectionalrelation_ConceptA6", type=testbidirectionalrelation_ConceptE, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conceptf7: BinaryAssociation = BinaryAssociation(
    name="conceptf7",
    ends={
        Property(name="testbidirectionalrelation_ConceptF", type=testbidirectionalrelation_ConceptA, multiplicity=Multiplicity(1, 1)),
        Property(name="testbidirectionalrelation_ConceptA8", type=testbidirectionalrelation_ConceptF, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conceptg9: BinaryAssociation = BinaryAssociation(
    name="conceptg9",
    ends={
        Property(name="testbidirectionalrelation_ConceptG", type=testbidirectionalrelation_ConceptA, multiplicity=Multiplicity(1, 1)),
        Property(name="testbidirectionalrelation_ConceptA10", type=testbidirectionalrelation_ConceptG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conceptg22: BinaryAssociation = BinaryAssociation(
    name="conceptg22",
    ends={
        Property(name="24", type=testbidirectionalrelation_ConceptF, multiplicity=Multiplicity(1, 1)),
        Property(name="23", type=testbidirectionalrelation_ConceptG, multiplicity=Multiplicity(0, 9999))
    }
)
conceptf25: BinaryAssociation = BinaryAssociation(
    name="conceptf25",
    ends={
        Property(name="27", type=testbidirectionalrelation_ConceptG, multiplicity=Multiplicity(1, 1)),
        Property(name="26", type=testbidirectionalrelation_ConceptF, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="testbidirectionalrelation",
    types={testbidirectionalrelation_ConceptA, testbidirectionalrelation_ConceptB, testbidirectionalrelation_ConceptC, testbidirectionalrelation_ConceptD, testbidirectionalrelation_ConceptE, testbidirectionalrelation_ConceptF, testbidirectionalrelation_ConceptG},
    associations={conceptc11, conceptb13, concepte16, conceptd19, conceptb0, conceptc1, conceptd3, concepte5, conceptf7, conceptg9, conceptg22, conceptf25},
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
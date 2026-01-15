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
testbidirectionalrelation_ConceptG = Class(name="testbidirectionalrelation::ConceptG")
testbidirectionalrelation_ConceptA = Class(name="testbidirectionalrelation::ConceptA")
testbidirectionalrelation_ConceptB = Class(name="testbidirectionalrelation::ConceptB")
testbidirectionalrelation_ConceptC = Class(name="testbidirectionalrelation::ConceptC")
testbidirectionalrelation_ConceptD = Class(name="testbidirectionalrelation::ConceptD")
testbidirectionalrelation_ConceptE = Class(name="testbidirectionalrelation::ConceptE")
testbidirectionalrelation_ConceptF = Class(name="testbidirectionalrelation::ConceptF")

# testbidirectionalrelation_ConceptG class attributes and methods

# testbidirectionalrelation_ConceptA class attributes and methods

# testbidirectionalrelation_ConceptB class attributes and methods

# testbidirectionalrelation_ConceptC class attributes and methods

# testbidirectionalrelation_ConceptD class attributes and methods

# testbidirectionalrelation_ConceptE class attributes and methods

# testbidirectionalrelation_ConceptF class attributes and methods

# Relationships
conceptg9: BinaryAssociation = BinaryAssociation(
    name="conceptg9",
    ends={
        Property(name="testbidirectionalrelation_ConceptG", type=testbidirectionalrelation_ConceptA, multiplicity=Multiplicity(1, 1)),
        Property(name="testbidirectionalrelation_ConceptA10", type=testbidirectionalrelation_ConceptG, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
conceptc11: BinaryAssociation = BinaryAssociation(
    name="conceptc11",
    ends={
        Property(name="ConceptC", type=testbidirectionalrelation_ConceptB, multiplicity=Multiplicity(1, 1)),
        Property(name="conceptb", type=testbidirectionalrelation_ConceptC, multiplicity=Multiplicity(0, 1))
    }
)
conceptb12: BinaryAssociation = BinaryAssociation(
    name="conceptb12",
    ends={
        Property(name="ConceptB", type=testbidirectionalrelation_ConceptC, multiplicity=Multiplicity(1, 1)),
        Property(name="conceptc", type=testbidirectionalrelation_ConceptB, multiplicity=Multiplicity(0, 1))
    }
)
concepte13: BinaryAssociation = BinaryAssociation(
    name="concepte13",
    ends={
        Property(name="ConceptE", type=testbidirectionalrelation_ConceptD, multiplicity=Multiplicity(1, 1)),
        Property(name="conceptd", type=testbidirectionalrelation_ConceptE, multiplicity=Multiplicity(0, 1))
    }
)
conceptd14: BinaryAssociation = BinaryAssociation(
    name="conceptd14",
    ends={
        Property(name="ConceptD", type=testbidirectionalrelation_ConceptE, multiplicity=Multiplicity(1, 1)),
        Property(name="concepte", type=testbidirectionalrelation_ConceptD, multiplicity=Multiplicity(0, 9999))
    }
)
conceptg15: BinaryAssociation = BinaryAssociation(
    name="conceptg15",
    ends={
        Property(name="ConceptG", type=testbidirectionalrelation_ConceptF, multiplicity=Multiplicity(1, 1)),
        Property(name="conceptf", type=testbidirectionalrelation_ConceptG, multiplicity=Multiplicity(0, 9999))
    }
)
conceptf16: BinaryAssociation = BinaryAssociation(
    name="conceptf16",
    ends={
        Property(name="ConceptF", type=testbidirectionalrelation_ConceptG, multiplicity=Multiplicity(1, 1)),
        Property(name="conceptg", type=testbidirectionalrelation_ConceptF, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="testbidirectionalrelation",
    types={testbidirectionalrelation_ConceptG, testbidirectionalrelation_ConceptA, testbidirectionalrelation_ConceptB, testbidirectionalrelation_ConceptC, testbidirectionalrelation_ConceptD, testbidirectionalrelation_ConceptE, testbidirectionalrelation_ConceptF},
    associations={conceptg9, conceptb0, conceptc1, conceptd3, concepte5, conceptf7, conceptc11, conceptb12, concepte13, conceptd14, conceptg15, conceptf16},
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
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
Tristate: Enumeration = Enumeration(
    name="Tristate",
    literals={
            EnumerationLiteral(name="TRUE"),
			EnumerationLiteral(name="FALSE"),
			EnumerationLiteral(name="UNDEFINED")
    }
)

# Classes
sample_SampleClassC = Class(name="sample::SampleClassC")
sample_SampleClassB = Class(name="sample::SampleClassB")
sample_SampleClassA = Class(name="sample::SampleClassA")
SampleClassInterface = Class(name="SampleClassInterface")
sample_SampleClassInterface = Class(name="sample::SampleClassInterface", is_abstract=True)

# sample_SampleClassC class attributes and methods

# sample_SampleClassB class attributes and methods

# sample_SampleClassA class attributes and methods
sample_SampleClassA_sampleAttribute: Property = Property(name="sampleAttribute", type=StringType)
sample_SampleClassA.attributes={sample_SampleClassA_sampleAttribute}

# SampleClassInterface class attributes and methods

# sample_SampleClassInterface class attributes and methods
sample_SampleClassInterface_m_doSomething: Method = Method(name="doSomething", parameters={Parameter(name='input')}, type=StringType)
sample_SampleClassInterface.methods={sample_SampleClassInterface_m_doSomething}

# Relationships
A0: BinaryAssociation = BinaryAssociation(
    name="A0",
    ends={
        Property(name="sample_SampleClassA", type=sample_SampleClassC, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_SampleClassC", type=sample_SampleClassA, multiplicity=Multiplicity(0, 1))
    }
)
B1: BinaryAssociation = BinaryAssociation(
    name="B1",
    ends={
        Property(name="sample_SampleClassB", type=sample_SampleClassC, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_SampleClassC2", type=sample_SampleClassB, multiplicity=Multiplicity(0, 2))
    }
)

# Generalizations
gen_sample_SampleClassA_SampleClassInterface = Generalization(general=SampleClassInterface, specific=sample_SampleClassA)

# Domain Model
domain_model = DomainModel(
    name="sample",
    types={sample_SampleClassC, sample_SampleClassB, sample_SampleClassA, SampleClassInterface, sample_SampleClassInterface, Tristate},
    associations={A0, B1},
    generalizations={gen_sample_SampleClassA_SampleClassInterface},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
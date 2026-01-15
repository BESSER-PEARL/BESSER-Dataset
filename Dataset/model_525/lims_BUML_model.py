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
Gender: Enumeration = Enumeration(
    name="Gender",
    literals={
            EnumerationLiteral(name="UNKNOWN"),
			EnumerationLiteral(name="MALE"),
			EnumerationLiteral(name="FEMALE")
    }
)

# Classes
Lims_Family = Class(name="Lims::Family")
Lims_Individual = Class(name="Lims::Individual")
Lims_Laboratory = Class(name="Lims::Laboratory")
Lims_Sample = Class(name="Lims::Sample")
Lims_Run = Class(name="Lims::Run")
Lims_Sequencer = Class(name="Lims::Sequencer")
Lims_Sequenced = Class(name="Lims::Sequenced")

# Lims_Family class attributes and methods
Lims_Family_name: Property = Property(name="name", type=StringType)
Lims_Family.attributes={Lims_Family_name}

# Lims_Individual class attributes and methods
Lims_Individual_gender: Property = Property(name="gender", type=StringType)
Lims_Individual_name: Property = Property(name="name", type=StringType)
Lims_Individual.attributes={Lims_Individual_gender, Lims_Individual_name}

# Lims_Laboratory class attributes and methods

# Lims_Sample class attributes and methods
Lims_Sample_id: Property = Property(name="id", type=StringType)
Lims_Sample.attributes={Lims_Sample_id}

# Lims_Run class attributes and methods
Lims_Run_name: Property = Property(name="name", type=StringType)
Lims_Run_date: Property = Property(name="date", type=DateType)
Lims_Run.attributes={Lims_Run_date, Lims_Run_name}

# Lims_Sequencer class attributes and methods
Lims_Sequencer_name: Property = Property(name="name", type=StringType)
Lims_Sequencer.attributes={Lims_Sequencer_name}

# Lims_Sequenced class attributes and methods

# Relationships
individuals0: BinaryAssociation = BinaryAssociation(
    name="individuals0",
    ends={
        Property(name="Individual", type=Lims_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family", type=Lims_Individual, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
laboratory1: BinaryAssociation = BinaryAssociation(
    name="laboratory1",
    ends={
        Property(name="Laboratory", type=Lims_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="families", type=Lims_Laboratory, multiplicity=Multiplicity(1, 1))
    }
)
family5: BinaryAssociation = BinaryAssociation(
    name="family5",
    ends={
        Property(name="Family6", type=Lims_Individual, multiplicity=Multiplicity(1, 1)),
        Property(name="individuals", type=Lims_Family, multiplicity=Multiplicity(1, 1))
    }
)
Father8: BinaryAssociation = BinaryAssociation(
    name="Father8",
    ends={
        Property(name="Lims_Individual", type=Lims_Individual, multiplicity=Multiplicity(1, 1)),
        Property(name="Lims_Individual7", type=Lims_Individual, multiplicity=Multiplicity(0, 1))
    }
)
Mother10: BinaryAssociation = BinaryAssociation(
    name="Mother10",
    ends={
        Property(name="Lims_Individual11", type=Lims_Individual, multiplicity=Multiplicity(1, 1)),
        Property(name="Lims_Individual9", type=Lims_Individual, multiplicity=Multiplicity(0, 1))
    }
)
samples12: BinaryAssociation = BinaryAssociation(
    name="samples12",
    ends={
        Property(name="Sample", type=Lims_Individual, multiplicity=Multiplicity(1, 1)),
        Property(name="individual", type=Lims_Sample, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
runs13: BinaryAssociation = BinaryAssociation(
    name="runs13",
    ends={
        Property(name="Run", type=Lims_Sequencer, multiplicity=Multiplicity(1, 1)),
        Property(name="sequencer", type=Lims_Run, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
families2: BinaryAssociation = BinaryAssociation(
    name="families2",
    ends={
        Property(name="Family", type=Lims_Laboratory, multiplicity=Multiplicity(1, 1)),
        Property(name="laboratory", type=Lims_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequencers3: BinaryAssociation = BinaryAssociation(
    name="sequencers3",
    ends={
        Property(name="Sequencer", type=Lims_Laboratory, multiplicity=Multiplicity(1, 1)),
        Property(name="laboratory4", type=Lims_Sequencer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequencer17: BinaryAssociation = BinaryAssociation(
    name="sequencer17",
    ends={
        Property(name="Sequencer18", type=Lims_Run, multiplicity=Multiplicity(1, 1)),
        Property(name="runs", type=Lims_Sequencer, multiplicity=Multiplicity(1, 1))
    }
)
individual19: BinaryAssociation = BinaryAssociation(
    name="individual19",
    ends={
        Property(name="Individual20", type=Lims_Sample, multiplicity=Multiplicity(1, 1)),
        Property(name="samples", type=Lims_Individual, multiplicity=Multiplicity(1, 1))
    }
)
run21: BinaryAssociation = BinaryAssociation(
    name="run21",
    ends={
        Property(name="Run22", type=Lims_Sequenced, multiplicity=Multiplicity(1, 1)),
        Property(name="sequenced", type=Lims_Run, multiplicity=Multiplicity(1, 1))
    }
)
sample23: BinaryAssociation = BinaryAssociation(
    name="sample23",
    ends={
        Property(name="Lims_Sample", type=Lims_Sequenced, multiplicity=Multiplicity(1, 1)),
        Property(name="Lims_Sequenced", type=Lims_Sample, multiplicity=Multiplicity(1, 1))
    }
)
laboratory14: BinaryAssociation = BinaryAssociation(
    name="laboratory14",
    ends={
        Property(name="Laboratory15", type=Lims_Sequencer, multiplicity=Multiplicity(1, 1)),
        Property(name="sequencers", type=Lims_Laboratory, multiplicity=Multiplicity(1, 1))
    }
)
sequenced16: BinaryAssociation = BinaryAssociation(
    name="sequenced16",
    ends={
        Property(name="Sequenced", type=Lims_Run, multiplicity=Multiplicity(1, 1)),
        Property(name="run", type=Lims_Sequenced, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Lims",
    types={Lims_Family, Lims_Individual, Lims_Laboratory, Lims_Sample, Lims_Run, Lims_Sequencer, Lims_Sequenced, Gender},
    associations={individuals0, laboratory1, family5, Father8, Mother10, samples12, runs13, families2, sequencers3, sequencer17, individual19, run21, sample23, laboratory14, sequenced16},
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
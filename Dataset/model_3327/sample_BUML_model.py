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
sample_Then = Class(name="sample::Then")
sample_Story = Class(name="sample::Story")
sample_Scenario = Class(name="sample::Scenario")
sample_When = Class(name="sample::When")
sample_Given = Class(name="sample::Given")
sample_Sentence = Class(name="sample::Sentence")

# sample_Then class attributes and methods

# sample_Story class attributes and methods
sample_Story_Role: Property = Property(name="Role", type=StringType)
sample_Story_Feature: Property = Property(name="Feature", type=StringType)
sample_Story_Benefit: Property = Property(name="Benefit", type=StringType)
sample_Story_Title: Property = Property(name="Title", type=StringType)
sample_Story.attributes={sample_Story_Role, sample_Story_Feature, sample_Story_Title, sample_Story_Benefit}

# sample_Scenario class attributes and methods
sample_Scenario_Title: Property = Property(name="Title", type=StringType)
sample_Scenario.attributes={sample_Scenario_Title}

# sample_When class attributes and methods

# sample_Given class attributes and methods

# sample_Sentence class attributes and methods
sample_Sentence_Text: Property = Property(name="Text", type=StringType)
sample_Sentence.attributes={sample_Sentence_Text}

# Relationships
then5: BinaryAssociation = BinaryAssociation(
    name="then5",
    ends={
        Property(name="sample_Then", type=sample_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_Scenario6", type=sample_Then, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
scenarios0: BinaryAssociation = BinaryAssociation(
    name="scenarios0",
    ends={
        Property(name="sample_Scenario", type=sample_Story, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_Story", type=sample_Scenario, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
when1: BinaryAssociation = BinaryAssociation(
    name="when1",
    ends={
        Property(name="sample_When", type=sample_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_Scenario2", type=sample_When, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
given3: BinaryAssociation = BinaryAssociation(
    name="given3",
    ends={
        Property(name="sample_Given", type=sample_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_Scenario4", type=sample_Given, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sentence7: BinaryAssociation = BinaryAssociation(
    name="sentence7",
    ends={
        Property(name="sample_Sentence", type=sample_When, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_When8", type=sample_Sentence, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sentence9: BinaryAssociation = BinaryAssociation(
    name="sentence9",
    ends={
        Property(name="sample_Sentence11", type=sample_Given, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_Given10", type=sample_Sentence, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sentence12: BinaryAssociation = BinaryAssociation(
    name="sentence12",
    ends={
        Property(name="sample_Sentence14", type=sample_Then, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_Then13", type=sample_Sentence, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="sample",
    types={sample_Then, sample_Story, sample_Scenario, sample_When, sample_Given, sample_Sentence},
    associations={then5, scenarios0, when1, given3, sentence7, sentence9, sentence12},
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
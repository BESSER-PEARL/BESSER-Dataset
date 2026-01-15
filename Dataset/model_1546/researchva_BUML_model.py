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
researchva_Researcher = Class(name="researchva::Researcher")
researchva_Write = Class(name="researchva::Write")
researchva_Review = Class(name="researchva::Review")
researchva_Paper = Class(name="researchva::Paper")
researchva_Skill = Class(name="researchva::Skill")
Named = Class(name="Named")
researchva_Paragraph = Class(name="researchva::Paragraph")
Counted = Class(name="Counted")
researchva_ReviewNote = Class(name="researchva::ReviewNote")
Labelled = Class(name="Labelled")
researchva_PublicationStructure = Class(name="researchva::PublicationStructure")
researchva_Keyword = Class(name="researchva::Keyword")
researchva_Named = Class(name="researchva::Named", is_abstract=True)
researchva_Counted = Class(name="researchva::Counted", is_abstract=True)
researchva_Labelled = Class(name="researchva::Labelled", is_abstract=True)

# researchva_Researcher class attributes and methods
researchva_Researcher_name: Property = Property(name="name", type=StringType)
researchva_Researcher_forName: Property = Property(name="forName", type=StringType)
researchva_Researcher.attributes={researchva_Researcher_name, researchva_Researcher_forName}

# researchva_Write class attributes and methods
researchva_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
researchva_Write.attributes={researchva_Write_timeSpent}

# researchva_Review class attributes and methods
researchva_Review_date: Property = Property(name="date", type=DateType)
researchva_Review.attributes={researchva_Review_date}

# researchva_Paper class attributes and methods

# researchva_Skill class attributes and methods
researchva_Skill_description: Property = Property(name="description", type=StringType)
researchva_Skill.attributes={researchva_Skill_description}

# Named class attributes and methods

# researchva_Paragraph class attributes and methods
researchva_Paragraph_content: Property = Property(name="content", type=StringType)
researchva_Paragraph.attributes={researchva_Paragraph_content}

# Counted class attributes and methods

# researchva_ReviewNote class attributes and methods
researchva_ReviewNote_content: Property = Property(name="content", type=StringType)
researchva_ReviewNote.attributes={researchva_ReviewNote_content}

# Labelled class attributes and methods

# researchva_PublicationStructure class attributes and methods

# researchva_Keyword class attributes and methods
researchva_Keyword_word: Property = Property(name="word", type=StringType)
researchva_Keyword.attributes={researchva_Keyword_word}

# researchva_Named class attributes and methods
researchva_Named_name: Property = Property(name="name", type=StringType)
researchva_Named.attributes={researchva_Named_name}

# researchva_Counted class attributes and methods
researchva_Counted_id: Property = Property(name="id", type=IntegerType)
researchva_Counted.attributes={researchva_Counted_id}

# researchva_Labelled class attributes and methods
researchva_Labelled_lname: Property = Property(name="lname", type=StringType)
researchva_Labelled.attributes={researchva_Labelled_lname}

# Relationships
writes0: BinaryAssociation = BinaryAssociation(
    name="writes0",
    ends={
        Property(name="researchva_Write", type=researchva_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="researchva_Researcher", type=researchva_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews1: BinaryAssociation = BinaryAssociation(
    name="reviews1",
    ends={
        Property(name="researchva_Review", type=researchva_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="researchva_Researcher2", type=researchva_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_papers3: BinaryAssociation = BinaryAssociation(
    name="res_papers3",
    ends={
        Property(name="Paper", type=researchva_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=researchva_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills4: BinaryAssociation = BinaryAssociation(
    name="skills4",
    ends={
        Property(name="researchva_Skill", type=researchva_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="researchva_Researcher5", type=researchva_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs6: BinaryAssociation = BinaryAssociation(
    name="paragraphs6",
    ends={
        Property(name="researchva_Paragraph", type=researchva_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="researchva_Paper", type=researchva_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors7: BinaryAssociation = BinaryAssociation(
    name="authors7",
    ends={
        Property(name="Researcher", type=researchva_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=researchva_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
citedBy9: BinaryAssociation = BinaryAssociation(
    name="citedBy9",
    ends={
        Property(name="researchva_Paper10", type=researchva_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="researchva_Paper8", type=researchva_Paper, multiplicity=Multiplicity(0, 1))
    }
)
reviews11: BinaryAssociation = BinaryAssociation(
    name="reviews11",
    ends={
        Property(name="researchva_ReviewNote", type=researchva_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="researchva_Paragraph12", type=researchva_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraph13: BinaryAssociation = BinaryAssociation(
    name="paragraph13",
    ends={
        Property(name="researchva_Paragraph15", type=researchva_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="researchva_Write14", type=researchva_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
reviewNote16: BinaryAssociation = BinaryAssociation(
    name="reviewNote16",
    ends={
        Property(name="researchva_ReviewNote18", type=researchva_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="researchva_Review17", type=researchva_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
researchers19: BinaryAssociation = BinaryAssociation(
    name="researchers19",
    ends={
        Property(name="researchva_Researcher20", type=researchva_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="researchva_PublicationStructure", type=researchva_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers21: BinaryAssociation = BinaryAssociation(
    name="papers21",
    ends={
        Property(name="researchva_Paper23", type=researchva_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="researchva_PublicationStructure22", type=researchva_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allKeyWords24: BinaryAssociation = BinaryAssociation(
    name="allKeyWords24",
    ends={
        Property(name="researchva_Keyword", type=researchva_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="researchva_PublicationStructure25", type=researchva_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_researchva_Paper_Named = Generalization(general=Named, specific=researchva_Paper)
gen_researchva_Paragraph_Counted = Generalization(general=Counted, specific=researchva_Paragraph)
gen_researchva_Paragraph_Named = Generalization(general=Named, specific=researchva_Paragraph)
gen_researchva_ReviewNote_Named = Generalization(general=Named, specific=researchva_ReviewNote)
gen_researchva_Write_Labelled = Generalization(general=Labelled, specific=researchva_Write)
gen_researchva_Review_Labelled = Generalization(general=Labelled, specific=researchva_Review)
gen_researchva_PublicationStructure_Named = Generalization(general=Named, specific=researchva_PublicationStructure)
gen_researchva_Keyword_Named = Generalization(general=Named, specific=researchva_Keyword)

# Domain Model
domain_model = DomainModel(
    name="researchva",
    types={researchva_Researcher, researchva_Write, researchva_Review, researchva_Paper, researchva_Skill, Named, researchva_Paragraph, Counted, researchva_ReviewNote, Labelled, researchva_PublicationStructure, researchva_Keyword, researchva_Named, researchva_Counted, researchva_Labelled},
    associations={writes0, reviews1, res_papers3, skills4, paragraphs6, authors7, citedBy9, reviews11, paragraph13, reviewNote16, researchers19, papers21, allKeyWords24},
    generalizations={gen_researchva_Paper_Named, gen_researchva_Paragraph_Counted, gen_researchva_Paragraph_Named, gen_researchva_ReviewNote_Named, gen_researchva_Write_Labelled, gen_researchva_Review_Labelled, gen_researchva_PublicationStructure_Named, gen_researchva_Keyword_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
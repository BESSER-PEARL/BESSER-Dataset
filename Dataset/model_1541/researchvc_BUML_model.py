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
researchvc_Review = Class(name="researchvc::Review")
researchvc_Paper = Class(name="researchvc::Paper")
researchvc_Skill = Class(name="researchvc::Skill")
Named = Class(name="Named")
researchvc_Paragraph = Class(name="researchvc::Paragraph")
researchvc_Researcher = Class(name="researchvc::Researcher")
researchvc_Write = Class(name="researchvc::Write")
Counted = Class(name="Counted")
researchvc_ReviewNote = Class(name="researchvc::ReviewNote")
Labelled = Class(name="Labelled")
researchvc_PaperKeyword = Class(name="researchvc::PaperKeyword")
researchvc_PublicationStructure = Class(name="researchvc::PublicationStructure")
researchvc_Keyword = Class(name="researchvc::Keyword")
researchvc_Named = Class(name="researchvc::Named", is_abstract=True)
researchvc_Counted = Class(name="researchvc::Counted", is_abstract=True)
researchvc_Labelled = Class(name="researchvc::Labelled", is_abstract=True)

# researchvc_Review class attributes and methods
researchvc_Review_date: Property = Property(name="date", type=DateType)
researchvc_Review.attributes={researchvc_Review_date}

# researchvc_Paper class attributes and methods

# researchvc_Skill class attributes and methods
researchvc_Skill_description: Property = Property(name="description", type=StringType)
researchvc_Skill.attributes={researchvc_Skill_description}

# Named class attributes and methods

# researchvc_Paragraph class attributes and methods
researchvc_Paragraph_content: Property = Property(name="content", type=StringType)
researchvc_Paragraph.attributes={researchvc_Paragraph_content}

# researchvc_Researcher class attributes and methods
researchvc_Researcher_name: Property = Property(name="name", type=StringType)
researchvc_Researcher_forName: Property = Property(name="forName", type=StringType)
researchvc_Researcher.attributes={researchvc_Researcher_forName, researchvc_Researcher_name}

# researchvc_Write class attributes and methods
researchvc_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
researchvc_Write.attributes={researchvc_Write_timeSpent}

# Counted class attributes and methods

# researchvc_ReviewNote class attributes and methods
researchvc_ReviewNote_content: Property = Property(name="content", type=StringType)
researchvc_ReviewNote.attributes={researchvc_ReviewNote_content}

# Labelled class attributes and methods

# researchvc_PaperKeyword class attributes and methods
researchvc_PaperKeyword_weight: Property = Property(name="weight", type=IntegerType)
researchvc_PaperKeyword.attributes={researchvc_PaperKeyword_weight}

# researchvc_PublicationStructure class attributes and methods

# researchvc_Keyword class attributes and methods
researchvc_Keyword_word: Property = Property(name="word", type=StringType)
researchvc_Keyword.attributes={researchvc_Keyword_word}

# researchvc_Named class attributes and methods
researchvc_Named_name: Property = Property(name="name", type=StringType)
researchvc_Named.attributes={researchvc_Named_name}

# researchvc_Counted class attributes and methods
researchvc_Counted_id: Property = Property(name="id", type=IntegerType)
researchvc_Counted.attributes={researchvc_Counted_id}

# researchvc_Labelled class attributes and methods
researchvc_Labelled_lname: Property = Property(name="lname", type=StringType)
researchvc_Labelled.attributes={researchvc_Labelled_lname}

# Relationships
writes0: BinaryAssociation = BinaryAssociation(
    name="writes0",
    ends={
        Property(name="researchvc_Researcher", type=researchvc_Write, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="researchvc_Write", type=researchvc_Researcher, multiplicity=Multiplicity(1, 1))
    }
)
reviews1: BinaryAssociation = BinaryAssociation(
    name="reviews1",
    ends={
        Property(name="researchvc_Review", type=researchvc_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="researchvc_Researcher2", type=researchvc_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_papers3: BinaryAssociation = BinaryAssociation(
    name="res_papers3",
    ends={
        Property(name="Paper", type=researchvc_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=researchvc_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills4: BinaryAssociation = BinaryAssociation(
    name="skills4",
    ends={
        Property(name="researchvc_Skill", type=researchvc_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="researchvc_Researcher5", type=researchvc_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews13: BinaryAssociation = BinaryAssociation(
    name="reviews13",
    ends={
        Property(name="researchvc_ReviewNote", type=researchvc_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="researchvc_Paragraph14", type=researchvc_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs6: BinaryAssociation = BinaryAssociation(
    name="paragraphs6",
    ends={
        Property(name="researchvc_Paragraph", type=researchvc_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="researchvc_Paper", type=researchvc_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors7: BinaryAssociation = BinaryAssociation(
    name="authors7",
    ends={
        Property(name="Researcher", type=researchvc_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=researchvc_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
keywords8: BinaryAssociation = BinaryAssociation(
    name="keywords8",
    ends={
        Property(name="researchvc_PaperKeyword", type=researchvc_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="researchvc_Paper9", type=researchvc_PaperKeyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
citedBy11: BinaryAssociation = BinaryAssociation(
    name="citedBy11",
    ends={
        Property(name="researchvc_Paper12", type=researchvc_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="researchvc_Paper10", type=researchvc_Paper, multiplicity=Multiplicity(0, 1))
    }
)
researchers21: BinaryAssociation = BinaryAssociation(
    name="researchers21",
    ends={
        Property(name="researchvc_Researcher22", type=researchvc_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="researchvc_PublicationStructure", type=researchvc_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers23: BinaryAssociation = BinaryAssociation(
    name="papers23",
    ends={
        Property(name="researchvc_Paper25", type=researchvc_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="researchvc_PublicationStructure24", type=researchvc_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allKeyWords26: BinaryAssociation = BinaryAssociation(
    name="allKeyWords26",
    ends={
        Property(name="researchvc_Keyword", type=researchvc_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="researchvc_PublicationStructure27", type=researchvc_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraph15: BinaryAssociation = BinaryAssociation(
    name="paragraph15",
    ends={
        Property(name="researchvc_Paragraph17", type=researchvc_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="researchvc_Write16", type=researchvc_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
reviewNote18: BinaryAssociation = BinaryAssociation(
    name="reviewNote18",
    ends={
        Property(name="researchvc_ReviewNote20", type=researchvc_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="researchvc_Review19", type=researchvc_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
keyword28: BinaryAssociation = BinaryAssociation(
    name="keyword28",
    ends={
        Property(name="researchvc_Keyword30", type=researchvc_PaperKeyword, multiplicity=Multiplicity(1, 1)),
        Property(name="researchvc_PaperKeyword29", type=researchvc_Keyword, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_researchvc_Paper_Named = Generalization(general=Named, specific=researchvc_Paper)
gen_researchvc_Paragraph_Counted = Generalization(general=Counted, specific=researchvc_Paragraph)
gen_researchvc_Paragraph_Named = Generalization(general=Named, specific=researchvc_Paragraph)
gen_researchvc_ReviewNote_Named = Generalization(general=Named, specific=researchvc_ReviewNote)
gen_researchvc_Write_Labelled = Generalization(general=Labelled, specific=researchvc_Write)
gen_researchvc_PublicationStructure_Named = Generalization(general=Named, specific=researchvc_PublicationStructure)
gen_researchvc_Review_Labelled = Generalization(general=Labelled, specific=researchvc_Review)
gen_researchvc_Keyword_Named = Generalization(general=Named, specific=researchvc_Keyword)

# Domain Model
domain_model = DomainModel(
    name="researchvc",
    types={researchvc_Review, researchvc_Paper, researchvc_Skill, Named, researchvc_Paragraph, researchvc_Researcher, researchvc_Write, Counted, researchvc_ReviewNote, Labelled, researchvc_PaperKeyword, researchvc_PublicationStructure, researchvc_Keyword, researchvc_Named, researchvc_Counted, researchvc_Labelled},
    associations={writes0, reviews1, res_papers3, skills4, reviews13, paragraphs6, authors7, keywords8, citedBy11, researchers21, papers23, allKeyWords26, paragraph15, reviewNote18, keyword28},
    generalizations={gen_researchvc_Paper_Named, gen_researchvc_Paragraph_Counted, gen_researchvc_Paragraph_Named, gen_researchvc_ReviewNote_Named, gen_researchvc_Write_Labelled, gen_researchvc_PublicationStructure_Named, gen_researchvc_Review_Labelled, gen_researchvc_Keyword_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
tp4_PublicationProcess = Class(name="tp4::PublicationProcess")
Named = Class(name="Named")
tp4_Phases = Class(name="tp4::Phases")
tp4_Researcher = Class(name="tp4::Researcher")
tp4_Write = Class(name="tp4::Write")
tp4_Skill = Class(name="tp4::Skill")
tp4_Position = Class(name="tp4::Position")
tp4_Paragraph = Class(name="tp4::Paragraph")
tp4_Progress = Class(name="tp4::Progress")
tp4_Review = Class(name="tp4::Review")
tp4_Paper = Class(name="tp4::Paper")
Counted = Class(name="Counted")
tp4_ReviewNote = Class(name="tp4::ReviewNote")
Labelled = Class(name="Labelled")
tp4_Keyword = Class(name="tp4::Keyword")
tp4_PublicationStructure = Class(name="tp4::PublicationStructure")
tp4_PublicationSystem = Class(name="tp4::PublicationSystem")
tp4_Named = Class(name="tp4::Named", is_abstract=True)
tp4_Counted = Class(name="tp4::Counted", is_abstract=True)
tp4_Labelled = Class(name="tp4::Labelled", is_abstract=True)

# tp4_PublicationProcess class attributes and methods
tp4_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
tp4_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
tp4_PublicationProcess.attributes={tp4_PublicationProcess_maxTime, tp4_PublicationProcess_minTime}

# Named class attributes and methods

# tp4_Phases class attributes and methods
tp4_Phases_name: Property = Property(name="name", type=StringType)
tp4_Phases.attributes={tp4_Phases_name}

# tp4_Researcher class attributes and methods
tp4_Researcher_name: Property = Property(name="name", type=StringType)
tp4_Researcher_forName: Property = Property(name="forName", type=StringType)
tp4_Researcher.attributes={tp4_Researcher_name, tp4_Researcher_forName}

# tp4_Write class attributes and methods
tp4_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
tp4_Write.attributes={tp4_Write_timeSpent}

# tp4_Skill class attributes and methods
tp4_Skill_description: Property = Property(name="description", type=StringType)
tp4_Skill.attributes={tp4_Skill_description}

# tp4_Position class attributes and methods
tp4_Position_description: Property = Property(name="description", type=StringType)
tp4_Position.attributes={tp4_Position_description}

# tp4_Paragraph class attributes and methods
tp4_Paragraph_content: Property = Property(name="content", type=StringType)
tp4_Paragraph.attributes={tp4_Paragraph_content}

# tp4_Progress class attributes and methods
tp4_Progress_percent: Property = Property(name="percent", type=IntegerType)
tp4_Progress.attributes={tp4_Progress_percent}

# tp4_Review class attributes and methods
tp4_Review_date: Property = Property(name="date", type=DateType)
tp4_Review.attributes={tp4_Review_date}

# tp4_Paper class attributes and methods

# Counted class attributes and methods

# tp4_ReviewNote class attributes and methods
tp4_ReviewNote_content: Property = Property(name="content", type=StringType)
tp4_ReviewNote.attributes={tp4_ReviewNote_content}

# Labelled class attributes and methods

# tp4_Keyword class attributes and methods
tp4_Keyword_description: Property = Property(name="description", type=StringType)
tp4_Keyword.attributes={tp4_Keyword_description}

# tp4_PublicationStructure class attributes and methods

# tp4_PublicationSystem class attributes and methods

# tp4_Named class attributes and methods
tp4_Named_name: Property = Property(name="name", type=StringType)
tp4_Named.attributes={tp4_Named_name}

# tp4_Counted class attributes and methods
tp4_Counted_id: Property = Property(name="id", type=IntegerType)
tp4_Counted.attributes={tp4_Counted_id}

# tp4_Labelled class attributes and methods
tp4_Labelled_lname: Property = Property(name="lname", type=StringType)
tp4_Labelled.attributes={tp4_Labelled_lname}

# Relationships
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="tp4_Phases", type=tp4_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="tp4_PublicationProcess", type=tp4_Phases, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
skills5: BinaryAssociation = BinaryAssociation(
    name="skills5",
    ends={
        Property(name="tp4_Skill", type=tp4_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="tp4_Researcher6", type=tp4_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
position7: BinaryAssociation = BinaryAssociation(
    name="position7",
    ends={
        Property(name="tp4_Position", type=tp4_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="tp4_Researcher8", type=tp4_Position, multiplicity=Multiplicity(0, 1))
    }
)
paragraphs9: BinaryAssociation = BinaryAssociation(
    name="paragraphs9",
    ends={
        Property(name="tp4_Paragraph", type=tp4_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="tp4_Paper", type=tp4_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writes1: BinaryAssociation = BinaryAssociation(
    name="writes1",
    ends={
        Property(name="tp4_Write", type=tp4_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="tp4_Researcher", type=tp4_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews2: BinaryAssociation = BinaryAssociation(
    name="reviews2",
    ends={
        Property(name="tp4_Review", type=tp4_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="tp4_Researcher3", type=tp4_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_papers4: BinaryAssociation = BinaryAssociation(
    name="res_papers4",
    ends={
        Property(name="Paper", type=tp4_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=tp4_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
reviews14: BinaryAssociation = BinaryAssociation(
    name="reviews14",
    ends={
        Property(name="tp4_ReviewNote", type=tp4_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="tp4_Paragraph15", type=tp4_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
progress10: BinaryAssociation = BinaryAssociation(
    name="progress10",
    ends={
        Property(name="Progress", type=tp4_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=tp4_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors11: BinaryAssociation = BinaryAssociation(
    name="authors11",
    ends={
        Property(name="Researcher", type=tp4_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=tp4_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
keywords12: BinaryAssociation = BinaryAssociation(
    name="keywords12",
    ends={
        Property(name="tp4_Keyword", type=tp4_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="tp4_Paper13", type=tp4_Keyword, multiplicity=Multiplicity(0, 9999))
    }
)
process16: BinaryAssociation = BinaryAssociation(
    name="process16",
    ends={
        Property(name="tp4_Progress", type=tp4_PublicationProcess, multiplicity=Multiplicity(0, 1)),
        Property(name="tp4_PublicationProcess17", type=tp4_Progress, multiplicity=Multiplicity(1, 1))
    }
)
paper18: BinaryAssociation = BinaryAssociation(
    name="paper18",
    ends={
        Property(name="Paper19", type=tp4_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="progress", type=tp4_Paper, multiplicity=Multiplicity(0, 1))
    }
)
paragraph20: BinaryAssociation = BinaryAssociation(
    name="paragraph20",
    ends={
        Property(name="tp4_Paragraph22", type=tp4_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="tp4_Write21", type=tp4_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
reviewNote23: BinaryAssociation = BinaryAssociation(
    name="reviewNote23",
    ends={
        Property(name="tp4_Review24", type=tp4_ReviewNote, multiplicity=Multiplicity(0, 1)),
        Property(name="tp4_ReviewNote25", type=tp4_Review, multiplicity=Multiplicity(1, 1))
    }
)
researchers26: BinaryAssociation = BinaryAssociation(
    name="researchers26",
    ends={
        Property(name="tp4_Researcher27", type=tp4_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="tp4_PublicationStructure", type=tp4_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers28: BinaryAssociation = BinaryAssociation(
    name="papers28",
    ends={
        Property(name="tp4_Paper30", type=tp4_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="tp4_PublicationStructure29", type=tp4_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processView31: BinaryAssociation = BinaryAssociation(
    name="processView31",
    ends={
        Property(name="tp4_PublicationProcess32", type=tp4_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tp4_PublicationSystem", type=tp4_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuralView33: BinaryAssociation = BinaryAssociation(
    name="structuralView33",
    ends={
        Property(name="tp4_PublicationSystem34", type=tp4_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="tp4_PublicationStructure35", type=tp4_PublicationSystem, multiplicity=Multiplicity(1, 1))
    }
)
positions36: BinaryAssociation = BinaryAssociation(
    name="positions36",
    ends={
        Property(name="tp4_Position38", type=tp4_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tp4_PublicationSystem37", type=tp4_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allKeywords39: BinaryAssociation = BinaryAssociation(
    name="allKeywords39",
    ends={
        Property(name="tp4_Keyword41", type=tp4_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="tp4_PublicationSystem40", type=tp4_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent43: BinaryAssociation = BinaryAssociation(
    name="parent43",
    ends={
        Property(name="tp4_Position44", type=tp4_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="tp4_Position42", type=tp4_Position, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_tp4_PublicationProcess_Named = Generalization(general=Named, specific=tp4_PublicationProcess)
gen_tp4_Paper_Named = Generalization(general=Named, specific=tp4_Paper)
gen_tp4_Paragraph_Counted = Generalization(general=Counted, specific=tp4_Paragraph)
gen_tp4_Paragraph_Named = Generalization(general=Named, specific=tp4_Paragraph)
gen_tp4_ReviewNote_Named = Generalization(general=Named, specific=tp4_ReviewNote)
gen_tp4_Progress_Labelled = Generalization(general=Labelled, specific=tp4_Progress)
gen_tp4_Write_Labelled = Generalization(general=Labelled, specific=tp4_Write)
gen_tp4_Review_Labelled = Generalization(general=Labelled, specific=tp4_Review)
gen_tp4_PublicationStructure_Named = Generalization(general=Named, specific=tp4_PublicationStructure)
gen_tp4_PublicationSystem_Named = Generalization(general=Named, specific=tp4_PublicationSystem)
gen_tp4_Keyword_Named = Generalization(general=Named, specific=tp4_Keyword)
gen_tp4_Position_Named = Generalization(general=Named, specific=tp4_Position)

# Domain Model
domain_model = DomainModel(
    name="tp4",
    types={tp4_PublicationProcess, Named, tp4_Phases, tp4_Researcher, tp4_Write, tp4_Skill, tp4_Position, tp4_Paragraph, tp4_Progress, tp4_Review, tp4_Paper, Counted, tp4_ReviewNote, Labelled, tp4_Keyword, tp4_PublicationStructure, tp4_PublicationSystem, tp4_Named, tp4_Counted, tp4_Labelled},
    associations={phases0, skills5, position7, paragraphs9, writes1, reviews2, res_papers4, reviews14, progress10, authors11, keywords12, process16, paper18, paragraph20, reviewNote23, researchers26, papers28, processView31, structuralView33, positions36, allKeywords39, parent43},
    generalizations={gen_tp4_PublicationProcess_Named, gen_tp4_Paper_Named, gen_tp4_Paragraph_Counted, gen_tp4_Paragraph_Named, gen_tp4_ReviewNote_Named, gen_tp4_Progress_Labelled, gen_tp4_Write_Labelled, gen_tp4_Review_Labelled, gen_tp4_PublicationStructure_Named, gen_tp4_PublicationSystem_Named, gen_tp4_Keyword_Named, gen_tp4_Position_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
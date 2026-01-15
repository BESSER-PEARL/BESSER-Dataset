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
SequenceType: Enumeration = Enumeration(
    name="SequenceType",
    literals={
            EnumerationLiteral(name="startToStart"),
			EnumerationLiteral(name="finishToStart"),
			EnumerationLiteral(name="startToFinish"),
			EnumerationLiteral(name="finishToFinish")
    }
)

# Classes
publication2014b_PublicationPhase = Class(name="publication2014b::PublicationPhase")
publication2014b_Rule = Class(name="publication2014b::Rule")
publication2014b_Sequence = Class(name="publication2014b::Sequence")
publication2014b_Researcher = Class(name="publication2014b::Researcher")
publication2014b_PublicationProcess = Class(name="publication2014b::PublicationProcess")
Named = Class(name="Named")
publication2014b_Write = Class(name="publication2014b::Write")
publication2014b_Review = Class(name="publication2014b::Review")
publication2014b_Paper = Class(name="publication2014b::Paper")
Counted = Class(name="Counted")
publication2014b_ReviewNote = Class(name="publication2014b::ReviewNote")
publication2014b_Paragraph = Class(name="publication2014b::Paragraph")
publication2014b_Progress = Class(name="publication2014b::Progress")
publication2014b_PublicationStructure = Class(name="publication2014b::PublicationStructure")
Labelled = Class(name="Labelled")
publication2014b_PublicationSystem = Class(name="publication2014b::PublicationSystem")
publication2014b_Named = Class(name="publication2014b::Named", is_abstract=True)
publication2014b_Counted = Class(name="publication2014b::Counted", is_abstract=True)
publication2014b_Labelled = Class(name="publication2014b::Labelled", is_abstract=True)

# publication2014b_PublicationPhase class attributes and methods
publication2014b_PublicationPhase_name: Property = Property(name="name", type=StringType)
publication2014b_PublicationPhase_minTime: Property = Property(name="minTime", type=IntegerType)
publication2014b_PublicationPhase_maxTime: Property = Property(name="maxTime", type=IntegerType)
publication2014b_PublicationPhase.attributes={publication2014b_PublicationPhase_name, publication2014b_PublicationPhase_maxTime, publication2014b_PublicationPhase_minTime}

# publication2014b_Rule class attributes and methods
publication2014b_Rule_text: Property = Property(name="text", type=StringType)
publication2014b_Rule_key: Property = Property(name="key", type=StringType)
publication2014b_Rule.attributes={publication2014b_Rule_key, publication2014b_Rule_text}

# publication2014b_Sequence class attributes and methods
publication2014b_Sequence_sequenceType: Property = Property(name="sequenceType", type=StringType)
publication2014b_Sequence.attributes={publication2014b_Sequence_sequenceType}

# publication2014b_Researcher class attributes and methods
publication2014b_Researcher_name: Property = Property(name="name", type=StringType)
publication2014b_Researcher_forName: Property = Property(name="forName", type=StringType)
publication2014b_Researcher_position: Property = Property(name="position", type=StringType)
publication2014b_Researcher.attributes={publication2014b_Researcher_name, publication2014b_Researcher_position, publication2014b_Researcher_forName}

# publication2014b_PublicationProcess class attributes and methods
publication2014b_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
publication2014b_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
publication2014b_PublicationProcess.attributes={publication2014b_PublicationProcess_maxTime, publication2014b_PublicationProcess_minTime}

# Named class attributes and methods

# publication2014b_Write class attributes and methods

# publication2014b_Review class attributes and methods

# publication2014b_Paper class attributes and methods

# Counted class attributes and methods

# publication2014b_ReviewNote class attributes and methods
publication2014b_ReviewNote_content: Property = Property(name="content", type=StringType)
publication2014b_ReviewNote.attributes={publication2014b_ReviewNote_content}

# publication2014b_Paragraph class attributes and methods
publication2014b_Paragraph_content: Property = Property(name="content", type=StringType)
publication2014b_Paragraph.attributes={publication2014b_Paragraph_content}

# publication2014b_Progress class attributes and methods
publication2014b_Progress_percent: Property = Property(name="percent", type=IntegerType)
publication2014b_Progress_time: Property = Property(name="time", type=IntegerType)
publication2014b_Progress.attributes={publication2014b_Progress_time, publication2014b_Progress_percent}

# publication2014b_PublicationStructure class attributes and methods

# Labelled class attributes and methods

# publication2014b_PublicationSystem class attributes and methods

# publication2014b_Named class attributes and methods
publication2014b_Named_name: Property = Property(name="name", type=StringType)
publication2014b_Named.attributes={publication2014b_Named_name}

# publication2014b_Counted class attributes and methods
publication2014b_Counted_id: Property = Property(name="id", type=IntegerType)
publication2014b_Counted.attributes={publication2014b_Counted_id}

# publication2014b_Labelled class attributes and methods
publication2014b_Labelled_lname: Property = Property(name="lname", type=StringType)
publication2014b_Labelled.attributes={publication2014b_Labelled_lname}

# Relationships
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="publication2014b_PublicationPhase", type=publication2014b_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014b_PublicationProcess", type=publication2014b_PublicationPhase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publicationRules1: BinaryAssociation = BinaryAssociation(
    name="publicationRules1",
    ends={
        Property(name="publication2014b_Rule", type=publication2014b_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014b_PublicationProcess2", type=publication2014b_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linksToSuccessors3: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessors3",
    ends={
        Property(name="publication2014b_Sequence", type=publication2014b_PublicationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014b_PublicationPhase4", type=publication2014b_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
neededPerson5: BinaryAssociation = BinaryAssociation(
    name="neededPerson5",
    ends={
        Property(name="Researcher", type=publication2014b_PublicationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="phaseParticipation", type=publication2014b_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
rules6: BinaryAssociation = BinaryAssociation(
    name="rules6",
    ends={
        Property(name="publication2014b_Rule8", type=publication2014b_PublicationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014b_PublicationPhase7", type=publication2014b_Rule, multiplicity=Multiplicity(0, 9999))
    }
)
phaseParticipation15: BinaryAssociation = BinaryAssociation(
    name="phaseParticipation15",
    ends={
        Property(name="PublicationPhase", type=publication2014b_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="neededPerson", type=publication2014b_PublicationPhase, multiplicity=Multiplicity(0, 9999))
    }
)
writes16: BinaryAssociation = BinaryAssociation(
    name="writes16",
    ends={
        Property(name="publication2014b_Write", type=publication2014b_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014b_Researcher", type=publication2014b_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews17: BinaryAssociation = BinaryAssociation(
    name="reviews17",
    ends={
        Property(name="publication2014b_Review", type=publication2014b_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014b_Researcher18", type=publication2014b_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers19: BinaryAssociation = BinaryAssociation(
    name="papers19",
    ends={
        Property(name="Paper", type=publication2014b_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=publication2014b_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
successor9: BinaryAssociation = BinaryAssociation(
    name="successor9",
    ends={
        Property(name="publication2014b_PublicationPhase11", type=publication2014b_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014b_Sequence10", type=publication2014b_PublicationPhase, multiplicity=Multiplicity(1, 1))
    }
)
predecessor12: BinaryAssociation = BinaryAssociation(
    name="predecessor12",
    ends={
        Property(name="publication2014b_PublicationPhase14", type=publication2014b_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014b_Sequence13", type=publication2014b_PublicationPhase, multiplicity=Multiplicity(1, 1))
    }
)
authors22: BinaryAssociation = BinaryAssociation(
    name="authors22",
    ends={
        Property(name="Researcher23", type=publication2014b_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="papers", type=publication2014b_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
reviews24: BinaryAssociation = BinaryAssociation(
    name="reviews24",
    ends={
        Property(name="publication2014b_ReviewNote", type=publication2014b_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014b_Paragraph25", type=publication2014b_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs20: BinaryAssociation = BinaryAssociation(
    name="paragraphs20",
    ends={
        Property(name="publication2014b_Paragraph", type=publication2014b_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014b_Paper", type=publication2014b_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
progress21: BinaryAssociation = BinaryAssociation(
    name="progress21",
    ends={
        Property(name="Progress", type=publication2014b_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=publication2014b_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paper28: BinaryAssociation = BinaryAssociation(
    name="paper28",
    ends={
        Property(name="Paper29", type=publication2014b_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="progress", type=publication2014b_Paper, multiplicity=Multiplicity(0, 1))
    }
)
paragraph30: BinaryAssociation = BinaryAssociation(
    name="paragraph30",
    ends={
        Property(name="publication2014b_Paragraph32", type=publication2014b_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014b_Write31", type=publication2014b_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
reviewNote33: BinaryAssociation = BinaryAssociation(
    name="reviewNote33",
    ends={
        Property(name="publication2014b_ReviewNote35", type=publication2014b_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014b_Review34", type=publication2014b_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
process26: BinaryAssociation = BinaryAssociation(
    name="process26",
    ends={
        Property(name="publication2014b_PublicationProcess27", type=publication2014b_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014b_Progress", type=publication2014b_PublicationProcess, multiplicity=Multiplicity(0, 1))
    }
)
processView41: BinaryAssociation = BinaryAssociation(
    name="processView41",
    ends={
        Property(name="publication2014b_PublicationProcess42", type=publication2014b_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014b_PublicationSystem", type=publication2014b_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuralView43: BinaryAssociation = BinaryAssociation(
    name="structuralView43",
    ends={
        Property(name="publication2014b_PublicationStructure45", type=publication2014b_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014b_PublicationSystem44", type=publication2014b_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
researchers36: BinaryAssociation = BinaryAssociation(
    name="researchers36",
    ends={
        Property(name="publication2014b_Researcher37", type=publication2014b_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014b_PublicationStructure", type=publication2014b_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers38: BinaryAssociation = BinaryAssociation(
    name="papers38",
    ends={
        Property(name="publication2014b_Paper40", type=publication2014b_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014b_PublicationStructure39", type=publication2014b_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_publication2014b_PublicationProcess_Named = Generalization(general=Named, specific=publication2014b_PublicationProcess)
gen_publication2014b_Paper_Named = Generalization(general=Named, specific=publication2014b_Paper)
gen_publication2014b_Paragraph_Counted = Generalization(general=Counted, specific=publication2014b_Paragraph)
gen_publication2014b_Paragraph_Named = Generalization(general=Named, specific=publication2014b_Paragraph)
gen_publication2014b_ReviewNote_Named = Generalization(general=Named, specific=publication2014b_ReviewNote)
gen_publication2014b_Write_Labelled = Generalization(general=Labelled, specific=publication2014b_Write)
gen_publication2014b_Review_Labelled = Generalization(general=Labelled, specific=publication2014b_Review)
gen_publication2014b_PublicationStructure_Named = Generalization(general=Named, specific=publication2014b_PublicationStructure)
gen_publication2014b_Progress_Labelled = Generalization(general=Labelled, specific=publication2014b_Progress)

# Domain Model
domain_model = DomainModel(
    name="publication2014b",
    types={publication2014b_PublicationPhase, publication2014b_Rule, publication2014b_Sequence, publication2014b_Researcher, publication2014b_PublicationProcess, Named, publication2014b_Write, publication2014b_Review, publication2014b_Paper, Counted, publication2014b_ReviewNote, publication2014b_Paragraph, publication2014b_Progress, publication2014b_PublicationStructure, Labelled, publication2014b_PublicationSystem, publication2014b_Named, publication2014b_Counted, publication2014b_Labelled, SequenceType},
    associations={phases0, publicationRules1, linksToSuccessors3, neededPerson5, rules6, phaseParticipation15, writes16, reviews17, papers19, successor9, predecessor12, authors22, reviews24, paragraphs20, progress21, paper28, paragraph30, reviewNote33, process26, processView41, structuralView43, researchers36, papers38},
    generalizations={gen_publication2014b_PublicationProcess_Named, gen_publication2014b_Paper_Named, gen_publication2014b_Paragraph_Counted, gen_publication2014b_Paragraph_Named, gen_publication2014b_ReviewNote_Named, gen_publication2014b_Write_Labelled, gen_publication2014b_Review_Labelled, gen_publication2014b_PublicationStructure_Named, gen_publication2014b_Progress_Labelled},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
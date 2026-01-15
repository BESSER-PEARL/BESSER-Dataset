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
publication2014c_Sequence = Class(name="publication2014c::Sequence")
publication2014c_PublicationProcess = Class(name="publication2014c::PublicationProcess")
Named = Class(name="Named")
publication2014c_PublicationPhase = Class(name="publication2014c::PublicationPhase")
publication2014c_Rule = Class(name="publication2014c::Rule")
publication2014c_Write = Class(name="publication2014c::Write")
publication2014c_Review = Class(name="publication2014c::Review")
publication2014c_Paper = Class(name="publication2014c::Paper")
publication2014c_Researcher = Class(name="publication2014c::Researcher")
publication2014c_PublicationStructure = Class(name="publication2014c::PublicationStructure")
publication2014c_Paragraph = Class(name="publication2014c::Paragraph")
publication2014c_Progress = Class(name="publication2014c::Progress")
Counted = Class(name="Counted")
publication2014c_PublicationSystem = Class(name="publication2014c::PublicationSystem")
publication2014c_ReviewNote = Class(name="publication2014c::ReviewNote")
publication2014c_Named = Class(name="publication2014c::Named", is_abstract=True)
Labelled = Class(name="Labelled")
publication2014c_Labelled = Class(name="publication2014c::Labelled", is_abstract=True)
publication2014c_Counted = Class(name="publication2014c::Counted", is_abstract=True)

# publication2014c_Sequence class attributes and methods
publication2014c_Sequence_sequenceType: Property = Property(name="sequenceType", type=StringType)
publication2014c_Sequence.attributes={publication2014c_Sequence_sequenceType}

# publication2014c_PublicationProcess class attributes and methods
publication2014c_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
publication2014c_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
publication2014c_PublicationProcess.attributes={publication2014c_PublicationProcess_maxTime, publication2014c_PublicationProcess_minTime}

# Named class attributes and methods

# publication2014c_PublicationPhase class attributes and methods
publication2014c_PublicationPhase_name: Property = Property(name="name", type=StringType)
publication2014c_PublicationPhase_minTime: Property = Property(name="minTime", type=IntegerType)
publication2014c_PublicationPhase_maxTime: Property = Property(name="maxTime", type=IntegerType)
publication2014c_PublicationPhase.attributes={publication2014c_PublicationPhase_maxTime, publication2014c_PublicationPhase_minTime, publication2014c_PublicationPhase_name}

# publication2014c_Rule class attributes and methods
publication2014c_Rule_text: Property = Property(name="text", type=StringType)
publication2014c_Rule_key: Property = Property(name="key", type=StringType)
publication2014c_Rule.attributes={publication2014c_Rule_text, publication2014c_Rule_key}

# publication2014c_Write class attributes and methods

# publication2014c_Review class attributes and methods

# publication2014c_Paper class attributes and methods

# publication2014c_Researcher class attributes and methods
publication2014c_Researcher_name: Property = Property(name="name", type=StringType)
publication2014c_Researcher_forName: Property = Property(name="forName", type=StringType)
publication2014c_Researcher_position: Property = Property(name="position", type=StringType)
publication2014c_Researcher.attributes={publication2014c_Researcher_name, publication2014c_Researcher_forName, publication2014c_Researcher_position}

# publication2014c_PublicationStructure class attributes and methods

# publication2014c_Paragraph class attributes and methods
publication2014c_Paragraph_content: Property = Property(name="content", type=StringType)
publication2014c_Paragraph.attributes={publication2014c_Paragraph_content}

# publication2014c_Progress class attributes and methods
publication2014c_Progress_percent: Property = Property(name="percent", type=IntegerType)
publication2014c_Progress_time: Property = Property(name="time", type=IntegerType)
publication2014c_Progress.attributes={publication2014c_Progress_time, publication2014c_Progress_percent}

# Counted class attributes and methods

# publication2014c_PublicationSystem class attributes and methods

# publication2014c_ReviewNote class attributes and methods
publication2014c_ReviewNote_content: Property = Property(name="content", type=StringType)
publication2014c_ReviewNote.attributes={publication2014c_ReviewNote_content}

# publication2014c_Named class attributes and methods
publication2014c_Named_name: Property = Property(name="name", type=StringType)
publication2014c_Named.attributes={publication2014c_Named_name}

# Labelled class attributes and methods

# publication2014c_Labelled class attributes and methods
publication2014c_Labelled_lname: Property = Property(name="lname", type=StringType)
publication2014c_Labelled.attributes={publication2014c_Labelled_lname}

# publication2014c_Counted class attributes and methods
publication2014c_Counted_id: Property = Property(name="id", type=IntegerType)
publication2014c_Counted.attributes={publication2014c_Counted_id}

# Relationships
linksToSuccessors3: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessors3",
    ends={
        Property(name="publication2014c_Sequence", type=publication2014c_PublicationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014c_PublicationPhase4", type=publication2014c_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="publication2014c_PublicationPhase", type=publication2014c_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014c_PublicationProcess", type=publication2014c_PublicationPhase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publicationRules1: BinaryAssociation = BinaryAssociation(
    name="publicationRules1",
    ends={
        Property(name="publication2014c_Rule", type=publication2014c_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014c_PublicationProcess2", type=publication2014c_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writes16: BinaryAssociation = BinaryAssociation(
    name="writes16",
    ends={
        Property(name="publication2014c_Write", type=publication2014c_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014c_Researcher", type=publication2014c_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews17: BinaryAssociation = BinaryAssociation(
    name="reviews17",
    ends={
        Property(name="publication2014c_Review", type=publication2014c_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014c_Researcher18", type=publication2014c_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers19: BinaryAssociation = BinaryAssociation(
    name="papers19",
    ends={
        Property(name="Paper", type=publication2014c_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=publication2014c_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
neededPerson5: BinaryAssociation = BinaryAssociation(
    name="neededPerson5",
    ends={
        Property(name="Researcher", type=publication2014c_PublicationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="phaseParticipation", type=publication2014c_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
rules6: BinaryAssociation = BinaryAssociation(
    name="rules6",
    ends={
        Property(name="publication2014c_Rule8", type=publication2014c_PublicationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014c_PublicationPhase7", type=publication2014c_Rule, multiplicity=Multiplicity(0, 9999))
    }
)
successor9: BinaryAssociation = BinaryAssociation(
    name="successor9",
    ends={
        Property(name="publication2014c_PublicationPhase11", type=publication2014c_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014c_Sequence10", type=publication2014c_PublicationPhase, multiplicity=Multiplicity(1, 1))
    }
)
predecessor12: BinaryAssociation = BinaryAssociation(
    name="predecessor12",
    ends={
        Property(name="publication2014c_PublicationPhase14", type=publication2014c_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014c_Sequence13", type=publication2014c_PublicationPhase, multiplicity=Multiplicity(1, 1))
    }
)
phaseParticipation15: BinaryAssociation = BinaryAssociation(
    name="phaseParticipation15",
    ends={
        Property(name="PublicationPhase", type=publication2014c_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="neededPerson", type=publication2014c_PublicationPhase, multiplicity=Multiplicity(0, 9999))
    }
)
paper28: BinaryAssociation = BinaryAssociation(
    name="paper28",
    ends={
        Property(name="Paper29", type=publication2014c_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="progress", type=publication2014c_Paper, multiplicity=Multiplicity(0, 1))
    }
)
paragraph30: BinaryAssociation = BinaryAssociation(
    name="paragraph30",
    ends={
        Property(name="publication2014c_Paragraph32", type=publication2014c_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014c_Write31", type=publication2014c_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
reviewNote33: BinaryAssociation = BinaryAssociation(
    name="reviewNote33",
    ends={
        Property(name="publication2014c_ReviewNote35", type=publication2014c_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014c_Review34", type=publication2014c_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
paragraphs20: BinaryAssociation = BinaryAssociation(
    name="paragraphs20",
    ends={
        Property(name="publication2014c_Paragraph", type=publication2014c_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014c_Paper", type=publication2014c_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
progress21: BinaryAssociation = BinaryAssociation(
    name="progress21",
    ends={
        Property(name="Progress", type=publication2014c_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=publication2014c_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors22: BinaryAssociation = BinaryAssociation(
    name="authors22",
    ends={
        Property(name="Researcher23", type=publication2014c_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="papers", type=publication2014c_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
researchers36: BinaryAssociation = BinaryAssociation(
    name="researchers36",
    ends={
        Property(name="publication2014c_Researcher37", type=publication2014c_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014c_PublicationStructure", type=publication2014c_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers38: BinaryAssociation = BinaryAssociation(
    name="papers38",
    ends={
        Property(name="publication2014c_Paper40", type=publication2014c_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014c_PublicationStructure39", type=publication2014c_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processView41: BinaryAssociation = BinaryAssociation(
    name="processView41",
    ends={
        Property(name="publication2014c_PublicationProcess42", type=publication2014c_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014c_PublicationSystem", type=publication2014c_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reviews24: BinaryAssociation = BinaryAssociation(
    name="reviews24",
    ends={
        Property(name="publication2014c_ReviewNote", type=publication2014c_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014c_Paragraph25", type=publication2014c_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuralView43: BinaryAssociation = BinaryAssociation(
    name="structuralView43",
    ends={
        Property(name="publication2014c_PublicationStructure45", type=publication2014c_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014c_PublicationSystem44", type=publication2014c_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
process26: BinaryAssociation = BinaryAssociation(
    name="process26",
    ends={
        Property(name="publication2014c_PublicationProcess27", type=publication2014c_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014c_Progress", type=publication2014c_PublicationProcess, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_publication2014c_PublicationProcess_Named = Generalization(general=Named, specific=publication2014c_PublicationProcess)
gen_publication2014c_Write_Labelled = Generalization(general=Labelled, specific=publication2014c_Write)
gen_publication2014c_Paper_Named = Generalization(general=Named, specific=publication2014c_Paper)
gen_publication2014c_Review_Labelled = Generalization(general=Labelled, specific=publication2014c_Review)
gen_publication2014c_PublicationStructure_Named = Generalization(general=Named, specific=publication2014c_PublicationStructure)
gen_publication2014c_Paragraph_Counted = Generalization(general=Counted, specific=publication2014c_Paragraph)
gen_publication2014c_Paragraph_Named = Generalization(general=Named, specific=publication2014c_Paragraph)
gen_publication2014c_ReviewNote_Named = Generalization(general=Named, specific=publication2014c_ReviewNote)
gen_publication2014c_Progress_Labelled = Generalization(general=Labelled, specific=publication2014c_Progress)

# Domain Model
domain_model = DomainModel(
    name="publication2014c",
    types={publication2014c_Sequence, publication2014c_PublicationProcess, Named, publication2014c_PublicationPhase, publication2014c_Rule, publication2014c_Write, publication2014c_Review, publication2014c_Paper, publication2014c_Researcher, publication2014c_PublicationStructure, publication2014c_Paragraph, publication2014c_Progress, Counted, publication2014c_PublicationSystem, publication2014c_ReviewNote, publication2014c_Named, Labelled, publication2014c_Labelled, publication2014c_Counted, SequenceType},
    associations={linksToSuccessors3, phases0, publicationRules1, writes16, reviews17, papers19, neededPerson5, rules6, successor9, predecessor12, phaseParticipation15, paper28, paragraph30, reviewNote33, paragraphs20, progress21, authors22, researchers36, papers38, processView41, reviews24, structuralView43, process26},
    generalizations={gen_publication2014c_PublicationProcess_Named, gen_publication2014c_Write_Labelled, gen_publication2014c_Paper_Named, gen_publication2014c_Review_Labelled, gen_publication2014c_PublicationStructure_Named, gen_publication2014c_Paragraph_Counted, gen_publication2014c_Paragraph_Named, gen_publication2014c_ReviewNote_Named, gen_publication2014c_Progress_Labelled},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
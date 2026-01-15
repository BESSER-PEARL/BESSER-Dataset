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
publication_PublicationProcess = Class(name="publication::PublicationProcess")
Named = Class(name="Named")
publication_PublicationPhase = Class(name="publication::PublicationPhase")
publication_Researcher = Class(name="publication::Researcher")
publication_PlaceHolderPP = Class(name="publication::PlaceHolderPP")
publication_PlaceHolderRule = Class(name="publication::PlaceHolderRule")
publication_Rule = Class(name="publication::Rule")
publication_Sequence = Class(name="publication::Sequence")
publication_Paragraph = Class(name="publication::Paragraph")
publication_Progress = Class(name="publication::Progress")
Counted = Class(name="Counted")
publication_ReviewNote = Class(name="publication::ReviewNote")
publication_Write = Class(name="publication::Write")
publication_Review = Class(name="publication::Review")
publication_Paper = Class(name="publication::Paper")
publication_PlaceHolderRs = Class(name="publication::PlaceHolderRs")
publication_PublicationStructure = Class(name="publication::PublicationStructure")
publication_PublicationSystem = Class(name="publication::PublicationSystem")
publication_Named = Class(name="publication::Named", is_abstract=True)
publication_PlaceHolderRn = Class(name="publication::PlaceHolderRn")
Labelled = Class(name="Labelled")
publication_PlaceHolder = Class(name="publication::PlaceHolder", is_abstract=True)
publication_Counted = Class(name="publication::Counted", is_abstract=True)
publication_Labelled = Class(name="publication::Labelled", is_abstract=True)
PlaceHolder = Class(name="PlaceHolder")

# publication_PublicationProcess class attributes and methods
publication_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
publication_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
publication_PublicationProcess.attributes={publication_PublicationProcess_maxTime, publication_PublicationProcess_minTime}

# Named class attributes and methods

# publication_PublicationPhase class attributes and methods
publication_PublicationPhase_maxTime: Property = Property(name="maxTime", type=IntegerType)
publication_PublicationPhase_name: Property = Property(name="name", type=StringType)
publication_PublicationPhase_minTime: Property = Property(name="minTime", type=IntegerType)
publication_PublicationPhase.attributes={publication_PublicationPhase_maxTime, publication_PublicationPhase_name, publication_PublicationPhase_minTime}

# publication_Researcher class attributes and methods
publication_Researcher_name: Property = Property(name="name", type=StringType)
publication_Researcher_forName: Property = Property(name="forName", type=StringType)
publication_Researcher_position: Property = Property(name="position", type=StringType)
publication_Researcher.attributes={publication_Researcher_name, publication_Researcher_position, publication_Researcher_forName}

# publication_PlaceHolderPP class attributes and methods

# publication_PlaceHolderRule class attributes and methods

# publication_Rule class attributes and methods
publication_Rule_text: Property = Property(name="text", type=StringType)
publication_Rule_key: Property = Property(name="key", type=StringType)
publication_Rule.attributes={publication_Rule_text, publication_Rule_key}

# publication_Sequence class attributes and methods
publication_Sequence_sequenceType: Property = Property(name="sequenceType", type=StringType)
publication_Sequence.attributes={publication_Sequence_sequenceType}

# publication_Paragraph class attributes and methods
publication_Paragraph_content: Property = Property(name="content", type=StringType)
publication_Paragraph.attributes={publication_Paragraph_content}

# publication_Progress class attributes and methods
publication_Progress_percent: Property = Property(name="percent", type=IntegerType)
publication_Progress_time: Property = Property(name="time", type=IntegerType)
publication_Progress.attributes={publication_Progress_time, publication_Progress_percent}

# Counted class attributes and methods

# publication_ReviewNote class attributes and methods
publication_ReviewNote_content: Property = Property(name="content", type=StringType)
publication_ReviewNote.attributes={publication_ReviewNote_content}

# publication_Write class attributes and methods

# publication_Review class attributes and methods

# publication_Paper class attributes and methods

# publication_PlaceHolderRs class attributes and methods

# publication_PublicationStructure class attributes and methods

# publication_PublicationSystem class attributes and methods

# publication_Named class attributes and methods
publication_Named_name: Property = Property(name="name", type=StringType)
publication_Named.attributes={publication_Named_name}

# publication_PlaceHolderRn class attributes and methods

# Labelled class attributes and methods

# publication_PlaceHolder class attributes and methods

# publication_Counted class attributes and methods
publication_Counted_id: Property = Property(name="id", type=IntegerType)
publication_Counted.attributes={publication_Counted_id}

# publication_Labelled class attributes and methods
publication_Labelled_lname: Property = Property(name="lname", type=StringType)
publication_Labelled.attributes={publication_Labelled_lname}

# PlaceHolder class attributes and methods

# Relationships
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="publication_PublicationPhase", type=publication_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_PublicationProcess", type=publication_PublicationPhase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
neededPerson5: BinaryAssociation = BinaryAssociation(
    name="neededPerson5",
    ends={
        Property(name="Researcher", type=publication_PublicationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="phaseParticipation", type=publication_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
rules6: BinaryAssociation = BinaryAssociation(
    name="rules6",
    ends={
        Property(name="publication_Rule8", type=publication_PublicationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_PublicationPhase7", type=publication_Rule, multiplicity=Multiplicity(0, 9999))
    }
)
placeholder9: BinaryAssociation = BinaryAssociation(
    name="placeholder9",
    ends={
        Property(name="publication_PlaceHolderPP", type=publication_PublicationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_PublicationPhase10", type=publication_PlaceHolderPP, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
successor11: BinaryAssociation = BinaryAssociation(
    name="successor11",
    ends={
        Property(name="publication_PublicationPhase13", type=publication_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Sequence12", type=publication_PublicationPhase, multiplicity=Multiplicity(1, 1))
    }
)
predecessor14: BinaryAssociation = BinaryAssociation(
    name="predecessor14",
    ends={
        Property(name="publication_PublicationPhase16", type=publication_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Sequence15", type=publication_PublicationPhase, multiplicity=Multiplicity(1, 1))
    }
)
placeholder17: BinaryAssociation = BinaryAssociation(
    name="placeholder17",
    ends={
        Property(name="publication_PlaceHolderRule", type=publication_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Rule18", type=publication_PlaceHolderRule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
phaseParticipation19: BinaryAssociation = BinaryAssociation(
    name="phaseParticipation19",
    ends={
        Property(name="PublicationPhase", type=publication_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="neededPerson", type=publication_PublicationPhase, multiplicity=Multiplicity(0, 9999))
    }
)
publicationRules1: BinaryAssociation = BinaryAssociation(
    name="publicationRules1",
    ends={
        Property(name="publication_Rule", type=publication_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_PublicationProcess2", type=publication_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linksToSuccessors3: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessors3",
    ends={
        Property(name="publication_Sequence", type=publication_PublicationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_PublicationPhase4", type=publication_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs26: BinaryAssociation = BinaryAssociation(
    name="paragraphs26",
    ends={
        Property(name="publication_Paragraph", type=publication_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Paper", type=publication_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
progress27: BinaryAssociation = BinaryAssociation(
    name="progress27",
    ends={
        Property(name="Progress", type=publication_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=publication_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors28: BinaryAssociation = BinaryAssociation(
    name="authors28",
    ends={
        Property(name="Researcher29", type=publication_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="papers", type=publication_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
reviews30: BinaryAssociation = BinaryAssociation(
    name="reviews30",
    ends={
        Property(name="publication_ReviewNote", type=publication_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Paragraph31", type=publication_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writes20: BinaryAssociation = BinaryAssociation(
    name="writes20",
    ends={
        Property(name="publication_Write", type=publication_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Researcher", type=publication_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews21: BinaryAssociation = BinaryAssociation(
    name="reviews21",
    ends={
        Property(name="publication_Review", type=publication_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Researcher22", type=publication_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers23: BinaryAssociation = BinaryAssociation(
    name="papers23",
    ends={
        Property(name="Paper", type=publication_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=publication_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
placeholder24: BinaryAssociation = BinaryAssociation(
    name="placeholder24",
    ends={
        Property(name="publication_PlaceHolderRs", type=publication_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Researcher25", type=publication_PlaceHolderRs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paper36: BinaryAssociation = BinaryAssociation(
    name="paper36",
    ends={
        Property(name="progress", type=publication_Paper, multiplicity=Multiplicity(0, 1)),
        Property(name="Paper37", type=publication_Progress, multiplicity=Multiplicity(1, 1))
    }
)
paragraph38: BinaryAssociation = BinaryAssociation(
    name="paragraph38",
    ends={
        Property(name="publication_Paragraph40", type=publication_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Write39", type=publication_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
reviewNote41: BinaryAssociation = BinaryAssociation(
    name="reviewNote41",
    ends={
        Property(name="publication_ReviewNote43", type=publication_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Review42", type=publication_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
researchers44: BinaryAssociation = BinaryAssociation(
    name="researchers44",
    ends={
        Property(name="publication_Researcher45", type=publication_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_PublicationStructure", type=publication_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers46: BinaryAssociation = BinaryAssociation(
    name="papers46",
    ends={
        Property(name="publication_Paper48", type=publication_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_PublicationStructure47", type=publication_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processView49: BinaryAssociation = BinaryAssociation(
    name="processView49",
    ends={
        Property(name="publication_PublicationProcess50", type=publication_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_PublicationSystem", type=publication_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuralView51: BinaryAssociation = BinaryAssociation(
    name="structuralView51",
    ends={
        Property(name="publication_PublicationStructure53", type=publication_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_PublicationSystem52", type=publication_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
placeholder32: BinaryAssociation = BinaryAssociation(
    name="placeholder32",
    ends={
        Property(name="publication_PlaceHolderRn", type=publication_ReviewNote, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_ReviewNote33", type=publication_PlaceHolderRn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
process34: BinaryAssociation = BinaryAssociation(
    name="process34",
    ends={
        Property(name="publication_PublicationProcess35", type=publication_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="publication_Progress", type=publication_PublicationProcess, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_publication_PublicationProcess_Named = Generalization(general=Named, specific=publication_PublicationProcess)
gen_publication_Paper_Named = Generalization(general=Named, specific=publication_Paper)
gen_publication_Paragraph_Counted = Generalization(general=Counted, specific=publication_Paragraph)
gen_publication_Paragraph_Named = Generalization(general=Named, specific=publication_Paragraph)
gen_publication_Write_Labelled = Generalization(general=Labelled, specific=publication_Write)
gen_publication_Review_Labelled = Generalization(general=Labelled, specific=publication_Review)
gen_publication_PublicationStructure_Named = Generalization(general=Named, specific=publication_PublicationStructure)
gen_publication_ReviewNote_Named = Generalization(general=Named, specific=publication_ReviewNote)
gen_publication_Progress_Labelled = Generalization(general=Labelled, specific=publication_Progress)
gen_publication_PlaceHolderRn_PlaceHolder = Generalization(general=PlaceHolder, specific=publication_PlaceHolderRn)
gen_publication_PlaceHolderPP_PlaceHolder = Generalization(general=PlaceHolder, specific=publication_PlaceHolderPP)
gen_publication_PlaceHolderRs_PlaceHolder = Generalization(general=PlaceHolder, specific=publication_PlaceHolderRs)
gen_publication_PlaceHolderRule_PlaceHolder = Generalization(general=PlaceHolder, specific=publication_PlaceHolderRule)

# Domain Model
domain_model = DomainModel(
    name="publication",
    types={publication_PublicationProcess, Named, publication_PublicationPhase, publication_Researcher, publication_PlaceHolderPP, publication_PlaceHolderRule, publication_Rule, publication_Sequence, publication_Paragraph, publication_Progress, Counted, publication_ReviewNote, publication_Write, publication_Review, publication_Paper, publication_PlaceHolderRs, publication_PublicationStructure, publication_PublicationSystem, publication_Named, publication_PlaceHolderRn, Labelled, publication_PlaceHolder, publication_Counted, publication_Labelled, PlaceHolder, SequenceType},
    associations={phases0, neededPerson5, rules6, placeholder9, successor11, predecessor14, placeholder17, phaseParticipation19, publicationRules1, linksToSuccessors3, paragraphs26, progress27, authors28, reviews30, writes20, reviews21, papers23, placeholder24, paper36, paragraph38, reviewNote41, researchers44, papers46, processView49, structuralView51, placeholder32, process34},
    generalizations={gen_publication_PublicationProcess_Named, gen_publication_Paper_Named, gen_publication_Paragraph_Counted, gen_publication_Paragraph_Named, gen_publication_Write_Labelled, gen_publication_Review_Labelled, gen_publication_PublicationStructure_Named, gen_publication_ReviewNote_Named, gen_publication_Progress_Labelled, gen_publication_PlaceHolderRn_PlaceHolder, gen_publication_PlaceHolderPP_PlaceHolder, gen_publication_PlaceHolderRs_PlaceHolder, gen_publication_PlaceHolderRule_PlaceHolder},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
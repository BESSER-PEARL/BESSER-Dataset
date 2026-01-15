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
revision_PublicationProcess = Class(name="revision::PublicationProcess")
Named = Class(name="Named")
revision_Rule = Class(name="revision::Rule")
revision_Sequence = Class(name="revision::Sequence")
revision_Researcher = Class(name="revision::Researcher")
revision_PublicationPhase = Class(name="revision::PublicationPhase")
revision_PlaceHolderRule = Class(name="revision::PlaceHolderRule")
revision_Write = Class(name="revision::Write")
revision_Review = Class(name="revision::Review")
revision_Paper = Class(name="revision::Paper")
revision_PlaceHolderRs = Class(name="revision::PlaceHolderRs")
revision_PlaceHolderPP = Class(name="revision::PlaceHolderPP")
revision_Progress = Class(name="revision::Progress")
Counted = Class(name="Counted")
revision_ReviewNote = Class(name="revision::ReviewNote")
revision_PlaceHolderRn = Class(name="revision::PlaceHolderRn")
Labelled = Class(name="Labelled")
revision_Paragraph = Class(name="revision::Paragraph")
revision_PublicationSystem = Class(name="revision::PublicationSystem")
revision_Named = Class(name="revision::Named", is_abstract=True)
revision_Counted = Class(name="revision::Counted", is_abstract=True)
revision_Labelled = Class(name="revision::Labelled", is_abstract=True)
PlaceHolder = Class(name="PlaceHolder")
revision_PlaceHolder = Class(name="revision::PlaceHolder", is_abstract=True)
revision_PublicationStructure = Class(name="revision::PublicationStructure")

# revision_PublicationProcess class attributes and methods
revision_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
revision_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
revision_PublicationProcess.attributes={revision_PublicationProcess_minTime, revision_PublicationProcess_maxTime}

# Named class attributes and methods

# revision_Rule class attributes and methods
revision_Rule_text: Property = Property(name="text", type=StringType)
revision_Rule_key: Property = Property(name="key", type=StringType)
revision_Rule.attributes={revision_Rule_key, revision_Rule_text}

# revision_Sequence class attributes and methods
revision_Sequence_sequenceType: Property = Property(name="sequenceType", type=StringType)
revision_Sequence.attributes={revision_Sequence_sequenceType}

# revision_Researcher class attributes and methods
revision_Researcher_name: Property = Property(name="name", type=StringType)
revision_Researcher_forName: Property = Property(name="forName", type=StringType)
revision_Researcher_position: Property = Property(name="position", type=StringType)
revision_Researcher.attributes={revision_Researcher_forName, revision_Researcher_position, revision_Researcher_name}

# revision_PublicationPhase class attributes and methods
revision_PublicationPhase_name: Property = Property(name="name", type=StringType)
revision_PublicationPhase_minTime: Property = Property(name="minTime", type=IntegerType)
revision_PublicationPhase_maxTime: Property = Property(name="maxTime", type=IntegerType)
revision_PublicationPhase.attributes={revision_PublicationPhase_minTime, revision_PublicationPhase_maxTime, revision_PublicationPhase_name}

# revision_PlaceHolderRule class attributes and methods

# revision_Write class attributes and methods

# revision_Review class attributes and methods

# revision_Paper class attributes and methods

# revision_PlaceHolderRs class attributes and methods

# revision_PlaceHolderPP class attributes and methods

# revision_Progress class attributes and methods
revision_Progress_percent: Property = Property(name="percent", type=IntegerType)
revision_Progress.attributes={revision_Progress_percent}

# Counted class attributes and methods

# revision_ReviewNote class attributes and methods
revision_ReviewNote_content: Property = Property(name="content", type=StringType)
revision_ReviewNote.attributes={revision_ReviewNote_content}

# revision_PlaceHolderRn class attributes and methods

# Labelled class attributes and methods

# revision_Paragraph class attributes and methods
revision_Paragraph_content: Property = Property(name="content", type=StringType)
revision_Paragraph.attributes={revision_Paragraph_content}

# revision_PublicationSystem class attributes and methods

# revision_Named class attributes and methods
revision_Named_name: Property = Property(name="name", type=StringType)
revision_Named.attributes={revision_Named_name}

# revision_Counted class attributes and methods
revision_Counted_id: Property = Property(name="id", type=IntegerType)
revision_Counted.attributes={revision_Counted_id}

# revision_Labelled class attributes and methods
revision_Labelled_lname: Property = Property(name="lname", type=StringType)
revision_Labelled.attributes={revision_Labelled_lname}

# PlaceHolder class attributes and methods

# revision_PlaceHolder class attributes and methods

# revision_PublicationStructure class attributes and methods

# Relationships
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="revision_PublicationPhase", type=revision_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_PublicationProcess", type=revision_PublicationPhase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publicationRules1: BinaryAssociation = BinaryAssociation(
    name="publicationRules1",
    ends={
        Property(name="revision_Rule", type=revision_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_PublicationProcess2", type=revision_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linksToSuccessors3: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessors3",
    ends={
        Property(name="revision_Sequence", type=revision_PublicationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_PublicationPhase4", type=revision_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
neededPerson5: BinaryAssociation = BinaryAssociation(
    name="neededPerson5",
    ends={
        Property(name="Researcher", type=revision_PublicationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="phaseParticipation", type=revision_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
rules6: BinaryAssociation = BinaryAssociation(
    name="rules6",
    ends={
        Property(name="revision_Rule8", type=revision_PublicationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_PublicationPhase7", type=revision_Rule, multiplicity=Multiplicity(0, 9999))
    }
)
successor11: BinaryAssociation = BinaryAssociation(
    name="successor11",
    ends={
        Property(name="revision_PublicationPhase13", type=revision_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_Sequence12", type=revision_PublicationPhase, multiplicity=Multiplicity(1, 1))
    }
)
predecessor14: BinaryAssociation = BinaryAssociation(
    name="predecessor14",
    ends={
        Property(name="revision_PublicationPhase16", type=revision_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_Sequence15", type=revision_PublicationPhase, multiplicity=Multiplicity(1, 1))
    }
)
placeholder17: BinaryAssociation = BinaryAssociation(
    name="placeholder17",
    ends={
        Property(name="revision_PlaceHolderRule", type=revision_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_Rule18", type=revision_PlaceHolderRule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
phaseParticipation19: BinaryAssociation = BinaryAssociation(
    name="phaseParticipation19",
    ends={
        Property(name="PublicationPhase", type=revision_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="neededPerson", type=revision_PublicationPhase, multiplicity=Multiplicity(0, 9999))
    }
)
writes20: BinaryAssociation = BinaryAssociation(
    name="writes20",
    ends={
        Property(name="revision_Write", type=revision_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_Researcher", type=revision_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews21: BinaryAssociation = BinaryAssociation(
    name="reviews21",
    ends={
        Property(name="revision_Review", type=revision_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_Researcher22", type=revision_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers23: BinaryAssociation = BinaryAssociation(
    name="papers23",
    ends={
        Property(name="Paper", type=revision_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=revision_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
placeholder24: BinaryAssociation = BinaryAssociation(
    name="placeholder24",
    ends={
        Property(name="revision_PlaceHolderRs", type=revision_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_Researcher25", type=revision_PlaceHolderRs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
placeholder9: BinaryAssociation = BinaryAssociation(
    name="placeholder9",
    ends={
        Property(name="revision_PlaceHolderPP", type=revision_PublicationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_PublicationPhase10", type=revision_PlaceHolderPP, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
progress27: BinaryAssociation = BinaryAssociation(
    name="progress27",
    ends={
        Property(name="Progress", type=revision_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=revision_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors28: BinaryAssociation = BinaryAssociation(
    name="authors28",
    ends={
        Property(name="Researcher29", type=revision_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="papers", type=revision_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
reviews30: BinaryAssociation = BinaryAssociation(
    name="reviews30",
    ends={
        Property(name="revision_ReviewNote", type=revision_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_Paragraph31", type=revision_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
placeholder32: BinaryAssociation = BinaryAssociation(
    name="placeholder32",
    ends={
        Property(name="revision_PlaceHolderRn", type=revision_ReviewNote, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_ReviewNote33", type=revision_PlaceHolderRn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
process34: BinaryAssociation = BinaryAssociation(
    name="process34",
    ends={
        Property(name="revision_PublicationProcess35", type=revision_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_Progress", type=revision_PublicationProcess, multiplicity=Multiplicity(0, 1))
    }
)
paper36: BinaryAssociation = BinaryAssociation(
    name="paper36",
    ends={
        Property(name="Paper37", type=revision_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="progress", type=revision_Paper, multiplicity=Multiplicity(0, 1))
    }
)
paragraph38: BinaryAssociation = BinaryAssociation(
    name="paragraph38",
    ends={
        Property(name="revision_Paragraph40", type=revision_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_Write39", type=revision_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
paragraphs26: BinaryAssociation = BinaryAssociation(
    name="paragraphs26",
    ends={
        Property(name="revision_Paragraph", type=revision_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_Paper", type=revision_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
researchers44: BinaryAssociation = BinaryAssociation(
    name="researchers44",
    ends={
        Property(name="revision_Researcher45", type=revision_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_PublicationStructure", type=revision_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers46: BinaryAssociation = BinaryAssociation(
    name="papers46",
    ends={
        Property(name="revision_Paper48", type=revision_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_PublicationStructure47", type=revision_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processView49: BinaryAssociation = BinaryAssociation(
    name="processView49",
    ends={
        Property(name="revision_PublicationProcess50", type=revision_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_PublicationSystem", type=revision_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuralView51: BinaryAssociation = BinaryAssociation(
    name="structuralView51",
    ends={
        Property(name="revision_PublicationStructure53", type=revision_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_PublicationSystem52", type=revision_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reviewNote41: BinaryAssociation = BinaryAssociation(
    name="reviewNote41",
    ends={
        Property(name="revision_ReviewNote43", type=revision_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="revision_Review42", type=revision_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_revision_PublicationProcess_Named = Generalization(general=Named, specific=revision_PublicationProcess)
gen_revision_Paragraph_Counted = Generalization(general=Counted, specific=revision_Paragraph)
gen_revision_Paragraph_Named = Generalization(general=Named, specific=revision_Paragraph)
gen_revision_ReviewNote_Named = Generalization(general=Named, specific=revision_ReviewNote)
gen_revision_Progress_Labelled = Generalization(general=Labelled, specific=revision_Progress)
gen_revision_Write_Labelled = Generalization(general=Labelled, specific=revision_Write)
gen_revision_Paper_Named = Generalization(general=Named, specific=revision_Paper)
gen_revision_Review_Labelled = Generalization(general=Labelled, specific=revision_Review)
gen_revision_PlaceHolderRs_PlaceHolder = Generalization(general=PlaceHolder, specific=revision_PlaceHolderRs)
gen_revision_PlaceHolderRule_PlaceHolder = Generalization(general=PlaceHolder, specific=revision_PlaceHolderRule)
gen_revision_PlaceHolderRn_PlaceHolder = Generalization(general=PlaceHolder, specific=revision_PlaceHolderRn)
gen_revision_PlaceHolderPP_PlaceHolder = Generalization(general=PlaceHolder, specific=revision_PlaceHolderPP)
gen_revision_PublicationStructure_Named = Generalization(general=Named, specific=revision_PublicationStructure)

# Domain Model
domain_model = DomainModel(
    name="revision",
    types={revision_PublicationProcess, Named, revision_Rule, revision_Sequence, revision_Researcher, revision_PublicationPhase, revision_PlaceHolderRule, revision_Write, revision_Review, revision_Paper, revision_PlaceHolderRs, revision_PlaceHolderPP, revision_Progress, Counted, revision_ReviewNote, revision_PlaceHolderRn, Labelled, revision_Paragraph, revision_PublicationSystem, revision_Named, revision_Counted, revision_Labelled, PlaceHolder, revision_PlaceHolder, revision_PublicationStructure, SequenceType},
    associations={phases0, publicationRules1, linksToSuccessors3, neededPerson5, rules6, successor11, predecessor14, placeholder17, phaseParticipation19, writes20, reviews21, papers23, placeholder24, placeholder9, progress27, authors28, reviews30, placeholder32, process34, paper36, paragraph38, paragraphs26, researchers44, papers46, processView49, structuralView51, reviewNote41},
    generalizations={gen_revision_PublicationProcess_Named, gen_revision_Paragraph_Counted, gen_revision_Paragraph_Named, gen_revision_ReviewNote_Named, gen_revision_Progress_Labelled, gen_revision_Write_Labelled, gen_revision_Paper_Named, gen_revision_Review_Labelled, gen_revision_PlaceHolderRs_PlaceHolder, gen_revision_PlaceHolderRule_PlaceHolder, gen_revision_PlaceHolderRn_PlaceHolder, gen_revision_PlaceHolderPP_PlaceHolder, gen_revision_PublicationStructure_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
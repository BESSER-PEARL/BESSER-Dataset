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
publication2014_Researcher = Class(name="publication2014::Researcher")
publication2014_PlaceHolderPP = Class(name="publication2014::PlaceHolderPP")
publication2014_PublicationProcess = Class(name="publication2014::PublicationProcess")
Named = Class(name="Named")
publication2014_PublicationPhase = Class(name="publication2014::PublicationPhase")
publication2014_Rule = Class(name="publication2014::Rule")
publication2014_Sequence = Class(name="publication2014::Sequence")
publication2014_PlaceHolderRs = Class(name="publication2014::PlaceHolderRs")
publication2014_Paragraph = Class(name="publication2014::Paragraph")
publication2014_Progress = Class(name="publication2014::Progress")
Counted = Class(name="Counted")
publication2014_ReviewNote = Class(name="publication2014::ReviewNote")
publication2014_PlaceHolderRule = Class(name="publication2014::PlaceHolderRule")
publication2014_Write = Class(name="publication2014::Write")
publication2014_Review = Class(name="publication2014::Review")
publication2014_Paper = Class(name="publication2014::Paper")
publication2014_PublicationStructure = Class(name="publication2014::PublicationStructure")
publication2014_PublicationSystem = Class(name="publication2014::PublicationSystem")
publication2014_PlaceHolderRn = Class(name="publication2014::PlaceHolderRn")
Labelled = Class(name="Labelled")
publication2014_Named = Class(name="publication2014::Named", is_abstract=True)
publication2014_Counted = Class(name="publication2014::Counted", is_abstract=True)
publication2014_Labelled = Class(name="publication2014::Labelled", is_abstract=True)
PlaceHolder = Class(name="PlaceHolder")
publication2014_PlaceHolder = Class(name="publication2014::PlaceHolder", is_abstract=True)

# publication2014_Researcher class attributes and methods
publication2014_Researcher_name: Property = Property(name="name", type=StringType)
publication2014_Researcher_forName: Property = Property(name="forName", type=StringType)
publication2014_Researcher_position: Property = Property(name="position", type=StringType)
publication2014_Researcher.attributes={publication2014_Researcher_position, publication2014_Researcher_name, publication2014_Researcher_forName}

# publication2014_PlaceHolderPP class attributes and methods

# publication2014_PublicationProcess class attributes and methods
publication2014_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
publication2014_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
publication2014_PublicationProcess.attributes={publication2014_PublicationProcess_minTime, publication2014_PublicationProcess_maxTime}

# Named class attributes and methods

# publication2014_PublicationPhase class attributes and methods
publication2014_PublicationPhase_minTime: Property = Property(name="minTime", type=IntegerType)
publication2014_PublicationPhase_maxTime: Property = Property(name="maxTime", type=IntegerType)
publication2014_PublicationPhase_name: Property = Property(name="name", type=StringType)
publication2014_PublicationPhase.attributes={publication2014_PublicationPhase_maxTime, publication2014_PublicationPhase_name, publication2014_PublicationPhase_minTime}

# publication2014_Rule class attributes and methods
publication2014_Rule_text: Property = Property(name="text", type=StringType)
publication2014_Rule_key: Property = Property(name="key", type=StringType)
publication2014_Rule.attributes={publication2014_Rule_key, publication2014_Rule_text}

# publication2014_Sequence class attributes and methods
publication2014_Sequence_sequenceType: Property = Property(name="sequenceType", type=StringType)
publication2014_Sequence.attributes={publication2014_Sequence_sequenceType}

# publication2014_PlaceHolderRs class attributes and methods

# publication2014_Paragraph class attributes and methods
publication2014_Paragraph_content: Property = Property(name="content", type=StringType)
publication2014_Paragraph.attributes={publication2014_Paragraph_content}

# publication2014_Progress class attributes and methods
publication2014_Progress_percent: Property = Property(name="percent", type=IntegerType)
publication2014_Progress_time: Property = Property(name="time", type=IntegerType)
publication2014_Progress.attributes={publication2014_Progress_percent, publication2014_Progress_time}

# Counted class attributes and methods

# publication2014_ReviewNote class attributes and methods
publication2014_ReviewNote_content: Property = Property(name="content", type=StringType)
publication2014_ReviewNote.attributes={publication2014_ReviewNote_content}

# publication2014_PlaceHolderRule class attributes and methods

# publication2014_Write class attributes and methods

# publication2014_Review class attributes and methods

# publication2014_Paper class attributes and methods

# publication2014_PublicationStructure class attributes and methods

# publication2014_PublicationSystem class attributes and methods

# publication2014_PlaceHolderRn class attributes and methods

# Labelled class attributes and methods

# publication2014_Named class attributes and methods
publication2014_Named_name: Property = Property(name="name", type=StringType)
publication2014_Named.attributes={publication2014_Named_name}

# publication2014_Counted class attributes and methods
publication2014_Counted_id: Property = Property(name="id", type=IntegerType)
publication2014_Counted.attributes={publication2014_Counted_id}

# publication2014_Labelled class attributes and methods
publication2014_Labelled_lname: Property = Property(name="lname", type=StringType)
publication2014_Labelled.attributes={publication2014_Labelled_lname}

# PlaceHolder class attributes and methods

# publication2014_PlaceHolder class attributes and methods

# Relationships
neededPerson5: BinaryAssociation = BinaryAssociation(
    name="neededPerson5",
    ends={
        Property(name="Researcher", type=publication2014_PublicationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="phaseParticipation", type=publication2014_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
rules6: BinaryAssociation = BinaryAssociation(
    name="rules6",
    ends={
        Property(name="publication2014_Rule8", type=publication2014_PublicationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_PublicationPhase7", type=publication2014_Rule, multiplicity=Multiplicity(0, 9999))
    }
)
placeholder9: BinaryAssociation = BinaryAssociation(
    name="placeholder9",
    ends={
        Property(name="publication2014_PlaceHolderPP", type=publication2014_PublicationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_PublicationPhase10", type=publication2014_PlaceHolderPP, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
successor11: BinaryAssociation = BinaryAssociation(
    name="successor11",
    ends={
        Property(name="publication2014_PublicationPhase13", type=publication2014_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_Sequence12", type=publication2014_PublicationPhase, multiplicity=Multiplicity(1, 1))
    }
)
predecessor14: BinaryAssociation = BinaryAssociation(
    name="predecessor14",
    ends={
        Property(name="publication2014_PublicationPhase16", type=publication2014_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_Sequence15", type=publication2014_PublicationPhase, multiplicity=Multiplicity(1, 1))
    }
)
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="publication2014_PublicationPhase", type=publication2014_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_PublicationProcess", type=publication2014_PublicationPhase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publicationRules1: BinaryAssociation = BinaryAssociation(
    name="publicationRules1",
    ends={
        Property(name="publication2014_Rule", type=publication2014_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_PublicationProcess2", type=publication2014_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linksToSuccessors3: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessors3",
    ends={
        Property(name="publication2014_Sequence", type=publication2014_PublicationPhase, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_PublicationPhase4", type=publication2014_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
placeholder24: BinaryAssociation = BinaryAssociation(
    name="placeholder24",
    ends={
        Property(name="publication2014_PlaceHolderRs", type=publication2014_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_Researcher25", type=publication2014_PlaceHolderRs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paragraphs26: BinaryAssociation = BinaryAssociation(
    name="paragraphs26",
    ends={
        Property(name="publication2014_Paragraph", type=publication2014_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_Paper", type=publication2014_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
progress27: BinaryAssociation = BinaryAssociation(
    name="progress27",
    ends={
        Property(name="Progress", type=publication2014_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=publication2014_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors28: BinaryAssociation = BinaryAssociation(
    name="authors28",
    ends={
        Property(name="Researcher29", type=publication2014_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="papers", type=publication2014_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
reviews30: BinaryAssociation = BinaryAssociation(
    name="reviews30",
    ends={
        Property(name="publication2014_ReviewNote", type=publication2014_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_Paragraph31", type=publication2014_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
placeholder17: BinaryAssociation = BinaryAssociation(
    name="placeholder17",
    ends={
        Property(name="publication2014_PlaceHolderRule", type=publication2014_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_Rule18", type=publication2014_PlaceHolderRule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
phaseParticipation19: BinaryAssociation = BinaryAssociation(
    name="phaseParticipation19",
    ends={
        Property(name="PublicationPhase", type=publication2014_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="neededPerson", type=publication2014_PublicationPhase, multiplicity=Multiplicity(0, 9999))
    }
)
writes20: BinaryAssociation = BinaryAssociation(
    name="writes20",
    ends={
        Property(name="publication2014_Write", type=publication2014_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_Researcher", type=publication2014_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews21: BinaryAssociation = BinaryAssociation(
    name="reviews21",
    ends={
        Property(name="publication2014_Review", type=publication2014_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_Researcher22", type=publication2014_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers23: BinaryAssociation = BinaryAssociation(
    name="papers23",
    ends={
        Property(name="Paper", type=publication2014_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=publication2014_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
reviewNote41: BinaryAssociation = BinaryAssociation(
    name="reviewNote41",
    ends={
        Property(name="publication2014_ReviewNote43", type=publication2014_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_Review42", type=publication2014_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
researchers44: BinaryAssociation = BinaryAssociation(
    name="researchers44",
    ends={
        Property(name="publication2014_Researcher45", type=publication2014_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_PublicationStructure", type=publication2014_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers46: BinaryAssociation = BinaryAssociation(
    name="papers46",
    ends={
        Property(name="publication2014_Paper48", type=publication2014_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_PublicationStructure47", type=publication2014_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processView49: BinaryAssociation = BinaryAssociation(
    name="processView49",
    ends={
        Property(name="publication2014_PublicationProcess50", type=publication2014_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_PublicationSystem", type=publication2014_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuralView51: BinaryAssociation = BinaryAssociation(
    name="structuralView51",
    ends={
        Property(name="publication2014_PublicationStructure53", type=publication2014_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_PublicationSystem52", type=publication2014_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
placeholder32: BinaryAssociation = BinaryAssociation(
    name="placeholder32",
    ends={
        Property(name="publication2014_PlaceHolderRn", type=publication2014_ReviewNote, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_ReviewNote33", type=publication2014_PlaceHolderRn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
process34: BinaryAssociation = BinaryAssociation(
    name="process34",
    ends={
        Property(name="publication2014_PublicationProcess35", type=publication2014_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_Progress", type=publication2014_PublicationProcess, multiplicity=Multiplicity(0, 1))
    }
)
paper36: BinaryAssociation = BinaryAssociation(
    name="paper36",
    ends={
        Property(name="Paper37", type=publication2014_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="progress", type=publication2014_Paper, multiplicity=Multiplicity(0, 1))
    }
)
paragraph38: BinaryAssociation = BinaryAssociation(
    name="paragraph38",
    ends={
        Property(name="publication2014_Paragraph40", type=publication2014_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="publication2014_Write39", type=publication2014_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_publication2014_PublicationProcess_Named = Generalization(general=Named, specific=publication2014_PublicationProcess)
gen_publication2014_Paper_Named = Generalization(general=Named, specific=publication2014_Paper)
gen_publication2014_Paragraph_Counted = Generalization(general=Counted, specific=publication2014_Paragraph)
gen_publication2014_Paragraph_Named = Generalization(general=Named, specific=publication2014_Paragraph)
gen_publication2014_PublicationStructure_Named = Generalization(general=Named, specific=publication2014_PublicationStructure)
gen_publication2014_ReviewNote_Named = Generalization(general=Named, specific=publication2014_ReviewNote)
gen_publication2014_Progress_Labelled = Generalization(general=Labelled, specific=publication2014_Progress)
gen_publication2014_Write_Labelled = Generalization(general=Labelled, specific=publication2014_Write)
gen_publication2014_Review_Labelled = Generalization(general=Labelled, specific=publication2014_Review)
gen_publication2014_PlaceHolderRs_PlaceHolder = Generalization(general=PlaceHolder, specific=publication2014_PlaceHolderRs)
gen_publication2014_PlaceHolderRule_PlaceHolder = Generalization(general=PlaceHolder, specific=publication2014_PlaceHolderRule)
gen_publication2014_PlaceHolderRn_PlaceHolder = Generalization(general=PlaceHolder, specific=publication2014_PlaceHolderRn)
gen_publication2014_PlaceHolderPP_PlaceHolder = Generalization(general=PlaceHolder, specific=publication2014_PlaceHolderPP)

# Domain Model
domain_model = DomainModel(
    name="publication2014",
    types={publication2014_Researcher, publication2014_PlaceHolderPP, publication2014_PublicationProcess, Named, publication2014_PublicationPhase, publication2014_Rule, publication2014_Sequence, publication2014_PlaceHolderRs, publication2014_Paragraph, publication2014_Progress, Counted, publication2014_ReviewNote, publication2014_PlaceHolderRule, publication2014_Write, publication2014_Review, publication2014_Paper, publication2014_PublicationStructure, publication2014_PublicationSystem, publication2014_PlaceHolderRn, Labelled, publication2014_Named, publication2014_Counted, publication2014_Labelled, PlaceHolder, publication2014_PlaceHolder, SequenceType},
    associations={neededPerson5, rules6, placeholder9, successor11, predecessor14, phases0, publicationRules1, linksToSuccessors3, placeholder24, paragraphs26, progress27, authors28, reviews30, placeholder17, phaseParticipation19, writes20, reviews21, papers23, reviewNote41, researchers44, papers46, processView49, structuralView51, placeholder32, process34, paper36, paragraph38},
    generalizations={gen_publication2014_PublicationProcess_Named, gen_publication2014_Paper_Named, gen_publication2014_Paragraph_Counted, gen_publication2014_Paragraph_Named, gen_publication2014_PublicationStructure_Named, gen_publication2014_ReviewNote_Named, gen_publication2014_Progress_Labelled, gen_publication2014_Write_Labelled, gen_publication2014_Review_Labelled, gen_publication2014_PlaceHolderRs_PlaceHolder, gen_publication2014_PlaceHolderRule_PlaceHolder, gen_publication2014_PlaceHolderRn_PlaceHolder, gen_publication2014_PlaceHolderPP_PlaceHolder},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
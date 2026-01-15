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
StateType: Enumeration = Enumeration(
    name="StateType",
    literals={
            EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="ongoing"),
			EnumerationLiteral(name="final")
    }
)

# Classes
research23_PublicationProcess = Class(name="research23::PublicationProcess")
Named = Class(name="Named")
research23_Researcher = Class(name="research23::Researcher")
research23_Write = Class(name="research23::Write")
research23_Review = Class(name="research23::Review")
research23_Paper = Class(name="research23::Paper")
research23_Skill = Class(name="research23::Skill")
research23_Position = Class(name="research23::Position")
research23_Collaboration = Class(name="research23::Collaboration")
research23_Paragraph = Class(name="research23::Paragraph")
research23_Progress = Class(name="research23::Progress")
research23_Phase = Class(name="research23::Phase")
research23_State = Class(name="research23::State")
Counted = Class(name="Counted")
research23_ReviewNote = Class(name="research23::ReviewNote")
Labelled = Class(name="Labelled")
research23_PaperKeyword = Class(name="research23::PaperKeyword")
research23_KnowledgeManager = Class(name="research23::KnowledgeManager")
research23_PublicationStatus = Class(name="research23::PublicationStatus")
research23_PublicationSystem = Class(name="research23::PublicationSystem")
research23_Named = Class(name="research23::Named", is_abstract=True)
research23_Counted = Class(name="research23::Counted", is_abstract=True)
research23_PublicationStructure = Class(name="research23::PublicationStructure")
research23_Keyword = Class(name="research23::Keyword")
research23_Labelled = Class(name="research23::Labelled", is_abstract=True)
research23_StateMachineObject = Class(name="research23::StateMachineObject", is_abstract=True)
research23_Transition = Class(name="research23::Transition")
StateMachineObject = Class(name="StateMachineObject")
research23_Action = Class(name="research23::Action")
research23_StateMachineVariable = Class(name="research23::StateMachineVariable")

# research23_PublicationProcess class attributes and methods
research23_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
research23_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
research23_PublicationProcess.attributes={research23_PublicationProcess_maxTime, research23_PublicationProcess_minTime}

# Named class attributes and methods

# research23_Researcher class attributes and methods
research23_Researcher_name: Property = Property(name="name", type=StringType)
research23_Researcher_forName: Property = Property(name="forName", type=StringType)
research23_Researcher.attributes={research23_Researcher_forName, research23_Researcher_name}

# research23_Write class attributes and methods
research23_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
research23_Write.attributes={research23_Write_timeSpent}

# research23_Review class attributes and methods
research23_Review_date: Property = Property(name="date", type=DateType)
research23_Review.attributes={research23_Review_date}

# research23_Paper class attributes and methods

# research23_Skill class attributes and methods
research23_Skill_description: Property = Property(name="description", type=StringType)
research23_Skill.attributes={research23_Skill_description}

# research23_Position class attributes and methods
research23_Position_description: Property = Property(name="description", type=StringType)
research23_Position.attributes={research23_Position_description}

# research23_Collaboration class attributes and methods
research23_Collaboration_ratio: Property = Property(name="ratio", type=IntegerType)
research23_Collaboration.attributes={research23_Collaboration_ratio}

# research23_Paragraph class attributes and methods
research23_Paragraph_content: Property = Property(name="content", type=StringType)
research23_Paragraph.attributes={research23_Paragraph_content}

# research23_Progress class attributes and methods
research23_Progress_percent: Property = Property(name="percent", type=IntegerType)
research23_Progress.attributes={research23_Progress_percent}

# research23_Phase class attributes and methods
research23_Phase_name: Property = Property(name="name", type=StringType)
research23_Phase.attributes={research23_Phase_name}

# research23_State class attributes and methods
research23_State_id: Property = Property(name="id", type=IntegerType)
research23_State_kind: Property = Property(name="kind", type=StringType)
research23_State_name: Property = Property(name="name", type=StringType)
research23_State.attributes={research23_State_id, research23_State_kind, research23_State_name}

# Counted class attributes and methods

# research23_ReviewNote class attributes and methods
research23_ReviewNote_content: Property = Property(name="content", type=StringType)
research23_ReviewNote.attributes={research23_ReviewNote_content}

# Labelled class attributes and methods

# research23_PaperKeyword class attributes and methods
research23_PaperKeyword_weight: Property = Property(name="weight", type=IntegerType)
research23_PaperKeyword.attributes={research23_PaperKeyword_weight}

# research23_KnowledgeManager class attributes and methods

# research23_PublicationStatus class attributes and methods
research23_PublicationStatus_label: Property = Property(name="label", type=StringType)
research23_PublicationStatus.attributes={research23_PublicationStatus_label}

# research23_PublicationSystem class attributes and methods

# research23_Named class attributes and methods
research23_Named_name: Property = Property(name="name", type=StringType)
research23_Named.attributes={research23_Named_name}

# research23_Counted class attributes and methods
research23_Counted_id: Property = Property(name="id", type=IntegerType)
research23_Counted.attributes={research23_Counted_id}

# research23_PublicationStructure class attributes and methods

# research23_Keyword class attributes and methods
research23_Keyword_word: Property = Property(name="word", type=StringType)
research23_Keyword.attributes={research23_Keyword_word}

# research23_Labelled class attributes and methods
research23_Labelled_lname: Property = Property(name="lname", type=StringType)
research23_Labelled.attributes={research23_Labelled_lname}

# research23_StateMachineObject class attributes and methods
research23_StateMachineObject_label: Property = Property(name="label", type=StringType)
research23_StateMachineObject.attributes={research23_StateMachineObject_label}

# research23_Transition class attributes and methods
research23_Transition_guardLabel: Property = Property(name="guardLabel", type=StringType)
research23_Transition_guardExpression: Property = Property(name="guardExpression", type=StringType)
research23_Transition.attributes={research23_Transition_guardLabel, research23_Transition_guardExpression}

# StateMachineObject class attributes and methods

# research23_Action class attributes and methods
research23_Action_actionLabel: Property = Property(name="actionLabel", type=StringType)
research23_Action_actionStatement: Property = Property(name="actionStatement", type=StringType)
research23_Action.attributes={research23_Action_actionLabel, research23_Action_actionStatement}

# research23_StateMachineVariable class attributes and methods

# Relationships
writes1: BinaryAssociation = BinaryAssociation(
    name="writes1",
    ends={
        Property(name="research23_Write", type=research23_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Researcher", type=research23_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews2: BinaryAssociation = BinaryAssociation(
    name="reviews2",
    ends={
        Property(name="research23_Review", type=research23_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Researcher3", type=research23_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_papers4: BinaryAssociation = BinaryAssociation(
    name="res_papers4",
    ends={
        Property(name="Paper", type=research23_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=research23_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills5: BinaryAssociation = BinaryAssociation(
    name="skills5",
    ends={
        Property(name="research23_Skill", type=research23_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Researcher6", type=research23_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_position7: BinaryAssociation = BinaryAssociation(
    name="res_position7",
    ends={
        Property(name="research23_Position", type=research23_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Researcher8", type=research23_Position, multiplicity=Multiplicity(0, 1))
    }
)
collaborations9: BinaryAssociation = BinaryAssociation(
    name="collaborations9",
    ends={
        Property(name="research23_Collaboration", type=research23_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Researcher10", type=research23_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs11: BinaryAssociation = BinaryAssociation(
    name="paragraphs11",
    ends={
        Property(name="research23_Paragraph", type=research23_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Paper", type=research23_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
progress12: BinaryAssociation = BinaryAssociation(
    name="progress12",
    ends={
        Property(name="Progress", type=research23_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=research23_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="research23_Phase", type=research23_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_PublicationProcess", type=research23_Phase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state19: BinaryAssociation = BinaryAssociation(
    name="state19",
    ends={
        Property(name="research23_State", type=research23_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Paper20", type=research23_State, multiplicity=Multiplicity(0, 1))
    }
)
reviews21: BinaryAssociation = BinaryAssociation(
    name="reviews21",
    ends={
        Property(name="research23_ReviewNote", type=research23_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Paragraph22", type=research23_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process23: BinaryAssociation = BinaryAssociation(
    name="process23",
    ends={
        Property(name="research23_PublicationProcess24", type=research23_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Progress", type=research23_PublicationProcess, multiplicity=Multiplicity(0, 1))
    }
)
paper25: BinaryAssociation = BinaryAssociation(
    name="paper25",
    ends={
        Property(name="Paper26", type=research23_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="progress", type=research23_Paper, multiplicity=Multiplicity(0, 1))
    }
)
paragraph27: BinaryAssociation = BinaryAssociation(
    name="paragraph27",
    ends={
        Property(name="research23_Paragraph29", type=research23_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Write28", type=research23_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
authors13: BinaryAssociation = BinaryAssociation(
    name="authors13",
    ends={
        Property(name="Researcher", type=research23_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=research23_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
keywords14: BinaryAssociation = BinaryAssociation(
    name="keywords14",
    ends={
        Property(name="research23_PaperKeyword", type=research23_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Paper15", type=research23_PaperKeyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
citedBy17: BinaryAssociation = BinaryAssociation(
    name="citedBy17",
    ends={
        Property(name="research23_Paper18", type=research23_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Paper16", type=research23_Paper, multiplicity=Multiplicity(0, 1))
    }
)
researchers33: BinaryAssociation = BinaryAssociation(
    name="researchers33",
    ends={
        Property(name="research23_Researcher34", type=research23_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_PublicationStructure", type=research23_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers35: BinaryAssociation = BinaryAssociation(
    name="papers35",
    ends={
        Property(name="research23_Paper37", type=research23_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_PublicationStructure36", type=research23_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
knowledgeMan38: BinaryAssociation = BinaryAssociation(
    name="knowledgeMan38",
    ends={
        Property(name="research23_KnowledgeManager", type=research23_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_PublicationStructure39", type=research23_KnowledgeManager, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
status40: BinaryAssociation = BinaryAssociation(
    name="status40",
    ends={
        Property(name="research23_PublicationStatus", type=research23_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_PublicationStructure41", type=research23_PublicationStatus, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
processView42: BinaryAssociation = BinaryAssociation(
    name="processView42",
    ends={
        Property(name="research23_PublicationProcess43", type=research23_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_PublicationSystem", type=research23_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuralView44: BinaryAssociation = BinaryAssociation(
    name="structuralView44",
    ends={
        Property(name="research23_PublicationStructure46", type=research23_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_PublicationSystem45", type=research23_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
positions47: BinaryAssociation = BinaryAssociation(
    name="positions47",
    ends={
        Property(name="research23_Position49", type=research23_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_PublicationSystem48", type=research23_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviewNote30: BinaryAssociation = BinaryAssociation(
    name="reviewNote30",
    ends={
        Property(name="research23_ReviewNote32", type=research23_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Review31", type=research23_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
parent51: BinaryAssociation = BinaryAssociation(
    name="parent51",
    ends={
        Property(name="research23_Position52", type=research23_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Position50", type=research23_Position, multiplicity=Multiplicity(0, 1))
    }
)
kpapers53: BinaryAssociation = BinaryAssociation(
    name="kpapers53",
    ends={
        Property(name="research23_Paper54", type=research23_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Keyword", type=research23_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
allkeywords55: BinaryAssociation = BinaryAssociation(
    name="allkeywords55",
    ends={
        Property(name="research23_Keyword57", type=research23_KnowledgeManager, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_KnowledgeManager56", type=research23_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyword58: BinaryAssociation = BinaryAssociation(
    name="keyword58",
    ends={
        Property(name="research23_Keyword60", type=research23_PaperKeyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_PaperKeyword59", type=research23_Keyword, multiplicity=Multiplicity(0, 1))
    }
)
col_paper61: BinaryAssociation = BinaryAssociation(
    name="col_paper61",
    ends={
        Property(name="research23_Paper63", type=research23_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Collaboration62", type=research23_Paper, multiplicity=Multiplicity(0, 1))
    }
)
pubStates66: BinaryAssociation = BinaryAssociation(
    name="pubStates66",
    ends={
        Property(name="research23_State68", type=research23_PublicationStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_PublicationStatus67", type=research23_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
t_actions69: BinaryAssociation = BinaryAssociation(
    name="t_actions69",
    ends={
        Property(name="research23_Action", type=research23_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Transition", type=research23_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source70: BinaryAssociation = BinaryAssociation(
    name="source70",
    ends={
        Property(name="research23_State72", type=research23_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Transition71", type=research23_State, multiplicity=Multiplicity(0, 1))
    }
)
target73: BinaryAssociation = BinaryAssociation(
    name="target73",
    ends={
        Property(name="research23_State75", type=research23_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Transition74", type=research23_State, multiplicity=Multiplicity(0, 1))
    }
)
transitions76: BinaryAssociation = BinaryAssociation(
    name="transitions76",
    ends={
        Property(name="research23_Transition78", type=research23_State, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_State77", type=research23_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
machineVariables64: BinaryAssociation = BinaryAssociation(
    name="machineVariables64",
    ends={
        Property(name="research23_StateMachineVariable", type=research23_PublicationStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_PublicationStatus65", type=research23_StateMachineVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next83: BinaryAssociation = BinaryAssociation(
    name="next83",
    ends={
        Property(name="research23_Action84", type=research23_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_Action82", type=research23_Action, multiplicity=Multiplicity(0, 1))
    }
)
s_actions79: BinaryAssociation = BinaryAssociation(
    name="s_actions79",
    ends={
        Property(name="research23_Action81", type=research23_State, multiplicity=Multiplicity(1, 1)),
        Property(name="research23_State80", type=research23_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_research23_PublicationProcess_Named = Generalization(general=Named, specific=research23_PublicationProcess)
gen_research23_Paper_Named = Generalization(general=Named, specific=research23_Paper)
gen_research23_Paragraph_Counted = Generalization(general=Counted, specific=research23_Paragraph)
gen_research23_Paragraph_Named = Generalization(general=Named, specific=research23_Paragraph)
gen_research23_ReviewNote_Named = Generalization(general=Named, specific=research23_ReviewNote)
gen_research23_Progress_Labelled = Generalization(general=Labelled, specific=research23_Progress)
gen_research23_Write_Labelled = Generalization(general=Labelled, specific=research23_Write)
gen_research23_PublicationStructure_Named = Generalization(general=Named, specific=research23_PublicationStructure)
gen_research23_PublicationSystem_Named = Generalization(general=Named, specific=research23_PublicationSystem)
gen_research23_Review_Labelled = Generalization(general=Labelled, specific=research23_Review)
gen_research23_Position_Named = Generalization(general=Named, specific=research23_Position)
gen_research23_Keyword_Named = Generalization(general=Named, specific=research23_Keyword)
gen_research23_KnowledgeManager_Named = Generalization(general=Named, specific=research23_KnowledgeManager)
gen_research23_Transition_StateMachineObject = Generalization(general=StateMachineObject, specific=research23_Transition)
gen_research23_State_StateMachineObject = Generalization(general=StateMachineObject, specific=research23_State)

# Domain Model
domain_model = DomainModel(
    name="research23",
    types={research23_PublicationProcess, Named, research23_Researcher, research23_Write, research23_Review, research23_Paper, research23_Skill, research23_Position, research23_Collaboration, research23_Paragraph, research23_Progress, research23_Phase, research23_State, Counted, research23_ReviewNote, Labelled, research23_PaperKeyword, research23_KnowledgeManager, research23_PublicationStatus, research23_PublicationSystem, research23_Named, research23_Counted, research23_PublicationStructure, research23_Keyword, research23_Labelled, research23_StateMachineObject, research23_Transition, StateMachineObject, research23_Action, research23_StateMachineVariable, StateType},
    associations={writes1, reviews2, res_papers4, skills5, res_position7, collaborations9, paragraphs11, progress12, phases0, state19, reviews21, process23, paper25, paragraph27, authors13, keywords14, citedBy17, researchers33, papers35, knowledgeMan38, status40, processView42, structuralView44, positions47, reviewNote30, parent51, kpapers53, allkeywords55, keyword58, col_paper61, pubStates66, t_actions69, source70, target73, transitions76, machineVariables64, next83, s_actions79},
    generalizations={gen_research23_PublicationProcess_Named, gen_research23_Paper_Named, gen_research23_Paragraph_Counted, gen_research23_Paragraph_Named, gen_research23_ReviewNote_Named, gen_research23_Progress_Labelled, gen_research23_Write_Labelled, gen_research23_PublicationStructure_Named, gen_research23_PublicationSystem_Named, gen_research23_Review_Labelled, gen_research23_Position_Named, gen_research23_Keyword_Named, gen_research23_KnowledgeManager_Named, gen_research23_Transition_StateMachineObject, gen_research23_State_StateMachineObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
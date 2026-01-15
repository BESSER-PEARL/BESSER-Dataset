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
research16_PublicationProcess = Class(name="research16::PublicationProcess")
Named = Class(name="Named")
research16_Phase = Class(name="research16::Phase")
research16_Collaboration = Class(name="research16::Collaboration")
research16_Paragraph = Class(name="research16::Paragraph")
research16_Progress = Class(name="research16::Progress")
research16_PaperKeyword = Class(name="research16::PaperKeyword")
research16_Researcher = Class(name="research16::Researcher")
research16_Write = Class(name="research16::Write")
research16_Review = Class(name="research16::Review")
research16_Paper = Class(name="research16::Paper")
research16_Skill = Class(name="research16::Skill")
research16_Position = Class(name="research16::Position")
Labelled = Class(name="Labelled")
research16_State = Class(name="research16::State")
Counted = Class(name="Counted")
research16_ReviewNote = Class(name="research16::ReviewNote")
research16_PublicationStatus = Class(name="research16::PublicationStatus")
research16_Named = Class(name="research16::Named", is_abstract=True)
research16_Counted = Class(name="research16::Counted", is_abstract=True)
research16_Labelled = Class(name="research16::Labelled", is_abstract=True)
research16_PublicationStructure = Class(name="research16::PublicationStructure")
research16_KnowledgeManager = Class(name="research16::KnowledgeManager")
research16_PublicationSystem = Class(name="research16::PublicationSystem")
research16_Keyword = Class(name="research16::Keyword")
research16_Action = Class(name="research16::Action")
research16_StateMachineVariable = Class(name="research16::StateMachineVariable")
research16_StateMachineObject = Class(name="research16::StateMachineObject", is_abstract=True)
research16_Transition = Class(name="research16::Transition")
StateMachineObject = Class(name="StateMachineObject")

# research16_PublicationProcess class attributes and methods
research16_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
research16_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
research16_PublicationProcess.attributes={research16_PublicationProcess_minTime, research16_PublicationProcess_maxTime}

# Named class attributes and methods

# research16_Phase class attributes and methods
research16_Phase_name: Property = Property(name="name", type=StringType)
research16_Phase.attributes={research16_Phase_name}

# research16_Collaboration class attributes and methods
research16_Collaboration_ratio: Property = Property(name="ratio", type=IntegerType)
research16_Collaboration.attributes={research16_Collaboration_ratio}

# research16_Paragraph class attributes and methods
research16_Paragraph_content: Property = Property(name="content", type=StringType)
research16_Paragraph.attributes={research16_Paragraph_content}

# research16_Progress class attributes and methods
research16_Progress_percent: Property = Property(name="percent", type=IntegerType)
research16_Progress.attributes={research16_Progress_percent}

# research16_PaperKeyword class attributes and methods
research16_PaperKeyword_weight: Property = Property(name="weight", type=IntegerType)
research16_PaperKeyword.attributes={research16_PaperKeyword_weight}

# research16_Researcher class attributes and methods
research16_Researcher_name: Property = Property(name="name", type=StringType)
research16_Researcher_forName: Property = Property(name="forName", type=StringType)
research16_Researcher.attributes={research16_Researcher_name, research16_Researcher_forName}

# research16_Write class attributes and methods
research16_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
research16_Write.attributes={research16_Write_timeSpent}

# research16_Review class attributes and methods
research16_Review_date: Property = Property(name="date", type=DateType)
research16_Review.attributes={research16_Review_date}

# research16_Paper class attributes and methods

# research16_Skill class attributes and methods
research16_Skill_description: Property = Property(name="description", type=StringType)
research16_Skill.attributes={research16_Skill_description}

# research16_Position class attributes and methods
research16_Position_description: Property = Property(name="description", type=StringType)
research16_Position.attributes={research16_Position_description}

# Labelled class attributes and methods

# research16_State class attributes and methods
research16_State_id: Property = Property(name="id", type=IntegerType)
research16_State_kind: Property = Property(name="kind", type=StringType)
research16_State_name: Property = Property(name="name", type=StringType)
research16_State.attributes={research16_State_kind, research16_State_id, research16_State_name}

# Counted class attributes and methods

# research16_ReviewNote class attributes and methods
research16_ReviewNote_content: Property = Property(name="content", type=StringType)
research16_ReviewNote.attributes={research16_ReviewNote_content}

# research16_PublicationStatus class attributes and methods
research16_PublicationStatus_label: Property = Property(name="label", type=StringType)
research16_PublicationStatus.attributes={research16_PublicationStatus_label}

# research16_Named class attributes and methods
research16_Named_name: Property = Property(name="name", type=StringType)
research16_Named.attributes={research16_Named_name}

# research16_Counted class attributes and methods
research16_Counted_id: Property = Property(name="id", type=IntegerType)
research16_Counted.attributes={research16_Counted_id}

# research16_Labelled class attributes and methods
research16_Labelled_lname: Property = Property(name="lname", type=StringType)
research16_Labelled.attributes={research16_Labelled_lname}

# research16_PublicationStructure class attributes and methods

# research16_KnowledgeManager class attributes and methods

# research16_PublicationSystem class attributes and methods

# research16_Keyword class attributes and methods
research16_Keyword_word: Property = Property(name="word", type=StringType)
research16_Keyword.attributes={research16_Keyword_word}

# research16_Action class attributes and methods
research16_Action_actionLabel: Property = Property(name="actionLabel", type=StringType)
research16_Action_actionStatement: Property = Property(name="actionStatement", type=StringType)
research16_Action.attributes={research16_Action_actionLabel, research16_Action_actionStatement}

# research16_StateMachineVariable class attributes and methods

# research16_StateMachineObject class attributes and methods
research16_StateMachineObject_label: Property = Property(name="label", type=StringType)
research16_StateMachineObject.attributes={research16_StateMachineObject_label}

# research16_Transition class attributes and methods
research16_Transition_guardLabel: Property = Property(name="guardLabel", type=StringType)
research16_Transition_guardExpression: Property = Property(name="guardExpression", type=StringType)
research16_Transition.attributes={research16_Transition_guardExpression, research16_Transition_guardLabel}

# StateMachineObject class attributes and methods

# Relationships
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="research16_Phase", type=research16_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_PublicationProcess", type=research16_Phase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collaborations9: BinaryAssociation = BinaryAssociation(
    name="collaborations9",
    ends={
        Property(name="research16_Collaboration", type=research16_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Researcher10", type=research16_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs11: BinaryAssociation = BinaryAssociation(
    name="paragraphs11",
    ends={
        Property(name="research16_Paragraph", type=research16_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Paper", type=research16_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
progress12: BinaryAssociation = BinaryAssociation(
    name="progress12",
    ends={
        Property(name="Progress", type=research16_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=research16_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors13: BinaryAssociation = BinaryAssociation(
    name="authors13",
    ends={
        Property(name="Researcher", type=research16_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=research16_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
writes1: BinaryAssociation = BinaryAssociation(
    name="writes1",
    ends={
        Property(name="research16_Write", type=research16_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Researcher", type=research16_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews2: BinaryAssociation = BinaryAssociation(
    name="reviews2",
    ends={
        Property(name="research16_Review", type=research16_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Researcher3", type=research16_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_papers4: BinaryAssociation = BinaryAssociation(
    name="res_papers4",
    ends={
        Property(name="Paper", type=research16_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=research16_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills5: BinaryAssociation = BinaryAssociation(
    name="skills5",
    ends={
        Property(name="research16_Skill", type=research16_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Researcher6", type=research16_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_position7: BinaryAssociation = BinaryAssociation(
    name="res_position7",
    ends={
        Property(name="research16_Position", type=research16_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Researcher8", type=research16_Position, multiplicity=Multiplicity(0, 1))
    }
)
process23: BinaryAssociation = BinaryAssociation(
    name="process23",
    ends={
        Property(name="research16_PublicationProcess24", type=research16_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Progress", type=research16_PublicationProcess, multiplicity=Multiplicity(0, 1))
    }
)
paper25: BinaryAssociation = BinaryAssociation(
    name="paper25",
    ends={
        Property(name="Paper26", type=research16_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="progress", type=research16_Paper, multiplicity=Multiplicity(0, 1))
    }
)
paragraph27: BinaryAssociation = BinaryAssociation(
    name="paragraph27",
    ends={
        Property(name="research16_Paragraph29", type=research16_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Write28", type=research16_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
reviewNote30: BinaryAssociation = BinaryAssociation(
    name="reviewNote30",
    ends={
        Property(name="research16_ReviewNote32", type=research16_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Review31", type=research16_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
keywords14: BinaryAssociation = BinaryAssociation(
    name="keywords14",
    ends={
        Property(name="research16_PaperKeyword", type=research16_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Paper15", type=research16_PaperKeyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
citedBy17: BinaryAssociation = BinaryAssociation(
    name="citedBy17",
    ends={
        Property(name="research16_Paper18", type=research16_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Paper16", type=research16_Paper, multiplicity=Multiplicity(0, 1))
    }
)
state19: BinaryAssociation = BinaryAssociation(
    name="state19",
    ends={
        Property(name="research16_State", type=research16_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Paper20", type=research16_State, multiplicity=Multiplicity(0, 1))
    }
)
reviews21: BinaryAssociation = BinaryAssociation(
    name="reviews21",
    ends={
        Property(name="research16_ReviewNote", type=research16_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Paragraph22", type=research16_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processView40: BinaryAssociation = BinaryAssociation(
    name="processView40",
    ends={
        Property(name="research16_PublicationProcess41", type=research16_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_PublicationSystem", type=research16_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuralView42: BinaryAssociation = BinaryAssociation(
    name="structuralView42",
    ends={
        Property(name="research16_PublicationStructure44", type=research16_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_PublicationSystem43", type=research16_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
positions45: BinaryAssociation = BinaryAssociation(
    name="positions45",
    ends={
        Property(name="research16_Position47", type=research16_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_PublicationSystem46", type=research16_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviorView48: BinaryAssociation = BinaryAssociation(
    name="behaviorView48",
    ends={
        Property(name="research16_PublicationStatus", type=research16_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_PublicationSystem49", type=research16_PublicationStatus, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
researchers33: BinaryAssociation = BinaryAssociation(
    name="researchers33",
    ends={
        Property(name="research16_Researcher34", type=research16_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_PublicationStructure", type=research16_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers35: BinaryAssociation = BinaryAssociation(
    name="papers35",
    ends={
        Property(name="research16_Paper37", type=research16_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_PublicationStructure36", type=research16_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
knowledgeMan38: BinaryAssociation = BinaryAssociation(
    name="knowledgeMan38",
    ends={
        Property(name="research16_KnowledgeManager", type=research16_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_PublicationStructure39", type=research16_KnowledgeManager, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
kpapers53: BinaryAssociation = BinaryAssociation(
    name="kpapers53",
    ends={
        Property(name="research16_Paper54", type=research16_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Keyword", type=research16_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
allkeywords55: BinaryAssociation = BinaryAssociation(
    name="allkeywords55",
    ends={
        Property(name="research16_Keyword57", type=research16_KnowledgeManager, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_KnowledgeManager56", type=research16_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyword58: BinaryAssociation = BinaryAssociation(
    name="keyword58",
    ends={
        Property(name="research16_Keyword60", type=research16_PaperKeyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_PaperKeyword59", type=research16_Keyword, multiplicity=Multiplicity(0, 1))
    }
)
parent51: BinaryAssociation = BinaryAssociation(
    name="parent51",
    ends={
        Property(name="research16_Position52", type=research16_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Position50", type=research16_Position, multiplicity=Multiplicity(0, 1))
    }
)
t_actions69: BinaryAssociation = BinaryAssociation(
    name="t_actions69",
    ends={
        Property(name="research16_Action", type=research16_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Transition", type=research16_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source70: BinaryAssociation = BinaryAssociation(
    name="source70",
    ends={
        Property(name="research16_State72", type=research16_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Transition71", type=research16_State, multiplicity=Multiplicity(0, 1))
    }
)
target73: BinaryAssociation = BinaryAssociation(
    name="target73",
    ends={
        Property(name="research16_State75", type=research16_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Transition74", type=research16_State, multiplicity=Multiplicity(0, 1))
    }
)
transitions76: BinaryAssociation = BinaryAssociation(
    name="transitions76",
    ends={
        Property(name="research16_Transition78", type=research16_State, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_State77", type=research16_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
s_actions79: BinaryAssociation = BinaryAssociation(
    name="s_actions79",
    ends={
        Property(name="research16_Action81", type=research16_State, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_State80", type=research16_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
col_paper61: BinaryAssociation = BinaryAssociation(
    name="col_paper61",
    ends={
        Property(name="research16_Paper63", type=research16_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Collaboration62", type=research16_Paper, multiplicity=Multiplicity(0, 1))
    }
)
machineVariables64: BinaryAssociation = BinaryAssociation(
    name="machineVariables64",
    ends={
        Property(name="research16_StateMachineVariable", type=research16_PublicationStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_PublicationStatus65", type=research16_StateMachineVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pubStates66: BinaryAssociation = BinaryAssociation(
    name="pubStates66",
    ends={
        Property(name="research16_State68", type=research16_PublicationStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_PublicationStatus67", type=research16_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next83: BinaryAssociation = BinaryAssociation(
    name="next83",
    ends={
        Property(name="research16_Action84", type=research16_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="research16_Action82", type=research16_Action, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_research16_PublicationProcess_Named = Generalization(general=Named, specific=research16_PublicationProcess)
gen_research16_Paper_Named = Generalization(general=Named, specific=research16_Paper)
gen_research16_Progress_Labelled = Generalization(general=Labelled, specific=research16_Progress)
gen_research16_Write_Labelled = Generalization(general=Labelled, specific=research16_Write)
gen_research16_Review_Labelled = Generalization(general=Labelled, specific=research16_Review)
gen_research16_Paragraph_Counted = Generalization(general=Counted, specific=research16_Paragraph)
gen_research16_Paragraph_Named = Generalization(general=Named, specific=research16_Paragraph)
gen_research16_ReviewNote_Named = Generalization(general=Named, specific=research16_ReviewNote)
gen_research16_PublicationStructure_Named = Generalization(general=Named, specific=research16_PublicationStructure)
gen_research16_PublicationSystem_Named = Generalization(general=Named, specific=research16_PublicationSystem)
gen_research16_Keyword_Named = Generalization(general=Named, specific=research16_Keyword)
gen_research16_KnowledgeManager_Named = Generalization(general=Named, specific=research16_KnowledgeManager)
gen_research16_Position_Named = Generalization(general=Named, specific=research16_Position)
gen_research16_State_StateMachineObject = Generalization(general=StateMachineObject, specific=research16_State)
gen_research16_Transition_StateMachineObject = Generalization(general=StateMachineObject, specific=research16_Transition)

# Domain Model
domain_model = DomainModel(
    name="research16",
    types={research16_PublicationProcess, Named, research16_Phase, research16_Collaboration, research16_Paragraph, research16_Progress, research16_PaperKeyword, research16_Researcher, research16_Write, research16_Review, research16_Paper, research16_Skill, research16_Position, Labelled, research16_State, Counted, research16_ReviewNote, research16_PublicationStatus, research16_Named, research16_Counted, research16_Labelled, research16_PublicationStructure, research16_KnowledgeManager, research16_PublicationSystem, research16_Keyword, research16_Action, research16_StateMachineVariable, research16_StateMachineObject, research16_Transition, StateMachineObject, StateType},
    associations={phases0, collaborations9, paragraphs11, progress12, authors13, writes1, reviews2, res_papers4, skills5, res_position7, process23, paper25, paragraph27, reviewNote30, keywords14, citedBy17, state19, reviews21, processView40, structuralView42, positions45, behaviorView48, researchers33, papers35, knowledgeMan38, kpapers53, allkeywords55, keyword58, parent51, t_actions69, source70, target73, transitions76, s_actions79, col_paper61, machineVariables64, pubStates66, next83},
    generalizations={gen_research16_PublicationProcess_Named, gen_research16_Paper_Named, gen_research16_Progress_Labelled, gen_research16_Write_Labelled, gen_research16_Review_Labelled, gen_research16_Paragraph_Counted, gen_research16_Paragraph_Named, gen_research16_ReviewNote_Named, gen_research16_PublicationStructure_Named, gen_research16_PublicationSystem_Named, gen_research16_Keyword_Named, gen_research16_KnowledgeManager_Named, gen_research16_Position_Named, gen_research16_State_StateMachineObject, gen_research16_Transition_StateMachineObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
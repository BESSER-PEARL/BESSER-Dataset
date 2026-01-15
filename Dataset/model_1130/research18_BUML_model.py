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
research18_PublicationProcess = Class(name="research18::PublicationProcess")
Named = Class(name="Named")
research18_Phase = Class(name="research18::Phase")
research18_Researcher = Class(name="research18::Researcher")
research18_Review = Class(name="research18::Review")
research18_Paper = Class(name="research18::Paper")
research18_Skill = Class(name="research18::Skill")
research18_Position = Class(name="research18::Position")
research18_Collaboration = Class(name="research18::Collaboration")
research18_Paragraph = Class(name="research18::Paragraph")
research18_Progress = Class(name="research18::Progress")
research18_Write = Class(name="research18::Write")
research18_ReviewNote = Class(name="research18::ReviewNote")
Labelled = Class(name="Labelled")
research18_PaperKeyword = Class(name="research18::PaperKeyword")
research18_State = Class(name="research18::State")
Counted = Class(name="Counted")
research18_KnowledgeManager = Class(name="research18::KnowledgeManager")
research18_PublicationSystem = Class(name="research18::PublicationSystem")
research18_PublicationStatus = Class(name="research18::PublicationStatus")
research18_Named = Class(name="research18::Named", is_abstract=True)
research18_PublicationStructure = Class(name="research18::PublicationStructure")
research18_Keyword = Class(name="research18::Keyword")
research18_Counted = Class(name="research18::Counted", is_abstract=True)
research18_Labelled = Class(name="research18::Labelled", is_abstract=True)
research18_StateMachineObject = Class(name="research18::StateMachineObject", is_abstract=True)
research18_Transition = Class(name="research18::Transition")
StateMachineObject = Class(name="StateMachineObject")
research18_Action = Class(name="research18::Action")
research18_StateMachineVariable = Class(name="research18::StateMachineVariable")

# research18_PublicationProcess class attributes and methods
research18_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
research18_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
research18_PublicationProcess.attributes={research18_PublicationProcess_maxTime, research18_PublicationProcess_minTime}

# Named class attributes and methods

# research18_Phase class attributes and methods
research18_Phase_name: Property = Property(name="name", type=StringType)
research18_Phase.attributes={research18_Phase_name}

# research18_Researcher class attributes and methods
research18_Researcher_name: Property = Property(name="name", type=StringType)
research18_Researcher_forName: Property = Property(name="forName", type=StringType)
research18_Researcher.attributes={research18_Researcher_forName, research18_Researcher_name}

# research18_Review class attributes and methods
research18_Review_date: Property = Property(name="date", type=DateType)
research18_Review.attributes={research18_Review_date}

# research18_Paper class attributes and methods

# research18_Skill class attributes and methods
research18_Skill_description: Property = Property(name="description", type=StringType)
research18_Skill.attributes={research18_Skill_description}

# research18_Position class attributes and methods
research18_Position_description: Property = Property(name="description", type=StringType)
research18_Position.attributes={research18_Position_description}

# research18_Collaboration class attributes and methods
research18_Collaboration_ratio: Property = Property(name="ratio", type=IntegerType)
research18_Collaboration.attributes={research18_Collaboration_ratio}

# research18_Paragraph class attributes and methods
research18_Paragraph_content: Property = Property(name="content", type=StringType)
research18_Paragraph.attributes={research18_Paragraph_content}

# research18_Progress class attributes and methods
research18_Progress_percent: Property = Property(name="percent", type=IntegerType)
research18_Progress.attributes={research18_Progress_percent}

# research18_Write class attributes and methods
research18_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
research18_Write.attributes={research18_Write_timeSpent}

# research18_ReviewNote class attributes and methods
research18_ReviewNote_content: Property = Property(name="content", type=StringType)
research18_ReviewNote.attributes={research18_ReviewNote_content}

# Labelled class attributes and methods

# research18_PaperKeyword class attributes and methods
research18_PaperKeyword_weight: Property = Property(name="weight", type=IntegerType)
research18_PaperKeyword.attributes={research18_PaperKeyword_weight}

# research18_State class attributes and methods
research18_State_id: Property = Property(name="id", type=IntegerType)
research18_State_kind: Property = Property(name="kind", type=StringType)
research18_State_name: Property = Property(name="name", type=StringType)
research18_State.attributes={research18_State_id, research18_State_kind, research18_State_name}

# Counted class attributes and methods

# research18_KnowledgeManager class attributes and methods

# research18_PublicationSystem class attributes and methods

# research18_PublicationStatus class attributes and methods
research18_PublicationStatus_label: Property = Property(name="label", type=StringType)
research18_PublicationStatus.attributes={research18_PublicationStatus_label}

# research18_Named class attributes and methods
research18_Named_name: Property = Property(name="name", type=StringType)
research18_Named.attributes={research18_Named_name}

# research18_PublicationStructure class attributes and methods

# research18_Keyword class attributes and methods
research18_Keyword_word: Property = Property(name="word", type=StringType)
research18_Keyword.attributes={research18_Keyword_word}

# research18_Counted class attributes and methods
research18_Counted_id: Property = Property(name="id", type=IntegerType)
research18_Counted.attributes={research18_Counted_id}

# research18_Labelled class attributes and methods
research18_Labelled_lname: Property = Property(name="lname", type=StringType)
research18_Labelled.attributes={research18_Labelled_lname}

# research18_StateMachineObject class attributes and methods
research18_StateMachineObject_label: Property = Property(name="label", type=StringType)
research18_StateMachineObject.attributes={research18_StateMachineObject_label}

# research18_Transition class attributes and methods
research18_Transition_guardLabel: Property = Property(name="guardLabel", type=StringType)
research18_Transition_guardExpression: Property = Property(name="guardExpression", type=StringType)
research18_Transition.attributes={research18_Transition_guardExpression, research18_Transition_guardLabel}

# StateMachineObject class attributes and methods

# research18_Action class attributes and methods
research18_Action_actionLabel: Property = Property(name="actionLabel", type=StringType)
research18_Action_actionStatement: Property = Property(name="actionStatement", type=StringType)
research18_Action.attributes={research18_Action_actionLabel, research18_Action_actionStatement}

# research18_StateMachineVariable class attributes and methods

# Relationships
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="research18_Phase", type=research18_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_PublicationProcess", type=research18_Phase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews2: BinaryAssociation = BinaryAssociation(
    name="reviews2",
    ends={
        Property(name="research18_Review", type=research18_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Researcher3", type=research18_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_papers4: BinaryAssociation = BinaryAssociation(
    name="res_papers4",
    ends={
        Property(name="Paper", type=research18_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=research18_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills5: BinaryAssociation = BinaryAssociation(
    name="skills5",
    ends={
        Property(name="research18_Skill", type=research18_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Researcher6", type=research18_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_position7: BinaryAssociation = BinaryAssociation(
    name="res_position7",
    ends={
        Property(name="research18_Position", type=research18_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Researcher8", type=research18_Position, multiplicity=Multiplicity(0, 1))
    }
)
collaborations9: BinaryAssociation = BinaryAssociation(
    name="collaborations9",
    ends={
        Property(name="research18_Collaboration", type=research18_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Researcher10", type=research18_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs11: BinaryAssociation = BinaryAssociation(
    name="paragraphs11",
    ends={
        Property(name="research18_Paragraph", type=research18_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Paper", type=research18_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
progress12: BinaryAssociation = BinaryAssociation(
    name="progress12",
    ends={
        Property(name="Progress", type=research18_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=research18_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors13: BinaryAssociation = BinaryAssociation(
    name="authors13",
    ends={
        Property(name="Researcher", type=research18_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=research18_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
writes1: BinaryAssociation = BinaryAssociation(
    name="writes1",
    ends={
        Property(name="research18_Write", type=research18_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Researcher", type=research18_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews21: BinaryAssociation = BinaryAssociation(
    name="reviews21",
    ends={
        Property(name="research18_ReviewNote", type=research18_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Paragraph22", type=research18_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process23: BinaryAssociation = BinaryAssociation(
    name="process23",
    ends={
        Property(name="research18_PublicationProcess24", type=research18_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Progress", type=research18_PublicationProcess, multiplicity=Multiplicity(0, 1))
    }
)
paper25: BinaryAssociation = BinaryAssociation(
    name="paper25",
    ends={
        Property(name="Paper26", type=research18_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="progress", type=research18_Paper, multiplicity=Multiplicity(0, 1))
    }
)
paragraph27: BinaryAssociation = BinaryAssociation(
    name="paragraph27",
    ends={
        Property(name="research18_Paragraph29", type=research18_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Write28", type=research18_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
keywords14: BinaryAssociation = BinaryAssociation(
    name="keywords14",
    ends={
        Property(name="research18_PaperKeyword", type=research18_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Paper15", type=research18_PaperKeyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
citedBy17: BinaryAssociation = BinaryAssociation(
    name="citedBy17",
    ends={
        Property(name="research18_Paper18", type=research18_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Paper16", type=research18_Paper, multiplicity=Multiplicity(0, 1))
    }
)
state19: BinaryAssociation = BinaryAssociation(
    name="state19",
    ends={
        Property(name="research18_State", type=research18_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Paper20", type=research18_State, multiplicity=Multiplicity(0, 1))
    }
)
researchers33: BinaryAssociation = BinaryAssociation(
    name="researchers33",
    ends={
        Property(name="research18_Researcher34", type=research18_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_PublicationStructure", type=research18_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers35: BinaryAssociation = BinaryAssociation(
    name="papers35",
    ends={
        Property(name="research18_Paper37", type=research18_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_PublicationStructure36", type=research18_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
knowledgeMan38: BinaryAssociation = BinaryAssociation(
    name="knowledgeMan38",
    ends={
        Property(name="research18_KnowledgeManager", type=research18_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_PublicationStructure39", type=research18_KnowledgeManager, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
processView40: BinaryAssociation = BinaryAssociation(
    name="processView40",
    ends={
        Property(name="research18_PublicationProcess41", type=research18_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_PublicationSystem", type=research18_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuralView42: BinaryAssociation = BinaryAssociation(
    name="structuralView42",
    ends={
        Property(name="research18_PublicationStructure44", type=research18_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_PublicationSystem43", type=research18_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
positions45: BinaryAssociation = BinaryAssociation(
    name="positions45",
    ends={
        Property(name="research18_Position47", type=research18_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_PublicationSystem46", type=research18_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviorView48: BinaryAssociation = BinaryAssociation(
    name="behaviorView48",
    ends={
        Property(name="research18_PublicationStatus", type=research18_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_PublicationSystem49", type=research18_PublicationStatus, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reviewNote30: BinaryAssociation = BinaryAssociation(
    name="reviewNote30",
    ends={
        Property(name="research18_ReviewNote32", type=research18_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Review31", type=research18_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
parent51: BinaryAssociation = BinaryAssociation(
    name="parent51",
    ends={
        Property(name="research18_Position52", type=research18_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Position50", type=research18_Position, multiplicity=Multiplicity(0, 1))
    }
)
kpapers53: BinaryAssociation = BinaryAssociation(
    name="kpapers53",
    ends={
        Property(name="research18_Paper54", type=research18_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Keyword", type=research18_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
allkeywords55: BinaryAssociation = BinaryAssociation(
    name="allkeywords55",
    ends={
        Property(name="research18_Keyword57", type=research18_KnowledgeManager, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_KnowledgeManager56", type=research18_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyword58: BinaryAssociation = BinaryAssociation(
    name="keyword58",
    ends={
        Property(name="research18_Keyword60", type=research18_PaperKeyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_PaperKeyword59", type=research18_Keyword, multiplicity=Multiplicity(0, 1))
    }
)
pubStates66: BinaryAssociation = BinaryAssociation(
    name="pubStates66",
    ends={
        Property(name="research18_State68", type=research18_PublicationStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_PublicationStatus67", type=research18_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
t_actions69: BinaryAssociation = BinaryAssociation(
    name="t_actions69",
    ends={
        Property(name="research18_Action", type=research18_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Transition", type=research18_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source70: BinaryAssociation = BinaryAssociation(
    name="source70",
    ends={
        Property(name="research18_State72", type=research18_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Transition71", type=research18_State, multiplicity=Multiplicity(0, 1))
    }
)
target73: BinaryAssociation = BinaryAssociation(
    name="target73",
    ends={
        Property(name="research18_State75", type=research18_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Transition74", type=research18_State, multiplicity=Multiplicity(0, 1))
    }
)
col_paper61: BinaryAssociation = BinaryAssociation(
    name="col_paper61",
    ends={
        Property(name="research18_Paper63", type=research18_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_Collaboration62", type=research18_Paper, multiplicity=Multiplicity(0, 1))
    }
)
machineVariables64: BinaryAssociation = BinaryAssociation(
    name="machineVariables64",
    ends={
        Property(name="research18_StateMachineVariable", type=research18_PublicationStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_PublicationStatus65", type=research18_StateMachineVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next83: BinaryAssociation = BinaryAssociation(
    name="next83",
    ends={
        Property(name="research18_Action82", type=research18_Action, multiplicity=Multiplicity(0, 1)),
        Property(name="research18_Action84", type=research18_Action, multiplicity=Multiplicity(1, 1))
    }
)
transitions76: BinaryAssociation = BinaryAssociation(
    name="transitions76",
    ends={
        Property(name="research18_Transition78", type=research18_State, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_State77", type=research18_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
s_actions79: BinaryAssociation = BinaryAssociation(
    name="s_actions79",
    ends={
        Property(name="research18_Action81", type=research18_State, multiplicity=Multiplicity(1, 1)),
        Property(name="research18_State80", type=research18_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_research18_PublicationProcess_Named = Generalization(general=Named, specific=research18_PublicationProcess)
gen_research18_Paper_Named = Generalization(general=Named, specific=research18_Paper)
gen_research18_ReviewNote_Named = Generalization(general=Named, specific=research18_ReviewNote)
gen_research18_Progress_Labelled = Generalization(general=Labelled, specific=research18_Progress)
gen_research18_Write_Labelled = Generalization(general=Labelled, specific=research18_Write)
gen_research18_Paragraph_Counted = Generalization(general=Counted, specific=research18_Paragraph)
gen_research18_Paragraph_Named = Generalization(general=Named, specific=research18_Paragraph)
gen_research18_PublicationSystem_Named = Generalization(general=Named, specific=research18_PublicationSystem)
gen_research18_Review_Labelled = Generalization(general=Labelled, specific=research18_Review)
gen_research18_PublicationStructure_Named = Generalization(general=Named, specific=research18_PublicationStructure)
gen_research18_Position_Named = Generalization(general=Named, specific=research18_Position)
gen_research18_Keyword_Named = Generalization(general=Named, specific=research18_Keyword)
gen_research18_KnowledgeManager_Named = Generalization(general=Named, specific=research18_KnowledgeManager)
gen_research18_Transition_StateMachineObject = Generalization(general=StateMachineObject, specific=research18_Transition)
gen_research18_State_StateMachineObject = Generalization(general=StateMachineObject, specific=research18_State)

# Domain Model
domain_model = DomainModel(
    name="research18",
    types={research18_PublicationProcess, Named, research18_Phase, research18_Researcher, research18_Review, research18_Paper, research18_Skill, research18_Position, research18_Collaboration, research18_Paragraph, research18_Progress, research18_Write, research18_ReviewNote, Labelled, research18_PaperKeyword, research18_State, Counted, research18_KnowledgeManager, research18_PublicationSystem, research18_PublicationStatus, research18_Named, research18_PublicationStructure, research18_Keyword, research18_Counted, research18_Labelled, research18_StateMachineObject, research18_Transition, StateMachineObject, research18_Action, research18_StateMachineVariable, StateType},
    associations={phases0, reviews2, res_papers4, skills5, res_position7, collaborations9, paragraphs11, progress12, authors13, writes1, reviews21, process23, paper25, paragraph27, keywords14, citedBy17, state19, researchers33, papers35, knowledgeMan38, processView40, structuralView42, positions45, behaviorView48, reviewNote30, parent51, kpapers53, allkeywords55, keyword58, pubStates66, t_actions69, source70, target73, col_paper61, machineVariables64, next83, transitions76, s_actions79},
    generalizations={gen_research18_PublicationProcess_Named, gen_research18_Paper_Named, gen_research18_ReviewNote_Named, gen_research18_Progress_Labelled, gen_research18_Write_Labelled, gen_research18_Paragraph_Counted, gen_research18_Paragraph_Named, gen_research18_PublicationSystem_Named, gen_research18_Review_Labelled, gen_research18_PublicationStructure_Named, gen_research18_Position_Named, gen_research18_Keyword_Named, gen_research18_KnowledgeManager_Named, gen_research18_Transition_StateMachineObject, gen_research18_State_StateMachineObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
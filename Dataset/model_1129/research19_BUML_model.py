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
research19_PublicationProcess = Class(name="research19::PublicationProcess")
Named = Class(name="Named")
research19_Phase = Class(name="research19::Phase")
research19_Researcher = Class(name="research19::Researcher")
research19_Paragraph = Class(name="research19::Paragraph")
research19_Progress = Class(name="research19::Progress")
research19_PaperKeyword = Class(name="research19::PaperKeyword")
research19_State = Class(name="research19::State")
research19_Write = Class(name="research19::Write")
research19_Review = Class(name="research19::Review")
research19_Paper = Class(name="research19::Paper")
research19_Skill = Class(name="research19::Skill")
research19_Position = Class(name="research19::Position")
research19_Collaboration = Class(name="research19::Collaboration")
research19_PublicationStructure = Class(name="research19::PublicationStructure")
Counted = Class(name="Counted")
research19_ReviewNote = Class(name="research19::ReviewNote")
Labelled = Class(name="Labelled")
research19_Counted = Class(name="research19::Counted", is_abstract=True)
research19_Labelled = Class(name="research19::Labelled", is_abstract=True)
research19_KnowledgeManager = Class(name="research19::KnowledgeManager")
research19_PublicationSystem = Class(name="research19::PublicationSystem")
research19_PublicationStatus = Class(name="research19::PublicationStatus")
research19_Named = Class(name="research19::Named", is_abstract=True)
research19_StateMachineVariable = Class(name="research19::StateMachineVariable")
research19_StateMachineObject = Class(name="research19::StateMachineObject", is_abstract=True)
research19_Transition = Class(name="research19::Transition")
StateMachineObject = Class(name="StateMachineObject")
research19_Keyword = Class(name="research19::Keyword")
research19_Action = Class(name="research19::Action")

# research19_PublicationProcess class attributes and methods
research19_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
research19_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
research19_PublicationProcess.attributes={research19_PublicationProcess_minTime, research19_PublicationProcess_maxTime}

# Named class attributes and methods

# research19_Phase class attributes and methods
research19_Phase_name: Property = Property(name="name", type=StringType)
research19_Phase.attributes={research19_Phase_name}

# research19_Researcher class attributes and methods
research19_Researcher_name: Property = Property(name="name", type=StringType)
research19_Researcher_forName: Property = Property(name="forName", type=StringType)
research19_Researcher.attributes={research19_Researcher_name, research19_Researcher_forName}

# research19_Paragraph class attributes and methods
research19_Paragraph_content: Property = Property(name="content", type=StringType)
research19_Paragraph.attributes={research19_Paragraph_content}

# research19_Progress class attributes and methods
research19_Progress_percent: Property = Property(name="percent", type=IntegerType)
research19_Progress.attributes={research19_Progress_percent}

# research19_PaperKeyword class attributes and methods
research19_PaperKeyword_weight: Property = Property(name="weight", type=IntegerType)
research19_PaperKeyword.attributes={research19_PaperKeyword_weight}

# research19_State class attributes and methods
research19_State_id: Property = Property(name="id", type=IntegerType)
research19_State_kind: Property = Property(name="kind", type=StringType)
research19_State_name: Property = Property(name="name", type=StringType)
research19_State.attributes={research19_State_kind, research19_State_id, research19_State_name}

# research19_Write class attributes and methods
research19_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
research19_Write.attributes={research19_Write_timeSpent}

# research19_Review class attributes and methods
research19_Review_date: Property = Property(name="date", type=DateType)
research19_Review.attributes={research19_Review_date}

# research19_Paper class attributes and methods

# research19_Skill class attributes and methods
research19_Skill_description: Property = Property(name="description", type=StringType)
research19_Skill.attributes={research19_Skill_description}

# research19_Position class attributes and methods
research19_Position_description: Property = Property(name="description", type=StringType)
research19_Position.attributes={research19_Position_description}

# research19_Collaboration class attributes and methods
research19_Collaboration_ratio: Property = Property(name="ratio", type=IntegerType)
research19_Collaboration.attributes={research19_Collaboration_ratio}

# research19_PublicationStructure class attributes and methods

# Counted class attributes and methods

# research19_ReviewNote class attributes and methods
research19_ReviewNote_content: Property = Property(name="content", type=StringType)
research19_ReviewNote.attributes={research19_ReviewNote_content}

# Labelled class attributes and methods

# research19_Counted class attributes and methods
research19_Counted_id: Property = Property(name="id", type=IntegerType)
research19_Counted.attributes={research19_Counted_id}

# research19_Labelled class attributes and methods
research19_Labelled_lname: Property = Property(name="lname", type=StringType)
research19_Labelled.attributes={research19_Labelled_lname}

# research19_KnowledgeManager class attributes and methods

# research19_PublicationSystem class attributes and methods

# research19_PublicationStatus class attributes and methods
research19_PublicationStatus_label: Property = Property(name="label", type=StringType)
research19_PublicationStatus.attributes={research19_PublicationStatus_label}

# research19_Named class attributes and methods
research19_Named_name: Property = Property(name="name", type=StringType)
research19_Named.attributes={research19_Named_name}

# research19_StateMachineVariable class attributes and methods

# research19_StateMachineObject class attributes and methods
research19_StateMachineObject_label: Property = Property(name="label", type=StringType)
research19_StateMachineObject.attributes={research19_StateMachineObject_label}

# research19_Transition class attributes and methods
research19_Transition_guardLabel: Property = Property(name="guardLabel", type=StringType)
research19_Transition_guardExpression: Property = Property(name="guardExpression", type=StringType)
research19_Transition.attributes={research19_Transition_guardExpression, research19_Transition_guardLabel}

# StateMachineObject class attributes and methods

# research19_Keyword class attributes and methods
research19_Keyword_word: Property = Property(name="word", type=StringType)
research19_Keyword.attributes={research19_Keyword_word}

# research19_Action class attributes and methods
research19_Action_actionLabel: Property = Property(name="actionLabel", type=StringType)
research19_Action_actionStatement: Property = Property(name="actionStatement", type=StringType)
research19_Action.attributes={research19_Action_actionLabel, research19_Action_actionStatement}

# Relationships
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="research19_Phase", type=research19_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_PublicationProcess", type=research19_Phase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs11: BinaryAssociation = BinaryAssociation(
    name="paragraphs11",
    ends={
        Property(name="research19_Paragraph", type=research19_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Paper", type=research19_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
progress12: BinaryAssociation = BinaryAssociation(
    name="progress12",
    ends={
        Property(name="Progress", type=research19_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=research19_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors13: BinaryAssociation = BinaryAssociation(
    name="authors13",
    ends={
        Property(name="Researcher", type=research19_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=research19_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
keywords14: BinaryAssociation = BinaryAssociation(
    name="keywords14",
    ends={
        Property(name="research19_PaperKeyword", type=research19_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Paper15", type=research19_PaperKeyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
citedBy17: BinaryAssociation = BinaryAssociation(
    name="citedBy17",
    ends={
        Property(name="research19_Paper18", type=research19_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Paper16", type=research19_Paper, multiplicity=Multiplicity(0, 1))
    }
)
state19: BinaryAssociation = BinaryAssociation(
    name="state19",
    ends={
        Property(name="research19_State", type=research19_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Paper20", type=research19_State, multiplicity=Multiplicity(0, 1))
    }
)
writes1: BinaryAssociation = BinaryAssociation(
    name="writes1",
    ends={
        Property(name="research19_Write", type=research19_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Researcher", type=research19_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews2: BinaryAssociation = BinaryAssociation(
    name="reviews2",
    ends={
        Property(name="research19_Review", type=research19_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Researcher3", type=research19_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_papers4: BinaryAssociation = BinaryAssociation(
    name="res_papers4",
    ends={
        Property(name="Paper", type=research19_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=research19_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills5: BinaryAssociation = BinaryAssociation(
    name="skills5",
    ends={
        Property(name="research19_Skill", type=research19_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Researcher6", type=research19_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_position7: BinaryAssociation = BinaryAssociation(
    name="res_position7",
    ends={
        Property(name="research19_Position", type=research19_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Researcher8", type=research19_Position, multiplicity=Multiplicity(0, 1))
    }
)
collaborations9: BinaryAssociation = BinaryAssociation(
    name="collaborations9",
    ends={
        Property(name="research19_Collaboration", type=research19_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Researcher10", type=research19_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraph27: BinaryAssociation = BinaryAssociation(
    name="paragraph27",
    ends={
        Property(name="research19_Paragraph29", type=research19_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Write28", type=research19_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
reviewNote30: BinaryAssociation = BinaryAssociation(
    name="reviewNote30",
    ends={
        Property(name="research19_ReviewNote32", type=research19_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Review31", type=research19_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
reviews21: BinaryAssociation = BinaryAssociation(
    name="reviews21",
    ends={
        Property(name="research19_ReviewNote", type=research19_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Paragraph22", type=research19_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process23: BinaryAssociation = BinaryAssociation(
    name="process23",
    ends={
        Property(name="research19_PublicationProcess24", type=research19_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Progress", type=research19_PublicationProcess, multiplicity=Multiplicity(0, 1))
    }
)
paper25: BinaryAssociation = BinaryAssociation(
    name="paper25",
    ends={
        Property(name="Paper26", type=research19_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="progress", type=research19_Paper, multiplicity=Multiplicity(0, 1))
    }
)
parent51: BinaryAssociation = BinaryAssociation(
    name="parent51",
    ends={
        Property(name="research19_Position52", type=research19_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Position50", type=research19_Position, multiplicity=Multiplicity(0, 1))
    }
)
researchers33: BinaryAssociation = BinaryAssociation(
    name="researchers33",
    ends={
        Property(name="research19_Researcher34", type=research19_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_PublicationStructure", type=research19_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers35: BinaryAssociation = BinaryAssociation(
    name="papers35",
    ends={
        Property(name="research19_Paper37", type=research19_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_PublicationStructure36", type=research19_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
knowledgeMan38: BinaryAssociation = BinaryAssociation(
    name="knowledgeMan38",
    ends={
        Property(name="research19_KnowledgeManager", type=research19_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_PublicationStructure39", type=research19_KnowledgeManager, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
processView40: BinaryAssociation = BinaryAssociation(
    name="processView40",
    ends={
        Property(name="research19_PublicationProcess41", type=research19_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_PublicationSystem", type=research19_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuralView42: BinaryAssociation = BinaryAssociation(
    name="structuralView42",
    ends={
        Property(name="research19_PublicationStructure44", type=research19_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_PublicationSystem43", type=research19_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
positions45: BinaryAssociation = BinaryAssociation(
    name="positions45",
    ends={
        Property(name="research19_Position47", type=research19_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_PublicationSystem46", type=research19_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviorView48: BinaryAssociation = BinaryAssociation(
    name="behaviorView48",
    ends={
        Property(name="research19_PublicationStatus", type=research19_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_PublicationSystem49", type=research19_PublicationStatus, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
col_paper61: BinaryAssociation = BinaryAssociation(
    name="col_paper61",
    ends={
        Property(name="research19_Paper63", type=research19_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Collaboration62", type=research19_Paper, multiplicity=Multiplicity(0, 1))
    }
)
machineVariables64: BinaryAssociation = BinaryAssociation(
    name="machineVariables64",
    ends={
        Property(name="research19_StateMachineVariable", type=research19_PublicationStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_PublicationStatus65", type=research19_StateMachineVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pubStates66: BinaryAssociation = BinaryAssociation(
    name="pubStates66",
    ends={
        Property(name="research19_State68", type=research19_PublicationStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_PublicationStatus67", type=research19_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kpapers53: BinaryAssociation = BinaryAssociation(
    name="kpapers53",
    ends={
        Property(name="research19_Paper54", type=research19_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Keyword", type=research19_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
allkeywords55: BinaryAssociation = BinaryAssociation(
    name="allkeywords55",
    ends={
        Property(name="research19_Keyword57", type=research19_KnowledgeManager, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_KnowledgeManager56", type=research19_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyword58: BinaryAssociation = BinaryAssociation(
    name="keyword58",
    ends={
        Property(name="research19_Keyword60", type=research19_PaperKeyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_PaperKeyword59", type=research19_Keyword, multiplicity=Multiplicity(0, 1))
    }
)
next83: BinaryAssociation = BinaryAssociation(
    name="next83",
    ends={
        Property(name="research19_Action84", type=research19_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Action82", type=research19_Action, multiplicity=Multiplicity(0, 1))
    }
)
t_actions69: BinaryAssociation = BinaryAssociation(
    name="t_actions69",
    ends={
        Property(name="research19_Action", type=research19_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Transition", type=research19_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source70: BinaryAssociation = BinaryAssociation(
    name="source70",
    ends={
        Property(name="research19_State72", type=research19_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Transition71", type=research19_State, multiplicity=Multiplicity(0, 1))
    }
)
target73: BinaryAssociation = BinaryAssociation(
    name="target73",
    ends={
        Property(name="research19_State75", type=research19_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_Transition74", type=research19_State, multiplicity=Multiplicity(0, 1))
    }
)
transitions76: BinaryAssociation = BinaryAssociation(
    name="transitions76",
    ends={
        Property(name="research19_Transition78", type=research19_State, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_State77", type=research19_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
s_actions79: BinaryAssociation = BinaryAssociation(
    name="s_actions79",
    ends={
        Property(name="research19_Action81", type=research19_State, multiplicity=Multiplicity(1, 1)),
        Property(name="research19_State80", type=research19_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_research19_PublicationProcess_Named = Generalization(general=Named, specific=research19_PublicationProcess)
gen_research19_Paper_Named = Generalization(general=Named, specific=research19_Paper)
gen_research19_Write_Labelled = Generalization(general=Labelled, specific=research19_Write)
gen_research19_Review_Labelled = Generalization(general=Labelled, specific=research19_Review)
gen_research19_PublicationStructure_Named = Generalization(general=Named, specific=research19_PublicationStructure)
gen_research19_Paragraph_Counted = Generalization(general=Counted, specific=research19_Paragraph)
gen_research19_Paragraph_Named = Generalization(general=Named, specific=research19_Paragraph)
gen_research19_ReviewNote_Named = Generalization(general=Named, specific=research19_ReviewNote)
gen_research19_Progress_Labelled = Generalization(general=Labelled, specific=research19_Progress)
gen_research19_Position_Named = Generalization(general=Named, specific=research19_Position)
gen_research19_PublicationSystem_Named = Generalization(general=Named, specific=research19_PublicationSystem)
gen_research19_Transition_StateMachineObject = Generalization(general=StateMachineObject, specific=research19_Transition)
gen_research19_Keyword_Named = Generalization(general=Named, specific=research19_Keyword)
gen_research19_KnowledgeManager_Named = Generalization(general=Named, specific=research19_KnowledgeManager)
gen_research19_State_StateMachineObject = Generalization(general=StateMachineObject, specific=research19_State)

# Domain Model
domain_model = DomainModel(
    name="research19",
    types={research19_PublicationProcess, Named, research19_Phase, research19_Researcher, research19_Paragraph, research19_Progress, research19_PaperKeyword, research19_State, research19_Write, research19_Review, research19_Paper, research19_Skill, research19_Position, research19_Collaboration, research19_PublicationStructure, Counted, research19_ReviewNote, Labelled, research19_Counted, research19_Labelled, research19_KnowledgeManager, research19_PublicationSystem, research19_PublicationStatus, research19_Named, research19_StateMachineVariable, research19_StateMachineObject, research19_Transition, StateMachineObject, research19_Keyword, research19_Action, StateType},
    associations={phases0, paragraphs11, progress12, authors13, keywords14, citedBy17, state19, writes1, reviews2, res_papers4, skills5, res_position7, collaborations9, paragraph27, reviewNote30, reviews21, process23, paper25, parent51, researchers33, papers35, knowledgeMan38, processView40, structuralView42, positions45, behaviorView48, col_paper61, machineVariables64, pubStates66, kpapers53, allkeywords55, keyword58, next83, t_actions69, source70, target73, transitions76, s_actions79},
    generalizations={gen_research19_PublicationProcess_Named, gen_research19_Paper_Named, gen_research19_Write_Labelled, gen_research19_Review_Labelled, gen_research19_PublicationStructure_Named, gen_research19_Paragraph_Counted, gen_research19_Paragraph_Named, gen_research19_ReviewNote_Named, gen_research19_Progress_Labelled, gen_research19_Position_Named, gen_research19_PublicationSystem_Named, gen_research19_Transition_StateMachineObject, gen_research19_Keyword_Named, gen_research19_KnowledgeManager_Named, gen_research19_State_StateMachineObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
research20_Phase = Class(name="research20::Phase")
research20_Researcher = Class(name="research20::Researcher")
research20_PublicationProcess = Class(name="research20::PublicationProcess")
Named = Class(name="Named")
research20_Progress = Class(name="research20::Progress")
research20_PaperKeyword = Class(name="research20::PaperKeyword")
research20_State = Class(name="research20::State")
Counted = Class(name="Counted")
research20_Write = Class(name="research20::Write")
research20_Review = Class(name="research20::Review")
research20_Paper = Class(name="research20::Paper")
research20_Skill = Class(name="research20::Skill")
research20_Position = Class(name="research20::Position")
research20_Collaboration = Class(name="research20::Collaboration")
research20_Paragraph = Class(name="research20::Paragraph")
research20_PublicationStructure = Class(name="research20::PublicationStructure")
research20_ReviewNote = Class(name="research20::ReviewNote")
Labelled = Class(name="Labelled")
research20_PublicationStatus = Class(name="research20::PublicationStatus")
research20_PublicationSystem = Class(name="research20::PublicationSystem")
research20_KnowledgeManager = Class(name="research20::KnowledgeManager")
research20_Named = Class(name="research20::Named", is_abstract=True)
research20_Counted = Class(name="research20::Counted", is_abstract=True)
research20_Labelled = Class(name="research20::Labelled", is_abstract=True)
research20_Keyword = Class(name="research20::Keyword")
research20_StateMachineVariable = Class(name="research20::StateMachineVariable")
research20_StateMachineObject = Class(name="research20::StateMachineObject", is_abstract=True)
research20_Transition = Class(name="research20::Transition")
StateMachineObject = Class(name="StateMachineObject")
research20_Action = Class(name="research20::Action")

# research20_Phase class attributes and methods
research20_Phase_name: Property = Property(name="name", type=StringType)
research20_Phase.attributes={research20_Phase_name}

# research20_Researcher class attributes and methods
research20_Researcher_name: Property = Property(name="name", type=StringType)
research20_Researcher_forName: Property = Property(name="forName", type=StringType)
research20_Researcher.attributes={research20_Researcher_name, research20_Researcher_forName}

# research20_PublicationProcess class attributes and methods
research20_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
research20_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
research20_PublicationProcess.attributes={research20_PublicationProcess_minTime, research20_PublicationProcess_maxTime}

# Named class attributes and methods

# research20_Progress class attributes and methods
research20_Progress_percent: Property = Property(name="percent", type=IntegerType)
research20_Progress.attributes={research20_Progress_percent}

# research20_PaperKeyword class attributes and methods
research20_PaperKeyword_weight: Property = Property(name="weight", type=IntegerType)
research20_PaperKeyword.attributes={research20_PaperKeyword_weight}

# research20_State class attributes and methods
research20_State_id: Property = Property(name="id", type=IntegerType)
research20_State_kind: Property = Property(name="kind", type=StringType)
research20_State_name: Property = Property(name="name", type=StringType)
research20_State.attributes={research20_State_name, research20_State_id, research20_State_kind}

# Counted class attributes and methods

# research20_Write class attributes and methods
research20_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
research20_Write.attributes={research20_Write_timeSpent}

# research20_Review class attributes and methods
research20_Review_date: Property = Property(name="date", type=DateType)
research20_Review.attributes={research20_Review_date}

# research20_Paper class attributes and methods

# research20_Skill class attributes and methods
research20_Skill_description: Property = Property(name="description", type=StringType)
research20_Skill.attributes={research20_Skill_description}

# research20_Position class attributes and methods
research20_Position_description: Property = Property(name="description", type=StringType)
research20_Position.attributes={research20_Position_description}

# research20_Collaboration class attributes and methods
research20_Collaboration_ratio: Property = Property(name="ratio", type=IntegerType)
research20_Collaboration.attributes={research20_Collaboration_ratio}

# research20_Paragraph class attributes and methods
research20_Paragraph_content: Property = Property(name="content", type=StringType)
research20_Paragraph.attributes={research20_Paragraph_content}

# research20_PublicationStructure class attributes and methods

# research20_ReviewNote class attributes and methods
research20_ReviewNote_content: Property = Property(name="content", type=StringType)
research20_ReviewNote.attributes={research20_ReviewNote_content}

# Labelled class attributes and methods

# research20_PublicationStatus class attributes and methods
research20_PublicationStatus_label: Property = Property(name="label", type=StringType)
research20_PublicationStatus.attributes={research20_PublicationStatus_label}

# research20_PublicationSystem class attributes and methods

# research20_KnowledgeManager class attributes and methods

# research20_Named class attributes and methods
research20_Named_name: Property = Property(name="name", type=StringType)
research20_Named.attributes={research20_Named_name}

# research20_Counted class attributes and methods
research20_Counted_id: Property = Property(name="id", type=IntegerType)
research20_Counted.attributes={research20_Counted_id}

# research20_Labelled class attributes and methods
research20_Labelled_lname: Property = Property(name="lname", type=StringType)
research20_Labelled.attributes={research20_Labelled_lname}

# research20_Keyword class attributes and methods
research20_Keyword_word: Property = Property(name="word", type=StringType)
research20_Keyword.attributes={research20_Keyword_word}

# research20_StateMachineVariable class attributes and methods

# research20_StateMachineObject class attributes and methods
research20_StateMachineObject_label: Property = Property(name="label", type=StringType)
research20_StateMachineObject.attributes={research20_StateMachineObject_label}

# research20_Transition class attributes and methods
research20_Transition_guardLabel: Property = Property(name="guardLabel", type=StringType)
research20_Transition_guardExpression: Property = Property(name="guardExpression", type=StringType)
research20_Transition.attributes={research20_Transition_guardLabel, research20_Transition_guardExpression}

# StateMachineObject class attributes and methods

# research20_Action class attributes and methods
research20_Action_actionLabel: Property = Property(name="actionLabel", type=StringType)
research20_Action_actionStatement: Property = Property(name="actionStatement", type=StringType)
research20_Action.attributes={research20_Action_actionStatement, research20_Action_actionLabel}

# Relationships
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="research20_Phase", type=research20_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_PublicationProcess", type=research20_Phase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs11: BinaryAssociation = BinaryAssociation(
    name="paragraphs11",
    ends={
        Property(name="research20_Paragraph", type=research20_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Paper", type=research20_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
progress12: BinaryAssociation = BinaryAssociation(
    name="progress12",
    ends={
        Property(name="Progress", type=research20_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=research20_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors13: BinaryAssociation = BinaryAssociation(
    name="authors13",
    ends={
        Property(name="Researcher", type=research20_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=research20_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
keywords14: BinaryAssociation = BinaryAssociation(
    name="keywords14",
    ends={
        Property(name="research20_PaperKeyword", type=research20_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Paper15", type=research20_PaperKeyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
citedBy17: BinaryAssociation = BinaryAssociation(
    name="citedBy17",
    ends={
        Property(name="research20_Paper18", type=research20_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Paper16", type=research20_Paper, multiplicity=Multiplicity(0, 1))
    }
)
state19: BinaryAssociation = BinaryAssociation(
    name="state19",
    ends={
        Property(name="research20_State", type=research20_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Paper20", type=research20_State, multiplicity=Multiplicity(0, 1))
    }
)
writes1: BinaryAssociation = BinaryAssociation(
    name="writes1",
    ends={
        Property(name="research20_Write", type=research20_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Researcher", type=research20_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews2: BinaryAssociation = BinaryAssociation(
    name="reviews2",
    ends={
        Property(name="research20_Review", type=research20_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Researcher3", type=research20_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_papers4: BinaryAssociation = BinaryAssociation(
    name="res_papers4",
    ends={
        Property(name="Paper", type=research20_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=research20_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills5: BinaryAssociation = BinaryAssociation(
    name="skills5",
    ends={
        Property(name="research20_Skill", type=research20_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Researcher6", type=research20_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_position7: BinaryAssociation = BinaryAssociation(
    name="res_position7",
    ends={
        Property(name="research20_Position", type=research20_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Researcher8", type=research20_Position, multiplicity=Multiplicity(0, 1))
    }
)
collaborations9: BinaryAssociation = BinaryAssociation(
    name="collaborations9",
    ends={
        Property(name="research20_Collaboration", type=research20_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Researcher10", type=research20_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraph27: BinaryAssociation = BinaryAssociation(
    name="paragraph27",
    ends={
        Property(name="research20_Paragraph29", type=research20_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Write28", type=research20_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
reviewNote30: BinaryAssociation = BinaryAssociation(
    name="reviewNote30",
    ends={
        Property(name="research20_ReviewNote32", type=research20_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Review31", type=research20_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
reviews21: BinaryAssociation = BinaryAssociation(
    name="reviews21",
    ends={
        Property(name="research20_ReviewNote", type=research20_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Paragraph22", type=research20_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process23: BinaryAssociation = BinaryAssociation(
    name="process23",
    ends={
        Property(name="research20_PublicationProcess24", type=research20_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Progress", type=research20_PublicationProcess, multiplicity=Multiplicity(0, 1))
    }
)
paper25: BinaryAssociation = BinaryAssociation(
    name="paper25",
    ends={
        Property(name="Paper26", type=research20_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="progress", type=research20_Paper, multiplicity=Multiplicity(0, 1))
    }
)
behaviorView40: BinaryAssociation = BinaryAssociation(
    name="behaviorView40",
    ends={
        Property(name="research20_PublicationStatus", type=research20_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_PublicationStructure41", type=research20_PublicationStatus, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
processView42: BinaryAssociation = BinaryAssociation(
    name="processView42",
    ends={
        Property(name="research20_PublicationProcess43", type=research20_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_PublicationSystem", type=research20_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
researchers33: BinaryAssociation = BinaryAssociation(
    name="researchers33",
    ends={
        Property(name="research20_Researcher34", type=research20_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_PublicationStructure", type=research20_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers35: BinaryAssociation = BinaryAssociation(
    name="papers35",
    ends={
        Property(name="research20_Paper37", type=research20_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_PublicationStructure36", type=research20_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
knowledgeMan38: BinaryAssociation = BinaryAssociation(
    name="knowledgeMan38",
    ends={
        Property(name="research20_KnowledgeManager", type=research20_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_PublicationStructure39", type=research20_KnowledgeManager, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuralView44: BinaryAssociation = BinaryAssociation(
    name="structuralView44",
    ends={
        Property(name="research20_PublicationStructure46", type=research20_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_PublicationSystem45", type=research20_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
positions47: BinaryAssociation = BinaryAssociation(
    name="positions47",
    ends={
        Property(name="research20_Position49", type=research20_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_PublicationSystem48", type=research20_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allkeywords55: BinaryAssociation = BinaryAssociation(
    name="allkeywords55",
    ends={
        Property(name="research20_Keyword57", type=research20_KnowledgeManager, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_KnowledgeManager56", type=research20_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent51: BinaryAssociation = BinaryAssociation(
    name="parent51",
    ends={
        Property(name="research20_Position52", type=research20_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Position50", type=research20_Position, multiplicity=Multiplicity(0, 1))
    }
)
kpapers53: BinaryAssociation = BinaryAssociation(
    name="kpapers53",
    ends={
        Property(name="research20_Paper54", type=research20_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Keyword", type=research20_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
machineVariables64: BinaryAssociation = BinaryAssociation(
    name="machineVariables64",
    ends={
        Property(name="research20_StateMachineVariable", type=research20_PublicationStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_PublicationStatus65", type=research20_StateMachineVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pubStates66: BinaryAssociation = BinaryAssociation(
    name="pubStates66",
    ends={
        Property(name="research20_State68", type=research20_PublicationStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_PublicationStatus67", type=research20_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyword58: BinaryAssociation = BinaryAssociation(
    name="keyword58",
    ends={
        Property(name="research20_Keyword60", type=research20_PaperKeyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_PaperKeyword59", type=research20_Keyword, multiplicity=Multiplicity(0, 1))
    }
)
col_paper61: BinaryAssociation = BinaryAssociation(
    name="col_paper61",
    ends={
        Property(name="research20_Paper63", type=research20_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Collaboration62", type=research20_Paper, multiplicity=Multiplicity(0, 1))
    }
)
source70: BinaryAssociation = BinaryAssociation(
    name="source70",
    ends={
        Property(name="research20_State72", type=research20_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Transition71", type=research20_State, multiplicity=Multiplicity(0, 1))
    }
)
target73: BinaryAssociation = BinaryAssociation(
    name="target73",
    ends={
        Property(name="research20_State75", type=research20_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Transition74", type=research20_State, multiplicity=Multiplicity(0, 1))
    }
)
transitions76: BinaryAssociation = BinaryAssociation(
    name="transitions76",
    ends={
        Property(name="research20_Transition78", type=research20_State, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_State77", type=research20_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
t_actions69: BinaryAssociation = BinaryAssociation(
    name="t_actions69",
    ends={
        Property(name="research20_Action", type=research20_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Transition", type=research20_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
s_actions79: BinaryAssociation = BinaryAssociation(
    name="s_actions79",
    ends={
        Property(name="research20_Action81", type=research20_State, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_State80", type=research20_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next83: BinaryAssociation = BinaryAssociation(
    name="next83",
    ends={
        Property(name="research20_Action84", type=research20_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="research20_Action82", type=research20_Action, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_research20_PublicationProcess_Named = Generalization(general=Named, specific=research20_PublicationProcess)
gen_research20_Paragraph_Counted = Generalization(general=Counted, specific=research20_Paragraph)
gen_research20_Paragraph_Named = Generalization(general=Named, specific=research20_Paragraph)
gen_research20_Paper_Named = Generalization(general=Named, specific=research20_Paper)
gen_research20_Review_Labelled = Generalization(general=Labelled, specific=research20_Review)
gen_research20_PublicationStructure_Named = Generalization(general=Named, specific=research20_PublicationStructure)
gen_research20_ReviewNote_Named = Generalization(general=Named, specific=research20_ReviewNote)
gen_research20_Progress_Labelled = Generalization(general=Labelled, specific=research20_Progress)
gen_research20_Write_Labelled = Generalization(general=Labelled, specific=research20_Write)
gen_research20_PublicationSystem_Named = Generalization(general=Named, specific=research20_PublicationSystem)
gen_research20_Position_Named = Generalization(general=Named, specific=research20_Position)
gen_research20_KnowledgeManager_Named = Generalization(general=Named, specific=research20_KnowledgeManager)
gen_research20_Keyword_Named = Generalization(general=Named, specific=research20_Keyword)
gen_research20_State_StateMachineObject = Generalization(general=StateMachineObject, specific=research20_State)
gen_research20_Transition_StateMachineObject = Generalization(general=StateMachineObject, specific=research20_Transition)

# Domain Model
domain_model = DomainModel(
    name="research20",
    types={research20_Phase, research20_Researcher, research20_PublicationProcess, Named, research20_Progress, research20_PaperKeyword, research20_State, Counted, research20_Write, research20_Review, research20_Paper, research20_Skill, research20_Position, research20_Collaboration, research20_Paragraph, research20_PublicationStructure, research20_ReviewNote, Labelled, research20_PublicationStatus, research20_PublicationSystem, research20_KnowledgeManager, research20_Named, research20_Counted, research20_Labelled, research20_Keyword, research20_StateMachineVariable, research20_StateMachineObject, research20_Transition, StateMachineObject, research20_Action, StateType},
    associations={phases0, paragraphs11, progress12, authors13, keywords14, citedBy17, state19, writes1, reviews2, res_papers4, skills5, res_position7, collaborations9, paragraph27, reviewNote30, reviews21, process23, paper25, behaviorView40, processView42, researchers33, papers35, knowledgeMan38, structuralView44, positions47, allkeywords55, parent51, kpapers53, machineVariables64, pubStates66, keyword58, col_paper61, source70, target73, transitions76, t_actions69, s_actions79, next83},
    generalizations={gen_research20_PublicationProcess_Named, gen_research20_Paragraph_Counted, gen_research20_Paragraph_Named, gen_research20_Paper_Named, gen_research20_Review_Labelled, gen_research20_PublicationStructure_Named, gen_research20_ReviewNote_Named, gen_research20_Progress_Labelled, gen_research20_Write_Labelled, gen_research20_PublicationSystem_Named, gen_research20_Position_Named, gen_research20_KnowledgeManager_Named, gen_research20_Keyword_Named, gen_research20_State_StateMachineObject, gen_research20_Transition_StateMachineObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
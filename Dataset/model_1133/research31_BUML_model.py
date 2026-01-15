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
research31_Phase = Class(name="research31::Phase")
research31_Researcher = Class(name="research31::Researcher")
research31_PublicationProcess = Class(name="research31::PublicationProcess")
Named = Class(name="Named")
research31_Paragraph = Class(name="research31::Paragraph")
research31_Progress = Class(name="research31::Progress")
research31_PaperKeyword = Class(name="research31::PaperKeyword")
research31_State = Class(name="research31::State")
research31_Write = Class(name="research31::Write")
research31_Review = Class(name="research31::Review")
research31_Paper = Class(name="research31::Paper")
research31_Skill = Class(name="research31::Skill")
research31_Position = Class(name="research31::Position")
research31_Collaboration = Class(name="research31::Collaboration")
Counted = Class(name="Counted")
research31_ReviewNote = Class(name="research31::ReviewNote")
Labelled = Class(name="Labelled")
research31_KnowledgeManager = Class(name="research31::KnowledgeManager")
research31_PublicationStatus = Class(name="research31::PublicationStatus")
research31_PublicationSystem = Class(name="research31::PublicationSystem")
research31_PublicationStructure = Class(name="research31::PublicationStructure")
research31_Counted = Class(name="research31::Counted", is_abstract=True)
research31_Labelled = Class(name="research31::Labelled", is_abstract=True)
research31_Keyword = Class(name="research31::Keyword")
research31_Named = Class(name="research31::Named", is_abstract=True)
research31_StateMachineVariable = Class(name="research31::StateMachineVariable")
research31_StateMachineObject = Class(name="research31::StateMachineObject", is_abstract=True)
research31_Transition = Class(name="research31::Transition")
StateMachineObject = Class(name="StateMachineObject")
research31_Action = Class(name="research31::Action")

# research31_Phase class attributes and methods
research31_Phase_name: Property = Property(name="name", type=StringType)
research31_Phase.attributes={research31_Phase_name}

# research31_Researcher class attributes and methods
research31_Researcher_name: Property = Property(name="name", type=StringType)
research31_Researcher_forName: Property = Property(name="forName", type=StringType)
research31_Researcher.attributes={research31_Researcher_forName, research31_Researcher_name}

# research31_PublicationProcess class attributes and methods
research31_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
research31_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
research31_PublicationProcess.attributes={research31_PublicationProcess_minTime, research31_PublicationProcess_maxTime}

# Named class attributes and methods

# research31_Paragraph class attributes and methods
research31_Paragraph_content: Property = Property(name="content", type=StringType)
research31_Paragraph.attributes={research31_Paragraph_content}

# research31_Progress class attributes and methods
research31_Progress_percent: Property = Property(name="percent", type=IntegerType)
research31_Progress.attributes={research31_Progress_percent}

# research31_PaperKeyword class attributes and methods
research31_PaperKeyword_weight: Property = Property(name="weight", type=IntegerType)
research31_PaperKeyword.attributes={research31_PaperKeyword_weight}

# research31_State class attributes and methods
research31_State_id: Property = Property(name="id", type=IntegerType)
research31_State_kind: Property = Property(name="kind", type=StringType)
research31_State_name: Property = Property(name="name", type=StringType)
research31_State.attributes={research31_State_name, research31_State_kind, research31_State_id}

# research31_Write class attributes and methods
research31_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
research31_Write.attributes={research31_Write_timeSpent}

# research31_Review class attributes and methods
research31_Review_date: Property = Property(name="date", type=DateType)
research31_Review.attributes={research31_Review_date}

# research31_Paper class attributes and methods

# research31_Skill class attributes and methods
research31_Skill_description: Property = Property(name="description", type=StringType)
research31_Skill.attributes={research31_Skill_description}

# research31_Position class attributes and methods
research31_Position_description: Property = Property(name="description", type=StringType)
research31_Position.attributes={research31_Position_description}

# research31_Collaboration class attributes and methods
research31_Collaboration_ratio: Property = Property(name="ratio", type=IntegerType)
research31_Collaboration.attributes={research31_Collaboration_ratio}

# Counted class attributes and methods

# research31_ReviewNote class attributes and methods
research31_ReviewNote_content: Property = Property(name="content", type=StringType)
research31_ReviewNote.attributes={research31_ReviewNote_content}

# Labelled class attributes and methods

# research31_KnowledgeManager class attributes and methods

# research31_PublicationStatus class attributes and methods
research31_PublicationStatus_label: Property = Property(name="label", type=StringType)
research31_PublicationStatus.attributes={research31_PublicationStatus_label}

# research31_PublicationSystem class attributes and methods

# research31_PublicationStructure class attributes and methods

# research31_Counted class attributes and methods
research31_Counted_id: Property = Property(name="id", type=IntegerType)
research31_Counted.attributes={research31_Counted_id}

# research31_Labelled class attributes and methods
research31_Labelled_lname: Property = Property(name="lname", type=StringType)
research31_Labelled.attributes={research31_Labelled_lname}

# research31_Keyword class attributes and methods
research31_Keyword_word: Property = Property(name="word", type=StringType)
research31_Keyword.attributes={research31_Keyword_word}

# research31_Named class attributes and methods
research31_Named_name: Property = Property(name="name", type=StringType)
research31_Named.attributes={research31_Named_name}

# research31_StateMachineVariable class attributes and methods

# research31_StateMachineObject class attributes and methods
research31_StateMachineObject_label: Property = Property(name="label", type=StringType)
research31_StateMachineObject.attributes={research31_StateMachineObject_label}

# research31_Transition class attributes and methods
research31_Transition_guardLabel: Property = Property(name="guardLabel", type=StringType)
research31_Transition_guardExpression: Property = Property(name="guardExpression", type=StringType)
research31_Transition.attributes={research31_Transition_guardLabel, research31_Transition_guardExpression}

# StateMachineObject class attributes and methods

# research31_Action class attributes and methods
research31_Action_actionLabel: Property = Property(name="actionLabel", type=StringType)
research31_Action_actionStatement: Property = Property(name="actionStatement", type=StringType)
research31_Action.attributes={research31_Action_actionStatement, research31_Action_actionLabel}

# Relationships
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="research31_Phase", type=research31_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_PublicationProcess", type=research31_Phase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs11: BinaryAssociation = BinaryAssociation(
    name="paragraphs11",
    ends={
        Property(name="research31_Paragraph", type=research31_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Paper", type=research31_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
progress12: BinaryAssociation = BinaryAssociation(
    name="progress12",
    ends={
        Property(name="Progress", type=research31_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=research31_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors13: BinaryAssociation = BinaryAssociation(
    name="authors13",
    ends={
        Property(name="Researcher", type=research31_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=research31_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
keywords14: BinaryAssociation = BinaryAssociation(
    name="keywords14",
    ends={
        Property(name="research31_PaperKeyword", type=research31_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Paper15", type=research31_PaperKeyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
citedBy17: BinaryAssociation = BinaryAssociation(
    name="citedBy17",
    ends={
        Property(name="research31_Paper18", type=research31_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Paper16", type=research31_Paper, multiplicity=Multiplicity(0, 1))
    }
)
writes1: BinaryAssociation = BinaryAssociation(
    name="writes1",
    ends={
        Property(name="research31_Write", type=research31_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Researcher", type=research31_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews2: BinaryAssociation = BinaryAssociation(
    name="reviews2",
    ends={
        Property(name="research31_Review", type=research31_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Researcher3", type=research31_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_papers4: BinaryAssociation = BinaryAssociation(
    name="res_papers4",
    ends={
        Property(name="Paper", type=research31_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=research31_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills5: BinaryAssociation = BinaryAssociation(
    name="skills5",
    ends={
        Property(name="research31_Skill", type=research31_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Researcher6", type=research31_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_position7: BinaryAssociation = BinaryAssociation(
    name="res_position7",
    ends={
        Property(name="research31_Position", type=research31_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Researcher8", type=research31_Position, multiplicity=Multiplicity(0, 1))
    }
)
collaborations9: BinaryAssociation = BinaryAssociation(
    name="collaborations9",
    ends={
        Property(name="research31_Collaboration", type=research31_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Researcher10", type=research31_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process23: BinaryAssociation = BinaryAssociation(
    name="process23",
    ends={
        Property(name="research31_PublicationProcess24", type=research31_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Progress", type=research31_PublicationProcess, multiplicity=Multiplicity(0, 1))
    }
)
paper25: BinaryAssociation = BinaryAssociation(
    name="paper25",
    ends={
        Property(name="Paper26", type=research31_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="progress", type=research31_Paper, multiplicity=Multiplicity(0, 1))
    }
)
state19: BinaryAssociation = BinaryAssociation(
    name="state19",
    ends={
        Property(name="research31_State", type=research31_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Paper20", type=research31_State, multiplicity=Multiplicity(0, 1))
    }
)
paragraph27: BinaryAssociation = BinaryAssociation(
    name="paragraph27",
    ends={
        Property(name="research31_Paragraph29", type=research31_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Write28", type=research31_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
reviews21: BinaryAssociation = BinaryAssociation(
    name="reviews21",
    ends={
        Property(name="research31_ReviewNote", type=research31_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Paragraph22", type=research31_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviewNote30: BinaryAssociation = BinaryAssociation(
    name="reviewNote30",
    ends={
        Property(name="research31_ReviewNote32", type=research31_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Review31", type=research31_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
researchers33: BinaryAssociation = BinaryAssociation(
    name="researchers33",
    ends={
        Property(name="research31_Researcher34", type=research31_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_PublicationStructure", type=research31_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers35: BinaryAssociation = BinaryAssociation(
    name="papers35",
    ends={
        Property(name="research31_Paper37", type=research31_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_PublicationStructure36", type=research31_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
knowledgeMan38: BinaryAssociation = BinaryAssociation(
    name="knowledgeMan38",
    ends={
        Property(name="research31_KnowledgeManager", type=research31_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_PublicationStructure39", type=research31_KnowledgeManager, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
status40: BinaryAssociation = BinaryAssociation(
    name="status40",
    ends={
        Property(name="research31_PublicationStatus", type=research31_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_PublicationStructure41", type=research31_PublicationStatus, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
processView42: BinaryAssociation = BinaryAssociation(
    name="processView42",
    ends={
        Property(name="research31_PublicationProcess43", type=research31_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_PublicationSystem", type=research31_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent51: BinaryAssociation = BinaryAssociation(
    name="parent51",
    ends={
        Property(name="research31_Position52", type=research31_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Position50", type=research31_Position, multiplicity=Multiplicity(0, 1))
    }
)
kpapers53: BinaryAssociation = BinaryAssociation(
    name="kpapers53",
    ends={
        Property(name="research31_Paper54", type=research31_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Keyword", type=research31_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
structuralView44: BinaryAssociation = BinaryAssociation(
    name="structuralView44",
    ends={
        Property(name="research31_PublicationStructure46", type=research31_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_PublicationSystem45", type=research31_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
positions47: BinaryAssociation = BinaryAssociation(
    name="positions47",
    ends={
        Property(name="research31_Position49", type=research31_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_PublicationSystem48", type=research31_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyword58: BinaryAssociation = BinaryAssociation(
    name="keyword58",
    ends={
        Property(name="research31_Keyword60", type=research31_PaperKeyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_PaperKeyword59", type=research31_Keyword, multiplicity=Multiplicity(0, 1))
    }
)
col_paper61: BinaryAssociation = BinaryAssociation(
    name="col_paper61",
    ends={
        Property(name="research31_Paper63", type=research31_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Collaboration62", type=research31_Paper, multiplicity=Multiplicity(0, 1))
    }
)
machineVariables64: BinaryAssociation = BinaryAssociation(
    name="machineVariables64",
    ends={
        Property(name="research31_StateMachineVariable", type=research31_PublicationStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_PublicationStatus65", type=research31_StateMachineVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pubStates66: BinaryAssociation = BinaryAssociation(
    name="pubStates66",
    ends={
        Property(name="research31_State68", type=research31_PublicationStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_PublicationStatus67", type=research31_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allkeywords55: BinaryAssociation = BinaryAssociation(
    name="allkeywords55",
    ends={
        Property(name="research31_Keyword57", type=research31_KnowledgeManager, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_KnowledgeManager56", type=research31_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target73: BinaryAssociation = BinaryAssociation(
    name="target73",
    ends={
        Property(name="research31_State75", type=research31_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Transition74", type=research31_State, multiplicity=Multiplicity(0, 1))
    }
)
transitions76: BinaryAssociation = BinaryAssociation(
    name="transitions76",
    ends={
        Property(name="research31_Transition78", type=research31_State, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_State77", type=research31_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
s_actions79: BinaryAssociation = BinaryAssociation(
    name="s_actions79",
    ends={
        Property(name="research31_Action81", type=research31_State, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_State80", type=research31_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next83: BinaryAssociation = BinaryAssociation(
    name="next83",
    ends={
        Property(name="research31_Action84", type=research31_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Action82", type=research31_Action, multiplicity=Multiplicity(0, 1))
    }
)
t_actions69: BinaryAssociation = BinaryAssociation(
    name="t_actions69",
    ends={
        Property(name="research31_Action", type=research31_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Transition", type=research31_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source70: BinaryAssociation = BinaryAssociation(
    name="source70",
    ends={
        Property(name="research31_State72", type=research31_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research31_Transition71", type=research31_State, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_research31_PublicationProcess_Named = Generalization(general=Named, specific=research31_PublicationProcess)
gen_research31_Paper_Named = Generalization(general=Named, specific=research31_Paper)
gen_research31_Write_Labelled = Generalization(general=Labelled, specific=research31_Write)
gen_research31_Paragraph_Counted = Generalization(general=Counted, specific=research31_Paragraph)
gen_research31_Paragraph_Named = Generalization(general=Named, specific=research31_Paragraph)
gen_research31_Review_Labelled = Generalization(general=Labelled, specific=research31_Review)
gen_research31_ReviewNote_Named = Generalization(general=Named, specific=research31_ReviewNote)
gen_research31_Progress_Labelled = Generalization(general=Labelled, specific=research31_Progress)
gen_research31_PublicationSystem_Named = Generalization(general=Named, specific=research31_PublicationSystem)
gen_research31_PublicationStructure_Named = Generalization(general=Named, specific=research31_PublicationStructure)
gen_research31_Position_Named = Generalization(general=Named, specific=research31_Position)
gen_research31_Keyword_Named = Generalization(general=Named, specific=research31_Keyword)
gen_research31_Transition_StateMachineObject = Generalization(general=StateMachineObject, specific=research31_Transition)
gen_research31_KnowledgeManager_Named = Generalization(general=Named, specific=research31_KnowledgeManager)
gen_research31_State_StateMachineObject = Generalization(general=StateMachineObject, specific=research31_State)

# Domain Model
domain_model = DomainModel(
    name="research31",
    types={research31_Phase, research31_Researcher, research31_PublicationProcess, Named, research31_Paragraph, research31_Progress, research31_PaperKeyword, research31_State, research31_Write, research31_Review, research31_Paper, research31_Skill, research31_Position, research31_Collaboration, Counted, research31_ReviewNote, Labelled, research31_KnowledgeManager, research31_PublicationStatus, research31_PublicationSystem, research31_PublicationStructure, research31_Counted, research31_Labelled, research31_Keyword, research31_Named, research31_StateMachineVariable, research31_StateMachineObject, research31_Transition, StateMachineObject, research31_Action, StateType},
    associations={phases0, paragraphs11, progress12, authors13, keywords14, citedBy17, writes1, reviews2, res_papers4, skills5, res_position7, collaborations9, process23, paper25, state19, paragraph27, reviews21, reviewNote30, researchers33, papers35, knowledgeMan38, status40, processView42, parent51, kpapers53, structuralView44, positions47, keyword58, col_paper61, machineVariables64, pubStates66, allkeywords55, target73, transitions76, s_actions79, next83, t_actions69, source70},
    generalizations={gen_research31_PublicationProcess_Named, gen_research31_Paper_Named, gen_research31_Write_Labelled, gen_research31_Paragraph_Counted, gen_research31_Paragraph_Named, gen_research31_Review_Labelled, gen_research31_ReviewNote_Named, gen_research31_Progress_Labelled, gen_research31_PublicationSystem_Named, gen_research31_PublicationStructure_Named, gen_research31_Position_Named, gen_research31_Keyword_Named, gen_research31_Transition_StateMachineObject, gen_research31_KnowledgeManager_Named, gen_research31_State_StateMachineObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
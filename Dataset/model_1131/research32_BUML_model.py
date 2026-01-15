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
            EnumerationLiteral(name="ongoing"),
			EnumerationLiteral(name="final"),
			EnumerationLiteral(name="initial")
    }
)

# Classes
research32_PublicationProcess = Class(name="research32::PublicationProcess")
Named = Class(name="Named")
research32_Phase = Class(name="research32::Phase")
research32_Researcher = Class(name="research32::Researcher")
research32_Write = Class(name="research32::Write")
research32_Review = Class(name="research32::Review")
research32_Paper = Class(name="research32::Paper")
research32_Skill = Class(name="research32::Skill")
research32_Position = Class(name="research32::Position")
research32_Collaboration = Class(name="research32::Collaboration")
research32_Progress = Class(name="research32::Progress")
research32_PaperKeyword = Class(name="research32::PaperKeyword")
research32_State = Class(name="research32::State")
Counted = Class(name="Counted")
research32_ReviewNote = Class(name="research32::ReviewNote")
research32_Paragraph = Class(name="research32::Paragraph")
Labelled = Class(name="Labelled")
research32_PublicationStructure = Class(name="research32::PublicationStructure")
research32_KnowledgeManager = Class(name="research32::KnowledgeManager")
research32_PublicationStatus = Class(name="research32::PublicationStatus")
research32_PublicationSystem = Class(name="research32::PublicationSystem")
research32_Named = Class(name="research32::Named", is_abstract=True)
research32_Counted = Class(name="research32::Counted", is_abstract=True)
research32_Labelled = Class(name="research32::Labelled", is_abstract=True)
research32_Keyword = Class(name="research32::Keyword")
research32_StateMachineVariable = Class(name="research32::StateMachineVariable")
research32_StateMachineObject = Class(name="research32::StateMachineObject", is_abstract=True)
research32_Transition = Class(name="research32::Transition")
StateMachineObject = Class(name="StateMachineObject")
research32_Action = Class(name="research32::Action")

# research32_PublicationProcess class attributes and methods
research32_PublicationProcess_minTime: Property = Property(name="minTime", type=IntegerType)
research32_PublicationProcess_maxTime: Property = Property(name="maxTime", type=IntegerType)
research32_PublicationProcess.attributes={research32_PublicationProcess_maxTime, research32_PublicationProcess_minTime}

# Named class attributes and methods

# research32_Phase class attributes and methods
research32_Phase_name: Property = Property(name="name", type=StringType)
research32_Phase.attributes={research32_Phase_name}

# research32_Researcher class attributes and methods
research32_Researcher_name: Property = Property(name="name", type=StringType)
research32_Researcher_forName: Property = Property(name="forName", type=StringType)
research32_Researcher.attributes={research32_Researcher_name, research32_Researcher_forName}

# research32_Write class attributes and methods
research32_Write_timeSpent: Property = Property(name="timeSpent", type=IntegerType)
research32_Write.attributes={research32_Write_timeSpent}

# research32_Review class attributes and methods
research32_Review_date: Property = Property(name="date", type=DateType)
research32_Review.attributes={research32_Review_date}

# research32_Paper class attributes and methods

# research32_Skill class attributes and methods
research32_Skill_description: Property = Property(name="description", type=StringType)
research32_Skill.attributes={research32_Skill_description}

# research32_Position class attributes and methods
research32_Position_description: Property = Property(name="description", type=StringType)
research32_Position.attributes={research32_Position_description}

# research32_Collaboration class attributes and methods
research32_Collaboration_ratio: Property = Property(name="ratio", type=IntegerType)
research32_Collaboration.attributes={research32_Collaboration_ratio}

# research32_Progress class attributes and methods
research32_Progress_percent: Property = Property(name="percent", type=IntegerType)
research32_Progress.attributes={research32_Progress_percent}

# research32_PaperKeyword class attributes and methods
research32_PaperKeyword_weight: Property = Property(name="weight", type=IntegerType)
research32_PaperKeyword.attributes={research32_PaperKeyword_weight}

# research32_State class attributes and methods
research32_State_id: Property = Property(name="id", type=IntegerType)
research32_State_kind: Property = Property(name="kind", type=StringType)
research32_State_name: Property = Property(name="name", type=StringType)
research32_State.attributes={research32_State_kind, research32_State_name, research32_State_id}

# Counted class attributes and methods

# research32_ReviewNote class attributes and methods
research32_ReviewNote_content: Property = Property(name="content", type=StringType)
research32_ReviewNote.attributes={research32_ReviewNote_content}

# research32_Paragraph class attributes and methods
research32_Paragraph_content: Property = Property(name="content", type=StringType)
research32_Paragraph.attributes={research32_Paragraph_content}

# Labelled class attributes and methods

# research32_PublicationStructure class attributes and methods

# research32_KnowledgeManager class attributes and methods

# research32_PublicationStatus class attributes and methods
research32_PublicationStatus_label: Property = Property(name="label", type=StringType)
research32_PublicationStatus.attributes={research32_PublicationStatus_label}

# research32_PublicationSystem class attributes and methods

# research32_Named class attributes and methods
research32_Named_name: Property = Property(name="name", type=StringType)
research32_Named.attributes={research32_Named_name}

# research32_Counted class attributes and methods
research32_Counted_id: Property = Property(name="id", type=IntegerType)
research32_Counted.attributes={research32_Counted_id}

# research32_Labelled class attributes and methods
research32_Labelled_lname: Property = Property(name="lname", type=StringType)
research32_Labelled.attributes={research32_Labelled_lname}

# research32_Keyword class attributes and methods
research32_Keyword_word: Property = Property(name="word", type=StringType)
research32_Keyword.attributes={research32_Keyword_word}

# research32_StateMachineVariable class attributes and methods

# research32_StateMachineObject class attributes and methods
research32_StateMachineObject_label: Property = Property(name="label", type=StringType)
research32_StateMachineObject.attributes={research32_StateMachineObject_label}

# research32_Transition class attributes and methods
research32_Transition_guardLabel: Property = Property(name="guardLabel", type=StringType)
research32_Transition_guardExpression: Property = Property(name="guardExpression", type=StringType)
research32_Transition.attributes={research32_Transition_guardLabel, research32_Transition_guardExpression}

# StateMachineObject class attributes and methods

# research32_Action class attributes and methods
research32_Action_actionLabel: Property = Property(name="actionLabel", type=StringType)
research32_Action_actionStatement: Property = Property(name="actionStatement", type=StringType)
research32_Action.attributes={research32_Action_actionStatement, research32_Action_actionLabel}

# Relationships
phases0: BinaryAssociation = BinaryAssociation(
    name="phases0",
    ends={
        Property(name="research32_Phase", type=research32_PublicationProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_PublicationProcess", type=research32_Phase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writes1: BinaryAssociation = BinaryAssociation(
    name="writes1",
    ends={
        Property(name="research32_Write", type=research32_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Researcher", type=research32_Write, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reviews2: BinaryAssociation = BinaryAssociation(
    name="reviews2",
    ends={
        Property(name="research32_Review", type=research32_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Researcher3", type=research32_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_papers4: BinaryAssociation = BinaryAssociation(
    name="res_papers4",
    ends={
        Property(name="Paper", type=research32_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=research32_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
skills5: BinaryAssociation = BinaryAssociation(
    name="skills5",
    ends={
        Property(name="research32_Skill", type=research32_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Researcher6", type=research32_Skill, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
res_position7: BinaryAssociation = BinaryAssociation(
    name="res_position7",
    ends={
        Property(name="research32_Position", type=research32_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Researcher8", type=research32_Position, multiplicity=Multiplicity(0, 1))
    }
)
collaborations9: BinaryAssociation = BinaryAssociation(
    name="collaborations9",
    ends={
        Property(name="research32_Collaboration", type=research32_Researcher, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Researcher10", type=research32_Collaboration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs11: BinaryAssociation = BinaryAssociation(
    name="paragraphs11",
    ends={
        Property(name="research32_Paragraph", type=research32_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Paper", type=research32_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
progress12: BinaryAssociation = BinaryAssociation(
    name="progress12",
    ends={
        Property(name="Progress", type=research32_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="paper", type=research32_Progress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors13: BinaryAssociation = BinaryAssociation(
    name="authors13",
    ends={
        Property(name="Researcher", type=research32_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="res_papers", type=research32_Researcher, multiplicity=Multiplicity(0, 9999))
    }
)
keywords14: BinaryAssociation = BinaryAssociation(
    name="keywords14",
    ends={
        Property(name="research32_PaperKeyword", type=research32_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Paper15", type=research32_PaperKeyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
citedBy17: BinaryAssociation = BinaryAssociation(
    name="citedBy17",
    ends={
        Property(name="research32_Paper18", type=research32_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Paper16", type=research32_Paper, multiplicity=Multiplicity(0, 1))
    }
)
state19: BinaryAssociation = BinaryAssociation(
    name="state19",
    ends={
        Property(name="research32_State", type=research32_Paper, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Paper20", type=research32_State, multiplicity=Multiplicity(0, 1))
    }
)
reviews21: BinaryAssociation = BinaryAssociation(
    name="reviews21",
    ends={
        Property(name="research32_ReviewNote", type=research32_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Paragraph22", type=research32_ReviewNote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
process23: BinaryAssociation = BinaryAssociation(
    name="process23",
    ends={
        Property(name="research32_PublicationProcess24", type=research32_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Progress", type=research32_PublicationProcess, multiplicity=Multiplicity(0, 1))
    }
)
paper25: BinaryAssociation = BinaryAssociation(
    name="paper25",
    ends={
        Property(name="Paper26", type=research32_Progress, multiplicity=Multiplicity(1, 1)),
        Property(name="progress", type=research32_Paper, multiplicity=Multiplicity(0, 1))
    }
)
paragraph27: BinaryAssociation = BinaryAssociation(
    name="paragraph27",
    ends={
        Property(name="research32_Paragraph29", type=research32_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Write28", type=research32_Paragraph, multiplicity=Multiplicity(0, 1))
    }
)
reviewNote30: BinaryAssociation = BinaryAssociation(
    name="reviewNote30",
    ends={
        Property(name="research32_ReviewNote32", type=research32_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Review31", type=research32_ReviewNote, multiplicity=Multiplicity(0, 1))
    }
)
researchers33: BinaryAssociation = BinaryAssociation(
    name="researchers33",
    ends={
        Property(name="research32_Researcher34", type=research32_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_PublicationStructure", type=research32_Researcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
papers35: BinaryAssociation = BinaryAssociation(
    name="papers35",
    ends={
        Property(name="research32_Paper37", type=research32_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_PublicationStructure36", type=research32_Paper, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
knowledgeMan38: BinaryAssociation = BinaryAssociation(
    name="knowledgeMan38",
    ends={
        Property(name="research32_KnowledgeManager", type=research32_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_PublicationStructure39", type=research32_KnowledgeManager, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
status40: BinaryAssociation = BinaryAssociation(
    name="status40",
    ends={
        Property(name="research32_PublicationStatus", type=research32_PublicationStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_PublicationStructure41", type=research32_PublicationStatus, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
processView42: BinaryAssociation = BinaryAssociation(
    name="processView42",
    ends={
        Property(name="research32_PublicationProcess43", type=research32_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_PublicationSystem", type=research32_PublicationProcess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structuralView44: BinaryAssociation = BinaryAssociation(
    name="structuralView44",
    ends={
        Property(name="research32_PublicationStructure46", type=research32_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_PublicationSystem45", type=research32_PublicationStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
positions47: BinaryAssociation = BinaryAssociation(
    name="positions47",
    ends={
        Property(name="research32_Position49", type=research32_PublicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_PublicationSystem48", type=research32_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent51: BinaryAssociation = BinaryAssociation(
    name="parent51",
    ends={
        Property(name="research32_Position52", type=research32_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Position50", type=research32_Position, multiplicity=Multiplicity(0, 1))
    }
)
kpapers53: BinaryAssociation = BinaryAssociation(
    name="kpapers53",
    ends={
        Property(name="research32_Paper54", type=research32_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Keyword", type=research32_Paper, multiplicity=Multiplicity(0, 9999))
    }
)
allkeywords55: BinaryAssociation = BinaryAssociation(
    name="allkeywords55",
    ends={
        Property(name="research32_Keyword57", type=research32_KnowledgeManager, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_KnowledgeManager56", type=research32_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyword58: BinaryAssociation = BinaryAssociation(
    name="keyword58",
    ends={
        Property(name="research32_Keyword60", type=research32_PaperKeyword, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_PaperKeyword59", type=research32_Keyword, multiplicity=Multiplicity(0, 1))
    }
)
col_paper61: BinaryAssociation = BinaryAssociation(
    name="col_paper61",
    ends={
        Property(name="research32_Paper63", type=research32_Collaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Collaboration62", type=research32_Paper, multiplicity=Multiplicity(0, 1))
    }
)
pubStates66: BinaryAssociation = BinaryAssociation(
    name="pubStates66",
    ends={
        Property(name="research32_State68", type=research32_PublicationStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_PublicationStatus67", type=research32_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
t_actions69: BinaryAssociation = BinaryAssociation(
    name="t_actions69",
    ends={
        Property(name="research32_Action", type=research32_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Transition", type=research32_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source70: BinaryAssociation = BinaryAssociation(
    name="source70",
    ends={
        Property(name="research32_State72", type=research32_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Transition71", type=research32_State, multiplicity=Multiplicity(0, 1))
    }
)
target73: BinaryAssociation = BinaryAssociation(
    name="target73",
    ends={
        Property(name="research32_State75", type=research32_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Transition74", type=research32_State, multiplicity=Multiplicity(0, 1))
    }
)
transitions76: BinaryAssociation = BinaryAssociation(
    name="transitions76",
    ends={
        Property(name="research32_Transition78", type=research32_State, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_State77", type=research32_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
s_actions79: BinaryAssociation = BinaryAssociation(
    name="s_actions79",
    ends={
        Property(name="research32_Action81", type=research32_State, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_State80", type=research32_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next83: BinaryAssociation = BinaryAssociation(
    name="next83",
    ends={
        Property(name="research32_Action84", type=research32_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_Action82", type=research32_Action, multiplicity=Multiplicity(0, 1))
    }
)
machineVariables64: BinaryAssociation = BinaryAssociation(
    name="machineVariables64",
    ends={
        Property(name="research32_StateMachineVariable", type=research32_PublicationStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="research32_PublicationStatus65", type=research32_StateMachineVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_research32_PublicationProcess_Named = Generalization(general=Named, specific=research32_PublicationProcess)
gen_research32_Paper_Named = Generalization(general=Named, specific=research32_Paper)
gen_research32_Paragraph_Counted = Generalization(general=Counted, specific=research32_Paragraph)
gen_research32_Paragraph_Named = Generalization(general=Named, specific=research32_Paragraph)
gen_research32_ReviewNote_Named = Generalization(general=Named, specific=research32_ReviewNote)
gen_research32_Progress_Labelled = Generalization(general=Labelled, specific=research32_Progress)
gen_research32_Write_Labelled = Generalization(general=Labelled, specific=research32_Write)
gen_research32_Review_Labelled = Generalization(general=Labelled, specific=research32_Review)
gen_research32_PublicationStructure_Named = Generalization(general=Named, specific=research32_PublicationStructure)
gen_research32_PublicationSystem_Named = Generalization(general=Named, specific=research32_PublicationSystem)
gen_research32_Position_Named = Generalization(general=Named, specific=research32_Position)
gen_research32_Keyword_Named = Generalization(general=Named, specific=research32_Keyword)
gen_research32_KnowledgeManager_Named = Generalization(general=Named, specific=research32_KnowledgeManager)
gen_research32_Transition_StateMachineObject = Generalization(general=StateMachineObject, specific=research32_Transition)
gen_research32_State_StateMachineObject = Generalization(general=StateMachineObject, specific=research32_State)

# Domain Model
domain_model = DomainModel(
    name="research32",
    types={research32_PublicationProcess, Named, research32_Phase, research32_Researcher, research32_Write, research32_Review, research32_Paper, research32_Skill, research32_Position, research32_Collaboration, research32_Progress, research32_PaperKeyword, research32_State, Counted, research32_ReviewNote, research32_Paragraph, Labelled, research32_PublicationStructure, research32_KnowledgeManager, research32_PublicationStatus, research32_PublicationSystem, research32_Named, research32_Counted, research32_Labelled, research32_Keyword, research32_StateMachineVariable, research32_StateMachineObject, research32_Transition, StateMachineObject, research32_Action, StateType},
    associations={phases0, writes1, reviews2, res_papers4, skills5, res_position7, collaborations9, paragraphs11, progress12, authors13, keywords14, citedBy17, state19, reviews21, process23, paper25, paragraph27, reviewNote30, researchers33, papers35, knowledgeMan38, status40, processView42, structuralView44, positions47, parent51, kpapers53, allkeywords55, keyword58, col_paper61, pubStates66, t_actions69, source70, target73, transitions76, s_actions79, next83, machineVariables64},
    generalizations={gen_research32_PublicationProcess_Named, gen_research32_Paper_Named, gen_research32_Paragraph_Counted, gen_research32_Paragraph_Named, gen_research32_ReviewNote_Named, gen_research32_Progress_Labelled, gen_research32_Write_Labelled, gen_research32_Review_Labelled, gen_research32_PublicationStructure_Named, gen_research32_PublicationSystem_Named, gen_research32_Position_Named, gen_research32_Keyword_Named, gen_research32_KnowledgeManager_Named, gen_research32_Transition_StateMachineObject, gen_research32_State_StateMachineObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
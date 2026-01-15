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
Keys: Enumeration = Enumeration(
    name="Keys",
    literals={
            EnumerationLiteral(name="V"),
			EnumerationLiteral(name="W"),
			EnumerationLiteral(name="X"),
			EnumerationLiteral(name="Y"),
			EnumerationLiteral(name="Z"),
			EnumerationLiteral(name="SPACE"),
			EnumerationLiteral(name="ENTER"),
			EnumerationLiteral(name="UP"),
			EnumerationLiteral(name="DOWN"),
			EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT"),
			EnumerationLiteral(name="A"),
			EnumerationLiteral(name="B"),
			EnumerationLiteral(name="C"),
			EnumerationLiteral(name="D"),
			EnumerationLiteral(name="E"),
			EnumerationLiteral(name="F"),
			EnumerationLiteral(name="G"),
			EnumerationLiteral(name="H"),
			EnumerationLiteral(name="I"),
			EnumerationLiteral(name="J"),
			EnumerationLiteral(name="K"),
			EnumerationLiteral(name="L"),
			EnumerationLiteral(name="M"),
			EnumerationLiteral(name="N"),
			EnumerationLiteral(name="O"),
			EnumerationLiteral(name="P"),
			EnumerationLiteral(name="Q"),
			EnumerationLiteral(name="R"),
			EnumerationLiteral(name="S"),
			EnumerationLiteral(name="T"),
			EnumerationLiteral(name="U")
    }
)

# Classes
klang_EventHandler = Class(name="klang::EventHandler")
klang_Statement = Class(name="klang::Statement")
klang_Event = Class(name="klang::Event", is_abstract=True)
klang_VariableDeclaration = Class(name="klang::VariableDeclaration")
klang_Expression = Class(name="klang::Expression")
klang_SceneActor = Class(name="klang::SceneActor")
klang_Program = Class(name="klang::Program")
klang_SpriteActor = Class(name="klang::SpriteActor")
klang_GameStartEvent = Class(name="klang::GameStartEvent")
GlobalEvent = Class(name="GlobalEvent")
klang_ClickEvent = Class(name="klang::ClickEvent")
ActorEvent = Class(name="ActorEvent")
klang_KeyPressEvent = Class(name="klang::KeyPressEvent")
klang_CollisionEvent = Class(name="klang::CollisionEvent")
klang_AbstractActor = Class(name="klang::AbstractActor", is_abstract=True)
klang_MessageReceivedEvent = Class(name="klang::MessageReceivedEvent")
klang_TreeNode = Class(name="klang::TreeNode", is_abstract=True)
klang_GlobalEvent = Class(name="klang::GlobalEvent", is_abstract=True)
Event = Class(name="Event")
klang_ActorEvent = Class(name="klang::ActorEvent", is_abstract=True)

# klang_EventHandler class attributes and methods

# klang_Statement class attributes and methods

# klang_Event class attributes and methods
klang_Event_m_matchingEvent: Method = Method(name="matchingEvent", parameters={Parameter(name='other')}, type=BooleanType)
klang_Event.methods={klang_Event_m_matchingEvent}

# klang_VariableDeclaration class attributes and methods
klang_VariableDeclaration_name: Property = Property(name="name", type=StringType)
klang_VariableDeclaration.attributes={klang_VariableDeclaration_name}

# klang_Expression class attributes and methods

# klang_SceneActor class attributes and methods

# klang_Program class attributes and methods

# klang_SpriteActor class attributes and methods

# klang_GameStartEvent class attributes and methods

# GlobalEvent class attributes and methods

# klang_ClickEvent class attributes and methods

# ActorEvent class attributes and methods

# klang_KeyPressEvent class attributes and methods
klang_KeyPressEvent_key: Property = Property(name="key", type=StringType)
klang_KeyPressEvent.attributes={klang_KeyPressEvent_key}

# klang_CollisionEvent class attributes and methods

# klang_AbstractActor class attributes and methods
klang_AbstractActor_name: Property = Property(name="name", type=StringType)
klang_AbstractActor_subject: Property = Property(name="subject", type=StringType)
klang_AbstractActor_subjectType: Property = Property(name="subjectType", type=StringType)
klang_AbstractActor_m_isInScope: Method = Method(name="isInScope", parameters={Parameter(name='variableName')}, type=BooleanType)
klang_AbstractActor_m_getVariableDeclaration: Method = Method(name="getVariableDeclaration", parameters={Parameter(name='variableName')}, type=StringType)
klang_AbstractActor_m_isInLocalScope: Method = Method(name="isInLocalScope", parameters={Parameter(name='variableName')}, type=BooleanType)
klang_AbstractActor_m_isInParentScope: Method = Method(name="isInParentScope", parameters={Parameter(name='variableName')}, type=BooleanType)
klang_AbstractActor_m_getVariableDeclarations: Method = Method(name="getVariableDeclarations", parameters={Parameter(name='variableName')})
klang_AbstractActor.attributes={klang_AbstractActor_subject, klang_AbstractActor_subjectType, klang_AbstractActor_name}
klang_AbstractActor.methods={klang_AbstractActor_m_getVariableDeclarations, klang_AbstractActor_m_isInScope, klang_AbstractActor_m_getVariableDeclaration, klang_AbstractActor_m_isInLocalScope, klang_AbstractActor_m_isInParentScope}

# klang_MessageReceivedEvent class attributes and methods
klang_MessageReceivedEvent_name: Property = Property(name="name", type=StringType)
klang_MessageReceivedEvent.attributes={klang_MessageReceivedEvent_name}

# klang_TreeNode class attributes and methods

# klang_GlobalEvent class attributes and methods

# Event class attributes and methods

# klang_ActorEvent class attributes and methods

# Relationships
statements3: BinaryAssociation = BinaryAssociation(
    name="statements3",
    ends={
        Property(name="klang_Statement", type=klang_EventHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="klang_EventHandler", type=klang_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referenceEvent4: BinaryAssociation = BinaryAssociation(
    name="referenceEvent4",
    ends={
        Property(name="klang_Event", type=klang_EventHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="klang_EventHandler5", type=klang_Event, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression6: BinaryAssociation = BinaryAssociation(
    name="expression6",
    ends={
        Property(name="klang_Expression", type=klang_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="klang_VariableDeclaration", type=klang_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
program0: BinaryAssociation = BinaryAssociation(
    name="program0",
    ends={
        Property(name="Program", type=klang_SceneActor, multiplicity=Multiplicity(1, 1)),
        Property(name="sceneActor", type=klang_Program, multiplicity=Multiplicity(0, 1))
    }
)
program1: BinaryAssociation = BinaryAssociation(
    name="program1",
    ends={
        Property(name="Program2", type=klang_SpriteActor, multiplicity=Multiplicity(1, 1)),
        Property(name="spriteActors", type=klang_Program, multiplicity=Multiplicity(0, 1))
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="klang_SpriteActor", type=klang_CollisionEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="klang_CollisionEvent", type=klang_SpriteActor, multiplicity=Multiplicity(0, 1))
    }
)
sceneActor11: BinaryAssociation = BinaryAssociation(
    name="sceneActor11",
    ends={
        Property(name="SceneActor", type=klang_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="program", type=klang_SceneActor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventHandlers7: BinaryAssociation = BinaryAssociation(
    name="eventHandlers7",
    ends={
        Property(name="EventHandler", type=klang_AbstractActor, multiplicity=Multiplicity(1, 1)),
        Property(name="actor", type=klang_EventHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localVariables8: BinaryAssociation = BinaryAssociation(
    name="localVariables8",
    ends={
        Property(name="VariableDeclaration", type=klang_AbstractActor, multiplicity=Multiplicity(1, 1)),
        Property(name="actor9", type=klang_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
spriteActors12: BinaryAssociation = BinaryAssociation(
    name="spriteActors12",
    ends={
        Property(name="SpriteActor", type=klang_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="program13", type=klang_SpriteActor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_klang_GameStartEvent_GlobalEvent = Generalization(general=GlobalEvent, specific=klang_GameStartEvent)
gen_klang_ClickEvent_ActorEvent = Generalization(general=ActorEvent, specific=klang_ClickEvent)
gen_klang_KeyPressEvent_GlobalEvent = Generalization(general=GlobalEvent, specific=klang_KeyPressEvent)
gen_klang_CollisionEvent_ActorEvent = Generalization(general=ActorEvent, specific=klang_CollisionEvent)
gen_klang_MessageReceivedEvent_GlobalEvent = Generalization(general=GlobalEvent, specific=klang_MessageReceivedEvent)
gen_klang_GlobalEvent_Event = Generalization(general=Event, specific=klang_GlobalEvent)
gen_klang_ActorEvent_Event = Generalization(general=Event, specific=klang_ActorEvent)

# Domain Model
domain_model = DomainModel(
    name="klang",
    types={klang_EventHandler, klang_Statement, klang_Event, klang_VariableDeclaration, klang_Expression, klang_SceneActor, klang_Program, klang_SpriteActor, klang_GameStartEvent, GlobalEvent, klang_ClickEvent, ActorEvent, klang_KeyPressEvent, klang_CollisionEvent, klang_AbstractActor, klang_MessageReceivedEvent, klang_TreeNode, klang_GlobalEvent, Event, klang_ActorEvent, Keys},
    associations={statements3, referenceEvent4, expression6, program0, program1, target10, sceneActor11, eventHandlers7, localVariables8, spriteActors12},
    generalizations={gen_klang_GameStartEvent_GlobalEvent, gen_klang_ClickEvent_ActorEvent, gen_klang_KeyPressEvent_GlobalEvent, gen_klang_CollisionEvent_ActorEvent, gen_klang_MessageReceivedEvent_GlobalEvent, gen_klang_GlobalEvent_Event, gen_klang_ActorEvent_Event},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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

# Classes
UMLMetamodelFragment_Stereotype = Class(name="UMLMetamodelFragment_Stereotype")
UMLMetamodelFragment_StateMachine = Class(name="UMLMetamodelFragment_StateMachine")
State = Class(name="State")
UMLMetamodelFragment_State = Class(name="UMLMetamodelFragment_State")
StateVertex = Class(name="StateVertex")
UMLMetamodelFragment_Class = Class(name="UMLMetamodelFragment_Class")
Generalization_ = Class(name="Generalization_")
Dependency = Class(name="Dependency")
UMLMetamodelFragment_Generalization = Class(name="UMLMetamodelFragment_Generalization_")
UMLMetamodelFragment_Dependency = Class(name="UMLMetamodelFragment_Dependency")
StateMachine = Class(name="StateMachine")
Class_ = Class(name="Class")
Stereotype = Class(name="Stereotype")
Transition = Class(name="Transition")
UMLMetamodelFragment_CompositeState = Class(name="UMLMetamodelFragment_CompositeState")
UMLMetamodelFragment_SimpleState = Class(name="UMLMetamodelFragment_SimpleState")
UMLMetamodelFragment_FinalState = Class(name="UMLMetamodelFragment_FinalState")
UMLMetamodelFragment_StateVertex = Class(name="UMLMetamodelFragment_StateVertex")
CompositeState = Class(name="CompositeState")
UMLMetamodelFragment_PseudoState = Class(name="UMLMetamodelFragment_PseudoState")
UMLMetamodelFragment_Transition = Class(name="UMLMetamodelFragment_Transition")
Event = Class(name="Event")
UMLMetamodelFragment_Event = Class(name="UMLMetamodelFragment_Event")

# UMLMetamodelFragment_Stereotype class attributes and methods
UMLMetamodelFragment_Stereotype_baseClass: Property = Property(name="baseClass", type=StringType)
UMLMetamodelFragment_Stereotype.attributes={UMLMetamodelFragment_Stereotype_baseClass}

# UMLMetamodelFragment_StateMachine class attributes and methods

# State class attributes and methods

# UMLMetamodelFragment_State class attributes and methods

# StateVertex class attributes and methods

# UMLMetamodelFragment_Class class attributes and methods

# Generalization_ class attributes and methods

# Dependency class attributes and methods

# UMLMetamodelFragment_Generalization class attributes and methods

# UMLMetamodelFragment_Dependency class attributes and methods

# StateMachine class attributes and methods

# Class class attributes and methods

# Stereotype class attributes and methods

# Transition class attributes and methods

# UMLMetamodelFragment_CompositeState class attributes and methods

# UMLMetamodelFragment_SimpleState class attributes and methods

# UMLMetamodelFragment_FinalState class attributes and methods

# UMLMetamodelFragment_StateVertex class attributes and methods

# CompositeState class attributes and methods

# UMLMetamodelFragment_PseudoState class attributes and methods

# UMLMetamodelFragment_Transition class attributes and methods

# Event class attributes and methods

# UMLMetamodelFragment_Event class attributes and methods

# Relationships
stereotype7: BinaryAssociation = BinaryAssociation(
    name="stereotype7",
    ends={
        Property(name="Stereotype", type=UMLMetamodelFragment_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedElement", type=Stereotype, multiplicity=Multiplicity(1, 1))
    }
)
extendedElement8: BinaryAssociation = BinaryAssociation(
    name="extendedElement8",
    ends={
        Property(name="Dependency9", type=UMLMetamodelFragment_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotype", type=Dependency, multiplicity=Multiplicity(1, 1))
    }
)
context10: BinaryAssociation = BinaryAssociation(
    name="context10",
    ends={
        Property(name="Class11", type=UMLMetamodelFragment_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLMetamodelFragment_StateMachine", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
top12: BinaryAssociation = BinaryAssociation(
    name="top12",
    ends={
        Property(name="State", type=UMLMetamodelFragment_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=State, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parent0: BinaryAssociation = BinaryAssociation(
    name="parent0",
    ends={
        Property(name="Generalization_", type=UMLMetamodelFragment_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLMetamodelFragment_Class", type=Generalization_, multiplicity=Multiplicity(1, 1))
    }
)
child1: BinaryAssociation = BinaryAssociation(
    name="child1",
    ends={
        Property(name="Generalization3", type=UMLMetamodelFragment_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLMetamodelFragment_Class2", type=Generalization_, multiplicity=Multiplicity(1, 1))
    }
)
dependency4: BinaryAssociation = BinaryAssociation(
    name="dependency4",
    ends={
        Property(name="Dependency", type=UMLMetamodelFragment_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="client", type=Dependency, multiplicity=Multiplicity(1, 1))
    }
)
supplier5: BinaryAssociation = BinaryAssociation(
    name="supplier5",
    ends={
        Property(name="StateMachine", type=UMLMetamodelFragment_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLMetamodelFragment_Dependency", type=StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
client6: BinaryAssociation = BinaryAssociation(
    name="client6",
    ends={
        Property(name="Class", type=UMLMetamodelFragment_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="dependency", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
stateMachine13: BinaryAssociation = BinaryAssociation(
    name="stateMachine13",
    ends={
        Property(name="StateMachine14", type=UMLMetamodelFragment_State, multiplicity=Multiplicity(1, 1)),
        Property(name="top", type=StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
internal15: BinaryAssociation = BinaryAssociation(
    name="internal15",
    ends={
        Property(name="Transition", type=UMLMetamodelFragment_State, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLMetamodelFragment_State", type=Transition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subvertex16: BinaryAssociation = BinaryAssociation(
    name="subvertex16",
    ends={
        Property(name="StateVertex", type=UMLMetamodelFragment_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeState", type=StateVertex, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
compositeState17: BinaryAssociation = BinaryAssociation(
    name="compositeState17",
    ends={
        Property(name="CompositeState", type=UMLMetamodelFragment_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
trigger18: BinaryAssociation = BinaryAssociation(
    name="trigger18",
    ends={
        Property(name="Event", type=UMLMetamodelFragment_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLMetamodelFragment_Transition", type=Event, multiplicity=Multiplicity(0, 1))
    }
)
source19: BinaryAssociation = BinaryAssociation(
    name="source19",
    ends={
        Property(name="StateVertex21", type=UMLMetamodelFragment_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLMetamodelFragment_Transition20", type=StateVertex, multiplicity=Multiplicity(1, 1))
    }
)
target22: BinaryAssociation = BinaryAssociation(
    name="target22",
    ends={
        Property(name="StateVertex24", type=UMLMetamodelFragment_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="UMLMetamodelFragment_Transition23", type=StateVertex, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_UMLMetamodelFragment_State_StateVertex = Generalization(general=StateVertex, specific=UMLMetamodelFragment_State)
gen_UMLMetamodelFragment_CompositeState_State = Generalization(general=State, specific=UMLMetamodelFragment_CompositeState)
gen_UMLMetamodelFragment_SimpleState_State = Generalization(general=State, specific=UMLMetamodelFragment_SimpleState)
gen_UMLMetamodelFragment_FinalState_State = Generalization(general=State, specific=UMLMetamodelFragment_FinalState)
gen_UMLMetamodelFragment_PseudoState_StateVertex = Generalization(general=StateVertex, specific=UMLMetamodelFragment_PseudoState)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={UMLMetamodelFragment_Stereotype, UMLMetamodelFragment_StateMachine, State, UMLMetamodelFragment_State, StateVertex, UMLMetamodelFragment_Class, Generalization_, Dependency, UMLMetamodelFragment_Generalization, UMLMetamodelFragment_Dependency, StateMachine, Class_, Stereotype, Transition, UMLMetamodelFragment_CompositeState, UMLMetamodelFragment_SimpleState, UMLMetamodelFragment_FinalState, UMLMetamodelFragment_StateVertex, CompositeState, UMLMetamodelFragment_PseudoState, UMLMetamodelFragment_Transition, Event, UMLMetamodelFragment_Event},
    associations={stereotype7, extendedElement8, context10, top12, parent0, child1, dependency4, supplier5, client6, stateMachine13, internal15, subvertex16, compositeState17, trigger18, source19, target22},
    generalizations={gen_UMLMetamodelFragment_State_StateVertex, gen_UMLMetamodelFragment_CompositeState_State, gen_UMLMetamodelFragment_SimpleState_State, gen_UMLMetamodelFragment_FinalState_State, gen_UMLMetamodelFragment_PseudoState_StateVertex},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
PseudostateKind: Enumeration = Enumeration(
    name="PseudostateKind",
    literals={
            EnumerationLiteral(name="initial")
    }
)

# Classes
fsmcore_StateMachine = Class(name="fsmcore::StateMachine")
NamedElement = Class(name="NamedElement")
fsmcore_Transition = Class(name="fsmcore::Transition")
fsmcore_Region = Class(name="fsmcore::Region")
fsmcore_AbstractState = Class(name="fsmcore::AbstractState", is_abstract=True)
fsmcore_Trigger = Class(name="fsmcore::Trigger")
fsmcore_Constraint = Class(name="fsmcore::Constraint")
fsmcore_State = Class(name="fsmcore::State")
AbstractState = Class(name="AbstractState")
fsmcore_Program = Class(name="fsmcore::Program")
fsmcore_Statement = Class(name="fsmcore::Statement", is_abstract=True)
fsmcore_Conditional = Class(name="fsmcore::Conditional")
Statement = Class(name="Statement")
fsmcore_Loop = Class(name="fsmcore::Loop")
fsmcore_NamedElement = Class(name="fsmcore::NamedElement")
fsmcore_FinalState = Class(name="fsmcore::FinalState")
State = Class(name="State")
fsmcore_VarDecl = Class(name="fsmcore::VarDecl")
fsmcore_Pseudostate = Class(name="fsmcore::Pseudostate")

# fsmcore_StateMachine class attributes and methods

# NamedElement class attributes and methods

# fsmcore_Transition class attributes and methods

# fsmcore_Region class attributes and methods

# fsmcore_AbstractState class attributes and methods

# fsmcore_Trigger class attributes and methods
fsmcore_Trigger_expression: Property = Property(name="expression", type=BooleanType)
fsmcore_Trigger.attributes={fsmcore_Trigger_expression}

# fsmcore_Constraint class attributes and methods
fsmcore_Constraint_m_evalConstraint: Method = Method(name="evalConstraint", parameters={Parameter(name='context')})
fsmcore_Constraint.methods={fsmcore_Constraint_m_evalConstraint}

# fsmcore_State class attributes and methods

# AbstractState class attributes and methods

# fsmcore_Program class attributes and methods
fsmcore_Program_m_eval: Method = Method(name="eval", parameters={Parameter(name='context')})
fsmcore_Program.methods={fsmcore_Program_m_eval}

# fsmcore_Statement class attributes and methods
fsmcore_Statement_m_eval: Method = Method(name="eval", parameters={Parameter(name='context')})
fsmcore_Statement.methods={fsmcore_Statement_m_eval}

# fsmcore_Conditional class attributes and methods

# Statement class attributes and methods

# fsmcore_Loop class attributes and methods

# fsmcore_NamedElement class attributes and methods
fsmcore_NamedElement_name: Property = Property(name="name", type=StringType)
fsmcore_NamedElement.attributes={fsmcore_NamedElement_name}

# fsmcore_FinalState class attributes and methods

# State class attributes and methods

# fsmcore_VarDecl class attributes and methods

# fsmcore_Pseudostate class attributes and methods
fsmcore_Pseudostate_kind: Property = Property(name="kind", type=StringType)
fsmcore_Pseudostate.attributes={fsmcore_Pseudostate_kind}

# Relationships
transitions3: BinaryAssociation = BinaryAssociation(
    name="transitions3",
    ends={
        Property(name="fsmcore_Transition", type=fsmcore_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_Region4", type=fsmcore_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming5: BinaryAssociation = BinaryAssociation(
    name="incoming5",
    ends={
        Property(name="7", type=fsmcore_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=fsmcore_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing8: BinaryAssociation = BinaryAssociation(
    name="outgoing8",
    ends={
        Property(name="10", type=fsmcore_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=fsmcore_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
ownerRegion11: BinaryAssociation = BinaryAssociation(
    name="ownerRegion11",
    ends={
        Property(name="13", type=fsmcore_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=fsmcore_Region, multiplicity=Multiplicity(1, 1))
    }
)
regions0: BinaryAssociation = BinaryAssociation(
    name="regions0",
    ends={
        Property(name="fsmcore_Region", type=fsmcore_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_StateMachine", type=fsmcore_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subvertex1: BinaryAssociation = BinaryAssociation(
    name="subvertex1",
    ends={
        Property(name="2", type=fsmcore_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=fsmcore_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger21: BinaryAssociation = BinaryAssociation(
    name="trigger21",
    ends={
        Property(name="fsmcore_Trigger", type=fsmcore_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_Transition22", type=fsmcore_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target23: BinaryAssociation = BinaryAssociation(
    name="target23",
    ends={
        Property(name="25", type=fsmcore_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="24", type=fsmcore_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
source26: BinaryAssociation = BinaryAssociation(
    name="source26",
    ends={
        Property(name="28", type=fsmcore_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="27", type=fsmcore_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
guard29: BinaryAssociation = BinaryAssociation(
    name="guard29",
    ends={
        Property(name="fsmcore_Constraint", type=fsmcore_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_Transition30", type=fsmcore_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doActivity14: BinaryAssociation = BinaryAssociation(
    name="doActivity14",
    ends={
        Property(name="fsmcore_Program", type=fsmcore_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_State", type=fsmcore_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry15: BinaryAssociation = BinaryAssociation(
    name="entry15",
    ends={
        Property(name="fsmcore_Program17", type=fsmcore_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_State16", type=fsmcore_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit18: BinaryAssociation = BinaryAssociation(
    name="exit18",
    ends={
        Property(name="fsmcore_Program20", type=fsmcore_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_State19", type=fsmcore_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements31: BinaryAssociation = BinaryAssociation(
    name="statements31",
    ends={
        Property(name="fsmcore_Statement", type=fsmcore_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_Program32", type=fsmcore_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_fsmcore_StateMachine_NamedElement = Generalization(general=NamedElement, specific=fsmcore_StateMachine)
gen_fsmcore_AbstractState_NamedElement = Generalization(general=NamedElement, specific=fsmcore_AbstractState)
gen_fsmcore_Region_NamedElement = Generalization(general=NamedElement, specific=fsmcore_Region)
gen_fsmcore_Transition_NamedElement = Generalization(general=NamedElement, specific=fsmcore_Transition)
gen_fsmcore_State_AbstractState = Generalization(general=AbstractState, specific=fsmcore_State)
gen_fsmcore_Conditional_Statement = Generalization(general=Statement, specific=fsmcore_Conditional)
gen_fsmcore_Loop_Statement = Generalization(general=Statement, specific=fsmcore_Loop)
gen_fsmcore_FinalState_State = Generalization(general=State, specific=fsmcore_FinalState)
gen_fsmcore_VarDecl_Statement = Generalization(general=Statement, specific=fsmcore_VarDecl)
gen_fsmcore_Pseudostate_AbstractState = Generalization(general=AbstractState, specific=fsmcore_Pseudostate)

# Domain Model
domain_model = DomainModel(
    name="fsmcore",
    types={fsmcore_StateMachine, NamedElement, fsmcore_Transition, fsmcore_Region, fsmcore_AbstractState, fsmcore_Trigger, fsmcore_Constraint, fsmcore_State, AbstractState, fsmcore_Program, fsmcore_Statement, fsmcore_Conditional, Statement, fsmcore_Loop, fsmcore_NamedElement, fsmcore_FinalState, State, fsmcore_VarDecl, fsmcore_Pseudostate, PseudostateKind},
    associations={transitions3, incoming5, outgoing8, ownerRegion11, regions0, subvertex1, trigger21, target23, source26, guard29, doActivity14, entry15, exit18, statements31},
    generalizations={gen_fsmcore_StateMachine_NamedElement, gen_fsmcore_AbstractState_NamedElement, gen_fsmcore_Region_NamedElement, gen_fsmcore_Transition_NamedElement, gen_fsmcore_State_AbstractState, gen_fsmcore_Conditional_Statement, gen_fsmcore_Loop_Statement, gen_fsmcore_FinalState_State, gen_fsmcore_VarDecl_Statement, gen_fsmcore_Pseudostate_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
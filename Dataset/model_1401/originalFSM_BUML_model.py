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
fsmcore_StateMachine = Class(name="fsmcore_StateMachine")
NamedElement = Class(name="NamedElement")
fsmcore_Region = Class(name="fsmcore_Region")
fsmcore_AbstractState = Class(name="fsmcore_AbstractState", is_abstract=True)
fsmcore_Transition = Class(name="fsmcore_Transition")
fsmcore_State = Class(name="fsmcore_State")
AbstractState = Class(name="AbstractState")
fsmcore_Program = Class(name="fsmcore_Program")
fsmcore_Trigger = Class(name="fsmcore_Trigger")
fsmcore_Constraint = Class(name="fsmcore_Constraint")
fsmcore_Statement = Class(name="fsmcore_Statement", is_abstract=True)
fsmcore_Conditional = Class(name="fsmcore_Conditional")
Statement = Class(name="Statement")
fsmcore_Loop = Class(name="fsmcore_Loop")
fsmcore_VarDecl = Class(name="fsmcore_VarDecl")
fsmcore_Pseudostate = Class(name="fsmcore_Pseudostate")
fsmcore_FinalState = Class(name="fsmcore_FinalState")
State = Class(name="State")
fsmcore_NamedElement = Class(name="fsmcore_NamedElement")

# fsmcore_StateMachine class attributes and methods

# NamedElement class attributes and methods

# fsmcore_Region class attributes and methods

# fsmcore_AbstractState class attributes and methods

# fsmcore_Transition class attributes and methods

# fsmcore_State class attributes and methods

# AbstractState class attributes and methods

# fsmcore_Program class attributes and methods
fsmcore_Program_m_eval: Method = Method(name="eval", parameters={Parameter(name='fsmcore_context', type=StringType)})
fsmcore_Program.methods={fsmcore_Program_m_eval}

# fsmcore_Trigger class attributes and methods
fsmcore_Trigger_expression: Property = Property(name="expression", type=BooleanType)
fsmcore_Trigger.attributes={fsmcore_Trigger_expression}

# fsmcore_Constraint class attributes and methods
fsmcore_Constraint_m_evalConstraint: Method = Method(name="evalConstraint", parameters={Parameter(name='fsmcore_context', type=StringType)})
fsmcore_Constraint.methods={fsmcore_Constraint_m_evalConstraint}

# fsmcore_Statement class attributes and methods
fsmcore_Statement_m_eval: Method = Method(name="eval", parameters={Parameter(name='fsmcore_context', type=StringType)})
fsmcore_Statement.methods={fsmcore_Statement_m_eval}

# fsmcore_Conditional class attributes and methods

# Statement class attributes and methods

# fsmcore_Loop class attributes and methods

# fsmcore_VarDecl class attributes and methods

# fsmcore_Pseudostate class attributes and methods
fsmcore_Pseudostate_kind: Property = Property(name="kind", type=StringType)
fsmcore_Pseudostate.attributes={fsmcore_Pseudostate_kind}

# fsmcore_FinalState class attributes and methods

# State class attributes and methods

# fsmcore_NamedElement class attributes and methods
fsmcore_NamedElement_name: Property = Property(name="name", type=StringType)
fsmcore_NamedElement.attributes={fsmcore_NamedElement_name}

# Relationships
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
        Property(name="AbstractState", type=fsmcore_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerRegion", type=fsmcore_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions2: BinaryAssociation = BinaryAssociation(
    name="transitions2",
    ends={
        Property(name="fsmcore_Transition", type=fsmcore_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_Region3", type=fsmcore_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming4: BinaryAssociation = BinaryAssociation(
    name="incoming4",
    ends={
        Property(name="Transition", type=fsmcore_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsmcore_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="Transition6", type=fsmcore_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsmcore_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
ownerRegion7: BinaryAssociation = BinaryAssociation(
    name="ownerRegion7",
    ends={
        Property(name="Region", type=fsmcore_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=fsmcore_Region, multiplicity=Multiplicity(1, 1))
    }
)
doActivity8: BinaryAssociation = BinaryAssociation(
    name="doActivity8",
    ends={
        Property(name="fsmcore_Program", type=fsmcore_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_State", type=fsmcore_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry9: BinaryAssociation = BinaryAssociation(
    name="entry9",
    ends={
        Property(name="fsmcore_Program11", type=fsmcore_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_State10", type=fsmcore_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit12: BinaryAssociation = BinaryAssociation(
    name="exit12",
    ends={
        Property(name="fsmcore_Program14", type=fsmcore_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_State13", type=fsmcore_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger15: BinaryAssociation = BinaryAssociation(
    name="trigger15",
    ends={
        Property(name="fsmcore_Trigger", type=fsmcore_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_Transition16", type=fsmcore_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="AbstractState18", type=fsmcore_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=fsmcore_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
source19: BinaryAssociation = BinaryAssociation(
    name="source19",
    ends={
        Property(name="AbstractState20", type=fsmcore_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=fsmcore_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
statements23: BinaryAssociation = BinaryAssociation(
    name="statements23",
    ends={
        Property(name="fsmcore_Statement", type=fsmcore_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_Program24", type=fsmcore_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard21: BinaryAssociation = BinaryAssociation(
    name="guard21",
    ends={
        Property(name="fsmcore_Constraint", type=fsmcore_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_Transition22", type=fsmcore_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_fsmcore_StateMachine_NamedElement = Generalization(general=NamedElement, specific=fsmcore_StateMachine)
gen_fsmcore_Region_NamedElement = Generalization(general=NamedElement, specific=fsmcore_Region)
gen_fsmcore_AbstractState_NamedElement = Generalization(general=NamedElement, specific=fsmcore_AbstractState)
gen_fsmcore_State_AbstractState = Generalization(general=AbstractState, specific=fsmcore_State)
gen_fsmcore_Transition_NamedElement = Generalization(general=NamedElement, specific=fsmcore_Transition)
gen_fsmcore_Conditional_Statement = Generalization(general=Statement, specific=fsmcore_Conditional)
gen_fsmcore_Loop_Statement = Generalization(general=Statement, specific=fsmcore_Loop)
gen_fsmcore_VarDecl_Statement = Generalization(general=Statement, specific=fsmcore_VarDecl)
gen_fsmcore_Pseudostate_AbstractState = Generalization(general=AbstractState, specific=fsmcore_Pseudostate)
gen_fsmcore_FinalState_State = Generalization(general=State, specific=fsmcore_FinalState)

# Domain Model
domain_model = DomainModel(
    name="fsmcore",
    types={fsmcore_StateMachine, NamedElement, fsmcore_Region, fsmcore_AbstractState, fsmcore_Transition, fsmcore_State, AbstractState, fsmcore_Program, fsmcore_Trigger, fsmcore_Constraint, fsmcore_Statement, fsmcore_Conditional, Statement, fsmcore_Loop, fsmcore_VarDecl, fsmcore_Pseudostate, fsmcore_FinalState, State, fsmcore_NamedElement, PseudostateKind},
    associations={regions0, subvertex1, transitions2, incoming4, outgoing5, ownerRegion7, doActivity8, entry9, exit12, trigger15, target17, source19, statements23, guard21},
    generalizations={gen_fsmcore_StateMachine_NamedElement, gen_fsmcore_Region_NamedElement, gen_fsmcore_AbstractState_NamedElement, gen_fsmcore_State_AbstractState, gen_fsmcore_Transition_NamedElement, gen_fsmcore_Conditional_Statement, gen_fsmcore_Loop_Statement, gen_fsmcore_VarDecl_Statement, gen_fsmcore_Pseudostate_AbstractState, gen_fsmcore_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
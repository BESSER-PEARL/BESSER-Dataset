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
cpsml_ODE = Class(name="cpsml_ODE")
cpsml_System = Class(name="cpsml_System")
cpsml_Variable = Class(name="cpsml_Variable")
cpsml_State = Class(name="cpsml_State")
cpsml_Transition = Class(name="cpsml_Transition", is_abstract=True)
cpsml_ProbTransition = Class(name="cpsml_ProbTransition")
cpsml_ComTransition = Class(name="cpsml_ComTransition")
cpsml_Interval = Class(name="cpsml_Interval")
cpsml_IndeVariable = Class(name="cpsml_IndeVariable")
Transition = Class(name="Transition")
cpsml_Function = Class(name="cpsml_Function")
cpsml_Condition = Class(name="cpsml_Condition")
cpsml_DeVariable = Class(name="cpsml_DeVariable")
cpsml_Fright = Class(name="cpsml_Fright")

# cpsml_ODE class attributes and methods
cpsml_ODE_name: Property = Property(name="name", type=StringType)
cpsml_ODE.attributes={cpsml_ODE_name}

# cpsml_System class attributes and methods
cpsml_System_name: Property = Property(name="name", type=StringType)
cpsml_System_ran: Property = Property(name="ran", type=StringType)
cpsml_System_sub: Property = Property(name="sub", type=IntegerType)
cpsml_System_y0label: Property = Property(name="y0label", type=IntegerType)
cpsml_System_m_main: Method = Method(name="main", parameters={})
cpsml_System_m_dojump: Method = Method(name="dojump", parameters={})
cpsml_System_m_callscilab: Method = Method(name="callscilab", parameters={})
cpsml_System_m_RealizeInitializeModel: Method = Method(name="RealizeInitializeModel", parameters={Parameter(name='cpsml_arguments', type=StringType)})
cpsml_System.attributes={cpsml_System_y0label, cpsml_System_sub, cpsml_System_ran, cpsml_System_name}
cpsml_System.methods={cpsml_System_m_callscilab, cpsml_System_m_main, cpsml_System_m_dojump, cpsml_System_m_RealizeInitializeModel}

# cpsml_Variable class attributes and methods
cpsml_Variable_value: Property = Property(name="value", type=FloatType)
cpsml_Variable_Globalnv: Property = Property(name="Globalnv", type=FloatType)
cpsml_Variable.attributes={cpsml_Variable_Globalnv, cpsml_Variable_value}

# cpsml_State class attributes and methods
cpsml_State_name: Property = Property(name="name", type=BooleanType)
cpsml_State.attributes={cpsml_State_name}

# cpsml_Transition class attributes and methods
cpsml_Transition_name: Property = Property(name="name", type=StringType)
cpsml_Transition_event: Property = Property(name="event", type=StringType)
cpsml_Transition_guard: Property = Property(name="guard", type=StringType)
cpsml_Transition_action: Property = Property(name="action", type=StringType)
cpsml_Transition_m_holds: Method = Method(name="holds", parameters={})
cpsml_Transition.attributes={cpsml_Transition_name, cpsml_Transition_guard, cpsml_Transition_event, cpsml_Transition_action}
cpsml_Transition.methods={cpsml_Transition_m_holds}

# cpsml_ProbTransition class attributes and methods
cpsml_ProbTransition_probability: Property = Property(name="probability", type=FloatType)
cpsml_ProbTransition.attributes={cpsml_ProbTransition_probability}

# cpsml_ComTransition class attributes and methods

# cpsml_Interval class attributes and methods
cpsml_Interval_name: Property = Property(name="name", type=StringType)
cpsml_Interval_left: Property = Property(name="left", type=FloatType)
cpsml_Interval_right: Property = Property(name="right", type=FloatType)
cpsml_Interval_subinterval: Property = Property(name="subinterval", type=FloatType)
cpsml_Interval.attributes={cpsml_Interval_right, cpsml_Interval_subinterval, cpsml_Interval_name, cpsml_Interval_left}

# cpsml_IndeVariable class attributes and methods
cpsml_IndeVariable_name: Property = Property(name="name", type=StringType)
cpsml_IndeVariable.attributes={cpsml_IndeVariable_name}

# Transition class attributes and methods

# cpsml_Function class attributes and methods
cpsml_Function_name: Property = Property(name="name", type=StringType)
cpsml_Function.attributes={cpsml_Function_name}

# cpsml_Condition class attributes and methods
cpsml_Condition_name: Property = Property(name="name", type=StringType)
cpsml_Condition.attributes={cpsml_Condition_name}

# cpsml_DeVariable class attributes and methods
cpsml_DeVariable_name: Property = Property(name="name", type=StringType)
cpsml_DeVariable.attributes={cpsml_DeVariable_name}

# cpsml_Fright class attributes and methods
cpsml_Fright_name: Property = Property(name="name", type=StringType)
cpsml_Fright.attributes={cpsml_Fright_name}

# Relationships
initialState8: BinaryAssociation = BinaryAssociation(
    name="initialState8",
    ends={
        Property(name="cpsml_State10", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System9", type=cpsml_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedodes11: BinaryAssociation = BinaryAssociation(
    name="ownedodes11",
    ends={
        Property(name="cpsml_ODE", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System12", type=cpsml_ODE, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currentState13: BinaryAssociation = BinaryAssociation(
    name="currentState13",
    ends={
        Property(name="cpsml_State15", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System14", type=cpsml_State, multiplicity=Multiplicity(0, 1))
    }
)
ownedvariables0: BinaryAssociation = BinaryAssociation(
    name="ownedvariables0",
    ends={
        Property(name="cpsml_Variable", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System", type=cpsml_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedvariable1: BinaryAssociation = BinaryAssociation(
    name="relatedvariable1",
    ends={
        Property(name="cpsml_Variable3", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System2", type=cpsml_Variable, multiplicity=Multiplicity(1, 1))
    }
)
ownedStates4: BinaryAssociation = BinaryAssociation(
    name="ownedStates4",
    ends={
        Property(name="cpsml_State", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System5", type=cpsml_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTransitions6: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions6",
    ends={
        Property(name="cpsml_Transition", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System7", type=cpsml_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subtransitions36: BinaryAssociation = BinaryAssociation(
    name="subtransitions36",
    ends={
        Property(name="cpsml_Transition38", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State37", type=cpsml_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subodes39: BinaryAssociation = BinaryAssociation(
    name="subodes39",
    ends={
        Property(name="cpsml_ODE41", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State40", type=cpsml_ODE, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subrelatedvariables42: BinaryAssociation = BinaryAssociation(
    name="subrelatedvariables42",
    ends={
        Property(name="cpsml_Variable44", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State43", type=cpsml_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fatherState16: BinaryAssociation = BinaryAssociation(
    name="fatherState16",
    ends={
        Property(name="cpsml_State18", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System17", type=cpsml_State, multiplicity=Multiplicity(0, 1))
    }
)
ptok19: BinaryAssociation = BinaryAssociation(
    name="ptok19",
    ends={
        Property(name="cpsml_ProbTransition", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System20", type=cpsml_ProbTransition, multiplicity=Multiplicity(0, 1))
    }
)
slaveode21: BinaryAssociation = BinaryAssociation(
    name="slaveode21",
    ends={
        Property(name="cpsml_ODE23", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State22", type=cpsml_ODE, multiplicity=Multiplicity(1, 1))
    }
)
outgoingComTransitions24: BinaryAssociation = BinaryAssociation(
    name="outgoingComTransitions24",
    ends={
        Property(name="ComTransition", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="csrc", type=cpsml_ComTransition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingComTransitions25: BinaryAssociation = BinaryAssociation(
    name="incomingComTransitions25",
    ends={
        Property(name="ComTransition26", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ctgt", type=cpsml_ComTransition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingProbTransitions27: BinaryAssociation = BinaryAssociation(
    name="outgoingProbTransitions27",
    ends={
        Property(name="ProbTransition", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="psrc", type=cpsml_ProbTransition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingProbTransitions28: BinaryAssociation = BinaryAssociation(
    name="incomingProbTransitions28",
    ends={
        Property(name="ProbTransition29", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ptgt", type=cpsml_ProbTransition, multiplicity=Multiplicity(0, 9999))
    }
)
subStates31: BinaryAssociation = BinaryAssociation(
    name="subStates31",
    ends={
        Property(name="cpsml_State32", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State30", type=cpsml_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialsubstate34: BinaryAssociation = BinaryAssociation(
    name="initialsubstate34",
    ends={
        Property(name="cpsml_State35", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State33", type=cpsml_State, multiplicity=Multiplicity(1, 1))
    }
)
interval62: BinaryAssociation = BinaryAssociation(
    name="interval62",
    ends={
        Property(name="cpsml_Interval", type=cpsml_ODE, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_ODE63", type=cpsml_Interval, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
indevariable64: BinaryAssociation = BinaryAssociation(
    name="indevariable64",
    ends={
        Property(name="cpsml_IndeVariable", type=cpsml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_Function65", type=cpsml_IndeVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subrelatedvariable45: BinaryAssociation = BinaryAssociation(
    name="subrelatedvariable45",
    ends={
        Property(name="cpsml_Variable47", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State46", type=cpsml_Variable, multiplicity=Multiplicity(1, 1))
    }
)
relatedvariable248: BinaryAssociation = BinaryAssociation(
    name="relatedvariable248",
    ends={
        Property(name="cpsml_Variable50", type=cpsml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_Transition49", type=cpsml_Variable, multiplicity=Multiplicity(1, 1))
    }
)
csrc51: BinaryAssociation = BinaryAssociation(
    name="csrc51",
    ends={
        Property(name="State", type=cpsml_ComTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingComTransitions", type=cpsml_State, multiplicity=Multiplicity(1, 1))
    }
)
ctgt52: BinaryAssociation = BinaryAssociation(
    name="ctgt52",
    ends={
        Property(name="State53", type=cpsml_ComTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingComTransitions", type=cpsml_State, multiplicity=Multiplicity(1, 1))
    }
)
psrc54: BinaryAssociation = BinaryAssociation(
    name="psrc54",
    ends={
        Property(name="State55", type=cpsml_ProbTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingProbTransitions", type=cpsml_State, multiplicity=Multiplicity(1, 1))
    }
)
ptgt56: BinaryAssociation = BinaryAssociation(
    name="ptgt56",
    ends={
        Property(name="State57", type=cpsml_ProbTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingProbTransitions", type=cpsml_State, multiplicity=Multiplicity(1, 1))
    }
)
function58: BinaryAssociation = BinaryAssociation(
    name="function58",
    ends={
        Property(name="cpsml_Function", type=cpsml_ODE, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_ODE59", type=cpsml_Function, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition60: BinaryAssociation = BinaryAssociation(
    name="condition60",
    ends={
        Property(name="cpsml_Condition", type=cpsml_ODE, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_ODE61", type=cpsml_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
devariable66: BinaryAssociation = BinaryAssociation(
    name="devariable66",
    ends={
        Property(name="cpsml_DeVariable", type=cpsml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_Function67", type=cpsml_DeVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fright68: BinaryAssociation = BinaryAssociation(
    name="fright68",
    ends={
        Property(name="cpsml_Fright", type=cpsml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_Function69", type=cpsml_Fright, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_cpsml_ComTransition_Transition = Generalization(general=Transition, specific=cpsml_ComTransition)
gen_cpsml_ProbTransition_Transition = Generalization(general=Transition, specific=cpsml_ProbTransition)

# Domain Model
domain_model = DomainModel(
    name="cpsml",
    types={cpsml_ODE, cpsml_System, cpsml_Variable, cpsml_State, cpsml_Transition, cpsml_ProbTransition, cpsml_ComTransition, cpsml_Interval, cpsml_IndeVariable, Transition, cpsml_Function, cpsml_Condition, cpsml_DeVariable, cpsml_Fright},
    associations={initialState8, ownedodes11, currentState13, ownedvariables0, relatedvariable1, ownedStates4, ownedTransitions6, subtransitions36, subodes39, subrelatedvariables42, fatherState16, ptok19, slaveode21, outgoingComTransitions24, incomingComTransitions25, outgoingProbTransitions27, incomingProbTransitions28, subStates31, initialsubstate34, interval62, indevariable64, subrelatedvariable45, relatedvariable248, csrc51, ctgt52, psrc54, ptgt56, function58, condition60, devariable66, fright68},
    generalizations={gen_cpsml_ComTransition_Transition, gen_cpsml_ProbTransition_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
dtmc_Dtmc = Class(name="dtmc::Dtmc")
dtmc_Module = Class(name="dtmc::Module")
dtmc_Node = Class(name="dtmc::Node")
dtmc_Transition = Class(name="dtmc::Transition", is_abstract=True)
dtmc_SynchronizedTransition = Class(name="dtmc::SynchronizedTransition")
Transition = Class(name="Transition")
dtmc_CallTransition = Class(name="dtmc::CallTransition")
dtmc_InvokedTransition = Class(name="dtmc::InvokedTransition")
dtmc_StandardTransition = Class(name="dtmc::StandardTransition")

# dtmc_Dtmc class attributes and methods

# dtmc_Module class attributes and methods
dtmc_Module_isAutonomous: Property = Property(name="isAutonomous", type=BooleanType)
dtmc_Module.attributes={dtmc_Module_isAutonomous}

# dtmc_Node class attributes and methods
dtmc_Node_isStart: Property = Property(name="isStart", type=BooleanType)
dtmc_Node_isEnd: Property = Property(name="isEnd", type=BooleanType)
dtmc_Node_isFail: Property = Property(name="isFail", type=BooleanType)
dtmc_Node.attributes={dtmc_Node_isFail, dtmc_Node_isEnd, dtmc_Node_isStart}

# dtmc_Transition class attributes and methods
dtmc_Transition_probability: Property = Property(name="probability", type=StringType)
dtmc_Transition.attributes={dtmc_Transition_probability}

# dtmc_SynchronizedTransition class attributes and methods

# Transition class attributes and methods

# dtmc_CallTransition class attributes and methods

# dtmc_InvokedTransition class attributes and methods

# dtmc_StandardTransition class attributes and methods

# Relationships
modules0: BinaryAssociation = BinaryAssociation(
    name="modules0",
    ends={
        Property(name="dtmc_Module", type=dtmc_Dtmc, multiplicity=Multiplicity(1, 1)),
        Property(name="dtmc_Dtmc", type=dtmc_Module, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
module1: BinaryAssociation = BinaryAssociation(
    name="module1",
    ends={
        Property(name="Module", type=dtmc_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=dtmc_Module, multiplicity=Multiplicity(1, 1))
    }
)
outTransitions2: BinaryAssociation = BinaryAssociation(
    name="outTransitions2",
    ends={
        Property(name="Transition", type=dtmc_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="_from", type=dtmc_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
inTransitions3: BinaryAssociation = BinaryAssociation(
    name="inTransitions3",
    ends={
        Property(name="Transition4", type=dtmc_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="_to", type=dtmc_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
_from5: BinaryAssociation = BinaryAssociation(
    name="_from5",
    ends={
        Property(name="Node", type=dtmc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outTransitions", type=dtmc_Node, multiplicity=Multiplicity(0, 1))
    }
)
_to6: BinaryAssociation = BinaryAssociation(
    name="_to6",
    ends={
        Property(name="Node7", type=dtmc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="inTransitions", type=dtmc_Node, multiplicity=Multiplicity(0, 1))
    }
)
module8: BinaryAssociation = BinaryAssociation(
    name="module8",
    ends={
        Property(name="Module9", type=dtmc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=dtmc_Module, multiplicity=Multiplicity(1, 1))
    }
)
syncWith11: BinaryAssociation = BinaryAssociation(
    name="syncWith11",
    ends={
        Property(name="SynchronizedTransition", type=dtmc_SynchronizedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="synchedWith", type=dtmc_SynchronizedTransition, multiplicity=Multiplicity(1, 9999))
    }
)
synchedWith13: BinaryAssociation = BinaryAssociation(
    name="synchedWith13",
    ends={
        Property(name="SynchronizedTransition14", type=dtmc_SynchronizedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="syncWith", type=dtmc_SynchronizedTransition, multiplicity=Multiplicity(1, 9999))
    }
)
nodes15: BinaryAssociation = BinaryAssociation(
    name="nodes15",
    ends={
        Property(name="Node16", type=dtmc_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="module", type=dtmc_Node, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transitions17: BinaryAssociation = BinaryAssociation(
    name="transitions17",
    ends={
        Property(name="Transition19", type=dtmc_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="module18", type=dtmc_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callTransition21: BinaryAssociation = BinaryAssociation(
    name="callTransition21",
    ends={
        Property(name="CallTransition", type=dtmc_InvokedTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="invokedTransition", type=dtmc_CallTransition, multiplicity=Multiplicity(1, 1))
    }
)
invokedTransition20: BinaryAssociation = BinaryAssociation(
    name="invokedTransition20",
    ends={
        Property(name="InvokedTransition", type=dtmc_CallTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="callTransition", type=dtmc_InvokedTransition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_dtmc_SynchronizedTransition_Transition = Generalization(general=Transition, specific=dtmc_SynchronizedTransition)
gen_dtmc_CallTransition_Transition = Generalization(general=Transition, specific=dtmc_CallTransition)
gen_dtmc_StandardTransition_Transition = Generalization(general=Transition, specific=dtmc_StandardTransition)
gen_dtmc_InvokedTransition_Transition = Generalization(general=Transition, specific=dtmc_InvokedTransition)

# Domain Model
domain_model = DomainModel(
    name="dtmc",
    types={dtmc_Dtmc, dtmc_Module, dtmc_Node, dtmc_Transition, dtmc_SynchronizedTransition, Transition, dtmc_CallTransition, dtmc_InvokedTransition, dtmc_StandardTransition},
    associations={modules0, module1, outTransitions2, inTransitions3, _from5, _to6, module8, syncWith11, synchedWith13, nodes15, transitions17, callTransition21, invokedTransition20},
    generalizations={gen_dtmc_SynchronizedTransition_Transition, gen_dtmc_CallTransition_Transition, gen_dtmc_StandardTransition_Transition, gen_dtmc_InvokedTransition_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
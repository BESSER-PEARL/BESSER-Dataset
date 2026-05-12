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
mIO: Enumeration = Enumeration(
    name="mIO",
    literals={
            EnumerationLiteral(name="in_"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="inout")
    }
)

# Classes
metaCompo_mPort = Class(name="metaCompo_mPort")
metaCompo_mFSM = Class(name="metaCompo_mFSM")
metaCompo_mVariable = Class(name="metaCompo_mVariable")
metaCompo_mState = Class(name="metaCompo_mState")
metaCompo_mComp = Class(name="metaCompo_mComp")
metaCompo_mTransition = Class(name="metaCompo_mTransition")

# metaCompo_mPort class attributes and methods
metaCompo_mPort_name: Property = Property(name="name", type=StringType)
metaCompo_mPort_io: Property = Property(name="io", type=StringType)
metaCompo_mPort_type: Property = Property(name="type", type=StringType)
metaCompo_mPort.attributes={metaCompo_mPort_name, metaCompo_mPort_type, metaCompo_mPort_io}

# metaCompo_mFSM class attributes and methods
metaCompo_mFSM_name: Property = Property(name="name", type=StringType)
metaCompo_mFSM.attributes={metaCompo_mFSM_name}

# metaCompo_mVariable class attributes and methods
metaCompo_mVariable_name: Property = Property(name="name", type=StringType)
metaCompo_mVariable_type: Property = Property(name="type", type=StringType)
metaCompo_mVariable.attributes={metaCompo_mVariable_type, metaCompo_mVariable_name}

# metaCompo_mState class attributes and methods
metaCompo_mState_name: Property = Property(name="name", type=StringType)
metaCompo_mState.attributes={metaCompo_mState_name}

# metaCompo_mComp class attributes and methods
metaCompo_mComp_type: Property = Property(name="type", type=StringType)
metaCompo_mComp_name: Property = Property(name="name", type=StringType)
metaCompo_mComp.attributes={metaCompo_mComp_name, metaCompo_mComp_type}

# metaCompo_mTransition class attributes and methods
metaCompo_mTransition_name: Property = Property(name="name", type=StringType)
metaCompo_mTransition_triggerExp: Property = Property(name="triggerExp", type=StringType)
metaCompo_mTransition_guard: Property = Property(name="guard", type=StringType)
metaCompo_mTransition_action: Property = Property(name="action", type=StringType)
metaCompo_mTransition.attributes={metaCompo_mTransition_triggerExp, metaCompo_mTransition_guard, metaCompo_mTransition_name, metaCompo_mTransition_action}

# Relationships
subComps1: BinaryAssociation = BinaryAssociation(
    name="subComps1",
    ends={
        Property(name="metaCompo_mComp", type=metaCompo_mComp, multiplicity=Multiplicity(1, 1)),
        Property(name="metaCompo_mComp0", type=metaCompo_mComp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ports2: BinaryAssociation = BinaryAssociation(
    name="ports2",
    ends={
        Property(name="metaCompo_mPort", type=metaCompo_mComp, multiplicity=Multiplicity(1, 1)),
        Property(name="metaCompo_mComp3", type=metaCompo_mPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
FSMs4: BinaryAssociation = BinaryAssociation(
    name="FSMs4",
    ends={
        Property(name="mFSM", type=metaCompo_mComp, multiplicity=Multiplicity(1, 1)),
        Property(name="component", type=metaCompo_mFSM, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
compVar5: BinaryAssociation = BinaryAssociation(
    name="compVar5",
    ends={
        Property(name="metaCompo_mVariable", type=metaCompo_mComp, multiplicity=Multiplicity(1, 1)),
        Property(name="metaCompo_mComp6", type=metaCompo_mVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectedTo8: BinaryAssociation = BinaryAssociation(
    name="connectedTo8",
    ends={
        Property(name="metaCompo_mPort9", type=metaCompo_mPort, multiplicity=Multiplicity(1, 1)),
        Property(name="metaCompo_mPort7", type=metaCompo_mPort, multiplicity=Multiplicity(0, 1))
    }
)
connToVar10: BinaryAssociation = BinaryAssociation(
    name="connToVar10",
    ends={
        Property(name="metaCompo_mVariable12", type=metaCompo_mPort, multiplicity=Multiplicity(1, 1)),
        Property(name="metaCompo_mPort11", type=metaCompo_mVariable, multiplicity=Multiplicity(0, 1))
    }
)
component13: BinaryAssociation = BinaryAssociation(
    name="component13",
    ends={
        Property(name="mComp", type=metaCompo_mFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="FSMs", type=metaCompo_mComp, multiplicity=Multiplicity(1, 1))
    }
)
fsmVar14: BinaryAssociation = BinaryAssociation(
    name="fsmVar14",
    ends={
        Property(name="metaCompo_mVariable15", type=metaCompo_mFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="metaCompo_mFSM", type=metaCompo_mVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states16: BinaryAssociation = BinaryAssociation(
    name="states16",
    ends={
        Property(name="mState", type=metaCompo_mFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=metaCompo_mState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningFSM22: BinaryAssociation = BinaryAssociation(
    name="owningFSM22",
    ends={
        Property(name="mFSM23", type=metaCompo_mState, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=metaCompo_mFSM, multiplicity=Multiplicity(1, 1))
    }
)
stateVar24: BinaryAssociation = BinaryAssociation(
    name="stateVar24",
    ends={
        Property(name="metaCompo_mVariable26", type=metaCompo_mState, multiplicity=Multiplicity(1, 1)),
        Property(name="metaCompo_mState25", type=metaCompo_mVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingTransitions27: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions27",
    ends={
        Property(name="mTransition", type=metaCompo_mState, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=metaCompo_mTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransitions28: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions28",
    ends={
        Property(name="mTransition29", type=metaCompo_mState, multiplicity=Multiplicity(1, 1)),
        Property(name="destination", type=metaCompo_mTransition, multiplicity=Multiplicity(0, 9999))
    }
)
subStates31: BinaryAssociation = BinaryAssociation(
    name="subStates31",
    ends={
        Property(name="metaCompo_mState32", type=metaCompo_mState, multiplicity=Multiplicity(1, 1)),
        Property(name="metaCompo_mState30", type=metaCompo_mState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source33: BinaryAssociation = BinaryAssociation(
    name="source33",
    ends={
        Property(name="mState34", type=metaCompo_mTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=metaCompo_mState, multiplicity=Multiplicity(1, 1))
    }
)
destination35: BinaryAssociation = BinaryAssociation(
    name="destination35",
    ends={
        Property(name="mState36", type=metaCompo_mTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=metaCompo_mState, multiplicity=Multiplicity(1, 1))
    }
)
trigerringVar37: BinaryAssociation = BinaryAssociation(
    name="trigerringVar37",
    ends={
        Property(name="metaCompo_mVariable38", type=metaCompo_mTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="metaCompo_mTransition", type=metaCompo_mVariable, multiplicity=Multiplicity(0, 9999))
    }
)
triggeringPort39: BinaryAssociation = BinaryAssociation(
    name="triggeringPort39",
    ends={
        Property(name="metaCompo_mPort41", type=metaCompo_mTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="metaCompo_mTransition40", type=metaCompo_mPort, multiplicity=Multiplicity(0, 9999))
    }
)
initialState17: BinaryAssociation = BinaryAssociation(
    name="initialState17",
    ends={
        Property(name="metaCompo_mState", type=metaCompo_mFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="metaCompo_mFSM18", type=metaCompo_mState, multiplicity=Multiplicity(1, 1))
    }
)
finalState19: BinaryAssociation = BinaryAssociation(
    name="finalState19",
    ends={
        Property(name="metaCompo_mState21", type=metaCompo_mFSM, multiplicity=Multiplicity(1, 1)),
        Property(name="metaCompo_mFSM20", type=metaCompo_mState, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="metaCompo",
    types={metaCompo_mPort, metaCompo_mFSM, metaCompo_mVariable, metaCompo_mState, metaCompo_mComp, metaCompo_mTransition, mIO},
    associations={subComps1, ports2, FSMs4, compVar5, connectedTo8, connToVar10, component13, fsmVar14, states16, owningFSM22, stateVar24, outgoingTransitions27, incomingTransitions28, subStates31, source33, destination35, trigerringVar37, triggeringPort39, initialState17, finalState19},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
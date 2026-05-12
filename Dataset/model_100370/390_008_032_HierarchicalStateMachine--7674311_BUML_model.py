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
HSM_MgaObject = Class(name="HSM_MgaObject")
HSM_DataVar = Class(name="HSM_DataVar")
HSM_StateBase = Class(name="HSM_StateBase")
MgaObject = Class(name="MgaObject")
AssociationStateState = Class(name="AssociationStateState")
DataVar = Class(name="DataVar")
AssociationDataStateBase = Class(name="AssociationDataStateBase")
HSM_StateDateRelation = Class(name="HSM_StateDateRelation")
StateBase = Class(name="StateBase")
OrState = Class(name="OrState")
HSM_Transition = Class(name="HSM_Transition")
HSM_RootFolder = Class(name="HSM_RootFolder")
RootFolder = Class(name="RootFolder")
HSM_OrState = Class(name="HSM_OrState")
CompoundState = Class(name="CompoundState")
State = Class(name="State")
Init = Class(name="Init")
HSM_PrimitiveState = Class(name="HSM_PrimitiveState")
HSM_Init = Class(name="HSM_Init")
PrimitiveState = Class(name="PrimitiveState")
StateDataRelation = Class(name="StateDataRelation")
Transition = Class(name="Transition")
HSM_AndState = Class(name="HSM_AndState")
HSM_CompoundState = Class(name="HSM_CompoundState")
AndState = Class(name="AndState")
HSM_State = Class(name="HSM_State")
HSM_StateDataRelation = Class(name="HSM_StateDataRelation")
HSM_AssociationStateState = Class(name="HSM_AssociationStateState")
HSM_AssociationDataStateBase = Class(name="HSM_AssociationDataStateBase")

# HSM_MgaObject class attributes and methods
HSM_MgaObject_name: Property = Property(name="name", type=StringType)
HSM_MgaObject_position: Property = Property(name="position", type=StringType)
HSM_MgaObject.attributes={HSM_MgaObject_name, HSM_MgaObject_position}

# HSM_DataVar class attributes and methods

# HSM_StateBase class attributes and methods
HSM_StateBase_defaultTransition: Property = Property(name="defaultTransition", type=StringType)
HSM_StateBase_marked: Property = Property(name="marked", type=StringType)
HSM_StateBase.attributes={HSM_StateBase_defaultTransition, HSM_StateBase_marked}

# MgaObject class attributes and methods

# AssociationStateState class attributes and methods

# DataVar class attributes and methods

# AssociationDataStateBase class attributes and methods

# HSM_StateDateRelation class attributes and methods
HSM_StateDateRelation_value: Property = Property(name="value", type=StringType)
HSM_StateDateRelation_color: Property = Property(name="color", type=StringType)
HSM_StateDateRelation.attributes={HSM_StateDateRelation_color, HSM_StateDateRelation_value}

# StateBase class attributes and methods

# OrState class attributes and methods

# HSM_Transition class attributes and methods
HSM_Transition_guard: Property = Property(name="guard", type=StringType)
HSM_Transition_trigger: Property = Property(name="trigger", type=StringType)
HSM_Transition_action: Property = Property(name="action", type=StringType)
HSM_Transition_isSync: Property = Property(name="isSync", type=StringType)
HSM_Transition.attributes={HSM_Transition_guard, HSM_Transition_isSync, HSM_Transition_trigger, HSM_Transition_action}

# HSM_RootFolder class attributes and methods
HSM_RootFolder_name: Property = Property(name="name", type=StringType)
HSM_RootFolder.attributes={HSM_RootFolder_name}

# RootFolder class attributes and methods

# HSM_OrState class attributes and methods

# CompoundState class attributes and methods

# State class attributes and methods

# Init class attributes and methods

# HSM_PrimitiveState class attributes and methods

# HSM_Init class attributes and methods

# PrimitiveState class attributes and methods

# StateDataRelation class attributes and methods

# Transition class attributes and methods

# HSM_AndState class attributes and methods

# HSM_CompoundState class attributes and methods

# AndState class attributes and methods

# HSM_State class attributes and methods

# HSM_StateDataRelation class attributes and methods
HSM_StateDataRelation_value: Property = Property(name="value", type=StringType)
HSM_StateDataRelation_color: Property = Property(name="color", type=StringType)
HSM_StateDataRelation.attributes={HSM_StateDataRelation_color, HSM_StateDataRelation_value}

# HSM_AssociationStateState class attributes and methods

# HSM_AssociationDataStateBase class attributes and methods

# Relationships
associationStateStatedst0: BinaryAssociation = BinaryAssociation(
    name="associationStateStatedst0",
    ends={
        Property(name="AssociationStateState", type=HSM_StateBase, multiplicity=Multiplicity(1, 1)),
        Property(name="dstTransition", type=AssociationStateState, multiplicity=Multiplicity(1, 9999))
    }
)
associationStateStatesrc1: BinaryAssociation = BinaryAssociation(
    name="associationStateStatesrc1",
    ends={
        Property(name="AssociationStateState2", type=HSM_StateBase, multiplicity=Multiplicity(1, 1)),
        Property(name="srcTransition", type=AssociationStateState, multiplicity=Multiplicity(1, 9999))
    }
)
data3: BinaryAssociation = BinaryAssociation(
    name="data3",
    ends={
        Property(name="DataVar", type=HSM_StateBase, multiplicity=Multiplicity(1, 1)),
        Property(name="stateBase", type=DataVar, multiplicity=Multiplicity(0, 9999))
    }
)
associationDataStateBase4: BinaryAssociation = BinaryAssociation(
    name="associationDataStateBase4",
    ends={
        Property(name="AssociationDataStateBase", type=HSM_StateBase, multiplicity=Multiplicity(1, 1)),
        Property(name="stateBase5", type=AssociationDataStateBase, multiplicity=Multiplicity(1, 1))
    }
)
stateBase6: BinaryAssociation = BinaryAssociation(
    name="stateBase6",
    ends={
        Property(name="StateBase", type=HSM_DataVar, multiplicity=Multiplicity(1, 1)),
        Property(name="data", type=StateBase, multiplicity=Multiplicity(0, 9999))
    }
)
orState7: BinaryAssociation = BinaryAssociation(
    name="orState7",
    ends={
        Property(name="OrState", type=HSM_DataVar, multiplicity=Multiplicity(1, 1)),
        Property(name="dataVar", type=OrState, multiplicity=Multiplicity(1, 1))
    }
)
associationDataStateBase8: BinaryAssociation = BinaryAssociation(
    name="associationDataStateBase8",
    ends={
        Property(name="AssociationDataStateBase10", type=HSM_DataVar, multiplicity=Multiplicity(1, 1)),
        Property(name="dataVar9", type=AssociationDataStateBase, multiplicity=Multiplicity(1, 1))
    }
)
orState11: BinaryAssociation = BinaryAssociation(
    name="orState11",
    ends={
        Property(name="OrState12", type=HSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=OrState, multiplicity=Multiplicity(1, 1))
    }
)
associationStateState13: BinaryAssociation = BinaryAssociation(
    name="associationStateState13",
    ends={
        Property(name="AssociationStateState15", type=HSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition14", type=AssociationStateState, multiplicity=Multiplicity(1, 1))
    }
)
dataVar25: BinaryAssociation = BinaryAssociation(
    name="dataVar25",
    ends={
        Property(name="DataVar27", type=HSM_OrState, multiplicity=Multiplicity(1, 1)),
        Property(name="orState26", type=DataVar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootFolders16: BinaryAssociation = BinaryAssociation(
    name="rootFolders16",
    ends={
        Property(name="RootFolder", type=HSM_RootFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_RootFolder", type=RootFolder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orState17: BinaryAssociation = BinaryAssociation(
    name="orState17",
    ends={
        Property(name="OrState18", type=HSM_RootFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="rootFolder", type=OrState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootFolder19: BinaryAssociation = BinaryAssociation(
    name="rootFolder19",
    ends={
        Property(name="RootFolder20", type=HSM_OrState, multiplicity=Multiplicity(1, 1)),
        Property(name="orState", type=RootFolder, multiplicity=Multiplicity(1, 1))
    }
)
state21: BinaryAssociation = BinaryAssociation(
    name="state21",
    ends={
        Property(name="State", type=HSM_OrState, multiplicity=Multiplicity(1, 1)),
        Property(name="orState22", type=State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init23: BinaryAssociation = BinaryAssociation(
    name="init23",
    ends={
        Property(name="Init", type=HSM_OrState, multiplicity=Multiplicity(1, 1)),
        Property(name="orState24", type=Init, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
stateDataRelation28: BinaryAssociation = BinaryAssociation(
    name="stateDataRelation28",
    ends={
        Property(name="StateDataRelation", type=HSM_OrState, multiplicity=Multiplicity(1, 1)),
        Property(name="orState29", type=StateDataRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition30: BinaryAssociation = BinaryAssociation(
    name="transition30",
    ends={
        Property(name="Transition", type=HSM_OrState, multiplicity=Multiplicity(1, 1)),
        Property(name="orState31", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compoundState32: BinaryAssociation = BinaryAssociation(
    name="compoundState32",
    ends={
        Property(name="CompoundState", type=HSM_OrState, multiplicity=Multiplicity(1, 1)),
        Property(name="orState33", type=CompoundState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compoundState34: BinaryAssociation = BinaryAssociation(
    name="compoundState34",
    ends={
        Property(name="CompoundState35", type=HSM_AndState, multiplicity=Multiplicity(1, 1)),
        Property(name="andState", type=CompoundState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
andState36: BinaryAssociation = BinaryAssociation(
    name="andState36",
    ends={
        Property(name="AndState", type=HSM_CompoundState, multiplicity=Multiplicity(1, 1)),
        Property(name="compoundState", type=AndState, multiplicity=Multiplicity(1, 1))
    }
)
orState37: BinaryAssociation = BinaryAssociation(
    name="orState37",
    ends={
        Property(name="OrState39", type=HSM_CompoundState, multiplicity=Multiplicity(1, 1)),
        Property(name="compoundState38", type=OrState, multiplicity=Multiplicity(1, 1))
    }
)
dstTransition51: BinaryAssociation = BinaryAssociation(
    name="dstTransition51",
    ends={
        Property(name="StateBase52", type=HSM_AssociationStateState, multiplicity=Multiplicity(1, 1)),
        Property(name="associationStateStatedst", type=StateBase, multiplicity=Multiplicity(1, 9999))
    }
)
orState40: BinaryAssociation = BinaryAssociation(
    name="orState40",
    ends={
        Property(name="OrState41", type=HSM_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="init", type=OrState, multiplicity=Multiplicity(1, 1))
    }
)
orState42: BinaryAssociation = BinaryAssociation(
    name="orState42",
    ends={
        Property(name="OrState43", type=HSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=OrState, multiplicity=Multiplicity(1, 1))
    }
)
orState44: BinaryAssociation = BinaryAssociation(
    name="orState44",
    ends={
        Property(name="OrState45", type=HSM_StateDataRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="stateDataRelation", type=OrState, multiplicity=Multiplicity(1, 1))
    }
)
associationDataStateBase146: BinaryAssociation = BinaryAssociation(
    name="associationDataStateBase146",
    ends={
        Property(name="AssociationDataStateBase48", type=HSM_StateDataRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="stateDataRelation47", type=AssociationDataStateBase, multiplicity=Multiplicity(1, 1))
    }
)
transition49: BinaryAssociation = BinaryAssociation(
    name="transition49",
    ends={
        Property(name="Transition50", type=HSM_AssociationStateState, multiplicity=Multiplicity(1, 1)),
        Property(name="associationStateState", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
srcTransition53: BinaryAssociation = BinaryAssociation(
    name="srcTransition53",
    ends={
        Property(name="StateBase54", type=HSM_AssociationStateState, multiplicity=Multiplicity(1, 1)),
        Property(name="associationStateStatesrc", type=StateBase, multiplicity=Multiplicity(1, 9999))
    }
)
stateDataRelation55: BinaryAssociation = BinaryAssociation(
    name="stateDataRelation55",
    ends={
        Property(name="StateDataRelation56", type=HSM_AssociationDataStateBase, multiplicity=Multiplicity(1, 1)),
        Property(name="associationDataStateBase1", type=StateDataRelation, multiplicity=Multiplicity(1, 1))
    }
)
dataVar57: BinaryAssociation = BinaryAssociation(
    name="dataVar57",
    ends={
        Property(name="DataVar58", type=HSM_AssociationDataStateBase, multiplicity=Multiplicity(1, 1)),
        Property(name="associationDataStateBase", type=DataVar, multiplicity=Multiplicity(1, 9999))
    }
)
stateBase59: BinaryAssociation = BinaryAssociation(
    name="stateBase59",
    ends={
        Property(name="StateBase61", type=HSM_AssociationDataStateBase, multiplicity=Multiplicity(1, 1)),
        Property(name="associationDataStateBase60", type=StateBase, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_HSM_DataVar_MgaObject = Generalization(general=MgaObject, specific=HSM_DataVar)
gen_HSM_StateBase_MgaObject = Generalization(general=MgaObject, specific=HSM_StateBase)
gen_HSM_StateDateRelation_MgaObject = Generalization(general=MgaObject, specific=HSM_StateDateRelation)
gen_HSM_Transition_MgaObject = Generalization(general=MgaObject, specific=HSM_Transition)
gen_HSM_OrState_CompoundState = Generalization(general=CompoundState, specific=HSM_OrState)
gen_HSM_PrimitiveState_StateBase = Generalization(general=StateBase, specific=HSM_PrimitiveState)
gen_HSM_AndState_CompoundState = Generalization(general=CompoundState, specific=HSM_AndState)
gen_HSM_CompoundState_StateBase = Generalization(general=StateBase, specific=HSM_CompoundState)
gen_HSM_Init_PrimitiveState = Generalization(general=PrimitiveState, specific=HSM_Init)
gen_HSM_State_PrimitiveState = Generalization(general=PrimitiveState, specific=HSM_State)
gen_HSM_StateDataRelation_PrimitiveState = Generalization(general=PrimitiveState, specific=HSM_StateDataRelation)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={HSM_MgaObject, HSM_DataVar, HSM_StateBase, MgaObject, AssociationStateState, DataVar, AssociationDataStateBase, HSM_StateDateRelation, StateBase, OrState, HSM_Transition, HSM_RootFolder, RootFolder, HSM_OrState, CompoundState, State, Init, HSM_PrimitiveState, HSM_Init, PrimitiveState, StateDataRelation, Transition, HSM_AndState, HSM_CompoundState, AndState, HSM_State, HSM_StateDataRelation, HSM_AssociationStateState, HSM_AssociationDataStateBase},
    associations={associationStateStatedst0, associationStateStatesrc1, data3, associationDataStateBase4, stateBase6, orState7, associationDataStateBase8, orState11, associationStateState13, dataVar25, rootFolders16, orState17, rootFolder19, state21, init23, stateDataRelation28, transition30, compoundState32, compoundState34, andState36, orState37, dstTransition51, orState40, orState42, orState44, associationDataStateBase146, transition49, srcTransition53, stateDataRelation55, dataVar57, stateBase59},
    generalizations={gen_HSM_DataVar_MgaObject, gen_HSM_StateBase_MgaObject, gen_HSM_StateDateRelation_MgaObject, gen_HSM_Transition_MgaObject, gen_HSM_OrState_CompoundState, gen_HSM_PrimitiveState_StateBase, gen_HSM_AndState_CompoundState, gen_HSM_CompoundState_StateBase, gen_HSM_Init_PrimitiveState, gen_HSM_State_PrimitiveState, gen_HSM_StateDataRelation_PrimitiveState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
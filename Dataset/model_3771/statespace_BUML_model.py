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
statespace_Rule = Class(name="statespace::Rule")
statespace_StateSpace = Class(name="statespace::StateSpace")
Storage = Class(name="Storage")
statespace_State = Class(name="statespace::State")
statespace_EqualityHelper = Class(name="statespace::EqualityHelper")
statespace_EStringToStringMapEntry = Class(name="statespace::EStringToStringMapEntry")
statespace_Transition = Class(name="statespace::Transition")
statespace_Model = Class(name="statespace::Model")
statespace_EObjectIntegerMapEntry = Class(name="statespace::EObjectIntegerMapEntry")
statespace_EAttribute = Class(name="statespace::EAttribute")
statespace_EClass = Class(name="statespace::EClass")
statespace_Storage = Class(name="statespace::Storage")
statespace_EObject = Class(name="statespace::EObject")

# statespace_Rule class attributes and methods

# statespace_StateSpace class attributes and methods
statespace_StateSpace_stateCount: Property = Property(name="stateCount", type=IntegerType)
statespace_StateSpace_transitionCount: Property = Property(name="transitionCount", type=IntegerType)
statespace_StateSpace_layoutZoomLevel: Property = Property(name="layoutZoomLevel", type=IntegerType)
statespace_StateSpace_layoutHideLabels: Property = Property(name="layoutHideLabels", type=BooleanType)
statespace_StateSpace_layoutHideIndizes: Property = Property(name="layoutHideIndizes", type=BooleanType)
statespace_StateSpace_maxStateDistance: Property = Property(name="maxStateDistance", type=IntegerType)
statespace_StateSpace_layoutStateRepulsion: Property = Property(name="layoutStateRepulsion", type=IntegerType)
statespace_StateSpace_layoutTransitionAttraction: Property = Property(name="layoutTransitionAttraction", type=IntegerType)
statespace_StateSpace_allParameterKeys: Property = Property(name="allParameterKeys", type=StringType)
statespace_StateSpace_m_removeState: Method = Method(name="removeState", parameters={Parameter(name='state')}, type=BooleanType)
statespace_StateSpace_m_updateEqualityHelper: Method = Method(name="updateEqualityHelper", parameters={})
statespace_StateSpace_m_incTransitionCount: Method = Method(name="incTransitionCount", parameters={}, type=IntegerType)
statespace_StateSpace.attributes={statespace_StateSpace_stateCount, statespace_StateSpace_layoutStateRepulsion, statespace_StateSpace_transitionCount, statespace_StateSpace_layoutHideLabels, statespace_StateSpace_maxStateDistance, statespace_StateSpace_layoutZoomLevel, statespace_StateSpace_layoutHideIndizes, statespace_StateSpace_layoutTransitionAttraction, statespace_StateSpace_allParameterKeys}
statespace_StateSpace.methods={statespace_StateSpace_m_removeState, statespace_StateSpace_m_incTransitionCount, statespace_StateSpace_m_updateEqualityHelper}

# Storage class attributes and methods

# statespace_State class attributes and methods
statespace_State_index: Property = Property(name="index", type=IntegerType)
statespace_State_open: Property = Property(name="open", type=BooleanType)
statespace_State_goal: Property = Property(name="goal", type=BooleanType)
statespace_State_pruned: Property = Property(name="pruned", type=BooleanType)
statespace_State_location: Property = Property(name="location", type=StringType)
statespace_State_objectCount: Property = Property(name="objectCount", type=IntegerType)
statespace_State_hashCode: Property = Property(name="hashCode", type=IntegerType)
statespace_State_derivedFrom: Property = Property(name="derivedFrom", type=IntegerType)
statespace_State_objectKeys: Property = Property(name="objectKeys", type=StringType)
statespace_State_m_isInitial: Method = Method(name="isInitial", parameters={}, type=BooleanType)
statespace_State_m_getOutgoing: Method = Method(name="getOutgoing", parameters={Parameter(name='match'), Parameter(name='target'), Parameter(name='rule'), Parameter(name='paramIDs')}, type=StringType)
statespace_State.attributes={statespace_State_location, statespace_State_derivedFrom, statespace_State_pruned, statespace_State_goal, statespace_State_open, statespace_State_hashCode, statespace_State_objectCount, statespace_State_objectKeys, statespace_State_index}
statespace_State.methods={statespace_State_m_getOutgoing, statespace_State_m_isInitial}

# statespace_EqualityHelper class attributes and methods
statespace_EqualityHelper_checkLinkOrder: Property = Property(name="checkLinkOrder", type=BooleanType)
statespace_EqualityHelper_m_equals: Method = Method(name="equals", parameters={Parameter(name='model1'), Parameter(name='model2')}, type=BooleanType)
statespace_EqualityHelper_m_hashCode: Method = Method(name="hashCode", parameters={Parameter(name='model')}, type=IntegerType)
statespace_EqualityHelper_m_setStateSpace: Method = Method(name="setStateSpace", parameters={Parameter(name='stateSpace')})
statespace_EqualityHelper.attributes={statespace_EqualityHelper_checkLinkOrder}
statespace_EqualityHelper.methods={statespace_EqualityHelper_m_equals, statespace_EqualityHelper_m_hashCode, statespace_EqualityHelper_m_setStateSpace}

# statespace_EStringToStringMapEntry class attributes and methods

# statespace_Transition class attributes and methods
statespace_Transition_parameterCount: Property = Property(name="parameterCount", type=IntegerType)
statespace_Transition_parameterKeys: Property = Property(name="parameterKeys", type=StringType)
statespace_Transition_match: Property = Property(name="match", type=IntegerType)
statespace_Transition_m_getLabel: Method = Method(name="getLabel", parameters={}, type=StringType)
statespace_Transition.attributes={statespace_Transition_parameterCount, statespace_Transition_parameterKeys, statespace_Transition_match}
statespace_Transition.methods={statespace_Transition_m_getLabel}

# statespace_Model class attributes and methods
statespace_Model_objectKeys: Property = Property(name="objectKeys", type=StringType)
statespace_Model_resource: Property = Property(name="resource", type=StringType)
statespace_Model_eGraph: Property = Property(name="eGraph", type=StringType)
statespace_Model_objectCount: Property = Property(name="objectCount", type=IntegerType)
statespace_Model_m_getCopy: Method = Method(name="getCopy", parameters={Parameter(name='match')}, type=StringType)
statespace_Model_m_updateObjectKeys: Method = Method(name="updateObjectKeys", parameters={Parameter(name='identityTypes')}, type=BooleanType)
statespace_Model_m_collectMissingRootObjects: Method = Method(name="collectMissingRootObjects", parameters={})
statespace_Model.attributes={statespace_Model_eGraph, statespace_Model_resource, statespace_Model_objectKeys, statespace_Model_objectCount}
statespace_Model.methods={statespace_Model_m_collectMissingRootObjects, statespace_Model_m_getCopy, statespace_Model_m_updateObjectKeys}

# statespace_EObjectIntegerMapEntry class attributes and methods
statespace_EObjectIntegerMapEntry_value: Property = Property(name="value", type=StringType)
statespace_EObjectIntegerMapEntry.attributes={statespace_EObjectIntegerMapEntry_value}

# statespace_EAttribute class attributes and methods

# statespace_EClass class attributes and methods

# statespace_Storage class attributes and methods
statespace_Storage_data: Property = Property(name="data", type=StringType)
statespace_Storage_m_getData: Method = Method(name="getData", parameters={Parameter(name='index')}, type=IntegerType)
statespace_Storage_m_getData: Method = Method(name="getData", parameters={Parameter(name='endIndex'), Parameter(name='beginIndex')}, type=StringType)
statespace_Storage_m_setData: Method = Method(name="setData", parameters={Parameter(name='beginIndex'), Parameter(name='value')})
statespace_Storage_m_setData: Method = Method(name="setData", parameters={Parameter(name='beginIndex'), Parameter(name='value'), Parameter(name='endIndex')})
statespace_Storage_m_setData: Method = Method(name="setData", parameters={Parameter(name='value'), Parameter(name='index')})
statespace_Storage.attributes={statespace_Storage_data}
statespace_Storage.methods={statespace_Storage_m_getData, statespace_Storage_m_getData, statespace_Storage_m_setData, statespace_Storage_m_setData, statespace_Storage_m_setData}

# statespace_EObject class attributes and methods

# Relationships
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="State", type=statespace_StateSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="stateSpace", type=statespace_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialStates2: BinaryAssociation = BinaryAssociation(
    name="initialStates2",
    ends={
        Property(name="statespace_State", type=statespace_StateSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="statespace_StateSpace3", type=statespace_State, multiplicity=Multiplicity(0, 9999))
    }
)
rules0: BinaryAssociation = BinaryAssociation(
    name="rules0",
    ends={
        Property(name="statespace_Rule", type=statespace_StateSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="statespace_StateSpace", type=statespace_Rule, multiplicity=Multiplicity(0, 9999))
    }
)
equalityHelper7: BinaryAssociation = BinaryAssociation(
    name="equalityHelper7",
    ends={
        Property(name="statespace_EqualityHelper", type=statespace_StateSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="statespace_StateSpace8", type=statespace_EqualityHelper, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
openStates4: BinaryAssociation = BinaryAssociation(
    name="openStates4",
    ends={
        Property(name="statespace_State6", type=statespace_StateSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="statespace_StateSpace5", type=statespace_State, multiplicity=Multiplicity(0, 9999))
    }
)
properties9: BinaryAssociation = BinaryAssociation(
    name="properties9",
    ends={
        Property(name="statespace_EStringToStringMapEntry", type=statespace_StateSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="statespace_StateSpace10", type=statespace_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing12: BinaryAssociation = BinaryAssociation(
    name="outgoing12",
    ends={
        Property(name="Transition13", type=statespace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=statespace_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateSpace14: BinaryAssociation = BinaryAssociation(
    name="stateSpace14",
    ends={
        Property(name="StateSpace", type=statespace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=statespace_StateSpace, multiplicity=Multiplicity(0, 1))
    }
)
incoming11: BinaryAssociation = BinaryAssociation(
    name="incoming11",
    ends={
        Property(name="Transition", type=statespace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=statespace_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
model15: BinaryAssociation = BinaryAssociation(
    name="model15",
    ends={
        Property(name="statespace_State16", type=statespace_Model, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="statespace_Model", type=statespace_State, multiplicity=Multiplicity(1, 1))
    }
)
objectHashCodes17: BinaryAssociation = BinaryAssociation(
    name="objectHashCodes17",
    ends={
        Property(name="statespace_EObjectIntegerMapEntry", type=statespace_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="statespace_Model18", type=statespace_EObjectIntegerMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectKeysMap19: BinaryAssociation = BinaryAssociation(
    name="objectKeysMap19",
    ends={
        Property(name="statespace_EObjectIntegerMapEntry21", type=statespace_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="statespace_Model20", type=statespace_EObjectIntegerMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source22: BinaryAssociation = BinaryAssociation(
    name="source22",
    ends={
        Property(name="State23", type=statespace_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=statespace_State, multiplicity=Multiplicity(0, 1))
    }
)
target24: BinaryAssociation = BinaryAssociation(
    name="target24",
    ends={
        Property(name="State25", type=statespace_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=statespace_State, multiplicity=Multiplicity(0, 1))
    }
)
rule26: BinaryAssociation = BinaryAssociation(
    name="rule26",
    ends={
        Property(name="statespace_Rule27", type=statespace_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statespace_Transition", type=statespace_Rule, multiplicity=Multiplicity(0, 1))
    }
)
ignoredAttributes28: BinaryAssociation = BinaryAssociation(
    name="ignoredAttributes28",
    ends={
        Property(name="statespace_EAttribute", type=statespace_EqualityHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="statespace_EqualityHelper29", type=statespace_EAttribute, multiplicity=Multiplicity(1, 9999))
    }
)
identityTypes30: BinaryAssociation = BinaryAssociation(
    name="identityTypes30",
    ends={
        Property(name="statespace_EClass", type=statespace_EqualityHelper, multiplicity=Multiplicity(1, 1)),
        Property(name="statespace_EqualityHelper31", type=statespace_EClass, multiplicity=Multiplicity(1, 9999))
    }
)
key32: BinaryAssociation = BinaryAssociation(
    name="key32",
    ends={
        Property(name="statespace_EObject", type=statespace_EObjectIntegerMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="statespace_EObjectIntegerMapEntry33", type=statespace_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_statespace_StateSpace_Storage = Generalization(general=Storage, specific=statespace_StateSpace)
gen_statespace_State_Storage = Generalization(general=Storage, specific=statespace_State)
gen_statespace_Transition_Storage = Generalization(general=Storage, specific=statespace_Transition)

# Domain Model
domain_model = DomainModel(
    name="statespace",
    types={statespace_Rule, statespace_StateSpace, Storage, statespace_State, statespace_EqualityHelper, statespace_EStringToStringMapEntry, statespace_Transition, statespace_Model, statespace_EObjectIntegerMapEntry, statespace_EAttribute, statespace_EClass, statespace_Storage, statespace_EObject},
    associations={states1, initialStates2, rules0, equalityHelper7, openStates4, properties9, outgoing12, stateSpace14, incoming11, model15, objectHashCodes17, objectKeysMap19, source22, target24, rule26, ignoredAttributes28, identityTypes30, key32},
    generalizations={gen_statespace_StateSpace_Storage, gen_statespace_State_Storage, gen_statespace_Transition_Storage},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
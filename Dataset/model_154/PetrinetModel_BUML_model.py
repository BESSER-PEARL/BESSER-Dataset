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
petrinetmodel_Petrinet = Class(name="petrinetmodel_Petrinet")
petrinetmodel_Transition = Class(name="petrinetmodel_Transition")
petrinetmodel_Place = Class(name="petrinetmodel_Place")
petrinetmodel_EdgeToPlace = Class(name="petrinetmodel_EdgeToPlace")
petrinetmodel_EdgeToTransaction = Class(name="petrinetmodel_EdgeToTransaction")
Edge = Class(name="Edge")
petrinetmodel_Edge = Class(name="petrinetmodel_Edge")

# petrinetmodel_Petrinet class attributes and methods
petrinetmodel_Petrinet_m_fireTransactionsByPriority: Method = Method(name="fireTransactionsByPriority", parameters={})
petrinetmodel_Petrinet_m_init: Method = Method(name="init", parameters={})
petrinetmodel_Petrinet.methods={petrinetmodel_Petrinet_m_init, petrinetmodel_Petrinet_m_fireTransactionsByPriority}

# petrinetmodel_Transition class attributes and methods
petrinetmodel_Transition_token: Property = Property(name="token", type=IntegerType)
petrinetmodel_Transition_id: Property = Property(name="id", type=IntegerType)
petrinetmodel_Transition_priority: Property = Property(name="priority", type=IntegerType)
petrinetmodel_Transition_m_prepare: Method = Method(name="prepare", parameters={}, type=BooleanType)
petrinetmodel_Transition_m_fire: Method = Method(name="fire", parameters={})
petrinetmodel_Transition_m_addInputPlace: Method = Method(name="addInputPlace", parameters={Parameter(name='petrinetmodel_p', type=StringType)})
petrinetmodel_Transition.attributes={petrinetmodel_Transition_token, petrinetmodel_Transition_priority, petrinetmodel_Transition_id}
petrinetmodel_Transition.methods={petrinetmodel_Transition_m_prepare, petrinetmodel_Transition_m_fire, petrinetmodel_Transition_m_addInputPlace}

# petrinetmodel_Place class attributes and methods
petrinetmodel_Place_token: Property = Property(name="token", type=IntegerType)
petrinetmodel_Place_id: Property = Property(name="id", type=IntegerType)
petrinetmodel_Place_m_addToken: Method = Method(name="addToken", parameters={})
petrinetmodel_Place_m_hasToken: Method = Method(name="hasToken", parameters={}, type=BooleanType)
petrinetmodel_Place_m_removeToken: Method = Method(name="removeToken", parameters={})
petrinetmodel_Place_m_init: Method = Method(name="init", parameters={})
petrinetmodel_Place.attributes={petrinetmodel_Place_id, petrinetmodel_Place_token}
petrinetmodel_Place.methods={petrinetmodel_Place_m_removeToken, petrinetmodel_Place_m_hasToken, petrinetmodel_Place_m_addToken, petrinetmodel_Place_m_init}

# petrinetmodel_EdgeToPlace class attributes and methods

# petrinetmodel_EdgeToTransaction class attributes and methods

# Edge class attributes and methods

# petrinetmodel_Edge class attributes and methods
petrinetmodel_Edge_weight: Property = Property(name="weight", type=IntegerType)
petrinetmodel_Edge.attributes={petrinetmodel_Edge_weight}

# Relationships
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="petrinetmodel_Transition", type=petrinetmodel_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetmodel_Petrinet", type=petrinetmodel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
places1: BinaryAssociation = BinaryAssociation(
    name="places1",
    ends={
        Property(name="petrinetmodel_Place", type=petrinetmodel_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetmodel_Petrinet2", type=petrinetmodel_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out3: BinaryAssociation = BinaryAssociation(
    name="out3",
    ends={
        Property(name="petrinetmodel_EdgeToPlace", type=petrinetmodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetmodel_Transition4", type=petrinetmodel_EdgeToPlace, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inputPlaces5: BinaryAssociation = BinaryAssociation(
    name="inputPlaces5",
    ends={
        Property(name="petrinetmodel_Place7", type=petrinetmodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetmodel_Transition6", type=petrinetmodel_Place, multiplicity=Multiplicity(0, 9999))
    }
)
out8: BinaryAssociation = BinaryAssociation(
    name="out8",
    ends={
        Property(name="petrinetmodel_EdgeToTransaction", type=petrinetmodel_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetmodel_Place9", type=petrinetmodel_EdgeToTransaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in_10: BinaryAssociation = BinaryAssociation(
    name="in_10",
    ends={
        Property(name="petrinetmodel_Place12", type=petrinetmodel_EdgeToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetmodel_EdgeToPlace11", type=petrinetmodel_Place, multiplicity=Multiplicity(1, 1))
    }
)
in_13: BinaryAssociation = BinaryAssociation(
    name="in_13",
    ends={
        Property(name="petrinetmodel_Transition15", type=petrinetmodel_EdgeToTransaction, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetmodel_EdgeToTransaction14", type=petrinetmodel_Transition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petrinetmodel_EdgeToPlace_Edge = Generalization(general=Edge, specific=petrinetmodel_EdgeToPlace)
gen_petrinetmodel_EdgeToTransaction_Edge = Generalization(general=Edge, specific=petrinetmodel_EdgeToTransaction)

# Domain Model
domain_model = DomainModel(
    name="petrinetmodel",
    types={petrinetmodel_Petrinet, petrinetmodel_Transition, petrinetmodel_Place, petrinetmodel_EdgeToPlace, petrinetmodel_EdgeToTransaction, Edge, petrinetmodel_Edge},
    associations={transitions0, places1, out3, inputPlaces5, out8, in_10, in_13},
    generalizations={gen_petrinetmodel_EdgeToPlace_Edge, gen_petrinetmodel_EdgeToTransaction_Edge},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
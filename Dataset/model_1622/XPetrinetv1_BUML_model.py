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
petrinetv1_Net = Class(name="petrinetv1::Net")
petrinetv1_Place = Class(name="petrinetv1::Place")
petrinetv1_Transition = Class(name="petrinetv1::Transition")

# petrinetv1_Net class attributes and methods
petrinetv1_Net_m_initialize: Method = Method(name="initialize", parameters={Parameter(name='args')})
petrinetv1_Net_m_markingToString: Method = Method(name="markingToString", parameters={})
petrinetv1_Net_m_run: Method = Method(name="run", parameters={})
petrinetv1_Net.methods={petrinetv1_Net_m_run, petrinetv1_Net_m_initialize, petrinetv1_Net_m_markingToString}

# petrinetv1_Place class attributes and methods
petrinetv1_Place_name: Property = Property(name="name", type=StringType)
petrinetv1_Place_initialTokens: Property = Property(name="initialTokens", type=IntegerType)
petrinetv1_Place_tokens: Property = Property(name="tokens", type=IntegerType)
petrinetv1_Place.attributes={petrinetv1_Place_name, petrinetv1_Place_tokens, petrinetv1_Place_initialTokens}

# petrinetv1_Transition class attributes and methods
petrinetv1_Transition_name: Property = Property(name="name", type=StringType)
petrinetv1_Transition_m_isEnabled: Method = Method(name="isEnabled", parameters={})
petrinetv1_Transition_m_fire: Method = Method(name="fire", parameters={})
petrinetv1_Transition.attributes={petrinetv1_Transition_name}
petrinetv1_Transition.methods={petrinetv1_Transition_m_fire, petrinetv1_Transition_m_isEnabled}

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="petrinetv1_Place", type=petrinetv1_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv1_Net", type=petrinetv1_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="petrinetv1_Transition", type=petrinetv1_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv1_Net2", type=petrinetv1_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input3: BinaryAssociation = BinaryAssociation(
    name="input3",
    ends={
        Property(name="petrinetv1_Place5", type=petrinetv1_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv1_Transition4", type=petrinetv1_Place, multiplicity=Multiplicity(1, 9999))
    }
)
output6: BinaryAssociation = BinaryAssociation(
    name="output6",
    ends={
        Property(name="petrinetv1_Place8", type=petrinetv1_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv1_Transition7", type=petrinetv1_Place, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="petrinetv1",
    types={petrinetv1_Net, petrinetv1_Place, petrinetv1_Transition},
    associations={places0, transitions1, input3, output6},
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
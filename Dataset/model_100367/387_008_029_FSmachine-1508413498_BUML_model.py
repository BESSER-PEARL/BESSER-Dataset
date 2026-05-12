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
FSmachine_AbstractConection = Class(name="FSmachine_AbstractConection")
FSmachine_Root = Class(name="FSmachine_Root")
FSmachine_AbstractObject = Class(name="FSmachine_AbstractObject")
FSmachine_TimeConnection = Class(name="FSmachine_TimeConnection")
FSmachine_State = Class(name="FSmachine_State")
AbstractObject = Class(name="AbstractObject")
FSmachine_ReasonConnection = Class(name="FSmachine_ReasonConnection")
AbstractConection = Class(name="AbstractConection")

# FSmachine_AbstractConection class attributes and methods
FSmachine_AbstractConection_name: Property = Property(name="name", type=StringType)
FSmachine_AbstractConection.attributes={FSmachine_AbstractConection_name}

# FSmachine_Root class attributes and methods
FSmachine_Root_FSmachineName: Property = Property(name="FSmachineName", type=StringType)
FSmachine_Root.attributes={FSmachine_Root_FSmachineName}

# FSmachine_AbstractObject class attributes and methods
FSmachine_AbstractObject_name: Property = Property(name="name", type=StringType)
FSmachine_AbstractObject_active: Property = Property(name="active", type=BooleanType)
FSmachine_AbstractObject_m_checkStatussen: Method = Method(name="checkStatussen", parameters={}, type=BooleanType)
FSmachine_AbstractObject_m_makeMeActive: Method = Method(name="makeMeActive", parameters={})
FSmachine_AbstractObject.attributes={FSmachine_AbstractObject_name, FSmachine_AbstractObject_active}
FSmachine_AbstractObject.methods={FSmachine_AbstractObject_m_makeMeActive, FSmachine_AbstractObject_m_checkStatussen}

# FSmachine_TimeConnection class attributes and methods
FSmachine_TimeConnection_when: Property = Property(name="when", type=StringType)
FSmachine_TimeConnection.attributes={FSmachine_TimeConnection_when}

# FSmachine_State class attributes and methods
FSmachine_State_description: Property = Property(name="description", type=StringType)
FSmachine_State_data: Property = Property(name="data", type=StringType)
FSmachine_State.attributes={FSmachine_State_data, FSmachine_State_description}

# AbstractObject class attributes and methods

# FSmachine_ReasonConnection class attributes and methods
FSmachine_ReasonConnection_reason: Property = Property(name="reason", type=StringType)
FSmachine_ReasonConnection.attributes={FSmachine_ReasonConnection_reason}

# AbstractConection class attributes and methods

# Relationships
connections1: BinaryAssociation = BinaryAssociation(
    name="connections1",
    ends={
        Property(name="AbstractConection", type=FSmachine_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="par", type=FSmachine_AbstractConection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objects0: BinaryAssociation = BinaryAssociation(
    name="objects0",
    ends={
        Property(name="AbstractObject", type=FSmachine_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=FSmachine_AbstractObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conParent5: BinaryAssociation = BinaryAssociation(
    name="conParent5",
    ends={
        Property(name="AbstractConection6", type=FSmachine_AbstractObject, multiplicity=Multiplicity(1, 1)),
        Property(name="prev", type=FSmachine_AbstractConection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent2: BinaryAssociation = BinaryAssociation(
    name="parent2",
    ends={
        Property(name="Root", type=FSmachine_AbstractObject, multiplicity=Multiplicity(1, 1)),
        Property(name="objects", type=FSmachine_Root, multiplicity=Multiplicity(0, 1))
    }
)
conChild3: BinaryAssociation = BinaryAssociation(
    name="conChild3",
    ends={
        Property(name="AbstractConection4", type=FSmachine_AbstractObject, multiplicity=Multiplicity(1, 1)),
        Property(name="next", type=FSmachine_AbstractConection, multiplicity=Multiplicity(0, 1))
    }
)
par7: BinaryAssociation = BinaryAssociation(
    name="par7",
    ends={
        Property(name="Root8", type=FSmachine_AbstractConection, multiplicity=Multiplicity(1, 1)),
        Property(name="connections", type=FSmachine_Root, multiplicity=Multiplicity(0, 1))
    }
)
next9: BinaryAssociation = BinaryAssociation(
    name="next9",
    ends={
        Property(name="AbstractObject10", type=FSmachine_AbstractConection, multiplicity=Multiplicity(1, 1)),
        Property(name="conChild", type=FSmachine_AbstractObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
prev11: BinaryAssociation = BinaryAssociation(
    name="prev11",
    ends={
        Property(name="AbstractObject12", type=FSmachine_AbstractConection, multiplicity=Multiplicity(1, 1)),
        Property(name="conParent", type=FSmachine_AbstractObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_FSmachine_TimeConnection_AbstractConection = Generalization(general=AbstractConection, specific=FSmachine_TimeConnection)
gen_FSmachine_State_AbstractObject = Generalization(general=AbstractObject, specific=FSmachine_State)
gen_FSmachine_ReasonConnection_AbstractConection = Generalization(general=AbstractConection, specific=FSmachine_ReasonConnection)

# Domain Model
domain_model = DomainModel(
    name="FSmachine",
    types={FSmachine_AbstractConection, FSmachine_Root, FSmachine_AbstractObject, FSmachine_TimeConnection, FSmachine_State, AbstractObject, FSmachine_ReasonConnection, AbstractConection},
    associations={connections1, objects0, conParent5, parent2, conChild3, par7, next9, prev11},
    generalizations={gen_FSmachine_TimeConnection_AbstractConection, gen_FSmachine_State_AbstractObject, gen_FSmachine_ReasonConnection_AbstractConection},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
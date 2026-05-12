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
unql_Program = Class(name="unql_Program")
unql_Definition = Class(name="unql_Definition")
unql_Connection = Class(name="unql_Connection")
unql_Select = Class(name="unql_Select")

# unql_Program class attributes and methods

# unql_Definition class attributes and methods
unql_Definition_name: Property = Property(name="name", type=StringType)
unql_Definition_type: Property = Property(name="type", type=StringType)
unql_Definition.attributes={unql_Definition_type, unql_Definition_name}

# unql_Connection class attributes and methods
unql_Connection_name: Property = Property(name="name", type=StringType)
unql_Connection_url: Property = Property(name="url", type=StringType)
unql_Connection_username: Property = Property(name="username", type=StringType)
unql_Connection_password: Property = Property(name="password", type=StringType)
unql_Connection.attributes={unql_Connection_name, unql_Connection_username, unql_Connection_password, unql_Connection_url}

# unql_Select class attributes and methods
unql_Select_relations: Property = Property(name="relations", type=StringType)
unql_Select_conditions: Property = Property(name="conditions", type=StringType)
unql_Select_attributes: Property = Property(name="attributes", type=StringType)
unql_Select.attributes={unql_Select_relations, unql_Select_attributes, unql_Select_conditions}

# Relationships
definitions0: BinaryAssociation = BinaryAssociation(
    name="definitions0",
    ends={
        Property(name="unql_Definition", type=unql_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="unql_Program", type=unql_Definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections1: BinaryAssociation = BinaryAssociation(
    name="connections1",
    ends={
        Property(name="unql_Connection", type=unql_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="unql_Program2", type=unql_Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
queries3: BinaryAssociation = BinaryAssociation(
    name="queries3",
    ends={
        Property(name="unql_Select", type=unql_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="unql_Program4", type=unql_Select, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="unql",
    types={unql_Program, unql_Definition, unql_Connection, unql_Select},
    associations={definitions0, connections1, queries3},
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
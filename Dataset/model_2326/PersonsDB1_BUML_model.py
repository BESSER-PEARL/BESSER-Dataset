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
pdb1_Person = Class(name="pdb1::Person")
pdb1_Database = Class(name="pdb1::Database")

# pdb1_Person class attributes and methods
pdb1_Person_firstName: Property = Property(name="firstName", type=StringType)
pdb1_Person_lastName: Property = Property(name="lastName", type=StringType)
pdb1_Person_birthday: Property = Property(name="birthday", type=StringType)
pdb1_Person_placeOfBirth: Property = Property(name="placeOfBirth", type=StringType)
pdb1_Person_id: Property = Property(name="id", type=StringType)
pdb1_Person_incrementalID: Property = Property(name="incrementalID", type=StringType)
pdb1_Person.attributes={pdb1_Person_firstName, pdb1_Person_birthday, pdb1_Person_placeOfBirth, pdb1_Person_id, pdb1_Person_incrementalID, pdb1_Person_lastName}

# pdb1_Database class attributes and methods
pdb1_Database_name: Property = Property(name="name", type=StringType)
pdb1_Database.attributes={pdb1_Database_name}

# Relationships
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="Person", type=pdb1_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="database", type=pdb1_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
database1: BinaryAssociation = BinaryAssociation(
    name="database1",
    ends={
        Property(name="Database", type=pdb1_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="persons", type=pdb1_Database, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="pdb1",
    types={pdb1_Person, pdb1_Database},
    associations={persons0, database1},
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
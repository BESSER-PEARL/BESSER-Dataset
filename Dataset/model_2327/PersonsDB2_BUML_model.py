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
pdb2_Database = Class(name="pdb2::Database")
pdb2_Person = Class(name="pdb2::Person")

# pdb2_Database class attributes and methods
pdb2_Database_name: Property = Property(name="name", type=StringType)
pdb2_Database.attributes={pdb2_Database_name}

# pdb2_Person class attributes and methods
pdb2_Person_name: Property = Property(name="name", type=StringType)
pdb2_Person_birthday: Property = Property(name="birthday", type=StringType)
pdb2_Person_placeOfBirth: Property = Property(name="placeOfBirth", type=StringType)
pdb2_Person_id: Property = Property(name="id", type=StringType)
pdb2_Person_incrementalID: Property = Property(name="incrementalID", type=StringType)
pdb2_Person.attributes={pdb2_Person_placeOfBirth, pdb2_Person_incrementalID, pdb2_Person_name, pdb2_Person_birthday, pdb2_Person_id}

# Relationships
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="Person", type=pdb2_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="database", type=pdb2_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
database1: BinaryAssociation = BinaryAssociation(
    name="database1",
    ends={
        Property(name="Database", type=pdb2_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="persons", type=pdb2_Database, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="pdb2",
    types={pdb2_Database, pdb2_Person},
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
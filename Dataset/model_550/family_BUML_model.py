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
family_Man = Class(name="family::Man")
family_Family = Class(name="family::Family")
family_Person = Class(name="family::Person", is_abstract=True)
Person = Class(name="Person")
family_Woman = Class(name="family::Woman")

# family_Man class attributes and methods

# family_Family class attributes and methods
family_Family_name: Property = Property(name="name", type=StringType)
family_Family.attributes={family_Family_name}

# family_Person class attributes and methods
family_Person_name: Property = Property(name="name", type=StringType)
family_Person_eCivil: Property = Property(name="eCivil", type=StringType)
family_Person_provincia: Property = Property(name="provincia", type=StringType)
family_Person_fechaNacimiento: Property = Property(name="fechaNacimiento", type=StringType)
family_Person.attributes={family_Person_name, family_Person_provincia, family_Person_eCivil, family_Person_fechaNacimiento}

# Person class attributes and methods

# family_Woman class attributes and methods

# Relationships
father1: BinaryAssociation = BinaryAssociation(
    name="father1",
    ends={
        Property(name="family_Man", type=family_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Person2", type=family_Man, multiplicity=Multiplicity(0, 1))
    }
)
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="family_Person", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Family", type=family_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mother3: BinaryAssociation = BinaryAssociation(
    name="mother3",
    ends={
        Property(name="family_Woman", type=family_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Person4", type=family_Woman, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_family_Man_Person = Generalization(general=Person, specific=family_Man)
gen_family_Woman_Person = Generalization(general=Person, specific=family_Woman)

# Domain Model
domain_model = DomainModel(
    name="family",
    types={family_Man, family_Family, family_Person, Person, family_Woman},
    associations={father1, members0, mother3},
    generalizations={gen_family_Man_Person, gen_family_Woman_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
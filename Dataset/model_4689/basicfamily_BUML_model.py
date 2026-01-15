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
basicfamily_Family = Class(name="basicfamily::Family")
basicfamily_Person = Class(name="basicfamily::Person")
basicfamily_Relation = Class(name="basicfamily::Relation")
basicfamily_Woman = Class(name="basicfamily::Woman")
basicfamily_Man = Class(name="basicfamily::Man")
Person = Class(name="Person")

# basicfamily_Family class attributes and methods
basicfamily_Family_name: Property = Property(name="name", type=StringType)
basicfamily_Family.attributes={basicfamily_Family_name}

# basicfamily_Person class attributes and methods
basicfamily_Person_name: Property = Property(name="name", type=StringType)
basicfamily_Person_birthDate: Property = Property(name="birthDate", type=DateType)
basicfamily_Person.attributes={basicfamily_Person_name, basicfamily_Person_birthDate}

# basicfamily_Relation class attributes and methods
basicfamily_Relation_description: Property = Property(name="description", type=StringType)
basicfamily_Relation.attributes={basicfamily_Relation_description}

# basicfamily_Woman class attributes and methods

# basicfamily_Man class attributes and methods

# Person class attributes and methods

# Relationships
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="basicfamily_Person", type=basicfamily_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="basicfamily_Family", type=basicfamily_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="basicfamily_Relation", type=basicfamily_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="basicfamily_Family2", type=basicfamily_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parents4: BinaryAssociation = BinaryAssociation(
    name="parents4",
    ends={
        Property(name="Person", type=basicfamily_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=basicfamily_Person, multiplicity=Multiplicity(0, 2))
    }
)
children6: BinaryAssociation = BinaryAssociation(
    name="children6",
    ends={
        Property(name="Person7", type=basicfamily_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="parents", type=basicfamily_Person, multiplicity=Multiplicity(0, 9999))
    }
)
mother8: BinaryAssociation = BinaryAssociation(
    name="mother8",
    ends={
        Property(name="basicfamily_Woman", type=basicfamily_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="basicfamily_Person9", type=basicfamily_Woman, multiplicity=Multiplicity(0, 1))
    }
)
father10: BinaryAssociation = BinaryAssociation(
    name="father10",
    ends={
        Property(name="basicfamily_Man", type=basicfamily_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="basicfamily_Person11", type=basicfamily_Man, multiplicity=Multiplicity(0, 1))
    }
)
relations12: BinaryAssociation = BinaryAssociation(
    name="relations12",
    ends={
        Property(name="basicfamily_Relation14", type=basicfamily_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="basicfamily_Person13", type=basicfamily_Relation, multiplicity=Multiplicity(0, 9999))
    }
)
personA15: BinaryAssociation = BinaryAssociation(
    name="personA15",
    ends={
        Property(name="basicfamily_Person17", type=basicfamily_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="basicfamily_Relation16", type=basicfamily_Person, multiplicity=Multiplicity(1, 1))
    }
)
personB18: BinaryAssociation = BinaryAssociation(
    name="personB18",
    ends={
        Property(name="basicfamily_Person20", type=basicfamily_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="basicfamily_Relation19", type=basicfamily_Person, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_basicfamily_Man_Person = Generalization(general=Person, specific=basicfamily_Man)
gen_basicfamily_Woman_Person = Generalization(general=Person, specific=basicfamily_Woman)

# Domain Model
domain_model = DomainModel(
    name="basicfamily",
    types={basicfamily_Family, basicfamily_Person, basicfamily_Relation, basicfamily_Woman, basicfamily_Man, Person},
    associations={members0, relations1, parents4, children6, mother8, father10, relations12, personA15, personB18},
    generalizations={gen_basicfamily_Man_Person, gen_basicfamily_Woman_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
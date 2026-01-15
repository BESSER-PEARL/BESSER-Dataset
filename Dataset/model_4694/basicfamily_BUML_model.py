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
Person = Class(name="Person")
basicfamily_Family = Class(name="basicfamily::Family")
basicfamily_Person = Class(name="basicfamily::Person", is_abstract=True)
basicfamily_Man = Class(name="basicfamily::Man")
basicfamily_Woman = Class(name="basicfamily::Woman")

# Person class attributes and methods

# basicfamily_Family class attributes and methods
basicfamily_Family_name: Property = Property(name="name", type=StringType)
basicfamily_Family.attributes={basicfamily_Family_name}

# basicfamily_Person class attributes and methods
basicfamily_Person_name: Property = Property(name="name", type=StringType)
basicfamily_Person.attributes={basicfamily_Person_name}

# basicfamily_Man class attributes and methods

# basicfamily_Woman class attributes and methods

# Relationships
parents8: BinaryAssociation = BinaryAssociation(
    name="parents8",
    ends={
        Property(name="Person9", type=basicfamily_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=basicfamily_Person, multiplicity=Multiplicity(0, 2))
    }
)
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="basicfamily_Person", type=basicfamily_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="basicfamily_Family", type=basicfamily_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
father1: BinaryAssociation = BinaryAssociation(
    name="father1",
    ends={
        Property(name="basicfamily_Man", type=basicfamily_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="basicfamily_Person2", type=basicfamily_Man, multiplicity=Multiplicity(0, 1))
    }
)
mother3: BinaryAssociation = BinaryAssociation(
    name="mother3",
    ends={
        Property(name="basicfamily_Woman", type=basicfamily_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="basicfamily_Person4", type=basicfamily_Woman, multiplicity=Multiplicity(0, 1))
    }
)
children6: BinaryAssociation = BinaryAssociation(
    name="children6",
    ends={
        Property(name="Person", type=basicfamily_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="parents", type=basicfamily_Person, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_basicfamily_Man_Person = Generalization(general=Person, specific=basicfamily_Man)
gen_basicfamily_Woman_Person = Generalization(general=Person, specific=basicfamily_Woman)

# Domain Model
domain_model = DomainModel(
    name="basicfamily",
    types={Person, basicfamily_Family, basicfamily_Person, basicfamily_Man, basicfamily_Woman},
    associations={parents8, members0, father1, mother3, children6},
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
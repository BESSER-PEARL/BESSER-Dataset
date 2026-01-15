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
basicfamily_Person = Class(name="basicfamily::Person", is_abstract=True)
basicfamily_Woman = Class(name="basicfamily::Woman")
basicfamily_Man = Class(name="basicfamily::Man")
Person = Class(name="Person")
basicfamily_Family = Class(name="basicfamily::Family")

# basicfamily_Person class attributes and methods
basicfamily_Person_name: Property = Property(name="name", type=StringType)
basicfamily_Person.attributes={basicfamily_Person_name}

# basicfamily_Woman class attributes and methods

# basicfamily_Man class attributes and methods

# Person class attributes and methods

# basicfamily_Family class attributes and methods
basicfamily_Family_name: Property = Property(name="name", type=StringType)
basicfamily_Family.attributes={basicfamily_Family_name}

# Relationships
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="basicfamily_Person", type=basicfamily_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="basicfamily_Family", type=basicfamily_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parents2: BinaryAssociation = BinaryAssociation(
    name="parents2",
    ends={
        Property(name="Person", type=basicfamily_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=basicfamily_Person, multiplicity=Multiplicity(0, 2))
    }
)
children4: BinaryAssociation = BinaryAssociation(
    name="children4",
    ends={
        Property(name="Person5", type=basicfamily_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="parents", type=basicfamily_Person, multiplicity=Multiplicity(0, 9999))
    }
)
mother6: BinaryAssociation = BinaryAssociation(
    name="mother6",
    ends={
        Property(name="basicfamily_Woman", type=basicfamily_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="basicfamily_Person7", type=basicfamily_Woman, multiplicity=Multiplicity(0, 1))
    }
)
father8: BinaryAssociation = BinaryAssociation(
    name="father8",
    ends={
        Property(name="basicfamily_Man", type=basicfamily_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="basicfamily_Person9", type=basicfamily_Man, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_basicfamily_Man_Person = Generalization(general=Person, specific=basicfamily_Man)
gen_basicfamily_Woman_Person = Generalization(general=Person, specific=basicfamily_Woman)

# Domain Model
domain_model = DomainModel(
    name="basicfamily",
    types={basicfamily_Person, basicfamily_Woman, basicfamily_Man, Person, basicfamily_Family},
    associations={members0, parents2, children4, mother6, father8},
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
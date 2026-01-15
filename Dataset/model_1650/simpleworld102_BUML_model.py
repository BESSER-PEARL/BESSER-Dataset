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
simpleworld102_Person = Class(name="simpleworld102::Person")
simpleworld102_Relations = Class(name="simpleworld102::Relations")
simpleworld102_Element = Class(name="simpleworld102::Element")
simpleworld102_Thing = Class(name="simpleworld102::Thing")
Named = Class(name="Named")
simpleworld102_Part = Class(name="simpleworld102::Part")
simpleworld102_World = Class(name="simpleworld102::World")
simpleworld102_Named = Class(name="simpleworld102::Named", is_abstract=True)

# simpleworld102_Person class attributes and methods
simpleworld102_Person_name: Property = Property(name="name", type=StringType)
simpleworld102_Person_foreName: Property = Property(name="foreName", type=StringType)
simpleworld102_Person.attributes={simpleworld102_Person_foreName, simpleworld102_Person_name}

# simpleworld102_Relations class attributes and methods
simpleworld102_Relations_since: Property = Property(name="since", type=IntegerType)
simpleworld102_Relations.attributes={simpleworld102_Relations_since}

# simpleworld102_Element class attributes and methods
simpleworld102_Element_description: Property = Property(name="description", type=StringType)
simpleworld102_Element.attributes={simpleworld102_Element_description}

# simpleworld102_Thing class attributes and methods

# Named class attributes and methods

# simpleworld102_Part class attributes and methods
simpleworld102_Part_content: Property = Property(name="content", type=StringType)
simpleworld102_Part_id: Property = Property(name="id", type=IntegerType)
simpleworld102_Part.attributes={simpleworld102_Part_id, simpleworld102_Part_content}

# simpleworld102_World class attributes and methods

# simpleworld102_Named class attributes and methods
simpleworld102_Named_name: Property = Property(name="name", type=StringType)
simpleworld102_Named.attributes={simpleworld102_Named_name}

# Relationships
components6: BinaryAssociation = BinaryAssociation(
    name="components6",
    ends={
        Property(name="simpleworld102_Thing7", type=simpleworld102_Part, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="simpleworld102_Part", type=simpleworld102_Thing, multiplicity=Multiplicity(1, 1))
    }
)
persons8: BinaryAssociation = BinaryAssociation(
    name="persons8",
    ends={
        Property(name="Person", type=simpleworld102_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="things", type=simpleworld102_Person, multiplicity=Multiplicity(0, 9999))
    }
)
parent10: BinaryAssociation = BinaryAssociation(
    name="parent10",
    ends={
        Property(name="simpleworld102_Thing11", type=simpleworld102_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleworld102_Thing9", type=simpleworld102_Thing, multiplicity=Multiplicity(0, 1))
    }
)
relations0: BinaryAssociation = BinaryAssociation(
    name="relations0",
    ends={
        Property(name="simpleworld102_Relations", type=simpleworld102_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleworld102_Person", type=simpleworld102_Relations, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="simpleworld102_Element", type=simpleworld102_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleworld102_Person2", type=simpleworld102_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thing3: BinaryAssociation = BinaryAssociation(
    name="thing3",
    ends={
        Property(name="simpleworld102_Thing", type=simpleworld102_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleworld102_Person4", type=simpleworld102_Thing, multiplicity=Multiplicity(0, 1))
    }
)
things5: BinaryAssociation = BinaryAssociation(
    name="things5",
    ends={
        Property(name="Thing", type=simpleworld102_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="persons", type=simpleworld102_Thing, multiplicity=Multiplicity(0, 9999))
    }
)
parts12: BinaryAssociation = BinaryAssociation(
    name="parts12",
    ends={
        Property(name="simpleworld102_Part14", type=simpleworld102_Relations, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleworld102_Relations13", type=simpleworld102_Part, multiplicity=Multiplicity(0, 1))
    }
)
persons15: BinaryAssociation = BinaryAssociation(
    name="persons15",
    ends={
        Property(name="simpleworld102_Person16", type=simpleworld102_World, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleworld102_World", type=simpleworld102_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
things17: BinaryAssociation = BinaryAssociation(
    name="things17",
    ends={
        Property(name="simpleworld102_Thing19", type=simpleworld102_World, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleworld102_World18", type=simpleworld102_Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_simpleworld102_Part_Named = Generalization(general=Named, specific=simpleworld102_Part)
gen_simpleworld102_Thing_Named = Generalization(general=Named, specific=simpleworld102_Thing)
gen_simpleworld102_World_Named = Generalization(general=Named, specific=simpleworld102_World)

# Domain Model
domain_model = DomainModel(
    name="simpleworld102",
    types={simpleworld102_Person, simpleworld102_Relations, simpleworld102_Element, simpleworld102_Thing, Named, simpleworld102_Part, simpleworld102_World, simpleworld102_Named},
    associations={components6, persons8, parent10, relations0, elements1, thing3, things5, parts12, persons15, things17},
    generalizations={gen_simpleworld102_Part_Named, gen_simpleworld102_Thing_Named, gen_simpleworld102_World_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
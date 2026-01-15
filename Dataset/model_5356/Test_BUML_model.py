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
test_Container = Class(name="test::Container")
test_Foo = Class(name="test::Foo")
test_Bar = Class(name="test::Bar")

# test_Container class attributes and methods

# test_Foo class attributes and methods
test_Foo_fooA: Property = Property(name="fooA", type=StringType)
test_Foo.attributes={test_Foo_fooA}

# test_Bar class attributes and methods
test_Bar_barA: Property = Property(name="barA", type=StringType)
test_Bar.attributes={test_Bar_barA}

# Relationships
fooz0: BinaryAssociation = BinaryAssociation(
    name="fooz0",
    ends={
        Property(name="test_Foo", type=test_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="test_Container", type=test_Foo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
barz1: BinaryAssociation = BinaryAssociation(
    name="barz1",
    ends={
        Property(name="test_Bar", type=test_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="test_Container2", type=test_Bar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foos3: BinaryAssociation = BinaryAssociation(
    name="foos3",
    ends={
        Property(name="test_Foo5", type=test_Bar, multiplicity=Multiplicity(1, 1)),
        Property(name="test_Bar4", type=test_Foo, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_Container, test_Foo, test_Bar},
    associations={fooz0, barz1, foos3},
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
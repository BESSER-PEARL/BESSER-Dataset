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
c_AbstractClass = Class(name="c::AbstractClass", is_abstract=True)
c_Foo = Class(name="c::Foo")
AbstractClass = Class(name="AbstractClass")
c_Bar = Class(name="c::Bar")
Foo = Class(name="Foo")

# c_AbstractClass class attributes and methods
c_AbstractClass_name: Property = Property(name="name", type=StringType)
c_AbstractClass.attributes={c_AbstractClass_name}

# c_Foo class attributes and methods
c_Foo_description: Property = Property(name="description", type=StringType)
c_Foo.attributes={c_Foo_description}

# AbstractClass class attributes and methods

# c_Bar class attributes and methods
c_Bar_value: Property = Property(name="value", type=StringType)
c_Bar.attributes={c_Bar_value}

# Foo class attributes and methods

# Relationships
bar0: BinaryAssociation = BinaryAssociation(
    name="bar0",
    ends={
        Property(name="c_Bar", type=c_Foo, multiplicity=Multiplicity(1, 1)),
        Property(name="c_Foo", type=c_Bar, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foos1: BinaryAssociation = BinaryAssociation(
    name="foos1",
    ends={
        Property(name="c_Foo3", type=c_Bar, multiplicity=Multiplicity(1, 1)),
        Property(name="c_Bar2", type=c_Foo, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_c_Foo_AbstractClass = Generalization(general=AbstractClass, specific=c_Foo)
gen_c_Bar_Foo = Generalization(general=Foo, specific=c_Bar)

# Domain Model
domain_model = DomainModel(
    name="c",
    types={c_AbstractClass, c_Foo, AbstractClass, c_Bar, Foo},
    associations={bar0, foos1},
    generalizations={gen_c_Foo_AbstractClass, gen_c_Bar_Foo},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
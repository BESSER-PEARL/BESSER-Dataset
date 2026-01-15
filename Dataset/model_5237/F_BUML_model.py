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
f_X = Class(name="f::X")
f_Y = Class(name="f::Y")

# f_X class attributes and methods
f_X_m_foo: Method = Method(name="foo", parameters={})
f_X.methods={f_X_m_foo}

# f_Y class attributes and methods
f_Y_a: Property = Property(name="a", type=StringType)
f_Y.attributes={f_Y_a}

# Relationships
ys0: BinaryAssociation = BinaryAssociation(
    name="ys0",
    ends={
        Property(name="f_Y", type=f_X, multiplicity=Multiplicity(1, 1)),
        Property(name="f_X", type=f_Y, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="f",
    types={f_X, f_Y},
    associations={ys0},
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
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
opposite2_Root = Class(name="opposite2::Root")
opposite2_EndA = Class(name="opposite2::EndA")
opposite2_ConcreteEndB1 = Class(name="opposite2::ConcreteEndB1")
AbstractClassB = Class(name="AbstractClassB")
opposite2_ConcreteEndB2 = Class(name="opposite2::ConcreteEndB2")
opposite2_AbstractClassB = Class(name="opposite2::AbstractClassB", is_abstract=True)

# opposite2_Root class attributes and methods

# opposite2_EndA class attributes and methods

# opposite2_ConcreteEndB1 class attributes and methods

# AbstractClassB class attributes and methods

# opposite2_ConcreteEndB2 class attributes and methods

# opposite2_AbstractClassB class attributes and methods

# Relationships
theAs0: BinaryAssociation = BinaryAssociation(
    name="theAs0",
    ends={
        Property(name="opposite2_EndA", type=opposite2_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="opposite2_Root", type=opposite2_EndA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
theBs1: BinaryAssociation = BinaryAssociation(
    name="theBs1",
    ends={
        Property(name="opposite2_AbstractClassB", type=opposite2_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="opposite2_Root2", type=opposite2_AbstractClassB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toA3: BinaryAssociation = BinaryAssociation(
    name="toA3",
    ends={
        Property(name="EndA", type=opposite2_AbstractClassB, multiplicity=Multiplicity(1, 1)),
        Property(name="toB", type=opposite2_EndA, multiplicity=Multiplicity(0, 9999))
    }
)
toB4: BinaryAssociation = BinaryAssociation(
    name="toB4",
    ends={
        Property(name="AbstractClassB", type=opposite2_EndA, multiplicity=Multiplicity(1, 1)),
        Property(name="toA", type=opposite2_AbstractClassB, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_opposite2_ConcreteEndB1_AbstractClassB = Generalization(general=AbstractClassB, specific=opposite2_ConcreteEndB1)
gen_opposite2_ConcreteEndB2_AbstractClassB = Generalization(general=AbstractClassB, specific=opposite2_ConcreteEndB2)

# Domain Model
domain_model = DomainModel(
    name="opposite2",
    types={opposite2_Root, opposite2_EndA, opposite2_ConcreteEndB1, AbstractClassB, opposite2_ConcreteEndB2, opposite2_AbstractClassB},
    associations={theAs0, theBs1, toA3, toB4},
    generalizations={gen_opposite2_ConcreteEndB1_AbstractClassB, gen_opposite2_ConcreteEndB2_AbstractClassB},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
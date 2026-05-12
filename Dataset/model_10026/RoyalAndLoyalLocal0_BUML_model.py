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
RoyalAndLoyal_Container_RandL = Class(name="RoyalAndLoyal_Container_RandL")
RoyalAndLoyal_Customer = Class(name="RoyalAndLoyal_Customer")

# RoyalAndLoyal_Container_RandL class attributes and methods

# RoyalAndLoyal_Customer class attributes and methods
RoyalAndLoyal_Customer_name: Property = Property(name="name", type=StringType)
RoyalAndLoyal_Customer_m_updateName: Method = Method(name="updateName", parameters={Parameter(name='RoyalAndLoyal_name', type=StringType)})
RoyalAndLoyal_Customer.attributes={RoyalAndLoyal_Customer_name}
RoyalAndLoyal_Customer.methods={RoyalAndLoyal_Customer_m_updateName}

# Relationships
ref_RandL_Customer0: BinaryAssociation = BinaryAssociation(
    name="ref_RandL_Customer0",
    ends={
        Property(name="RoyalAndLoyal_Customer", type=RoyalAndLoyal_Container_RandL, multiplicity=Multiplicity(1, 1)),
        Property(name="RoyalAndLoyal_Container_RandL", type=RoyalAndLoyal_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)


# OCL Constraints
invariant_UniqueName: Constraint = Constraint(
    name="invariant_UniqueName",
    context=RoyalAndLoyal_Customer,
    expression="context Customer inv: Customer.allInstances()->forAll(c1, c2 : Customer| c1.name = c2.name implies c1 = c2)",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="RoyalAndLoyal",
    types={RoyalAndLoyal_Container_RandL, RoyalAndLoyal_Customer},
    associations={ref_RandL_Customer0},
    constraints={invariant_UniqueName},
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
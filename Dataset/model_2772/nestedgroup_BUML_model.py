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
nestedgroup_A = Class(name="nestedgroup::A")
nestedgroup_CType = Class(name="nestedgroup::CType")
nestedgroup_Element = Class(name="nestedgroup::Element")

# nestedgroup_A class attributes and methods
nestedgroup_A_group: Property = Property(name="group", type=StringType)
nestedgroup_A_b: Property = Property(name="b", type=StringType)
nestedgroup_A_name: Property = Property(name="name", type=StringType)
nestedgroup_A.attributes={nestedgroup_A_group, nestedgroup_A_name, nestedgroup_A_b}

# nestedgroup_CType class attributes and methods
nestedgroup_CType_cname: Property = Property(name="cname", type=StringType)
nestedgroup_CType_cvalue: Property = Property(name="cvalue", type=StringType)
nestedgroup_CType.attributes={nestedgroup_CType_cvalue, nestedgroup_CType_cname}

# nestedgroup_Element class attributes and methods
nestedgroup_Element_mixed: Property = Property(name="mixed", type=StringType)
nestedgroup_Element_name: Property = Property(name="name", type=StringType)
nestedgroup_Element_true: Property = Property(name="true", type=StringType)
nestedgroup_Element.attributes={nestedgroup_Element_true, nestedgroup_Element_mixed, nestedgroup_Element_name}

# Relationships
c0: BinaryAssociation = BinaryAssociation(
    name="c0",
    ends={
        Property(name="nestedgroup_CType", type=nestedgroup_A, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedgroup_A", type=nestedgroup_CType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c1: BinaryAssociation = BinaryAssociation(
    name="c1",
    ends={
        Property(name="nestedgroup_CType2", type=nestedgroup_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedgroup_Element", type=nestedgroup_CType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
recursive4: BinaryAssociation = BinaryAssociation(
    name="recursive4",
    ends={
        Property(name="nestedgroup_Element5", type=nestedgroup_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedgroup_Element3", type=nestedgroup_Element, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="nestedgroup",
    types={nestedgroup_A, nestedgroup_CType, nestedgroup_Element},
    associations={c0, c1, recursive4},
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
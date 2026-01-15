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
ChangingOverTime_TimeStampedElement = Class(name="ChangingOverTime::TimeStampedElement")
ChangingOverTime_Tree = Class(name="ChangingOverTime::Tree")
ChangingOverTime_NodeKind = Class(name="ChangingOverTime::NodeKind")
ChangingOverTime_LinkKind = Class(name="ChangingOverTime::LinkKind")
TimeStampedElement = Class(name="TimeStampedElement")
ChangingOverTime_BindingKind = Class(name="ChangingOverTime::BindingKind")
ChangingOverTime_Entity = Class(name="ChangingOverTime::Entity")

# ChangingOverTime_TimeStampedElement class attributes and methods
ChangingOverTime_TimeStampedElement_effectiveDate: Property = Property(name="effectiveDate", type=DateType)
ChangingOverTime_TimeStampedElement_expirationDate: Property = Property(name="expirationDate", type=DateType)
ChangingOverTime_TimeStampedElement.attributes={ChangingOverTime_TimeStampedElement_expirationDate, ChangingOverTime_TimeStampedElement_effectiveDate}

# ChangingOverTime_Tree class attributes and methods

# ChangingOverTime_NodeKind class attributes and methods

# ChangingOverTime_LinkKind class attributes and methods

# TimeStampedElement class attributes and methods

# ChangingOverTime_BindingKind class attributes and methods

# ChangingOverTime_Entity class attributes and methods

# Relationships
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="NodeKind", type=ChangingOverTime_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="tree", type=ChangingOverTime_NodeKind, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parent5: BinaryAssociation = BinaryAssociation(
    name="parent5",
    ends={
        Property(name="ChangingOverTime_NodeKind6", type=ChangingOverTime_LinkKind, multiplicity=Multiplicity(1, 1)),
        Property(name="ChangingOverTime_LinkKind", type=ChangingOverTime_NodeKind, multiplicity=Multiplicity(1, 1))
    }
)
child7: BinaryAssociation = BinaryAssociation(
    name="child7",
    ends={
        Property(name="ChangingOverTime_NodeKind9", type=ChangingOverTime_LinkKind, multiplicity=Multiplicity(1, 1)),
        Property(name="ChangingOverTime_LinkKind8", type=ChangingOverTime_NodeKind, multiplicity=Multiplicity(1, 1))
    }
)
tree1: BinaryAssociation = BinaryAssociation(
    name="tree1",
    ends={
        Property(name="Tree", type=ChangingOverTime_NodeKind, multiplicity=Multiplicity(1, 1)),
        Property(name="root", type=ChangingOverTime_Tree, multiplicity=Multiplicity(0, 1))
    }
)
node2: BinaryAssociation = BinaryAssociation(
    name="node2",
    ends={
        Property(name="ChangingOverTime_NodeKind", type=ChangingOverTime_BindingKind, multiplicity=Multiplicity(1, 1)),
        Property(name="ChangingOverTime_BindingKind", type=ChangingOverTime_NodeKind, multiplicity=Multiplicity(1, 1))
    }
)
entity3: BinaryAssociation = BinaryAssociation(
    name="entity3",
    ends={
        Property(name="ChangingOverTime_Entity", type=ChangingOverTime_BindingKind, multiplicity=Multiplicity(1, 1)),
        Property(name="ChangingOverTime_BindingKind4", type=ChangingOverTime_Entity, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ChangingOverTime_Entity_TimeStampedElement = Generalization(general=TimeStampedElement, specific=ChangingOverTime_Entity)
gen_ChangingOverTime_NodeKind_TimeStampedElement = Generalization(general=TimeStampedElement, specific=ChangingOverTime_NodeKind)
gen_ChangingOverTime_BindingKind_TimeStampedElement = Generalization(general=TimeStampedElement, specific=ChangingOverTime_BindingKind)

# Domain Model
domain_model = DomainModel(
    name="ChangingOverTime",
    types={ChangingOverTime_TimeStampedElement, ChangingOverTime_Tree, ChangingOverTime_NodeKind, ChangingOverTime_LinkKind, TimeStampedElement, ChangingOverTime_BindingKind, ChangingOverTime_Entity},
    associations={root0, parent5, child7, tree1, node2, entity3},
    generalizations={gen_ChangingOverTime_Entity_TimeStampedElement, gen_ChangingOverTime_NodeKind_TimeStampedElement, gen_ChangingOverTime_BindingKind_TimeStampedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
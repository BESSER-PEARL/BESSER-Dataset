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
NamedElement = Class(name="NamedElement")
yye_Base = Class(name="yye::Base")
yye_NamedElement = Class(name="yye::NamedElement", is_abstract=True)
yye_Relation = Class(name="yye::Relation")
yye_Foo = Class(name="yye::Foo")
yye_Alias = Class(name="yye::Alias")

# NamedElement class attributes and methods

# yye_Base class attributes and methods
yye_Base_id: Property = Property(name="id", type=IntegerType)
yye_Base.attributes={yye_Base_id}

# yye_NamedElement class attributes and methods
yye_NamedElement_name: Property = Property(name="name", type=StringType)
yye_NamedElement.attributes={yye_NamedElement_name}

# yye_Relation class attributes and methods
yye_Relation_since: Property = Property(name="since", type=StringType)
yye_Relation.attributes={yye_Relation_since}

# yye_Foo class attributes and methods
yye_Foo_id: Property = Property(name="id", type=StringType)
yye_Foo.attributes={yye_Foo_id}

# yye_Alias class attributes and methods
yye_Alias_id: Property = Property(name="id", type=StringType)
yye_Alias.attributes={yye_Alias_id}

# Relationships
relations0: BinaryAssociation = BinaryAssociation(
    name="relations0",
    ends={
        Property(name="Relation", type=yye_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=yye_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foos1: BinaryAssociation = BinaryAssociation(
    name="foos1",
    ends={
        Property(name="yye_Foo", type=yye_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="yye_Base", type=yye_Foo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subRelations7: BinaryAssociation = BinaryAssociation(
    name="subRelations7",
    ends={
        Property(name="yye_Relation8", type=yye_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="yye_Relation6", type=yye_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aliases2: BinaryAssociation = BinaryAssociation(
    name="aliases2",
    ends={
        Property(name="yye_Alias", type=yye_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="yye_NamedElement", type=yye_Alias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing3: BinaryAssociation = BinaryAssociation(
    name="fromThing3",
    ends={
        Property(name="Base", type=yye_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=yye_Base, multiplicity=Multiplicity(0, 1))
    }
)
toThing4: BinaryAssociation = BinaryAssociation(
    name="toThing4",
    ends={
        Property(name="yye_Base5", type=yye_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="yye_Relation", type=yye_Base, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_yye_Base_NamedElement = Generalization(general=NamedElement, specific=yye_Base)
gen_yye_Relation_NamedElement = Generalization(general=NamedElement, specific=yye_Relation)

# Domain Model
domain_model = DomainModel(
    name="yye",
    types={NamedElement, yye_Base, yye_NamedElement, yye_Relation, yye_Foo, yye_Alias},
    associations={relations0, foos1, subRelations7, aliases2, fromThing3, toThing4},
    generalizations={gen_yye_Base_NamedElement, gen_yye_Relation_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
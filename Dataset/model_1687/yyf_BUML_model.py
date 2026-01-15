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
yyf_Relation = Class(name="yyf::Relation")
yyf_Foo = Class(name="yyf::Foo")
yyf_Output = Class(name="yyf::Output")
yyf_NamedElement = Class(name="yyf::NamedElement", is_abstract=True)
yyf_Base = Class(name="yyf::Base")
NamedElement = Class(name="NamedElement")
yyf_Alias = Class(name="yyf::Alias")
yyf_Bar = Class(name="yyf::Bar")

# yyf_Relation class attributes and methods
yyf_Relation_since: Property = Property(name="since", type=StringType)
yyf_Relation.attributes={yyf_Relation_since}

# yyf_Foo class attributes and methods
yyf_Foo_id: Property = Property(name="id", type=StringType)
yyf_Foo.attributes={yyf_Foo_id}

# yyf_Output class attributes and methods
yyf_Output_id: Property = Property(name="id", type=StringType)
yyf_Output.attributes={yyf_Output_id}

# yyf_NamedElement class attributes and methods
yyf_NamedElement_name: Property = Property(name="name", type=StringType)
yyf_NamedElement.attributes={yyf_NamedElement_name}

# yyf_Base class attributes and methods
yyf_Base_id: Property = Property(name="id", type=IntegerType)
yyf_Base.attributes={yyf_Base_id}

# NamedElement class attributes and methods

# yyf_Alias class attributes and methods
yyf_Alias_id: Property = Property(name="id", type=StringType)
yyf_Alias.attributes={yyf_Alias_id}

# yyf_Bar class attributes and methods
yyf_Bar_id: Property = Property(name="id", type=StringType)
yyf_Bar.attributes={yyf_Bar_id}

# Relationships
relations0: BinaryAssociation = BinaryAssociation(
    name="relations0",
    ends={
        Property(name="Relation", type=yyf_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=yyf_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foos1: BinaryAssociation = BinaryAssociation(
    name="foos1",
    ends={
        Property(name="yyf_Foo", type=yyf_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="yyf_Base", type=yyf_Foo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ouputs2: BinaryAssociation = BinaryAssociation(
    name="ouputs2",
    ends={
        Property(name="yyf_Output", type=yyf_Base, multiplicity=Multiplicity(1, 1)),
        Property(name="yyf_Base3", type=yyf_Output, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing7: BinaryAssociation = BinaryAssociation(
    name="fromThing7",
    ends={
        Property(name="Base", type=yyf_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=yyf_Base, multiplicity=Multiplicity(0, 1))
    }
)
toThing8: BinaryAssociation = BinaryAssociation(
    name="toThing8",
    ends={
        Property(name="yyf_Base9", type=yyf_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="yyf_Relation", type=yyf_Base, multiplicity=Multiplicity(0, 1))
    }
)
subRelations11: BinaryAssociation = BinaryAssociation(
    name="subRelations11",
    ends={
        Property(name="yyf_Relation12", type=yyf_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="yyf_Relation10", type=yyf_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aliases4: BinaryAssociation = BinaryAssociation(
    name="aliases4",
    ends={
        Property(name="yyf_Alias", type=yyf_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="yyf_NamedElement", type=yyf_Alias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bars5: BinaryAssociation = BinaryAssociation(
    name="bars5",
    ends={
        Property(name="yyf_Bar", type=yyf_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="yyf_NamedElement6", type=yyf_Bar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output13: BinaryAssociation = BinaryAssociation(
    name="output13",
    ends={
        Property(name="yyf_Output15", type=yyf_Bar, multiplicity=Multiplicity(1, 1)),
        Property(name="yyf_Bar14", type=yyf_Output, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_yyf_Base_NamedElement = Generalization(general=NamedElement, specific=yyf_Base)
gen_yyf_Relation_NamedElement = Generalization(general=NamedElement, specific=yyf_Relation)

# Domain Model
domain_model = DomainModel(
    name="yyf",
    types={yyf_Relation, yyf_Foo, yyf_Output, yyf_NamedElement, yyf_Base, NamedElement, yyf_Alias, yyf_Bar},
    associations={relations0, foos1, ouputs2, fromThing7, toThing8, subRelations11, aliases4, bars5, output13},
    generalizations={gen_yyf_Base_NamedElement, gen_yyf_Relation_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
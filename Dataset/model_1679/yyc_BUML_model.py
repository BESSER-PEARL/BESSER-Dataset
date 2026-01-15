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
yyc_RelatedTo = Class(name="yyc::RelatedTo")
yyc_Thing = Class(name="yyc::Thing")
yyc_Alias = Class(name="yyc::Alias")
yyc_Blias = Class(name="yyc::Blias")

# yyc_RelatedTo class attributes and methods
yyc_RelatedTo_since: Property = Property(name="since", type=StringType)
yyc_RelatedTo.attributes={yyc_RelatedTo_since}

# yyc_Thing class attributes and methods
yyc_Thing_id: Property = Property(name="id", type=IntegerType)
yyc_Thing.attributes={yyc_Thing_id}

# yyc_Alias class attributes and methods
yyc_Alias_id: Property = Property(name="id", type=StringType)
yyc_Alias.attributes={yyc_Alias_id}

# yyc_Blias class attributes and methods
yyc_Blias_id: Property = Property(name="id", type=StringType)
yyc_Blias.attributes={yyc_Blias_id}

# Relationships
relations0: BinaryAssociation = BinaryAssociation(
    name="relations0",
    ends={
        Property(name="RelatedTo", type=yyc_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=yyc_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromThing1: BinaryAssociation = BinaryAssociation(
    name="fromThing1",
    ends={
        Property(name="Thing", type=yyc_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=yyc_Thing, multiplicity=Multiplicity(0, 1))
    }
)
aliases2: BinaryAssociation = BinaryAssociation(
    name="aliases2",
    ends={
        Property(name="yyc_Alias", type=yyc_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="yyc_RelatedTo", type=yyc_Alias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bliases3: BinaryAssociation = BinaryAssociation(
    name="bliases3",
    ends={
        Property(name="yyc_Blias", type=yyc_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="yyc_RelatedTo4", type=yyc_Blias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="yyc",
    types={yyc_RelatedTo, yyc_Thing, yyc_Alias, yyc_Blias},
    associations={relations0, fromThing1, aliases2, bliases3},
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
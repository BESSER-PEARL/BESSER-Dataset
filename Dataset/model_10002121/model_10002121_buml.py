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
Product = Class(name="Product")
ProductGroup = Class(name="ProductGroup")
ProductGroupProduct = Class(name="ProductGroupProduct")
Events = Class(name="Events")
EventsProductGroup = Class(name="EventsProductGroup")

# Product class attributes and methods
Product_name: Property = Property(name="name", type=StringType)
Product_id: Property = Property(name="id", type=IntegerType)
Product.attributes={Product_id, Product_name}

# ProductGroup class attributes and methods
ProductGroup_id: Property = Property(name="id", type=IntegerType)
ProductGroup_name: Property = Property(name="name", type=StringType)
ProductGroup.attributes={ProductGroup_name, ProductGroup_id}

# ProductGroupProduct class attributes and methods
ProductGroupProduct_id: Property = Property(name="id", type=IntegerType)
ProductGroupProduct_ProductGroup: Property = Property(name="ProductGroup", type=ProductGroup)
ProductGroupProduct_Product: Property = Property(name="Product", type=Product)
ProductGroupProduct_weight: Property = Property(name="weight", type=IntegerType)
ProductGroupProduct.attributes={ProductGroupProduct_id, ProductGroupProduct_Product, ProductGroupProduct_weight, ProductGroupProduct_ProductGroup}

# Events class attributes and methods
Events_id: Property = Property(name="id", type=IntegerType)
Events_datetime: Property = Property(name="datetime", type=IntegerType)
Events_user: Property = Property(name="user", type=StringType)
Events_name: Property = Property(name="name", type=StringType)
Events.attributes={Events_user, Events_datetime, Events_id, Events_name}

# EventsProductGroup class attributes and methods
EventsProductGroup_id: Property = Property(name="id", type=IntegerType)
EventsProductGroup_Event: Property = Property(name="Event", type=Events)
EventsProductGroup_ProductGroup: Property = Property(name="ProductGroup", type=ProductGroup)
EventsProductGroup.attributes={EventsProductGroup_ProductGroup, EventsProductGroup_Event, EventsProductGroup_id}

# Relationships
ProductGroupProduct_Product: BinaryAssociation = BinaryAssociation(
    name="ProductGroupProduct_Product",
    ends={
        Property(name="product0", type=Product, multiplicity=Multiplicity(0, 1)),
        Property(name="productGroupProduct1", type=ProductGroupProduct, multiplicity=Multiplicity(0, 1))
    }
)
ProductGroupProduct_ProductGroup: BinaryAssociation = BinaryAssociation(
    name="ProductGroupProduct_ProductGroup",
    ends={
        Property(name="productGroup2", type=ProductGroup, multiplicity=Multiplicity(0, 1)),
        Property(name="productGroupProduct3", type=ProductGroupProduct, multiplicity=Multiplicity(0, 1))
    }
)
EventsProductGroup_ProductGroup: BinaryAssociation = BinaryAssociation(
    name="EventsProductGroup_ProductGroup",
    ends={
        Property(name="productGroup4", type=ProductGroup, multiplicity=Multiplicity(0, 1)),
        Property(name="eventsProductGroup5", type=EventsProductGroup, multiplicity=Multiplicity(0, 1))
    }
)
EventsProductGroup_Events: BinaryAssociation = BinaryAssociation(
    name="EventsProductGroup_Events",
    ends={
        Property(name="events6", type=Events, multiplicity=Multiplicity(0, 1)),
        Property(name="eventsProductGroup7", type=EventsProductGroup, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_podzQJTgEeiilJ4tAEXZQQ",
    types={Product, ProductGroup, ProductGroupProduct, Events, EventsProductGroup},
    associations={ProductGroupProduct_Product, ProductGroupProduct_ProductGroup, EventsProductGroup_ProductGroup, EventsProductGroup_Events},
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
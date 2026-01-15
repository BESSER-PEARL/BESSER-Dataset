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
b_Model = Class(name="b::Model")
b_B = Class(name="b::B")
b_Ebook = Class(name="b::Ebook")

# b_Model class attributes and methods

# b_B class attributes and methods
b_B_id: Property = Property(name="id", type=StringType)
b_B.attributes={b_B_id}

# b_Ebook class attributes and methods
b_Ebook_label: Property = Property(name="label", type=StringType)
b_Ebook_info: Property = Property(name="info", type=StringType)
b_Ebook_date: Property = Property(name="date", type=StringType)
b_Ebook_category: Property = Property(name="category", type=StringType)
b_Ebook.attributes={b_Ebook_date, b_Ebook_info, b_Ebook_label, b_Ebook_category}

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="b_B", type=b_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Model", type=b_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
y1: BinaryAssociation = BinaryAssociation(
    name="y1",
    ends={
        Property(name="b_Ebook", type=b_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="b_Model2", type=b_Ebook, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="b",
    types={b_Model, b_B, b_Ebook},
    associations={b0, y1},
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
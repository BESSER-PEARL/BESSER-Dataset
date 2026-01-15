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
myDsl_JAVAID = Class(name="myDsl::JAVAID")
myDsl_Interface = Class(name="myDsl::Interface")
myDsl_Attribute = Class(name="myDsl::Attribute")
myDsl_Model = Class(name="myDsl::Model")
myDsl_Type = Class(name="myDsl::Type")
myDsl_TypeDef = Class(name="myDsl::TypeDef")
Type = Class(name="Type")

# myDsl_JAVAID class attributes and methods
myDsl_JAVAID_name: Property = Property(name="name", type=StringType)
myDsl_JAVAID.attributes={myDsl_JAVAID_name}

# myDsl_Interface class attributes and methods

# myDsl_Attribute class attributes and methods
myDsl_Attribute_many: Property = Property(name="many", type=BooleanType)
myDsl_Attribute.attributes={myDsl_Attribute_many}

# myDsl_Model class attributes and methods

# myDsl_Type class attributes and methods
myDsl_Type_name: Property = Property(name="name", type=StringType)
myDsl_Type.attributes={myDsl_Type_name}

# myDsl_TypeDef class attributes and methods

# Type class attributes and methods

# Relationships
mappedType1: BinaryAssociation = BinaryAssociation(
    name="mappedType1",
    ends={
        Property(name="myDsl_JAVAID", type=myDsl_TypeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeDef", type=myDsl_JAVAID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superInterface3: BinaryAssociation = BinaryAssociation(
    name="superInterface3",
    ends={
        Property(name="myDsl_Interface", type=myDsl_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Interface2", type=myDsl_Interface, multiplicity=Multiplicity(0, 1))
    }
)
attributes4: BinaryAssociation = BinaryAssociation(
    name="attributes4",
    ends={
        Property(name="myDsl_Attribute", type=myDsl_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Interface5", type=myDsl_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="myDsl_Type", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="myDsl_Type8", type=myDsl_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Attribute7", type=myDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_myDsl_Interface_Type = Generalization(general=Type, specific=myDsl_Interface)
gen_myDsl_Attribute_Type = Generalization(general=Type, specific=myDsl_Attribute)
gen_myDsl_TypeDef_Type = Generalization(general=Type, specific=myDsl_TypeDef)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_JAVAID, myDsl_Interface, myDsl_Attribute, myDsl_Model, myDsl_Type, myDsl_TypeDef, Type},
    associations={mappedType1, superInterface3, attributes4, types0, type6},
    generalizations={gen_myDsl_Interface_Type, gen_myDsl_Attribute_Type, gen_myDsl_TypeDef_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
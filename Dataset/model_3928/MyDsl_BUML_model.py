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
myDsl_File = Class(name="myDsl::File")
myDsl_Element = Class(name="myDsl::Element")
myDsl_Import = Class(name="myDsl::Import")
Element = Class(name="Element")
myDsl_Namespace = Class(name="myDsl::Namespace")
myDsl_Type = Class(name="myDsl::Type")
myDsl_Entity = Class(name="myDsl::Entity")
Type = Class(name="Type")
myDsl_Property = Class(name="myDsl::Property")
myDsl_Datatype = Class(name="myDsl::Datatype")

# myDsl_File class attributes and methods

# myDsl_Element class attributes and methods

# myDsl_Import class attributes and methods
myDsl_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
myDsl_Import.attributes={myDsl_Import_importedNamespace}

# Element class attributes and methods

# myDsl_Namespace class attributes and methods
myDsl_Namespace_name: Property = Property(name="name", type=StringType)
myDsl_Namespace.attributes={myDsl_Namespace_name}

# myDsl_Type class attributes and methods
myDsl_Type_name: Property = Property(name="name", type=StringType)
myDsl_Type.attributes={myDsl_Type_name}

# myDsl_Entity class attributes and methods

# Type class attributes and methods

# myDsl_Property class attributes and methods
myDsl_Property_name: Property = Property(name="name", type=StringType)
myDsl_Property.attributes={myDsl_Property_name}

# myDsl_Datatype class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="myDsl_Element", type=myDsl_File, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_File", type=myDsl_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="myDsl_Element2", type=myDsl_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Namespace", type=myDsl_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties3: BinaryAssociation = BinaryAssociation(
    name="properties3",
    ends={
        Property(name="myDsl_Property", type=myDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entity", type=myDsl_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="myDsl_Type", type=myDsl_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Property5", type=myDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_myDsl_Import_Element = Generalization(general=Element, specific=myDsl_Import)
gen_myDsl_Namespace_Element = Generalization(general=Element, specific=myDsl_Namespace)
gen_myDsl_Type_Element = Generalization(general=Element, specific=myDsl_Type)
gen_myDsl_Entity_Type = Generalization(general=Type, specific=myDsl_Entity)
gen_myDsl_Datatype_Type = Generalization(general=Type, specific=myDsl_Datatype)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_File, myDsl_Element, myDsl_Import, Element, myDsl_Namespace, myDsl_Type, myDsl_Entity, Type, myDsl_Property, myDsl_Datatype},
    associations={elements0, elements1, properties3, type4},
    generalizations={gen_myDsl_Import_Element, gen_myDsl_Namespace_Element, gen_myDsl_Type_Element, gen_myDsl_Entity_Type, gen_myDsl_Datatype_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
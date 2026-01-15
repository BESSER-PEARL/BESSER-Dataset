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
smalluml_Class = Class(name="smalluml::Class")
NamedElement = Class(name="NamedElement")
smalluml_Method = Class(name="smalluml::Method")
smalluml_Type = Class(name="smalluml::Type")
smalluml_Float = Class(name="smalluml::Float")
Type = Class(name="Type")
smalluml_Int = Class(name="smalluml::Int")
smalluml_Boolean = Class(name="smalluml::Boolean")
smalluml_String = Class(name="smalluml::String")
smalluml_NamedElement = Class(name="smalluml::NamedElement")
smalluml_Diagram = Class(name="smalluml::Diagram")
smalluml_Association = Class(name="smalluml::Association")
smalluml_Role = Class(name="smalluml::Role")
smalluml_Heritage = Class(name="smalluml::Heritage")

# smalluml_Class class attributes and methods

# NamedElement class attributes and methods

# smalluml_Method class attributes and methods

# smalluml_Type class attributes and methods

# smalluml_Float class attributes and methods

# Type class attributes and methods

# smalluml_Int class attributes and methods

# smalluml_Boolean class attributes and methods

# smalluml_String class attributes and methods

# smalluml_NamedElement class attributes and methods
smalluml_NamedElement_name: Property = Property(name="name", type=StringType)
smalluml_NamedElement.attributes={smalluml_NamedElement_name}

# smalluml_Diagram class attributes and methods

# smalluml_Association class attributes and methods

# smalluml_Role class attributes and methods
smalluml_Role_upper: Property = Property(name="upper", type=IntegerType)
smalluml_Role_lower: Property = Property(name="lower", type=IntegerType)
smalluml_Role.attributes={smalluml_Role_upper, smalluml_Role_lower}

# smalluml_Heritage class attributes and methods

# Relationships
method0: BinaryAssociation = BinaryAssociation(
    name="method0",
    ends={
        Property(name="smalluml_Method", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class", type=smalluml_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute1: BinaryAssociation = BinaryAssociation(
    name="attribute1",
    ends={
        Property(name="smalluml_Type", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class2", type=smalluml_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters3: BinaryAssociation = BinaryAssociation(
    name="parameters3",
    ends={
        Property(name="smalluml_Type5", type=smalluml_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Method4", type=smalluml_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
return6: BinaryAssociation = BinaryAssociation(
    name="return6",
    ends={
        Property(name="smalluml_Type8", type=smalluml_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Method7", type=smalluml_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assoc21: BinaryAssociation = BinaryAssociation(
    name="assoc21",
    ends={
        Property(name="smalluml_Association22", type=smalluml_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Diagram", type=smalluml_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
heritage23: BinaryAssociation = BinaryAssociation(
    name="heritage23",
    ends={
        Property(name="smalluml_Heritage25", type=smalluml_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Diagram24", type=smalluml_Heritage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class26: BinaryAssociation = BinaryAssociation(
    name="class26",
    ends={
        Property(name="smalluml_Class28", type=smalluml_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Diagram27", type=smalluml_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
used9: BinaryAssociation = BinaryAssociation(
    name="used9",
    ends={
        Property(name="smalluml_Role", type=smalluml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Association", type=smalluml_Role, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
user10: BinaryAssociation = BinaryAssociation(
    name="user10",
    ends={
        Property(name="smalluml_Role12", type=smalluml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Association11", type=smalluml_Role, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mother13: BinaryAssociation = BinaryAssociation(
    name="mother13",
    ends={
        Property(name="smalluml_Role14", type=smalluml_Heritage, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Heritage", type=smalluml_Role, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
child15: BinaryAssociation = BinaryAssociation(
    name="child15",
    ends={
        Property(name="smalluml_Role17", type=smalluml_Heritage, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Heritage16", type=smalluml_Role, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
class18: BinaryAssociation = BinaryAssociation(
    name="class18",
    ends={
        Property(name="smalluml_Class20", type=smalluml_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Role19", type=smalluml_Class, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_smalluml_Class_NamedElement = Generalization(general=NamedElement, specific=smalluml_Class)
gen_smalluml_Method_NamedElement = Generalization(general=NamedElement, specific=smalluml_Method)
gen_smalluml_Type_NamedElement = Generalization(general=NamedElement, specific=smalluml_Type)
gen_smalluml_Float_Type = Generalization(general=Type, specific=smalluml_Float)
gen_smalluml_Int_Type = Generalization(general=Type, specific=smalluml_Int)
gen_smalluml_Boolean_Type = Generalization(general=Type, specific=smalluml_Boolean)
gen_smalluml_String_Type = Generalization(general=Type, specific=smalluml_String)
gen_smalluml_Association_NamedElement = Generalization(general=NamedElement, specific=smalluml_Association)
gen_smalluml_Heritage_NamedElement = Generalization(general=NamedElement, specific=smalluml_Heritage)
gen_smalluml_Role_NamedElement = Generalization(general=NamedElement, specific=smalluml_Role)

# Domain Model
domain_model = DomainModel(
    name="smalluml",
    types={smalluml_Class, NamedElement, smalluml_Method, smalluml_Type, smalluml_Float, Type, smalluml_Int, smalluml_Boolean, smalluml_String, smalluml_NamedElement, smalluml_Diagram, smalluml_Association, smalluml_Role, smalluml_Heritage},
    associations={method0, attribute1, parameters3, return6, assoc21, heritage23, class26, used9, user10, mother13, child15, class18},
    generalizations={gen_smalluml_Class_NamedElement, gen_smalluml_Method_NamedElement, gen_smalluml_Type_NamedElement, gen_smalluml_Float_Type, gen_smalluml_Int_Type, gen_smalluml_Boolean_Type, gen_smalluml_String_Type, gen_smalluml_Association_NamedElement, gen_smalluml_Heritage_NamedElement, gen_smalluml_Role_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
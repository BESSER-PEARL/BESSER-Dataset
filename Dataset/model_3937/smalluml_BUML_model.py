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
smalluml_SchemaUML = Class(name="smalluml::SchemaUML")
smalluml_Generalisation = Class(name="smalluml::Generalisation")
smalluml_SmallClass = Class(name="smalluml::SmallClass")
smalluml_Association = Class(name="smalluml::Association")
smalluml_Attribute = Class(name="smalluml::Attribute")
smalluml_Methode = Class(name="smalluml::Methode")
smalluml_Role = Class(name="smalluml::Role")

# smalluml_SchemaUML class attributes and methods

# smalluml_Generalisation class attributes and methods

# smalluml_SmallClass class attributes and methods
smalluml_SmallClass_name: Property = Property(name="name", type=StringType)
smalluml_SmallClass.attributes={smalluml_SmallClass_name}

# smalluml_Association class attributes and methods
smalluml_Association_name: Property = Property(name="name", type=StringType)
smalluml_Association.attributes={smalluml_Association_name}

# smalluml_Attribute class attributes and methods
smalluml_Attribute_name: Property = Property(name="name", type=StringType)
smalluml_Attribute_type: Property = Property(name="type", type=StringType)
smalluml_Attribute.attributes={smalluml_Attribute_name, smalluml_Attribute_type}

# smalluml_Methode class attributes and methods
smalluml_Methode_name: Property = Property(name="name", type=StringType)
smalluml_Methode_returnType: Property = Property(name="returnType", type=StringType)
smalluml_Methode.attributes={smalluml_Methode_name, smalluml_Methode_returnType}

# smalluml_Role class attributes and methods
smalluml_Role_Multiplicity: Property = Property(name="Multiplicity", type=StringType)
smalluml_Role.attributes={smalluml_Role_Multiplicity}

# Relationships
gene0: BinaryAssociation = BinaryAssociation(
    name="gene0",
    ends={
        Property(name="smalluml_Generalisation", type=smalluml_SchemaUML, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_SchemaUML", type=smalluml_Generalisation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c1: BinaryAssociation = BinaryAssociation(
    name="c1",
    ends={
        Property(name="smalluml_SmallClass", type=smalluml_SchemaUML, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_SchemaUML2", type=smalluml_SmallClass, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
ass3: BinaryAssociation = BinaryAssociation(
    name="ass3",
    ends={
        Property(name="smalluml_Association", type=smalluml_SchemaUML, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_SchemaUML4", type=smalluml_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listeAttribute5: BinaryAssociation = BinaryAssociation(
    name="listeAttribute5",
    ends={
        Property(name="smalluml_Attribute", type=smalluml_SmallClass, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_SmallClass6", type=smalluml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listeMethode7: BinaryAssociation = BinaryAssociation(
    name="listeMethode7",
    ends={
        Property(name="smalluml_Methode", type=smalluml_SmallClass, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_SmallClass8", type=smalluml_Methode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="smalluml_SmallClass11", type=smalluml_Generalisation, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Generalisation10", type=smalluml_SmallClass, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cible12: BinaryAssociation = BinaryAssociation(
    name="cible12",
    ends={
        Property(name="smalluml_SmallClass14", type=smalluml_Generalisation, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Generalisation13", type=smalluml_SmallClass, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="smalluml_SmallClass17", type=smalluml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Association16", type=smalluml_SmallClass, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cible18: BinaryAssociation = BinaryAssociation(
    name="cible18",
    ends={
        Property(name="smalluml_SmallClass20", type=smalluml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Association19", type=smalluml_SmallClass, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
listeAttribute21: BinaryAssociation = BinaryAssociation(
    name="listeAttribute21",
    ends={
        Property(name="smalluml_Attribute23", type=smalluml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Association22", type=smalluml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listeRole24: BinaryAssociation = BinaryAssociation(
    name="listeRole24",
    ends={
        Property(name="smalluml_Role", type=smalluml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Association25", type=smalluml_Role, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
classDedie26: BinaryAssociation = BinaryAssociation(
    name="classDedie26",
    ends={
        Property(name="smalluml_SmallClass28", type=smalluml_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Role27", type=smalluml_SmallClass, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="smalluml",
    types={smalluml_SchemaUML, smalluml_Generalisation, smalluml_SmallClass, smalluml_Association, smalluml_Attribute, smalluml_Methode, smalluml_Role},
    associations={gene0, c1, ass3, listeAttribute5, listeMethode7, source9, cible12, source15, cible18, listeAttribute21, listeRole24, classDedie26},
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
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

# Enumerations
HibernateAnnotationTypes: Enumeration = Enumeration(
    name="HibernateAnnotationTypes",
    literals={
            EnumerationLiteral(name="OneToMany"),
			EnumerationLiteral(name="ManyToOne"),
			EnumerationLiteral(name="ManyToMany"),
			EnumerationLiteral(name="OneToOne"),
			EnumerationLiteral(name="Column")
    }
)

HibernateCascadeTypes: Enumeration = Enumeration(
    name="HibernateCascadeTypes",
    literals={
            EnumerationLiteral(name="CascadeAll")
    }
)

# Classes
metamodel_Datatype = Class(name="metamodel::Datatype")
Type = Class(name="Type")
metamodel_Entity = Class(name="metamodel::Entity")
metamodel_Attribute = Class(name="metamodel::Attribute")
metamodel_Model = Class(name="metamodel::Model")
metamodel_Type = Class(name="metamodel::Type", is_abstract=True)
metamodel_HibernateAnnotation = Class(name="metamodel::HibernateAnnotation")

# metamodel_Datatype class attributes and methods

# Type class attributes and methods

# metamodel_Entity class attributes and methods

# metamodel_Attribute class attributes and methods
metamodel_Attribute_name: Property = Property(name="name", type=StringType)
metamodel_Attribute_list: Property = Property(name="list", type=BooleanType)
metamodel_Attribute.attributes={metamodel_Attribute_list, metamodel_Attribute_name}

# metamodel_Model class attributes and methods

# metamodel_Type class attributes and methods
metamodel_Type_name: Property = Property(name="name", type=StringType)
metamodel_Type.attributes={metamodel_Type_name}

# metamodel_HibernateAnnotation class attributes and methods
metamodel_HibernateAnnotation_annotationType: Property = Property(name="annotationType", type=StringType)
metamodel_HibernateAnnotation_unique: Property = Property(name="unique", type=StringType)
metamodel_HibernateAnnotation_cascade: Property = Property(name="cascade", type=StringType)
metamodel_HibernateAnnotation.attributes={metamodel_HibernateAnnotation_cascade, metamodel_HibernateAnnotation_annotationType, metamodel_HibernateAnnotation_unique}

# Relationships
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="metamodel_Type", type=metamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Model", type=metamodel_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="metamodel_Attribute", type=metamodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Entity", type=metamodel_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappedBy7: BinaryAssociation = BinaryAssociation(
    name="mappedBy7",
    ends={
        Property(name="metamodel_Attribute9", type=metamodel_HibernateAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_HibernateAnnotation8", type=metamodel_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="metamodel_Type4", type=metamodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Attribute3", type=metamodel_Type, multiplicity=Multiplicity(0, 1))
    }
)
annotations5: BinaryAssociation = BinaryAssociation(
    name="annotations5",
    ends={
        Property(name="metamodel_HibernateAnnotation", type=metamodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Attribute6", type=metamodel_HibernateAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_metamodel_Datatype_Type = Generalization(general=Type, specific=metamodel_Datatype)
gen_metamodel_Entity_Type = Generalization(general=Type, specific=metamodel_Entity)

# Domain Model
domain_model = DomainModel(
    name="metamodel",
    types={metamodel_Datatype, Type, metamodel_Entity, metamodel_Attribute, metamodel_Model, metamodel_Type, metamodel_HibernateAnnotation, HibernateAnnotationTypes, HibernateCascadeTypes},
    associations={types0, attributes1, mappedBy7, type2, annotations5},
    generalizations={gen_metamodel_Datatype_Type, gen_metamodel_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
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
Annotation: Enumeration = Enumeration(
    name="Annotation",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="OneToOne"),
			EnumerationLiteral(name="OneToMany"),
			EnumerationLiteral(name="ManyToOne"),
			EnumerationLiteral(name="ManyToMany"),
			EnumerationLiteral(name="ManyToManyMapped"),
			EnumerationLiteral(name="Id")
    }
)

# Classes
metamodel_Model = Class(name="metamodel::Model")
metamodel_Type = Class(name="metamodel::Type", is_abstract=True)
metamodel_Datatype = Class(name="metamodel::Datatype")
Type = Class(name="Type")
metamodel_Entity = Class(name="metamodel::Entity")
metamodel_Feature = Class(name="metamodel::Feature")
metamodel_Query = Class(name="metamodel::Query")
metamodel_parameter = Class(name="metamodel::parameter")

# metamodel_Model class attributes and methods

# metamodel_Type class attributes and methods
metamodel_Type_name: Property = Property(name="name", type=StringType)
metamodel_Type.attributes={metamodel_Type_name}

# metamodel_Datatype class attributes and methods

# Type class attributes and methods

# metamodel_Entity class attributes and methods

# metamodel_Feature class attributes and methods
metamodel_Feature_name: Property = Property(name="name", type=StringType)
metamodel_Feature_annotation: Property = Property(name="annotation", type=StringType)
metamodel_Feature_mappedBy: Property = Property(name="mappedBy", type=StringType)
metamodel_Feature.attributes={metamodel_Feature_mappedBy, metamodel_Feature_annotation, metamodel_Feature_name}

# metamodel_Query class attributes and methods
metamodel_Query_methodName: Property = Property(name="methodName", type=StringType)
metamodel_Query_queryString: Property = Property(name="queryString", type=StringType)
metamodel_Query.attributes={metamodel_Query_queryString, metamodel_Query_methodName}

# metamodel_parameter class attributes and methods
metamodel_parameter_name: Property = Property(name="name", type=StringType)
metamodel_parameter.attributes={metamodel_parameter_name}

# Relationships
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="metamodel_Type", type=metamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Model", type=metamodel_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features1: BinaryAssociation = BinaryAssociation(
    name="features1",
    ends={
        Property(name="metamodel_Feature", type=metamodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Entity", type=metamodel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
queries2: BinaryAssociation = BinaryAssociation(
    name="queries2",
    ends={
        Property(name="metamodel_Query", type=metamodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Entity3", type=metamodel_Query, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="metamodel_Type6", type=metamodel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Feature5", type=metamodel_Type, multiplicity=Multiplicity(0, 1))
    }
)
EReference07: BinaryAssociation = BinaryAssociation(
    name="EReference07",
    ends={
        Property(name="metamodel_Entity9", type=metamodel_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Query8", type=metamodel_Entity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters10: BinaryAssociation = BinaryAssociation(
    name="parameters10",
    ends={
        Property(name="metamodel_parameter", type=metamodel_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Query11", type=metamodel_parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type12: BinaryAssociation = BinaryAssociation(
    name="type12",
    ends={
        Property(name="metamodel_Type14", type=metamodel_parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_parameter13", type=metamodel_Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_metamodel_Datatype_Type = Generalization(general=Type, specific=metamodel_Datatype)
gen_metamodel_Entity_Type = Generalization(general=Type, specific=metamodel_Entity)

# Domain Model
domain_model = DomainModel(
    name="metamodel",
    types={metamodel_Model, metamodel_Type, metamodel_Datatype, Type, metamodel_Entity, metamodel_Feature, metamodel_Query, metamodel_parameter, Annotation},
    associations={types0, features1, queries2, type4, EReference07, parameters10, type12},
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
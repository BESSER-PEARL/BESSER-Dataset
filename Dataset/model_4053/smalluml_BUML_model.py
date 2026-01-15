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
Entity = Class(name="Entity")
smalluml_Attribute = Class(name="smalluml::Attribute")
smalluml_Class = Class(name="smalluml::Class")
smalluml_Enumeration = Class(name="smalluml::Enumeration")
smalluml_Operation = Class(name="smalluml::Operation")
smalluml_ClassDiagram = Class(name="smalluml::ClassDiagram")
smalluml_Entity = Class(name="smalluml::Entity")
smalluml_Type = Class(name="smalluml::Type")
smalluml_Parameter = Class(name="smalluml::Parameter")
smalluml_Cardinalities = Class(name="smalluml::Cardinalities")
smalluml_Association = Class(name="smalluml::Association")
smalluml_BooleanType = Class(name="smalluml::BooleanType")
Type = Class(name="Type")
smalluml_RealType = Class(name="smalluml::RealType")
smalluml_IntegerType = Class(name="smalluml::IntegerType")

# Entity class attributes and methods

# smalluml_Attribute class attributes and methods
smalluml_Attribute_name: Property = Property(name="name", type=StringType)
smalluml_Attribute.attributes={smalluml_Attribute_name}

# smalluml_Class class attributes and methods
smalluml_Class_abstract: Property = Property(name="abstract", type=BooleanType)
smalluml_Class.attributes={smalluml_Class_abstract}

# smalluml_Enumeration class attributes and methods
smalluml_Enumeration_variable: Property = Property(name="variable", type=StringType)
smalluml_Enumeration_name: Property = Property(name="name", type=StringType)
smalluml_Enumeration.attributes={smalluml_Enumeration_name, smalluml_Enumeration_variable}

# smalluml_Operation class attributes and methods
smalluml_Operation_name: Property = Property(name="name", type=StringType)
smalluml_Operation.attributes={smalluml_Operation_name}

# smalluml_ClassDiagram class attributes and methods
smalluml_ClassDiagram_name: Property = Property(name="name", type=StringType)
smalluml_ClassDiagram.attributes={smalluml_ClassDiagram_name}

# smalluml_Entity class attributes and methods
smalluml_Entity_name: Property = Property(name="name", type=StringType)
smalluml_Entity.attributes={smalluml_Entity_name}

# smalluml_Type class attributes and methods

# smalluml_Parameter class attributes and methods
smalluml_Parameter_name: Property = Property(name="name", type=StringType)
smalluml_Parameter.attributes={smalluml_Parameter_name}

# smalluml_Cardinalities class attributes and methods
smalluml_Cardinalities_lowerbound: Property = Property(name="lowerbound", type=IntegerType)
smalluml_Cardinalities_upperbound: Property = Property(name="upperbound", type=IntegerType)
smalluml_Cardinalities.attributes={smalluml_Cardinalities_upperbound, smalluml_Cardinalities_lowerbound}

# smalluml_Association class attributes and methods

# smalluml_BooleanType class attributes and methods

# Type class attributes and methods

# smalluml_RealType class attributes and methods

# smalluml_IntegerType class attributes and methods

# Relationships
attributes0: BinaryAssociation = BinaryAssociation(
    name="attributes0",
    ends={
        Property(name="smalluml_Attribute", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class", type=smalluml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends2: BinaryAssociation = BinaryAssociation(
    name="extends2",
    ends={
        Property(name="smalluml_Class3", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class1", type=smalluml_Class, multiplicity=Multiplicity(0, 1))
    }
)
operations4: BinaryAssociation = BinaryAssociation(
    name="operations4",
    ends={
        Property(name="smalluml_Operation", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class5", type=smalluml_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities6: BinaryAssociation = BinaryAssociation(
    name="entities6",
    ends={
        Property(name="smalluml_Entity", type=smalluml_ClassDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_ClassDiagram", type=smalluml_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeReturn7: BinaryAssociation = BinaryAssociation(
    name="typeReturn7",
    ends={
        Property(name="smalluml_Type", type=smalluml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Operation8", type=smalluml_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters9: BinaryAssociation = BinaryAssociation(
    name="parameters9",
    ends={
        Property(name="smalluml_Parameter", type=smalluml_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Operation10", type=smalluml_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="smalluml_Type13", type=smalluml_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Attribute12", type=smalluml_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="smalluml_Type16", type=smalluml_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Parameter15", type=smalluml_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cardinalities17: BinaryAssociation = BinaryAssociation(
    name="cardinalities17",
    ends={
        Property(name="smalluml_Cardinalities", type=smalluml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Association", type=smalluml_Cardinalities, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetclass18: BinaryAssociation = BinaryAssociation(
    name="targetclass18",
    ends={
        Property(name="smalluml_Class20", type=smalluml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Association19", type=smalluml_Class, multiplicity=Multiplicity(1, 1))
    }
)
sourceclass21: BinaryAssociation = BinaryAssociation(
    name="sourceclass21",
    ends={
        Property(name="smalluml_Class23", type=smalluml_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Association22", type=smalluml_Class, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_smalluml_Class_Entity = Generalization(general=Entity, specific=smalluml_Class)
gen_smalluml_IntegerType_Type = Generalization(general=Type, specific=smalluml_IntegerType)
gen_smalluml_Enumeration_Type = Generalization(general=Type, specific=smalluml_Enumeration)
gen_smalluml_Association_Entity = Generalization(general=Entity, specific=smalluml_Association)
gen_smalluml_BooleanType_Type = Generalization(general=Type, specific=smalluml_BooleanType)
gen_smalluml_RealType_Type = Generalization(general=Type, specific=smalluml_RealType)

# Domain Model
domain_model = DomainModel(
    name="smalluml",
    types={Entity, smalluml_Attribute, smalluml_Class, smalluml_Enumeration, smalluml_Operation, smalluml_ClassDiagram, smalluml_Entity, smalluml_Type, smalluml_Parameter, smalluml_Cardinalities, smalluml_Association, smalluml_BooleanType, Type, smalluml_RealType, smalluml_IntegerType},
    associations={attributes0, extends2, operations4, entities6, typeReturn7, parameters9, type11, type14, cardinalities17, targetclass18, sourceclass21},
    generalizations={gen_smalluml_Class_Entity, gen_smalluml_IntegerType_Type, gen_smalluml_Enumeration_Type, gen_smalluml_Association_Entity, gen_smalluml_BooleanType_Type, gen_smalluml_RealType_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
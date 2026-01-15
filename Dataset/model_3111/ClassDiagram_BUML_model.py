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
classdiagram_Generalization = Class(name="classdiagram::Generalization")
classdiagram_Diagram = Class(name="classdiagram::Diagram")
classdiagram_Class = Class(name="classdiagram::Class")
classdiagram_Association = Class(name="classdiagram::Association")
classdiagram_PrimitiveDataType = Class(name="classdiagram::PrimitiveDataType")
classdiagram_Aggregation = Class(name="classdiagram::Aggregation")
Association = Class(name="Association")
classdiagram_Composition = Class(name="classdiagram::Composition")
classdiagram_Dependency = Class(name="classdiagram::Dependency")
AttributeValue = Class(name="AttributeValue")
classdiagram_Attribute = Class(name="classdiagram::Attribute")
classdiagram_Method = Class(name="classdiagram::Method")
classdiagram_Realization = Class(name="classdiagram::Realization")
classdiagram_Interface = Class(name="classdiagram::Interface")
classdiagram_InterfaceRealization = Class(name="classdiagram::InterfaceRealization")
classdiagram_AttributeValue = Class(name="classdiagram::AttributeValue", is_abstract=True)

# classdiagram_Generalization class attributes and methods

# classdiagram_Diagram class attributes and methods

# classdiagram_Class class attributes and methods
classdiagram_Class_name: Property = Property(name="name", type=StringType)
classdiagram_Class_is_persistent: Property = Property(name="is_persistent", type=BooleanType)
classdiagram_Class.attributes={classdiagram_Class_name, classdiagram_Class_is_persistent}

# classdiagram_Association class attributes and methods
classdiagram_Association_name: Property = Property(name="name", type=StringType)
classdiagram_Association_sourceMultiplicity: Property = Property(name="sourceMultiplicity", type=IntegerType)
classdiagram_Association_targetMultiplicity: Property = Property(name="targetMultiplicity", type=IntegerType)
classdiagram_Association.attributes={classdiagram_Association_sourceMultiplicity, classdiagram_Association_targetMultiplicity, classdiagram_Association_name}

# classdiagram_PrimitiveDataType class attributes and methods
classdiagram_PrimitiveDataType_name: Property = Property(name="name", type=StringType)
classdiagram_PrimitiveDataType.attributes={classdiagram_PrimitiveDataType_name}

# classdiagram_Aggregation class attributes and methods

# Association class attributes and methods

# classdiagram_Composition class attributes and methods

# classdiagram_Dependency class attributes and methods

# AttributeValue class attributes and methods

# classdiagram_Attribute class attributes and methods
classdiagram_Attribute_name: Property = Property(name="name", type=StringType)
classdiagram_Attribute_is_primary: Property = Property(name="is_primary", type=BooleanType)
classdiagram_Attribute.attributes={classdiagram_Attribute_is_primary, classdiagram_Attribute_name}

# classdiagram_Method class attributes and methods
classdiagram_Method_name: Property = Property(name="name", type=StringType)
classdiagram_Method.attributes={classdiagram_Method_name}

# classdiagram_Realization class attributes and methods

# classdiagram_Interface class attributes and methods
classdiagram_Interface_name: Property = Property(name="name", type=StringType)
classdiagram_Interface.attributes={classdiagram_Interface_name}

# classdiagram_InterfaceRealization class attributes and methods

# classdiagram_AttributeValue class attributes and methods

# Relationships
generalizations5: BinaryAssociation = BinaryAssociation(
    name="generalizations5",
    ends={
        Property(name="classdiagram_Generalization", type=classdiagram_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Diagram6", type=classdiagram_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="classdiagram_Class9", type=classdiagram_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Association8", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="classdiagram_Class", type=classdiagram_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Diagram", type=classdiagram_Class, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
associations1: BinaryAssociation = BinaryAssociation(
    name="associations1",
    ends={
        Property(name="classdiagram_Association", type=classdiagram_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Diagram2", type=classdiagram_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types3: BinaryAssociation = BinaryAssociation(
    name="types3",
    ends={
        Property(name="classdiagram_PrimitiveDataType", type=classdiagram_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Diagram4", type=classdiagram_PrimitiveDataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="classdiagram_Class12", type=classdiagram_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Association11", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
attribute13: BinaryAssociation = BinaryAssociation(
    name="attribute13",
    ends={
        Property(name="classdiagram_Attribute", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Class14", type=classdiagram_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method15: BinaryAssociation = BinaryAssociation(
    name="method15",
    ends={
        Property(name="classdiagram_Method", type=classdiagram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Class16", type=classdiagram_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target30: BinaryAssociation = BinaryAssociation(
    name="target30",
    ends={
        Property(name="classdiagram_Class32", type=classdiagram_InterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_InterfaceRealization31", type=classdiagram_Class, multiplicity=Multiplicity(0, 9999))
    }
)
source33: BinaryAssociation = BinaryAssociation(
    name="source33",
    ends={
        Property(name="classdiagram_Class34", type=classdiagram_Realization, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Realization", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
source17: BinaryAssociation = BinaryAssociation(
    name="source17",
    ends={
        Property(name="classdiagram_Class19", type=classdiagram_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Generalization18", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="classdiagram_Class22", type=classdiagram_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Generalization21", type=classdiagram_Class, multiplicity=Multiplicity(1, 1))
    }
)
attribute23: BinaryAssociation = BinaryAssociation(
    name="attribute23",
    ends={
        Property(name="classdiagram_Attribute24", type=classdiagram_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Interface", type=classdiagram_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method25: BinaryAssociation = BinaryAssociation(
    name="method25",
    ends={
        Property(name="classdiagram_Method27", type=classdiagram_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Interface26", type=classdiagram_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source28: BinaryAssociation = BinaryAssociation(
    name="source28",
    ends={
        Property(name="classdiagram_Interface29", type=classdiagram_InterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_InterfaceRealization", type=classdiagram_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
target35: BinaryAssociation = BinaryAssociation(
    name="target35",
    ends={
        Property(name="classdiagram_Class37", type=classdiagram_Realization, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Realization36", type=classdiagram_Class, multiplicity=Multiplicity(1, 9999))
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="classdiagram_AttributeValue", type=classdiagram_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="classdiagram_Attribute39", type=classdiagram_AttributeValue, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_classdiagram_Aggregation_Association = Generalization(general=Association, specific=classdiagram_Aggregation)
gen_classdiagram_Composition_Association = Generalization(general=Association, specific=classdiagram_Composition)
gen_classdiagram_Class_AttributeValue = Generalization(general=AttributeValue, specific=classdiagram_Class)
gen_classdiagram_Dependency_Association = Generalization(general=Association, specific=classdiagram_Dependency)
gen_classdiagram_PrimitiveDataType_AttributeValue = Generalization(general=AttributeValue, specific=classdiagram_PrimitiveDataType)

# Domain Model
domain_model = DomainModel(
    name="classdiagram",
    types={classdiagram_Generalization, classdiagram_Diagram, classdiagram_Class, classdiagram_Association, classdiagram_PrimitiveDataType, classdiagram_Aggregation, Association, classdiagram_Composition, classdiagram_Dependency, AttributeValue, classdiagram_Attribute, classdiagram_Method, classdiagram_Realization, classdiagram_Interface, classdiagram_InterfaceRealization, classdiagram_AttributeValue},
    associations={generalizations5, source7, classes0, associations1, types3, target10, attribute13, method15, target30, source33, source17, target20, attribute23, method25, source28, target35, type38},
    generalizations={gen_classdiagram_Aggregation_Association, gen_classdiagram_Composition_Association, gen_classdiagram_Class_AttributeValue, gen_classdiagram_Dependency_Association, gen_classdiagram_PrimitiveDataType_AttributeValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
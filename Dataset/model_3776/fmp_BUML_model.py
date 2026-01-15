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
ValueType: Enumeration = Enumeration(
    name="ValueType",
    literals={
            EnumerationLiteral(name="FEATURE"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="STRING")
    }
)

ConfigState: Enumeration = Enumeration(
    name="ConfigState",
    literals={
            EnumerationLiteral(name="USER_SELECTED"),
			EnumerationLiteral(name="USER_ELIMINATED"),
			EnumerationLiteral(name="MACHINE_SELECTED"),
			EnumerationLiteral(name="MACHINE_ELIMINATED"),
			EnumerationLiteral(name="UNDECIDED")
    }
)

# Classes
fmp_Reference = Class(name="fmp::Reference")
fmp_TypedValue = Class(name="fmp::TypedValue")
fmp_Feature = Class(name="fmp::Feature")
Clonable = Class(name="Clonable")
fmp_Node = Class(name="fmp::Node", is_abstract=True)
fmp_Constraint = Class(name="fmp::Constraint")
fmp_FeatureGroup = Class(name="fmp::FeatureGroup")
Node = Class(name="Node")
fmp_Project = Class(name="fmp::Project")
fmp_Clonable = Class(name="fmp::Clonable", is_abstract=True)

# fmp_Reference class attributes and methods

# fmp_TypedValue class attributes and methods
fmp_TypedValue_integerValue: Property = Property(name="integerValue", type=StringType)
fmp_TypedValue_stringValue: Property = Property(name="stringValue", type=StringType)
fmp_TypedValue_floatValue: Property = Property(name="floatValue", type=StringType)
fmp_TypedValue.attributes={fmp_TypedValue_stringValue, fmp_TypedValue_integerValue, fmp_TypedValue_floatValue}

# fmp_Feature class attributes and methods
fmp_Feature_name: Property = Property(name="name", type=StringType)
fmp_Feature_valueType: Property = Property(name="valueType", type=StringType)
fmp_Feature.attributes={fmp_Feature_name, fmp_Feature_valueType}

# Clonable class attributes and methods

# fmp_Node class attributes and methods
fmp_Node_id: Property = Property(name="id", type=StringType)
fmp_Node_max: Property = Property(name="max", type=IntegerType)
fmp_Node_min: Property = Property(name="min", type=IntegerType)
fmp_Node.attributes={fmp_Node_id, fmp_Node_min, fmp_Node_max}

# fmp_Constraint class attributes and methods
fmp_Constraint_text: Property = Property(name="text", type=StringType)
fmp_Constraint.attributes={fmp_Constraint_text}

# fmp_FeatureGroup class attributes and methods

# Node class attributes and methods

# fmp_Project class attributes and methods

# fmp_Clonable class attributes and methods
fmp_Clonable_state: Property = Property(name="state", type=StringType)
fmp_Clonable.attributes={fmp_Clonable_state}

# Relationships
references2: BinaryAssociation = BinaryAssociation(
    name="references2",
    ends={
        Property(name="Reference", type=fmp_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=fmp_Reference, multiplicity=Multiplicity(0, 9999))
    }
)
typedValue3: BinaryAssociation = BinaryAssociation(
    name="typedValue3",
    ends={
        Property(name="fmp_TypedValue", type=fmp_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="fmp_Feature4", type=fmp_TypedValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
configurations1: BinaryAssociation = BinaryAssociation(
    name="configurations1",
    ends={
        Property(name="fmp_Feature", type=fmp_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="fmp_Feature0", type=fmp_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
describedNode5: BinaryAssociation = BinaryAssociation(
    name="describedNode5",
    ends={
        Property(name="Node", type=fmp_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="properties", type=fmp_Node, multiplicity=Multiplicity(0, 1))
    }
)
constraints6: BinaryAssociation = BinaryAssociation(
    name="constraints6",
    ends={
        Property(name="fmp_Constraint", type=fmp_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="fmp_Feature7", type=fmp_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
confs9: BinaryAssociation = BinaryAssociation(
    name="confs9",
    ends={
        Property(name="Node10", type=fmp_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="origin", type=fmp_Node, multiplicity=Multiplicity(0, 9999))
    }
)
origin12: BinaryAssociation = BinaryAssociation(
    name="origin12",
    ends={
        Property(name="Node13", type=fmp_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="confs", type=fmp_Node, multiplicity=Multiplicity(0, 1))
    }
)
children15: BinaryAssociation = BinaryAssociation(
    name="children15",
    ends={
        Property(name="fmp_Node", type=fmp_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="fmp_Node14", type=fmp_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prototype33: BinaryAssociation = BinaryAssociation(
    name="prototype33",
    ends={
        Property(name="Clonable34", type=fmp_Clonable, multiplicity=Multiplicity(1, 1)),
        Property(name="clones", type=fmp_Clonable, multiplicity=Multiplicity(0, 1))
    }
)
properties16: BinaryAssociation = BinaryAssociation(
    name="properties16",
    ends={
        Property(name="Feature", type=fmp_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="describedNode", type=fmp_Feature, multiplicity=Multiplicity(0, 1))
    }
)
feature17: BinaryAssociation = BinaryAssociation(
    name="feature17",
    ends={
        Property(name="Feature18", type=fmp_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="references", type=fmp_Feature, multiplicity=Multiplicity(0, 1))
    }
)
model19: BinaryAssociation = BinaryAssociation(
    name="model19",
    ends={
        Property(name="fmp_Feature20", type=fmp_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="fmp_Project", type=fmp_Feature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metaModel21: BinaryAssociation = BinaryAssociation(
    name="metaModel21",
    ends={
        Property(name="fmp_Feature23", type=fmp_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="fmp_Project22", type=fmp_Feature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metaMetaModel24: BinaryAssociation = BinaryAssociation(
    name="metaMetaModel24",
    ends={
        Property(name="fmp_Feature26", type=fmp_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="fmp_Project25", type=fmp_Feature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
featureValue27: BinaryAssociation = BinaryAssociation(
    name="featureValue27",
    ends={
        Property(name="fmp_Feature29", type=fmp_TypedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="fmp_TypedValue28", type=fmp_Feature, multiplicity=Multiplicity(0, 1))
    }
)
clones31: BinaryAssociation = BinaryAssociation(
    name="clones31",
    ends={
        Property(name="Clonable", type=fmp_Clonable, multiplicity=Multiplicity(1, 1)),
        Property(name="prototype", type=fmp_Clonable, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_fmp_Feature_Clonable = Generalization(general=Clonable, specific=fmp_Feature)
gen_fmp_Reference_Clonable = Generalization(general=Clonable, specific=fmp_Reference)
gen_fmp_FeatureGroup_Node = Generalization(general=Node, specific=fmp_FeatureGroup)
gen_fmp_Clonable_Node = Generalization(general=Node, specific=fmp_Clonable)

# Domain Model
domain_model = DomainModel(
    name="fmp",
    types={fmp_Reference, fmp_TypedValue, fmp_Feature, Clonable, fmp_Node, fmp_Constraint, fmp_FeatureGroup, Node, fmp_Project, fmp_Clonable, ValueType, ConfigState},
    associations={references2, typedValue3, configurations1, describedNode5, constraints6, confs9, origin12, children15, prototype33, properties16, feature17, model19, metaModel21, metaMetaModel24, featureValue27, clones31},
    generalizations={gen_fmp_Feature_Clonable, gen_fmp_Reference_Clonable, gen_fmp_FeatureGroup_Node, gen_fmp_Clonable_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
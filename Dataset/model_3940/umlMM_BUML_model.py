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
UmlMM_Classifier = Class(name="UmlMM::Classifier")
UmlMM_UmlPackage = Class(name="UmlMM::UmlPackage")
UmlMM_DataType = Class(name="UmlMM::DataType")
Classifier = Class(name="Classifier")
UmlMM_Class = Class(name="UmlMM::Class")
UmlMM_Operation = Class(name="UmlMM::Operation")
UmlMM_Property = Class(name="UmlMM::Property")
UmlMM_Parameter = Class(name="UmlMM::Parameter")

# UmlMM_Classifier class attributes and methods

# UmlMM_UmlPackage class attributes and methods
UmlMM_UmlPackage_name: Property = Property(name="name", type=StringType)
UmlMM_UmlPackage.attributes={UmlMM_UmlPackage_name}

# UmlMM_DataType class attributes and methods
UmlMM_DataType_name: Property = Property(name="name", type=StringType)
UmlMM_DataType.attributes={UmlMM_DataType_name}

# Classifier class attributes and methods

# UmlMM_Class class attributes and methods
UmlMM_Class_name: Property = Property(name="name", type=StringType)
UmlMM_Class.attributes={UmlMM_Class_name}

# UmlMM_Operation class attributes and methods
UmlMM_Operation_name: Property = Property(name="name", type=StringType)
UmlMM_Operation.attributes={UmlMM_Operation_name}

# UmlMM_Property class attributes and methods
UmlMM_Property_upper: Property = Property(name="upper", type=IntegerType)
UmlMM_Property_lower: Property = Property(name="lower", type=IntegerType)
UmlMM_Property_name: Property = Property(name="name", type=StringType)
UmlMM_Property.attributes={UmlMM_Property_name, UmlMM_Property_upper, UmlMM_Property_lower}

# UmlMM_Parameter class attributes and methods
UmlMM_Parameter_name: Property = Property(name="name", type=StringType)
UmlMM_Parameter.attributes={UmlMM_Parameter_name}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="Classifier", type=UmlMM_UmlPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="_UmlPackage", type=UmlMM_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
_UmlPackage1: BinaryAssociation = BinaryAssociation(
    name="_UmlPackage1",
    ends={
        Property(name="UmlPackage", type=UmlMM_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=UmlMM_UmlPackage, multiplicity=Multiplicity(1, 1))
    }
)
operation2: BinaryAssociation = BinaryAssociation(
    name="operation2",
    ends={
        Property(name="Operation", type=UmlMM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="_Class", type=UmlMM_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
_property3: BinaryAssociation = BinaryAssociation(
    name="_property3",
    ends={
        Property(name="Property", type=UmlMM_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="_Class4", type=UmlMM_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
_Class5: BinaryAssociation = BinaryAssociation(
    name="_Class5",
    ends={
        Property(name="Class", type=UmlMM_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=UmlMM_Class, multiplicity=Multiplicity(1, 1))
    }
)
parameter6: BinaryAssociation = BinaryAssociation(
    name="parameter6",
    ends={
        Property(name="Parameter", type=UmlMM_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="_Operation", type=UmlMM_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="UmlMM_Classifier", type=UmlMM_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="UmlMM_Parameter", type=UmlMM_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
_Operation8: BinaryAssociation = BinaryAssociation(
    name="_Operation8",
    ends={
        Property(name="Operation9", type=UmlMM_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameter", type=UmlMM_Operation, multiplicity=Multiplicity(1, 1))
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="UmlMM_Classifier11", type=UmlMM_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UmlMM_Property", type=UmlMM_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
_Class12: BinaryAssociation = BinaryAssociation(
    name="_Class12",
    ends={
        Property(name="Class13", type=UmlMM_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="_property", type=UmlMM_Class, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_UmlMM_DataType_Classifier = Generalization(general=Classifier, specific=UmlMM_DataType)
gen_UmlMM_Class_Classifier = Generalization(general=Classifier, specific=UmlMM_Class)

# Domain Model
domain_model = DomainModel(
    name="UmlMM",
    types={UmlMM_Classifier, UmlMM_UmlPackage, UmlMM_DataType, Classifier, UmlMM_Class, UmlMM_Operation, UmlMM_Property, UmlMM_Parameter},
    associations={elements0, _UmlPackage1, operation2, _property3, _Class5, parameter6, type7, _Operation8, type10, _Class12},
    generalizations={gen_UmlMM_DataType_Classifier, gen_UmlMM_Class_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
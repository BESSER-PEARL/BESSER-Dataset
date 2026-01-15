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
ModelKind: Enumeration = Enumeration(
    name="ModelKind",
    literals={
            EnumerationLiteral(name="KM3"),
			EnumerationLiteral(name="UML2")
    }
)

ElementKind: Enumeration = Enumeration(
    name="ElementKind",
    literals={
            EnumerationLiteral(name="metamodel"),
			EnumerationLiteral(name="model"),
			EnumerationLiteral(name="package"),
			EnumerationLiteral(name="interface"),
			EnumerationLiteral(name="class")
    }
)

# Classes
Measure_RootMeasureSet = Class(name="Measure::RootMeasureSet")
Measure_Category = Class(name="Measure::Category")
Measure_MeasureSet = Class(name="Measure::MeasureSet")
Measure_Metric = Class(name="Measure::Metric")
Measure_Measure = Class(name="Measure::Measure", is_abstract=True)
Measure_IntegerMeasure = Class(name="Measure::IntegerMeasure")
Measure = Class(name="Measure")
Measure_DoubleMeasure = Class(name="Measure::DoubleMeasure")
Measure_PercentageMeasure = Class(name="Measure::PercentageMeasure")

# Measure_RootMeasureSet class attributes and methods
Measure_RootMeasureSet_modelType: Property = Property(name="modelType", type=StringType)
Measure_RootMeasureSet.attributes={Measure_RootMeasureSet_modelType}

# Measure_Category class attributes and methods
Measure_Category_name: Property = Property(name="name", type=StringType)
Measure_Category_desc: Property = Property(name="desc", type=StringType)
Measure_Category.attributes={Measure_Category_name, Measure_Category_desc}

# Measure_MeasureSet class attributes and methods
Measure_MeasureSet_elementType: Property = Property(name="elementType", type=StringType)
Measure_MeasureSet_elementName: Property = Property(name="elementName", type=StringType)
Measure_MeasureSet.attributes={Measure_MeasureSet_elementType, Measure_MeasureSet_elementName}

# Measure_Metric class attributes and methods
Measure_Metric_name: Property = Property(name="name", type=StringType)
Measure_Metric_desc: Property = Property(name="desc", type=StringType)
Measure_Metric_preferredValue: Property = Property(name="preferredValue", type=StringType)
Measure_Metric.attributes={Measure_Metric_name, Measure_Metric_preferredValue, Measure_Metric_desc}

# Measure_Measure class attributes and methods

# Measure_IntegerMeasure class attributes and methods
Measure_IntegerMeasure_value: Property = Property(name="value", type=StringType)
Measure_IntegerMeasure.attributes={Measure_IntegerMeasure_value}

# Measure class attributes and methods

# Measure_DoubleMeasure class attributes and methods
Measure_DoubleMeasure_value: Property = Property(name="value", type=StringType)
Measure_DoubleMeasure.attributes={Measure_DoubleMeasure_value}

# Measure_PercentageMeasure class attributes and methods
Measure_PercentageMeasure_value: Property = Property(name="value", type=StringType)
Measure_PercentageMeasure.attributes={Measure_PercentageMeasure_value}

# Relationships
categories0: BinaryAssociation = BinaryAssociation(
    name="categories0",
    ends={
        Property(name="Category", type=Measure_RootMeasureSet, multiplicity=Multiplicity(1, 1)),
        Property(name="root", type=Measure_Category, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
measureSets1: BinaryAssociation = BinaryAssociation(
    name="measureSets1",
    ends={
        Property(name="MeasureSet", type=Measure_RootMeasureSet, multiplicity=Multiplicity(1, 1)),
        Property(name="root2", type=Measure_MeasureSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metrics3: BinaryAssociation = BinaryAssociation(
    name="metrics3",
    ends={
        Property(name="Metric", type=Measure_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="category", type=Measure_Metric, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
root4: BinaryAssociation = BinaryAssociation(
    name="root4",
    ends={
        Property(name="RootMeasureSet", type=Measure_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="categories", type=Measure_RootMeasureSet, multiplicity=Multiplicity(1, 1))
    }
)
measures7: BinaryAssociation = BinaryAssociation(
    name="measures7",
    ends={
        Property(name="Measure", type=Measure_MeasureSet, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=Measure_Measure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root8: BinaryAssociation = BinaryAssociation(
    name="root8",
    ends={
        Property(name="RootMeasureSet9", type=Measure_MeasureSet, multiplicity=Multiplicity(1, 1)),
        Property(name="measureSets", type=Measure_RootMeasureSet, multiplicity=Multiplicity(0, 1))
    }
)
subsets11: BinaryAssociation = BinaryAssociation(
    name="subsets11",
    ends={
        Property(name="MeasureSet12", type=Measure_MeasureSet, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=Measure_MeasureSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent14: BinaryAssociation = BinaryAssociation(
    name="parent14",
    ends={
        Property(name="MeasureSet15", type=Measure_MeasureSet, multiplicity=Multiplicity(1, 1)),
        Property(name="subsets", type=Measure_MeasureSet, multiplicity=Multiplicity(0, 1))
    }
)
metric16: BinaryAssociation = BinaryAssociation(
    name="metric16",
    ends={
        Property(name="Measure_Metric", type=Measure_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="Measure_Measure", type=Measure_Metric, multiplicity=Multiplicity(1, 1))
    }
)
owner17: BinaryAssociation = BinaryAssociation(
    name="owner17",
    ends={
        Property(name="MeasureSet18", type=Measure_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="measures", type=Measure_MeasureSet, multiplicity=Multiplicity(1, 1))
    }
)
category5: BinaryAssociation = BinaryAssociation(
    name="category5",
    ends={
        Property(name="Category6", type=Measure_Metric, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics", type=Measure_Category, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Measure_IntegerMeasure_Measure = Generalization(general=Measure, specific=Measure_IntegerMeasure)
gen_Measure_DoubleMeasure_Measure = Generalization(general=Measure, specific=Measure_DoubleMeasure)
gen_Measure_PercentageMeasure_Measure = Generalization(general=Measure, specific=Measure_PercentageMeasure)

# Domain Model
domain_model = DomainModel(
    name="Measure",
    types={Measure_RootMeasureSet, Measure_Category, Measure_MeasureSet, Measure_Metric, Measure_Measure, Measure_IntegerMeasure, Measure, Measure_DoubleMeasure, Measure_PercentageMeasure, ModelKind, ElementKind},
    associations={categories0, measureSets1, metrics3, root4, measures7, root8, subsets11, parent14, metric16, owner17, category5},
    generalizations={gen_Measure_IntegerMeasure_Measure, gen_Measure_DoubleMeasure_Measure, gen_Measure_PercentageMeasure_Measure},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
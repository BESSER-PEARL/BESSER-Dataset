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
benchmark_NamedElement = Class(name="benchmark::NamedElement")
benchmark_Scenario = Class(name="benchmark::Scenario")
NamedElement = Class(name="NamedElement")
benchmark_InputData = Class(name="benchmark::InputData")
benchmark_TestCase = Class(name="benchmark::TestCase")
benchmark_Variant = Class(name="benchmark::Variant")
benchmark_TimeResult = Class(name="benchmark::TimeResult")
benchmark_Property = Class(name="benchmark::Property")

# benchmark_NamedElement class attributes and methods
benchmark_NamedElement_name: Property = Property(name="name", type=StringType)
benchmark_NamedElement.attributes={benchmark_NamedElement_name}

# benchmark_Scenario class attributes and methods

# NamedElement class attributes and methods

# benchmark_InputData class attributes and methods

# benchmark_TestCase class attributes and methods

# benchmark_Variant class attributes and methods

# benchmark_TimeResult class attributes and methods
benchmark_TimeResult_elapsedTime: Property = Property(name="elapsedTime", type=StringType)
benchmark_TimeResult_elapsedMaxTime: Property = Property(name="elapsedMaxTime", type=StringType)
benchmark_TimeResult.attributes={benchmark_TimeResult_elapsedTime, benchmark_TimeResult_elapsedMaxTime}

# benchmark_Property class attributes and methods
benchmark_Property_value: Property = Property(name="value", type=StringType)
benchmark_Property_name: Property = Property(name="name", type=StringType)
benchmark_Property.attributes={benchmark_Property_name, benchmark_Property_value}

# Relationships
properties9: BinaryAssociation = BinaryAssociation(
    name="properties9",
    ends={
        Property(name="benchmark_Property", type=benchmark_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="benchmark_NamedElement", type=benchmark_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variant10: BinaryAssociation = BinaryAssociation(
    name="variant10",
    ends={
        Property(name="Variant", type=benchmark_TimeResult, multiplicity=Multiplicity(1, 1)),
        Property(name="results", type=benchmark_Variant, multiplicity=Multiplicity(0, 1))
    }
)
properties11: BinaryAssociation = BinaryAssociation(
    name="properties11",
    ends={
        Property(name="benchmark_Property13", type=benchmark_TimeResult, multiplicity=Multiplicity(1, 1)),
        Property(name="benchmark_TimeResult12", type=benchmark_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputData0: BinaryAssociation = BinaryAssociation(
    name="inputData0",
    ends={
        Property(name="benchmark_InputData", type=benchmark_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="benchmark_Scenario", type=benchmark_InputData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
testCases1: BinaryAssociation = BinaryAssociation(
    name="testCases1",
    ends={
        Property(name="benchmark_TestCase", type=benchmark_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="benchmark_Scenario2", type=benchmark_TestCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variants3: BinaryAssociation = BinaryAssociation(
    name="variants3",
    ends={
        Property(name="benchmark_Variant", type=benchmark_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="benchmark_Scenario4", type=benchmark_Variant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputData5: BinaryAssociation = BinaryAssociation(
    name="inputData5",
    ends={
        Property(name="InputData", type=benchmark_TestCase, multiplicity=Multiplicity(1, 1)),
        Property(name="tests", type=benchmark_InputData, multiplicity=Multiplicity(0, 1))
    }
)
results6: BinaryAssociation = BinaryAssociation(
    name="results6",
    ends={
        Property(name="benchmark_TimeResult", type=benchmark_TestCase, multiplicity=Multiplicity(1, 1)),
        Property(name="benchmark_TestCase7", type=benchmark_TimeResult, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tests8: BinaryAssociation = BinaryAssociation(
    name="tests8",
    ends={
        Property(name="TestCase", type=benchmark_InputData, multiplicity=Multiplicity(1, 1)),
        Property(name="inputData", type=benchmark_TestCase, multiplicity=Multiplicity(0, 9999))
    }
)
results14: BinaryAssociation = BinaryAssociation(
    name="results14",
    ends={
        Property(name="TimeResult", type=benchmark_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="variant", type=benchmark_TimeResult, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_benchmark_Variant_NamedElement = Generalization(general=NamedElement, specific=benchmark_Variant)
gen_benchmark_Scenario_NamedElement = Generalization(general=NamedElement, specific=benchmark_Scenario)
gen_benchmark_TestCase_NamedElement = Generalization(general=NamedElement, specific=benchmark_TestCase)
gen_benchmark_InputData_NamedElement = Generalization(general=NamedElement, specific=benchmark_InputData)

# Domain Model
domain_model = DomainModel(
    name="benchmark",
    types={benchmark_NamedElement, benchmark_Scenario, NamedElement, benchmark_InputData, benchmark_TestCase, benchmark_Variant, benchmark_TimeResult, benchmark_Property},
    associations={properties9, variant10, properties11, inputData0, testCases1, variants3, inputData5, results6, tests8, results14},
    generalizations={gen_benchmark_Variant_NamedElement, gen_benchmark_Scenario_NamedElement, gen_benchmark_TestCase_NamedElement, gen_benchmark_InputData_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)
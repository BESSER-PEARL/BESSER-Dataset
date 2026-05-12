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
User = Class(name="User")
Count_Steps_and_Calories = Class(name="Count_Steps_and_Calories")
Draw_Path = Class(name="Draw_Path")
Update_Data = Class(name="Update_Data")
Weekly_Chart = Class(name="Weekly_Chart")
Give_Name = Class(name="Give_Name")
Give_Weight = Class(name="Give_Weight")
Count_Steps = Class(name="Count_Steps")
Calculate_caloriesBurnt = Class(name="Calculate_caloriesBurnt")

# User class attributes and methods
User_Name: Property = Property(name="Name", type=StringType)
User_Weight: Property = Property(name="Weight", type=IntegerType)
User_Steps: Property = Property(name="Steps", type=IntegerType)
User_Calories_Burnt: Property = Property(name="Calories_Burnt", type=StringType)
User_Path_Drawn: Property = Property(name="Path_Drawn", type=StringType)
User.attributes={User_Calories_Burnt, User_Steps, User_Weight, User_Path_Drawn, User_Name}

# Count_Steps_and_Calories class attributes and methods
Count_Steps_and_Calories_Name: Property = Property(name="Name", type=StringType)
Count_Steps_and_Calories_Steps: Property = Property(name="Steps", type=IntegerType)
Count_Steps_and_Calories_CaloriesBurnt: Property = Property(name="CaloriesBurnt", type=StringType)
Count_Steps_and_Calories.attributes={Count_Steps_and_Calories_Name, Count_Steps_and_Calories_CaloriesBurnt, Count_Steps_and_Calories_Steps}

# Draw_Path class attributes and methods
Draw_Path_Name: Property = Property(name="Name", type=StringType)
Draw_Path_Route: Property = Property(name="Route", type=StringType)
Draw_Path.attributes={Draw_Path_Route, Draw_Path_Name}

# Update_Data class attributes and methods
Update_Data_Name: Property = Property(name="Name", type=StringType)
Update_Data_Weight: Property = Property(name="Weight", type=IntegerType)
Update_Data.attributes={Update_Data_Name, Update_Data_Weight}

# Weekly_Chart class attributes and methods
Weekly_Chart_Name: Property = Property(name="Name", type=StringType)
Weekly_Chart_CaloriesBurnt: Property = Property(name="CaloriesBurnt", type=StringType)
Weekly_Chart_Steps: Property = Property(name="Steps", type=IntegerType)
Weekly_Chart.attributes={Weekly_Chart_Name, Weekly_Chart_Steps, Weekly_Chart_CaloriesBurnt}

# Give_Name class attributes and methods
Give_Name_Name: Property = Property(name="Name", type=StringType)
Give_Name.attributes={Give_Name_Name}

# Give_Weight class attributes and methods
Give_Weight_Weight: Property = Property(name="Weight", type=IntegerType)
Give_Weight.attributes={Give_Weight_Weight}

# Count_Steps class attributes and methods
Count_Steps_Steps: Property = Property(name="Steps", type=IntegerType)
Count_Steps.attributes={Count_Steps_Steps}

# Calculate_caloriesBurnt class attributes and methods
Calculate_caloriesBurnt_Name: Property = Property(name="Name", type=StringType)
Calculate_caloriesBurnt_CaloriesBurnt: Property = Property(name="CaloriesBurnt", type=StringType)
Calculate_caloriesBurnt_Steps: Property = Property(name="Steps", type=IntegerType)
Calculate_caloriesBurnt.attributes={Calculate_caloriesBurnt_CaloriesBurnt, Calculate_caloriesBurnt_Name, Calculate_caloriesBurnt_Steps}

# Relationships
Count_Steps_and_Calories__Count_Steps: BinaryAssociation = BinaryAssociation(
    name="Count_Steps_and_Calories__Count_Steps",
    ends={
        Property(name="count_Steps0", type=Count_Steps, multiplicity=Multiplicity(0, 1)),
        Property(name="count_Steps_and_Calories1", type=Count_Steps_and_Calories, multiplicity=Multiplicity(0, 1))
    }
)
Count_Steps_and_Calories__Calculate_caloriesBurnt: BinaryAssociation = BinaryAssociation(
    name="Count_Steps_and_Calories__Calculate_caloriesBurnt",
    ends={
        Property(name="calculate_caloriesBurnt2", type=Calculate_caloriesBurnt, multiplicity=Multiplicity(0, 1)),
        Property(name="count_Steps_and_Calories3", type=Count_Steps_and_Calories, multiplicity=Multiplicity(0, 1))
    }
)
Update_Data__Give_Name: BinaryAssociation = BinaryAssociation(
    name="Update_Data__Give_Name",
    ends={
        Property(name="give_Name4", type=Give_Name, multiplicity=Multiplicity(0, 1)),
        Property(name="update_Data5", type=Update_Data, multiplicity=Multiplicity(0, 1))
    }
)
Update_Data__Give_Weight: BinaryAssociation = BinaryAssociation(
    name="Update_Data__Give_Weight",
    ends={
        Property(name="give_Weight6", type=Give_Weight, multiplicity=Multiplicity(0, 1)),
        Property(name="update_Data7", type=Update_Data, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_VcWEgAB9EeiLEbIzy5aHfg",
    types={User, Count_Steps_and_Calories, Draw_Path, Update_Data, Weekly_Chart, Give_Name, Give_Weight, Count_Steps, Calculate_caloriesBurnt},
    associations={Count_Steps_and_Calories__Count_Steps, Count_Steps_and_Calories__Calculate_caloriesBurnt, Update_Data__Give_Name, Update_Data__Give_Weight},
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
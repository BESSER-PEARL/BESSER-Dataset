





import java.util.List;
import java.util.ArrayList;

public class gsml_Task  {

    private float MinRequirement;
    private String Name;
    private String MinRequirementType;





    private gsml_Grading gsml_grading;




    private gsml_Grading gsml_grading;


    public gsml_Task(
        float MinRequirement,        String Name,        String MinRequirementType    ) {
        this.MinRequirement = MinRequirement;
        this.Name = Name;
        this.MinRequirementType = MinRequirementType;
    }


    public float getMinrequirement() {
        return MinRequirement;
    }

    public void setMinrequirement(float MinRequirement) {
        this.MinRequirement = MinRequirement;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getMinrequirementtype() {
        return MinRequirementType;
    }

    public void setMinrequirementtype(String MinRequirementType) {
        this.MinRequirementType = MinRequirementType;
    }

    public gsml_Grading getGsml_grading() {
        return gsml_grading;
    }

    public void setGsml_grading(gsml_Grading gsml_grading) {
        this.gsml_grading = gsml_grading;
    }
    public gsml_Grading getGsml_grading() {
        return gsml_grading;
    }

    public void setGsml_grading(gsml_Grading gsml_grading) {
        this.gsml_grading = gsml_grading;
    }

}
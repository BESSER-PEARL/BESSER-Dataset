





import java.util.List;
import java.util.ArrayList;

public class gsml_Task  {

    private String Name;
    private float MinRequirement;
    private String MinRequirementType;





    private gsml_Grading gsml_grading;




    private gsml_Grading gsml_grading;


    public gsml_Task(
        String Name,        float MinRequirement,        String MinRequirementType    ) {
        this.Name = Name;
        this.MinRequirement = MinRequirement;
        this.MinRequirementType = MinRequirementType;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public float getMinrequirement() {
        return MinRequirement;
    }

    public void setMinrequirement(float MinRequirement) {
        this.MinRequirement = MinRequirement;
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
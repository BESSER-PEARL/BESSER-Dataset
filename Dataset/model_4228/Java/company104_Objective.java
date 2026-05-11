





import java.util.List;
import java.util.ArrayList;

public class company104_Objective  {

    private float value;
    private String type;
    private String nature;





    private company104_ObjectiveReach company104_objectivereach;




    private company104_Goal company104_goal;


    public company104_Objective(
        float value,        String type,        String nature    ) {
        this.value = value;
        this.type = type;
        this.nature = nature;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getNature() {
        return nature;
    }

    public void setNature(String nature) {
        this.nature = nature;
    }

    public company104_ObjectiveReach getCompany104_objectivereach() {
        return company104_objectivereach;
    }

    public void setCompany104_objectivereach(company104_ObjectiveReach company104_objectivereach) {
        this.company104_objectivereach = company104_objectivereach;
    }
    public company104_Goal getCompany104_goal() {
        return company104_goal;
    }

    public void setCompany104_goal(company104_Goal company104_goal) {
        this.company104_goal = company104_goal;
    }

}
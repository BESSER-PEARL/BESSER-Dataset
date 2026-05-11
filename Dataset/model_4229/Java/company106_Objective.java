





import java.util.List;
import java.util.ArrayList;

public class company106_Objective  {

    private String nature;
    private float value;
    private String type;





    private company106_Goal company106_goal;


    public company106_Objective(
        String nature,        float value,        String type    ) {
        this.nature = nature;
        this.value = value;
        this.type = type;
    }


    public String getNature() {
        return nature;
    }

    public void setNature(String nature) {
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

    public company106_Goal getCompany106_goal() {
        return company106_goal;
    }

    public void setCompany106_goal(company106_Goal company106_goal) {
        this.company106_goal = company106_goal;
    }

}
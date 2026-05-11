





import java.util.List;
import java.util.ArrayList;

public class giraffeDSL_StressRangeType  {

    private String many;
    private String name;
    private String type;





    private giraffeDSL_Stress giraffedsl_stress;


    public giraffeDSL_StressRangeType(
        String many,        String name,        String type    ) {
        this.many = many;
        this.name = name;
        this.type = type;
    }


    public String getMany() {
        return many;
    }

    public void setMany(String many) {
        this.many = many;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public giraffeDSL_Stress getGiraffedsl_stress() {
        return giraffedsl_stress;
    }

    public void setGiraffedsl_stress(giraffeDSL_Stress giraffedsl_stress) {
        this.giraffedsl_stress = giraffedsl_stress;
    }

}
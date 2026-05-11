





import java.util.List;
import java.util.ArrayList;

public class giraffeDSL_StressClassType  {

    private String type;
    private String name;
    private String many;





    private giraffeDSL_Stress giraffedsl_stress;


    public giraffeDSL_StressClassType(
        String type,        String name,        String many    ) {
        this.type = type;
        this.name = name;
        this.many = many;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMany() {
        return many;
    }

    public void setMany(String many) {
        this.many = many;
    }

    public giraffeDSL_Stress getGiraffedsl_stress() {
        return giraffedsl_stress;
    }

    public void setGiraffedsl_stress(giraffeDSL_Stress giraffedsl_stress) {
        this.giraffedsl_stress = giraffedsl_stress;
    }

}
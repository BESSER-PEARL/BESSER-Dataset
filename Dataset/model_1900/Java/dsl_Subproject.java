





import java.util.List;
import java.util.ArrayList;

public class dsl_Subproject  {

    private String name;





    private dsl_JeeProject dsl_jeeproject;


    public dsl_Subproject(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_JeeProject getDsl_jeeproject() {
        return dsl_jeeproject;
    }

    public void setDsl_jeeproject(dsl_JeeProject dsl_jeeproject) {
        this.dsl_jeeproject = dsl_jeeproject;
    }

}
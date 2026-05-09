





import java.util.List;
import java.util.ArrayList;

public class dsl_Descriptor  {

    private String name;





    private dsl_Subproject dsl_subproject;


    public dsl_Descriptor(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_Subproject getDsl_subproject() {
        return dsl_subproject;
    }

    public void setDsl_subproject(dsl_Subproject dsl_subproject) {
        this.dsl_subproject = dsl_subproject;
    }

}
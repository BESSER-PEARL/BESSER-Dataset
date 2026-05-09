





import java.util.List;
import java.util.ArrayList;

public class dsl_Library  {

    private String name;
    private String isNative;





    private dsl_Subproject dsl_subproject;


    public dsl_Library(
        String name,        String isNative    ) {
        this.name = name;
        this.isNative = isNative;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIsnative() {
        return isNative;
    }

    public void setIsnative(String isNative) {
        this.isNative = isNative;
    }

    public dsl_Subproject getDsl_subproject() {
        return dsl_subproject;
    }

    public void setDsl_subproject(dsl_Subproject dsl_subproject) {
        this.dsl_subproject = dsl_subproject;
    }

}
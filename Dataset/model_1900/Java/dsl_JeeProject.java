





import java.util.List;
import java.util.ArrayList;

public class dsl_JeeProject  {

    private String name;





    private dsl_JavaApp dsl_javaapp;


    public dsl_JeeProject(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_JavaApp getDsl_javaapp() {
        return dsl_javaapp;
    }

    public void setDsl_javaapp(dsl_JavaApp dsl_javaapp) {
        this.dsl_javaapp = dsl_javaapp;
    }

}
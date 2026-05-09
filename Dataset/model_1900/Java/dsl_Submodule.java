





import java.util.List;
import java.util.ArrayList;

public class dsl_Submodule  {

    private String name;





    private dsl_Module dsl_module;


    public dsl_Submodule(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_Module getDsl_module() {
        return dsl_module;
    }

    public void setDsl_module(dsl_Module dsl_module) {
        this.dsl_module = dsl_module;
    }

}
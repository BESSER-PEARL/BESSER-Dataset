





import java.util.List;
import java.util.ArrayList;

public class dsl_Operation  {

    private String type;





    private dsl_Submodule dsl_submodule;


    public dsl_Operation(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public dsl_Submodule getDsl_submodule() {
        return dsl_submodule;
    }

    public void setDsl_submodule(dsl_Submodule dsl_submodule) {
        this.dsl_submodule = dsl_submodule;
    }

}
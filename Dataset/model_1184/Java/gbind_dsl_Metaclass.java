





import java.util.List;
import java.util.ArrayList;

public class gbind_dsl_Metaclass  {

    private String name;





    private dsl_gbind_EClass dsl_gbind_eclass;


    public gbind_dsl_Metaclass(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_gbind_EClass getDsl_gbind_eclass() {
        return dsl_gbind_eclass;
    }

    public void setDsl_gbind_eclass(dsl_gbind_EClass dsl_gbind_eclass) {
        this.dsl_gbind_eclass = dsl_gbind_eclass;
    }

}
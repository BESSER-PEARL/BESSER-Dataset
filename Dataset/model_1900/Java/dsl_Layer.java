





import java.util.List;
import java.util.ArrayList;

public class dsl_Layer  {

    private String name;





    private dsl_Component dsl_component;


    public dsl_Layer(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_Component getDsl_component() {
        return dsl_component;
    }

    public void setDsl_component(dsl_Component dsl_component) {
        this.dsl_component = dsl_component;
    }

}
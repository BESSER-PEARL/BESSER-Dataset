





import java.util.List;
import java.util.ArrayList;

public class dslComponent_Port  {

    private String name;





    private dslComponent_Component dslcomponent_component;


    public dslComponent_Port(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dslComponent_Component getDslcomponent_component() {
        return dslcomponent_component;
    }

    public void setDslcomponent_component(dslComponent_Component dslcomponent_component) {
        this.dslcomponent_component = dslcomponent_component;
    }

}
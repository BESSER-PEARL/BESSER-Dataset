





import java.util.List;
import java.util.ArrayList;

public class dslComponent_Component  {

    private String name;
    private String id;





    private dslComponent_Subsystem dslcomponent_subsystem;


    public dslComponent_Component(
        String name,        String id    ) {
        this.name = name;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public dslComponent_Subsystem getDslcomponent_subsystem() {
        return dslcomponent_subsystem;
    }

    public void setDslcomponent_subsystem(dslComponent_Subsystem dslcomponent_subsystem) {
        this.dslcomponent_subsystem = dslcomponent_subsystem;
    }

}
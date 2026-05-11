





import java.util.List;
import java.util.ArrayList;

public class dslComponent_ControlSubsystem  {

    private String name;





    private dslComponent_Subsystem dslcomponent_subsystem;


    public dslComponent_ControlSubsystem(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dslComponent_Subsystem getDslcomponent_subsystem() {
        return dslcomponent_subsystem;
    }

    public void setDslcomponent_subsystem(dslComponent_Subsystem dslcomponent_subsystem) {
        this.dslcomponent_subsystem = dslcomponent_subsystem;
    }

}
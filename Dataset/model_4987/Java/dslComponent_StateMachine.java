





import java.util.List;
import java.util.ArrayList;

public class dslComponent_StateMachine  {

    private String name;





    private dslComponent_ControlSubsystem dslcomponent_controlsubsystem;




    private dslComponent_Component dslcomponent_component;


    public dslComponent_StateMachine(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dslComponent_ControlSubsystem getDslcomponent_controlsubsystem() {
        return dslcomponent_controlsubsystem;
    }

    public void setDslcomponent_controlsubsystem(dslComponent_ControlSubsystem dslcomponent_controlsubsystem) {
        this.dslcomponent_controlsubsystem = dslcomponent_controlsubsystem;
    }
    public dslComponent_Component getDslcomponent_component() {
        return dslcomponent_component;
    }

    public void setDslcomponent_component(dslComponent_Component dslcomponent_component) {
        this.dslcomponent_component = dslcomponent_component;
    }

}
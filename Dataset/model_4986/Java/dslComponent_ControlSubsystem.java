





import java.util.List;
import java.util.ArrayList;

public class dslComponent_ControlSubsystem  {

    private String name;





    private dslComponent_Subsystem dslcomponent_subsystem;




    private List<dslComponent_StateMachine> dslcomponent_statemachines;


    public dslComponent_ControlSubsystem(
        String name    ) {
        this.name = name;
        this.dslcomponent_statemachines = new ArrayList<>();
    }

    public dslComponent_ControlSubsystem(
        String name        ArrayList<dslComponent_StateMachine> dslcomponent_statemachines    ) {
        this.name = name;
        this.dslcomponent_statemachines = dslcomponent_statemachines;
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
    public List<dslComponent_StateMachine> getDslcomponent_statemachines() {
        return dslcomponent_statemachines;
    }

    public void addDslcomponent_statemachine(Dslcomponent_statemachine dslcomponent_statemachine) {
        this.dslcomponent_statemachines.add(dslcomponent_statemachine);
    }

}
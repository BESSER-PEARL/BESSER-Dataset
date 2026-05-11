





import java.util.List;
import java.util.ArrayList;

public class dslComponent_Component  {

    private String id;
    private String name;





    private dslComponent_Subsystem dslcomponent_subsystem;




    private List<dslComponent_StateMachine> dslcomponent_statemachines;


    public dslComponent_Component(
        String id,        String name    ) {
        this.id = id;
        this.name = name;
        this.dslcomponent_statemachines = new ArrayList<>();
    }

    public dslComponent_Component(
        String id,        String name        ArrayList<dslComponent_StateMachine> dslcomponent_statemachines    ) {
        this.id = id;
        this.name = name;
        this.dslcomponent_statemachines = dslcomponent_statemachines;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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
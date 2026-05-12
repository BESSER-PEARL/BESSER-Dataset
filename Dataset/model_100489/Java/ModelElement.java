





import java.util.List;
import java.util.ArrayList;

public class ModelElement  {






    private Core_Namespace core_namespace;




    private State_Machines_StateMachine state_machines_statemachine;


    public ModelElement(
    ) {
    }



    public Core_Namespace getCore_namespace() {
        return core_namespace;
    }

    public void setCore_namespace(Core_Namespace core_namespace) {
        this.core_namespace = core_namespace;
    }
    public State_Machines_StateMachine getState_machines_statemachine() {
        return state_machines_statemachine;
    }

    public void setState_machines_statemachine(State_Machines_StateMachine state_machines_statemachine) {
        this.state_machines_statemachine = state_machines_statemachine;
    }

}
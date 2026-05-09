





import java.util.List;
import java.util.ArrayList;

public class metaModelStateMachine_state  {






    private List<metaModelStateMachine_StateMachine> metamodelstatemachine_statemachines;




    private metaModelStateMachine_StateMachine metamodelstatemachine_statemachine;


    public metaModelStateMachine_state(
    ) {
        this.metamodelstatemachine_statemachines = new ArrayList<>();
    }

    public metaModelStateMachine_state(
        ArrayList<metaModelStateMachine_StateMachine> metamodelstatemachine_statemachines    ) {
        this.metamodelstatemachine_statemachines = metamodelstatemachine_statemachines;
    }


    public List<metaModelStateMachine_StateMachine> getMetamodelstatemachine_statemachines() {
        return metamodelstatemachine_statemachines;
    }

    public void addMetamodelstatemachine_statemachine(Metamodelstatemachine_statemachine metamodelstatemachine_statemachine) {
        this.metamodelstatemachine_statemachines.add(metamodelstatemachine_statemachine);
    }
    public metaModelStateMachine_StateMachine getMetamodelstatemachine_statemachine() {
        return metamodelstatemachine_statemachine;
    }

    public void setMetamodelstatemachine_statemachine(metaModelStateMachine_StateMachine metamodelstatemachine_statemachine) {
        this.metamodelstatemachine_statemachine = metamodelstatemachine_statemachine;
    }

}
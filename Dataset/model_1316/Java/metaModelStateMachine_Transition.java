





import java.util.List;
import java.util.ArrayList;

public class metaModelStateMachine_Transition  {






    private metaModelStateMachine_state metamodelstatemachine_state;




    private metaModelStateMachine_StateMachine metamodelstatemachine_statemachine;




    private List<metaModelStateMachine_StateMachine> metamodelstatemachine_statemachines;




    private metaModelStateMachine_state metamodelstatemachine_state;




    private metaModelStateMachine_state metamodelstatemachine_state;


    public metaModelStateMachine_Transition(
    ) {
        this.metamodelstatemachine_statemachines = new ArrayList<>();
    }

    public metaModelStateMachine_Transition(
        ArrayList<metaModelStateMachine_StateMachine> metamodelstatemachine_statemachines    ) {
        this.metamodelstatemachine_statemachines = metamodelstatemachine_statemachines;
    }


    public metaModelStateMachine_state getMetamodelstatemachine_state() {
        return metamodelstatemachine_state;
    }

    public void setMetamodelstatemachine_state(metaModelStateMachine_state metamodelstatemachine_state) {
        this.metamodelstatemachine_state = metamodelstatemachine_state;
    }
    public metaModelStateMachine_StateMachine getMetamodelstatemachine_statemachine() {
        return metamodelstatemachine_statemachine;
    }

    public void setMetamodelstatemachine_statemachine(metaModelStateMachine_StateMachine metamodelstatemachine_statemachine) {
        this.metamodelstatemachine_statemachine = metamodelstatemachine_statemachine;
    }
    public List<metaModelStateMachine_StateMachine> getMetamodelstatemachine_statemachines() {
        return metamodelstatemachine_statemachines;
    }

    public void addMetamodelstatemachine_statemachine(Metamodelstatemachine_statemachine metamodelstatemachine_statemachine) {
        this.metamodelstatemachine_statemachines.add(metamodelstatemachine_statemachine);
    }
    public metaModelStateMachine_state getMetamodelstatemachine_state() {
        return metamodelstatemachine_state;
    }

    public void setMetamodelstatemachine_state(metaModelStateMachine_state metamodelstatemachine_state) {
        this.metamodelstatemachine_state = metamodelstatemachine_state;
    }
    public metaModelStateMachine_state getMetamodelstatemachine_state() {
        return metamodelstatemachine_state;
    }

    public void setMetamodelstatemachine_state(metaModelStateMachine_state metamodelstatemachine_state) {
        this.metamodelstatemachine_state = metamodelstatemachine_state;
    }

}
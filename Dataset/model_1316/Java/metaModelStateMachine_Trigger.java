





import java.util.List;
import java.util.ArrayList;

public class metaModelStateMachine_Trigger  {






    private metaModelStateMachine_Transition metamodelstatemachine_transition;




    private List<metaModelStateMachine_Transition> metamodelstatemachine_transitions;


    public metaModelStateMachine_Trigger(
    ) {
        this.metamodelstatemachine_transitions = new ArrayList<>();
    }

    public metaModelStateMachine_Trigger(
        ArrayList<metaModelStateMachine_Transition> metamodelstatemachine_transitions    ) {
        this.metamodelstatemachine_transitions = metamodelstatemachine_transitions;
    }


    public metaModelStateMachine_Transition getMetamodelstatemachine_transition() {
        return metamodelstatemachine_transition;
    }

    public void setMetamodelstatemachine_transition(metaModelStateMachine_Transition metamodelstatemachine_transition) {
        this.metamodelstatemachine_transition = metamodelstatemachine_transition;
    }
    public List<metaModelStateMachine_Transition> getMetamodelstatemachine_transitions() {
        return metamodelstatemachine_transitions;
    }

    public void addMetamodelstatemachine_transition(Metamodelstatemachine_transition metamodelstatemachine_transition) {
        this.metamodelstatemachine_transitions.add(metamodelstatemachine_transition);
    }

}
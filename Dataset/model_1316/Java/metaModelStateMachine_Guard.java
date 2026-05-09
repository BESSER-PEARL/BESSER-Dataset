





import java.util.List;
import java.util.ArrayList;

public class metaModelStateMachine_Guard  {






    private List<metaModelStateMachine_Transition> metamodelstatemachine_transitions;




    private metaModelStateMachine_Transition metamodelstatemachine_transition;


    public metaModelStateMachine_Guard(
    ) {
        this.metamodelstatemachine_transitions = new ArrayList<>();
    }

    public metaModelStateMachine_Guard(
        ArrayList<metaModelStateMachine_Transition> metamodelstatemachine_transitions    ) {
        this.metamodelstatemachine_transitions = metamodelstatemachine_transitions;
    }


    public List<metaModelStateMachine_Transition> getMetamodelstatemachine_transitions() {
        return metamodelstatemachine_transitions;
    }

    public void addMetamodelstatemachine_transition(Metamodelstatemachine_transition metamodelstatemachine_transition) {
        this.metamodelstatemachine_transitions.add(metamodelstatemachine_transition);
    }
    public metaModelStateMachine_Transition getMetamodelstatemachine_transition() {
        return metamodelstatemachine_transition;
    }

    public void setMetamodelstatemachine_transition(metaModelStateMachine_Transition metamodelstatemachine_transition) {
        this.metamodelstatemachine_transition = metamodelstatemachine_transition;
    }

}
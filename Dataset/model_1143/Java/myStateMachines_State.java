





import java.util.List;
import java.util.ArrayList;

public class myStateMachines_State  {

    private String name;
    private String actions;





    private myStateMachines_Statemachine mystatemachines_statemachine;




    private myStateMachines_Statemachine mystatemachines_statemachine;




    private List<myStateMachines_Transition> mystatemachines_transitions;




    private myStateMachines_Transition mystatemachines_transition;


    public myStateMachines_State(
        String name,        String actions    ) {
        this.name = name;
        this.actions = actions;
        this.mystatemachines_transitions = new ArrayList<>();
    }

    public myStateMachines_State(
        String name,        String actions        ArrayList<myStateMachines_Transition> mystatemachines_transitions    ) {
        this.name = name;
        this.actions = actions;
        this.mystatemachines_transitions = mystatemachines_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getActions() {
        return actions;
    }

    public void setActions(String actions) {
        this.actions = actions;
    }

    public myStateMachines_Statemachine getMystatemachines_statemachine() {
        return mystatemachines_statemachine;
    }

    public void setMystatemachines_statemachine(myStateMachines_Statemachine mystatemachines_statemachine) {
        this.mystatemachines_statemachine = mystatemachines_statemachine;
    }
    public myStateMachines_Statemachine getMystatemachines_statemachine() {
        return mystatemachines_statemachine;
    }

    public void setMystatemachines_statemachine(myStateMachines_Statemachine mystatemachines_statemachine) {
        this.mystatemachines_statemachine = mystatemachines_statemachine;
    }
    public List<myStateMachines_Transition> getMystatemachines_transitions() {
        return mystatemachines_transitions;
    }

    public void addMystatemachines_transition(Mystatemachines_transition mystatemachines_transition) {
        this.mystatemachines_transitions.add(mystatemachines_transition);
    }
    public myStateMachines_Transition getMystatemachines_transition() {
        return mystatemachines_transition;
    }

    public void setMystatemachines_transition(myStateMachines_Transition mystatemachines_transition) {
        this.mystatemachines_transition = mystatemachines_transition;
    }

}
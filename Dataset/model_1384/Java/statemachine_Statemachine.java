





import java.util.List;
import java.util.ArrayList;

public class statemachine_Statemachine extends Region {

    private String name;





    private List<statemachine_Transition> statemachine_transitions;


    public statemachine_Statemachine(
        String name    ) {
        super(
        );
        this.name = name;
        this.statemachine_transitions = new ArrayList<>();
    }

    public statemachine_Statemachine(
        String name        ArrayList<statemachine_Transition> statemachine_transitions    ) {
        this.name = name;
        this.statemachine_transitions = statemachine_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<statemachine_Transition> getStatemachine_transitions() {
        return statemachine_transitions;
    }

    public void addStatemachine_transition(Statemachine_transition statemachine_transition) {
        this.statemachine_transitions.add(statemachine_transition);
    }

}
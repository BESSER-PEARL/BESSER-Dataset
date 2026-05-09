




import java.util.UUID;

import java.util.List;
import java.util.ArrayList;

public class statemachine_Statechart  {

    private String UUID;
    private String name;





    private List<statemachine_Transition> statemachine_transitions;


    public statemachine_Statechart(
        String UUID,        String name    ) {
        this.UUID = UUID;
        this.name = name;
        this.statemachine_transitions = new ArrayList<>();
    }

    public statemachine_Statechart(
        String UUID,        String name        ArrayList<statemachine_Transition> statemachine_transitions    ) {
        this.UUID = UUID;
        this.name = name;
        this.statemachine_transitions = statemachine_transitions;
    }

    public String getUuid() {
        return UUID;
    }

    public void setUuid(String UUID) {
        this.UUID = UUID;
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
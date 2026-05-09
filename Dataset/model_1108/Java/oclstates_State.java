





import java.util.List;
import java.util.ArrayList;

public class oclstates_State  {

    private String name;
    private boolean initial;





    private oclstates_Statemachine oclstates_statemachine;




    private oclstates_Statemachine oclstates_statemachine;




    private List<oclstates_Transition> oclstates_transitions;




    private oclstates_Transition oclstates_transition;


    public oclstates_State(
        String name,        boolean initial    ) {
        this.name = name;
        this.initial = initial;
        this.oclstates_transitions = new ArrayList<>();
    }

    public oclstates_State(
        String name,        boolean initial        ArrayList<oclstates_Transition> oclstates_transitions    ) {
        this.name = name;
        this.initial = initial;
        this.oclstates_transitions = oclstates_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }

    public oclstates_Statemachine getOclstates_statemachine() {
        return oclstates_statemachine;
    }

    public void setOclstates_statemachine(oclstates_Statemachine oclstates_statemachine) {
        this.oclstates_statemachine = oclstates_statemachine;
    }
    public oclstates_Statemachine getOclstates_statemachine() {
        return oclstates_statemachine;
    }

    public void setOclstates_statemachine(oclstates_Statemachine oclstates_statemachine) {
        this.oclstates_statemachine = oclstates_statemachine;
    }
    public List<oclstates_Transition> getOclstates_transitions() {
        return oclstates_transitions;
    }

    public void addOclstates_transition(Oclstates_transition oclstates_transition) {
        this.oclstates_transitions.add(oclstates_transition);
    }
    public oclstates_Transition getOclstates_transition() {
        return oclstates_transition;
    }

    public void setOclstates_transition(oclstates_Transition oclstates_transition) {
        this.oclstates_transition = oclstates_transition;
    }

}
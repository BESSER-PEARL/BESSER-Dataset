





import java.util.List;
import java.util.ArrayList;

public class gfsm_FSM  {

    private String name;





    private gfsm_Transition gfsm_transition;




    private List<gfsm_Transition> gfsm_transitions;


    public gfsm_FSM(
        String name    ) {
        this.name = name;
        this.gfsm_transitions = new ArrayList<>();
    }

    public gfsm_FSM(
        String name        ArrayList<gfsm_Transition> gfsm_transitions    ) {
        this.name = name;
        this.gfsm_transitions = gfsm_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public gfsm_Transition getGfsm_transition() {
        return gfsm_transition;
    }

    public void setGfsm_transition(gfsm_Transition gfsm_transition) {
        this.gfsm_transition = gfsm_transition;
    }
    public List<gfsm_Transition> getGfsm_transitions() {
        return gfsm_transitions;
    }

    public void addGfsm_transition(Gfsm_transition gfsm_transition) {
        this.gfsm_transitions.add(gfsm_transition);
    }

}
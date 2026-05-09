





import java.util.List;
import java.util.ArrayList;

public class gfsm_State  {

    private String name;





    private gfsm_FSM gfsm_fsm;




    private gfsm_FSM gfsm_fsm;




    private gfsm_Transition gfsm_transition;




    private gfsm_Transition gfsm_transition;




    private List<gfsm_Transition> gfsm_transitions;




    private gfsm_FSM gfsm_fsm;




    private List<gfsm_Transition> gfsm_transitions;


    public gfsm_State(
        String name    ) {
        this.name = name;
        this.gfsm_transitions = new ArrayList<>();
        this.gfsm_transitions = new ArrayList<>();
    }

    public gfsm_State(
        String name        ArrayList<gfsm_Transition> gfsm_transitions,        ArrayList<gfsm_Transition> gfsm_transitions    ) {
        this.name = name;
        this.gfsm_transitions = gfsm_transitions;
        this.gfsm_transitions = gfsm_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public gfsm_FSM getGfsm_fsm() {
        return gfsm_fsm;
    }

    public void setGfsm_fsm(gfsm_FSM gfsm_fsm) {
        this.gfsm_fsm = gfsm_fsm;
    }
    public gfsm_FSM getGfsm_fsm() {
        return gfsm_fsm;
    }

    public void setGfsm_fsm(gfsm_FSM gfsm_fsm) {
        this.gfsm_fsm = gfsm_fsm;
    }
    public gfsm_Transition getGfsm_transition() {
        return gfsm_transition;
    }

    public void setGfsm_transition(gfsm_Transition gfsm_transition) {
        this.gfsm_transition = gfsm_transition;
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
    public gfsm_FSM getGfsm_fsm() {
        return gfsm_fsm;
    }

    public void setGfsm_fsm(gfsm_FSM gfsm_fsm) {
        this.gfsm_fsm = gfsm_fsm;
    }
    public List<gfsm_Transition> getGfsm_transitions() {
        return gfsm_transitions;
    }

    public void addGfsm_transition(Gfsm_transition gfsm_transition) {
        this.gfsm_transitions.add(gfsm_transition);
    }

}
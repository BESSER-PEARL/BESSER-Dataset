





import java.util.List;
import java.util.ArrayList;

public class gfsm_State  {

    private String name;





    private List<gfsm_Transition> gfsm_transitions;




    private List<gfsm_Transition> gfsm_transitions;




    private gfsm_Machine gfsm_machine;




    private gfsm_Transition gfsm_transition;




    private gfsm_Transition gfsm_transition;




    private gfsm_Machine gfsm_machine;


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

    public List<gfsm_Transition> getGfsm_transitions() {
        return gfsm_transitions;
    }

    public void addGfsm_transition(Gfsm_transition gfsm_transition) {
        this.gfsm_transitions.add(gfsm_transition);
    }
    public List<gfsm_Transition> getGfsm_transitions() {
        return gfsm_transitions;
    }

    public void addGfsm_transition(Gfsm_transition gfsm_transition) {
        this.gfsm_transitions.add(gfsm_transition);
    }
    public gfsm_Machine getGfsm_machine() {
        return gfsm_machine;
    }

    public void setGfsm_machine(gfsm_Machine gfsm_machine) {
        this.gfsm_machine = gfsm_machine;
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
    public gfsm_Machine getGfsm_machine() {
        return gfsm_machine;
    }

    public void setGfsm_machine(gfsm_Machine gfsm_machine) {
        this.gfsm_machine = gfsm_machine;
    }

}
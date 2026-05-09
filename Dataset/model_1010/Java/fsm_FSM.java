





import java.util.List;
import java.util.ArrayList;

public class fsm_FSM  {

    private String name;





    private List<fsm_Transition> fsm_transitions;


    public fsm_FSM(
        String name    ) {
        this.name = name;
        this.fsm_transitions = new ArrayList<>();
    }

    public fsm_FSM(
        String name        ArrayList<fsm_Transition> fsm_transitions    ) {
        this.name = name;
        this.fsm_transitions = fsm_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<fsm_Transition> getFsm_transitions() {
        return fsm_transitions;
    }

    public void addFsm_transition(Fsm_transition fsm_transition) {
        this.fsm_transitions.add(fsm_transition);
    }

}
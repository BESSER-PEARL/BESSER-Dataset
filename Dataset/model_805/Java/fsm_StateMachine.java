





import java.util.List;
import java.util.ArrayList;

public class fsm_StateMachine extends NamedElement {

    private String producedString;
    private String unprocessedString;
    private String consummedString;





    private List<fsm_Transition> fsm_transitions;




    private List<fsm_State> fsm_states;




    private fsm_State fsm_state;




    private fsm_State fsm_state;




    private fsm_State fsm_state;


    public fsm_StateMachine(
        String producedString,        String unprocessedString,        String consummedString    ) {
        super(
        );
        this.producedString = producedString;
        this.unprocessedString = unprocessedString;
        this.consummedString = consummedString;
        this.fsm_transitions = new ArrayList<>();
        this.fsm_states = new ArrayList<>();
    }

    public fsm_StateMachine(
        String producedString,        String unprocessedString,        String consummedString        ArrayList<fsm_Transition> fsm_transitions,        ArrayList<fsm_State> fsm_states    ) {
        this.producedString = producedString;
        this.unprocessedString = unprocessedString;
        this.consummedString = consummedString;
        this.fsm_transitions = fsm_transitions;
        this.fsm_states = fsm_states;
    }

    public String getProducedstring() {
        return producedString;
    }

    public void setProducedstring(String producedString) {
        this.producedString = producedString;
    }
    public String getUnprocessedstring() {
        return unprocessedString;
    }

    public void setUnprocessedstring(String unprocessedString) {
        this.unprocessedString = unprocessedString;
    }
    public String getConsummedstring() {
        return consummedString;
    }

    public void setConsummedstring(String consummedString) {
        this.consummedString = consummedString;
    }

    public List<fsm_Transition> getFsm_transitions() {
        return fsm_transitions;
    }

    public void addFsm_transition(Fsm_transition fsm_transition) {
        this.fsm_transitions.add(fsm_transition);
    }
    public List<fsm_State> getFsm_states() {
        return fsm_states;
    }

    public void addFsm_state(Fsm_state fsm_state) {
        this.fsm_states.add(fsm_state);
    }
    public fsm_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(fsm_State fsm_state) {
        this.fsm_state = fsm_state;
    }
    public fsm_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(fsm_State fsm_state) {
        this.fsm_state = fsm_state;
    }
    public fsm_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(fsm_State fsm_state) {
        this.fsm_state = fsm_state;
    }

}
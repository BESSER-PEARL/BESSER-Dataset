





import java.util.List;
import java.util.ArrayList;

public class fsm_StateMachine extends NamedElement {

    private String unprocessedString;
    private String producedString;
    private String consummedString;





    private List<fsm_Transition> fsm_transitions;


    public fsm_StateMachine(
        String unprocessedString,        String producedString,        String consummedString    ) {
        super(
        );
        this.unprocessedString = unprocessedString;
        this.producedString = producedString;
        this.consummedString = consummedString;
        this.fsm_transitions = new ArrayList<>();
    }

    public fsm_StateMachine(
        String unprocessedString,        String producedString,        String consummedString        ArrayList<fsm_Transition> fsm_transitions    ) {
        this.unprocessedString = unprocessedString;
        this.producedString = producedString;
        this.consummedString = consummedString;
        this.fsm_transitions = fsm_transitions;
    }

    public String getUnprocessedstring() {
        return unprocessedString;
    }

    public void setUnprocessedstring(String unprocessedString) {
        this.unprocessedString = unprocessedString;
    }
    public String getProducedstring() {
        return producedString;
    }

    public void setProducedstring(String producedString) {
        this.producedString = producedString;
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

}
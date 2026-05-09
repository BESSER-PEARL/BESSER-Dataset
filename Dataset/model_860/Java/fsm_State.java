





import java.util.List;
import java.util.ArrayList;

public class fsm_State extends NamedElement {

    private int initialTime;
    private int finalTime;





    private fsm_StateMachine fsm_statemachine;




    private fsm_Transition fsm_transition;




    private fsm_Transition fsm_transition;




    private fsm_StateMachine fsm_statemachine;




    private List<fsm_Transition> fsm_transitions;




    private List<fsm_Transition> fsm_transitions;


    public fsm_State(
        int initialTime,        int finalTime    ) {
        super(
        );
        this.initialTime = initialTime;
        this.finalTime = finalTime;
        this.fsm_transitions = new ArrayList<>();
        this.fsm_transitions = new ArrayList<>();
    }

    public fsm_State(
        int initialTime,        int finalTime        ArrayList<fsm_Transition> fsm_transitions,        ArrayList<fsm_Transition> fsm_transitions    ) {
        this.initialTime = initialTime;
        this.finalTime = finalTime;
        this.fsm_transitions = fsm_transitions;
        this.fsm_transitions = fsm_transitions;
    }

    public int getInitialtime() {
        return initialTime;
    }

    public void setInitialtime(int initialTime) {
        this.initialTime = initialTime;
    }
    public int getFinaltime() {
        return finalTime;
    }

    public void setFinaltime(int finalTime) {
        this.finalTime = finalTime;
    }

    public fsm_StateMachine getFsm_statemachine() {
        return fsm_statemachine;
    }

    public void setFsm_statemachine(fsm_StateMachine fsm_statemachine) {
        this.fsm_statemachine = fsm_statemachine;
    }
    public fsm_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(fsm_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }
    public fsm_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(fsm_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }
    public fsm_StateMachine getFsm_statemachine() {
        return fsm_statemachine;
    }

    public void setFsm_statemachine(fsm_StateMachine fsm_statemachine) {
        this.fsm_statemachine = fsm_statemachine;
    }
    public List<fsm_Transition> getFsm_transitions() {
        return fsm_transitions;
    }

    public void addFsm_transition(Fsm_transition fsm_transition) {
        this.fsm_transitions.add(fsm_transition);
    }
    public List<fsm_Transition> getFsm_transitions() {
        return fsm_transitions;
    }

    public void addFsm_transition(Fsm_transition fsm_transition) {
        this.fsm_transitions.add(fsm_transition);
    }

}
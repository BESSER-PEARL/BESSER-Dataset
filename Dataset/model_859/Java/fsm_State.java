





import java.util.List;
import java.util.ArrayList;

public class fsm_State extends NamedElement {

    private int finalTime;
    private int initialTime;





    private fsm_StateMachine fsm_statemachine;




    private fsm_StateMachine fsm_statemachine;


    public fsm_State(
        int finalTime,        int initialTime    ) {
        super(
        );
        this.finalTime = finalTime;
        this.initialTime = initialTime;
    }


    public int getFinaltime() {
        return finalTime;
    }

    public void setFinaltime(int finalTime) {
        this.finalTime = finalTime;
    }
    public int getInitialtime() {
        return initialTime;
    }

    public void setInitialtime(int initialTime) {
        this.initialTime = initialTime;
    }

    public fsm_StateMachine getFsm_statemachine() {
        return fsm_statemachine;
    }

    public void setFsm_statemachine(fsm_StateMachine fsm_statemachine) {
        this.fsm_statemachine = fsm_statemachine;
    }
    public fsm_StateMachine getFsm_statemachine() {
        return fsm_statemachine;
    }

    public void setFsm_statemachine(fsm_StateMachine fsm_statemachine) {
        this.fsm_statemachine = fsm_statemachine;
    }

}






import java.util.List;
import java.util.ArrayList;

public class fsm_State  {

    private String name;
    private boolean isInitialState;





    private fsm_FiniteStateMachine fsm_finitestatemachine;




    private fsm_FiniteStateMachine fsm_finitestatemachine;


    public fsm_State(
        String name,        boolean isInitialState    ) {
        this.name = name;
        this.isInitialState = isInitialState;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsinitialstate() {
        return isInitialState;
    }

    public void setIsinitialstate(boolean isInitialState) {
        this.isInitialState = isInitialState;
    }

    public fsm_FiniteStateMachine getFsm_finitestatemachine() {
        return fsm_finitestatemachine;
    }

    public void setFsm_finitestatemachine(fsm_FiniteStateMachine fsm_finitestatemachine) {
        this.fsm_finitestatemachine = fsm_finitestatemachine;
    }
    public fsm_FiniteStateMachine getFsm_finitestatemachine() {
        return fsm_finitestatemachine;
    }

    public void setFsm_finitestatemachine(fsm_FiniteStateMachine fsm_finitestatemachine) {
        this.fsm_finitestatemachine = fsm_finitestatemachine;
    }

}
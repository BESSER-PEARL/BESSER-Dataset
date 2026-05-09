





import java.util.List;
import java.util.ArrayList;

public class FSM_AbstractState  {

    private String name;
    private String envs;





    private FSM_StateMachine fsm_statemachine;




    private FSM_StateMachine fsm_statemachine;


    public FSM_AbstractState(
        String name,        String envs    ) {
        this.name = name;
        this.envs = envs;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEnvs() {
        return envs;
    }

    public void setEnvs(String envs) {
        this.envs = envs;
    }

    public FSM_StateMachine getFsm_statemachine() {
        return fsm_statemachine;
    }

    public void setFsm_statemachine(FSM_StateMachine fsm_statemachine) {
        this.fsm_statemachine = fsm_statemachine;
    }
    public FSM_StateMachine getFsm_statemachine() {
        return fsm_statemachine;
    }

    public void setFsm_statemachine(FSM_StateMachine fsm_statemachine) {
        this.fsm_statemachine = fsm_statemachine;
    }

}
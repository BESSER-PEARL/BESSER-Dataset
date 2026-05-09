





import java.util.List;
import java.util.ArrayList;

public class FSM_StateMachine  {

    private String name;





    private List<FSM_State> fsm_states;




    private FSM_State fsm_state;


    public FSM_StateMachine(
        String name    ) {
        this.name = name;
        this.fsm_states = new ArrayList<>();
    }

    public FSM_StateMachine(
        String name        ArrayList<FSM_State> fsm_states    ) {
        this.name = name;
        this.fsm_states = fsm_states;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<FSM_State> getFsm_states() {
        return fsm_states;
    }

    public void addFsm_state(Fsm_state fsm_state) {
        this.fsm_states.add(fsm_state);
    }
    public FSM_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(FSM_State fsm_state) {
        this.fsm_state = fsm_state;
    }

}
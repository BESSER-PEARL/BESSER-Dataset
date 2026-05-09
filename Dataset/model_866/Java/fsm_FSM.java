





import java.util.List;
import java.util.ArrayList;

public class fsm_FSM  {






    private List<fsm_State> fsm_states;




    private fsm_InitialState fsm_initialstate;


    public fsm_FSM(
    ) {
        this.fsm_states = new ArrayList<>();
    }

    public fsm_FSM(
        ArrayList<fsm_State> fsm_states    ) {
        this.fsm_states = fsm_states;
    }


    public List<fsm_State> getFsm_states() {
        return fsm_states;
    }

    public void addFsm_state(Fsm_state fsm_state) {
        this.fsm_states.add(fsm_state);
    }
    public fsm_InitialState getFsm_initialstate() {
        return fsm_initialstate;
    }

    public void setFsm_initialstate(fsm_InitialState fsm_initialstate) {
        this.fsm_initialstate = fsm_initialstate;
    }

}
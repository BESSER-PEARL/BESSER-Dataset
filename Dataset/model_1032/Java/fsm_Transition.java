





import java.util.List;
import java.util.ArrayList;

public class fsm_Transition  {

    private String name;
    private String trigger;





    private List<fsm_State> fsm_states;




    private fsm_FSM fsm_fsm;


    public fsm_Transition(
        String name,        String trigger    ) {
        this.name = name;
        this.trigger = trigger;
        this.fsm_states = new ArrayList<>();
    }

    public fsm_Transition(
        String name,        String trigger        ArrayList<fsm_State> fsm_states    ) {
        this.name = name;
        this.trigger = trigger;
        this.fsm_states = fsm_states;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }

    public List<fsm_State> getFsm_states() {
        return fsm_states;
    }

    public void addFsm_state(Fsm_state fsm_state) {
        this.fsm_states.add(fsm_state);
    }
    public fsm_FSM getFsm_fsm() {
        return fsm_fsm;
    }

    public void setFsm_fsm(fsm_FSM fsm_fsm) {
        this.fsm_fsm = fsm_fsm;
    }

}
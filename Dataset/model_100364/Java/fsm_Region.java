





import java.util.List;
import java.util.ArrayList;

public class fsm_Region  {






    private List<fsm_State> fsm_states;




    private fsm_CompositeState fsm_compositestate;




    private fsm_CompositeState fsm_compositestate;


    public fsm_Region(
    ) {
        this.fsm_states = new ArrayList<>();
    }

    public fsm_Region(
        ArrayList<fsm_State> fsm_states    ) {
        this.fsm_states = fsm_states;
    }


    public List<fsm_State> getFsm_states() {
        return fsm_states;
    }

    public void addFsm_state(Fsm_state fsm_state) {
        this.fsm_states.add(fsm_state);
    }
    public fsm_CompositeState getFsm_compositestate() {
        return fsm_compositestate;
    }

    public void setFsm_compositestate(fsm_CompositeState fsm_compositestate) {
        this.fsm_compositestate = fsm_compositestate;
    }
    public fsm_CompositeState getFsm_compositestate() {
        return fsm_compositestate;
    }

    public void setFsm_compositestate(fsm_CompositeState fsm_compositestate) {
        this.fsm_compositestate = fsm_compositestate;
    }

}
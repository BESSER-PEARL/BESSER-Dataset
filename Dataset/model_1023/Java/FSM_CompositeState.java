





import java.util.List;
import java.util.ArrayList;

public class FSM_CompositeState extends AbstractState {






    private FSM_AbstractState fsm_abstractstate;




    private List<FSM_AbstractState> fsm_abstractstates;


    public FSM_CompositeState(
    ) {
        super(
        );
        this.fsm_abstractstates = new ArrayList<>();
    }

    public FSM_CompositeState(
        ArrayList<FSM_AbstractState> fsm_abstractstates    ) {
        this.fsm_abstractstates = fsm_abstractstates;
    }


    public FSM_AbstractState getFsm_abstractstate() {
        return fsm_abstractstate;
    }

    public void setFsm_abstractstate(FSM_AbstractState fsm_abstractstate) {
        this.fsm_abstractstate = fsm_abstractstate;
    }
    public List<FSM_AbstractState> getFsm_abstractstates() {
        return fsm_abstractstates;
    }

    public void addFsm_abstractstate(Fsm_abstractstate fsm_abstractstate) {
        this.fsm_abstractstates.add(fsm_abstractstate);
    }

}






import java.util.List;
import java.util.ArrayList;

public class fsm_CompositeState extends AbstractState {






    private List<fsm_AbstractState> fsm_abstractstates;




    private fsm_AbstractState fsm_abstractstate;


    public fsm_CompositeState(
    ) {
        super(
        );
        this.fsm_abstractstates = new ArrayList<>();
    }

    public fsm_CompositeState(
        ArrayList<fsm_AbstractState> fsm_abstractstates    ) {
        this.fsm_abstractstates = fsm_abstractstates;
    }


    public List<fsm_AbstractState> getFsm_abstractstates() {
        return fsm_abstractstates;
    }

    public void addFsm_abstractstate(Fsm_abstractstate fsm_abstractstate) {
        this.fsm_abstractstates.add(fsm_abstractstate);
    }
    public fsm_AbstractState getFsm_abstractstate() {
        return fsm_abstractstate;
    }

    public void setFsm_abstractstate(fsm_AbstractState fsm_abstractstate) {
        this.fsm_abstractstate = fsm_abstractstate;
    }

}
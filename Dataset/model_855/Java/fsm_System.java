





import java.util.List;
import java.util.ArrayList;

public class fsm_System  {






    private List<fsm_FSM> fsm_fsms;


    public fsm_System(
    ) {
        this.fsm_fsms = new ArrayList<>();
    }

    public fsm_System(
        ArrayList<fsm_FSM> fsm_fsms    ) {
        this.fsm_fsms = fsm_fsms;
    }


    public List<fsm_FSM> getFsm_fsms() {
        return fsm_fsms;
    }

    public void addFsm_fsm(Fsm_fsm fsm_fsm) {
        this.fsm_fsms.add(fsm_fsm);
    }

}
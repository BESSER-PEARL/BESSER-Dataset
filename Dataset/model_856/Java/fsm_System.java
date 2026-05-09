





import java.util.List;
import java.util.ArrayList;

public class fsm_System  {






    private List<fsm_FSM> fsm_fsms;




    private List<fsm_Buffer> fsm_buffers;


    public fsm_System(
    ) {
        this.fsm_fsms = new ArrayList<>();
        this.fsm_buffers = new ArrayList<>();
    }

    public fsm_System(
        ArrayList<fsm_FSM> fsm_fsms,        ArrayList<fsm_Buffer> fsm_buffers    ) {
        this.fsm_fsms = fsm_fsms;
        this.fsm_buffers = fsm_buffers;
    }


    public List<fsm_FSM> getFsm_fsms() {
        return fsm_fsms;
    }

    public void addFsm_fsm(Fsm_fsm fsm_fsm) {
        this.fsm_fsms.add(fsm_fsm);
    }
    public List<fsm_Buffer> getFsm_buffers() {
        return fsm_buffers;
    }

    public void addFsm_buffer(Fsm_buffer fsm_buffer) {
        this.fsm_buffers.add(fsm_buffer);
    }

}
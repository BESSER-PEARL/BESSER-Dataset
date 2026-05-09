





import java.util.List;
import java.util.ArrayList;

public class fsm_FSMSystem extends NamedElement {






    private List<fsm_Buffer> fsm_buffers;




    private List<fsm_StateMachine> fsm_statemachines;


    public fsm_FSMSystem(
    ) {
        super(
        );
        this.fsm_buffers = new ArrayList<>();
        this.fsm_statemachines = new ArrayList<>();
    }

    public fsm_FSMSystem(
        ArrayList<fsm_Buffer> fsm_buffers,        ArrayList<fsm_StateMachine> fsm_statemachines    ) {
        this.fsm_buffers = fsm_buffers;
        this.fsm_statemachines = fsm_statemachines;
    }


    public List<fsm_Buffer> getFsm_buffers() {
        return fsm_buffers;
    }

    public void addFsm_buffer(Fsm_buffer fsm_buffer) {
        this.fsm_buffers.add(fsm_buffer);
    }
    public List<fsm_StateMachine> getFsm_statemachines() {
        return fsm_statemachines;
    }

    public void addFsm_statemachine(Fsm_statemachine fsm_statemachine) {
        this.fsm_statemachines.add(fsm_statemachine);
    }

}
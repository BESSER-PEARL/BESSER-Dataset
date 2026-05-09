





import java.util.List;
import java.util.ArrayList;

public class fsm_Model extends NamedElement {






    private List<fsm_FiniteStateMachine> fsm_finitestatemachines;


    public fsm_Model(
    ) {
        super(
        );
        this.fsm_finitestatemachines = new ArrayList<>();
    }

    public fsm_Model(
        ArrayList<fsm_FiniteStateMachine> fsm_finitestatemachines    ) {
        this.fsm_finitestatemachines = fsm_finitestatemachines;
    }


    public List<fsm_FiniteStateMachine> getFsm_finitestatemachines() {
        return fsm_finitestatemachines;
    }

    public void addFsm_finitestatemachine(Fsm_finitestatemachine fsm_finitestatemachine) {
        this.fsm_finitestatemachines.add(fsm_finitestatemachine);
    }

}
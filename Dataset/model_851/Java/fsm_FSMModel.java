





import java.util.List;
import java.util.ArrayList;

public class fsm_FSMModel extends NamedElement {






    private List<fsm_StateMachine> fsm_statemachines;


    public fsm_FSMModel(
    ) {
        super(
        );
        this.fsm_statemachines = new ArrayList<>();
    }

    public fsm_FSMModel(
        ArrayList<fsm_StateMachine> fsm_statemachines    ) {
        this.fsm_statemachines = fsm_statemachines;
    }


    public List<fsm_StateMachine> getFsm_statemachines() {
        return fsm_statemachines;
    }

    public void addFsm_statemachine(Fsm_statemachine fsm_statemachine) {
        this.fsm_statemachines.add(fsm_statemachine);
    }

}
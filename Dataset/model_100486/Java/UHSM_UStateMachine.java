





import java.util.List;
import java.util.ArrayList;

public class UHSM_UStateMachine extends StateMachine {






    private List<UHSM_StateMachine> uhsm_statemachines;


    public UHSM_UStateMachine(
    ) {
        super(
        );
        this.uhsm_statemachines = new ArrayList<>();
    }

    public UHSM_UStateMachine(
        ArrayList<UHSM_StateMachine> uhsm_statemachines    ) {
        this.uhsm_statemachines = uhsm_statemachines;
    }


    public List<UHSM_StateMachine> getUhsm_statemachines() {
        return uhsm_statemachines;
    }

    public void addUhsm_statemachine(Uhsm_statemachine uhsm_statemachine) {
        this.uhsm_statemachines.add(uhsm_statemachine);
    }

}
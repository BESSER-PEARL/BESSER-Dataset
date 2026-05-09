





import java.util.List;
import java.util.ArrayList;

public class statemachine_State extends AbstractState {






    private List<statemachine_StateAction> statemachine_stateactions;


    public statemachine_State(
    ) {
        super(
        );
        this.statemachine_stateactions = new ArrayList<>();
    }

    public statemachine_State(
        ArrayList<statemachine_StateAction> statemachine_stateactions    ) {
        this.statemachine_stateactions = statemachine_stateactions;
    }


    public List<statemachine_StateAction> getStatemachine_stateactions() {
        return statemachine_stateactions;
    }

    public void addStatemachine_stateaction(Statemachine_stateaction statemachine_stateaction) {
        this.statemachine_stateactions.add(statemachine_stateaction);
    }

}
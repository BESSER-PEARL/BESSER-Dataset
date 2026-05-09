





import java.util.List;
import java.util.ArrayList;

public class pivot_StateMachine extends Behavior {






    private List<pivot_StateMachine> pivot_statemachines;


    public pivot_StateMachine(
    ) {
        super(
        );
        this.pivot_statemachines = new ArrayList<>();
    }

    public pivot_StateMachine(
        ArrayList<pivot_StateMachine> pivot_statemachines    ) {
        this.pivot_statemachines = pivot_statemachines;
    }


    public List<pivot_StateMachine> getPivot_statemachines() {
        return pivot_statemachines;
    }

    public void addPivot_statemachine(Pivot_statemachine pivot_statemachine) {
        this.pivot_statemachines.add(pivot_statemachine);
    }

}
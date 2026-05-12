





import java.util.List;
import java.util.ArrayList;

public class StateMachine_StateMachineBehavioralModel  {






    private List<StateMachine_StateMachine> statemachine_statemachines;


    public StateMachine_StateMachineBehavioralModel(
    ) {
        this.statemachine_statemachines = new ArrayList<>();
    }

    public StateMachine_StateMachineBehavioralModel(
        ArrayList<StateMachine_StateMachine> statemachine_statemachines    ) {
        this.statemachine_statemachines = statemachine_statemachines;
    }


    public List<StateMachine_StateMachine> getStatemachine_statemachines() {
        return statemachine_statemachines;
    }

    public void addStatemachine_statemachine(Statemachine_statemachine statemachine_statemachine) {
        this.statemachine_statemachines.add(statemachine_statemachine);
    }

}
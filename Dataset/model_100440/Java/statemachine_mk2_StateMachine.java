





import java.util.List;
import java.util.ArrayList;

public class statemachine_mk2_StateMachine  {






    private List<statemachine_mk2_SimpleState> statemachine_mk2_simplestates;


    public statemachine_mk2_StateMachine(
    ) {
        this.statemachine_mk2_simplestates = new ArrayList<>();
    }

    public statemachine_mk2_StateMachine(
        ArrayList<statemachine_mk2_SimpleState> statemachine_mk2_simplestates    ) {
        this.statemachine_mk2_simplestates = statemachine_mk2_simplestates;
    }


    public List<statemachine_mk2_SimpleState> getStatemachine_mk2_simplestates() {
        return statemachine_mk2_simplestates;
    }

    public void addStatemachine_mk2_simplestate(Statemachine_mk2_simplestate statemachine_mk2_simplestate) {
        this.statemachine_mk2_simplestates.add(statemachine_mk2_simplestate);
    }

}
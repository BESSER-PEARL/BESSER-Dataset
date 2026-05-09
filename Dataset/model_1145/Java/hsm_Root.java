





import java.util.List;
import java.util.ArrayList;

public class hsm_Root  {






    private List<hsm_StateMachine> hsm_statemachines;


    public hsm_Root(
    ) {
        this.hsm_statemachines = new ArrayList<>();
    }

    public hsm_Root(
        ArrayList<hsm_StateMachine> hsm_statemachines    ) {
        this.hsm_statemachines = hsm_statemachines;
    }


    public List<hsm_StateMachine> getHsm_statemachines() {
        return hsm_statemachines;
    }

    public void addHsm_statemachine(Hsm_statemachine hsm_statemachine) {
        this.hsm_statemachines.add(hsm_statemachine);
    }

}
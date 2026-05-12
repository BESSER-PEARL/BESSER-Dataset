





import java.util.List;
import java.util.ArrayList;

public class statemachines_StatemachineOwner  {






    private List<statemachines_Statemachine> statemachines_statemachines;


    public statemachines_StatemachineOwner(
    ) {
        this.statemachines_statemachines = new ArrayList<>();
    }

    public statemachines_StatemachineOwner(
        ArrayList<statemachines_Statemachine> statemachines_statemachines    ) {
        this.statemachines_statemachines = statemachines_statemachines;
    }


    public List<statemachines_Statemachine> getStatemachines_statemachines() {
        return statemachines_statemachines;
    }

    public void addStatemachines_statemachine(Statemachines_statemachine statemachines_statemachine) {
        this.statemachines_statemachines.add(statemachines_statemachine);
    }

}






import java.util.List;
import java.util.ArrayList;

public class statemachines_CustomSystem  {






    private List<statemachines_CustomEvent> statemachines_customevents;




    private StateMachine statemachine;


    public statemachines_CustomSystem(
    ) {
        this.statemachines_customevents = new ArrayList<>();
    }

    public statemachines_CustomSystem(
        ArrayList<statemachines_CustomEvent> statemachines_customevents    ) {
        this.statemachines_customevents = statemachines_customevents;
    }


    public List<statemachines_CustomEvent> getStatemachines_customevents() {
        return statemachines_customevents;
    }

    public void addStatemachines_customevent(Statemachines_customevent statemachines_customevent) {
        this.statemachines_customevents.add(statemachines_customevent);
    }
    public StateMachine getStatemachine() {
        return statemachine;
    }

    public void setStatemachine(StateMachine statemachine) {
        this.statemachine = statemachine;
    }

}
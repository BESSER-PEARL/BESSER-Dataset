





import java.util.List;
import java.util.ArrayList;

public class statemachines_Behavior extends NamedElement {






    private List<statemachines_SignalEventOccurrence> statemachines_signaleventoccurrences;




    private statemachines_Transition statemachines_transition;


    public statemachines_Behavior(
    ) {
        super(
        );
        this.statemachines_signaleventoccurrences = new ArrayList<>();
    }

    public statemachines_Behavior(
        ArrayList<statemachines_SignalEventOccurrence> statemachines_signaleventoccurrences    ) {
        this.statemachines_signaleventoccurrences = statemachines_signaleventoccurrences;
    }


    public List<statemachines_SignalEventOccurrence> getStatemachines_signaleventoccurrences() {
        return statemachines_signaleventoccurrences;
    }

    public void addStatemachines_signaleventoccurrence(Statemachines_signaleventoccurrence statemachines_signaleventoccurrence) {
        this.statemachines_signaleventoccurrences.add(statemachines_signaleventoccurrence);
    }
    public statemachines_Transition getStatemachines_transition() {
        return statemachines_transition;
    }

    public void setStatemachines_transition(statemachines_Transition statemachines_transition) {
        this.statemachines_transition = statemachines_transition;
    }

}
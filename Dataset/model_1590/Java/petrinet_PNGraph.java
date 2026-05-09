





import java.util.List;
import java.util.ArrayList;

public class petrinet_PNGraph  {






    private List<petrinet_Transition> petrinet_transitions;


    public petrinet_PNGraph(
    ) {
        this.petrinet_transitions = new ArrayList<>();
    }

    public petrinet_PNGraph(
        ArrayList<petrinet_Transition> petrinet_transitions    ) {
        this.petrinet_transitions = petrinet_transitions;
    }


    public List<petrinet_Transition> getPetrinet_transitions() {
        return petrinet_transitions;
    }

    public void addPetrinet_transition(Petrinet_transition petrinet_transition) {
        this.petrinet_transitions.add(petrinet_transition);
    }

}
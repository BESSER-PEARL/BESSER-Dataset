





import java.util.List;
import java.util.ArrayList;

public class petrinet_PetriNet  {

    private String name;





    private List<petrinet_Transition> petrinet_transitions;




    private petrinet_Transition petrinet_transition;


    public petrinet_PetriNet(
        String name    ) {
        this.name = name;
        this.petrinet_transitions = new ArrayList<>();
    }

    public petrinet_PetriNet(
        String name        ArrayList<petrinet_Transition> petrinet_transitions    ) {
        this.name = name;
        this.petrinet_transitions = petrinet_transitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<petrinet_Transition> getPetrinet_transitions() {
        return petrinet_transitions;
    }

    public void addPetrinet_transition(Petrinet_transition petrinet_transition) {
        this.petrinet_transitions.add(petrinet_transition);
    }
    public petrinet_Transition getPetrinet_transition() {
        return petrinet_transition;
    }

    public void setPetrinet_transition(petrinet_Transition petrinet_transition) {
        this.petrinet_transition = petrinet_transition;
    }

}






import java.util.List;
import java.util.ArrayList;

public class PetriNet_Place extends NamedElement {






    private List<PetriNet_Transition> petrinet_transitions;




    private List<PetriNet_Transition> petrinet_transitions;




    private PetriNet_Transition petrinet_transition;




    private PetriNet_Transition petrinet_transition;


    public PetriNet_Place(
    ) {
        super(
        );
        this.petrinet_transitions = new ArrayList<>();
        this.petrinet_transitions = new ArrayList<>();
    }

    public PetriNet_Place(
        ArrayList<PetriNet_Transition> petrinet_transitions,        ArrayList<PetriNet_Transition> petrinet_transitions    ) {
        this.petrinet_transitions = petrinet_transitions;
        this.petrinet_transitions = petrinet_transitions;
    }


    public List<PetriNet_Transition> getPetrinet_transitions() {
        return petrinet_transitions;
    }

    public void addPetrinet_transition(Petrinet_transition petrinet_transition) {
        this.petrinet_transitions.add(petrinet_transition);
    }
    public List<PetriNet_Transition> getPetrinet_transitions() {
        return petrinet_transitions;
    }

    public void addPetrinet_transition(Petrinet_transition petrinet_transition) {
        this.petrinet_transitions.add(petrinet_transition);
    }
    public PetriNet_Transition getPetrinet_transition() {
        return petrinet_transition;
    }

    public void setPetrinet_transition(PetriNet_Transition petrinet_transition) {
        this.petrinet_transition = petrinet_transition;
    }
    public PetriNet_Transition getPetrinet_transition() {
        return petrinet_transition;
    }

    public void setPetrinet_transition(PetriNet_Transition petrinet_transition) {
        this.petrinet_transition = petrinet_transition;
    }

}
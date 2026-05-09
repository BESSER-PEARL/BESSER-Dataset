





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Net  {






    private PetriNet_TPArc petrinet_tparc;




    private List<PetriNet_TPArc> petrinet_tparcs;




    private PetriNet_Place petrinet_place;




    private List<PetriNet_Place> petrinet_places;




    private List<PetriNet_Transition> petrinet_transitions;




    private PetriNet_Transition petrinet_transition;


    public PetriNet_Net(
    ) {
        this.petrinet_tparcs = new ArrayList<>();
        this.petrinet_places = new ArrayList<>();
        this.petrinet_transitions = new ArrayList<>();
    }

    public PetriNet_Net(
        ArrayList<PetriNet_TPArc> petrinet_tparcs,        ArrayList<PetriNet_Place> petrinet_places,        ArrayList<PetriNet_Transition> petrinet_transitions    ) {
        this.petrinet_tparcs = petrinet_tparcs;
        this.petrinet_places = petrinet_places;
        this.petrinet_transitions = petrinet_transitions;
    }


    public PetriNet_TPArc getPetrinet_tparc() {
        return petrinet_tparc;
    }

    public void setPetrinet_tparc(PetriNet_TPArc petrinet_tparc) {
        this.petrinet_tparc = petrinet_tparc;
    }
    public List<PetriNet_TPArc> getPetrinet_tparcs() {
        return petrinet_tparcs;
    }

    public void addPetrinet_tparc(Petrinet_tparc petrinet_tparc) {
        this.petrinet_tparcs.add(petrinet_tparc);
    }
    public PetriNet_Place getPetrinet_place() {
        return petrinet_place;
    }

    public void setPetrinet_place(PetriNet_Place petrinet_place) {
        this.petrinet_place = petrinet_place;
    }
    public List<PetriNet_Place> getPetrinet_places() {
        return petrinet_places;
    }

    public void addPetrinet_place(Petrinet_place petrinet_place) {
        this.petrinet_places.add(petrinet_place);
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

}
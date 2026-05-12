





import java.util.List;
import java.util.ArrayList;

public class standardPetriNets_PetriNet  {

    private String name;





    private List<standardPetriNets_Place> standardpetrinets_places;




    private List<standardPetriNets_Transition> standardpetrinets_transitions;




    private List<standardPetriNets_OutputArc> standardpetrinets_outputarcs;


    public standardPetriNets_PetriNet(
        String name    ) {
        this.name = name;
        this.standardpetrinets_places = new ArrayList<>();
        this.standardpetrinets_transitions = new ArrayList<>();
        this.standardpetrinets_outputarcs = new ArrayList<>();
    }

    public standardPetriNets_PetriNet(
        String name        ArrayList<standardPetriNets_Place> standardpetrinets_places,        ArrayList<standardPetriNets_Transition> standardpetrinets_transitions,        ArrayList<standardPetriNets_OutputArc> standardpetrinets_outputarcs    ) {
        this.name = name;
        this.standardpetrinets_places = standardpetrinets_places;
        this.standardpetrinets_transitions = standardpetrinets_transitions;
        this.standardpetrinets_outputarcs = standardpetrinets_outputarcs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<standardPetriNets_Place> getStandardpetrinets_places() {
        return standardpetrinets_places;
    }

    public void addStandardpetrinets_place(Standardpetrinets_place standardpetrinets_place) {
        this.standardpetrinets_places.add(standardpetrinets_place);
    }
    public List<standardPetriNets_Transition> getStandardpetrinets_transitions() {
        return standardpetrinets_transitions;
    }

    public void addStandardpetrinets_transition(Standardpetrinets_transition standardpetrinets_transition) {
        this.standardpetrinets_transitions.add(standardpetrinets_transition);
    }
    public List<standardPetriNets_OutputArc> getStandardpetrinets_outputarcs() {
        return standardpetrinets_outputarcs;
    }

    public void addStandardpetrinets_outputarc(Standardpetrinets_outputarc standardpetrinets_outputarc) {
        this.standardpetrinets_outputarcs.add(standardpetrinets_outputarc);
    }

}
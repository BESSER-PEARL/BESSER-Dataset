





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Net extends Identifiable {






    private List<PetriNet_OutputArc> petrinet_outputarcs;




    private List<PetriNet_Token> petrinet_tokens;




    private List<PetriNet_Place> petrinet_places;




    private List<PetriNet_InputArc> petrinet_inputarcs;


    public PetriNet_Net(
    ) {
        super(
        );
        this.petrinet_outputarcs = new ArrayList<>();
        this.petrinet_tokens = new ArrayList<>();
        this.petrinet_places = new ArrayList<>();
        this.petrinet_inputarcs = new ArrayList<>();
    }

    public PetriNet_Net(
        ArrayList<PetriNet_OutputArc> petrinet_outputarcs,        ArrayList<PetriNet_Token> petrinet_tokens,        ArrayList<PetriNet_Place> petrinet_places,        ArrayList<PetriNet_InputArc> petrinet_inputarcs    ) {
        this.petrinet_outputarcs = petrinet_outputarcs;
        this.petrinet_tokens = petrinet_tokens;
        this.petrinet_places = petrinet_places;
        this.petrinet_inputarcs = petrinet_inputarcs;
    }


    public List<PetriNet_OutputArc> getPetrinet_outputarcs() {
        return petrinet_outputarcs;
    }

    public void addPetrinet_outputarc(Petrinet_outputarc petrinet_outputarc) {
        this.petrinet_outputarcs.add(petrinet_outputarc);
    }
    public List<PetriNet_Token> getPetrinet_tokens() {
        return petrinet_tokens;
    }

    public void addPetrinet_token(Petrinet_token petrinet_token) {
        this.petrinet_tokens.add(petrinet_token);
    }
    public List<PetriNet_Place> getPetrinet_places() {
        return petrinet_places;
    }

    public void addPetrinet_place(Petrinet_place petrinet_place) {
        this.petrinet_places.add(petrinet_place);
    }
    public List<PetriNet_InputArc> getPetrinet_inputarcs() {
        return petrinet_inputarcs;
    }

    public void addPetrinet_inputarc(Petrinet_inputarc petrinet_inputarc) {
        this.petrinet_inputarcs.add(petrinet_inputarc);
    }

}